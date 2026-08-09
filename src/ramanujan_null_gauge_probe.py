#!/usr/bin/env python3
"""Exact probe for the finite high-prime Ramanujan null gauge.

On an active integer range ``1 <= n <= Y`` and with finite Ramanujan
cutoff ``N = 2Y``, every prime ``Y < p <= 2Y`` obeys

    c_1(n) + c_p(n) = 0.

These finite-range null relations move the sole continuum zero mode in the
completed finite Ramanujan expansion into nonzero integer and rational
frequencies.  Logarithms of distinct primes are represented formally, so the
reconstruction checks below are exact rather than floating-point tests.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction

from finite_ramanujan_completion_probe import (
    expected_von_mangoldt,
    finite_coefficients,
    mobius_sieve,
    ramanujan_sum,
)


CONSTANT_KEY = 0
AffineLogVector = dict[int, Fraction]


def primes_between(lower: int, upper: int) -> tuple[int, ...]:
    """Return the primes in the half-open interval ``(lower, upper]``."""

    if lower < 1 or upper <= lower:
        raise ValueError("require 1 <= lower < upper")
    sieve = [True] * (upper + 1)
    sieve[0:2] = [False, False]
    for p in range(2, math.isqrt(upper) + 1):
        if not sieve[p]:
            continue
        for multiple in range(p * p, upper + 1, p):
            sieve[multiple] = False
    return tuple(p for p in range(lower + 1, upper + 1) if sieve[p])


def inverse_totient_weights(active_limit: int) -> dict[int, Fraction]:
    """Return the minimum-ledger normalized weights on ``Y < p <= 2Y``."""

    primes = primes_between(active_limit, 2 * active_limit)
    if not primes:
        raise ValueError("the dyadic prime cloud is empty")
    reciprocal_sum = sum((Fraction(1, p - 1) for p in primes), Fraction())
    return {p: Fraction(1, p - 1) / reciprocal_sum for p in primes}


def add_scaled(
    target: AffineLogVector,
    source: AffineLogVector,
    scale: Fraction,
) -> None:
    """Add ``scale * source`` to ``target`` in place."""

    for basis, coefficient in source.items():
        target[basis] = target.get(basis, Fraction()) + scale * coefficient
        if target[basis] == 0:
            del target[basis]


def gauged_coefficients(active_limit: int) -> list[AffineLogVector]:
    """Return the exact all-nonzero-mode coefficients at cutoff ``2Y``.

    Index one is the coefficient of the punctured integer lattice, so it is
    exactly one.  For ``q >= 2`` the entries multiply the complete primitive
    nonzero rational lattice of denominator ``q``.
    """

    cutoff = 2 * active_limit
    original = finite_coefficients(cutoff)
    result: list[AffineLogVector] = [dict(vector) for vector in original]

    # z = LambdaHat_N(1) - 1 is the old continuum zero coefficient.
    zero_mode: AffineLogVector = dict(original[1])
    zero_mode[CONSTANT_KEY] = zero_mode.get(CONSTANT_KEY, Fraction()) - 1

    result[1] = {CONSTANT_KEY: Fraction(1)}
    for p, weight in inverse_totient_weights(active_limit).items():
        add_scaled(result[p], zero_mode, -weight)
    return result


def reconstruct_gauged(active_limit: int, n: int) -> AffineLogVector:
    """Reconstruct ``Lambda(n)`` from the gauged nonzero-mode blocks."""

    if not 1 <= n <= active_limit:
        raise ValueError("n must lie in the active range")
    cutoff = 2 * active_limit
    mobius = mobius_sieve(cutoff)
    coefficients = gauged_coefficients(active_limit)
    result: AffineLogVector = {}
    for q in range(1, cutoff + 1):
        weight = ramanujan_sum(q, n, mobius)
        add_scaled(result, coefficients[q], Fraction(weight))
    return result


def null_relation(active_limit: int, n: int) -> Fraction:
    """Return ``c_1(n) + sum_p w_p c_p(n)`` exactly."""

    if not 1 <= n <= active_limit:
        raise ValueError("n must lie in the active range")
    mobius = mobius_sieve(2 * active_limit)
    value = Fraction(ramanujan_sum(1, n, mobius))
    for p, weight in inverse_totient_weights(active_limit).items():
        value += weight * ramanujan_sum(p, n, mobius)
    return value


def evaluate(vector: AffineLogVector) -> float:
    """Numerically evaluate a formal affine prime-log vector."""

    return sum(
        float(coefficient) * (1.0 if basis == CONSTANT_KEY else math.log(basis))
        for basis, coefficient in vector.items()
    )


def coefficient_ledger(coefficients: list[AffineLogVector]) -> float:
    """Return ``sum_q phi(q)|h_q|^2`` for numerically evaluated entries."""

    limit = len(coefficients) - 1
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] != p:
            continue
        for multiple in range(p, limit + 1, p):
            phi[multiple] -= phi[multiple] // p
    return sum(phi[q] * evaluate(coefficients[q]) ** 2 for q in range(1, limit + 1))


def optimal_adjustment_ledger(active_limit: int) -> Fraction:
    """Return the exact minimum of ``sum phi(p) w_p^2`` subject to sum w=1."""

    weights = inverse_totient_weights(active_limit)
    return sum((Fraction(p - 1) * weight * weight for p, weight in weights.items()), Fraction())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--active-limit", type=int, default=24)
    args = parser.parse_args()

    active_limit = args.active_limit
    for n in range(1, active_limit + 1):
        if null_relation(active_limit, n) != 0:
            raise AssertionError(f"null relation failed at n={n}")
        if reconstruct_gauged(active_limit, n) != expected_von_mangoldt(n):
            raise AssertionError(f"gauged reconstruction failed at n={n}")

    original = [dict(vector) for vector in finite_coefficients(2 * active_limit)]
    gauged = gauged_coefficients(active_limit)
    print(f"verified_exactly_for_1_through_{active_limit}")
    print(f"prime_cloud_size={len(inverse_totient_weights(active_limit))}")
    print(f"original_ledger={coefficient_ledger(original):.12g}")
    print(f"gauged_ledger={coefficient_ledger(gauged):.12g}")


if __name__ == "__main__":
    main()
