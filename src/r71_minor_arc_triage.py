#!/usr/bin/env python3
"""Replayable triage for a two-frequency R71 ``minor-arc`` split.

There are two separate facts in this module.

First, on a finite cyclic group the weighted energy of the *completed* field

    h = tail - center

has the exact two-frequency expansion

    sum_x psi[x] |h[x]|^2
      = N^(-2) sum_(k,l) psihat[l-k] hhat[k] conjugate(hhat[l]).

Splitting the difference frequency ``l-k`` into a near and a far set is an
exact identity.  Cauchy--Schwarz and finite Plancherel give the useful bound

    |E_far| <= ||h||_2^2 N^(-1) sum_(v far) |psihat[v]|.

The far summand is nevertheless signed.  It is not a positive minor-arc
energy.  Tail--tail, both tail--center cross terms, and center--center are all
retained below.

Second, the existing completed R71 microblock supplies a D-rated continuous
counterexample to positivity.  Extend the complete field by zero outside the
displayed compact block and hard-cut the difference frequency at ``Omega``.
If

    psi_near(x) = integral_{|v|<=Omega} psihat(v)e(vx) dv/(2*pi),

then ``E_near = integral psi_near |h|^2`` and
``E_far = E-E_near``.  At the default ``X=127, Y=8`` fixture, ``E_far`` is
strictly negative and the sign is stable under Gaussian-quadrature
refinement.  This is finite numerical evidence, not an asymptotic theorem.

For the analytic application one may first localize the complete field by a
bounded compact cutoff ``chi=1`` on ``supp(psi)``.  A uniform Gevrey-s block
weight, ``s>1``, has Fourier tail

    integral_{|v|>T} |psihat(v)| dv
       <= poly(T) exp(-c T^(1/s)).

Together with the elementary complete-field budget ``||chi h||_2^2 <=
exp(R+o(R))``, taking ``T=K R^s`` makes the far piece exponentially
negligible.  The exact near term depends on ``chi``; only its equivalence
class modulo the negligible far term is cutoff-independent.  This is a
near-band reduction, not an estimate of the remaining arithmetic band and
not an additive-rational minor-arc theorem.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable

import numpy as np

from r71_large_value_width_probe import build_completed_microblock


@dataclass(frozen=True)
class BandComponents:
    """Tail/center expansion of one real band contribution."""

    tail_tail: float
    tail_center: float
    center_center: float

    @property
    def completed(self) -> float:
        return self.tail_tail + self.tail_center + self.center_center


@dataclass(frozen=True)
class FiniteDFTBandAudit:
    """Exact finite-DFT near/far ledger for a completed field."""

    size: int
    near_radius: int
    physical_energy: float
    spectral_energy: float
    near_energy: float
    far_energy: float
    far_young_bound: float
    total_components: BandComponents
    near_components: BandComponents
    far_components: BandComponents
    physical_spectral_error: float
    near_far_error: float
    total_component_error: float
    near_component_error: float
    far_component_error: float
    maximum_imaginary_residual: float


def _as_complex_vector(values: Iterable[complex], name: str) -> np.ndarray:
    answer = np.asarray(tuple(values), dtype=complex)
    if answer.ndim != 1 or len(answer) < 2:
        raise ValueError(f"{name} must be a one-dimensional vector of length >= 2")
    if not np.all(np.isfinite(answer)):
        raise ValueError(f"{name} must be finite")
    return answer


def _cyclic_distance(index: int, size: int) -> int:
    residue = index % size
    return min(residue, size - residue)


def _masked_dft_pairing(
    weight_hat: np.ndarray,
    left_hat: np.ndarray,
    right_hat: np.ndarray,
    mask: np.ndarray,
) -> complex:
    """Return the normalized two-frequency pairing on a difference mask."""

    size = len(weight_hat)
    total = 0.0j
    for left_index in range(size):
        for right_index in range(size):
            difference = (right_index - left_index) % size
            if mask[difference]:
                total += (
                    weight_hat[difference]
                    * left_hat[left_index]
                    * np.conj(right_hat[right_index])
                )
    return total / (size * size)


def _dft_components(
    weight_hat: np.ndarray,
    tail_hat: np.ndarray,
    center_hat: np.ndarray,
    mask: np.ndarray,
) -> tuple[BandComponents, float]:
    tail_tail = _masked_dft_pairing(
        weight_hat, tail_hat, tail_hat, mask
    )
    tail_center_complex = -(
        _masked_dft_pairing(weight_hat, tail_hat, center_hat, mask)
        + _masked_dft_pairing(weight_hat, center_hat, tail_hat, mask)
    )
    center_center = _masked_dft_pairing(
        weight_hat, center_hat, center_hat, mask
    )
    values = (tail_tail, tail_center_complex, center_center)
    imaginary_residual = max(abs(value.imag) for value in values)
    return (
        BandComponents(*(float(value.real) for value in values)),
        float(imaginary_residual),
    )


def finite_dft_band_audit(
    tail: Iterable[complex],
    center: Iterable[complex],
    weight: Iterable[float],
    near_radius: int,
) -> FiniteDFTBandAudit:
    """Audit the exact completed near/far identity on ``Z/NZ``.

    The DFT convention is NumPy's unnormalized forward transform:

    ``fhat[k] = sum_x f[x] exp(-2*pi*i*k*x/N)``.

    The weight must be real and nonnegative.  The near set is defined using
    cyclic distance of the difference frequency.  All computations are
    floating replays of finite algebraic identities.
    """

    tail_values = _as_complex_vector(tail, "tail")
    center_values = _as_complex_vector(center, "center")
    weight_values = _as_complex_vector(weight, "weight")
    size = len(tail_values)
    if len(center_values) != size or len(weight_values) != size:
        raise ValueError("tail, center, and weight must have equal lengths")
    if np.max(np.abs(weight_values.imag)) > 1.0e-14:
        raise ValueError("weight must be real")
    real_weight = weight_values.real
    if np.min(real_weight) < 0.0:
        raise ValueError("weight must be nonnegative")
    if (
        not isinstance(near_radius, int)
        or isinstance(near_radius, bool)
        or not 0 <= near_radius <= size // 2
    ):
        raise ValueError("near_radius must lie between zero and floor(N/2)")

    completed = tail_values - center_values
    tail_hat = np.fft.fft(tail_values)
    center_hat = np.fft.fft(center_values)
    completed_hat = tail_hat - center_hat
    weight_hat = np.fft.fft(real_weight)
    near_mask = np.asarray(
        [_cyclic_distance(index, size) <= near_radius for index in range(size)]
    )
    far_mask = ~near_mask

    total_complex = _masked_dft_pairing(
        weight_hat, completed_hat, completed_hat, np.ones(size, dtype=bool)
    )
    near_complex = _masked_dft_pairing(
        weight_hat, completed_hat, completed_hat, near_mask
    )
    far_complex = _masked_dft_pairing(
        weight_hat, completed_hat, completed_hat, far_mask
    )
    physical = float(np.dot(real_weight, np.abs(completed) ** 2))

    total_components, total_imaginary = _dft_components(
        weight_hat, tail_hat, center_hat, np.ones(size, dtype=bool)
    )
    near_components, near_imaginary = _dft_components(
        weight_hat, tail_hat, center_hat, near_mask
    )
    far_components, far_imaginary = _dft_components(
        weight_hat, tail_hat, center_hat, far_mask
    )

    # For each difference v, Cauchy bounds the frequency correlation by
    # ||hhat||_2^2 = N ||h||_2^2.  The N^(-2) DFT normalization leaves the
    # factor below.
    far_weight_l1 = float(np.sum(np.abs(weight_hat[far_mask])))
    completed_l2_squared = float(np.sum(np.abs(completed) ** 2))
    far_bound = completed_l2_squared * far_weight_l1 / size

    maximum_imaginary = max(
        abs(total_complex.imag),
        abs(near_complex.imag),
        abs(far_complex.imag),
        total_imaginary,
        near_imaginary,
        far_imaginary,
    )
    spectral = float(total_complex.real)
    near = float(near_complex.real)
    far = float(far_complex.real)
    return FiniteDFTBandAudit(
        size=size,
        near_radius=near_radius,
        physical_energy=physical,
        spectral_energy=spectral,
        near_energy=near,
        far_energy=far,
        far_young_bound=far_bound,
        total_components=total_components,
        near_components=near_components,
        far_components=far_components,
        physical_spectral_error=abs(physical - spectral),
        near_far_error=abs(spectral - near - far),
        total_component_error=abs(spectral - total_components.completed),
        near_component_error=abs(near - near_components.completed),
        far_component_error=abs(far - far_components.completed),
        maximum_imaginary_residual=float(maximum_imaginary),
    )


@dataclass(frozen=True)
class ContinuousDifferenceBandAudit:
    """D-rated compact-block hard difference-frequency audit."""

    scale: float
    cutoff: int
    omega: float
    gaussian_order: int
    quadrature_size: int
    total_components: BandComponents
    near_components: BandComponents
    far_components: BandComponents
    total_energy: float
    near_energy: float
    far_energy: float
    near_far_error: float
    total_component_error: float
    near_component_error: float
    far_component_error: float
    minimum_near_weight: float
    maximum_near_weight: float

    @property
    def far_is_negative(self) -> bool:
        return self.far_energy < 0.0


def _continuous_components(
    quadrature_weights: np.ndarray,
    band_weight: np.ndarray,
    tail: np.ndarray,
    center: np.ndarray,
) -> BandComponents:
    return BandComponents(
        tail_tail=float(np.dot(quadrature_weights, band_weight * tail * tail)),
        tail_center=float(
            np.dot(quadrature_weights, band_weight * (-2.0 * tail * center))
        ),
        center_center=float(
            np.dot(quadrature_weights, band_weight * center * center)
        ),
    )


def completed_difference_band_audit(
    scale: float = 127.0,
    cutoff: int = 8,
    omega: float = 17.09975946676696,
    *,
    step: float = 0.04,
    order: int = 1,
    half_width: float | None = None,
    taper_power: int = 2,
    gaussian_order: int = 24,
) -> ContinuousDifferenceBandAudit:
    """Reproduce the signed hard difference-band split on an R71 block.

    The physical energy uses ``psi=taper**2``.  The field is extended by zero
    outside the compact diagnostic interval before the difference-frequency
    split.  For the radian Fourier convention
    ``fhat(v)=integral f(x) exp(-i*v*x) dx``, the inverse transform of
    ``1_(|v|<=omega) psihat(v)`` is the sinc convolution

    ``psi_near(x)=integral psi(y) sin(omega(x-y))/(pi(x-y)) dy``.

    The returned result is a quadrature diagnostic.  In particular, it does
    not certify an asymptotic sign or a statement for a different exterior
    localization.
    """

    if not math.isfinite(omega) or omega <= 0.0:
        raise ValueError("omega must be finite and positive")
    model = build_completed_microblock(
        scale=scale,
        cutoff=cutoff,
        step=step,
        order=order,
        half_width=half_width,
        taper_power=taper_power,
        gaussian_order=gaussian_order,
    )
    nodes = model.quadrature_nodes - model.logarithmic_center
    quadrature_weights = model.quadrature_weights
    physical_weight = model.taper_values**2
    differences = nodes[:, np.newaxis] - nodes[np.newaxis, :]
    # np.sinc(y)=sin(pi*y)/(pi*y), including the removable value at zero.
    sinc_kernel = (omega / math.pi) * np.sinc(
        omega * differences / math.pi
    )
    near_weight = sinc_kernel @ (quadrature_weights * physical_weight)
    far_weight = physical_weight - near_weight

    total_components = _continuous_components(
        quadrature_weights,
        physical_weight,
        model.tail_values,
        model.center_values,
    )
    near_components = _continuous_components(
        quadrature_weights,
        near_weight,
        model.tail_values,
        model.center_values,
    )
    far_components = _continuous_components(
        quadrature_weights,
        far_weight,
        model.tail_values,
        model.center_values,
    )
    total = float(
        np.dot(
            quadrature_weights,
            physical_weight * model.completed_values**2,
        )
    )
    near = float(
        np.dot(
            quadrature_weights,
            near_weight * model.completed_values**2,
        )
    )
    far = float(
        np.dot(
            quadrature_weights,
            far_weight * model.completed_values**2,
        )
    )
    return ContinuousDifferenceBandAudit(
        scale=scale,
        cutoff=cutoff,
        omega=omega,
        gaussian_order=gaussian_order,
        quadrature_size=len(nodes),
        total_components=total_components,
        near_components=near_components,
        far_components=far_components,
        total_energy=total,
        near_energy=near,
        far_energy=far,
        near_far_error=abs(total - near - far),
        total_component_error=abs(total - total_components.completed),
        near_component_error=abs(near - near_components.completed),
        far_component_error=abs(far - far_components.completed),
        minimum_near_weight=float(np.min(near_weight)),
        maximum_near_weight=float(np.max(near_weight)),
    )


@dataclass(frozen=True)
class MinorArcExponentPassport:
    """Exponent ledger for the eta target and a negligible far band."""

    eta: float
    natural_energy_exponent: float
    target_exponent: float
    far_exponent: float
    far_margin_below_target: float
    far_is_negligible_at_target_scale: bool


@dataclass(frozen=True)
class AdditivePrincipalBandPassport:
    """Power ledger for the exact additive principal-band localization."""

    eta: float
    aperture_exponent: float
    spline_order: int
    target_energy_exponent: float
    tail_amplitude_exponent: float
    tail_energy_exponent: float
    cross_term_exponent: float
    localization_error_exponent: float
    localization_is_negligible_at_target_scale: bool


def additive_principal_band_passport(
    eta: float = 0.01,
    *,
    aperture_exponent: float = 0.01,
    spline_order: int = 4,
) -> AdditivePrincipalBandPassport:
    """Bookkeep the completed additive Fourier split.

    The principal band is ``|xi| <= X^(-1+aperture_exponent)``.  If the
    compact order-``k`` logarithmic B-spline has additive Fourier decay
    ``(1+|X*xi|)^(-k-1)``, its complementary field has exponent
    ``1/2-k*aperture_exponent``.  Squaring gives the tail energy exponent,
    while pairing with the trivial ``X^(1/2+o(1))`` major field gives the
    displayed cross-term exponent.  This is exponent algebra, not a proof of
    the B-spline estimate or of the remaining principal-band bound.
    """

    if not math.isfinite(eta) or not 0.0 < eta < 0.5:
        raise ValueError("eta must lie strictly between zero and one half")
    if (
        not math.isfinite(aperture_exponent)
        or not 0.0 < aperture_exponent < 1.0
    ):
        raise ValueError("aperture_exponent must lie strictly between zero and one")
    if (
        not isinstance(spline_order, int)
        or isinstance(spline_order, bool)
        or spline_order < 1
    ):
        raise ValueError("spline_order must be a positive integer")
    target = 1.0 - 2.0 * eta
    tail_amplitude = 0.5 - spline_order * aperture_exponent
    tail_energy = 2.0 * tail_amplitude
    cross = 0.5 + tail_amplitude
    error = max(tail_energy, cross)
    return AdditivePrincipalBandPassport(
        eta=eta,
        aperture_exponent=aperture_exponent,
        spline_order=spline_order,
        target_energy_exponent=target,
        tail_amplitude_exponent=tail_amplitude,
        tail_energy_exponent=tail_energy,
        cross_term_exponent=cross,
        localization_error_exponent=error,
        localization_is_negligible_at_target_scale=error < target,
    )


@dataclass(frozen=True)
class AffineCenterMoments:
    """Exact two-moment coefficients representing the affine R71 center."""

    alpha: Fraction
    beta: Fraction
    normalization: Fraction
    zeroth_moment: Fraction
    first_moment: Fraction
    constant_density: Fraction
    logarithmic_density: Fraction
    recovered_alpha: Fraction
    recovered_beta: Fraction


def affine_center_moments(
    alpha: Fraction | int,
    beta: Fraction | int,
    normalization: Fraction | int,
    zeroth_moment: Fraction | int,
    first_moment: Fraction | int,
) -> AffineCenterMoments:
    """Solve the exact moment equations for ``A+B log(t)``.

    If ``J0=integral V(v)exp(-v/2)dv`` and
    ``J1=integral v V(v)exp(-v/2)dv``, then substitution
    ``v=r-log(t)`` gives

    ``integral t^(-1/2)V(r-log(t))(A+B log(t))dt``
    ``=exp(r/2)[(A*J0-B*J1)+(B*J0)r]``.

    The returned rational identities match this with
    ``exp(r/2)(alpha+beta*r)/normalization``.  This checks only the algebraic
    center allocation, not the analytic integral.
    """

    alpha_q = Fraction(alpha)
    beta_q = Fraction(beta)
    norm_q = Fraction(normalization)
    j0_q = Fraction(zeroth_moment)
    j1_q = Fraction(first_moment)
    if norm_q == 0 or j0_q == 0:
        raise ValueError("normalization and zeroth moment must be nonzero")
    logarithmic = beta_q / (norm_q * j0_q)
    constant = alpha_q / (norm_q * j0_q) + (
        beta_q * j1_q / (norm_q * j0_q**2)
    )
    return AffineCenterMoments(
        alpha=alpha_q,
        beta=beta_q,
        normalization=norm_q,
        zeroth_moment=j0_q,
        first_moment=j1_q,
        constant_density=constant,
        logarithmic_density=logarithmic,
        recovered_alpha=norm_q * (constant * j0_q - logarithmic * j1_q),
        recovered_beta=norm_q * logarithmic * j0_q,
    )


def minor_arc_exponent_passport(
    eta: float = 0.01,
    *,
    natural_energy_exponent: float = 1.0,
    far_saving_in_eta_units: float = 3.0,
) -> MinorArcExponentPassport:
    """Return the fixed-power bookkeeping used by the triage.

    The desired completed-energy exponent is ``1-2*eta``.  The default far
    exponent is ``1-3*eta``; it is deliberately strictly smaller, so adding
    the signed far term cannot alter the target exponent.
    """

    if not math.isfinite(eta) or not 0.0 < eta < 0.5:
        raise ValueError("eta must lie strictly between zero and one half")
    if not math.isfinite(natural_energy_exponent):
        raise ValueError("natural_energy_exponent must be finite")
    if (
        not math.isfinite(far_saving_in_eta_units)
        or far_saving_in_eta_units <= 2.0
    ):
        raise ValueError("far saving must be strictly more than two eta units")
    target = natural_energy_exponent - 2.0 * eta
    far = natural_energy_exponent - far_saving_in_eta_units * eta
    margin = target - far
    return MinorArcExponentPassport(
        eta=eta,
        natural_energy_exponent=natural_energy_exponent,
        target_exponent=target,
        far_exponent=far,
        far_margin_below_target=margin,
        far_is_negligible_at_target_scale=margin > 0.0,
    )


def gevrey_frequency_constant(
    *,
    gevrey_order: float,
    fourier_decay_rate: float,
    natural_energy_exponent: float,
    desired_far_exponent: float,
) -> float:
    """Solve the Gevrey exponent budget for ``T=K R^s``.

    Ignoring polynomial factors (which are ``exp(o(R))``), the standard tail
    estimate and a natural energy exponent ``B`` give

    ``E_far <= exp((B-c*K^(1/s))R+o(R))``.

    This function returns the least formal ``K`` making the displayed main
    exponent equal to ``desired_far_exponent``.  It records bookkeeping; it
    does not assert a Gevrey constant for an unspecified block weight.
    """

    values = (
        gevrey_order,
        fourier_decay_rate,
        natural_energy_exponent,
        desired_far_exponent,
    )
    if not all(math.isfinite(value) for value in values):
        raise ValueError("all exponent data must be finite")
    if gevrey_order <= 1.0:
        raise ValueError("compactly supported Gevrey order must exceed one")
    if fourier_decay_rate <= 0.0:
        raise ValueError("fourier_decay_rate must be positive")
    gap = natural_energy_exponent - desired_far_exponent
    if gap <= 0.0:
        raise ValueError("desired far exponent must be below the natural one")
    return (gap / fourier_decay_rate) ** gevrey_order


def _default_dft_fixture() -> FiniteDFTBandAudit:
    points = np.arange(16, dtype=float)
    tail = (
        0.7 * np.cos(2.0 * math.pi * points / 16.0)
        + 0.3 * np.sin(6.0 * math.pi * points / 16.0)
        + 0.05 * points
    )
    center = 0.18 + 0.015 * points
    weight = (1.0 - ((points - 7.5) / 8.5) ** 2) ** 2
    return finite_dft_band_audit(tail, center, weight, near_radius=2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=float, default=127.0)
    parser.add_argument("--cutoff", type=int, default=8)
    parser.add_argument("--omega", type=float, default=17.09975946676696)
    parser.add_argument("--gaussian-order", type=int, default=24)
    args = parser.parse_args()

    dft = _default_dft_fixture()
    continuous = completed_difference_band_audit(
        scale=args.scale,
        cutoff=args.cutoff,
        omega=args.omega,
        gaussian_order=args.gaussian_order,
    )
    passport = minor_arc_exponent_passport()
    additive = additive_principal_band_passport()
    center = affine_center_moments(3, -2, 5, 7, 11)
    print(
        "finite DFT: "
        f"E={dft.spectral_energy:.12g} "
        f"near={dft.near_energy:.12g} far={dft.far_energy:+.12g} "
        f"Young={dft.far_young_bound:.12g} "
        f"closure={dft.near_far_error:.3g}"
    )
    print(
        "completed microblock: "
        f"X={continuous.scale:g} Y={continuous.cutoff} "
        f"Omega={continuous.omega:.12g} "
        f"E={continuous.total_energy:.12g} "
        f"near={continuous.near_energy:.12g} "
        f"far={continuous.far_energy:+.12g}"
    )
    print(
        "far sectors: "
        f"TT={continuous.far_components.tail_tail:+.12g} "
        f"TC={continuous.far_components.tail_center:+.12g} "
        f"CC={continuous.far_components.center_center:+.12g}"
    )
    print(
        "exponents: "
        f"eta={passport.eta:g} target={passport.target_exponent:g} "
        f"far={passport.far_exponent:g} "
        f"margin={passport.far_margin_below_target:g}"
    )
    print(
        "additive principal band: "
        f"order={additive.spline_order} "
        f"tail-field={additive.tail_amplitude_exponent:g} "
        f"tail-energy={additive.tail_energy_exponent:g} "
        f"cross={additive.cross_term_exponent:g} "
        f"target={additive.target_energy_exponent:g}"
    )
    print(
        "affine center moments: "
        f"A={center.constant_density} B={center.logarithmic_density} "
        f"alpha={center.recovered_alpha} beta={center.recovered_beta}"
    )
    print("rating=D finite sign diagnostic; no asymptotic arithmetic bound")


if __name__ == "__main__":
    main()
