from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Callable

import mpmath as mp
import pytest


ComplexFunction = Callable[[complex], complex]


def sharp(function: ComplexFunction, s: complex) -> complex:
    return function(s.conjugate()).conjugate()


def reflect_sharp(function: ComplexFunction, s: complex) -> complex:
    return sharp(function, 1 - s)


def r95_multiplier(s: complex) -> complex:
    return (s - 1) / (s * (s + 1))


def causal_box_multiplier(s: complex, width: float) -> complex:
    return (1 - cmath.exp(-width * s)) / s


def test_completion_defect_is_even_and_odd_channel_is_odd() -> None:
    rho = 0.81 + 2.7j

    def logarithmic_derivative(s: complex) -> complex:
        return 1 / (s - rho)

    def defect(s: complex) -> complex:
        return logarithmic_derivative(s) + reflect_sharp(
            logarithmic_derivative, s
        )

    def odd(s: complex) -> complex:
        return logarithmic_derivative(s) - reflect_sharp(
            logarithmic_derivative, s
        )

    for s in (0.37 + 0.9j, 1.2 - 0.4j, -0.3 + 1.7j):
        assert reflect_sharp(defect, s) == pytest.approx(defect(s))
        assert reflect_sharp(odd, s) == pytest.approx(-odd(s))


def test_symmetric_off_line_quartet_has_zero_defect() -> None:
    rho = 0.83 + 3.2j
    orbit = (rho, rho.conjugate(), 1 - rho, 1 - rho.conjugate())

    def polynomial(s: complex) -> complex:
        value = 1.0 + 0.0j
        for zero in orbit:
            value *= s - zero
        return value

    def logarithmic_derivative(s: complex) -> complex:
        return sum(1 / (s - zero) for zero in orbit)

    for s in (0.2 + 0.7j, 0.91 + 1.1j, 1.4 - 0.8j):
        assert polynomial(1 - s) == pytest.approx(polynomial(s))
        assert logarithmic_derivative(1 - s) == pytest.approx(
            -logarithmic_derivative(s)
        )


def test_quartet_r95_carrier_keeps_the_near_one_exponent() -> None:
    beta = 0.83
    gamma = 3.2
    rho = beta + 1j * gamma
    reflected = 1 - beta + 1j * gamma
    coefficient = r95_multiplier(rho)
    reflected_coefficient = r95_multiplier(reflected)

    def carrier(log_x: float) -> float:
        return -2 * (
            (coefficient * cmath.exp(rho * log_x)).real
            + (reflected_coefficient * cmath.exp(reflected * log_x)).real
        )

    phase = cmath.phase(coefficient)
    n = 30
    aligned = (-phase + 2 * math.pi * n) / gamma
    opposed = (-phase + (2 * n + 1) * math.pi) / gamma
    assert carrier(aligned) < 0
    assert carrier(opposed) > 0

    ratio = (
        abs(reflected_coefficient)
        * math.exp((1 - beta) * aligned)
        / (abs(coefficient) * math.exp(beta * aligned))
    )
    assert ratio < 1e-10


def test_fixed_causal_box_has_no_zero_in_the_open_right_half_plane() -> None:
    width = 1.7
    for k in (-4, -1, 1, 5):
        root = 2j * math.pi * k / width
        assert abs(causal_box_multiplier(root, width)) < 2e-15

    for s in (0.1 + 8j, 0.83 + 3.2j, 1.2 - 0.5j):
        assert abs(causal_box_multiplier(s, width)) > 1e-8
        numerical = mp.quad(lambda u: mp.exp(-s * u), [0, width])
        assert complex(numerical) == pytest.approx(
            causal_box_multiplier(s, width), rel=1e-12, abs=1e-12
        )


def test_r95_completion_decomposition_is_exact() -> None:
    rho = 0.77 + 2.1j

    def completed_log_derivative(s: complex) -> complex:
        return 1 / (s - rho) + 0.3 * s

    s = 1.3 + 0.6j
    kappa = 0.2 - 0.1j
    pole_order = 1
    reflected = reflect_sharp(completed_log_derivative, s)
    even_defect = completed_log_derivative(s) + reflected
    odd_channel = completed_log_derivative(s) - reflected
    logarithmic_euler = kappa - completed_log_derivative(s)

    left = r95_multiplier(s) * (
        logarithmic_euler - pole_order / (s - 1)
    )
    right = -r95_multiplier(s) * even_defect / 2 + r95_multiplier(s) * (
        -odd_channel / 2 + kappa - pole_order / (s - 1)
    )
    assert left == pytest.approx(right)


def test_r68_type_i_complement_is_regular_at_a_zero() -> None:
    mobius_head = Fraction(2, 7)
    lambda_head = Fraction(3, 11)
    multiplicity = 3

    for denominator in (10, 100, 1000):
        t = Fraction(1, denominator)
        zeta_value = t**multiplicity
        zeta_derivative = multiplicity * t ** (multiplicity - 1)
        k_value = -zeta_derivative / zeta_value
        type_ii = (1 - zeta_value * mobius_head) * (
            k_value - lambda_head
        )
        type_i = (
            lambda_head
            - mobius_head * zeta_derivative
            - zeta_value * mobius_head * lambda_head
        )
        assert k_value - type_ii == type_i
        assert t * type_ii == -multiplicity - t * lambda_head + (
            multiplicity * mobius_head * zeta_value
            + t * zeta_value * mobius_head * lambda_head
        )


def test_selberg_reflection_parity_algebra() -> None:
    def even_part(s: complex) -> complex:
        u = s - 0.5
        return 2 + u * u

    def even_derivative(s: complex) -> complex:
        return 2 * (s - 0.5)

    def odd_part(s: complex) -> complex:
        u = s - 0.5
        return u + u**3

    def odd_derivative(s: complex) -> complex:
        u = s - 0.5
        return 1 + 3 * u * u

    def selberg(s: complex) -> complex:
        k_value = even_part(s) + odd_part(s)
        k_derivative = even_derivative(s) + odd_derivative(s)
        return k_value * k_value - k_derivative

    for s in (0.31 + 0.8j, 1.2 - 0.6j):
        even_projection = (selberg(s) + selberg(1 - s)) / 2
        odd_projection = (selberg(s) - selberg(1 - s)) / 2
        assert even_projection == pytest.approx(
            even_part(s) ** 2 + odd_part(s) ** 2 - odd_derivative(s)
        )
        assert odd_projection == pytest.approx(
            2 * even_part(s) * odd_part(s) - even_derivative(s)
        )


def test_zeta_logarithmic_derivative_reflection_identity() -> None:
    mp.mp.dps = 60
    s = mp.mpc("0.72", "7.3")

    def completion_derivative(z: mp.mpc) -> mp.mpc:
        return (
            1 / z
            + 1 / (z - 1)
            - mp.log(mp.pi) / 2
            + mp.digamma(z / 2) / 2
        )

    def k_value(z: mp.mpc) -> mp.mpc:
        return -mp.diff(mp.zeta, z) / mp.zeta(z)

    discrepancy = (
        k_value(s)
        + k_value(1 - s)
        - completion_derivative(s)
        - completion_derivative(1 - s)
    )
    assert abs(discrepancy) < mp.mpf("1e-50")
