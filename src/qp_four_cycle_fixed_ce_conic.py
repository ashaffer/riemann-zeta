"""Exact fixed-``(C,E)`` conic invariants for QP four-cycles.

The functions in this module are finite integer algebra.  They support the
nonparabolic-conic argument in
``ZETA23-QP-FOUR-CYCLE-FIXED-CE-NONPARABOLIC-CONIC-THEOREM-2026-08-15.md``;
they make no asymptotic claim by themselves.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


Matrix2 = tuple[int, int, int, int]


def determinant(matrix: Sequence[int]) -> int:
    """Return the determinant of a row-major two-by-two matrix."""

    if len(matrix) != 4:
        raise ValueError("a two-by-two matrix needs four entries")
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def multiply(left: Sequence[int], right: Sequence[int]) -> Matrix2:
    """Multiply two row-major two-by-two matrices."""

    if len(left) != 4 or len(right) != 4:
        raise ValueError("two two-by-two matrices are required")
    a, b, c, d = left
    e, f, g, h = right
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def adjugate(matrix: Sequence[int]) -> Matrix2:
    """Return the row-major adjugate."""

    if len(matrix) != 4:
        raise ValueError("a two-by-two matrix needs four entries")
    a, b, c, d = matrix
    return (d, -b, -c, a)


def color_form(colors: Sequence[int]) -> Matrix2:
    """Return ``K=(c11,-c12;-c21,c22)`` from oriented colors."""

    if len(colors) != 4:
        raise ValueError("four oriented colors are required")
    c11, c12, c21, c22 = colors
    return (c11, -c12, -c21, c22)


def coefficient_pairing(left: Sequence[int], right: Sequence[int]) -> int:
    """Return the entrywise coefficient pairing."""

    if len(left) != 4 or len(right) != 4:
        raise ValueError("two two-by-two matrices are required")
    return sum(a * b for a, b in zip(left, right))


@dataclass(frozen=True)
class FixedCEConicInvariants:
    """Integer invariants of a fixed color/difference/product triple."""

    color_determinant: int
    energy_determinant: int
    common_level: int
    color_energy_pairing: int
    a_trace: int
    a_determinant: int
    alpha: int
    beta: int
    gamma: int
    x0: int
    y0: int
    z0: int
    idempotent_quadric_left: int
    idempotent_quadric_right: int
    level_plane_left: int
    level_plane_right: int
    infinity_discriminant: int
    full_degeneracy_parameter: int


def fixed_ce_conic_invariants(
    colors: Sequence[int], energy: Sequence[int], product: Sequence[int]
) -> FixedCEConicInvariants:
    """Return and verify the canonical fixed-``(C,E)`` conic data.

    ``product`` should be a rank-one matrix ``M`` and ``product-energy``
    should also be rank one.  The returned identities remain meaningful
    without those hypotheses, but the two displayed quadric sides agree
    precisely in the pair-completion situation.
    """

    if len(energy) != 4 or len(product) != 4:
        raise ValueError("energy and product must be two-by-two matrices")
    k_matrix = color_form(colors)
    delta = determinant(energy)
    level = coefficient_pairing(k_matrix, product)
    pairing = coefficient_pairing(k_matrix, energy)

    # A=K^T E.
    k_transpose = (k_matrix[0], k_matrix[2], k_matrix[1], k_matrix[3])
    a_matrix = multiply(k_transpose, energy)
    alpha, beta, gamma, bottom_right = a_matrix

    # T=adj(E)M=Delta R.  Pair completions have tr(T)=Delta.
    t_matrix = multiply(adjugate(energy), product)
    x0 = t_matrix[0] - t_matrix[3]
    y0 = t_matrix[1]
    z0 = t_matrix[2]

    color_det = determinant(k_matrix)
    infinity_discriminant = 16 * (alpha * alpha + beta * gamma)
    return FixedCEConicInvariants(
        color_determinant=color_det,
        energy_determinant=delta,
        common_level=level,
        color_energy_pairing=pairing,
        a_trace=alpha + bottom_right,
        a_determinant=determinant(a_matrix),
        alpha=alpha,
        beta=beta,
        gamma=gamma,
        x0=x0,
        y0=y0,
        z0=z0,
        idempotent_quadric_left=x0 * x0 + 4 * y0 * z0,
        idempotent_quadric_right=delta * delta,
        level_plane_left=alpha * x0 + gamma * y0 + beta * z0,
        level_plane_right=level * delta,
        infinity_discriminant=infinity_discriminant,
        full_degeneracy_parameter=level * level + color_det * delta,
    )


def beta_norm_identity(invariants: FixedCEConicInvariants) -> tuple[int, int]:
    """Return both sides of the completed-square norm identity.

    This is the ``beta != 0`` chart.  Equality follows from the two
    canonical conic equations.
    """

    beta = invariants.beta
    if beta == 0:
        raise ValueError("the beta chart is singular; swap the off-diagonal chart")
    alpha = invariants.alpha
    x0 = invariants.x0
    y0 = invariants.y0
    delta_energy = invariants.energy_determinant
    level = invariants.common_level
    k = invariants.color_determinant

    quadratic_discriminant = -16 * k * delta_energy
    u1 = 2 * beta * x0 - 4 * alpha * y0
    linear_term = -16 * beta * level * delta_energy
    v1 = 2 * quadratic_discriminant * y0 + linear_term
    left = v1 * v1 - 4 * quadratic_discriminant * u1 * u1
    right = (
        256
        * beta
        * beta
        * delta_energy
        * delta_energy
        * invariants.full_degeneracy_parameter
    )
    return left, right
