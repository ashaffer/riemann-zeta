from __future__ import annotations

import cmath
import math

import pytest


def causal_box_multiplier(s: complex, width: float) -> complex:
    return (1 - cmath.exp(-width * s)) / s


def r68_window_multiplier(s: complex, h: float, k: int) -> complex:
    length = h * k
    if abs(s) < 1e-14:
        return complex(length)
    return (
        2 * cmath.sinh(length * s / 2) / s
        * (cmath.sinh(h * s / 2) / (h * s / 2)) ** k
    )


def test_strip_width_maps_to_the_r68_energy_exponent() -> None:
    for delta in (0.01, 0.1, 0.25, 0.49, 0.5):
        displacement = 0.5 - delta
        assert 2 * displacement == pytest.approx(1 - 2 * delta)


def test_separate_square_root_rectangles_receive_only_half_the_saving() -> None:
    for delta in (0.02, 0.1, 0.3, 0.49):
        mobius_factor_exponent_in_x = 0.25 - delta / 2
        prime_factor_exponent_in_x = 0.25
        rectangle_exponent = (
            mobius_factor_exponent_in_x + prime_factor_exponent_in_x
        )
        assert rectangle_exponent == pytest.approx(0.5 - delta / 2)


def test_off_diagonal_upper_bound_follows_from_complete_energy() -> None:
    for diagonal, energy in ((0.0, 3.0), (2.0, 7.0), (8.0, 1.0)):
        off_diagonal = energy - diagonal
        assert off_diagonal <= energy
        assert diagonal + off_diagonal == pytest.approx(energy)


def test_fixed_box_multiplier_is_nonzero_in_the_open_right_half_plane() -> None:
    width = 1.7
    for s in (0.01 + 20j, 0.2 + 3.1j, 0.9 - 7j):
        assert abs(causal_box_multiplier(s, width)) > 1e-10

    for integer in (-4, -1, 1, 5):
        zero = 2j * math.pi * integer / width
        assert abs(causal_box_multiplier(zero, width)) < 2e-15


def test_symmetric_strip_quartet_obeys_the_endpoint_power_bound() -> None:
    delta = 0.17
    beta = 1 - delta
    gamma = 4.2
    zeros = (
        beta + 1j * gamma,
        beta - 1j * gamma,
        1 - beta + 1j * gamma,
        1 - beta - 1j * gamma,
    )
    width = 1.3

    def coefficient(rho: complex) -> complex:
        return (
            (1 - rho)
            / (rho * (rho + 1))
            * causal_box_multiplier(rho, width)
        )

    absolute_constant = sum(abs(coefficient(rho)) for rho in zeros)
    for log_x in (1.0, 3.0, 10.0, 40.0):
        contribution = sum(
            coefficient(rho) * cmath.exp(rho * log_x) for rho in zeros
        )
        endpoint_scale = math.exp((1 - delta) * log_x)
        assert abs(contribution) <= absolute_constant * endpoint_scale


def test_fixed_r68_window_retains_every_off_axis_carrier() -> None:
    h = 0.4
    k = 3
    for rho in (0.83 + 4.2j, 0.17 + 4.2j, 0.5 + 7.1j):
        displacement = rho - 0.5
        assert abs(r68_window_multiplier(displacement, h, k)) > 1e-9
