import math
from fractions import Fraction

import numpy as np
import pytest

from qp_four_cycle_weighted_secant_lab import (
    actual_residual_slope_block_fixture_ledger,
    aligned_modulus_support_counts,
    anchor_completion_loads,
    b_process_boundary_audit_ledger,
    bilinear_complete_sum_prediction,
    completion_secant_determinants,
    complementary_kernel_projection_pair,
    common_carrier_incidence_ledger,
    conditional_abc_closure_audit_ledger,
    conditional_polynomial_arc_covering_ledger,
    conductor_lowered_crt_index,
    critical_covolume_anchor_factors,
    cross_cusp_kuznetsov_audit_ledger,
    cubic_reciprocal_endpoint_ledger,
    delta_normalization_audit_ledger,
    determinant_cell_covering_barrier_ledger,
    determinant_cell_step_cutoff_ledger,
    determinant_level_stratification_ledger,
    exact_quartic_prime_exclusion_ledger,
    exact_cubic_ray_persistent_count,
    exact_zero_transition_quotient,
    exact_successive_minima_squares,
    farey_split_quadric_matching,
    farey_volume_plane_barrier,
    fixed_determinant_cotlar_ledger,
    fixed_a_factorial_energy_certificate,
    fixed_a_huxley_saturator,
    fixed_a_transition_energy_audit_ledger,
    fixed_a_transition_pair_identity,
    fixed_energy_pairing_coefficients,
    fixed_row_pair_codegree_dichotomy_ledger,
    fixed_row_pair_secant_norm_ledger,
    fixed_secant_layer_ledger,
    fejer_diagonal_cubic_fallback_ledger,
    four_completion_volume_ledger,
    hsm_arc_inverse_obstruction_ledger,
    hsm_stationary_packet_audit_ledger,
    hsm_uniform_closure_route_audit_ledger,
    hsm_spacing_fallback_ledger,
    hsm_spacing_phase,
    hsm_spacing_sharpness_fixture,
    kernel_minima_ledger,
    intermodulus_crt_audit_ledger,
    lll_reduce,
    minor_product_kernel_gate_ledger,
    nonprincipal_stabilizer_increment,
    off_diagonal_form,
    opposite_fan_polynomial_arc_ledger,
    parallel_quartic_uniqueness_ledger,
    positive_rectangular_completion_ledger,
    primitive_tangent_slope_block_ledger,
    primitive_slope_modular_lift,
    projective_common_neighbor_ledger,
    projected_positive_quartic_search,
    quartic_high_step_fan_barrier_ledger,
    quotient_proportionality_identity,
    rational_ray_visibility_ledger,
    reduced_determinant_fan_ledger,
    residual_factorization_ledger,
    relevant_strip_integer_lift_ledger,
    saturated_kernel_basis,
    secant_triangle_ledger,
    signed_color_relation,
    slope_block_fourier_gate_ledger,
    slope_block_anchor_resultant_ledger,
    slope_block_random_scale_ledger,
    symmetric_tangent_cell_residual,
    symmetric_tangent_packing_ledger,
    stationary_fan_cross_identity,
    tangent_low_mode_l2_barrier_ledger,
    ternary_quadric_discriminant_ledger,
    weighted_isolated_cell_audit,
    zero_quotient_content,
)
from qp_four_cycle_pair_completion import completion_level, energy_difference
from qp_four_cycle_hostile_lab import is_prime, shell_values


def test_saturated_kernel_basis_has_exact_covolume() -> None:
    normal = (11, -13, -17, 19)
    basis = saturated_kernel_basis(normal)
    assert all(sum(x * y for x, y in zip(normal, vector)) == 0 for vector in basis)
    gram = np.asarray(basis, dtype=object) @ np.asarray(basis, dtype=object).T
    determinant = (
        gram[0, 0] * (gram[1, 1] * gram[2, 2] - gram[1, 2] * gram[2, 1])
        - gram[0, 1] * (gram[1, 0] * gram[2, 2] - gram[1, 2] * gram[2, 0])
        + gram[0, 2] * (gram[1, 0] * gram[2, 1] - gram[1, 1] * gram[2, 0])
    )
    assert determinant == sum(value * value for value in normal)


def test_exact_minima_on_coordinate_lattice() -> None:
    basis = ((1, 0, 0, 0), (0, 2, 0, 0), (0, 0, 3, 0))
    reduced = lll_reduce(basis)
    assert exact_successive_minima_squares(reduced) == (1, 4, 9)


def test_color_kernel_minima_are_ordered_and_exactly_orthogonal() -> None:
    colors = (23, 29, 31, 37)
    ledger = kernel_minima_ledger(colors)
    normal = (23, -29, -31, 37)
    assert ledger.minima_squares[0] <= ledger.minima_squares[1] <= ledger.minima_squares[2]
    assert all(
        sum(x * y for x, y in zip(normal, vector)) == 0
        for vector in ledger.reduced_basis
    )


def test_single_color_off_diagonal_form_has_sharp_maximum() -> None:
    values = (11, 13, 17, 19)
    completions = tuple((index, index + 1, index + 2, index + 3) for index in range(3))
    form = off_diagonal_form(values, {(11, 13, 17, 19): completions})
    vector = np.full(4, 0.5)
    value, gradient = form.value_and_gradient(vector)
    assert value == pytest.approx(3 * 2 / 16)
    assert np.dot(vector, gradient) == pytest.approx(4 * value)
    lower, optimizer = projected_positive_quartic_search(form)
    assert lower == pytest.approx(3 * 2 / 16, abs=1.0e-10)
    assert np.linalg.norm(optimizer) == pytest.approx(1.0)
    assert form.best_flattening_schur_bound() == pytest.approx(6.0)
    ledger = common_carrier_incidence_ledger(
        {(11, 13, 17, 19): completions}
    )
    left_pair = ledger.right_vertices.index((11, 17))
    right_pair = ledger.right_vertices.index((13, 19))
    gram = ledger.matrix.T @ ledger.matrix
    assert gram[left_pair, right_pair] == len(completions)


def test_sparse_fresh_color_rectangles_separate_anchor_load_from_operator() -> None:
    order = 5
    anchor = 2
    groups = {}
    for row_index in range(order):
        anchor_row = 100 + row_index
        anchor_column = 200 + row_index
        for partner_index in range(order - 1):
            token = row_index * order + partner_index
            partner_row = 1_000 + token
            partner_column = 2_000 + token
            colors = (
                anchor,
                10_000 + 3 * token,
                10_001 + 3 * token,
                10_002 + 3 * token,
            )
            groups[colors] = (
                (anchor_row, partner_row, anchor_column, partner_column),
            )

    loads = anchor_completion_loads(groups)
    assert loads[anchor] == order * (order - 1)
    assert max(load for color, load in loads.items() if color != anchor) == 1

    ledger = common_carrier_incidence_ledger(groups)
    assert ledger.edge_count == 2 * order * (order - 1)
    assert ledger.maximum_left_degree == 2
    assert ledger.maximum_right_degree == 1
    assert ledger.operator_norm == pytest.approx(math.sqrt(2))


def test_projective_shared_neighbor_identities_are_exact() -> None:
    first_left = (10_259, 10_313)
    second_left = (12_511, 12_577)
    shared_right = (15_241, 15_161)
    ledger = projective_common_neighbor_ledger(
        first_left, second_left, shared_right
    )
    assert ledger.first_identity_left == ledger.first_identity_right
    assert ledger.second_identity_left == ledger.second_identity_right
    assert ledger.left_determinant == (
        first_left[0] * second_left[1]
        - first_left[1] * second_left[0]
    )


def test_actual_residual_factorization_recovers_carriers_and_shifts() -> None:
    fixture = actual_residual_slope_block_fixture_ledger()
    ledger = residual_factorization_ledger(fixture.q, fixture.edges)
    assert ledger.edge_count == 10
    assert ledger.recovered_carriers == tuple(edge[2] for edge in fixture.edges)
    assert ledger.recovered_shifts == tuple(
        a2 * c2 - a1 * c1 for a1, a2, _carrier, c1, c2 in fixture.edges
    )
    assert ledger.first_residual_levels == (
        -145_757_173,
        -124_606_005,
        -97_692_069,
        -87_297_013,
    )
    assert ledger.second_residual_levels == ledger.first_residual_levels
    assert ledger.maximum_first_level_multiplicity == 3
    assert ledger.maximum_second_level_multiplicity == 3
    assert ledger.maximum_pair_multiplicity == 1
    assert ledger.projection_edge_bound == 6 * 4


def test_q25013_block_is_legal_and_defeats_resultant_sparsity() -> None:
    ledger = actual_residual_slope_block_fixture_ledger()
    shell_lower = ledger.q * math.exp(-0.2) / 2
    shell_upper = ledger.q * math.exp(0.2) / 2
    nodes = {value for edge in ledger.edges for value in edge}
    assert is_prime(ledger.q)
    assert all(is_prime(value) for value in nodes)
    assert all(shell_lower < value < shell_upper for value in nodes)
    assert len(ledger.edges) == 10
    assert all(len(set(edge)) == 5 for edge in ledger.edges)
    assert ledger.maximum_normalized_frequency < ledger.cutoff
    assert ledger.maximum_carrier_interval_length < 1
    assert ledger.ratio_span_in_degree_bins < 5
    assert ledger.carrier_diameter == 2_926
    assert ledger.anchor_shift == 184
    assert ledger.row_determinant_coordinates == (
        (0, 184),
        (-90, 98),
        (-184, 0),
        (-466, -294),
    )
    assert ledger.color_determinant_coordinates == tuple(
        (alpha, h) for h, alpha in ledger.row_determinant_coordinates
    )
    assert ledger.maximum_resultant_error == 0
    for a1, a2, _carrier, c1, c2 in ledger.edges:
        resultant = slope_block_anchor_resultant_ledger(
            ledger.anchor_left,
            ledger.anchor_reciprocal_color,
            (a1, a2),
            (c2, c1),
        )
        assert resultant.anchor_shift_is_unit
        assert resultant.resultant_left == resultant.resultant_right


