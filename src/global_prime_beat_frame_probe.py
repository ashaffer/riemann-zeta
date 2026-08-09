#!/usr/bin/env python3
"""Global square-root-prime low-beat frame diagnostic.

For ``Q=floor(sqrt(H))``, take distinct primes ``p,r in [Q/2,Q]`` and
small positive determinants ``theta``.  CRT supplies primitive numerators
``a,b`` with

    a*r-b*p=theta,
    a/p-b/r=theta/(p*r).

The corresponding shell frequency is ``nu=H*theta/(p*r)``.  This module
tests whether the union over many prime pairs approximates the constant
contact envelope, and compares it with a single fixed pair.  It also records
matrix-unfolding ranks and nuclear/projective-norm proxies for the coefficient
tensor indexed by ``(p,r,theta)``.

All beat coefficients are independent.  No Ramanujan shared-coefficient
constraint, reciprocal Wright amplitude, prime weight, or completion identity
is imposed.  The calculations are therefore mechanism diagnostics, not an
estimate for the zeta function or a zero-free strip.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import linprog
from scipy.sparse import csc_matrix, hstack, vstack


@dataclass(frozen=True)
class PrimeBeat:
    """One positive determinant representative."""

    p_index: int
    r_index: int
    prime_p: int
    prime_r: int
    theta: int
    numerator_p: int
    numerator_r: int
    scaled_frequency: float


@dataclass(frozen=True)
class GlobalFrameDiagnostic:
    """Canonical minimum-l2 global frame and separation diagnostics."""

    active_scale: int
    theta_limit: int
    requested_rms_error: float
    quadrature_rms_error: float
    holdout_rms_error: float
    holdout_max_error: float
    coefficient_l1: float
    coefficient_l2: float
    frame_effective_rank: int
    frame_condition_number: float
    prime_unfold_rank: int
    prime_unfold_nuclear_norm: float
    theta_unfold_rank: int
    theta_unfold_nuclear_norm: float
    theta_slice_projective_proxy: float
    output_rank_at_tenfold_error: int
    best_fixed_pair_rms_error: float
    best_fixed_pair: tuple[int, int]
    primes: tuple[int, ...]
    beats: tuple[PrimeBeat, ...] = field(repr=False, compare=False)
    coefficients: np.ndarray = field(repr=False, compare=False)


@dataclass(frozen=True)
class SparseGlobalFrameDiagnostic:
    """Adaptive minimum-l1 global frame diagnostic."""

    active_scale: int
    theta_limit: int
    requested_uniform_error: float
    holdout_max_error: float
    holdout_rms_error: float
    coefficient_l1: float
    coefficient_l2: float
    support_size: int
    active_prime_pairs: int
    prime_unfold_rank: int
    cp_rank_edge_bound: int
    primes: tuple[int, ...]
    beats: tuple[PrimeBeat, ...] = field(repr=False, compare=False)
    coefficients: np.ndarray = field(repr=False, compare=False)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def square_root_prime_window(active_scale: int) -> tuple[int, ...]:
    """Return primes in ``[ceil(sqrt(H)/2),floor(sqrt(H))]``."""

    if active_scale < 64:
        raise ValueError("active_scale must be at least 64")
    order = math.isqrt(active_scale)
    lower = math.ceil(order / 2)
    primes = tuple(value for value in range(lower, order + 1) if _is_prime(value))
    if len(primes) < 2:
        raise ValueError("the square-root prime window contains fewer than two primes")
    return primes


def crt_low_beat(theta: int, prime_p: int, prime_r: int) -> tuple[int, int]:
    """Return standard numerators satisfying ``a*r-b*p=theta`` exactly."""

    if prime_p == prime_r or not _is_prime(prime_p) or not _is_prime(prime_r):
        raise ValueError("prime_p and prime_r must be distinct primes")
    if not 0 < theta < min(prime_p, prime_r):
        raise ValueError("theta must lie strictly between zero and both primes")
    numerator_p = (theta * pow(prime_r, -1, prime_p)) % prime_p
    numerator_r = (numerator_p * prime_r - theta) // prime_p
    if not 0 < numerator_r < prime_r:
        raise ArithmeticError("the CRT representative left the primitive range")
    return numerator_p, numerator_r


def global_prime_beats(
    active_scale: int,
    theta_limit: int = 4,
) -> tuple[tuple[int, ...], tuple[PrimeBeat, ...]]:
    """Return primes and all unordered-pair low beats through ``theta_limit``."""

    if theta_limit < 1:
        raise ValueError("theta_limit must be positive")
    primes = square_root_prime_window(active_scale)
    if theta_limit >= primes[0]:
        raise ValueError("theta_limit must be below the prime window")
    beats: list[PrimeBeat] = []
    for theta in range(1, theta_limit + 1):
        for p_index, prime_p in enumerate(primes):
            for r_index in range(p_index + 1, len(primes)):
                prime_r = primes[r_index]
                numerator_p, numerator_r = crt_low_beat(theta, prime_p, prime_r)
                beats.append(
                    PrimeBeat(
                        p_index=p_index,
                        r_index=r_index,
                        prime_p=prime_p,
                        prime_r=prime_r,
                        theta=theta,
                        numerator_p=numerator_p,
                        numerator_r=numerator_r,
                        scaled_frequency=active_scale * theta / (prime_p * prime_r),
                    )
                )
    return primes, tuple(beats)


def _design(points: np.ndarray, beats: tuple[PrimeBeat, ...]) -> np.ndarray:
    frequencies = np.asarray([beat.scaled_frequency for beat in beats])
    return np.cos(
        2.0 * math.pi * (np.asarray(points)[:, None] - 0.5) * frequencies[None, :]
    )


def _coefficient_tensor(
    primes: tuple[int, ...],
    theta_limit: int,
    beats: tuple[PrimeBeat, ...],
    coefficients: np.ndarray,
) -> np.ndarray:
    tensor = np.zeros((len(primes), len(primes), theta_limit), dtype=float)
    for coefficient, beat in zip(coefficients, beats, strict=True):
        # Splitting equally across orientations makes contraction against the
        # two symmetric entries recover the original unordered-pair weight.
        tensor[beat.p_index, beat.r_index, beat.theta - 1] = coefficient / 2.0
        tensor[beat.r_index, beat.p_index, beat.theta - 1] = coefficient / 2.0
    return tensor


def _tensor_coefficients(
    tensor: np.ndarray,
    beats: tuple[PrimeBeat, ...],
) -> np.ndarray:
    return np.asarray(
        [
            tensor[beat.p_index, beat.r_index, beat.theta - 1]
            + tensor[beat.r_index, beat.p_index, beat.theta - 1]
            for beat in beats
        ]
    )


def _minimum_l2_coefficients(
    weighted_design: np.ndarray,
    weighted_target: np.ndarray,
    tolerance: float,
) -> tuple[np.ndarray, float, np.ndarray]:
    gram = weighted_design @ weighted_design.T
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    eigenvalues = np.maximum(eigenvalues, 0.0)
    coordinates = eigenvectors.T @ weighted_target
    largest = max(1.0, float(eigenvalues[-1]))

    def residual(log_penalty: float) -> float:
        penalty = math.exp(log_penalty)
        return float(
            np.linalg.norm(penalty * coordinates / (eigenvalues + penalty))
        )

    lower = math.log(largest) - 44.0
    upper = math.log(largest) + 20.0
    if residual(lower) > tolerance:
        raise RuntimeError("requested global-frame error is numerically unattainable")
    for _ in range(100):
        middle = (lower + upper) / 2.0
        if residual(middle) < tolerance:
            lower = middle
        else:
            upper = middle
    penalty = math.exp((lower + upper) / 2.0)
    dual = eigenvectors @ (coordinates / (eigenvalues + penalty))
    coefficients = weighted_design.T @ dual
    return coefficients, residual(math.log(penalty)), eigenvalues


def _best_fixed_pair(
    active_scale: int,
    theta_limit: int,
    primes: tuple[int, ...],
    points: np.ndarray,
    square_root_weights: np.ndarray,
) -> tuple[float, tuple[int, int]]:
    target = square_root_weights
    best_error = math.inf
    best_pair = (0, 0)
    for p_index, prime_p in enumerate(primes):
        for prime_r in primes[p_index + 1 :]:
            frequencies = np.asarray(
                [
                    active_scale * theta / (prime_p * prime_r)
                    for theta in range(1, theta_limit + 1)
                ]
            )
            design = (
                np.cos(
                    2.0
                    * math.pi
                    * (points[:, None] - 0.5)
                    * frequencies[None, :]
                )
                * square_root_weights[:, None]
            )
            coefficients = np.linalg.lstsq(design, target, rcond=1.0e-13)[0]
            error = float(np.linalg.norm(design @ coefficients - target))
            if error < best_error:
                best_error = error
                best_pair = (prime_p, prime_r)
    return best_error, best_pair


def analyze_global_frame(
    active_scale: int,
    *,
    theta_limit: int = 4,
    error_constant: float = 15.0,
    holdout_grid_size: int = 4097,
) -> GlobalFrameDiagnostic:
    """Return the canonical minimum-l2 global low-beat diagnostic."""

    primes, beats = global_prime_beats(active_scale, theta_limit)
    maximum_frequency = max(beat.scaled_frequency for beat in beats)
    quadrature_order = max(180, math.ceil(6.0 * maximum_frequency) + 40)
    nodes, weights = leggauss(quadrature_order)
    points = (nodes + 1.0) / 2.0
    square_root_weights = np.sqrt(weights / 2.0)
    weighted_design = _design(points, beats) * square_root_weights[:, None]
    target = square_root_weights
    tolerance = error_constant / active_scale
    coefficients, quadrature_error, eigenvalues = _minimum_l2_coefficients(
        weighted_design,
        target,
        tolerance,
    )

    holdout = np.linspace(0.0, 1.0, holdout_grid_size)
    holdout_error = _design(holdout, beats) @ coefficients - 1.0
    tensor = _coefficient_tensor(primes, theta_limit, beats, coefficients)
    prime_unfolding = tensor.reshape(len(primes), len(primes) * theta_limit)
    prime_u, prime_s, prime_vh = np.linalg.svd(prime_unfolding, full_matrices=False)
    theta_s = np.linalg.svd(
        np.moveaxis(tensor, 2, 0).reshape(theta_limit, len(primes) ** 2),
        compute_uv=False,
    )
    prime_rank_tolerance = prime_s[0] * 1.0e-10
    theta_rank_tolerance = theta_s[0] * 1.0e-10

    output_rank = len(primes)
    for rank in range(1, len(primes) + 1):
        approximation = (
            (prime_u[:, :rank] * prime_s[:rank]) @ prime_vh[:rank]
        ).reshape(tensor.shape)
        approximate_coefficients = _tensor_coefficients(approximation, beats)
        output_error = float(
            np.linalg.norm(weighted_design @ approximate_coefficients - target)
        )
        if output_error <= 10.0 * tolerance:
            output_rank = rank
            break

    theta_slice_projective = 0.0
    for theta_index in range(theta_limit):
        theta_slice_projective += float(
            np.sum(np.linalg.svd(tensor[:, :, theta_index], compute_uv=False))
        )

    positive = eigenvalues[eigenvalues > eigenvalues[-1] * 1.0e-12]
    frame_condition = float(math.sqrt(eigenvalues[-1] / positive[0]))
    fixed_error, fixed_pair = _best_fixed_pair(
        active_scale,
        theta_limit,
        primes,
        points,
        square_root_weights,
    )
    return GlobalFrameDiagnostic(
        active_scale=active_scale,
        theta_limit=theta_limit,
        requested_rms_error=tolerance,
        quadrature_rms_error=quadrature_error,
        holdout_rms_error=float(
            math.sqrt(np.trapz(np.abs(holdout_error) ** 2, holdout))
        ),
        holdout_max_error=float(np.max(np.abs(holdout_error))),
        coefficient_l1=float(np.sum(np.abs(coefficients))),
        coefficient_l2=float(np.linalg.norm(coefficients)),
        frame_effective_rank=len(positive),
        frame_condition_number=frame_condition,
        prime_unfold_rank=int(np.count_nonzero(prime_s > prime_rank_tolerance)),
        prime_unfold_nuclear_norm=float(np.sum(prime_s)),
        theta_unfold_rank=int(np.count_nonzero(theta_s > theta_rank_tolerance)),
        theta_unfold_nuclear_norm=float(np.sum(theta_s)),
        theta_slice_projective_proxy=theta_slice_projective,
        output_rank_at_tenfold_error=output_rank,
        best_fixed_pair_rms_error=fixed_error,
        best_fixed_pair=fixed_pair,
        primes=primes,
        beats=beats,
        coefficients=coefficients,
    )


def analyze_sparse_global_frame(
    active_scale: int,
    *,
    theta_limit: int = 4,
    error_constant: float = 250.0,
    holdout_grid_size: int = 4097,
    max_iterations: int = 8,
) -> SparseGlobalFrameDiagnostic:
    """Return an adaptive minimum-l1 uniform global-frame diagnostic."""

    primes, beats = global_prime_beats(active_scale, theta_limit)
    tolerance = error_constant / active_scale
    grid = list(np.linspace(0.0, 1.0, 129))
    holdout = np.linspace(0.0, 1.0, holdout_grid_size)
    coefficients = np.zeros(len(beats))
    holdout_error = np.ones_like(holdout)
    for _ in range(max_iterations):
        points = np.asarray(sorted(set(grid)))
        design = _design(points, beats)
        sparse_design = csc_matrix(design)
        signed = hstack((sparse_design, -sparse_design), format="csc")
        result = linprog(
            np.ones(2 * len(beats)),
            A_ub=vstack((signed, -signed), format="csc"),
            b_ub=np.concatenate(
                (
                    np.ones(len(points)) + tolerance,
                    -np.ones(len(points)) + tolerance,
                )
            ),
            bounds=(0.0, None),
            method="highs",
        )
        if not result.success:
            raise RuntimeError(f"sparse global-frame solve failed: {result.message}")
        coefficients = result.x[: len(beats)] - result.x[len(beats) :]
        holdout_error = _design(holdout, beats) @ coefficients - 1.0
        absolute_error = np.abs(holdout_error)
        if float(np.max(absolute_error)) <= 1.001 * tolerance:
            break
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
        raise RuntimeError("adaptive sparse global-frame solve did not validate")

    tensor = _coefficient_tensor(primes, theta_limit, beats, coefficients)
    singular_values = np.linalg.svd(
        tensor.reshape(len(primes), len(primes) * theta_limit),
        compute_uv=False,
    )
    support = np.abs(coefficients) > 1.0e-8
    active_pairs = {
        (beat.p_index, beat.r_index)
        for beat, selected in zip(beats, support, strict=True)
        if selected
    }
    support_size = int(np.count_nonzero(support))
    return SparseGlobalFrameDiagnostic(
        active_scale=active_scale,
        theta_limit=theta_limit,
        requested_uniform_error=tolerance,
        holdout_max_error=float(np.max(np.abs(holdout_error))),
        holdout_rms_error=float(
            math.sqrt(np.trapz(np.abs(holdout_error) ** 2, holdout))
        ),
        coefficient_l1=float(np.sum(np.abs(coefficients))),
        coefficient_l2=float(np.linalg.norm(coefficients)),
        support_size=support_size,
        active_prime_pairs=len(active_pairs),
        prime_unfold_rank=int(
            np.count_nonzero(singular_values > singular_values[0] * 1.0e-10)
        ),
        cp_rank_edge_bound=2 * support_size,
        primes=primes,
        beats=beats,
        coefficients=coefficients,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=int, default=10000)
    parser.add_argument("--theta-limit", type=int, default=4)
    parser.add_argument("--sparse", action="store_true")
    args = parser.parse_args()
    if args.sparse:
        result = analyze_sparse_global_frame(
            args.scale,
            theta_limit=args.theta_limit,
        )
        print(f"prime_count={len(result.primes)}")
        print(f"beat_count={len(result.beats)}")
        print(f"holdout_max_error={result.holdout_max_error:.12g}")
        print(f"coefficient_l1={result.coefficient_l1:.12g}")
        print(f"support_size={result.support_size}")
        print(f"cp_rank_edge_bound={result.cp_rank_edge_bound}")
    else:
        result = analyze_global_frame(
            args.scale,
            theta_limit=args.theta_limit,
        )
        print(f"prime_count={len(result.primes)}")
        print(f"beat_count={len(result.beats)}")
        print(f"holdout_rms_error={result.holdout_rms_error:.12g}")
        print(f"coefficient_l1={result.coefficient_l1:.12g}")
        print(f"coefficient_l2={result.coefficient_l2:.12g}")
        print(f"prime_unfold_rank={result.prime_unfold_rank}")
        print(f"prime_unfold_nuclear_norm={result.prime_unfold_nuclear_norm:.12g}")
        print(f"output_rank_at_tenfold_error={result.output_rank_at_tenfold_error}")
        print(f"best_fixed_pair_rms_error={result.best_fixed_pair_rms_error:.12g}")


if __name__ == "__main__":
    main()
