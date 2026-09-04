from fractions import Fraction

from qp_bp_rounding_hsm_ledger import shell_modulus_ledger, top_dfi_ledger


def test_shell_modulus_bp_has_only_a_tiny_conditional_margin() -> None:
    ledger = shell_modulus_ledger()
    assert ledger.first_relative_exponent == -Fraction(19, 1056)
    assert ledger.second_relative_exponent == -Fraction(1, 48)
    assert ledger.third_relative_exponent == -Fraction(5, 99)
    assert ledger.dominant_saving == Fraction(19, 1056)
    assert ledger.required_saving == Fraction(1, 66)
    assert ledger.conditional_margin == Fraction(1, 352)


def test_top_dfi_native_variables_miss_both_bp_interfaces() -> None:
    ledger = top_dfi_ledger()
    assert ledger.fan_in_modulus == Fraction(8, 25)
    assert ledger.product_difference_in_modulus == Fraction(16, 25)
    assert ledger.fan_below_lower_threshold == Fraction(101, 700)
    assert ledger.product_block_count_in_modulus == Fraction(7, 50)
    assert ledger.one_long_axis_cauchy_cost_in_modulus == Fraction(7, 100)
    assert ledger.one_long_axis_net_loss_in_modulus == Fraction(31, 800)
    assert ledger.unequal_theorem_bad_term_in_modulus == Fraction(1, 75)

