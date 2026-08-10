#!/usr/bin/env python3
"""Exact principal-pole ledger for a high-order Mellin detector.

This module proves no zero-free region.  It isolates the finite algebra behind
the central Mellin pole discovered in the proportional-order mollifier audit.

In the principal simple-pole model, after writing ``z = w - 1`` and
``L = log(Y)``, the fixed first-order auxiliary kernel produces

    exp(L*z) / (z**(k-1) * (z-z0)).

Shifting the contour crosses both ``z=z0`` and, for ``k>1``, ``z=0``.  The
target residue and the complete central residue polynomial combine exactly as

    [exp(L*z0) - sum_{n=0}^{k-2} (L*z0)^n/n!] / z0^(k-1).

Thus the completed carrier is an exponential Taylor remainder.  For positive
real ``z0=delta`` and ``k ~ alpha*L`` its target-survival fraction is a Poisson
upper tail.  It tends to zero when ``delta<alpha`` and to one when
``delta>alpha``.  This resolves the apparent absolute-convergence paradox for
large ``alpha`` without treating the central polynomial as an error.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass

from high_order_mollifier_shift import naive_carrier_rate


@dataclass(frozen=True)
class PrincipalPoleLedger:
    """Exact target/center decomposition in the principal simple-pole model."""

    order: int
    log_scale: float
    pole_offset: complex
    target_residue: complex
    central_residue: complex
    completed_residue: complex
    target_survival_fraction: complex


def _require_order(order: int) -> None:
    if not isinstance(order, int) or isinstance(order, bool) or order < 1:
        raise ValueError("order must be a positive integer")


def _require_log_scale(log_scale: float) -> None:
    if not math.isfinite(log_scale) or log_scale <= 0.0:
        raise ValueError("log_scale must be finite and strictly positive")


def _require_nonzero_finite_complex(value: complex, name: str) -> complex:
    answer = complex(value)
    if (
        not math.isfinite(answer.real)
        or not math.isfinite(answer.imag)
        or answer == 0.0
    ):
        raise ValueError(f"{name} must be finite and nonzero")
    return answer


def truncated_exponential(value: complex, degree: int) -> complex:
    """Return ``sum_{n=0}^degree value^n/n!``; degree ``-1`` means zero."""

    if not isinstance(degree, int) or isinstance(degree, bool) or degree < -1:
        raise ValueError("degree must be an integer of at least minus one")
    z = complex(value)
    if not math.isfinite(z.real) or not math.isfinite(z.imag):
        raise ValueError("value must be finite")
    if degree == -1:
        return 0.0j
    total = 1.0 + 0.0j
    term = 1.0 + 0.0j
    for n in range(1, degree + 1):
        term *= z / n
        total += term
    return total


def target_simple_pole_residue(
    order: int, log_scale: float, pole_offset: complex
) -> complex:
    """Residue at the target pole before adding the central residue."""

    _require_order(order)
    _require_log_scale(log_scale)
    z0 = _require_nonzero_finite_complex(pole_offset, "pole_offset")
    return cmath.exp(log_scale * z0) / z0 ** (order - 1)


def central_residue_polynomial_coefficients(
    order: int, pole_offset: complex
) -> tuple[complex, ...]:
    r"""Coefficients of the central residue polynomial in ``L``.

    The returned tuple ``c`` satisfies

    ``central(L) = sum_n c[n] * L**n``.

    For ``order=1`` there is no central pole and the tuple is empty.
    """

    _require_order(order)
    z0 = _require_nonzero_finite_complex(pole_offset, "pole_offset")
    pole_power = order - 1
    return tuple(
        -1.0 / (math.factorial(n) * z0 ** (pole_power - n))
        for n in range(pole_power)
    )


def evaluate_polynomial(coefficients: tuple[complex, ...], value: float) -> complex:
    """Evaluate coefficients in ascending power order by Horner's rule."""

    if not math.isfinite(value):
        raise ValueError("value must be finite")
    total = 0.0 + 0.0j
    for coefficient in reversed(coefficients):
        total = total * value + coefficient
    return total


