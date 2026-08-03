"""Resolve the Hodge observability row into low and high old modes.

For one consecutive event, write the enlarged Weil block as

    Q_b = [[A, X], [X.T, C]],

and let ``T=(I-tau)Y`` be the Hodge return trace.  Since the old incidence
operator is ``S=A+D_a I``, ``A`` and ``S`` have the same eigenvectors.  In
that basis the desired strengthened block inequality is exactly

    sum_j (X_j.T X_j / a_j + T_j.T T_j) <= C.

This script reports how much of that row-contraction budget is consumed by
the modes above a chosen low-sector dimension, and the exact contraction of
the remaining low block after the high modes have been Schur-eliminated.
Every result is a finite Galerkin diagnostic.
"""
from __future__ import annotations

import argparse
import math

import mpmath as mp
import numpy as np
from scipy.linalg import eigh as generalized_eigh
from scipy.linalg import eigvalsh as generalized_eigvalsh

from hodge_event_scan import (
    default_cutoff,
    event_catalog,
    matched_collar_degree,
)
from incidence_poincare_ratio import degree_deficit
from incidence_shell_completion import (
    archimedean_matrix,
    block_gram,
    hat_group,
    pole_vectors,
    prime_matrix,
    relative_decomposition,
)


def _ratio(numerator: np.ndarray, denominator: np.ndarray) -> float:
    """Largest generalized eigenvalue, with symmetric roundoff removed."""
    numerator = (numerator + numerator.T) / 2
    denominator = (denominator + denominator.T) / 2
    if np.linalg.eigvalsh(denominator)[0] <= 0:
        return math.inf
    return float(generalized_eigvalsh(
        numerator, denominator,
        subset_by_index=[len(denominator) - 1, len(denominator) - 1])[0])


def event_blocks(old_support: float, new_support: float,
                 old_degree: int, collar_degree: int,
                 cutoff: float, intervals: int, chunk: int):
    """Return ``A,X,C,T,S`` in the common relative decomposition."""
    old_radius = old_support / 4
    new_radius = new_support / 4
    old_centers, old_widths = hat_group(
        -old_radius, old_radius, old_degree)
    left_centers, left_widths = hat_group(
        -new_radius, -old_radius, collar_degree)
    right_centers, right_widths = hat_group(
        old_radius, new_radius, collar_degree)
    centers = np.concatenate([old_centers, left_centers, right_centers])
    widths = np.concatenate([old_widths, left_widths, right_widths])
    gram = block_gram(
        [old_degree, collar_degree, collar_degree],
        [old_widths[0], left_widths[0], right_widths[0]])
    plus, minus = pole_vectors(centers, widths)
    coordinates, old_dimension = relative_decomposition(
        gram, plus, minus, old_degree)
    total_dimension = len(centers) - 2
    old_slice = slice(0, old_dimension)
    collar_slice = slice(old_dimension, total_dimension)

    archimedean = archimedean_matrix(
        centers, widths, gram, cutoff, intervals, chunk)
    pole = np.outer(plus, minus) + np.outer(minus, plus)
    old_prime = prime_matrix(centers, widths, old_support)
    new_prime = prime_matrix(centers, widths, new_support)
    old_form = coordinates.T @ (
        archimedean + pole - old_prime) @ coordinates
    new_form = coordinates.T @ (
        archimedean + pole - new_prime) @ coordinates

    old_scalar = float(degree_deficit(old_support))
    new_scalar = float(degree_deficit(new_support))
    event_scalar = new_scalar - old_scalar
    identity = np.eye(total_dimension)
    old_gradient = old_form + old_scalar * identity
    shell_gradient = new_form - old_form + event_scalar * identity

    incidence_old = old_gradient[old_slice, old_slice]
    old_cross = old_gradient[collar_slice, old_slice]
    shell_cross = shell_gradient[collar_slice, old_slice]
    edge_p = (math.sqrt(old_scalar) * old_cross
              @ np.linalg.inv(incidence_old))
    edge_q = shell_cross / math.sqrt(event_scalar)
    shell_ratio = math.sqrt(event_scalar / old_scalar)
    return_map = edge_q - shell_ratio * edge_p

    s_values, s_vectors = np.linalg.eigh(
        (incidence_old + incidence_old.T) / 2)
    tau_values = np.sqrt(s_values / (s_values + event_scalar))
    tau = (s_vectors * tau_values) @ s_vectors.T
    return_factor = tau @ return_map.T
    trace = (np.eye(old_dimension) - tau) @ return_factor

    old_weil = (new_form[old_slice, old_slice]
                + new_form[old_slice, old_slice].T) / 2
    cross = new_form[old_slice, collar_slice]
    collar = (new_form[collar_slice, collar_slice]
              + new_form[collar_slice, collar_slice].T) / 2
    reflection_indices = np.concatenate([
        np.arange(old_degree - 1, -1, -1),
        old_degree + collar_degree
        + np.arange(collar_degree - 1, -1, -1),
        old_degree + np.arange(collar_degree - 1, -1, -1),
    ])
    old_coordinates = coordinates[:, old_slice]
    collar_coordinates = coordinates[:, collar_slice]
    old_reflection = (old_coordinates.T @ gram
                      @ old_coordinates[reflection_indices, :])
    collar_reflection = (collar_coordinates.T @ gram
                         @ collar_coordinates[reflection_indices, :])
    return (old_weil, cross, collar, trace, incidence_old,
            old_reflection, collar_reflection, old_scalar, event_scalar)


