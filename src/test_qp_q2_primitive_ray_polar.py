from fractions import Fraction

import numpy as np

from qp_q2_primitive_ray_polar import (
    aligned_unit_residuals,
    common_carrier_ray_witness,
    coarse_principal_weighted_bounds,
    full_ray_correlation,
    hypothetical_drz_ledger,
    identical_cover_product_identity,
    log_triangle_polar_identity,
    near_regular_intersection_matrix,
    near_regular_overlap_lower_bound,
    normalized_triangle_projection_overlap,
    primitive_coarse_baseline,
    primitive_ray_correlation,
    primitive_ray_correlation_via_ramanujan,
    ray_pair_counts,
    triangle_intersection_matrix,
    wright_fixed_factor_ledger,
)


def test_aligned_residual_fibres_and_constant_coarse_baseline() -> None:
    q, degree = 11, 3
    residuals = aligned_unit_residuals(q, degree)
    assert len(residuals) == 2 * degree * (q - 1)
    for ratio in (1, 2, 7, 13, 37):
        _, count_q = ray_pair_counts(q, degree, ratio)
        assert count_q == 4 * degree**2 * (q - 1)
        assert full_ray_correlation(q, degree, ratio) - primitive_ray_correlation(
            q, degree, ratio
        ) == primitive_coarse_baseline(q, degree)


def test_primitive_ray_formula_matches_ramanujan_expansion() -> None:
    q, degree = 13, 2
    for ratio in range(1, q**2):
        if ratio % q:
            assert primitive_ray_correlation(
                q, degree, ratio
            ) == primitive_ray_correlation_via_ramanujan(q, degree, ratio)


def test_identity_ray_value_is_the_primitive_parseval_mass() -> None:
    q, degree = 17, 3
    expected = Fraction(2 * degree * (q - 1), q**2) - Fraction(
        4 * degree**2 * (q - 1), q**3
    )
    assert primitive_ray_correlation(q, degree, 1) == expected
    assert expected > 0


def test_every_common_carrier_pair_has_an_exact_q2_quotient_witness() -> None:
    witness = common_carrier_ray_witness(
        q=101,
        carrier=47,
        first_row=43,
        first_colour=53,
        second_row=59,
        second_colour=61,
    )
    assert witness.identity_holds
    assert witness.vanishes_mod_q_squared(101)


def test_log_coordinate_is_the_exact_negative_triangle_polar() -> None:
    identity = log_triangle_polar_identity(101, 41, 43, 47)
    np.testing.assert_allclose(
        identity.coordinate_sum, identity.residual_log, rtol=0, atol=2e-16
    )
    np.testing.assert_allclose(
        identity.adjacency_quadratic,
        identity.polar_quadratic,
        rtol=0,
        atol=2e-16,
    )


def test_weighted_coarse_principal_schatten_factor() -> None:
    bounds = coarse_principal_weighted_bounds(
        q=101, degree=9, shell_size=40, coefficient_support=17
    )
    assert bounds.hilbert_schmidt_squared_factor == Fraction(4 * 9**2 * 40, 101**2)
    assert bounds.operator_squared_factor == Fraction(4 * 9**2 * 17, 101**2)
    assert bounds.schatten_fourth_factor == (
        bounds.hilbert_schmidt_squared_factor * bounds.operator_squared_factor
    )


def test_triangle_projection_cross_gram_is_normalized_intersection_matrix() -> None:
    first = [(0, 1, 2), (3, 4, 5)]
    second = [(0, 3, 6), (1, 4, 7)]
    intersection = triangle_intersection_matrix(first, second)
    assert np.array_equal(intersection, np.ones((2, 2), dtype=np.int64))
    assert normalized_triangle_projection_overlap(first, second) == np.linalg.norm(
        intersection, ord=2
    ) / 3


def test_near_perfect_matching_alignment_has_no_uniform_stability_gap() -> None:
    for size in (5, 11, 31):
        matrix = near_regular_intersection_matrix(size)
        assert matrix.sum() == 3 * size - 1
        assert np.min(matrix.sum(axis=0)) == 2
        assert np.min(matrix.sum(axis=1)) == 2
        observed = np.linalg.norm(matrix, ord=2) / 3
        assert observed >= float(near_regular_overlap_lower_bound(size)) - 1e-12
        assert observed < 1


def test_identical_matching_cover_forces_equal_total_product() -> None:
    first = [(2, 3, 5), (7, 11, 13)]
    second = [(2, 7, 11), (3, 5, 13)]
    assert identical_cover_product_identity(first, second)
    assert not identical_cover_product_identity(first, [(2, 7, 17), (3, 5, 13)])


def test_span_one_log_projection_does_not_remove_literal_branching_cross_block() -> None:
    from qp_q2_packet_cross_gram_discovery import (
        block_matrix,
        build_q2_residue_atom_model,
        short_residual_matching_blocks,
    )

    q = 4_751
    model = build_q2_residue_atom_model(q)
    blocks = {block.index: block for block in short_residual_matching_blocks(model)}
    first = block_matrix(blocks[2], model.dimension).toarray().astype(float)
    second = block_matrix(blocks[23], model.dimension).toarray().astype(float)
    constant = np.ones(model.dimension)
    logarithm = np.log(2 * model.values.astype(float) / q)
    polar = np.column_stack((constant, logarithm))
    projection = np.eye(model.dimension) - polar @ np.linalg.inv(
        polar.T @ polar
    ) @ polar.T
    # This exact prime-power/product-window fixture retains essentially the
    # full sqrt(6) branching cross norm after the two global polar vectors
    # are removed.  A family-level arithmetic estimate is still required.
    projected_norm = np.linalg.norm(
        projection @ first @ projection @ second @ projection, ord=2
    )
    assert projected_norm > 2.29


def test_withdrawn_drz_hypothetical_exponent_ledger() -> None:
    ledger = hypothetical_drz_ledger()
    assert ledger.fixed_layer_bound == Fraction(61, 99)
    assert ledger.fixed_layer_dense_trivial == Fraction(49, 66)
    assert ledger.fixed_layer_dense_saving == Fraction(25, 198)
    assert ledger.top_dfi_balanced_saving == Fraction(25, 396)
    assert ledger.required_qp_saving == Fraction(24, 396)
    assert ledger.top_dfi_margin == Fraction(1, 396)


def test_wright_fixed_factor_exact_exponent_ledger() -> None:
    ledger = wright_fixed_factor_ledger()
    assert ledger.true_l2_trivial == 1
    assert ledger.literal_base_with_fixed_factor == Fraction(91, 66)
    assert ledger.literal_bracket_terms == (
        Fraction(-25, 264),
        Fraction(25, 264),
        Fraction(-191, 660),
        Fraction(-73, 660),
        Fraction(-25, 264),
    )
    assert ledger.literal_bound == Fraction(389, 264)
    assert ledger.literal_loss == Fraction(125, 264)
    assert ledger.no_fixed_factor_saving == Fraction(41, 660)
    assert ledger.required_qp_saving == Fraction(40, 660)
    assert ledger.no_fixed_factor_margin == Fraction(1, 660)
    assert ledger.scaled_inverse_m_exponent == Fraction(75, 33)
    assert ledger.scaled_inverse_n_squared_exponent == Fraction(50, 33)
