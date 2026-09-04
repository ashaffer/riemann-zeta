#!/usr/bin/env python3
"""Exact finite replays for the S1-B1 completed-source commutator audit.

The routines here check algebra and support bookkeeping only.  They do not
estimate the R71 energy, prove a zero-free strip, or prove RH.
"""

from __future__ import annotations

from dataclasses import dataclass
import cmath
import math
from typing import Callable, Sequence

import numpy as np


def mobius_values(limit: int) -> np.ndarray:
    """Return ``mu(0), ..., mu(limit)`` as exact integers."""

    if limit < 1:
        raise ValueError("limit must be positive")
    values = np.ones(limit + 1, dtype=np.int64)
    values[0] = 0
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for prime in range(2, limit + 1):
        if not is_prime[prime]:
            continue
        values[prime::prime] *= -1
        square = prime * prime
        if square <= limit:
            values[square::square] = 0
        if prime <= limit // 2:
            is_prime[2 * prime::prime] = False
    return values


def weighted_mobius_values(limit: int) -> np.ndarray:
    """Return the R128 coefficients ``C(n) = -mu(n) log(n)``."""

    mu = mobius_values(limit)
    values = np.zeros(limit + 1, dtype=float)
    indices = np.arange(1, limit + 1, dtype=float)
    values[1:] = -mu[1:] * np.log(indices)
    return values


def divisor_convolution_matrix(coefficients: Sequence[complex]) -> np.ndarray:
    """Lower-triangular matrix for Dirichlet convolution by ``coefficients``.

    Coordinates are indexed by the positive integers ``1, ..., N``.  Thus
    ``matrix[n-1, d-1] = coefficients[n/d]`` when ``d`` divides ``n``.
    """

    limit = len(coefficients) - 1
    if limit < 1:
        raise ValueError("coefficient vector must include a positive index")
    matrix = np.zeros((limit, limit), dtype=np.complex128)
    for n in range(1, limit + 1):
        for divisor in range(1, n + 1):
            if n % divisor == 0:
                matrix[n - 1, divisor - 1] = coefficients[n // divisor]
    return matrix


def window_commutator(
    weights: Sequence[complex], operator: np.ndarray
) -> np.ndarray:
    """Return ``M_w T - T M_w`` for one finite divisor section."""

    weight = np.asarray(weights, dtype=np.complex128)
    if operator.shape != (weight.size, weight.size):
        raise ValueError("weight/operator dimension mismatch")
    multiplication = np.diag(weight)
    return multiplication @ operator - operator @ multiplication


@dataclass(frozen=True)
class NarrowShellReplay:
    """Norm ledger for a hard shell with output truncated at its upper edge."""

    source_norm: float
    commutator_norm: float
    inner_weight_residual_norm: float
    exterior_leakage_norm: float


def narrow_shell_replay(
    *, limit: int, shell_start: int, shell_end: int
) -> NarrowShellReplay:
    """Replay the exact narrow-shell collapse of the literal S1-B1 seed.

    If ``2 * shell_start > shell_end``, the compressed inner-weight term is
    zero because the only possible cofactor is one and ``C(1)=0``.  Any
    nonzero second term lies outside the output cutoff.
    """

    if not (1 <= shell_start <= shell_end <= limit):
        raise ValueError("invalid shell")
    coefficients = weighted_mobius_values(limit)
    convolution = divisor_convolution_matrix(coefficients)
    weights = np.zeros(limit, dtype=float)
    weights[shell_start - 1 : shell_end] = 1.0
    output = np.zeros(limit, dtype=float)
    output[:shell_end] = 1.0
    ones = np.ones(limit, dtype=float)

    source = weights * (convolution @ ones)
    inner_weight = convolution @ weights
    commutator = window_commutator(weights, convolution) @ ones
    compressed_residual = output * inner_weight
    compressed_commutator = output * commutator
    exterior = (1.0 - output) * inner_weight
    return NarrowShellReplay(
        source_norm=float(np.linalg.norm(source)),
        commutator_norm=float(np.linalg.norm(compressed_commutator)),
        inner_weight_residual_norm=float(np.linalg.norm(compressed_residual)),
        exterior_leakage_norm=float(np.linalg.norm(exterior)),
    )


def reflect(values: Sequence[complex]) -> np.ndarray:
    """Finite involutive reflection used for exact operator replays."""

    return np.asarray(values, dtype=np.complex128)[::-1].copy()


def odd_projection(values: Sequence[complex]) -> np.ndarray:
    """Return ``(I-R) values / 2``."""

    value = np.asarray(values, dtype=np.complex128)
    return (value - reflect(value)) / 2.0


def reflection_multiplier_commutator(
    multiplier: Sequence[complex], values: Sequence[complex]
) -> np.ndarray:
    """Return ``[P_-, M_H] values`` on a finite reflected grid."""

    h = np.asarray(multiplier, dtype=np.complex128)
    value = np.asarray(values, dtype=np.complex128)
    if h.shape != value.shape:
        raise ValueError("multiplier/value dimension mismatch")
    return odd_projection(h * value) - h * odd_projection(value)


def reflection_multiplier_closed_form(
    multiplier: Sequence[complex], values: Sequence[complex]
) -> np.ndarray:
    """Closed form ``(H-RH) R(values) / 2`` for the same commutator."""

    h = np.asarray(multiplier, dtype=np.complex128)
    value = np.asarray(values, dtype=np.complex128)
    if h.shape != value.shape:
        raise ValueError("multiplier/value dimension mismatch")
    return (h - reflect(h)) * reflect(value) / 2.0


def q_h_multiplier(step: float, z: complex) -> complex:
    """The R102 Mellin multiplier ``(exp(h z)-exp(h/2))^2``."""

    return (cmath.exp(step * z) - math.exp(step / 2.0)) ** 2


def q_h_reflection_difference(step: float, z: complex) -> complex:
    """Factored value of ``q_h(z)-q_h(-z)``."""

    return 4.0 * cmath.sinh(step * z) * (
        cmath.cosh(step * z) - math.exp(step / 2.0)
    )


def completed_archimedean_log_derivative(
    s: complex, digamma: Callable[[complex], complex]
) -> complex:
    """Return ``C_zeta'/C_zeta`` at ``s`` using a supplied digamma."""

    return (
        1.0 / s
        + 1.0 / (s - 1.0)
        - 0.5 * math.log(math.pi)
        + 0.5 * digamma(s / 2.0)
    )


def two_commutator_closed_form(
    first: Sequence[complex], second: Sequence[complex], values: Sequence[complex]
) -> np.ndarray:
    """Return the scalar form of two iterated reflection commutators.

    With ``C_H=[P_-,M_H]``, exact crossed-product algebra gives
    ``C_G C_H f = -(G-RG)(H-RH)f/4``.
    """

    g = np.asarray(first, dtype=np.complex128)
    h = np.asarray(second, dtype=np.complex128)
    value = np.asarray(values, dtype=np.complex128)
    if g.shape != h.shape or h.shape != value.shape:
        raise ValueError("dimension mismatch")
    return -(g - reflect(g)) * (h - reflect(h)) * value / 4.0

