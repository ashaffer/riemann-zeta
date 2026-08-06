"""Bounded-memory phase-winding diagnostic for Suzuki characteristics.

For the repository's support convention ``L``, Suzuki's differential
operator acts on ``(-a, a)`` with ``a = L/4``.  Conditional on full indicator
width, the geometric fixed-window Weyl prediction is therefore

    N([0, T]) = a T / pi + O(1) = L T / (4 pi) + O(1).

This module compares that prediction with two numerical observables of the
finite Legendre compression of the completed-Weil metric:

* roots of the phases ``theta = 0`` and ``theta = pi``;
* the unwrapped winding of the boundary phasor on ``[0, T]``.

The default CLI is intentionally small.  It runs the three certified supports
``1.75, 2.485, 2.996`` and dimensions ``8, 10, 12`` sequentially.  Every such
row is a *finite-Galerkin diagnostic*, not a computation of the exact
unbounded self-adjoint extension.  The repository's continuum positivity
certificates justify the default shift only through ``L = 749/250``; the code
does not extrapolate that safety statement to larger supports.
"""

from __future__ import annotations

import argparse
import csv
import gc
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

import numpy as np

from shift_phase_covariance_falsifier import ShiftedCharacteristic
from spectral_margins import spectral_form
from suzuki_selected_divisor_alignment import (
    continuum_positivity_certificate,
    first_critical_line_ordinates,
    measured_metric_floor,
)


_TWO_PI = 2.0 * np.pi
CONTINUUM_SAFETY_MAX_SUPPORT = 749.0 / 250.0
DEFAULT_SUPPORTS = (1.75, 2.485, 2.996)
DEFAULT_DIMENSIONS = (8, 10, 12)


def geometric_weyl_turns(support: float, height: float) -> float:
    """Return the fixed-window Weyl main term ``L*T/(4*pi)``."""

    if support <= 0.0 or height <= 0.0:
        raise ValueError("support and height must be positive")
    return float(support * height / (4.0 * np.pi))


def smooth_zeta_zero_count(height: float) -> float:
    """Return the smooth Riemann--von Mangoldt approximation.

    This is

    ``T/(2*pi) * (log(T/(2*pi)) - 1) + 7/8``.

    It omits the fluctuating argument and remainder terms and is used only as
    a density benchmark, never as an exact zero count.
    """

    if height <= 0.0:
        raise ValueError("height must be positive")
    scaled = height / _TWO_PI
    return float(scaled * (np.log(scaled) - 1.0) + 7.0 / 8.0)


def count_matching_support(height: float) -> float:
    """Return ``2*(log(T/(2*pi))-1)``, the leading density match.

    Equating ``L*T/(4*pi)`` with the first two growing terms of the smooth
    zeta count gives this support.  The constant ``7/8`` is deliberately not
    absorbed into a height-dependent finite correction.
    """

    if height <= 0.0:
        raise ValueError("height must be positive")
    return float(2.0 * (np.log(height / _TWO_PI) - 1.0))


def _unit_phasors(phasors: Sequence[complex] | np.ndarray) -> np.ndarray:
    values = np.asarray(phasors, dtype=complex)
    if values.ndim != 1 or values.size < 2:
        raise ValueError("phasors must be a one-dimensional sequence of length >= 2")
    if not np.all(np.isfinite(values)):
        raise ValueError("phasors must be finite")
    moduli = np.abs(values)
    if np.any(moduli < 1e-14):
        raise ValueError("phasors must be nonzero")
    return values / moduli


def phase_winding(phasors: Sequence[complex] | np.ndarray) -> float:
    """Return the sampled unwrapped phase increment in turns.

    The caller must sample densely enough that the phase change between
    adjacent points is below ``pi``.  ``maximum_unwrapped_step`` is reported
    by the CLI so that this assumption is visible in every diagnostic row.
    """

    angles = np.unwrap(np.angle(_unit_phasors(phasors)))
    return float((angles[-1] - angles[0]) / _TWO_PI)


