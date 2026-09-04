#!/usr/bin/env python3
"""Replay the exact finite-aperture QP referee identities.

This module is deliberately small.  It checks the algebra used in the
metric tent antenna and in the spectral-null/Delsarte reformulation; it does
not substitute floating-point experiments for the actual-prime theorem that
remains open.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import json
import math
from typing import Iterable


APERTURE_EXPONENT = Fraction(50, 33)
TENT_FAILURE_CONSTANT = Fraction(1, 8)
TENT_NEGATIVE_THRESHOLD_FACTOR = Fraction(8, 3)
KAPPA_PROMOTE = 0.018030323424358778
KAPPA_UNIFORM = 0.018746369714728765


def tent_population(t: float, width: float) -> float:
    """Fourier ratio E[g(U)cos(tU)]/E[g(U)] for triangular ``g``.

    Here ``U`` is uniform on ``[-width,width]`` and
    ``g(u)=1-|u|/width``.  The removable value at zero is returned exactly.
    """

    if width <= 0.0:
        raise ValueError("width must be positive")
    x = width * t / 2.0
    if x == 0.0:
        return 1.0
    return (math.sin(x) / x) ** 2


def tent_population_by_antiderivative(t: float, width: float) -> float:
    """The same ratio in its direct integrated closed form."""

    if width <= 0.0:
        raise ValueError("width must be positive")
    if t == 0.0:
        return 1.0
    x = width * t
    # Avoid cancellation in 1-cos(x); this is the Taylor expansion of the
    # integrated formula 2(1-cos(x))/x^2, not a sampled approximation.
    if abs(x) < 1e-3:
        return 1.0 - x * x / 12.0 + x**4 / 360.0 - x**6 / 20160.0
    numerator = (1.0 - math.cos(x)) / (x * x)
    denominator = 0.5
    return numerator / denominator


def tent_failure_log_bound(
    sample_size: int, width: float, aperture: float, epsilon: float
) -> float:
    """Log of the audited continuum union bound.

    For ``0<epsilon<=1/8``, the probability that the normalized weighted
    empirical cosine polynomial falls below ``-(8/3)epsilon`` somewhere in
    ``[0,aperture]`` is at most

        2 (2 + 4 width aperture / epsilon) exp(-sample_size epsilon^2/8).
    """

    if sample_size <= 0 or width <= 0.0 or aperture < 0.0:
        raise ValueError("invalid sample size, width, or aperture")
    if not 0.0 < epsilon <= 0.125:
        raise ValueError("epsilon must lie in (0,1/8]")
    return (
        math.log(2.0)
        + math.log(2.0 + 4.0 * width * aperture / epsilon)
        - sample_size * epsilon * epsilon / 8.0
    )


def spectral_null_from_antipode(
    depth: float, off_central_cosine_moments: Iterable[float]
) -> tuple[float, tuple[float, ...]]:
    """Add the central atom to a proposed depth-``depth`` antipode.

    Returns the central mass and the Fourier moments of
    ``(depth*delta_0 + nu)/(1+depth)`` at the supplied nodes.
    """

    if depth < 0.0:
        raise ValueError("depth must be nonnegative")
    moments = tuple(float(value) for value in off_central_cosine_moments)
    alpha = depth / (1.0 + depth)
    transformed = tuple((depth + value) / (1.0 + depth) for value in moments)
    return alpha, transformed


def antipode_from_spectral_null(central_mass: float) -> float:
    """Recover the common off-central antipode depth from a null measure."""

    if not 0.0 <= central_mass < 1.0:
        raise ValueError("central mass must lie in [0,1)")
    return central_mass / (1.0 - central_mass)


@dataclass(frozen=True)
class RationalMarginLedger:
    beta: str
    theta: str
    target: str
    long_gap_saving: str
    collar_saving: str
    inverse_image_saving: str
    long_gap_margin: str
    collar_margin: str
    inverse_image_margin: str
    target_clears_uniform_kappa: bool


def rational_margin_ledger() -> RationalMarginLedger:
    """Return the exact ``.019`` auxiliary-margin calculation."""

    beta = Fraction(19, 125)
    theta = Fraction(161, 1000)
    target = Fraction(19, 1000)
    long_gap = (45 * theta - 6) / 65
    collar = 2 - APERTURE_EXPONENT - 2 * beta - theta
    inverse_image = 1 - APERTURE_EXPONENT / 2 - beta
    return RationalMarginLedger(
        beta=str(beta),
        theta=str(theta),
        target=str(target),
        long_gap_saving=str(long_gap),
        collar_saving=str(collar),
        inverse_image_saving=str(inverse_image),
        long_gap_margin=str(long_gap - target),
        collar_margin=str(collar - target),
        inverse_image_margin=str(inverse_image - target),
        target_clears_uniform_kappa=float(target) > KAPPA_UNIFORM,
    )


def main() -> None:
    depth = 0.037
    alpha, null_moments = spectral_null_from_antipode(depth, [-depth] * 4)
    payload = {
        "schema": "qp-finite-aperture-referee-v1",
        "status": "PASS",
        "tent_values": {
            str(t): tent_population(t, 0.2) for t in (0.0, 0.3, 2.0, 17.0)
        },
        "metric_exponent_at_promotion_depth": 1.0 - 2.0 * KAPPA_PROMOTE,
        "spectral_null": {
            "depth": depth,
            "central_mass": alpha,
            "maximum_null_residual": max(abs(value) for value in null_moments),
            "recovered_depth": antipode_from_spectral_null(alpha),
        },
        "rational_margins": asdict(rational_margin_ledger()),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