def test_fixed_row_pair_secant_transposes_the_binary_norm_exactly() -> None:
    # Rows 0 and 1 of the actual q=25013 block share the two displayed
    # color vertices.  Their Pluecker level is literally equal, not merely
    # close, and all eight variable factors are ordinary primes.
    first_row = (10_559, 11_443)
    second_row = (11_443, 12_401)
    first_neighbor = (14_369, 13_259, 12_893, 11_897)
    second_neighbor = (12_893, 11_897, 14_369, 13_259)
    ledger = fixed_row_pair_secant_norm_ledger(
        first_row,
        second_row,
        first_neighbor,
        second_neighbor,
    )
    assert ledger.row_determinant == -90
    assert ledger.first_level == ledger.second_level == 1_344_514
    assert ledger.secant == (0, -294, 294, 0)
    assert ledger.secant_determinant == 86_436
    assert ledger.kernel_defect == 0
    assert ledger.norm_rhs == 1_807_710_116_956
    assert ledger.norm_discriminant == 31_116_960
    assert ledger.relation_secant_trace == 0
    assert ledger.secant_involution_trace == 0
    assert ledger.mixed_trace == (
        2 * ledger.first_level * ledger.secant_determinant
    )
    assert ledger.relation_secant_square_defect == (0, 0, 0, 0)
    assert ledger.secant_involution_square_defect == (0, 0, 0, 0)
    assert ledger.anticommutator_defect == (0, 0, 0, 0)
    assert ledger.norm_square_defect == (0, 0, 0, 0)
    assert ledger.norm_reduction_is_nondegenerate


def test_fixed_row_pair_codegree_has_sharp_square_root_ledger_only() -> None:
    ledger = fixed_row_pair_codegree_dichotomy_ledger()
    assert ledger.degree_exponent_in_q == Fraction(16, 33)
    assert ledger.generic_cubic_lattice_term_exponent_in_q == Fraction(15, 33)
    assert ledger.generic_factorial_energy_exponent_in_degree == 1
    assert ledger.codegree_exponent_in_q == Fraction(8, 33)
    assert ledger.codegree_exponent_in_degree == Fraction(1, 2)
    assert ledger.exceptional_third_minimum_exponent_in_q == Fraction(17, 33)
    assert ledger.exceptional_plane_separation_margin_exponent_in_q == Fraction(1, 33)
    assert ledger.norm_main_exponent_in_q == 2
    assert ledger.norm_perturbation_exponent_in_q == Fraction(48, 33)
    assert ledger.norm_nonvanishing_margin_exponent_in_q == Fraction(18, 33)
    assert ledger.fixed_secant_multiplicity_is_subpower
    assert ledger.generic_factorial_energy_closes_at_degree
    assert ledger.exceptional_nonparabolic_count_is_subpower
    assert ledger.exceptional_power_count_forces_parabolic_chart
    assert ledger.parabolic_chart_cover_is_subpower
    assert not ledger.near_sharp_generic_count_forces_chart
    assert not ledger.slope_block_bound_proved
    assert not ledger.full_four_cycle_bound_proved


def test_primitive_slope_bin_has_one_exact_modular_lift() -> None:
    reference = (101, 103)
    vector = (107, 109)
    offset = reference[0] * vector[1] - reference[1] * vector[0]
    ledger = primitive_slope_modular_lift(reference, offset, 100, 110)
    assert offset == -12
    assert ledger.first_coordinate_residue == vector[0] % reference[0]
    assert ledger.vector == vector


def test_slope_block_random_scale_is_exactly_fifteen_sixteenths() -> None:
    ledger = slope_block_random_scale_ledger()
    assert ledger.degree_exponent_in_q == Fraction(16, 33)
    assert ledger.raw_pair_exponent_in_q == Fraction(32, 33)
    assert ledger.carrier_density_exponent_in_q == Fraction(-17, 33)
    assert ledger.expected_edge_exponent_in_q == Fraction(15, 33)
    assert ledger.expected_edge_exponent_in_degree == Fraction(15, 16)
    assert ledger.margin_to_degree_exponent == Fraction(1, 16)


def test_slope_block_fourier_gate_has_no_second_moment_slack() -> None:
    ledger = slope_block_fourier_gate_ledger()
    assert ledger.carrier_window_exponent_in_q == Fraction(-17, 33)
    assert ledger.selberg_degree_exponent_in_q == Fraction(17, 33)
    assert ledger.zero_mode_exponent_in_q == Fraction(15, 33)
    assert ledger.target_l1_exponent_in_q == 1
    assert ledger.target_average_exponent_in_q == Fraction(16, 33)
    assert ledger.target_second_moment_exponent_in_q == Fraction(49, 33)
    assert ledger.target_second_moment_exponent_in_degree == Fraction(49, 16)


def test_stationary_minor_product_kernel_has_exact_diagonal_and_spectral_gap() -> None:
    ledger = minor_product_kernel_gate_ledger()
    assert ledger.degree_exponent_in_q == Fraction(16, 33)
    assert ledger.ell_block_exponent_in_q == Fraction(17, 33)
    assert ledger.fan_modulus_exponent_in_q == Fraction(25, 33)
    assert ledger.dual_side_exponent_in_q == Fraction(42, 33)
    assert ledger.product_scale_exponent_in_q == Fraction(84, 33)
    assert ledger.phase_coherence_width_exponent_in_q == Fraction(34, 33)
    assert ledger.stationary_shift_spacing_exponent_in_q == Fraction(51, 33)
    assert ledger.stationary_amplitude_exponent_in_q == Fraction(-34, 33)
    assert ledger.pair_weight_l2_exponent_in_q == Fraction(100, 33)
    assert ledger.unscaled_diagonal_moment_exponent_in_q == Fraction(117, 33)
    assert ledger.scaled_diagonal_moment_exponent_in_q == Fraction(49, 33)
    assert ledger.target_minor_moment_exponent_in_q == Fraction(49, 33)
    assert ledger.required_average_short_shift_exponent_in_q == Fraction(66, 33)
    assert ledger.classical_per_shift_benchmark_exponent_in_q == Fraction(72, 33)
    assert ledger.classical_short_shift_total_exponent_in_q == Fraction(106, 33)
    assert ledger.classical_aggregate_excess_exponent_in_q == Fraction(2, 11)
    assert ledger.arbitrary_path_length_exponent_in_q == Fraction(17, 33)
    assert ledger.arbitrary_path_l2_loss_exponent_in_q == Fraction(17, 33)
    assert ledger.actual_stationary_weight_is_mellin_separable
    assert not ledger.arbitrary_diagonal_path_is_separable
    assert not ledger.shifted_multiplication_table_theorem_proved


def test_hsm_spacing_fallback_reproduces_only_the_existing_p_loss() -> None:
    ledger = hsm_spacing_fallback_ledger()
    assert ledger.aperture_exponent_in_q == Fraction(8, 33)
    assert ledger.hsm_length_exponent_in_q == Fraction(17, 33)
    assert ledger.sharp_endpoint_exponent_in_q == Fraction(16, 33)
    assert ledger.fallback_endpoint_exponent_in_q == Fraction(24, 33)
    assert ledger.endpoint_gap_exponent_in_q == Fraction(8, 33)
    assert ledger.kernel_fallback_exponent_in_q == Fraction(41, 33)
    assert ledger.normalized_target_exponent_in_q == Fraction(17, 33)
    assert ledger.normalized_fallback_exponent_in_q == Fraction(25, 33)
    assert ledger.normalized_loss_exponent_in_q == Fraction(8, 33)
    assert ledger.local_target_exponent_in_q == Fraction(16, 33)
    assert ledger.local_fallback_exponent_in_q == Fraction(24, 33)
    assert ledger.local_fallback_exponent_in_degree == Fraction(3, 2)
    assert ledger.fallback_spacing_theorem_proved
    assert not ledger.sharp_spacing_theorem_proved
    assert ledger.fallback_reproduces_existing_high_step_loss
    assert not ledger.slope_block_bound_proved


def test_fejer_diagonal_cubic_fallback_saves_but_does_not_close() -> None:
    ledger = fejer_diagonal_cubic_fallback_ledger()
    assert ledger.aperture_exponent_in_q == Fraction(8, 33)
    assert ledger.hsm_length_exponent_in_q == Fraction(17, 33)
    assert ledger.trivial_gap_exponent_in_p == 1
    assert ledger.trivial_rational_incidence_exponent_in_denominator == 2
    assert ledger.huxley_first_p_exponent == Fraction(3, 4)
    assert ledger.huxley_first_denominator_exponent == Fraction(1, 4)
    assert ledger.huxley_second_p_exponent == Fraction(1, 3)
    assert ledger.huxley_second_denominator_exponent == 1
    assert ledger.crossover_denominator_exponent_in_p == Fraction(3, 7)
    assert ledger.fallback_gap_exponent_in_p == Fraction(3, 7)
    assert ledger.fallback_gap_exponent_in_q == Fraction(8, 77)
    assert ledger.target_exponent_in_q == Fraction(17, 33)
    assert ledger.fallback_exponent_in_q == Fraction(1573, 2541)
    assert ledger.exact_rational_ray_exponent_in_length == 1
    assert ledger.exact_rational_rays_close_at_target
    assert ledger.diagonal_peak_fallback_proved
    assert not ledger.sharp_diagonal_peak_bound_proved
    assert not ledger.full_weighted_hsm_proved


def test_exact_cubic_rays_have_period_cube_and_only_linear_mass() -> None:
    base = 120
    length = 100_000
    count = exact_cubic_ray_persistent_count(base, length, 60, 120)
    assert count >= 2 * length  # m=60 and m=120 have denominator one.
    assert count <= 15 * length
    with pytest.raises(ValueError):
        exact_cubic_ray_persistent_count(base, length, 0, 120)


