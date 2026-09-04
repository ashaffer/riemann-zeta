from fractions import Fraction

import pytest

from qp_guth_maynard_l3_lp import (
    H,
    count_exponent,
    exponent_branches,
    target_exponent,
    third_layer_exponent,
)


def test_project_ledger() -> None:
    assert H == Fraction(16, 33)
    assert target_exponent() == Fraction(4, 33)


def test_claimed_eight_elevenths_threshold_fails() -> None:
    m = Fraction(8, 11)
    v = m / 2
    e = exponent_branches(m, v)
    assert e == {
        "l2": Fraction(-8, 11),
        "common": Fraction(-32, 33),
        "classical": Fraction(-5, 11),
        "gm": Fraction(-28, 55),
    }
    assert count_exponent(m, v) == Fraction(-8, 11)
    assert third_layer_exponent(m, v) == Fraction(4, 11)
    assert third_layer_exponent(m, v) > target_exponent()


@pytest.mark.parametrize(
    "m",
    [Fraction(1, 3), Fraction(1, 2), Fraction(8, 11), Fraction(4, 5)],
)
def test_endpoint_l2_obstruction_through_four_fifths(m: Fraction) -> None:
    assert third_layer_exponent(m, m / 2) == m / 2
    assert third_layer_exponent(m, m / 2) > target_exponent()


@pytest.mark.parametrize("m", [Fraction(4, 5), Fraction(9, 10), Fraction(1)])
def test_high_support_common_obstruction(m: Fraction) -> None:
    assert third_layer_exponent(m, Fraction(1, 5)) == Fraction(1, 5)
    assert Fraction(1, 5) > target_exponent()


def test_one_block_endpoint_is_exact() -> None:
    m = Fraction(8, 33)
    assert third_layer_exponent(m, m / 2) == target_exponent()


def test_domain_validation() -> None:
    with pytest.raises(ValueError):
        exponent_branches(Fraction(1, 2), Fraction(1, 3))
