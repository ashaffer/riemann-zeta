from fractions import Fraction

import pytest

from qp_sector_combination_gate import SectorCombinationLedger, active_ledger


def test_active_baseline_and_burgess_threshold() -> None:
    ledger = active_ledger()
    assert ledger.residual_exponent == Fraction(16, 33)
    assert ledger.raw_skew_exponent == Fraction(8, 33)
    assert ledger.full_shell_baseline == Fraction(49, 66)
    assert ledger.burgess_skew_exponent == Fraction(227, 1056)
    assert ledger.burgess_threshold == Fraction(29, 1056)


def test_side_dominance_piecewise_ledger() -> None:
    ledger = active_ledger()
    theta = Fraction(1, 100)
    assert ledger.side_dominant_exponent(theta) == Fraction(49, 66) - theta
    assert ledger.side_dominant_exponent(Fraction(1, 20)) == Fraction(755, 1056)


def test_central_dominance_piecewise_ledger() -> None:
    epsilon = Fraction(1, 100)
    ledger = active_ledger(epsilon)
    theta_small = Fraction(1, 100)
    assert (
        ledger.central_dominant_exponent(theta_small)
        == Fraction(49, 66) - 2 * theta_small
    )
    assert ledger.central_dominant_exponent(Fraction(8, 33)) == Fraction(17, 66)
    assert ledger.central_dominant_exponent(Fraction(1, 3)) == (
        Fraction(1, 4) - epsilon / 2
    )


def test_density_one_active_ledger() -> None:
    h = Fraction(16, 33)
    density_skew = h / 4 + Fraction(1, 16)
    assert density_skew == Fraction(97, 528)
    assert Fraction(1, 2) + density_skew == Fraction(361, 528)
    assert h / 2 - density_skew == Fraction(31, 528)


def test_invalid_parameters() -> None:
    with pytest.raises(ValueError):
        SectorCombinationLedger(Fraction(3, 2), Fraction(1, 4))
    with pytest.raises(ValueError):
        SectorCombinationLedger(Fraction(50, 33), Fraction(1, 2))
    with pytest.raises(ValueError):
        active_ledger().side_dominant_exponent(Fraction(-1, 10))
