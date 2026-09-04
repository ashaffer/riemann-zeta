from fractions import Fraction

import pytest

from qp_four_cycle_l43_profile import (
    chapman_mudgal_hsm_ledger,
    l43_effective_support,
    operator_profile_exponent,
    three_coordinate_projections_are_injective,
    trace_profile_exponent,
    transverse_profile_exponent,
)


def test_three_coordinate_matching() -> None:
    # The four tuples form a partial 3-dimensional permutation tensor.
    colors = (
        (11, 13, 17, 19),
        (11, 13, 23, 29),
        (11, 31, 17, 37),
        (41, 13, 17, 43),
    )
    assert three_coordinate_projections_are_injective(colors)

    collision = colors + ((11, 13, 17, 47),)
    assert not three_coordinate_projections_are_injective(collision)


def test_effective_support_for_flat_weights() -> None:
    for support in (1, 2, 7, 32):
        weights = [support ** (-0.5)] * support
        assert l43_effective_support(weights) == pytest.approx(float(support))


def test_exact_piecewise_trace_profile() -> None:
    checkpoints = {
        Fraction(0): Fraction(1),
        Fraction(1, 2): Fraction(1),
        Fraction(5, 8): Fraction(9, 8),
        Fraction(3, 4): Fraction(5, 4),
        Fraction(15, 16): Fraction(5, 4),
        Fraction(31, 32): Fraction(41, 32),
        Fraction(1): Fraction(21, 16),
        Fraction(2): Fraction(21, 16),
    }
    for mu, expected in checkpoints.items():
        assert trace_profile_exponent(mu) == expected


def test_operator_and_transverse_endpoints() -> None:
    assert operator_profile_exponent(Fraction(1, 2)) == Fraction(1, 4)
    assert transverse_profile_exponent(Fraction(1, 2)) == Fraction(41, 66)

    assert operator_profile_exponent(Fraction(3, 4)) == Fraction(5, 16)
    assert transverse_profile_exponent(Fraction(3, 4)) == Fraction(43, 66)

    assert operator_profile_exponent(Fraction(1)) == Fraction(21, 64)
    assert transverse_profile_exponent(Fraction(1)) == Fraction(29, 44)


def test_negative_profile_is_rejected() -> None:
    with pytest.raises(ValueError):
        trace_profile_exponent(Fraction(-1, 10))


def test_chapman_mudgal_hsm_no_match_ledger() -> None:
    ledger = chapman_mudgal_hsm_ledger()

    assert ledger.product_scale_exponent_in_q == Fraction(84, 33)
    assert ledger.coefficient_density_exponent_in_q == Fraction(16, 33)
    assert ledger.hsm_target_exponent_in_q == Fraction(100, 33)

    assert ledger.formal_weighted_error_exponent_in_q == Fraction(92, 33)
    assert ledger.formal_margin_exponent_in_q == Fraction(8, 33)

    assert ledger.four_kernel_twist_count_exponent_in_q == Fraction(32, 33)
    assert ledger.absolute_twist_error_exponent_in_q == Fraction(108, 33)
    assert ledger.absolute_twist_loss_exponent_in_q == Fraction(8, 33)

    assert ledger.unweighted_theorem_only
    assert not ledger.weighted_stability_is_proved
    assert not ledger.weighted_main_term_cancellation_is_proved
    assert not ledger.closes_hsm
