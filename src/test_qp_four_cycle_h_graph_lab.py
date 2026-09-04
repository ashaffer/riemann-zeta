import math

import numpy as np
import pytest
from scipy.sparse import csr_matrix

from qp_four_cycle_h_graph_lab import (
    PairIncidenceGraph,
    build_pair_incidence_graph,
    canonical_color_rectangle,
    decode_pair,
    enumerate_rectangles,
    enumerate_three_by_three_grids,
    filtered_pair_incidence_graph,
    h_graph_ledger,
    smallest_core_component,
    wedge_ledger,
)
from qp_four_cycle_hostile_lab import FourCycleCore


def test_builder_uses_ordered_pairs_and_exact_edge_weights() -> None:
    core = FourCycleCore(
        q=101,
        aperture=1.5,
        width=0.2,
        cutoff=1.0,
        values=np.asarray([41, 43, 47], dtype=np.int64),
        rows=np.asarray([0, 1, 0, 1], dtype=np.int32),
        columns=np.asarray([0, 0, 1, 1], dtype=np.int32),
        colors=np.asarray([0, 1, 1, 2], dtype=np.int32),
        weights=np.asarray([1.0, 0.5, 0.75, 0.25], dtype=float),
    )
    graph = build_pair_incidence_graph(core)
    decoded_left = {
        decode_pair(int(code), core.dimension)
        for code in graph.left_pair_codes
    }
    assert decoded_left == {(0, 1), (1, 0)}
    assert graph.support.shape == (2, 4)
    assert graph.support.nnz == 4
    assert sorted(graph.weighted.data.tolist()) == [0.1875, 0.1875, 0.5, 0.5]
    assert sorted(graph.carriers.data.tolist()) == [41, 41, 43, 43]


def test_four_cycle_has_degeneracy_and_arboricity_two() -> None:
    support = csr_matrix(np.ones((2, 2), dtype=np.int32))
    graph = PairIncidenceGraph(
        left_pair_codes=np.asarray([1, 2]),
        right_pair_codes=np.asarray([3, 4]),
        support=support,
        weighted=support.astype(float),
    )
    ledger = h_graph_ledger(graph)
    assert ledger.edges == 4
    assert ledger.connected_components == 1
    assert ledger.cyclic_components == 1
    assert ledger.total_cycle_rank == 1
    assert ledger.maximum_component_excess == 1
    assert ledger.four_cycles == 1
    assert ledger.two_core_vertices == 4
    assert ledger.degeneracy == 2
    assert ledger.certified_arboricity == 2
    assert ledger.support_spectral_norm == pytest.approx(2.0, abs=1.0e-11)
    witness = smallest_core_component(graph, 2)
    assert witness is not None
    assert len(witness.left_pair_codes) == 2
    assert len(witness.right_pair_codes) == 2
    assert len(witness.edges) == 4
    assert smallest_core_component(graph, 3) is None


def test_path_is_a_forest_with_arboricity_one() -> None:
    support = csr_matrix(np.asarray([[1, 1], [0, 1]], dtype=np.int32))
    graph = PairIncidenceGraph(
        left_pair_codes=np.asarray([1, 2]),
        right_pair_codes=np.asarray([3, 4]),
        support=support,
        weighted=support.astype(float),
    )
    ledger = h_graph_ledger(graph)
    assert ledger.total_cycle_rank == 0
    assert ledger.four_cycles == 0
    assert ledger.two_core_vertices == 0
    assert ledger.degeneracy == 1
    assert ledger.certified_arboricity == 1
    assert ledger.support_spectral_norm == pytest.approx(
        (1.0 + math.sqrt(5.0)) / 2.0, abs=1.0e-11
    )


def test_rectangle_enumerator_separates_generic_unordered_hyperedges() -> None:
    values = np.asarray([11, 13, 17, 19, 23, 29, 31, 37], dtype=np.int64)
    core = FourCycleCore(
        q=101,
        aperture=1.5,
        width=0.2,
        cutoff=1.0,
        values=values,
        rows=np.asarray([0, 0, 1, 1], dtype=np.int32),
        columns=np.asarray([2, 3, 2, 3], dtype=np.int32),
        colors=np.asarray([4, 5, 6, 7], dtype=np.int32),
        weights=np.ones(4),
    )
    graph = build_pair_incidence_graph(core)
    rectangles = enumerate_rectangles(core, graph)
    assert len(rectangles) == 1
    rectangle = rectangles[0]
    assert rectangle.colors == (23, 29, 31, 37)
    assert rectangle.color_determinant == -48
    assert rectangle.distinct_node_count == 8
    assert rectangle.distinct_unordered_hyperedges == 4
    ledger = wedge_ledger(rectangles)
    assert ledger.rectangles == 1
    assert ledger.zero_color_determinants == 0
    assert ledger.minimum_nonzero_determinant == 48
    assert ledger.maximum_determinant == 48
    assert ledger.all_eight_coordinates_distinct == 1
    assert ledger.all_four_unordered_hyperedges_distinct == 1
    assert ledger.maximum_exact_color_completion == 1
    assert ledger.maximum_color_orbit_completion == 1
    assert canonical_color_rectangle((23, 29, 31, 37)) == (
        23,
        29,
        31,
        37,
    )
    assert filtered_pair_incidence_graph(
        core, graph, keep="all_five_distinct"
    ).support.nnz == graph.support.nnz


def test_same_unordered_hyperedge_filter_removes_role_permutations() -> None:
    core = FourCycleCore(
        q=101,
        aperture=1.5,
        width=0.2,
        cutoff=1.0,
        values=np.asarray([11, 13, 17], dtype=np.int64),
        rows=np.asarray([0, 1], dtype=np.int32),
        columns=np.asarray([2, 2], dtype=np.int32),
        colors=np.asarray([1, 0], dtype=np.int32),
        weights=np.ones(2),
    )
    graph = build_pair_incidence_graph(core)
    assert graph.support.nnz == 2
    filtered = filtered_pair_incidence_graph(
        core, graph, keep="distinct_hyperedges"
    )
    assert filtered.support.nnz == 0


def test_completed_three_by_three_grid_and_color_determinant() -> None:
    values = np.asarray(
        [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67],
        dtype=np.int64,
    )
    rows = []
    columns = []
    colors = []
    for row in range(3):
        for column in range(3):
            rows.append(row)
            columns.append(3 + column)
            colors.append(6 + 3 * row + column)
    core = FourCycleCore(
        q=101,
        aperture=1.5,
        width=0.2,
        cutoff=1.0,
        values=values,
        rows=np.asarray(rows, dtype=np.int32),
        columns=np.asarray(columns, dtype=np.int32),
        colors=np.asarray(colors, dtype=np.int32),
        weights=np.ones(9),
    )
    grids = enumerate_three_by_three_grids(core)
    assert len(grids) == 1
    grid = grids[0]
    assert grid.rows == (11, 13, 17)
    assert grid.columns == (19, 23, 29)
    assert grid.colors == (31, 37, 41, 43, 47, 53, 59, 61, 67)
    a, b, c, d, e, f, g, h, i = grid.colors
    assert grid.color_determinant == (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )
    assert grid.distinct_unordered_hyperedges == 9
