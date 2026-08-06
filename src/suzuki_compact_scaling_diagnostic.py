"""Fixed-compact scaling and Clark-weight diagnostic for Suzuki models.

This is a bounded-memory numerical checkpoint for two different possible
lower bounds on the boundary phase ``Phi``:

    integrated:  Phi(T) - Phi(0) >= c L T,
    pointwise:   Phi'(t) >= c L.

The second assertion is strictly stronger.  A model can retain the geometric
root count while its local phase derivative becomes small and its Clark
weights ``2*pi/Phi'(lambda)`` become large.

Completed-Weil rows use finite Legendre compressions and are labelled as such.
They are not computations of the exact unbounded extension.  Existing
continuum certificates are used only through ``L = 749/250``.  Rows at larger
support, or near a measured Galerkin floor not covered by a full-space lower
bound, remain numerical Galerkin data only.

The phase-derivative and Clark-weight columns are likewise grid-derived
proxies.  A Galerkin projection need not preserve the Green identity that
makes the continuum Livšic phase monotone, so a nonpositive sampled derivative
is a discretization warning rather than a negative Clark mass.  Exact Clark
measure language applies only after that operator-theoretic structure has been
proved for the object being sampled.

The CLI builds one matrix and one characteristic at a time, samples only the
largest requested compact, then derives every smaller-compact row from that
same grid.  Scalar and Dirichlet-energy controls are included.
"""

from __future__ import annotations

import argparse
import csv
import gc
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

from shift_phase_covariance_falsifier import (
    ShiftedCharacteristic,
    dirichlet_energy_metric,
    scalar_coercive_metric,
)
from spectral_margins import spectral_form
from suzuki_phase_winding_diagnostic import (
    CONTINUUM_SAFETY_MAX_SUPPORT,
    geometric_weyl_turns,
)
from suzuki_selected_divisor_alignment import (
    continuum_positivity_certificate,
    measured_metric_floor,
)


DEFAULT_SUPPORTS = (1.0, 1.75, 2.485, 2.996, 3.555)
DEFAULT_DIMENSIONS = (10, 12)
DEFAULT_HEIGHTS = (20.0, 40.0, 60.0, 96.0)
DEFAULT_SHIFTS = (-0.25, -1.0)


@dataclass(frozen=True)
class CompactScalingRow:
    model: str
    diagnostic_scope: str
    basis_kind: str
    support: float
    dimension: int
    shift: float
    shift_role: str
    measured_metric_floor: float
    shifted_condition_number: float
    completed_weil_continuum_shift_certified_safe: bool
    continuum_safety_scope: str
    height: float
    grid_spacing: float
    theta_zero_root_count: int
    theta_pi_root_count: int
    delta_phi_radians: float
    delta_phi_turns: float
    delta_phi_over_support: float
    delta_phi_over_support_height: float
    geometric_weyl_turns: float
    winding_minus_weyl_turns: float
    maximum_unwrapped_grid_step: float
    phase_derivative_minimum: float
    phase_derivative_q05: float
    phase_derivative_median: float
    phase_derivative_maximum: float
    phase_derivative_minimum_over_support: float
    phase_derivative_q05_over_support: float
    phase_derivative_median_over_support: float
    root_phase_derivative_minimum: float
    nonpositive_root_phase_derivative_count: int
    positive_clark_weight_minimum: float
    positive_clark_weight_median: float
    positive_clark_weight_maximum: float
    median_clark_weight_times_support: float


def near_floor_shift(
    metric: np.ndarray, target_condition: float = 1.0e6
) -> float:
    """Choose a resolvable shift just below the measured Galerkin floor.

    For a non-scalar Hermitian matrix, the gap is chosen so that the shifted
    spectral condition number is approximately ``target_condition``.  Scalar
    matrices use a small relative gap because their shifted condition number
    is one for every admissible shift.
    """

    if target_condition <= 1.0:
        raise ValueError("target_condition must exceed one")
    values = np.linalg.eigvalsh(
        (np.asarray(metric, dtype=float) + np.asarray(metric, dtype=float).T)
        / 2.0
    )
    if values.size < 2:
        raise ValueError("metric must have dimension at least two")
    floor = float(values[0])
    width = float(values[-1] - values[0])
    gap = max(width / (target_condition - 1.0), abs(floor) * 1e-6, 1e-10)
    return floor - gap


