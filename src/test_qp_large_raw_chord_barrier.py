import math

from qp_four_cycle_residual_gate import prime_power_base
from qp_four_cycle_hostile_lab import shell_values
from qp_large_raw_chord_barrier import (
    FIXTURE_DEGREE,
    FIXTURE_NEIGHBORS,
    FIXTURE_Q,
    FIXTURE_ROWS,
    chord_ledger,
    cubic_residual,
    fixture_labels,
    literal_common_neighbors,
)


def test_fixture_is_a_globally_distinct_all_prime_shell() -> None:
    labels = fixture_labels()
    assert len(labels) == len(set(labels))
    assert all(prime_power_base(value) == value for value in labels)
    lower = FIXTURE_Q * math.exp(-0.2) / 2
    upper = FIXTURE_Q * math.exp(0.2) / 2
    assert all(lower < value < upper for value in labels[1:])


def test_all_eight_corners_obey_the_literal_product_window() -> None:
    for item in FIXTURE_NEIGHBORS:
        assert FIXTURE_ROWS[1] * item.second_color - FIXTURE_ROWS[0] * item.first_color == item.h
        assert abs(cubic_residual(FIXTURE_Q, FIXTURE_ROWS[0], item, second=False)) < FIXTURE_Q * FIXTURE_DEGREE
        assert abs(cubic_residual(FIXTURE_Q, FIXTURE_ROWS[1], item, second=True)) < FIXTURE_Q * FIXTURE_DEGREE


def test_the_literal_hard_window_has_exactly_the_four_displayed_neighbors() -> None:
    shell = tuple(map(int, shell_values(FIXTURE_Q / 2, 0.2, "prime_powers")))
    actual = literal_common_neighbors(
        FIXTURE_Q, FIXTURE_DEGREE, FIXTURE_ROWS, shell
    )
    assert actual == tuple(sorted(FIXTURE_NEIGHBORS, key=lambda item: item.h))


def test_two_isolated_chords_have_one_large_color_translation_and_two_carrier_drops() -> None:
    first = chord_ledger(FIXTURE_NEIGHBORS[0], FIXTURE_NEIGHBORS[2])
    second = chord_ledger(FIXTURE_NEIGHBORS[1], FIXTURE_NEIGHBORS[3])
    assert first.residual_shift == second.residual_shift == 14_754
    assert first.first_color_rise == second.first_color_rise == 135_816
    assert first.second_color_rise == second.second_color_rise == 122_166
    assert first.carrier_drop == 116_872
    assert second.carrier_drop == 132_186
    assert first.direction_gcd == second.direction_gcd == 6
    assert first.color_line_invariant == -15_630
    assert second.color_line_invariant == -13_854
    assert first.first_color_rise > FIXTURE_DEGREE
    assert first.direction_gcd < math.sqrt(FIXTURE_DEGREE)
    assert (first.first_product_change, first.second_product_change) == (-14_528, 382)
    assert (second.first_product_change, second.second_product_change) == (-26_370, -10_236)
