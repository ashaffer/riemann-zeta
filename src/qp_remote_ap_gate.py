#!/usr/bin/env python3
"""Exact remote arithmetic-progression interpolants for the QP gate.

For actual nodes ``u_j`` and a step ``tau`` put

    R_tau(u) = product_j (cos(tau*u) - cos(tau*u_j)).

Writing ``R_tau(u)=sum_k r_k cos(k*tau*u)``, if ``r_0 != 0`` then

    F_tau(u) = 1 - R_tau(u)/r_0

has no zero-frequency term and satisfies ``F_tau(u_j)=1``.  Thus its
nonconstant Chebyshev coefficients are the weights of an exact signed
representation on the AP ``tau, ..., M*tau``.  The total variation is
``sum_{k>=1}|r_k/r_0|``.

The construction is exact algebraically.  Floating calculations in this
module are diagnostics for its directional cost, not interval certificates.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import numpy as np
from numpy.polynomial.chebyshev import chebmul, chebval
from scipy.optimize import minimize_scalar

from qp_nodal_product_gate import FULL_APERTURE_EXPONENT, actual_nodes


KAPPA_PROMOTE = 0.0180303234
LOW_FREQUENCY_EXPONENT = 0.01
PACKET_COUNT_EXPONENT_MULTIPLIER = 2.0


def effective_cosine_nodes(nodes: np.ndarray, digits: int = 14) -> np.ndarray:
    """Quotient duplicate cosine rows by their absolute node.

    Exact duplicates can occur only when two shell integers multiply to
    ``Y^2``.  The rounded quotient is used only by the floating diagnostic;
    the theorem is stated after the exact ``|u|`` quotient.
    """
    absolute = np.abs(np.asarray(nodes, dtype=float))
    return np.unique(np.round(absolute, digits))


def normalized_chebyshev_nodal_coefficients(
    nodes: np.ndarray, tau: float
) -> np.ndarray:
    """Return scaled Chebyshev coefficients of the AP nodal product.

    A common positive scale is removed after each multiplication.  It has no
    effect on coefficient ratios and avoids overflow/underflow.
    """
    coefficients = np.asarray([1.0])
    for root in np.cos(tau * np.asarray(nodes, dtype=float)):
        coefficients = chebmul(coefficients, np.asarray([-root, 1.0]))
        scale = float(np.max(np.abs(coefficients)))
        if not math.isfinite(scale) or scale == 0.0:
            raise ArithmeticError("Chebyshev nodal product lost finite scale")
        coefficients /= scale
    return coefficients


def ap_directional_cost(nodes: np.ndarray, tau: float) -> float:
    """TV cost of the exact zero-constant AP interpolant."""
    if tau <= 0.0:
        raise ValueError("tau must be positive")
    coefficients = normalized_chebyshev_nodal_coefficients(nodes, tau)
    constant = abs(float(coefficients[0]))
    if constant == 0.0:
        return math.inf
    return float(np.sum(np.abs(coefficients[1:])) / constant)


def ap_weights(nodes: np.ndarray, tau: float) -> np.ndarray:
    """Weights ``c_k`` for ``sum_{k=1}^M c_k cos(k*tau*u_j)=1``."""
    coefficients = normalized_chebyshev_nodal_coefficients(nodes, tau)
    if coefficients[0] == 0.0:
        raise ValueError("the nodal product has zero constant Chebyshev term")
    return -coefficients[1:] / coefficients[0]


def positive_antipode_depth(weights: np.ndarray, tolerance: float = 1e-10) -> float:
    """Depth ``r`` when AP weights encode a positive ``-r*1`` measure.

    If ``c`` represents ``1`` and every ``c_k<=0``, then
    ``w_k=-r*c_k`` is a probability precisely for
    ``r=-1/sum(c_k)``.  Otherwise this AP support has no positive antipode
    through its unique square representation.
    """
    values = np.asarray(weights, dtype=float)
    total = float(np.sum(values))
    if np.max(values) > tolerance or total >= 0.0:
        return 0.0
    return -1.0 / total


def harmonic_number(indices: np.ndarray | list[int]) -> float:
    """Sum ``1/k`` over positive AP indices."""
    values = np.asarray(indices, dtype=int)
    if values.ndim != 1 or len(values) == 0 or np.any(values <= 0):
        raise ValueError("indices must be a nonempty list of positive integers")
    return float(np.sum(1.0 / values))


def dilation_shadow_measure_bound(
    *, packet_count: float, packet_radius: float, indices: np.ndarray | list[int]
) -> float:
    """Union-bound measure of AP steps hitting fixed exceptional packets.

    An interval of radius ``rho`` in the physical frequency variable pulls
    back under ``tau -> k*tau`` to length ``2*rho/k``.
    """
    if packet_count < 0.0 or packet_radius < 0.0:
        raise ValueError("packet count and radius must be nonnegative")
    return 2.0 * packet_count * packet_radius * harmonic_number(indices)


def required_peak(node_count: int, coefficient_tv: float) -> float:
    """Scalar peak forced by a TV-bounded representation of ``1``."""
    if node_count <= 0 or coefficient_tv <= 0.0:
        raise ValueError("node count and TV must be positive")
    return node_count / coefficient_tv


def harmonic_ap_weights(
    nodes: np.ndarray, tau: float, indices: np.ndarray | list[int]
) -> np.ndarray:
    """Solve the exact square cosine system on arbitrary AP harmonics.

    This is the numerical realization of the carrier-replacement Cramer
    ratios.  It is accepted only as a floating diagnostic; callers must
    inspect the residual.
    """
    values = np.asarray(nodes, dtype=float)
    harmonics = np.asarray(indices, dtype=int)
    if len(harmonics) != len(values) or np.any(harmonics <= 0):
        raise ValueError("one positive harmonic index is required per node")
    matrix = np.cos(np.outer(values, tau * harmonics))
    return np.linalg.solve(matrix, np.ones(len(values)))


def harmonic_ap_residual(
    nodes: np.ndarray,
    tau: float,
    indices: np.ndarray | list[int],
    weights: np.ndarray | None = None,
) -> float:
    """Maximum residual for an arbitrary square harmonic AP solution."""
    values = np.asarray(nodes, dtype=float)
    harmonics = np.asarray(indices, dtype=int)
    if weights is None:
        weights = harmonic_ap_weights(values, tau, harmonics)
    matrix = np.cos(np.outer(values, tau * harmonics))
    return float(np.max(np.abs(matrix @ np.asarray(weights) - 1.0)))


@dataclass(frozen=True)
class RemoteBlockDiagnostic:
    y: float
    node_count: int
    first_harmonic: int
    last_harmonic: int
    tau_min: float
    tau_max: float
    best_tau: float
    first_frequency: float
    last_frequency: float
    cost: float
    cost_exponent: float
    promotion_budget: float
    beats_promotion_budget: bool
    best_positive_tau: float | None
    best_positive_depth: float
    best_positive_cost: float
    positive_beats_promotion_budget: bool
    interpolation_residual: float


def scan_all_remote_harmonic_block(
    y: float,
    width: float,
    *,
    samples: int = 2000,
    refinements: int = 16,
    tau_min: float = 1.0,
    residual_tolerance: float = 1e-8,
) -> RemoteBlockDiagnostic:
    """Scan ``{M*tau,...,(2M-1)*tau}``, whose every atom is remote."""
    nodes = effective_cosine_nodes(actual_nodes(y, width))
    node_count = len(nodes)
    if node_count == 0:
        raise ValueError("no actual prime-power nodes in the shell")
    indices = np.arange(node_count, 2 * node_count, dtype=int)
    tau_max = y**FULL_APERTURE_EXPONENT / (2.0 * node_count)
    if tau_max <= tau_min:
        raise ValueError("the all-remote AP block has no legal step interval")

    def solution(value: float) -> tuple[float, float, np.ndarray | None]:
        try:
            weights = harmonic_ap_weights(nodes, value, indices)
        except np.linalg.LinAlgError:
            return math.inf, math.inf, None
        residual = harmonic_ap_residual(nodes, value, indices, weights)
        cost = float(np.sum(np.abs(weights)))
        if not math.isfinite(cost) or residual > residual_tolerance:
            return math.inf, residual, None
        return cost, residual, weights

    grid = np.linspace(tau_min, tau_max, samples)
    costs = np.full(len(grid), math.inf)
    positive_depths = np.zeros(len(grid))
    for position, tau_value in enumerate(grid):
        cost, _, weights = solution(float(tau_value))
        costs[position] = cost
        if weights is not None:
            positive_depths[position] = positive_antipode_depth(weights)
    finite = np.flatnonzero(np.isfinite(costs))
    if len(finite) == 0:
        raise ArithmeticError("no stable all-remote AP system was sampled")
    order = finite[np.argsort(costs[finite])]
    candidates = [(float(costs[order[0]]), float(grid[order[0]]))]
    spacing = float(grid[1] - grid[0]) if len(grid) > 1 else tau_max - tau_min
    for index in order[:refinements]:
        left = max(tau_min, float(grid[index]) - spacing)
        right = min(tau_max, float(grid[index]) + spacing)
        if right <= left:
            continue

        def objective(value: float) -> float:
            cost, _, _ = solution(float(value))
            return math.log(cost)

        result = minimize_scalar(
            objective,
            bounds=(left, right),
            method="bounded",
            options={"xatol": max(1e-12, spacing * 1e-10)},
        )
        if math.isfinite(result.fun):
            candidates.append((math.exp(float(result.fun)), float(result.x)))
    cost, tau = min(candidates)
    final_cost, residual, _ = solution(tau)
    if not math.isclose(cost, final_cost, rel_tol=1e-9, abs_tol=1e-12):
        raise ArithmeticError("remote AP refinement did not replay")

    positive_indices = np.flatnonzero(positive_depths > 0.0)
    if len(positive_indices):
        positive_index = int(
            positive_indices[np.argmax(positive_depths[positive_indices])]
        )
        positive_depth = float(positive_depths[positive_index])
        positive_tau: float | None = float(grid[positive_index])
        positive_cost = 1.0 / positive_depth
    else:
        positive_depth = 0.0
        positive_tau = None
        positive_cost = math.inf
    budget = y**KAPPA_PROMOTE
    return RemoteBlockDiagnostic(
        y=y,
        node_count=node_count,
        first_harmonic=int(indices[0]),
        last_harmonic=int(indices[-1]),
        tau_min=tau_min,
        tau_max=tau_max,
        best_tau=tau,
        first_frequency=node_count * tau,
        last_frequency=(2 * node_count - 1) * tau,
        cost=cost,
        cost_exponent=math.log(cost) / math.log(y),
        promotion_budget=budget,
        beats_promotion_budget=cost < budget,
        best_positive_tau=positive_tau,
        best_positive_depth=positive_depth,
        best_positive_cost=positive_cost,
        positive_beats_promotion_budget=positive_cost < budget,
        interpolation_residual=residual,
    )


def ap_shadow_exponents(kappa: float = KAPPA_PROMOTE) -> dict[str, float]:
    """Promotion-budget exponents for the full ``M``-harmonic AP family."""
    step_interval = FULL_APERTURE_EXPONENT - 1.0
    shadow = PACKET_COUNT_EXPONENT_MULTIPLIER * kappa
    return {
        "packet_shadow": shadow,
        "legal_step_interval": step_interval,
        "relative_density": shadow - step_interval,
    }


def interpolation_residual(nodes: np.ndarray, tau: float) -> float:
    """Maximum floating residual of the exact AP interpolation identity."""
    weights = ap_weights(nodes, tau)
    harmonics = np.arange(1, len(weights) + 1, dtype=float)
    values = np.cos(np.outer(np.asarray(nodes), tau * harmonics)) @ weights
    return float(np.max(np.abs(values - 1.0)))


def stable_ap_cost(
    nodes: np.ndarray, tau: float, residual_tolerance: float = 1e-9
) -> float:
    """Return the AP cost only when its floating identity is trustworthy."""
    cost = ap_directional_cost(nodes, tau)
    if not math.isfinite(cost):
        return math.inf
    residual = interpolation_residual(nodes, tau)
    if not math.isfinite(residual) or residual > residual_tolerance:
        return math.inf
    return cost


def nodal_polynomial_residual(nodes: np.ndarray, tau: float) -> float:
    """Scale-free check that the Chebyshev nodal product vanishes."""
    coefficients = normalized_chebyshev_nodal_coefficients(nodes, tau)
    roots = np.cos(tau * np.asarray(nodes))
    numerator = np.max(np.abs(chebval(roots, coefficients)))
    denominator = max(1.0, float(np.sum(np.abs(coefficients))))
    return float(numerator / denominator)


@dataclass(frozen=True)
class APDiagnostic:
    y: float
    node_count: int
    tau_min: float
    tau_max: float
    best_tau: float
    top_frequency: float
    top_frequency_over_nodes: float
    cost: float
    cost_exponent: float
    promotion_budget: float
    beats_promotion_budget: bool
    positive_steps_sampled: int
    best_positive_tau: float | None
    best_positive_depth: float
    best_positive_cost: float
    positive_beats_promotion_budget: bool
    interpolation_residual: float
    nodal_polynomial_residual: float


def scan_ap_steps(
    y: float,
    width: float,
    *,
    samples: int = 4000,
    refinements: int = 24,
) -> APDiagnostic:
    """Grid and locally refine AP steps whose full support is legal."""
    nodes = effective_cosine_nodes(actual_nodes(y, width))
    if len(nodes) == 0:
        raise ValueError("no actual prime-power nodes in the shell")
    tau_min = y**LOW_FREQUENCY_EXPONENT
    tau_max = y**FULL_APERTURE_EXPONENT / len(nodes)
    if tau_max <= tau_min:
        raise ValueError("no legal M-harmonic AP at this scale")
    grid = np.linspace(tau_min, tau_max, samples)
    costs_list: list[float] = []
    positive_depths_list: list[float] = []
    for tau_value in grid:
        tau_float = float(tau_value)
        cost_value = stable_ap_cost(nodes, tau_float)
        costs_list.append(cost_value)
        if math.isfinite(cost_value):
            positive_depths_list.append(
                positive_antipode_depth(ap_weights(nodes, tau_float))
            )
        else:
            positive_depths_list.append(0.0)
    costs = np.asarray(costs_list)
    positive_depths = np.asarray(positive_depths_list)
    finite = np.flatnonzero(np.isfinite(costs))
    if len(finite) == 0:
        raise ArithmeticError("all sampled AP costs are infinite")
    order = finite[np.argsort(costs[finite])]
    candidates: list[tuple[float, float]] = [
        (float(costs[order[0]]), float(grid[order[0]]))
    ]
    spacing = float(grid[1] - grid[0]) if len(grid) > 1 else tau_max - tau_min
    for index in order[:refinements]:
        left = max(tau_min, float(grid[index]) - spacing)
        right = min(tau_max, float(grid[index]) + spacing)
        if right <= left:
            continue
        result = minimize_scalar(
            lambda value: math.log(stable_ap_cost(nodes, float(value))),
            bounds=(left, right),
            method="bounded",
            options={"xatol": max(1e-12, spacing * 1e-10)},
        )
        candidates.append((math.exp(float(result.fun)), float(result.x)))
    cost, tau = min(candidates)
    positive_indices = np.flatnonzero(positive_depths > 0.0)
    if len(positive_indices):
        best_positive_index = int(
            positive_indices[np.argmax(positive_depths[positive_indices])]
        )
        best_positive_depth = float(positive_depths[best_positive_index])
        best_positive_tau: float | None = float(grid[best_positive_index])
        best_positive_cost = 1.0 / best_positive_depth
    else:
        best_positive_depth = 0.0
        best_positive_tau = None
        best_positive_cost = math.inf
    top = len(nodes) * tau
    budget = y**KAPPA_PROMOTE
    return APDiagnostic(
        y=y,
        node_count=len(nodes),
        tau_min=tau_min,
        tau_max=tau_max,
        best_tau=tau,
        top_frequency=top,
        top_frequency_over_nodes=top / len(nodes),
        cost=cost,
        cost_exponent=math.log(cost) / math.log(y),
        promotion_budget=budget,
        beats_promotion_budget=cost < budget,
        positive_steps_sampled=len(positive_indices),
        best_positive_tau=best_positive_tau,
        best_positive_depth=best_positive_depth,
        best_positive_cost=best_positive_cost,
        positive_beats_promotion_budget=best_positive_cost < budget,
        interpolation_residual=interpolation_residual(nodes, tau),
        nodal_polynomial_residual=nodal_polynomial_residual(nodes, tau),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--Y", nargs="+", type=float, default=[100, 300, 1000])
    parser.add_argument("--width", type=float, default=0.2)
    parser.add_argument("--samples", type=int, default=4000)
    parser.add_argument("--refinements", type=int, default=24)
    parser.add_argument("--remote-block", action="store_true")
    args = parser.parse_args()
    diagnostics = [
        scan_ap_steps(
            y,
            args.width,
            samples=args.samples,
            refinements=args.refinements,
        )
        for y in args.Y
    ]
    payload = {
        "schema": "qp-remote-ap-gate-v1",
        "polarity": (
            "an upper bound on AP cost promotes only when it is below "
            "Y^(kappa_promote-eta); failure of this family does not kill QP"
        ),
        "kappa_promote": KAPPA_PROMOTE,
        "dilation_shadow_exponents": ap_shadow_exponents(),
        "diagnostics": [asdict(item) for item in diagnostics],
    }
    if args.remote_block:
        payload["all_remote_block_diagnostics"] = [
            asdict(
                scan_all_remote_harmonic_block(
                    y,
                    args.width,
                    samples=args.samples,
                    refinements=args.refinements,
                )
            )
            for y in args.Y
        ]
    print(
        json.dumps(
            payload,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
