#!/usr/bin/env python3
"""Low-memory normalization check for the fixed-box Weil observable.

This evaluates the exact arithmetic side

    B_l(R) = J_l (exp(R/2)+exp(-R/2))
             - sum Lambda(n)/sqrt(n) w_l(log(n)-R)
             - Gamma_l(R)

and, optionally, compares it with a truncation of its critical-line zero
series.  The comparison is a diagnostic only.  The analytic theorem and its
trust boundary are in ``results/FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md``.
"""

from __future__ import annotations

import argparse
import math

import mpmath as mp
import numpy as np
from scipy.integrate import quad

from signed_garding_failfast import prime_powers


def triangle(value: np.ndarray | float, length: float) -> np.ndarray | float:
    """The normalized box autocorrelation ``(1-|value|/length)_+``."""
    answer = np.maximum(1.0 - np.abs(value) / length, 0.0)
    return answer if np.ndim(value) else float(answer)


def ramp(value: np.ndarray | float, length: float) -> np.ndarray | float:
    """The clipped ramp whose length-``length`` difference is ``triangle``."""
    if length <= 0:
        raise ValueError("length must be positive")
    answer = np.clip(np.asarray(value, dtype=float) / length, 0.0, 1.0)
    return answer if np.ndim(value) else float(answer)


def main_coefficient(length: float) -> float:
    """The coefficient cancelling the positive zeta-pole main term."""
    if length <= 0:
        raise ValueError("length must be positive")
    return 16.0 * math.sinh(length / 4.0) ** 2 / length


def archimedean_correction(length: float, separation: float) -> float:
    """The positive integral subtracted in the time-domain Weil formula."""
    if not separation > length > 0:
        raise ValueError("require separation > length > 0")

    def integrand(u: float) -> float:
        weight = triangle(u - separation, length)
        # This stable spelling equals exp(u/2)/(exp(u)-exp(-u)).
        return weight * math.exp(-u / 2.0) / (-math.expm1(-2.0 * u))

    left = separation - length
    return quad(integrand, left, separation, epsabs=2e-14, epsrel=2e-14)[0] + quad(
        integrand,
        separation,
        separation + length,
        epsabs=2e-14,
        epsrel=2e-14,
    )[0]


def prime_triangle_sum(
    length: float,
    separation: float,
    logs: np.ndarray,
    weights: np.ndarray,
) -> float:
    """Return ``sum Lambda(n)/sqrt(n) w_l(log(n)-R)``."""
    return float(weights @ triangle(logs - separation, length))


def arithmetic_cross(length: float, separation: float) -> dict[str, float]:
    """Evaluate the three exact arithmetic components of ``B_l(R)``."""
    if not separation > length > 0:
        raise ValueError("require separation > length > 0")
    limit = math.ceil(math.exp(separation + length))
    logs, weights = prime_powers(limit)
    coefficient = main_coefficient(length)
    pole = coefficient * (
        math.exp(separation / 2.0) + math.exp(-separation / 2.0)
    )
    prime = prime_triangle_sum(length, separation, logs, weights)
    arch = archimedean_correction(length, separation)
    return {
        "coefficient": coefficient,
        "pole": pole,
        "prime": prime,
        "archimedean": arch,
        "cross": pole - prime - arch,
        "discrepancy": prime - coefficient * math.exp(separation / 2.0),
    }


def truncated_zero_cross(
    length: float, separation: float, count: int, dps: int = 30
) -> mp.mpf:
    """Truncate the paired critical-line cosine series at ``count`` zeros."""
    if count < 0:
        raise ValueError("count must be nonnegative")
    with mp.workdps(dps):
        ell = mp.mpf(length)
        radius = mp.mpf(separation)
        answer = mp.mpf("0")
        for index in range(1, count + 1):
            gamma = mp.im(mp.zetazero(index))
            coefficient = 4 * mp.sin(ell * gamma / 2) ** 2 / (
                ell * gamma**2
            )
            answer += 2 * coefficient * mp.cos(gamma * radius)
        return +answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=float, default=1.0)
    parser.add_argument("--separation", type=float, default=4.0)
    parser.add_argument("--zeros", type=int, default=100)
    parser.add_argument("--dps", type=int, default=30)
    args = parser.parse_args()

    values = arithmetic_cross(args.length, args.separation)
    for key, value in values.items():
        print(f"{key}={value:.16g}")
    if args.zeros:
        zero_value = truncated_zero_cross(
            args.length, args.separation, args.zeros, args.dps
        )
        print(f"zero_sum_{args.zeros}={mp.nstr(zero_value, 18)}")
        print(f"zero_minus_arithmetic={mp.nstr(zero_value-values['cross'], 10)}")


if __name__ == "__main__":
    main()
