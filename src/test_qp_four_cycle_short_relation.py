from qp_four_cycle_short_relation import (
    invertible_fiber_ledger,
    rank_one_fiber_ledger,
)


def test_invertible_relation_product_completion() -> None:
    # det(e)=-1.  Both bases have common fibre level H=7.
    ledger = invertible_fiber_ledger(
        (1, 2, 3, 5),
        (7, 0),
        (14, 7),
        4,
        3,
    )
    assert ledger.colors == (15, 4, 29, 16)
    assert ledger.relation_value == 0
    assert ledger.color_determinant == 124
    assert ledger.mixed_coefficient == 1
    assert ledger.polynomial_determinant == ledger.color_determinant
    assert ledger.completed_product_left == ledger.completed_product_right


def test_rank_one_relation_tangent_factorization() -> None:
    ledger = rank_one_fiber_ledger(
        (1, 1),
        (1, 1),
        (1, 0),
        3,
        10,
        14,
    )
    assert ledger.colors == (13, 10, 17, 14)
    assert ledger.relation == (1, 1, 1, 1)
    assert ledger.relation_value == 0
    assert ledger.color_determinant == 12
    assert ledger.second_factor == 4
    assert ledger.factored_determinant == ledger.color_determinant
    assert ledger.first_vertical_level == -4
    assert ledger.second_vertical_level == -4


def test_signed_rank_one_relation() -> None:
    # s1*u0-s2*v0 = 2*1-(-1)*(-1)=1.
    ledger = rank_one_fiber_ledger(
        (2, -1),
        (2, -1),
        (1, -1),
        -3,
        5,
        -4,
    )
    assert ledger.relation_value == 0
    assert ledger.color_determinant == ledger.factored_determinant
    assert ledger.first_vertical_level == (
        -ledger.second_factor * -1
    )
    assert ledger.second_vertical_level == (
        -ledger.second_factor * 2
    )
