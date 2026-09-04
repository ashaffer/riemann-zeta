from fractions import Fraction

from qp_dfi_bandpass_zero_arc import dfi_bandpass_zero_arc_ledger


def test_balanced_bandpass_scales() -> None:
    ledger = dfi_bandpass_zero_arc_ledger()
    assert ledger.degree_exponent == Fraction(16, 33)
    assert ledger.delta_modulus_exponent == Fraction(25, 33)
    assert ledger.mismatch_exponent == Fraction(34, 33)
    assert ledger.transition_modulus_exponent == Fraction(9, 33)
    assert ledger.mismatch_over_delta_modulus_exponent == Fraction(3, 11)
    assert ledger.mismatch_over_delta_modulus_in_degree == Fraction(9, 16)
    assert ledger.maximal_positive_frozen_extension_in_degree == Fraction(1, 16)
    assert ledger.endpoint_positive_frozen_loss_in_degree == Fraction(5, 8)
    assert (
        ledger.mismatch_over_delta_modulus_in_degree
        + ledger.maximal_positive_frozen_extension_in_degree
        == ledger.endpoint_positive_frozen_loss_in_degree
    )


def test_status_does_not_promote_zero_arc() -> None:
    ledger = dfi_bandpass_zero_arc_ledger()
    assert ledger.nonzero_farey_sector_rapidly_decaying
    assert not ledger.noncoprime_sector_requires_separate_poisson
    assert not ledger.ramanujan_axis_requires_separate_absolute_bound
    assert not ledger.zero_arc_bound_proved
    assert not ledger.four_cycle_improvement_proved
