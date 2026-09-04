"""Finite-scale diagnostics for the actual-node transverse-return depth.

For actual prime-power shell nodes ``a(t)=(cos(t*u_j))`` and a calibrated
residual ``v=a(t0)+D*1``, this module brackets

    s_v = sup {s >= 0 : -s*v in conv(a(H))}.

The lower endpoint comes from a finite-pool primal probability.  The upper
guard comes from a dual polynomial, a continuum validation grid, and exact
first/second derivative guards.  LP and cosine arithmetic remain floating
point; outputs are diagnostics, not interval certificates.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math

import numpy as np
from scipy.optimize import linprog

from qp_radialization_lab import (
    cosine_atoms,
    directional_interval_scan,
    local_maxima_indices,
    prime_powers_in_shell,
    primes_in_shell,
    refine_dual_maximum,
    uniform_grid,
)


@dataclass(frozen=True)
class FiniteTransversePrimal:
    depth: float
    weights: np.ndarray
    equality_residual: float
    success: bool


@dataclass(frozen=True)
class FiniteTransverseDual:
    level: float
    coefficients: np.ndarray
    equality_residual: float
    inequality_violation: float
    success: bool


def solve_finite_transverse_primal(
    nodes: np.ndarray, times: np.ndarray, residual: np.ndarray
) -> FiniteTransversePrimal:
    """Maximize ``s`` with ``sum w_t a(t)=-s*residual`` on a finite pool."""

    atoms = cosine_atoms(nodes, times)
    coordinates, count = atoms.shape
    objective = np.r_[np.zeros(count), -1.0]
    equality = np.zeros((coordinates + 1, count + 1))
    equality[:coordinates, :count] = atoms
    equality[:coordinates, -1] = residual
    equality[-1, :count] = 1.0
    rhs = np.r_[np.zeros(coordinates), 1.0]
    result = linprog(
        objective,
        A_eq=equality,
        b_eq=rhs,
        bounds=[(0.0, None)] * count + [(0.0, None)],
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        return FiniteTransversePrimal(0.0, np.zeros(count), math.inf, False)
    residual_error = float(np.max(np.abs(equality @ result.x - rhs)))
    return FiniteTransversePrimal(
        float(result.x[-1]), result.x[:-1], residual_error, True
    )


def solve_finite_transverse_dual(
    nodes: np.ndarray,
    times: np.ndarray,
    residual: np.ndarray,
    *,
    coefficient_bound: float | None = None,
) -> FiniteTransverseDual:
    """Solve ``inf_(y.residual=-1) max_pool y.a(t)``."""

    atoms = cosine_atoms(nodes, times)
    coordinates, count = atoms.shape
    objective = np.r_[np.zeros(coordinates), 1.0]
    inequalities = np.c_[atoms.T, -np.ones(count)]
    equality = np.zeros((1, coordinates + 1))
    equality[0, :coordinates] = residual
    coefficient_bounds = (
        [(None, None)] * coordinates
        if coefficient_bound is None
        else [(-coefficient_bound, coefficient_bound)] * coordinates
    )
    result = linprog(
        objective,
        A_ub=inequalities,
        b_ub=np.zeros(count),
        A_eq=equality,
        b_eq=np.array([-1.0]),
        bounds=coefficient_bounds + [(None, None)],
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        return FiniteTransverseDual(math.inf, np.zeros(coordinates), math.inf, math.inf, False)
    coefficients = result.x[:-1]
    level = float(result.x[-1])
    equality_residual = abs(float(np.dot(coefficients, residual)) + 1.0)
    inequality_violation = max(
        0.0, float(np.max(atoms.T @ coefficients - level))
    )
    return FiniteTransverseDual(
        level,
        coefficients,
        equality_residual,
        inequality_violation,
        True,
    )


@dataclass(frozen=True)
class TransverseBracket:
    lower: float
    upper_guard: float
    finite_dual_level: float
    validation_maximum: float
    validation_argmax: float
    dual_lipschitz: float
    dual_curvature: float
    validation_step: float
    pool_size: int
    support_size: int
    primal_residual: float
    dual_equality_residual: float
    dual_inequality_violation: float
    dual_max_abs_coefficient: float
    dual_coefficient_bound: float
    dual_bound_active: bool
    exchange_iterations: int
    floating_point_only: bool = True


def transverse_exchange(
    nodes: np.ndarray,
    residual: np.ndarray,
    left: float,
    right: float,
    *,
    initial_factor: int = 8,
    validation_phase_step: float = 0.08,
    max_iterations: int = 8,
    relative_gap: float = 2e-3,
    seed_times: np.ndarray | None = None,
    dual_coefficient_bound: float = 1.0e4,
) -> TransverseBracket:
    """Exchange bracket for the continuum transverse-return depth."""

    nodes = np.asarray(nodes, dtype=float)
    residual = np.asarray(residual, dtype=float)
    if residual.shape != nodes.shape:
        raise ValueError("residual and nodes must have the same shape")
    maximum_node = float(np.max(nodes))
    initial_count = max(64, initial_factor * (len(nodes) + 1))
    pool = np.linspace(left, right, initial_count)
    if seed_times is not None:
        seeds = np.asarray(seed_times, dtype=float)
        seeds = seeds[(seeds >= left) & (seeds <= right)]
        pool = np.unique(np.r_[pool, seeds])
    validation = uniform_grid(left, right, maximum_node, validation_phase_step)
    step = float(validation[1] - validation[0])
    primal = FiniteTransversePrimal(0.0, np.zeros(len(pool)), math.inf, False)
    dual = FiniteTransverseDual(math.inf, np.zeros(len(nodes)), math.inf, math.inf, False)
    refined_max = math.inf
    argmax = left
    upper = math.inf

    for iteration in range(1, max_iterations + 1):
        dual = solve_finite_transverse_dual(
            nodes,
            pool,
            residual,
            coefficient_bound=dual_coefficient_bound,
        )
        primal = solve_finite_transverse_primal(nodes, pool, residual)
        if not dual.success:
            break
        values = cosine_atoms(nodes, validation).T @ dual.coefficients
        refined_max, argmax = refine_dual_maximum(
            nodes, dual.coefficients, validation, values
        )
        lipschitz = float(np.dot(np.abs(dual.coefficients), nodes))
        curvature = float(np.dot(np.abs(dual.coefficients), nodes * nodes))
        first_order_guard = float(np.max(values)) + 0.5 * lipschitz * step
        second_order_guard = float(np.max(values)) + curvature * step * step / 8.0
        upper = max(refined_max, min(first_order_guard, second_order_guard))
        if primal.success:
            gap = upper - primal.depth
            scale = max(abs(primal.depth), 1e-12)
            if gap <= relative_gap * scale + 1e-10:
                break
        maxima = local_maxima_indices(values)
        strongest = maxima[
            np.argsort(values[maxima])[-min(2 * len(nodes), len(maxima)) :]
        ]
        pool = np.unique(np.r_[pool, argmax, validation[strongest]])

    lipschitz = float(np.dot(np.abs(dual.coefficients), nodes)) if dual.success else math.inf
    curvature = (
        float(np.dot(np.abs(dual.coefficients), nodes * nodes))
        if dual.success
        else math.inf
    )
    support_size = int(np.sum(primal.weights > 1e-8)) if primal.success else 0
    max_abs_coefficient = (
        float(np.max(np.abs(dual.coefficients))) if dual.success else math.inf
    )
    return TransverseBracket(
        lower=float(primal.depth) if primal.success else 0.0,
        upper_guard=float(upper),
        finite_dual_level=float(dual.level),
        validation_maximum=float(refined_max),
        validation_argmax=float(argmax),
        dual_lipschitz=lipschitz,
        dual_curvature=curvature,
        validation_step=step,
        pool_size=len(pool),
        support_size=support_size,
        primal_residual=float(primal.equality_residual),
        dual_equality_residual=float(dual.equality_residual),
        dual_inequality_violation=float(dual.inequality_violation),
        dual_max_abs_coefficient=max_abs_coefficient,
        dual_coefficient_bound=dual_coefficient_bound,
        dual_bound_active=max_abs_coefficient >= 0.999 * dual_coefficient_bound,
        exchange_iterations=iteration,
    )


def first_odd_resonance(node: float, left: float, right: float) -> float:
    """First ``(2k+1)pi/node`` in ``[left,right]``."""

    index = max(0, math.ceil((left * node / math.pi - 1.0) / 2.0))
    time = (2 * index + 1) * math.pi / node
    if time > right:
        raise ValueError("node has no odd resonance in the requested band")
    return time


def calibrated_residual(nodes: np.ndarray, time: float, depth: float) -> np.ndarray:
    if not 0.0 < depth <= 1.0:
        raise ValueError("calibrated depth must lie in (0,1]")
    return np.cos(nodes * time) + depth


def run_transverse_instance(
    N: int,
    *,
    center_offset: float = 0.5,
    width: float = 0.2,
    turan_aperture: float = 1.5,
    full_lower_exponent: float = 0.01,
    full_aperture: float = 50.0 / 33.0,
    phase_step: float = 0.08,
    max_exchange_iterations: int = 8,
) -> dict:
    """Run singleton and broad-interval transverse diagnostics."""

    Y = N + center_offset
    powers, nodes = prime_powers_in_shell(Y, width)
    primes, prime_logs = primes_in_shell(Y, width)
    high_left = N**0.5
    high_right = N**turan_aperture
    full_left = Y**full_lower_exponent
    full_right = Y**full_aperture

    # Prefer the shell prime closest to the center among those having an odd
    # resonance in the finite Turan band (tiny diagnostic scales need not
    # admit a resonance for the very closest prime).
    eligible: list[tuple[float, int, float]] = []
    for prime, signed_log in zip(primes, prime_logs, strict=True):
        power_index = int(np.flatnonzero(powers == int(prime))[0])
        node = float(nodes[power_index])
        try:
            resonance = first_odd_resonance(node, high_left, high_right)
        except ValueError:
            continue
        eligible.append((abs(float(signed_log)), int(prime), resonance))
    if not eligible:
        raise ValueError("no shell prime has an odd resonance in the Turan band")
    _, singleton_prime, singleton_time = min(eligible)
    singleton_residual = calibrated_residual(nodes, singleton_time, 1.0)
    singleton = transverse_exchange(
        nodes,
        singleton_residual,
        full_left,
        full_right,
        validation_phase_step=phase_step,
        max_iterations=max_exchange_iterations,
        seed_times=np.array([singleton_time]),
    )

    broad_direction = directional_interval_scan(
        primes,
        prime_logs,
        float(N),
        high_left,
        high_right,
        minimum_count=1,
        phase_step=phase_step,
    )
    mask = (primes >= broad_direction.left_prime) & (primes <= broad_direction.right_prime)
    broad_depth = -float(np.mean(np.cos(prime_logs[mask] * broad_direction.time)))
    broad_residual = calibrated_residual(nodes, broad_direction.time, broad_depth)
    broad = transverse_exchange(
        nodes,
        broad_residual,
        full_left,
        full_right,
        validation_phase_step=phase_step,
        max_iterations=max_exchange_iterations,
        seed_times=np.array([broad_direction.time]),
    )

    return {
        "N": N,
        "Y": Y,
        "shell_width": width,
        "prime_power_count": len(powers),
        "prime_count": len(primes),
        "one_over_dimension": 1.0 / len(nodes),
        "singleton": {
            "prime": singleton_prime,
            "time": singleton_time,
            "depth": 1.0,
            "bracket": asdict(singleton),
        },
        "broad_interval": {
            "left_prime": broad_direction.left_prime,
            "right_prime": broad_direction.right_prime,
            "prime_count": broad_direction.prime_count,
            "time": broad_direction.time,
            "probability_depth": broad_depth,
            "mass_depth": broad_direction.lower,
            "bracket": asdict(broad),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, nargs="+", default=[70, 200, 600, 1000])
    parser.add_argument("--phase-step", type=float, default=0.08)
    parser.add_argument("--iterations", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    results = [
        run_transverse_instance(
            N,
            phase_step=args.phase_step,
            max_exchange_iterations=args.iterations,
        )
        for N in args.N
    ]
    if args.json:
        print(json.dumps(results, indent=2))
        return
    for result in results:
        singleton = result["singleton"]["bracket"]
        broad = result["broad_interval"]
        broad_bracket = broad["bracket"]
        print(
            f"N={result['N']} M={result['prime_power_count']} 1/M={result['one_over_dimension']:.6g} "
            f"singleton=[{singleton['lower']:.6g},{singleton['upper_guard']:.6g}] "
            f"broad_D={broad['probability_depth']:.6g} "
            f"broad=[{broad_bracket['lower']:.6g},{broad_bracket['upper_guard']:.6g}]"
        )


if __name__ == "__main__":
    main()
