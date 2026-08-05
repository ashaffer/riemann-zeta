#!/usr/bin/env python3
"""Exact finite gates for the squarefree fugacity polynomial.

    P_N(z) = sum_{n <= N} mu(n)^2 z^omega(n),   P_N(-1) = M(N).

The script computes its integer coefficients and exact Routh--Hurwitz
principal minors.  With ``--sympy`` it also computes an exact discriminant
and exact real-root count.  This is a lightweight scout, not evidence for a
uniform stability theorem or for RH.
"""

from __future__ import annotations

import argparse
import json
import math
from typing import Sequence

from mobius_boundary_exchange import smallest_prime_factors, squarefree_factorization


def fugacity_coefficients(limit: int) -> list[int]:
    spf = smallest_prime_factors(limit)
    coefficients = [0]
    for n in range(1, limit + 1):
        factors = squarefree_factorization(n, spf)
        if factors is None:
            continue
        degree = len(factors)
        while len(coefficients) <= degree:
            coefficients.append(0)
        coefficients[degree] += 1
    return coefficients


def bareiss_determinant(matrix: Sequence[Sequence[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    a = [list(row) for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                a[i][j] = numerator // previous
        previous = pivot_value
        for i in range(k + 1, n):
            a[i][k] = 0
        for j in range(k + 1, n):
            a[k][j] = 0
    return sign * a[-1][-1]


def hurwitz_minors(coefficients: Sequence[int]) -> list[int]:
    """Principal Hurwitz minors for coefficients in ascending order."""

    descending = list(reversed(coefficients))
    degree = len(descending) - 1
    matrix = [[0] * degree for _ in range(degree)]
    for i in range(degree):
        for j in range(degree):
            coefficient_index = 2 * j - i + 1
            if 0 <= coefficient_index <= degree:
                matrix[i][j] = descending[coefficient_index]
    return [bareiss_determinant([row[:k] for row in matrix[:k]]) for k in range(1, degree + 1)]


def exact_root_data(coefficients: Sequence[int]) -> dict[str, int]:
    try:
        import sympy as sp
    except ImportError as exc:  # pragma: no cover - optional audit dependency
        raise SystemExit("--sympy requested, but sympy is not installed") from exc
    z = sp.Symbol("z")
    polynomial = sum(a * z**k for k, a in enumerate(coefficients))
    return {
        "discriminant": int(sp.discriminant(polynomial, z)),
        "real_root_count": int(sp.Poly(polynomial, z).count_roots(-sp.oo, sp.oo)),
    }


def first_nonreal_cutoff(limit: int) -> dict[str, object] | None:
    """Return the first non-real-rooted truncation through ``limit`` exactly."""

    spf = smallest_prime_factors(limit)
    coefficients = [0]
    for n in range(1, limit + 1):
        factors = squarefree_factorization(n, spf)
        if factors is None:
            continue
        degree = len(factors)
        while len(coefficients) <= degree:
            coefficients.append(0)
        coefficients[degree] += 1
        if n < 2:
            continue
        root_data = exact_root_data(coefficients)
        if root_data["real_root_count"] < len(coefficients) - 1:
            return {
                "first_nonreal_N": n,
                "coefficients_ascending": coefficients.copy(),
                **root_data,
            }
    return None


def run(limit: int, use_sympy: bool) -> dict[str, object]:
    if limit < 2:
        raise ValueError("N must be at least 2")
    coefficients = fugacity_coefficients(limit)
    mertens = sum((-1) ** k * a for k, a in enumerate(coefficients))
    squarefree_count = sum(coefficients)
    minors = hurwitz_minors(coefficients)
    ratio = abs(mertens) / squarefree_count
    result: dict[str, object] = {
        "N": limit,
        "coefficients_ascending": coefficients,
        "degree": len(coefficients) - 1,
        "P_minus_one": mertens,
        "P_plus_one": squarefree_count,
        "hurwitz_minors": minors,
        "hurwitz_gate_passes": all(value > 0 for value in minors),
        "observed_log_saving": "infinity" if ratio == 0 else -math.log(ratio),
        "rh_scale_log_saving": 0.5 * math.log(limit),
    }
    if use_sympy:
        result.update(exact_root_data(coefficients))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", nargs="*", type=int)
    parser.add_argument(
        "--sympy", action="store_true", help="add exact discriminant and real-root count"
    )
    parser.add_argument(
        "--first-nonreal",
        metavar="N",
        type=int,
        help="use exact Sturm counts to find the first failure through N",
    )
    args = parser.parse_args()
    if args.first_nonreal is not None:
        print(json.dumps(first_nonreal_cutoff(args.first_nonreal), sort_keys=True))
    limits = args.N
    if not limits and args.first_nonreal is None:
        limits = [1000, 10000, 100000]
    for limit in limits:
        print(json.dumps(run(limit, args.sympy), sort_keys=True))


if __name__ == "__main__":
    main()
