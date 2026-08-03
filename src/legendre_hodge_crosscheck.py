"""Independent compact-Legendre cross-check of the Hodge event constant.

This uses the smooth polynomial bump basis and Fourier-multiplier assembly in
``event_cross_ratio.py``, rather than the piecewise-linear hats and exact
spatial prime overlaps in ``tilted_cycle_completion.py``.  It reconstructs
the same nested old/collar relative decomposition and reports the best
constant in

    F + R - H >= c Y* (I-tau)^2 Y.

The newly activated shift has exactly zero old--old overlap.  Because this
implementation represents that shift by a truncated Fourier integral, the
reported shell-isometry error is a mandatory tail-resolution control.  Runs
with a large error are not comparable evidence.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.linalg import eigvalsh as generalized_eigvalsh
from scipy.linalg import null_space

from event_cross_ratio import combined_basis, prime_powers, weil_matrix
from hodge_event_scan import event_catalog, matched_collar_degree
from incidence_poincare_ratio import degree_deficit


@dataclass(frozen=True)
class Crosscheck:
    prime_power: int
    old_support: float
    new_support: float
    old_degree: int
    collar_degree: int
    smooth_power: int
    xquad: int
    xmax: float
    dxi: float
    basis_gram_error: float
    shell_isometry_error: float
    full_kernel_schur_error: float
    old_incidence_minimum: float
    old_incidence_maximum: float
    fresh_ratio: float
    full_ratio: float
    hodge_lower_ratio: float
    hodge_exact_ratio: float
    surplus_to_hodge_loss_ratio: float
    full_surplus_minimum: float
    hodge_loss_maximum: float
    old_gap: float
    full_gap: float


def relative_coordinates(old_support: float, new_support: float,
                         old_degree: int, collar_degree: int,
                         smooth_power: int,
                         xquad: int) -> tuple[np.ndarray, float]:
    """Return an orthonormal [old relative | corrected collar] basis."""
    old_radius = old_support / 4
    new_radius = new_support / 4
    x, wx, basis = combined_basis(
        old_radius, new_radius, old_degree, collar_degree,
        smooth_power, xquad)
    gram = basis.T @ (wx[:, None] * basis)
    basis_gram_error = float(np.linalg.norm(
        gram - np.eye(len(gram)), ord=2))
    plus = (wx * np.exp(x / 2)) @ basis
    minus = (wx * np.exp(-x / 2)) @ basis
    full_relative = null_space(np.vstack([plus, minus]))
    old_relative_local = null_space(np.vstack([
        plus[:old_degree], minus[:old_degree]]))
    old_relative = np.zeros((len(plus), old_degree - 2))
    old_relative[:old_degree] = old_relative_local
    collar_coordinates = null_space(old_relative.T @ full_relative)
    corrected_collar = full_relative @ collar_coordinates
    coordinates = np.column_stack([old_relative, corrected_collar])
    orthogonality_error = float(np.linalg.norm(
        coordinates.T @ coordinates - np.eye(coordinates.shape[1]),
        ord=2))
    return coordinates, max(basis_gram_error, orthogonality_error)


def _smallest_ratio(numerator: np.ndarray,
                    denominator: np.ndarray) -> float:
    return float(generalized_eigvalsh(
        (numerator + numerator.T) / 2,
        (denominator + denominator.T) / 2,
        subset_by_index=[0, 0])[0])


def diagnose(prime_power: int, old_support: float, new_support: float,
             old_degree: int, collar_degree: int, smooth_power: int,
             xquad: int, xmax: float, dxi: float,
             chunk: int) -> Crosscheck:
    old_radius = old_support / 4
    new_radius = new_support / 4
    powers = prime_powers(math.ceil(math.exp(new_support / 2)) + 10)
    active_old = [
        (n, logp) for n, logp in powers
        if 2 * math.log(n) < old_support]
    active_new = [
        (n, logp) for n, logp in powers
        if 2 * math.log(n) < new_support]
    activated = sorted(set(n for n, _ in active_new)
                       - set(n for n, _ in active_old))
    if activated != [prime_power]:
        raise ValueError(f"interval activates {activated}, expected {prime_power}")

    coordinates, basis_gram_error = relative_coordinates(
        old_support, new_support, old_degree, collar_degree,
        smooth_power, xquad)
    old_matrix = weil_matrix(
        old_radius, new_radius, active_old,
        old_degree, collar_degree, smooth_power,
        xquad, xmax, dxi, chunk)
    new_matrix = weil_matrix(
        old_radius, new_radius, active_new,
        old_degree, collar_degree, smooth_power,
        xquad, xmax, dxi, chunk)
    old_form = coordinates.T @ old_matrix @ coordinates
    new_form = coordinates.T @ new_matrix @ coordinates

    old_scalar = float(degree_deficit(old_support))
    new_scalar = float(degree_deficit(new_support))
    event_scalar = new_scalar - old_scalar
    total_dimension = coordinates.shape[1]
    old_dimension = old_degree - 2
    collar_dimension = total_dimension - old_dimension
    identity = np.eye(total_dimension)
    old_gradient = old_form + old_scalar * identity
    shell_gradient = new_form - old_form + event_scalar * identity
    full_gradient = new_form + new_scalar * identity
    old_slice = slice(0, old_dimension)
    collar_slice = slice(old_dimension, total_dimension)

    shell_isometry_error = float(np.linalg.norm(
        shell_gradient[old_slice, old_slice]
        - event_scalar * np.eye(old_dimension), ord=2))
    incidence_old = old_gradient[old_slice, old_slice]
    old_cross = old_gradient[collar_slice, old_slice]
    shell_cross = shell_gradient[collar_slice, old_slice]
    edge_p = (math.sqrt(old_scalar) * old_cross
              @ np.linalg.inv(incidence_old))
    edge_q = shell_cross / math.sqrt(event_scalar)
    shell_ratio = math.sqrt(event_scalar / old_scalar)
    return_map = edge_q - shell_ratio * edge_p
    old_dual = old_scalar * np.linalg.inv(incidence_old)
    cycle_metric = np.eye(old_dimension) + shell_ratio ** 2 * old_dual
    returning = return_map @ np.linalg.solve(cycle_metric, return_map.T)

    s_values, s_vectors = np.linalg.eigh(
        (incidence_old + incidence_old.T) / 2)
    tau_values = np.sqrt(s_values / (s_values + event_scalar))
    tau = (s_vectors * tau_values) @ s_vectors.T
    return_factor = tau @ return_map.T

    shell_fresh = (
        shell_gradient[collar_slice, collar_slice]
        - edge_q @ edge_q.T)
    old_fresh = (
        old_gradient[collar_slice, collar_slice]
        - old_cross @ np.linalg.solve(incidence_old, old_cross.T))
    fresh = (old_fresh + shell_fresh)
    fresh = (fresh + fresh.T) / 2
    returning = (returning + returning.T) / 2

    full_old = full_gradient[old_slice, old_slice]
    full_cross = full_gradient[old_slice, collar_slice]
    full_collar = full_gradient[collar_slice, collar_slice]
    incidence_schur = (
        full_collar - full_cross.T
        @ np.linalg.solve(full_old, full_cross))
    full_kernel_schur_error = float(np.linalg.norm(
        fresh + returning - incidence_schur, ord=2))
    old_weil = new_form[old_slice, old_slice]
    leakage = np.linalg.solve(full_old, full_cross)
    threshold = new_scalar * (
        np.eye(collar_dimension)
        + leakage.T @ full_old @ np.linalg.solve(old_weil, leakage))
    threshold = (threshold + threshold.T) / 2

    complement = np.eye(old_dimension) - tau
    loss = return_factor.T @ complement @ complement @ return_factor
    loss = (loss + loss.T) / 2
    surplus = fresh + returning - threshold
    surplus = (surplus + surplus.T) / 2
    surplus_values = np.linalg.eigvalsh(surplus)
    if surplus_values[0] <= 0:
        surplus_to_loss = math.nan
    else:
        loss_over_surplus = float(generalized_eigvalsh(
            loss, surplus,
            subset_by_index=[collar_dimension - 1,
                             collar_dimension - 1])[0])
        surplus_to_loss = (
            math.inf if loss_over_surplus <= 0 else 1 / loss_over_surplus)
    hodge_lower = fresh + returning - loss

    hodge_response = fresh + return_factor.T @ tau @ return_factor
    hodge_metric = fresh + return_factor.T @ tau @ tau @ return_factor
    hodge_exact = hodge_response @ np.linalg.solve(
        hodge_metric, hodge_response)
    hodge_exact = (hodge_exact + hodge_exact.T) / 2
    old_gap = float(np.linalg.eigvalsh(
        (new_form[old_slice, old_slice]
         + new_form[old_slice, old_slice].T) / 2)[0])
    full_gap = float(np.linalg.eigvalsh((new_form + new_form.T) / 2)[0])

    return Crosscheck(
        prime_power=prime_power,
        old_support=old_support,
        new_support=new_support,
        old_degree=old_degree,
        collar_degree=collar_degree,
        smooth_power=smooth_power,
        xquad=xquad,
        xmax=xmax,
        dxi=dxi,
        basis_gram_error=basis_gram_error,
        shell_isometry_error=shell_isometry_error,
        full_kernel_schur_error=full_kernel_schur_error,
        old_incidence_minimum=float(s_values[0]),
        old_incidence_maximum=float(s_values[-1]),
        fresh_ratio=_smallest_ratio(fresh, threshold),
        full_ratio=_smallest_ratio(fresh + returning, threshold),
        hodge_lower_ratio=_smallest_ratio(hodge_lower, threshold),
        hodge_exact_ratio=_smallest_ratio(hodge_exact, threshold),
        surplus_to_hodge_loss_ratio=surplus_to_loss,
        full_surplus_minimum=float(surplus_values[0]),
        hodge_loss_maximum=float(np.linalg.eigvalsh(loss)[-1]),
        old_gap=old_gap,
        full_gap=full_gap,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-power", type=int, default=5)
    parser.add_argument("--old-degrees", nargs="+", type=int,
                        default=[12, 16, 20, 24])
    parser.add_argument("--collar-degrees", nargs="+", type=int)
    parser.add_argument("--mesh-ratio", type=float, default=0.42)
    parser.add_argument("--minimum-collar-fraction", type=float, default=1/24)
    parser.add_argument("--smooth-powers", nargs="+", type=int, default=[4])
    parser.add_argument("--xquad", type=int, default=160)
    parser.add_argument("--xmax", type=float, default=80.0)
    parser.add_argument("--dxi", type=float, default=0.025)
    parser.add_argument("--chunk", type=int, default=256)
    args = parser.parse_args()

    catalog = event_catalog()
    positions = {n: index for index, (_, n, _, _) in enumerate(catalog)}
    if args.prime_power not in positions:
        parser.error("prime power is absent from the event catalog")
    position = positions[args.prime_power]
    if position == 0 or position + 1 >= len(catalog):
        parser.error("event needs a predecessor and successor")
    event_support = catalog[position][3]
    old_support = (catalog[position - 1][3] + event_support) / 2
    new_support = (event_support + catalog[position + 1][3]) / 2
    if (args.collar_degrees is not None
            and len(args.collar_degrees) != len(args.old_degrees)):
        parser.error("collar degree list must match old degree list")

    fields = list(Crosscheck.__dataclass_fields__)
    print(",".join(fields))
    for smooth_power in args.smooth_powers:
        for index, old_degree in enumerate(args.old_degrees):
            collar_degree = (
                args.collar_degrees[index]
                if args.collar_degrees is not None
                else matched_collar_degree(
                    old_support, new_support, old_degree,
                    args.mesh_ratio, args.minimum_collar_fraction))
            result = diagnose(
                args.prime_power, old_support, new_support,
                old_degree, collar_degree, smooth_power,
                args.xquad, args.xmax, args.dxi, args.chunk)
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
