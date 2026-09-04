import math

from qp_cross_gram_moment_gate import (
    admissible_resonance_multiplicity,
    admissible_unit_resonance_multiplicity,
    critical_ap_energy_exponents,
    distinct_cell_correction_exponent,
    fejer_required_lag_magnitude,
    heath_brown_ledger,
    repeated_lag_pair_count,
    repeated_lag_weight,
)


def test_fixed_slice_heath_brown_exponents() -> None:
    ledger = heath_brown_ledger()
    assert math.isclose(ledger.packet_exponent, 0.038)
    assert math.isclose(ledger.pair_count_term, -0.924)
    assert math.isclose(ledger.repeated_difference_term, 0.038)
    assert math.isclose(
        ledger.aperture_term, 0.0475 + 25.0 / 33.0 - 1.0
    )
    assert ledger.pair_count_frobenius < ledger.required_residual
    assert ledger.aperture_frobenius < ledger.required_residual
    assert math.isclose(ledger.repeated_difference_gap, 0.038)


def test_repeated_ap_lag_has_no_rank_dilution() -> None:
    length = 10_000
    coefficient = length ** -0.5
    assert repeated_lag_pair_count(length, 1) == length - 1
    weight = repeated_lag_weight(length, coefficient, 1)
    assert math.isclose(weight, 1.0 - 1.0 / length)
    assert math.isclose(
        admissible_unit_resonance_multiplicity(coefficient),
        math.sqrt(length),
    )
    assert math.isclose(
        admissible_resonance_multiplicity(coefficient, 0.1),
        10.0 * math.sqrt(length),
    )


def test_critical_ap_saturates_energy_term() -> None:
    ledger = critical_ap_energy_exponents(0.019)
    assert math.isclose(ledger["critical_length"], 0.038)
    assert math.isclose(ledger["ap_energy"], 0.114)
    assert math.isclose(
        ledger["ap_energy"], ledger["large_value_second_term"]
    )
    assert ledger["first_term"] < 0.0


def test_distinct_cell_and_stable_ap_gates() -> None:
    correction = distinct_cell_correction_exponent()
    assert correction < 0.0
    assert math.isclose(correction, 50.0 / 33.0 - 1.6 + 0.076)

    lag_floor = fejer_required_lag_magnitude(100_000_000, 2.0)
    assert lag_floor > 0.019
