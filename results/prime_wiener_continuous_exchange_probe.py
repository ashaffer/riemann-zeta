#!/usr/bin/env python3
"""Continuous-frequency Remez/exchange probe for the cosine Wiener gate.

The optimization is the real-cosine continuous relaxation

    inf_lambda sup_{0 <= xi <= B} |b(xi)-sum_j lambda_j cos(xi*u_j)|.

It uses a cutting-plane LP and locates stationary residual extrema by
bracketed root finding.  The output is conjecture-mining evidence only, not
an interval-certified semi-infinite optimization or an asymptotic theorem.
"""

from __future__ import annotations

import argparse
import json
import math

import numpy as np
from scipy.optimize import brentq, linprog


def prime_powers(limit: int) -> list[int]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    values: set[int] = set()
    for p in np.flatnonzero(sieve):
        q = int(p)
        while q <= limit:
            values.add(q)
            if q > limit // int(p):
                break
            q *= int(p)
    return sorted(values)


class ContinuousInstance:
    def __init__(self, Y: float, width: float, alpha: float, bandwidth: float):
        self.Y = Y
        self.width = width
        self.alpha = alpha
        self.bandwidth = bandwidth
        lower, upper = Y * math.exp(-width), Y * math.exp(width)
        self.nodes = np.array(
            [
                math.log(n / Y)
                for n in prime_powers(math.ceil(upper))
                if lower <= n <= upper
            ],
            dtype=float,
        )

    def features(self, xi: np.ndarray) -> np.ndarray:
        return np.cos(np.outer(self.nodes, np.asarray(xi, dtype=float)))

    def feature_derivative(self, xi: np.ndarray) -> np.ndarray:
        return -self.nodes[:, None] * np.sin(
            np.outer(self.nodes, np.asarray(xi, dtype=float))
        )

    def target(self, xi: np.ndarray) -> np.ndarray:
        xi = np.asarray(xi, dtype=float)
        s = self.alpha + 1j * xi
        value = 2.0 * (np.cosh(s * self.width) - 1.0) / (
            self.width * s * s
        )
        return value.real

    def target_derivative(self, xi: np.ndarray) -> np.ndarray:
        xi = np.asarray(xi, dtype=float)
        s = self.alpha + 1j * xi
        fp = (2.0 / self.width) * (
            self.width * np.sinh(self.width * s) / (s * s)
            - 2.0 * (np.cosh(self.width * s) - 1.0) / (s * s * s)
        )
        return -fp.imag

    def residual(self, xi: np.ndarray, lam: np.ndarray) -> np.ndarray:
        return self.target(xi) - self.features(xi).T @ lam

    def residual_derivative(self, xi: np.ndarray, lam: np.ndarray) -> np.ndarray:
        return self.target_derivative(xi) - self.feature_derivative(xi).T @ lam

    def normalized_cosine_gram(self, left: float, right: float) -> np.ndarray:
        """Return the exact normalized Gramian on a frequency interval."""
        if not right > left:
            raise ValueError("Gram interval must have positive length")
        length = right - left

        def normalized_integral(freq: np.ndarray) -> np.ndarray:
            answer = np.empty_like(freq)
            small = np.abs(freq) < 1e-14
            answer[small] = 1.0
            answer[~small] = (
                np.sin(right * freq[~small]) - np.sin(left * freq[~small])
            ) / (length * freq[~small])
            return answer

        difference = self.nodes[:, None] - self.nodes[None, :]
        total = self.nodes[:, None] + self.nodes[None, :]
        return 0.5 * (normalized_integral(difference) + normalized_integral(total))

    def l2_frame_certificate(self, xi0: float, left_fraction: float = 0.5) -> dict:
        """Construct a rigorous (up to floating linear algebra) TV certificate.

        The signed high-band density is proportional to ``a(xi)^T G^-1 a(xi0)``.
        Its total variation is at most the displayed L2 representation cost.
        The analytic target tail bound then gives a feasible annihilating measure.
        """
        left = left_fraction * self.bandwidth
        gram = self.normalized_cosine_gram(left, self.bandwidth)
        eigenvalues, eigenvectors = np.linalg.eigh(gram)
        q = self.features(np.array([xi0]))[:, 0]
        cutoff = max(1e-14, 1e-12 * float(np.max(eigenvalues)))
        retained = eigenvalues > cutoff
        q_coordinates = eigenvectors.T @ q
        unresolved = float(np.linalg.norm(q_coordinates[~retained]))
        q_norm = max(float(np.linalg.norm(q)), 1e-300)
        representable = unresolved <= 1e-9 * q_norm
        if representable:
            representation_cost = math.sqrt(
                max(
                    float(
                        np.sum(
                            q_coordinates[retained] ** 2 / eigenvalues[retained]
                        )
                    ),
                    0.0,
                )
            )
        else:
            representation_cost = None
        tail_bound = 2.0 * (math.cosh(self.alpha * self.width) + 1.0) / (
            self.width * (left * left + self.alpha * self.alpha)
        )
        target0 = float(self.target(np.array([xi0]))[0])
        lower = (
            max(
                0.0,
                (target0 - representation_cost * tail_bound)
                / (1.0 + representation_cost),
            )
            if representation_cost is not None
            else 0.0
        )
        smallest_retained = float(np.min(eigenvalues[retained]))
        return {
            "xi0": float(xi0),
            "gram_min_eigenvalue": float(eigenvalues[0]),
            "gram_max_eigenvalue": float(eigenvalues[-1]),
            "gram_condition_retained": float(eigenvalues[-1] / smallest_retained),
            "gram_numerical_rank": int(np.sum(retained)),
            "carrier_unresolved_null_component": unresolved,
            "l2_representation_cost": representation_cost,
            "analytic_high_band_target_bound": tail_bound,
            "certified_lower_bound_floating_gram": lower,
        }


