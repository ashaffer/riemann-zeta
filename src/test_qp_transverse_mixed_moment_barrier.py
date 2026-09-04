from fractions import Fraction

import pytest

from qp_transverse_mixed_moment_barrier import (
    MixedMomentLedger,
    active_ledger,
    endpoint_ratio_from_negative_skew_bound,
    endpoint_ratio_from_skewness,
    minimum_bin_collision_count,
    two_point_standardized_moments,
    uniform_pair_energy_floor,
)


def test_active_cubic_ledger_recovers_fourth_moment_exponent() -> None:
    ledger = active_ledger()
    assert ledger.packet_exponent == Fraction(16, 33)
    assert ledger.cubic_schur_exponent == Fraction(8, 33)
    assert ledger.generic_leverage_exponent == Fraction(1, 2)
    assert ledger.transverse_exponent == Fraction(49, 66)


def test_two_point_laws_saturate_endpoint_formula() -> None:
    for probability in (0.2, 0.5, 0.8):
        endpoint, skewness = two_point_standardized_moments(probability)
        assert endpoint_ratio_from_skewness(skewness) == pytest.approx(endpoint)


def test_negative_skew_bound_is_positive_and_monotone() -> None:
    values = [endpoint_ratio_from_negative_skew_bound(value) for value in (0, 1, 4, 20)]
    assert values[0] == pytest.approx(1.0)
    assert all(left > right for left, right in zip(values, values[1:]))
    assert values[-1] >= 1.0 / 21.0
    with pytest.raises(ValueError):
        endpoint_ratio_from_negative_skew_bound(-1.0)


def test_exact_balanced_bin_collision_floor() -> None:
    # Ten items in three bins are balanced as 4,3,3.
    assert minimum_bin_collision_count(10, 3) == 34
    assert minimum_bin_collision_count(2, 5) == 2
    with pytest.raises(ValueError):
        minimum_bin_collision_count(1, 0)


def test_uniform_ordered_pair_energy_floor() -> None:
    # Four nodes give sixteen ordered pairs.  In four bins the exact balanced
    # floor is 4*4^2 / 4^2 = 4.
    assert uniform_pair_energy_floor(4, 4) == pytest.approx(4.0)
    with pytest.raises(ValueError):
        uniform_pair_energy_floor(0, 4)


def test_invalid_apertures_are_rejected() -> None:
    with pytest.raises(ValueError):
        MixedMomentLedger(Fraction(1))
    with pytest.raises(ValueError):
        MixedMomentLedger(Fraction(2))
