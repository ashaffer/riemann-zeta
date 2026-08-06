"""Finite-Galerkin selected-divisor alignment with injective root matching.

For a fixed completed-Weil Galerkin metric and a numerically safe shift, the
Suzuki boundary phasor determines a real-zero divisor for every extension
phase.  This diagnostic asks whether one phase makes a selected finite list of
known critical-line zeta ordinates close to *distinct* finite roots.

Alternating zeta ordinates form the training set.  A deterministic phase grid
minimizes their order-preserving injective root-matching cost.  After fitting,
all selected ordinates are matched jointly and injectively; consequently no
finite root can be reused between training and holdout.  The earlier circular
phasor fit is retained only as a baseline, because phasor error need not
control root distance when phase slopes are large.

The ordinates are immutable decimal centers from the Platt/LMFDB rigorously
complete zero dataset, whose source reports absolute precision
``2.5e-31``.  This program converts those centers to float64, so the ensuing
calculation is still a numerical diagnostic rather than interval arithmetic.
Every completed-Weil result is a finite Galerkin diagnostic.  The phase
optimum is only relative to the stated phase/root grids and refinement depth.
On the three default supports, the repository's independent full-space
certificates make the default shift ``-0.25`` continuum-safe; beyond
``L=749/250`` no all-support safety claim is made.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from typing import Sequence

import numpy as np

from shift_phase_covariance_falsifier import (
    ShiftedCharacteristic,
    scalar_coercive_metric,
)
from spectral_margins import spectral_form


_TWO_PI = 2.0 * np.pi

# Displayed centers from the Platt/LMFDB dataset.  LMFDB reports that the raw
# ordinates were rigorously isolated with absolute precision 2^-102 and
# displays these centers to absolute precision 2.5e-31.  Keeping the strings
# here makes the target list deterministic; converting them to float64 below
# deliberately does not claim to retain an interval certificate.
#
# https://www.lmfdb.org/knowledge/show/rcs.source.zeros.zeta
# https://www.lmfdb.org/L/1/1/1.1/r0/0/0
_PLATT_LMFDB_ZERO_CENTERS = (
    "14.13472514173469379045725198356",
    "21.02203963877155499262847959390",
    "25.01085758014568876321379099256",
    "30.42487612585951321031189753058",
    "32.93506158773918969066236896407",
    "37.58617815882567125721776348071",
    "40.91871901214749518739812691463",
    "43.32707328091499951949612216541",
    "48.00515088116715972794247274943",
    "49.77383247767230218191678467856",
    "52.97032147771446064414729660888",
    "56.44624769706339480436775947671",
    "59.34704400260235307965364867499",
    "60.83177852460980984425990182452",
    "65.11254404808160666087505425318",
    "67.07981052949417371447882889652",
    "69.54640171117397925292685752656",
    "72.06715767448190758252210796983",
    "75.70469069908393316832691676203",
    "77.14484006887480537268266485631",
)
_PLATT_LMFDB_ABSOLUTE_PRECISION = 2.5e-31


@dataclass(frozen=True)
class ContinuumPositivityCertificate:
    endpoint: float
    lower_bound: float
    provenance: str
    scope: str


_CONTINUUM_CERTIFICATES = (
    ContinuumPositivityCertificate(
        endpoint=7.0 / 4.0,
        lower_bound=2.2699e-5,
        provenance=(
            "analytic+FLINT-Arb full-space certificate: "
            "src/fullinf_unrestricted_certificate.py"
        ),
        scope="endpoint 7/4 and smaller supports by nested-support monotonicity",
    ),
    ContinuumPositivityCertificate(
        endpoint=497.0 / 200.0,
        lower_bound=9.99e-11,
        provenance=(
            "analytic+FLINT-Arb full-space certificate: "
            "src/fullinf_unrestricted_p3_certificate.py"
        ),
        scope="endpoint 497/200 and smaller supports by nested-support monotonicity",
    ),
    ContinuumPositivityCertificate(
        endpoint=749.0 / 250.0,
        lower_bound=9.9e-16,
        provenance=(
            "analytic+FLINT-Arb full-space certificate: "
            "src/fullinf_unrestricted_n4_certificate.py"
        ),
        scope="endpoint 749/250 and smaller supports by nested-support monotonicity",
    ),
)


def continuum_positivity_certificate(
    support: float,
) -> ContinuumPositivityCertificate | None:
    """Return the strongest applicable documented full-space certificate.

    These certificates use the repository's analytic plus FLINT-Arb trust
    base.  They cover only supports through ``749/250``, not all supports.
    """

    if support <= 0:
        raise ValueError("support must be positive")
    tolerance = 1e-12
    for certificate in _CONTINUUM_CERTIFICATES:
        if support <= certificate.endpoint + tolerance:
            return certificate
    return None


def first_critical_line_ordinates(count: int, dps: int = 50) -> np.ndarray:
    """Return float64 centers of the first Platt/LMFDB certified zeros.

    ``dps`` remains in the API for compatibility with the earlier runtime
    mpmath implementation; immutable source strings now determine the values.
    """

    if count < 2:
        raise ValueError("at least two ordinates are required")
    if dps < 16:
        raise ValueError("dps must be at least 16")
    if count > len(_PLATT_LMFDB_ZERO_CENTERS):
        raise ValueError(
            f"only the first {len(_PLATT_LMFDB_ZERO_CENTERS)} immutable "
            "Platt/LMFDB centers are bundled"
        )
    return np.asarray(_PLATT_LMFDB_ZERO_CENTERS[:count], dtype=float)


@dataclass(frozen=True)
class CircularPhaseFit:
    phase: float
    phasor: complex
    resultant_length: float
    residual_rms: float
    residual_max: float
    chord_diameter: float


def fit_circular_phase(phasors: Sequence[complex]) -> CircularPhaseFit:
    """Fit one unit phasor by circular mean."""

    values = np.asarray(phasors, dtype=complex)
    if values.ndim != 1 or values.size < 2:
        raise ValueError("at least two one-dimensional phasors are required")
    moduli = np.abs(values)
    if np.any(moduli < 1e-14):
        raise ValueError("phasors must be nonzero")
    values = values / moduli
    mean = np.mean(values)
    resultant = float(abs(mean))
    if resultant < 1e-12:
        raise FloatingPointError("the circular mean phase is unresolved")
    fitted = mean / abs(mean)
    residuals = np.abs(values - fitted)
    pairwise = np.abs(values[:, None] - values[None, :])
    return CircularPhaseFit(
        phase=float(np.mod(np.angle(fitted), _TWO_PI)),
        phasor=complex(fitted),
        resultant_length=resultant,
        residual_rms=float(np.sqrt(np.mean(residuals**2))),
        residual_max=float(np.max(residuals)),
        chord_diameter=float(np.max(pairwise)),
    )


def alternating_split(count: int) -> tuple[np.ndarray, np.ndarray]:
    """Return disjoint alternating training and held-out indices."""

    if count < 5:
        raise ValueError("use at least five divisors for an alternating split")
    return np.arange(0, count, 2), np.arange(1, count, 2)


def measured_metric_floor(metric: np.ndarray, shift: float) -> float:
    """Numerically measure the Hermitian floor and reject an unsafe shift."""

    matrix = np.asarray(metric, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("metric must be square")
    floor = float(np.linalg.eigvalsh((matrix + matrix.T) / 2.0)[0])
    if not shift < floor:
        raise ValueError(
            f"shift {shift} is not below the numerically measured "
            f"Galerkin floor {floor}"
        )
    return floor


@dataclass(frozen=True)
class OrderedInjectiveMatch:
    target_count: int
    root_count: int
    root_indices: np.ndarray
    matched_roots: np.ndarray
    residuals: np.ndarray
    rms: float
    maximum: float
    squared_cost: float


def ordered_injective_match(
    targets: Sequence[float], roots: Sequence[float]
) -> OrderedInjectiveMatch:
    """Least-squares increasing injection from targets into distinct roots.

    Dynamic programming permits roots to be skipped, never reused.  The
    returned root indices are strictly increasing and minimize the sum of
    squared distances among all order-preserving injections.
    """

    target_values = np.asarray(targets, dtype=float)
    root_values = np.asarray(roots, dtype=float)
    if (
        target_values.ndim != 1
        or root_values.ndim != 1
        or target_values.size == 0
    ):
        raise ValueError("targets and roots must be nonempty one-dimensional arrays")
    if np.any(np.diff(target_values) <= 0) or np.any(np.diff(root_values) <= 0):
        raise ValueError("targets and roots must both be strictly increasing")
    target_count = target_values.size
    root_count = root_values.size
    if root_count < target_count:
        raise ValueError("there are too few distinct roots for an injective match")

    costs = np.full((target_count + 1, root_count + 1), np.inf)
    take = np.zeros((target_count + 1, root_count + 1), dtype=bool)
    costs[0, :] = 0.0
    for target_index in range(1, target_count + 1):
        # At least target_index roots are needed for target_index matches.
        for root_index in range(target_index, root_count + 1):
            skip_cost = costs[target_index, root_index - 1]
            difference = (
                target_values[target_index - 1] - root_values[root_index - 1]
            )
            take_cost = costs[target_index - 1, root_index - 1] + difference**2
            if take_cost < skip_cost:
                costs[target_index, root_index] = take_cost
                take[target_index, root_index] = True
            else:
                costs[target_index, root_index] = skip_cost

    indices = np.empty(target_count, dtype=int)
    target_index = target_count
    root_index = root_count
    while target_index > 0:
        if root_index <= 0:
            raise RuntimeError("injective-match backtracking failed")
        if take[target_index, root_index]:
            indices[target_index - 1] = root_index - 1
            target_index -= 1
            root_index -= 1
        else:
            root_index -= 1
    matched = root_values[indices]
    residuals = np.abs(matched - target_values)
    squared_cost = float(np.sum(residuals**2))
    return OrderedInjectiveMatch(
        target_count=int(target_count),
        root_count=int(root_count),
        root_indices=indices,
        matched_roots=matched,
        residuals=residuals,
        rms=float(np.sqrt(squared_cost / target_count)),
        maximum=float(np.max(residuals)),
        squared_cost=squared_cost,
    )


class PhaseRootScanner:
    """One bounded-memory boundary-phasor grid reused for every trial phase."""

    def __init__(
        self,
        characteristic: ShiftedCharacteristic,
        z_min: float,
        z_max: float,
        samples: int,
    ) -> None:
        if not z_min < z_max or samples < 1001:
            raise ValueError("invalid phase-root scan grid")
        self.characteristic = characteristic
        self.grid = np.linspace(z_min, z_max, samples)
        self.phasors = characteristic.boundary_phasor(self.grid)
        self.z_min = float(z_min)
        self.z_max = float(z_max)
        self.samples = int(samples)
        self.spacing = float((z_max - z_min) / (samples - 1))

    def approximate_roots(self, phase: float) -> np.ndarray:
        """Interpolate phase crossings on the cached grid.

        Exact final statistics use ``ShiftedCharacteristic.real_zeros``.  This
        approximation is used only by the declared finite phase search.
        """

        rotated = self.phasors * np.exp(-1j * phase)
        sine = np.imag(rotated)
        crossing = np.flatnonzero(sine[:-1] * sine[1:] < 0.0)
        if crossing.size == 0:
            return np.empty(0, dtype=float)
        left_sine = sine[crossing]
        right_sine = sine[crossing + 1]
        fractions = -left_sine / (right_sine - left_sine)
        real_part = np.real(rotated)
        aligned_real = (
            real_part[crossing]
            + fractions * (real_part[crossing + 1] - real_part[crossing])
        )
        genuine = aligned_real > 0.0
        crossing = crossing[genuine]
        fractions = fractions[genuine]
        return self.grid[crossing] + fractions * (
            self.grid[crossing + 1] - self.grid[crossing]
        )


@dataclass(frozen=True)
class PhaseGridOptimization:
    phase: float
    training_match_rms: float
    training_match_max: float
    approximate_root_count: int
    evaluations: int
    phase_grid_size: int
    refinement_levels: int
    root_grid_spacing: float


def optimize_phase_by_training_roots(
    scanner: PhaseRootScanner,
    training_divisors: Sequence[float],
    phase_grid_size: int = 129,
    refinement_levels: int = 2,
    refinement_grid_size: int = 33,
    seed_phases: Sequence[float] = (),
) -> PhaseGridOptimization:
    """Minimize injective training-root distance on a deterministic phase grid."""

    targets = np.asarray(training_divisors, dtype=float)
    if targets.ndim != 1 or targets.size < 2 or np.any(np.diff(targets) <= 0):
        raise ValueError("training divisors must be strictly increasing")
    if phase_grid_size < 8 or refinement_grid_size < 5 or refinement_levels < 0:
        raise ValueError("phase optimizer grids are too small")

    best: tuple[float, float, float, int] | None = None
    evaluations = 0

    def evaluate(phase: float) -> None:
        nonlocal best, evaluations
        normalized_phase = float(np.mod(phase, _TWO_PI))
        roots = scanner.approximate_roots(normalized_phase)
        evaluations += 1
        if roots.size < targets.size:
            return
        match = ordered_injective_match(targets, roots)
        candidate = (
            match.squared_cost,
            normalized_phase,
            match.maximum,
            int(roots.size),
        )
        if best is None or candidate[:2] < best[:2]:
            best = candidate

    coarse = np.linspace(0.0, _TWO_PI, phase_grid_size, endpoint=False)
    for phase in coarse:
        evaluate(float(phase))
    for phase in seed_phases:
        evaluate(float(phase))
    if best is None:
        raise RuntimeError("no trial phase produced enough finite roots")

    half_width = _TWO_PI / phase_grid_size
    for _ in range(refinement_levels):
        center = best[1]
        offsets = np.linspace(-half_width, half_width, refinement_grid_size)
        for offset in offsets:
            evaluate(center + float(offset))
        half_width = 2.0 * half_width / (refinement_grid_size - 1)

    assert best is not None
    rms = float(np.sqrt(best[0] / targets.size))
    return PhaseGridOptimization(
        phase=best[1],
        training_match_rms=rms,
        training_match_max=best[2],
        approximate_root_count=best[3],
        evaluations=evaluations,
        phase_grid_size=phase_grid_size,
        refinement_levels=refinement_levels,
        root_grid_spacing=scanner.spacing,
    )


def _rms(values: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.asarray(values, dtype=float) ** 2)))


def _match_or_infinite(
    targets: np.ndarray, roots: np.ndarray
) -> OrderedInjectiveMatch | None:
    if roots.size < targets.size:
        return None
    return ordered_injective_match(targets, roots)


@dataclass(frozen=True)
class SelectedDivisorAlignment:
    model: str
    support: float
    dimension: int
    shift: float
    shift_role: str
    measured_metric_floor: float
    certified_continuum_lower_bound: float
    continuum_shift_certified_safe: bool
    continuum_certificate_provenance: str
    continuum_certificate_scope: str
    divisor_source: str
    divisor_count: int
    training_count: int
    holdout_count: int
    circular_phase: float
    circular_resultant_length: float
    circular_training_phasor_rms: float
    circular_training_phasor_max: float
    circular_global_match_rms: float
    circular_global_match_max: float
    optimized_phase: float
    optimizer_training_rms: float
    optimizer_training_max: float
    optimizer_approximate_root_count: int
    optimizer_evaluations: int
    optimizer_phase_grid_size: int
    optimizer_refinement_levels: int
    optimizer_root_grid_spacing: float
    optimized_training_phasor_rms: float
    optimized_training_phasor_max: float
    optimized_holdout_phasor_rms: float
    optimized_holdout_phasor_max: float
    optimized_training_characteristic_rms: float
    optimized_training_characteristic_max: float
    optimized_holdout_characteristic_rms: float
    optimized_holdout_characteristic_max: float
    train_only_injective_rms: float
    train_only_injective_max: float
    global_injective_rms: float
    global_injective_max: float
    global_training_injective_rms: float
    global_training_injective_max: float
    global_holdout_injective_rms: float
    global_holdout_injective_max: float
    finite_root_count: int
    roots_below_first_divisor: int
    roots_inside_divisor_span: int
    roots_above_last_divisor: int
    matched_root_index_min: int
    matched_root_index_max: int
    matched_root_index_span: int
    skipped_roots_inside_matched_span: int
    maximum_matched_index_jump: int
    training_matched_root_indices: str
    holdout_matched_root_indices: str
    symmetry_theta_zero_has_root_at_zero: bool
    symmetry_theta_zero_global_rms: float
    symmetry_theta_zero_global_max: float
    symmetry_theta_zero_training_rms: float
    symmetry_theta_zero_training_max: float
    symmetry_theta_zero_holdout_rms: float
    symmetry_theta_zero_holdout_max: float
    symmetry_theta_zero_finite_root_count: int
    symmetry_theta_pi_global_rms: float
    symmetry_theta_pi_global_max: float
    symmetry_theta_pi_training_rms: float
    symmetry_theta_pi_training_max: float
    symmetry_theta_pi_holdout_rms: float
    symmetry_theta_pi_holdout_max: float
    symmetry_theta_pi_finite_root_count: int
    symmetry_constraint_scope: str
    root_scan_min: float
    root_scan_max: float


def selected_divisor_alignment(
    model: str,
    characteristic: ShiftedCharacteristic,
    measured_floor: float,
    shift_role: str,
    divisors: Sequence[float],
    divisor_source: str,
    continuum_certificate: ContinuumPositivityCertificate | None = None,
    root_scan_min: float = 0.0,
    root_scan_max: float | None = None,
    root_samples: int = 30001,
    phase_grid_size: int = 129,
    refinement_levels: int = 2,
    refinement_grid_size: int = 33,
) -> SelectedDivisorAlignment:
    """Fit on alternating divisors and globally rematch all divisors."""

    values = np.asarray(divisors, dtype=float)
    if values.ndim != 1 or values.size < 5 or not np.all(np.diff(values) > 0):
        raise ValueError("divisors must be a strictly increasing list of length >= 5")
    train, holdout = alternating_split(values.size)
    required = characteristic.boundary_phasor(values)
    circular = fit_circular_phase(required[train])

    scan_max = root_scan_max
    if scan_max is None:
        scan_max = float(values[-1] + 40.0)
    scanner = PhaseRootScanner(
        characteristic, root_scan_min, scan_max, root_samples
    )
    optimization = optimize_phase_by_training_roots(
        scanner,
        values[train],
        phase_grid_size=phase_grid_size,
        refinement_levels=refinement_levels,
        refinement_grid_size=refinement_grid_size,
        seed_phases=[circular.phase],
    )

    circular_roots = characteristic.real_zeros(
        circular.phase,
        root_scan_min,
        scan_max,
        samples=root_samples,
    )
    circular_global = _match_or_infinite(values, circular_roots)

    optimized_roots = characteristic.real_zeros(
        optimization.phase,
        root_scan_min,
        scan_max,
        samples=root_samples,
    )
    train_only = ordered_injective_match(values[train], optimized_roots)
    global_match = ordered_injective_match(values, optimized_roots)
    global_training_residuals = global_match.residuals[train]
    global_holdout_residuals = global_match.residuals[holdout]

    optimized_phasor = np.exp(1j * optimization.phase)
    optimized_phasor_residuals = np.abs(required - optimized_phasor)
    characteristic_residuals = characteristic.normalized_characteristic_residual(
        values, optimization.phase
    )
    matched_indices = global_match.root_indices
    index_differences = np.diff(matched_indices)

    theta_zero_center_residual = characteristic.normalized_characteristic_residual(
        np.asarray([0.0]), 0.0
    )
    theta_zero_roots = characteristic.real_zeros(
        0.0,
        root_scan_min,
        scan_max,
        samples=root_samples,
    )
    theta_zero_match = _match_or_infinite(values, theta_zero_roots)
    if theta_zero_match is None:
        theta_zero_global_rms = theta_zero_global_max = float("inf")
        theta_zero_training_rms = theta_zero_training_max = float("inf")
        theta_zero_holdout_rms = theta_zero_holdout_max = float("inf")
    else:
        theta_zero_training = theta_zero_match.residuals[train]
        theta_zero_holdout = theta_zero_match.residuals[holdout]
        theta_zero_global_rms = theta_zero_match.rms
        theta_zero_global_max = theta_zero_match.maximum
        theta_zero_training_rms = _rms(theta_zero_training)
        theta_zero_training_max = float(np.max(theta_zero_training))
        theta_zero_holdout_rms = _rms(theta_zero_holdout)
        theta_zero_holdout_max = float(np.max(theta_zero_holdout))

    theta_pi_roots = characteristic.real_zeros(
        np.pi,
        root_scan_min,
        scan_max,
        samples=root_samples,
    )
    theta_pi_match = _match_or_infinite(values, theta_pi_roots)
    if theta_pi_match is None:
        theta_pi_global_rms = theta_pi_global_max = float("inf")
        theta_pi_training_rms = theta_pi_training_max = float("inf")
        theta_pi_holdout_rms = theta_pi_holdout_max = float("inf")
    else:
        theta_pi_training = theta_pi_match.residuals[train]
        theta_pi_holdout = theta_pi_match.residuals[holdout]
        theta_pi_global_rms = theta_pi_match.rms
        theta_pi_global_max = theta_pi_match.maximum
        theta_pi_training_rms = _rms(theta_pi_training)
        theta_pi_training_max = float(np.max(theta_pi_training))
        theta_pi_holdout_rms = _rms(theta_pi_holdout)
        theta_pi_holdout_max = float(np.max(theta_pi_holdout))

    certified_bound = (
        continuum_certificate.lower_bound
        if continuum_certificate is not None
        else float("nan")
    )
    certified_safe = (
        continuum_certificate is not None
        and characteristic.shift < continuum_certificate.lower_bound
    )

    return SelectedDivisorAlignment(
        model=model,
        support=4.0 * characteristic.radius,
        dimension=characteristic.dimension,
        shift=characteristic.shift,
        shift_role=shift_role,
        measured_metric_floor=float(measured_floor),
        certified_continuum_lower_bound=certified_bound,
        continuum_shift_certified_safe=certified_safe,
        continuum_certificate_provenance=(
            continuum_certificate.provenance
            if continuum_certificate is not None
            else "none for this support/model"
        ),
        continuum_certificate_scope=(
            continuum_certificate.scope + "; not an all-support certificate"
            if continuum_certificate is not None
            else "no applicable certificate; full-space safety not asserted"
        ),
        divisor_source=divisor_source,
        divisor_count=int(values.size),
        training_count=int(train.size),
        holdout_count=int(holdout.size),
        circular_phase=circular.phase,
        circular_resultant_length=circular.resultant_length,
        circular_training_phasor_rms=circular.residual_rms,
        circular_training_phasor_max=circular.residual_max,
        circular_global_match_rms=(
            circular_global.rms if circular_global is not None else float("inf")
        ),
        circular_global_match_max=(
            circular_global.maximum if circular_global is not None else float("inf")
        ),
        optimized_phase=optimization.phase,
        optimizer_training_rms=optimization.training_match_rms,
        optimizer_training_max=optimization.training_match_max,
        optimizer_approximate_root_count=optimization.approximate_root_count,
        optimizer_evaluations=optimization.evaluations,
        optimizer_phase_grid_size=optimization.phase_grid_size,
        optimizer_refinement_levels=optimization.refinement_levels,
        optimizer_root_grid_spacing=optimization.root_grid_spacing,
        optimized_training_phasor_rms=_rms(optimized_phasor_residuals[train]),
        optimized_training_phasor_max=float(
            np.max(optimized_phasor_residuals[train])
        ),
        optimized_holdout_phasor_rms=_rms(optimized_phasor_residuals[holdout]),
        optimized_holdout_phasor_max=float(
            np.max(optimized_phasor_residuals[holdout])
        ),
        optimized_training_characteristic_rms=_rms(
            characteristic_residuals[train]
        ),
        optimized_training_characteristic_max=float(
            np.max(characteristic_residuals[train])
        ),
        optimized_holdout_characteristic_rms=_rms(
            characteristic_residuals[holdout]
        ),
        optimized_holdout_characteristic_max=float(
            np.max(characteristic_residuals[holdout])
        ),
        train_only_injective_rms=train_only.rms,
        train_only_injective_max=train_only.maximum,
        global_injective_rms=global_match.rms,
        global_injective_max=global_match.maximum,
        global_training_injective_rms=_rms(global_training_residuals),
        global_training_injective_max=float(np.max(global_training_residuals)),
        global_holdout_injective_rms=_rms(global_holdout_residuals),
        global_holdout_injective_max=float(np.max(global_holdout_residuals)),
        finite_root_count=int(optimized_roots.size),
        roots_below_first_divisor=int(np.sum(optimized_roots < values[0])),
        roots_inside_divisor_span=int(
            np.sum((optimized_roots >= values[0]) & (optimized_roots <= values[-1]))
        ),
        roots_above_last_divisor=int(np.sum(optimized_roots > values[-1])),
        matched_root_index_min=int(matched_indices[0]),
        matched_root_index_max=int(matched_indices[-1]),
        matched_root_index_span=int(matched_indices[-1] - matched_indices[0] + 1),
        skipped_roots_inside_matched_span=int(
            matched_indices[-1] - matched_indices[0] + 1 - values.size
        ),
        maximum_matched_index_jump=int(np.max(index_differences)),
        training_matched_root_indices=";".join(
            str(int(index)) for index in matched_indices[train]
        ),
        holdout_matched_root_indices=";".join(
            str(int(index)) for index in matched_indices[holdout]
        ),
        symmetry_theta_zero_has_root_at_zero=bool(
            theta_zero_center_residual[0] < 1e-10
        ),
        symmetry_theta_zero_global_rms=theta_zero_global_rms,
        symmetry_theta_zero_global_max=theta_zero_global_max,
        symmetry_theta_zero_training_rms=theta_zero_training_rms,
        symmetry_theta_zero_training_max=theta_zero_training_max,
        symmetry_theta_zero_holdout_rms=theta_zero_holdout_rms,
        symmetry_theta_zero_holdout_max=theta_zero_holdout_max,
        symmetry_theta_zero_finite_root_count=int(theta_zero_roots.size),
        symmetry_theta_pi_global_rms=theta_pi_global_rms,
        symmetry_theta_pi_global_max=theta_pi_global_max,
        symmetry_theta_pi_training_rms=theta_pi_training_rms,
        symmetry_theta_pi_training_max=theta_pi_training_max,
        symmetry_theta_pi_holdout_rms=theta_pi_holdout_rms,
        symmetry_theta_pi_holdout_max=theta_pi_holdout_max,
        symmetry_theta_pi_finite_root_count=int(theta_pi_roots.size),
        symmetry_constraint_scope=(
            "E(-x)=E(x)^-1: exact +/- divisor alignment forces theta=0 or pi; "
            "theta=0 has a central root (extraneous for direct Xi, but not "
            "automatically for the proposed z^2 xi/xi-prime target); both "
            "phases are separate finite controls, not restrictions on an "
            "asymptotic fit"
        ),
        root_scan_min=float(root_scan_min),
        root_scan_max=float(scan_max),
    )


def result_row(result: SelectedDivisorAlignment) -> dict[str, object]:
    row = dict(vars(result))
    row["shift_numerically_safe"] = result.shift < result.measured_metric_floor
    row["optimizer_scope"] = "declared-phase-grid-and-root-resolution"
    row["status"] = "finite-Galerkin-diagnostic"
    return row


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--supports", type=float, nargs="+", default=[1.75, 2.485, 2.996]
    )
    parser.add_argument("--dimensions", type=int, nargs="+", default=[8, 10, 12])
    parser.add_argument("--shift", type=float, default=-0.25)
    parser.add_argument("--conditioning-control-shift", type=float, default=-1.0)
    parser.add_argument("--skip-conditioning-control", action="store_true")
    parser.add_argument("--zero-count", type=int, default=12)
    parser.add_argument("--zero-dps", type=int, default=50)
    parser.add_argument("--form-dps", type=int, default=35)
    parser.add_argument("--root-samples", type=int, default=30001)
    parser.add_argument("--root-margin", type=float, default=40.0)
    parser.add_argument("--phase-grid-size", type=int, default=129)
    parser.add_argument("--phase-refinements", type=int, default=2)
    parser.add_argument("--refinement-grid-size", type=int, default=33)
    args = parser.parse_args()
    if args.zero_count < 5:
        parser.error("use at least five zeta ordinates")
    if args.root_samples < 1001:
        parser.error("the root scan needs at least 1001 samples")

    ordinates = first_critical_line_ordinates(args.zero_count, args.zero_dps)
    scan_max = float(ordinates[-1] + args.root_margin)
    results: list[SelectedDivisorAlignment] = []

    # Positive control: roots generated by one scalar-metric phase must recover
    # that planted phase and remain distinct under the global rematching.
    control_dimension = max(args.dimensions)
    control_radius = args.supports[0] / 4.0
    control_metric = scalar_coercive_metric(control_dimension)
    control_floor = measured_metric_floor(control_metric, args.shift)
    control = ShiftedCharacteristic(
        control_metric, control_radius, args.shift, basis_kind="legendre"
    )
    planted_phase = 0.37
    control_scan_max = max(
        scan_max,
        float((args.zero_count + 2) * np.pi / control_radius),
    )
    control_roots = control.real_zeros(
        planted_phase, 0.0, control_scan_max, samples=args.root_samples
    )
    if control_roots.size < args.zero_count:
        raise RuntimeError("the scalar control produced too few finite roots")
    results.append(
        selected_divisor_alignment(
            "scalar-self-spectrum-control",
            control,
            control_floor,
            "primary",
            control_roots[: args.zero_count],
            "finite-characteristic-roots",
            continuum_certificate=ContinuumPositivityCertificate(
                endpoint=float("inf"),
                lower_bound=5.0,
                provenance="exact scalar metric control",
                scope="synthetic scalar control only",
            ),
            root_scan_min=0.0,
            root_scan_max=control_scan_max,
            root_samples=args.root_samples,
            phase_grid_size=args.phase_grid_size,
            refinement_levels=args.phase_refinements,
            refinement_grid_size=args.refinement_grid_size,
        )
    )

    for support in args.supports:
        for dimension in args.dimensions:
            high_precision_metric = spectral_form(
                support, dimension, dps=args.form_dps
            )
            metric = np.asarray(high_precision_metric.tolist(), dtype=float)
            shifts = [(args.shift, "primary")]
            if (
                not args.skip_conditioning_control
                and args.conditioning_control_shift != args.shift
            ):
                shifts.append(
                    (args.conditioning_control_shift, "conditioning-robustness")
                )
            certificate = continuum_positivity_certificate(support)
            for shift, shift_role in shifts:
                floor = measured_metric_floor(metric, shift)
                characteristic = ShiftedCharacteristic(
                    metric, support / 4.0, shift, basis_kind="legendre"
                )
                results.append(
                    selected_divisor_alignment(
                        "completed-Weil-selected-zeta-divisor",
                        characteristic,
                        floor,
                        shift_role,
                        ordinates,
                        (
                            "Platt/LMFDB rigorously isolated line zeros; "
                            f"source precision={_PLATT_LMFDB_ABSOLUTE_PRECISION}; "
                            "float64 centers used by diagnostic"
                        ),
                        continuum_certificate=certificate,
                        root_scan_min=0.0,
                        root_scan_max=scan_max,
                        root_samples=args.root_samples,
                        phase_grid_size=args.phase_grid_size,
                        refinement_levels=args.phase_refinements,
                        refinement_grid_size=args.refinement_grid_size,
                    )
                )

    rows = [result_row(result) for result in results]
    writer = csv.DictWriter(sys.stdout, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)


if __name__ == "__main__":
    main()
