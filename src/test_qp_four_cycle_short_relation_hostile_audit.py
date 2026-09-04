from fractions import Fraction

import pytest

from qp_four_cycle_short_relation import (
    determinant,
    invertible_fiber_ledger,
    rank_one_fiber_ledger,
)


@pytest.mark.parametrize(
    "relation,left_base,right_base,s,t",
    [
        ((1, 2, 3, 5), (7, 0), (14, 7), 4, 3),
        ((2, -1, 1, 1), (3, 5), (11, 0), -2, 4),
        ((-1, 2, 3, -2), (4, -1), (0, -1), 3, -4),
    ],
)
def test_invertible_completion_identity_with_signs(
    relation, left_base, right_base, s, t
) -> None:
    ledger = invertible_fiber_ledger(
        relation, left_base, right_base, s, t
    )
    assert determinant(relation) != 0
    assert ledger.relation_value == 0
    assert ledger.color_determinant == ledger.polynomial_determinant
    assert ledger.completed_product_left == ledger.completed_product_right


@pytest.mark.parametrize(
    "row,column,bezout,h,p,q",
    [
        ((1, 1), (1, 1), (1, 0), 3, 10, 14),
        ((2, -1), (2, -1), (1, -1), -3, 5, -4),
        ((-2, 3), (3, 2), (1, 1), 4, -7, 9),
    ],
)
def test_rank_one_factorization_with_signs(row, column, bezout, h, p, q) -> None:
    ledger = rank_one_fiber_ledger(row, column, bezout, h, p, q)
    assert ledger.relation_value == 0
    assert ledger.color_determinant == ledger.factored_determinant
    assert ledger.first_vertical_level == -column[1] * ledger.second_factor
    assert ledger.second_vertical_level == -column[0] * ledger.second_factor


def test_exact_47_over_128_exponent_ledger() -> None:
    relation_cutoff = Fraction(1, 16)
    short_fourth_trace = 1 + 5 * relation_cutoff
    long_fourth_trace = Fraction(3, 2) - relation_cutoff / 2
    operator = long_fourth_trace / 4
    transverse = Fraction(1, 2) + operator * Fraction(16, 33)

    assert short_fourth_trace == Fraction(21, 16)
    assert long_fourth_trace == Fraction(47, 32)
    assert short_fourth_trace < long_fourth_trace
    assert operator == Fraction(47, 128)
    assert transverse == Fraction(179, 264)
    assert Fraction(45, 66) - transverse == Fraction(1, 264)
