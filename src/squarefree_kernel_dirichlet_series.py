#!/usr/bin/env python3
"""Euler-product factorization for the squarefree reciprocity sieve kernel.

This module proves no long-mollifier estimate and no zero-free region. It
records the exact finite Euler-product algebra and the residue coefficient at
the unique zeta pole suggested by the infinite product.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction

from prime_reciprocity_sieve_kernel import primes_up_to


def _require_sign(sign: int) -> None:
    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or 1")


def _odd_distinct_prime_factors(value: int) -> tuple[int, ...]:
    """Distinct odd prime factors of a nonzero integer."""

    if not isinstance(value, int) or isinstance(value, bool) or value == 0:
        raise ValueError("value must be a nonzero integer")
    remaining = abs(value)
    factors: list[int] = []
    while remaining % 2 == 0:
        remaining //= 2
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            factors.append(p)
            while remaining % p == 0:
                remaining //= p
        p += 2
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def base_local_factor(p: int, z: complex) -> complex:
    """Return ``1+p^(-z)/(p-1)`` for an odd prime p."""

    if p < 3 or p % 2 == 0:
        raise ValueError("p must be an odd prime")
    return 1.0 + cmath.exp(-complex(z) * math.log(p)) / (p - 1)


def zeta_removed_local_factor(p: int, z: complex) -> complex:
    r"""Return ``(1+p^(-z)/(p-1))(1-p^(-1-z))``."""

    power = cmath.exp(-complex(z) * math.log(p))
    return (1.0 + power / (p - 1)) * (1.0 - power / p)


def branch_local_factor(p: int, value: int, sign: int, z: complex) -> complex:
    """Actual local Euler factor for one congruence branch."""

    _require_sign(sign)
    if value % p == 0:
        return 1.0 + 0.0j
    indicator = int(value % p == sign % p)
    coefficient = 1.0 / (p - 1) - indicator
    return 1.0 + coefficient * cmath.exp(-complex(z) * math.log(p))


def branch_correction_factor(p: int, value: int, sign: int, z: complex) -> complex:
    """Ratio of the actual branch factor to the universal base factor."""

    return branch_local_factor(p, value, sign, z) / base_local_factor(p, z)


def finite_raw_euler_product(
    prime_limit: int, value: int, sign: int, z: complex
) -> complex:
    """Direct product of branch factors over odd primes up to P."""

    _require_sign(sign)
    answer = 1.0 + 0.0j
    for p in primes_up_to(prime_limit):
        if p > 2:
            answer *= branch_local_factor(p, value, sign, z)
    return answer


def finite_factorized_euler_product(
    prime_limit: int, value: int, sign: int, z: complex
) -> complex:
    r"""Same product as partial zeta factor, analytic H factor, and corrections."""

    _require_sign(sign)
    partial_odd_zeta = 1.0 + 0.0j
    analytic_product = 1.0 + 0.0j
    corrections = 1.0 + 0.0j
    zc = complex(z)
    for p in primes_up_to(prime_limit):
        if p == 2:
            continue
        power = cmath.exp(-zc * math.log(p))
        partial_odd_zeta /= 1.0 - power / p
        analytic_product *= zeta_removed_local_factor(p, zc)
        corrections *= branch_correction_factor(p, value, sign, zc)
    return partial_odd_zeta * analytic_product * corrections


def branch_pole_residue(value: int, sign: int) -> Fraction:
    r"""Residue at z=0 of the infinite one-branch Dirichlet series.

    The universal odd-prime base has residue one half. Primes dividing value
    contribute ``(p-1)/p``; primes dividing ``value-sign`` contribute ``1/p``.
    If ``value`` or ``value-sign`` is zero, infinitely many local factors are
    altered and the zeta pole is removed, so the residue is zero.
    """

    _require_sign(sign)
    if value == 0 or value == sign:
        return Fraction(0)
    answer = Fraction(1, 2)
    for p in _odd_distinct_prime_factors(value):
        answer *= Fraction(p - 1, p)
    for p in _odd_distinct_prime_factors(value - sign):
        answer /= p
    return answer


def even_kernel_pole_residue(value: int) -> Fraction:
    """Residue for the average of the plus and minus branches."""

    return (branch_pole_residue(value, 1) + branch_pole_residue(value, -1)) / 2


def normalized_log_taper_leading_coefficient(value: int) -> Fraction:
    r"""Coefficient of ``log y`` after first-order normalized log tapering.

    If the Dirichlet series is ``C/z+O(1)``, then

      1/log(y) * integral F(z)y^z dz/z^2

    has leading term ``(C/2)log(y)``.
    """

    return even_kernel_pole_residue(value) / 2
