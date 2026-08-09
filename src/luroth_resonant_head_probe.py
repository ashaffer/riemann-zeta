"""Diagnostics for the R95 Luroth resonant-head analysis.

The routines verify exact finite-head and Hurwitz-tail identities and sample
the alias/stationary-window asymptotics.  They are numerical diagnostics, not
a zero-free theorem.
"""
from __future__ import annotations

import argparse
import cmath
import math


def digit_contribution(n: int, s: complex) -> complex:
    """Return the exact n-th Luroth correlation contribution J_n(s)."""

    if n < 1:
        raise ValueError("n must be positive")
    z = complex(s)
    if z == 0 or z == -1:
        raise ValueError("the displayed formula has a removable/singular denominator")
    return (
        z * n ** (-z) - n ** (1 - z) + n * (n + 1) ** (-z)
    ) / (z * (z + 1))


def direct_head(cutoff: int, s: complex) -> complex:
    """Sum the first ``cutoff`` exact digit contributions."""

    if cutoff < 0:
        raise ValueError("cutoff must be nonnegative")
    return sum((digit_contribution(n, s) for n in range(1, cutoff + 1)), 0.0j)


def closed_head(cutoff: int, s: complex) -> complex:
    """Evaluate the summation-by-parts closed form for the finite head."""

    if cutoff < 1:
        return 0.0j
    z = complex(s)
    partial_zeta = sum((n ** (-z) for n in range(1, cutoff + 1)), 0.0j)
    return (
        (z - 1) * partial_zeta + cutoff * (cutoff + 1) ** (-z)
    ) / (z * (z + 1))


def exact_tail(cutoff: int, s: complex) -> complex:
    """Evaluate the exact Hurwitz-zeta tail from R94/R95."""

    if cutoff < 0:
        raise ValueError("cutoff must be nonnegative")
    import mpmath as mp

    z = mp.mpc(s)
    a = mp.mpf(cutoff + 1)
    value = (
        (z - 1) * mp.zeta(z, a) + a ** (-z) - a ** (1 - z)
    ) / (z * (z + 1))
    return complex(value)


def linear_tail_symbol(z: complex) -> complex:
    """Return G(z), the alias-free linear-cutoff response symbol."""

    z = complex(z)
    if z == 0:
        raise ValueError("G has a pole at zero")
    return 1 / (z * (1 - cmath.exp(-z))) - 1 / z**2


def alias_response(k: int) -> complex:
    """Return the limiting target response at the k-th integer alias."""

    if k < 1:
        raise ValueError("k must be positive")
    return 1 / (2j * math.pi * k)


def scaled_alias_sample(k: int, sigma: float, height: float) -> complex:
    """Sample n^(s+1) J_n(s) at n nearest height/(2*pi*k)."""

    if height <= 0:
        raise ValueError("height must be positive")
    n = max(1, round(height / (2 * math.pi * k)))
    s = complex(sigma, height)
    return n ** (s + 1) * digit_contribution(n, s)


def fresnel_window(c: float, steps: int = 20_000) -> complex:
    """Midpoint quadrature for integral_-c^c exp(2*pi^2*i*u^2) du."""

    if c <= 0 or steps < 1:
        raise ValueError("c and steps must be positive")
    mesh = 2 * c / steps
    return mesh * sum(
        (
            cmath.exp(2j * math.pi**2 * (-c + (index + 0.5) * mesh) ** 2)
            for index in range(steps)
        ),
        0.0j,
    )


def stationary_block(k: int, s: complex, c: float) -> complex:
    """Sum the exact digits in the k-th sqrt-height stationary window."""

    z = complex(s)
    if k < 1 or z.imag <= 0 or c <= 0:
        raise ValueError("require k>=1, positive height, and c>0")
    center = z.imag / (2 * math.pi * k)
    radius = c * math.sqrt(z.imag) / k
    lower = max(1, math.ceil(center - radius))
    upper = math.floor(center + radius)
    return sum((digit_contribution(n, z) for n in range(lower, upper + 1)), 0.0j)


def stationary_prediction(k: int, s: complex, c: float) -> complex:
    """Return the leading R95 stationary-window prediction."""

    z = complex(s)
    if k < 1 or z.imag <= 0:
        raise ValueError("require k>=1 and positive height")
    t = z.imag
    common_phase = cmath.exp(1j * (t - t * math.log(t / (2 * math.pi))))
    return (
        (2 * math.pi) ** z.real
        * fresnel_window(c)
        / 1j
        * t ** (-z.real - 0.5)
        * common_phase
        * k ** (z - 1)
    )


def run_probe(sigma: float, height: float, kmax: int, c: float) -> None:
    s = complex(sigma, height)
    cutoff = max(1, round(2 * height))
    a = cutoff + 1
    observed_tail = a ** (s + 1) * exact_tail(cutoff, s)
    predicted_tail = linear_tail_symbol(1j * height / a)
    print(f"s={s}, linear cutoff a={a}")
    print(f"scaled tail:      {observed_tail}")
    print(f"limiting symbol:  {predicted_tail}")
    print(f"symbol error:     {abs(observed_tail - predicted_tail):.6g}")
    for k in range(1, kmax + 1):
        alias = scaled_alias_sample(k, sigma, height)
        block = stationary_block(k, s, c)
        prediction = stationary_prediction(k, s, c)
        print(
            f"k={k}: alias_error={abs(alias-alias_response(k)):.6g}, "
            f"block_relative_error={abs(block-prediction)/abs(prediction):.6g}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sigma", type=float, default=0.9)
    parser.add_argument("--height", type=float, default=100_000.0)
    parser.add_argument("--kmax", type=int, default=3)
    parser.add_argument("--window", type=float, default=0.12)
    args = parser.parse_args()
    run_probe(args.sigma, args.height, args.kmax, args.window)


if __name__ == "__main__":
    main()
