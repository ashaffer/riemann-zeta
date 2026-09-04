from fractions import Fraction

import pytest

from qp_weighted_near_determinant_literature_gate import (
    NearDeterminantLedger,
    active_ledger,
    centered_linear_phase_is_integral,
    revival_lower_bound_scale,
    robert_sargos_curvature,
)


def test_active_power_ledger() -> None:
    ledger = active_ledger()
    assert ledger.residual_exponent == Fraction(16, 33)
    assert ledger.schur_skew_exponent == Fraction(8, 33)
    assert ledger.current_transverse_exponent == Fraction(49, 66)
    assert ledger.conjectural_quarter_skew_exponent == Fraction(4, 33)
    assert ledger.conjectural_quarter_transverse_exponent == Fraction(41, 66)


def test_revival_scale_matches_quarter_power() -> None:
    ledger = active_ledger()
    assert ledger.revival_window_exponent == Fraction(8, 33)
    assert ledger.revival_l3_gain_exponent == Fraction(4, 33)


def test_formal_bettin_chandee_number_is_marked_only_as_formal() -> None:
    ledger = active_ledger()
    assert ledger.formal_bettin_chandee_saving == Fraction(27, 220)
    assert ledger.formal_bettin_chandee_transverse_exponent == Fraction(409, 660)


def test_revival_lower_bound_normalization() -> None:
    assert revival_lower_bound_scale(100.0, 4.0, 4) == pytest.approx(200.0)
    with pytest.raises(ValueError):
        revival_lower_bound_scale(0.0, 4.0, 4)
    with pytest.raises(ValueError):
        revival_lower_bound_scale(100.0, 4.0, 0)


def test_half_integer_center_linear_alignment() -> None:
    # Y=10.5 and p=11: 2p-2Y=1, so every integer revival aligns.
    assert centered_linear_phase_is_integral(11, 21, 7)
    with pytest.raises(ValueError):
        centered_linear_phase_is_integral(11, 20, 7)


def test_robert_sargos_excludes_the_linear_exponent() -> None:
    assert robert_sargos_curvature(Fraction(1)) == 0
    assert robert_sargos_curvature(Fraction(2)) == 2


def test_invalid_aperture() -> None:
    with pytest.raises(ValueError):
        NearDeterminantLedger(Fraction(1))
    with pytest.raises(ValueError):
        NearDeterminantLedger(Fraction(2))
