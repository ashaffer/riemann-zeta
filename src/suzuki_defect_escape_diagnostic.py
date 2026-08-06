"""Low-memory checkpoint for nested Suzuki defect-vector compatibility.

Fix one negative shift ``sigma=-c<0`` and let

    T_a = A_a + c I,
    v_a = T_a^{-1} exp(-x),
    s_a = ||v_a||_{T_a}^2.

For the natural zero-extension ``J_ab`` from a smaller window into a larger
one, consistency of the fixed-shift form gives the exact continuum identity

    P_{J_ab V_a} v_b = J_ab v_a.                         (1)

Indeed, both sides have pairing ``<u,exp(-x)>_L2`` with every old vector.
Consequently the normalized-vector statistics depend only on ``s_a,s_b``:

    squared projection mass = s_a/s_b,
    coherence               = sqrt(s_a/s_b),
    tail fraction           = 1-s_a/s_b,
    squared distance        = 2(1-sqrt(s_a/s_b)).        (2)

There is also an analytic escape proof, not merely a numerical suggestion.
Choose a fixed compact-core vector ``u`` with
``F=<u,exp(-x)> != 0``.  A left translation by ``r`` preserves its fixed-shift
energy and multiplies ``F`` by ``exp(r)``.  Riesz/Cauchy therefore gives

    s_a >= exp(2r) |F|^2 / ||u||_T^2                    (3)

whenever the translated support fits in the window.  Hence ``s_a`` diverges
and the normalized ``v_a`` converge weakly to zero against every fixed old
core vector.  They cannot be the strongly convergent comparison vectors in a
natural zero-extension resolvent limit.

The rows below are only finite Legendre--Weil Galerkin corroboration of this
analytic conclusion.  They do not compute characteristic roots and make no
claim that any Galerkin roots form a spectral measure.  Continuum shift
certification is labelled separately from the floating compression.

The module sets common numerical backends to one thread before importing
NumPy.  Matrices are constructed and released one at a time.
"""

from __future__ import annotations

import argparse
import gc
import math
import os
from dataclasses import dataclass
from typing import Sequence


for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ.setdefault(_thread_variable, "1")

import numpy as np

from shift_phase_covariance_falsifier import ShiftedCharacteristic
from spectral_margins import spectral_form
from suzuki_phase_winding_diagnostic import CONTINUUM_SAFETY_MAX_SUPPORT
from suzuki_selected_divisor_alignment import continuum_positivity_certificate


# Keep the routine default inside the repository's continuum-certified range.
# The longer ``4 6 8`` corroboration is available explicitly from the CLI.
DEFAULT_SUPPORTS = (1.0, 1.75, 2.485, 2.996)
DEFAULT_DIMENSIONS = (10, 12)


@dataclass(frozen=True)
class ProjectionStatistics:
    squared_projection_mass: float
    normalized_coherence: float
    projection_tail_fraction: float
    normalized_squared_distance: float


@dataclass(frozen=True)
class DefectEscapeRow:
    support: float
    dimension: int
    shift: float
    measured_metric_floor: float
    measured_galerkin_shift_admissible: bool
    continuum_shift_certified_safe: bool
    continuum_safety_scope: str
    minus_defect_norm_sq: float
    plus_defect_norm_sq: float
    reflection_relative_error: float
    opposite_defect_coherence: float
    base_support: float
    base_squared_projection_mass: float
    base_normalized_coherence: float
    base_projection_tail_fraction: float
    base_normalized_squared_distance: float
    previous_support: float
    adjacent_squared_projection_mass: float
    adjacent_normalized_coherence: float
    adjacent_projection_tail_fraction: float
    adjacent_normalized_squared_distance: float


def nested_projection_statistics(
    smaller_norm_sq: float,
    larger_norm_sq: float,
    relative_tolerance: float = 1e-12,
) -> ProjectionStatistics:
    """Evaluate the exact scalar consequences of the projection identity."""

    smaller = float(smaller_norm_sq)
    larger = float(larger_norm_sq)
    if not math.isfinite(smaller) or not math.isfinite(larger):
        raise ValueError("defect norms must be finite")
    if smaller <= 0.0 or larger <= 0.0:
        raise ValueError("defect norms must be positive")
    tolerance = relative_tolerance * max(smaller, larger)
    if smaller > larger + tolerance:
        raise ValueError("nested defect norm must be nondecreasing")
    ratio = min(1.0, smaller / larger)
    coherence = math.sqrt(ratio)
    return ProjectionStatistics(
        squared_projection_mass=ratio,
        normalized_coherence=coherence,
        projection_tail_fraction=1.0 - ratio,
        normalized_squared_distance=2.0 * (1.0 - coherence),
    )


def translated_riesz_lower_bound(
    pairing_abs: float,
    fixed_energy: float,
    left_displacement: float,
) -> float:
    """Lower bound (3) furnished by one translated compact-core vector."""

    pairing = float(pairing_abs)
    energy = float(fixed_energy)
    displacement = float(left_displacement)
    if pairing <= 0.0 or energy <= 0.0 or displacement < 0.0:
        raise ValueError(
            "pairing and energy must be positive and displacement nonnegative"
        )
    return math.exp(2.0 * displacement) * pairing**2 / energy


def _continuum_scope(support: float, shift: float) -> tuple[bool, str]:
    certificate = continuum_positivity_certificate(support)
    safe = bool(
        certificate is not None
        and support <= CONTINUUM_SAFETY_MAX_SUPPORT + 1e-12
        and shift < certificate.lower_bound
    )
    if safe:
        return True, certificate.scope
    if certificate is None:
        return False, "no repository continuum certificate beyond L=749/250"
    return (
        False,
        "shift is not below the documented full-space lower bound",
    )


