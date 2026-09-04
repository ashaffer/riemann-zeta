from __future__ import annotations

import cmath
import math
from fractions import Fraction

import pytest


def prime_divisors(n: int) -> tuple[int, ...]:
    factors: list[int] = []
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            factors.append(p)
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def mobius(n: int) -> int:
    factors = prime_divisors(n)
    if any(n % (p * p) == 0 for p in factors):
        return 0
    return -1 if len(factors) % 2 else 1


def jordan_ratio(n: int, order: int) -> Fraction:
    value = Fraction(1)
    for p in prime_divisors(n):
        value *= 1 - Fraction(1, p**order)
    return value


def von_mangoldt(n: int) -> float:
    factors = prime_divisors(n)
    if len(factors) != 1:
        return 0.0
    return math.log(factors[0])


def sawtooth_kernel(y: float) -> float:
    count = math.floor(y)
    return count * (count + 1 - y) / y


def test_euler_jordan_cocycle_is_exact_on_coefficients() -> None:
    for n in range(1, 80):
        for z, w in ((1, 1), (1, 2), (2, 3)):
            left = jordan_ratio(n, z + w)
            right = sum(
                jordan_ratio(n // d, z)
                * Fraction(1, d**z)
                * jordan_ratio(d, w)
                for d in divisors(n)
            )
            assert left == right


def test_boundary_derivative_is_von_mangoldt() -> None:
    for n in range(1, 200):
        derivative = -sum(mobius(d) * math.log(d) for d in divisors(n))
        assert derivative == pytest.approx(von_mangoldt(n), abs=3e-14)


def test_positive_sawtooth_formula_and_bounds() -> None:
    for tenth in range(10, 1000):
        y = tenth / 10
        count = math.floor(y)
        direct = sum(2 * m / y - 1 for m in range(1, count + 1))
        closed = count * (1 - (y - count)) / y
        assert sawtooth_kernel(y) == pytest.approx(direct, abs=3e-14)
        assert sawtooth_kernel(y) == pytest.approx(closed, abs=3e-14)
        assert 0 <= sawtooth_kernel(y) <= 1


def test_r95_direct_and_mobius_tangent_formulas_match() -> None:
    for x in (10.0, 37.25, 101.75, 256.0):
        direct = sum(
            von_mangoldt(n) * (2 * n / x - 1)
            for n in range(1, math.floor(x) + 1)
        ) - (1 - 1 / x)
        transformed = -sum(
            mobius(d) * math.log(d) * sawtooth_kernel(x / d)
            for d in range(1, math.floor(x) + 1)
        ) - (1 - 1 / x)
        assert direct == pytest.approx(transformed, abs=2e-12)


def test_sparse_surgery_local_coefficients_obey_the_geometric_bound() -> None:
    q = 3
    d = 0.4
    gamma = 0.7
    prime = 1_000_003
    a = prime ** (-d - 1j * gamma)

    numerator = [1.0 + 0.0j]
    for root in (a,) * q + (a.conjugate(),) * q:
        updated = [0.0j] * (len(numerator) + 1)
        for index, coefficient in enumerate(numerator):
            updated[index] += coefficient
            updated[index + 1] -= root * coefficient
        numerator = updated

    local_coefficients = []
    partial = 0.0j
    for coefficient in numerator:
        partial += coefficient
        local_coefficients.append(partial)

    tail = abs(1 - a) ** (2 * q)
    assert (1 + abs(a)) ** (2 * q) < 2
    assert all(abs(value.imag) < 1e-14 for value in local_coefficients)
    assert all(value.real > 0 for value in local_coefficients)
    assert local_coefficients[-1].real == pytest.approx(tail)

    for power in range(1, 8):
        logarithmic_coefficient = 1 - 2 * q * prime ** (-power * d) * math.cos(
            power * gamma * math.log(prime)
        )
        assert logarithmic_coefficient > 0


def test_scalar_zero_boundary_layer_has_critical_interior_size_but_full_tangent() -> None:
    beta = 0.93
    gamma = 14.1
    phase = 0.2
    x = 10_000.0

    def carrier(z: float) -> float:
        return z * x ** (beta - z) * math.cos(gamma * math.log(x) + phase)

    for z in (0.01, 0.1, 0.4):
        assert abs(carrier(z)) <= z * x ** (1 - z)

    step = 1e-7
    numerical_tangent = (carrier(step) - carrier(-step)) / (2 * step)
    exact_tangent = x**beta * math.cos(gamma * math.log(x) + phase)
    assert numerical_tangent == pytest.approx(exact_tangent, rel=2e-9)


def test_poisson_fourier_semigroup_multiplier() -> None:
    for frequency in (0.0, 0.4, 3.0, 20.0):
        for a, b in ((0.2, 0.7), (1.0, 2.0)):
            assert cmath.exp(-(a + b) * abs(frequency)) == pytest.approx(
                cmath.exp(-a * abs(frequency))
                * cmath.exp(-b * abs(frequency))
            )