def _positive_weight_statistics(
    root_derivatives: np.ndarray, support: float
) -> tuple[int, float, float, float, float, float]:
    """Summarize formal ``2*pi/Phi'`` weights where the grid proxy is positive.

    These become Clark weights only for a structure-preserving characteristic;
    the caller records nonpositive derivatives instead of interpreting them as
    signed spectral mass.
    """

    if root_derivatives.size == 0:
        nan = float("nan")
        return 0, nan, nan, nan, nan, nan
    nonpositive = int(np.sum(root_derivatives <= 0.0))
    positive = root_derivatives[root_derivatives > 0.0]
    minimum_derivative = float(np.min(root_derivatives))
    if positive.size == 0:
        nan = float("nan")
        return nonpositive, minimum_derivative, nan, nan, nan, nan
    weights = 2.0 * np.pi / positive
    minimum = float(np.min(weights))
    median = float(np.median(weights))
    maximum = float(np.max(weights))
    return (
        nonpositive,
        minimum_derivative,
        minimum,
        median,
        maximum,
        median * support,
    )


def analyze_characteristic_on_compacts(
    characteristic: ShiftedCharacteristic,
    model: str,
    diagnostic_scope: str,
    support: float,
    shift_role: str,
    heights: Sequence[float],
    samples: int,
    continuum_safe: bool,
    continuum_safety_scope: str,
) -> list[CompactScalingRow]:
    """Sample one characteristic once and analyze all requested compacts."""

    compact_heights = np.asarray(heights, dtype=float)
    if compact_heights.ndim != 1 or compact_heights.size == 0:
        raise ValueError("heights must be a nonempty one-dimensional sequence")
    if np.any(compact_heights <= 0.0) or np.any(np.diff(compact_heights) <= 0.0):
        raise ValueError("heights must be positive and strictly increasing")
    if support <= 0.0 or samples < 1001:
        raise ValueError("support must be positive and samples at least 1001")

    maximum_height = float(compact_heights[-1])
    grid = np.linspace(0.0, maximum_height, samples)
    phasors = characteristic.boundary_phasor(grid)
    unit_phasors = phasors / np.abs(phasors)
    angles = np.unwrap(np.angle(unit_phasors))
    grid_steps = np.abs(np.diff(angles))
    maximum_grid_step = float(np.max(grid_steps))
    if maximum_grid_step >= np.pi:
        raise RuntimeError("phase grid is too coarse to unwrap unambiguously")
    derivative = np.gradient(angles, grid, edge_order=2)

    theta_zero_roots = characteristic.real_zeros(
        0.0, 0.0, maximum_height, samples=samples
    )
    theta_pi_roots = characteristic.real_zeros(
        np.pi, 0.0, maximum_height, samples=samples
    )
    theta_zero_derivatives = np.interp(
        theta_zero_roots, grid, derivative
    )

    shifted = (
        characteristic.metric
        - characteristic.shift * np.eye(characteristic.dimension)
    )
    condition_number = float(np.linalg.cond(shifted))
    rows: list[CompactScalingRow] = []
    for height in compact_heights:
        endpoint_angle = float(np.interp(height, grid, angles))
        delta_phi = endpoint_angle - float(angles[0])
        upper_index = int(np.searchsorted(grid, height, side="right"))
        local_derivative = derivative[:upper_index]
        if grid[upper_index - 1] < height:
            local_derivative = np.append(
                local_derivative,
                float(np.interp(height, grid, derivative)),
            )

        zero_count = int(
            np.searchsorted(theta_zero_roots, height, side="right")
        )
        pi_count = int(
            np.searchsorted(theta_pi_roots, height, side="right")
        )
        root_derivatives = theta_zero_derivatives[:zero_count]
        (
            nonpositive_count,
            root_derivative_minimum,
            clark_minimum,
            clark_median,
            clark_maximum,
            scaled_clark_median,
        ) = _positive_weight_statistics(root_derivatives, support)
        weyl_turns = geometric_weyl_turns(support, float(height))

        rows.append(
            CompactScalingRow(
                model=model,
                diagnostic_scope=diagnostic_scope,
                basis_kind=characteristic.basis_kind,
                support=float(support),
                dimension=characteristic.dimension,
                shift=characteristic.shift,
                shift_role=shift_role,
                measured_metric_floor=characteristic.metric_floor,
                shifted_condition_number=condition_number,
                completed_weil_continuum_shift_certified_safe=continuum_safe,
                continuum_safety_scope=continuum_safety_scope,
                height=float(height),
                grid_spacing=float(grid[1] - grid[0]),
                theta_zero_root_count=zero_count,
                theta_pi_root_count=pi_count,
                delta_phi_radians=delta_phi,
                delta_phi_turns=delta_phi / (2.0 * np.pi),
                delta_phi_over_support=delta_phi / support,
                delta_phi_over_support_height=delta_phi / (support * height),
                geometric_weyl_turns=weyl_turns,
                winding_minus_weyl_turns=(
                    delta_phi / (2.0 * np.pi) - weyl_turns
                ),
                maximum_unwrapped_grid_step=maximum_grid_step,
                phase_derivative_minimum=float(np.min(local_derivative)),
                phase_derivative_q05=float(
                    np.quantile(local_derivative, 0.05)
                ),
                phase_derivative_median=float(np.median(local_derivative)),
                phase_derivative_maximum=float(np.max(local_derivative)),
                phase_derivative_minimum_over_support=(
                    float(np.min(local_derivative)) / support
                ),
                phase_derivative_q05_over_support=(
                    float(np.quantile(local_derivative, 0.05)) / support
                ),
                phase_derivative_median_over_support=(
                    float(np.median(local_derivative)) / support
                ),
                root_phase_derivative_minimum=root_derivative_minimum,
                nonpositive_root_phase_derivative_count=nonpositive_count,
                positive_clark_weight_minimum=clark_minimum,
                positive_clark_weight_median=clark_median,
                positive_clark_weight_maximum=clark_maximum,
                median_clark_weight_times_support=scaled_clark_median,
            )
        )
    return rows


