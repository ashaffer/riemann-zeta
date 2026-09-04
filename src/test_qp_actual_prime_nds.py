from qp_actual_prime_nds import (
    actual_prime_residual_double_star,
    determinant_label_map,
    error_divisor_ledger,
    error_pair_step,
    four_completion_chains,
    neighbourhood_degree_sums,
    same_determinant_step,
)


def test_literal_all_prime_residual_double_star() -> None:
    fixture = actual_prime_residual_double_star()
    assert fixture.q == 5_868_182
    assert fixture.D == 1_912
    assert fixture.central.determinant == -72
    assert fixture.same_center_arm.determinant == -36
    assert fixture.same_color_arm.determinant == -36
    assert fixture.central_center_degree_lower_bound == 4
    assert fixture.central_color_degree_lower_bound == 4
    assert fixture.central_nds_lower_bound == 14
    assert max(map(abs, fixture.same_color_arm.residuals)) < fixture.q * fixture.D


def test_fixture_replays_through_four_completions_and_labels() -> None:
    fixture = actual_prime_residual_double_star()
    chains = four_completion_chains(
        fixture.q, fixture.D, fixture.primes, fixture.central.colors
    )
    labels = determinant_label_map(chains)
    target = (
        fixture.central.determinant,
        fixture.central.colors[1] * fixture.same_center_arm.colors[0]
        - fixture.central.colors[0] * fixture.same_center_arm.colors[1],
    )
    assert target in labels
    assert len(chains) >= fixture.central_nds_lower_bound


def test_exact_approximate_gcd_identity() -> None:
    fixture = actual_prime_residual_double_star()
    ledger = error_divisor_ledger(
        fixture.central.row,
        fixture.same_center_arm.row,
        fixture.central.colors,
        fixture.same_center_arm.colors,
    )
    assert ledger.linear_error == ledger.factored_linear_error
    assert ledger.endpoint_determinant != 0


def test_primitive_determinant_and_error_steps() -> None:
    assert same_determinant_step((101, 103), (107, 109), (210, 210)) == -1
    assert error_pair_step((101, 103), (5, 7), (106, 110)) == -1


def test_neighbourhood_degree_sum_definition() -> None:
    p0, p1 = (1, 2), (3, 4)
    g0, g1 = (5, 6), (7, 8)
    values = neighbourhood_degree_sums(((p0, g0), (p0, g1), (p1, g0)))
    assert values[g0] == 3
    assert values[g1] == 2