def test_shifted_cube_endpoint_has_a_real_abc_quality_barrier() -> None:
    ledger = cubic_reciprocal_endpoint_ledger()
    assert ledger.denominator_exponent_in_p == Fraction(11, 32)
    assert ledger.residual_exponent_in_p == Fraction(7, 32)
    assert ledger.gcd_multiplicity_exponent_in_p == Fraction(21, 32)
    assert ledger.desired_raw_count_exponent_in_p == Fraction(11, 32)
    assert ledger.huxley_raw_count_exponent_in_p == Fraction(9, 16)
    assert ledger.konyagin_raw_count_exponent_in_p == Fraction(43, 80)
    assert ledger.konyagin_raw_gap_exponent_in_p == Fraction(31, 160)
    assert ledger.restored_target_exponent_in_p == 1
    assert ledger.restored_konyagin_exponent_in_p == Fraction(191, 160)
    assert ledger.restored_gap_exponent_in_p == Fraction(31, 160)
    assert ledger.common_gcd_upper_exponent_in_p == Fraction(7, 32)
    assert ledger.height_before_common_gcd_exponent_in_p == Fraction(107, 32)
    assert ledger.radical_before_common_gcd_exponent_in_p == Fraction(93, 32)
    assert ledger.primitive_height_lower_exponent_in_p == Fraction(100, 32)
    assert ledger.primitive_radical_upper_exponent_in_p == Fraction(93, 32)
    assert ledger.primitive_abc_quality_lower_bound == Fraction(107, 93)
    assert ledger.abc_epsilon_barrier == Fraction(14, 93)
    assert ledger.common_gcd_cancels_from_height_and_radical
    assert ledger.zero_residual_raw_count_exponent_in_p == Fraction(11, 96)
    assert ledger.zero_residual_exact_rays_target_controlled
    assert ledger.polynomial_term_degree_before_common_gcd == 107
    assert ledger.polynomial_radical_degree_before_common_gcd == 93
    assert ledger.polynomial_common_gcd_degree_upper_bound == 7
    assert (
        ledger.polynomial_term_degree_after_common_gcd
        > ledger.polynomial_radical_degree_upper_bound
    )
    assert ledger.pointwise_exclusion_is_abc_level
    assert ledger.polynomial_counterfamily_excluded
    assert not ledger.averaged_cubic_theorem_proved
    assert not ledger.sharp_hsm_proved


def test_conditional_abc_audit_stops_at_three_quality_one_gates() -> None:
    ledger = conditional_abc_closure_audit_ledger()
    assert ledger.diagonal_unconditional_gap_exponent_in_p == Fraction(3, 7)
    assert ledger.diagonal_huxley_d_parameter == 2
    assert ledger.diagonal_huxley_primitive_term_exponents_in_p == (
        Fraction(5, 8),
        Fraction(5, 8),
        Fraction(3, 5),
        Fraction(25, 72),
    )
    assert ledger.diagonal_huxley_pure_minor_floor_exponent_in_p == Fraction(5, 8)
    assert ledger.diagonal_transition_target_exponent_in_p == Fraction(9, 16)
    assert (
        ledger.diagonal_huxley_primitive_count_bound_exponent_in_p
        == Fraction(5, 8)
    )
    assert ledger.diagonal_abc_huxley_gap_exponent_in_p == Fraction(1, 16)
    assert ledger.diagonal_abc_huxley_gap_exponent_in_q == Fraction(1, 66)
    assert ledger.diagonal_abc_huxley_total_exponent_in_q == Fraction(35, 66)
    assert ledger.transition_coefficient_exponent_in_p == Fraction(9, 16)
    assert ledger.transition_residual_exponent_in_p == Fraction(7, 16)
    assert ledger.transition_term_height_exponent_in_p == Fraction(57, 16)
    assert ledger.transition_generic_radical_exponent_in_p == Fraction(57, 16)
    assert ledger.transition_abc_quality == 1
    assert ledger.transition_hensel_bound_exponent_in_p == 1
    assert ledger.transition_target_exponent_in_p == Fraction(9, 16)
    assert ledger.transition_hensel_gap_exponent_in_p == Fraction(7, 16)
    assert ledger.transition_abc_residual_lower_exponent_in_p == Fraction(7, 16)
    assert ledger.spacing_generic_height_exponent_in_q == 4
    assert ledger.spacing_generic_radical_exponent_in_q == 4
    assert ledger.spacing_generic_abc_quality == 1
    assert ledger.fixed_row_degree_exponent_in_q == Fraction(16, 33)
    assert ledger.fixed_row_main_minimum_exponent_in_q == 2
    assert ledger.fixed_row_correction_upper_exponent_in_q == Fraction(48, 33)
    assert ledger.fixed_row_main_correction_gap_exponent_in_q == Fraction(18, 33)
    assert ledger.fixed_row_generic_abc_quality == 1
    assert ledger.abc_huxley_diagonal_bound_is_conditional
    assert not ledger.abc_huxley_diagonal_target_proved
    assert ledger.transition_hensel_bound_proved
    assert not ledger.transition_target_proved_under_abc
    assert ledger.transition_abc_only_forces_top_residual_shell
    assert ledger.spacing_t_zero_target_bound_proved
    assert ledger.spacing_exact_zero_residual_nonzero_level_impossible
    assert not ledger.sharp_spacing_endpoint_proved_under_abc
    assert ledger.fixed_row_cross_product_identity_exact
    assert not ledger.fixed_row_abc_forces_tangent_chart_reuse
    assert not ledger.weighted_hsm_proved_under_abc
    assert not ledger.slope_block_bound_proved_under_abc
    assert not ledger.full_four_cycle_bound_proved_under_abc


def test_fixed_a_transition_energy_audit_has_exact_open_boundary() -> None:
    ledger = fixed_a_transition_energy_audit_ledger()
    assert ledger.coefficient_exponent_in_p == Fraction(9, 16)
    assert ledger.residual_exponent_in_p == Fraction(7, 16)
    assert ledger.target_count_exponent_in_p == Fraction(9, 16)
    assert ledger.sufficient_factorial_energy_exponent_in_p == Fraction(9, 16)
    assert ledger.huxley_count_exponent_in_p == Fraction(5, 8)
    assert ledger.huxley_critical_cell_exponent_in_p == Fraction(3, 8)
    assert ledger.huxley_cells_exponent_in_p == Fraction(5, 8)
    assert ledger.missing_saving_exponent_in_p == Fraction(1, 16)
    assert ledger.same_a_pair_gap_exponent_in_p == Fraction(7, 16)
    assert ledger.same_a_three_point_span_exponent_in_p == Fraction(23, 48)
    assert ledger.same_a_six_point_span_exponent_in_p == Fraction(39, 80)
    assert (
        ledger.same_a_three_point_span_exponent_in_p
        == (2 - ledger.coefficient_exponent_in_p) / 3
    )
    assert (
        ledger.same_a_six_point_span_exponent_in_p
        == (9 - 3 * ledger.coefficient_exponent_in_p) / 15
    )
    assert ledger.zero_residual_factorial_energy_exponent_in_p == Fraction(9, 16)
    assert ledger.saturator_denominator_labels_exponent_in_p == Fraction(9, 16)
    assert ledger.saturator_points_per_label_exponent_in_p == Fraction(1, 16)
    assert ledger.saturator_same_label_spacing_exponent_in_p == Fraction(15, 16)
    assert ledger.saturator_total_points_exponent_in_p == Fraction(5, 8)
    assert ledger.factorial_energy_bound_is_sufficient
    assert ledger.same_a_pair_identities_are_exact
    assert ledger.zero_residual_rays_are_target_controlled
    assert ledger.local_determinant_spacing_is_proved
    assert ledger.three_point_spacing_is_unconditional
    assert ledger.six_point_spacing_requires_nonzero_alternant
    assert not ledger.current_constraints_force_target
    assert not ledger.fixed_a_factorial_energy_proved
    assert not ledger.transition_target_proved


def test_fixed_a_transition_pair_identities_are_exact() -> None:
    modulus = 10
    coefficient = 7
    first_u, first_b = 9, 5
    second_u, second_b = 11, 9
    first_residual = coefficient * first_u**3 - first_b * modulus**3
    second_residual = coefficient * second_u**3 - second_b * modulus**3
    identity = fixed_a_transition_pair_identity(
        modulus,
        coefficient,
        first_u,
        first_b,
        first_residual,
        second_u,
        second_b,
        second_residual,
    )
    assert identity.gap == 2
    assert identity.quotient_gap == 4
    assert identity.residual_gap == second_residual - first_residual
    assert identity.differenced_identity == identity.residual_gap
    assert modulus**3 * identity.cross_cubic_residual == identity.cross_cubic_identity


def test_fixed_a_factorial_energy_and_zero_ray_parameterization() -> None:
    certificate = fixed_a_factorial_energy_certificate((1, 3, 0, 2))
    assert certificate.total_count == 6
    assert certificate.factorial_energy == 8
    assert certificate.square_energy == 14
    assert certificate.square_energy == (
        certificate.total_count + certificate.factorial_energy
    )
    assert certificate.cauchy_left == 36
    assert certificate.cauchy_right == 56
    assert certificate.cauchy_left <= certificate.cauchy_right

    quotient = exact_zero_transition_quotient(12, 54, 8)
    assert quotient == 16
    assert 54 * 8**3 == quotient * 12**3
    assert exact_zero_transition_quotient(12, 55, 8) is None


def test_fixed_a_huxley_saturator_obeys_all_abstract_spacings() -> None:
    labels = 8
    multiplicity = 4
    incidences = fixed_a_huxley_saturator(labels, multiplicity)
    assert len(incidences) == labels * multiplicity
    assert {cell for _, cell in incidences} == set(range(labels * multiplicity))
    for label in range(labels):
        cells = [cell for current, cell in incidences if current == label]
        assert len(cells) == multiplicity
        assert all(right - left == labels for left, right in zip(cells, cells[1:]))
    certificate = fixed_a_factorial_energy_certificate(
        tuple(multiplicity for _ in range(labels))
    )
    assert certificate.total_count == labels * multiplicity
    assert certificate.factorial_energy == labels * multiplicity * (multiplicity - 1)


def test_hsm_spacing_endpoint_fixtures_are_exact_and_dirichlet_weighted() -> None:
    q = 177_827_953
    aperture = 100
    assert is_prime(q)
    fixture = hsm_spacing_sharpness_fixture(q, aperture)
    assert (fixture.row_modulus, fixture.color_modulus) == (
        1_778_280,
        1_778_281,
    )
    assert math.gcd(fixture.row_modulus, fixture.color_modulus) == 1
    assert fixture.threshold == Fraction(aperture**2, q)
    assert fixture.center == (50, 50)
    assert fixture.center_shift_cutoff == 5
    assert fixture.center_relations_tested == 25
    assert fixture.center_relations_passing == 25
    assert fixture.center_all_tested_relations_pass
    assert fixture.center_nearest_integer_is_shift_sum
    assert fixture.center_maximum_distance <= fixture.threshold
    assert fixture.gcd_shell == (50, 75)
    assert fixture.gcd_relations_tested == 3_063
    assert fixture.gcd_relations_passing == 3_063
    assert fixture.gcd_all_tested_relations_pass
    assert fixture.gcd_maximum_distance <= fixture.threshold
    assert fixture.minimum_triangular_autocorrelation >= aperture // 4

    center_phase = hsm_spacing_phase(
        q,
        fixture.row_modulus,
        fixture.color_modulus,
        50,
        50,
        1,
        1,
    )
    assert abs(center_phase - 2) <= fixture.threshold


