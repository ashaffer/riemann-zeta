"""Finite algebra for the QP radialization normalization gate.

The companion report proves that the probability-normalized directional
depth is saturated by an isolated actual prime and defines the corrected
Turan normalization.  This module replays only the elementary identities;
it does not prove corrected radialization, QP, or a zero-free strip.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


PROJECT_WIDTH = 1.0 / 5.0
CENTER_FACTOR = 2.0 * math.exp(PROJECT_WIDTH)


@dataclass(frozen=True)
class SingletonCertificate:
    prime: int
    center: float
    node: float
    height: float
    cosine: float
    probability_depth: float


def singleton_certificate(prime: int, offset: float = 0.5) -> SingletonCertificate:
    """Construct the exact isolated-prime depth-one certificate."""

    if prime < 2:
        raise ValueError("prime must be at least two")
    if offset <= 0.0:
        raise ValueError("offset must be positive")
    center = prime + offset
    node = math.log(center / prime)
    height = math.pi / node
    cosine = math.cos(height * math.log(prime / center))
    return SingletonCertificate(
        prime=prime,
        center=center,
        node=node,
        height=height,
        cosine=cosine,
        probability_depth=-cosine,
    )


def singleton_height_bounds(prime: int, offset: float = 0.5) -> tuple[float, float]:
    """Return bounds from ``x/(1+x)<=log(1+x)<=x``."""

    if prime < 2:
        raise ValueError("prime must be at least two")
    if offset <= 0.0:
        raise ValueError("offset must be positive")
    return math.pi * prime / offset, math.pi * (prime + offset) / offset


def mass_normalized_depth(
    probability_depth: float, prime_count: int, reference_scale: float
) -> float:
    """Apply the exact conversion ``E=(M/N)D``."""

    if not -1.0 <= probability_depth <= 1.0:
        raise ValueError("probability_depth must lie in [-1,1]")
    if prime_count < 1 or reference_scale <= 0.0:
        raise ValueError("prime_count and reference_scale must be positive")
    return prime_count * probability_depth / reference_scale


def phase_localization_constant(partition_count: int) -> float:
    """Return the exact ``4 J_w/3`` constant in the corrected comparison."""

    if partition_count < 1:
        raise ValueError("partition_count must be positive")
    return 4.0 * partition_count / 3.0


def radial_pairing_value(prime_count: int, reference_scale: float, depth: float) -> float:
    """Return ``(M/N)r`` from exact pairing with a radial measure."""

    if prime_count < 1 or reference_scale <= 0.0 or depth < 0.0:
        raise ValueError("inputs must be nonnegative with positive count and scale")
    return prime_count * depth / reference_scale


def minimum_prime_count_for_event(reference_scale: float, event_depth: float) -> int:
    """Return the necessary count ``ceil(N*E)`` for a mass-normalized event."""

    if reference_scale <= 0.0 or not 0.0 <= event_depth <= 1.0:
        raise ValueError("scale must be positive and event_depth must lie in [0,1]")
    return math.ceil(reference_scale * event_depth)


def probability_depth_from_mass_event(
    event_depth: float, prime_count: int, reference_scale: float
) -> float:
    """Invert ``E=(M/N)D`` to return ``D=N*E/M``."""

    if event_depth < 0.0 or prime_count < 1 or reference_scale <= 0.0:
        raise ValueError("inputs must be nonnegative with positive count and scale")
    return reference_scale * event_depth / prime_count


def radial_depth_from_transverse_return(
    directional_depth: float, transverse_return: float
) -> float:
    """Return the exact mixed depth ``D*s/(1+s)`` from Proposition 5.2."""

    if directional_depth < 0.0 or transverse_return < 0.0:
        raise ValueError("depths must be nonnegative")
    return directional_depth * transverse_return / (1.0 + transverse_return)


def required_transverse_return(directional_depth: float, radial_target: float) -> float:
    """Solve ``D*s/(1+s)>=r`` for the least ``s``.

    The target must be strictly smaller than the available directional depth.
    """

    if directional_depth <= 0.0 or radial_target < 0.0:
        raise ValueError("directional_depth must be positive and target nonnegative")
    if radial_target >= directional_depth:
        raise ValueError("radial_target must be smaller than directional_depth")
    return radial_target / (directional_depth - radial_target)


def canonical_positive_return_ledger(
    center: float,
    band_length: float,
    prime_count: int,
    *,
    hilbert_constant: float = 1.0,
    mean_constant: float = 1.0,
) -> dict[str, float]:
    """Replay the quantitative ledger in Proposition 5.3.

    Constants encode the fixed-width separation and reciprocal-node bounds.
    A positive returned lower bound certifies the algebraic comparison; the
    analytic inequalities supplying the constants are proved in the report.
    """

    if center <= 1.0 or band_length <= 0.0 or prime_count < 1:
        raise ValueError("center, band_length, and prime_count must be positive")
    if hilbert_constant < 0.0 or mean_constant < 0.0:
        raise ValueError("constants must be nonnegative")
    second_moment = (1.0 - hilbert_constant * center / band_length) / (
        2.0 * prime_count
    )
    mean_error = (
        mean_constant * center * math.log(center) / (band_length * prime_count)
    )
    positive_return = 0.5 * (second_moment - mean_error)
    return {
        "second_moment_lower": second_moment,
        "mean_error": mean_error,
        "positive_return_lower": positive_return,
    }
