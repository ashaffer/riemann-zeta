from fractions import Fraction

import pytest

from completed_source_constructive_search import (
    annihilator_countermodel,
    causal_ramp_boundary_correction,
    cauchy_hankel_rank_witness,
    finite_source_word,
    four_cauchy_lerch_derivative,
    polynomial_contact_residual,
    regular_parametrix_residual,
)


def test_finite_source_word_exact_reconstruction_off_contact() -> None:
    for depth in range(1, 9):
        ledger = finite_source_word(depth, Fraction(2, 3), Fraction(7, 5))
        assert ledger.reconstruction_defect == 0


def test_every_finite_depth_retains_full_contact_charge() -> None:
    for depth in range(1, 20):
        ledger = finite_source_word(depth, -1, Fraction(11, 7))
        assert ledger.old_operator_a == 0
        assert ledger.factor_term == 0
        assert ledger.remainder_term == ledger.charge_gamma


def test_regular_polynomial_cannot_change_contact_residual() -> None:
    for coefficients in ((0,), (1,), (1, -1, 1), (7, -3, 0, 5)):
        ledger = polynomial_contact_residual(coefficients, Fraction(-9, 4))
        assert ledger.residual_multiplier_at_contact == 1
        assert ledger.residual_charge == ledger.charge_gamma


def test_annihilator_countermodel_has_zero_compressed_equations() -> None:
    ledger = annihilator_countermodel()
    zero = Fraction(0)
    assert all(entry == zero for row in ledger.annihilator_times_source for entry in row)
    assert all(entry == zero for row in ledger.old_compression for entry in row)


def test_annihilator_countermodel_still_charges_old_kernel() -> None:
    ledger = annihilator_countermodel()
    assert ledger.exterior_charge == (0, 1, 0)
    assert ledger.exterior_charge_norm_squared == 1


@pytest.mark.parametrize("order", range(1, 9))
def test_cauchy_hankel_witness_has_full_finite_rank(order: int) -> None:
    ledger = cauchy_hankel_rank_witness(order)
    assert ledger.agreement_defect == 0
    assert ledger.determinant_by_elimination > 0


def test_regular_parametrix_is_identity_on_an_annihilator_zero() -> None:
    for value in (-100, -1, 0, 1, 100):
        assert regular_parametrix_residual(value, 0) == 1


@pytest.mark.parametrize("q", (Fraction(3, 2), 2, 3, 7, 20))
def test_four_cauchy_lerch_derivative_identity(q: Fraction | int) -> None:
    ledger = four_cauchy_lerch_derivative(q)
    assert ledger.agreement_defect == 0
    assert ledger.four_channel_sum == 4 * ledger.q**3 / (ledger.q**4 - 1)
    assert ledger.lerch_derivative == -2 * ledger.q**3 / (ledger.q**4 - 1)


def test_causal_ramp_retains_exact_initial_collar() -> None:
    ramp, source, collar = causal_ramp_boundary_correction(Fraction(5, 3), -7)
    assert ramp == source - collar
    assert collar == Fraction(5, 3)


def test_invalid_depth_and_order_are_rejected() -> None:
    with pytest.raises(ValueError):
        finite_source_word(0, -1)
    with pytest.raises(ValueError):
        cauchy_hankel_rank_witness(0)
    with pytest.raises(ValueError):
        four_cauchy_lerch_derivative(1)
    with pytest.raises(ValueError):
        four_cauchy_lerch_derivative(-1)
