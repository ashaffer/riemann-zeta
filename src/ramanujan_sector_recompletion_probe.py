#!/usr/bin/env python3
"""Exact checks for the R83 Ramanujan-sector recompletion.

The probe isolates two finite algebra facts used by the analytic report:

* the square matrix ``(c_q(n))_{1 <= n,q <= Y}`` has determinant ``Y!``;
  hence a complete-block null gauge that changes the constant block must use
  a modulus larger than the active range;
* the determinant-zero singular-series fluctuation has uniformly bounded
  interval sums, with the exact elementary majorant
  ``sum_q |h_q|^2 sigma(q)``.

All arithmetic is integral or rational.  The program is a certificate for
the finite identities, not a numerical estimate for zeta zeros.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction

from finite_ramanujan_completion_probe import mobius_sieve, ramanujan_sum


Matrix = list[list[int]]


def matrix_product(left: Matrix, right: Matrix) -> Matrix:
    """Multiply two integer matrices."""

    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible nonempty matrices")
    columns = len(right[0])
    return [
        [
            sum(left[row][inner] * right[inner][column] for inner in range(len(right)))
            for column in range(columns)
        ]
        for row in range(len(left))
    ]


def ramanujan_matrix(limit: int) -> Matrix:
    """Return ``C[n-1][q-1] = c_q(n)`` for ``1 <= n,q <= limit``."""

    if limit < 1:
        raise ValueError("limit must be positive")
    mobius = mobius_sieve(limit)
    return [
        [ramanujan_sum(q, n, mobius) for q in range(1, limit + 1)]
        for n in range(1, limit + 1)
    ]


def divisor_factor_matrices(limit: int) -> tuple[Matrix, Matrix]:
    """Return the triangular factors ``C=A B`` of the Ramanujan matrix.

    ``A[n,d]=1_(d|n)`` is lower triangular with unit diagonal, while
    ``B[d,q]=d mu(q/d) 1_(d|q)`` is upper triangular with diagonal ``q``.
    Indices in the returned Python matrices are shifted down by one.
    """

    if limit < 1:
        raise ValueError("limit must be positive")
    mobius = mobius_sieve(limit)
    incidence: Matrix = []
    transform: Matrix = []
    for n in range(1, limit + 1):
        incidence.append([int(n % d == 0) for d in range(1, limit + 1)])
    for d in range(1, limit + 1):
        transform.append(
            [d * mobius[q // d] if q % d == 0 else 0 for q in range(1, limit + 1)]
        )
    return incidence, transform


def determinant_certificate(limit: int) -> int:
    """Return the determinant certified by the triangular factorization."""

    if limit < 1:
        raise ValueError("limit must be positive")
    return math.factorial(limit)


def divisor_sum(value: int) -> int:
    """Return ``sigma(value)``."""

    if value < 1:
        raise ValueError("value must be positive")
    return sum(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def interval_ramanujan_sum(q: int, start: int, length: int) -> int:
    """Return ``sum_{start < h <= start+length} c_q(h)`` exactly."""

    if q < 1 or start < 0 or length < 0:
        raise ValueError("require q >= 1, start >= 0, and length >= 0")
    mobius = mobius_sieve(q)
    return sum(
        ramanujan_sum(q, h, mobius)
        for h in range(start + 1, start + length + 1)
    )


def singular_series_interval_sum(
    coefficients: list[Fraction],
    start: int,
    length: int,
) -> Fraction:
    """Return an interval sum of ``R(h)=sum_{q>=2}|h_q|^2 c_q(h)``."""

    if len(coefficients) < 2:
        raise ValueError("coefficients must include indices zero and one")
    result = Fraction()
    for q in range(2, len(coefficients)):
        result += coefficients[q] * coefficients[q] * interval_ramanujan_sum(
            q, start, length
        )
    return result


def singular_series_interval_majorant(coefficients: list[Fraction]) -> Fraction:
    """Return ``sum_{q>=2}|h_q|^2 sigma(q)``."""

    if len(coefficients) < 2:
        raise ValueError("coefficients must include indices zero and one")
    return sum(
        (
            coefficients[q]
            * coefficients[q]
            * Fraction(divisor_sum(q))
            for q in range(2, len(coefficients))
        ),
        Fraction(),
    )


def mean_ramanujan_correlation(q: int, r: int, shift: int) -> Fraction:
    """Average ``c_q(n+shift)c_r(n)`` over one common period."""

    if q < 1 or r < 1 or shift < 0:
        raise ValueError("q,r must be positive and shift nonnegative")
    period = math.lcm(q, r)
    mobius = mobius_sieve(max(q, r))
    total = sum(
        ramanujan_sum(q, n + shift, mobius)
        * ramanujan_sum(r, n, mobius)
        for n in range(1, period + 1)
    )
    return Fraction(total, period)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=12)
    args = parser.parse_args()

    incidence, transform = divisor_factor_matrices(args.limit)
    if matrix_product(incidence, transform) != ramanujan_matrix(args.limit):
        raise AssertionError("Ramanujan matrix factorization failed")

    for q in range(2, args.limit + 1):
        for start in range(args.limit + 1):
            for length in range(args.limit + 1):
                if abs(interval_ramanujan_sum(q, start, length)) > divisor_sum(q):
                    raise AssertionError("interval majorant failed")

    print(f"verified_limit={args.limit}")
    print(f"ramanujan_matrix_determinant={determinant_certificate(args.limit)}")


if __name__ == "__main__":
    main()
