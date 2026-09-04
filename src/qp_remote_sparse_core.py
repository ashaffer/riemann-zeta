#!/usr/bin/env python3
"""Sparse-core and persistence lemmas for positive remote AP antipodes.

These are deterministic consequences of a positive antipode.  They do not
prove that the actual prime-log flow enters, or avoids, a positive chamber
before the legal QP aperture.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import numpy as np


def negative_peak_weight(depth: float) -> float:
    """Weight forced onto scalar correlations at most ``-depth/2``."""
    if not 0.0 < depth <= 1.0:
        raise ValueError("depth must lie in (0,1]")
    return depth / (2.0 - depth)


def lattice_points_per_radius_one_packet(step: float) -> int:
    """Maximum points of ``step*Z`` in a closed interval of length two."""
    if step <= 0.0:
        raise ValueError("step must be positive")
    return math.floor(2.0 / step) + 1


@dataclass(frozen=True)
class SparseCoreBound:
    depth: float
    packet_count: int
    step: float
    forced_weight: float
    exceptional_harmonic_count: int
    largest_weight_lower: float


def sparse_core_bound(depth: float, packet_count: int, step: float) -> SparseCoreBound:
    """Combine one-point polarity with a fixed-width exceptional cover."""
    if packet_count <= 0:
        raise ValueError("packet_count must be positive")
    forced = negative_peak_weight(depth)
    exceptional_count = packet_count * lattice_points_per_radius_one_packet(step)
    return SparseCoreBound(
        depth=depth,
        packet_count=packet_count,
        step=step,
        forced_weight=forced,
        exceptional_harmonic_count=exceptional_count,
        largest_weight_lower=forced / exceptional_count,
    )


@dataclass(frozen=True)
class SignPersistenceCertificate:
    size: int
    top_harmonic: int
    cost: float
    depth: float
    minimum_negative_coefficient: float
    inverse_infinity_norm: float
    phase_radius: float
    perturbed_cost_upper: float
    perturbed_depth_lower: float


def sign_persistence_certificate(
    phases: np.ndarray, harmonics: np.ndarray
) -> SignPersistenceCertificate:
    """Certify a sup-norm phase box retaining all negative Cramer signs.

    Let ``A[j,k]=cos(harmonics[k]*phases[j])`` and ``c=A^-1*1``.  If every
    ``c_k<0``, then ``-1/sum(c)`` is the positive-antipode depth.  For a
    phase perturbation of sup norm ``rho``, the entrywise Lipschitz bound and
    a Neumann-series argument preserve invertibility and all signs whenever

        rho <= min(1/(2 beta M K), m/(4 beta K C)),

    where ``beta=||A^-1||_infinity``, ``K=max harmonics``,
    ``m=min(-c_k)``, and ``C=sum |c_k|``.
    """
    theta = np.asarray(phases, dtype=float)
    indices = np.asarray(harmonics, dtype=int)
    if theta.ndim != 1 or indices.shape != theta.shape or len(theta) == 0:
        raise ValueError("phases and harmonics must be nonempty vectors of equal size")
    if np.any(indices <= 0) or len(np.unique(indices)) != len(indices):
        raise ValueError("harmonics must be distinct positive integers")
    matrix = np.cos(np.outer(theta, indices))
    inverse = np.linalg.inv(matrix)
    coefficients = inverse @ np.ones(len(theta))
    if np.max(coefficients) >= 0.0:
        raise ValueError("the supplied phase point is not in a strict positive chamber")
    size = len(theta)
    top = int(np.max(indices))
    cost = float(np.sum(-coefficients))
    margin = float(np.min(-coefficients))
    beta = float(np.linalg.norm(inverse, ord=np.inf))
    radius = min(
        1.0 / (2.0 * beta * size * top),
        margin / (4.0 * beta * top * cost),
    )
    # The coefficient perturbation is at most margin/2 by construction.
    cost_upper = cost + size * margin / 2.0
    return SignPersistenceCertificate(
        size=size,
        top_harmonic=top,
        cost=cost,
        depth=1.0 / cost,
        minimum_negative_coefficient=margin,
        inverse_infinity_norm=beta,
        phase_radius=radius,
        perturbed_cost_upper=cost_upper,
        perturbed_depth_lower=1.0 / cost_upper,
    )


def phase_box_haar_log_volume(radius: float, dimension: int) -> float:
    """Log Haar volume of a product box of phase radius ``radius``."""
    if not 0.0 < radius <= math.pi or dimension <= 0:
        raise ValueError("radius must be in (0,pi] and dimension positive")
    return dimension * math.log(radius / math.pi)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--depth", type=float, default=0.1)
    parser.add_argument("--packets", type=int, default=100)
    parser.add_argument("--step", type=float, default=1.0)
    args = parser.parse_args()
    print(
        json.dumps(
            {
                "verdict": (
                    "a positive AP has a sparse negative-peak core, but this "
                    "does not exclude a deterministic exceptional step"
                ),
                "sparse_core": asdict(
                    sparse_core_bound(args.depth, args.packets, args.step)
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
