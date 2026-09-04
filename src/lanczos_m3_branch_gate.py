"""Fail-fast scan for the genuinely informative Lanczos cubic branch.

For the completed sharp-grid operator ``K`` and target carrier ``a``, the
first Lanczos moments are

    m1 = <a, K a>,  m2 = <a, K^2 a>,  m3 = <a, K^3 a>.

Only points with ``m1 < 0`` test the proposed cubic rescue.  At such a point
``m3 >= 0`` gives the sharp eight-ninths carrier witness described in the
companion theorem card.  This module therefore counts the negative-``m1``
branch explicitly instead of pooling it with favorable but irrelevant
positive-``m1`` samples.

The selected-row compression is evaluated by orthogonal projectors in the
full critical-grid coordinates.  This avoids forming a separate floating
nullspace for each target depth and makes a large deterministic scan cheap.
Every arithmetic matrix still contains the actual von Mangoldt prime powers,
the exact rank-two pole matrix, and the archimedean matrix used by the
high-height fixture.

All scans are floating scouts.  A negative branch point must be replayed by
the Arb machinery in :mod:`subfull_direct_q_failfast` before it is a theorem.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math
from typing import Iterable, Sequence

import numpy as np

from high_height_carrier_slice import (
    archimedean_matrix_sign,
    endpoint_null_basis,
    pole_matrix_sign,
    prime_matrix_sign,
)
from signed_garding_failfast import prime_powers


@dataclass(frozen=True)
class LanczosBranchPoint:
    height_T: int
    half_count: int
    grid_center: float
    gamma_fraction: float
    grid_phase: float
    alpha: float
    jet_order: int
    grid_dimension: int
    selected_dimension: int
    kappa: float
    m1: float
    m2: float
    m3: float
    sigma_squared: float
    shifted_hankel_reversal: float
    theta_star: float | None


def actual_matrix_at_center(
    height: int, half_count: int, center: float
) -> tuple[np.ndarray, np.ndarray, float]:
    """Return the actual completed matrix on one centered critical grid."""
    if height <= 4:
        raise ValueError("height must exceed four")
    length = math.log(height)
    spacing = 2.0 * math.pi / length
    indices = np.arange(-half_count, half_count + 1, dtype=int)
    tau = center + spacing * indices
    if tau[0] < height - 1e-11 or tau[-1] > 2.0 * height + 1e-11:
        raise ValueError("critical grid leaves the dyadic band")
    logs, weights = prime_powers(height)
    matrix = (
        archimedean_matrix_sign(tau, length)
        + pole_matrix_sign(tau, indices, length)
        - prime_matrix_sign(tau, length, logs, weights)
    ) / (length * length)
    return (matrix + matrix.conj().T) / 2.0, indices, spacing


def conditioned_carrier(
    indices: np.ndarray,
    *,
    length: float,
    grid_phase: float,
    alpha: float,
    jet_order: int,
) -> tuple[np.ndarray, np.ndarray, float, int]:
    """Return ``(a,P,kappa,dim S)`` for the target-only quotient.

    The carrier row is independent of the absolute grid center.  We therefore
    use a zero-centered dummy grid with candidate ordinate ``-h*phase``.
    """
    if not -0.5 <= grid_phase <= 0.5:
        raise ValueError("phase must lie in [-1/2,1/2]")
    if not 0.0 < alpha < 0.5:
        raise ValueError("alpha must lie in (0,1/2)")
    spacing = 2.0 * math.pi / length
    tau = spacing * indices
    gamma = -spacing * grid_phase
    z = gamma - 1j * alpha
    common = 2.0 * np.sin(
        length * (z - gamma) / 2.0 - math.pi * grid_phase
    )
    values = common / (z - tau)

    endpoint = endpoint_null_basis(indices, jet_order)
    endpoint_projection = endpoint @ endpoint.conj().T
    selected_x = endpoint_projection @ np.real(values)
    x_norm_squared = float(np.vdot(selected_x, selected_x).real)
    if x_norm_squared <= 1e-24:
        raise ValueError("selected positive row is numerically zero")
    selected_projection = endpoint_projection - np.outer(
        selected_x, np.conj(selected_x)
    ) / x_norm_squared
    projected_y = selected_projection @ np.imag(values)
    y_norm_squared = float(np.vdot(projected_y, projected_y).real)
    if y_norm_squared <= 1e-24:
        raise ValueError("selected carrier is numerically zero")
    carrier = projected_y / math.sqrt(y_norm_squared)
    kappa = 2.0 * y_norm_squared / (length * length)
    selected_dimension = int(indices.size - jet_order - 1)
    return carrier, selected_projection, kappa, selected_dimension


def lanczos_branch_point(
    matrix: np.ndarray,
    indices: np.ndarray,
    *,
    height: int,
    center: float,
    grid_phase: float,
    alpha: float,
    jet_order: int,
    arithmetic_shift: float = 0.0,
) -> LanczosBranchPoint:
    """Evaluate the compressed moments and the exact moment threshold."""
    length = math.log(height)
    carrier, projection, kappa, selected_dimension = conditioned_carrier(
        indices,
        length=length,
        grid_phase=grid_phase,
        alpha=alpha,
        jet_order=jet_order,
    )
    operator = np.asarray(matrix, dtype=complex) - arithmetic_shift * np.eye(
        indices.size
    )
    ka = projection @ (operator @ carrier)
    m1 = float(np.vdot(carrier, ka).real)
    m2 = float(np.vdot(ka, ka).real)
    m3 = float(np.vdot(ka, operator @ ka).real)
    sigma_squared = max(0.0, m2 - m1 * m1)
    reversal = m2 * m2 - m1 * m3
    theta_star: float | None = None
    if m1 < 0.0 and sigma_squared > 1e-28 and reversal >= 0.0:
        sigma = math.sqrt(sigma_squared)
        slope = (-m1) / (sigma + math.sqrt(reversal) / sigma)
        theta_star = 1.0 / (1.0 + slope * slope)
    elif m1 < 0.0 and sigma_squared <= 1e-28:
        theta_star = 0.0
    elif m1 < 0.0 and reversal < 0.0:
        theta_star = 0.0

    spacing = 2.0 * math.pi / length
    gamma = center - spacing * grid_phase
    return LanczosBranchPoint(
        height_T=int(height),
        half_count=int((indices.size - 1) // 2),
        grid_center=float(center),
        gamma_fraction=float(gamma / height),
        grid_phase=float(grid_phase),
        alpha=float(alpha),
        jet_order=int(jet_order),
        grid_dimension=int(indices.size),
        selected_dimension=selected_dimension,
        kappa=kappa,
        m1=m1,
        m2=m2,
        m3=m3,
        sigma_squared=sigma_squared,
        shifted_hankel_reversal=reversal,
        theta_star=theta_star,
    )


def deterministic_branch_scan(
    *,
    heights: Sequence[int],
    half_counts: Sequence[int],
    center_count: int,
    phases: Sequence[float],
    alphas: Sequence[float],
    maximum_jet_order: int | None = None,
    negative_tolerance: float = 1e-10,
) -> dict[str, object]:
    """Scan critical-grid coordinates and isolate all negative-``m1`` rows."""
    if center_count < 1:
        raise ValueError("center_count must be positive")
    point_count = 0
    base_count = 0
    skipped_bases = 0
    skipped_points = 0
    negative_rows: list[LanczosBranchPoint] = []
    minimum: LanczosBranchPoint | None = None

    for height in heights:
        length = math.log(height)
        spacing = 2.0 * math.pi / length
        for half_count in half_counts:
            lower = height + half_count * spacing
            upper = 2.0 * height - half_count * spacing
            if not lower < upper:
                skipped_bases += 1
                continue
            centers = (
                np.asarray([(lower + upper) / 2.0])
                if center_count == 1
                else np.linspace(lower + 1e-9, upper - 1e-9, center_count)
            )
            for center in centers:
                matrix, indices, _ = actual_matrix_at_center(
                    int(height), int(half_count), float(center)
                )
                base_count += 1
                largest_jet = indices.size - 2
                if maximum_jet_order is not None:
                    largest_jet = min(largest_jet, maximum_jet_order)
                for jet_order in range(largest_jet + 1):
                    for phase in phases:
                        gamma = center - spacing * phase
                        if not height < gamma < 2.0 * height:
                            skipped_points += len(alphas)
                            continue
                        for alpha in alphas:
                            try:
                                row = lanczos_branch_point(
                                    matrix,
                                    indices,
                                    height=int(height),
                                    center=float(center),
                                    grid_phase=float(phase),
                                    alpha=float(alpha),
                                    jet_order=jet_order,
                                )
                            except ValueError:
                                skipped_points += 1
                                continue
                            point_count += 1
                            if minimum is None or row.m1 < minimum.m1:
                                minimum = row
                            if row.m1 < -negative_tolerance:
                                negative_rows.append(row)

    if minimum is None:
        raise ValueError("scan produced no valid points")
    negative_m3 = [row for row in negative_rows if row.m3 < -negative_tolerance]
    failed_theta = [
        row for row in negative_rows
        if row.theta_star is not None and row.theta_star < 8.0 / 9.0
    ]
    return {
        "scope": "floating actual-coefficient m3 branch scout",
        "base_count": base_count,
        "skipped_base_count": skipped_bases,
        "point_count": point_count,
        "skipped_point_count": skipped_points,
        "negative_m1_count": len(negative_rows),
        "negative_m1_and_m3_count": len(negative_m3),
        "negative_m1_theta_star_below_eight_ninths_count": len(failed_theta),
        "minimum_m1_point": asdict(minimum),
        "negative_m1_points": [asdict(row) for row in negative_rows[:100]],
    }


def shifted_calibration() -> dict[str, object]:
    """Floating moment control matching the existing rigorous ``K-I`` test."""
    height = 16
    length = math.log(height)
    spacing = 2.0 * math.pi / length
    phase = 0.49
    gamma = 1.31 * height
    center = gamma + spacing * phase
    half_count = int(math.floor(0.32 * height / spacing))
    matrix, indices, _ = actual_matrix_at_center(height, half_count, center)
    row = lanczos_branch_point(
        matrix,
        indices,
        height=height,
        center=center,
        grid_phase=phase,
        alpha=0.499,
        jet_order=1,
        arithmetic_shift=1.0,
    )
    return {
        "scope": "shifted calibration only; not an arithmetic claim",
        "point": asdict(row),
        "rigorous_control": (
            "The existing 128-bit Arb LDL certificate proves "
            "K_ar-I <= -10^-3 I on this entire selected quotient."
        ),
    }


def adaptive_minimum_m1(
    *,
    height: int,
    half_count: int,
    jet_order: int,
    seed: int = 20260812,
    maximum_iterations: int = 300,
    population_size: int = 20,
) -> dict[str, object]:
    """Continuously minimize ``m1`` in center, phase, and target depth.

    This is still a floating scout and has no box-coverage interpretation.
    It is useful for trying to enter the negative branch between Cartesian
    samples and for selecting a rational point for a later Arb replay.
    """
    from scipy.optimize import differential_evolution

    length = math.log(height)
    spacing = 2.0 * math.pi / length
    lower = height + half_count * spacing + 1e-9
    upper = 2.0 * height - half_count * spacing - 1e-9
    if not lower < upper:
        raise ValueError("requested critical grid does not fit in the band")

    def objective(parameters: np.ndarray) -> float:
        center, phase, alpha = (float(value) for value in parameters)
        gamma = center - spacing * phase
        if not height < gamma < 2.0 * height:
            return 1e3
        matrix, indices, _ = actual_matrix_at_center(
            height, half_count, center
        )
        try:
            return lanczos_branch_point(
                matrix,
                indices,
                height=height,
                center=center,
                grid_phase=phase,
                alpha=alpha,
                jet_order=jet_order,
            ).m1
        except ValueError:
            return 1e3

    result = differential_evolution(
        objective,
        [(lower, upper), (-0.5, 0.5), (1e-8, 0.5 - 1e-9)],
        seed=seed,
        maxiter=maximum_iterations,
        popsize=population_size,
        tol=1e-10,
        polish=True,
        workers=1,
        updating="immediate",
    )
    center, phase, alpha = (float(value) for value in result.x)
    matrix, indices, _ = actual_matrix_at_center(height, half_count, center)
    point = lanczos_branch_point(
        matrix,
        indices,
        height=height,
        center=center,
        grid_phase=phase,
        alpha=alpha,
        jet_order=jet_order,
    )
    return {
        "scope": "floating adaptive minimum; no continuous box certificate",
        "function_evaluations": int(result.nfev),
        "optimizer_success": bool(result.success),
        "point": asdict(point),
    }


def lower_edge_variance_admission_gate(
    *, m1: float, m2: float, lower_edge_scale: float, theta: float
) -> dict[str, float | bool]:
    """Evaluate the sharp elementary SOS sufficient condition.

    If ``K >= -M I``, ``m1=-r<0``, and

        m2 >= max(r*M, r^2/(1-theta)),

    then the first Lanczos plane has a nonnegative state retaining carrier
    fraction at least ``theta``.  The theorem and proof are recorded in the
    branch-execution report; this function only evaluates its scalar gate.
    """
    if not m1 < 0.0:
        raise ValueError("the variance gate is only for m1<0")
    if lower_edge_scale < -m1:
        raise ValueError("a valid lower-edge scale must satisfy M>=-m1")
    if not 0.0 < theta < 1.0:
        raise ValueError("theta must lie in (0,1)")
    r = -m1
    determinant_requirement = r * lower_edge_scale
    carrier_requirement = r * r / (1.0 - theta)
    required = max(determinant_requirement, carrier_requirement)
    return {
        "admission_guaranteed": bool(m2 >= required),
        "required_m2": required,
        "actual_m2": m2,
        "margin": m2 - required,
        "determinant_requirement": determinant_requirement,
        "carrier_requirement": carrier_requirement,
    }


def _csv_ints(value: str) -> list[int]:
    return [int(item) for item in value.split(",") if item.strip()]


def _csv_floats(value: str) -> list[float]:
    return [float(item) for item in value.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--heights", default="11,12,13,14,15,16,19,24,32,48,64,96,128")
    parser.add_argument("--half-counts", default="2,3,4,6,8")
    parser.add_argument("--center-count", type=int, default=11)
    parser.add_argument("--phases", default="-0.5,-0.375,-0.25,-0.125,0,0.125,0.25,0.375,0.5")
    parser.add_argument("--alphas", default="0.000001,0.05,0.15,0.25,0.35,0.45,0.499999")
    parser.add_argument("--maximum-jet-order", type=int, default=None)
    args = parser.parse_args()
    result = deterministic_branch_scan(
        heights=_csv_ints(args.heights),
        half_counts=_csv_ints(args.half_counts),
        center_count=args.center_count,
        phases=_csv_floats(args.phases),
        alphas=_csv_floats(args.alphas),
        maximum_jet_order=args.maximum_jet_order,
    )
    result["shifted_calibration"] = shifted_calibration()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
