import math

import numpy as np

from qp_k23_higher_trace_gate import (
    affine_tangent_triple_height,
    disjoint_complete_blocks,
    height_excess_ledger,
    k23_elimination_ledger,
    k23_moment_ledger,
    short_orthogonals_are_collinear,
    triple_codegrees,
)


def test_k23_elimination_identities() -> None:
    ledger = k23_elimination_ledger(
        a=(101, 103, 107),
        A=(109, 113, 127),
        p=(131, 137),
        q=(139, 149),
    )
    assert ledger.first_recovery == tuple(
        ledger.column_determinant * value for value in ledger.a
    )
    assert ledger.second_recovery == tuple(
        ledger.column_determinant * value for value in ledger.A
    )
    assert ledger.orthogonal_to_a
    assert ledger.orthogonal_to_A


def test_short_orthogonals_are_forced_collinear() -> None:
    a = (101, 103, 107)
    # The primitive vector (103,-101,0) is orthogonal to a.  Its negative
    # multiple is the only other vector used here, so the short conclusion
    # can be replayed without a numerical approximation.
    h = (103, -101, 0)
    other = (-206, 202, 0)
    assert short_orthogonals_are_collinear(a, h, other)


def test_k23_double_count_and_operator_bounds() -> None:
    matrix = disjoint_complete_blocks(blocks=2, order=4)
    ledger = k23_moment_ledger(matrix)
    expected = 2 * math.comb(4, 3) * math.comb(4, 2)
    assert ledger.left_triple_excess == expected
    assert ledger.right_pair_excess == expected
    assert np.isclose(ledger.operator_norm_squared, 16.0)
    assert ledger.operator_norm_squared <= ledger.global_excess_operator_bound
    assert ledger.operator_norm_squared <= ledger.local_excess_operator_bound


def test_height_cap_on_one_affine_tangent_block() -> None:
    order = 6
    degree_scale = order * order
    matrix = disjoint_complete_blocks(blocks=1, order=order)
    heights = {
        triple: affine_tangent_triple_height(triple)
        for triple in triple_codegrees(matrix)
    }
    assert max(heights.values()) <= order - 1
    ledger = height_excess_ledger(matrix, heights, degree_scale)
    assert ledger.k23_excess == math.comb(order, 3) * math.comb(order, 2)
    assert ledger.k23_excess <= ledger.global_height_upper_bound


def test_sixth_trace_is_not_the_k23_count() -> None:
    # A six-cycle has no K_(3,2), but it contributes nontrivially to the
    # sixth trace.  This is the basic logical mismatch in the proposed route.
    cycle = np.array(
        [
            [1, 1, 0],
            [0, 1, 1],
            [1, 0, 1],
        ],
        dtype=int,
    )
    ledger = k23_moment_ledger(cycle)
    assert ledger.left_triple_excess == 0
    assert ledger.sixth_trace > 0
