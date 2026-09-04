from fractions import Fraction

from qp_four_cycle_parabolic_global_audit import (
    actual_prime_scaled_relation_ledger,
    parabolic_scalar_barrier_ledger,
)


def test_actual_prime_colors_do_not_force_raw_additivity() -> None:
    ledger = actual_prime_scaled_relation_ledger(
        166_013,
        (93_607, 87_383, 79_229, 73_961),
        (11, 13),
        (14, 15),
    )
    assert ledger.all_colors_prime
    assert ledger.shell_log_radius < 0.2
    assert ledger.weighted_relation_defect == 0
    assert ledger.raw_additive_defect == 956
    assert ledger.color_determinant == -380


def test_exceptional_parabolic_scalar_balance_stops_at_eleven_eighths() -> None:
    ledger = parabolic_scalar_barrier_ledger()
    assert ledger.split_threshold == Fraction(3, 8)
    assert ledger.relation_height_cutoff == Fraction(1, 4)
    assert ledger.direction_count == Fraction(1, 2)
    assert ledger.fixed_relation_color_mass == Fraction(1, 2)
    assert ledger.chart_length == Fraction(3, 8)
    assert ledger.low_trace == Fraction(11, 8)
    assert ledger.high_trace == Fraction(11, 8)
