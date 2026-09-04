from qp_four_cycle_parabolic_color_normal_form import (
    parabolic_color_normal_form,
)


def test_rational_additive_color_normal_form_and_determinant_gap() -> None:
    # r=(2,3), s=(5,7).  The weighted colors form the additive rectangle
    # with normalized gaps 7 and 3; det(C)=-21.
    ledger = parabolic_color_normal_form(
        (2100, 1497, 1393, 993),
        (2, 3),
        (5, 7),
    )
    assert ledger.weighted_additive_defect == 0
    assert ledger.color_determinant == -21
    assert ledger.first_normalized_gap == 7
    assert ledger.second_normalized_gap == 3
    assert ledger.determinant_gap_defect == 0


def test_equal_directions_recover_the_ordinary_additive_grid() -> None:
    ledger = parabolic_color_normal_form(
        (100, 93, 89, 82),
        (1, 1),
        (-1, -1),
    )
    assert ledger.color_determinant == -77
    assert abs(ledger.first_normalized_gap * ledger.second_normalized_gap) == 77

