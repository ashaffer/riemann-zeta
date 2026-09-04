from fractions import Fraction

import pytest

from qp_support_graph_k23_gate import (
    critical_k23_exponent_ledger,
    fixed_pair_height_bin_ledger,
    high_partner_exponent_ledger,
    relation_label_ledger,
    scalar_qp_three_pivot_ledger,
    support_graph_k23_ledger,
    uniform_subset_partner_saturation,
)


def _complete_bipartite(order: int) -> list[list[int]]:
    size = 2 * order
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for left in range(order):
        for right in range(order, size):
            matrix[left][right] = 1
            matrix[right][left] = 1
    return matrix


def test_k23_double_count_on_complete_bipartite_graph() -> None:
    ledger = support_graph_k23_ledger(_complete_bipartite(3), threshold=3)
    assert ledger.edges == 9
    assert ledger.maximum_degree == 3
    assert ledger.high_pair_count == 6
    assert ledger.high_codegree_first_moment == 18
    assert ledger.high_codegree_second_moment == 54
    assert ledger.high_codegree_third_factorial_moment == 6
    assert ledger.pivot_triple_pair_moment == 6
    assert ledger.k23_identity_holds


def test_scalar_qp_three_pivot_tangent_fixture() -> None:
    # Full-integer tangent data.  The center is deliberately much larger
    # than D^2 so that the short-orthogonal collinearity step is literal.
    center = 100_000_001
    order = 5
    q = 2 * center
    degree = 100 * order * order
    pivot_parameters = (0, 2, 4)
    endpoint_parameters = (0, 2, 4)
    pivots = tuple(center + 2 * order + value for value in pivot_parameters)
    endpoints = tuple(center + value for value in endpoint_parameters)
    completions = tuple(
        tuple(center - 2 * order - i - j for j in pivot_parameters)
        for i in endpoint_parameters
    )
    ledger = scalar_qp_three_pivot_ledger(
        q,
        degree,
        pivots,
        endpoints,
        completions,
        shell_minimum=center - 4 * order,
        shell_maximum=center + 3 * order,
    )
    assert ledger.maximum_absolute_residual <= q * degree
    assert ledger.universal_cross_product_bound == degree
    assert ledger.observed_cross_product_bound == 16
    assert ledger.primitive_normal == (1, -2, 1)
    assert ledger.primitive_height == 2
    assert ledger.normal_multipliers == (-4, -8)
    assert len(endpoints) <= ledger.common_endpoint_upper_bound
    assert ledger.short_orthogonal_collinearity_certified


def test_three_pivot_certificate_requires_the_d_squared_separation() -> None:
    center = 100_000_001
    order = 5
    q = 2 * center
    pivots = tuple(center + 2 * order + value for value in (0, 2, 4))
    endpoints = tuple(center + value for value in (0, 2))
    completions = tuple(
        tuple(center - 2 * order - i - j for j in (0, 2, 4))
        for i in (0, 2)
    )
    with pytest.raises(ValueError, match="short-orthogonal separation"):
        scalar_qp_three_pivot_ledger(
            q,
            20_000,
            pivots,
            endpoints,
            completions,
            shell_minimum=center - 4 * order,
            shell_maximum=center + 3 * order,
        )


def test_raw_relation_label_count_and_reciprocal_mass() -> None:
    first = relation_label_ledger(1)
    second = relation_label_ledger(2)
    assert first.nonzero_raw_labels == 26
    assert first.raw_reciprocal_height_mass == 26
    assert second.nonzero_raw_labels == 124
    assert second.raw_reciprocal_height_mass == 75


def test_critical_support_stops_at_an_exact_quarter_power() -> None:
    ledger = critical_k23_exponent_ledger(
        Fraction(15, 8), Fraction(7, 8)
    )
    assert ledger.elementary_high_pair_bound == 3
    assert ledger.k23_high_pair_bound == Fraction(13, 4)
    assert ledger.k23_minus_elementary == Fraction(1, 4)
    assert ledger.dyadic_codegree_second_moment_bound == 5
    assert ledger.dyadic_carleson_second_moment_target == Fraction(19, 4)
    assert ledger.target_gap == Fraction(1, 4)
    assert ledger.saving_needed_to_match_elementary == Fraction(1, 4)
    assert ledger.saving_needed_for_carleson_layer == Fraction(1, 4)
    assert not ledger.k23_improves_elementary
    assert not ledger.carleson_second_moment_closes


def test_quarter_power_saving_only_matches_and_strictly_more_improves() -> None:
    matching = critical_k23_exponent_ledger(
        Fraction(15, 8), Fraction(7, 8), Fraction(1, 4)
    )
    improving = critical_k23_exponent_ledger(
        Fraction(15, 8), Fraction(7, 8), Fraction(1, 4) + Fraction(1, 100)
    )
    assert matching.k23_high_pair_bound == matching.elementary_high_pair_bound
    assert matching.carleson_second_moment_closes
    assert not matching.k23_improves_elementary
    assert improving.k23_improves_elementary
    assert improving.carleson_second_moment_closes


def test_fixed_pair_height_bin_has_only_R_times_divisor_many_third_rows() -> None:
    center = 10_000
    scale = 12
    row = lambda parameter: (center + 3 * parameter, center + 3 * parameter + 1)
    # The factor three cancels from the primitive cross product, so the
    # height of (p_0,p_1,p_t) is still t; all displayed nodes are distinct.
    third_rows = tuple(row(parameter) for parameter in range(scale, 2 * scale))
    ledger = fixed_pair_height_bin_ledger(
        row(0),
        row(1),
        third_rows,
        scale,
        shell_minimum=center,
        shell_maximum=center + 6 * scale,
    )
    assert ledger.anchor_determinant == -3
    assert ledger.divisor_count == 2
    assert ledger.third_row_count == scale
    assert ledger.primitive_heights == tuple(range(scale, 2 * scale))
    assert ledger.fixed_determinant_injective
    assert ledger.third_row_count <= ledger.upper_bound


def test_critical_high_partner_cap_improves_but_misses_by_one_eighth() -> None:
    ledger = high_partner_exponent_ledger(Fraction(7, 8))
    assert ledger.partner_count == Fraction(1, 4)
    assert ledger.weighted_uncompleted_tail == Fraction(1, 4)
    assert ledger.completed_trace == Fraction(9, 8)
    assert ledger.previous_uncompleted_tail == Fraction(3, 8)
    assert ledger.improvement_over_previous == Fraction(1, 8)
    assert ledger.desired_uncompleted_tail == Fraction(1, 8)
    assert ledger.remaining_trace_gap == Fraction(1, 8)
    assert ledger.square_root_degree_spectral_scale == 1
    assert ledger.spectral_saving_needed_from_schur == Fraction(1, 8)
    assert ledger.improves_previous_high_tail
    assert not ledger.proves_sharp_trace
    assert not ledger.packet_free_spectral_theorem_proved


def test_uniform_subset_design_saturates_the_partner_bound() -> None:
    ledger = uniform_subset_partner_saturation(8)
    assert ledger.rows == 64
    assert ledger.subset_size == 8
    assert ledger.high_partners_per_anchor == 63
    assert ledger.partner_bound_scale == 81
    assert ledger.partner_to_bound_ratio == Fraction(7, 9)
    assert ledger.fixed_pair_triple_sum <= ledger.row_degree
    assert ledger.triple_height_cap_certified
