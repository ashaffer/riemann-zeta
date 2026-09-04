"""Finite probes for the source-conditioned QP saddle.

This is a theorem-discovery diagnostic, not an asymptotic certificate.  It
constructs a negative actual-prime source direction and solves the sampled
radial LP

    max r  subject to  sum_t lambda_t a(t) = -r v,
                       lambda_t >= 0,  sum_t lambda_t = 1.

The dual is ``inf_{y.v=-1} max_t y.a(t)``.  The support of ``lambda`` is the
contact set of an optimal sampled separator.  The experiment tests (and
typically refutes) the tempting hypothesis that this contact set is bounded
independently of the number of prime coordinates.
"""

from __future__ import annotations

import argparse
import json
import math

import numpy as np
from scipy.optimize import linprog

from qp_radialization_lab import cosine_atoms, primes_in_shell


def source_saddle(
    center: float,
    *,
    shell_width: float = 0.2,
    source_points: int = 20_001,
    contact_points: int = 12_001,
) -> dict[str, float | int | bool]:
    """Solve one sampled source-conditioned primal/dual saddle."""

    primes, signed_nodes = primes_in_shell(center, shell_width)
    nodes = np.abs(signed_nodes)
    if len(nodes) == 0:
        raise ValueError("the shell contains no primes")

    source_times = np.linspace(center**0.5, center, source_points)
    source_means = np.mean(cosine_atoms(nodes, source_times), axis=0)
    source_index = int(np.argmin(source_means))
    source_time = float(source_times[source_index])
    source_mean = float(source_means[source_index])
    if source_mean >= 0.0:
        raise RuntimeError("the sampled shell has no negative uniform source")

    depth = -source_mean
    source_atom = np.cos(nodes * source_time)
    direction = source_atom + depth * np.ones(len(nodes))

    left = center**0.01
    right = center ** (50.0 / 33.0)
    contact_times = np.linspace(left, right, contact_points)
    atoms = cosine_atoms(nodes, contact_times)

    # Variables are (lambda_1,...,lambda_T,r).  The coordinate equations are
    # A lambda + r v = 0, followed by sum lambda = 1.
    equality = np.zeros((len(nodes) + 1, contact_points + 1))
    equality[: len(nodes), :contact_points] = atoms
    equality[: len(nodes), -1] = direction
    equality[-1, :contact_points] = 1.0
    rhs = np.zeros(len(nodes) + 1)
    rhs[-1] = 1.0
    objective = np.zeros(contact_points + 1)
    objective[-1] = -1.0

    primal = linprog(
        objective,
        A_eq=equality,
        b_eq=rhs,
        bounds=[(0.0, None)] * (contact_points + 1),
        method="highs",
        options={
            "dual_feasibility_tolerance": 1e-9,
            "primal_feasibility_tolerance": 1e-9,
        },
    )
    if not primal.success:
        raise RuntimeError(f"sampled radial LP failed: {primal.message}")

    weights = primal.x[:contact_points]
    radius = float(primal.x[-1])
    support_threshold = max(1e-10, 1e-8 * float(np.max(weights)))
    support = np.flatnonzero(weights > support_threshold)
    weighted_atoms = atoms[:, support] * np.sqrt(weights[support])[None, :]
    singular_values = np.linalg.svd(weighted_atoms, compute_uv=False)
    stable_rank = float(
        np.sum(singular_values * singular_values) / (singular_values[0] ** 2)
    )
    singular_cutoff = 1e-10 * float(singular_values[0])
    retained_singular_values = singular_values[singular_values > singular_cutoff]
    numerical_rank = int(len(retained_singular_values))
    smallest_retained_singular = float(retained_singular_values[-1])
    contact_condition_number = float(
        singular_values[0] / smallest_retained_singular
    )
    effective_contacts = float(1.0 / np.sum(weights[support] ** 2))

    # Solve the displayed separator LP independently as a duality check.
    dual_objective = np.r_[np.zeros(len(nodes)), 1.0]
    dual_inequalities = np.c_[atoms.T, -np.ones(contact_points)]
    dual_equality = np.zeros((1, len(nodes) + 1))
    dual_equality[0, : len(nodes)] = direction
    dual = linprog(
        dual_objective,
        A_ub=dual_inequalities,
        b_ub=np.zeros(contact_points),
        A_eq=dual_equality,
        b_eq=np.array([-1.0]),
        bounds=[(None, None)] * (len(nodes) + 1),
        method="highs",
        options={
            "dual_feasibility_tolerance": 1e-9,
            "primal_feasibility_tolerance": 1e-9,
        },
    )
    if not dual.success:
        raise RuntimeError(f"sampled separator LP failed: {dual.message}")

    residual = float(np.max(np.abs(equality @ primal.x - rhs)))
    separator = dual.x[: len(nodes)]
    separator_l1 = float(np.linalg.norm(separator, ord=1))
    separator_l2 = float(np.linalg.norm(separator))
    contact_reach = (
        float(contact_times[support[-1]] / right) if len(support) else math.nan
    )
    # Linear response at the active contacts to log-frequency perturbations
    # delta(lambda_p)=xi_p/B.  A tiny least singular value exposes a signed
    # superresolution direction invisible to the contact equations.
    scaled_contact_times = contact_times[support] / right
    shift_jacobian = -(
        scaled_contact_times[:, None]
        * np.sin(contact_times[support, None] * nodes[None, :])
        * separator[None, :]
    )
    shift_singular_values = np.linalg.svd(shift_jacobian, compute_uv=False)
    shift_cutoff = 1e-10 * float(shift_singular_values[0])
    retained_shift_singular_values = shift_singular_values[
        shift_singular_values > shift_cutoff
    ]
    shift_numerical_rank = int(len(retained_shift_singular_values))
    shift_smallest_retained = float(retained_shift_singular_values[-1])
    shift_condition_number = float(
        shift_singular_values[0] / shift_smallest_retained
    )
    return {
        "center": center,
        "prime_count": int(len(primes)),
        "source_time": source_time,
        "source_depth": depth,
        "radius": radius,
        "dual_level": float(dual.x[-1]),
        "duality_gap": abs(radius - float(dual.x[-1])),
        "contact_support_size": int(len(support)),
        "contact_effective_size": effective_contacts,
        "weighted_contact_stable_rank": stable_rank,
        "weighted_contact_numerical_rank": numerical_rank,
        "weighted_contact_largest_singular": float(singular_values[0]),
        "weighted_contact_smallest_retained_singular": smallest_retained_singular,
        "weighted_contact_condition_number": contact_condition_number,
        "contact_time_min": (
            float(contact_times[support[0]]) if len(support) else math.nan
        ),
        "contact_time_max": (
            float(contact_times[support[-1]]) if len(support) else math.nan
        ),
        "contact_time_max_over_band_top": contact_reach,
        "separator_l1": separator_l1,
        "separator_l2": separator_l2,
        # If every log-frequency is perturbed by at most 1/B, the elementary
        # Lipschitz estimate at the furthest active contact is bounded by this
        # number.  It diagnoses stability; it is not a certified transport
        # error and is generally much too large for the PQR target.
        "unit_B_shift_l1_bound_at_contacts": separator_l1 * contact_reach,
        "unit_B_shift_l1_bound_full_band": separator_l1,
        "unit_B_shift_jacobian_numerical_rank": shift_numerical_rank,
        "unit_B_shift_jacobian_largest_singular": float(
            shift_singular_values[0]
        ),
        "unit_B_shift_jacobian_smallest_singular": float(
            shift_singular_values[-1]
        ),
        "unit_B_shift_jacobian_smallest_retained_singular": (
            shift_smallest_retained
        ),
        "unit_B_shift_jacobian_condition_number": shift_condition_number,
        "primal_residual": residual,
        "floating_point_only": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("centers", nargs="*", type=float, default=[100.5, 200.5, 400.5])
    parser.add_argument("--shell-width", type=float, default=0.2)
    parser.add_argument("--source-points", type=int, default=20_001)
    parser.add_argument("--contact-points", type=int, default=12_001)
    args = parser.parse_args()
    records = [
        source_saddle(
            center,
            shell_width=args.shell_width,
            source_points=args.source_points,
            contact_points=args.contact_points,
        )
        for center in args.centers
    ]
    print(json.dumps(records, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
