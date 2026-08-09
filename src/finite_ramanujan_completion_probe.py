#!/usr/bin/env python3
"""Exact symbolic check of the finite von-Mangoldt Ramanujan expansion.

Logarithms of distinct primes are tracked as formal basis vectors with
rational coefficients.  This verifies, without floating-point tolerance,

    Lambda_N(n) = sum_(q<=N) LambdaHat_N(q) c_q(n)

on the active range ``n<=N``.  The analytic estimates and Poisson completion
are proved in ``COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md``.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


LogVector = dict[int, Fraction]


def mobius_sieve(limit: int) -> list[int]:
    """Return the Möbius function on ``0..limit``."""

    if limit < 1:
        raise ValueError("limit must be positive")
    values = [1] * (limit + 1)
    values[0] = 0
    prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        for multiple in range(p, limit + 1, p):
            prime[multiple] = False
            values[multiple] *= -1
        square = p * p
        for multiple in range(square, limit + 1, square):
            values[multiple] = 0
    return values


def prime_factors(value: int) -> tuple[int, ...]:
    """Return the distinct prime factors of a positive integer."""

    if value < 1:
        raise ValueError("value must be positive")
    factors: list[int] = []
    residual = value
    divisor = 2
    while divisor * divisor <= residual:
        if residual % divisor == 0:
            factors.append(divisor)
            while residual % divisor == 0:
                residual //= divisor
        divisor += 1
    if residual > 1:
        factors.append(residual)
    return tuple(factors)


def ramanujan_sum(q: int, n: int, mobius: list[int]) -> int:
    """Return ``c_q(n)`` from the divisor formula."""

    common = math.gcd(q, n)
    return sum(
        divisor * mobius[q // divisor]
        for divisor in range(1, common + 1)
        if common % divisor == 0
    )


def finite_coefficients(limit: int) -> list[LogVector]:
    """Return formal-log vectors for ``LambdaHat_N(q)``."""

    mobius = mobius_sieve(limit)
    coefficients: list[LogVector] = [{} for _ in range(limit + 1)]
    for d in range(1, limit + 1):
        if mobius[d] == 0:
            continue
        contribution = Fraction(-mobius[d], d)
        factors = prime_factors(d)
        for q in range(1, d + 1):
            if d % q != 0:
                continue
            for p in factors:
                coefficients[q][p] = coefficients[q].get(p, Fraction()) + contribution
    return coefficients


def reconstruct(limit: int, n: int) -> LogVector:
    """Reconstruct ``Lambda_N(n)`` in the formal prime-log basis."""

    if not 1 <= n <= limit:
        raise ValueError("n must lie in the active range")
    mobius = mobius_sieve(limit)
    coefficients = finite_coefficients(limit)
    result: LogVector = {}
    for q in range(1, limit + 1):
        weight = ramanujan_sum(q, n, mobius)
        for p, coefficient in coefficients[q].items():
            result[p] = result.get(p, Fraction()) + weight * coefficient
    return {p: coefficient for p, coefficient in result.items() if coefficient}


def expected_von_mangoldt(n: int) -> LogVector:
    """Return the formal vector for ``Lambda(n)``."""

    factors = prime_factors(n)
    if len(factors) != 1:
        return {}
    p = factors[0]
    residual = n
    while residual % p == 0:
        residual //= p
    return {p: Fraction(1)} if residual == 1 and n > 1 else {}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()
    for n in range(1, args.limit + 1):
        if reconstruct(args.limit, n) != expected_von_mangoldt(n):
            raise AssertionError(f"finite expansion failed at n={n}")
    print(f"verified_exactly_for_1_through_{args.limit}")


if __name__ == "__main__":
    main()
