#!/usr/bin/env python3
"""Old-ground-sector test of event-specific cross cancellation.

Unlike event_cross_ratio.py, the old vectors here are generalized lowest
eigenvectors of the high-precision x-kernel Weil matrix.  Their cross coupling
to two collar hat spaces is evaluated componentwise as pole + archimedean -
prime.  This is an arithmetic-side diagnostic and uses no zeta zeros or RH.
"""
from __future__ import annotations

import argparse
import csv
import math
import pathlib
import sys

import mpmath as mp
import numpy as np
import scipy.linalg
from scipy.special import digamma
from sympy import primerange

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from hp_margins import hp_form
from weil_core import hatFT


def prime_powers(limit: int) -> list[tuple[int, int]]:
    out: dict[int, int] = {}
    for p in primerange(2, limit + 1):
        q = p
        while q <= limit:
            out[q] = p
            if q > limit // p:
                break
            q *= p
    return sorted(out.items())


def old_modes(a: float, m: int, count: int, dps: int):
    Qmp, Gmp = hp_form(4 * a, m, dps=dps)
    Q = np.array(Qmp.tolist(), float)
    G = np.array(Gmp.tolist(), float)
    eigenvalues, vectors = scipy.linalg.eigh(Q, G, subset_by_index=[0, count - 1])
    d = 2 * a / (m + 1)
    centers = np.linspace(-a + d, a - d, m)
    return eigenvalues, vectors, centers, d


def collar_hats(a: float, b: float, degree: int):
    d = (b - a) / (degree + 1)
    right = np.linspace(a + d, b - d, degree)
    return np.concatenate((-right[::-1], right)), d


def pole_vector(centers: np.ndarray, d: float, sign: float) -> np.ndarray:
    s = sign / 2
    factor = (2 * np.cosh(s * d) - 2) / (s * s * d)
    return np.exp(s * centers) * factor


def simpson_grid(rmax: float, intervals: int):
    if intervals % 2:
        intervals += 1
    r = np.linspace(0, rmax, intervals + 1)
    h = rmax / intervals
    w = np.ones(intervals + 1)
    w[1:-1:2] = 4
    w[2:-1:2] = 2
    return r, w * h / 3


def component_blocks(a, b, active, old_vectors, old_centers, old_d,
                     collar_centers, collar_d, rmax, intervals, chunk):
    r, wr = simpson_grid(rmax, intervals)
    ko = old_vectors.shape[1]
    kc = len(collar_centers)
    arch_cross = np.zeros((ko, kc))
    prime_cross = np.zeros((ko, kc))
    arch_collar = np.zeros((kc, kc))
    prime_collar = np.zeros((kc, kc))
    for start in range(0, len(r), chunk):
        rr = r[start:start + chunk]
        ww = wr[start:start + chunk]
        Fo = hatFT(rr, old_centers, old_d) @ old_vectors
        Fc = hatFT(rr, collar_centers, collar_d)
        arch_symbol = np.real(digamma(.25 + .5j * rr)) - math.log(math.pi)
        prime_symbol = np.zeros_like(rr)
        for n, p in active:
            prime_symbol += 2 * math.log(p) / math.sqrt(n) * np.cos(math.log(n) * rr)
        arch_cross += np.real(Fo.conj().T @ ((ww * arch_symbol)[:, None] * Fc)) / math.pi
        prime_cross += np.real(Fo.conj().T @ ((ww * prime_symbol)[:, None] * Fc)) / math.pi
        arch_collar += np.real(Fc.conj().T @ ((ww * arch_symbol)[:, None] * Fc)) / math.pi
        prime_collar += np.real(Fc.conj().T @ ((ww * prime_symbol)[:, None] * Fc)) / math.pi

    op = pole_vector(old_centers, old_d, 1) @ old_vectors
    om = pole_vector(old_centers, old_d, -1) @ old_vectors
    cp = pole_vector(collar_centers, collar_d, 1)
    cm = pole_vector(collar_centers, collar_d, -1)
    pole_cross = np.outer(op, cm) + np.outer(om, cp)
    pole_collar = np.outer(cp, cm) + np.outer(cm, cp)
    total_cross = pole_cross + arch_cross - prime_cross
    total_collar = pole_collar + arch_collar - prime_collar
    return pole_cross, arch_cross, prime_cross, total_cross, total_collar


