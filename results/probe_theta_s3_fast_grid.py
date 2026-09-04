"""Fast nonrigorous scout for the actual-theta third tail S_3(T, P).

The exact formula is

  S_3(T,P) = L(T) - (2/pi) int_0^inf
      [Z(T)^2-Z(T+x)Z(T-x)] sin(Px)/x^3 dx,

where Z(t)=xi((1-it)/2)/4 is even and
L(T)=Z'(T)^2-Z(T)Z''(T).  On a uniform x-grid, a DST-I evaluates
all P=k*pi/W at once.  The constant Z(T)^2 tail after W is integrated
analytically; the remaining product tail is deliberately omitted.

This is a candidate finder, not an interval certificate.  Apparent negative
values must be rerun with arbitrary precision and then Arb.
"""

from __future__ import annotations

import argparse
import math
import time

import mpmath as mp
import numpy as np
from scipy.fft import dst
from scipy.special import loggamma, sici


def critical_transform_grid(t: np.ndarray, dps: int, backend: str) -> np.ndarray:
    """Evaluate exp(pi*t/8)*xi((1-it)/2)/4 for t>=0.

    If q=t/2, then

      Z(t)=-(q^2+1/4)/8*pi^(-1/4)*|Gamma(1/4+iq/2)|*HardyZ(q).

    The exponentially small gamma factor is formed in logarithmic scale.
    mpmath supplies HardyZ; all remaining operations are vectorized doubles.
    """
    if backend == "arb":
        from flint import acb, arb, ctx

        ctx.dps = dps
        pi = arb.pi()
        imaginary_unit = acb(0, 1)

        def one(value: float) -> float:
            s = (1 - imaginary_unit * arb(float(value))) / 2
            xi = (
                arb("0.5")
                * s
                * (s - 1)
                * ((-s / 2) * pi.log()).exp()
                * (s / 2).gamma()
                * s.zeta()
            )
            scaled = xi / 4 * (pi * arb(float(value)) / 8).exp()
            return float(scaled.real.mid())

        return np.fromiter((one(value) for value in t), float, len(t))

    mp.mp.dps = dps
    q = t / 2.0
    hardy = np.fromiter((float(mp.siegelz(float(x))) for x in q), float, len(q))
    log_amp = (
        np.log((q * q + 0.25) / 8.0)
        - 0.25 * math.log(math.pi)
        + np.real(loggamma(0.25 + 0.5j * q))
    )
    return -np.exp(log_amp + math.pi * t / 8.0) * hardy


def constant_sine_cubic_tail(p: np.ndarray, cutoff: float) -> np.ndarray:
    """Integral from cutoff to infinity of sin(p*x)/x^3, for p>0."""
    si, _ = sici(p * cutoff)
    return (
        np.sin(p * cutoff) / (2.0 * cutoff**2)
        + p * np.cos(p * cutoff) / (2.0 * cutoff)
        - 0.5 * p * p * (math.pi / 2.0 - si)
    )


def extrapolate_laguerre(product_gap: np.ndarray, dx: float, count: int = 6) -> float:
    """Extrapolate [Z(T)^2-Z(T+x)Z(T-x)]/x^2 to x=0."""
    j = np.arange(1, count + 1, dtype=float)
    x2 = (j * dx) ** 2
    values = product_gap[1 : count + 1] / x2
    degree = min(3, count - 1)
    return float(np.polynomial.polynomial.polyfit(x2, values, degree)[0])


def scan(args: argparse.Namespace) -> None:
    dx = args.dx
    # At height T the x-integral is retained through W=T+margin and needs
    # transform arguments through T+W=2T+margin.
    t_values = np.arange(0.0, 2.0 * args.t_max + args.margin + dx / 2.0, dx)
    started = time.time()
    z = critical_transform_grid(t_values, args.dps, args.backend)
    print(
        "transform grid",
        len(t_values),
        "extent", t_values[-1],
        "dx", dx,
        "seconds", round(time.time() - started, 3),
    )

    stride = max(1, int(round(args.t_step / dx)))
    i_first = max(1, int(math.ceil(args.t_min / dx)))
    i_last = min(int(math.floor(args.t_max / dx)), len(z) - 2)
    records: list[tuple[float, float, float, float, float]] = []

    for i in range(i_first, i_last + 1, stride):
        t = i * dx
        # W is aligned to the common grid and lies margin beyond T.  This
        # makes the discarded product tail exponentially small relative to
        # the main scale.
        n = min(i + int(round(args.margin / dx)), len(z) - 1 - i)
        if n < 16:
            continue
        j = np.arange(n + 1)
        # All quantities are divided by exp(-pi*T/4).  For x<=T the
        # exponential factors in Z(T+x)Z(T-x) cancel exactly.  For x>T an
        # extra exp(-pi*(x-T)/4) remains.  This avoids underflow past T~960.
        product_factor = np.ones(n + 1)
        beyond = j > i
        product_factor[beyond] = np.exp(-math.pi * (j[beyond] - i) * dx / 4.0)
        gap = z[i] * z[i] - product_factor * z[i + j] * z[np.abs(i - j)]
        laguerre = extrapolate_laguerre(gap, dx)

        x = j[1:n] * dx
        divided = gap[1:n] / (x**3)
        sine_sums = dst(divided, type=1)
        # scipy's DST-I is 2*sum_j f_j sin(pi*j*k/n).
        integral = 0.5 * dx * sine_sums
        k = np.arange(1, n)
        p = math.pi * k / (n * dx)
        keep = p <= min(args.p_max, math.log1p(t) + args.wedge_pad)
        p = p[keep]
        integral = integral[keep]
        # Although gap/x^3 itself behaves like L/x, the full integrand has
        # the finite endpoint limit L*P.  DST-I contains only the interior
        # trapezoid nodes, so restore the half-weight at x=0.
        integral += 0.5 * dx * laguerre * p
        integral += z[i] * z[i] * constant_sine_cubic_tail(p, n * dx)
        s3 = laguerre - (2.0 / math.pi) * integral

        scale = max(abs(laguerre), z[i] * z[i], np.finfo(float).tiny)
        relative = s3 / scale
        if len(s3):
            m = int(np.argmin(relative))
            records.append((float(relative[m]), float(s3[m]), float(t), float(p[m]), laguerre))
        records.append((laguerre / scale, laguerre, float(t), 0.0, laguerre))

    records.sort(key=lambda row: row[0])
    print("smallest S_3/scale candidates")
    for relative, value, t, p, laguerre in records[: args.show]:
        print(
            f"T={t:.9g} P={p:.9g} scaled_S3={value:+.17e} "
            f"relative={relative:+.9e} scaled_L={laguerre:+.17e}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--t-min", type=float, default=0.0)
    parser.add_argument("--t-max", type=float, default=200.0)
    parser.add_argument("--t-step", type=float, default=0.2)
    parser.add_argument("--p-max", type=float, default=10.0)
    parser.add_argument("--wedge-pad", type=float, default=3.0)
    parser.add_argument("--margin", type=float, default=35.0)
    parser.add_argument("--dx", type=float, default=0.025)
    parser.add_argument("--dps", type=int, default=25)
    parser.add_argument("--backend", choices=("arb", "mpmath"), default="arb")
    parser.add_argument("--show", type=int, default=30)
    scan(parser.parse_args())
