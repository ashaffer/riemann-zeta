import numpy as np

from qp_residual_block_triangle_matching import (
    affine_plane_sts9_parallel_classes,
    blocks_are_vertex_matchings,
    product_residual,
    residual_blocks,
    same_short_block_forces_disjoint_or_equal,
    schatten_fourth_power,
    weighted_steiner_adjacency,
)


def test_shared_node_and_short_residual_gap_force_same_product():
    q = 1009
    first = (401, 409, 419)
    equal_permutation = (419, 401, 409)
    assert same_short_block_forces_disjoint_or_equal(q, first, equal_permutation, q)


def test_literal_actual_triples_form_matchings_in_q_blocks():
    # Two disjoint triples can share a block; a shared-node distinct triple
    # cannot when the width is below eight times every node.
    q = 101
    triples = [(41, 43, 47), (53, 59, 61), (41, 67, 71)]
    assert blocks_are_vertex_matchings(q, triples, q)
    blocks = residual_blocks(q, triples, q)
    assert sum(len(edges) for edges in blocks.values()) == 3


def test_residual_formula_is_exact():
    assert product_residual(101, (41, 43, 47)) == 8 * 41 * 43 * 47 - 101**3


def test_sts9_parallel_classes_are_matchings_and_cover_each_pair_once():
    classes = affine_plane_sts9_parallel_classes()
    assert len(classes) == 4
    pairs = []
    for parallel_class in classes:
        assert len(parallel_class) == 3
        assert len({v for edge in parallel_class for v in edge}) == 9
        for edge in parallel_class:
            pairs.extend(tuple(sorted(pair)) for pair in __import__("itertools").combinations(edge, 2))
    assert len(pairs) == 36
    assert len(set(pairs)) == 36


def test_matching_blocks_alone_do_not_give_sharp_fourth_trace():
    classes = affine_plane_sts9_parallel_classes()
    z = np.ones(9) / 3.0
    matrix = weighted_steiner_adjacency(classes, z)
    expected = (np.ones((9, 9)) - np.eye(9)) / 3.0
    assert np.allclose(matrix, expected)
    # The vertex hyperedge degree is four, whereas the fourth trace is much
    # larger than four.  Arithmetic ordering, not block matching alone, must
    # supply the desired cancellation.
    assert schatten_fourth_power(matrix) > 4.0

