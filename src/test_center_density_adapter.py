from fractions import Fraction

import pytest

from center_density_adapter import (
    CENTER_EXCEPTION_SAVING,
    CenterDensityLedger,
    absolute_witness_min_density,
    center_exception_saving,
    center_sets_must_intersect,
    eligible_interval_min_fraction,
    ledger_payload,
    negative_arc_density,
    phase_discrepancy_saving,
)


def test_exact_center_exception_margin() -> None:
    assert center_exception_saving(
        Fraction(1187, 13000), Fraction(379, 20000)
    ) == Fraction(3137, 520000)
    assert CENTER_EXCEPTION_SAVING == Fraction(3137, 520000)


def test_optimized_phase_discrepancy_savings() -> None:
    assert phase_discrepancy_saving(Fraction(50, 33)) == Fraction(16, 99)
    assert phase_discrepancy_saving(Fraction(1)) == Fraction(1, 4)
    with pytest.raises(ValueError):
        phase_discrepancy_saving(Fraction(2))


def test_negative_arc_density() -> None:
    assert negative_arc_density(0.75) == pytest.approx(0.2300534561626159)
    assert eligible_interval_min_fraction(0.2) == pytest.approx(
        0.22140275816016985
    )
    assert absolute_witness_min_density(0.75, 0.2) == pytest.approx(
        0.05093446974133945
    )
    with pytest.raises(ValueError):
        negative_arc_density(1.0)


def test_strict_center_set_intersection_condition() -> None:
    margin = Fraction(3137, 520000)
    assert center_sets_must_intersect(margin, Fraction(1, 200))
    assert not center_sets_must_intersect(margin, margin)
    assert CenterDensityLedger().closes_conditionally(Fraction(1, 200))


def test_payload_keeps_open_statuses() -> None:
    payload = ledger_payload()
    assert payload["pointwise_upper_exponent"] == "379/20000"
    assert payload["center_exception_saving"] == "3137/520000"
    assert payload["averaged_gcg4_status"] == "OPEN"
    assert payload["event_conditioned_density_ltrad_status"] == "OPEN"
    assert payload["uniform_zero_free_strip_status"] == "OPEN"
    assert payload["RH_status"] == "OPEN"
