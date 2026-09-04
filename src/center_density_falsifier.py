"""Finite synthetic falsifiers for the center-density research direction.

These fixtures use real pseudo-nodes, not logarithms of actual primes.  They
therefore falsify only geometry/density/partition-of-unity proof classes.

Two effects are isolated:

* a small density modulation produces a large unweighted source Fourier
  coefficient, while Voronoi cell weights compensate it;
* snapping the same modulated nodes to an odd half-grid creates a Bragg peak
  for every recentering, regardless of the positive nodal weights.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np


def modulated_quantile_nodes(
    count: int,
    *,
    width: float,
    frequency: float,
    modulation: float,
    bisection_steps: int = 64,
) -> np.ndarray:
    """Quantiles of ``1-modulation*cos(frequency*u)`` on ``[-width,width]``."""

    if count < 2 or width <= 0 or frequency <= 0:
        raise ValueError("invalid count, width, or frequency")
    if not 0 < modulation < 1:
        raise ValueError("modulation must lie strictly between zero and one")

    left = -float(width)
    right = float(width)
    normalizer = (
        2 * width
        - modulation
        * (math.sin(frequency * width) - math.sin(-frequency * width))
        / frequency
    )

    def cdf(values: np.ndarray) -> np.ndarray:
        return (
            values
            + width
            - modulation
            * (
                np.sin(frequency * values)
                - math.sin(-frequency * width)
            )
            / frequency
        ) / normalizer

    targets = (np.arange(count, dtype=float) + 0.5) / count
    lower = np.full(count, left)
    upper = np.full(count, right)
    for _ in range(bisection_steps):
        middle = (lower + upper) / 2
        below = cdf(middle) < targets
        lower = np.where(below, middle, lower)
        upper = np.where(below, upper, middle)
    return (lower + upper) / 2


def voronoi_weights(
    nodes: np.ndarray,
    *,
    left: float,
    right: float,
) -> np.ndarray:
    """Normalized nearest-node cell lengths on a bounded interval."""

    nodes = np.asarray(nodes, dtype=float)
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError("nodes must be a one-dimensional nontrivial array")
    if not left < nodes[0] < nodes[-1] < right:
        raise ValueError("nodes must lie strictly inside the interval")
    if not np.all(np.diff(nodes) > 0):
        raise ValueError("nodes must be strictly increasing")

    boundaries = np.empty(len(nodes) + 1)
    boundaries[0] = left
    boundaries[-1] = right
    boundaries[1:-1] = (nodes[:-1] + nodes[1:]) / 2
    weights = np.diff(boundaries)
    return weights / np.sum(weights)


def odd_half_grid_snap(nodes: np.ndarray, frequency: float) -> np.ndarray:
    """Snap nodes to ``frequency*x = pi (mod 2*pi)``."""

    nodes = np.asarray(nodes, dtype=float)
    if nodes.ndim != 1 or frequency <= 0:
        raise ValueError("invalid nodes or frequency")
    indices = np.rint((frequency * nodes / math.pi - 1) / 2)
    snapped = (2 * indices + 1) * math.pi / frequency
    if not np.all(np.diff(snapped) > 0):
        raise ValueError("frequency is too small for an injective snap")
    return snapped


def fourier_value(
    nodes: np.ndarray,
    weights: np.ndarray,
    frequency: float,
) -> complex:
    """Return the normalized weighted Fourier value."""

    nodes = np.asarray(nodes, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if nodes.shape != weights.shape:
        raise ValueError("nodes and weights must have matching shapes")
    return complex(np.sum(weights * np.exp(1j * frequency * nodes)))


@dataclass(frozen=True)
class FalsifierMetrics:
    """Metrics for the deterministic finite pseudo-node fixture."""

    unweighted_source_real: float
    voronoi_source_real: float
    bragg_modulus: float
    maximum_gap: float
    snap_displacement: float


def deterministic_fixture(
    *,
    count: int = 4000,
    width: float = 0.2,
    source_periods: int = 20,
    modulation: float = 0.2,
    bragg_frequency: float = 10_000_000.0,
) -> FalsifierMetrics:
    """Build a modulated-density source and an odd-half-grid Bragg peak."""

    source_frequency = source_periods * math.pi / width
    nodes = modulated_quantile_nodes(
        count,
        width=width,
        frequency=source_frequency,
        modulation=modulation,
    )
    snapped = odd_half_grid_snap(nodes, bragg_frequency)
    uniform = np.full(count, 1 / count)
    snapped_weights = voronoi_weights(snapped, left=-width, right=width)
    # All three readings now use the same snapped node system.  The snap is
    # much finer than the source wavelength, so it preserves the density
    # modulation while imposing exact coherence at the Bragg frequency.
    unweighted_source = fourier_value(snapped, uniform, source_frequency)
    voronoi_source = fourier_value(
        snapped,
        snapped_weights,
        source_frequency,
    )
    bragg = fourier_value(snapped, snapped_weights, bragg_frequency)

    return FalsifierMetrics(
        unweighted_source_real=unweighted_source.real,
        voronoi_source_real=voronoi_source.real,
        bragg_modulus=abs(bragg),
        maximum_gap=float(np.max(np.diff(snapped))),
        snap_displacement=float(np.max(np.abs(snapped - nodes))),
    )
