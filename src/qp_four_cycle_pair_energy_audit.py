"""Exact algebra for the QP completion-pair energy gate.

The routines in this module are finite, integer identities.  They do not
assert the missing weighted completion-pair estimate or the four-cycle
bound.
"""

from __future__ import annotations

from dataclasses import dataclass


ColorMatrix = tuple[int, int, int, int]
Completion = tuple[int, int, int, int]
EnergyMatrix = tuple[int, int, int, int]


@dataclass(frozen=True)
class PairIdentityLedger:
    """All exact secant identities for two carrier completions."""

    first_level: int
    second_level: int
    energy: EnergyMatrix
    energy_linear_form: int
    energy_determinant: int
    row_cross_determinant: int
    column_cross_determinant: int
    first_cross_level: int
    second_cross_level: int
    lagrange_defect: int
    elimination_defect: int


@dataclass(frozen=True)
class CommonModulusLedger:
    """Exact shift/product identities based at ``c11`` and ``c22``."""

    color_determinant: int
    level: int
    u1: int
    u2: int
    v1: int
    v2: int
    top_left_product: int
    bottom_right_product: int
    first_product_defect: int
    second_product_defect: int
    common_modulus_defect: int


@dataclass(frozen=True)
class ProjectionCountermodelLedger:
    """Degree/fibre counts in the linear-hypergraph projection model."""

    degree_cap: int
    shared_endpoint_pairs: int
    bottom_color_pairs: int
    maximum_node_degree: int
    completion_multiplicity: int
    top_projection_square_fibre: int


@dataclass(frozen=True)
class FixedEnergyNormLedger:
    """Exact binary-norm reduction for one nonzero completion secant."""

    color_determinant: int
    energy_determinant: int
    level: int
    norm_rhs: int
    color_energy_trace: int
    energy_involution_trace: int
    mixed_trace: int
    color_energy_square_defect: EnergyMatrix
    energy_involution_square_defect: EnergyMatrix
    anticommutator_defect: EnergyMatrix
    norm_square_defect: EnergyMatrix


def _determinant(values: EnergyMatrix | ColorMatrix) -> int:
    return values[0] * values[3] - values[1] * values[2]


def _product_matrix(completion: Completion) -> EnergyMatrix:
    a1, a2, b1, b2 = completion
    return (a1 * b1, a1 * b2, a2 * b1, a2 * b2)


def _matrix_product(
    left: EnergyMatrix, right: EnergyMatrix
) -> EnergyMatrix:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def _matrix_add(
    left: EnergyMatrix, right: EnergyMatrix
) -> EnergyMatrix:
    return tuple(x + y for x, y in zip(left, right))  # type: ignore[return-value]


def _matrix_scale(scale: int, matrix: EnergyMatrix) -> EnergyMatrix:
    return tuple(scale * value for value in matrix)  # type: ignore[return-value]


def _matrix_transpose(matrix: EnergyMatrix) -> EnergyMatrix:
    return (matrix[0], matrix[2], matrix[1], matrix[3])


def _adjugate(matrix: EnergyMatrix) -> EnergyMatrix:
    return (matrix[3], -matrix[1], -matrix[2], matrix[0])


def _level(colors: ColorMatrix, completion: Completion) -> int:
    c11, c12, c21, c22 = colors
    m11, m12, m21, m22 = _product_matrix(completion)
    return c11 * m11 + c22 * m22 - c12 * m12 - c21 * m21


