import math

import numpy as np

from qp_peller_log_hankel_audit import (
    affine_axis_ledger,
    anti_diagonal_fourth_mass,
    anti_diagonal_matrix,
    approximate_packet_packing_ledger,
    continuum_box_pulse_fourth_lower,
    direct_single_bin_bound,
    dyadic_reciprocal_step_sum,
    dyadic_degree_schatten_bound,
    fixed_slope_packet_theorem_ledger,
    log_linearization_error,
    peller_scale_ledger,
    schatten_fourth_power,
    unstratified_tradeoff_obstruction,
)


def test_project_exponents_in_the_peller_scale_ledger() -> None:
    q = 10.0**33
    degree = q ** (16.0 / 33.0)
    ledger = peller_scale_ledger(q, degree)
    assert math.isclose(ledger.log_pulse_width, q ** (-50.0 / 33.0))
    assert math.isclose(ledger.pulse_to_gap_ratio, q ** (-17.0 / 33.0))
    assert math.isclose(ledger.tangent_packet_order, q ** (8.0 / 33.0))
    assert math.isclose(ledger.uniform_to_actual_loss, q ** (17.0 / 33.0))
    assert math.isclose(
        16.0 * ledger.continuum_to_actual_loss, q ** (34.0 / 33.0)
    )


def test_one_hankel_antidiagonal_is_a_partial_permutation() -> None:
    for order in (3, 8, 17):
        for diagonal in range(2 * order - 1):
            matrix = anti_diagonal_matrix(order, diagonal)
            expected = anti_diagonal_fourth_mass(order, diagonal)
            assert np.count_nonzero(matrix) == expected
            assert math.isclose(schatten_fourth_power(matrix), expected)


def test_continuum_pulse_lower_bound_has_inverse_width_scaling() -> None:
    assert continuum_box_pulse_fourth_lower(1.0 / 64.0) == 4.0
    assert continuum_box_pulse_fourth_lower(1.0 / 128.0) == 8.0


def test_log_linearization_breaks_at_square_root_scale() -> None:
    center = 10**8
    degree = 10**4
    small = log_linearization_error(center, int(math.sqrt(degree)))
    twice = log_linearization_error(center, 2 * int(math.sqrt(degree)))
    epsilon = degree / center**2
    assert small < epsilon
    assert twice > epsilon


def test_affine_endpoint_identities_recover_defect_and_curvature() -> None:
    ledger = affine_axis_ledger(
        base=10_003,
        carrier_base=9_991,
        color_base=10_019,
        row_step=7,
        color_step=5,
        radius=13,
    )
    B = ledger.carrier_base
    L = ledger.radius
    assert ledger.recovered_stationarity_numerator == (
        2 * B * L * ledger.stationarity_defect
    )
    assert ledger.recovered_curvature_numerator == (
        -2 * B * ledger.curvature_term
    )


def test_fixed_slope_packet_packing_has_the_right_D_over_L_squared_tradeoff() -> None:
    degree = 10_000.0
    for radius in (5, 10, 25, 50):
        ledger = approximate_packet_packing_ledger(
            degree, row_step=1, color_step=1, radius=radius
        )
        # The explicit constants in the endpoint and packing intervals cost
        # a fixed factor only; the product is uniformly O(D).
        assert ledger.packet_count_times_radius_sq <= 3.0 * degree
        assert ledger.curvature_admissible


def test_fixed_slope_theorem_constants_for_both_disjointness_notions() -> None:
    # H/B_min is the geometric D-scale.  These parameters satisfy the
    # endpoint-implied curvature inequality P*S*L^2 <= 2H/B_min.
    ledger = fixed_slope_packet_theorem_ledger(
        window_radius=1_000_000.0,
        carrier_lower_bound=10_000.0,
        row_step=2,
        color_step=3,
        radius=5,
    )
    assert ledger.stationarity_defect_bound == 40.0
    assert ledger.curvature_term_bound == 200.0
    assert 2 * 3 * 5**2 <= ledger.curvature_term_bound
    assert ledger.interval_disjoint_budget <= ledger.proved_interval_budget_upper
    assert ledger.node_disjoint_budget <= ledger.proved_node_budget_upper
    assert ledger.node_disjoint_packet_bound >= ledger.interval_disjoint_packet_bound


def test_dyadic_comparable_step_sum_costs_one_per_scale() -> None:
    for lower in (1, 2, 4, 16, 128):
        assert 0.0 < dyadic_reciprocal_step_sum(lower) <= 1.0


def test_unstratified_operator_hs_tradeoff_is_polynomially_false_abstractly() -> None:
    ledger = unstratified_tradeoff_obstruction(100, 0.5)
    assert ledger.schatten_fourth == 0.5 * ledger.degree_budget
    assert ledger.fourth_to_degree_ratio == 0.5
    assert ledger.product_to_degree_ratio > 20.0


def test_single_degree_bin_operator_hs_bound() -> None:
    weights = [0.5, -0.5j, 0.5, 0.5j]
    # ||z||_2^2=1 and ||z||_1^2=4.
    assert math.isclose(direct_single_bin_bound(16.0, weights), 64.0)


def test_dyadic_degree_bound_records_triangle_factor() -> None:
    degrees = {0: 1.0, 1: 2.0, 2: 7.0}
    weights = {0: 1.0, 1: 2.0, 2: 3.0}
    # Three nonempty dyadic bins.  Their one-bin contributions are
    # 1*1^2*1^2, 2*2^2*2^2, and 8*3^2*3^2.
    expected = 3**3 * (1.0 + 32.0 + 648.0)
    assert math.isclose(dyadic_degree_schatten_bound(degrees, weights), expected)
