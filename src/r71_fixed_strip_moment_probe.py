#!/usr/bin/env python3
"""D-rated finite moment scout for the completed R71 fixed-strip sprint.

The minimum-width program asks whether a coefficient-specific completed
moment estimate can beat the generic length barrier.  This script makes a
small finite comparison; it proves no asymptotic estimate.

For each scale it imports the faithful tapered microblock from
``r71_large_value_width_probe``.  Every grouped product whose compact
profile intersects the block is transformed separately, including boundary
profiles, and the exact rank-two center is appended as one signed channel.
The sum of these channels is checked against the directly transformed
completed field.

On ``[-T,T]`` the script compares

    M_p(T) = integral |sum_j F_j(t)|^p dt,     p=4,6,

with three deliberately different baselines.

* A longer finite frequency window measures how much of the sampled moment
  is concentrated near the origin.  It is not called a whole-line limit.
* A Bohr-type phase baseline independently randomizes the phase of every
  already-completed channel at each frequency.  If
  ``S_r=sum_j |F_j|^r``, the exact phase expectations are

      E|sum e^(i theta_j)F_j|^4 = 2 S_2^2-S_4,
      E|sum e^(i theta_j)F_j|^6 = 6 S_2^3-9 S_2 S_4+4 S_6.

* A collision-aware multiplicative-energy baseline gives each grouped
  product its actual integer label, assigns the continuum center the formal
  label one, and groups pair or triple monomials with exactly equal product.
  This retains the finite multiplicative relations missed by independent
  atom phases.  The formal center label makes it a comparator, not a Haar
  theorem for the completed continuum field.

The center is therefore retained, not estimated or discarded, although the
phase randomization is only a comparator.  Ratios above one diagnose coherent
reinforcement relative to this comparator; ratios below one diagnose
cancellation.  Fits of ``log(moment)`` against ``log(scale)`` are labelled
candidate finite-range exponents.  They are D-rated numerical evidence and
must not be read as power laws, zero-free regions, or evidence for RH.

The optional cutoff-grid stress test is intentionally adversarial.  It asks
whether either tempting finite domination survives changes of the Vaughan
cutoff.  A ratio above one is reported as a finite counterexample to that
proposed domination, not as evidence for large values at asymptotic scale.
"""

from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np
from numpy.polynomial.legendre import leggauss

from r71_large_value_width_probe import (
    CompletedMicroblock,
    build_completed_microblock,
    centered_transform,
    compact_taper,
)
from ward_nonlocal_covariance_probe import compact_profile


SUPPORTED_MOMENT_POWERS = (4, 6)


def _validate_power(power: int) -> None:
    if power not in SUPPORTED_MOMENT_POWERS:
        raise ValueError("this diagnostic supports moment powers four and six")


def bohr_phase_moment_density(
    channel_values: np.ndarray, power: int
) -> np.ndarray:
    """Return the exact independent-phase ``p``-moment at each frequency.

    ``channel_values`` has shape ``(frequency_count, channel_count)``.  The
    last channel may be the signed center; the formula depends only on
    channel moduli, as an independent-phase comparator should.
    """

    _validate_power(power)
    values = np.asarray(channel_values, dtype=complex)
    if values.ndim != 2 or values.shape[1] < 1:
        raise ValueError("channel_values must be a nonempty two-dimensional array")
    if not np.all(np.isfinite(values)):
        raise ValueError("channel_values must be finite")
    squared = np.abs(values) ** 2
    second_sum = np.sum(squared, axis=1)
    fourth_sum = np.sum(squared**2, axis=1)
    if power == 4:
        answer = 2.0 * second_sum**2 - fourth_sum
    else:
        sixth_sum = np.sum(squared**3, axis=1)
        answer = (
            6.0 * second_sum**3
            - 9.0 * second_sum * fourth_sum
            + 4.0 * sixth_sum
        )
    # The expressions are nonnegative exactly.  Clip only roundoff-scale
    # negative noise and reject a materially inconsistent result.
    scale = max(1.0, float(np.max(np.abs(answer))))
    tolerance = 100.0 * np.finfo(float).eps * scale
    if float(np.min(answer)) < -tolerance:
        raise RuntimeError("the Bohr phase-moment formula became negative")
    return np.maximum(answer, 0.0)


def _multiset_multiplicity(indices: tuple[int, ...]) -> int:
    """Number of ordered tuples represented by one sorted multiset."""

    answer = math.factorial(len(indices))
    for index in set(indices):
        answer //= math.factorial(indices.count(index))
    return answer