def pair_identity_ledger(
    colors: ColorMatrix, first: Completion, second: Completion
) -> PairIdentityLedger:
    """Return the exact pair identities, with zero defects when valid.

    The elimination defect equals ``a1*b1*(L-L')``.  In particular it is
    zero for two completions on the same pinned residual level.
    """

    c11, c12, c21, c22 = colors
    a1, a2, b1, b2 = first
    A1, A2, B1, B2 = second
    first_products = _product_matrix(first)
    second_products = _product_matrix(second)
    energy = tuple(
        left - right
        for left, right in zip(first_products, second_products)
    )
    e11, e12, e21, e22 = energy
    first_level = _level(colors, first)
    second_level = _level(colors, second)
    energy_linear_form = (
        c11 * e11 + c22 * e22 - c12 * e12 - c21 * e21
    )
    row_cross = a1 * A2 - a2 * A1
    column_cross = b1 * B2 - b2 * B1
    first_cross_level = (
        c11 * a1 * B1
        - c12 * a1 * B2
        - c21 * a2 * B1
        + c22 * a2 * B2
    )
    second_cross_level = (
        c11 * A1 * b1
        - c12 * A1 * b2
        - c21 * A2 * b1
        + c22 * A2 * b2
    )
    lagrange_defect = (
        first_level * second_level
        - first_cross_level * second_cross_level
        - _determinant(colors) * row_cross * column_cross
    )
    u2 = b1 * c21 - b2 * c22
    v2 = a1 * c12 - a2 * c22
    elimination_left = (
        e11 * first_level
        + row_cross * B1 * u2
        + column_cross * A1 * v2
        - c22 * row_cross * column_cross
    )
    elimination_defect = elimination_left - a1 * b1 * (
        first_level - second_level
    )
    return PairIdentityLedger(
        first_level=first_level,
        second_level=second_level,
        energy=energy,  # type: ignore[arg-type]
        energy_linear_form=energy_linear_form,
        energy_determinant=_determinant(energy),  # type: ignore[arg-type]
        row_cross_determinant=row_cross,
        column_cross_determinant=column_cross,
        first_cross_level=first_cross_level,
        second_cross_level=second_cross_level,
        lagrange_defect=lagrange_defect,
        elimination_defect=elimination_defect,
    )


def common_modulus_ledger(
    colors: ColorMatrix, completion: Completion
) -> CommonModulusLedger:
    """Return the two exact shift-product identities.

    With ``m=c11``, the advertised modular relation

    ``u1*v1 == c12*c21*(a2*b2) (mod m)``

    is the reduction of the stronger equality

    ``u1*v1 = m*L-k*(a2*b2)``.
    """

    c11, c12, c21, c22 = colors
    a1, a2, b1, b2 = completion
    determinant = _determinant(colors)
    level = _level(colors, completion)
    u1 = b1 * c11 - b2 * c12
    u2 = b1 * c21 - b2 * c22
    v1 = a1 * c11 - a2 * c21
    v2 = a1 * c12 - a2 * c22
    top_left_product = a1 * b1
    bottom_right_product = a2 * b2
    first_product_defect = (
        u1 * v1 - (c11 * level - determinant * bottom_right_product)
    )
    second_product_defect = (
        u2 * v2 - (c22 * level - determinant * top_left_product)
    )
    common_modulus_defect = (
        u1 * v1 - c12 * c21 * bottom_right_product
    ) % c11
    return CommonModulusLedger(
        color_determinant=determinant,
        level=level,
        u1=u1,
        u2=u2,
        v1=v1,
        v2=v2,
        top_left_product=top_left_product,
        bottom_right_product=bottom_right_product,
        first_product_defect=first_product_defect,
        second_product_defect=second_product_defect,
        common_modulus_defect=common_modulus_defect,
    )