def sampled_phase_root_count(
    phasors: Sequence[complex] | np.ndarray,
    phase: float,
    zero_tolerance: float = 1e-12,
) -> int:
    """Count sampled crossings of ``E(T) = exp(i*phase)``.

    The sign-crossing test rejects antipodal crossings using the real part.
    Exact sampled roots, including a root at the left endpoint, are counted
    once.  This is a grid diagnostic; ``ShiftedCharacteristic.real_zeros``
    remains the bisection-based root locator.
    """

    if zero_tolerance <= 0.0:
        raise ValueError("zero_tolerance must be positive")
    rotated = _unit_phasors(phasors) * np.exp(-1j * float(phase))
    sine = np.imag(rotated)
    real = np.real(rotated)
    positions: list[float] = []

    for index in range(sine.size - 1):
        left = float(sine[index])
        right = float(sine[index + 1])
        candidate: float | None = None
        aligned_real: float | None = None
        if abs(left) < zero_tolerance:
            candidate = float(index)
            aligned_real = float(real[index])
        elif left * right < 0.0:
            fraction = -left / (right - left)
            candidate = float(index) + fraction
            aligned_real = float(
                real[index] + fraction * (real[index + 1] - real[index])
            )
        if candidate is None or aligned_real is None or aligned_real <= 0.0:
            continue
        if not positions or abs(candidate - positions[-1]) > 1e-7:
            positions.append(candidate)

    if abs(float(sine[-1])) < zero_tolerance and float(real[-1]) > 0.0:
        endpoint = float(sine.size - 1)
        if not positions or abs(endpoint - positions[-1]) > 1e-7:
            positions.append(endpoint)
    return len(positions)


@dataclass(frozen=True)
class PhaseWindingDiagnostic:
    model: str
    diagnostic_scope: str
    support: float
    dimension: int
    shift: float
    measured_galerkin_floor: float
    continuum_shift_certified_safe: bool
    continuum_certificate_endpoint: float
    continuum_certificate_lower_bound: float
    continuum_safety_scope: str
    height: float
    samples: int
    theta_zero_root_count: int
    theta_pi_root_count: int
    sampled_theta_zero_count: int
    sampled_theta_pi_count: int
    phase_winding_turns: float
    maximum_unwrapped_step: float
    geometric_weyl_turns: float
    winding_minus_weyl: float
    smooth_zeta_count: float
    leading_count_matching_support: float


def completed_weil_phase_winding_diagnostic(
    support: float,
    dimension: int,
    shift: float,
    height: float,
    samples: int = 12001,
    form_dps: int = 35,
) -> PhaseWindingDiagnostic:
    """Compute one completed-Weil finite-Galerkin diagnostic row."""

    if support <= 0.0 or height <= 0.0:
        raise ValueError("support and height must be positive")
    if dimension < 2:
        raise ValueError("dimension must be at least two")
    if samples < 1001:
        raise ValueError("samples must be at least 1001")
    if form_dps < 20:
        raise ValueError("form_dps must be at least 20")

    high_precision_metric = spectral_form(
        support, dimension, dps=form_dps
    )
    metric = np.asarray(high_precision_metric.tolist(), dtype=float)
    del high_precision_metric
    measured_floor = measured_metric_floor(metric, shift)
    characteristic = ShiftedCharacteristic(
        metric, support / 4.0, shift, basis_kind="legendre"
    )

    grid = np.linspace(0.0, height, samples)
    phasors = characteristic.boundary_phasor(grid)
    angles = np.unwrap(np.angle(_unit_phasors(phasors)))
    winding = phase_winding(phasors)
    maximum_step = float(np.max(np.abs(np.diff(angles))))
    if maximum_step >= np.pi:
        raise RuntimeError("phase grid is too coarse to unwrap unambiguously")

    sampled_zero = sampled_phase_root_count(phasors, 0.0)
    sampled_pi = sampled_phase_root_count(phasors, np.pi)
    exact_zero = int(
        characteristic.real_zeros(
            0.0, 0.0, height, samples=samples
        ).size
    )
    exact_pi = int(
        characteristic.real_zeros(
            np.pi, 0.0, height, samples=samples
        ).size
    )
    if sampled_zero != exact_zero or sampled_pi != exact_pi:
        raise RuntimeError(
            "sampled phase counts disagree with bisection root counts; "
            "increase samples"
        )

    certificate = continuum_positivity_certificate(support)
    certified_safe = bool(
        certificate is not None
        and support <= CONTINUUM_SAFETY_MAX_SUPPORT + 1e-12
        and shift < certificate.lower_bound
    )
    if certificate is None:
        certificate_endpoint = float("nan")
        certificate_lower_bound = float("nan")
        safety_scope = (
            "no repository continuum certificate beyond L=749/250"
        )
    else:
        certificate_endpoint = certificate.endpoint
        certificate_lower_bound = certificate.lower_bound
        safety_scope = certificate.scope

    weyl = geometric_weyl_turns(support, height)
    return PhaseWindingDiagnostic(
        model="completed-Weil Legendre compression",
        diagnostic_scope=(
            "finite-Galerkin diagnostic; not the exact unbounded extension"
        ),
        support=float(support),
        dimension=int(dimension),
        shift=float(shift),
        measured_galerkin_floor=measured_floor,
        continuum_shift_certified_safe=certified_safe,
        continuum_certificate_endpoint=certificate_endpoint,
        continuum_certificate_lower_bound=certificate_lower_bound,
        continuum_safety_scope=safety_scope,
        height=float(height),
        samples=int(samples),
        theta_zero_root_count=exact_zero,
        theta_pi_root_count=exact_pi,
        sampled_theta_zero_count=sampled_zero,
        sampled_theta_pi_count=sampled_pi,
        phase_winding_turns=winding,
        maximum_unwrapped_step=maximum_step,
        geometric_weyl_turns=weyl,
        winding_minus_weyl=winding - weyl,
        smooth_zeta_count=smooth_zeta_zero_count(height),
        leading_count_matching_support=count_matching_support(height),
    )


