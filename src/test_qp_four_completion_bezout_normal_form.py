from qp_four_completion_bezout_normal_form import (
    BezoutFourCompletionChart,
    hard_diamond,
    prime_nonzero_mixed_remainder_fixture,
)


def test_symbolic_normal_form_on_small_data() -> None:
    chart = BezoutFourCompletionChart.from_anchor((11, 13))
    ledger = chart.audit_pair((17, 19), (23, 29))
    assert ledger.delta == -60
    assert ledger.h == -20
    assert ledger.middle_determinant == -160
    assert ledger.middle_sum == 942
    assert chart.K[0][0] * chart.K[1][1] - chart.K[0][1] ** 2 == -1


def test_hard_diamond_is_exact_maximum() -> None:
    diamond = hard_diamond(101, 17, 47, 523, -11)
    assert diamond.diamond_value == max(
        abs(diamond.first_residual), abs(diamond.second_residual)
    )


def test_literal_prime_chain_has_nonzero_small_mixed_remainder() -> None:
    fixture = prime_nonzero_mixed_remainder_fixture()
    ledger = fixture.ledger
    assert ledger.delta == -72
    assert ledger.h == 36
    assert ledger.middle_determinant == -36
    assert ledger.delta * ledger.h == -2592
    assert fixture.D**2 < fixture.q
    assert abs(ledger.delta * ledger.h) < 2 * fixture.anchor[0] * fixture.anchor[1]
    assert fixture.base_diamond.holds
    assert fixture.next_diamond.holds


def test_factorisations_are_the_original_coordinate_products() -> None:
    fixture = prime_nonzero_mixed_remainder_fixture()
    c, C = fixture.anchor
    b, B = fixture.center
    d, E = fixture.partner
    z = fixture.ledger
    assert z.anchor_sum + z.delta == 2 * b * c
    assert z.anchor_sum - z.delta == 2 * B * C
    assert z.partner_sum + z.h == 2 * C * d
    assert z.partner_sum - z.h == 2 * c * E
    assert z.middle_sum + z.middle_determinant == 2 * b * d
    assert z.middle_sum - z.middle_determinant == 2 * B * E
