"""Exact checks for the anchor-GCD reciprocal-height theorem."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd
from typing import Iterable, Sequence


Vector2 = tuple[int, int]


def det2(x: Vector2, y: Vector2) -> int:
    return x[0] * y[1] - x[1] * y[0]


def cross3(x: Sequence[int], y: Sequence[int]) -> tuple[int, int, int]:
    if len(x) != 3 or len(y) != 3:
        raise ValueError("cross3 requires two three-vectors")
    return (
        x[1] * y[2] - x[2] * y[1],
        x[2] * y[0] - x[0] * y[2],
        x[0] * y[1] - x[1] * y[0],
    )


def content(values: Iterable[int]) -> int:
    answer = 0
    for value in values:
        answer = gcd(answer, abs(int(value)))
    return answer


def primitive_height(rows: Sequence[Vector2]) -> int:
    if len(rows) != 3:
        raise ValueError("exactly three rows are required")
    aa = tuple(row[0] for row in rows)
    bb = tuple(row[1] for row in rows)
    raw = cross3(aa, bb)
    common = content(raw)
    if common == 0:
        raise ValueError("the row triple has rank less than two")
    return max(abs(value) for value in raw) // common


def reciprocal_height_sum(rows: Sequence[Vector2]) -> Fraction:
    total = Fraction(0)
    for triple in combinations(rows, 3):
        total += Fraction(1, primitive_height(triple))
    return total


def anchored_normalized_gcd_majorant(rows: Sequence[Vector2]) -> Fraction:
    """The sum of the anchored upper bound in (2.4), divided by three."""

    total = Fraction(0)
    for anchor_index, anchor in enumerate(rows):
        determinants = [
            abs(det2(anchor, row))
            for index, row in enumerate(rows)
            if index != anchor_index
        ]
        if any(value == 0 for value in determinants):
            raise ValueError("all row pairs must be nonparallel")
        for first, second in combinations(determinants, 2):
            total += Fraction(gcd(first, second), max(first, second))
    return total / 3


def defect_cross_identity(
    rows: Sequence[Vector2],
    gamma: Vector2,
    partner: Vector2,
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    """Return both sides of e cross f = -det(gamma,partner)*(a cross A)."""

    if len(rows) != 3:
        raise ValueError("exactly three rows are required")
    c, d = gamma
    cp, dp = partner
    aa = tuple(row[0] for row in rows)
    bb = tuple(row[1] for row in rows)
    ee = tuple(c * a - d * b for a, b in rows)
    ff = tuple(cp * a - dp * b for a, b in rows)
    left = cross3(ee, ff)
    k = det2(gamma, partner)
    right = tuple(-k * value for value in cross3(aa, bb))
    return left, right


def core_tail_exponent(
    multiplicity_exponent: Fraction,
    core_excess_exponent: Fraction,
) -> Fraction:
    """Completed trace exponent 1+2*mu from M=K*D^mu."""

    del multiplicity_exponent  # It cancels after multiplying the high tail by K.
    return Fraction(1) + 2 * core_excess_exponent


def low_determinant_factorial_bound(D: int, K: int) -> tuple[int, int]:
    """Return (partner cap, second-factorial scale) for |k|<=D/K."""

    if D <= 0 or K <= 0:
        raise ValueError("D and K must be positive")
    partner_cap = 2 * (D // K)
    # binom(m,2) < 2*K^2 when m<2K.
    return partner_cap, 2 * partner_cap * K * K


def quotient_coordinates(
    vector: Vector2, anchor: Vector2, complement: Vector2
) -> tuple[int, int]:
    """Return (m,e) in vector=m*anchor-e*complement.

    The caller must supply ``det(anchor, complement)=1``.
    """

    if det2(anchor, complement) != 1:
        raise ValueError("the complement must have determinant one")
    m = det2(vector, complement)
    e = det2(vector, anchor)
    if vector != (
        m * anchor[0] - e * complement[0],
        m * anchor[1] - e * complement[1],
    ):
        raise AssertionError("unimodular reconstruction failed")
    return m, e


def quotient_defect_identity(
    row: Vector2,
    anchor: Vector2,
    partner: Vector2,
    complement: Vector2,
) -> tuple[int, int]:
    """Return det(row,partner) and e*n-m*k from (6.4)."""

    m, e = quotient_coordinates(row, anchor, complement)
    n = det2(partner, complement)
    k = -det2(anchor, partner)
    return det2(row, partner), e * n - m * k
