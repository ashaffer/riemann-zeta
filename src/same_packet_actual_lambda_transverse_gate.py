#!/usr/bin/env python3
"""Exact finite algebra for the actual-Lambda transverse reserve gate.

This module does not insert a scan point into the zeta divisor.  It checks
the arithmetic-side identities which are valid before a candidate is assumed
to be a zero, and the exponent ledger used by the conditional isolation
theorem after an *actual* candidate zero is assumed in a contradiction.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from scipy.linalg import null_space

from high_height_carrier_slice import shift_overlap_sign


@dataclass(frozen=True)
class TransverseData:
    carrier_rayleigh: float
    schur_residual: float
    transverse_lambda_min: float
    transverse_lambda_max: float
    transverse_dimension: int


def _hermitian(matrix: np.ndarray) -> np.ndarray:
    matrix = np.asarray(matrix, dtype=complex)
    return (matrix + matrix.conj().T) / 2.0


def transverse_data(reserve: np.ndarray, carrier_direction: np.ndarray) -> TransverseData:
    """Return the exact carrier/complement invariants of a Hermitian matrix."""
    reserve = _hermitian(reserve)
    e = np.asarray(carrier_direction, dtype=complex)
    e = e / np.linalg.norm(e)
    transverse = null_space(e.conj()[None, :], rcond=1e-12)
    if transverse.shape[1] == 0:
        raise ValueError("the carrier has no transverse complement")
    compression = _hermitian(transverse.conj().T @ reserve @ transverse)
    eigenvalues = np.linalg.eigvalsh(compression)
    schur = transverse.conj().T @ reserve @ e
    return TransverseData(
        carrier_rayleigh=float(np.vdot(e, reserve @ e).real),
        schur_residual=float(np.linalg.norm(schur)),
        transverse_lambda_min=float(eigenvalues[0]),
        transverse_lambda_max=float(eigenvalues[-1]),
        transverse_dimension=int(transverse.shape[1]),
    )


def actual_lambda_cross_coefficient(
    tau: np.ndarray,
    length: float,
    logs: np.ndarray,
    weights: np.ndarray,
    inclusion: np.ndarray,
    e: np.ndarray,
    v: np.ndarray,
    background_raw: np.ndarray,
) -> complex:
    """Evaluate ``<e,R v>`` from the exact finite actual-Lambda sum.

    ``weights`` are Lambda(n)/sqrt(n), ``background_raw`` is the pole plus
    archimedean raw matrix, and ``inclusion`` embeds the selected quotient.
    The rank-one selected carrier is absent because callers impose ``e^*v=0``.
    """
    tau = np.asarray(tau, dtype=float)
    logs = np.asarray(logs, dtype=float)
    weights = np.asarray(weights, dtype=float)
    inclusion = np.asarray(inclusion, dtype=complex)
    e = np.asarray(e, dtype=complex)
    v = np.asarray(v, dtype=complex)
    if abs(np.vdot(e, v)) > 1e-9 * np.linalg.norm(e) * np.linalg.norm(v):
        raise ValueError("v must be transverse to e")
    compressed_background = inclusion.conj().T @ background_raw @ inclusion
    answer = np.vdot(e, compressed_background @ v) / (length * length)
    for log_n, weight in zip(logs, weights):
        shifted = inclusion.conj().T @ shift_overlap_sign(
            tau, length, float(log_n)
        ) @ inclusion
        answer -= (
            2.0 * float(weight) * np.vdot(e, shifted @ v) / (length * length)
        )
    return complex(answer)


def actual_lambda_schur_vector(
    tau: np.ndarray,
    length: float,
    logs: np.ndarray,
    weights: np.ndarray,
    inclusion: np.ndarray,
    e: np.ndarray,
    background_raw: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return coordinates of ``P_W R e`` and its vector summands in a basis of W."""
    tau = np.asarray(tau, dtype=float)
    inclusion = np.asarray(inclusion, dtype=complex)
    e = np.asarray(e, dtype=complex)
    e = e / np.linalg.norm(e)
    transverse = null_space(e.conj()[None, :], rcond=1e-12)
    background = (
        transverse.conj().T
        @ inclusion.conj().T
        @ background_raw
        @ inclusion
        @ e
        / (length * length)
    )
    prime_columns: list[np.ndarray] = []
    total = background.copy()
    for log_n, weight in zip(np.asarray(logs), np.asarray(weights)):
        column = (
            transverse.conj().T
            @ inclusion.conj().T
            @ shift_overlap_sign(tau, length, float(log_n))
            @ inclusion
            @ e
        )
        scaled = -2.0 * float(weight) * column / (length * length)
        prime_columns.append(scaled)
        total += scaled
    columns = (
        np.column_stack(prime_columns)
        if prime_columns
        else np.empty((transverse.shape[1], 0), dtype=complex)
    )
    return total, background, columns


def gram_energy(background: np.ndarray, columns: np.ndarray) -> float:
    """Expand the Schur norm as the full signed two-prime Gram sum."""
    background = np.asarray(background, dtype=complex)
    columns = np.asarray(columns, dtype=complex)
    gram = columns.conj().T @ columns
    linear = columns.conj().T @ background
    return float(
        np.vdot(background, background).real
        + 2.0 * np.sum(linear).real
        + np.sum(gram).real
    )


def isolation_log_ratio(
    log_x: float,
    carrier_exponent: float,
    remainder_exponent: float,
    log_power: float = 0.0,
) -> float:
    """Log of ``X^remainder L^A / (X^carrier/L)``.

    A value tending to minus infinity is exactly the shallow-isolation
    condition used to make every transverse invariant ``o(K)``.
    """
    if log_x <= 1.0:
        raise ValueError("log_x must exceed one")
    return (
        (remainder_exponent - carrier_exponent) * log_x
        + (log_power + 1.0) * math.log(log_x)
    )


def two_channel_best(
    eta: float, r: float, c: float, z: complex
) -> tuple[float, float]:
    """Best reserve and phase for ``sqrt(eta)e+e^(iphi)sqrt(1-eta)v``."""
    if not 0.0 < eta < 1.0:
        raise ValueError("eta must lie in (0,1)")
    phase = -math.atan2(z.imag, z.real) if abs(z) else 0.0
    value = (
        eta * r
        + (1.0 - eta) * c
        + 2.0 * math.sqrt(eta * (1.0 - eta)) * abs(z)
    )
    return float(value), float(phase)
