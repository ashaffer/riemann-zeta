import numpy as np
import pytest

from qp_finite_carrier_relative_trace import (
    actual_carrier_spectral_ledger,
    broad_common_neighbor_identity,
    build_actual_carrier_matrix,
    carrier_anova_dense,
    carrier_degree_anova_ledger,
    cyclic_carrier_kernel,
    cyclic_character_coefficients,
    cyclic_character_matrix,
    cyclic_hankel_matrix,
    cyclic_regularized_remainder_norm,
    cyclic_threshold_polar_modes,
    exact_balanced_degree,
    exact_schur_sqrt_certificates,
    independent_induced_symmetric_span_rank,
    narrow_shell_has_one_power_per_prime,
)


def test_exact_balanced_degree_uses_integer_inequalities() -> None:
    assert exact_balanced_degree(200_003) == 371
    degree = exact_balanced_degree(1_000_003)
    assert degree**33 <= 1_000_003**16 < (degree + 1) ** 33


def test_cyclic_character_expansion_and_exact_remainder_norm() -> None:
    source = (1, 0, 2, 1, 0, 0, 1)
    window = (0, 1, 0, 1, 1, 0, 0)
    kernel = cyclic_carrier_kernel(source, window)
    hankel = cyclic_hankel_matrix(kernel)
    coefficients = cyclic_character_coefficients(kernel)
    assert cyclic_character_matrix(coefficients) == pytest.approx(hankel)

    threshold = sorted(abs(value) for value in coefficients)[-3]
    removed = cyclic_threshold_polar_modes(coefficients, threshold - 1e-9)
    remainder = hankel - cyclic_character_matrix(coefficients, removed)
    assert np.linalg.svd(remainder, compute_uv=False)[0] == pytest.approx(
        cyclic_regularized_remainder_norm(coefficients, removed)
    )


def test_induced_character_tensors_span_every_symmetric_matrix() -> None:
    for size in (1, 2, 3, 4):
        assert independent_induced_symmetric_span_rank(size, 3) == size * (size + 1) // 2
    assert narrow_shell_has_one_power_per_prime(0.2)


def test_actual_q200003_matrix_contains_the_literal_masked_cycle() -> None:
    core = build_actual_carrier_matrix(200_003)
    index = {int(value): position for position, value in enumerate(core.values)}
    expected = {
        (83_777, 101_411): 117_709,
        (83_777, 117_709): 101_411,
        (101_411, 101_411): 97_241,
        (101_411, 117_709): 83_777,
    }
    for (carrier, colour), label in expected.items():
        assert core.support[index[carrier], index[colour]] == 1
        assert core.labels[index[carrier], index[colour]] == label


def test_actual_prime_matrix_has_no_sqrt_D_polar_mode_at_q25013() -> None:
    core = build_actual_carrier_matrix(25_013)
    ledger = actual_carrier_spectral_ledger(core, eigenvalue_count=8)
    assert ledger.dimension == 535
    assert ledger.edges == 78
    assert ledger.maximum_degree == 4
    assert ledger.centered_ratio < 0.23
    assert ledger.doubly_centered_ratio < 0.23
    assert ledger.threshold_polar_rank_in_computed_spectrum == 0
    assert ledger.schur_proves_sqrt_degree
    assert ledger.double_schur_proves_sqrt_degree
    assert exact_schur_sqrt_certificates(core) == (True, True)


def test_exact_constant_degree_broad_anova_and_covariance_identity() -> None:
    core = build_actual_carrier_matrix(1_013)
    mean_centered, broad, degree_channel, delta = carrier_anova_dense(core.support)
    assert mean_centered == pytest.approx(broad + degree_channel)
    assert np.sum(delta) == pytest.approx(0)
    degree_norm = np.linalg.svd(degree_channel, compute_uv=False)[0]
    ledger = carrier_degree_anova_ledger(core)
    assert degree_norm == pytest.approx(ledger.degree_channel_norm)
    assert ledger.maximum_degree <= ledger.exact_product_interval_degree_cap

    covariance_left, covariance_right = broad_common_neighbor_identity(core.support)
    assert covariance_left == pytest.approx(covariance_right)
