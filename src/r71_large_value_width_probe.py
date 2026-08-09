#!/usr/bin/env python3
"""Minimum-width and moment gates for the completed R71 microblock.

This module deliberately works with the field on the logarithmic block,
not with a boundary-truncated Dirichlet polynomial.  Fix ``ell = k*h`` and
write

    G(R) = sum_n a_Y(n) n^(-1/2) W_(h,k)(R-log(n)) - z_Y(R),

where ``a_Y = mu_(>Y) * Lambda_(>Y) * 1``, ``W_(h,k)`` is the compact
fixed-step coboundary, and ``z_Y`` is the exact rank-two Type-I center.  For
one microblock ``I=[R_0-B,R_0+B]`` we use the compact polynomial taper

    tau(R) = (1 - ((R-R_0)/B)^2)^p_+,

and numerically evaluate the faithful completed transform

    F(t) = integral_I tau(R) G(R) exp(-itR) dR.             (1)

Every grouped product whose compact profile intersects ``I`` is included,
including products meeting only a boundary strip.  Gaussian quadrature is
split at every arithmetic B-spline knot.  Thus the finite arithmetic field
and its center are exact; only the displayed Fourier integrals are floating
quadrature diagnostics.  Refinement must be checked before interpreting a
small numerical margin.

The harmless phase ``exp(it R_0)`` centers (1):

    F_c(t) = integral_I tau(R) G(R) exp(-it(R-R_0)) dR.

Consequently ``F_c`` has exponential type ``B``, rather than the misleading
raw type ``R_0+B``.  At a *global* real maximum ``M``, Bernstein's inequality
gives

    meas{|F| >= theta M} >= 2(1-theta)/B.                 (2)

At a merely sampled value, the always-valid L1 derivative bound gives the
weaker width reported below.  The module also records the optimized Markov
moment gate and the term-count Turan--Remez diagnostic.  None of these
calculations supplies the missing arithmetic moment estimate, the R71
block-schedule converse, or a proof concerning zeta zeros.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field
from typing import Iterable

import numpy as np
from numpy.polynomial.legendre import leggauss

from type2_block_mechanism_probe import _arithmetic_sieve
from ward_nonlocal_covariance_probe import (
    _center_parameters,
    _grouped_tail_coefficients,
    bspline_cdf,
    compact_profile,
)


def compact_taper(
    values: np.ndarray | float,
    center: float,
    half_width: float,
    power: int = 2,
) -> np.ndarray:
    """Return ``(1-((R-center)/B)^2)^power`` on ``|R-center|<B``.

    ``power >= 2`` makes both the taper and its first derivative vanish at
    the endpoints.  This suppresses the artificial boundary jump created by
    a rectangular block while retaining a completely explicit compact
    support.
    """

    if not math.isfinite(center):
        raise ValueError("center must be finite")
    if not math.isfinite(half_width) or half_width <= 0.0:
        raise ValueError("half_width must be finite and positive")
    if not isinstance(power, int) or isinstance(power, bool) or power < 2:
        raise ValueError("taper power must be an integer at least two")
    array = np.asarray(values, dtype=float)
    scaled = (array - center) / half_width
    base = np.maximum(0.0, 1.0 - scaled * scaled)
    answer = base**power
    return np.where(np.abs(scaled) < 1.0, answer, 0.0)


def compact_window_l2_norm(step: float, order: int) -> float:
    """Return the L2 norm of the unnormalized fixed-step coboundary.

    The integral is split at every B-spline knot.  On each segment the
    window is polynomial of degree ``order``, so Gauss order ``order+1`` is
    sufficient for its square; a slightly larger order is used as a guard.
    """

    if not math.isfinite(step) or step <= 0.0:
        raise ValueError("step must be finite and positive")
    if not isinstance(order, int) or isinstance(order, bool) or order < 1:
        raise ValueError("order must be a positive integer")
    width = order * step
    nodes, weights = leggauss(max(4, order + 2))
    pieces: list[float] = []
    boundaries = np.linspace(-width, width, 2 * order + 1)
    for left, right in zip(boundaries, boundaries[1:]):
        midpoint = (left + right) / 2.0
        radius = (right - left) / 2.0
        local = midpoint + radius * nodes
        window = bspline_cdf(local + width, step, order) - bspline_cdf(
            local, step, order
        )
        pieces.append(float(radius * np.dot(weights, window * window)))
    norm_squared = math.fsum(pieces)
    if not norm_squared > 0.0:
        raise RuntimeError("compact-window norm is not positive")
    return math.sqrt(norm_squared)


@dataclass(frozen=True)
class CompletedMicroblock:
    """Finite cutoff-complete field and a knot-split quadrature ledger."""

    scale: float
    cutoff: int
    step: float
    order: int
    logarithmic_center: float
    half_width: float
    lower: float
    upper: float
    coboundary_width: float
    taper_power: int
    gaussian_order: int
    arithmetic_limit: int
    window_l2_norm: float
    center_j_zero: float
    center_p: float
    center_q: float
    center_alpha: float
    center_beta: float
    active_product_values: tuple[int, ...]
    grouped_coefficients: tuple[float, ...]
    quadrature_nodes: np.ndarray = field(repr=False, compare=False)
    quadrature_weights: np.ndarray = field(repr=False, compare=False)
    taper_values: np.ndarray = field(repr=False, compare=False)
    tail_values: np.ndarray = field(repr=False, compare=False)
    center_values: np.ndarray = field(repr=False, compare=False)
    completed_values: np.ndarray = field(repr=False, compare=False)

    @property
    def quadrature_size(self) -> int:
        return len(self.quadrature_nodes)

    @property
    def tapered_l1_norm(self) -> float:
        return float(
            np.dot(
                self.quadrature_weights,
                np.abs(self.taper_values * self.completed_values),
            )
        )

    @property
    def tapered_l2_energy(self) -> float:
        tapered = self.taper_values * self.completed_values
        return float(np.dot(self.quadrature_weights, tapered * tapered))


def _profile_breakpoints(
    logarithms: Iterable[float],
    lower: float,
    upper: float,
    step: float,
    order: int,
) -> list[float]:
    points = {lower, upper}
    # The two CDFs in W(R-log n) have the combined knots
    # log(n) + j*h, -order <= j <= order.
    for logarithm in logarithms:
        for index in range(-order, order + 1):
            point = logarithm + index * step
            if lower < point < upper:
                points.add(point)
    return sorted(points)


def _block_quadrature(
    breakpoints: list[float], gaussian_order: int
) -> tuple[np.ndarray, np.ndarray]:
    if gaussian_order < 8:
        raise ValueError("gaussian_order must be at least eight")
    base_nodes, base_weights = leggauss(gaussian_order)
    nodes: list[np.ndarray] = []
    weights: list[np.ndarray] = []
    for left, right in zip(breakpoints, breakpoints[1:]):
        if right <= left:
            continue
        midpoint = (left + right) / 2.0
        radius = (right - left) / 2.0
        nodes.append(midpoint + radius * base_nodes)
        weights.append(radius * base_weights)
    if not nodes:
        raise RuntimeError("the microblock quadrature has no segments")
    return np.concatenate(nodes), np.concatenate(weights)


def build_completed_microblock(
    scale: float = 59.0,
    cutoff: int = 4,
    step: float = 0.04,
    order: int = 1,
    half_width: float | None = None,
    taper_power: int = 2,
    gaussian_order: int = 24,
) -> CompletedMicroblock:
    """Build the faithful tapered R71 field on one finite microblock.

    The default half-width is ``4*k*h``.  Unlike a safe-core polynomial,
    this builder includes every nonzero grouped product whose compact
    profile touches the closed microblock.  Boundary profiles are then
    truncated only by the explicit taper in (1).
    """

    if not math.isfinite(scale) or scale <= 4.0:
        raise ValueError("scale must be finite and exceed four")
    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    if not math.isfinite(step) or step <= 0.0:
        raise ValueError("step must be finite and positive")
    if not isinstance(order, int) or isinstance(order, bool) or order < 1:
        raise ValueError("order must be a positive integer")
    coboundary_width = order * step
    if half_width is None:
        half_width = 4.0 * coboundary_width
    if not math.isfinite(half_width) or half_width <= 0.0:
        raise ValueError("half_width must be finite and positive")
    if half_width < coboundary_width:
        raise ValueError("half_width must be at least the compact-window width")
    if not isinstance(taper_power, int) or taper_power < 2:
        raise ValueError("taper_power must be an integer at least two")

    logarithmic_center = math.log(scale)
    lower = logarithmic_center - half_width
    upper = logarithmic_center + half_width
    if upper + coboundary_width > math.log(float(np.finfo(float).max)):
        raise ValueError("the requested arithmetic range overflows float")
    arithmetic_limit = math.ceil(math.exp(upper + coboundary_width)) + 2
    mu, _, mangoldt, _ = _arithmetic_sieve(arithmetic_limit)
    grouped = _grouped_tail_coefficients(
        cutoff, arithmetic_limit, mu, mangoldt
    )

    active_products: list[int] = []
    coefficients: list[float] = []
    logarithms: list[float] = []
    for value in np.flatnonzero(grouped):
        integer = int(value)
        if integer < 1:
            continue
        logarithm = math.log(integer)
        if (
            logarithm + coboundary_width >= lower
            and logarithm - coboundary_width <= upper
        ):
            active_products.append(integer)
            coefficients.append(float(grouped[integer]))
            logarithms.append(logarithm)

    breakpoints = _profile_breakpoints(
        logarithms, lower, upper, step, order
    )
    nodes, weights = _block_quadrature(breakpoints, gaussian_order)
    taper = compact_taper(
        nodes, logarithmic_center, half_width, taper_power
    )
    window_norm = compact_window_l2_norm(step, order)

    tail_values = np.zeros_like(nodes)
    for value, coefficient, logarithm in zip(
        active_products, coefficients, logarithms
    ):
        tail_values += coefficient * compact_profile(
            nodes,
            logarithm,
            step,
            order,
            coboundary_width,
            1.0 / math.sqrt(value),
        )
    tail_values /= window_norm

    j_zero, p_value, q_value = _center_parameters(
        cutoff, step, order, mu, mangoldt
    )
    exponential_width = math.exp(coboundary_width / 2.0)
    alpha = (
        (exponential_width - 1.0) * (j_zero - q_value)
        - exponential_width * p_value * coboundary_width
    )
    beta = -(exponential_width - 1.0) * p_value
    center_values = (
        np.exp(nodes / 2.0) * (alpha + beta * nodes) / window_norm
    )
    completed_values = tail_values - center_values

    return CompletedMicroblock(
        scale=scale,
        cutoff=cutoff,
        step=step,
        order=order,
        logarithmic_center=logarithmic_center,
        half_width=half_width,
        lower=lower,
        upper=upper,
        coboundary_width=coboundary_width,
        taper_power=taper_power,
        gaussian_order=gaussian_order,
        arithmetic_limit=arithmetic_limit,
        window_l2_norm=window_norm,
        center_j_zero=j_zero,
        center_p=p_value,
        center_q=q_value,
        center_alpha=alpha,
        center_beta=beta,
        active_product_values=tuple(active_products),
        grouped_coefficients=tuple(coefficients),
        quadrature_nodes=nodes,
        quadrature_weights=weights,
        taper_values=taper,
        tail_values=tail_values,
        center_values=center_values,
        completed_values=completed_values,
    )


def _component_values(model: CompletedMicroblock, component: str) -> np.ndarray:
    if component == "completed":
        return model.completed_values
    if component == "tail":
        return model.tail_values
    if component == "center":
        return model.center_values
    raise ValueError("component must be 'completed', 'tail', or 'center'")


def centered_transform(
    model: CompletedMicroblock,
    frequencies: np.ndarray | Iterable[float] | float,
    derivative_order: int = 0,
    component: str = "completed",
    chunk_size: int = 2048,
) -> np.ndarray | complex:
    """Evaluate the phase-centered transform and its derivatives.

    The derivative is with respect to frequency.  Centering replaces the
    raw factor ``R`` by ``R-R_0`` before taking moments, which is the
    numerically and analytically relevant width scale.
    """

    if derivative_order < 0 or not isinstance(derivative_order, int):
        raise ValueError("derivative_order must be a nonnegative integer")
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")
    scalar = np.ndim(frequencies) == 0
    frequency_array = np.asarray(frequencies, dtype=float)
    if not np.all(np.isfinite(frequency_array)):
        raise ValueError("frequencies must be finite")
    flat = frequency_array.reshape(-1)
    centered_nodes = model.quadrature_nodes - model.logarithmic_center
    values = _component_values(model, component)
    amplitudes = model.quadrature_weights * model.taper_values * values
    if derivative_order:
        amplitudes = amplitudes * (-1j * centered_nodes) ** derivative_order
    answer = np.empty(len(flat), dtype=complex)
    for start in range(0, len(flat), chunk_size):
        local = flat[start : start + chunk_size]
        phases = np.exp(-1j * local[:, np.newaxis] * centered_nodes)
        answer[start : start + len(local)] = phases @ amplitudes
    reshaped = answer.reshape(frequency_array.shape)
    return complex(reshaped) if scalar else reshaped


def raw_transform(
    model: CompletedMicroblock,
    frequencies: np.ndarray | Iterable[float] | float,
    derivative_order: int = 0,
    component: str = "completed",
) -> np.ndarray | complex:
    """Evaluate the uncentered transform for orders zero and one."""

    if derivative_order not in (0, 1):
        raise ValueError("raw_transform currently supports derivative orders 0 and 1")
    frequency_array = np.asarray(frequencies, dtype=float)
    centered = centered_transform(model, frequency_array, 0, component)
    phase = np.exp(-1j * frequency_array * model.logarithmic_center)
    if derivative_order == 0:
        answer = phase * centered
    else:
        centered_derivative = centered_transform(
            model, frequency_array, 1, component
        )
        answer = phase * (
            centered_derivative
            - 1j * model.logarithmic_center * centered
        )
    return complex(answer) if np.ndim(frequencies) == 0 else answer


def _validate_fraction(fraction: float) -> None:
    if not math.isfinite(fraction) or not 0.0 < fraction < 1.0:
        raise ValueError("fraction must lie strictly between zero and one")


def raw_point_width(
    value: float,
    global_supremum: float,
    log_bandwidth: float,
    fraction: float = 0.5,
) -> float:
    """Return the full Bernstein interval guaranteed at one raw value.

    Let ``P`` have logarithmic frequency diameter ``Omega`` and global real
    supremum ``M``.  If ``|P(t_0)|=V``, demodulation gives exponential type
    ``Omega/2`` and hence

        |P(t)| >= fraction*V

    on a full interval of length

        4*(1-fraction)*V/(Omega*M).

    The ratio ``V/M`` is essential: a local value cannot silently be treated
    as a global maximum.
    """

    if not math.isfinite(value) or value <= 0.0:
        raise ValueError("value must be finite and positive")
    if not math.isfinite(global_supremum) or global_supremum <= 0.0:
        raise ValueError("global_supremum must be finite and positive")
    if value > global_supremum:
        raise ValueError("value cannot exceed the global supremum")
    if not math.isfinite(log_bandwidth) or log_bandwidth <= 0.0:
        raise ValueError("log_bandwidth must be finite and positive")
    _validate_fraction(fraction)
    return (
        4.0
        * (1.0 - fraction)
        * value
        / (log_bandwidth * global_supremum)
    )


def compact_global_width(
    half_width: float, fraction: float = 0.5
) -> float:
    """Return the full Bernstein interval at a compact global maximum.

    A Fourier transform of a field supported in ``[-B,B]`` has exponential
    type ``B`` after demodulation.  At a global maximum its ``fraction``
    superlevel set contains an interval of length ``2(1-fraction)/B``.
    """

    if not math.isfinite(half_width) or half_width <= 0.0:
        raise ValueError("half_width must be finite and positive")
    _validate_fraction(fraction)
    return 2.0 * (1.0 - fraction) / half_width


@dataclass(frozen=True)
class EnergyExceptionalGate:
    """Calibration of the completed L2-energy exceptional-set lemma."""

    energy: float
    support_length: float
    height: float
    eta: float
    spectral_energy_floor: float
    threshold: float
    exceptional_measure_lower_bound: float


def energy_exceptional_gate(
    energy: float,
    support_length: float,
    height: float,
    eta: float,
) -> EnergyExceptionalGate:
    """Return the threshold and forced measure from completed energy.

    Here ``height`` is ``T`` for the frequency interval ``[-T,T]``.  Under

        integral_(-T)^T |F|^2 >= 2*pi*eta*energy,

    the threshold and forced exceptional measure are respectively

        lambda = sqrt(pi*eta*energy/(2*T)),
        measure{|t|<=T: |F(t)|>=lambda} >= pi*eta/H,

    where ``H`` is the full logarithmic support length.
    """

    if not math.isfinite(energy) or energy <= 0.0:
        raise ValueError("energy must be finite and positive")
    if not math.isfinite(support_length) or support_length <= 0.0:
        raise ValueError("support_length must be finite and positive")
    if not math.isfinite(height) or height <= 0.0:
        raise ValueError("height must be finite and positive")
    if not math.isfinite(eta) or not 0.0 < eta <= 1.0:
        raise ValueError("eta must lie in (0,1]")
    spectral_floor = 2.0 * math.pi * eta * energy
    threshold = math.sqrt(math.pi * eta * energy / (2.0 * height))
    lower_measure = math.pi * eta / support_length
    return EnergyExceptionalGate(
        energy=energy,
        support_length=support_length,
        height=height,
        eta=eta,
        spectral_energy_floor=spectral_floor,
        threshold=threshold,
        exceptional_measure_lower_bound=lower_measure,
    )


def _validate_displacement(displacement: float) -> None:
    if (
        not math.isfinite(displacement)
        or displacement <= 0.0
        or displacement >= 0.5
    ):
        raise ValueError("displacement must lie strictly between zero and one half")


def _validate_positive_integer(value: int, name: str) -> None:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class SobolevExponentGate:
    """Fixed-order height/threshold exponents for an off-line carrier."""

    displacement: float
    derivative_order: int
    minimum_height_exponent: float
    limiting_threshold_exponent: float
    critical_displacement: float
    positive_threshold: bool


def sobolev_exponent_gate(
    displacement: float, q: int
) -> SobolevExponentGate:
    """Calibrate finite-height capture using ``q`` Sobolev derivatives.

    A displacement ``d`` requires a height exponent strictly larger than
    ``(1/2-d)/q``.  At that limiting height the completed-value exponent is
    ``d-(1/2-d)/(2q)``, positive exactly for ``d>1/(4q+2)``.
    """

    _validate_displacement(displacement)
    _validate_positive_integer(q, "q")
    minimum_height = (0.5 - displacement) / q
    threshold = displacement - (0.5 - displacement) / (2.0 * q)
    critical = 1.0 / (4.0 * q + 2.0)
    return SobolevExponentGate(
        displacement=displacement,
        derivative_order=q,
        minimum_height_exponent=minimum_height,
        limiting_threshold_exponent=threshold,
        critical_displacement=critical,
        positive_threshold=threshold > 0.0,
    )


@dataclass(frozen=True)
class GuthMaynardExponentGate:
    """The three normalized exponents in Guth--Maynard Theorem 1.1."""

    displacement: float
    height_exponent: float
    length_term_exponent: float
    second_term_exponent: float
    height_term_exponent: float
    one_value_barrier_exponent: float
    excludes_one_value: bool

    @property
    def normalized_exponents(self) -> tuple[float, float, float]:
        return (
            self.length_term_exponent,
            self.second_term_exponent,
            self.height_term_exponent,
        )


def guth_maynard_exponent_gate(
    displacement: float, height_exponent: float
) -> GuthMaynardExponentGate:
    """Return the normalized Theorem 1.1 large-value exponents.

    For ``N=exp(R)``, ``T=N^tau``, and the ordinary-polynomial threshold
    ``V=N^(1/2+d)``, the three terms have exponents

        1-2d,  8/5-4d,  tau+2/5-4d.

    Their maximum is the one-value barrier.  A counting estimate excludes
    even one value only when this maximum is strictly negative.  In
    particular the first term prevents exclusion for every ``d<1/2``.
    """

    _validate_displacement(displacement)
    if not math.isfinite(height_exponent) or height_exponent < 0.0:
        raise ValueError("height_exponent must be finite and nonnegative")
    first = 1.0 - 2.0 * displacement
    second = 8.0 / 5.0 - 4.0 * displacement
    third = height_exponent + 2.0 / 5.0 - 4.0 * displacement
    barrier = max(first, second, third)
    return GuthMaynardExponentGate(
        displacement=displacement,
        height_exponent=height_exponent,
        length_term_exponent=first,
        second_term_exponent=second,
        height_term_exponent=third,
        one_value_barrier_exponent=barrier,
        excludes_one_value=barrier < 0.0,
    )


@dataclass(frozen=True)
class RawMomentExponentGate:
    """Forced raw-moment exponent versus a proposed arithmetic upper bound."""

    displacement: float
    moment_order: int
    upper_exponent: float
    forced_exponent: float
    critical_displacement_for_zero_upper: float
    exclusion_margin: float
    excludes_displacement: bool


def raw_moment_gate(
    displacement: float,
    moment_order: int,
    upper_exponent: float,
) -> RawMomentExponentGate:
    """Compare a raw ``2m``-moment theorem with one forced peak.

    A value of size ``N^d`` and the unconditional ``N^(1/2+o(1))`` global
    bound force ``2m``-moment exponent

        (2m+1)d - 1/2.

    An independent upper exponent excludes the displacement precisely when
    it is strictly smaller than this forced exponent.
    """

    _validate_displacement(displacement)
    _validate_positive_integer(moment_order, "moment_order")
    if not math.isfinite(upper_exponent):
        raise ValueError("upper_exponent must be finite")
    forced = (2.0 * moment_order + 1.0) * displacement - 0.5
    margin = forced - upper_exponent
    return RawMomentExponentGate(
        displacement=displacement,
        moment_order=moment_order,
        upper_exponent=upper_exponent,
        forced_exponent=forced,
        critical_displacement_for_zero_upper=(
            1.0 / (4.0 * moment_order + 2.0)
        ),
        exclusion_margin=margin,
        excludes_displacement=margin > 0.0,
    )


@dataclass(frozen=True)
class WidthGate:
    theta: float
    frequency_bound: float
    frequency_points: int
    peak_frequency: float
    peak_modulus: float
    peak_is_interior: bool
    transform_at_zero: complex
    observed_superlevel_component_width: float
    observed_centered_derivative_maximum: float
    observed_raw_derivative_maximum: float
    observed_centered_derivative_width: float
    observed_raw_derivative_width: float
    centered_type: float
    raw_type: float
    conditional_global_bernstein_width: float
    l1_centered_width_at_observed_peak: float
    l1_raw_width_at_observed_peak: float
    reciprocal_logarithmic_scale: float


def _golden_maximum(
    model: CompletedMicroblock, left: float, right: float, iterations: int = 48
) -> tuple[float, float]:
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    x_left = right - ratio * (right - left)
    x_right = left + ratio * (right - left)

    def value(point: float) -> float:
        return abs(centered_transform(model, point))

    f_left = value(x_left)
    f_right = value(x_right)
    for _ in range(iterations):
        if f_left < f_right:
            left = x_left
            x_left = x_right
            f_left = f_right
            x_right = left + ratio * (right - left)
            f_right = value(x_right)
        else:
            right = x_right
            x_right = x_left
            f_right = f_left
            x_left = right - ratio * (right - left)
            f_left = value(x_left)
    point = (left + right) / 2.0
    return point, value(point)


def width_gate(
    model: CompletedMicroblock,
    frequency_bound: float = 300.0,
    frequency_points: int = 30_001,
    theta: float = 0.5,
) -> WidthGate:
    """Measure one peak and report raw versus centered width gates."""

    if not math.isfinite(frequency_bound) or frequency_bound <= 0.0:
        raise ValueError("frequency_bound must be finite and positive")
    if frequency_points < 101:
        raise ValueError("frequency_points must be at least 101")
    if not 0.0 < theta < 1.0:
        raise ValueError("theta must lie strictly between zero and one")
    frequencies = np.linspace(
        -frequency_bound, frequency_bound, frequency_points
    )
    transform = centered_transform(model, frequencies)
    moduli = np.abs(transform)
    peak_index = int(np.argmax(moduli))
    interior = 0 < peak_index < frequency_points - 1
    if interior:
        peak_frequency, peak_modulus = _golden_maximum(
            model,
            float(frequencies[peak_index - 1]),
            float(frequencies[peak_index + 1]),
        )
    else:
        peak_frequency = float(frequencies[peak_index])
        peak_modulus = float(moduli[peak_index])

    threshold = theta * peak_modulus
    mask = moduli >= threshold
    left_index = peak_index
    while left_index > 0 and mask[left_index - 1]:
        left_index -= 1
    right_index = peak_index
    while right_index + 1 < frequency_points and mask[right_index + 1]:
        right_index += 1
    if left_index == 0 or right_index == frequency_points - 1:
        observed_width = math.inf
    else:
        observed_width = float(
            frequencies[right_index] - frequencies[left_index]
        )

    centered_derivative = centered_transform(
        model, frequencies, derivative_order=1
    )
    raw_derivative = raw_transform(model, frequencies, derivative_order=1)
    centered_derivative_maximum = float(np.max(np.abs(centered_derivative)))
    raw_derivative_maximum = float(np.max(np.abs(raw_derivative)))
    numerator = 2.0 * (1.0 - theta) * peak_modulus
    centered_observed_width = (
        numerator / centered_derivative_maximum
        if centered_derivative_maximum
        else math.inf
    )
    raw_observed_width = (
        numerator / raw_derivative_maximum
        if raw_derivative_maximum
        else math.inf
    )

    l1_norm = model.tapered_l1_norm
    centered_type = model.half_width
    raw_type = max(abs(model.lower), abs(model.upper))
    l1_centered = (
        numerator / (centered_type * l1_norm) if l1_norm else math.inf
    )
    l1_raw = numerator / (raw_type * l1_norm) if l1_norm else math.inf
    return WidthGate(
        theta=theta,
        frequency_bound=frequency_bound,
        frequency_points=frequency_points,
        peak_frequency=peak_frequency,
        peak_modulus=peak_modulus,
        peak_is_interior=interior,
        transform_at_zero=complex(centered_transform(model, 0.0)),
        observed_superlevel_component_width=observed_width,
        observed_centered_derivative_maximum=centered_derivative_maximum,
        observed_raw_derivative_maximum=raw_derivative_maximum,
        observed_centered_derivative_width=centered_observed_width,
        observed_raw_derivative_width=raw_observed_width,
        centered_type=centered_type,
        raw_type=raw_type,
        conditional_global_bernstein_width=(
            2.0 * (1.0 - theta) / centered_type
        ),
        l1_centered_width_at_observed_peak=l1_centered,
        l1_raw_width_at_observed_peak=l1_raw,
        reciprocal_logarithmic_scale=1.0 / model.logarithmic_center,
    )


@dataclass(frozen=True)
class MomentGate:
    power: int
    optimized_theta: float
    moment_upper_bound: float
    peak_lower_bound: float
    markov_measure_upper_bound: float
    centered_bernstein_measure_lower_bound: float
    raw_bernstein_measure_lower_bound: float
    logarithmic_moment_gap: float
    centered_required_gap: float
    raw_required_gap: float
    centered_gap_margin: float
    raw_gap_margin: float


def moment_gate(
    moment_upper_bound: float,
    peak_lower_bound: float,
    power: int,
    centered_type: float,
    raw_type: float,
) -> MomentGate:
    """Return the optimized Bernstein-versus-Markov exclusion gate.

    For ``theta=p/(p+1)``, an independently proved moment upper bound would
    contradict a peak of height at least ``H`` when

        p log(H) - log(U_p)
          > log(B(p+1)/2) + p log(1+1/p).

    Supplying the numerically measured completed moment is descriptive but
    circular; this function does not turn it into an arithmetic estimate.
    """

    if not isinstance(power, int) or isinstance(power, bool) or power < 1:
        raise ValueError("power must be a positive integer")
    if not math.isfinite(moment_upper_bound) or moment_upper_bound <= 0.0:
        raise ValueError("moment_upper_bound must be finite and positive")
    if not math.isfinite(peak_lower_bound) or peak_lower_bound <= 0.0:
        raise ValueError("peak_lower_bound must be finite and positive")
    if centered_type <= 0.0 or raw_type <= 0.0:
        raise ValueError("exponential types must be positive")
    theta = power / (power + 1.0)
    markov = moment_upper_bound / (theta * peak_lower_bound) ** power
    gap = power * math.log(peak_lower_bound) - math.log(moment_upper_bound)

    def required(exponential_type: float) -> float:
        return (
            math.log(exponential_type * (power + 1.0) / 2.0)
            + power * math.log1p(1.0 / power)
        )

    centered_required = required(centered_type)
    raw_required = required(raw_type)
    return MomentGate(
        power=power,
        optimized_theta=theta,
        moment_upper_bound=moment_upper_bound,
        peak_lower_bound=peak_lower_bound,
        markov_measure_upper_bound=markov,
        centered_bernstein_measure_lower_bound=(
            2.0 / (centered_type * (power + 1.0))
        ),
        raw_bernstein_measure_lower_bound=(
            2.0 / (raw_type * (power + 1.0))
        ),
        logarithmic_moment_gap=gap,
        centered_required_gap=centered_required,
        raw_required_gap=raw_required,
        centered_gap_margin=gap - centered_required,
        raw_gap_margin=gap - raw_required,
    )


def sampled_frequency_moments(
    model: CompletedMicroblock,
    frequency_bound: float,
    frequency_points: int,
    powers: Iterable[int],
) -> dict[int, float]:
    """Trapezoidal moments on a finite symmetric frequency interval."""

    frequencies = np.linspace(
        -frequency_bound, frequency_bound, frequency_points
    )
    moduli = np.abs(centered_transform(model, frequencies))
    answer: dict[int, float] = {}
    for power in powers:
        if not isinstance(power, int) or power < 1:
            raise ValueError("moment powers must be positive integers")
        answer[power] = float(np.trapz(moduli**power, frequencies))
    return answer


@dataclass(frozen=True)
class RemezGate:
    term_count: int
    theta: float
    interval_length: float
    turan_constant: float
    critical_theta: float
    superlevel_measure_lower_bound: float


def turan_remez_gate(
    term_count: int,
    theta: float = 0.5,
    interval_length: float = 1.0,
    turan_constant: float = 4.0,
) -> RemezGate:
    """Term-count Turan--Remez diagnostic for the *tail polynomial only*.

    Under the schematic normalization

        sup_I |P| <= (C |I|/|E|)^(N-1) sup_E |P|,

    the reported lower bound is
    ``|I| max(0, 1-C*theta^(1/(N-1)))``.  The completed center is not an
    ``N``-term Dirichlet polynomial, so this gate must not be advertised as
    a completed-field theorem.
    """

    if term_count < 1:
        raise ValueError("term_count must be positive")
    if not 0.0 < theta < 1.0:
        raise ValueError("theta must lie strictly between zero and one")
    if interval_length <= 0.0 or turan_constant < 1.0:
        raise ValueError("invalid interval length or Turan constant")
    if term_count == 1:
        critical = 1.0
        lower = interval_length
    else:
        critical = turan_constant ** (-(term_count - 1))
        lower = interval_length * max(
            0.0,
            1.0
            - turan_constant * theta ** (1.0 / (term_count - 1)),
        )
    return RemezGate(
        term_count,
        theta,
        interval_length,
        turan_constant,
        critical,
        lower,
    )


@dataclass(frozen=True)
class SyntheticModeAudit:
    basepoint: float
    half_width: float
    taper_power: int
    displacement: float
    ordinate: float
    peak_frequency: float
    peak_modulus: float
    observed_half_height_width: float
    bernstein_half_height_width: float
    pure_frequency_raw_derivative_ratio: float
    pure_frequency_centered_derivative_ratio: float


def synthetic_mode_audit(
    basepoint: float = 1_000.0,
    half_width: float = 10.0,
    taper_power: int = 2,
    displacement: float = 0.1,
    ordinate: float = 14.134725141734694,
    gaussian_order: int = 512,
) -> SyntheticModeAudit:
    """Audit a tapered synthetic off-line carrier on one scale block.

    The centered signal is ``tau(x) exp((delta+i*gamma)x)`` on ``[-B,B]``.
    Its transform has a rigorous global maximum at ``t=gamma`` by the
    triangle inequality.  The two pure-frequency derivative ratios record
    separately that ``exp(-it*basepoint)`` changes phase but not modulus.
    """

    if not all(
        math.isfinite(value)
        for value in (basepoint, half_width, displacement, ordinate)
    ):
        raise ValueError("synthetic parameters must be finite")
    if basepoint <= half_width or half_width <= 0.0:
        raise ValueError("require basepoint > half_width > 0")
    if taper_power < 2 or gaussian_order < 32:
        raise ValueError("invalid taper power or Gaussian order")
    nodes, weights = leggauss(gaussian_order)
    x_values = half_width * nodes
    scaled_weights = half_width * weights
    taper = compact_taper(x_values, 0.0, half_width, taper_power)
    amplitudes = scaled_weights * taper * np.exp(displacement * x_values)

    def transform(offset: np.ndarray | float) -> np.ndarray | complex:
        scalar = np.ndim(offset) == 0
        array = np.asarray(offset, dtype=float).reshape(-1)
        answer = np.exp(-1j * array[:, np.newaxis] * x_values) @ amplitudes
        return complex(answer[0]) if scalar else answer

    peak_modulus = float(abs(transform(0.0)))
    threshold = peak_modulus / 2.0
    right = max(1.0 / half_width, abs(displacement), 1.0e-3)
    while abs(transform(right)) >= threshold:
        right *= 2.0
        if right > 1.0e6:
            raise RuntimeError("failed to bracket the synthetic half-height")
    left = 0.0
    for _ in range(64):
        midpoint = (left + right) / 2.0
        if abs(transform(midpoint)) >= threshold:
            left = midpoint
        else:
            right = midpoint
    observed_width = 2.0 * (left + right) / 2.0
    return SyntheticModeAudit(
        basepoint=basepoint,
        half_width=half_width,
        taper_power=taper_power,
        displacement=displacement,
        ordinate=ordinate,
        peak_frequency=ordinate,
        peak_modulus=peak_modulus,
        observed_half_height_width=observed_width,
        bernstein_half_height_width=1.0 / half_width,
        pure_frequency_raw_derivative_ratio=basepoint,
        pure_frequency_centered_derivative_ratio=0.0,
    )


def quadrature_refinement_error(
    model: CompletedMicroblock,
    frequencies: Iterable[float] = (0.0, 1.0, 25.0, 50.0),
    refined_order: int | None = None,
) -> float:
    """Rebuild at a higher Gauss order and compare completed transforms."""

    if refined_order is None:
        refined_order = model.gaussian_order + 8
    if refined_order <= model.gaussian_order:
        raise ValueError("refined_order must exceed the model Gaussian order")
    refined = build_completed_microblock(
        scale=model.scale,
        cutoff=model.cutoff,
        step=model.step,
        order=model.order,
        half_width=model.half_width,
        taper_power=model.taper_power,
        gaussian_order=refined_order,
    )
    frequency_array = np.asarray(tuple(frequencies), dtype=float)
    coarse_values = centered_transform(model, frequency_array)
    refined_values = centered_transform(refined, frequency_array)
    return float(np.max(np.abs(coarse_values - refined_values)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=float, default=59.0)
    parser.add_argument("--cutoff", type=int, default=4)
    parser.add_argument("--step", type=float, default=0.04)
    parser.add_argument("--order", type=int, default=1)
    parser.add_argument("--half-width", type=float)
    parser.add_argument("--taper-power", type=int, default=2)
    parser.add_argument("--gaussian-order", type=int, default=24)
    parser.add_argument("--frequency-bound", type=float, default=300.0)
    parser.add_argument("--frequency-points", type=int, default=30_001)
    parser.add_argument("--theta", type=float, default=0.5)
    parser.add_argument("--moment-powers", nargs="+", type=int, default=[2, 4, 8])
    parser.add_argument("--skip-synthetic", action="store_true")
    args = parser.parse_args()

    model = build_completed_microblock(
        scale=args.scale,
        cutoff=args.cutoff,
        step=args.step,
        order=args.order,
        half_width=args.half_width,
        taper_power=args.taper_power,
        gaussian_order=args.gaussian_order,
    )
    gate = width_gate(
        model,
        args.frequency_bound,
        args.frequency_points,
        args.theta,
    )
    print(
        f"X={model.scale:g} Y={model.cutoff} h={model.step:g} "
        f"k={model.order} R={model.logarithmic_center:.9g} "
        f"B={model.half_width:.9g} taper={model.taper_power}"
    )
    print(
        f"products={len(model.active_product_values)} "
        f"quadrature={model.quadrature_size} limit={model.arithmetic_limit}"
    )
    if len(model.active_product_values) <= 40:
        print(f"active products: {model.active_product_values}")
    print(
        f"peak t={gate.peak_frequency:+.9g} "
        f"|F|={gate.peak_modulus:.12g} "
        f"interior={gate.peak_is_interior} "
        f"observed-width={gate.observed_superlevel_component_width:.9g}"
    )
    print(
        "width gates: "
        f"centered-Bernstein(global)={gate.conditional_global_bernstein_width:.9g} "
        f"centered-L1(sample)={gate.l1_centered_width_at_observed_peak:.9g} "
        f"raw-L1(sample)={gate.l1_raw_width_at_observed_peak:.9g} "
        f"1/R={gate.reciprocal_logarithmic_scale:.9g}"
    )
    refinement = quadrature_refinement_error(model)
    print(f"quadrature refinement max error={refinement:.3e}")

    moments = sampled_frequency_moments(
        model,
        args.frequency_bound,
        args.frequency_points,
        args.moment_powers,
    )
    for power in args.moment_powers:
        audit = moment_gate(
            moments[power],
            gate.peak_modulus,
            power,
            gate.centered_type,
            gate.raw_type,
        )
        print(
            f"p={power} sampled-U={moments[power]:.9g} "
            f"centered-gap-margin={audit.centered_gap_margin:+.9g} "
            f"raw-gap-margin={audit.raw_gap_margin:+.9g}"
        )

    remez = turan_remez_gate(
        max(1, len(model.active_product_values)), args.theta
    )
    print(
        "tail-only Remez: "
        f"critical-theta={remez.critical_theta:.3e} "
        f"lower-measure={remez.superlevel_measure_lower_bound:.9g}"
    )
    if not args.skip_synthetic:
        synthetic = synthetic_mode_audit()
        print(
            "synthetic mode: "
            f"peak={synthetic.peak_frequency:.9g} "
            f"observed-half-width={synthetic.observed_half_height_width:.9g} "
            f"Bernstein={synthetic.bernstein_half_height_width:.9g} "
            f"pure raw/centered derivative ratios="
            f"{synthetic.pure_frequency_raw_derivative_ratio:.9g}/"
            f"{synthetic.pure_frequency_centered_derivative_ratio:.9g}"
        )
    print("interpretation=numerical width gate; no arithmetic moment bound proved")


if __name__ == "__main__":
    main()
