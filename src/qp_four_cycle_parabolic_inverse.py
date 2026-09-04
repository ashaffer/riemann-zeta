"""Exact quadratic-at-infinity invariant for affine rank-one plane sections."""

from __future__ import annotations

from dataclasses import dataclass


Matrix2 = tuple[int, int, int, int]


def _det(matrix: Matrix2) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


@dataclass(frozen=True)
class PlaneSectionInfinityLedger:
    first_square_coefficient: int
    mixed_coefficient: int
    second_square_coefficient: int
    infinity_discriminant: int
    is_parabolic: bool


def plane_section_infinity_ledger(
    first_direction: Matrix2,
    second_direction: Matrix2,
) -> PlaneSectionInfinityLedger:
    """Return the homogeneous determinant conic on a rational plane."""

    v = first_direction
    w = second_direction
    first = _det(v)
    second = _det(w)
    mixed = v[0] * w[3] + w[0] * v[3] - v[1] * w[2] - w[1] * v[2]
    discriminant = mixed * mixed - 4 * first * second
    return PlaneSectionInfinityLedger(
        first_square_coefficient=first,
        mixed_coefficient=mixed,
        second_square_coefficient=second,
        infinity_discriminant=discriminant,
        is_parabolic=(discriminant == 0),
    )


def translation_grid_plane_directions(
    row_base: tuple[int, int],
    column_base: tuple[int, int],
) -> tuple[Matrix2, Matrix2]:
    """Return the linear and quadratic product-matrix directions in ``t``."""

    a1, a2 = row_base
    b1, b2 = column_base
    linear = (b1 - a1, b2 - a1, b1 - a2, b2 - a2)
    quadratic = (-1, -1, -1, -1)
    return linear, quadratic

