"""Exact odd-prime recentering of the QP tangent alias.

This module records an integer-shell obstruction, not an actual-prime-power
counterexample.  It is useful for separating the direct four-cycle mass
from the stronger pair-of-completions energy.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


ROW_SLOPE = 1728
COLOR_SLOPE = 1331
MODULUS = 3168
RESIDUE = 2591


@dataclass(frozen=True)
class RecenteredAlias:
    q: int
    row_center: int
    color_anchor: int
    base_residual: int
    slope_defect: int


def recentered_alias(q: int) -> RecenteredAlias:
    """Return the exact rational recentering for ``q == 2591 (mod 3168)``.

    The identities are

    ``8*A**2*C = q**3 -(3*q-1)//4`` and
    ``1728*C-1331*A = 1089``.
    """

    if q % MODULUS != RESIDUE:
        raise ValueError("q must be congruent to 2591 modulo 3168")
    if q % 2 == 0:
        raise ValueError("q must be odd")
    a = 3 * (2 * q - 1) // 11
    c = 121 * (q + 1) // 288
    if 11 * a != 3 * (2 * q - 1):
        raise AssertionError("row center is not integral")
    if 288 * c != 121 * (q + 1):
        raise AssertionError("color anchor is not integral")
    base_residual = 8 * a * a * c - q**3
    slope_defect = ROW_SLOPE * c - COLOR_SLOPE * a
    return RecenteredAlias(
        q=q,
        row_center=a,
        color_anchor=c,
        base_residual=base_residual,
        slope_defect=slope_defect,
    )


def alias_entry(
    alias: RecenteredAlias,
    row_step: int,
    column_step: int,
    translation: int,
    row_index: int,
    column_index: int,
) -> tuple[int, int, int]:
    """Return one ``(row, carrier, color)`` entry of the tangent grid."""

    if row_index not in (0, 1) or column_index not in (0, 1):
        raise ValueError("indices must be zero or one")
    u = row_index * row_step
    v = column_index * column_step
    return (
        alias.row_center + ROW_SLOPE * u + translation,
        alias.row_center + ROW_SLOPE * v - translation,
        alias.color_anchor - COLOR_SLOPE * (u + v),
    )


def product_increment(
    alias: RecenteredAlias,
    u: int,
    v: int,
    translation: int,
) -> int:
    """Return ``abc-A**2*C`` by the exact defect-aware formula."""

    a = alias.row_center
    c = alias.color_anchor
    r = ROW_SLOPE
    s = COLOR_SLOPE
    total = u + v
    quadratic = r * r * u * v + r * (v - u) * translation - translation**2
    return (
        a * alias.slope_defect * total
        + c * quadratic
        - a * r * s * total**2
        - s * total * quadratic
    )


def displayed_mass_scales(length: int, fan_length: int) -> tuple[float, float]:
    """Return displayed and pair-completion scales for the spiked vector.

    There are ``fan_length**2`` color matrices, ``length`` translations per
    matrix, and ``3*fan_length+1`` non-anchor colors.  The anchor has squared
    mass ``1/4`` and the other colors share squared mass ``3/4``.  The first
    output counts only the deliberately displayed fixed-color rectangles;
    the merged Hankel patch also has cross-level rectangles.
    """

    if length < 2 or fan_length < 2:
        raise ValueError("both lengths must be at least two")
    nonanchor = 3 * fan_length + 1
    color_product = 3.0**1.5 / (16.0 * nonanchor**1.5)
    patches = fan_length * (fan_length - 1)
    displayed = patches * length * color_product
    pair_energy = patches * length * (length - 1) * color_product
    return displayed, pair_energy


def exact_anchor_is_not_a_prime_power(alias: RecenteredAlias) -> bool:
    """Certify the simple prime-power obstruction for the exact anchor.

    Along the progression, ``C=11**2*k`` and ``k`` is not divisible by 11.
    Hence ``C`` has at least two distinct prime divisors.
    """

    c = alias.color_anchor
    if c % 121:
        raise AssertionError("the exact anchor lost its factor 11^2")
    quotient = c // 121
    return quotient > 1 and gcd(quotient, 11) == 1
