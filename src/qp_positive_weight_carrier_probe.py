"""Finite actual-prime probe for the positive-weight carrier problem.

This module is deliberately diagnostic.  It scans attained contiguous
source intervals and solves sampled versions of

    rho_+(v) = inf_{w >= 0, w in C_Y, w.v = 1}
                   -inf_{t in H_Y} sum_p w_p cos(t u_p).

``C_Y`` equates the two weights on every opposite-side reflected pair with
``B * |u-u'| <= kappa``.  The unpaired variant additionally sets both
vertices of every such pair to zero.  Exchange plus a second-derivative grid
guard gives floating-point brackets for the continuum problem; it is not an
interval-arithmetic certificate and makes no asymptotic threshold claim.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from qp_radialization_lab import (
    cosine_atoms,
    local_maxima_indices,
    primes_in_shell,
    uniform_grid,
)


@dataclass(frozen=True)
class SourceEvent:
    profile: str
    start: int
    length: int
    time: float
    depth: float
    mass: float


@dataclass(frozen=True)
class PositiveCarrierBracket:
    lower: float
    upper_guard: float
    feasible: bool
    support_size: int
    effective_support_size: float
    weight_mass: float
    probability_source_leverage: float
    probability_negative_depth_lower: float
    probability_negative_depth_upper: float
    paired_weight_mass: float
    source_weight_mass: float
    source_weight_fraction: float
    source_support_size: int
    source_leverage: float
    l1_distance_to_uniform_source: float
    active_indices: tuple[int, ...]
    active_probability_weights: tuple[float, ...]
    validation_argmin: float
    source_residual: float
    pair_residual: float
    pool_size: int
    validation_size: int
    exchange_iterations: int
    curvature_guard: float
    floating_point_only: bool = True


def canonical_reflected_pairs(
    signed_nodes: np.ndarray,
    center: float,
    *,
    kappa: float = 1.0,
) -> tuple[tuple[int, int], ...]:
    """Return the canonical disjoint opposite-side ``B^-1`` matching."""

    signed_nodes = np.asarray(signed_nodes, dtype=float)
    band_top = center ** (50.0 / 33.0)
    lower = np.flatnonzero(signed_nodes < 0.0)
    upper = np.flatnonzero(signed_nodes > 0.0)
    candidates: list[tuple[float, int, int]] = []
    for lower_index in lower:
        differences = np.abs(
            np.abs(signed_nodes[upper]) - abs(signed_nodes[lower_index])
        )
        for local_index in np.flatnonzero(differences <= kappa / band_top):
            candidates.append(
                (float(differences[local_index]), int(lower_index), int(upper[local_index]))
            )

    # Same-side prime spacing makes conflicts absent in the intended range.
    # Greedy resolution keeps synthetic controls well-defined if a finite
    # perturbation happens to create a conflict.
    used_lower: set[int] = set()
    used_upper: set[int] = set()
    pairs: list[tuple[int, int]] = []
    for _, lower_index, upper_index in sorted(candidates):
        if lower_index in used_lower or upper_index in used_upper:
            continue
        pairs.append((lower_index, upper_index))
        used_lower.add(lower_index)
        used_upper.add(upper_index)
    return tuple(sorted(pairs))


def attained_fixed_length_event(
    signed_nodes: np.ndarray,
    center: float,
    length: int,
    *,
    source_points: int = 4_001,
    profile: str = "fixed",
) -> SourceEvent:
    """Find the most negative attained contiguous interval of fixed length."""

    signed_nodes = np.asarray(signed_nodes, dtype=float)
    count = len(signed_nodes)
    if not 1 <= length <= count:
        raise ValueError("source interval length is outside the node array")
    scale = int(math.floor(center))
    times = np.linspace(scale**0.5, float(scale), source_points)
    atoms = cosine_atoms(np.abs(signed_nodes), times)
    cumulative = np.vstack([np.zeros((1, source_points)), np.cumsum(atoms, axis=0)])
    window_sums = cumulative[length:] - cumulative[:-length]
    flat_index = int(np.argmin(window_sums))
    start, time_index = np.unravel_index(flat_index, window_sums.shape)
    source_sum = float(window_sums[start, time_index])
    depth = -source_sum / length
    return SourceEvent(
        profile=profile,
        start=int(start),
        length=int(length),
        time=float(times[time_index]),
        depth=float(depth),
        mass=float(-source_sum / scale),
    )


def order_scramble_control(signed_nodes: np.ndarray, seed: int) -> np.ndarray:
    """Scramble source order within each side while preserving all nodes."""

    result = np.asarray(signed_nodes, dtype=float).copy()
    rng = np.random.default_rng(seed)
    for sign in (-1, 1):
        indices = np.flatnonzero(np.signbit(result) if sign < 0 else result > 0.0)
        result[indices] = result[indices][rng.permutation(len(indices))]
    return result


def gap_scramble_control(signed_nodes: np.ndarray, seed: int) -> np.ndarray:
    """Permute within-side log gaps, retaining counts and side spans."""

    result = np.asarray(signed_nodes, dtype=float).copy()
    rng = np.random.default_rng(seed)
    for sign in (-1, 1):
        indices = np.flatnonzero(result < 0.0) if sign < 0 else np.flatnonzero(result > 0.0)
        values = np.sort(result[indices])
        if len(values) <= 2:
            continue
        gaps = np.diff(values)
        rebuilt = np.r_[values[0], values[0] + np.cumsum(gaps[rng.permutation(len(gaps))])]
        result[indices] = rebuilt
    return result


def source_phase_lift_control(
    signed_nodes: np.ndarray,
    source_time: float,
    seed: int,
) -> np.ndarray:
    """Randomize phase lifts while preserving every source cosine exactly.

    For each side separately, replace ``u`` by another solution of
    ``cos(source_time*u')=cos(source_time*u)`` in that side's observed
    absolute-frequency span.  The coordinate order is retained, so every
    contiguous source interval has the same value at ``source_time``.  This
    is a labelled synthetic control, not another prime shell.
    """

    signed_nodes = np.asarray(signed_nodes, dtype=float)
    result = signed_nodes.copy()
    rng = np.random.default_rng(seed)
    period = 2.0 * math.pi
    for sign in (-1, 1):
        indices = np.flatnonzero(signed_nodes < 0.0) if sign < 0 else np.flatnonzero(signed_nodes > 0.0)
        if not len(indices):
            continue
        absolute = np.abs(signed_nodes[indices])
        left = float(np.min(absolute))
        right = float(np.max(absolute))
        for index in indices:
            original = abs(float(signed_nodes[index]))
            angle = math.acos(max(-1.0, min(1.0, math.cos(source_time * original))))
            first_k = math.floor(source_time * left / period) - 1
            last_k = math.ceil(source_time * right / period) + 1
            candidates: list[float] = []
            for k in range(first_k, last_k + 1):
                for orientation in (-1.0, 1.0):
                    candidate = (period * k + orientation * angle) / source_time
                    if left - 1e-14 <= candidate <= right + 1e-14 and candidate > 0.0:
                        candidates.append(float(candidate))
            candidates = sorted(set(round(candidate, 15) for candidate in candidates))
            alternatives = [candidate for candidate in candidates if abs(candidate - original) > 1e-12]
            chosen = float(rng.choice(alternatives if alternatives else candidates))
            result[index] = math.copysign(chosen, float(sign))
    return result


def _solve_sampled_positive_carrier(
    nodes: np.ndarray,
    direction: np.ndarray,
    times: np.ndarray,
    pairs: tuple[tuple[int, int], ...],
    *,
    unpaired_only: bool,
) -> tuple[np.ndarray, float] | None:
    """Solve one sampled positive-carrier LP."""

    nodes = np.asarray(nodes, dtype=float)
    direction = np.asarray(direction, dtype=float)
    atoms = cosine_atoms(nodes, times)
    count = len(nodes)

    # Variables are (w_1,...,w_n,rho), and -F_w(t) <= rho.
    objective = np.r_[np.zeros(count), 1.0]
    inequalities = np.c_[-atoms.T, -np.ones(len(times))]
    equality = np.zeros((1 + len(pairs), count + 1))
    equality[0, :count] = direction
    rhs = np.zeros(1 + len(pairs))
    rhs[0] = 1.0
    for row, (lower_index, upper_index) in enumerate(pairs, start=1):
        equality[row, lower_index] = 1.0
        equality[row, upper_index] = -1.0

    paired_vertices = {index for pair in pairs for index in pair}
    bounds: list[tuple[float | None, float | None]] = []
    for index in range(count):
        if unpaired_only and index in paired_vertices:
            bounds.append((0.0, 0.0))
        else:
            bounds.append((0.0, None))
    bounds.append((None, None))

    solution = linprog(
        objective,
        A_ub=inequalities,
        b_ub=np.zeros(len(times)),
        A_eq=equality,
        b_eq=rhs,
        bounds=bounds,
        method="highs",
        options={
            "dual_feasibility_tolerance": 1e-9,
            "primal_feasibility_tolerance": 1e-9,
        },
    )
    if not solution.success:
        return None
    return solution.x[:count], float(solution.x[-1])


def _polynomial_values(nodes: np.ndarray, weights: np.ndarray, times: np.ndarray) -> np.ndarray:
    values = np.empty(len(times))
    chunk = 30_000
    for left in range(0, len(times), chunk):
        right = min(len(times), left + chunk)
        values[left:right] = cosine_atoms(nodes, times[left:right]).T @ weights
    return values


def positive_carrier_exchange(
    nodes: np.ndarray,
    direction: np.ndarray,
    center: float,
    pairs: tuple[tuple[int, int], ...],
    *,
    unpaired_only: bool = False,
    initial_points: int = 1_001,
    validation_phase_step: float = 0.25,
    max_iterations: int = 6,
    source_indices: np.ndarray | None = None,
) -> PositiveCarrierBracket:
    """Return a floating lower/guarded-upper bracket for ``rho_+``."""

    nodes = np.asarray(nodes, dtype=float)
    left = center**0.01
    right = center ** (50.0 / 33.0)
    pool = np.linspace(left, right, max(initial_points, 8 * (len(nodes) + 1)))
    validation = uniform_grid(
        left,
        right,
        float(np.max(nodes)),
        validation_phase_step,
    )
    validation_step = float(validation[1] - validation[0])
    solution: tuple[np.ndarray, float] | None = None
    upper = math.inf
    curvature_guard = math.inf

    for iteration in range(1, max_iterations + 1):
        solution = _solve_sampled_positive_carrier(
            nodes,
            direction,
            pool,
            pairs,
            unpaired_only=unpaired_only,
        )
        if solution is None:
            return PositiveCarrierBracket(
                lower=math.inf,
                upper_guard=math.inf,
                feasible=False,
                support_size=0,
                effective_support_size=0.0,
                weight_mass=math.inf,
                probability_source_leverage=0.0,
                probability_negative_depth_lower=math.inf,
                probability_negative_depth_upper=math.inf,
                paired_weight_mass=math.inf,
                source_weight_mass=math.inf,
                source_weight_fraction=math.nan,
                source_support_size=0,
                source_leverage=math.nan,
                l1_distance_to_uniform_source=math.nan,
                active_indices=(),
                active_probability_weights=(),
                validation_argmin=math.nan,
                source_residual=math.inf,
                pair_residual=math.inf,
                pool_size=len(pool),
                validation_size=len(validation),
                exchange_iterations=iteration,
                curvature_guard=math.inf,
            )
        weights, lower = solution
        values = _polynomial_values(nodes, weights, validation)
        curvature = float(np.dot(weights, nodes * nodes))
        curvature_guard = curvature * validation_step**2 / 8.0
        upper = -float(np.min(values)) + curvature_guard
        if upper - lower <= 2e-4 * max(1.0, abs(lower)) + 1e-9:
            break

        minima = local_maxima_indices(-values)
        chosen = minima[
            np.argsort(values[minima])[: min(2 * len(nodes), len(minima))]
        ]
        pool = np.unique(np.r_[pool, validation[chosen]])

    assert solution is not None
    weights, lower = solution
    source_residual = abs(float(np.dot(weights, direction)) - 1.0)
    pair_residual = max(
        (abs(float(weights[i] - weights[j])) for i, j in pairs),
        default=0.0,
    )
    support_threshold = max(1e-10, 1e-8 * float(np.max(weights)))
    if source_indices is None:
        source_indices_array = np.empty(0, dtype=int)
    else:
        source_indices_array = np.asarray(source_indices, dtype=int)
    weight_mass = float(np.sum(weights))
    source_weight_mass = float(np.sum(weights[source_indices_array]))
    probability_weights = weights / weight_mass
    uniform_source = np.zeros(len(weights))
    if len(source_indices_array):
        uniform_source[source_indices_array] = 1.0 / len(source_indices_array)
        l1_distance = float(np.sum(np.abs(probability_weights - uniform_source)))
    else:
        l1_distance = math.nan
    active_indices_array = np.flatnonzero(weights > support_threshold)
    return PositiveCarrierBracket(
        lower=float(lower),
        upper_guard=float(upper),
        feasible=True,
        support_size=int(np.count_nonzero(weights > support_threshold)),
        effective_support_size=float(
            weight_mass * weight_mass / np.dot(weights, weights)
        ),
        weight_mass=weight_mass,
        probability_source_leverage=1.0 / weight_mass,
        probability_negative_depth_lower=float(lower / weight_mass),
        probability_negative_depth_upper=float(upper / weight_mass),
        paired_weight_mass=float(
            np.sum(weights[list({index for pair in pairs for index in pair})])
            if pairs
            else 0.0
        ),
        source_weight_mass=source_weight_mass,
        source_weight_fraction=(
            source_weight_mass / weight_mass if weight_mass > 0.0 else math.nan
        ),
        source_support_size=int(
            np.count_nonzero(weights[source_indices_array] > support_threshold)
        ),
        source_leverage=float(
            np.dot(weights[source_indices_array], direction[source_indices_array])
        ),
        l1_distance_to_uniform_source=l1_distance,
        active_indices=tuple(int(index) for index in active_indices_array),
        active_probability_weights=tuple(
            float(probability_weights[index]) for index in active_indices_array
        ),
        validation_argmin=float(validation[int(np.argmin(values))]),
        source_residual=source_residual,
        pair_residual=pair_residual,
        pool_size=len(pool),
        validation_size=len(validation),
        exchange_iterations=iteration,
        curvature_guard=float(curvature_guard),
    )


def probe_center(
    center: float,
    *,
    shell_width: float = 0.2,
    source_points: int = 4_001,
    initial_points: int = 1_001,
    validation_phase_step: float = 0.25,
    max_iterations: int = 6,
    seed: int = 1729,
) -> list[dict[str, object]]:
    """Probe actual nodes and two matched controls at one center."""

    primes, actual_signed = primes_in_shell(center, shell_width)
    controls = {
        "actual": actual_signed,
        "order_scramble": order_scramble_control(actual_signed, seed + int(center)),
        "gap_scramble": gap_scramble_control(actual_signed, seed + 2 * int(center)),
    }
    lengths = {
        "full": len(primes),
        "half": max(1, math.ceil(len(primes) / 2)),
    }
    records: list[dict[str, object]] = []
    for control_name, signed_nodes in controls.items():
        pairs = canonical_reflected_pairs(signed_nodes, center)
        nodes = np.abs(signed_nodes)
        for profile, length in lengths.items():
            event = attained_fixed_length_event(
                signed_nodes,
                center,
                length,
                source_points=source_points,
                profile=profile,
            )
            direction = np.cos(nodes * event.time) + event.depth
            source_indices = np.arange(event.start, event.start + event.length)
            full = positive_carrier_exchange(
                nodes,
                direction,
                center,
                pairs,
                initial_points=initial_points,
                validation_phase_step=validation_phase_step,
                max_iterations=max_iterations,
                source_indices=source_indices,
            )
            unpaired = positive_carrier_exchange(
                nodes,
                direction,
                center,
                pairs,
                unpaired_only=True,
                initial_points=initial_points,
                validation_phase_step=validation_phase_step,
                max_iterations=max_iterations,
                source_indices=source_indices,
            )
            full_record = asdict(full)
            unpaired_record = asdict(unpaired)
            if control_name == "actual":
                full_record["active_prime_labels"] = [
                    int(primes[index]) for index in full.active_indices
                ]
                unpaired_record["active_prime_labels"] = [
                    int(primes[index]) for index in unpaired.active_indices
                ]
            records.append(
                {
                    "center": center,
                    "scale": int(math.floor(center)),
                    "prime_count": int(len(primes)),
                    "control": control_name,
                    "pair_count": int(len(pairs)),
                    "event": asdict(event),
                    "rho_positive": full_record,
                    "rho_positive_unpaired": unpaired_record,
                }
            )

    # Per-event phase-lift controls preserve t_0, M, D, and e exactly rather
    # than selecting a different source extremum on the synthetic nodes.
    for profile, length in lengths.items():
        event = attained_fixed_length_event(
            actual_signed,
            center,
            length,
            source_points=source_points,
            profile=profile,
        )
        lifted = source_phase_lift_control(
            actual_signed,
            event.time,
            seed + 3 * int(center) + length,
        )
        lifted_nodes = np.abs(lifted)
        lifted_pairs = canonical_reflected_pairs(lifted, center)
        direction = np.cos(lifted_nodes * event.time) + event.depth
        source_indices = np.arange(event.start, event.start + event.length)
        full = positive_carrier_exchange(
            lifted_nodes,
            direction,
            center,
            lifted_pairs,
            initial_points=initial_points,
            validation_phase_step=validation_phase_step,
            max_iterations=max_iterations,
            source_indices=source_indices,
        )
        unpaired = positive_carrier_exchange(
            lifted_nodes,
            direction,
            center,
            lifted_pairs,
            unpaired_only=True,
            initial_points=initial_points,
            validation_phase_step=validation_phase_step,
            max_iterations=max_iterations,
            source_indices=source_indices,
        )
        source_cosine_error = float(
            np.max(
                np.abs(
                    np.cos(lifted_nodes * event.time)
                    - np.cos(np.abs(actual_signed) * event.time)
                )
            )
        )
        records.append(
            {
                "center": center,
                "scale": int(math.floor(center)),
                "prime_count": int(len(primes)),
                "control": "source_phase_lift",
                "pair_count": int(len(lifted_pairs)),
                "source_cosine_error": source_cosine_error,
                "event": asdict(event),
                "rho_positive": asdict(full),
                "rho_positive_unpaired": asdict(unpaired),
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("centers", nargs="*", type=float, default=[254.5, 500.5, 800.5])
    parser.add_argument("--shell-width", type=float, default=0.2)
    parser.add_argument("--source-points", type=int, default=4_001)
    parser.add_argument("--initial-points", type=int, default=1_001)
    parser.add_argument("--validation-phase-step", type=float, default=0.25)
    parser.add_argument("--max-iterations", type=int, default=6)
    parser.add_argument("--seed", type=int, default=1729)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records: list[dict[str, object]] = []
    for center in args.centers:
        records.extend(
            probe_center(
                center,
                shell_width=args.shell_width,
                source_points=args.source_points,
                initial_points=args.initial_points,
                validation_phase_step=args.validation_phase_step,
                max_iterations=args.max_iterations,
                seed=args.seed,
            )
        )
    artifact = {
        "metadata": {
            "centers": args.centers,
            "shell_width": args.shell_width,
            "source_points": args.source_points,
            "initial_points": args.initial_points,
            "validation_phase_step": args.validation_phase_step,
            "max_iterations": args.max_iterations,
            "seed": args.seed,
            "source_profiles": ["full", "half"],
            "floating_point_only": True,
        },
        "records": records,
    }
    payload = json.dumps(artifact, indent=2, sort_keys=True)
    if args.output is not None:
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
