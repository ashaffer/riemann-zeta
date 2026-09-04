from qp_fixed_level_pair_resultant import (
    carrier_rectangle_minor,
    completion_invariant,
    partner_level_spacing,
    pair_resultant,
)


def test_actual_prime_minor_58_fixture() -> None:
    anchor = (13_469, 13_687)
    rows = ((11_171, 10_993), (12_163, 11_969))
    anchor_carriers = (13_001, 11_941)
    first_partner = (12_457, 12_659)
    first_carriers = (14_057, 12_911)
    second_partner = (14_449, 14_683)
    second_carriers = (12_119, 11_131)

    assert carrier_rectangle_minor(first_carriers, second_carriers) == 58
    for partner, carriers in (
        (first_partner, first_carriers),
        (second_partner, second_carriers),
    ):
        for row, b, capital_b in zip(rows, anchor_carriers, carriers):
            invariant = completion_invariant(
                anchor, partner, row, (b, capital_b)
            )
            assert invariant.level_identity_error == 0
            assert invariant.gap_identity_error == 0
        resultant = pair_resultant(
            anchor,
            partner,
            rows[0],
            rows[1],
            (anchor_carriers[0], carriers[0]),
            (anchor_carriers[1], carriers[1]),
        )
        assert resultant.identity_error == 0


def test_separate_actual_binet_fixture() -> None:
    result = pair_resultant(
        (13_103, 10_799),
        (12_659, 10_433),
        (10_903, 13_229),
        (11_483, 13_933),
        (13_693, 14_173),
        (13_001, 13_457),
    )
    assert result.row_determinant == 2_892
    assert result.carrier_determinant == 3_528
    assert result.forward_mixed_level == -14_196_858
    assert result.reverse_mixed_level == -12_798_402
    assert result.identity_error == 0


def test_actual_partner_level_spacing_identity() -> None:
    spacing = partner_level_spacing(
        25_013,
        (13_469, 13_687),
        (12_457, 12_659),
        (14_449, 14_683),
    )
    assert spacing.spacing_identity_error == 0
    assert spacing.partner_determinant != 0
    assert abs(spacing.first_center - spacing.second_center) > 25_013
    assert spacing.first_rounded_level != spacing.second_rounded_level
