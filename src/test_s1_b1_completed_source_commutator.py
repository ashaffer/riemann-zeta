"""Regression tests for the exact S1-B1 algebraic audit."""

from __future__ import annotations

import cmath

import numpy as np

from s1_b1_completed_source_commutator import (
    divisor_convolution_matrix,
    narrow_shell_replay,
    odd_projection,
    q_h_multiplier,
    q_h_reflection_difference,
    reflect,
    reflection_multiplier_closed_form,
    reflection_multiplier_commutator,
    two_commutator_closed_form,
    weighted_mobius_values,
    window_commutator,
)


def test_c_convolved_with_one_is_von_mangoldt_on_finite_section() -> None:
    limit = 160
    coefficients = weighted_mobius_values(limit)
    convolution = divisor_convolution_matrix(coefficients)
    recovered = np.real_if_close(convolution @ np.ones(limit))
    expected = np.zeros(limit)
    for n in range(1, limit + 1):
        value = 0.0
        prime = 2
        remainder = n
        while prime * prime <= remainder:
            if remainder % prime:
                prime += 1
                continue
            exponent = 0
            while remainder % prime == 0:
                remainder //= prime
                exponent += 1
            if remainder == 1 and exponent > 0:
                value = np.log(prime)
            break
        else:
            if remainder > 1:
                value = np.log(remainder)
        expected[n - 1] = value
    np.testing.assert_allclose(recovered, expected, atol=2e-14)


def test_window_commutator_has_exact_kernel_difference() -> None:
    limit = 40
    coefficients = weighted_mobius_values(limit)
    operator = divisor_convolution_matrix(coefficients)
    weight = np.linspace(-0.7, 1.3, limit) ** 2
    commutator = window_commutator(weight, operator)
    expected = np.zeros_like(commutator)
    for n in range(1, limit + 1):
        for divisor in range(1, n + 1):
            if n % divisor == 0:
                expected[n - 1, divisor - 1] = (
                    coefficients[n // divisor]
                    * (weight[n - 1] - weight[divisor - 1])
                )
    np.testing.assert_allclose(commutator, expected, atol=2e-14)


def test_literal_narrow_shell_commutator_is_exactly_the_source() -> None:
    for limit in (64, 128, 256):
        replay = narrow_shell_replay(
            limit=limit, shell_start=limit // 3, shell_end=limit // 2
        )
        assert replay.source_norm > 0.0
        assert replay.inner_weight_residual_norm < 1e-13
        assert abs(replay.commutator_norm - replay.source_norm) < 1e-13
        assert replay.exterior_leakage_norm > 0.0


def test_reflection_commutator_closed_form() -> None:
    rng = np.random.default_rng(2301)
    multiplier = rng.normal(size=18) + 1j * rng.normal(size=18)
    values = rng.normal(size=18) + 1j * rng.normal(size=18)
    np.testing.assert_allclose(
        reflection_multiplier_commutator(multiplier, values),
        reflection_multiplier_closed_form(multiplier, values),
        atol=2e-14,
    )


def test_even_multiplier_has_zero_reflection_commutator() -> None:
    rng = np.random.default_rng(2302)
    half = rng.normal(size=9) + 1j * rng.normal(size=9)
    multiplier = np.concatenate([half, half[::-1]])
    values = rng.normal(size=18) + 1j * rng.normal(size=18)
    np.testing.assert_allclose(
        reflection_multiplier_commutator(multiplier, values), 0.0, atol=2e-14
    )


def test_qh_reflection_difference_factorization() -> None:
    for step, z in (
        (0.13, 0.21 + 3.7j),
        (0.7, -0.31 + 2.2j),
        (1.4, 1.1j),
    ):
        lhs = q_h_multiplier(step, z) - q_h_multiplier(step, -z)
        rhs = q_h_reflection_difference(step, z)
        assert abs(lhs - rhs) < 2e-13


def test_two_reflection_commutators_return_scalar_multiplication() -> None:
    rng = np.random.default_rng(2303)
    first = rng.normal(size=20) + 1j * rng.normal(size=20)
    second = rng.normal(size=20) + 1j * rng.normal(size=20)
    values = rng.normal(size=20) + 1j * rng.normal(size=20)
    iterated = reflection_multiplier_commutator(
        first, reflection_multiplier_commutator(second, values)
    )
    np.testing.assert_allclose(
        iterated,
        two_commutator_closed_form(first, second, values),
        atol=2e-14,
    )


def test_odd_projection_is_an_idempotent_on_reflected_grid() -> None:
    values = np.array([1 + 2j, 3 - 4j, -2 + 1j, 7 + 3j])
    np.testing.assert_allclose(odd_projection(odd_projection(values)), odd_projection(values))
    np.testing.assert_allclose(reflect(odd_projection(values)), -odd_projection(values))

