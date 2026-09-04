"""Exact exponent and reweighting ledgers for the actual-prime QP gate.

This module does *not* estimate the actual-prime Delsarte value.  It records
the algebra behind three sharply scoped conclusions:

* a fixed-power natural prime-twist modulus estimate over the full QP band
  meets Turan's localization criterion and therefore proves a fixed strip;
* scalar KMT-sized bounds cannot control a packet source of rank
  ``Y ** (2*c)`` through an entrywise/Gram argument;
* a positive square reweighting pays its exact effective-rank factor when a
  scalar characteristic-function estimate is applied term by term.

The mathematical proofs and the quantifier audit are in the companion report
``results/ZETA23-QP-ACTUAL-PRIME-MULTIPLICATIVE-EXPLICIT-FORMULA-GATE-2026-08-14.md``.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Mapping

import numpy as np


QP_APERTURE_EXPONENT = 50.0 / 33.0
QP_LOWER_HEIGHT_EXPONENT = 0.01
TURAN_SAFE_LOWER_HEIGHT_EXPONENT = 0.5
QP_FIXED_SLICE_C = 0.019


@dataclass(frozen=True)
class TuranBandLedger:
    """Exponent checks needed to insert the QP band into Turan's criterion."""

    beta: float
    beta_sixth_root: float
    length_exponent: float
    upper_height_exponent_at_shortest_length: float
    lower_height_exponent_at_longest_length: float
    saving_exponent_at_shortest_length: float
    strip_width: float

    @property
    def admissible(self) -> bool:
        return (
            self.upper_height_exponent_at_shortest_length > 1.0
            and self.lower_height_exponent_at_longest_length < 1.0
            and self.saving_exponent_at_shortest_length > self.beta
        )


def turan_band_ledger(
    beta: float,
    *,
    power_saving: float = QP_FIXED_SLICE_C,
    aperture_exponent: float = QP_APERTURE_EXPONENT,
    lower_height_exponent: float = TURAN_SAFE_LOWER_HEIGHT_EXPONENT,
    aperture_slack: float = 1.0e-3,
) -> TuranBandLedger:
    """Return a quantitative specialization of Turan's localization window.

    Turan uses prime lengths between

    ``T ** (D*(1-beta**(1/6)))`` and
    ``T ** (D*(1+beta**(1/6)))``.

    We choose ``D`` so that the shortest such length has QP top aperture
    ``T ** (1+aperture_slack)``.  By default the lower edge is the safe
    half-power sub-band, which is contained in the complete QP band and avoids
    the elementary sharp-cutoff pole term at height ``N**0.01``.  The returned
    fields check both band inclusions and the power in Turan's inequality.
    """

    if not 0.0 < beta < 1.0:
        raise ValueError("beta must lie in (0, 1)")
    if power_saving <= 0.0:
        raise ValueError("power_saving must be positive")
    if aperture_exponent <= 0.0:
        raise ValueError("aperture_exponent must be positive")
    if not 0.0 <= lower_height_exponent < aperture_exponent:
        raise ValueError("invalid lower-height exponent")
    if aperture_slack <= 0.0:
        raise ValueError("aperture_slack must be positive")

    root = beta ** (1.0 / 6.0)
    length_exponent = (1.0 + aperture_slack) / (
        aperture_exponent * (1.0 - root)
    )
    upper_min = aperture_exponent * length_exponent * (1.0 - root)
    lower_max = lower_height_exponent * length_exponent * (1.0 + root)
    saving_min = power_saving * length_exponent * (1.0 - root)
    return TuranBandLedger(
        beta=beta,
        beta_sixth_root=root,
        length_exponent=length_exponent,
        upper_height_exponent_at_shortest_length=upper_min,
        lower_height_exponent_at_longest_length=lower_max,
        saving_exponent_at_shortest_length=saving_min,
        strip_width=beta * beta,
    )


def limiting_turan_strip_width(
    power_saving: float = QP_FIXED_SLICE_C,
    aperture_exponent: float = QP_APERTURE_EXPONENT,
) -> float:
    """The width approached by the top-aperture Turan specialization.

    This is a conservative explicit consequence, not an optimization over
    every placement of Turan's prime lengths inside the complete QP band.
    """

    if power_saving <= 0.0 or aperture_exponent <= 0.0:
        raise ValueError("exponents must be positive")
    return (power_saving / aperture_exponent) ** 2


def carrier_leverage_upper(
    packet_count: int, scalar_mean_bound: float, gram_lower_bound: float
) -> float:
    """Best carrier-leverage bound from scalar means plus ``H >= gamma I``.

    If ``m_i = E b_i``, ``|m_i| <= delta``, and the unprojected packet Gram
    satisfies ``H >= gamma I``, then

    ``m.T @ inv(H) @ m <= R * delta**2 / gamma``.
    """

    if packet_count < 1:
        raise ValueError("packet_count must be positive")
    if scalar_mean_bound < 0.0:
        raise ValueError("scalar_mean_bound must be nonnegative")
    if gram_lower_bound <= 0.0:
        raise ValueError("gram_lower_bound must be positive")
    return packet_count * scalar_mean_bound**2 / gram_lower_bound


def kmt_rank_tax(y: float, c: float = QP_FIXED_SLICE_C) -> float:
    """Return ``sqrt(Y**(2c)) / log(Y)**0.3``.

    This is the dimensionless source tax ``delta_KMT * sqrt(R)`` at the
    large-value packet count ``R=Y**(2c)``.  It tends to infinity for every
    fixed positive ``c``.
    """

    if y <= 1.0:
        raise ValueError("y must exceed one")
    if c <= 0.0:
        raise ValueError("c must be positive")
    return y**c / math.log(y) ** 0.3


