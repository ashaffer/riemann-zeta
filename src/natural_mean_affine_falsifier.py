#!/usr/bin/env python3
"""Finite checks for natural reciprocal-phase centering and affine repair.

For a prime ``r`` and integer ``k``, inversion permutes the nonzero residue
classes, so

    mean_{p in (Z/rZ)^*} e(-k * inverse(p) / r)
        = c_r(k) / (r - 1).

The natural mean is ``-1/(r-1)`` when ``r`` does not divide ``k``, not one.
This module checks the corresponding exact carrier split, the integration by
parts identity that turns one affine theta factor into a derivative of the
cutoff, and two finite affine-profile stress tests for the common dual
``W(theta/(p*r))``.

The affine-profile experiments are diagnostics, not asymptotic estimates or
evidence about zeros of zeta.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from numpy.polynomial.legendre import leggauss

from common_dual_prime_beat_probe import (
    global_gram_formula,
    prime_centered_target,
)


@dataclass(frozen=True)
class NaturalCenteringDiagnostic:
    """One complete prime-unit centering calculation."""

    prime: int
    frequency: int
    ramanujan_sum: int
    predicted_mean: complex
    direct_mean: complex
    mean_error: float
    raw_shift_norm_squared: float
    raw_shift_norm_squared_formula: float
    centered_norm_squared: float
    centered_norm_squared_formula: float
    centered_sum_error: float


@dataclass(frozen=True)
class CarrierSplitDiagnostic:
    """Elementwise check of the natural-mean carrier decomposition."""

    prime: int
    frequency: int
    sample_count: int
    maximum_split_error: float
    centered_phase_sum_error: float
    original_norm: float
    oscillatory_norm: float
    residual_carrier_norm: float


@dataclass(frozen=True)
class AffineIBPDiagnostic:
    """Gaussian-quadrature check of the compact-support affine identity."""

    scale_g: float
    modulus_m: int
    modulus_n: int
    theta: int
    quadrature_order: int
    left_value: complex
    right_value: complex
    identity_error: float
    relative_identity_error: float
    refinement_error: float


@dataclass(frozen=True)
class ReciprocalDerivativeTransferDiagnostic:
    """Exact complex-algebra check of the reciprocal derivative transfer."""

    prime: int
    frequency: int
    reciprocal_mean: complex
    transfer_error: float
    centered_interpolation_error: float
    invariant_projection_error: float
    coefficient_amplification: float


@dataclass(frozen=True)
class AffineApproximationDiagnostic:
    """Least-squares affine fit to one finite common-dual theta profile."""

    profile_name: str
    length: int
    prime_p: int
    prime_r: int
    theta_count: int
    relative_l2_residual: float
    relative_linf_residual: float
    phase_span_cycles: float


def _is_prime(value: int) -> bool:
    return value >= 2 and all(
        value % divisor for divisor in range(2, math.isqrt(value) + 1)
    )


def ramanujan_sum_prime(prime: int, frequency: int) -> int:
    """Return ``c_prime(frequency)`` for a prime modulus."""

    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    return prime - 1 if frequency % prime == 0 else -1


def prime_unit_phases(prime: int, frequency: int) -> np.ndarray:
    """Return ``e(-k inverse(p)/r)`` over every nonzero class ``p mod r``."""

    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    inverses = np.asarray(
        [pow(residue, -1, prime) for residue in range(1, prime)],
        dtype=float,
    )
    return np.exp(-2j * math.pi * frequency * inverses / prime)


def analyze_natural_centering(
    prime: int = 11,
    frequency: int = 3,
) -> NaturalCenteringDiagnostic:
    """Compare the artificial shift by one with the exact unit-group mean."""

    phases = prime_unit_phases(prime, frequency)
    ramanujan_sum = ramanujan_sum_prime(prime, frequency)
    predicted_mean = complex(ramanujan_sum / (prime - 1))
    direct_mean = complex(np.mean(phases))
    raw_norm_squared = float(np.vdot(phases - 1.0, phases - 1.0).real)
    centered_norm_squared = float(
        np.vdot(phases - predicted_mean, phases - predicted_mean).real
    )
    raw_formula = float(2 * (prime - 1) - 2 * ramanujan_sum)
    centered_formula = float(
        (prime - 1) * (1.0 - abs(predicted_mean) ** 2)
    )
    return NaturalCenteringDiagnostic(
        prime=prime,
        frequency=frequency,
        ramanujan_sum=ramanujan_sum,
        predicted_mean=predicted_mean,
        direct_mean=direct_mean,
        mean_error=abs(direct_mean - predicted_mean),
        raw_shift_norm_squared=raw_norm_squared,
        raw_shift_norm_squared_formula=raw_formula,
        centered_norm_squared=centered_norm_squared,
        centered_norm_squared_formula=centered_formula,
        centered_sum_error=float(abs(np.sum(phases - predicted_mean))),
    )


def analyze_carrier_split(
    prime: int = 11,
    frequency: int = 3,
    *,
    seed: int = 8501,
) -> CarrierSplitDiagnostic:
    """Check ``h*z-gamma = h*(z-mu) + (mu*h-gamma)`` coefficientwise."""

    phases = prime_unit_phases(prime, frequency)
    mean = ramanujan_sum_prime(prime, frequency) / (prime - 1)
    rng = np.random.default_rng(seed)
    count = len(phases)
    h = rng.normal(size=count) + 1j * rng.normal(size=count)
    gamma = rng.normal(size=count) + 1j * rng.normal(size=count)
    slow = np.exp(2j * math.pi * rng.random(count))
    original = slow * (h * phases - gamma)
    oscillatory = slow * h * (phases - mean)
    residual = slow * (mean * h - gamma)
    return CarrierSplitDiagnostic(
        prime=prime,
        frequency=frequency,
        sample_count=count,
        maximum_split_error=float(np.max(np.abs(original - oscillatory - residual))),
        centered_phase_sum_error=float(abs(np.sum(phases - mean))),
        original_norm=float(np.linalg.norm(original)),
        oscillatory_norm=float(np.linalg.norm(oscillatory)),
        residual_carrier_norm=float(np.linalg.norm(residual)),
    )


def _affine_ibp_values(
    scale_g: float,
    modulus_m: int,
    modulus_n: int,
    theta: int,
    order: int,
) -> tuple[complex, complex]:
    """Evaluate both sides of the affine integration-by-parts identity."""

    nodes, weights = leggauss(order)
    base = 1.0 - nodes**2
    # This is F(u)=L(u+g*j,u) for a smooth compactly supported polynomial L.
    cutoff = base**8 * (1.0 + 0.2 * nodes)
    cutoff_derivative = (
        -16.0 * nodes * base**7 * (1.0 + 0.2 * nodes)
        + 0.2 * base**8
    )
    phase = np.exp(
        2j
        * math.pi
        * theta
        * nodes
        / (scale_g * modulus_m * modulus_n)
    )
    lattice_integral = scale_g * np.dot(weights, cutoff * phase)
    left = theta * lattice_integral / (modulus_m * modulus_n)
    right = -(scale_g**2) * np.dot(weights, cutoff_derivative * phase) / (
        2j * math.pi
    )
    return complex(left), complex(right)


def analyze_affine_ibp(
    *,
    scale_g: float = 3.0,
    modulus_m: int = 17,
    modulus_n: int = 19,
    theta: int = 7,
    quadrature_order: int = 64,
) -> AffineIBPDiagnostic:
    """Verify ``theta*A/(mn) = -g^2/(2 pi i) int F' e``."""

    if scale_g <= 0.0 or min(modulus_m, modulus_n, theta) <= 0:
        raise ValueError("all scales, moduli, and theta must be positive")
    if quadrature_order < 16:
        raise ValueError("quadrature_order must be at least 16")
    left, right = _affine_ibp_values(
        scale_g, modulus_m, modulus_n, theta, quadrature_order
    )
    refined_left, refined_right = _affine_ibp_values(
        scale_g, modulus_m, modulus_n, theta, 2 * quadrature_order
    )
    error = abs(left - right)
    refinement = max(abs(left - refined_left), abs(right - refined_right))
    return AffineIBPDiagnostic(
        scale_g=scale_g,
        modulus_m=modulus_m,
        modulus_n=modulus_n,
        theta=theta,
        quadrature_order=quadrature_order,
        left_value=left,
        right_value=right,
        identity_error=error,
        relative_identity_error=error / max(abs(left), np.finfo(float).tiny),
        refinement_error=refinement,
    )


