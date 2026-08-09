#!/usr/bin/env python3
"""Probe the scaled additive twist of the proportional B-spline window.

For the unnormalized compact window ``W_(h,k)`` define

    T_(h,k)(s, xi)
      = integral W_(h,k)(u) exp(-s*u) exp(-2*pi*i*xi*exp(-u)) du.

At ``xi=0`` this is the usual coboundary multiplier.  For
``0 < Re(s) < 1`` and fixed nonzero ``xi``, the analytic limit as ``k`` tends
to infinity is

    Gamma(s) (2*pi*abs(xi))**(-s)
      exp(-i*sign(xi)*pi*s/2).

The numerical integration here is a modest-order diagnostic only.  The
limit theorem is proved analytically in
``COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md``.
"""

from __future__ import annotations

import argparse
import cmath
import math

from scipy.integrate import quad
from scipy.special import gamma

from fixed_step_spectral_cooling_probe import compact_window


def scaled_additive_limit(s: complex, xi: float) -> complex:
    """Return the nonzero-frequency Gamma-limit multiplier."""

    value = complex(s)
    if not 0.0 < value.real < 1.0:
        raise ValueError("s must satisfy 0 < Re(s) < 1")
    if not math.isfinite(xi) or xi == 0.0:
        raise ValueError("xi must be finite and nonzero")
    sign = 1.0 if xi > 0.0 else -1.0
    return complex(gamma(value)) * (2.0 * math.pi * abs(xi)) ** (-value) * (
        cmath.exp(-0.5j * sign * math.pi * value)
    )


def finite_scaled_additive_multiplier(
    s: complex,
    h: float,
    order: int,
    xi: float,
    *,
    absolute_tolerance: float = 1.0e-9,
) -> complex:
    """Numerically integrate the exact finite-order multiplier.

    Splitting at the B-spline knots keeps the modest-order regression stable.
    This is not intended for highly oscillatory production calculations.
    """

    value = complex(s)
    if not math.isfinite(h) or h <= 0.0:
        raise ValueError("h must be finite and positive")
    if not isinstance(order, int) or isinstance(order, bool) or order <= 0:
        raise ValueError("order must be a positive integer")
    if not math.isfinite(xi):
        raise ValueError("xi must be finite")
    if not math.isfinite(absolute_tolerance) or absolute_tolerance <= 0.0:
        raise ValueError("absolute_tolerance must be finite and positive")

    def integrand(u: float) -> complex:
        phase = -2.0j * math.pi * xi * math.exp(-u)
        return compact_window(u, h, order) * cmath.exp(-value * u + phase)

    real_part = 0.0
    imaginary_part = 0.0
    for index in range(-order, order):
        left = index * h
        right = (index + 1) * h
        real_part += quad(
            lambda u: integrand(u).real,
            left,
            right,
            epsabs=absolute_tolerance,
            limit=200,
        )[0]
        imaginary_part += quad(
            lambda u: integrand(u).imag,
            left,
            right,
            epsabs=absolute_tolerance,
            limit=200,
        )[0]
    return complex(real_part, imaginary_part)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--delta", type=float, default=0.2)
    parser.add_argument("--gamma", type=float, default=0.7)
    parser.add_argument("--xi", type=float, default=0.3)
    parser.add_argument("--h", type=float, default=0.2)
    parser.add_argument("--order", type=int, default=20)
    args = parser.parse_args()
    s = complex(args.delta, args.gamma)
    finite = finite_scaled_additive_multiplier(
        s,
        args.h,
        args.order,
        args.xi,
    )
    limiting = scaled_additive_limit(s, args.xi)
    print(f"finite={finite!r}")
    print(f"limit={limiting!r}")
    print(f"absolute_error={abs(finite-limiting):.12g}")


if __name__ == "__main__":
    main()
