from fractions import Fraction

from qp_balanced_parabolic_anchored_first_moment import (
    affine_line_star_ledger,
    final_affine_prime_gate_ledger,
    former_balanced_face_ledger,
    relaxed_constant_box_ledger,
    regular_common_x_model,
    symmetric_curvature_closure_ledger,
)


def test_former_balanced_face_is_far_below_four_cycle_strength() -> None:
    ledger = former_balanced_face_ledger()
    assert ledger.top_bottom_mass == Fraction(3, 16)
    assert ledger.left_right_mass == Fraction(19, 16)
    assert ledger.relation_mass == Fraction(3, 16)
    assert ledger.occupied_line_singleton == Fraction(5, 16)
    assert ledger.occupied_line_curvature == Fraction(15, 32)
    assert ledger.weighted_singleton == Fraction(1, 2)
    assert ledger.weighted_curvature == Fraction(21, 32)


def test_relaxed_constant_box_exposes_geometric_mean_loss() -> None:
    ledger = relaxed_constant_box_ledger(
        eta_count=16,
        row_count=9,
        column_count=9,
        line_count=25,
    )
    # For R=S the cross energy is E times the top energy.  The square of
    # the geometric-mean/smaller-bound ratio is therefore exactly E.
    assert ledger.artificial_loss_squared == 16


def test_symmetric_face_has_chart_principal_overlap() -> None:
    ledger = symmetric_curvature_closure_ledger()
    assert ledger.relation_mass == Fraction(15, 16)
    assert ledger.old_curvature_multiplier == Fraction(7, 32)
    assert ledger.repeated_line_multiplier == Fraction(1, 8)
    assert ledger.chart_count == Fraction(11, 4)
    assert ledger.chart_support_threshold == Fraction(15, 8)
    assert ledger.principal_support_threshold == Fraction(31, 16)
    assert ledger.support_overlap == Fraction(1, 16)
    assert ledger.nonprincipal_curvature == Fraction(113, 128)


def test_final_affine_prime_gate_exponents() -> None:
    ledger = final_affine_prime_gate_ledger()
    assert ledger.direction_height == Fraction(13, 32)
    assert ledger.relation_mass == Fraction(45, 64)
    assert ledger.line_multiplier_floor == Fraction(5, 16)
    assert ledger.inverse_sqrt_line_sum == Fraction(5, 32)
    assert ledger.longitudinal_prefactor == Fraction(19, 64)
    assert ledger.pointwise_curvature == Fraction(29, 64)
    assert ledger.weighted_curvature == Fraction(37, 32)
    assert ledger.line_parameter_length == Fraction(9, 64)


def test_regular_common_x_model_saturates_both_matchings() -> None:
    model = regular_common_x_model(group_order=11, lift_degree=3)
    assert model.is_regular
    assert model.chart_count == 33
    assert model.token_energy == Fraction(1, 11)
    assert model.chart_weight == Fraction(1, 11)
    assert model.total_chart_mass == 3


def test_exact_a_one_variable_b_line_star() -> None:
    ledger = affine_line_star_ledger(
        eta=35,
        theta=11,
        column_scale=7,
        column_multiplier=13,
        gamma=17,
        u=19,
        v=23,
    )
    assert ledger.alpha == 77
    assert ledger.beta == 3185
    assert ledger.transverse_gcd == 2695
    assert ledger.row_multiplier == 1
    assert ledger.column_multiplier == 13
    assert ledger.reduced_level == 13 * 19 + 23 + 17 * 7 * 13
