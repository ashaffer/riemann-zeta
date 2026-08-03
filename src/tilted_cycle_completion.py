"""Scan tilted old/shell--return cycle graphs against the amplified demand.

Let ``F`` be the capacity of the orthogonal old-edge and shell innovations,
and let ``R`` be the coupled return capacity.  If ``Z_F* Z_F=F`` and
``Z_R* Z_R=R``, the graph-like cycle subspace

    J_t = range([Z_F; t Z_R])

has response capacity

    G_t = (F+tR) (F+t^2 R)^dagger (F+tR).

At ``t=0`` this is the return-free capacity.  At ``t=1`` it is ``F+R``,
the full response capacity and hence the Weil-Schur equivalence boundary.
The script verifies the formula using explicit square-root factors and finds
the unique threshold ``t_star`` for ``G_t >= H``.  It also tests the canonical
operator tilt ``tau(S)=sqrt(S/(S+q^2))`` in the actual return coordinates.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import mpmath as mp
import numpy as np
from scipy.linalg import eigvalsh as generalized_eigvalsh
from scipy.optimize import brentq

from incidence_poincare_ratio import degree_deficit
from incidence_shell_completion import (
    archimedean_matrix,
    block_gram,
    hat_group,
    pole_vectors,
    prime_matrix,
    relative_decomposition,
)
from weil_core import PRIME_POWERS


@dataclass(frozen=True)
class TiltedDiagnostic:
    old_support: float
    new_support: float
    activated_event_count: int
    activated_event_index: int
    activated_prime_power: int
    activated_prime: int
    old_relative_dimension: int
    collar_relative_dimension: int
    old_degree_scalar: float
    new_degree_scalar: float
    shell_degree_q2: float
    old_incidence_minimum: float
    old_incidence_maximum: float
    old_incidence_condition: float
    q2_over_old_incidence_minimum: float
    factor_formula_error: float
    full_endpoint_error: float
    return_parameterization_error: float
    return_scalar_formula_error: float
    return_identity_endpoint_error: float
    minimum_grid_increment: float
    ratio_at_zero: float
    ratio_at_quarter: float
    ratio_at_half: float
    ratio_at_three_quarters: float
    weighted_ratio_at_three_quarters: float
    ratio_at_four_fifths: float
    weighted_ratio_at_four_fifths: float
    degree_ratio_t: float
    ratio_at_degree_ratio: float
    weighted_ratio_at_degree_ratio: float
    degree_ratio_above_threshold: float
    sqrt_degree_ratio_t: float
    ratio_at_sqrt_degree_ratio: float
    weighted_ratio_at_sqrt_degree_ratio: float
    sqrt_degree_ratio_above_threshold: float
    hodge_tau_minimum: float
    hodge_tau_maximum: float
    full_surplus_minimum: float
    hodge_loss_minimum: float
    hodge_loss_maximum: float
    hodge_loss_rank: int
    surplus_to_hodge_loss_ratio: float
    scaled_surplus_to_hodge_loss_ratio: float
    surplus_to_sharp_smoothing_ratio: float
    surplus_to_s2_smoothing_ratio: float
    hodge_lower_ratio: float
    hodge_lower_minimum: float
    hodge_tilt_ratio: float
    ratio_at_one: float
    weighted_threshold_alpha: float
    threshold_t: float
    one_minus_threshold: float
    canonical_margin: float
    tilt_width_to_canonical_margin: float


def tilted_data(old_support: float, new_support: float,
                old_degree: int, collar_degree: int,
                cutoff: float, intervals: int,
                chunk: int) -> tuple[
                    np.ndarray, np.ndarray, np.ndarray, float, int, int,
                    np.ndarray, np.ndarray, np.ndarray, float, float]:
    """Assemble ``F``, ``R``, ``H`` and the canonical finite Weil margin."""
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
    coordinates, old_relative_dimension = relative_decomposition(
        gram, plus, minus, old_degree)
    relative_dimension = len(centers) - 2
    collar_relative_dimension = (
        relative_dimension - old_relative_dimension)

    archimedean = archimedean_matrix(
        centers, widths, gram, cutoff, intervals, chunk)
    pole = np.outer(plus, minus) + np.outer(minus, plus)
    old_prime = prime_matrix(centers, widths, old_support)
    new_prime = prime_matrix(centers, widths, new_support)
    old_form = coordinates.T @ (
        archimedean + pole - old_prime) @ coordinates
    new_form = coordinates.T @ (
        archimedean + pole - new_prime) @ coordinates

    old_degree_scalar = float(degree_deficit(old_support))
    new_degree_scalar = float(degree_deficit(new_support))
    shell_degree = new_degree_scalar - old_degree_scalar
    identity = np.eye(relative_dimension)
    old_gradient = old_form + old_degree_scalar * identity
    shell_gradient = (
        new_form - old_form + shell_degree * identity)
    full_gradient = new_form + new_degree_scalar * identity

    old_slice = slice(0, old_relative_dimension)
    collar_slice = slice(old_relative_dimension, relative_dimension)
    old_places_old = old_gradient[old_slice, old_slice]
    old_cross = old_gradient[collar_slice, old_slice]
    shell_cross = shell_gradient[collar_slice, old_slice]

    edge_p = (math.sqrt(old_degree_scalar) * old_cross
              @ np.linalg.inv(old_places_old))
    edge_q = shell_cross / math.sqrt(shell_degree)
    shell_ratio = math.sqrt(shell_degree / old_degree_scalar)
    return_map = edge_q - shell_ratio * edge_p
    old_dual_gram = old_degree_scalar * np.linalg.inv(old_places_old)
    cycle_metric = (
        np.eye(old_relative_dimension)
        + shell_ratio ** 2 * old_dual_gram)
    return_capacity = return_map @ np.linalg.solve(
        cycle_metric, return_map.T)
    old_incidence_values, old_incidence_vectors = np.linalg.eigh(
        (old_places_old + old_places_old.T) / 2)
    if old_incidence_values[0] <= 0:
        raise ValueError("old incidence Gram matrix is not positive definite")
    hodge_tau_values = np.sqrt(
        old_incidence_values / (old_incidence_values + shell_degree))
    hodge_tau = ((old_incidence_vectors * hodge_tau_values)
                 @ old_incidence_vectors.T)
    normalized_return_factor = hodge_tau @ return_map.T

    shell_fresh = (
        shell_gradient[collar_slice, collar_slice]
        - edge_q @ edge_q.T)
    old_fresh = (
        old_gradient[collar_slice, collar_slice]
        - old_cross @ np.linalg.solve(old_places_old, old_cross.T))
    fresh_capacity = old_fresh + shell_fresh

    full_old = full_gradient[old_slice, old_slice]
    full_cross = full_gradient[old_slice, collar_slice]
    old_weil = new_form[old_slice, old_slice]
    leakage = np.linalg.solve(full_old, full_cross)
    threshold = new_degree_scalar * (
        np.eye(collar_relative_dimension)
        + leakage.T @ full_old @ np.linalg.solve(old_weil, leakage))

    fresh_capacity = (fresh_capacity + fresh_capacity.T) / 2
    return_capacity = (return_capacity + return_capacity.T) / 2
    threshold = (threshold + threshold.T) / 2
    full_gap = float(np.linalg.eigvalsh(
        (new_form + new_form.T) / 2)[0])
    canonical_margin = full_gap / (new_degree_scalar + full_gap)
    return (fresh_capacity, return_capacity, threshold, canonical_margin,
            old_relative_dimension, collar_relative_dimension,
            normalized_return_factor, hodge_tau, old_incidence_values,
            old_degree_scalar, new_degree_scalar)


def psd_factor(matrix: np.ndarray) -> np.ndarray:
    """Return ``Z`` with ``Z.T @ Z`` equal to a symmetric PSD matrix."""
    values, vectors = np.linalg.eigh((matrix + matrix.T) / 2)
    scale = max(1.0, float(np.max(np.abs(values))))
    tolerance = len(values) * np.finfo(float).eps * scale
    if values[0] < -10 * tolerance:
        raise ValueError(f"matrix is not PSD: minimum eigenvalue {values[0]}")
    return np.sqrt(np.maximum(values, 0.0))[:, None] * vectors.T


def tilted_capacity(fresh: np.ndarray, returning: np.ndarray,
                    tilt: float) -> np.ndarray:
    numerator = fresh + tilt * returning
    metric = fresh + tilt ** 2 * returning
    capacity = numerator @ np.linalg.solve(metric, numerator)
    return (capacity + capacity.T) / 2


def generalized_ratio(capacity: np.ndarray,
                      threshold: np.ndarray) -> float:
    return float(generalized_eigvalsh(
        capacity, threshold, subset_by_index=[0, 0])[0])


def diagnose_tilt(old_support: float, new_support: float,
                  old_degree: int, collar_degree: int,
                  cutoff: float, intervals: int,
                  chunk: int, grid_size: int) -> TiltedDiagnostic:
    (fresh, returning, threshold, canonical_margin, old_dim, collar_dim,
     normalized_return_factor, hodge_tau, old_incidence_values,
     old_degree_scalar, new_degree_scalar) = tilted_data(
         old_support, new_support, old_degree, collar_degree,
         cutoff, intervals, chunk)

    factor_fresh = psd_factor(fresh)
    factor_return = psd_factor(returning)
    response = np.hstack([factor_fresh.T, factor_return.T])
    factor_formula_error = 0.0
    for tilt in (0.0, 0.173, 0.5, 0.811, 1.0):
        graph = np.vstack([factor_fresh, tilt * factor_return])
        projection = graph @ np.linalg.solve(
            graph.T @ graph, graph.T)
        explicit_capacity = response @ projection @ response.T
        formula_capacity = tilted_capacity(fresh, returning, tilt)
        relative_error = np.linalg.norm(
            explicit_capacity - formula_capacity, ord=2
        ) / np.linalg.norm(formula_capacity, ord=2)
        factor_formula_error = max(factor_formula_error, relative_error)

    full_endpoint_error = float(np.linalg.norm(
        tilted_capacity(fresh, returning, 1.0) - fresh - returning,
        ord=2) / np.linalg.norm(fresh + returning, ord=2))
    return_parameterization_error = float(np.linalg.norm(
        normalized_return_factor.T @ normalized_return_factor - returning,
        ord=2) / np.linalg.norm(returning, ord=2))

    def operator_tilt_capacity(operator: np.ndarray) -> np.ndarray:
        response_part = (
            normalized_return_factor.T @ operator
            @ normalized_return_factor)
        metric_part = (
            normalized_return_factor.T @ operator @ operator
            @ normalized_return_factor)
        response_matrix = fresh + response_part
        capacity = response_matrix @ np.linalg.solve(
            fresh + metric_part, response_matrix)
        return (capacity + capacity.T) / 2

    scalar_check = 0.731
    return_scalar_formula_error = float(np.linalg.norm(
        operator_tilt_capacity(
            scalar_check * np.eye(old_dim))
        - tilted_capacity(fresh, returning, scalar_check),
        ord=2) / np.linalg.norm(fresh + returning, ord=2))
    return_identity_endpoint_error = float(np.linalg.norm(
        operator_tilt_capacity(np.eye(old_dim)) - fresh - returning,
        ord=2) / np.linalg.norm(fresh + returning, ord=2))

    def ratio(tilt: float) -> float:
        return generalized_ratio(
            tilted_capacity(fresh, returning, tilt), threshold)

    def weighted_ratio(weight: float) -> float:
        return generalized_ratio(
            fresh + weight * returning, threshold)

    ratio_at_zero = ratio(0.0)
    ratio_at_one = ratio(1.0)
    if ratio_at_zero >= 1:
        threshold_t = 0.0
    elif ratio_at_one < 1:
        threshold_t = math.nan
    else:
        threshold_t = float(brentq(
            lambda tilt: ratio(tilt) - 1,
            0.0, 1.0, xtol=5e-13, rtol=5e-13))
    if ratio_at_zero >= 1:
        weighted_threshold_alpha = 0.0
    elif ratio_at_one < 1:
        weighted_threshold_alpha = math.nan
    else:
        weighted_threshold_alpha = float(brentq(
            lambda weight: weighted_ratio(weight) - 1,
            0.0, 1.0, xtol=5e-13, rtol=5e-13))

    grid = np.linspace(0.0, 1.0, grid_size)
    grid_ratios = np.array([ratio(float(tilt)) for tilt in grid])
    minimum_grid_increment = float(np.min(np.diff(grid_ratios)))
    one_minus_threshold = (
        1 - threshold_t if math.isfinite(threshold_t) else math.nan)
    tilt_width_to_canonical_margin = (
        one_minus_threshold / canonical_margin
        if canonical_margin != 0 else math.nan)
    degree_ratio_t = old_degree_scalar / new_degree_scalar
    sqrt_degree_ratio_t = math.sqrt(degree_ratio_t)
    hodge_capacity = operator_tilt_capacity(hodge_tau)
    hodge_tau_values, hodge_tau_vectors = np.linalg.eigh(hodge_tau)
    hodge_complement = np.eye(old_dim) - hodge_tau
    hodge_loss = (
        normalized_return_factor.T @ hodge_complement @ hodge_complement
        @ normalized_return_factor)
    hodge_loss = (hodge_loss + hodge_loss.T) / 2
    full_surplus = fresh + returning - threshold
    full_surplus = (full_surplus + full_surplus.T) / 2
    hodge_lower = fresh + returning - hodge_loss
    hodge_lower = (hodge_lower + hodge_lower.T) / 2
    hodge_loss_values = np.linalg.eigvalsh(hodge_loss)
    full_surplus_values = np.linalg.eigvalsh(full_surplus)
    loss_tolerance = (
        collar_dim * np.finfo(float).eps
        * max(1.0, abs(float(hodge_loss_values[-1]))))
    hodge_loss_rank = int(np.sum(hodge_loss_values > loss_tolerance))
    surplus_tolerance = (
        collar_dim * np.finfo(float).eps
        * max(1.0, float(np.linalg.norm(full_surplus, ord=2))))
    def surplus_domination_ratio(loss: np.ndarray) -> float:
        if full_surplus_values[0] <= surplus_tolerance:
            return math.nan
        loss_over_surplus = float(generalized_eigvalsh(
            (loss + loss.T) / 2, full_surplus,
            subset_by_index=[collar_dim - 1, collar_dim - 1])[0])
        return math.inf if loss_over_surplus <= 0 else 1 / loss_over_surplus

    surplus_to_hodge_loss_ratio = surplus_domination_ratio(hodge_loss)
    shell_degree_q2 = new_degree_scalar - old_degree_scalar
    sharp_smoothing_values = (
        shell_degree_q2 ** 2
        / (4 * old_incidence_values
           * (old_incidence_values + shell_degree_q2)))
    s2_smoothing_values = (
        shell_degree_q2 ** 2 / (4 * old_incidence_values ** 2))
    sharp_smoothing_operator = (
        (hodge_tau_vectors * sharp_smoothing_values)
        @ hodge_tau_vectors.T)
    s2_smoothing_operator = (
        (hodge_tau_vectors * s2_smoothing_values)
        @ hodge_tau_vectors.T)
    sharp_smoothing_loss = (
        normalized_return_factor.T @ sharp_smoothing_operator
        @ normalized_return_factor)
    s2_smoothing_loss = (
        normalized_return_factor.T @ s2_smoothing_operator
        @ normalized_return_factor)
    surplus_to_sharp_smoothing_ratio = surplus_domination_ratio(
        sharp_smoothing_loss)
    surplus_to_s2_smoothing_ratio = surplus_domination_ratio(
        s2_smoothing_loss)
    hodge_lower_difference = hodge_lower - threshold
    hodge_lower_difference = (
        hodge_lower_difference + hodge_lower_difference.T) / 2

    event_catalog = sorted(
        {(int(n), int(prime)) for n, prime in PRIME_POWERS},
        key=lambda item: math.log(item[0]))
    activated_events = [
        (index + 1, n, prime)
        for index, (n, prime) in enumerate(event_catalog)
        if old_support < 2 * math.log(n) < new_support]
    activated_event_count = len(activated_events)
    if activated_event_count == 1:
        activated_event_index, activated_prime_power, activated_prime = (
            activated_events[0])
    else:
        activated_event_index = -1
        activated_prime_power = 0
        activated_prime = 0

    return TiltedDiagnostic(
        old_support=old_support,
        new_support=new_support,
        activated_event_count=activated_event_count,
        activated_event_index=activated_event_index,
        activated_prime_power=activated_prime_power,
        activated_prime=activated_prime,
        old_relative_dimension=old_dim,
        collar_relative_dimension=collar_dim,
        old_degree_scalar=old_degree_scalar,
        new_degree_scalar=new_degree_scalar,
        shell_degree_q2=shell_degree_q2,
        old_incidence_minimum=float(old_incidence_values[0]),
        old_incidence_maximum=float(old_incidence_values[-1]),
        old_incidence_condition=float(
            old_incidence_values[-1] / old_incidence_values[0]),
        q2_over_old_incidence_minimum=float(
            shell_degree_q2 / old_incidence_values[0]),
        factor_formula_error=factor_formula_error,
        full_endpoint_error=full_endpoint_error,
        return_parameterization_error=return_parameterization_error,
        return_scalar_formula_error=return_scalar_formula_error,
        return_identity_endpoint_error=return_identity_endpoint_error,
        minimum_grid_increment=minimum_grid_increment,
        ratio_at_zero=ratio_at_zero,
        ratio_at_quarter=ratio(0.25),
        ratio_at_half=ratio(0.5),
        ratio_at_three_quarters=ratio(0.75),
        weighted_ratio_at_three_quarters=weighted_ratio(15 / 16),
        ratio_at_four_fifths=ratio(0.8),
        weighted_ratio_at_four_fifths=weighted_ratio(24 / 25),
        degree_ratio_t=degree_ratio_t,
        ratio_at_degree_ratio=ratio(degree_ratio_t),
        weighted_ratio_at_degree_ratio=weighted_ratio(
            2 * degree_ratio_t - degree_ratio_t ** 2),
        degree_ratio_above_threshold=(
            degree_ratio_t - threshold_t),
        sqrt_degree_ratio_t=sqrt_degree_ratio_t,
        ratio_at_sqrt_degree_ratio=ratio(sqrt_degree_ratio_t),
        weighted_ratio_at_sqrt_degree_ratio=weighted_ratio(
            2 * sqrt_degree_ratio_t - sqrt_degree_ratio_t ** 2),
        sqrt_degree_ratio_above_threshold=(
            sqrt_degree_ratio_t - threshold_t),
        hodge_tau_minimum=float(hodge_tau_values[0]),
        hodge_tau_maximum=float(hodge_tau_values[-1]),
        full_surplus_minimum=float(full_surplus_values[0]),
        hodge_loss_minimum=float(hodge_loss_values[0]),
        hodge_loss_maximum=float(hodge_loss_values[-1]),
        hodge_loss_rank=hodge_loss_rank,
        surplus_to_hodge_loss_ratio=surplus_to_hodge_loss_ratio,
        scaled_surplus_to_hodge_loss_ratio=(
            surplus_to_hodge_loss_ratio * shell_degree_q2
            / old_incidence_values[0]),
        surplus_to_sharp_smoothing_ratio=(
            surplus_to_sharp_smoothing_ratio),
        surplus_to_s2_smoothing_ratio=surplus_to_s2_smoothing_ratio,
        hodge_lower_ratio=generalized_ratio(hodge_lower, threshold),
        hodge_lower_minimum=float(np.linalg.eigvalsh(
            hodge_lower_difference)[0]),
        hodge_tilt_ratio=generalized_ratio(hodge_capacity, threshold),
        ratio_at_one=ratio_at_one,
        weighted_threshold_alpha=weighted_threshold_alpha,
        threshold_t=threshold_t,
        one_minus_threshold=one_minus_threshold,
        canonical_margin=canonical_margin,
        tilt_width_to_canonical_margin=tilt_width_to_canonical_margin,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.75, 2.485, 2.996, 3.555, 4.04])
    parser.add_argument("--old-degree", type=int, default=121)
    parser.add_argument("--collar-degree", type=int, default=40)
    parser.add_argument("--arch-cutoff", type=float, default=1600.0)
    parser.add_argument("--arch-intervals", type=int, default=160000)
    parser.add_argument("--chunk", type=int, default=2000)
    parser.add_argument("--grid-size", type=int, default=17)
    args = parser.parse_args()
    if args.grid_size < 2:
        parser.error("--grid-size must be at least 2")
    mp.mp.dps = 30

    fields = list(TiltedDiagnostic.__dataclass_fields__)
    print(",".join(fields))
    for old_support, new_support in zip(args.supports[:-1], args.supports[1:]):
        result = diagnose_tilt(
            old_support, new_support, args.old_degree, args.collar_degree,
            args.arch_cutoff, args.arch_intervals, args.chunk, args.grid_size)
        values = []
        for field in fields:
            value = getattr(result, field)
            if isinstance(value, int):
                values.append(str(value))
            else:
                values.append(f"{value:.12e}")
        print(",".join(values), flush=True)


if __name__ == "__main__":
    main()
