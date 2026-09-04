"""Event-free finite diagnostics for positive prime antennas.

For shell nodes ``u_p = |log(p/Y)|`` this module probes

    delta_+(Y) = inf_{alpha >= 0, sum alpha = 1}
                     -inf_{t in H_Y} sum_p alpha_p cos(t u_p)

on three nested feasible sets: the full probability simplex, the simplex
intersected with the canonical reflected-pair carrier, and that carrier with
the coordinate cap ``alpha_p <= C log(Y) / Y``.  The three sampled LPs use a
shared exchange pool, so their finite-pool lower values have the exact nesting
order.  A uniform validation grid and the positive-weight curvature bound
``sum alpha_p u_p**2`` give a guarded upper value for each returned candidate.

All brackets are floating-point diagnostics.  They are neither
interval-arithmetic certificates nor evidence for an asymptotic limit.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math
from pathlib import Path
from typing import Mapping

import numpy as np
from scipy.optimize import linprog

from qp_positive_weight_carrier_probe import canonical_reflected_pairs
from qp_radialization_lab import (
    cosine_atoms,
    local_maxima_indices,
    primes_in_shell,
    uniform_grid,
)


@dataclass(frozen=True)
class SampledPositiveAntennaSolution:
    """One finite-pool LP solution and its inequality dual contact measure."""

    weights: np.ndarray
    level: float
    dual_weights: np.ndarray
    dual_weight_sum: float
    complementarity_residual: float


@dataclass(frozen=True)
class PositiveAntennaBracket:
    """Floating lower/candidate-upper bracket for one positive antenna cone."""

    lower: float
    upper_guard: float
    feasible: bool
    coordinate_cap: float | None
    support_size: int
    effective_support_size: float
    max_coordinate: float
    saturated_coordinate_count: int
    active_indices: tuple[int, ...]
    active_probability_weights: tuple[float, ...]
    validation_minimum: float
    validation_argmin: float
    simplex_residual: float
    pair_residual: float
    cap_violation: float
    pool_size: int
    validation_size: int
    exchange_iterations: int
    curvature: float
    curvature_guard: float
    sampled_dual_contact_count: int
    sampled_dual_contact_times: tuple[float, ...]
    sampled_dual_contact_weights: tuple[float, ...]
    sampled_dual_weight_sum: float
    sampled_dual_complementarity_residual: float
    floating_point_only: bool = True


def _solve_sampled_positive_antenna(
    nodes: np.ndarray,
    times: np.ndarray,
    pairs: tuple[tuple[int, int], ...] = (),
    *,
    coordinate_cap: float | None = None,
) -> SampledPositiveAntennaSolution | None:
    """Minimize the worst negative value on a finite time pool.

    The variables are ``(alpha_1,...,alpha_n,rho)`` and the sampled
    constraints are ``-Phi_alpha(t) <= rho``.  HiGHS' nonpositive inequality
    marginals are negated to obtain the nonnegative contact measure.
    """

    nodes = np.asarray(nodes, dtype=float)
    times = np.asarray(times, dtype=float)
    if nodes.ndim != 1 or len(nodes) == 0 or np.any(nodes <= 0.0):
        raise ValueError("nodes must be a nonempty positive one-dimensional array")
    if times.ndim != 1 or len(times) == 0:
        raise ValueError("times must be a nonempty one-dimensional array")
    if coordinate_cap is not None:
        if not math.isfinite(coordinate_cap) or coordinate_cap <= 0.0:
            raise ValueError("coordinate_cap must be positive and finite")
        if len(nodes) * coordinate_cap < 1.0 - 1e-12:
            return None

    count = len(nodes)
    atoms = cosine_atoms(nodes, times)
    objective = np.r_[np.zeros(count), 1.0]
    inequalities = np.c_[-atoms.T, -np.ones(len(times))]
    equality = np.zeros((1 + len(pairs), count + 1))
    equality[0, :count] = 1.0
    rhs = np.zeros(1 + len(pairs))
    rhs[0] = 1.0
    for row, (first, second) in enumerate(pairs, start=1):
        if not (0 <= first < count and 0 <= second < count and first != second):
            raise ValueError("invalid carrier pair")
        equality[row, first] = 1.0
        equality[row, second] = -1.0

    alpha_bound = (0.0, coordinate_cap)
    solution = linprog(
        objective,
        A_ub=inequalities,
        b_ub=np.zeros(len(times)),
        A_eq=equality,
        b_eq=rhs,
        bounds=[alpha_bound] * count + [(None, None)],
        method="highs",
        options={
            "dual_feasibility_tolerance": 1e-9,
            "primal_feasibility_tolerance": 1e-9,
        },
    )
    if not solution.success:
        return None

    dual_weights = np.maximum(-np.asarray(solution.ineqlin.marginals), 0.0)
    slacks = np.asarray(solution.ineqlin.residual)
    return SampledPositiveAntennaSolution(
        weights=np.asarray(solution.x[:count]),
        level=float(solution.x[-1]),
        dual_weights=dual_weights,
        dual_weight_sum=float(np.sum(dual_weights)),
        complementarity_residual=float(
            np.max(np.abs(dual_weights * slacks), initial=0.0)
        ),
    )


def _polynomial_values(
    nodes: np.ndarray,
    weights: np.ndarray,
    times: np.ndarray,
) -> np.ndarray:
    """Evaluate a weighted cosine polynomial without one large atom matrix."""

    values = np.empty(len(times))
    chunk_size = 30_000
    for left in range(0, len(times), chunk_size):
        right = min(len(times), left + chunk_size)
        values[left:right] = cosine_atoms(nodes, times[left:right]).T @ weights
    return values


def _infeasible_bracket(
    coordinate_cap: float | None,
    pool_size: int,
    validation_size: int,
    iteration: int,
) -> PositiveAntennaBracket:
    return PositiveAntennaBracket(
        lower=math.inf,
        upper_guard=math.inf,
        feasible=False,
        coordinate_cap=coordinate_cap,
        support_size=0,
        effective_support_size=0.0,
        max_coordinate=math.inf,
        saturated_coordinate_count=0,
        active_indices=(),
        active_probability_weights=(),
        validation_minimum=-math.inf,
        validation_argmin=math.nan,
        simplex_residual=math.inf,
        pair_residual=math.inf,
        cap_violation=math.inf,
        pool_size=pool_size,
        validation_size=validation_size,
        exchange_iterations=iteration,
        curvature=math.inf,
        curvature_guard=math.inf,
        sampled_dual_contact_count=0,
        sampled_dual_contact_times=(),
        sampled_dual_contact_weights=(),
        sampled_dual_weight_sum=0.0,
        sampled_dual_complementarity_residual=math.inf,
    )


def _make_bracket(
    solution: SampledPositiveAntennaSolution,
    nodes: np.ndarray,
    validation: np.ndarray,
    validation_values: np.ndarray,
    validation_step: float,
    pool: np.ndarray,
    pairs: tuple[tuple[int, int], ...],
    coordinate_cap: float | None,
    iteration: int,
) -> PositiveAntennaBracket:
    weights = solution.weights
    curvature = float(np.dot(weights, nodes * nodes))
    curvature_guard = curvature * validation_step**2 / 8.0
    validation_index = int(np.argmin(validation_values))
    support_threshold = max(1e-12, 1e-8 * float(np.max(weights)))
    active = np.flatnonzero(weights > support_threshold)
    dual_threshold = max(
        1e-12,
        1e-9 * float(np.max(solution.dual_weights, initial=0.0)),
    )
    contacts = np.flatnonzero(solution.dual_weights > dual_threshold)
    if coordinate_cap is None:
        saturated_count = 0
        cap_violation = 0.0
    else:
        saturation_tolerance = max(1e-10, 1e-7 * coordinate_cap)
        saturated_count = int(
            np.count_nonzero(weights >= coordinate_cap - saturation_tolerance)
        )
        cap_violation = max(0.0, float(np.max(weights)) - coordinate_cap)

    return PositiveAntennaBracket(
        lower=solution.level,
        upper_guard=-float(validation_values[validation_index]) + curvature_guard,
        feasible=True,
        coordinate_cap=coordinate_cap,
        support_size=int(len(active)),
        effective_support_size=float(1.0 / np.dot(weights, weights)),
        max_coordinate=float(np.max(weights)),
        saturated_coordinate_count=saturated_count,
        active_indices=tuple(int(index) for index in active),
        active_probability_weights=tuple(float(weights[index]) for index in active),
        validation_minimum=float(validation_values[validation_index]),
        validation_argmin=float(validation[validation_index]),
        simplex_residual=abs(float(np.sum(weights)) - 1.0),
        pair_residual=max(
            (abs(float(weights[first] - weights[second])) for first, second in pairs),
            default=0.0,
        ),
        cap_violation=cap_violation,
        pool_size=len(pool),
        validation_size=len(validation),
        exchange_iterations=iteration,
        curvature=curvature,
        curvature_guard=curvature_guard,
        sampled_dual_contact_count=int(len(contacts)),
        sampled_dual_contact_times=tuple(float(pool[index]) for index in contacts),
        sampled_dual_contact_weights=tuple(
            float(solution.dual_weights[index]) for index in contacts
        ),
        sampled_dual_weight_sum=solution.dual_weight_sum,
        sampled_dual_complementarity_residual=solution.complementarity_residual,
    )


def positive_antenna_exchange_family(
    nodes: np.ndarray,
    center: float,
    specifications: Mapping[
        str, tuple[tuple[tuple[int, int], ...], float | None]
    ],
    *,
    initial_points: int = 1_001,
    validation_phase_step: float = 0.25,
    max_iterations: int = 6,
    relative_gap: float = 2e-4,
) -> dict[str, PositiveAntennaBracket]:
    """Run nested antenna LPs on one shared exchange pool."""

    nodes = np.asarray(nodes, dtype=float)
    if not specifications:
        raise ValueError("at least one antenna specification is required")
    if max_iterations < 1:
        raise ValueError("max_iterations must be positive")
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
    brackets: dict[str, PositiveAntennaBracket] = {}

    for iteration in range(1, max_iterations + 1):
        solution_cache: dict[
            tuple[tuple[tuple[int, int], ...], float | None],
            SampledPositiveAntennaSolution | None,
        ] = {}
        value_cache: dict[
            tuple[tuple[tuple[int, int], ...], float | None], np.ndarray
        ] = {}
        additions: list[np.ndarray] = []
        all_gaps_small = True
        brackets = {}

        for name, (pairs, coordinate_cap) in specifications.items():
            key = (pairs, coordinate_cap)
            if key not in solution_cache:
                solution_cache[key] = _solve_sampled_positive_antenna(
                    nodes,
                    pool,
                    pairs,
                    coordinate_cap=coordinate_cap,
                )
            solution = solution_cache[key]
            if solution is None:
                brackets[name] = _infeasible_bracket(
                    coordinate_cap,
                    len(pool),
                    len(validation),
                    iteration,
                )
                continue
            if key not in value_cache:
                value_cache[key] = _polynomial_values(
                    nodes, solution.weights, validation
                )
            values = value_cache[key]
            bracket = _make_bracket(
                solution,
                nodes,
                validation,
                values,
                validation_step,
                pool,
                pairs,
                coordinate_cap,
                iteration,
            )
            brackets[name] = bracket
            gap_tolerance = relative_gap * max(1.0, abs(bracket.lower)) + 1e-9
            if bracket.upper_guard - bracket.lower > gap_tolerance:
                all_gaps_small = False

            minima = local_maxima_indices(-values)
            if len(minima):
                chosen = minima[
                    np.argsort(values[minima])[: min(2 * len(nodes), len(minima))]
                ]
                additions.append(validation[chosen])

        if all_gaps_small or iteration == max_iterations or not additions:
            break
        enlarged = np.unique(np.concatenate([pool, *additions]))
        if len(enlarged) == len(pool):
            break
        pool = enlarged

    return brackets


def compare_positive_antenna_cones(
    nodes: np.ndarray,
    center: float,
    pairs: tuple[tuple[int, int], ...],
    *,
    cap_constant: float = 4.0,
    initial_points: int = 1_001,
    validation_phase_step: float = 0.25,
    max_iterations: int = 6,
    relative_gap: float = 2e-4,
) -> dict[str, PositiveAntennaBracket]:
    """Compare unrestricted, carrier, and capped-carrier positive antennas."""

    if cap_constant <= 0.0 or not math.isfinite(cap_constant):
        raise ValueError("cap_constant must be positive and finite")
    cap = cap_constant * math.log(center) / center
    specifications = {
        "unrestricted_positive": ((), None),
        "carrier_positive": (pairs, None),
        "carrier_capped_positive": (pairs, cap),
    }
    return positive_antenna_exchange_family(
        nodes,
        center,
        specifications,
        initial_points=initial_points,
        validation_phase_step=validation_phase_step,
        max_iterations=max_iterations,
        relative_gap=relative_gap,
    )


def probe_center(
    center: float,
    *,
    shell_width: float = 0.2,
    cap_constant: float = 4.0,
    initial_points: int = 1_001,
    validation_phase_step: float = 0.25,
    max_iterations: int = 6,
    relative_gap: float = 2e-4,
) -> dict[str, object]:
    """Run the three event-free antenna probes on one actual prime shell."""

    primes, signed_nodes = primes_in_shell(center, shell_width)
    if not len(primes):
        raise ValueError("prime shell is empty")
    pairs = canonical_reflected_pairs(signed_nodes, center)
    brackets = compare_positive_antenna_cones(
        np.abs(signed_nodes),
        center,
        pairs,
        cap_constant=cap_constant,
        initial_points=initial_points,
        validation_phase_step=validation_phase_step,
        max_iterations=max_iterations,
        relative_gap=relative_gap,
    )
    serialized: dict[str, object] = {}
    for name, bracket in brackets.items():
        record = asdict(bracket)
        record["active_prime_labels"] = [
            int(primes[index]) for index in bracket.active_indices
        ]
        serialized[name] = record

    unrestricted = brackets["unrestricted_positive"]
    carrier = brackets["carrier_positive"]
    capped = brackets["carrier_capped_positive"]
    ordering_tolerance = 5e-8
    return {
        "center": center,
        "scale": int(math.floor(center)),
        "prime_count": int(len(primes)),
        "pair_count": int(len(pairs)),
        "pairs": [
            {
                "indices": [int(first), int(second)],
                "primes": [int(primes[first]), int(primes[second])],
                "absolute_node_gap": abs(
                    abs(float(signed_nodes[first])) - abs(float(signed_nodes[second]))
                ),
            }
            for first, second in pairs
        ],
        "coordinate_cap": cap_constant * math.log(center) / center,
        "sampled_lower_ordering_holds": bool(
            unrestricted.lower <= carrier.lower + ordering_tolerance
            and carrier.lower <= capped.lower + ordering_tolerance
        ),
        "sampled_carrier_penalty": carrier.lower - unrestricted.lower,
        "sampled_cap_penalty": capped.lower - carrier.lower,
        "antennas": serialized,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "centers",
        nargs="*",
        type=float,
        default=[500.5, 1_000.5, 2_000.5, 4_000.5, 8_000.5],
    )
    parser.add_argument("--shell-width", type=float, default=0.2)
    parser.add_argument("--cap-constant", type=float, default=4.0)
    parser.add_argument("--initial-points", type=int, default=1_001)
    parser.add_argument("--validation-phase-step", type=float, default=0.25)
    parser.add_argument("--max-iterations", type=int, default=6)
    parser.add_argument("--relative-gap", type=float, default=2e-4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    records = [
        probe_center(
            center,
            shell_width=args.shell_width,
            cap_constant=args.cap_constant,
            initial_points=args.initial_points,
            validation_phase_step=args.validation_phase_step,
            max_iterations=args.max_iterations,
            relative_gap=args.relative_gap,
        )
        for center in args.centers
    ]
    artifact = {
        "metadata": {
            "quantity": "event-free delta_+^C(Y)",
            "centers": args.centers,
            "shell_width": args.shell_width,
            "cap_constant": args.cap_constant,
            "coordinate_cap_formula": "C*log(Y)/Y",
            "high_band": "[Y^0.01,Y^(50/33)]",
            "carrier": "canonical opposite-side |abs(u)-abs(u')| <= Y^(-50/33) matching",
            "initial_points": args.initial_points,
            "validation_phase_step": args.validation_phase_step,
            "max_iterations": args.max_iterations,
            "relative_gap": args.relative_gap,
            "shared_exchange_pool": True,
            "floating_point_only": True,
            "interpretation": "finite diagnostic only; no asymptotic extrapolation",
        },
        "records": records,
    }
    payload = json.dumps(artifact, indent=2, sort_keys=True)
    if args.output is None:
        print(payload)
    else:
        args.output.write_text(payload + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
