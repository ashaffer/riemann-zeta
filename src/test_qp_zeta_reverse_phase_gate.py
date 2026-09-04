import pytest

from qp_zeta_reverse_phase_gate import (
    logarithmic_partition_count,
    minimum_atoms_for_mass_event,
    negative_mass_from_modulus,
    phase_discrepancy_exponents,
    reverse_bridge_ledger,
    singleton_mass_depth,
    singleton_probability_depth,
    turan_half_power_coverage,
    turan_strip_width,
)


def test_project_partition_count() -> None:
    assert logarithmic_partition_count(0.2) == 7


def test_phase_discrepancy_has_power_saving() -> None:
    exponents = phase_discrepancy_exponents(50.0 / 33.0, 0.1)
    assert all(value < 0.0 for value in exponents.values())
    assert exponents["upper_height"] == pytest.approx(-0.19242424242424239)


def test_phase_alignment_loses_only_a_constant() -> None:
    assert negative_mass_from_modulus(0.14) == pytest.approx(0.015)


def test_singleton_normalization_defect_is_removed() -> None:
    assert singleton_probability_depth() == 1.0
    assert singleton_mass_depth(10_000.0) == pytest.approx(0.0001)


def test_mass_event_forces_macroscopic_support() -> None:
    assert minimum_atoms_for_mass_event(10_000.0, 0.25) == 1000


def test_reverse_bridge_width() -> None:
    ledger = reverse_bridge_ledger()
    assert ledger["natural_saving"] == pytest.approx(0.019)
    assert ledger["strip_width"] == pytest.approx(0.0001572516)
    assert turan_strip_width(0.019, 50.0 / 33.0) == pytest.approx(0.0001572516)


def test_turan_half_power_coverage_at_project_slice() -> None:
    coverage = turan_half_power_coverage(0.019, 50.0 / 33.0)
    assert coverage == pytest.approx(0.944138238654184, abs=1e-12)
    assert coverage < 1.0
    assert turan_half_power_coverage(0.019, 1.44) > 1.0


def test_invalid_discrepancy_parameters() -> None:
    with pytest.raises(ValueError):
        phase_discrepancy_exponents(1.9, 0.2)