def analyze_reciprocal_derivative_transfer(
    prime: int = 11,
    frequency: int = 3,
    *,
    residue: int = 2,
    theta: int = 3,
    modulus_product: int = 143,
) -> ReciprocalDerivativeTransferDiagnostic:
    """Check the transfer identity and its invariant arithmetic projection."""

    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if math.gcd(residue, prime) != 1:
        raise ValueError("residue must be invertible modulo prime")
    if theta == 0 or modulus_product <= 0:
        raise ValueError("theta and modulus_product must be nonzero and positive")
    mean = complex(ramanujan_sum_prime(prime, frequency) / (prime - 1))
    if mean == 0.0:
        raise ValueError("the reciprocal mean must be nonzero")
    reciprocal = np.exp(
        -2j * math.pi * frequency * pow(residue, -1, prime) / prime
    )
    slow = np.exp(0.37j)
    native = 0.41 - 0.23j
    canonical = -0.17 + 0.52j
    amplitude = 0.73 + 0.19j
    derivative_amplitude = (
        -2j * math.pi * theta * amplitude / modulus_product
    )

    original = slow * (native * reciprocal - canonical) * amplitude
    transferred = slow * (
        canonical * (reciprocal - 1.0) * amplitude
        + modulus_product
        * (canonical - native)
        * reciprocal
        * derivative_amplitude
        / (2j * math.pi * theta)
    )

    interpolant = canonical / mean
    centered_interpolation = slow * (
        interpolant * (reciprocal - mean) * amplitude
        + (mean * interpolant - canonical) * amplitude
        + modulus_product
        * (interpolant - native)
        * reciprocal
        * derivative_amplitude
        / (2j * math.pi * theta)
    )
    projected_transfer = (
        canonical * (mean - 1.0) * amplitude
        + modulus_product
        * (canonical - native)
        * mean
        * derivative_amplitude
        / (2j * math.pi * theta)
    )
    invariant_projection = (mean * native - canonical) * amplitude
    return ReciprocalDerivativeTransferDiagnostic(
        prime=prime,
        frequency=frequency,
        reciprocal_mean=mean,
        transfer_error=float(abs(original - transferred)),
        centered_interpolation_error=float(abs(original - centered_interpolation)),
        invariant_projection_error=float(
            abs(projected_transfer - invariant_projection)
        ),
        coefficient_amplification=float(abs(interpolant) / abs(canonical)),
    )