def diagnose(old_support: float, new_support: float,
             old_degree: int, collar_degree: int,
             cutoff: float, intervals: int, chunk: int,
             low_counts: list[int]) -> list[dict[str, float | int]]:
    A, X, C, T, S, old_reflection, collar_reflection, old_scalar, event_scalar = event_blocks(
        old_support, new_support, old_degree, collar_degree,
        cutoff, intervals, chunk)
    a_values, vectors = np.linalg.eigh(A)
    if a_values[0] <= 0:
        raise ValueError(f"old Weil block is not positive: {a_values[0]}")
    # A=S-D_a I, so this also checks the common eigenbasis numerically.
    diagonalization_error = np.linalg.norm(
        vectors.T @ S @ vectors
        - np.diag(a_values + old_scalar), ord=2)
    x_modes = vectors.T @ X
    t_modes = vectors.T @ T
    old_parities = np.diag(vectors.T @ old_reflection @ vectors)
    collar_parities, collar_vectors = np.linalg.eigh(
        (collar_reflection + collar_reflection.T) / 2)
    even_collar = collar_vectors[:, collar_parities > 0]
    odd_collar = collar_vectors[:, collar_parities < 0]
    cross_costs = [
        np.outer(x_modes[j], x_modes[j]) / a_values[j]
        for j in range(len(a_values))
    ]
    trace_costs = [
        np.outer(t_modes[j], t_modes[j])
        for j in range(len(a_values))
    ]
    costs = [cross_cost + trace_cost
             for cross_cost, trace_cost in zip(cross_costs, trace_costs)]
    total_cost = sum(costs, np.zeros_like(C))
    total_ratio = _ratio(total_cost, C)
    schur_surplus = C - sum(cross_costs, np.zeros_like(C))
    hodge_loss = sum(trace_costs, np.zeros_like(C))
    hodge_generalized_values, hodge_generalized_vectors = generalized_eigh(
        hodge_loss, schur_surplus)
    hodge_w = hodge_generalized_vectors[:, -1]
    hodge_w /= math.sqrt(float(hodge_w @ schur_surplus @ hodge_w))
    hodge_lambda = float(hodge_generalized_values[-1])
    trace_on_worst = t_modes @ hodge_w
    correction_on_worst = -(x_modes @ hodge_w) / a_values
    cross_cost_on_worst = (x_modes @ hodge_w) ** 2 / a_values

    def leading_fraction(values: np.ndarray, count: int) -> float:
        denominator = float(np.sum(values))
        if denominator <= 0:
            return 0.0
        return float(np.sum(values[:min(count, len(values))]) / denominator)

    trace_low4_fraction = leading_fraction(trace_on_worst ** 2, 4)
    correction_low4_fraction = leading_fraction(
        correction_on_worst ** 2, 4)
    cross_cost_low4_fraction = leading_fraction(cross_cost_on_worst, 4)
    hodge_worst_parity = float(
        hodge_w @ collar_reflection @ hodge_w / (hodge_w @ hodge_w))
    rows = []
    for requested in low_counts:
        low_count = min(max(0, requested), len(a_values))
        low_cost = sum(costs[:low_count], np.zeros_like(C))
        low_cross_cost = sum(cross_costs[:low_count], np.zeros_like(C))
        low_trace_cost = sum(trace_costs[:low_count], np.zeros_like(C))
        high_cost = total_cost - low_cost
        after_high = C - high_cost
        high_x_norm = (float(np.linalg.norm(x_modes[low_count:], ord=2))
                       if low_count < len(a_values) else 0.0)
        high_t_norm = (float(np.linalg.norm(t_modes[low_count:], ord=2))
                       if low_count < len(a_values) else 0.0)
        collar_minimum = float(np.linalg.eigvalsh(C)[0])
        crude_high_fraction = 0.0
        if low_count < len(a_values):
            crude_high_fraction = (
                high_x_norm ** 2 / a_values[low_count]
                + high_t_norm ** 2) / collar_minimum
        def parity_spectrum(basis: np.ndarray) -> tuple[float, float]:
            if basis.shape[1] == 0:
                return 0.0, 0.0
            values = generalized_eigvalsh(
                basis.T @ low_cost @ basis,
                basis.T @ after_high @ basis)
            largest = float(values[-1])
            second = float(values[-2]) if len(values) > 1 else 0.0
            return largest, second
        even_ratio, even_second = parity_spectrum(even_collar)
        odd_ratio, odd_second = parity_spectrum(odd_collar)
        rows.append({
            "low_count": low_count,
            "high_count": len(a_values) - low_count,
            "low_cutoff": (float(a_values[low_count - 1])
                           if low_count else 0.0),
            "next_eigenvalue": (float(a_values[low_count])
                                if low_count < len(a_values) else math.inf),
            "high_budget_fraction": _ratio(high_cost, C),
            "crude_high_fraction": crude_high_fraction,
            "high_cross_norm": high_x_norm,
            "high_trace_norm": high_t_norm,
            "collar_minimum": collar_minimum,
            "low_contraction_after_high": _ratio(low_cost, after_high),
            "low_even_count": int(np.sum(old_parities[:low_count] > 0)),
            "low_odd_count": int(np.sum(old_parities[:low_count] < 0)),
            "low_even_contraction": even_ratio,
            "low_even_second": even_second,
            "low_odd_contraction": odd_ratio,
            "low_odd_second": odd_second,
            "low_cross_only_after_high": _ratio(low_cross_cost, after_high),
            "low_trace_only_after_high": _ratio(low_trace_cost, after_high),
            "after_high_minimum": float(np.linalg.eigvalsh(
                (after_high + after_high.T) / 2)[0]),
            "total_row_ratio": total_ratio,
            "total_reserve": 1 / total_ratio if total_ratio > 0 else math.inf,
            "hodge_domination_constant": 1 / hodge_lambda,
            "hodge_worst_parity": hodge_worst_parity,
            "hodge_trace_low4_fraction": trace_low4_fraction,
            "hodge_correction_low4_fraction": correction_low4_fraction,
            "hodge_cross_cost_low4_fraction": cross_cost_low4_fraction,
            "old_gap": float(a_values[0]),
            "old_scalar": old_scalar,
            "event_scalar": event_scalar,
            "diagonalization_error": float(diagonalization_error),
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-power", type=int, default=5)
    parser.add_argument("--old-degree", type=int, default=121)
    parser.add_argument("--collar-degree", type=int)
    parser.add_argument("--mesh-ratio", type=float, default=0.42)
    parser.add_argument("--minimum-collar-fraction", type=float, default=1/24)
    parser.add_argument("--cutoff", type=float)
    parser.add_argument("--interval-density", type=float, default=100.0)
    parser.add_argument("--chunk", type=int, default=2000)
    parser.add_argument("--low-counts", nargs="+", type=int,
                        default=[1, 2, 4, 8, 16, 32, 64])
    args = parser.parse_args()
    catalog = event_catalog()
    positions = {n: i for i, (_, n, _, _) in enumerate(catalog)}
    position = positions[args.prime_power]
    if position == 0 or position + 1 == len(catalog):
        parser.error("event needs a predecessor and successor")
    event_support = catalog[position][3]
    old_support = (catalog[position - 1][3] + event_support) / 2
    new_support = (event_support + catalog[position + 1][3]) / 2
    collar_degree = args.collar_degree or matched_collar_degree(
        old_support, new_support, args.old_degree,
        args.mesh_ratio, args.minimum_collar_fraction)
    cutoff = args.cutoff or default_cutoff(args.old_degree)
    intervals = int(round(args.interval_density * cutoff))
    if intervals % 2:
        intervals += 1
    mp.mp.dps = 30
    rows = diagnose(
        old_support, new_support, args.old_degree, collar_degree,
        cutoff, intervals, args.chunk, args.low_counts)
    fields = list(rows[0])
    print(",".join(fields))
    for row in rows:
        print(",".join(
            str(row[field]) if isinstance(row[field], int)
            else f"{row[field]:.12e}"
            for field in fields))


if __name__ == "__main__":
    main()
