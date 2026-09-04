from fractions import Fraction

import pytest

from qp_calibrated_cubic_projection_nogo import (
    CalibratedCubicModel,
    active_exponent,
    calibration_average,
    phase_vector_counts,
    standardized_two_point_atoms,
    two_point_moments,
)


def test_exact_calibration_and_phase_counts() -> None:
    assert phase_vector_counts(100) == (25, 75)
    average_phase, average_residual = calibration_average(100)
    assert average_phase == pytest.approx(-0.5)
    assert average_residual == pytest.approx(0.0)


@pytest.mark.parametrize("skew", [0.0, 1.0, 3.5, 10.0])
def test_two_point_law_has_requested_signed_moments(skew: float) -> None:
    mean, variance, third = two_point_moments(skew)
    assert mean == pytest.approx(0.0, abs=1e-12)
    assert variance == pytest.approx(1.0)
    assert third == pytest.approx(-skew)


def test_large_atom_is_negative_for_negative_skew() -> None:
    probability, positive, negative = standardized_two_point_atoms(8.0)
    assert probability > 0.5
    assert 0.0 < positive < 1.0
    assert negative < -1.0


def test_witness_saturates_joint_power_scale() -> None:
    model = CalibratedCubicModel(dimension=10_000, packet_factor=100.0)
    assert model.witness_joint_value >= model.asymptotic_joint_floor
    assert model.carrier_norm == pytest.approx((3 * 10_000 / 4) ** 0.5)


def test_active_exponent_is_49_over_66() -> None:
    assert active_exponent() == Fraction(49, 66)


def test_invalid_model_parameters_are_rejected() -> None:
    with pytest.raises(ValueError):
        CalibratedCubicModel(dimension=10, packet_factor=2.0)
    with pytest.raises(ValueError):
        CalibratedCubicModel(dimension=100, packet_factor=100.0)
    with pytest.raises(ValueError):
        standardized_two_point_atoms(-1.0)
