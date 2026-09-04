from fractions import Fraction

from qp_selected_degree_mellin_bdh_gate import (
    heath_brown_zero_line_scales,
    selected_degree_mellin_ledger,
)


def test_balanced_selected_degree_mellin_deficits() -> None:
    ledger = selected_degree_mellin_ledger()
    assert ledger.mellin_bandwidth_exponent == Fraction(25, 8)
    assert ledger.desired_squared_exponent == Fraction(23, 8)
    assert ledger.ordinary_sampling_squared_exponent == Fraction(63, 16)
    assert ledger.ordinary_sampling_deficit == Fraction(17, 16)
    assert ledger.heath_brown_nonpolar_squared_exponent == Fraction(33, 8)
    assert ledger.heath_brown_nonpolar_deficit == Fraction(5, 4)
    assert ledger.heath_brown_support_threshold_exponent == Fraction(25, 8)
    assert ledger.improved_mean_shift_exponent == 1


def test_heath_brown_zero_line_translation() -> None:
    scales = heath_brown_zero_line_scales(
        q_exponent=Fraction(33, 16),
        bandwidth_exponent=Fraction(25, 8),
        beta_support_exponent=Fraction(33, 16),
    )
    assert scales.coherent_term == Fraction(165, 16)
    assert scales.nonpolar_term == Fraction(29, 4)
    assert scales.mellin_weighted_coherent_term == Fraction(115, 16)
    assert scales.mellin_weighted_nonpolar_term == Fraction(33, 8)

