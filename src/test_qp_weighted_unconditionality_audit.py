from fractions import Fraction
from math import sqrt

import numpy as np

from qp_residual_block_triangle_matching import affine_plane_sts9_parallel_classes
from qp_four_cycle_hostile_lab import exact_prime_rectangle_fixture
from qp_four_cycle_weighted_secant_lab import farey_volume_plane_barrier
from qp_weighted_triangle_rademacher_square import (
    exact_rademacher_fourth_average,
    validate_linear_matching_partition,
    weighted_class_matrices,
)
from qp_weighted_unconditionality_audit import (
    block_pattern_survives_rademacher,
    critical_defect_fan_exponents,
    critical_tangent_scaling,
    fan_determinant_collision_ledger,
    flat_bin_rademacher_bound,
    forced_prime_power_progression_step_divisor,
    prime_power_progression_step_passes,
    plane_label_square_function_ledger,
    rademacher_pairing_ledger,
    residual_excess_ledger,
    weighted_completion_recurrence_bounds,
)


def test_three_pairing_formula_matches_exact_sign_enumeration():
    matrices = [
        np.array([[0, 1 + 2j], [1 + 2j, 0]], dtype=complex),
        np.array([[1j, 2], [2, -1j]], dtype=complex),
        np.array([[1, -1j], [-1j, 3]], dtype=complex),
    ]
    ledger = rademacher_pairing_ledger(matrices)
    exact = exact_rademacher_fourth_average(matrices)
    np.testing.assert_allclose(ledger.expectation, exact, rtol=1e-12, atol=1e-12)


def test_refined_flat_bin_bound_controls_both_square_orientations():
    classes = affine_plane_sts9_parallel_classes()
    z = np.ones(9, dtype=complex) / 3
    _, degree = validate_linear_matching_partition(9, classes)
    matrices = weighted_class_matrices(9, classes, z)
    exact = exact_rademacher_fourth_average(matrices)
    ledger = flat_bin_rademacher_bound(
        degree, 9, np.linalg.norm(z), bin_constant=1.0
    )
    assert exact <= ledger.rademacher_fourth_bound + 1e-12


def test_critical_flat_bin_random_budget_is_D_to_the_one_eighth():
    # D=256 and M=D^(15/8)=32768 are integral in this replay.
    degree = 256
    support = 32768
    ledger = flat_bin_rademacher_bound(degree, support, bin_constant=4.0)
    assert degree * degree / support == 2
    # Constants are intentionally retained; the scaling is Delta^2/M.
    assert ledger.rademacher_fourth_bound <= 300 * degree**2 / support


def test_actual_prime_rectangle_is_killed_and_has_nonzero_determinant():
    fixture = exact_prime_rectangle_fixture()
    ledger = residual_excess_ledger(
        fixture.q, fixture.rows, fixture.columns, fixture.colors
    )
    assert ledger.determinant_identity_defect == 0
    assert ledger.color_determinant == 6
    assert not ledger.survives_rademacher
    assert len(set(ledger.block_labels)) == 4


def test_even_label_patterns_are_exactly_the_random_survivors():
    assert block_pattern_survives_rademacher((1, 1, 7, 7))
    assert block_pattern_survives_rademacher((3, 3, 3, 3))
    assert not block_pattern_survives_rademacher((1, 1, 2, 3))
    assert not block_pattern_survives_rademacher((1, 2, 3, 4))


def test_prime_power_progression_forces_a_primorial_step():
    assert forced_prime_power_progression_step_divisor(12) == 2 * 3 * 5
    assert prime_power_progression_step_passes(12, 30)
    assert not prime_power_progression_step_passes(12, 6)
    # Five primes in an AP with step six obey the necessary p=2 condition.
    assert prime_power_progression_step_passes(5, 6)


def test_integer_tangent_fixture_can_be_put_at_the_critical_exponents():
    ledger = critical_tangent_scaling(2)
    assert ledger.center_condition_holds
    assert ledger.order == 2**8
    assert ledger.center == 2**33
    # D/q^(16/33) is the fixed constant 100/2^(16/33).
    np.testing.assert_allclose(
        ledger.degree_parameter / ledger.q ** (16 / 33),
        100 / 2 ** (16 / 33),
        rtol=1e-12,
    )


