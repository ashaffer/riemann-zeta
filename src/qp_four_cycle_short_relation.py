"""Exact algebra for the QP short color-relation decomposition.

This module replays the two factorizations used in the fixed-relation
square-root theorem.  It does not implement or assert the analytic operator
bound itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


Matrix2 = tuple[int, int, int, int]
Pair = tuple[int, int]


def determinant(matrix: Matrix2) -> int:
    """Return a row-major two-by-two determinant."""

    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def color_relation(relation: Matrix2, colors: Matrix2) -> int:
    """Return ``e11*c11+e22*c22-e12*c12-e21*c21``."""

    e11, e12, e21, e22 = relation
    c11, c12, c21, c22 = colors
    return e11 * c11 + e22 * c22 - e12 * c12 - e21 * c21


@dataclass(frozen=True)
class InvertibleFiberLedger:
    """The bilinear determinant and its completed product identity."""

    colors: Matrix2
    relation_value: int
    color_determinant: int
    mixed_coefficient: int
    polynomial_determinant: int
    completed_product_left: int
    completed_product_right: int


def invertible_fiber_ledger(
    relation: Matrix2,
    left_base: Pair,
    right_base: Pair,
    left_parameter: int,
    right_parameter: int,
) -> InvertibleFiberLedger:
    """Replay the product completion on one common linear fibre.

    The two bases must have the same relation level.  Directions are the
    primitive kernel directions of the corresponding row of ``relation``.
    """

    e11, e12, e21, e22 = relation
    g1 = gcd(e11, e12)
    g2 = gcd(e21, e22)
    if not g1 or not g2:
        raise ValueError("both coefficient rows must be nonzero")
    if determinant(relation) == 0:
        raise ValueError("the relation must be invertible")
    if e11 * left_base[0] - e12 * left_base[1] != (
        e21 * right_base[0] - e22 * right_base[1]
    ):
        raise ValueError("the bases are on different fibres")

    p = (e12 // g1, e11 // g1)
    q = (e22 // g2, e21 // g2)
    s = left_parameter
    t = right_parameter
    left = (left_base[0] + s * p[0], left_base[1] + s * p[1])
    right = (right_base[0] + t * q[0], right_base[1] + t * q[1])
    colors = (left[0], left[1], right[0], right[1])

    def det_pair(first: Pair, second: Pair) -> int:
        return first[0] * second[1] - first[1] * second[0]

    c = det_pair(p, q)
    a = det_pair(p, right_base)
    b = det_pair(left_base, q)
    d = det_pair(left_base, right_base)
    polynomial = c * s * t + a * s + b * t + d
    completed_left = (c * s + b) * (c * t + a)
    completed_right = c * polynomial + (a * b - c * d)
    return InvertibleFiberLedger(
        colors=colors,
        relation_value=color_relation(relation, colors),
        color_determinant=determinant(colors),
        mixed_coefficient=c,
        polynomial_determinant=polynomial,
        completed_product_left=completed_left,
        completed_product_right=completed_right,
    )


@dataclass(frozen=True)
class RankOneFiberLedger:
    """The exact ``det C=h*ell`` tangent factorization."""

    colors: Matrix2
    relation: Matrix2
    relation_value: int
    color_determinant: int
    second_factor: int
    factored_determinant: int
    first_vertical_level: int
    second_vertical_level: int


def rank_one_fiber_ledger(
    row_factor: Pair,
    column_factor: Pair,
    bezout_pair: Pair,
    level: int,
    first_parameter: int,
    second_parameter: int,
) -> RankOneFiberLedger:
    """Build the colors in the rank-one parametrization and audit it."""

    r1, r2 = row_factor
    s1, s2 = column_factor
    u0, v0 = bezout_pair
    if s1 * u0 - s2 * v0 != 1:
        raise ValueError("bezout_pair must satisfy s1*u0-s2*v0=1")
    h = level
    p = first_parameter
    q = second_parameter
    x = r2 * h * u0 + p * s2
    y = r2 * h * v0 + p * s1
    z = r1 * h * u0 + q * s2
    w = r1 * h * v0 + q * s1
    colors = (x, y, z, w)
    relation = (r1 * s1, r1 * s2, r2 * s1, r2 * s2)
    ell = r2 * q - r1 * p
    return RankOneFiberLedger(
        colors=colors,
        relation=relation,
        relation_value=color_relation(relation, colors),
        color_determinant=determinant(colors),
        second_factor=ell,
        factored_determinant=h * ell,
        first_vertical_level=r1 * x - r2 * z,
        second_vertical_level=r1 * y - r2 * w,
    )
