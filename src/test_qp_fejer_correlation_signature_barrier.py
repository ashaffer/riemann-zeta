from fractions import Fraction

from qp_fejer_correlation_signature_barrier import (
    correlation_signature_exponent_ledger,
    dyadic_prefix_responses,
    exact_linear_grid_row_sum,
    fejer_inverse_radius,
    half_lobe_counterexample,
    independent_factor_cluster_exponent,
    nonlinear_newton_grid_row_sum,
    normalized_dirichlet_amplitude,
    normalized_fejer_direct,
    normalized_fejer_kernel,
    numerical_linear_grid_row_sum,
    numerical_abs_dirichlet_row_sum,
    triangular_fejer_coefficients,
)


def test_triangular_coefficients_and_sine_quotient_agree() -> None:
    for order in (5, 12, 31):
        coefficients = triangular_fejer_coefficients(order)
        assert sum(coefficients.values(), Fraction()) == 1
        for theta in (Fraction(1, 17), Fraction(3, 29), Fraction(1, 2)):
            direct = normalized_fejer_direct(order, theta)
            closed = normalized_fejer_kernel(order, theta)
            assert abs(direct.imag) < 1.0e-12
            assert abs(direct.real - closed) < 1.0e-12


def test_half_lobe_has_large_correlation_and_bad_harmonic() -> None:
    fixture = half_lobe_counterexample(order=21 * 128, odd_lobe=21)
    assert fixture.lower_bound <= fixture.response <= fixture.upper_bound
    assert fixture.anti_aligned_distance == Fraction(1, 2)
    assert fixture.response > 0.4 / (21 * 21)


def test_dyadic_multiscale_does_not_remove_half_lobe() -> None:
    order, odd_lobe, depth = 31 * 256, 31, 8
    responses = dyadic_prefix_responses(order, odd_lobe, depth)
    assert len(responses) == depth + 1
    assert min(responses) >= responses[0] - 1.0e-12
    # Despite every prefix being large, a supported harmonic is antipodal.
    fixture = half_lobe_counterexample(order, odd_lobe)
    assert fixture.anti_aligned_harmonic < order
    assert fixture.anti_aligned_distance == Fraction(1, 2)


def test_inverse_radius_has_square_root_threshold_loss() -> None:
    order, threshold = 10_000, 1.0e-4
    assert fejer_inverse_radius(order, threshold) == 1.0 / 200.0


def test_exponent_ledger_and_four_independent_factor_boundary() -> None:
    ledger = correlation_signature_exponent_ledger()
    assert ledger["scalar_cluster"] == Fraction(103, 96)
    assert ledger["scalar_miss"] == Fraction(5, 96)
    assert ledger["fejer_riesz_amplitude_cluster"] == Fraction(55, 48)
    assert ledger["fejer_riesz_amplitude_miss"] == Fraction(1, 8)
    assert ledger["tensor_cluster"] == Fraction(199, 192)
    assert ledger["tensor_miss"] == Fraction(1, 64)
    assert ledger["minimum_independent_factors"] == 4
    assert independent_factor_cluster_exponent(3) > Fraction(49, 48)
    assert independent_factor_cluster_exponent(4) < Fraction(49, 48)
    assert ledger["four_factor_margin"] == Fraction(1, 384)
    assert ledger["weighted_block_cluster"] == 1
    assert ledger["weighted_block_margin"] == Fraction(1, 48)


def test_exact_linear_grid_row_sum_uses_actual_weights() -> None:
    for order, modulus in ((7, 101), (20, 257), (31, 512)):
        expected = exact_linear_grid_row_sum(order, modulus)
        for anchor in (0, modulus // 3, modulus - 1):
            observed = numerical_linear_grid_row_sum(order, modulus, anchor)
            assert abs(observed - float(expected)) < 1.0e-10


def test_fejer_riesz_square_root_has_only_logarithmic_schur_loss() -> None:
    order, modulus = 31, 1024
    assert abs(normalized_dirichlet_amplitude(order, Fraction()) - 1) < 1.0e-12
    row = numerical_abs_dirichlet_row_sum(order, modulus)
    # The elementary Dirichlet tail is O((Q/H) log H).
    assert row < 5.0 * (modulus / order) * 4.0


def test_physical_newton_grid_has_q_over_h_row_scale() -> None:
    Q, order = 2003, 61
    values = tuple(range(-Q // 4, Q // 4 + 1))
    maximum = max(
        nonlinear_newton_grid_row_sum(order, Q, values, anchor)
        for anchor in values[::100]
    )
    # A compact-collar distortion changes only the absolute constant.
    assert maximum < 10.0 * Q / order
