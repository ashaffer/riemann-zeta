"""Exact rank ledger for the KMT-to-positive-square cluster proposal.

This module does *not* model the actual prime logarithms.  It checks the
finite-dimensional inequalities used in the companion report:

* a mixture of squares whose tails have support at most ``L`` has carrier
  coefficient l1 norm at most ``sqrt(L*s*d)``;
* stable normalization and ``R`` carrier coefficients of normalized size
  ``epsilon`` therefore force a macroscopic block;
* applying an entrywise scalar characteristic-function bound ``eta`` to the
  nonlinear tail covariance pays ``2*eta*(L-1)*d/Z``.

The last item is a black-box estimate, not a lower bound for the actual
covariance.  Its purpose is to show exactly why scalar KMT cannot certify the
simultaneous square repair.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np


@dataclass(frozen=True)
class MixtureLedger:
    carrier_l1: float
    baseline_energy: float
    tail_energy: float
    diagonal_energy: float
    maximum_tail_support: int
    cauchy_upper: float


def mixture_ledger(
    baselines: Sequence[complex], tails: Sequence[Sequence[complex]]
) -> MixtureLedger:
    """Return the exact energies and the block-Cauchy carrier bound.

    Row ``alpha`` represents

    ``|x_alpha + sum_i y_alpha_i exp(-i t_i u)|^2``.

    Zero tail entries are ignored when computing the maximum support.
    """

    x = np.asarray(baselines, dtype=complex)
    y = np.asarray(tails, dtype=complex)
    if y.ndim != 2 or x.ndim != 1 or y.shape[0] != x.size:
        raise ValueError("tails must be a matrix with one row per baseline")
    support = int(np.max(np.count_nonzero(y, axis=1), initial=0))
    s = float(np.vdot(x, x).real)
    d = float(np.vdot(y.ravel(), y.ravel()).real)
    carrier = np.conjugate(x) @ y
    carrier_l1 = float(np.sum(np.abs(carrier)))
    upper = math.sqrt(max(0.0, support * s * d))
    return MixtureLedger(carrier_l1, s, d, s + d, support, upper)


def forced_block_size(
    packet_count: int,
    epsilon: float,
    *,
    linear_fraction: float = 1.0,
    normalization_ratio: float = 1.0,
) -> float:
    """Lower bound on block support in a stable linear-lift architecture.

    The assumptions are ``|b_i| >= linear_fraction*epsilon*Z`` and
    ``s+d <= normalization_ratio*Z``.  The returned real lower bound is

    ``(2*linear_fraction*R*epsilon/normalization_ratio)^2``.
    """

    if packet_count < 1 or epsilon <= 0.0:
        raise ValueError("packet_count and epsilon must be positive")
    if linear_fraction <= 0.0 or normalization_ratio <= 0.0:
        raise ValueError("fractions must be positive")
    return (
        2.0 * linear_fraction * packet_count * epsilon / normalization_ratio
    ) ** 2


def forced_tail_energy_fraction(
    packet_count: int,
    epsilon: float,
    block_size: int,
    *,
    linear_fraction: float = 1.0,
    normalization_ratio: float = 1.0,
) -> float:
    """Lower bound for ``d/Z`` from block Cauchy and stable normalization."""

    if block_size < 1:
        raise ValueError("block_size must be positive")
    numerator = (linear_fraction * packet_count * epsilon) ** 2
    return numerator / (block_size * normalization_ratio)


def termwise_covariance_certificate(
    eta: float, block_size: int, tail_energy_fraction: float
) -> float:
    """Scalar-KMT upper-bound value for the nonlinear covariance remainder.

    Diagonal tail pairs cancel in ``Phi_h(t)-Phi(t)``.  Each remaining
    covariance bracket has modulus at most ``2*eta`` when its translated
    frequency and the target are in the KMT band.  Cauchy gives
    ``sum_{i != j}|a_i a_j| <= (L-1)||a||_2^2``.
    """

    if eta < 0.0 or block_size < 1 or tail_energy_fraction < 0.0:
        raise ValueError("invalid covariance-certificate parameters")
    return 2.0 * eta * (block_size - 1) * tail_energy_fraction


def local_positive_radius(shell_width: float, cosine_floor: float = 0.5) -> float:
    """Radius on which ``cos(delta*u)>=cosine_floor`` for ``|u|<=w``."""

    if shell_width <= 0.0 or not 0.0 < cosine_floor < 1.0:
        raise ValueError("invalid shell width or cosine floor")
    return math.acos(cosine_floor) / shell_width


def maximum_separated_points(interval_length: float, separation: float = 1.0) -> int:
    """Maximum number of separation-``separation`` points in an interval."""

    if interval_length < 0.0 or separation <= 0.0:
        raise ValueError("invalid interval length or separation")
    return int(math.floor(interval_length / separation)) + 1


def fixed_sum_sign_moments(side: int, depth: int = 2) -> tuple[int, float, float]:
    """Moments of the exchangeable fixed-sum sign obstruction.

    There are ``R=side^2`` signs and every row has sum ``-depth*side``.
    The returned tuple is ``(R, E X_i, E X_i X_j)`` for ``i != j``.
    Parity and range are checked so that such rows exist.
    """

    if side < 2 or depth < 1 or depth > side:
        raise ValueError("invalid side or depth")
    r = side * side
    total = -depth * side
    if (r + total) % 2:
        raise ValueError("fixed sign sum has the wrong parity")
    mean = total / r
    off_diagonal = (total * total - r) / (r * (r - 1))
    return r, mean, off_diagonal


def asymptotic_ledger(log_y: float, c: float = 0.019) -> dict[str, float]:
    """Evaluate the exponent ledger without constructing the enormous ``Y``."""

    if log_y <= 0.0 or c <= 0.0:
        raise ValueError("log_y and c must be positive")
    epsilon = math.exp(-c * log_y)
    eta = log_y ** -0.3
    r = math.exp(2.0 * c * log_y)
    return {
        "epsilon": epsilon,
        "eta": eta,
        "packet_count": r,
        "eta_times_rank": eta * r,
        "eta_over_epsilon": eta / epsilon,
        "critical_block_lower": 4.0 * r,
    }

