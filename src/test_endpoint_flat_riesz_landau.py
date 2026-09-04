from __future__ import annotations

import math
from fractions import Fraction

import mpmath as mp
import pytest

from endpoint_flat_riesz_landau import (
    endpoint_flat_beta_coefficients,
    endpoint_flat_beta_continuum,
    endpoint_flat_beta_mellin_target,
    endpoint_flat_beta_ramp,
    endpoint_flat_beta_weight,
    endpoint_flat_beta_weight_exact,
    endpoint_flat_riesz_derivative_numerator,
    endpoint_flat_riesz_error,
    fixed_orientation_bad_mass,
)
from pole_killing_boundary_calculus import endpoint_flat_exponential_coefficients
from shifted_psi_ramp_bridge import von_mangoldt_table


def test_beta_coefficients_equal_the_minimal_consecutive_rate_filter() -> None:
    for order in range(7):
        assert endpoint_flat_beta_coefficients(order) == (
            endpoint_flat_exponential_coefficients(
                tuple(range(order + 2)), notch_order=1
            )
        )


def test_closed_beta_weight_equals_its_exact_polynomial() -> None:
    for order in range(7):
        coefficients = endpoint_flat_beta_coefficients(order)
        for ratio in (Fraction(0), Fraction(1, 7), Fraction(2, 3), Fraction(1)):
            polynomial = sum(
                (coefficient * ratio**index
                 for index, coefficient in enumerate(coefficients)),
                Fraction(0),
            )
            assert endpoint_flat_beta_weight_exact(order, ratio) == polynomial


def test_beta_weight_has_the_exact_endpoint_order_and_single_front() -> None:
    for order in range(1, 7):
        front = Fraction(1, order + 2)
        assert endpoint_flat_beta_weight_exact(order, front) == 0
        assert endpoint_flat_beta_weight_exact(order, Fraction(0)) < 0
        assert endpoint_flat_beta_weight_exact(order, Fraction(1)) == 0
        assert endpoint_flat_beta_weight_exact(order, (front + 1) / 2) > 0


def test_beta_mellin_transform_matches_the_rational_target() -> None:
    mp.mp.dps = 60
    for order in range(6):
        s = mp.mpf("1.7")
        integral = mp.quad(
            lambda y: endpoint_flat_beta_weight(order, float(y))
            * y ** (s - 1),
            [0, 1],
        )
        target = (s - 1) / mp.fprod(s + index for index in range(order + 2))
        assert abs(integral - target) < mp.mpf("1e-16")
        assert endpoint_flat_beta_mellin_target(order, Fraction(7, 4)) == (
            Fraction(3, 4)
            / math.prod(
                (Fraction(7, 4) + index for index in range(order + 2)),
                start=Fraction(1),
            )
        )


def test_order_zero_is_the_original_r96_ramp() -> None:
    table = von_mangoldt_table(100)
    x = 97.25
    expected = math.fsum(
        table[n] * (2 * n / x - 1) for n in range(2, 98) if table[n]
    ) - 1 + 1 / x
    assert endpoint_flat_beta_ramp(0, x, table) == pytest.approx(expected)


def test_first_endpoint_flat_formula_is_the_quadratic_weight() -> None:
    table = von_mangoldt_table(100)
    x = 97.25
    expected = math.fsum(
        table[n] * (-0.5 + 2 * n / x - 1.5 * (n / x) ** 2)
        for n in range(2, 98)
        if table[n]
    ) - 0.5 * (1 - 1 / x) ** 2
    assert endpoint_flat_beta_ramp(1, x, table) == pytest.approx(expected)


def test_riesz_derivative_identity_by_finite_difference() -> None:
    table = von_mangoldt_table(200)
    x = 150.25
    step = 1e-4
    for order in range(5):
        numerical_derivative = (
            endpoint_flat_riesz_error(order, x + step, table)
            - endpoint_flat_riesz_error(order, x - step, table)
        ) / (2 * step)
        exact_numerator = endpoint_flat_riesz_derivative_numerator(
            order, x, table
        )
        assert x * x * numerical_derivative == pytest.approx(
            exact_numerator, abs=2e-8
        )


def test_continuum_and_fixed_orientation_jordan_mass() -> None:
    assert endpoint_flat_beta_continuum(1, 2.0) == pytest.approx(1 / 8)
    values = (-3.0, 2.0, -1.0)
    weights = (0.5, 2.0, 1.0)
    assert fixed_orientation_bad_mass(values, weights, orientation=1) == 2.5
    assert fixed_orientation_bad_mass(values, weights, orientation=-1) == 4.0


def test_invalid_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        endpoint_flat_beta_coefficients(-1)
    with pytest.raises(ValueError):
        endpoint_flat_beta_weight(1, 1.1)
    with pytest.raises(ValueError):
        fixed_orientation_bad_mass((1.0,), orientation=0)  # type: ignore[arg-type]

