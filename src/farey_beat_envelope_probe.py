#!/usr/bin/env python3
"""Independent-coefficient Farey-beat envelope diagnostic.

Let ``Q=floor(sqrt(Y))`` and let ``F_Q`` be the reduced Farey fractions in
``[0,1]``.  This probe uses the nonzero quadratic beat frequencies

    nu = Y (f-g),                  f,g in F_Q, f>g,

to approximate a constant or Gaussian envelope on the rescaled shell
``x=(t-Y)/Y in [0,1]``.  It computes either a discretized minimum-l1 uniform
approximation or a minimum-l2 quadrature approximation.

The coefficients of distinct beats are independent here.  In the completed
Ramanujan square they need not factor through one shared denominator vector,
and the continuous Poisson/Wright amplitude is absent.  Consequently this is
a D-rated mechanism diagnostic, not a zero-free-region computation.  Its
purpose is to answer the preliminary approximation-and-coefficient-norm gate.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Callable

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import linprog
from scipy.sparse import csc_matrix, hstack, vstack


Envelope = Callable[[np.ndarray], np.ndarray]


@dataclass(frozen=True)
class FareyBeat:
    """One unique positive Farey difference and a representative pair."""

    difference: Fraction
    left: Fraction
    right: Fraction
    multiplicity: int
    scaled_frequency: float


@dataclass(frozen=True)
class EnvelopeApproximation:
    """One finite beat-envelope approximation."""

    active_scale: int
    farey_order: int
    bandlimit: float
    target_name: str
    objective: str
    requested_error: float
    training_error: float
    holdout_rms_error: float
    holdout_max_error: float
    coefficient_l1: float
    coefficient_l2: float
    support_size: int
    beats: tuple[FareyBeat, ...] = field(repr=False, compare=False)
    coefficients: np.ndarray = field(repr=False, compare=False)


def constant_envelope(points: np.ndarray) -> np.ndarray:
    """Return the constant contact envelope."""

    return np.ones_like(np.asarray(points, dtype=float))


def gaussian_envelope(points: np.ndarray) -> np.ndarray:
    """Return the smooth positive shell surrogate used in the audit."""

    values = np.asarray(points, dtype=float)
    return np.exp(-0.5 * ((values - 0.5) / 0.22) ** 2)


def _envelope(name: str) -> Envelope:
    if name == "constant":
        return constant_envelope
    if name == "gaussian":
        return gaussian_envelope
    raise ValueError("target_name must be 'constant' or 'gaussian'")


def reduced_farey_fractions(order: int) -> tuple[Fraction, ...]:
    """Return all reduced fractions in ``[0,1]`` of denominator at most Q."""

    if order < 2:
        raise ValueError("Farey order must be at least two")
    values = {
        Fraction(numerator, denominator)
        for denominator in range(1, order + 1)
        for numerator in range(denominator + 1)
        if math.gcd(numerator, denominator) == 1
    }
    return tuple(sorted(values))


def farey_beats(active_scale: int, bandlimit: float = 16.0) -> tuple[FareyBeat, ...]:
    """Return unique positive beats with ``Y(f-g) <= bandlimit``."""

    if active_scale < 4:
        raise ValueError("active_scale must be at least four")
    if not math.isfinite(bandlimit) or bandlimit <= 0.0:
        raise ValueError("bandlimit must be finite and positive")
    order = math.isqrt(active_scale)
    fractions = reduced_farey_fractions(order)
    representatives: dict[Fraction, tuple[Fraction, Fraction]] = {}
    multiplicities: dict[Fraction, int] = {}
    for index, left in enumerate(fractions):
        for right in fractions[:index]:
            difference = left - right
            if float(active_scale * difference) > bandlimit:
                continue
            representatives.setdefault(difference, (left, right))
            multiplicities[difference] = multiplicities.get(difference, 0) + 1
    return tuple(
        FareyBeat(
            difference=difference,
            left=representatives[difference][0],
            right=representatives[difference][1],
            multiplicity=multiplicities[difference],
            scaled_frequency=float(active_scale * difference),
        )
        for difference in sorted(representatives)
    )


def _design(points: np.ndarray, beats: tuple[FareyBeat, ...]) -> np.ndarray:
    frequencies = np.asarray([beat.scaled_frequency for beat in beats])
    return np.cos(
        2.0 * math.pi * (np.asarray(points)[:, None] - 0.5) * frequencies[None, :]
    )


def minimum_l1_uniform_approximation(
    active_scale: int,
    *,
    bandlimit: float = 16.0,
    error_constant: float = 15.0,
    target_name: str = "constant",
    initial_grid_size: int = 129,
    holdout_grid_size: int = 4097,
    max_iterations: int = 8,
) -> EnvelopeApproximation:
    """Solve an adaptive discretized minimum-l1 uniform approximation."""

    if error_constant <= 0.0 or not math.isfinite(error_constant):
        raise ValueError("error_constant must be finite and positive")
    if initial_grid_size < 17 or holdout_grid_size < initial_grid_size:
        raise ValueError("the training and holdout grids are too small")
    target = _envelope(target_name)
    beats = farey_beats(active_scale, bandlimit)
    if not beats:
        raise ValueError("the selected beat band is empty")
    tolerance = error_constant / active_scale
    grid = list(np.linspace(0.0, 1.0, initial_grid_size))
    holdout = np.linspace(0.0, 1.0, holdout_grid_size)
    holdout_target = target(holdout)
    coefficients = np.zeros(len(beats))
    training_error = math.inf

    for _ in range(max_iterations):
        points = np.asarray(sorted(set(grid)))
        design = _design(points, beats)
        sparse_design = csc_matrix(design)
        signed = hstack((sparse_design, -sparse_design), format="csc")
        constraints = vstack((signed, -signed), format="csc")
        values = target(points)
        upper_bounds = np.concatenate((values + tolerance, -values + tolerance))
        result = linprog(
            np.ones(2 * len(beats)),
            A_ub=constraints,
            b_ub=upper_bounds,
            bounds=(0.0, None),
            method="highs",
        )
        if not result.success:
            raise RuntimeError(f"minimum-l1 beat solve failed: {result.message}")
        coefficients = result.x[: len(beats)] - result.x[len(beats) :]
        training_error = float(np.max(np.abs(design @ coefficients - values)))
        holdout_error = _design(holdout, beats) @ coefficients - holdout_target
        absolute_error = np.abs(holdout_error)
        if float(np.max(absolute_error)) <= 1.001 * tolerance:
            break

        # Constraint generation adds local error extrema rather than making
        # the LP dense on the entire validation grid.
        local = np.where(
            (absolute_error[1:-1] >= absolute_error[:-2])
            & (absolute_error[1:-1] >= absolute_error[2:])
            & (absolute_error[1:-1] > 1.0001 * tolerance)
        )[0] + 1
        candidates = np.concatenate(
            (np.asarray([0]), local, np.asarray([len(holdout) - 1]))
        )
        candidates = candidates[absolute_error[candidates] > 1.0001 * tolerance]
        strongest = candidates[
            np.argsort(-absolute_error[candidates])[:128]
        ]
        grid.extend(holdout[strongest].tolist())
    else:
        raise RuntimeError("adaptive minimum-l1 solve did not validate")

    holdout_error = _design(holdout, beats) @ coefficients - holdout_target
    return EnvelopeApproximation(
        active_scale=active_scale,
        farey_order=math.isqrt(active_scale),
        bandlimit=bandlimit,
        target_name=target_name,
        objective="l1-uniform",
        requested_error=tolerance,
        training_error=training_error,
        holdout_rms_error=float(
            math.sqrt(np.trapz(np.abs(holdout_error) ** 2, holdout))
        ),
        holdout_max_error=float(np.max(np.abs(holdout_error))),
        coefficient_l1=float(np.sum(np.abs(coefficients))),
        coefficient_l2=float(np.linalg.norm(coefficients)),
        support_size=int(np.sum(np.abs(coefficients) > 1.0e-8)),
        beats=beats,
        coefficients=coefficients,
    )


def minimum_l2_rms_approximation(
    active_scale: int,
    *,
    bandlimit: float = 16.0,
    error_constant: float = 1.0,
    target_name: str = "constant",
    quadrature_order: int = 240,
    holdout_grid_size: int = 4097,
) -> EnvelopeApproximation:
    """Return the minimum-l2 coefficients at a requested quadrature RMS error."""

    if error_constant <= 0.0 or not math.isfinite(error_constant):
        raise ValueError("error_constant must be finite and positive")
    target = _envelope(target_name)
    beats = farey_beats(active_scale, bandlimit)
    nodes, weights = leggauss(quadrature_order)
    points = (nodes + 1.0) / 2.0
    square_root_weights = np.sqrt(weights / 2.0)
    weighted_design = _design(points, beats) * square_root_weights[:, None]
    weighted_target = target(points) * square_root_weights
    gram = weighted_design @ weighted_design.T
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    eigenvalues = np.maximum(eigenvalues, 0.0)
    coordinates = eigenvectors.T @ weighted_target
    tolerance = error_constant / active_scale
    largest = max(1.0, float(eigenvalues[-1]))

    def residual(log_penalty: float) -> float:
        penalty = math.exp(log_penalty)
        return float(
            np.linalg.norm(penalty * coordinates / (eigenvalues + penalty))
        )

    lower = math.log(largest) - 45.0
    upper = math.log(largest) + 20.0
    if residual(lower) > tolerance:
        raise RuntimeError("requested RMS error is below the numerical resolution")
    for _ in range(100):
        middle = (lower + upper) / 2.0
        if residual(middle) < tolerance:
            lower = middle
        else:
            upper = middle
    penalty = math.exp((lower + upper) / 2.0)
    dual = eigenvectors @ (coordinates / (eigenvalues + penalty))
    coefficients = weighted_design.T @ dual
    training_error = residual(math.log(penalty))

    holdout = np.linspace(0.0, 1.0, holdout_grid_size)
    holdout_error = _design(holdout, beats) @ coefficients - target(holdout)
    return EnvelopeApproximation(
        active_scale=active_scale,
        farey_order=math.isqrt(active_scale),
        bandlimit=bandlimit,
        target_name=target_name,
        objective="l2-rms",
        requested_error=tolerance,
        training_error=training_error,
        holdout_rms_error=float(
            math.sqrt(np.trapz(np.abs(holdout_error) ** 2, holdout))
        ),
        holdout_max_error=float(np.max(np.abs(holdout_error))),
        coefficient_l1=float(np.sum(np.abs(coefficients))),
        coefficient_l2=float(np.linalg.norm(coefficients)),
        support_size=int(np.sum(np.abs(coefficients) > 1.0e-8)),
        beats=beats,
        coefficients=coefficients,
    )


def l1_spectral_gap_lower_bound(
    active_scale: int,
    farey_order: int,
    uniform_error: float,
) -> float:
    """Return the elementary mean-value lower bound for constant approximation."""

    if active_scale < 1 or farey_order < 1:
        raise ValueError("scale and order must be positive")
    if not 0.0 <= uniform_error < 1.0:
        raise ValueError("uniform_error must lie in [0,1)")
    return math.pi * (1.0 - uniform_error) * active_scale / farey_order**2


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=int, default=256)
    parser.add_argument("--bandlimit", type=float, default=16.0)
    parser.add_argument("--error-constant", type=float, default=15.0)
    parser.add_argument("--target", choices=("constant", "gaussian"), default="constant")
    parser.add_argument("--objective", choices=("l1", "l2"), default="l1")
    args = parser.parse_args()

    if args.objective == "l1":
        result = minimum_l1_uniform_approximation(
            args.scale,
            bandlimit=args.bandlimit,
            error_constant=args.error_constant,
            target_name=args.target,
        )
    else:
        result = minimum_l2_rms_approximation(
            args.scale,
            bandlimit=args.bandlimit,
            error_constant=args.error_constant,
            target_name=args.target,
        )
    print(f"farey_order={result.farey_order}")
    print(f"beat_count={len(result.beats)}")
    print(f"requested_error={result.requested_error:.12g}")
    print(f"holdout_rms_error={result.holdout_rms_error:.12g}")
    print(f"holdout_max_error={result.holdout_max_error:.12g}")
    print(f"coefficient_l1={result.coefficient_l1:.12g}")
    print(f"coefficient_l2={result.coefficient_l2:.12g}")
    print(f"support_size={result.support_size}")


if __name__ == "__main__":
    main()