def _defect_norm_data(
    characteristic: ShiftedCharacteristic,
) -> tuple[float, float, float]:
    shifted_metric = (
        characteristic.metric
        - characteristic.shift * np.eye(characteristic.dimension)
    )
    minus = characteristic.v_minus_coefficients
    plus = characteristic.v_plus_coefficients
    minus_norm_sq = float(np.real(np.vdot(minus, shifted_metric @ minus)))
    plus_norm_sq = float(np.real(np.vdot(plus, shifted_metric @ plus)))
    cross = complex(np.vdot(minus, shifted_metric @ plus))
    if minus_norm_sq <= 0.0 or plus_norm_sq <= 0.0:
        raise FloatingPointError("Galerkin defect norm is not positive")
    coherence = abs(cross) / math.sqrt(minus_norm_sq * plus_norm_sq)
    return minus_norm_sq, plus_norm_sq, coherence


def build_defect_escape_rows(
    supports: Sequence[float],
    dimension: int,
    shift: float = -0.25,
    form_dps: int = 30,
) -> list[DefectEscapeRow]:
    """Build one matrix at a time and compare its defect norm to prior rows."""

    ordered_supports = sorted(set(float(value) for value in supports))
    if not ordered_supports or ordered_supports[0] <= 0.0:
        raise ValueError("supports must be nonempty and positive")
    if dimension < 2:
        raise ValueError("dimension must be at least two")

    rows: list[DefectEscapeRow] = []
    base_support = ordered_supports[0]
    base_norm_sq: float | None = None
    previous_support = base_support
    previous_norm_sq: float | None = None
    for support in ordered_supports:
        high_precision = spectral_form(support, dimension, dps=form_dps)
        metric = np.asarray(high_precision.tolist(), dtype=float)
        del high_precision
        metric = (metric + metric.T) / 2.0
        floor = float(np.linalg.eigvalsh(metric)[0])
        admissible = bool(shift < floor)
        if not admissible:
            raise ValueError(
                f"shift {shift} is not below measured floor {floor} at L={support}"
            )
        characteristic = ShiftedCharacteristic(
            metric, support / 4.0, shift
        )
        minus_norm_sq, plus_norm_sq, opposite_coherence = _defect_norm_data(
            characteristic
        )
        reflection_error = abs(plus_norm_sq - minus_norm_sq) / minus_norm_sq

        if base_norm_sq is None:
            base_norm_sq = minus_norm_sq
        if previous_norm_sq is None:
            previous_norm_sq = minus_norm_sq
        base_stats = nested_projection_statistics(base_norm_sq, minus_norm_sq)
        adjacent_stats = nested_projection_statistics(
            previous_norm_sq, minus_norm_sq
        )
        continuum_safe, continuum_scope = _continuum_scope(support, shift)
        rows.append(
            DefectEscapeRow(
                support=support,
                dimension=dimension,
                shift=float(shift),
                measured_metric_floor=floor,
                measured_galerkin_shift_admissible=admissible,
                continuum_shift_certified_safe=continuum_safe,
                continuum_safety_scope=continuum_scope,
                minus_defect_norm_sq=minus_norm_sq,
                plus_defect_norm_sq=plus_norm_sq,
                reflection_relative_error=reflection_error,
                opposite_defect_coherence=opposite_coherence,
                base_support=base_support,
                base_squared_projection_mass=base_stats.squared_projection_mass,
                base_normalized_coherence=base_stats.normalized_coherence,
                base_projection_tail_fraction=base_stats.projection_tail_fraction,
                base_normalized_squared_distance=(
                    base_stats.normalized_squared_distance
                ),
                previous_support=previous_support,
                adjacent_squared_projection_mass=(
                    adjacent_stats.squared_projection_mass
                ),
                adjacent_normalized_coherence=(
                    adjacent_stats.normalized_coherence
                ),
                adjacent_projection_tail_fraction=(
                    adjacent_stats.projection_tail_fraction
                ),
                adjacent_normalized_squared_distance=(
                    adjacent_stats.normalized_squared_distance
                ),
            )
        )
        previous_support = support
        previous_norm_sq = minus_norm_sq
        del characteristic, metric
        gc.collect()
    return rows


def _print_row(row: DefectEscapeRow) -> None:
    print(
        f"{row.support:.3f},{row.dimension},{row.shift:.9g},"
        f"{row.measured_metric_floor:.9g},"
        f"{str(row.continuum_shift_certified_safe).lower()},"
        f"{row.minus_defect_norm_sq:.12g},"
        f"{row.reflection_relative_error:.3e},"
        f"{row.opposite_defect_coherence:.9g},"
        f"{row.base_squared_projection_mass:.9g},"
        f"{row.base_normalized_coherence:.9g},"
        f"{row.base_projection_tail_fraction:.9g},"
        f"{row.base_normalized_squared_distance:.9g},"
        f"{row.previous_support:.3f},"
        f"{row.adjacent_normalized_coherence:.9g},"
        f"{row.adjacent_projection_tail_fraction:.9g}",
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
    parser.add_argument("--form-dps", type=int, default=30)
    args = parser.parse_args()

    print(
        "L,m,shift,measured_floor,continuum_shift_safe,s_minus,"
        "reflection_error,opposite_defect_coherence,base_projection_mass,"
        "base_coherence,base_tail_fraction,base_distance_sq,previous_L,"
        "adjacent_coherence,adjacent_tail_fraction",
        flush=True,
    )
    for dimension in args.dimensions:
        for row in build_defect_escape_rows(
            args.supports,
            dimension,
            shift=args.shift,
            form_dps=args.form_dps,
        ):
            _print_row(row)


if __name__ == "__main__":
    main()