def central_simple_pole_residue(
    order: int, log_scale: float, pole_offset: complex
) -> complex:
    """Complete residue at the new central pole ``w=1``."""

    _require_log_scale(log_scale)
    coefficients = central_residue_polynomial_coefficients(order, pole_offset)
    return evaluate_polynomial(coefficients, log_scale)


def completed_simple_pole_residue(
    order: int, log_scale: float, pole_offset: complex
) -> complex:
    """Target plus central residue, evaluated without any asymptotic step."""

    return target_simple_pole_residue(order, log_scale, pole_offset) + (
        central_simple_pole_residue(order, log_scale, pole_offset)
    )


def completed_tail_formula(
    order: int, log_scale: float, pole_offset: complex
) -> complex:
    """Equivalent exponential-Taylor-remainder formula."""

    _require_order(order)
    _require_log_scale(log_scale)
    z0 = _require_nonzero_finite_complex(pole_offset, "pole_offset")
    degree = order - 2
    remainder = cmath.exp(log_scale * z0) - truncated_exponential(
        log_scale * z0, degree
    )
    return remainder / z0 ** (order - 1)


def target_survival_fraction(
    order: int, log_scale: float, pole_offset: complex
) -> complex:
    """Completed residue divided by the uncompleted target residue."""

    _require_order(order)
    _require_log_scale(log_scale)
    z0 = _require_nonzero_finite_complex(pole_offset, "pole_offset")
    return 1.0 - cmath.exp(-log_scale * z0) * truncated_exponential(
        log_scale * z0, order - 2
    )


def real_target_survival_fraction(
    order: int, log_scale: float, displacement: float
) -> float:
    r"""Real positive specialization of the survival fraction.

    It is the Poisson upper-tail probability

    ``P(Poisson(delta*L) >= order-1)``

    up to floating-point rounding.
    """

    if not math.isfinite(displacement) or displacement <= 0.0:
        raise ValueError("displacement must be finite and strictly positive")
    value = target_survival_fraction(order, log_scale, displacement)
    tolerance = 200.0 * math.ulp(1.0) * max(1.0, abs(value))
    if abs(value.imag) > tolerance:
        raise RuntimeError("real specialization developed an imaginary part")
    answer = value.real
    if answer < 0.0 and answer > -tolerance:
        answer = 0.0
    if answer > 1.0 and answer < 1.0 + tolerance:
        answer = 1.0
    if not 0.0 <= answer <= 1.0:
        raise RuntimeError("survival fraction left the exact interval [0,1]")
    return answer


def principal_pole_ledger(
    order: int, log_scale: float, pole_offset: complex
) -> PrincipalPoleLedger:
    """Build the exact finite residue ledger."""

    target = target_simple_pole_residue(order, log_scale, pole_offset)
    central = central_simple_pole_residue(order, log_scale, pole_offset)
    completed = target + central
    return PrincipalPoleLedger(
        order=order,
        log_scale=log_scale,
        pole_offset=complex(pole_offset),
        target_residue=target,
        central_residue=central,
        completed_residue=completed,
        target_survival_fraction=completed / target,
    )


def predicted_completed_principal_rate(alpha: float, displacement: float) -> float:
    r"""Large-deviation exponent in the positive-real principal-pole model.

    For ``k ~ alpha*L`` the central polynomial cancels the positive naive rate
    when ``delta<=alpha``.  When ``delta>alpha``, the Poisson upper tail tends
to one and the naive rate survives.

    This is a principal-pole model ledger, not a complete high-order
    zero-free criterion for zeta.
    """

    if not math.isfinite(alpha) or alpha <= 0.0:
        raise ValueError("alpha must be finite and strictly positive")
    if not math.isfinite(displacement) or displacement <= 0.0:
        raise ValueError("displacement must be finite and strictly positive")
    if displacement <= alpha:
        return 0.0
    return naive_carrier_rate(alpha, displacement)
