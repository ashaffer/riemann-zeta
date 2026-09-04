from collections import Counter
from fractions import Fraction

import pytest

from qp_collective_dyadic_gate import (
    balanced_packet_overlap_ledger,
    collective_dyadic_ledger,
    completion_pair_dyadic_ledger,
    completion_secant_peaks,
    rooted_surrogate_ledger,
    signed_dyadic_cell,
    weighted_packet_overlap_ledger,
)
from qp_four_cycle_translation_grid import translation_grid_entry


def test_signed_cells_are_half_open_and_unique() -> None:
    assert signed_dyadic_cell(1, -1) == (1, -1, 0, 0)
    assert signed_dyadic_cell(7, -8) == (1, -1, 2, 3)
    assert signed_dyadic_cell(-16, 31) == (-1, 1, 4, 4)


def test_collective_bucketing_is_an_exact_partition() -> None:
    ledger = collective_dyadic_ledger(
        [
            (1, 1, Fraction(1, 3)),
            (2, -3, Fraction(2, 3)),
            (-4, 7, Fraction(5, 2)),
            (-4, 7, Fraction(1, 2)),
        ]
    )

    assert ledger.item_count == 4
    assert ledger.occupied_cells == 3
    assert ledger.total_weight == 4
    assert ledger.partition_is_exact
    assert ledger.pigeonhole_bound_holds
    assert ledger.admissible_cell_count == 4 * 3 * 3


def test_completion_pair_bridge_retains_factorial_multiplicity_and_weight() -> None:
    first_colors = (2, 3, 5, 7)
    second_colors = (11, 13, 17, 19)
    groups = {
        first_colors: ((3, 5, 7, 11), (5, 8, 11, 17)),
        second_colors: (
            (2, 3, 5, 7),
            (3, 5, 7, 11),
            (5, 8, 11, 17),
        ),
    }
    weights = {first_colors: Fraction(3, 2), second_colors: Fraction(1, 3)}
    ledger = completion_pair_dyadic_ledger(groups, weights)

    assert completion_secant_peaks(groups[first_colors][0], groups[first_colors][1]) == (
        -1,
        -2,
    )
    assert ledger.item_count == 2 * 1 + 3 * 2
    assert ledger.total_weight == 2 * Fraction(3, 2) + 6 * Fraction(1, 3)
    assert ledger.partition_is_exact


def test_root_maximum_can_lose_a_polynomial_factor() -> None:
    roots = {root: Fraction(1) for root in range(257)}
    ledger = rooted_surrogate_ledger(roots)

    assert ledger.total_weight == 257
    assert ledger.maximum_root_weight == 1
    assert ledger.replacement_factor == 257


def test_gate_rejects_precisely_the_two_unsafe_inputs() -> None:
    with pytest.raises(ValueError, match="nonzero"):
        signed_dyadic_cell(0, 1)
    with pytest.raises(ValueError, match="nonnegative"):
        collective_dyadic_ledger([(1, 1, Fraction(-1))])


def test_weighted_packet_overlap_charges_participation_not_packet_count() -> None:
    disjoint = weighted_packet_overlap_ledger(
        (Fraction(7), (f"left-{index}",), (f"right-{index}",))
        for index in range(100)
    )
    assert disjoint.packet_count == 100
    assert disjoint.total_local_bound == 700
    assert disjoint.maximum_left_load == 7
    assert disjoint.maximum_right_load == 7
    assert disjoint.squared_operator_bound == 49

    common_left = weighted_packet_overlap_ledger(
        (Fraction(7), ("common",), (f"right-{index}",))
        for index in range(100)
    )
    assert common_left.maximum_left_load == 700
    assert common_left.maximum_right_load == 7
    assert common_left.squared_operator_bound == 4_900


def test_free_packet_balancing_uses_dual_left_and_right_charges() -> None:
    ledger = balanced_packet_overlap_ledger(
        [
            (Fraction(6), Fraction(3), ("left-a",), ("right",)),
            (Fraction(10), Fraction(5), ("left-b",), ("right",)),
        ]
    )
    assert ledger.packet_count == 2
    assert ledger.maximum_left_load == 5
    assert ledger.maximum_right_load == Fraction(6 * 6, 3) + Fraction(10 * 10, 5)
    assert ledger.squared_operator_bound == 160

    with pytest.raises(ValueError, match="positive"):
        balanced_packet_overlap_ledger([(Fraction(1), Fraction(0), (), ())])


def test_translation_grid_can_concentrate_many_pairs_in_one_signed_cell() -> None:
    completions = []
    for translation in range(-165, 158):
        first_row, first_column, _ = translation_grid_entry(
            5_720_399,
            8,
            7,
            15,
            translation,
            0,
            0,
            column_step=14,
        )
        second_row, _, _ = translation_grid_entry(
            5_720_399,
            8,
            7,
            15,
            translation,
            1,
            0,
            column_step=14,
        )
        _, second_column, _ = translation_grid_entry(
            5_720_399,
            8,
            7,
            15,
            translation,
            0,
            1,
            column_step=14,
        )
        completions.append(
            (first_row, second_row, first_column, second_column)
        )

    cells: Counter[tuple[int, int, int, int]] = Counter()
    for first_index, first in enumerate(completions):
        for second_index, second in enumerate(completions):
            if first_index == second_index:
                continue
            cells[signed_dyadic_cell(*completion_secant_peaks(first, second))] += 1

    assert len(completions) == 323
    assert sum(cells.values()) == 104_006
    assert len(cells) == 32
    assert max(cells.values()) == 14_351