def unique_sorted(values: np.ndarray, tolerance: float = 1e-12) -> np.ndarray:
    values = np.sort(np.asarray(values, dtype=float))
    if len(values) == 0:
        return values
    kept = [values[0]]
    for value in values[1:]:
        if value - kept[-1] > tolerance * max(1.0, abs(value)):
            kept.append(value)
    return np.array(kept)


def solve_chebyshev(inst: ContinuousInstance, points: np.ndarray):
    V = inst.features(points)
    b = inst.target(points)
    m, d = V.shape
    result = linprog(
        np.r_[np.zeros(m), 1.0],
        A_ub=np.block([[V.T, -np.ones((d, 1))], [-V.T, -np.ones((d, 1))]]),
        b_ub=np.r_[b, -b],
        bounds=[(None, None)] * m + [(0.0, None)],
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        raise RuntimeError(result.message)
    return result.x[:-1], float(result.x[-1])


def stationary_extrema(
    inst: ContinuousInstance, lam: np.ndarray, oversample: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    umax = max(float(np.max(np.abs(inst.nodes))), inst.width, 1e-3)
    # Roughly `oversample` samples between extrema of the fastest cosine.
    count = max(1000, int(math.ceil(inst.bandwidth * umax * oversample / math.pi)))
    grid = np.linspace(0.0, inst.bandwidth, count + 1)
    derivative = inst.residual_derivative(grid, lam)
    roots: list[float] = []
    for i in range(count):
        left, right = derivative[i], derivative[i + 1]
        if left == 0.0:
            roots.append(float(grid[i]))
        elif left * right < 0.0:
            roots.append(
                brentq(
                    lambda x: float(inst.residual_derivative(np.array([x]), lam)[0]),
                    float(grid[i]),
                    float(grid[i + 1]),
                    xtol=1e-11,
                    rtol=1e-13,
                )
            )
    points = unique_sorted(np.r_[0.0, roots, inst.bandwidth])
    residual = inst.residual(points, lam)
    derivative_at_points = inst.residual_derivative(points, lam)
    return points, residual, derivative_at_points


def primal_on_extrema(inst: ContinuousInstance, points: np.ndarray):
    V = inst.features(points)
    b = inst.target(points)
    d = len(points)
    result = linprog(
        np.r_[-b, b],
        A_ub=np.ones((1, 2 * d)),
        b_ub=np.array([1.0]),
        A_eq=np.concatenate([V, -V], axis=1),
        b_eq=np.zeros(len(inst.nodes)),
        bounds=(0.0, None),
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        raise RuntimeError(result.message)
    h = result.x[:d] - result.x[d:]
    return -float(result.fun), h


def solve_continuous(
    Y: float,
    width: float,
    alpha: float,
    bandwidth: float,
    tolerance: float,
    max_iterations: int,
    oversample: float,
    include_support_details: bool = False,
) -> dict:
    inst = ContinuousInstance(Y, width, alpha, bandwidth)
    m = len(inst.nodes)
    initial_count = max(8 * (m + 1), 500)
    constraints = np.linspace(0.0, bandwidth, initial_count)
    history: list[tuple[float, float, int]] = []

    for iteration in range(1, max_iterations + 1):
        lam, level = solve_chebyshev(inst, constraints)
        extrema, residual, derivative = stationary_extrema(inst, lam, oversample)
        absolute = np.abs(residual)
        maximum = float(np.max(absolute))
        history.append((level, maximum, len(constraints)))
        if maximum <= level * (1.0 + tolerance) + 1e-10:
            break
        violation = absolute > level * (1.0 + tolerance / 5.0) + 1e-11
        candidates = extrema[violation]
        if len(candidates) > 4 * (m + 1):
            order = np.argsort(absolute[violation])[-4 * (m + 1) :]
            candidates = candidates[order]
        constraints = unique_sorted(np.r_[constraints, candidates])
    else:
        iteration = max_iterations

    # Recompute the final extrema and obtain the sparse signed design there.
    extrema, residual, derivative = stationary_extrema(inst, lam, oversample)
    primal_value, h = primal_on_extrema(inst, extrema)
    support = np.flatnonzero(np.abs(h) > 1e-8)
    support_xi = extrema[support]
    support_h = h[support]
    support_mass = np.abs(support_h)
    support_mass /= max(float(np.sum(support_mass)), 1e-300)
    support_derivative = derivative[support]
    interior = (support_xi > 1e-8) & (support_xi < bandwidth - 1e-8)
    sorted_support = np.sort(support_xi)
    gaps = np.diff(sorted_support)
    support_sign = np.sign(residual[support])
    ordered_sign = support_sign[np.argsort(support_xi)]
    sign_changes = int(np.sum(ordered_sign[1:] != ordered_sign[:-1])) if len(ordered_sign) > 1 else 0
    absolute_residual = np.abs(residual)
    maximum_residual = float(np.max(absolute_residual))
    near_active = absolute_residual >= (1.0 - 5e-4) * maximum_residual
    near_sign = np.sign(residual[near_active])
    near_order = np.argsort(extrema[near_active])
    near_sign = near_sign[near_order]
    order = np.argsort(support_xi)
    support_xi = support_xi[order]
    support_h = support_h[order]
    support_mass = support_mass[order]
    sorted_support = support_xi
    gaps = np.diff(sorted_support)
    normalized_gaps = gaps * max(len(support) - 1, 1) / max(bandwidth, 1e-300)
    phase_cell = np.mod(support_xi / (2.0 * math.pi * Y), 1.0)
    support_target = inst.target(support_xi)
    objective_terms = support_h * support_target
    dominant_index = int(np.argmax(support_mass)) if len(support_mass) else None
    if len(support) > 1:
        # A Voronoi-cell proxy tests whether the design is approximately a
        # continuous density discretization rather than a phase-locked code.
        cell = np.empty(len(support))
        cell[0] = 0.5 * gaps[0]
        cell[-1] = 0.5 * gaps[-1]
        if len(support) > 2:
            cell[1:-1] = 0.5 * (gaps[:-1] + gaps[1:])
        weight_cell_correlation = float(np.corrcoef(support_mass, cell)[0, 1])
    else:
        weight_cell_correlation = None
    answer = {
        "Y": Y,
        "nodes": m,
        "bandwidth": bandwidth,
        "iterations": iteration,
        "constraints": len(constraints),
        "extrema": len(extrema),
        "E_continuous": maximum_residual,
        "LP_level": level,
        "extrema_primal": primal_value,
        "relative_exchange_gap": (maximum_residual - level) / max(level, 1e-300),
        "support": len(support),
        "support_bound_M_plus_1": m + 1,
        "support_min": float(np.min(support_xi)) if len(support) else None,
        "support_max": float(np.max(support_xi)) if len(support) else None,
        "support_median": float(np.median(support_xi)) if len(support) else None,
        "support_min_gap": float(np.min(gaps)) if len(gaps) else None,
        "support_median_gap": float(np.median(gaps)) if len(gaps) else None,
        "support_normalized_quantiles": (
            [float(x) for x in np.quantile(support_xi / bandwidth, [0, .1, .25, .5, .75, .9, 1])]
            if len(support)
            else []
        ),
        "normalized_gap_quantiles": (
            [float(x) for x in np.quantile(normalized_gaps, [0, .1, .25, .5, .75, .9, 1])]
            if len(normalized_gaps)
            else []
        ),
        "weight_quantiles": (
            [float(x) for x in np.quantile(support_mass, [0, .1, .25, .5, .75, .9, 1])]
            if len(support_mass)
            else []
        ),
        "weight_effective_support": (
            float(1.0 / np.dot(support_mass, support_mass)) if len(support_mass) else 0.0
        ),
        "weight_cell_correlation": weight_cell_correlation,
        "dominant_weight": (
            float(support_mass[dominant_index]) if dominant_index is not None else 0.0
        ),
        "dominant_xi": (
            float(support_xi[dominant_index]) if dominant_index is not None else None
        ),
        "dominant_weight_over_E": (
            float(support_mass[dominant_index] / maximum_residual)
            if dominant_index is not None
            else 0.0
        ),
        "mass_below_xi_50": float(np.sum(support_mass[support_xi <= 50.0])),
        "objective_fraction_below_xi_50": (
            float(np.sum(objective_terms[support_xi <= 50.0]) / primal_value)
            if primal_value != 0.0
            else 0.0
        ),
        "phase_cell_resultant": (
            float(abs(np.mean(np.exp(2j * math.pi * phase_cell))))
            if len(phase_cell)
            else 0.0
        ),
        "support_sign_changes": sign_changes,
        "near_active_extrema": int(np.sum(near_active)),
        "near_active_sign_changes": (
            int(np.sum(near_sign[1:] != near_sign[:-1])) if len(near_sign) > 1 else 0
        ),
        "max_interior_stationarity_error": (
            float(np.max(np.abs(support_derivative[interior])))
            if np.any(interior)
            else 0.0
        ),
        "prime_null_residual": (
            float(np.max(np.abs(inst.features(extrema) @ h))) if m else 0.0
        ),
        "history": history,
        "zero_atom_l2_frame_certificate": inst.l2_frame_certificate(0.0),
    }
    if dominant_index is not None:
        answer["dominant_atom_l2_frame_certificate"] = inst.l2_frame_certificate(
            float(support_xi[dominant_index])
        )
    if include_support_details:
        answer["support_details"] = [
            {
                "xi": float(xi),
                "xi_over_B": float(xi / bandwidth),
                "signed_h": float(coeff),
                "weight": float(weight),
                "target_b": float(target),
                "objective_term_hb": float(coeff * target),
                "phase_cell_xi_over_2piY_mod_1": float(cell),
            }
            for xi, coeff, weight, target, cell in zip(
                support_xi, support_h, support_mass, support_target, phase_cell
            )
        ]
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--Y", nargs="+", type=float, default=[100, 300, 1000])
    parser.add_argument("--width", type=float, default=0.2)
    parser.add_argument("--alpha", type=float, default=0.49)
    parser.add_argument("--bandwidth-ratio", type=float, default=2.0)
    parser.add_argument(
        "--bandwidth-power",
        type=float,
        default=None,
        help="use B=Y^power (overrides --bandwidth-ratio and --full-aperture)",
    )
    parser.add_argument("--full-aperture", action="store_true")
    parser.add_argument("--tolerance", type=float, default=2e-6)
    parser.add_argument("--max-iterations", type=int, default=12)
    parser.add_argument("--oversample", type=float, default=10.0)
    parser.add_argument(
        "--show-support",
        action="store_true",
        help="include every support atom, signed coefficient, and design weight",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="print strict JSON rather than a Python dictionary",
    )
    args = parser.parse_args()
    for Y in args.Y:
        if args.bandwidth_power is not None:
            bandwidth = Y ** args.bandwidth_power
        elif args.full_aperture:
            bandwidth = Y ** (50.0 / 33.0)
        else:
            bandwidth = args.bandwidth_ratio * Y
        answer = solve_continuous(
            Y,
            args.width,
            args.alpha,
            bandwidth,
            args.tolerance,
            args.max_iterations,
            args.oversample,
            args.show_support,
        )
        print(json.dumps(answer, sort_keys=True) if args.json else answer)


if __name__ == "__main__":
    main()
