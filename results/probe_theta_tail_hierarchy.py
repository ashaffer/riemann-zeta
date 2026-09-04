"""Numerical scout for the exact full-theta tail hierarchy.

This is deliberately a *falsification* probe, not an interval proof.  With

    h_T(p) = int_R Phi((p+q)/2) Phi((p-q)/2) cos(T q) dq,
    S_1(P) = int_P^infinity h_T(p) dp,
    S_k(P) = int_P^infinity S_{k-1}(x) dx,

it evaluates h on a tensor grid and obtains the higher tails by repeated
backward integration.  A reported negative value is a candidate which must
then be checked by arbitrary-precision or interval quadrature.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import math

import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss
from scipy.integrate import cumulative_trapezoid


def phi(x: np.ndarray) -> np.ndarray:
    """Rodgers--Tao theta kernel, stabilized with Phi(-u)=Phi(u)."""
    x = np.abs(np.asarray(x, dtype=float))
    e4 = np.exp(4.0 * x)
    ans = np.zeros_like(x)
    # On x>=0 the series is extremely rapidly convergent.
    for n in range(1, 16):
        ans += (
            2.0 * np.pi**2 * n**4 * np.exp(9.0 * x)
            - 3.0 * np.pi * n**2 * np.exp(5.0 * x)
        ) * np.exp(-np.pi * n * n * e4)
    return ans


def backward_integral(values: np.ndarray, grid: np.ndarray) -> np.ndarray:
    """Return int_grid[i]^grid[-1] values(x) dx along axis zero."""
    return -cumulative_trapezoid(
        values[::-1], grid[::-1], axis=0, initial=0.0
    )[::-1]


def scout(
    p_max: float,
    p_count: int,
    q_max: float,
    q_count: int,
    t_max: float,
    t_step: float,
    max_k: int,
) -> None:
    p = np.linspace(0.0, p_max, p_count)
    q0, qw0 = leggauss(q_count)
    q = q_max * q0
    qw = q_max * qw0

    base = phi((p[:, None] + q[None, :]) / 2.0)
    base *= phi((p[:, None] - q[None, :]) / 2.0)
    base *= qw[None, :]

    t = np.arange(0.0, t_max + 0.5 * t_step, t_step)
    h = base @ np.cos(q[:, None] * t[None, :])

    tails = h
    print("grid", p_count, q_count, len(t), "p_max", p_max, "q_max", q_max)
    for k in range(1, max_k + 1):
        tails = backward_integral(tails, p)
        flat = int(np.argmin(tails))
        ip, it = np.unravel_index(flat, tails.shape)
        print(
            f"S_{k}: min={tails[ip, it]:+.17e} "
            f"at P={p[ip]:.9g}, T={t[it]:.9g}; "
            f"S_{k}(0) min={np.min(tails[0]):+.17e}"
        )


def mp_xi(s: mp.mpc) -> mp.mpc:
    """Entire Riemann xi in the normalization used by the theta kernel."""
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def critical_transform(t: mp.mpf) -> mp.mpf:
    """f(t)=int Phi(u) exp(-i t u)du=xi((1-i t)/2)/4."""
    return mp.re(mp_xi((1 - 1j * t) / 2) / 4)


def constant_cosine_tail(p: mp.mpf, cutoff: mp.mpf) -> mp.mpf:
    """int_cutoff^infinity cos(p*w)/w^2 dw (p>=0)."""
    if p == 0:
        return 1 / cutoff
    return mp.cos(p * cutoff) / cutoff - p * (
        mp.pi / 2 - mp.si(p * cutoff)
    )


def constant_sine_cubic_tail(p: mp.mpf, cutoff: mp.mpf) -> mp.mpf:
    """int_cutoff^infinity sin(p*w)/w^3 dw (p>=0)."""
    if p == 0:
        return mp.mpf("0")
    return (
        mp.sin(p * cutoff) / (2 * cutoff**2)
        + p * mp.cos(p * cutoff) / (2 * cutoff)
        - p**2 * (mp.pi / 2 - mp.si(p * cutoff)) / 2
    )


def verify_s2_fourier(t0: float, p0: float, cutoff: float, dps: int) -> None:
    """Arbitrary-precision check of the exact Turan/cosine formula for S_2.

    The product tail beyond ``cutoff`` is omitted; the constant f(t)^2 tail
    is integrated analytically.  Increase both cutoff and dps to test
    stability.  This remains a high-precision probe, not interval arithmetic.
    """
    mp.mp.dps = dps
    t = mp.mpf(t0)
    p = mp.mpf(p0)
    w_max = mp.mpf(cutoff)
    ft = critical_transform(t)
    fp = mp.diff(critical_transform, t)
    fpp = mp.diff(critical_transform, t, 2)
    laguerre = fp * fp - ft * fpp

    def integrand(w: mp.mpf) -> mp.mpf:
        if abs(w) < mp.mpf(10) ** (-(dps // 3)):
            return laguerre
        turan = ft * ft - critical_transform(t + w) * critical_transform(t - w)
        return mp.cos(p * w) * turan / (w * w)

    # Unit panels keep the zeta evaluations and oscillation under control.
    mesh = [mp.mpf(j) for j in range(int(mp.floor(w_max)) + 1)]
    if mesh[-1] != w_max:
        mesh.append(w_max)
    main = mp.fsum(mp.quad(integrand, [a, b]) for a, b in zip(mesh, mesh[1:]))
    main += ft * ft * constant_cosine_tail(p, w_max)
    value = 2 * main / mp.pi
    edge_product = critical_transform(t + w_max) * critical_transform(t - w_max)
    print(
        "mp S_2",
        "T=", mp.nstr(t, 12),
        "P=", mp.nstr(p, 12),
        "value=", mp.nstr(value, min(50, dps - 5)),
    )
    print("Laguerre coefficient=", mp.nstr(laguerre, min(30, dps - 5)))
    print("product at cutoff=", mp.nstr(edge_product, 12))


def verify_s3_fourier(t0: float, p0: float, cutoff: float, dps: int) -> None:
    """Arbitrary-precision check of S_3 from the integrated Turan formula."""
    mp.mp.dps = dps
    t = mp.mpf(t0)
    p = mp.mpf(p0)
    w_max = mp.mpf(cutoff)
    ft = critical_transform(t)
    fp = mp.diff(critical_transform, t)
    fpp = mp.diff(critical_transform, t, 2)
    laguerre = fp * fp - ft * fpp

    def integrand(w: mp.mpf) -> mp.mpf:
        if abs(w) < mp.mpf(10) ** (-(dps // 3)):
            return laguerre * p
        turan = ft * ft - critical_transform(t + w) * critical_transform(t - w)
        return turan * mp.sin(p * w) / w**3

    mesh = [mp.mpf(j) for j in range(int(mp.floor(w_max)) + 1)]
    if mesh[-1] != w_max:
        mesh.append(w_max)
    correction = mp.fsum(
        mp.quad(integrand, [a, b]) for a, b in zip(mesh, mesh[1:])
    )
    correction += ft * ft * constant_sine_cubic_tail(p, w_max)
    value = laguerre - 2 * correction / mp.pi
    edge_product = critical_transform(t + w_max) * critical_transform(t - w_max)
    print(
        "mp S_3",
        "T=", mp.nstr(t, 12),
        "P=", mp.nstr(p, 12),
        "value=", mp.nstr(value, min(50, dps - 5)),
    )
    print("S_3(T,0)=Laguerre coefficient=", mp.nstr(laguerre, min(30, dps - 5)))
    print("product at cutoff=", mp.nstr(edge_product, 12))


def atomic_lp_test(scales: list[float], max_k: int) -> None:
    """Exact finite test family with positive inverse and LP transform.

    The measure is the convolution of symmetric atoms at ``+-scales[j]``;
    its Fourier transform is ``prod_j cos(scales[j] t)``, hence belongs to
    Laguerre--Polya.  This tests whether those generic properties force any
    of the tail signs (they do not force S_2).
    """
    atoms: dict[float, float] = {0.0: 1.0}
    for scale in scales:
        nxt: defaultdict[float, float] = defaultdict(float)
        for x, mass in atoms.items():
            nxt[x + scale] += mass / 2.0
            nxt[x - scale] += mass / 2.0
        atoms = dict(nxt)
    support = np.array(sorted(atoms))
    mass = np.array([atoms[x] for x in support])
    u = support[:, None]
    v = support[None, :]
    weights = mass[:, None] * mass[None, :]
    p_values = np.linspace(0.0, max(0.0, 2.0 * np.max(support)), 801)
    t_values = np.linspace(0.0, 4.0 * np.pi, 801)
    best = [(float("inf"), 0.0, 0.0) for _ in range(max_k + 1)]
    diff = (u - v).ravel()
    summ = (u + v).ravel()
    pair_weight = (2.0 * weights).ravel()
    phases = pair_weight[:, None] * np.cos(diff[:, None] * t_values[None, :])
    positive = np.maximum(summ[:, None] - p_values[None, :], 0.0)
    for k in range(2, max_k + 1):
        values = (positive ** (k - 1)).T @ phases / math.factorial(k - 1)
        flat = int(np.argmin(values))
        ip, it = np.unravel_index(flat, values.shape)
        best[k] = (float(values[ip, it]), float(p_values[ip]), float(t_values[it]))
    print("atomic LP scales", scales, "support", support.tolist())
    for k in range(2, max_k + 1):
        value, p, t = best[k]
        print(f"S_{k}: min={value:+.12e} at P={p:.9g}, T={t:.9g}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-max", type=float, default=3.0)
    parser.add_argument("--p-count", type=int, default=1201)
    parser.add_argument("--q-max", type=float, default=3.0)
    parser.add_argument("--q-count", type=int, default=800)
    parser.add_argument("--t-max", type=float, default=60.0)
    parser.add_argument("--t-step", type=float, default=0.1)
    parser.add_argument("--max-k", type=int, default=6)
    parser.add_argument(
        "--verify-s2", nargs=2, type=float, metavar=("T", "P"),
        help="verify S_2(T,P) from its exact Fourier/Turan representation",
    )
    parser.add_argument(
        "--verify-s3", nargs=2, type=float, metavar=("T", "P"),
        help="verify S_3(T,P) from its integrated Fourier/Turan representation",
    )
    parser.add_argument("--cutoff", type=float, default=100.0)
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument(
        "--atomic-scales", nargs="+", type=float,
        help="test the positive atomic LP family prod cos(scale*t)",
    )
    args = parser.parse_args()
    if args.atomic_scales:
        atomic_lp_test(args.atomic_scales, args.max_k)
    elif args.verify_s3:
        verify_s3_fourier(
            args.verify_s3[0], args.verify_s3[1], args.cutoff, args.dps
        )
    elif args.verify_s2:
        verify_s2_fourier(
            args.verify_s2[0], args.verify_s2[1], args.cutoff, args.dps
        )
    else:
        scout(
            args.p_max,
            args.p_count,
            args.q_max,
            args.q_count,
            args.t_max,
            args.t_step,
            args.max_k,
        )
