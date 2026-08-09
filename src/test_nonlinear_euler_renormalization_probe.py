from cmath import exp
from fractions import Fraction
from math import log, pi

import pytest

from nonlinear_euler_renormalization_probe import (
    gc_local_coefficient,
    higher_renormalized_local_coefficients,
    scalar_squarefree_layer_coefficient,
    zero_preserving_example_taylor,
)


def test_exceptional_prime_cancellation_and_quadratic_residual() -> None:
    assert gc_local_coefficient(Fraction(1), 1) == 0
    assert gc_local_coefficient(Fraction(1), 2) == Fraction(-1, 2)
    assert gc_local_coefficient(Fraction(1), 3) == Fraction(-1, 3)


@pytest.mark.parametrize("r", [2, 3, 4, 7])
def test_higher_renormalization_first_surviving_layer(r: int) -> None:
    coefficients = higher_renormalized_local_coefficients(r, r + 2)
    assert coefficients[0] == 1
    assert coefficients[1:r] == [0] * (r - 1)
    assert coefficients[r] == Fraction(-1, r)


def test_zero_preserving_scalar_example_moves_mass_to_semiprimes() -> None:
    coefficients = zero_preserving_example_taylor(4)
    assert coefficients == [
        Fraction(1),
        Fraction(0),
        Fraction(-1, 2),
        Fraction(1, 3),
        Fraction(-1, 8),
    ]
    assert scalar_squarefree_layer_coefficient(coefficients[2], 2) == -1


def test_squarefree_layer_counts_ordered_convolution_assignments() -> None:
    assert scalar_squarefree_layer_coefficient(Fraction(5, 12), 3) == Fraction(-5, 2)


def test_invalid_truncation_parameters_are_rejected() -> None:
    with pytest.raises(ValueError):
        higher_renormalized_local_coefficients(1, 3)
    with pytest.raises(ValueError):
        higher_renormalized_local_coefficients(2, -1)
    with pytest.raises(ValueError):
        scalar_squarefree_layer_coefficient(1, 0)


@pytest.mark.parametrize("k", [-3, -1, 0, 2, 5])
def test_finite_dyadic_zero_factor_has_vertical_lattice(k: int) -> None:
    s = 1 + 2j * pi * k / log(2)
    assert abs(1 - exp((1 - s) * log(2))) < 2e-14