def _affine_fit_diagnostic(
    profile_name: str,
    weights: np.ndarray,
    points: np.ndarray,
    theta: np.ndarray,
    prime_p: int,
    prime_r: int,
) -> AffineApproximationDiagnostic:
    values = np.exp(
        -2j
        * math.pi
        * theta[:, None]
        * points[None, :]
        / (prime_p * prime_r)
    ) @ weights
    centered_theta = theta - float(np.mean(theta))
    theta_scale = max(float(np.ptp(theta)), 1.0)
    design = np.column_stack((np.ones(len(theta)), centered_theta / theta_scale))
    fitted = design @ np.linalg.lstsq(design, values, rcond=None)[0]
    residual = values - fitted
    return AffineApproximationDiagnostic(
        profile_name=profile_name,
        length=len(points),
        prime_p=prime_p,
        prime_r=prime_r,
        theta_count=len(theta),
        relative_l2_residual=float(
            np.linalg.norm(residual) / np.linalg.norm(values)
        ),
        relative_linf_residual=float(
            np.max(np.abs(residual)) / np.max(np.abs(values))
        ),
        phase_span_cycles=float(
            np.max(points) * (theta[-1] - theta[0]) / (prime_p * prime_r)
        ),
    )


def analyze_affine_profiles(
    length: int = 64,
    primes: tuple[int, ...] = (11, 13, 17),
    *,
    prime_p: int = 11,
    prime_r: int = 13,
    theta_limit: int = 10,
) -> tuple[AffineApproximationDiagnostic, AffineApproximationDiagnostic]:
    """Fit affine theta profiles for canonical and endpoint-mass duals."""

    if prime_p not in primes or prime_r not in primes or prime_p == prime_r:
        raise ValueError("prime_p and prime_r must be distinct members of primes")
    theta = np.asarray(
        [
            value
            for value in range(1, theta_limit + 1)
            if math.gcd(value, prime_p * prime_r) == 1
        ],
        dtype=float,
    )
    if len(theta) < 3:
        raise ValueError("at least three primitive theta values are required")
    points = np.arange(1, length + 1, dtype=float)
    gram = global_gram_formula(length, primes)
    canonical_weights = np.linalg.solve(gram, prime_centered_target(length))
    endpoint_weights = np.zeros(length)
    endpoint_weights[-1] = 1.0
    return (
        _affine_fit_diagnostic(
            "canonical-Lambda-minus-one",
            canonical_weights,
            points,
            theta,
            prime_p,
            prime_r,
        ),
        _affine_fit_diagnostic(
            "endpoint-unit-mass",
            endpoint_weights,
            points,
            theta,
            prime_p,
            prime_r,
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=11)
    parser.add_argument("--frequency", type=int, default=3)
    args = parser.parse_args()

    centering = analyze_natural_centering(args.prime, args.frequency)
    split = analyze_carrier_split(args.prime, args.frequency)
    ibp = analyze_affine_ibp()
    transfer = analyze_reciprocal_derivative_transfer(
        args.prime, args.frequency
    )
    profiles = analyze_affine_profiles()
    print(f"natural_mean={centering.predicted_mean.real:.12g}")
    print(f"mean_error={centering.mean_error:.12g}")
    print(f"norm_squared_e_minus_1={centering.raw_shift_norm_squared:.12g}")
    print(f"norm_squared_e_minus_mu={centering.centered_norm_squared:.12g}")
    print(f"carrier_split_error={split.maximum_split_error:.12g}")
    print(f"ibp_relative_error={ibp.relative_identity_error:.12g}")
    print(f"ibp_refinement_error={ibp.refinement_error:.12g}")
    print(f"reciprocal_transfer_error={transfer.transfer_error:.12g}")
    print(
        "natural_centering_coefficient_amplification="
        f"{transfer.coefficient_amplification:.12g}"
    )
    for profile in profiles:
        print(
            f"affine_relative_l2[{profile.profile_name}]="
            f"{profile.relative_l2_residual:.12g}"
        )


if __name__ == "__main__":
    main()
