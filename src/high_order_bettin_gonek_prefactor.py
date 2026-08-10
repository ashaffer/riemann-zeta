#!/usr/bin/env python3
"""Exact finite Taylor completion for the zeta Bettin--Gonek prefactor.

This module proves no zero-free region.  It upgrades the principal simple-pole
ledger in ``high_order_mellin_residue`` by retaining the complete rational
factor that remains after the zeta factors cancel in the zeta specialization
of the Bettin--Gonek contour argument.

With ``z=w-1`` and target offset ``z0=rho-1/2-it``, the relevant factor is

    B_t(z) = (z-1/2+it) / ((z+2)^2 (z+2+it)^3).

For logarithmic cutoff order ``k``, the target and central residues combine as

    [F_t(z0) - Taylor_{k-2}(F_t,0)(z0)] / z0^(k-1),

where ``F_t(z)=exp(Lz)B_t(z)`` and ``L=log(Y)``.  This identity is finite and
exact; the remaining research problem is a uniform growing-order estimate of
that Taylor remainder inside the full mollified moment argument.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class FullPrefactorResidueLedger:
    """Exact target/center decomposition for the complete rational prefactor."""

    order: int
    log_scale: float
    height: float
    target_offset: complex
    target_residue: complex
    central_residue: complex
    completed_residue: complex
    completed_over_target: complex


def _require_order(order: int) -> None:
    if not isinstance(order, int) or isinstance(order, bool) or order < 1:
        raise ValueError("order must be a positive integer")


def _require_log_scale(log_scale: float) -> None:
    if not math.isfinite(log_scale) or log_scale <= 0.0:
        raise ValueError("log_scale must be finite and strictly positive")


def _require_height(height: float) -> None:
    if not math.isfinite(height):
        raise ValueError("height must be finite")


def _require_nonzero_finite_complex(value: complex, name: str) -> complex:
    answer = complex(value)
    if (
        not math.isfinite(answer.real)
        or not math.isfinite(answer.imag)
        or answer == 0.0
    ):
        raise ValueError(f"{name} must be finite and nonzero")
    return answer


def _series_multiply(
    left: tuple[complex, ...], right: tuple[complex, ...], degree: int
) -> tuple[complex, ...]:
    answer = [0.0j] * (degree + 1)
    for i, left_value in enumerate(left):
        if i > degree:
            break
        for j, right_value in enumerate(right):
            if i + j > degree:
                break
            answer[i + j] += left_value * right_value
    return tuple(answer)


def _series_inverse(
    coefficients: tuple[complex, ...], degree: int
) -> tuple[complex, ...]:
    if not coefficients or coefficients[0] == 0.0:
        raise ValueError("the power series must have nonzero constant term")
    answer = [0.0j] * (degree + 1)
    answer[0] = 1.0 / coefficients[0]
    for n in range(1, degree + 1):
        answer[n] = -sum(
            coefficients[j] * answer[n - j]
            for j in range(1, min(n, len(coefficients) - 1) + 1)
        ) / coefficients[0]
    return tuple(answer)


def bettin_gonek_prefactor(value: complex, height: float) -> complex:
    r"""Return ``B_t(z)=(z-1/2+it)/((z+2)^2(z+2+it)^3)``."""

    _require_height(height)
    z = complex(value)
    if not math.isfinite(z.real) or not math.isfinite(z.imag):
        raise ValueError("value must be finite")
    return (z - 0.5 + 1j * height) / (
        (z + 2.0) ** 2 * (z + 2.0 + 1j * height) ** 3
    )


def prefactor_taylor_coefficients(
    height: float, degree: int
) -> tuple[complex, ...]:
    """Taylor coefficients of ``B_t`` at zero through the requested degree."""

    _require_height(height)
    if not isinstance(degree, int) or isinstance(degree, bool) or degree < 0:
        raise ValueError("degree must be a nonnegative integer")
    c = 2.0 + 1j * height
    first_denominator = (4.0 + 0.0j, 4.0 + 0.0j, 1.0 + 0.0j)
    second_denominator = (c**3, 3.0 * c**2, 3.0 * c, 1.0 + 0.0j)
    denominator = _series_multiply(
        first_denominator, second_denominator, degree
    )
    reciprocal = _series_inverse(denominator, degree)
    numerator = (-0.5 + 1j * height, 1.0 + 0.0j)
    return _series_multiply(numerator, reciprocal, degree)


def completed_factor_taylor_coefficients(
    log_scale: float, height: float, degree: int
) -> tuple[complex, ...]:
    """Taylor coefficients of ``exp(Lz) B_t(z)`` at zero."""

    _require_log_scale(log_scale)
    coefficients = prefactor_taylor_coefficients(height, degree)
    exponential = tuple(
        log_scale**n / math.factorial(n) for n in range(degree + 1)
    )
    return _series_multiply(coefficients, exponential, degree)


def evaluate_taylor(
    coefficients: tuple[complex, ...], value: complex
) -> complex:
    """Evaluate an ascending-order Taylor coefficient tuple."""

    z = complex(value)
    if not math.isfinite(z.real) or not math.isfinite(z.imag):
        raise ValueError("value must be finite")
    answer = 0.0j
    for coefficient in reversed(coefficients):
        answer = answer * z + coefficient
    return answer


def target_full_prefactor_residue(
    order: int, log_scale: float, height: float, target_offset: complex
) -> complex:
    """Target residue before adding the central Taylor polynomial."""

    _require_order(order)
    _require_log_scale(log_scale)
    z0 = _require_nonzero_finite_complex(target_offset, "target_offset")
    return (
        cmath.exp(log_scale * z0)
        * bettin_gonek_prefactor(z0, height)
        / z0 ** (order - 1)
    )


def central_full_prefactor_residue(
    order: int, log_scale: float, height: float, target_offset: complex
) -> complex:
    """Complete residue at ``w=1`` for the retained rational prefactor."""

    _require_order(order)
    _require_log_scale(log_scale)
    z0 = _require_nonzero_finite_complex(target_offset, "target_offset")
    if order == 1:
        return 0.0j
    coefficients = completed_factor_taylor_coefficients(
        log_scale, height, order - 2
    )
    return -sum(
        coefficients[j] / z0 ** (order - 1 - j)
        for j in range(order - 1)
    )


def completed_full_prefactor_residue(
    order: int, log_scale: float, height: float, target_offset: complex
) -> complex:
    """Target plus central residue."""

    return target_full_prefactor_residue(
        order, log_scale, height, target_offset
    ) + central_full_prefactor_residue(
        order, log_scale, height, target_offset
    )


def full_prefactor_taylor_remainder(
    order: int, log_scale: float, height: float, target_offset: complex
) -> complex:
    """Equivalent exact Taylor-remainder expression."""

    _require_order(order)
    _require_log_scale(log_scale)
    z0 = _require_nonzero_finite_complex(target_offset, "target_offset")
    full_value = cmath.exp(log_scale * z0) * bettin_gonek_prefactor(z0, height)
    if order == 1:
        truncated = 0.0j
    else:
        coefficients = completed_factor_taylor_coefficients(
            log_scale, height, order - 2
        )
        truncated = evaluate_taylor(coefficients, z0)
    return (full_value - truncated) / z0 ** (order - 1)


def full_prefactor_ledger(
    order: int, log_scale: float, height: float, target_offset: complex
) -> FullPrefactorResidueLedger:
    """Build the exact complete rational-prefactor residue ledger."""

    target = target_full_prefactor_residue(
        order, log_scale, height, target_offset
    )
    central = central_full_prefactor_residue(
        order, log_scale, height, target_offset
    )
    completed = target + central
    return FullPrefactorResidueLedger(
        order=order,
        log_scale=log_scale,
        height=height,
        target_offset=complex(target_offset),
        target_residue=target,
        central_residue=central,
        completed_residue=completed,
        completed_over_target=completed / target,
    )