def _completed_continuum_scope(
    support: float, shift: float
) -> tuple[bool, str]:
    certificate = continuum_positivity_certificate(support)
    safe = bool(
        certificate is not None
        and support <= CONTINUUM_SAFETY_MAX_SUPPORT + 1e-12
        and shift < certificate.lower_bound
    )
    if certificate is None:
        return False, "no repository continuum certificate beyond L=749/250"
    if safe:
        return True, certificate.scope
    return (
        False,
        "measured Galerkin admissibility only; shift is not below the "
        "documented full-space lower bound",
    )


def _distinct_shifts(
    metric: np.ndarray,
    fixed_shifts: Iterable[float],
    near_floor_condition: float | None,
) -> list[tuple[float, str]]:
    floor = float(np.linalg.eigvalsh((metric + metric.T) / 2.0)[0])
    shifts: list[tuple[float, str]] = []
    for shift in fixed_shifts:
        value = float(shift)
        if value < floor and not any(abs(value - prior) < 1e-13 for prior, _ in shifts):
            shifts.append((value, "fixed"))
    if near_floor_condition is not None:
        value = near_floor_shift(metric, near_floor_condition)
        if not any(abs(value - prior) < 1e-13 for prior, _ in shifts):
            shifts.append(
                (value, f"near-Galerkin-floor-cond-{near_floor_condition:.0e}")
            )
    if not shifts:
        raise ValueError("no requested shift lies below the measured metric floor")
    return shifts


def _print_header() -> None:
    print(
        "model,L,m,shift_role,shift,T,N0,Npi,DeltaPhi_over_L,"
        "DeltaPhi_over_LT,min_PhiPrime_over_L,q05_PhiPrime_over_L,"
        "median_Clark,max_Clark,nonpositive_root_derivatives,"
        "completed_continuum_safe",
        flush=True,
    )


def _print_row(row: CompactScalingRow) -> None:
    print(
        f"{row.model},{row.support:.3f},{row.dimension},{row.shift_role},"
        f"{row.shift:.12g},{row.height:.3f},{row.theta_zero_root_count},"
        f"{row.theta_pi_root_count},{row.delta_phi_over_support:.9f},"
        f"{row.delta_phi_over_support_height:.9f},"
        f"{row.phase_derivative_minimum_over_support:.9e},"
        f"{row.phase_derivative_q05_over_support:.9e},"
        f"{row.positive_clark_weight_median:.9g},"
        f"{row.positive_clark_weight_maximum:.9g},"
        f"{row.nonpositive_root_phase_derivative_count},"
        f"{str(row.completed_weil_continuum_shift_certified_safe).lower()}",
        flush=True,
    )


