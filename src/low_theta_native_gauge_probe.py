#!/usr/bin/env python3
"""Diagnostics for a theta-independent low-beat gauge.

There are two distinct questions here.

First, the global square-root-prime envelope probe allows an independent
coefficient for every ``(p,r,theta)``.  A coefficient inherited from a
Ramanujan pair would instead be independent of ``theta``.  The function
``analyze_profile_envelope`` imposes that constraint, or a fixed-dimensional
polynomial perturbation of it, and solves the resulting finite minimax
problem.

Second, smooth test functions do have rapidly decaying Fourier coefficients,
but this observation alone says nothing when a change of coordinates is
allowed to have very large coefficients.  The function
``analyze_exact_gauge`` splits an exact primitive Farey frame into tied low
theta packets and unrestricted high theta modes.  It compares the canonical
minimum-norm exact gauge, the cheapest gauge killing one prescribed contact,
and a deliberately ill-conditioned low-theta fit of the whole target.

These are finite mechanism tests.  They neither estimate the coefficients
arising in the zeta problem nor prove a zero-free region.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import linprog

from farey_beat_frame_probe import exact_gram_formula, primitive_residues
from finite_ramanujan_completion_probe import expected_von_mangoldt
from global_prime_beat_frame_probe import _design, global_prime_beats
from ramanujan_null_gauge_probe import evaluate


@dataclass(frozen=True)
class ProfileEnvelopeDiagnostic:
    """Minimum-l1 envelope reconstruction with a fixed theta profile bank."""

    active_scale: int
    theta_limit: int
    profile_dimension: int
    requested_uniform_error: float
    holdout_max_error: float
    parameter_l1: float
    expanded_beat_l1: float
    parameter_support: int
    active_pair_support: int


@dataclass(frozen=True)
class ExactGaugeDiagnostic:
    """One exact low-packet/high-theta decomposition."""

    length: int
    theta_limit: int
    target_name: str
    strategy: str
    prime_count: int
    pair_count: int
    reconstruction_error: float
    full_contact: float
    low_contact: float
    high_contact: float
    high_contact_majorant: float
    packet_parameter_l1: float
    expanded_low_l1: float
    expanded_low_l2: float
    high_l2: float
    total_l2: float
    pre_repair_residual_l2: float


def _theta_profiles(theta_limit: int, profile_dimension: int) -> np.ndarray:
    """Return the fixed monomial bank ``1,z,...`` on the theta indices."""

    if theta_limit < 1:
        raise ValueError("theta_limit must be positive")
    if not 1 <= profile_dimension <= theta_limit:
        raise ValueError("profile_dimension must lie between one and theta_limit")
    if theta_limit == 1:
        scaled_theta = np.zeros(1)
    else:
        scaled_theta = np.linspace(-1.0, 1.0, theta_limit)
    return np.vstack(
        [scaled_theta**degree for degree in range(profile_dimension)]
    )


def _profile_design(
    points: np.ndarray,
    beats: tuple,
    pair_indices: dict[tuple[int, int], int],
    profiles: np.ndarray,
) -> np.ndarray:
    """Contract the independent beat design against fixed theta profiles."""

    independent = _design(points, beats)
    profile_dimension = profiles.shape[0]
    result = np.zeros(
        (len(points), len(pair_indices) * profile_dimension), dtype=float
    )
    for column, beat in enumerate(beats):
        pair_index = pair_indices[(beat.p_index, beat.r_index)]
        start = pair_index * profile_dimension
        result[:, start : start + profile_dimension] += (
            independent[:, column, None]
            * profiles[:, beat.theta - 1][None, :]
        )
    return result


def analyze_profile_envelope(
    active_scale: int,
    *,
    theta_limit: int = 4,
    profile_dimension: int = 1,
    uniform_error: float = 0.1,
    holdout_grid_size: int = 4097,
    max_iterations: int = 8,
) -> ProfileEnvelopeDiagnostic:
    """Solve the finite minimum-l1 contact-envelope problem.

    Dimension one means that every low ``theta`` belonging to a fixed prime
    pair has the same coefficient.  Dimension two permits an affine
    perturbation in ``theta``.  The l1 objective is imposed on the parameters
    in the displayed monomial basis; ``expanded_beat_l1`` also reports the l1
    norm after expanding back into individual beats.
    """

    if not 0.0 < uniform_error < 1.0:
        raise ValueError("uniform_error must lie strictly between zero and one")
    _, beats = global_prime_beats(active_scale, theta_limit)
    pairs = sorted({(beat.p_index, beat.r_index) for beat in beats})
    pair_indices = {pair: index for index, pair in enumerate(pairs)}
    profiles = _theta_profiles(theta_limit, profile_dimension)
    grid = list(np.linspace(0.0, 1.0, 129))
    holdout = np.linspace(0.0, 1.0, holdout_grid_size)
    parameters = np.zeros(len(pairs) * profile_dimension)
    holdout_error = np.ones_like(holdout)

    for _ in range(max_iterations):
        points = np.asarray(sorted(set(grid)))
        design = _profile_design(points, beats, pair_indices, profiles)
        signed_design = np.hstack((design, -design))
        result = linprog(
            np.ones(2 * design.shape[1]),
            A_ub=np.vstack((signed_design, -signed_design)),
            b_ub=np.concatenate(
                (
                    np.ones(len(points)) + uniform_error,
                    -np.ones(len(points)) + uniform_error,
                )
            ),
            bounds=(0.0, None),
            method="highs",
        )
        if not result.success:
            raise RuntimeError(f"profile-envelope solve failed: {result.message}")
        parameters = result.x[: design.shape[1]] - result.x[design.shape[1] :]
        holdout_error = (
            _profile_design(holdout, beats, pair_indices, profiles) @ parameters
            - 1.0
        )
        absolute_error = np.abs(holdout_error)
        if float(np.max(absolute_error)) <= 1.001 * uniform_error:
            break
        local_maxima = np.where(
            (absolute_error[1:-1] >= absolute_error[:-2])
            & (absolute_error[1:-1] >= absolute_error[2:])
            & (absolute_error[1:-1] > 1.0001 * uniform_error)
        )[0] + 1
        candidates = np.concatenate(
            (
                np.asarray([0]),
                local_maxima,
                np.asarray([len(holdout) - 1]),
            )
        )
        candidates = candidates[
            absolute_error[candidates] > 1.0001 * uniform_error
        ]
        strongest = candidates[np.argsort(-absolute_error[candidates])[:128]]
        grid.extend(holdout[strongest].tolist())
    else:
        raise RuntimeError("adaptive profile-envelope solve did not validate")

    expanded = []
    active_pairs: set[tuple[int, int]] = set()
    for beat in beats:
        pair = (beat.p_index, beat.r_index)
        start = pair_indices[pair] * profile_dimension
        value = float(
            parameters[start : start + profile_dimension]
            @ profiles[:, beat.theta - 1]
        )
        expanded.append(value)
        if abs(value) > 1.0e-8:
            active_pairs.add(pair)
    return ProfileEnvelopeDiagnostic(
        active_scale=active_scale,
        theta_limit=theta_limit,
        profile_dimension=profile_dimension,
        requested_uniform_error=uniform_error,
        holdout_max_error=float(np.max(np.abs(holdout_error))),
        parameter_l1=float(np.sum(np.abs(parameters))),
        expanded_beat_l1=float(np.sum(np.abs(expanded))),
        parameter_support=int(np.count_nonzero(np.abs(parameters) > 1.0e-8)),
        active_pair_support=len(active_pairs),
    )


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def _exact_prime_bank(length: int) -> tuple[int, ...]:
    """Return primes in ``[1.5 sqrt(H),3 sqrt(H)]``."""

    if length < 32:
        raise ValueError("length must be at least 32")
    lower = math.ceil(1.5 * math.sqrt(length))
    upper = math.floor(3.0 * math.sqrt(length))
    primes = tuple(value for value in range(lower, upper + 1) if _is_prime(value))
    if len(primes) < 2:
        raise ValueError("the exact-frame prime bank has fewer than two primes")
    return primes


def _target(length: int, target_name: str) -> np.ndarray:
    if target_name == "constant":
        return np.ones(length)
    if target_name == "prime":
        return np.asarray(
            [
                evaluate(expected_von_mangoldt(value)) - 1.0
                for value in range(length + 1, 2 * length + 1)
            ],
            dtype=float,
        )
    raise ValueError("target_name must be 'constant' or 'prime'")


def _contact_weights(length: int) -> np.ndarray:
    """Return a normalized-grid sample of a compact C-infinity bump."""

    points = (np.arange(length, dtype=float) + 0.5) / length
    return np.exp(4.0 - 1.0 / (points * (1.0 - points))) / length


def _high_contact_majorant(
    points: np.ndarray,
    contact_weights: np.ndarray,
    dual: np.ndarray,
    pairs: tuple[tuple[int, int], ...],
    theta_limit: int,
    *,
    chunk_size: int = 512,
) -> float:
    """Return ``sum_high |c_theta <g,e_theta>|`` without a huge frame."""

    majorant = 0.0
    for prime_p, prime_r in pairs:
        modulus = prime_p * prime_r
        excluded = set(range(1, theta_limit + 1))
        excluded.update(modulus - theta for theta in range(1, theta_limit + 1))
        residues = np.asarray(
            [
                residue
                for residue in primitive_residues(modulus)
                if residue not in excluded
            ],
            dtype=float,
        )
        for start in range(0, len(residues), chunk_size):
            chunk = residues[start : start + chunk_size]
            modes = np.exp(
                2j
                * math.pi
                * points[:, None]
                * chunk[None, :]
                / modulus
            )
            coefficients = modes.conj().T @ dual
            contacts = contact_weights @ modes
            majorant += float(np.sum(np.abs(coefficients * contacts)))
    return majorant


def analyze_exact_gauge(
    length: int,
    *,
    theta_limit: int = 4,
    target_name: str = "constant",
    strategy: str = "joint",
    compute_majorant: bool = True,
) -> ExactGaugeDiagnostic:
    """Split an exact frame into tied low packets and free high modes.

    ``joint`` is the minimum-l2 exact representation in the combined frame.
    ``contact-zero`` is the minimum-l2 exact representation subject to zero
    high-sector contact with the fixed smooth bump.  ``low-fit`` first applies
    an unregularized least-squares fit of the *whole target* using only the
    tied packets and then repairs its residual exactly with high modes.
    ``high-only`` sets all packet parameters to zero.
    """

    if theta_limit < 1:
        raise ValueError("theta_limit must be positive")
    if strategy not in {"joint", "contact-zero", "low-fit", "high-only"}:
        raise ValueError("unknown exact-gauge strategy")
    primes = _exact_prime_bank(length)
    pairs = tuple(
        (prime_p, prime_r)
        for p_index, prime_p in enumerate(primes)
        for prime_r in primes[p_index + 1 :]
        if prime_p * prime_r > length
    )
    if not pairs:
        raise ValueError("the exact-frame pair bank is empty")
    if theta_limit >= min(primes):
        raise ValueError("theta_limit must be below every prime in the bank")

    integer_points = np.arange(length + 1, 2 * length + 1, dtype=float)
    packets: list[np.ndarray] = []
    high_gram = np.zeros((length, length), dtype=float)
    for prime_p, prime_r in pairs:
        modulus = prime_p * prime_r
        theta = np.arange(1, theta_limit + 1)
        low_residues = np.concatenate((theta, modulus - theta))
        low_modes = np.exp(
            2j
            * math.pi
            * integer_points[:, None]
            * low_residues[None, :]
            / modulus
        )
        packets.append(np.real(np.sum(low_modes, axis=1)))
        high_gram += exact_gram_formula(length, prime_p, prime_r) - np.real(
            low_modes @ low_modes.conj().T
        )
    packet_design = np.stack(packets, axis=1)
    high_gram = (high_gram + high_gram.T) / 2.0
    target = _target(length, target_name)
    weights = _contact_weights(length)
    modes_per_packet = 2 * theta_limit

    if strategy == "joint":
        joint_gram = high_gram + packet_design @ packet_design.T / modes_per_packet
        dual = np.linalg.solve(joint_gram, target)
        parameters = packet_design.T @ dual / modes_per_packet
        pre_repair_residual = target - packet_design @ parameters
    elif strategy == "contact-zero":
        # Minimize
        #
        #   L ||d||^2 + (target-Dd)^* G_high^{-1} (target-Dd)
        #
        # subject to <weights,target-Dd>=0.  This is the exact coefficient
        # norm, so the KKT solve measures the cheapest scalar contact gauge,
        # rather than over-solving by fitting the full target vector.
        inverse_high_design = np.linalg.solve(high_gram, packet_design)
        inverse_high_target = np.linalg.solve(high_gram, target)
        normal = (
            modes_per_packet * np.eye(packet_design.shape[1])
            + packet_design.T @ inverse_high_design
        )
        linear = packet_design.T @ inverse_high_target
        unconstrained = np.linalg.solve(normal, linear)
        contact_vector = packet_design.T @ weights
        normal_contact = np.linalg.solve(normal, contact_vector)
        denominator = float(contact_vector @ normal_contact)
        if denominator <= 0.0:
            raise RuntimeError("the low packets cannot alter the chosen contact")
        correction = (
            float(weights @ target - contact_vector @ unconstrained)
            / denominator
        )
        parameters = unconstrained + correction * normal_contact
        pre_repair_residual = target - packet_design @ parameters
        dual = np.linalg.solve(high_gram, pre_repair_residual)
    elif strategy == "low-fit":
        parameters = np.linalg.lstsq(
            packet_design, target, rcond=1.0e-13
        )[0]
        pre_repair_residual = target - packet_design @ parameters
        dual = np.linalg.solve(high_gram, pre_repair_residual)
    else:
        parameters = np.zeros(len(pairs))
        pre_repair_residual = target
        dual = np.linalg.solve(high_gram, target)

    low_reconstruction = packet_design @ parameters
    high_reconstruction = high_gram @ dual
    reconstruction = low_reconstruction + high_reconstruction
    high_norm_squared = float(dual @ high_gram @ dual)
    low_norm_squared = float(modes_per_packet * (parameters @ parameters))
    majorant = (
        _high_contact_majorant(
            integer_points,
            weights,
            dual,
            pairs,
            theta_limit,
        )
        if compute_majorant
        else math.nan
    )
    return ExactGaugeDiagnostic(
        length=length,
        theta_limit=theta_limit,
        target_name=target_name,
        strategy=strategy,
        prime_count=len(primes),
        pair_count=len(pairs),
        reconstruction_error=float(np.max(np.abs(reconstruction - target))),
        full_contact=float(weights @ target),
        low_contact=float(weights @ low_reconstruction),
        high_contact=float(weights @ high_reconstruction),
        high_contact_majorant=majorant,
        packet_parameter_l1=float(np.sum(np.abs(parameters))),
        expanded_low_l1=float(modes_per_packet * np.sum(np.abs(parameters))),
        expanded_low_l2=math.sqrt(max(0.0, low_norm_squared)),
        high_l2=math.sqrt(max(0.0, high_norm_squared)),
        total_l2=math.sqrt(max(0.0, low_norm_squared + high_norm_squared)),
        pre_repair_residual_l2=float(np.linalg.norm(pre_repair_residual)),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=int, default=4096)
    parser.add_argument("--theta-limit", type=int, default=4)
    parser.add_argument("--profile-dimension", type=int, default=1)
    parser.add_argument("--exact", action="store_true")
    parser.add_argument("--target", choices=("constant", "prime"), default="constant")
    parser.add_argument(
        "--strategy",
        choices=("joint", "contact-zero", "low-fit", "high-only"),
        default="joint",
    )
    args = parser.parse_args()
    if args.exact:
        result = analyze_exact_gauge(
            args.scale,
            theta_limit=args.theta_limit,
            target_name=args.target,
            strategy=args.strategy,
        )
        print(f"pair_count={result.pair_count}")
        print(f"reconstruction_error={result.reconstruction_error:.12g}")
        print(f"full_contact={result.full_contact:.12g}")
        print(f"high_contact={result.high_contact:.12g}")
        print(f"high_contact_majorant={result.high_contact_majorant:.12g}")
        print(f"total_l2={result.total_l2:.12g}")
    else:
        result = analyze_profile_envelope(
            args.scale,
            theta_limit=args.theta_limit,
            profile_dimension=args.profile_dimension,
        )
        print(f"holdout_max_error={result.holdout_max_error:.12g}")
        print(f"parameter_l1={result.parameter_l1:.12g}")
        print(f"expanded_beat_l1={result.expanded_beat_l1:.12g}")


if __name__ == "__main__":
    main()
