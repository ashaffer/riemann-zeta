"""Exact exponent ledger for the Gibbs halfspace obstruction to QP repair.

The companion report constructs a probability measure on ``T^R`` by
conditioning Haar measure on

    sum_i cos(theta_i) <= -sqrt(R).

Every positive reweighting remains in this halfspace, although all fixed
Fourier characters are small.  This module only replays the finite algebra
and the limiting truncated-Gaussian formulas.  It does not model the actual
prime-log orbit and it does not prove or disprove QP.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


def target_epsilon(packet_count: int) -> float:
    """The target ``epsilon=1/(2 sqrt(R))`` used by the obstruction."""

    if packet_count < 1:
        raise ValueError("packet_count must be positive")
    return 0.5 / math.sqrt(packet_count)


def forced_bad_moment(packet_count: int) -> float:
    """Upper bound for at least one moment after every positive reweighting.

    If ``sum_i X_i <= -sqrt(R)`` pointwise, averaging after an arbitrary
    positive reweighting shows ``min_i E_h X_i <= -1/sqrt(R)``.
    """

    if packet_count < 1:
        raise ValueError("packet_count must be positive")
    return -1.0 / math.sqrt(packet_count)


def fixed_degree_fourier_scale(packet_count: int, degree: int) -> float:
    """Return the theorem's ``R^(-degree/2)`` Fourier scale.

    The hidden constant depends on the fixed multi-index.  The function
    records only the power of ``R`` used in the analytic ledger.
    """

    if packet_count < 1 or degree < 1:
        raise ValueError("packet_count and degree must be positive")
    return packet_count ** (-0.5 * degree)


@dataclass(frozen=True)
class ShiftedSquareLedger:
    packet_count: int
    degree_one_count: int
    degree_three_count: int
    degree_one_contribution: float
    degree_three_contribution: float
    total_bound: float


def shifted_square_ledger(
    packet_count: int,
    *,
    degree_one_constant: float = 1.0,
    degree_three_constant: float = 1.0,
) -> ShiftedSquareLedger:
    """Bound ``sum_(i,j)|Phi(e_k+e_i-e_j)|^2`` in the torus model.

    Permutation symmetry leaves ``2R-1`` degree-one terms and
    ``(R-1)^2`` degree-three terms.  The fixed-degree theorem bounds these
    by ``C_1 R^-1/2`` and ``C_3 R^-3/2``, respectively.  Hence the complete
    square sum is ``O(1)``, stronger than the ``O(R)`` middle term allowed
    by the scalar Heath--Brown ledger.
    """

    if packet_count < 1:
        raise ValueError("packet_count must be positive")
    if degree_one_constant < 0.0 or degree_three_constant < 0.0:
        raise ValueError("Fourier constants must be nonnegative")
    r = packet_count
    n1 = 2 * r - 1
    n3 = (r - 1) ** 2
    b1 = n1 * degree_one_constant**2 / r
    b3 = n3 * degree_three_constant**2 / r**3
    return ShiftedSquareLedger(r, n1, n3, b1, b3, b1 + b3)


def _normal_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def _normal_cdf(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def limiting_common_tilt_mean(lambda_value: float) -> float:
    """Mean of the limiting conditioned Gaussian after a common Gibbs tilt.

    ``Z`` is ``N(0,1/2)`` conditioned on ``Z<=-1``.  Weighting by
    ``exp(lambda*Z)`` shifts the unconditioned Gaussian mean to ``lambda/2``.
    The returned conditional mean is strictly below ``-1`` for every finite
    nonnegative ``lambda``.
    """

    if lambda_value < 0.0:
        raise ValueError("lambda_value must be nonnegative")
    sigma = 1.0 / math.sqrt(2.0)
    shifted_mean = 0.5 * lambda_value
    alpha = (-1.0 - shifted_mean) / sigma
    cdf = _normal_cdf(alpha)
    if cdf == 0.0:
        raise OverflowError("lambda_value is too large for float evaluation")
    return shifted_mean - sigma * _normal_pdf(alpha) / cdf


def limiting_common_tilt_normalization(lambda_value: float) -> float:
    """Limiting normalized partition function for the common Gibbs tilt."""

    if lambda_value < 0.0:
        raise ValueError("lambda_value must be nonnegative")
    alpha = -math.sqrt(2.0) - lambda_value / math.sqrt(2.0)
    denominator = _normal_cdf(-math.sqrt(2.0))
    return math.exp(lambda_value * lambda_value / 4.0) * _normal_cdf(alpha) / denominator


def qp_scaling(log_y: float, c: float = 0.019) -> dict[str, float]:
    """Replay the fixed-power scaling without constructing an enormous Y."""

    if log_y <= 0.0 or c <= 0.0:
        raise ValueError("log_y and c must be positive")
    epsilon = math.exp(-c * log_y)
    packet_count = 0.25 * math.exp(2.0 * c * log_y)
    return {
        "epsilon": epsilon,
        "packet_count": packet_count,
        "fourier_scale": 2.0 * epsilon,
        "forced_bad_moment": -2.0 * epsilon,
        "packet_exponent": 2.0 * c,
    }
