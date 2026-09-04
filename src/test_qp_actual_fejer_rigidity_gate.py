from fractions import Fraction
from itertools import product

from qp_actual_fejer_rigidity_gate import (
    all_two_colorings_have_three_ap,
    fejer_weights,
    monochromatic_three_ap,
    perturbative_support_exponent,
    project_ledger,
)


def test_w_2_3_is_exactly_nine() -> None:
    assert all_two_colorings_have_three_ap(9)
    assert any(
        monochromatic_three_ap(tuple(colors)) is None
        for colors in product((0, 1), repeat=8)
    )


def test_fejer_weights_are_probability_and_large_on_first_half() -> None:
    for length in (1, 2, 9, 36, 101):
        weights = fejer_weights(length)
        assert sum(weights) == 1
        assert all(weight > 0 for weight in weights)
        assert all(
            weights[index - 1] >= Fraction(1, length)
            for index in range(1, length // 2 + 1)
        )


def test_project_exponent_is_sixteen_over_thirty_three() -> None:
    assert perturbative_support_exponent(Fraction(50, 33)) == Fraction(16, 33)
    assert project_ledger()["maximum_perturbative_support_exponent"] == "16/33"


def test_scope_is_explicitly_method_only() -> None:
    assert project_ledger()["scope"] == "Lipschitz-stable harmonic transfer only"