def multiplicative_energy_moment_density(
    channel_values: np.ndarray,
    channel_labels: Iterable[int],
    power: int,
    chunk_size: int = 32,
) -> np.ndarray:
    """Return a collision-aware finite multiplicative-energy comparator.

    Give the arithmetic channels their grouped-product labels and give the
    completed continuum center the formal label ``1``.  For ``m=power/2``
    this computes

    ``sum_r |sum_(n_1...n_m=r) prod_j F_(n_j)(t)|^2``,

    with ordered tuples.  The implementation starts from independent channel
    phases and adds exactly the cross terms between *different* channel
    multisets with equal integer product.  This is the exact Haar moment of
    the resulting formal finite character polynomial.  Because the actual
    completed center is a continuum transform rather than a Dirichlet atom,
    assigning it label one is only a finite comparator, not a Haar theorem
    for the completed transform and not an asymptotic estimate.
    """

    _validate_power(power)
    values = np.asarray(channel_values, dtype=complex)
    labels = tuple(channel_labels)
    if values.ndim != 2 or values.shape[1] < 1:
        raise ValueError("channel_values must be a nonempty two-dimensional array")
    if not np.all(np.isfinite(values)):
        raise ValueError("channel_values must be finite")
    if len(labels) != values.shape[1]:
        raise ValueError("channel_labels must match the channel count")
    if any(
        not isinstance(label, (int, np.integer))
        or isinstance(label, (bool, np.bool_))
        or label < 1
        for label in labels
    ):
        raise ValueError("channel labels must be positive integers")
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")

    degree = power // 2
    product_groups: dict[int, list[tuple[tuple[int, ...], int]]] = {}
    for indices in itertools.combinations_with_replacement(
        range(values.shape[1]), degree
    ):
        product = math.prod(labels[index] for index in indices)
        product_groups.setdefault(product, []).append(
            (indices, _multiset_multiplicity(indices))
        )

    # If every integer product identifies one channel multiset, this reduces
    # exactly to independent phases.  Only genuine product collisions need
    # to be evaluated below.
    collision_groups = [
        group for group in product_groups.values() if len(group) > 1
    ]
    answer = bohr_phase_moment_density(values, power)
    if not collision_groups:
        return answer

    flat_indices: list[tuple[int, ...]] = []
    multiplicities: list[int] = []
    group_starts: list[int] = []
    for group in collision_groups:
        group_starts.append(len(flat_indices))
        for indices, multiplicity in group:
            flat_indices.append(indices)
            multiplicities.append(multiplicity)
    index_array = np.asarray(flat_indices, dtype=np.intp)
    multiplicity_array = np.asarray(multiplicities, dtype=float)
    start_array = np.asarray(group_starts, dtype=np.intp)

    corrected = answer.copy()
    for start in range(0, len(values), chunk_size):
        local = values[start : start + chunk_size]
        monomials = (
            multiplicity_array[np.newaxis, :]
            * local[:, index_array[:, 0]]
        )
        for position in range(1, degree):
            monomials *= local[:, index_array[:, position]]
        coherent_groups = np.add.reduceat(monomials, start_array, axis=1)
        diagonal_groups = np.add.reduceat(
            np.abs(monomials) ** 2, start_array, axis=1
        )
        correction = np.sum(
            np.abs(coherent_groups) ** 2 - diagonal_groups, axis=1
        )
        corrected[start : start + len(local)] += correction.real

    scale = max(1.0, float(np.max(np.abs(corrected))))
    tolerance = 500.0 * np.finfo(float).eps * scale
    if not np.all(np.isfinite(corrected)) or float(np.min(corrected)) < -tolerance:
        raise RuntimeError("the multiplicative-energy comparator became invalid")
    return np.maximum(corrected, 0.0)


