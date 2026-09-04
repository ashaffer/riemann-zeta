"""Finite graph diagnostics for the actual-shell four-cycle incidence.

The left vertices are ordered pairs of distinct rows and the right vertices
are ordered pairs of colors.  An ordered pair of triples sharing a carrier
gives one bipartite edge.  These routines make no asymptotic assertion; they
replay the finite support and its exact graph invariants.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import Counter, defaultdict
from itertools import combinations
from typing import Literal

import numpy as np
from scipy.sparse import bmat, coo_matrix, csr_matrix
from scipy.sparse.csgraph import connected_components

from qp_four_cycle_hostile_lab import FourCycleCore


@dataclass(frozen=True)
class PairIncidenceGraph:
    """Compact ordered-pair encoding of the bipartite incidence graph."""

    left_pair_codes: np.ndarray
    right_pair_codes: np.ndarray
    support: csr_matrix
    weighted: csr_matrix
    carriers: csr_matrix | None = None


@dataclass(frozen=True)
class HCoreWitness:
    """A smallest connected component of a requested finite ``k``-core."""

    minimum_degree: int
    left_pair_codes: tuple[int, ...]
    right_pair_codes: tuple[int, ...]
    edges: tuple[tuple[int, int, int], ...]


@dataclass(frozen=True)
class RectangleRecord:
    """One unoriented row/column rectangle in the finite carry core."""

    first_row: int
    second_row: int
    first_column: int
    second_column: int
    colors: tuple[int, int, int, int]
    color_determinant: int
    kernel_mass: float
    distinct_node_count: int
    distinct_unordered_hyperedges: int


@dataclass(frozen=True)
class WedgeLedger:
    """Finite generic/permutation and completion-multiplicity counts."""

    rectangles: int
    zero_color_determinants: int
    minimum_nonzero_determinant: int
    maximum_determinant: int
    all_eight_coordinates_distinct: int
    all_four_unordered_hyperedges_distinct: int
    maximum_exact_color_completion: int
    maximum_color_orbit_completion: int


@dataclass(frozen=True)
class ThreeByThreeGrid:
    """One completed row/carrier 3-by-3 grid and its color matrix."""

    rows: tuple[int, int, int]
    columns: tuple[int, int, int]
    colors: tuple[int, int, int, int, int, int, int, int, int]
    color_determinant: int
    distinct_unordered_hyperedges: int


@dataclass(frozen=True)
class HGraphLedger:
    """Exact combinatorial invariants and deterministic norm diagnostics."""

    left_vertices: int
    right_vertices: int
    edges: int
    maximum_left_degree: int
    maximum_right_degree: int
    connected_components: int
    cyclic_components: int
    total_cycle_rank: int
    maximum_component_vertices: int
    maximum_component_edges: int
    maximum_component_excess: int
    four_cycles: int
    two_core_vertices: int
    degeneracy: int
    certified_arboricity: int | None
    support_spectral_norm: float
    weighted_spectral_norm: float


def build_pair_incidence_graph(core: FourCycleCore) -> PairIncidenceGraph:
    """Build the ordered row-pair/color-pair incidence from a finite core.

    The returned weighted edge from ``(a,a')`` to ``(c,c')`` has coefficient
    ``conj(kappa(a,b,c))*kappa(a',b,c')``.  A repeated edge would mean that
    two carriers complete the same four coordinates, so it is rejected.
    """

    dimension = core.dimension
    order = np.argsort(core.columns, kind="stable")
    columns = core.columns[order]
    rows = core.rows[order].astype(np.int64, copy=False)
    colors = core.colors[order].astype(np.int64, copy=False)
    weights = core.weights[order]

    if columns.size:
        boundaries = np.r_[
            0, np.flatnonzero(np.diff(columns)) + 1, columns.size
        ]
    else:
        boundaries = np.asarray([0], dtype=np.int64)

    left_chunks: list[np.ndarray] = []
    right_chunks: list[np.ndarray] = []
    weight_chunks: list[np.ndarray] = []
    carrier_chunks: list[np.ndarray] = []
    for start, stop in zip(boundaries[:-1], boundaries[1:]):
        carrier_degree = int(stop - start)
        if carrier_degree < 2:
            continue
        first = np.repeat(np.arange(carrier_degree), carrier_degree)
        second = np.tile(np.arange(carrier_degree), carrier_degree)
        non_diagonal = first != second
        first = first[non_diagonal]
        second = second[non_diagonal]

        local_rows = rows[start:stop]
        local_colors = colors[start:stop]
        local_weights = weights[start:stop]
        left_chunks.append(
            local_rows[first] * dimension + local_rows[second]
        )
        right_chunks.append(
            local_colors[first] * dimension + local_colors[second]
        )
        weight_chunks.append(
            np.conjugate(local_weights[first]) * local_weights[second]
        )
        carrier_chunks.append(
            np.full(
                first.size,
                int(core.values[int(columns[start])]),
                dtype=np.int64,
            )
        )

    if not left_chunks:
        empty = csr_matrix((0, 0), dtype=float)
        return PairIncidenceGraph(
            left_pair_codes=np.empty(0, dtype=np.int64),
            right_pair_codes=np.empty(0, dtype=np.int64),
            support=empty,
            weighted=empty.copy(),
            carriers=empty.copy(),
        )

    raw_left = np.concatenate(left_chunks)
    raw_right = np.concatenate(right_chunks)
    raw_weights = np.concatenate(weight_chunks)
    left_codes, left_indices = np.unique(raw_left, return_inverse=True)
    right_codes, right_indices = np.unique(raw_right, return_inverse=True)
    shape = (left_codes.size, right_codes.size)
    support = coo_matrix(
        (
            np.ones(raw_left.size, dtype=np.int32),
            (left_indices, right_indices),
        ),
        shape=shape,
    ).tocsr()
    support.sum_duplicates()
    if support.nnz != raw_left.size or np.any(support.data != 1):
        raise ValueError("one ordered-pair incidence has multiple carriers")
    weighted = coo_matrix(
        (raw_weights, (left_indices, right_indices)), shape=shape
    ).tocsr()
    weighted.sum_duplicates()
    carrier_values = np.concatenate(carrier_chunks)
    carriers = coo_matrix(
        (carrier_values, (left_indices, right_indices)), shape=shape
    ).tocsr()
    carriers.sum_duplicates()
    return PairIncidenceGraph(
        left_pair_codes=left_codes,
        right_pair_codes=right_codes,
        support=support,
        weighted=weighted,
        carriers=carriers,
    )


def _power_spectral_norm(
    matrix: csr_matrix, *, tolerance: float = 1.0e-13, iterations: int = 1000
) -> float:
    """Deterministic positive-start power iteration for a finite diagnostic."""

    if matrix.nnz == 0:
        return 0.0
    vector = np.ones(matrix.shape[1], dtype=float)
    vector /= np.linalg.norm(vector)
    previous = -1.0
    for _ in range(iterations):
        image = matrix @ vector
        back = matrix.conjugate().T @ image
        back_norm = float(np.linalg.norm(back))
        if back_norm == 0.0:
            return 0.0
        vector = back / back_norm
        value = float(np.linalg.norm(matrix @ vector))
        if abs(value - previous) <= tolerance * max(1.0, value):
            return value
        previous = value
    return value


def filtered_pair_incidence_graph(
    core: FourCycleCore,
    graph: PairIncidenceGraph,
    *,
    keep: Literal["distinct_hyperedges", "all_five_distinct"],
) -> PairIncidenceGraph:
    """Delete permutation edges or every repeated-node edge.

    ``distinct_hyperedges`` removes exactly the edges for which the two
    triples sharing the carrier are the same unordered 3-edge.  The stronger
    ``all_five_distinct`` mode retains only edges with five distinct values
    ``a,a',b,c,c'``.
    """

    if graph.carriers is None:
        raise ValueError("carrier labels are required for edge filtering")
    dimension = core.dimension
    coordinates = graph.support.tocoo()
    kept_rows: list[int] = []
    kept_columns: list[int] = []
    kept_weights: list[complex] = []
    kept_carriers: list[int] = []
    for left_index, right_index in zip(coordinates.row, coordinates.col):
        first_row, second_row = decode_pair(
            int(graph.left_pair_codes[int(left_index)]), dimension
        )
        first_color, second_color = decode_pair(
            int(graph.right_pair_codes[int(right_index)]), dimension
        )
        carrier = int(graph.carriers[int(left_index), int(right_index)])
        if keep == "distinct_hyperedges":
            retain = not (
                first_row == second_color and second_row == first_color
            )
        elif keep == "all_five_distinct":
            nodes = {
                int(core.values[first_row]),
                int(core.values[second_row]),
                carrier,
                int(core.values[first_color]),
                int(core.values[second_color]),
            }
            retain = len(nodes) == 5
        else:
            raise ValueError("unknown edge filter")
        if retain:
            kept_rows.append(int(left_index))
            kept_columns.append(int(right_index))
            kept_weights.append(graph.weighted[int(left_index), int(right_index)])
            kept_carriers.append(carrier)

    shape = graph.support.shape
    support = coo_matrix(
        (
            np.ones(len(kept_rows), dtype=np.int32),
            (kept_rows, kept_columns),
        ),
        shape=shape,
    ).tocsr()
    weighted = coo_matrix(
        (kept_weights, (kept_rows, kept_columns)), shape=shape
    ).tocsr()
    carriers = coo_matrix(
        (kept_carriers, (kept_rows, kept_columns)), shape=shape
    ).tocsr()
    live_left = support.getnnz(axis=1) > 0
    live_right = support.getnnz(axis=0) > 0
    return PairIncidenceGraph(
        left_pair_codes=graph.left_pair_codes[live_left],
        right_pair_codes=graph.right_pair_codes[live_right],
        support=support[live_left][:, live_right],
        weighted=weighted[live_left][:, live_right],
        carriers=carriers[live_left][:, live_right],
    )


def canonical_color_rectangle(
    colors: tuple[int, int, int, int]
) -> tuple[int, int, int, int]:
    """Canonicalize a 2-by-2 color matrix under row/column/transpose symmetries."""

    a, b, c, d = colors
    orbit = (
        (a, b, c, d),
        (c, d, a, b),
        (b, a, d, c),
        (d, c, b, a),
        (a, c, b, d),
        (b, d, a, c),
        (c, a, d, b),
        (d, b, c, a),
    )
    return min(orbit)


def enumerate_rectangles(
    core: FourCycleCore, graph: PairIncidenceGraph | None = None
) -> tuple[RectangleRecord, ...]:
    """Enumerate each unordered row-pair/column-pair rectangle once."""

    if graph is None:
        graph = build_pair_incidence_graph(core)
    if graph.carriers is None:
        raise ValueError("carrier labels are required for rectangle enumeration")
    dimension = core.dimension
    answer: list[RectangleRecord] = []
    for left_index, left_code in enumerate(graph.left_pair_codes):
        first_row_index, second_row_index = decode_pair(
            int(left_code), dimension
        )
        if first_row_index >= second_row_index:
            continue
        first_row = int(core.values[first_row_index])
        second_row = int(core.values[second_row_index])
        edge_data: list[tuple[int, int, int, float]] = []
        start = graph.support.indptr[left_index]
        stop = graph.support.indptr[left_index + 1]
        for right_index in graph.support.indices[start:stop]:
            first_color_index, second_color_index = decode_pair(
                int(graph.right_pair_codes[int(right_index)]), dimension
            )
            edge_data.append(
                (
                    int(graph.carriers[left_index, int(right_index)]),
                    int(core.values[first_color_index]),
                    int(core.values[second_color_index]),
                    abs(complex(graph.weighted[left_index, int(right_index)])),
                )
            )
        edge_data.sort()
        for first_edge, second_edge in combinations(edge_data, 2):
            first_column, c11, c21, first_weight = first_edge
            second_column, c12, c22, second_weight = second_edge
            colors = (c11, c12, c21, c22)
            nodes = (
                first_row,
                second_row,
                first_column,
                second_column,
                *colors,
            )
            hyperedges = {
                frozenset((first_row, first_column, c11)),
                frozenset((first_row, second_column, c12)),
                frozenset((second_row, first_column, c21)),
                frozenset((second_row, second_column, c22)),
            }
            answer.append(
                RectangleRecord(
                    first_row=first_row,
                    second_row=second_row,
                    first_column=first_column,
                    second_column=second_column,
                    colors=colors,
                    color_determinant=c11 * c22 - c12 * c21,
                    kernel_mass=first_weight * second_weight,
                    distinct_node_count=len(set(nodes)),
                    distinct_unordered_hyperedges=len(hyperedges),
                )
            )
    return tuple(answer)


def wedge_ledger(rectangles: tuple[RectangleRecord, ...]) -> WedgeLedger:
    """Summarize determinant, genericity, and fixed-color completion counts."""

    absolute_determinants = [abs(item.color_determinant) for item in rectangles]
    nonzero = [value for value in absolute_determinants if value]
    exact = Counter(item.colors for item in rectangles)
    orbit = Counter(canonical_color_rectangle(item.colors) for item in rectangles)
    return WedgeLedger(
        rectangles=len(rectangles),
        zero_color_determinants=sum(value == 0 for value in absolute_determinants),
        minimum_nonzero_determinant=min(nonzero, default=0),
        maximum_determinant=max(nonzero, default=0),
        all_eight_coordinates_distinct=sum(
            item.distinct_node_count == 8 for item in rectangles
        ),
        all_four_unordered_hyperedges_distinct=sum(
            item.distinct_unordered_hyperedges == 4 for item in rectangles
        ),
        maximum_exact_color_completion=max(exact.values(), default=0),
        maximum_color_orbit_completion=max(orbit.values(), default=0),
    )


def enumerate_three_by_three_grids(
    core: FourCycleCore,
) -> tuple[ThreeByThreeGrid, ...]:
    """Enumerate completed row/carrier ``K_(3,3)`` supports exactly."""

    rows_by_column: list[list[int]] = [
        [] for _ in range(core.dimension)
    ]
    color_lookup: dict[tuple[int, int], int] = {}
    for row, column, color in zip(core.rows, core.columns, core.colors):
        row_index = int(row)
        column_index = int(column)
        rows_by_column[column_index].append(row_index)
        color_lookup[row_index, column_index] = int(color)

    columns_by_row_triple: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for column_index, row_indices in enumerate(rows_by_column):
        for row_triple in combinations(sorted(row_indices), 3):
            columns_by_row_triple[row_triple].append(column_index)

    answer: list[ThreeByThreeGrid] = []
    for row_indices, column_indices in columns_by_row_triple.items():
        for selected_columns in combinations(column_indices, 3):
            color_indices = tuple(
                color_lookup[row_index, column_index]
                for row_index in row_indices
                for column_index in selected_columns
            )
            color_values = tuple(
                int(core.values[index]) for index in color_indices
            )
            a, b, c, d, e, f, g, h, i = color_values
            determinant = (
                a * (e * i - f * h)
                - b * (d * i - f * g)
                + c * (d * h - e * g)
            )
            row_values = tuple(
                int(core.values[index]) for index in row_indices
            )
            column_values = tuple(
                int(core.values[index]) for index in selected_columns
            )
            hyperedges = {
                frozenset((row_values[row], column_values[column], color_values[3 * row + column]))
                for row in range(3)
                for column in range(3)
            }
            answer.append(
                ThreeByThreeGrid(
                    rows=row_values,
                    columns=column_values,
                    colors=color_values,
                    color_determinant=determinant,
                    distinct_unordered_hyperedges=len(hyperedges),
                )
            )
    return tuple(answer)


def _k_core(
    adjacency: csr_matrix, minimum_degree: int
) -> tuple[np.ndarray, int]:
    """Return the exact finite ``minimum_degree`` core and peel count."""

    active = adjacency.getnnz(axis=1) >= minimum_degree
    peels = 0
    while np.any(active):
        neighbor_counts = adjacency @ active.astype(np.int32)
        updated = active & (neighbor_counts >= minimum_degree)
        peels += 1
        if np.array_equal(updated, active):
            return active, peels
        active = updated
    return active, peels


def _degeneracy(adjacency: csr_matrix) -> tuple[int, int]:
    """Compute degeneracy and the number of vertices in the two-core."""

    if adjacency.nnz == 0:
        return 0, 0
    maximum_degree = int(adjacency.getnnz(axis=1).max(initial=0))
    degeneracy = 0
    two_core_vertices = 0
    for minimum_degree in range(1, maximum_degree + 1):
        core, _ = _k_core(adjacency, minimum_degree)
        core_size = int(core.sum())
        if minimum_degree == 2:
            two_core_vertices = core_size
        if core_size == 0:
            break
        degeneracy = minimum_degree
    return degeneracy, two_core_vertices


def _four_cycle_count(support: csr_matrix) -> int:
    """Count unoriented simple four-cycles exactly."""

    if support.nnz == 0:
        return 0
    common = (support @ support.T).tocoo()
    upper = common.row < common.col
    multiplicities = common.data[upper].astype(np.int64, copy=False)
    return int(np.sum(multiplicities * (multiplicities - 1) // 2))


def h_graph_ledger(graph: PairIncidenceGraph) -> HGraphLedger:
    """Compute exact support invariants and finite weighted/support norms."""

    support = graph.support
    left_vertices, right_vertices = support.shape
    edges = int(support.nnz)
    maximum_left = int(support.getnnz(axis=1).max(initial=0))
    maximum_right = int(support.getnnz(axis=0).max(initial=0))

    if edges == 0:
        return HGraphLedger(
            left_vertices=left_vertices,
            right_vertices=right_vertices,
            edges=0,
            maximum_left_degree=0,
            maximum_right_degree=0,
            connected_components=left_vertices + right_vertices,
            cyclic_components=0,
            total_cycle_rank=0,
            maximum_component_vertices=int(bool(left_vertices + right_vertices)),
            maximum_component_edges=0,
            maximum_component_excess=0,
            four_cycles=0,
            two_core_vertices=0,
            degeneracy=0,
            certified_arboricity=0,
            support_spectral_norm=0.0,
            weighted_spectral_norm=0.0,
        )

    adjacency = bmat(
        [[None, support], [support.T, None]], format="csr", dtype=np.int32
    )
    component_count, labels = connected_components(
        adjacency, directed=False, return_labels=True
    )
    component_vertices = np.bincount(labels, minlength=component_count)
    coordinates = support.tocoo()
    edge_components = labels[coordinates.row]
    component_edges = np.bincount(
        edge_components, minlength=component_count
    )
    component_excess = component_edges - component_vertices + 1
    cyclic = component_excess > 0
    total_cycle_rank = int(component_excess[cyclic].sum())
    degeneracy, two_core_vertices = _degeneracy(adjacency)

    # A nonempty forest has arboricity one.  If a cycle exists and the graph
    # is two-degenerate, arboricity is exactly two.  For higher degeneracy the
    # finite routine deliberately returns no unsupported exact value.
    if total_cycle_rank == 0:
        arboricity: int | None = 1
    elif degeneracy <= 2:
        arboricity = 2
    else:
        arboricity = None

    return HGraphLedger(
        left_vertices=left_vertices,
        right_vertices=right_vertices,
        edges=edges,
        maximum_left_degree=maximum_left,
        maximum_right_degree=maximum_right,
        connected_components=int(component_count),
        cyclic_components=int(cyclic.sum()),
        total_cycle_rank=total_cycle_rank,
        maximum_component_vertices=int(component_vertices.max(initial=0)),
        maximum_component_edges=int(component_edges.max(initial=0)),
        maximum_component_excess=int(component_excess.max(initial=0)),
        four_cycles=_four_cycle_count(support),
        two_core_vertices=two_core_vertices,
        degeneracy=degeneracy,
        certified_arboricity=arboricity,
        support_spectral_norm=_power_spectral_norm(support.astype(float)),
        weighted_spectral_norm=_power_spectral_norm(graph.weighted),
    )


def smallest_core_component(
    graph: PairIncidenceGraph, minimum_degree: int
) -> HCoreWitness | None:
    """Return a smallest connected component of the finite ``k``-core."""

    if minimum_degree <= 0:
        raise ValueError("minimum_degree must be positive")
    support = graph.support
    if support.nnz == 0:
        return None
    adjacency = bmat(
        [[None, support], [support.T, None]], format="csr", dtype=np.int32
    )
    active, _ = _k_core(adjacency, minimum_degree)
    if not np.any(active):
        return None
    induced = adjacency[active][:, active]
    component_count, labels = connected_components(
        induced, directed=False, return_labels=True
    )
    sizes = np.bincount(labels, minlength=component_count)
    chosen = int(np.argmin(sizes))
    active_indices = np.flatnonzero(active)
    vertices = active_indices[labels == chosen]
    left_count = support.shape[0]
    left_indices = vertices[vertices < left_count]
    right_indices = vertices[vertices >= left_count] - left_count
    right_set = set(int(index) for index in right_indices)
    carriers = graph.carriers
    edge_list: list[tuple[int, int, int]] = []
    for left_index in left_indices:
        for right_index in support.getrow(int(left_index)).indices:
            if int(right_index) not in right_set:
                continue
            carrier = 0
            if carriers is not None:
                carrier = int(carriers[int(left_index), int(right_index)])
            edge_list.append(
                (
                    int(graph.left_pair_codes[int(left_index)]),
                    int(graph.right_pair_codes[int(right_index)]),
                    carrier,
                )
            )
    return HCoreWitness(
        minimum_degree=minimum_degree,
        left_pair_codes=tuple(
            int(graph.left_pair_codes[int(index)]) for index in left_indices
        ),
        right_pair_codes=tuple(
            int(graph.right_pair_codes[int(index)]) for index in right_indices
        ),
        edges=tuple(edge_list),
    )


def decode_pair(code: int, dimension: int) -> tuple[int, int]:
    """Decode the compact ordered-pair code used by the graph builder."""

    if code < 0 or dimension <= 0:
        raise ValueError("invalid ordered-pair code")
    return divmod(int(code), dimension)
