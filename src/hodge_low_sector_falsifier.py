"""One-factor-at-a-time falsifier for the activation-5 low Hodge sector.

This is deliberately a finite Galerkin diagnostic, not a continuum
certificate.  It perturbs the four numerical choices that could manufacture
the observed positive two-mode determinant independently:

* the old hat degree;
* the collar hat degree (reported also through its mesh ratio);
* the Fourier cutoff in the archimedean integral;
* the Simpson interval density.

For each section, old modes ``j >= 4`` are eliminated with their *exact*
ordinary Schur and Hodge costs.  On the odd collar parity sector, the script
then forms the normalized Gram matrix of the two odd modes among the first
four old Weil eigenmodes,

    G_ij = <x_i, D_high^-1 x_j> / sqrt(lambda_i lambda_j),

where ``D_high`` is the collar metric left after the high elimination.  The
sign of ``det(I-G)`` is the fail-fast two-mode cross test.  The exact odd
contraction including the two remaining Hodge rows is reported separately.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass

import mpmath as mp
import numpy as np
from scipy.linalg import eigvalsh as generalized_eigvalsh

from hodge_event_scan import default_cutoff, event_catalog, matched_collar_degree
from hodge_sector_scan import event_blocks


def _symmetric(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.T) / 2


def _largest_ratio(numerator: np.ndarray, denominator: np.ndarray) -> float:
    """Largest generalized eigenvalue of a symmetric matrix pair."""
    values = generalized_eigvalsh(_symmetric(numerator), _symmetric(denominator))
    return float(values[-1])


@dataclass(frozen=True)
class Case:
    family: str
    old_degree: int
    mesh_ratio: float
    collar_degree: int
    cutoff_scale: float
    cutoff: float
    interval_density: float


FIELDS = [
    "family", "old_degree", "collar_degree", "mesh_ratio",
    "cutoff_scale", "cutoff", "interval_density", "intervals",
    "old_lambda1", "old_lambda2", "old_lambda3", "old_lambda4",
    "old_lambda5", "lambda5_minus_lambda4", "lambda5_over_lambda4",
    "odd_index_1", "odd_index_2", "odd_parity_error",
    "g11", "g12", "g22", "g_min", "g_max", "det_i_minus_g",
    "first_pivot", "exact_odd_contraction", "odd_hodge_contraction",
    "even_g11", "even_g12", "even_g22", "even_g_min", "even_g_max",
    "even_det_i_minus_g", "even_first_pivot",
    "exact_even_contraction", "even_hodge_contraction",
    "low4_contraction", "high_budget_fraction", "residual_collar_min",
    "residual_odd_min", "raw_collar_min", "total_row_ratio",
    "total_even_ratio", "total_odd_ratio", "total_surplus_min",
    "mu3_high_start", "mu3_high_count", "mu3_medium_count",
    "mu3_high_budget_fraction", "mu3_residual_min",
    "mu3_medium_contraction", "mu3_after_medium_min",
    "old_reflection_commutator",
    "collar_reflection_commutator", "status",
]


def evaluate(old_support: float, new_support: float, case: Case,
             chunk: int) -> dict[str, object]:
    intervals = int(round(case.interval_density * case.cutoff))
    if intervals % 2:
        intervals += 1
    row: dict[str, object] = {
        "family": case.family,
        "old_degree": case.old_degree,
        "collar_degree": case.collar_degree,
        "mesh_ratio": case.mesh_ratio,
        "cutoff_scale": case.cutoff_scale,
        "cutoff": case.cutoff,
        "interval_density": case.interval_density,
        "intervals": intervals,
        "status": "ok",
    }
    try:
        A, X, C, T, _S, old_reflection, collar_reflection, _old_d, _event_d = (
            event_blocks(
                old_support, new_support, case.old_degree,
                case.collar_degree, case.cutoff, intervals, chunk))
        A = _symmetric(A)
        C = _symmetric(C)
        old_reflection = _symmetric(old_reflection)
        collar_reflection = _symmetric(collar_reflection)
        a_values, old_vectors = np.linalg.eigh(A)
        if len(a_values) < 5:
            raise ValueError("old relative sector has fewer than five modes")
        if a_values[0] <= 0:
            raise ValueError(f"old Weil block is nonpositive ({a_values[0]:.6e})")

        x_modes = old_vectors.T @ X
        t_modes = old_vectors.T @ T
        cross_costs = [
            np.outer(x_modes[j], x_modes[j]) / a_values[j]
            for j in range(len(a_values))
        ]
        trace_costs = [
            np.outer(t_modes[j], t_modes[j])
            for j in range(len(a_values))
        ]
        costs = [x_cost + t_cost
                 for x_cost, t_cost in zip(cross_costs, trace_costs)]
        zero = np.zeros_like(C)
        high_cost = sum(costs[4:], zero.copy())
        low_cost = sum(costs[:4], zero.copy())
        total_cost = high_cost + low_cost
        residual = _symmetric(C - high_cost)

        old_parities = np.diag(old_vectors.T @ old_reflection @ old_vectors)
        odd_indices = [j for j in range(4) if old_parities[j] < 0]
        even_indices = [j for j in range(4) if old_parities[j] > 0]
        if len(odd_indices) != 2:
            raise ValueError(
                "first four modes do not contain exactly two odd modes: "
                f"{old_parities[:4]}")
        if len(even_indices) != 2:
            raise ValueError(
                "first four modes do not contain exactly two even modes: "
                f"{old_parities[:4]}")

        collar_parities, collar_vectors = np.linalg.eigh(collar_reflection)
        odd_basis = collar_vectors[:, collar_parities < 0]
        even_basis = collar_vectors[:, collar_parities > 0]
        if odd_basis.shape[1] == 0:
            raise ValueError("empty odd collar sector")
        if even_basis.shape[1] == 0:
            raise ValueError("empty even collar sector")
        residual_odd = _symmetric(odd_basis.T @ residual @ odd_basis)
        residual_even = _symmetric(even_basis.T @ residual @ even_basis)
        if np.linalg.eigvalsh(residual_odd)[0] <= 0:
            raise ValueError("high-eliminated odd collar metric is nonpositive")
        if np.linalg.eigvalsh(residual_even)[0] <= 0:
            raise ValueError("high-eliminated even collar metric is nonpositive")

        def parity_metrics(indices: list[int], basis: np.ndarray,
                           metric: np.ndarray) -> tuple[
                               np.ndarray, np.ndarray, float, float]:
            selected_rows = x_modes[indices] @ basis
            normalized_rows = selected_rows / np.sqrt(
                a_values[indices])[:, None]
            gram = _symmetric(normalized_rows @ np.linalg.solve(
                metric, normalized_rows.T))
            trace_cost = sum(
                (trace_costs[j] for j in indices), zero.copy())
            exact_cost = sum((costs[j] for j in indices), zero.copy())
            exact_ratio = _largest_ratio(
                basis.T @ exact_cost @ basis, metric)
            trace_ratio = _largest_ratio(
                basis.T @ trace_cost @ basis, metric)
            return gram, np.linalg.eigvalsh(gram), exact_ratio, trace_ratio

        gram, gram_values, exact_odd_ratio, odd_hodge_ratio = parity_metrics(
            odd_indices, odd_basis, residual_odd)
        even_gram, even_gram_values, exact_even_ratio, even_hodge_ratio = (
            parity_metrics(even_indices, even_basis, residual_even))
        identity_minus_gram = np.eye(2) - gram
        even_identity_minus_gram = np.eye(2) - even_gram

        total_even_ratio = _largest_ratio(
            even_basis.T @ total_cost @ even_basis,
            even_basis.T @ C @ even_basis)
        total_odd_ratio = _largest_ratio(
            odd_basis.T @ total_cost @ odd_basis,
            odd_basis.T @ C @ odd_basis)

        # The proved raw high-tail estimate currently starts only near mu=3.
        # Keep the modes below that threshold visible as a separate medium
        # sector rather than silently calling modes j>=4 "high".
        high_start = int(np.searchsorted(a_values, 3.0, side="left"))
        high_mu_cost = sum(costs[high_start:], zero.copy())
        residual_mu = _symmetric(C - high_mu_cost)
        medium_cost = sum(costs[4:high_start], zero.copy())
        medium_ratio = (_largest_ratio(medium_cost, residual_mu)
                        if high_start > 4 else 0.0)
        after_medium = _symmetric(residual_mu - medium_cost)

        row.update({
            "old_lambda1": float(a_values[0]),
            "old_lambda2": float(a_values[1]),
            "old_lambda3": float(a_values[2]),
            "old_lambda4": float(a_values[3]),
            "old_lambda5": float(a_values[4]),
            "lambda5_minus_lambda4": float(a_values[4] - a_values[3]),
            "lambda5_over_lambda4": float(a_values[4] / a_values[3]),
            "odd_index_1": odd_indices[0],
            "odd_index_2": odd_indices[1],
            "odd_parity_error": float(max(
                abs(old_parities[j] + 1) for j in odd_indices)),
            "g11": float(gram[0, 0]),
            "g12": float(gram[0, 1]),
            "g22": float(gram[1, 1]),
            "g_min": float(gram_values[0]),
            "g_max": float(gram_values[-1]),
            "det_i_minus_g": float(np.linalg.det(identity_minus_gram)),
            "first_pivot": float(identity_minus_gram[0, 0]),
            "exact_odd_contraction": exact_odd_ratio,
            "odd_hodge_contraction": odd_hodge_ratio,
            "even_g11": float(even_gram[0, 0]),
            "even_g12": float(even_gram[0, 1]),
            "even_g22": float(even_gram[1, 1]),
            "even_g_min": float(even_gram_values[0]),
            "even_g_max": float(even_gram_values[-1]),
            "even_det_i_minus_g": float(np.linalg.det(
                even_identity_minus_gram)),
            "even_first_pivot": float(even_identity_minus_gram[0, 0]),
            "exact_even_contraction": exact_even_ratio,
            "even_hodge_contraction": even_hodge_ratio,
            "low4_contraction": _largest_ratio(low_cost, residual),
            "high_budget_fraction": _largest_ratio(high_cost, C),
            "residual_collar_min": float(np.linalg.eigvalsh(residual)[0]),
            "residual_odd_min": float(np.linalg.eigvalsh(residual_odd)[0]),
            "raw_collar_min": float(np.linalg.eigvalsh(C)[0]),
            "total_row_ratio": _largest_ratio(total_cost, C),
            "total_even_ratio": total_even_ratio,
            "total_odd_ratio": total_odd_ratio,
            "total_surplus_min": float(np.linalg.eigvalsh(
                _symmetric(C - total_cost))[0]),
            "mu3_high_start": high_start,
            "mu3_high_count": len(a_values) - high_start,
            "mu3_medium_count": max(0, high_start - 4),
            "mu3_high_budget_fraction": _largest_ratio(high_mu_cost, C),
            "mu3_residual_min": float(np.linalg.eigvalsh(residual_mu)[0]),
            "mu3_medium_contraction": medium_ratio,
            "mu3_after_medium_min": float(np.linalg.eigvalsh(
                after_medium)[0]),
            "old_reflection_commutator": float(np.linalg.norm(
                A @ old_reflection - old_reflection @ A, ord=2)),
            "collar_reflection_commutator": float(np.linalg.norm(
                residual @ collar_reflection
                - collar_reflection @ residual, ord=2)),
        })
    except (ValueError, np.linalg.LinAlgError) as error:
        row["status"] = f"error:{error}"
    return row


def _matched_case(family: str, old_support: float, new_support: float,
                  old_degree: int, mesh_ratio: float, cutoff_scale: float,
                  density: float, minimum_fraction: float) -> Case:
    collar_degree = matched_collar_degree(
        old_support, new_support, old_degree, mesh_ratio, minimum_fraction)
    cutoff = cutoff_scale * default_cutoff(old_degree)
    return Case(family, old_degree, mesh_ratio, collar_degree,
                cutoff_scale, cutoff, density)


def suite(old_support: float, new_support: float,
          reference_degree: int, reference_mesh_ratio: float,
          reference_cutoff_scale: float, reference_density: float,
          minimum_fraction: float, old_degrees: list[int],
          mesh_ratios: list[float], cutoff_scales: list[float],
          densities: list[float]) -> list[Case]:
    """Build a one-factor-at-a-time suite, removing duplicate baselines."""
    candidates: list[Case] = []
    for degree in old_degrees:
        candidates.append(_matched_case(
            "old_degree", old_support, new_support, degree,
            reference_mesh_ratio, reference_cutoff_scale,
            reference_density, minimum_fraction))
    for ratio in mesh_ratios:
        candidates.append(_matched_case(
            "collar_mesh", old_support, new_support, reference_degree,
            ratio, reference_cutoff_scale, reference_density,
            minimum_fraction))
    for scale in cutoff_scales:
        candidates.append(_matched_case(
            "fourier_cutoff", old_support, new_support, reference_degree,
            reference_mesh_ratio, scale, reference_density,
            minimum_fraction))
    for density in densities:
        candidates.append(_matched_case(
            "interval_density", old_support, new_support, reference_degree,
            reference_mesh_ratio, reference_cutoff_scale, density,
            minimum_fraction))

    # Keep a baseline in each family because it makes each one-factor table
    # independently readable.  Remove only exact duplicates within a family.
    seen: set[tuple[object, ...]] = set()
    cases: list[Case] = []
    for case in candidates:
        key = (case.family, case.old_degree, case.collar_degree, case.cutoff,
               case.interval_density)
        if key not in seen:
            seen.add(key)
            cases.append(case)
    return cases


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-power", type=int, default=5)
    parser.add_argument("--reference-degree", type=int, default=181)
    parser.add_argument("--reference-mesh-ratio", type=float, default=0.42)
    parser.add_argument("--reference-cutoff-scale", type=float, default=1.0)
    parser.add_argument("--reference-density", type=float, default=30.0)
    parser.add_argument("--minimum-collar-fraction", type=float, default=1/24)
    parser.add_argument("--old-degrees", nargs="+", type=int,
                        default=[61, 91, 121, 151, 181, 211, 241, 301])
    parser.add_argument("--mesh-ratios", nargs="+", type=float,
                        default=[0.28, 0.35, 0.42, 0.55, 0.70])
    parser.add_argument("--cutoff-scales", nargs="+", type=float,
                        default=[0.50, 0.75, 1.00, 1.25, 1.50])
    parser.add_argument("--densities", nargs="+", type=float,
                        default=[10.0, 20.0, 30.0, 60.0, 120.0])
    parser.add_argument(
        "--families", nargs="+",
        choices=["old_degree", "collar_mesh", "fourier_cutoff",
                 "interval_density"],
        default=["old_degree", "collar_mesh", "fourier_cutoff",
                 "interval_density"],
        help="run only the selected one-factor families")
    parser.add_argument("--chunk", type=int, default=2000)
    args = parser.parse_args()
    if min(args.mesh_ratios + [args.reference_mesh_ratio]) <= 0:
        parser.error("mesh ratios must be positive")
    if min(args.cutoff_scales + [args.reference_cutoff_scale]) <= 0:
        parser.error("cutoff scales must be positive")
    if min(args.densities + [args.reference_density]) <= 0:
        parser.error("interval densities must be positive")

    catalog = event_catalog()
    positions = {n: i for i, (_, n, _, _) in enumerate(catalog)}
    if args.prime_power not in positions:
        parser.error("prime power is absent from the event catalog")
    position = positions[args.prime_power]
    if position == 0 or position + 1 == len(catalog):
        parser.error("event needs a predecessor and successor")
    event_support = catalog[position][3]
    old_support = (catalog[position - 1][3] + event_support) / 2
    new_support = (event_support + catalog[position + 1][3]) / 2

    cases = suite(
        old_support, new_support, args.reference_degree,
        args.reference_mesh_ratio, args.reference_cutoff_scale,
        args.reference_density, args.minimum_collar_fraction,
        args.old_degrees, args.mesh_ratios, args.cutoff_scales,
        args.densities)
    cases = [case for case in cases if case.family in args.families]
    mp.mp.dps = 30
    writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS, extrasaction="ignore")
    writer.writeheader()
    for case in cases:
        row = evaluate(old_support, new_support, case, args.chunk)
        writer.writerow(row)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
