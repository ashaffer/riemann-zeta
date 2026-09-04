from fractions import Fraction
import math

import numpy as np

from qp_actual_prime_weight_barrier import (
    complex_characteristic,
    exact_positive_quadrature_degree_cap,
    half_grid_ledger,
    half_period_log_grid,
    normalized_cosine,
    one_packet_positive_range,
    packet_feature_hull,
    projected_single_packet_gram,
    single_cosine_tilt_moment,
    square_reweight_covariance_residual,
    square_reweight_ledger,
    square_reweighted_characteristic_direct,
    square_reweighted_characteristic_shifted,
    subset_bad_peak_probability_upper,
    worst_half_grid_perturbation_bound,
)


def test_half_grid_exact_rational_exponents_are_strict_savings() -> None:
    ledger = half_grid_ledger()
    assert Fraction(ledger.first_deleted_mass_exponent) == Fraction(-373, 4125)
    assert Fraction(ledger.component_padding_exponent) == Fraction(-746, 4125)
    assert Fraction(ledger.first_deleted_mass_exponent) < 0
    assert Fraction(ledger.component_padding_exponent) < 0


def test_every_positive_weight_has_the_same_half_grid_value() -> None:
    nodes, aperture, _ = half_period_log_grid(10_000.0)
    assert len(nodes) > 10
    for weights in (
        np.ones(len(nodes)),
        np.arange(1.0, len(nodes) + 1.0),
        np.geomspace(1.0, 100.0, len(nodes)),
    ):
        assert math.isclose(
            normalized_cosine(nodes, weights, aperture), -1.0, abs_tol=2e-12
        )


def test_half_grid_has_prime_density_scale() -> None:
    y = 100_000.0
    nodes, _, _ = half_period_log_grid(y)
    assert len(nodes) > 0.01 * y / math.log(y)
    assert len(nodes) < y / math.log(y)
    assert float(np.max(np.diff(nodes))) < 2.0 * math.log(y) / y


def test_perturbation_bound_is_quadratically_close_to_minus_one() -> None:
    error = 1e-3
    bound = worst_half_grid_perturbation_bound(error)
    assert -1.0 <= bound <= -1.0 + error * error / 2.0


def test_exact_quadrature_rank_cap() -> None:
    assert exact_positive_quadrature_degree_cap(1) == 0
    assert exact_positive_quadrature_degree_cap(37) == 36


def test_positive_packet_repair_is_convex_hull_not_gram_rank() -> None:
    feature = (-1.0, -0.5)
    assert projected_single_packet_gram(feature) == 0.125
    assert one_packet_positive_range(feature) == (-1.0, -0.5)
    assert not (one_packet_positive_range(feature)[0] <= 0.0 <= one_packet_positive_range(feature)[1])
    hull = packet_feature_hull((0.0, math.acos(-0.5)), (1.0,))
    assert np.allclose(hull[:, 0], (1.0, -0.5))


def test_random_subset_bound() -> None:
    assert math.isclose(
        subset_bad_peak_probability_upper(100, 0.1), math.exp(-0.5)
    )


def test_square_reweight_difference_kernel_identity_and_covariance() -> None:
    nodes = (0.13, 0.31, 0.49, 0.77)
    weights = (1.0, 2.0, 3.0, 4.0)
    shifts = (0.0, 1.7, 4.2)
    coefficients = (1.0 + 0.2j, -0.3 + 0.7j, 0.4 - 0.1j)
    height = 3.6
    direct = square_reweighted_characteristic_direct(
        nodes, weights, shifts, coefficients, height
    )
    shifted = square_reweighted_characteristic_shifted(
        nodes, weights, shifts, coefficients, height
    )
    assert abs(direct - shifted) < 2e-15

    ledger = square_reweight_ledger(nodes, weights, shifts, coefficients)
    base = complex_characteristic(nodes, weights, height)
    residual = square_reweight_covariance_residual(
        nodes, weights, shifts, coefficients, height
    )
    assert abs(direct - base - residual / ledger.normalization) < 2e-15
    assert 1.0 <= ledger.coefficient_effective_count <= len(shifts)


def test_square_reweight_cannot_move_a_constant_phase_packet() -> None:
    # Every node has the same feature at t=1.  Arbitrary positive h only
    # changes the node probabilities, so the packet moment remains fixed.
    nodes = (math.pi, 3.0 * math.pi, 5.0 * math.pi)
    weights = (1.0, 5.0, 2.0)
    shifts = (0.0, 0.23, 1.11)
    coefficients = (1.0, -0.7j, 0.2 + 0.1j)
    value = square_reweighted_characteristic_direct(
        nodes, weights, shifts, coefficients, 1.0
    )
    assert abs(value + 1.0) < 2e-15


def test_single_cosine_tilt_is_variance_limited() -> None:
    mean = -0.2
    second = 0.5
    delta = 0.4
    updated = single_cosine_tilt_moment(mean, second, delta)
    variance = second - mean * mean
    assert math.isclose(updated - mean, delta * variance / (1 + delta * mean))
    assert single_cosine_tilt_moment(-0.5, 0.25, 0.9) == -0.5
    small_mean = -0.03
    near_random_second = 0.49
    zeroing_delta = -small_mean / near_random_second
    assert abs(
        single_cosine_tilt_moment(
            small_mean, near_random_second, zeroing_delta
        )
    ) < 1e-15
