"""Exact algebra for the balanced broad incidence-fibration audit.

The functions here verify identities used in the accompanying report.  They
do not prove the sharp four-cycle estimate.  In particular, the explicit
twisted-cubic family is an integer/algebraic obstruction and is not asserted
to satisfy the project prime-power shell or the four product windows.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Iterable, Sequence


Vector2 = tuple[int, int]
Vector4 = tuple[int, int, int, int]


def determinant2(matrix: Sequence[int]) -> int:
    """Return the determinant of a row-major two-by-two matrix."""

    if len(matrix) != 4:
        raise ValueError("a two-by-two matrix needs four entries")
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def carrier_product(row: Vector2, column: Vector2) -> Vector4:
    """Return the row-major rank-one matrix ``row * column^T``."""

    return (
        row[0] * column[0],
        row[0] * column[1],
        row[1] * column[0],
        row[1] * column[1],
    )


def signed_color_level(colors: Vector4, product: Vector4) -> int:
    """Return ``c11*p11-c12*p12-c21*p21+c22*p22``."""

    return (
        colors[0] * product[0]
        - colors[1] * product[1]
        - colors[2] * product[2]
        + colors[3] * product[3]
    )


def completion_residuals(
    cubic_center: int, colors: Vector4, product: Vector4
) -> Vector4:
    """Return ``r_ij=8*c_ij*p_ij-cubic_center`` in row-major order."""

    return tuple(
        8 * color * entry - cubic_center
        for color, entry in zip(colors, product, strict=True)
    )  # type: ignore[return-value]


def alternating_residual_sum(residuals: Vector4) -> int:
    """Return the additive rectangular invariant of four residuals."""

    return residuals[0] - residuals[1] - residuals[2] + residuals[3]


def residual_cross_ratio(cubic_center: int, residuals: Vector4) -> Fraction:
    """Return the multiplicative rectangular invariant.

    The denominator is positive in the physical product window.  A generic
    nonzero check is retained here so the finite algebra can also be used
    outside that window.
    """

    shifted = tuple(cubic_center + value for value in residuals)
    denominator = shifted[1] * shifted[2]
    if denominator == 0:
        raise ZeroDivisionError("the off-diagonal shifted residual vanishes")
    return Fraction(shifted[0] * shifted[3], denominator)


def color_cross_ratio(colors: Vector4) -> Fraction:
    """Return ``c11*c22/(c12*c21)``."""

    denominator = colors[1] * colors[2]
    if denominator == 0:
        raise ZeroDivisionError("off-diagonal colors must be nonzero")
    return Fraction(colors[0] * colors[3], denominator)


def residual_fiber_identity(
    cubic_center: int, colors: Vector4, row: Vector2, column: Vector2
) -> tuple[int, Fraction]:
    """Return the two residual invariants of one exact completion.

    For a rank-one carrier product the output is exactly

    ``(8*signed_color_level(colors, P), color_cross_ratio(colors))``.
    """

    product = carrier_product(row, column)
    residuals = completion_residuals(cubic_center, colors, product)
    return (
        alternating_residual_sum(residuals),
        residual_cross_ratio(cubic_center, residuals),
    )


def same_color_secant_determinant(
    first: Vector4, second: Vector4
) -> int:
    """Return ``det(first-second)`` for two product matrices."""

    return determinant2(tuple(x - y for x, y in zip(first, second, strict=True)))


def _signed_color_matrix(colors: Vector4) -> tuple[tuple[int, int], tuple[int, int]]:
    return ((colors[0], -colors[1]), (-colors[2], colors[3]))


def _adjugate2(
    matrix: tuple[tuple[int, int], tuple[int, int]]
) -> tuple[tuple[int, int], tuple[int, int]]:
    return ((matrix[1][1], -matrix[0][1]), (-matrix[1][0], matrix[0][0]))


def _matrix_vector(
    matrix: tuple[tuple[int, int], tuple[int, int]], vector: Vector2
) -> Vector2:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def broad_twisted_cubic(
    colors: Vector4, constant: int, parameters: Iterable[int]
) -> tuple[Vector4, ...]:
    """Construct a ruling-free nonplanar family on one completion surface.

    Let ``K=((c11,-c12),(-c21,c22))`` and ``k=det(K)``.  For a parameter
    ``t`` put

    ``u_t=(1,t)``, ``y_t=(constant-t^2,t)``,
    ``v_t=adj(K)y_t``, and ``P_t=u_t v_t^T``.

    Then ``det(P_t)=0`` and ``<C,P_t>=k*constant``.  If all parameters are
    positive and their squares are smaller than ``constant``, both carrier
    vectors are positive for a positive color tuple.  Distinct parameters
    have invertible secants when ``k != 0``.
    """

    matrix = _signed_color_matrix(colors)
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        raise ValueError("the signed color matrix must be invertible")
    adjugate = _adjugate2(matrix)
    products: list[Vector4] = []
    for parameter in parameters:
        row = (1, parameter)
        auxiliary = (constant - parameter * parameter, parameter)
        column = _matrix_vector(adjugate, auxiliary)
        products.append(carrier_product(row, column))
    return tuple(products)


def affine_rank(points: Sequence[Vector4]) -> int:
    """Return the rational affine rank of a finite set of four-vectors."""

    if not points:
        return 0
    base = points[0]
    rows = [
        [Fraction(point[index] - base[index]) for index in range(4)]
        for point in points[1:]
    ]
    rank = 0
    column = 0
    while rank < len(rows) and column < 4:
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]), None
        )
        if pivot is None:
            column += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [entry / pivot_value for entry in rows[rank]]
        for row in range(len(rows)):
            if row == rank or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                rows[row][entry] - factor * rows[rank][entry]
                for entry in range(4)
            ]
        rank += 1
        column += 1
    return rank


def every_four_affinely_independent(points: Sequence[Vector4]) -> bool:
    """Test the plane-peeling obstruction on all four-point subsets."""

    return all(affine_rank(list(subset)) == 3 for subset in combinations(points, 4))


@dataclass(frozen=True)
class BalancedIncidenceFibrationLedger:
    total_color_exponent: Fraction
    slice_cap_exponent: Fraction
    trivial_incidence_exponent: Fraction
    target_incidence_exponent: Fraction
    mandatory_linear_term_exponent: Fraction
    missing_saving_exponent: Fraction
    endpoint_color_interval_exponent: Fraction


def balanced_incidence_fibration_ledger() -> BalancedIncidenceFibrationLedger:
    """Return the exact powers of ``D`` in the balanced broad endpoint."""

    total_colors = Fraction(73, 16)
    slice_cap = Fraction(5, 16)
    trivial = total_colors + slice_cap
    target = Fraction(76, 16)
    q_exponent = Fraction(33, 16)
    return BalancedIncidenceFibrationLedger(
        total_color_exponent=total_colors,
        slice_cap_exponent=slice_cap,
        trivial_incidence_exponent=trivial,
        target_incidence_exponent=target,
        mandatory_linear_term_exponent=trivial,
        missing_saving_exponent=trivial - target,
        endpoint_color_interval_exponent=1 - q_exponent,
    )