def dual_norm(row: np.ndarray, D: np.ndarray) -> float:
    return math.sqrt(max(0., float(row @ scipy.linalg.solve(D, row,
                                                            assume_a="pos"))))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--start", type=float, default=7 / 16)
    p.add_argument("--stop", type=float, default=1.25)
    p.add_argument("--events", type=int, default=10)
    p.add_argument("--old-size", type=int, default=61)
    p.add_argument("--low-modes", type=int, default=4)
    p.add_argument("--collar-degree", type=int, default=6)
    p.add_argument("--dps", type=int, default=40)
    p.add_argument("--rmax", type=float, default=1200)
    p.add_argument("--intervals", type=int, default=120000)
    p.add_argument("--chunk", type=int, default=2000)
    p.add_argument("--output", type=pathlib.Path,
                   default=pathlib.Path("results/low-energy-cross-cancellation.csv"))
    p.add_argument("--witness", type=pathlib.Path)
    args = p.parse_args()

    powers = prime_powers(math.ceil(math.exp(2 * args.stop)) + 2)
    thresholds = [math.log(n) / 2 for n, _ in powers
                  if args.start < math.log(n) / 2 <= args.stop][:args.events]
    rows = []
    a = args.start
    for event_index, b in enumerate(thresholds):
        ev, vec, oc, od = old_modes(a, args.old_size, args.low_modes, args.dps)
        cc, cd = collar_hats(a, b, args.collar_degree)
        active = [(n, prime) for n, prime in powers if math.log(n) <= 2*b + 1e-12]
        P, H, N, C, D = component_blocks(a, b, active, vec, oc, od, cc, cd,
                                         args.rmax, args.intervals, args.chunk)
        de = np.linalg.eigvalsh((D + D.T) / 2)
        if de[0] <= 0:
            print(f"event {event_index}: unresolved collar block min={de[0]:.3e}")
            a = b
            continue
        de, du = np.linalg.eigh((D + D.T) / 2)
        dinvhalf = (du / np.sqrt(de)[None, :]) @ du.T
        normalized_low_block = (C / np.sqrt(ev)[:, None]) @ dinvhalf
        su, ss, svh = np.linalg.svd(normalized_low_block, full_matrices=False)
        low_sector_ratio = float(ss[0])
        old_low_coeff = su[:, 0] / np.sqrt(ev)
        collar_coeff = dinvhalf @ svh[0]
        signed = [float(old_low_coeff @ X @ collar_coeff) for X in (P, H, N, C)]
        for j, lam in enumerate(ev):
            pn, hn, nn, cn = (dual_norm(X[j], D) for X in (P, H, N, C))
            rows.append(dict(event=event_index, a=a, b=b, width=b-a, mode=j,
                             old_eigenvalue=lam, collar_min=de[0],
                             pole_dual=pn, arch_dual=hn, prime_dual=nn,
                             total_dual=cn, normalized_ratio=cn/math.sqrt(lam),
                             cancellation=cn/(pn+hn+nn) if pn+hn+nn else 0.,
                             low_sector_ratio=low_sector_ratio))
        print(f"event={event_index} a={a:.6g} b={b:.6g} "
              f"lambda0={ev[0]:.3e} ratio0={rows[-args.low_modes]['normalized_ratio']:.3g} "
              f"cancel0={rows[-args.low_modes]['cancellation']:.3g} "
              f"sector_ratio={low_sector_ratio:.3g} "
              f"signed(P,H,N,total)=({signed[0]:.6g},{signed[1]:.6g},"
              f"{signed[2]:.6g},{signed[3]:.6g})")
        if args.witness is not None:
            args.witness.parent.mkdir(parents=True, exist_ok=True)
            np.savez(args.witness, a=a, b=b, eigenvalues=ev,
                     old_hat_coefficients=vec @ old_low_coeff,
                     collar_hat_coefficients=collar_coeff,
                     old_centers=oc, old_half_width=od,
                     collar_centers=cc, collar_half_width=cd,
                     singular_values=ss, signed_components=np.asarray(signed))
        a = b

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
