from fractions import Fraction

from qp_four_cycle_twenty_one_sixty_fourths import (
    FOURTH_TRACE_EXPONENT,
    MAX_SLICE_EXPONENT,
    MAX_TWO_MINIMUM_PRODUCT,
    OPERATOR_EXPONENT,
    TRANSVERSE_EXPONENT,
    curvature_times_gap_mass_exponent,
)


def test_global_exponent_ledger() -> None:
    assert MAX_TWO_MINIMUM_PRODUCT == Fraction(11, 8)
    assert MAX_SLICE_EXPONENT == Fraction(5, 16)
    assert FOURTH_TRACE_EXPONENT == Fraction(21, 16)
    assert OPERATOR_EXPONENT == Fraction(21, 64)
    assert TRANSVERSE_EXPONENT == Fraction(29, 44)


def test_curvature_cancels_height_exactly() -> None:
    for numerator in range(0, 65):
        assert curvature_times_gap_mass_exponent(
            Fraction(numerator, 64)
        ) == 1

