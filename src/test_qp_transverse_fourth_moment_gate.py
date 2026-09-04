from fractions import Fraction

import pytest

from qp_transverse_fourth_moment_gate import (
    FourthMomentLedger,
    active_ledger,
    centered_positive_cap_lower,
    convolution_cauchy_bound,
)


def test_active_exponents_are_exact() -> None:
    ledger = active_ledger()
    assert ledger.unresolved_pair_exponent == Fraction(16, 33)
    assert ledger.kurtosis_exponent == Fraction(16, 33)
    assert ledger.transverse_depth_exponent == Fraction(49, 66)
    assert ledger.gain_over_dimension_floor == Fraction(17, 66)
    assert ledger.even_moment_packet_exponent(2) == Fraction(16, 33)
    assert ledger.even_moment_depth_exponent(2) == Fraction(49, 66)


def test_fourth_moment_is_optimal_in_fixed_even_moment_family() -> None:
    ledger = active_ledger()
    exponents = [ledger.even_moment_depth_exponent(k) for k in range(2, 9)]
    assert exponents == sorted(exponents)
    assert all(exponent > exponents[0] for exponent in exponents[1:])
    assert ledger.even_moment_depth_exponent(3) == Fraction(115, 132)
    with pytest.raises(ValueError):
        ledger.even_moment_depth_exponent(1)


def test_gain_is_positive_exactly_above_linear_aperture() -> None:
    ledger = FourthMomentLedger(Fraction(6, 5))
    assert ledger.gain_over_dimension_floor == Fraction(1, 10)
    with pytest.raises(ValueError):
        FourthMomentLedger(Fraction(1))
    with pytest.raises(ValueError):
        FourthMomentLedger(Fraction(2))


def test_centered_moment_bound_on_two_point_law() -> None:
    # Z is +/-1 with equal probability: V=W=1 and sup Z=1.
    assert centered_positive_cap_lower(1.0, 1.0) == 0.5
    assert centered_positive_cap_lower(0.0, 0.0) == 0.0


def test_centered_moment_bound_rejects_impossible_input() -> None:
    with pytest.raises(ValueError):
        centered_positive_cap_lower(1.0, 0.0)
    with pytest.raises(ValueError):
        centered_positive_cap_lower(-1.0, 1.0)


def test_weighted_product_convolution_cauchy_bound() -> None:
    coefficients = {11: 1.25, 13: -0.75, 17: 2.0, 19: -1.5}
    lhs, rhs = convolution_cauchy_bound(coefficients)
    assert lhs <= rhs + 1e-12
    assert lhs > 0.0


def test_convolution_bound_handles_colliding_products() -> None:
    # 6*35=10*21 creates a genuinely nontrivial product collision.
    coefficients = {6: 1.0, 10: -2.0, 21: 0.5, 35: 3.0}
    lhs, rhs = convolution_cauchy_bound(coefficients)
    assert lhs <= rhs + 1e-12
