"""Tests for the complete theta-resolvent no-go."""

from __future__ import annotations

import math

from theta_bp_complete_resolvent_nogo import (
    complete_green,
    completion_symbol,
    expanded_completion_symbol,
    first_zero,
    green_total_mass,
    negative_witness,
)


def test_symbol_factorization() -> None:
    for t in (0.0, 0.3, 1.0, 2.75, -4.0):
        for frequency in (-5.0, -0.2, 0.0, 1.25, 8.0):
            assert math.isclose(
                completion_symbol(t, frequency),
                expanded_completion_symbol(t, frequency),
                rel_tol=2e-14,
                abs_tol=2e-14,
            )
            assert completion_symbol(t, frequency) >= 1.0


def test_zero_frequency_limit() -> None:
    for displacement in (0.0, 0.1, 1.0, 4.0):
        expected = complete_green(0.0, displacement)
        observed = complete_green(1e-7, displacement)
        assert math.isclose(observed, expected, rel_tol=2e-13, abs_tol=1e-15)


def test_explicit_negative_witness() -> None:
    for t in (0.01, 0.5, 1.0, 3.0, -7.0):
        displacement, simplified = negative_witness(t)
        assert simplified < 0.0
        assert complete_green(t, displacement) < 0.0
        assert math.isclose(
            complete_green(t, displacement),
            simplified,
            rel_tol=2e-13,
            abs_tol=1e-300,
        )
        assert complete_green(t, 0.0) > 0.0
        assert first_zero(t) < displacement


def test_evenness() -> None:
    for t in (0.0, 0.5, 3.0):
        for displacement in (0.0, 0.4, 2.0):
            assert complete_green(t, displacement) == complete_green(
                -t, displacement
            )
            assert complete_green(t, displacement) == complete_green(
                t, -displacement
            )


def test_total_mass_against_numerical_quadrature() -> None:
    import scipy.integrate

    for t in (0.0, 0.5, 1.0, 3.0):
        integral, error = scipy.integrate.quad(
            lambda x: 2.0 * complete_green(t, x),
            0.0,
            math.inf,
            epsabs=2e-13,
            epsrel=2e-13,
            limit=500,
        )
        assert error < 2e-11
        assert math.isclose(
            integral, green_total_mass(t), rel_tol=2e-11, abs_tol=2e-13
        )
