#!/usr/bin/env python3
"""Finite checks for the actual-prime positive-weight QP barrier.

The associated theorem card separates three issues which are easy to mix up.

* A half-period log lattice defeats *every* positive reweighting at one legal
  height while having prime-density cardinality and much better gap geometry
  than the primes.  It is a proof-class countermodel, not a prime model.
* Exact positive quadrature through degree ``n`` needs at least ``n + 1``
  nodes.  Consequently exact-quadrature transfer cannot reach the QP aperture.
* A signed projected-Gram packet correction need not remain in the probability
  simplex.  Positive correction is a convex-hull problem, not merely a rank
  problem.

The asymptotic proofs are in the report.  This module replays the finite
identities and the exact rational exponent ledger.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import argparse
import json
import math
from typing import Iterable, Sequence

import numpy as np


APERTURE_EXPONENT = Fraction(50, 33)
RECALIBRATED_DENOMINATOR_EXPONENT = Fraction(19, 125)
FIXED_SLICE_KILL_EXPONENT = Fraction(19, 1000)


@dataclass(frozen=True)
class HalfGridLedger:
    aperture_exponent: str
    denominator_exponent: str
    first_deleted_mass_exponent: str
    component_padding_exponent: str
    fixed_slice_kill_exponent: str


def half_grid_ledger() -> HalfGridLedger:
    """Return the exact exponents in the half-grid retention calculation."""

    a = APERTURE_EXPONENT
    beta = RECALIBRATED_DENOMINATOR_EXPONENT
    first = beta + a / 2 - 1
    padding = a - 2 + 2 * beta
    return HalfGridLedger(
        aperture_exponent=str(a),
        denominator_exponent=str(beta),
        first_deleted_mass_exponent=str(first),
        component_padding_exponent=str(padding),
        fixed_slice_kill_exponent=str(FIXED_SLICE_KILL_EXPONENT),
    )


def half_period_log_grid(
    y: float, width: float = 0.2, *, spacing_multiplier: int | None = None
) -> tuple[np.ndarray, float, int]:
    """Construct a positive half-period grid in ``(0,width)``.

    Every returned node has the form ``(2 k + 1) pi / B`` with the indices in
    one congruence class modulo ``spacing_multiplier``.  Therefore its cosine
    at ``B=Y^(50/33)`` is exactly ``-1`` in exact arithmetic.  The automatic
    multiplier makes the log spacing comparable with ``log(Y)/Y``.
    """

    if not y > math.e or not width > 0.0:
        raise ValueError("need Y>e and a positive width")
    aperture = y ** float(APERTURE_EXPONENT)
    if spacing_multiplier is None:
        spacing_multiplier = max(
            1, math.ceil(aperture * math.log(y) / (2.0 * math.pi * y))
        )
    if spacing_multiplier < 1:
        raise ValueError("spacing_multiplier must be positive")

    # Odd indices 2k+1 in a fixed class modulo 2L preserve the half-period.
    first_k = 0
    nodes: list[float] = []
    k = first_k
    while True:
        node = (2 * k + 1) * math.pi / aperture
        if node >= width:
            break
        nodes.append(node)
        k += spacing_multiplier
    if not nodes:
        raise ValueError("the requested scale produced no grid nodes")
    return np.asarray(nodes, dtype=float), aperture, spacing_multiplier


def normalized_cosine(
    nodes: Sequence[float], weights: Sequence[float], height: float
) -> float:
    """Evaluate a normalized positive cosine antenna."""

    u = np.asarray(nodes, dtype=float)
    lam = np.asarray(weights, dtype=float)
    if u.ndim != 1 or lam.ndim != 1 or len(u) != len(lam) or len(u) == 0:
        raise ValueError("nodes and weights must be nonempty vectors of equal length")
    if np.min(lam) < 0.0:
        raise ValueError("weights must be nonnegative")
    mass = float(np.sum(lam))
    if not mass > 0.0:
        raise ValueError("weights must have positive mass")
    return float(np.dot(lam, np.cos(height * u)) / mass)


def worst_half_grid_perturbation_bound(phase_error: float) -> float:
    """Upper bound ``-cos(delta)`` for ``|delta|<=phase_error<=pi``."""

    if not 0.0 <= phase_error <= math.pi:
        raise ValueError("phase_error must lie in [0,pi]")
    return -math.cos(phase_error)


def exact_positive_quadrature_degree_cap(node_count: int) -> int:
    """Largest degree not excluded by the Toeplitz rank obstruction.

    Exactness for all circle modes ``|k|<=n`` makes the order-``n`` moment
    matrix the identity of rank ``n+1``.  An ``M``-atomic positive rule has
    moment-matrix rank at most ``M``.  Hence ``n<=M-1``.
    """

    if node_count < 1:
        raise ValueError("node_count must be positive")
    return node_count - 1


def packet_feature_hull(
    nodes: Sequence[float], packet_heights: Sequence[float]
) -> np.ndarray:
    """Return coordinate feature vectors for positive packet correction.

    Row ``j`` is ``(cos(t_i u_j))_i``.  Positive weights realize exactly the
    convex hull of these rows.
    """

    u = np.asarray(nodes, dtype=float)
    t = np.asarray(packet_heights, dtype=float)
    if u.ndim != 1 or t.ndim != 1 or len(u) == 0 or len(t) == 0:
        raise ValueError("nodes and packet heights must be nonempty vectors")
    return np.cos(np.outer(u, t))


def projected_single_packet_gram(feature: Iterable[float]) -> float:
    """Squared norm after removing the constant coordinate direction."""

    values = np.asarray(tuple(feature), dtype=float)
    if values.ndim != 1 or len(values) < 2:
        raise ValueError("feature must contain at least two coordinates")
    centered = values - float(np.mean(values))
    return float(np.dot(centered, centered))


def one_packet_positive_range(feature: Iterable[float]) -> tuple[float, float]:
    """Exact scalar convex hull available to positive packet weights."""

    values = tuple(float(x) for x in feature)
    if not values:
        raise ValueError("feature must be nonempty")
    return min(values), max(values)


def subset_bad_peak_probability_upper(sample_size: int, epsilon: float) -> float:
    """Hoeffding upper bound for repairing a fixed ``-2 epsilon`` mean peak.

    Sampling nodes independently from a base positive rule gives variables in
    ``[-1,1]``.  If their mean is at most ``-2 epsilon``, the probability that
    the sampled average rises above ``-epsilon`` is at most the returned value.
    """

    if sample_size < 1 or not 0.0 < epsilon <= 0.5:
        raise ValueError("invalid sample size or epsilon")
    return math.exp(-0.5 * sample_size * epsilon * epsilon)


def complex_characteristic(
    nodes: Sequence[float], weights: Sequence[float], height: float
) -> complex:
    """Characteristic function of a normalized positive node rule."""

    u = np.asarray(nodes, dtype=float)
    lam = np.asarray(weights, dtype=float)
    if u.ndim != 1 or lam.ndim != 1 or len(u) != len(lam) or len(u) == 0:
        raise ValueError("nodes and weights must be nonempty vectors of equal length")
    if np.min(lam) < 0.0:
        raise ValueError("weights must be nonnegative")
    mass = float(np.sum(lam))
    if not mass > 0.0:
        raise ValueError("weights must have positive mass")
    return complex(np.dot(lam, np.exp(1j * height * u)) / mass)


@dataclass(frozen=True)
class SquareReweightLedger:
    normalization: float
    diagonal_energy: float
    off_diagonal_normalization: complex
    coefficient_effective_count: float
    maximum_weight_inflation_bound: float


def square_reweight_ledger(
    nodes: Sequence[float],
    weights: Sequence[float],
    shifts: Sequence[float],
    coefficients: Sequence[complex],
) -> SquareReweightLedger:
    """Normalization and diffuseness ledger for ``h=|sum c_s e^(isu)|^2``."""

    u = np.asarray(nodes, dtype=float)
    lam = np.asarray(weights, dtype=float)
    shifts_array = np.asarray(shifts, dtype=float)
    coeff = np.asarray(coefficients, dtype=complex)
    if (
        u.ndim != 1
        or lam.ndim != 1
        or len(u) != len(lam)
        or shifts_array.ndim != 1
        or coeff.ndim != 1
        or len(shifts_array) != len(coeff)
        or len(u) == 0
        or len(coeff) == 0
    ):
        raise ValueError("invalid node, shift, weight, or coefficient vectors")
    if np.min(lam) < 0.0 or not float(np.sum(lam)) > 0.0:
        raise ValueError("base weights must be nonnegative with positive mass")
    lam = lam / float(np.sum(lam))
    values = np.exp(1j * np.outer(u, shifts_array)) @ coeff
    h = np.abs(values) ** 2
    normalization = float(np.dot(lam, h))
    energy = float(np.vdot(coeff, coeff).real)
    if not normalization > 0.0 or not energy > 0.0:
        raise ValueError("the square multiplier vanishes on the node support")
    effective = float(np.sum(np.abs(coeff)) ** 2 / energy)
    inflation = float(np.max(h) / normalization)
    return SquareReweightLedger(
        normalization=normalization,
        diagonal_energy=energy,
        off_diagonal_normalization=complex(normalization - energy),
        coefficient_effective_count=effective,
        maximum_weight_inflation_bound=inflation,
    )


def square_reweighted_characteristic_direct(
    nodes: Sequence[float],
    weights: Sequence[float],
    shifts: Sequence[float],
    coefficients: Sequence[complex],
    height: float,
) -> complex:
    """Directly evaluate the characteristic function after square reweighting."""

    u = np.asarray(nodes, dtype=float)
    lam = np.asarray(weights, dtype=float)
    shifts_array = np.asarray(shifts, dtype=float)
    coeff = np.asarray(coefficients, dtype=complex)
    lam = lam / float(np.sum(lam))
    c_values = np.exp(1j * np.outer(u, shifts_array)) @ coeff
    new_weights = lam * np.abs(c_values) ** 2
    return complex(
        np.dot(new_weights, np.exp(1j * height * u)) / float(np.sum(new_weights))
    )


def square_reweighted_characteristic_shifted(
    nodes: Sequence[float],
    weights: Sequence[float],
    shifts: Sequence[float],
    coefficients: Sequence[complex],
    height: float,
) -> complex:
    """Replay the exact difference-kernel formula for square reweighting."""

    shifts_tuple = tuple(float(s) for s in shifts)
    coeff = tuple(complex(c) for c in coefficients)
    if len(shifts_tuple) != len(coeff) or not coeff:
        raise ValueError("shifts and coefficients must have equal positive length")
    numerator = 0j
    denominator = 0j
    for s, cs in zip(shifts_tuple, coeff):
        for r, cr in zip(shifts_tuple, coeff):
            factor = cs * cr.conjugate()
            denominator += factor * complex_characteristic(nodes, weights, s - r)
            numerator += factor * complex_characteristic(
                nodes, weights, height + s - r
            )
    if abs(denominator) < 1e-14:
        raise ValueError("the square multiplier has zero normalization")
    return numerator / denominator


def square_reweight_covariance_residual(
    nodes: Sequence[float],
    weights: Sequence[float],
    shifts: Sequence[float],
    coefficients: Sequence[complex],
    height: float,
) -> complex:
    """Return the off-diagonal covariance that changes the base antenna.

    If ``E=sum|c_s|^2``, ``N=Z-E``, and ``R_t`` is the off-diagonal shifted
    numerator, this returns ``R_t-Phi(t)N``.  The reweighting changes ``Phi(t)``
    by exactly this residual divided by ``Z``.
    """

    shifts_tuple = tuple(float(s) for s in shifts)
    coeff = tuple(complex(c) for c in coefficients)
    phi_t = complex_characteristic(nodes, weights, height)
    answer = 0j
    for i, (s, cs) in enumerate(zip(shifts_tuple, coeff)):
        for j, (r, cr) in enumerate(zip(shifts_tuple, coeff)):
            if i == j:
                continue
            difference = s - r
            answer += cs * cr.conjugate() * (
                complex_characteristic(nodes, weights, height + difference)
                - phi_t * complex_characteristic(nodes, weights, difference)
            )
    return answer


def single_cosine_tilt_moment(mean: float, second_moment: float, delta: float) -> float:
    """Exact one-packet update under ``h=1+delta*cos(t0*u)``.

    Here ``mean=E[X]`` and ``second_moment=E[X^2]`` for
    ``X=cos(t0*u)``.  Nonnegativity holds for ``|delta|<=1``.
    """

    if not -1.0 <= mean <= 1.0 or not mean * mean <= second_moment <= 1.0:
        raise ValueError("invalid first or second moment")
    if not -1.0 <= delta <= 1.0:
        raise ValueError("delta must lie in [-1,1]")
    normalization = 1.0 + delta * mean
    if not normalization > 0.0:
        raise ValueError("the tilted rule has zero normalization")
    return (mean + delta * second_moment) / normalization


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Y", type=float, default=10_000.0)
    parser.add_argument("--width", type=float, default=0.2)
    args = parser.parse_args()

    nodes, aperture, multiplier = half_period_log_grid(args.Y, args.width)
    weights = np.arange(1.0, len(nodes) + 1.0)
    feature = (-1.0, -0.5)
    payload = {
        "schema": "zeta23.qp-actual-prime-weight-barrier.v1",
        "ledger": asdict(half_grid_ledger()),
        "half_grid": {
            "Y": args.Y,
            "width": args.width,
            "node_count": len(nodes),
            "spacing_multiplier": multiplier,
            "aperture": aperture,
            "max_log_gap": float(np.max(np.diff(nodes))) if len(nodes) > 1 else None,
            "arbitrary_positive_weight_cosine_at_aperture": normalized_cosine(
                nodes, weights, aperture
            ),
        },
        "positive_packet_counterexample": {
            "feature": feature,
            "projected_gram": projected_single_packet_gram(feature),
            "positive_range": one_packet_positive_range(feature),
            "target_zero_feasible": False,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