def _default_height() -> float:
    return float(first_critical_line_ordinates(12)[-1] + 40.0)


def _print_header() -> None:
    print(
        "L,m,floor,N_theta0,N_thetapi,delta_arg_over_2pi,"
        "Weyl_LT_over_4pi,winding_minus_Weyl,max_unwrapped_step,"
        "continuum_safe,status"
    )


def _print_row(result: PhaseWindingDiagnostic) -> None:
    print(
        f"{result.support:.3f},{result.dimension},"
        f"{result.measured_galerkin_floor:.12e},"
        f"{result.theta_zero_root_count},{result.theta_pi_root_count},"
        f"{result.phase_winding_turns:.9f},"
        f"{result.geometric_weyl_turns:.9f},"
        f"{result.winding_minus_weyl:+.9f},"
        f"{result.maximum_unwrapped_step:.9f},"
        f"{str(result.continuum_shift_certified_safe).lower()},"
        "finite-Galerkin-diagnostic",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--supports", type=float, nargs="+", default=list(DEFAULT_SUPPORTS)
    )
    parser.add_argument(
        "--dimensions", type=int, nargs="+", default=list(DEFAULT_DIMENSIONS)
    )
    parser.add_argument("--shift", type=float, default=-0.25)
    parser.add_argument("--height", type=float, default=_default_height())
    parser.add_argument("--samples", type=int, default=12001)
    parser.add_argument("--form-dps", type=int, default=35)
    parser.add_argument(
        "--output",
        type=Path,
        help="optional CSV path; rows are still printed as they finish",
    )
    args = parser.parse_args()

    output_handle = None
    writer = None
    try:
        if args.output is not None:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            output_handle = args.output.open("w", newline="", encoding="utf-8")

        print(
            f"T={args.height:.12f} shift={args.shift} samples={args.samples}"
        )
        _print_header()
        for support in args.supports:
            for dimension in args.dimensions:
                result = completed_weil_phase_winding_diagnostic(
                    support=support,
                    dimension=dimension,
                    shift=args.shift,
                    height=args.height,
                    samples=args.samples,
                    form_dps=args.form_dps,
                )
                _print_row(result)
                if output_handle is not None:
                    row = asdict(result)
                    if writer is None:
                        writer = csv.DictWriter(
                            output_handle, fieldnames=list(row.keys())
                        )
                        writer.writeheader()
                    writer.writerow(row)
                    output_handle.flush()
                del result
                gc.collect()
    finally:
        if output_handle is not None:
            output_handle.close()


if __name__ == "__main__":
    main()