def test_relevant_strip_all_integer_lifts_are_capped_by_determinants() -> None:
    ledger = relevant_strip_integer_lift_ledger(
        (101, 97), 80, 120, determinant_bound=12
    )
    assert ledger.determinant_values_checked == 25
    assert ledger.admissible_vector_count <= 25
    assert ledger.maximum_lifts_per_determinant == 1
    assert ledger.cardinality_cap == 25


def test_actual_prime_reference_can_have_many_scattered_farey_bands() -> None:
    q = 1_161_203
    p = 580_607
    r = 579_583
    degree = round(q ** Fraction(16, 33))
    gap = p - r
    assert is_prime(q) and is_prime(p) and is_prime(r)
    assert degree == 872
    assert gap == 1_024
    assert (p + 1) // gap == 567
    assert (p + 1) % gap == 0
    shell_lower = math.ceil(q * math.exp(-0.2) / 2)
    shell_upper = math.floor(q * math.exp(0.2) / 2)
    assert shell_lower < r < p < shell_upper
    assert math.ceil((2 * degree + 1) / gap) == 2
    lifts = relevant_strip_integer_lift_ledger(
        (p, r), shell_lower, shell_upper, degree
    )
    assert lifts.admissible_vector_count == 519


def test_reduced_fan_basis_merges_the_actual_scattered_fixture() -> None:
    ledger = reduced_determinant_fan_ledger(
        (580_607, 579_583), determinant_bound=872
    )
    assert ledger.multiplier == 567
    assert ledger.shortest_vector == (1, 567)
    assert ledger.shortest_scaled_norm == Fraction(1, 872)
    assert ledger.primitive_basis_coordinates == (1, 0)
    assert ledger.fan_count_envelope == 4
    assert ledger.fan_length_envelope == 1_024
    assert ledger.fan_count_envelope <= 2 + 2 * math.ceil(math.sqrt(872))


