import pytest

from qp_four_cycle_permutation_sector import (
    Rectangle,
    canonical_hyperedge,
    classify_repeated_nodes,
    pair_unique,
    repeated_sector_ledger,
)


def test_adjacent_permutation_is_classified() -> None:
    rectangle = Rectangle(2, 7, 3, 5, 5, 3, 11, 13)
    result = classify_repeated_nodes(rectangle)
    assert result.adjacent_identical_hyperedge
    assert result.repeated_node


def test_opposite_cycle_forces_adjacent_permutation() -> None:
    # E11=E22={1,1,2}.  Pair uniqueness forces the adjacent cells
    # carrying the pair {1,1} to be the same unordered hyperedge.
    rectangle = Rectangle(1, 2, 2, 1, 1, 2, 2, 1)
    result = classify_repeated_nodes(rectangle)
    assert result.adjacent_identical_hyperedge


def test_opposite_transposition_is_two_square_sector() -> None:
    rectangle = Rectangle(2, 3, 3, 2, 5, 7, 11, 5)
    result = classify_repeated_nodes(rectangle)
    assert result.square_hyperedge
    assert not result.eight_distinct_labels


def test_opposite_color_equality_without_identical_edges() -> None:
    rectangle = Rectangle(2, 7, 3, 11, 5, 13, 17, 5)
    result = classify_repeated_nodes(rectangle)
    assert result.opposite_color_equality
    assert result.four_distinct_hyperedges


def test_exhaustive_multiset_classification() -> None:
    # Exhaust all 4,140 set partitions of the eight displayed positions via
    # restricted-growth strings.  This includes the generic case of just one
    # repeated pair and six otherwise distinct labels, which a small fixed
    # alphabet would miss.
    def equality_patterns(prefix: tuple[int, ...] = (0,)):
        if len(prefix) == 8:
            yield prefix
            return
        for value in range(max(prefix) + 2):
            yield from equality_patterns(prefix + (value,))

    checked = 0
    for pattern in equality_patterns():
        rectangle = Rectangle(*(value + 1 for value in pattern))
        if not rectangle.nondegenerate or not pair_unique(rectangle.hyperedges):
            continue
        result = classify_repeated_nodes(rectangle)
        if result.repeated_node:
            assert result.affordable_sector
        checked += 1
    assert checked > 200


def test_finite_weighted_ledger_accepts_complex_weights() -> None:
    rectangles = [
        Rectangle(2, 7, 3, 5, 5, 3, 11, 13),
        Rectangle(2, 3, 3, 2, 5, 7, 11, 5),
    ]
    # The two fixtures do not form one pair-unique ambient hypergraph, so
    # replay them separately.
    for rectangle in rectangles:
        weights = {
            node: complex(node % 3 - 1, node % 5 - 2)
            for node in rectangle.all_labels
        }
        ledger = repeated_sector_ledger([rectangle], weights)
        assert ledger["repeated_rectangles"] == 1
        assert ledger["absolute_mass"] <= ledger["certified_bound"] + 1e-12


def test_non_pair_unique_input_is_rejected() -> None:
    # The pair {2,3} has two different third nodes.
    assert not pair_unique(
        [canonical_hyperedge(2, 3, 5), canonical_hyperedge(2, 3, 7)]
    )
    # E11={2,3,5} and E12={2,3,7} assign two third nodes to {2,3}.
    rectangle = Rectangle(2, 11, 3, 7, 5, 3, 13, 17)
    with pytest.raises(ValueError):
        classify_repeated_nodes(rectangle)
