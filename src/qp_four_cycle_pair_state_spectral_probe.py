"""Finite pair-state/Schatten diagnostics for the QP four-cycle core.

This module implements the exact finite representation

``B_z = sum_c |z_c| (A_c tensor A_c)``,

where ``A_c`` is the (weighted) partial-permutation matrix of triples of
color ``c``.  Zero pair states are compressed, but the returned matrix has
the same nonzero singular values as the full ``n^2``-by-``n^2`` tensor.

For a real triple kernel, expansion of the fourth Schatten trace gives

``||B_z||_S4^4 = sum_C |sum_{X in Comp(C)} rho(X)|^2 prod_ij |z_cij|``.

Here directed completions include repeated rows and columns.  Consequently
the full Schatten trace is *not* the unresolved nondegenerate pair energy:
the diagonal and degenerate completion pairs must be separated.  The
functions below perform that separation exactly on a supplied finite core.

The module also profiles singular vectors on pair states.  For an edge from
``(x1,x2)`` to ``(y1,y2)`` it records the tangent shift

``h = x1*y1 - x2*y2``

and the Smith invariants of ``((x1,x2),(y2,y1))``.  The same convention
applies directly to the existing row-pair/color-pair incidence matrix.

All asymptotic conclusions remain open.  These routines are exact finite
algebra plus explicitly labelled floating-point eigensolver diagnostics.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import math
from typing import Mapping, Sequence

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import svds

from qp_four_cycle_hostile_lab import FourCycleCore


PairCode = int
ColorMatrix = tuple[int, int, int, int]
Completion = tuple[int, int, int, int]


@dataclass(frozen=True)
class ColorPartialPermutation:
    """One weighted color slice and its exact support degrees."""

    color_index: int
    matrix: csr_matrix
    entries: int
    maximum_row_support: int
    maximum_column_support: int


@dataclass(frozen=True)
class PairStateTransfer:
    """A compressed block of ``sum_c |z_c| A_c tensor A_c``.

    ``row_pair_codes`` and ``column_pair_codes`` use row-major pair codes
    ``first*n+second`` in the original node space.  The supported sectors
    are ``raw``, ``diagonal``, ``symmetric_offdiagonal``, and
    ``antisymmetric_offdiagonal``.
    """

    dimension: int
    sector: str
    row_pair_codes: np.ndarray
    column_pair_codes: np.ndarray
    matrix: csr_matrix


@dataclass(frozen=True)
class CompletionTerm:
    """One directed completed two-by-two grid."""

    completion: Completion
    amplitude: float


@dataclass(frozen=True)
class SchattenIdentityLedger:
    """The two independently assembled sides of the finite S4 identity."""

    pair_states_left: int
    pair_states_right: int
    tensor_entries: int
    directed_completions: int
    color_matrices: int
    transfer_fourth_mass: float
    completion_square_mass: float
    absolute_error: float


@dataclass(frozen=True)
class SmithMass:
    """Ordered-pair count and positive mass in one Smith class."""

    first_invariant: int
    second_invariant: int
    ordered_pairs: int
    mass: float


@dataclass(frozen=True)
class CompletionPairClassification:
    """Positive fourth-mass decomposition by completion/secant type."""

    total_mass: float
    pair_diagonal_mass: float
    degenerate_offdiagonal_mass: float
    genuine_offdiagonal_mass: float
    rank_one_secant_mass: float
    additive_tangent_mass: float
    near_square_tangent_mass: float
    ordered_pairs: int
    genuine_offdiagonal_pairs: int
    rank_one_secant_pairs: int
    additive_tangent_pairs: int
    near_square_tangent_pairs: int
    smith_masses: tuple[SmithMass, ...]


@dataclass(frozen=True)
class SingularTriplets:
    """Largest singular values/vectors of a finite compressed transfer."""

    singular_values: np.ndarray
    left_vectors: np.ndarray
    right_vectors: np.ndarray


@dataclass(frozen=True)
class SignGaugeLedger:
    """Certificate data for ``T = diag(r) S diag(c)`` with real signs."""

    equivalent: bool
    support_edges: int
    nontrivial_components: int
    conflicting_edges: int
    maximum_ratio_error: float


@dataclass(frozen=True)
class SmithInfluence:
    """Normalized absolute mode influence in one edge Smith class."""

    first_invariant: int
    second_invariant: int
    edge_count: int
    influence_fraction: float


@dataclass(frozen=True)
class PairStateModeProfile:
    """Localization, swap parity, tangent, and Smith data for one mode."""

    singular_value: float
    left_diagonal_mass: float
    right_diagonal_mass: float
    left_swap_expectation: float
    right_swap_expectation: float
    left_participation: float
    right_participation: float
    effective_influential_edges: float
    principal_tangent_influence_fraction: float
    threshold_tangent_influence_fraction: float
    weighted_mean_absolute_shift: float
    weighted_median_absolute_shift: int
    weighted_ninetieth_absolute_shift: int
    maximum_influence_absolute_shift: int
    smith_influences: tuple[SmithInfluence, ...]
    unreported_smith_influence_fraction: float


@dataclass(frozen=True)
class ActualPrimePowerSpectralLedger:
    """Compact reproducible output of the actual-prime-power probe."""

    q: int
    nodes: int
    triples: int
    live_colors: int
    degree_scale: float
    tensor_entries: int
    directed_completions: int
    color_matrices: int
    identity_error: float
    full_fourth_mass: float
    pair_diagonal_mass: float
    degenerate_offdiagonal_mass: float
    genuine_offdiagonal_mass: float
    genuine_offdiagonal_fraction: float
    genuine_offdiagonal_pairs: int
    secant_smith_classes: int
    rank_one_secant_pairs: int
    additive_tangent_pairs: int
    near_square_tangent_pairs: int
    diagonal_sector_fourth_mass: float
    symmetric_sector_fourth_mass: float
    antisymmetric_sector_fourth_mass: float
    diagonal_sector_top_singular: float
    symmetric_sector_top_singular: float
    antisymmetric_sector_top_singular: float
    exterior_sign_gauge_equivalent: bool
    exterior_sign_gauge_components: int
    incidence_edges: int
    incidence_top_singular: float
    incidence_mode_median_shift: int
    incidence_mode_ninetieth_shift: int
    incidence_mode_degree_window_fraction: float
    incidence_mode_dominant_smith_first: int
    incidence_mode_dominant_smith_second: int
    incidence_mode_dominant_smith_fraction: float


def _validate_core(core: FourCycleCore) -> None:
    size = len(core.rows)
    if not (len(core.columns) == len(core.colors) == len(core.weights) == size):
        raise ValueError("the core edge arrays must have equal length")
    n = core.dimension
    for name, array in (
        ("row", core.rows),
        ("column", core.columns),
        ("color", core.colors),
    ):
        if np.any(array < 0) or np.any(array >= n):
            raise ValueError(f"a {name} index lies outside the core")

    cells: set[tuple[int, int]] = set()
    color_rows: set[tuple[int, int]] = set()
    color_columns: set[tuple[int, int]] = set()
    for row, column, color in zip(core.rows, core.columns, core.colors):
        cell = (int(row), int(column))
        if cell in cells:
            raise ValueError("the triple core has two colors in one cell")
        cells.add(cell)
        row_key = (int(color), int(row))
        column_key = (int(color), int(column))
        if row_key in color_rows or column_key in color_columns:
            raise ValueError("a color slice is not a partial permutation")
        color_rows.add(row_key)
        color_columns.add(column_key)


def _absolute_color_weights(
    dimension: int,
    color_weights: Mapping[int, complex] | Sequence[complex] | None,
) -> np.ndarray:
    if color_weights is None:
        return np.ones(dimension, dtype=float)
    if isinstance(color_weights, Mapping):
        answer = np.zeros(dimension, dtype=float)
        for raw_index, value in color_weights.items():
            index = int(raw_index)
            if not 0 <= index < dimension:
                raise ValueError("a color weight index lies outside the core")
            answer[index] = abs(complex(value))
        return answer
    raw = np.asarray(color_weights)
    if raw.shape != (dimension,):
        raise ValueError("the color weight vector has the wrong dimension")
    return np.abs(raw.astype(complex)).real


def build_color_partial_permutations(
    core: FourCycleCore, *, kernel_weights: bool = True
) -> dict[int, ColorPartialPermutation]:
    """Construct every nonempty ``A_c`` and certify partial-permutation support."""

    _validate_core(core)
    n = core.dimension
    by_color: dict[int, list[int]] = defaultdict(list)
    for edge_index, color in enumerate(core.colors):
        by_color[int(color)].append(edge_index)

    answer: dict[int, ColorPartialPermutation] = {}
    for color, edge_indices in sorted(by_color.items()):
        indices = np.asarray(edge_indices, dtype=np.int64)
        rows = core.rows[indices].astype(np.int64, copy=False)
        columns = core.columns[indices].astype(np.int64, copy=False)
        data = (
            np.asarray(core.weights[indices])
            if kernel_weights
            else np.ones(indices.size, dtype=np.int64)
        )
        matrix = coo_matrix((data, (rows, columns)), shape=(n, n)).tocsr()
        matrix.sum_duplicates()
        row_support = matrix.getnnz(axis=1)
        column_support = matrix.getnnz(axis=0)
        maximum_row = int(row_support.max(initial=0))
        maximum_column = int(column_support.max(initial=0))
        if maximum_row > 1 or maximum_column > 1 or matrix.nnz != indices.size:
            raise AssertionError("validated color support ceased to be a matching")
        answer[color] = ColorPartialPermutation(
            color_index=color,
            matrix=matrix,
            entries=int(indices.size),
            maximum_row_support=maximum_row,
            maximum_column_support=maximum_column,
        )
    return answer


def _compressed_sparse_matrix(
    raw_rows: Sequence[int] | np.ndarray,
    raw_columns: Sequence[int] | np.ndarray,
    raw_data: Sequence[complex] | np.ndarray,
) -> tuple[np.ndarray, np.ndarray, csr_matrix]:
    rows = np.asarray(raw_rows, dtype=np.int64)
    columns = np.asarray(raw_columns, dtype=np.int64)
    data = np.asarray(raw_data)
    if not (rows.size == columns.size == data.size):
        raise ValueError("sparse coordinate arrays must have equal length")
    if rows.size == 0:
        return (
            np.empty(0, dtype=np.int64),
            np.empty(0, dtype=np.int64),
            csr_matrix((0, 0), dtype=data.dtype if data.size else float),
        )
    row_codes, row_indices = np.unique(rows, return_inverse=True)
    column_codes, column_indices = np.unique(columns, return_inverse=True)
    matrix = coo_matrix(
        (data, (row_indices, column_indices)),
        shape=(row_codes.size, column_codes.size),
    ).tocsr()
    matrix.sum_duplicates()
    matrix.eliminate_zeros()
    return row_codes, column_codes, matrix


def build_diagonal_tensor_transfer(
    core: FourCycleCore,
    color_weights: Mapping[int, complex] | Sequence[complex] | None = None,
    *,
    kernel_weights: bool = True,
    sector: str = "raw",
) -> PairStateTransfer:
    """Build a compressed diagonal-color tensor transfer.

    The symmetric and antisymmetric blocks use normalized pair bases.  A
    single unordered pair of color-``c`` edges contributes ``w_i*w_j`` to
    the symmetric block and the orientation sign times that value to the
    antisymmetric block; the two ordered tensor edges supply the factors of
    two which cancel the basis normalizations.
    """

    _validate_core(core)
    valid_sectors = {
        "raw",
        "diagonal",
        "symmetric_offdiagonal",
        "antisymmetric_offdiagonal",
    }
    if sector not in valid_sectors:
        raise ValueError(f"unknown tensor sector {sector!r}")
    n = core.dimension
    z = _absolute_color_weights(n, color_weights)
    by_color: dict[int, list[int]] = defaultdict(list)
    for edge_index, color in enumerate(core.colors):
        if z[int(color)] != 0.0:
            by_color[int(color)].append(edge_index)

    row_chunks: list[np.ndarray] = []
    column_chunks: list[np.ndarray] = []
    data_chunks: list[np.ndarray] = []
    for color, raw_edge_indices in by_color.items():
        edge_indices = np.asarray(raw_edge_indices, dtype=np.int64)
        rows = core.rows[edge_indices].astype(np.int64, copy=False)
        columns = core.columns[edge_indices].astype(np.int64, copy=False)
        weights = (
            np.asarray(core.weights[edge_indices])
            if kernel_weights
            else np.ones(edge_indices.size, dtype=np.int64)
        )
        color_weight = z[color]
        degree = edge_indices.size

        if sector == "raw":
            first = np.repeat(np.arange(degree), degree)
            second = np.tile(np.arange(degree), degree)
            row_chunks.append(rows[first] * n + rows[second])
            column_chunks.append(columns[first] * n + columns[second])
            data_chunks.append(color_weight * weights[first] * weights[second])
            continue

        if sector == "diagonal":
            row_chunks.append(rows * n + rows)
            column_chunks.append(columns * n + columns)
            data_chunks.append(color_weight * weights * weights)
            continue

        first, second = np.triu_indices(degree, k=1)
        if first.size == 0:
            continue
        first_rows = rows[first]
        second_rows = rows[second]
        first_columns = columns[first]
        second_columns = columns[second]
        if np.any(first_rows == second_rows) or np.any(
            first_columns == second_columns
        ):
            raise AssertionError("a color matching produced a repeated pair state")
        row_chunks.append(
            np.minimum(first_rows, second_rows) * n
            + np.maximum(first_rows, second_rows)
        )
        column_chunks.append(
            np.minimum(first_columns, second_columns) * n
            + np.maximum(first_columns, second_columns)
        )
        data = color_weight * weights[first] * weights[second]
        if sector == "antisymmetric_offdiagonal":
            row_sign = np.where(first_rows < second_rows, 1, -1)
            column_sign = np.where(first_columns < second_columns, 1, -1)
            data = data * row_sign * column_sign
        data_chunks.append(data)

    if row_chunks:
        raw_rows = np.concatenate(row_chunks)
        raw_columns = np.concatenate(column_chunks)
        raw_data = np.concatenate(data_chunks)
    else:
        raw_rows = np.empty(0, dtype=np.int64)
        raw_columns = np.empty(0, dtype=np.int64)
        raw_data = np.empty(0, dtype=float)
    row_codes, column_codes, matrix = _compressed_sparse_matrix(
        raw_rows, raw_columns, raw_data
    )
    return PairStateTransfer(
        dimension=n,
        sector=sector,
        row_pair_codes=row_codes,
        column_pair_codes=column_codes,
        matrix=matrix,
    )


def schatten_fourth_mass(matrix: csr_matrix) -> complex | float | int:
    """Return ``tr((B* B)^2)`` by an exact sparse Gram product when possible."""

    gram = (matrix.getH() @ matrix).tocsr()
    value = gram.multiply(gram.conjugate()).sum()
    if hasattr(value, "item"):
        value = value.item()
    if isinstance(value, complex) and abs(value.imag) <= 1.0e-13 * max(
        1.0, abs(value.real)
    ):
        return value.real
    return value


def directed_completion_groups(
    core: FourCycleCore,
    *,
    kernel_weights: bool = True,
    include_degenerate: bool = True,
) -> dict[ColorMatrix, tuple[CompletionTerm, ...]]:
    """Enumerate directed completions independently of the tensor builder."""

    _validate_core(core)
    if kernel_weights and not np.isrealobj(core.weights):
        raise ValueError("the completion-square identity here requires a real kernel")
    n = core.dimension
    rows: list[dict[int, tuple[int, float]]] = [dict() for _ in range(n)]
    for row, column, color, raw_weight in zip(
        core.rows, core.columns, core.colors, core.weights
    ):
        weight = float(raw_weight) if kernel_weights else 1.0
        rows[int(row)][int(column)] = (int(color), weight)

    groups: dict[ColorMatrix, list[CompletionTerm]] = defaultdict(list)
    for first_row in range(n):
        for second_row in range(n):
            if not include_degenerate and first_row == second_row:
                continue
            common_columns = sorted(rows[first_row].keys() & rows[second_row].keys())
            for first_column in common_columns:
                c11, w11 = rows[first_row][first_column]
                c21, w21 = rows[second_row][first_column]
                for second_column in common_columns:
                    if not include_degenerate and first_column == second_column:
                        continue
                    c12, w12 = rows[first_row][second_column]
                    c22, w22 = rows[second_row][second_column]
                    groups[c11, c12, c21, c22].append(
                        CompletionTerm(
                            completion=(
                                first_row,
                                second_row,
                                first_column,
                                second_column,
                            ),
                            amplitude=w11 * w12 * w21 * w22,
                        )
                    )
    return {
        colors: tuple(completions) for colors, completions in groups.items()
    }


def completion_square_mass(
    groups: Mapping[ColorMatrix, Sequence[CompletionTerm]],
    color_weights: Mapping[int, complex] | Sequence[complex] | None,
    *,
    dimension: int,
) -> float:
    """Evaluate the completion side of the real-kernel S4 identity."""

    z = _absolute_color_weights(dimension, color_weights)
    answer = 0.0
    for colors, completions in groups.items():
        color_product = math.prod(float(z[color]) for color in colors)
        amplitude = sum(float(term.amplitude) for term in completions)
        answer += amplitude * amplitude * color_product
    return answer


def schatten_identity_ledger(
    core: FourCycleCore,
    color_weights: Mapping[int, complex] | Sequence[complex] | None = None,
    *,
    kernel_weights: bool = True,
) -> SchattenIdentityLedger:
    """Build both sides independently and report their finite discrepancy."""

    transfer = build_diagonal_tensor_transfer(
        core,
        color_weights,
        kernel_weights=kernel_weights,
        sector="raw",
    )
    groups = directed_completion_groups(
        core, kernel_weights=kernel_weights, include_degenerate=True
    )
    transfer_mass = float(schatten_fourth_mass(transfer.matrix).real)
    completion_mass = completion_square_mass(
        groups, color_weights, dimension=core.dimension
    )
    return SchattenIdentityLedger(
        pair_states_left=transfer.matrix.shape[0],
        pair_states_right=transfer.matrix.shape[1],
        tensor_entries=transfer.matrix.nnz,
        directed_completions=sum(len(terms) for terms in groups.values()),
        color_matrices=len(groups),
        transfer_fourth_mass=transfer_mass,
        completion_square_mass=completion_mass,
        absolute_error=abs(transfer_mass - completion_mass),
    )


def _product_matrix(values: Sequence[int]) -> tuple[int, int, int, int]:
    a1, a2, b1, b2 = (int(value) for value in values)
    return (a1 * b1, a1 * b2, a2 * b1, a2 * b2)


def completion_pair_classification(
    core: FourCycleCore,
    groups: Mapping[ColorMatrix, Sequence[CompletionTerm]],
    color_weights: Mapping[int, complex] | Sequence[complex] | None,
    *,
    tangent_radius: int | None = None,
) -> CompletionPairClassification:
    """Decompose positive completion-square mass by secant geometry.

    The supplied completion amplitudes must be nonnegative.  Smith
    invariants refer to the two-by-two energy secant
    ``M(X)-M(X')``.  ``additive_tangent`` means exactly
    ``X-X'=(t,t,-t,-t)``.  A near-square pair has both carrier quadruples of
    diameter at most ``tangent_radius``.
    """

    z = _absolute_color_weights(core.dimension, color_weights)
    diagonal_mass = 0.0
    degenerate_mass = 0.0
    genuine_mass = 0.0
    rank_one_mass = 0.0
    additive_mass = 0.0
    near_square_mass = 0.0
    ordered_pairs = 0
    genuine_pairs = 0
    rank_one_pairs = 0
    additive_pairs = 0
    near_square_pairs = 0
    smith_counts: dict[tuple[int, int], int] = defaultdict(int)
    smith_masses: dict[tuple[int, int], float] = defaultdict(float)

    node_values = [int(value) for value in core.values]
    for colors, raw_terms in groups.items():
        terms = tuple(raw_terms)
        if any(term.amplitude < 0 for term in terms):
            raise ValueError("positive mass classification requires nonnegative kernel")
        color_product = math.prod(float(z[color]) for color in colors)
        value_completions = [
            tuple(node_values[index] for index in term.completion) for term in terms
        ]
        products = [_product_matrix(completion) for completion in value_completions]
        for first_index, first in enumerate(terms):
            first_values = value_completions[first_index]
            for second_index, second in enumerate(terms):
                ordered_pairs += 1
                mass = float(first.amplitude * second.amplitude * color_product)
                if first_index == second_index:
                    diagonal_mass += mass
                    continue
                second_values = value_completions[second_index]
                if (
                    first.completion[0] == first.completion[1]
                    or first.completion[2] == first.completion[3]
                    or second.completion[0] == second.completion[1]
                    or second.completion[2] == second.completion[3]
                ):
                    degenerate_mass += mass
                    continue

                genuine_pairs += 1
                genuine_mass += mass
                energy = tuple(
                    left - right
                    for left, right in zip(products[first_index], products[second_index])
                )
                determinant = energy[0] * energy[3] - energy[1] * energy[2]
                first_invariant = math.gcd(*(abs(value) for value in energy))
                second_invariant = (
                    abs(determinant) // first_invariant if first_invariant else 0
                )
                smith_key = (first_invariant, second_invariant)
                smith_counts[smith_key] += 1
                smith_masses[smith_key] += mass
                if determinant == 0:
                    rank_one_pairs += 1
                    rank_one_mass += mass

                difference = tuple(
                    left - right for left, right in zip(first_values, second_values)
                )
                if (
                    difference[0] == difference[1]
                    and difference[0] == -difference[2]
                    and difference[0] == -difference[3]
                ):
                    additive_pairs += 1
                    additive_mass += mass
                if tangent_radius is not None and (
                    max(first_values) - min(first_values) <= tangent_radius
                    and max(second_values) - min(second_values) <= tangent_radius
                ):
                    near_square_pairs += 1
                    near_square_mass += mass

    smith = tuple(
        SmithMass(
            first_invariant=key[0],
            second_invariant=key[1],
            ordered_pairs=smith_counts[key],
            mass=smith_masses[key],
        )
        for key in sorted(smith_counts)
    )
    total = diagonal_mass + degenerate_mass + genuine_mass
    return CompletionPairClassification(
        total_mass=total,
        pair_diagonal_mass=diagonal_mass,
        degenerate_offdiagonal_mass=degenerate_mass,
        genuine_offdiagonal_mass=genuine_mass,
        rank_one_secant_mass=rank_one_mass,
        additive_tangent_mass=additive_mass,
        near_square_tangent_mass=near_square_mass,
        ordered_pairs=ordered_pairs,
        genuine_offdiagonal_pairs=genuine_pairs,
        rank_one_secant_pairs=rank_one_pairs,
        additive_tangent_pairs=additive_pairs,
        near_square_tangent_pairs=near_square_pairs,
        smith_masses=smith,
    )


def largest_singular_triplets(
    matrix: csr_matrix,
    *,
    rank: int = 6,
    tolerance: float = 1.0e-11,
    maximum_iterations: int = 100_000,
) -> SingularTriplets:
    """Compute a deterministic finite leading singular subspace."""

    if rank <= 0:
        raise ValueError("rank must be positive")
    minimum_dimension = min(matrix.shape, default=0)
    if minimum_dimension == 0 or matrix.nnz == 0:
        return SingularTriplets(
            singular_values=np.empty(0),
            left_vectors=np.empty((matrix.shape[0], 0)),
            right_vectors=np.empty((matrix.shape[1], 0)),
        )
    requested = min(rank, minimum_dimension)
    if requested == minimum_dimension or minimum_dimension <= 32:
        left, singular_values, right_adjoint = np.linalg.svd(
            matrix.toarray(), full_matrices=False
        )
        return SingularTriplets(
            singular_values=singular_values[:requested],
            left_vectors=left[:, :requested],
            right_vectors=right_adjoint[:requested].conjugate().T,
        )

    left, singular_values, right_adjoint = svds(
        matrix,
        k=requested,
        which="LM",
        tol=tolerance,
        maxiter=maximum_iterations,
        random_state=0,
    )
    order = np.argsort(-singular_values)
    return SingularTriplets(
        singular_values=singular_values[order],
        left_vectors=left[:, order],
        right_vectors=right_adjoint[order].conjugate().T,
    )


def sign_gauge_ledger(
    first: csr_matrix,
    second: csr_matrix,
    *,
    tolerance: float = 1.0e-12,
) -> SignGaugeLedger:
    """Test real diagonal-sign equivalence of two sparse transfers.

    Equal support and edgewise ratios in ``{+1,-1}`` are necessary.  A
    bipartite traversal then checks whether those edge signs are a row sign
    times a column sign.  When the ledger is equivalent the two matrices
    have exactly the same singular spectrum (up to the stated numerical
    ratio tolerance for floating input).
    """

    if first.shape != second.shape:
        return SignGaugeLedger(False, 0, 0, 1, math.inf)
    left = first.tocoo()
    right = second.tocoo()
    left_entries = {
        (int(row), int(column)): complex(value)
        for row, column, value in zip(left.row, left.col, left.data)
        if value != 0
    }
    right_entries = {
        (int(row), int(column)): complex(value)
        for row, column, value in zip(right.row, right.col, right.data)
        if value != 0
    }
    if left_entries.keys() != right_entries.keys():
        symmetric_difference = len(left_entries.keys() ^ right_entries.keys())
        return SignGaugeLedger(
            False,
            len(left_entries.keys() & right_entries.keys()),
            0,
            symmetric_difference,
            math.inf,
        )

    row_adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(first.shape[0])
    ]
    column_adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(first.shape[1])
    ]
    conflicting = 0
    maximum_error = 0.0
    for (row, column), value in left_entries.items():
        ratio = right_entries[row, column] / value
        sign = 1 if ratio.real >= 0 else -1
        error = abs(ratio - sign)
        maximum_error = max(maximum_error, float(error))
        if error > tolerance:
            conflicting += 1
        row_adjacency[row].append((column, sign))
        column_adjacency[column].append((row, sign))

    row_signs = np.zeros(first.shape[0], dtype=np.int8)
    column_signs = np.zeros(first.shape[1], dtype=np.int8)
    components = 0
    for seed, neighbors in enumerate(row_adjacency):
        if row_signs[seed] or not neighbors:
            continue
        components += 1
        row_signs[seed] = 1
        stack: list[tuple[bool, int]] = [(True, seed)]
        while stack:
            is_row, vertex = stack.pop()
            if is_row:
                for column, edge_sign in row_adjacency[vertex]:
                    required = int(row_signs[vertex]) * edge_sign
                    if column_signs[column] and column_signs[column] != required:
                        conflicting += 1
                    elif not column_signs[column]:
                        column_signs[column] = required
                        stack.append((False, column))
            else:
                for row, edge_sign in column_adjacency[vertex]:
                    required = int(column_signs[vertex]) * edge_sign
                    if row_signs[row] and row_signs[row] != required:
                        conflicting += 1
                    elif not row_signs[row]:
                        row_signs[row] = required
                        stack.append((True, row))

    return SignGaugeLedger(
        equivalent=conflicting == 0,
        support_edges=len(left_entries),
        nontrivial_components=components,
        conflicting_edges=conflicting,
        maximum_ratio_error=maximum_error,
    )


def _swap_expectation(
    pair_codes: np.ndarray, vector: np.ndarray, dimension: int
) -> float:
    lookup = {int(code): index for index, code in enumerate(pair_codes)}
    swapped = np.zeros_like(vector)
    for index, raw_code in enumerate(pair_codes):
        first, second = divmod(int(raw_code), dimension)
        partner = lookup.get(second * dimension + first)
        if partner is not None:
            swapped[index] = vector[partner]
    return float(np.vdot(vector, swapped).real)


def _weighted_integer_quantile(
    values: np.ndarray, weights: np.ndarray, quantile: float
) -> int:
    if values.size == 0 or weights.sum() == 0:
        return 0
    order = np.argsort(values, kind="stable")
    cumulative = np.cumsum(weights[order])
    index = int(np.searchsorted(cumulative, quantile * cumulative[-1], side="left"))
    return int(values[order[min(index, values.size - 1)]])


def pair_state_mode_profile(
    core: FourCycleCore,
    row_pair_codes: Sequence[int] | np.ndarray,
    column_pair_codes: Sequence[int] | np.ndarray,
    matrix: csr_matrix,
    left_vector: Sequence[complex] | np.ndarray,
    right_vector: Sequence[complex] | np.ndarray,
    *,
    singular_value: float,
    tangent_threshold: int | None = None,
    maximum_smith_classes: int = 16,
) -> PairStateModeProfile:
    """Profile one transfer mode by diagonal, tangent, and Smith invariants.

    Edge influence is the absolute summand
    ``|conj(u_r) B_rc v_c|``.  This is a localization diagnostic, not a
    signed spectral decomposition when the mode or matrix changes sign.
    """

    if maximum_smith_classes <= 0:
        raise ValueError("maximum_smith_classes must be positive")
    row_codes = np.asarray(row_pair_codes, dtype=np.int64)
    column_codes = np.asarray(column_pair_codes, dtype=np.int64)
    left = np.asarray(left_vector)
    right = np.asarray(right_vector)
    if left.shape != (matrix.shape[0],) or right.shape != (matrix.shape[1],):
        raise ValueError("singular vectors have incompatible dimensions")
    if row_codes.shape != (matrix.shape[0],) or column_codes.shape != (
        matrix.shape[1],
    ):
        raise ValueError("pair-code arrays have incompatible dimensions")
    left_norm = float(np.vdot(left, left).real)
    right_norm = float(np.vdot(right, right).real)
    if left_norm == 0.0 or right_norm == 0.0:
        raise ValueError("mode vectors must be nonzero")
    left = left / math.sqrt(left_norm)
    right = right / math.sqrt(right_norm)

    n = core.dimension
    left_diagonal = np.asarray(
        [divmod(int(code), n)[0] == divmod(int(code), n)[1] for code in row_codes]
    )
    right_diagonal = np.asarray(
        [
            divmod(int(code), n)[0] == divmod(int(code), n)[1]
            for code in column_codes
        ]
    )
    coordinates = matrix.tocoo()
    influences = np.abs(
        np.conjugate(left[coordinates.row])
        * coordinates.data
        * right[coordinates.col]
    ).astype(float)
    influence_total = float(influences.sum())
    if influence_total == 0.0:
        normalized = np.zeros_like(influences)
    else:
        normalized = influences / influence_total

    shifts = np.zeros(coordinates.nnz, dtype=np.int64)
    smith_counts: dict[tuple[int, int], int] = defaultdict(int)
    smith_influence: dict[tuple[int, int], float] = defaultdict(float)
    values = core.values
    for edge_index, (row_index, column_index) in enumerate(
        zip(coordinates.row, coordinates.col)
    ):
        first_left, second_left = divmod(int(row_codes[row_index]), n)
        first_right, second_right = divmod(int(column_codes[column_index]), n)
        x1 = int(values[first_left])
        x2 = int(values[second_left])
        y1 = int(values[first_right])
        y2 = int(values[second_right])
        shift = x1 * y1 - x2 * y2
        shifts[edge_index] = abs(shift)
        first_invariant = math.gcd(x1, x2, y1, y2)
        second_invariant = abs(shift) // first_invariant
        key = (first_invariant, second_invariant)
        smith_counts[key] += 1
        smith_influence[key] += float(normalized[edge_index])

    principal_fraction = float(normalized[shifts == 0].sum())
    threshold_fraction = (
        float(normalized[shifts <= tangent_threshold].sum())
        if tangent_threshold is not None
        else 0.0
    )
    influence_square_sum = float(np.dot(normalized, normalized))
    maximum_index = int(np.argmax(normalized)) if normalized.size else 0
    ordered_smith_keys = sorted(
        smith_counts,
        key=lambda item: (-smith_influence[item], item),
    )
    reported_keys = ordered_smith_keys[:maximum_smith_classes]
    smith = tuple(
        SmithInfluence(
            first_invariant=key[0],
            second_invariant=key[1],
            edge_count=smith_counts[key],
            influence_fraction=smith_influence[key],
        )
        for key in reported_keys
    )
    return PairStateModeProfile(
        singular_value=float(singular_value),
        left_diagonal_mass=float(np.sum(np.abs(left[left_diagonal]) ** 2)),
        right_diagonal_mass=float(np.sum(np.abs(right[right_diagonal]) ** 2)),
        left_swap_expectation=_swap_expectation(row_codes, left, n),
        right_swap_expectation=_swap_expectation(column_codes, right, n),
        left_participation=1.0 / float(np.sum(np.abs(left) ** 4)),
        right_participation=1.0 / float(np.sum(np.abs(right) ** 4)),
        effective_influential_edges=(
            1.0 / influence_square_sum if influence_square_sum else 0.0
        ),
        principal_tangent_influence_fraction=principal_fraction,
        threshold_tangent_influence_fraction=threshold_fraction,
        weighted_mean_absolute_shift=float(np.dot(normalized, shifts)),
        weighted_median_absolute_shift=_weighted_integer_quantile(
            shifts, normalized, 0.5
        ),
        weighted_ninetieth_absolute_shift=_weighted_integer_quantile(
            shifts, normalized, 0.9
        ),
        maximum_influence_absolute_shift=(
            int(shifts[maximum_index]) if shifts.size else 0
        ),
        smith_influences=smith,
        unreported_smith_influence_fraction=max(
            0.0, 1.0 - sum(item.influence_fraction for item in smith)
        ),
    )


def actual_prime_power_spectral_ledger(
    q: int,
    *,
    width: float = 0.2,
    cutoff: float = 12.0,
    quadrature_order: int = 32,
    tangent_radius_factor: float = 5.0,
) -> ActualPrimePowerSpectralLedger:
    """Run the full finite probe used by the companion report.

    Runtime is governed by directed completion enumeration.  The largest
    audited fixture ``q=200003`` takes tens of seconds on the reference
    workspace; no asymptotic inference is made from that finite timing or
    from the returned eigensolver values.
    """

    from qp_four_cycle_h_graph_lab import (  # local to keep the core API light
        build_pair_incidence_graph,
        filtered_pair_incidence_graph,
    )
    from qp_four_cycle_hostile_lab import build_four_cycle_core

    core = build_four_cycle_core(
        int(q),
        width=width,
        cutoff=cutoff,
        kind="prime_powers",
        quadrature_order=quadrature_order,
    )
    live_colors = np.unique(core.colors)
    color_weights = np.zeros(core.dimension)
    color_weights[live_colors] = 1.0 / math.sqrt(len(live_colors))

    raw = build_diagonal_tensor_transfer(core, color_weights, sector="raw")
    groups = directed_completion_groups(core)
    transfer_mass = float(schatten_fourth_mass(raw.matrix).real)
    completion_mass = completion_square_mass(
        groups, color_weights, dimension=core.dimension
    )
    classification = completion_pair_classification(
        core,
        groups,
        color_weights,
        tangent_radius=math.ceil(
            tangent_radius_factor * math.sqrt(core.geometric_degree_cap)
        ),
    )

    sectors = {
        sector: build_diagonal_tensor_transfer(
            core, color_weights, sector=sector
        )
        for sector in (
            "diagonal",
            "symmetric_offdiagonal",
            "antisymmetric_offdiagonal",
        )
    }
    sector_masses = {
        sector: float(schatten_fourth_mass(transfer.matrix).real)
        for sector, transfer in sectors.items()
    }
    sector_tops = {
        sector: float(
            largest_singular_triplets(transfer.matrix, rank=1).singular_values[0]
        )
        for sector, transfer in sectors.items()
    }
    gauge = sign_gauge_ledger(
        sectors["symmetric_offdiagonal"].matrix,
        sectors["antisymmetric_offdiagonal"].matrix,
    )

    incidence = filtered_pair_incidence_graph(
        core,
        build_pair_incidence_graph(core),
        keep="all_five_distinct",
    )
    incidence_modes = largest_singular_triplets(incidence.weighted, rank=2)
    incidence_profile = pair_state_mode_profile(
        core,
        incidence.left_pair_codes,
        incidence.right_pair_codes,
        incidence.weighted,
        incidence_modes.left_vectors[:, 0],
        incidence_modes.right_vectors[:, 0],
        singular_value=incidence_modes.singular_values[0],
        tangent_threshold=math.ceil(core.geometric_degree_cap),
    )
    dominant_smith = incidence_profile.smith_influences[0]
    return ActualPrimePowerSpectralLedger(
        q=int(q),
        nodes=core.dimension,
        triples=len(core.rows),
        live_colors=len(live_colors),
        degree_scale=core.geometric_degree_cap,
        tensor_entries=raw.matrix.nnz,
        directed_completions=sum(len(terms) for terms in groups.values()),
        color_matrices=len(groups),
        identity_error=abs(transfer_mass - completion_mass),
        full_fourth_mass=classification.total_mass,
        pair_diagonal_mass=classification.pair_diagonal_mass,
        degenerate_offdiagonal_mass=classification.degenerate_offdiagonal_mass,
        genuine_offdiagonal_mass=classification.genuine_offdiagonal_mass,
        genuine_offdiagonal_fraction=(
            classification.genuine_offdiagonal_mass / classification.total_mass
            if classification.total_mass
            else 0.0
        ),
        genuine_offdiagonal_pairs=classification.genuine_offdiagonal_pairs,
        secant_smith_classes=len(classification.smith_masses),
        rank_one_secant_pairs=classification.rank_one_secant_pairs,
        additive_tangent_pairs=classification.additive_tangent_pairs,
        near_square_tangent_pairs=classification.near_square_tangent_pairs,
        diagonal_sector_fourth_mass=sector_masses["diagonal"],
        symmetric_sector_fourth_mass=sector_masses[
            "symmetric_offdiagonal"
        ],
        antisymmetric_sector_fourth_mass=sector_masses[
            "antisymmetric_offdiagonal"
        ],
        diagonal_sector_top_singular=sector_tops["diagonal"],
        symmetric_sector_top_singular=sector_tops[
            "symmetric_offdiagonal"
        ],
        antisymmetric_sector_top_singular=sector_tops[
            "antisymmetric_offdiagonal"
        ],
        exterior_sign_gauge_equivalent=gauge.equivalent,
        exterior_sign_gauge_components=gauge.nontrivial_components,
        incidence_edges=incidence.weighted.nnz,
        incidence_top_singular=float(incidence_modes.singular_values[0]),
        incidence_mode_median_shift=(
            incidence_profile.weighted_median_absolute_shift
        ),
        incidence_mode_ninetieth_shift=(
            incidence_profile.weighted_ninetieth_absolute_shift
        ),
        incidence_mode_degree_window_fraction=(
            incidence_profile.threshold_tangent_influence_fraction
        ),
        incidence_mode_dominant_smith_first=dominant_smith.first_invariant,
        incidence_mode_dominant_smith_second=dominant_smith.second_invariant,
        incidence_mode_dominant_smith_fraction=(
            dominant_smith.influence_fraction
        ),
    )


if __name__ == "__main__":
    import argparse
    from dataclasses import asdict
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q", type=int, nargs="+", help="odd prime moduli")
    parser.add_argument("--quadrature-order", type=int, default=32)
    arguments = parser.parse_args()
    for modulus in arguments.q:
        ledger = actual_prime_power_spectral_ledger(
            modulus, quadrature_order=arguments.quadrature_order
        )
        print(json.dumps(asdict(ledger), sort_keys=True), flush=True)