def test_high_step_matching_absorbs_quadratic_curvature_exactly() -> None:
    ledger = quartic_high_step_fan_barrier_ledger(2)
    assert ledger.step == 2**33
    assert ledger.center == ledger.step**2
    assert ledger.modulus == 2 * ledger.center
    assert ledger.aperture == 4 * ledger.fan_length**4
    assert ledger.edge_count == 2**8
    assert ledger.support_four_cycle_count == 0
    assert ledger.maximum_product_residual == ledger.product_window
    assert ledger.proposed_curvature_term == Fraction(4, 2**34)
    assert ledger.proposed_volume_term == Fraction(2, 2**18)
    assert ledger.proposed_bound_without_q_o < 2

    for index in (1, ledger.fan_length // 2, ledger.fan_length):
        first = ledger.center + ledger.step * index
        second = ledger.center - ledger.step * index
        carrier = ledger.center + index * index
        assert (
            first * second * carrier
            == ledger.center**3 - ledger.center * index**4
        )
        assert abs(
            8 * first * second * carrier - ledger.modulus**3
        ) <= ledger.product_window


def test_quartic_arc_sublevel_scale_is_exact_on_the_high_step_matching() -> None:
    barrier = quartic_high_step_fan_barrier_ledger(2)
    arc = opposite_fan_polynomial_arc_ledger(
        barrier.modulus,
        barrier.aperture,
        first_center=barrier.center,
        second_center=barrier.center,
        carrier_center=barrier.center,
        first_step=barrier.step,
        second_step=barrier.step,
        carrier_linear_step=0,
        carrier_quadratic_step=1,
    )
    assert arc.product_coefficients[1:4] == (0, 0, 0)
    assert arc.product_coefficients[4] == -barrier.center
    assert arc.polynomial_degree == 4
    assert arc.leading_coefficient == -8 * barrier.center
    assert arc.fourth_difference_coefficient == -192 * barrier.center
    assert arc.quartic_sublevel_scale_fourth_power == barrier.fan_length**4
    assert arc.log_concavity_scale_squared is None


def test_linear_carrier_arc_has_the_strict_log_concavity_scale() -> None:
    arc = opposite_fan_polynomial_arc_ledger(
        2_000_003,
        10_000,
        first_center=1_000_001,
        second_center=1_000_001,
        carrier_center=1_000_001,
        first_step=3,
        second_step=4,
        carrier_linear_step=5,
        carrier_quadratic_step=0,
    )
    assert arc.polynomial_degree == 3
    assert arc.quartic_sublevel_scale_fourth_power is None
    assert arc.log_concavity_scale_squared == Fraction(10_000, 50)


def test_exact_quartic_resonance_cannot_fit_two_actual_narrow_shell_fans() -> None:
    # (11+2t)(11-2t)(121+4t^2) has no t, t^2, or t^3 term.
    # The exact resonance forces the carrier centre out of any shell whose
    # endpoint ratio is below two.
    ledger = exact_quartic_prime_exclusion_ledger(
        first_center=11,
        second_center=11,
        carrier_center=121,
        first_step=2,
        second_step=2,
        carrier_linear_step=0,
        carrier_quadratic_step=4,
    )
    assert ledger.product_coefficients[1:4] == (0, 0, 0)
    assert ledger.primitive_fan_intercepts
    assert ledger.forced_equal_centers
    assert ledger.forced_equal_steps
    assert ledger.forced_center_square_divides_carrier
    assert ledger.carrier_to_center_ratio == 11
    assert ledger.narrow_shell_contradiction


def test_conditional_polynomial_arc_covering_has_exact_sb_exponents() -> None:
    ledger = conditional_polynomial_arc_covering_ledger()
    assert ledger.residual_height_exponent_in_q == Fraction(49, 33)
    assert ledger.random_volume_exponent_in_degree == Fraction(15, 16)
    assert ledger.worst_single_quadratic_arc_exponent_in_q == Fraction(49, 132)
    assert ledger.high_step_quartic_arc_exponent_in_q == Fraction(4, 33)
    assert ledger.linear_carrier_tangent_exponent_in_q == Fraction(8, 33)
    assert ledger.cubic_coefficient_exactness_threshold_in_q == Fraction(49, 99)
    assert ledger.cubic_threshold_gap_over_aperture_in_q == Fraction(1, 99)
    assert ledger.summed_quadratic_arc_exponent_in_degree == Fraction(63, 64)
    assert ledger.summed_quadratic_arc_exponent_in_q == Fraction(21, 44)
    assert ledger.conditional_total_exponent_in_degree == 1
    assert not ledger.arc_covering_theorem_proved


def test_four_point_coplanarity_cells_miss_random_volume_by_one_sixty_sixth() -> None:
    ledger = determinant_cell_covering_barrier_ledger()
    assert ledger.random_cell_area_exponent_in_q == Fraction(17, 33)
    assert ledger.largest_coplanar_cell_area_exponent_in_q == Fraction(1, 2)
    assert ledger.isolated_cell_gap_exponent_in_q == Fraction(1, 66)
    assert ledger.maximal_block_sparse_count_exponent_in_q == Fraction(31, 66)
    assert ledger.random_volume_exponent_in_q == Fraction(5, 11)
    assert ledger.maximal_block_sparse_count_exponent_in_degree == Fraction(31, 32)
    assert ledger.random_volume_exponent_in_degree == Fraction(15, 16)
    assert ledger.rich_cell_threshold == 4


def test_isolated_cell_global_step_cutoff_has_exact_active_powers() -> None:
    ledger = determinant_cell_step_cutoff_ledger()
    assert ledger.low_step_product_cutoff_exponent_in_q == Fraction(1, 33)
    assert ledger.low_step_product_cutoff_exponent_in_degree == Fraction(1, 16)
    assert ledger.bounded_step_isolated_exponent_in_q == Fraction(31, 66)
    assert ledger.bounded_step_isolated_exponent_in_degree == Fraction(31, 32)
    assert ledger.cutoff_isolated_exponent_in_q == Fraction(16, 33)
    assert ledger.cutoff_isolated_exponent_in_degree == 1
    assert ledger.worst_low_step_boundary_exponent_in_q == Fraction(17, 66)
    assert ledger.inherited_cell_occupancy == 3


def test_determinant_level_stratification_does_not_close_balanced_high_step() -> None:
    ledger = determinant_level_stratification_ledger()
    assert ledger.balanced_step_exponent_in_q == Fraction(25, 33)
    assert ledger.balanced_fan_length_exponent_in_q == Fraction(8, 33)
    assert ledger.balanced_fan_count_exponent_in_q == Fraction(8, 33)
    assert ledger.global_cell_count_exponent_in_degree == 1
    assert ledger.determinant_range_exponent_in_q == Fraction(49, 33)
    assert ledger.nonempty_levels_per_cell_exponent_in_degree == 1
    assert ledger.absolute_sqrt_nonempty_level_cost_exponent_in_degree == Fraction(3, 2)
    assert ledger.absolute_sqrt_range_cost_exponent_in_q == Fraction(27, 22)
    assert ledger.global_cell_level_bin_sqrt_exponent_in_degree == 1
    assert ledger.separable_coefficient_l2_exponent_in_degree == 1
    assert ledger.optimistic_global_l2_cost_exponent_in_degree == 2
    assert ledger.target_exponent_in_degree == 1
    assert not ledger.plane_index_preserves_separability
    assert not ledger.closes_balanced_high_step


def test_cross_cusp_kuznetsov_candidate_has_zero_slack_at_weak_data_lift() -> None:
    ledger = cross_cusp_kuznetsov_audit_ledger()
    assert ledger.physical_step_exponent_in_q == Fraction(25, 33)
    assert ledger.level_exponent_in_q == Fraction(50, 33)
    assert ledger.dual_side_exponent_in_q == Fraction(42, 33)
    assert ledger.product_length_exponent_in_q == Fraction(84, 33)
    assert ledger.shift_length_exponent_in_q == Fraction(34, 33)
    assert ledger.delta_modulus_exponent_in_q == Fraction(25, 33)
    assert ledger.one_side_alias_exponent_in_q == Fraction(17, 33)
    assert ledger.joint_alias_exponent_in_q == Fraction(34, 33)
    assert ledger.strong_data_power_exponent_in_q == Fraction(112, 33)
    assert ledger.weakest_data_power_exponent_in_q == Fraction(134, 33)
    assert ledger.translation_norm_fourth_power_exponent_in_q == Fraction(32, 33)
    assert ledger.weakest_total_data_rhs_exponent_in_q == Fraction(166, 33)
    assert ledger.weakest_data_square_root_exponent_in_q == Fraction(83, 33)
    assert ledger.shift_large_sieve_square_root_exponent_in_q == Fraction(17, 33)
    assert ledger.resulting_bound_exponent_in_q == Fraction(100, 33)
    assert ledger.target_exponent_in_q == Fraction(100, 33)
    assert ledger.strong_candidate_bound_exponent_in_q == Fraction(89, 33)
    assert ledger.strong_candidate_margin_exponent_in_q == Fraction(11, 33)
    assert ledger.naive_joint_alias_bound_exponent_in_q == Fraction(117, 33)
    assert ledger.naive_harmonic_diagonal_bound_exponent_in_q == Fraction(125, 33)
    assert not ledger.fixed_cusp_width_power_loss
    assert ledger.crt_separates_fan_and_residue_modulo_periods
    assert not ledger.long_dual_interval_is_alias_free
    assert not ledger.hilbert_tensorization_proves_data_lift
    assert not ledger.cross_cusp_closure_proved


def test_intermodulus_crt_has_an_exact_coherent_conductor_lowered_ray() -> None:
    ledger = intermodulus_crt_audit_ledger()
    assert ledger.delta_modulus_exponent_in_q == Fraction(25, 33)
    assert ledger.long_dual_quotient_exponent_in_q == Fraction(17, 33)
    assert ledger.target_squared_saving_exponent_in_q == Fraction(1, 11)
    assert ledger.desired_gram_constant_exponent_in_q == Fraction(2, 3)
    assert ledger.coherent_gram_eigenvalue_exponent_in_q == Fraction(25, 33)
    assert ledger.gram_exponent_miss_in_q == Fraction(1, 11)
    assert ledger.conditional_hecke_fold_length_exponent_in_q == Fraction(16, 33)
    assert ledger.spectral_level_exponent_in_q == Fraction(50, 33)
    assert ledger.weakest_data_power_exponent_in_q == Fraction(134, 33)
    assert ledger.coherent_ray_survives_conductor_lowering
    assert not ledger.uniform_intermodulus_saving_holds
    assert ledger.hecke_fold_valid_if_product_formula_holds
    assert not ledger.conductor_lowered_product_formula_proved
    assert not ledger.oldform_and_eisenstein_fold_automatic

    # k=t*c makes n/c independent of c, including across distinct primes.
    indices = {
        conductor_lowered_crt_index(101, 37, 5, c, 11, 7 * c)
        for c in (103, 107, 109, 113)
    }
    assert indices == {37 * 11 - 5 * 7 * 101}
    with pytest.raises(ValueError, match="not on"):
        conductor_lowered_crt_index(101, 37, 5, 103, 11, 7 * 103 + 1)


def test_delta_normalization_audit_keeps_every_missing_power_and_mode() -> None:
    ledger = delta_normalization_audit_ledger()
    assert ledger.aperture_exponent_in_q == Fraction(16, 33)
    assert ledger.kernel_block_length_exponent_in_q == Fraction(17, 33)
    assert ledger.fan_count_exponent_in_q == Fraction(8, 33)
    assert ledger.physical_step_exponent_in_q == Fraction(25, 33)
    assert ledger.spectral_level_exponent_in_q == Fraction(50, 33)
    assert ledger.dual_side_length_exponent_in_q == Fraction(42, 33)
    assert ledger.shift_length_exponent_in_q == Fraction(34, 33)
    assert ledger.delta_modulus_exponent_in_q == Fraction(25, 33)
    assert ledger.dfi_top_block_weight_exponent_in_q == Fraction(-50, 33)
    assert ledger.dfi_outer_average_exponent_in_q == Fraction(-25, 33)
    assert ledger.dfi_reciprocal_modulus_exponent_in_q == Fraction(-25, 33)
    assert ledger.dfi_mismatch_argument_exponent_in_q == Fraction(-16, 33)
    assert ledger.row_poisson_period_exponent_in_q == Fraction(50, 33)
    assert ledger.row_poisson_lattice_prefactor_exponent_in_q == Fraction(-8, 33)
    assert ledger.normalized_row_fourier_multiplier_exponent_in_q == Fraction(17, 33)
    assert ledger.long_quotient_exponent_in_q == Fraction(17, 33)
    assert ledger.two_row_multiplier_exponent_in_q == Fraction(34, 33)
    assert ledger.two_dimensional_lattice_prefactor_exponent_in_q == Fraction(-16, 33)
    assert ledger.complete_bilinear_sum_exponent_in_q == Fraction(75, 33)
    assert ledger.full_two_dimensional_poisson_prefactor_exponent_in_q == Fraction(59, 33)
    assert ledger.top_block_two_copy_outer_prefactor_exponent_in_q == Fraction(31, 11)
    assert ledger.normalized_nondegenerate_weil_exponent_in_q == Fraction(-25, 66)
    assert ledger.cauchy_joint_support_exponent_in_q == Fraction(16, 33)
    assert ledger.random_joint_support_required_exponent_in_q == Fraction(7, 33)
    assert ledger.top_block_parseval_bound_exponent_in_q == Fraction(109, 33)
    assert ledger.hsm_correlation_target_exponent_in_q == Fraction(100, 33)
    assert ledger.top_block_parseval_gap_exponent_in_q == Fraction(3, 11)
    assert ledger.aligned_single_modulus_support_exponent_in_q == Fraction(16, 33)
    assert ledger.aligned_support_excess_over_random_target_exponent_in_q == Fraction(3, 11)
    assert ledger.desired_intermodulus_gram_exponent_in_q == Fraction(2, 3)
    assert ledger.flat_single_fan_energy_saving_exponent_in_q == Fraction(8, 33)
    assert not ledger.exact_dfi_uses_only_top_moduli
    assert ledger.zero_phase_forces_one_fan_when_coprime
    assert ledger.flat_coefficients_gain_single_fan_density
    assert not ledger.uniform_l2_coefficients_gain_single_fan_density
    assert ledger.full_two_dimensional_poisson_removes_first_step_quotient
    assert ledger.one_sided_zero_becomes_kloosterman_after_full_transform
    assert not ledger.ramanujan_zero_axes_extracted
    assert not ledger.support_cauchy_and_fixed_c_parseval_close_top_block
    assert not ledger.support_only_random_joint_bound_holds_uniformly
    assert not ledger.farey_burgess_composition_proved
    assert not ledger.jutila_error_resolved
    assert not ledger.stationary_boundary_terms_resolved
    assert not ledger.eisenstein_terms_resolved
    assert not ledger.high_step_hsm_proved


def test_two_dimensional_poisson_complete_sum_has_jk_over_c_prefactor() -> None:
    c, R, S = 5, 3, 7
    a, U0, V0, r, s = 2, 1, 2, 1, 2
    nu, mu = 2, 6
    amplitude, phase = bilinear_complete_sum_prediction(
        c, R, S, a, U0, V0, r, s, nu, mu
    )
    brute = sum(
        np.exp(
            2j
            * np.pi
            * (
                a * x * y / c
                - U0 * r * x / R
                - V0 * s * y / S
                + nu * x / (c * R)
                + mu * y / (c * S)
            )
        )
        for x in range(c * R)
        for y in range(c * S)
    )
    predicted = amplitude * np.exp(2j * np.pi * phase / c)
    assert abs(brute - predicted) < 1e-9
    assert amplitude == c * R * S

    unsupported = bilinear_complete_sum_prediction(
        c, R, S, a, U0, V0, r, s, nu + 1, mu
    )
    assert unsupported == (0, 0)


def test_one_aligned_modulus_carries_a_positive_fraction_of_joint_support() -> None:
    row, color, joint = aligned_modulus_support_counts(101, 10, 10)
    assert row == 6
    assert color == 10
    assert joint == 60
    assert joint >= 10 * 10 // 2


def test_b_process_boundary_terms_retain_a_square_root_degree_loss() -> None:
    ledger = b_process_boundary_audit_ledger()
    assert ledger.low_mode_cutoff_exponent_in_q == Fraction(1, 33)
    assert ledger.low_mode_raw_sum_exponent_in_q == 1
    assert ledger.coherent_interior_raw_sum_exponent_in_q == 1
    assert ledger.balanced_boundary_per_mode_exponent_in_q == Fraction(8, 11)
    assert ledger.selberg_mode_count_exponent_in_q == Fraction(17, 33)
    assert ledger.boundary_raw_sum_exponent_in_q == Fraction(41, 33)
    assert ledger.selberg_coefficient_exponent_in_q == Fraction(-17, 33)
    assert ledger.boundary_weighted_exponent_in_q == Fraction(8, 11)
    assert ledger.target_weighted_exponent_in_q == Fraction(16, 33)
    assert ledger.boundary_loss_exponent_in_q == Fraction(8, 33)
    assert ledger.boundary_loss_exponent_in_degree == Fraction(1, 2)
    assert ledger.low_modes_close
    assert ledger.coherent_interior_closes
    assert not ledger.endpoint_terms_close
    assert not ledger.high_step_b_process_closes


def test_positive_rectangular_completion_removes_only_the_boundary_gate() -> None:
    ledger = positive_rectangular_completion_ledger()
    assert ledger.minimum_relevant_step_exponent_in_q == Fraction(17, 33)
    assert ledger.balanced_step_exponent_in_q == Fraction(25, 33)
    assert ledger.balanced_fan_count_exponent_in_q == Fraction(8, 33)
    assert ledger.balanced_completed_fan_length_exponent_in_q == Fraction(8, 33)
    assert ledger.completed_strip_size_exponent_in_q == Fraction(16, 33)
    assert ledger.zero_mode_exponent_in_q == Fraction(5, 11)
    assert ledger.conditional_raw_hsm_exponent_in_q == 1
    assert ledger.conditional_weighted_exponent_in_q == Fraction(16, 33)
    assert ledger.positive_completion_is_size_safe
    assert ledger.physical_cutoff_can_be_slow_and_smooth
    assert ledger.quotient_weights_remain_external_and_separable
    assert ledger.fanwise_fresnel_charts_are_absent
    assert ledger.boundary_gate_closes_conditionally_on_hsm
    assert not ledger.high_step_hsm_proved


def test_hsm_inverse_does_not_transfer_to_actual_quartic_arcs() -> None:
    ledger = hsm_arc_inverse_obstruction_ledger()
    assert ledger.aperture_exponent_in_q == Fraction(16, 33)
    assert ledger.selberg_frequency_exponent_in_q == Fraction(17, 33)
    assert ledger.hsm_product_scale_exponent_in_q == Fraction(84, 33)
    assert ledger.cross_cusp_level_exponent_in_q == Fraction(50, 33)
    assert ledger.cross_cusp_level_exponent_in_product_scale == Fraction(25, 42)
    assert ledger.fouvry_radziwill_level_exponent == Fraction(17, 33)
    assert ledger.cross_cusp_excess_over_fr_level == Fraction(37, 462)
    assert ledger.exact_quartic_threshold_exponent_in_q == Fraction(49, 99)
    assert ledger.quartic_integrality_gap_exponent_in_q == Fraction(1, 99)
    assert ledger.classical_hsm_gap_exponent_in_q == Fraction(2, 11)
    assert not ledger.positive_completion_retains_actual_node_mask
    assert not ledger.completed_hsm_excess_forces_original_arc_mass
    assert not ledger.fixed_direction_merger_controls_all_directions
    assert not ledger.exact_quartic_exclusion_controls_approximate_arcs
    assert not ledger.fouvry_radziwill_supplies_hsm
    assert not ledger.full_fc_inverse_route_closes


def test_hsm_stationary_packet_audit_separates_barrier_from_lower_bound() -> None:
    ledger = hsm_stationary_packet_audit_ledger()
    assert ledger.degree_exponent_in_q == Fraction(16, 33)
    assert ledger.fan_length_exponent_in_q == Fraction(8, 33)
    assert ledger.physical_step_exponent_in_q == Fraction(25, 33)
    assert ledger.ell_block_exponent_in_q == Fraction(17, 33)
    assert ledger.dual_side_exponent_in_q == Fraction(42, 33)
    assert ledger.product_scale_exponent_in_q == Fraction(84, 33)
    assert ledger.short_shift_exponent_in_q == Fraction(34, 33)
    assert ledger.primitive_zero_quotient_multiplier_exponent_in_q == Fraction(8, 33)
    assert ledger.stationary_tube_cross_bound_exponent_in_q == Fraction(-9, 33)
    assert ledger.pair_weight_l2_exponent_in_q == Fraction(100, 33)
    assert ledger.hsm_target_exponent_in_q == Fraction(117, 33)
    assert ledger.completed_tangent_packet_loss_exponent_in_q == Fraction(9, 33)
    assert ledger.completed_tangent_absolute_exponent_in_q == Fraction(126, 33)
    assert ledger.parabolic_chart_exponent_in_degree == Fraction(5, 4)
    assert ledger.parabolic_chart_exponent_in_q == Fraction(20, 33)
    assert ledger.zero_quotient_primitive_multiplicity_cap == 1
    assert ledger.physical_zero_quotient_is_excisable
    assert ledger.stationary_tube_locks_principal_fan_relation
    assert ledger.primitive_stationary_center_is_diagonal
    assert ledger.completed_tangent_absolute_barrier_certified
    assert not ledger.completed_tangent_is_hsm_lower_bound
    assert not ledger.full_short_shift_kernel_is_nonnegative
    assert ledger.exact_nonprincipal_alias_exists
    assert ledger.parabolic_chart_bound_proved
    assert not ledger.mask_sensitive_packet_covering_proved
    assert not ledger.positive_completion_retains_actual_mask
    assert not ledger.full_weighted_hsm_proved
    assert not ledger.slope_block_bound_proved
    assert not ledger.four_cycle_bound_proved


def test_uniform_hsm_route_audit_records_exact_fail_fast_powers() -> None:
    ledger = hsm_uniform_closure_route_audit_ledger()
    assert ledger.degree_exponent_in_q == Fraction(16, 33)
    assert ledger.fan_exponent_in_q == Fraction(8, 33)
    assert ledger.physical_step_exponent_in_q == Fraction(25, 33)
    assert ledger.dual_side_exponent_in_q == Fraction(42, 33)
    assert ledger.short_shift_exponent_in_q == Fraction(34, 33)
    assert ledger.fixed_short_shift_target_exponent_in_q == Fraction(100, 33)
    assert ledger.scalar_bblr_error_exponent_in_q == Fraction(97, 33)
    assert ledger.scalar_bblr_headroom_exponent_in_q == Fraction(3, 33)
    assert ledger.sqrt_degree_lift_exponent_in_q == Fraction(105, 33)
    assert ledger.sqrt_degree_lift_excess_exponent_in_q == Fraction(5, 33)
    assert ledger.full_degree_lift_exponent_in_q == Fraction(113, 33)
    assert ledger.full_degree_lift_excess_exponent_in_q == Fraction(13, 33)
    assert ledger.restricted_positive_target_exponent_in_q == Fraction(66, 33)
    assert ledger.restricted_zero_residue_floor_exponent_in_q == Fraction(75, 33)
    assert ledger.restricted_zero_residue_excess_exponent_in_q == Fraction(9, 33)
    assert ledger.flat_coefficient_alias_exponent_in_q == Fraction(83, 33)
    assert ledger.flat_coefficient_alias_excess_exponent_in_q == Fraction(17, 33)
    assert ledger.standard_decoupling_squared_loss_exponent_in_q == Fraction(21, 33)
    assert ledger.standard_decoupling_budget_excess_exponent_in_q == Fraction(5, 33)
    assert ledger.farey_fine_tube_occupancy_exponent_in_q == Fraction(24, 33)
    assert ledger.required_fine_tube_occupancy_exponent_in_q == Fraction(32, 33)
    assert ledger.conditional_incidence_squared_loss_exponent_in_q == Fraction(12, 33)
    assert ledger.conditional_incidence_margin_exponent_in_q == Fraction(4, 33)
    assert not ledger.positive_restricted_l1_target_is_true
    assert not ledger.scalar_bblr_accepts_four_fan_weights
    assert not ledger.ordinary_decoupling_closes_hsm
    assert not ledger.exact_ruling_sparsity_implies_approximate_energy
    assert not ledger.mask_preserving_energy_reduction_proved
    assert not ledger.signed_uniform_hsm_proved
    assert not ledger.uniform_four_cycle_proved


def test_zero_quotient_and_stationary_center_identities_are_exact() -> None:
    assert zero_quotient_content(1, 101, 103) == 1
    assert zero_quotient_content(7, 101, 103) == 7
    with pytest.raises(ValueError, match="coprime"):
        zero_quotient_content(1, 6, 15)

    # u=3/2 is the exact common ratio r'/r=s/s'.
    assert stationary_fan_cross_identity(2, 3, 3, 2, Fraction(3, 2)) == 0
    expanded, reduced = quotient_proportionality_identity(
        101, 37, 5, 2, 7, 3
    )
    assert expanded == reduced == 101 * (2 * 7 - 3 * 5)
    assert quotient_proportionality_identity(101, 37, 5, 2, 5, 2) == (0, 0)


def test_balanced_nonprincipal_stabilizer_alias_is_an_exact_integer() -> None:
    # d=L, A=Q, S=LQ, r=r'=1, s'=s-1 gives Delta=1.
    L = 11
    Q = 13
    increment = nonprincipal_stabilizer_increment(
        1, L, Q, 1, 1, 9, 8, L * Q
    )
    assert increment == -1
    assert increment.denominator == 1


def test_isolated_cells_preserve_separable_weights_and_half_open_boundaries() -> None:
    # The first three points straddle cell boundaries; floor assignment to
    # half-open cells is nevertheless unique.  The last two share a cell.
    pairs = ((0, 0), (3, 2), (4, 3), (8, 6), (9, 7))
    row_weights = {0: 1, 3: -2, 4: 3j, 8: 2 - 1j, 9: -1}
    color_weights = {0: 1j, 2: 2, 3: -1, 6: 1 + 1j, 7: 2j}
    phases = {pair: (-1 if index % 2 else 1) for index, pair in enumerate(pairs)}
    audit = weighted_isolated_cell_audit(
        pairs,
        row_weights,
        color_weights,
        row_cell_length=4,
        color_cell_length=3,
        phases=phases,
    )
    assert audit.occupied_pair_count == 5
    assert audit.occupied_cell_count == 3
    assert audit.maximum_cell_occupancy == 2
    assert audit.grid_overlap == 1
    assert audit.weighted_l1_mass <= audit.weighted_l1_supremum_bound
    assert audit.cellwise_square_sum <= audit.cellwise_square_bound + 1e-12
    assert audit.cellwise_square_bound <= audit.product_l2_square_bound + 1e-12

    with pytest.raises(ValueError, match="exceeds"):
        weighted_isolated_cell_audit(
            ((0, 0), (1, 0), (2, 0), (3, 0)),
            {0: 1, 1: 1, 2: 1, 3: 1},
            {0: 1},
            row_cell_length=4,
            color_cell_length=3,
        )


def test_high_step_quartic_arc_has_no_positive_parallel_copy() -> None:
    ledger = parallel_quartic_uniqueness_ledger(2)
    assert ledger.minimum_offset_error_quotient == 5 * ledger.step + 6
    assert ledger.legal_error_quotient_cap == ledger.quartic_length**4
    assert ledger.minimum_offset_error_quotient > ledger.legal_error_quotient_cap
    assert ledger.natural_carrier_is_unique_nearest_integer
    assert ledger.every_positive_parallel_offset_is_illegal
    assert ledger.central_arc_endpoint_is_legal

    x = ledger.quartic_length
    k = ledger.quartic_length
    a = ledger.center + ledger.step * x
    c = ledger.center - ledger.step * (x + k)
    b = ledger.center + ledger.step * k + x * x + x * k + k * k
    quotient = (
        ledger.step * k**3
        + 2 * ledger.step * k * k * x
        + 2 * ledger.step * k * x * x
        + k**3 * x
        + 2 * k * k * x * x
        + 2 * k * x**3
        + x**4
    )
    assert a * b * c - ledger.center**3 == -ledger.center * quotient


def test_tangent_low_modes_force_a_square_root_degree_l2_loss() -> None:
    ledger = tangent_low_mode_l2_barrier_ledger()
    assert ledger.coherent_mode_cutoff_exponent_in_q == Fraction(1, 33)
    assert ledger.coherent_sum_size_exponent_in_q == Fraction(32, 33)
    assert ledger.low_mode_l1_exponent_in_q == 1
    assert ledger.low_mode_l2_exponent_in_q == Fraction(65, 33)
    assert ledger.required_second_moment_exponent_in_q == Fraction(49, 33)
    assert ledger.second_moment_excess_exponent_in_q == Fraction(16, 33)
    assert ledger.cauchy_loss_exponent_in_q == Fraction(8, 33)


def test_actual_mersenne_reference_has_a_coherent_integer_enlargement() -> None:
    p = 2**31
    r = p - 1
    q = 4_294_967_311
    degree = 46_830
    length = degree // 10
    assert is_prime(r) and is_prime(q)
    assert q == 2 * p + 15
    assert (-pow(r, -1, p)) % p == 1
    assert q * math.exp(-0.2) / 2 < r < p < q * math.exp(0.2) / 2

    rho = Fraction(q, 2 * p) ** 3
    phase_arc_bound = (
        2 * (rho - 1) * length
        + 3 * rho * length**2 / p
        + 8 * rho * length**3 / p**2
    )
    assert phase_arc_bound < Fraction(1, 32)
    coherent_second_moment_ratio = (
        math.cos(2 * math.pi * float(phase_arc_bound)) ** 2
        * length**4
        / (q * degree)
    )
    assert coherent_second_moment_ratio > 2.3


def test_visibility_removes_a_generic_small_denominator_rational_ray() -> None:
    ledger = rational_ray_visibility_ledger((10, 11), 40_000, 60_000)
    assert ledger.first_multiplier == 4_000
    assert ledger.last_multiplier == 60_000 // 11
    assert ledger.lattice_points > 1_000
    assert ledger.primitive_points == 0


def test_primitive_tangent_packet_sharply_fills_one_slope_block() -> None:
    order = 7
    center = 6_001 * order**4
    ledger = primitive_tangent_slope_block_ledger(order, center)
    assert ledger.edge_count == order * order
    assert ledger.degree_scale == 100 * order * order
    assert ledger.maximum_cubic_residual <= ledger.q * ledger.degree_scale
    assert ledger.maximum_cross_shift <= 3 * order
    assert ledger.ratio_interval_width <= ledger.canonical_bin_width
    assert ledger.pair_unique
    assert ledger.all_five_distinct
    assert ledger.q_exceeds_degree_squared


def test_symmetric_tangent_packets_cannot_be_packed_past_degree_scale() -> None:
    degree = 100
    ledger = symmetric_tangent_packing_ledger(
        100_003, degree, search_radius=degree
    )
    assert ledger.candidate_edge_count == (2 * degree + 1) ** 2
    assert ledger.admissible_edge_count <= ledger.curvature_upper_bound
    assert ledger.maximum_admissible_radius_squared < degree
    assert ledger.ratio_interval_width <= ledger.canonical_bin_width


def test_actual_shell_has_at_most_two_consecutive_prime_power_pairs() -> None:
    # In a multiplicative shell of ratio <2 there is at most one even prime
    # power, namely one power of two.  Every consecutive pair contains that
    # even value, which can have only its left and right neighbor.
    values = tuple(int(value) for value in shell_values(2**14, 0.2))
    assert math.exp(0.4) < 2
    even_values = tuple(value for value in values if value % 2 == 0)
    consecutive = tuple(value for value in values if value + 1 in set(values))
    assert len(even_values) <= 1
    assert len(consecutive) <= 2


def test_gradient_matches_finite_difference_with_overlapping_terms() -> None:
    values = (2, 3, 5, 7, 11)
    groups = {
        (2, 3, 5, 7): ((1, 2, 3, 4), (2, 3, 4, 5)),
        (2, 3, 5, 11): ((1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)),
    }
    form = off_diagonal_form(values, groups)
    vector = np.asarray([0.31, 0.37, 0.41, 0.43, 0.47])
    value, gradient = form.value_and_gradient(vector)
    epsilon = 1.0e-7
    for index in range(len(values)):
        shifted = vector.copy()
        shifted[index] += epsilon
        shifted_value, _ = form.value_and_gradient(shifted)
        assert (shifted_value - value) / epsilon == pytest.approx(
            gradient[index], rel=1.0e-6, abs=1.0e-7
        )


def test_fixed_energy_determinant_fiber_is_a_pair_partial_matching() -> None:
    # This actual-prime-power example has two completions on exactly the
    # same integral level.  Its secant has a zero entry, so it also checks
    # that the argument does not divide by a preselected pivot.
    colors = (14723, 14207, 12211, 11783)
    first = (10267, 12379, 12941, 13411)
    second = (10733, 12941, 12379, 12829)
    first_products = (
        first[0] * first[2],
        first[0] * first[3],
        first[1] * first[2],
        first[1] * first[3],
    )
    second_products = (
        second[0] * second[2],
        second[0] * second[3],
        second[1] * second[2],
        second[1] * second[3],
    )
    energy = tuple(
        left - right for left, right in zip(first_products, second_products)
    )
    assert signed_color_relation(colors, energy) == 0
    assert energy[2] == 0
    assert energy[0] * energy[3] - energy[1] * energy[2] != 0
    top_coefficient, bottom_coefficient = fixed_energy_pairing_coefficients(
        colors, energy
    )
    assert top_coefficient != 0
    assert bottom_coefficient != 0


def test_two_relation_kernel_has_complementary_pair_projections() -> None:
    relations = ((1, 0, 1, 0), (0, 1, 0, 1))
    pairing = complementary_kernel_projection_pair(*relations)
    assert pairing is not None
    left, right = pairing
    assert set(left).isdisjoint(right)
    assert set(left) | set(right) == {0, 1, 2, 3}


def test_two_relation_parallel_triple_is_the_only_projection_exception() -> None:
    # The common kernel is {(x,x,x,y)}.  Its first three coordinate
    # functionals are parallel, so no partition has two injective sides.
    relations = ((1, -1, 0, 0), (1, 0, -1, 0))
    assert complementary_kernel_projection_pair(*relations) is None


def test_dependent_relations_are_rejected() -> None:
    with pytest.raises(ValueError, match="independent"):
        complementary_kernel_projection_pair((1, 2, 3, 4), (2, 4, 6, 8))


def test_actual_broad_fixture_has_large_secant_product() -> None:
    first = (10267, 12379, 12941, 13411)
    second = (10733, 12941, 12379, 12829)
    assert completion_secant_determinants(first, second) == (1440, 5320)
    assert 1440 * 5320 == 7_660_800
    groups = {(14723, 14207, 12211, 11783): (first, second)}
    ledger = fixed_secant_layer_ledger(
        groups,
        row_determinant=1440,
        column_determinant=5320,
    )
    assert ledger.ordered_pairs == 1
    assert ledger.maximum_top_color_pair_fibre == 1
    assert ledger.maximum_bottom_color_pair_fibre == 1
    assert ledger.schur_bound == 1


def test_translation_line_reuses_one_fixed_secant_layer() -> None:
    center = 10_000
    row_gap = 17
    column_gap = 19
    completions = tuple(
        (
            center + parameter,
            center + row_gap + parameter,
            center - parameter,
            center + column_gap - parameter,
        )
        for parameter in range(12)
    )
    for first, second in zip(completions, completions[1:]):
        assert completion_secant_determinants(first, second) == (
            -row_gap,
            column_gap,
        )
    groups = {(101, 103, 107, 109): completions}
    ledger = fixed_secant_layer_ledger(
        groups,
        row_determinant=-row_gap,
        column_determinant=column_gap,
    )
    assert ledger.ordered_pairs == len(completions) - 1
    assert ledger.maximum_top_color_pair_fibre == len(completions) - 1
    assert ledger.maximum_bottom_color_pair_fibre == len(completions) - 1
    assert ledger.schur_bound == len(completions) - 1


def test_exact_ternary_and_projective_discriminants() -> None:
    colors = (14723, 14207, 12211, 11783)
    completion = (10267, 12379, 12941, 13411)
    product = (
        completion[0] * completion[2],
        completion[0] * completion[3],
        completion[1] * completion[2],
        completion[1] * completion[3],
    )
    ledger = ternary_quadric_discriminant_ledger(colors, product)
    assert ledger.color_determinant == -568
    assert ledger.restricted_polar_discriminant == 2 * ledger.color_determinant
    assert ledger.projective_polar_discriminant == ledger.common_level**2


def test_farey_split_quadric_is_a_large_ruling_free_matching() -> None:
    order = 18
    products = farey_split_quadric_matching(order)
    assert len(products) >= 20
    assert all(
        product[0] * product[3] == product[1] * product[2]
        for product in products
    )
    assert all(product[1] - product[2] == -1 for product in products)
    assert all(max(product) <= order**2 for product in products)
    for index, left in enumerate(products):
        for right in products[index + 1 :]:
            difference = tuple(a - b for a, b in zip(left, right))
            assert difference[0] * difference[3] != difference[1] * difference[2]


def test_farey_volume_barrier_occupies_many_thin_exact_planes() -> None:
    order = 24
    barrier = farey_volume_plane_barrier(order)
    assert barrier.colors == (64, 71, 73, 81)
    assert barrier.colors[0] * barrier.colors[3] - barrier.colors[1] * barrier.colors[2] == 1
    assert len(barrier.completions) >= 40

    all_completions = (*barrier.anchors, *barrier.completions)
    products = tuple(
        (
            completion[0] * completion[2],
            completion[0] * completion[3],
            completion[1] * completion[2],
            completion[1] * completion[3],
        )
        for completion in all_completions
    )
    assert all(
        signed_color_relation(barrier.colors, product) == 1
        for product in products
    )
    for index, left in enumerate(products):
        for right in products[index + 1 :]:
            difference = tuple(a - b for a, b in zip(left, right))
            assert difference[0] * difference[3] != difference[1] * difference[2]

    replayed_indices = tuple(
        four_completion_volume_ledger(
            barrier.colors, (*barrier.anchors, completion)
        ).affine_volume_index
        for completion in barrier.completions
    )
    assert replayed_indices == barrier.volume_indices
    layer_sizes = {
        index: barrier.volume_indices.count(index)
        for index in set(barrier.volume_indices)
    }
    assert len(layer_sizes) >= len(barrier.completions) // 3
    assert max(layer_sizes.values()) <= 6


def test_odd_modulus_rejects_the_symmetric_tangent_baseline() -> None:
    modulus = 1_000_003
    center = (modulus - 1) // 2
    degree_scale = 1_000
    translation = 31
    assert translation * translation <= degree_scale
    residual = symmetric_tangent_cell_residual(
        modulus, center, translation
    )
    assert abs(residual) > modulus * degree_scale


def test_critical_covolume_anchor_is_not_a_prime_power_product() -> None:
    for parameter in range(16, 25):
        first, second, divisor = critical_covolume_anchor_factors(parameter)
        assert divisor == math.gcd(parameter + 1, 2)
        assert first > 1 and second > 1
        if parameter % 2:
            assert first % 8 == 2
            assert divisor == 2
        else:
            assert divisor == 1


def test_fixed_determinant_layers_are_aligned_not_cotlar_orthogonal() -> None:
    edge = ((101, 103), (107, 109))
    disjoint_edge = ((113, 127), (131, 137))
    ledger = fixed_determinant_cotlar_ledger(
        ((edge,), (edge,), (disjoint_edge,))
    )
    assert ledger.layers == 3
    assert ledger.distinct_master_edges == 2
    assert ledger.maximum_layers_per_edge == 2
    assert ledger.maximum_cotlar_overlap_sum == 2

    with pytest.raises(ValueError, match="master matching"):
        fixed_determinant_cotlar_ledger(
            ((edge,), (((101, 103), (139, 149)),)),
        )


def test_two_isolated_integer_chords_have_nonzero_cross_energy_overlap() -> None:
    # A legal q=2151, U=1 full-integer product-window fixture.  Each displayed
    # completion is all-eight-distinct from the four colors.  The two lines
    # have only their displayed endpoints, so both survive the >=3 rich-line
    # quotient.  This is a method obstruction, not an actual-prime fixture.
    q = 2151
    colors = (981, 978, 972, 969)
    chord_pairs = (
        (
            (971, 980, 1306, 1310),
            (974, 983, 1302, 1306),
        ),
        (
            (1294, 1306, 980, 983),
            (1298, 1310, 977, 980),
        ),
    )
    lower = math.ceil((q / 2.0) * math.exp(-0.2))
    upper = math.floor((q / 2.0) * math.exp(0.2))
    bandwidth = (q / 2.0) ** (50.0 / 33.0)
    numerator = q**3
    edge_maps = {}
    for color in colors:
        carrier_map = {}
        for row in range(lower, upper + 1):
            column = math.floor(numerator / (8 * row * color) + 0.5)
            if not lower <= column <= upper:
                continue
            frequency = bandwidth * math.log(
                8 * row * column * color / numerator
            )
            if abs(frequency) <= 1:
                carrier_map[row] = column
        edge_maps[color] = carrier_map

    exact_generic_fiber = []
    for first_row in range(lower, upper + 1):
        if (
            first_row not in edge_maps[colors[0]]
            or first_row not in edge_maps[colors[1]]
        ):
            continue
        first_column = edge_maps[colors[0]][first_row]
        second_column = edge_maps[colors[1]][first_row]
        for second_row in range(lower, upper + 1):
            if (
                edge_maps[colors[2]].get(second_row) != first_column
                or edge_maps[colors[3]].get(second_row) != second_column
            ):
                continue
            completion = (
                first_row,
                second_row,
                first_column,
                second_column,
            )
            if len(set(colors + completion)) == 8:
                exact_generic_fiber.append(completion)
    assert tuple(exact_generic_fiber) == tuple(
        completion for pair in chord_pairs for completion in pair
    )

    energies = []
    for first, second in chord_pairs:
        assert completion_level(colors, first) == completion_level(colors, second)
        assert len(set(colors + first)) == 8
        assert len(set(colors + second)) == 8
        assert all(lower <= value <= upper for value in colors + first + second)
        for completion in (first, second):
            a1, a2, b1, b2 = completion
            triples = (
                (a1, b1, colors[0]),
                (a1, b2, colors[1]),
                (a2, b1, colors[2]),
                (a2, b2, colors[3]),
            )
            frequencies = (
                bandwidth * math.log(8 * a * b * c / q**3)
                for a, b, c in triples
            )
            assert max(abs(value) for value in frequencies) < 1
        difference = tuple(right - left for left, right in zip(first, second))
        da1, da2, db1, db2 = difference
        quadratic = (
            colors[0] * da1 * db1
            - colors[1] * da1 * db2
            - colors[2] * da2 * db1
            + colors[3] * da2 * db2
        )
        assert quadratic == 0
        energies.append(energy_difference(first, second))

    assert energies == [(-22, -34, 14, 2), (-26, -38, 10, -2)]
    edge = ((colors[0], colors[1]), (colors[2], colors[3]))
    ledger = fixed_determinant_cotlar_ledger(((edge,), (edge,)))
    assert ledger.maximum_layers_per_edge == 2
    assert ledger.maximum_cotlar_overlap_sum == 2


def test_actual_prime_triangle_is_common_level_and_genuinely_varying() -> None:
    q = 11_801
    cutoff = 35
    colors = (6337, 5717, 5479, 4943)
    completions = (
        (5171, 5981, 6269, 6949),
        (5821, 6733, 5569, 6173),
        (5861, 6779, 5531, 6131),
    )
    all_nodes = colors + tuple(
        value for completion in completions for value in completion
    )
    assert len(set(all_nodes)) == len(all_nodes)
    assert all(is_prime(value) for value in all_nodes)
    lower = math.ceil((q / 2.0) * math.exp(-0.2))
    upper = math.floor((q / 2.0) * math.exp(0.2))
    bandwidth = (q / 2.0) ** (50.0 / 33.0)
    assert all(lower <= value <= upper for value in all_nodes)
    for completion in completions:
        a1, a2, b1, b2 = completion
        triples = (
            (a1, b1, colors[0]),
            (a1, b2, colors[1]),
            (a2, b1, colors[2]),
            (a2, b2, colors[3]),
        )
        assert max(
            abs(bandwidth * math.log(8 * a * b * c / q**3))
            for a, b, c in triples
        ) < cutoff

    shell = tuple(
        int(value)
        for value in shell_values(q / 2.0, 0.2, "prime_powers")
    )
    shell_set = set(shell)
    edge_maps = {}
    for color in colors:
        carrier_map = {}
        for row in shell:
            column = math.floor(q**3 / (8 * row * color) + 0.5)
            if column not in shell_set:
                continue
            frequency = bandwidth * math.log(
                8 * row * column * color / q**3
            )
            if abs(frequency) <= cutoff:
                carrier_map[row] = column
        edge_maps[color] = carrier_map
    exact_fiber = []
    for first_row in shell:
        if (
            first_row not in edge_maps[colors[0]]
            or first_row not in edge_maps[colors[1]]
        ):
            continue
        first_column = edge_maps[colors[0]][first_row]
        second_column = edge_maps[colors[1]][first_row]
        for second_row in shell:
            if (
                edge_maps[colors[2]].get(second_row) == first_column
                and edge_maps[colors[3]].get(second_row) == second_column
            ):
                completion = (
                    first_row,
                    second_row,
                    first_column,
                    second_column,
                )
                if len(set(colors + completion)) == 8:
                    exact_fiber.append(completion)
    assert tuple(exact_fiber) == completions

    ledger = secant_triangle_ledger(colors, completions)
    assert ledger.common_level == 2_282_556
    assert ledger.energies == (
        (-150, 246, -1188, -840),
        (-42, -758, 1428, 760),
        (192, 512, -240, 80),
    )
    assert ledger.energy_cocycle == (0, 0, 0, 0)
    assert ledger.row_pluecker == (942, -1554, 432)
    assert ledger.column_pluecker == (-444, 676, -320)
    assert ledger.energy_determinants == (418_248, 1_050_504, 138_240)
    assert ledger.homogeneous_normal == (
        4_696_450_792_896,
        -4_237_065_848_256,
        -4_060_735_442_112,
        3_663_533_199_552,
    )
    assert ledger.normal_content == 192
    assert ledger.normal_determinant == -60_738_674_272_174_080
    assert ledger.normal_determinant == ledger.factorized_normal_determinant
    assert ledger.pencil_discriminant == 66_571_014_489_955_460_775_936
    assert ledger.carrier_line_quadratics == (-32_136, -264, -35_856)
    assert not ledger.carrier_collinear


def test_four_point_khatri_rao_and_common_level_volume_quantization() -> None:
    # Four rank-one matrices on det(M)=0 and tr(M)=1.  Their affine span has
    # rank three and all six pairwise secants are invertible.
    colors = (1, 0, 0, 1)
    completions = (
        (1, 0, 1, 0),
        (0, 1, 0, 1),
        (1, 1, 2, -1),
        (-1, 1, -3, -2),
    )
    ledger = four_completion_volume_ledger(colors, completions)
    assert ledger.common_level == 1
    assert ledger.row_pluecker == (1, 1, 1, -1, 1, 2)
    assert ledger.column_pluecker == (1, -1, -2, -2, 3, -7)
    assert ledger.product_volume == -1
    assert ledger.khatri_rao_volume == -1
    assert ledger.secant_cofactor == (-1, 0, 0, -1)
    assert ledger.cofactor_content == 1
    assert ledger.affine_volume_index == -1
    assert ledger.common_level_volume == -1
    assert ledger.affine_rank_three
