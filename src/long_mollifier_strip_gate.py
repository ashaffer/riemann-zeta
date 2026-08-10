#!/usr/bin/env python3
"""Exact finite arithmetic and exponent ledger for a long-mollifier strip gate.

This module proves no analytic mollified-moment estimate. It records the
algebraic conversion from a mollifier length ``T**theta`` to the conditional
zero-free-strip boundary and checks the exact Dirichlet coefficients on the
absolute-convergence side.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True)
class LongMollifierStripGate:
    """Exponent bookkeeping for the averaged long-mollifier criterion."""

    theta: float
    natural_moment_exponent: float
    right_boundary: float
    strip_width: float
    additive_resolution_exponent_in_y: float


def long_mollifier_strip_gate(theta: float) -> LongMollifierStripGate:
    """Return the strip parameters associated with a fixed ``theta > 1``.

    The conditional input has natural size ``T**(theta + 1 + o(1))``. The
    averaged criterion then excludes zeros to the right of
    ``(theta + 1)/(2*theta)``. Functional-equation symmetry would give strip
    width ``(theta - 1)/(2*theta)``.
    """

    if not math.isfinite(theta) or theta <= 1.0:
        raise ValueError("theta must be finite and strictly greater than one")
    right_boundary = (theta + 1.0) / (2.0 * theta)
    strip_width = (theta - 1.0) / (2.0 * theta)
    return LongMollifierStripGate(
        theta=theta,
        natural_moment_exponent=theta + 1.0,
        right_boundary=right_boundary,
        strip_width=strip_width,
        additive_resolution_exponent_in_y=1.0 - 1.0 / theta,
    )


def theta_for_strip_width(strip_width: float) -> float:
    """Invert ``delta=(theta-1)/(2*theta)`` for ``0 < delta < 1/2``."""

    if not math.isfinite(strip_width) or not 0.0 < strip_width < 0.5:
        raise ValueError(
            "strip_width must be finite and strictly between zero and one half"
        )
    return 1.0 / (1.0 - 2.0 * strip_width)


def exact_long_mollifier_strip_gate(
    theta: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Exact rational version: ``(natural exponent, boundary, width)``."""

    if theta <= 1:
        raise ValueError("theta must be strictly greater than one")
    return (
        theta + 1,
        (theta + 1) / (2 * theta),
        (theta - 1) / (2 * theta),
    )


def _require_positive_integer(value: int, name: str) -> None:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def prime_factorization(n: int) -> dict[int, int]:
    """Return the prime factorization of a positive integer."""

    _require_positive_integer(n, "n")
    remaining = n
    factors: dict[int, int] = {}
    p = 2
    while p * p <= remaining:
        while remaining % p == 0:
            factors[p] = factors.get(p, 0) + 1
            remaining //= p
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def mobius(n: int) -> int:
    """The Moebius function ``mu(n)``."""

    factors = prime_factorization(n)
    if any(exponent > 1 for exponent in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def von_mangoldt(n: int) -> float:
    """The von Mangoldt function ``Lambda(n)`` as a real number."""

    factors = prime_factorization(n)
    if len(factors) != 1:
        return 0.0
    prime = next(iter(factors))
    return math.log(prime)


def divisors(n: int) -> tuple[int, ...]:
    """All positive divisors of ``n`` in increasing order."""

    factors = prime_factorization(n)
    result = [1]
    for prime, exponent in factors.items():
        powers = [prime**k for k in range(1, exponent + 1)]
        result = result + [divisor * power for divisor in result for power in powers]
    return tuple(sorted(result))


def logarithmic_mollifier_coefficient(n: int, y: float) -> float:
    r"""Return

    ``c_y(n) = sum_{d|n,d<=y} mu(d) log(y/d) / log(y)``.
    """

    _require_positive_integer(n, "n")
    if not math.isfinite(y) or y <= 1.0:
        raise ValueError("y must be finite and strictly greater than one")
    return sum(
        mobius(divisor) * math.log(y / divisor)
        for divisor in divisors(n)
        if divisor <= y
    ) / math.log(y)


def late_divisor_correction(n: int, y: float) -> float:
    r"""Return ``R_y(n)=sum_{d|n,d>y} mu(d) log(d/y)``."""

    _require_positive_integer(n, "n")
    if not math.isfinite(y) or y <= 1.0:
        raise ValueError("y must be finite and strictly greater than one")
    return sum(
        mobius(divisor) * math.log(divisor / y)
        for divisor in divisors(n)
        if divisor > y
    )


def completed_coefficient_formula(n: int, y: float) -> float:
    """Return ``(Lambda(n)+R_y(n))/log(y)`` for ``n>1``."""

    _require_positive_integer(n, "n")
    if n == 1:
        raise ValueError("the completed coefficient formula is stated for n > 1")
    if not math.isfinite(y) or y <= 1.0:
        raise ValueError("y must be finite and strictly greater than one")
    return (von_mangoldt(n) + late_divisor_correction(n, y)) / math.log(y)


def first_overlength_band_formula(n: int, y: float) -> float:
    """Return the exact formula valid when ``y < n <= 2*y``."""

    _require_positive_integer(n, "n")
    if not math.isfinite(y) or y <= 1.0:
        raise ValueError("y must be finite and strictly greater than one")
    if not y < n <= 2.0 * y:
        raise ValueError("the first-band formula requires y < n <= 2*y")
    return (von_mangoldt(n) + mobius(n) * math.log(n / y)) / math.log(y)


def sharp_reciprocal_coefficient(n: int, cutoff: int) -> int:
    """Coefficient of ``zeta(s) * sum_{d<=cutoff} mu(d)d^{-s}``."""

    _require_positive_integer(n, "n")
    _require_positive_integer(cutoff, "cutoff")
    return sum(mobius(divisor) for divisor in divisors(n) if divisor <= cutoff)


def verify_coefficient_ledger(
    y_values: Iterable[float], n_max: int, tolerance: float = 5.0e-13
) -> float:
    """Return the largest residual in the finite completed-coefficient audit."""

    _require_positive_integer(n_max, "n_max")
    if not math.isfinite(tolerance) or tolerance < 0.0:
        raise ValueError("tolerance must be finite and nonnegative")
    largest = 0.0
    for y in y_values:
        if not math.isfinite(y) or y <= 1.0:
            raise ValueError("every y value must be finite and greater than one")
        for n in range(2, n_max + 1):
            residual = abs(
                logarithmic_mollifier_coefficient(n, y)
                - completed_coefficient_formula(n, y)
            )
            largest = max(largest, residual)
            if residual > tolerance:
                raise AssertionError(
                    f"completed coefficient identity failed for n={n}, y={y}: "
                    f"{residual}"
                )
    return largest
