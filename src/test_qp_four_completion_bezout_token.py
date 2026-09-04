from math import gcd

from qp_four_completion_bezout_token import (
    BezoutTokenChart,
    det,
    hard_pair_diamond,
    hard_pair_residuals,
    principal_adjacent_relaxation,
    principal_middle_product_residual,
    principal_survivor_bound,
    verify_hard_pair_diamond,
)
from qp_actual_prime_nds import actual_prime_residual_double_star, four_completion_chains


def test_unimodular_token_round_trip_and_form_determinant() -> None:
    chart = BezoutTokenChart.canonical(101, 103)
    assert chart.c * chart.u - chart.C * chart.v == 1
    assert chart.form_determinant == -1
    center = (107, 109)
    endpoint = (113, 127)
    assert chart.token_to_center(chart.center_to_token(center)) == center
    assert chart.token_to_endpoint(chart.endpoint_to_token(endpoint)) == endpoint


def test_middle_difference_and_sum_are_exact_token_forms() -> None:
    chart = BezoutTokenChart.canonical(101, 103)
    center = (107, 109)
    endpoint = (113, 127)
    ledger = chart.transition_ledger(center, endpoint)
    assert ledger.token_difference == det(ledger.center_token, ledger.endpoint_token)
    assert ledger.token_difference == center[0] * endpoint[0] - center[1] * endpoint[1]
    assert ledger.token_sum == center[0] * endpoint[0] + center[1] * endpoint[1]


def test_token_gram_identity_is_the_exact_physical_factorisation() -> None:
    chart = BezoutTokenChart.canonical(101, 103)
    center = (107, 109)
    endpoint = (113, 127)
    gram = chart.gram_ledger(center, endpoint)
    assert gram.left_norm == -2 * center[0] * center[1]
    assert gram.right_norm == -2 * endpoint[0] * endpoint[1]
    assert gram.cross == center[0] * endpoint[0] + center[1] * endpoint[1]
    assert gram.area == center[0] * endpoint[0] - center[1] * endpoint[1]
    assert (gram.cross - gram.area, gram.cross + gram.area) == (
        2 * center[1] * endpoint[1],
        2 * center[0] * endpoint[0],
    )


def test_root_endpoint_is_e2_and_tokens_preserve_primitivity() -> None:
    chart = BezoutTokenChart.canonical(101, 103)
    assert chart.endpoint_to_token((101, 103)) == (0, 1)
    for pair in ((107, 109), (113, 127), (131, 137)):
        token = chart.center_to_token(pair)
        assert gcd(*pair) == gcd(*token)


def test_hard_windows_equal_one_token_diamond() -> None:
    chart = BezoutTokenChart.canonical(101, 103)
    q, D, row = 220, 50, 109
    center, endpoint = (107, 109), (113, 127)
    residuals = hard_pair_residuals(q, row, center, endpoint)
    ledger = chart.transition_ledger(center, endpoint)
    assert max(map(abs, residuals)) == hard_pair_diamond(
        q, row, ledger.token_sum, ledger.token_difference
    )
    assert verify_hard_pair_diamond(q, D, row, chart, center, endpoint)


def test_determinant_only_completion_has_quadratic_mass() -> None:
    D = 80
    chart, centers, endpoints = principal_adjacent_relaxation(10_000, D // 2)
    assert len(centers) * len(endpoints) == (D // 2) ** 2
    for center in centers:
        assert gcd(*center) == 1
        for endpoint in endpoints:
            ledger = chart.transition_ledger(center, endpoint)
            assert 0 < ledger.token_difference <= D


def test_principal_hard_mask_restores_an_ellipse() -> None:
    D = 160
    middle = 16 * D * D
    survivors = 0
    for r in range(1, D + 1):
        for s in range(1, D + 1):
            row, residual = principal_middle_product_residual(middle, r, s)
            if abs(8 * residual) <= 2 * middle * D:
                survivors += 1
                A = r - 1
                assert 16 * (A * A - A * s + s * s) <= 5 * D
    assert survivors <= principal_survivor_bound(D)
    assert principal_survivor_bound(D) <= 2 * D


def test_literal_actual_prime_chains_survive_the_token_lift_without_copies() -> None:
    fixture = actual_prime_residual_double_star()
    gamma = fixture.central.colors
    chart = BezoutTokenChart.canonical(*gamma)
    assert chart.endpoint_to_token(gamma) == (0, 1)
    chains = four_completion_chains(fixture.q, fixture.D, fixture.primes, gamma)
    assert len(chains) >= fixture.central_nds_lower_bound
    token_pairs = set()
    for chain in chains:
        assert verify_hard_pair_diamond(
            fixture.q,
            fixture.D,
            chain.base_row,
            chart,
            chain.centers,
            gamma,
        )
        assert verify_hard_pair_diamond(
            fixture.q,
            fixture.D,
            chain.next_row,
            chart,
            chain.centers,
            chain.next_colors,
        )
        token_pair = (
            chart.center_to_token(chain.centers),
            chart.endpoint_to_token(chain.next_colors),
        )
        assert token_pair not in token_pairs
        token_pairs.add(token_pair)