def _write_rows(
    writer: csv.DictWriter | None,
    output_handle,
    rows: Sequence[CompactScalingRow],
) -> csv.DictWriter | None:
    for row in rows:
        _print_row(row)
        if output_handle is not None:
            data = asdict(row)
            if writer is None:
                writer = csv.DictWriter(
                    output_handle, fieldnames=list(data.keys())
                )
                writer.writeheader()
            writer.writerow(data)
    if output_handle is not None:
        output_handle.flush()
    return writer


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--supports", type=float, nargs="+", default=list(DEFAULT_SUPPORTS)
    )
    parser.add_argument(
        "--dimensions", type=int, nargs="+", default=list(DEFAULT_DIMENSIONS)
    )
    parser.add_argument(
        "--heights", type=float, nargs="+", default=list(DEFAULT_HEIGHTS)
    )
    parser.add_argument(
        "--shifts", type=float, nargs="+", default=list(DEFAULT_SHIFTS)
    )
    parser.add_argument("--samples", type=int, default=12001)
    parser.add_argument("--form-dps", type=int, default=35)
    parser.add_argument(
        "--near-floor-condition",
        type=float,
        default=1.0e6,
        help="target shifted condition number; set <=1 to disable",
    )
    parser.add_argument("--skip-controls", action="store_true")
    parser.add_argument("--skip-completed", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    heights = sorted(set(float(value) for value in args.heights))
    near_condition = (
        args.near_floor_condition if args.near_floor_condition > 1.0 else None
    )
    output_handle = None
    writer = None
    integrated_ratios: list[tuple[float, str, float, float, str]] = []
    pointwise_ratios: list[tuple[float, str, float, float, str]] = []
    try:
        if args.output is not None:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            output_handle = args.output.open("w", newline="", encoding="utf-8")
        _print_header()

        if not args.skip_completed:
            for support in args.supports:
                for dimension in args.dimensions:
                    high_precision = spectral_form(
                        support, dimension, dps=args.form_dps
                    )
                    metric = np.asarray(high_precision.tolist(), dtype=float)
                    del high_precision
                    for shift, role in _distinct_shifts(
                        metric, args.shifts, near_condition
                    ):
                        measured_metric_floor(metric, shift)
                        continuum_safe, scope = _completed_continuum_scope(
                            support, shift
                        )
                        characteristic = ShiftedCharacteristic(
                            metric,
                            support / 4.0,
                            shift,
                            basis_kind="legendre",
                        )
                        rows = analyze_characteristic_on_compacts(
                            characteristic=characteristic,
                            model="completed-Weil-finite-Galerkin",
                            diagnostic_scope=(
                                "finite-Galerkin diagnostic; not exact extension"
                            ),
                            support=support,
                            shift_role=role,
                            heights=heights,
                            samples=args.samples,
                            continuum_safe=continuum_safe,
                            continuum_safety_scope=scope,
                        )
                        writer = _write_rows(writer, output_handle, rows)
                        integrated_ratios.extend(
                            (
                                row.delta_phi_over_support_height,
                                row.model,
                                row.support,
                                row.height,
                                row.shift_role,
                            )
                            for row in rows
                        )
                        pointwise_ratios.extend(
                            (
                                row.phase_derivative_minimum_over_support,
                                row.model,
                                row.support,
                                row.height,
                                row.shift_role,
                            )
                            for row in rows
                        )
                        del rows, characteristic
                        gc.collect()
                    del metric
                    gc.collect()

        if not args.skip_controls:
            control_dimension = max(args.dimensions)
            for support in args.supports:
                radius = support / 4.0
                controls = (
                    (
                        "scalar-control",
                        scalar_coercive_metric(control_dimension),
                        "legendre",
                        "exact scalar coercive control",
                    ),
                    (
                        "dirichlet-energy-control",
                        dirichlet_energy_metric(control_dimension, radius),
                        "dirichlet-sine",
                        "finite sine compression of an exact coercive control",
                    ),
                )
                for model, metric, basis_kind, scope in controls:
                    for shift, role in _distinct_shifts(
                        metric, args.shifts, near_condition
                    ):
                        characteristic = ShiftedCharacteristic(
                            metric, radius, shift, basis_kind=basis_kind
                        )
                        rows = analyze_characteristic_on_compacts(
                            characteristic=characteristic,
                            model=model,
                            diagnostic_scope=scope,
                            support=support,
                            shift_role=role,
                            heights=heights,
                            samples=args.samples,
                            continuum_safe=False,
                            continuum_safety_scope=(
                                "not a completed-Weil continuum claim"
                            ),
                        )
                        writer = _write_rows(writer, output_handle, rows)
                        integrated_ratios.extend(
                            (
                                row.delta_phi_over_support_height,
                                row.model,
                                row.support,
                                row.height,
                                row.shift_role,
                            )
                            for row in rows
                        )
                        pointwise_ratios.extend(
                            (
                                row.phase_derivative_minimum_over_support,
                                row.model,
                                row.support,
                                row.height,
                                row.shift_role,
                            )
                            for row in rows
                        )
                        del rows, characteristic
                        gc.collect()
                    del metric
                gc.collect()

        if integrated_ratios:
            integrated_minimum = min(integrated_ratios, key=lambda item: item[0])
            pointwise_minimum = min(pointwise_ratios, key=lambda item: item[0])
            print(
                "sampled_min_DeltaPhi_over_LT="
                f"{integrated_minimum[0]:.12g} at model={integrated_minimum[1]} "
                f"L={integrated_minimum[2]} T={integrated_minimum[3]} "
                f"shift_role={integrated_minimum[4]}",
                flush=True,
            )
            print(
                "sampled_min_PhiPrime_over_L="
                f"{pointwise_minimum[0]:.12g} at model={pointwise_minimum[1]} "
                f"L={pointwise_minimum[2]} T={pointwise_minimum[3]} "
                f"shift_role={pointwise_minimum[4]}",
                flush=True,
            )
    finally:
        if output_handle is not None:
            output_handle.close()


if __name__ == "__main__":
    main()