def test_full_symmetric_tangent_normalization_by_literal_sign_enumeration():
    length = 3
    center = 64 * length**3 + 1
    q = 2 * center
    raw_edges = []
    raw_labels = []
    node_values = set()
    for i in range(length):
        for j in range(length):
            edge = (
                center + i,
                center + 2 * length + j,
                center - 2 * length - i - j,
            )
            residual = 8 * edge[0] * edge[1] * edge[2] - q**3
            raw_edges.append(edge)
            raw_labels.append(residual // q)
            node_values.update(edge)
    values = tuple(sorted(node_values))
    index = {value: position for position, value in enumerate(values)}
    blocks = {}
    for edge, label in zip(raw_edges, raw_labels):
        blocks.setdefault(label, []).append(tuple(index[value] for value in edge))
    # Equal-label triples are genuine vertex matchings, including colors.
    for matching in blocks.values():
        flattened = [vertex for edge in matching for vertex in edge]
        assert len(flattened) == len(set(flattened))
    z = np.zeros(len(values), dtype=complex)
    for color in {edge[2] for edge in raw_edges}:
        z[index[color]] = 1 / sqrt(2 * length - 1)
    matrices = weighted_class_matrices(len(values), list(blocks.values()), z)
    all_plus = sum(matrices, start=np.zeros_like(matrices[0]))
    all_plus_fourth = float(
        np.trace((all_plus.conj().T @ all_plus) @ (all_plus.conj().T @ all_plus)).real
    )
    randomized = exact_rademacher_fourth_average(matrices)
    np.testing.assert_allclose(
        all_plus_fourth, 2 * length**4 / (2 * length - 1) ** 2
    )
    np.testing.assert_allclose(randomized, 2 * length**2 / (2 * length - 1))


def test_dense_endpoint_fan_forces_disjoint_equal_determinant_quadruples():
    center = 10_000
    points = tuple((center + step, center + step - 1) for step in range(1, 33))
    replay = fan_determinant_collision_ledger(
        points,
        determinant_cap=31,
        shell_minimum=center,
        shell_maximum=center + 32,
    )
    assert replay.directed_partial_matching_certified
    assert replay.plucker_identities_certified
    assert replay.disjoint_equal_determinant_edge_pairs > 0
    assert replay.disjoint_equal_determinant_edge_pairs >= (
        replay.cauchy_disjoint_lower_bound
    )
    assert replay.distinct_endpoint_quadruples > 0


def test_polynomial_trace_excess_forces_recurrent_four_completions():
    replay = weighted_completion_recurrence_bounds(16.0, 1.0)
    assert replay.mass_on_multiplicity_at_least_three_lower_bound == 14.0
    assert replay.ordered_recurrent_pair_mass_lower_bound == 240.0
    assert replay.ordered_distinct_quadruple_mass_lower_bound == 256.0


def test_critical_endpoint_fan_has_a_one_sixteenth_plane_label_gap():
    replay = critical_defect_fan_exponents()
    assert replay.randomized_budget + replay.automatic_fan_threshold == 1
    assert replay.endpoint_collision_quadruples == Fraction(5, 2)
    assert replay.four_completion_plane_labels - replay.automatic_fan_threshold == (
        replay.fan_to_plane_label_gap
    )


def test_plane_label_randomization_leaves_the_cross_plane_term_exactly():
    replay = plane_label_square_function_ledger((1, 1, 2, 3, 3, 4))
    assert replay.all_plus_square == 36
    assert replay.rademacher_square == 10
    assert replay.within_label_ordered_distinct_pairs == 4
    assert replay.cross_label_ordered_pairs == 26
    assert replay.within_label_ordered_distinct_pairs + replay.cross_label_ordered_pairs == 30
    assert replay.unconditionality_ratio == Fraction(18, 5)


def test_farey_planes_refute_label_only_square_function_packing():
    barrier = farey_volume_plane_barrier(36)
    replay = plane_label_square_function_ledger(barrier.volume_indices)
    assert replay.point_count >= 190
    assert replay.occupied_labels >= replay.point_count // 2
    assert replay.maximum_label_occupancy <= 6
    # Since sum r_t^2 <= (max r_t) sum r_t, the all-plus/random ratio is
    # at least N/max r_t.  The exact Farey fixture grows polynomially.
    assert replay.unconditionality_ratio >= Fraction(
        replay.point_count, replay.maximum_label_occupancy
    )
