#!/usr/bin/env python3
"""Exact algebra for the candidate-relative reserve fail-fast gate.

The module checks two facts used in the accompanying theorem card.

* A clean finite-power detector at a simple zero is locally the original
  logarithmic-derivative detector after integration by parts.
* The smallest coherent enlargement of a one-dimensional carrier is a
  two-channel Hermitian compression.  Its phase-optimized reserve is an
  elementary exact expression.

Nothing here estimates the actual von Mangoldt coefficients.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Mapping


Rational = Fraction
Series = dict[int, Rational]


def _convolve(left: Mapping[int, Rational], right: Mapping[int, Rational]) -> Series:
    out: Series = {}
    for left_power, left_value in left.items():
        for right_power, right_value in right.items():
            power = left_power + right_power
            out[power] = out.get(power, Fraction(0)) + left_value * right_value
    return {power: value for power, value in out.items() if value}


def series_power(series: Mapping[int, Rational], exponent: int) -> Series:
    """Raise a finite Laurent series to a nonnegative integral power."""

    if exponent < 0:
        raise ValueError("the exponent must be nonnegative")
    result: Series = {0: Fraction(1)}
    base = dict(series)
    for _ in range(exponent):
        result = _convolve(result, base)
    return result


def series_derivative(series: Mapping[int, Rational], order: int) -> Series:
    """Differentiate a finite Laurent series exactly."""

    if order < 0:
        raise ValueError("the derivative order must be nonnegative")
    result = dict(series)
    for _ in range(order):
        differentiated: Series = {}
        for power, value in result.items():
            if power:
                differentiated[power - 1] = value * power
        result = differentiated
    return result


def product_residue(left: Mapping[int, Rational], right: Mapping[int, Rational]) -> Rational:
    """Return the coefficient of z^-1 in a product."""

    return sum(
        left_value * right.get(-1 - left_power, Fraction(0))
        for left_power, left_value in left.items()
    )


def clean_power_residues(
    degree: int,
    multiplicity: int,
    analytic_germ: Iterable[Rational],
    test_tail: Iterable[Rational],
) -> tuple[Rational, Rational]:
    """Compare ``Res H X^degree`` with its differentiated linear detector.

    ``X=m/z+a_0+a_1*z+...`` and ``H`` starts at order ``degree-1``.
    The second value is

        Res H * m^(degree-1) * (-1)^(degree-1)/(degree-1)! * X^(degree-1),

    where the superscript on the last ``X`` denotes differentiation.
    """

    if degree < 1:
        raise ValueError("degree must be positive")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")

    x_series: Series = {-1: Fraction(multiplicity)}
    for power, value in enumerate(analytic_germ):
        x_series[power] = Fraction(value)

    h_series: Series = {}
    for offset, value in enumerate(test_tail):
        h_series[degree - 1 + offset] = Fraction(value)

    nonlinear = product_residue(h_series, series_power(x_series, degree))
    derivative = series_derivative(x_series, degree - 1)
    scale = Fraction(
        multiplicity ** (degree - 1) * ((-1) ** (degree - 1)),
        math.factorial(degree - 1),
    )
    linearized = product_residue(
        h_series, {power: scale * value for power, value in derivative.items()}
    )
    return nonlinear, linearized


def contact_leading_coefficient(
    polynomial_rows: Iterable[Iterable[complex]],
    weights: Iterable[float],
    multiplicity: int = 1,
) -> tuple[int, float]:
    """Leading pole coefficient of a positive polynomial covariance.

    Each row stores coefficients in increasing powers of ``X``.  The energy
    is ``sum_j weight_j |P_j(X)|^2``.  Near a zero, ``X~m/z``.  If any row is
    nonconstant and every weight is positive, the returned coefficient of
    ``|z|^(-2*d)`` is strictly positive.
    """

    rows = [list(row) for row in polynomial_rows]
    row_weights = list(weights)
    if len(rows) != len(row_weights):
        raise ValueError("one positive weight is required for each row")
    if any(weight <= 0 for weight in row_weights):
        raise ValueError("all covariance weights must be positive")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")

    degrees: list[int] = []
    for row in rows:
        degree = 0
        for index, coefficient in enumerate(row):
            if coefficient:
                degree = index
        degrees.append(degree)
    maximum_degree = max(degrees, default=0)
    coefficient = sum(
        weight
        * abs(row[maximum_degree] if maximum_degree < len(row) else 0j) ** 2
        for row, weight, degree in zip(rows, row_weights, degrees)
        if degree == maximum_degree
    ) * multiplicity ** (2 * maximum_degree)
    return maximum_degree, coefficient


def direct_two_channel_reserve(
    eta: float,
    r: float,
    c: float,
    z: complex,
    phase: float,
) -> float:
    """Evaluate the reserve on sqrt(eta)e+exp(i phase)sqrt(1-eta)v."""

    if not 0 <= eta <= 1:
        raise ValueError("eta must lie in [0,1]")
    return (
        eta * r
        + (1 - eta) * c
        + 2
        * math.sqrt(eta * (1 - eta))
        * (z * cmath.exp(1j * phase)).real
    )


def phase_optimized_two_channel_reserve(
    eta: float, r: float, c: float, z: complex
) -> tuple[float, float]:
    """Return the exact maximum and a maximizing phase."""

    phase = -cmath.phase(z) if z else 0.0
    maximum = eta * r + (1 - eta) * c + 2 * math.sqrt(
        eta * (1 - eta)
    ) * abs(z)
    return maximum, phase


def transverse_scale_floor(
    eta: float,
    epsilon: float,
    carrier: float,
    r: float,
) -> float:
    """Necessary lower bound for max(c_+, |z|) in a successful 2D block."""

    if not 0 < eta < 1:
        raise ValueError("eta must lie strictly between zero and one")
    if epsilon < 0 or carrier <= 0:
        raise ValueError("epsilon must be nonnegative and carrier positive")
    deficit = max(0.0, epsilon * eta * carrier - eta * r)
    denominator = (1 - eta) + 2 * math.sqrt(eta * (1 - eta))
    return deficit / denominator


def polarize_cross_entry(
    q_plus: float,
    q_minus: float,
    q_plus_i: float,
    q_minus_i: float,
) -> complex:
    """Recover e^* A v from four real Hermitian quadratic evaluations."""

    return (q_plus - q_minus) / 4 - 1j * (q_plus_i - q_minus_i) / 4


@dataclass(frozen=True)
class TwoChannelLedger:
    eta: float
    epsilon: float
    carrier: float
    r: float
    c: float
    z: complex

    def optimized_reserve(self) -> float:
        return phase_optimized_two_channel_reserve(
            self.eta, self.r, self.c, self.z
        )[0]

    def target(self) -> float:
        return self.epsilon * self.eta * self.carrier

    def closes_algebraic_gate(self) -> bool:
        return self.optimized_reserve() >= self.target()


def self_check() -> dict[str, object]:
    nonlinear_checks: dict[int, str] = {}
    for degree in range(1, 9):
        nonlinear, linearized = clean_power_residues(
            degree,
            multiplicity=3,
            analytic_germ=[Fraction(2, 3), Fraction(-5, 7), Fraction(11, 13)],
            test_tail=[Fraction(17, 19), Fraction(-23, 29), Fraction(31, 37)],
        )
        assert nonlinear == linearized
        nonlinear_checks[degree] = str(nonlinear)

    contact_degree, contact_coefficient = contact_leading_coefficient(
        [[1, 2 - 1j, 3], [2, -4j], [7]], [1.0, 2.0, 3.0], multiplicity=2
    )
    assert contact_degree == 2
    assert contact_coefficient > 0

    eta = 0.73
    r = -2.0
    c = 5.0
    z = 3 - 4j
    optimized, phase = phase_optimized_two_channel_reserve(eta, r, c, z)
    direct = direct_two_channel_reserve(eta, r, c, z, phase)
    assert math.isclose(optimized, direct, rel_tol=1e-13, abs_tol=1e-13)

    q_e = 7.0
    q_v = -2.0
    q_plus = q_e + q_v + 2 * z.real
    q_minus = q_e + q_v - 2 * z.real
    q_plus_i = q_e + q_v - 2 * z.imag
    q_minus_i = q_e + q_v + 2 * z.imag
    assert abs(polarize_cross_entry(q_plus, q_minus, q_plus_i, q_minus_i) - z) < 1e-12

    return {
        "clean_power_degrees": nonlinear_checks,
        "positive_contact_degree": contact_degree,
        "positive_contact_coefficient": contact_coefficient,
        "two_channel_phase_identity": True,
        "polarization_identity": True,
        "scope": "algebraic gate only; no actual-Lambda estimate",
    }


if __name__ == "__main__":
    print(self_check())