def effective_rank(coefficients: Iterable[complex]) -> float:
    """Return ``||c||_1^2 / ||c||_2^2`` for a nonzero coefficient vector."""

    c = np.asarray(list(coefficients), dtype=np.complex128)
    if c.ndim != 1 or c.size == 0:
        raise ValueError("coefficients must be a nonempty vector")
    l2_sq = float(np.vdot(c, c).real)
    if l2_sq == 0.0:
        raise ValueError("coefficients must be nonzero")
    return float(np.sum(np.abs(c)) ** 2 / l2_sq)


def square_reweight_termwise_bound(
    scalar_bound: float, coefficients: Iterable[complex]
) -> float:
    """Termwise characteristic-function bound after a positive square tilt.

    Suppose every nonzero frequency in the numerator and normalization obeys
    ``|Phi(v)| <= delta``.  For ``h=|sum c_s exp(i s u)|^2`` put
    ``K=||c||_1^2/||c||_2^2``.  If ``delta*(K-1)<1``, then the triangle
    inequality gives

    ``|Phi_h(t)| <= delta*K / (1-delta*(K-1))``.

    The function raises if the same scalar information does not even keep the
    normalization away from zero.
    """

    if not 0.0 <= scalar_bound < 1.0:
        raise ValueError("scalar_bound must lie in [0, 1)")
    rank = effective_rank(coefficients)
    denominator = 1.0 - scalar_bound * (rank - 1.0)
    if denominator <= 0.0:
        raise ValueError("termwise bounds do not control the normalization")
    return scalar_bound * rank / denominator


def direct_square_reweighted_characteristic(
    nodes: Iterable[float],
    probabilities: Iterable[float],
    shifts: Iterable[float],
    coefficients: Iterable[complex],
    query: float,
) -> complex:
    """Evaluate a finite positive square reweight directly on the node side."""

    u = np.asarray(list(nodes), dtype=float)
    p = np.asarray(list(probabilities), dtype=float)
    s = np.asarray(list(shifts), dtype=float)
    c = np.asarray(list(coefficients), dtype=np.complex128)
    if u.ndim != 1 or p.shape != u.shape or s.shape != c.shape:
        raise ValueError("incompatible one-dimensional inputs")
    if np.any(p < 0.0) or not np.isclose(np.sum(p), 1.0):
        raise ValueError("probabilities must be a probability vector")
    carrier = np.exp(1j * np.outer(u, s)) @ c
    weights = p * np.abs(carrier) ** 2
    normalization = float(np.sum(weights))
    if normalization <= 0.0:
        raise ValueError("the square tilt has zero normalization")
    return complex(np.sum(weights * np.exp(1j * query * u)) / normalization)


def expanded_square_reweighted_characteristic(
    nodes: Iterable[float],
    probabilities: Iterable[float],
    shifts: Iterable[float],
    coefficients: Iterable[complex],
    query: float,
) -> complex:
    """Evaluate the exact difference-frequency expansion of the square tilt."""

    u = np.asarray(list(nodes), dtype=float)
    p = np.asarray(list(probabilities), dtype=float)
    s = np.asarray(list(shifts), dtype=float)
    c = np.asarray(list(coefficients), dtype=np.complex128)
    if u.ndim != 1 or p.shape != u.shape or s.shape != c.shape:
        raise ValueError("incompatible one-dimensional inputs")
    if np.any(p < 0.0) or not np.isclose(np.sum(p), 1.0):
        raise ValueError("probabilities must be a probability vector")

    def phi(frequency: float) -> complex:
        return complex(np.sum(p * np.exp(1j * frequency * u)))

    numerator = 0.0j
    denominator = 0.0j
    for r, shift_r in enumerate(s):
        for q, shift_q in enumerate(s):
            coefficient = c[r] * np.conjugate(c[q])
            difference = shift_r - shift_q
            numerator += coefficient * phi(query + difference)
            denominator += coefficient * phi(difference)
    if abs(denominator) == 0.0:
        raise ValueError("the square tilt has zero normalization")
    return numerator / denominator


def selberg_square_weight_on_prime(
    prime: int, level: int, coefficients: Mapping[int, complex]
) -> float:
    """Evaluate ``|sum_{d|p,d<=D} lambda_d|^2`` at a prime ``p``."""

    if prime < 2 or any(prime % d == 0 for d in range(2, int(math.sqrt(prime)) + 1)):
        raise ValueError("prime must be prime")
    if level < 1:
        raise ValueError("level must be positive")
    total = 0.0j
    for divisor, coefficient in coefficients.items():
        if divisor < 1:
            raise ValueError("divisors must be positive")
        if divisor <= level and prime % divisor == 0:
            total += coefficient
    return float(abs(total) ** 2)


def negative_zero_pole_residue(beta: float, multiplicity: int = 1) -> float:
    """Residue of the one-sided Mellin transform at a matching zeta zero.

    For ``A_t(x)=sum_{n<=x} Lambda(n) cos(t log n)``, the Dirichlet series is
    ``-1/2*(zeta'/zeta(s-it)+zeta'/zeta(s+it))``.  A zero of multiplicity
    ``m`` at ``beta+it`` and its conjugate give residue ``-m``; after the
    partial-summation factor ``1/s`` the Mellin transform has residue
    ``-m/beta``.
    """

    if beta <= 0.0:
        raise ValueError("beta must be positive")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    return -float(multiplicity) / beta
