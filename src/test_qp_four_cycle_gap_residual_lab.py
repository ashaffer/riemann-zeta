from itertools import combinations

from qp_four_cycle_gap_residual_lab import gap_residual_core_ledger
from qp_four_cycle_h_graph_lab import RectangleRecord


def test_five_pairwise_uncovered_completions_form_a_four_core() -> None:
    rows = (10_000, 10_100)
    completions = (
        (20_000, 30_000, 40_000),
        (21_000, 31_000, 41_000),
        (22_000, 32_000, 42_000),
        (23_000, 33_000, 43_000),
        (24_000, 34_000, 44_000),
    )
    rectangles = []
    for first, second in combinations(completions, 2):
        b1, c11, c21 = first
        b2, c12, c22 = second
        nodes = (*rows, b1, b2, c11, c12, c21, c22)
        rectangles.append(
            RectangleRecord(
                first_row=rows[0],
                second_row=rows[1],
                first_column=b1,
                second_column=b2,
                colors=(c11, c12, c21, c22),
                color_determinant=c11 * c22 - c12 * c21,
                kernel_mass=1.0,
                distinct_node_count=len(set(nodes)),
                distinct_unordered_hyperedges=4,
            )
        )
    ledger = gap_residual_core_ledger(
        tuple(rectangles), degree_scale=1.0, constant=1.0
    )
    assert ledger.generic_rectangles == 10
    assert ledger.residual_rectangles == 10
    assert ledger.completion_vertices == 5
    assert ledger.degeneracy == 4
    assert len(ledger.smallest_core_vertices) == 5
    assert len(ledger.smallest_core_edges) == 10