def fixed_energy_norm_ledger(
    colors: ColorMatrix, first: Completion, second: Completion
) -> FixedEnergyNormLedger:
    """Verify the exact quadratic-order normalization of a fixed secant.

    Put ``M=M(first)``, ``E=M-M(second)``, ``Delta=det(E)`` and use the
    signed color matrix ``K``.  For equal levels define

    ``A=E*K^T``, ``T=2*M*adj(E)-Delta*I``,
    ``U=A*T-L*Delta*I``.

    Then ``A`` and ``T`` are traceless,

    ``A^2=-k*Delta*I``, ``T^2=Delta^2*I``,
    ``A*U+U*A=0``, and
    ``U^2=Delta^2*(L^2+k*Delta)*I``.

    The returned defect matrices are zero when the hypotheses hold.
    """

    c11, c12, c21, c22 = colors
    color_matrix: EnergyMatrix = (c11, -c12, -c21, c22)
    first_matrix = _product_matrix(first)
    second_matrix = _product_matrix(second)
    energy: EnergyMatrix = tuple(
        left - right
        for left, right in zip(first_matrix, second_matrix)
    )  # type: ignore[assignment]
    determinant = _determinant(energy)
    color_determinant = _determinant(color_matrix)
    level = _level(colors, first)
    identity: EnergyMatrix = (1, 0, 0, 1)
    color_energy = _matrix_product(
        energy, _matrix_transpose(color_matrix)
    )
    involution = _matrix_add(
        _matrix_scale(
            2, _matrix_product(first_matrix, _adjugate(energy))
        ),
        _matrix_scale(-determinant, identity),
    )
    mixed = _matrix_product(color_energy, involution)
    norm_matrix = _matrix_add(
        mixed, _matrix_scale(-level * determinant, identity)
    )
    norm_rhs = level * level + color_determinant * determinant
    return FixedEnergyNormLedger(
        color_determinant=color_determinant,
        energy_determinant=determinant,
        level=level,
        norm_rhs=norm_rhs,
        color_energy_trace=color_energy[0] + color_energy[3],
        energy_involution_trace=involution[0] + involution[3],
        mixed_trace=mixed[0] + mixed[3],
        color_energy_square_defect=_matrix_add(
            _matrix_product(color_energy, color_energy),
            _matrix_scale(color_determinant * determinant, identity),
        ),
        energy_involution_square_defect=_matrix_add(
            _matrix_product(involution, involution),
            _matrix_scale(-determinant * determinant, identity),
        ),
        anticommutator_defect=_matrix_add(
            _matrix_product(color_energy, norm_matrix),
            _matrix_product(norm_matrix, color_energy),
        ),
        norm_square_defect=_matrix_add(
            _matrix_product(norm_matrix, norm_matrix),
            _matrix_scale(-determinant * determinant * norm_rhs, identity),
        ),
    )


def color_energy_factorization(
    colors: ColorMatrix, energy: EnergyMatrix
) -> tuple[int, int]:
    """Return both sides of the pivoted color/energy factorization.

    If ``L_C(E)=0``, the returned integers agree:

    ``(e22*c12-e21*c11)(e22*c21-e12*c11)``
    ``= -det(E)*c11**2-e22**2*det(C)``.
    """

    c11, c12, c21, _ = colors
    _, e12, e21, e22 = energy
    left = (e22 * c12 - e21 * c11) * (
        e22 * c21 - e12 * c11
    )
    right = -_determinant(energy) * c11 * c11 - e22 * e22 * _determinant(
        colors
    )
    return left, right


def projection_countermodel_ledger(
    degree_cap: int,
) -> ProjectionCountermodelLedger:
    """Return the exact fibre counts in a linear 3-graph countermodel.

    Take ``r=degree_cap-1`` disjoint endpoint pairs.  One top color pair and
    each of ``r`` bottom color pairs support all ``r`` endpoint pairs.  The
    required centers are distinct for every endpoint/color-pair incidence.
    The resulting unordered 3-graph is linear, and every node has degree at
    most ``degree_cap``.  Nevertheless the top ``m^2`` projection fibre is
    ``r^3``.
    """

    if degree_cap < 2:
        raise ValueError("the degree cap must be at least two")
    shared = degree_cap - 1
    return ProjectionCountermodelLedger(
        degree_cap=degree_cap,
        shared_endpoint_pairs=shared,
        bottom_color_pairs=shared,
        maximum_node_degree=degree_cap,
        completion_multiplicity=shared,
        top_projection_square_fibre=shared**3,
    )


def off_diagonal_bootstrap_bound(
    weighted_color_mass: float, weighted_off_diagonal_pairs: float
) -> float:
    """Solve ``S^2 <= W*(S+P)`` for its nonnegative root."""

    if weighted_color_mass < 0 or weighted_off_diagonal_pairs < 0:
        raise ValueError("weighted masses must be nonnegative")
    W = weighted_color_mass
    P = weighted_off_diagonal_pairs
    return 0.5 * (W + (W * W + 4.0 * W * P) ** 0.5)
