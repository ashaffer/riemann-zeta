from fractions import Fraction

import pytest

from qp_sparse_self_correlated_energy import (
    CRITICAL_MU,
    classical_energy_exponent,
    critical_classical_bound,
    elliott_target_energy_exponent,
    mixed_energy_exponent,
    mixed_upper_bound,
    principal_energy_exponent,
    sparse_energy_ledger,
)


def test_critical_energy_ledger() -> None:
    ledger = sparse_energy_ledger()
    assert ledger.critical_support_in_d == Fraction(11, 8)
    assert ledger.critical_support_in_q == Fraction(2, 3)
    assert ledger.classical_energy == Fraction(71, 16)
    assert ledger.mixed_energy == Fraction(131, 32)
    assert ledger.principal_energy == Fraction(65, 16)
    assert ledger.proved_saving == Fraction(11, 32)
    assert ledger.principal_ceiling == Fraction(3, 8)
    assert ledger.open_gap == Fraction(1, 32)


def test_elliott_target_meets_the_principal_scale() -> None:
    ledger = sparse_energy_ledger()
    assert elliott_target_energy_exponent(CRITICAL_MU) == Fraction(65, 16)
    assert ledger.conjectural_energy == ledger.principal_energy


def test_raw_exponent_formulas() -> None:
    mu = Fraction(11, 8)
    assert classical_energy_exponent(mu) == Fraction(71, 16)
    assert mixed_energy_exponent(mu) == Fraction(131, 32)
    assert principal_energy_exponent(mu) == Fraction(65, 16)
    assert mixed_energy_exponent(mu) > principal_energy_exponent(mu)


def test_proper_power_piece_is_below_the_principal_obstruction() -> None:
    ledger = sparse_energy_ledger()
    assert ledger.proper_power_energy == Fraction(251, 64)
    assert ledger.principal_energy == Fraction(260, 64)
    assert ledger.proper_power_energy < ledger.principal_energy


def test_numeric_bounds_are_positive_and_below_classical_at_sample_scale() -> None:
    q, support_size, determinant_width = 20_011, 737, 121
    mixed = mixed_upper_bound(q, support_size, determinant_width)
    classical = critical_classical_bound(q, support_size, determinant_width)
    assert 0 < mixed < classical


def test_invalid_numeric_scales_are_rejected() -> None:
    with pytest.raises(ValueError, match="positive"):
        mixed_upper_bound(101, 0, 10)
    with pytest.raises(ValueError, match="positive"):
        critical_classical_bound(101, 10, -1)
