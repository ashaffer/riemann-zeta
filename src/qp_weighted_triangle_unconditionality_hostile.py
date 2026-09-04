"""Hostile certificates for weighted residual-block unconditionality.

The randomized weighted-triangle theorem is valid for complex
coefficients.  This module records its exact fourth-moment pairing and two
integer product-window warnings for removing the signs.

The scalable warning is the tangent grid

    a_i = m+i,
    b_j = m+2L+j,
    c_ij = m-2L-i-j,              1 <= i,j <= L.

The offsets add to zero.  Residual intervals of width ``q=2m`` are exact
level sets of ``Q(i,2L+j)=i^2+i(2L+j)+(2L+j)^2`` when ``m>48L^3``.  Every
level is a vertex matching, but flat coefficients on the ``c`` nodes turn
the all-plus weighted operator into a complete bipartite matrix.  Its
all-plus/randomized fourth-trace ratio is exactly ``L^2/(2L-1)``.

This is a full-integer tangent submask, not an actual prime-power
counterexample.  It rules out raw mask-uniform unconditionality before the
tangent/Hankel packets are peeled or merged.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt
from typing import Sequence

import numpy as np

from qp_weighted_triangle_rademacher_square import (
    exact_rademacher_fourth_average,
    schatten_fourth_power,
    validate_linear_matching_partition,
    weighted_class_matrices,
)


@dataclass(frozen=True)
class RademacherPairingLedger:
    right_square: float
    left_square: float
    transpose_pairing_real: float
    repeated_all_equal: float
    exact_average_from_pairings: float
    transpose_absolute_bound: float
    proved_upper_bound: float


def exact_rademacher_pairing_ledger(
    matrices: Sequence[np.ndarray],
) -> RademacherPairingLedger:
    r"""Expand ``E tr((X*X)^2)`` for real Rademacher signs exactly.

    For ``R=sum A_i^*A_i`` and ``L=sum A_iA_i^*``, the three pairings are

    ``tr(R^2)``, ``tr(L^2)``, and
    ``sum_ij tr((A_i^*A_j)^2)``.

    The all-equal quadruples occur in all three and must be subtracted
    twice.  For complex matrices,

    ``|tr(B^2)|<=||B||_HS^2``

    bounds the transpose pairing by ``tr(L^2)``.  Hence the safe bound is
    ``tr(R^2)+2tr(L^2)``.
    """

    if not matrices:
        return RademacherPairingLedger(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    arrays = [np.asarray(matrix, dtype=complex) for matrix in matrices]
    shape = arrays[0].shape
    if any(matrix.shape != shape for matrix in arrays):
        raise ValueError("all matrices must have one common shape")
    right = sum(
        (matrix.conj().T @ matrix for matrix in arrays),
        start=np.zeros((shape[1], shape[1]), dtype=complex),
    )
    left = sum(
        (matrix @ matrix.conj().T for matrix in arrays),
        start=np.zeros((shape[0], shape[0]), dtype=complex),
    )
    right_square = float(np.trace(right @ right).real)
    left_square = float(np.trace(left @ left).real)
    transpose = 0.0j
    transpose_absolute_bound = 0.0
    repeated = 0.0
    for first in arrays:
        self_gram = first.conj().T @ first
        repeated += float(np.trace(self_gram @ self_gram).real)
        for second in arrays:
            cross = first.conj().T @ second
            transpose += np.trace(cross @ cross)
            transpose_absolute_bound += float(np.linalg.norm(cross, "fro") ** 2)
    exact = right_square + left_square + float(transpose.real) - 2.0 * repeated
    return RademacherPairingLedger(
        right_square=right_square,
        left_square=left_square,
        transpose_pairing_real=float(transpose.real),
        repeated_all_equal=repeated,
        exact_average_from_pairings=exact,
        transpose_absolute_bound=transpose_absolute_bound,
        proved_upper_bound=right_square + 2.0 * left_square,
    )


@dataclass(frozen=True)
class CrossGramMultiplicityLedger:
    maximum_output_cell_multiplicity: int
    weighted_atomic_energy: float
    cross_gram_hilbert_schmidt_squared: float
    multiplicity_upper_bound: float


@dataclass(frozen=True)
class FactorTwoSquareLedger:
    """Exact local-mass ledger for one factor-two coefficient bin."""

    support_size: int
    maximum_hyperedge_degree: int
    coefficient_norm_squared: float
    maximum_coefficient_squared: float
    maximum_pivot_mass: float
    total_pivot_mass: float
    self_edge_energy: float
    cross_edge_energy: float
    right_square: float
    left_square: float
    refined_scale: float
    proved_square_bound: float
    proved_rademacher_bound: float


def factor_two_square_ledger(
    n: int,
    classes: Sequence[Sequence[Sequence[int]]],
    coefficients: Sequence[complex],
) -> FactorTwoSquareLedger:
    r"""Audit the diffuse-bin refinement of the weighted square theorem.

    Suppose ``z`` has ``M`` nonzero entries whose absolute values differ by
    at most a factor two, put ``s=||z||_2``, and let ``Delta`` be the maximum
    hyperedge degree.  If

    ``S_p=sum_(e contains p) sum_(u in e-p)|z_u|^2``, then linearity gives

    ``max_p S_p <= min(1,8 Delta/M)s^2`` and
    ``sum_p S_p <= 2 Delta s^2``.

    The cross-edge part of either square function is at most
    ``sum_p S_p^2``.  The self-edge identity is exactly

    ``||M_e^*M_e||_HS^2=2(sum_(u in e)|z_u|^2)^2``.

    Consequently both square functions are bounded by

    ``40 Delta min(1,Delta/M)s^4``

    and the complex Rademacher fourth moment by three times this quantity.
    Constants are deliberately explicit rather than optimized.
    """

    edges, maximum_degree = validate_linear_matching_partition(n, classes)
    z = np.asarray(coefficients, dtype=complex).reshape(-1)
    if z.size != n:
        raise ValueError("coefficients have the wrong size")
    magnitudes = np.abs(z)
    support = magnitudes[magnitudes > 0]
    support_size = int(support.size)
    if support_size and float(support.max()) > 2.0 * float(support.min()) * (
        1.0 + 1e-12
    ):
        raise ValueError("nonzero coefficient magnitudes must lie in a factor-two bin")

    norm_squared = float(np.vdot(z, z).real)
    maximum_coefficient_squared = (
        float(support.max() ** 2) if support_size else 0.0
    )
    pivot_masses = np.zeros(n, dtype=float)
    self_energy = 0.0
    incident_pivot_contributions: list[list[float]] = [[] for _ in range(n)]
    for edge in edges:
        edge_mass = float(sum(abs(z[vertex]) ** 2 for vertex in edge))
        self_energy += 2.0 * edge_mass**2
        for pivot in edge:
            pivot_mass = float(
                sum(abs(z[vertex]) ** 2 for vertex in edge if vertex != pivot)
            )
            pivot_masses[pivot] += pivot_mass
            incident_pivot_contributions[pivot].append(pivot_mass)

    cross_energy = 0.0
    for total, contributions in zip(pivot_masses, incident_pivot_contributions):
        cross_energy += float(total**2 - sum(value**2 for value in contributions))
    right_square = self_energy + cross_energy

    matrices = weighted_class_matrices(n, classes, z)
    if matrices:
        right = sum(
            (matrix.conj().T @ matrix for matrix in matrices),
            start=np.zeros((n, n), dtype=complex),
        )
        left = sum(
            (matrix @ matrix.conj().T for matrix in matrices),
            start=np.zeros((n, n), dtype=complex),
        )
        observed_right = float(np.linalg.norm(right, "fro") ** 2)
        observed_left = float(np.linalg.norm(left, "fro") ** 2)
        if not np.isclose(observed_right, right_square):
            raise AssertionError("the pivot ledger does not reconstruct the right square")
        if not np.isclose(observed_left, right_square):
            raise AssertionError("complex symmetry should give the same left square")
    else:
        observed_left = 0.0

    refined_scale = (
        maximum_degree
        * min(1.0, maximum_degree / support_size)
        * norm_squared**2
        if support_size and maximum_degree
        else 0.0
    )
    square_bound = 40.0 * refined_scale
    if right_square > square_bound + 1e-9 * max(1.0, square_bound):
        raise AssertionError("the explicit diffuse-bin square bound failed")
    return FactorTwoSquareLedger(
        support_size=support_size,
        maximum_hyperedge_degree=maximum_degree,
        coefficient_norm_squared=norm_squared,
        maximum_coefficient_squared=maximum_coefficient_squared,
        maximum_pivot_mass=float(pivot_masses.max(initial=0.0)),
        total_pivot_mass=float(pivot_masses.sum()),
        self_edge_energy=self_energy,
        cross_edge_energy=cross_energy,
        right_square=right_square,
        left_square=observed_left,
        refined_scale=refined_scale,
        proved_square_bound=square_bound,
        proved_rademacher_bound=3.0 * square_bound,
    )


def weighted_cross_gram_multiplicity_ledger(
    n: int,
    classes: Sequence[Sequence[Sequence[int]]],
    coefficients: Sequence[complex],
) -> CrossGramMultiplicityLedger:
    r"""Certify a sufficient cross-Gram Carleson multiplicity bound.

    For ``I!=J``, decompose ``A_I^*A_J`` into rank-one wedge atoms.  If
    edges ``e,f`` share ``p``, the atom has entries

    ``conj(M_e[p,u])*M_f[p,v]``, ``u in e-p``, ``v in f-p``.

    If at most ``mu`` nonzero atoms land in any output cell, entrywise
    Cauchy gives

    ``||sum_(I!=J) A_I^*A_J||_HS^2 <= mu sum_atoms ||atom||_HS^2``.

    The randomized square proof bounds the final atomic energy by
    ``2*Delta*||z||_2^4``.  Therefore ``mu=q^o(1)`` is an explicit
    sufficient packet-safe unconditionality theorem.
    """

    edges, _ = validate_linear_matching_partition(n, classes)
    del edges
    z = np.asarray(coefficients, dtype=complex).reshape(-1)
    if z.size != n:
        raise ValueError("coefficients have the wrong size")
    normalized_classes = [
        [tuple(int(vertex) for vertex in edge) for edge in matching]
        for matching in classes
    ]
    cell_counts: dict[tuple[int, int], int] = {}
    atomic_energy = 0.0
    atomic_sum = np.zeros((n, n), dtype=complex)

    def third(edge: tuple[int, int, int], first: int, second: int) -> int:
        return next(vertex for vertex in edge if vertex != first and vertex != second)

    for first_class, first_matching in enumerate(normalized_classes):
        for second_class, second_matching in enumerate(normalized_classes):
            if first_class == second_class:
                continue
            for first_edge in first_matching:
                first_vertices = set(first_edge)
                for second_edge in second_matching:
                    shared = first_vertices.intersection(second_edge)
                    if not shared:
                        continue
                    if len(shared) != 1:
                        raise AssertionError("global linearity was not retained")
                    pivot = next(iter(shared))
                    for row in first_vertices - {pivot}:
                        first_weight = z[third(first_edge, pivot, row)]
                        for column in set(second_edge) - {pivot}:
                            second_weight = z[third(second_edge, pivot, column)]
                            value = np.conjugate(first_weight) * second_weight
                            if value == 0:
                                continue
                            cell = (row, column)
                            cell_counts[cell] = cell_counts.get(cell, 0) + 1
                            atomic_sum[cell] += value
                            atomic_energy += float(abs(value) ** 2)

    matrices = weighted_class_matrices(n, classes, z)
    cross_gram = np.zeros((n, n), dtype=complex)
    for first_index, first in enumerate(matrices):
        for second_index, second in enumerate(matrices):
            if first_index != second_index:
                cross_gram += first.conj().T @ second
    if not np.allclose(cross_gram, atomic_sum):
        raise AssertionError("the wedge atoms do not reconstruct the cross Gram")
    multiplicity = max(cell_counts.values(), default=0)
    observed = float(np.linalg.norm(cross_gram, "fro") ** 2)
    return CrossGramMultiplicityLedger(
        maximum_output_cell_multiplicity=multiplicity,
        weighted_atomic_energy=atomic_energy,
        cross_gram_hilbert_schmidt_squared=observed,
        multiplicity_upper_bound=multiplicity * atomic_energy,
    )


@dataclass(frozen=True)
class TangentGridFixture:
    order: int
    centre: int
    q: int
    degree_parameter: int
    node_values: tuple[int, ...]
    classes: tuple[tuple[tuple[int, int, int], ...], ...]
    class_colours: tuple[int, ...]
    residual_by_edge: tuple[tuple[tuple[int, int, int], int], ...]
    coefficients: np.ndarray


def tangent_grid_fixture(order: int, centre: int | None = None) -> TangentGridFixture:
    """Build the exact integer tangent grid with legal width-``q`` blocks."""

    length = int(order)
    if length < 2:
        raise ValueError("order must be at least two")
    minimum_centre = 49 * length**3 + 1
    m = 100 * length**3 if centre is None else int(centre)
    if m < minimum_centre:
        raise ValueError("centre must exceed 49*order^3")
    q = 2 * m
    degree = 100 * length**2

    a_values = [m + i for i in range(1, length + 1)]
    b_values = [m + 2 * length + j for j in range(1, length + 1)]
    c_values = [m - 2 * length - total for total in range(2, 2 * length + 1)]
    values = tuple(a_values + b_values + c_values)
    c_index = {
        total: 2 * length + total - 2 for total in range(2, 2 * length + 1)
    }

    grouped: dict[int, list[tuple[int, int, int]]] = {}
    residuals: list[tuple[tuple[int, int, int], int]] = []
    for i in range(1, length + 1):
        x = i
        for j in range(1, length + 1):
            y = 2 * length + j
            edge = (i - 1, length + j - 1, c_index[i + j])
            product_value = (m + x) * (m + y) * (m - x - y)
            residual = 8 * product_value - q**3
            quadratic = x * x + x * y + y * y
            cubic = x * y * (x + y)
            if residual != -8 * m * quadratic - 8 * cubic:
                raise AssertionError("the tangent residual identity failed")
            colour = (-residual) // q
            if colour != 4 * quadratic:
                raise AssertionError("the width-q block is not the quadratic level")
            grouped.setdefault(colour, []).append(edge)
            residuals.append((edge, residual))

    colours = tuple(sorted(grouped))
    classes = tuple(tuple(grouped[colour]) for colour in colours)
    validate_linear_matching_partition(len(values), classes)

    coefficients = np.zeros(len(values), dtype=complex)
    coefficients[2 * length :] = 1.0 / sqrt(2 * length - 1)
    return TangentGridFixture(
        order=length,
        centre=m,
        q=q,
        degree_parameter=degree,
        node_values=values,
        classes=classes,
        class_colours=colours,
        residual_by_edge=tuple(residuals),
        coefficients=coefficients,
    )


@dataclass(frozen=True)
class TangentGridLedger:
    order: int
    vertices: int
    edges: int
    classes: int
    maximum_hyperedge_degree: int
    maximum_absolute_residual: int
    fine_window_radius: int
    maximum_log_shell_coordinate: float
    alternating_two_colour_rectangles: int
    all_plus_fourth_power: float
    randomized_fourth_power: float
    unconditionality_ratio: float
    exact_all_plus_formula: float
    exact_randomized_formula: float
    exact_ratio_formula: float
    ratio_as_fraction_of_sqrt_degree_parameter: float


def tangent_grid_ledger(fixture: TangentGridFixture) -> TangentGridLedger:
    """Check legality and the exact all-plus/randomized fourth moments."""

    length = fixture.order
    matrices = weighted_class_matrices(
        len(fixture.node_values), fixture.classes, fixture.coefficients
    )
    all_plus = schatten_fourth_power(
        sum(matrices, start=np.zeros_like(matrices[0]))
    )
    pairing = exact_rademacher_pairing_ledger(matrices)
    random_average = pairing.exact_average_from_pairings

    # The class colour of cell (i,j) is 4Q(i,2L+j).  Strict coordinate
    # monotonicity rules out a reversed two-colour rectangle.  Count it
    # explicitly as an executable guard.
    colour_grid = np.empty((length, length), dtype=np.int64)
    for i in range(1, length + 1):
        for j in range(1, length + 1):
            x = i
            y = 2 * length + j
            colour_grid[i - 1, j - 1] = 4 * (x * x + x * y + y * y)
    alternating = 0
    for first_row in range(length):
        for second_row in range(first_row + 1, length):
            for first_column in range(length):
                for second_column in range(first_column + 1, length):
                    if (
                        colour_grid[first_row, first_column]
                        == colour_grid[second_row, second_column]
                        and colour_grid[first_row, second_column]
                        == colour_grid[second_row, first_column]
                    ) or (
                        colour_grid[first_row, first_column]
                        == colour_grid[second_row, first_column]
                        and colour_grid[first_row, second_column]
                        == colour_grid[second_row, second_column]
                    ):
                        alternating += 1

    _, maximum_degree = validate_linear_matching_partition(
        len(fixture.node_values), fixture.classes
    )
    weight_count = 2 * length - 1
    exact_plus = 2.0 * length**4 / weight_count**2
    exact_random = 2.0 * length**2 / weight_count
    exact_ratio = length**2 / weight_count
    maximum_log = max(
        abs(log(2.0 * value / fixture.q)) for value in fixture.node_values
    )
    maximum_residual = max(abs(residual) for _, residual in fixture.residual_by_edge)
    return TangentGridLedger(
        order=length,
        vertices=len(fixture.node_values),
        edges=len(fixture.residual_by_edge),
        classes=len(fixture.classes),
        maximum_hyperedge_degree=maximum_degree,
        maximum_absolute_residual=maximum_residual,
        fine_window_radius=fixture.q * fixture.degree_parameter,
        maximum_log_shell_coordinate=maximum_log,
        alternating_two_colour_rectangles=alternating,
        all_plus_fourth_power=all_plus,
        randomized_fourth_power=random_average,
        unconditionality_ratio=all_plus / random_average,
        exact_all_plus_formula=exact_plus,
        exact_randomized_formula=exact_random,
        exact_ratio_formula=exact_ratio,
        ratio_as_fraction_of_sqrt_degree_parameter=(
            exact_ratio / sqrt(fixture.degree_parameter)
        ),
    )


@dataclass(frozen=True)
class IntegerC4Ledger:
    q: int
    degree_parameter: int
    residuals: tuple[int, int, int, int]
    block_indices: tuple[int, int, int, int]
    all_plus_fourth_power: float
    randomized_fourth_power: float
    ratio: float


def actual_integer_c4_ledger() -> IntegerC4Ledger:
    """Return a literal `q=1009` integer-shell pure weighted four-cycle."""

    q = 1009
    degree = 28
    shell_minimum = 414
    cycle_vertices = (484, 497, 463, 578)
    third_vertices = (558, 573, 459, 447)
    node_values = cycle_vertices + third_vertices
    index = {value: position for position, value in enumerate(node_values)}
    edge_values = (
        (463, 497, 558),
        (463, 484, 573),
        (459, 484, 578),
        (447, 497, 578),
    )
    classes = tuple(
        ((index[first], index[second], index[third]),)
        for first, second, third in edge_values
    )
    validate_linear_matching_partition(len(node_values), classes)
    coefficients = np.zeros(len(node_values), dtype=complex)
    coefficients[4:] = 0.5
    matrices = weighted_class_matrices(len(node_values), classes, coefficients)
    all_plus = schatten_fourth_power(sum(matrices, start=np.zeros_like(matrices[0])))
    randomized = exact_rademacher_fourth_average(matrices)
    residuals = tuple(
        int(8 * first * second * third - q**3)
        for first, second, third in edge_values
    )
    block_indices = tuple(
        (residual + q * degree) // (8 * shell_minimum) for residual in residuals
    )
    return IntegerC4Ledger(
        q=q,
        degree_parameter=degree,
        residuals=residuals,  # type: ignore[arg-type]
        block_indices=block_indices,  # type: ignore[arg-type]
        all_plus_fourth_power=all_plus,
        randomized_fourth_power=randomized,
        ratio=all_plus / randomized,
    )
