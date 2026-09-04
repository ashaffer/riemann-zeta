"""Exact weighted-additive color normal form for a parabolic completion chart."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class ParabolicColorNormalForm:
    color_determinant: int
    row_direction_gcd: int
    column_direction_gcd: int
    first_normalized_gap: int
    second_normalized_gap: int
    weighted_additive_defect: int
    determinant_gap_defect: int


def parabolic_color_normal_form(
    colors: tuple[int, int, int, int],
    row_direction: tuple[int, int],
    column_direction: tuple[int, int],
) -> ParabolicColorNormalForm:
    """Return the exact rational-additive color coordinates.

    The quadratic common-level coefficient must vanish:

    ``r1*s1*c11-r1*s2*c12-r2*s1*c21+r2*s2*c22=0``.

    All four direction coordinates are required to be nonzero; a power-size
    actual chart cannot have a stationary carrier coordinate by product
    spacing.
    """

    c11, c12, c21, c22 = colors
    r1, r2 = row_direction
    s1, s2 = column_direction
    if 0 in (r1, r2, s1, s2):
        raise ValueError("the nontrivial chart directions must be nonzero")
    gr = gcd(abs(r1), abs(r2))
    gs = gcd(abs(s1), abs(s2))
    rho1, rho2 = r1 // gr, r2 // gr
    sigma1, sigma2 = s1 // gs, s2 // gs
    weighted_defect = (
        r1 * s1 * c11
        - r1 * s2 * c12
        - r2 * s1 * c21
        + r2 * s2 * c22
    )
    if weighted_defect:
        raise ValueError("the quadratic common-level coefficient is nonzero")

    first_row_gap = s1 * c11 - s2 * c12
    second_row_gap = s1 * c21 - s2 * c22
    if first_row_gap % rho2 or second_row_gap % rho1:
        raise AssertionError("coprime row directions did not divide the gaps")
    first_gap = first_row_gap // rho2
    if second_row_gap // rho1 != first_gap:
        raise AssertionError("the two row-normalized gaps differ")

    first_column_gap = r1 * c11 - r2 * c21
    second_column_gap = r1 * c12 - r2 * c22
    if first_column_gap % sigma2 or second_column_gap % sigma1:
        raise AssertionError("coprime column directions did not divide the gaps")
    second_gap = first_column_gap // sigma2
    if second_column_gap // sigma1 != second_gap:
        raise AssertionError("the two column-normalized gaps differ")

    determinant = c11 * c22 - c12 * c21
    determinant_gap_defect = (
        first_gap * second_gap + determinant * gr * gs
    )
    if determinant_gap_defect:
        raise AssertionError("the normalized determinant-gap identity failed")
    return ParabolicColorNormalForm(
        color_determinant=determinant,
        row_direction_gcd=gr,
        column_direction_gcd=gs,
        first_normalized_gap=first_gap,
        second_normalized_gap=second_gap,
        weighted_additive_defect=weighted_defect,
        determinant_gap_defect=determinant_gap_defect,
    )

