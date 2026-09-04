from fractions import Fraction

from qp_transverse_two_inverse_ledger import (
    antedb_wrap_pair_cutoffs,
    bourgain_beta_wrap_exponents,
    defect_lifts,
    endpoint_inverse_steps,
    euclidean_rebranch_and_poisson_exponents,
    euclidean_rebranch_chart,
    euclidean_rebranch_lift,
    euclidean_second_rebranch_degree_interval,
    euclidean_third_rebranch_degree_interval,
    exponent_pair_wrap_cutoff,
    inverse_step_branch_exponents,
    shared_bezout_chart,
    shared_defect_lift,
    third_derivative_branch_exponents,
    transverse_exponent_ledger,
)


def test_endpoint_steps_are_inverse_gap_steps() -> None:
    ledger = endpoint_inverse_steps(101, 137)
    assert ledger.gap == 36
    assert (ledger.gap * ledger.step_mod_y) % ledger.y in (1, ledger.y - 1)
    assert (ledger.gap * ledger.step_mod_x) % ledger.x in (1, ledger.x - 1)


def test_two_inverse_steps_share_one_bezout_chart() -> None:
    for x, y in ((101, 137), (103, 149), (127, 181), (191, 193)):
        chart = shared_bezout_chart(x, y)
        endpoint = endpoint_inverse_steps(x, y)
        assert chart.m * x - chart.gap * chart.s == 1
        assert chart.step_mod_x == endpoint.step_mod_x
        assert chart.step_mod_y == endpoint.step_mod_y
        for defect in (-17, -1, 0, 8, 23):
            lift = shared_defect_lift(chart, defect, wrap=3)
            assert x * lift.first_completion - y * lift.second_completion == defect
            if lift.first_completion and lift.second_completion:
                left = Fraction(97, x * lift.first_completion)
                right = Fraction(97, y * lift.second_completion)
                assert left - right == -Fraction(
                    97 * defect,
                    x * y * lift.first_completion * lift.second_completion,
                )


def test_defect_lifts_replay_the_exact_linear_equation() -> None:
    x, y = 101, 137
    lifts = []
    for defect in range(-40, 41):
        lifts.extend(defect_lifts(x, y, defect, 70, 220, 70, 220))
    assert lifts
    assert all(
        x * lift.first_completion - y * lift.second_completion == lift.defect
        for lift in lifts
    )
    # The interval has length below 2y, so there are at most two first lifts.
    assert max(
        len(defect_lifts(x, y, defect, 70, 220, 70, 220))
        for defect in range(-40, 41)
    ) <= 2


def test_transverse_exponents_are_exact() -> None:
    ledger = transverse_exponent_ledger()
    assert ledger.degree_in_q == Fraction(16, 33)
    assert ledger.target_in_q == Fraction(14, 33)
    assert ledger.window_in_q == Fraction(-17, 33)
    assert ledger.selberg_degree_in_q == Fraction(17, 33)
    assert ledger.close_gap_in_q == Fraction(2, 11)
    assert ledger.completion_barrier_in_degree == Fraction(33, 32)
    assert ledger.completion_loss_to_target_in_degree == Fraction(5, 32)
    assert ledger.classical_large_sieve_in_degree == Fraction(49, 32)
    assert ledger.optimized_inverse_step_cutoff_in_degree == Fraction(27, 32)
    assert ledger.optimized_selberg_degree_at_cutoff_in_degree == Fraction(1, 8)
    assert ledger.third_derivative_inverse_step_cutoff_in_degree == Fraction(13, 12)
    assert ledger.third_derivative_selberg_degree_at_cutoff_in_degree == Fraction(1, 8)
    assert ledger.third_derivative_wrap_endpoint_at_cutoff_in_degree == Fraction(61, 96)
    assert ledger.bourgain_pair_inverse_step_cutoff_in_degree == Fraction(109, 96)
    assert ledger.antedb_pair_inverse_step_cutoff_in_degree == Fraction(
        1194107, 1050032
    )
    assert ledger.bourgain_beta_inverse_step_cutoff_in_degree == Fraction(73, 64)
    assert ledger.bourgain_beta_gain_over_third_derivative_in_degree == Fraction(
        11, 192
    )
    assert ledger.principal_two_box_in_degree == Fraction(-1, 16)


def test_inverse_step_branch_bound_hits_seven_eighths() -> None:
    terms = inverse_step_branch_exponents()
    assert max(terms.values()) == Fraction(7, 8)
    assert terms["vd_c_endpoint_at_cutoff"] == Fraction(1, 8)


def test_third_derivative_branch_bound_hits_seven_eighths() -> None:
    terms = third_derivative_branch_exponents()
    assert max(terms.values()) == Fraction(7, 8)
    assert terms["one_branch_endpoint"] == Fraction(5, 8)
    assert terms["wrap_endpoint"] == Fraction(61, 96)


def test_exponent_pair_wrap_optimization_and_antedb_scan() -> None:
    assert exponent_pair_wrap_cutoff(Fraction(13, 84), Fraction(55, 84)) == Fraction(
        109, 96
    )
    cutoffs = antedb_wrap_pair_cutoffs()
    assert max(cutoffs, key=cutoffs.get) == "trudgian_yang_1"
    assert cutoffs["trudgian_yang_1"] == Fraction(1194107, 1050032)
    assert cutoffs["trudgian_yang_1"] > cutoffs["bourgain"]
    assert Fraction(73, 64) > cutoffs["trudgian_yang_1"]


