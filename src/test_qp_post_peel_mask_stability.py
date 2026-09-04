import numpy as np

from qp_post_peel_mask_stability import (
    affine_triangle_family,
    hermitian_masked_anova,
    path_pair_mask,
    positive_gram_with_indefinite_threshold,
    rectangular_anova,
    sylvester_hadamard,
    two_carrier_lift_gap,
    zero_one_gamma2_lower_bound,
)


def test_exact_hermitian_masked_anova_and_covariance() -> None:
    kernel = np.array(
        [[3, 1 + 2j, -1], [1 - 2j, 4, 2j], [-1, -2j, 2]], dtype=complex
    )
    replay = hermitian_masked_anova(kernel)
    n = kernel.shape[0]
    u = np.ones(n, dtype=complex) / np.sqrt(n)
    w = replay.degree_fluctuation / np.sqrt(n)
    assert np.allclose(
        replay.centered,
        replay.broad + np.outer(u, w.conj()) + np.outer(w, u.conj()),
    )
    assert np.allclose(replay.broad @ replay.broad, replay.covariance)


def test_rectangular_anova_channels_and_two_covariances() -> None:
    matrix = np.array([[1, 2j, 3], [4, -1j, 2]], dtype=complex)
    replay = rectangular_anova(matrix)
    m, n = matrix.shape
    u = np.ones(m, dtype=complex) / np.sqrt(m)
    v = np.ones(n, dtype=complex) / np.sqrt(n)
    assert np.allclose(
        replay.centered,
        replay.broad
        + np.outer(replay.output_degree_channel, v.conj())
        + np.outer(u, replay.input_degree_channel.conj()),
    )
    assert np.allclose(replay.broad.conj().T @ replay.broad, replay.input_covariance)
    assert np.allclose(replay.broad @ replay.broad.conj().T, replay.output_covariance)


def test_smallest_pair_mask_is_not_a_gram_matrix() -> None:
    eigenvalues = np.linalg.eigvalsh(path_pair_mask())
    assert eigenvalues[0] < 0
    assert np.allclose(eigenvalues, [1 - np.sqrt(2), 1, 1 + np.sqrt(2)])


def test_schur_threshold_can_destroy_a_positive_gram_factorization() -> None:
    gram = positive_gram_with_indefinite_threshold()
    assert np.linalg.eigvalsh(gram)[0] > 0
    threshold = (gram >= 0.5).astype(float)
    assert np.array_equal(threshold, path_pair_mask())
    assert np.linalg.eigvalsh(threshold)[0] < 0


def test_even_psd_masks_do_not_tensorize_the_scalar_centered_bound() -> None:
    scalar_norm, lifted_energy = two_carrier_lift_gap(17)
    assert scalar_norm == 0
    assert np.isclose(lifted_energy, 8.0)


def test_affine_triangle_blocks_have_a_polynomial_unconditionality_gap() -> None:
    family = affine_triangle_family(dimension=3, subspace_dimension=2)
    n = family.full_sum.shape[0]
    identity = np.eye(n)
    ones = np.ones((n, n))
    assert len(family.factors) == (n - 1) // 2
    assert family.selected_count == (3**2 - 1) // 2
    assert np.array_equal(family.full_sum, ones - identity)

    # Every direction is a disjoint triangle factor, and distinct factors
    # are edge-disjoint.
    support_sum = np.zeros_like(family.full_sum)
    for factor in family.factors:
        assert np.all(factor.sum(axis=0) == 2)
        assert np.all(factor.sum(axis=1) == 2)
        assert np.isclose(np.linalg.norm(factor, ord=2), 2)
        assert not np.any((support_sum > 0) & (factor > 0))
        support_sum += factor

    projection = identity - ones / n
    full_centered_norm = np.linalg.norm(projection @ family.full_sum @ projection, ord=2)
    selected_centered_norm = np.linalg.norm(
        projection @ family.subspace_sum @ projection, ord=2
    )
    assert np.isclose(full_centered_norm, 1)
    assert np.isclose(selected_centered_norm, 2 * family.selected_count)

    # The same mean-zero coset contrast makes every selected triangle block
    # act by 2, so the best square-function constant is at least the number
    # of selected blocks.
    points = list(np.ndindex(*(3,) * 3))
    vector = np.array([1 if p[2] == 0 else -1 if p[2] == 1 else 0 for p in points], dtype=float)
    vector /= np.linalg.norm(vector)
    selected_factors = [
        factor
        for factor in family.factors
        if np.allclose(factor @ vector, 2 * vector)
    ]
    assert len(selected_factors) == family.selected_count
    lhs = np.linalg.norm(sum(factor @ vector for factor in selected_factors)) ** 2
    rhs = sum(np.linalg.norm(factor @ vector) ** 2 for factor in selected_factors)
    assert np.isclose(lhs / rhs, family.selected_count)


def test_hadamard_zero_one_masks_need_polynomial_factorization_norm() -> None:
    order = 8
    hadamard = sylvester_hadamard(order)
    assert np.array_equal(hadamard @ hadamard.T, order * np.eye(order))
    mask = (np.ones_like(hadamard) + hadamard) / 2
    assert set(np.unique(mask)) == {0.0, 1.0}
    assert zero_one_gamma2_lower_bound(order) > 0.9
