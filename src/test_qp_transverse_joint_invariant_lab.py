import math

import numpy as np
import pytest
from scipy.integrate import quad

from qp_transverse_joint_invariant_lab import (
    coefficient_packet_statistics,
    continuum_moment_model,
    cubic_spectral_diagnostic,
    optimize_joint_invariant,
    run_joint_invariant_instance,
    short_right_window_skew_diagnostic,
    spline_cosine_transform,
    stationary_identity_residual,
)


def test_spline_transform_is_normalized_even_and_decaying() -> None:
    bandwidth = 17.0
    values = np.array([0.0, 0.2, 1.0])
    assert spline_cosine_transform(0.0, bandwidth, 8) == 1.0
    assert np.allclose(
        spline_cosine_transform(values, bandwidth, 8),
        spline_cosine_transform(-values, bandwidth, 8),
    )
    assert abs(float(spline_cosine_transform(10.0, bandwidth, 8))) < 1.0e-6


def test_uniform_order_moments_match_direct_continuum_integration() -> None:
    # Order one is exactly uniform on [B/3,2B/3], giving an independent
    # one-dimensional quadrature check of every central moment formula.
    bandwidth = 19.0
    nodes = np.array([0.31, 0.73, 1.11])
    model = continuum_moment_model(nodes, bandwidth, spline_order=1)
    left, right = bandwidth / 3.0, 2.0 * bandwidth / 3.0
    density = 1.0 / (right - left)
    direct_mean = np.array(
        [quad(lambda t, u=u: math.cos(t * u) * density, left, right)[0] for u in nodes]
    )
    assert np.allclose(model.mean, direct_mean, atol=2.0e-12)
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            direct_covariance = quad(
                lambda t: (
                    (math.cos(t * nodes[i]) - direct_mean[i])
                    * (math.cos(t * nodes[j]) - direct_mean[j])
                    * density
                ),
                left,
                right,
            )[0]
            assert model.covariance[i, j] == pytest.approx(
                direct_covariance, abs=3.0e-11
            )
            for k in range(len(nodes)):
                direct_third = quad(
                    lambda t: (
                        (math.cos(t * nodes[i]) - direct_mean[i])
                        * (math.cos(t * nodes[j]) - direct_mean[j])
                        * (math.cos(t * nodes[k]) - direct_mean[k])
                        * density
                    ),
                    left,
                    right,
                )[0]
                assert model.third_central[i, j, k] == pytest.approx(
                    direct_third, abs=8.0e-11
                )


def test_optimizer_replays_variance_and_beats_leverage_start() -> None:
    nodes = np.array([0.13, 0.27, 0.44, 0.61])
    model = continuum_moment_model(nodes, 80.0, spline_order=6)
    residual = np.array([1.1, 0.2, 1.4, 0.7])
    candidate = optimize_joint_invariant(model, residual, starts=6, seed=4)
    assert candidate.value + 1.0e-9 >= candidate.leverage_upper
    assert abs(candidate.variance - 1.0) < 1.0e-8
    assert abs(candidate.residual_pairing + candidate.leverage) < 1.0e-8
    assert candidate.negative_skew >= 0.0
    assert stationary_identity_residual(model, residual, candidate) < 2.0e-5


def test_cubic_spectral_candidate_is_below_global_matricization_guard() -> None:
    nodes = np.array([0.13, 0.27, 0.44, 0.61])
    model = continuum_moment_model(nodes, 80.0, spline_order=6)
    diagnostic = cubic_spectral_diagnostic(model, starts=12, seed=3)
    assert diagnostic.negative_skew_candidate > 0.0
    assert (
        diagnostic.negative_skew_candidate
        <= diagnostic.matricization_upper + 1.0e-10
    )
    assert diagnostic.relative_stationarity_residual < 2.0e-5
    assert diagnostic.coefficients @ model.covariance @ diagnostic.coefficients == (
        pytest.approx(1.0, abs=2.0e-10)
    )


def test_short_right_prime_packet_obeys_half_integer_decay_bound() -> None:
    diagnostic = short_right_window_skew_diagnostic(100_000_000, spline_order=8)
    assert diagnostic.prime_count == 6
    assert diagnostic.covariance_lower_bound > 0.0
    assert (
        diagnostic.absolute_standardized_third
        <= diagnostic.rigorous_absolute_skew_upper
    )
    assert diagnostic.absolute_standardized_third < 1.0e-15
    assert diagnostic.packet_scale_quarter_power > 9.0


def test_packet_statistics_are_scale_invariant_and_bounded() -> None:
    coefficients = np.array([1.0, -2.0, 0.5, 3.0])
    signed_nodes = np.array([-0.11, -0.04, 0.041, 0.13])
    first = coefficient_packet_statistics(coefficients, signed_nodes, 100.0)
    second = coefficient_packet_statistics(7.0 * coefficients, signed_nodes, 100.0)
    for key in (
        "coefficient_effective_support",
        "near_reflection_endpoint_l2_share",
        "largest_product_packet_l1_share",
        "signed_product_packet_cancellation_ratio",
    ):
        assert first[key] == pytest.approx(float(second[key]), abs=1.0e-12)
    assert 1.0 <= first["coefficient_effective_support"] <= len(coefficients)
    assert 0.0 <= first["signed_product_packet_cancellation_ratio"] <= 1.0
    assert 0.0 <= first["near_reflection_endpoint_l2_share"] <= 1.0


def test_small_actual_instance_replays_both_calibrations() -> None:
    result = run_joint_invariant_instance(
        70, starts=4, phase_step=0.25, spline_order=6, seed=9
    )
    assert result["continuum_moments_from_exact_characteristic_function"]
    assert result["floating_nonlinear_candidates_only"]
    assert (
        result["negative_skew_spectral_candidate"]
        <= result["negative_skew_matricization_upper"] + 1.0e-10
    )
    assert result["negative_skew_spectral_relative_stationarity_residual"] < 2.0e-4
    for name in ("singleton", "broad"):
        row = result["residuals"][name]
        assert abs(row["calibration_dot_residual_replay"]) < 2.0e-12
        assert row["J_candidate"] >= row["leverage_upper"] - 1.0e-7
        assert row["negative_pairing_constraint_satisfied"]
        assert (
            row["J_candidate"]
            <= row["floating_matricization_global_J_upper"] + 1.0e-8
        )
        assert 0.0 <= row["J_over_floating_matricization_global_upper"] <= 1.0
        assert 0.0 <= row["whitened_calibrated_null_variance_share"] <= 1.0
        assert row["stationary_identity_relative_residual"] < 2.0e-4
