from fractions import Fraction

from qp_two_sided_residual_incidence_audit import (
    exact_bezout_square_pool,
    exact_dot_levels,
    exact_parabola_matching,
    greedy_two_sided_general_position,
    has_no_three_collinear,
    modular_inverse_parabola,
    modular_parabola_zero_level,
    two_sided_exponent_cap,
    two_sided_line_cap,
)


def test_two_sided_cap_is_the_minimum_of_the_one_sided_caps() -> None:
    ledger = two_sided_line_cap(101, (40, 60), (100, 120))
    assert ledger.combined_cap == min(ledger.row_cap, ledger.carrier_cap)
    assert ledger.row_cap < ledger.carrier_cap


def test_exponent_cap_has_no_spurious_product_gain() -> None:
    ledger = two_sided_exponent_cap(
        Fraction(11, 16),
        (Fraction(11, 16), Fraction(11, 16)),
        (Fraction(1), Fraction(1)),
    )
    assert ledger.row_exponent == Fraction(11, 32)
    assert ledger.carrier_exponent == Fraction(21, 32)
    assert ledger.combined_exponent == ledger.row_exponent


def test_modular_parabola_saturates_both_square_caps_at_exact_zero_level() -> None:
    matching = modular_parabola_zero_level(11)
    rows = [row for row, _ in matching]
    carriers = [carrier for _, carrier in matching]
    assert len(matching) == 11
    assert has_no_three_collinear(rows)
    assert has_no_three_collinear(carriers)
    assert exact_dot_levels(matching) == {0: 11}


def test_nonzero_modular_level_fragments_after_integer_lifting() -> None:
    prime = 17
    matching = modular_inverse_parabola(prime)
    rows = [row for row, _ in matching]
    carriers = [carrier for _, carrier in matching]
    assert has_no_three_collinear(rows)
    assert has_no_three_collinear(carriers)
    levels = exact_dot_levels(matching)
    assert all((level - 2) % prime == 0 for level in levels)
    assert len(levels) > 1


def test_exact_nonzero_parabola_has_no_rich_line() -> None:
    matching = [exact_parabola_matching(parameter) for parameter in range(1, 9)]
    rows = [row for row, _ in matching]
    carriers = [carrier for _, carrier in matching]
    assert exact_dot_levels(matching) == {1: 8}
    assert has_no_three_collinear(rows)
    assert has_no_three_collinear(carriers)


def test_balanced_bezout_pool_has_exact_level_and_large_general_position_sample() -> None:
    pool = exact_bezout_square_pool(19)
    assert len(pool) > 100
    assert exact_dot_levels(pool) == {1: len(pool)}
    assert max(abs(coordinate) for pair in pool for point in pair for coordinate in point) <= 60
    sample = max(
        (greedy_two_sided_general_position(pool, seed) for seed in range(5)),
        key=len,
    )
    assert len(sample) >= 8
    assert has_no_three_collinear([row for row, _ in sample])
    assert has_no_three_collinear([carrier for _, carrier in sample])