def test_bourgain_local_beta_hits_seven_eighths_exactly() -> None:
    terms = bourgain_beta_wrap_exponents()
    assert terms["alpha"] == terms["branch_length"] / terms["phase_parameter"]
    assert terms["beta"] == Fraction(1, 12) + Fraction(2, 3) * terms["alpha"]
    assert terms["per_branch_sum"] == terms["phase_parameter"] * terms["beta"]
    assert terms["wrap_count"] + terms["per_branch_sum"] == Fraction(7, 8)
    assert Fraction(5, 12) < terms["alpha"] < Fraction(3, 7)

    # At the endpoint, H=D^eta crosses alpha_H=3/7 here.  The two
    # Bourgain beta lines give continuous, increasing total exponents.
    transition = Fraction(17, 192)
    lower_intercept = Fraction(657, 896)
    lower_slope = Fraction(97, 84)
    upper_intercept = Fraction(71, 96)
    upper_slope = Fraction(13, 12)
    crossing_value = Fraction(1925, 2304)
    assert lower_intercept + lower_slope * transition == crossing_value
    assert upper_intercept + upper_slope * transition == crossing_value
    assert upper_intercept + upper_slope * Fraction(1, 8) == Fraction(7, 8)

    # At top frequency, the target is alpha-beta(alpha)>=2/35.
    assert terms["alpha"] - terms["beta"] == Fraction(2, 35)
    beta_at_five_twelfths = Fraction(2, 9) + Fraction(1, 3) * Fraction(5, 12)
    assert Fraction(5, 12) - beta_at_five_twelfths == Fraction(1, 18)
    assert Fraction(1, 18) < Fraction(2, 35)


def test_euclidean_rebranch_is_an_exact_unimodular_change() -> None:
    for host, step in ((137, 36), (149, 47), (181, 73), (193, 95)):
        chart = euclidean_rebranch_chart(host, step)
        assert host == chart.quotient * step + chart.signed_remainder
        assert chart.rho == abs(chart.signed_remainder)
        for defect in (-31, -1, 0, 19, 44):
            for wrap in (-7, 0, 5):
                sequence, completion = euclidean_rebranch_lift(
                    chart, defect, wrap
                )
                assert defect == sequence + chart.quotient * wrap
                assert completion == step * defect - host * wrap
                assert completion == step * sequence - chart.signed_remainder * wrap


def test_second_derivative_euclidean_sector_has_a_degree() -> None:
    powers = euclidean_rebranch_and_poisson_exponents()
    assert powers["second_step_minimum"] == Fraction(21, 16)
    assert powers["second_remainder_maximum"] == Fraction(27, 32)
    assert powers["second_product_minimum"] == Fraction(27, 16)
    assert powers["second_small_remainder_margin"] == Fraction(-7, 32)

    # At the corner where the resolution floor and curvature ceiling meet.
    lower, upper = euclidean_second_rebranch_degree_interval(
        Fraction(21, 16), Fraction(27, 32)
    )
    assert lower == upper == Fraction(1, 8)

    # At the opposite product boundary, the endpoint term reaches q/D.
    lower, upper = euclidean_second_rebranch_degree_interval(
        Fraction(21, 16), Fraction(3, 8)
    )
    assert lower == upper == Fraction(17, 16)


def test_third_derivative_euclidean_sector_has_a_degree() -> None:
    powers = euclidean_rebranch_and_poisson_exponents()
    assert powers["third_step_minimum"] == Fraction(25, 16)
    assert powers["third_remainder_maximum"] == Fraction(13, 12)
    assert powers["third_product_minimum"] == Fraction(7, 3)
    assert powers["third_drifting_fibre_endpoint"] == Fraction(61, 96)

    # The remainder ceiling meets the resolution floor.
    lower, upper = euclidean_third_rebranch_degree_interval(
        Fraction(25, 16), Fraction(13, 12)
    )
    assert lower == upper == Fraction(1, 8)

    # The product boundary makes the endpoint lower degree q/D.
    lower, upper = euclidean_third_rebranch_degree_interval(
        Fraction(25, 16), Fraction(37, 48)
    )
    assert lower == upper == Fraction(17, 16)


def test_cross_wrap_poisson_standard_bounds_miss_the_target() -> None:
    powers = euclidean_rebranch_and_poisson_exponents()
    assert powers["poisson_stationary_amplitude"] == Fraction(31, 32)
    assert powers["poisson_l1_barrier"] == Fraction(35, 32)
    assert (
        powers["poisson_l1_barrier"] - Fraction(7, 8)
        == powers["poisson_l1_loss_to_target"]
        == Fraction(7, 32)
    )
    assert powers["poisson_alias_orthogonal_large_sieve"] == Fraction(137, 128)
    assert (
        powers["poisson_alias_orthogonal_large_sieve"] - Fraction(7, 8)
        == powers["poisson_alias_orthogonal_loss_to_target"]
        == Fraction(25, 128)
    )
    assert powers["poisson_large_sieve_at_beta_cutoff"] == Fraction(145, 128)
    assert (
        powers["poisson_large_sieve_at_beta_cutoff"] - Fraction(7, 8)
        == powers["poisson_large_sieve_loss_to_target"]
        == Fraction(33, 128)
    )