def _local_profile_quadrature(
    model: CompletedMicroblock,
    product: int,
    coefficient: float,
    gaussian_order: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Quadrature nodes and signed amplitudes for one grouped product."""

    logarithm = math.log(product)
    width = model.coboundary_width
    lower = max(model.lower, logarithm - width)
    upper = min(model.upper, logarithm + width)
    if upper <= lower:
        return np.empty(0), np.empty(0)
    points = {lower, upper}
    for index in range(-model.order, model.order + 1):
        point = logarithm + index * model.step
        if lower < point < upper:
            points.add(point)
    boundaries = sorted(points)
    base_nodes, base_weights = leggauss(gaussian_order)
    nodes: list[np.ndarray] = []
    amplitudes: list[np.ndarray] = []
    for left, right in zip(boundaries, boundaries[1:]):
        midpoint = (left + right) / 2.0
        radius = (right - left) / 2.0
        local_nodes = midpoint + radius * base_nodes
        local_weights = radius * base_weights
        profile = coefficient * compact_profile(
            local_nodes,
            logarithm,
            model.step,
            model.order,
            model.coboundary_width,
            1.0 / math.sqrt(product),
        ) / model.window_l2_norm
        taper = compact_taper(
            local_nodes,
            model.logarithmic_center,
            model.half_width,
            model.taper_power,
        )
        nodes.append(local_nodes - model.logarithmic_center)
        amplitudes.append(local_weights * taper * profile)
    return np.concatenate(nodes), np.concatenate(amplitudes)


def _transform_atomic_measure(
    centered_nodes: np.ndarray,
    amplitudes: np.ndarray,
    frequencies: np.ndarray,
    chunk_size: int,
) -> np.ndarray:
    if len(centered_nodes) == 0:
        return np.zeros(len(frequencies), dtype=complex)
    answer = np.empty(len(frequencies), dtype=complex)
    for start in range(0, len(frequencies), chunk_size):
        local = frequencies[start : start + chunk_size]
        answer[start : start + len(local)] = (
            np.exp(-1j * local[:, np.newaxis] * centered_nodes)
            @ amplitudes
        )
    return answer


def completed_channel_transforms(
    model: CompletedMicroblock,
    frequencies: np.ndarray | Iterable[float],
    gaussian_order: int | None = None,
    chunk_size: int = 2048,
) -> np.ndarray:
    """Return every grouped-product transform plus the signed center.

    Boundary profiles are integrated on their actual intersection with the
    tapered block.  The final column is ``-Fourier[taper*center]`` so summing
    every column reconstructs the completed transform.
    """

    frequency_array = np.asarray(tuple(frequencies), dtype=float)
    if frequency_array.ndim != 1 or not np.all(np.isfinite(frequency_array)):
        raise ValueError("frequencies must be a finite one-dimensional iterable")
    if len(frequency_array) < 1:
        raise ValueError("at least one frequency is required")
    if gaussian_order is None:
        gaussian_order = model.gaussian_order
    if gaussian_order < 8:
        raise ValueError("gaussian_order must be at least eight")
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")

    channel_count = len(model.active_product_values) + 1
    channels = np.empty((len(frequency_array), channel_count), dtype=complex)
    for column, (product, coefficient) in enumerate(
        zip(model.active_product_values, model.grouped_coefficients)
    ):
        nodes, amplitudes = _local_profile_quadrature(
            model, product, coefficient, gaussian_order
        )
        channels[:, column] = _transform_atomic_measure(
            nodes, amplitudes, frequency_array, chunk_size
        )
    channels[:, -1] = -np.asarray(
        centered_transform(model, frequency_array, component="center")
    )
    return channels


@dataclass(frozen=True)
class FourthMomentStripGate:
    """Finite-height Sobolev ledger for a fourth-moment saving."""

    kappa: float
    derivative_order: int
    height_exponent_tau: float
    energy_saving_eta: float
    energy_upper_exponent: float
    right_boundary: float


def fourth_moment_strip_gate(
    kappa: float, derivative_order: int
) -> FourthMomentStripGate:
    """Calibrate the finite-height fourth-moment/Sobolev implication.

    This is the fallback when the fourth moment is known only through the
    optimized expanding height window.  A whole-line moment admits the sharp
    ``kappa/4`` implication recorded by ``full_moment_strip_gate``.  Neither
    function asserts that the required arithmetic moment estimate is known.
    """

    if not math.isfinite(kappa) or not 0.0 < kappa < 2.0:
        raise ValueError("kappa must be finite and strictly between zero and two")
    if (
        not isinstance(derivative_order, int)
        or isinstance(derivative_order, bool)
        or derivative_order < 1
    ):
        raise ValueError("derivative_order must be a positive integer")
    denominator = 4 * derivative_order + 1
    tau = kappa / denominator
    eta = derivative_order * tau
    return FourthMomentStripGate(
        kappa=kappa,
        derivative_order=derivative_order,
        height_exponent_tau=tau,
        energy_saving_eta=eta,
        energy_upper_exponent=1.0 - 2.0 * eta,
        right_boundary=1.0 - eta,
    )


@dataclass(frozen=True)
class FullMomentStripGate:
    """Sharp full-frequency moment-to-strip exponent ledger."""

    kappa: float
    moment_power: int
    baseline_moment_exponent: float
    maximum_displacement: float
    strip_width: float
    right_boundary: float


def full_moment_strip_gate(
    kappa: float, moment_power: int = 4
) -> FullMomentStripGate:
    """Calibrate a whole-line ``U_p <= N^(p/2-kappa)`` input.

    For every fixed ``p>=2`` the continuously translated completed local
    moment has exponential growth rate ``p*Delta``.  Consequently the input
    gives ``Delta <= 1/2-kappa/p`` and the zero-free boundary
    ``Re(rho) <= 1-kappa/p``.  This records the proved analytic implication,
    not the still-open arithmetic moment estimate.
    """

    if (
        not isinstance(moment_power, int)
        or isinstance(moment_power, bool)
        or moment_power < 2
    ):
        raise ValueError("moment_power must be an integer of at least two")
    maximum_kappa = moment_power / 2.0
    if not math.isfinite(kappa) or not 0.0 < kappa < maximum_kappa:
        raise ValueError(
            "kappa must be finite and lie strictly between zero and p/2"
        )
    strip_width = kappa / moment_power
    return FullMomentStripGate(
        kappa=kappa,
        moment_power=moment_power,
        baseline_moment_exponent=maximum_kappa,
        maximum_displacement=0.5 - strip_width,
        strip_width=strip_width,
        right_boundary=1.0 - strip_width,
    )


@dataclass(frozen=True)
class LocalMomentComparison:
    """One completed-versus-baseline comparison at fixed ``p`` and ``T``."""

    power: int
    height: float
    completed_moment: float
    bohr_phase_moment: float
    completed_to_bohr_ratio: float
    multiplicative_energy_moment: float
    completed_to_multiplicative_energy_ratio: float
    fraction_of_long_window_moment: float
    local_mean_to_long_mean_ratio: float
    candidate_moment_exponent: float
    candidate_coherence_exponent: float
    candidate_multiplicative_coherence_exponent: float


@dataclass(frozen=True)
class ScaleMomentAudit:
    """All finite moment diagnostics for one arithmetic scale."""

    scale: float
    cutoff: int
    logarithmic_scale: float
    active_product_count: int
    channel_count: int
    quadrature_size: int
    frequency_step: float
    long_height: float
    channel_completion_error: float
    comparisons: tuple[LocalMomentComparison, ...]

    def comparison(self, power: int, height: float) -> LocalMomentComparison:
        for item in self.comparisons:
            if item.power == power and math.isclose(
                item.height, height, rel_tol=0.0, abs_tol=1.0e-12
            ):
                return item
        raise KeyError((power, height))


@dataclass(frozen=True)
class MomentPowerFit:
    """Finite-range log--log slopes; these are not asymptotic exponents."""

    power: int
    height: float
    scale_count: int
    completed_moment_slope: float
    completed_moment_r_squared: float
    coherence_ratio_slope: float
    coherence_ratio_r_squared: float
    multiplicative_coherence_ratio_slope: float
    multiplicative_coherence_ratio_r_squared: float


@dataclass(frozen=True)
class FixedStripMomentScan:
    """Multi-scale D-rated audit and candidate power fits."""

    audits: tuple[ScaleMomentAudit, ...]
    fits: tuple[MomentPowerFit, ...]
    largest_fourth_moment_concentration: float
    largest_sixth_moment_concentration: float
    largest_fourth_multiplicative_concentration: float
    largest_sixth_multiplicative_concentration: float


@dataclass(frozen=True)
class CutoffConcentrationPeak:
    """Largest finite completed/phase ratio for one moment power."""

    power: int
    baseline: str
    scale: float
    cutoff: int
    height: float
    ratio: float
    active_product_count: int


@dataclass(frozen=True)
class CutoffMomentStress:
    """D-rated Cartesian scale-by-cutoff stress test."""

    scales: tuple[float, ...]
    cutoffs: tuple[int, ...]
    audits: tuple[ScaleMomentAudit, ...]
    peaks: tuple[CutoffConcentrationPeak, ...]
    phase_baseline_exceedance_count: int
    multiplicative_baseline_exceedance_count: int

    def peak(
        self, power: int, baseline: str = "phase"
    ) -> CutoffConcentrationPeak:
        _validate_power(power)
        if baseline not in ("phase", "multiplicative"):
            raise ValueError("baseline must be 'phase' or 'multiplicative'")
        for item in self.peaks:
            if item.power == power and item.baseline == baseline:
                return item
        raise KeyError((power, baseline))


def _integral_on_symmetric_window(
    frequencies: np.ndarray, values: np.ndarray, height: float
) -> float:
    mask = np.abs(frequencies) <= height + 1.0e-12
    selected_frequencies = frequencies[mask]
    if len(selected_frequencies) < 3:
        raise ValueError("frequency grid is too coarse for a requested height")
    return float(np.trapz(values[mask], selected_frequencies))


def audit_scale_moments(
    scale: float,
    cutoff: int | None = None,
    heights: tuple[float, ...] = (20.0, 40.0, 80.0),
    long_height: float = 160.0,
    frequency_step: float = 0.1,
    step: float = 0.04,
    order: int = 1,
    half_width: float | None = None,
    taper_power: int = 2,
    gaussian_order: int = 16,
) -> ScaleMomentAudit:
    """Compare completed fourth/sixth moments at one finite scale."""

    if not math.isfinite(scale) or scale <= 4.0:
        raise ValueError("scale must be finite and exceed four")
    if cutoff is None:
        cutoff = max(1, math.floor(scale ** (3.0 / 8.0)))
    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    if not heights:
        raise ValueError("provide at least one local height")
    if any(not math.isfinite(value) or value <= 0.0 for value in heights):
        raise ValueError("local heights must be finite and positive")
    if tuple(sorted(set(heights))) != heights:
        raise ValueError("heights must be strictly increasing")
    if not math.isfinite(long_height) or long_height <= heights[-1]:
        raise ValueError("long_height must exceed every local height")
    if not math.isfinite(frequency_step) or frequency_step <= 0.0:
        raise ValueError("frequency_step must be finite and positive")

    model = build_completed_microblock(
        scale=scale,
        cutoff=cutoff,
        step=step,
        order=order,
        half_width=half_width,
        taper_power=taper_power,
        gaussian_order=gaussian_order,
    )
    half_count = math.ceil(long_height / frequency_step)
    regular_frequencies = frequency_step * np.arange(
        -half_count, half_count + 1, dtype=float
    )
    exact_endpoints = np.asarray(
        [sign * height for height in (*heights, long_height) for sign in (-1, 1)]
    )
    frequencies = np.unique(np.concatenate([regular_frequencies, exact_endpoints]))
    channels = completed_channel_transforms(
        model, frequencies, gaussian_order=gaussian_order
    )
    completed_from_channels = np.sum(channels, axis=1)
    completed_direct = np.asarray(centered_transform(model, frequencies))
    completion_error = float(
        np.max(np.abs(completed_from_channels - completed_direct))
    )

    completed_densities = {
        power: np.abs(completed_from_channels) ** power
        for power in SUPPORTED_MOMENT_POWERS
    }
    bohr_densities = {
        power: bohr_phase_moment_density(channels, power)
        for power in SUPPORTED_MOMENT_POWERS
    }
    channel_labels = (*model.active_product_values, 1)
    multiplicative_densities = {
        power: multiplicative_energy_moment_density(
            channels, channel_labels, power
        )
        for power in SUPPORTED_MOMENT_POWERS
    }
    long_moments = {
        power: _integral_on_symmetric_window(
            frequencies, completed_densities[power], long_height
        )
        for power in SUPPORTED_MOMENT_POWERS
    }

    comparisons: list[LocalMomentComparison] = []
    for power in SUPPORTED_MOMENT_POWERS:
        for height in (*heights, long_height):
            completed_moment = _integral_on_symmetric_window(
                frequencies, completed_densities[power], height
            )
            bohr_moment = _integral_on_symmetric_window(
                frequencies, bohr_densities[power], height
            )
            multiplicative_moment = _integral_on_symmetric_window(
                frequencies, multiplicative_densities[power], height
            )
            if (
                bohr_moment <= 0.0
                or multiplicative_moment <= 0.0
                or completed_moment <= 0.0
            ):
                raise RuntimeError("a finite moment baseline is not positive")
            ratio = completed_moment / bohr_moment
            multiplicative_ratio = completed_moment / multiplicative_moment
            long_fraction = completed_moment / long_moments[power]
            mean_ratio = long_fraction * long_height / height
            comparisons.append(
                LocalMomentComparison(
                    power=power,
                    height=height,
                    completed_moment=completed_moment,
                    bohr_phase_moment=bohr_moment,
                    completed_to_bohr_ratio=ratio,
                    multiplicative_energy_moment=multiplicative_moment,
                    completed_to_multiplicative_energy_ratio=(
                        multiplicative_ratio
                    ),
                    fraction_of_long_window_moment=long_fraction,
                    local_mean_to_long_mean_ratio=mean_ratio,
                    candidate_moment_exponent=(
                        math.log(completed_moment) / math.log(scale)
                    ),
                    candidate_coherence_exponent=(
                        math.log(ratio) / math.log(scale)
                    ),
                    candidate_multiplicative_coherence_exponent=(
                        math.log(multiplicative_ratio) / math.log(scale)
                    ),
                )
            )

    return ScaleMomentAudit(
        scale=scale,
        cutoff=cutoff,
        logarithmic_scale=math.log(scale),
        active_product_count=len(model.active_product_values),
        channel_count=channels.shape[1],
        quadrature_size=model.quadrature_size,
        frequency_step=frequency_step,
        long_height=long_height,
        channel_completion_error=completion_error,
        comparisons=tuple(comparisons),
    )


def _linear_fit(x_values: np.ndarray, y_values: np.ndarray) -> tuple[float, float]:
    if len(x_values) < 2:
        return math.nan, math.nan
    design = np.column_stack([np.ones(len(x_values)), x_values])
    coefficients, *_ = np.linalg.lstsq(design, y_values, rcond=None)
    fitted = design @ coefficients
    residual = float(np.sum((y_values - fitted) ** 2))
    centered = float(np.sum((y_values - np.mean(y_values)) ** 2))
    r_squared = 1.0 if centered == 0.0 and residual == 0.0 else (
        1.0 - residual / centered if centered > 0.0 else math.nan
    )
    return float(coefficients[1]), r_squared


def fit_candidate_power_exponents(
    audits: tuple[ScaleMomentAudit, ...],
    heights: tuple[float, ...],
) -> tuple[MomentPowerFit, ...]:
    """Fit finite-range candidate slopes for moments and coherence ratios."""

    if len(audits) < 2:
        return ()
    logarithmic_scales = np.log([audit.scale for audit in audits])
    fits: list[MomentPowerFit] = []
    for power in SUPPORTED_MOMENT_POWERS:
        for height in heights:
            items = [audit.comparison(power, height) for audit in audits]
            moment_slope, moment_r2 = _linear_fit(
                logarithmic_scales,
                np.log([item.completed_moment for item in items]),
            )
            coherence_slope, coherence_r2 = _linear_fit(
                logarithmic_scales,
                np.log([item.completed_to_bohr_ratio for item in items]),
            )
            multiplicative_slope, multiplicative_r2 = _linear_fit(
                logarithmic_scales,
                np.log(
                    [
                        item.completed_to_multiplicative_energy_ratio
                        for item in items
                    ]
                ),
            )
            fits.append(
                MomentPowerFit(
                    power=power,
                    height=height,
                    scale_count=len(audits),
                    completed_moment_slope=moment_slope,
                    completed_moment_r_squared=moment_r2,
                    coherence_ratio_slope=coherence_slope,
                    coherence_ratio_r_squared=coherence_r2,
                    multiplicative_coherence_ratio_slope=(
                        multiplicative_slope
                    ),
                    multiplicative_coherence_ratio_r_squared=(
                        multiplicative_r2
                    ),
                )
            )
    return tuple(fits)


def scan_fixed_strip_moments(
    scales: tuple[float, ...] = (59.0, 127.0, 205.0, 500.0),
    cutoffs: tuple[int, ...] | None = None,
    heights: tuple[float, ...] = (20.0, 40.0, 80.0),
    long_height: float = 160.0,
    frequency_step: float = 0.1,
    step: float = 0.04,
    order: int = 1,
    half_width: float | None = None,
    taper_power: int = 2,
    gaussian_order: int = 16,
) -> FixedStripMomentScan:
    """Run the D-rated moment comparison on several scales and cutoffs."""

    if len(scales) < 1:
        raise ValueError("provide at least one scale")
    if tuple(sorted(set(scales))) != scales:
        raise ValueError("scales must be strictly increasing")
    if cutoffs is not None and len(cutoffs) != len(scales):
        raise ValueError("cutoffs must have the same length as scales")
    audits: list[ScaleMomentAudit] = []
    for index, scale in enumerate(scales):
        cutoff = None if cutoffs is None else cutoffs[index]
        audits.append(
            audit_scale_moments(
                scale=scale,
                cutoff=cutoff,
                heights=heights,
                long_height=long_height,
                frequency_step=frequency_step,
                step=step,
                order=order,
                half_width=half_width,
                taper_power=taper_power,
                gaussian_order=gaussian_order,
            )
        )
    audit_tuple = tuple(audits)
    fit_heights = (*heights, long_height)
    fits = fit_candidate_power_exponents(audit_tuple, fit_heights)
    fourth = max(
        item.completed_to_bohr_ratio
        for audit in audit_tuple
        for item in audit.comparisons
        if item.power == 4
    )
    sixth = max(
        item.completed_to_bohr_ratio
        for audit in audit_tuple
        for item in audit.comparisons
        if item.power == 6
    )
    multiplicative_fourth = max(
        item.completed_to_multiplicative_energy_ratio
        for audit in audit_tuple
        for item in audit.comparisons
        if item.power == 4
    )
    multiplicative_sixth = max(
        item.completed_to_multiplicative_energy_ratio
        for audit in audit_tuple
        for item in audit.comparisons
        if item.power == 6
    )
    return FixedStripMomentScan(
        audits=audit_tuple,
        fits=fits,
        largest_fourth_moment_concentration=fourth,
        largest_sixth_moment_concentration=sixth,
        largest_fourth_multiplicative_concentration=multiplicative_fourth,
        largest_sixth_multiplicative_concentration=multiplicative_sixth,
    )


def stress_cutoff_grid(
    scales: tuple[float, ...],
    cutoffs: tuple[int, ...],
    heights: tuple[float, ...] = (20.0, 40.0, 80.0),
    long_height: float = 160.0,
    frequency_step: float = 0.1,
    step: float = 0.04,
    order: int = 1,
    half_width: float | None = None,
    taper_power: int = 2,
    gaussian_order: int = 16,
) -> CutoffMomentStress:
    """Stress both finite comparators on a Cartesian scale-by-cutoff grid.

    This performs no scale fit, since changing the cutoff changes the finite
    object.  It records the largest ratio and counts sampled ratios above one;
    either is only a finite fail-fast diagnostic.
    """

    if not scales or tuple(sorted(set(scales))) != scales:
        raise ValueError("stress scales must be strictly increasing")
    if not cutoffs or tuple(sorted(set(cutoffs))) != cutoffs:
        raise ValueError("stress cutoffs must be strictly increasing")
    if any(cutoff < 1 for cutoff in cutoffs):
        raise ValueError("stress cutoffs must be positive")

    audits = tuple(
        audit_scale_moments(
            scale=scale,
            cutoff=cutoff,
            heights=heights,
            long_height=long_height,
            frequency_step=frequency_step,
            step=step,
            order=order,
            half_width=half_width,
            taper_power=taper_power,
            gaussian_order=gaussian_order,
        )
        for scale in scales
        for cutoff in cutoffs
    )
    peaks: list[CutoffConcentrationPeak] = []
    baseline_attributes = (
        ("phase", "completed_to_bohr_ratio"),
        ("multiplicative", "completed_to_multiplicative_energy_ratio"),
    )
    for baseline, attribute in baseline_attributes:
        for power in SUPPORTED_MOMENT_POWERS:
            audit, comparison = max(
                (
                    (audit, comparison)
                    for audit in audits
                    for comparison in audit.comparisons
                    if comparison.power == power
                ),
                key=lambda pair: getattr(pair[1], attribute),
            )
            peaks.append(
                CutoffConcentrationPeak(
                    power=power,
                    baseline=baseline,
                    scale=audit.scale,
                    cutoff=audit.cutoff,
                    height=comparison.height,
                    ratio=getattr(comparison, attribute),
                    active_product_count=audit.active_product_count,
                )
            )
    phase_exceedance_count = sum(
        comparison.completed_to_bohr_ratio > 1.0 + 1.0e-12
        for audit in audits
        for comparison in audit.comparisons
    )
    multiplicative_exceedance_count = sum(
        comparison.completed_to_multiplicative_energy_ratio > 1.0 + 1.0e-12
        for audit in audits
        for comparison in audit.comparisons
    )
    return CutoffMomentStress(
        scales=scales,
        cutoffs=cutoffs,
        audits=audits,
        peaks=tuple(peaks),
        phase_baseline_exceedance_count=phase_exceedance_count,
        multiplicative_baseline_exceedance_count=(
            multiplicative_exceedance_count
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scales", nargs="+", type=float, default=[59.0, 127.0, 205.0, 500.0]
    )
    parser.add_argument("--cutoffs", nargs="+", type=int)
    parser.add_argument("--heights", nargs="+", type=float, default=[20.0, 40.0, 80.0])
    parser.add_argument("--long-height", type=float, default=160.0)
    parser.add_argument("--frequency-step", type=float, default=0.1)
    parser.add_argument("--step", type=float, default=0.04)
    parser.add_argument("--order", type=int, default=1)
    parser.add_argument("--half-width", type=float)
    parser.add_argument("--taper-power", type=int, default=2)
    parser.add_argument("--gaussian-order", type=int, default=16)
    parser.add_argument(
        "--stress-scales",
        nargs="+",
        type=float,
        default=[127.0],
        help="scales for the Cartesian cutoff stress (default isolates the resonant block)",
    )
    parser.add_argument(
        "--stress-cutoffs",
        nargs="+",
        type=int,
        default=[4, 6, 8, 10],
        help="Cartesian cutoff grid used to fail-fast both comparators",
    )
    parser.add_argument(
        "--skip-cutoff-stress",
        action="store_true",
        help="run only the paired scale scan and candidate fits",
    )
    args = parser.parse_args()
    scales = tuple(args.scales)
    cutoffs = tuple(args.cutoffs) if args.cutoffs is not None else None
    heights = tuple(args.heights)
    scan = scan_fixed_strip_moments(
        scales=scales,
        cutoffs=cutoffs,
        heights=heights,
        long_height=args.long_height,
        frequency_step=args.frequency_step,
        step=args.step,
        order=args.order,
        half_width=args.half_width,
        taper_power=args.taper_power,
        gaussian_order=args.gaussian_order,
    )
    print("rating=D finite numerical diagnostic; no asymptotic claim")
    for audit in scan.audits:
        print(
            f"X={audit.scale:g} Y={audit.cutoff} "
            f"products={audit.active_product_count} channels={audit.channel_count} "
            f"closure={audit.channel_completion_error:.3e}"
        )
        for item in audit.comparisons:
            print(
                f"  p={item.power} T={item.height:g} "
                f"M={item.completed_moment:.9g} "
                f"M/phase={item.completed_to_bohr_ratio:.6g} "
                f"M/mult={item.completed_to_multiplicative_energy_ratio:.6g} "
                f"long-fraction={item.fraction_of_long_window_moment:.6g} "
                f"mean-ratio={item.local_mean_to_long_mean_ratio:.6g} "
                f"candidate-exp={item.candidate_moment_exponent:+.6g}"
            )
    print("candidate finite-range log-log fits")
    for fit in scan.fits:
        print(
            f"  p={fit.power} T={fit.height:g} "
            f"moment-slope={fit.completed_moment_slope:+.6g} "
            f"R2={fit.completed_moment_r_squared:.4f} "
            f"coherence-slope={fit.coherence_ratio_slope:+.6g} "
            f"R2={fit.coherence_ratio_r_squared:.4f} "
            f"mult-slope={fit.multiplicative_coherence_ratio_slope:+.6g} "
            f"R2={fit.multiplicative_coherence_ratio_r_squared:.4f}"
        )
    print(
        "largest completed/Bohr ratios: "
        f"p4={scan.largest_fourth_moment_concentration:.6g} "
        f"p6={scan.largest_sixth_moment_concentration:.6g}"
    )
    print(
        "largest completed/multiplicative-energy ratios: "
        f"p4={scan.largest_fourth_multiplicative_concentration:.6g} "
        f"p6={scan.largest_sixth_multiplicative_concentration:.6g}"
    )
    if not args.skip_cutoff_stress:
        stress = stress_cutoff_grid(
            scales=tuple(args.stress_scales),
            cutoffs=tuple(args.stress_cutoffs),
            heights=heights,
            long_height=args.long_height,
            frequency_step=args.frequency_step,
            step=args.step,
            order=args.order,
            half_width=args.half_width,
            taper_power=args.taper_power,
            gaussian_order=args.gaussian_order,
        )
        print(
            "cutoff-grid finite-baseline stress: "
            f"audits={len(stress.audits)} "
            f"phase-above-one={stress.phase_baseline_exceedance_count} "
            f"multiplicative-above-one="
            f"{stress.multiplicative_baseline_exceedance_count}"
        )
        for peak in stress.peaks:
            print(
                f"  baseline={peak.baseline} p={peak.power} "
                f"peak-ratio={peak.ratio:.6g} "
                f"X={peak.scale:g} Y={peak.cutoff} T={peak.height:g} "
                f"products={peak.active_product_count}"
            )
    print("interpretation=D-rated finite concentration scout only")


if __name__ == "__main__":
    main()
