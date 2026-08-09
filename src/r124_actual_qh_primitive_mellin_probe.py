#!/usr/bin/env python3
"""Numerical sign audit for the actual Q_h primitive Mellin kernel.

This probe uses the repository's exact fixed-step compact B-spline window
``W_(a,k)``, applies the R102 center annihilator

    V_Q(x) = V(x+2h)-2 exp(h/2)V(x+h)+exp(h)V(x),

forms

    f_R(t)=t^(-1/2)V_Q(R-log(t)),
    L(t,u)=integral psi(R)f_R(t)f_R(u)dR,
    Phi(x)=sum_(nu,ell) L(ell-nu*x,nu),

and samples the Hermitian multiplicative kernel

    k_H(u)=1/2[e^(-u/2)Phi(e^u)+e^(u/2)Phi(e^(-u))].

Its cosine transform is the primitive Hermitian Mellin multiplier.  The
calculation retains the whole requested comparable-ratio shell
``exp(-U)<=x<=exp(U)``.  It is a floating diagnostic, not an interval
certificate and not an estimate for Mobius sums.  The exact identity

    Phi(1)=integral psi(R)|sum_n f_R(n)|^2 dR

is evaluated independently as a normalization check.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from numpy.polynomial.legendre import leggauss

from fixed_step_spectral_cooling_probe import compact_window


@dataclass(frozen=True)
class PrimitiveMellinAudit:
    base_step: float
    order: int
    q_step: float
    localizer_half_width: float
    ratio_half_width: float
    integer_sample_count: int
    phi_at_one: float
    integer_gram_value: float
    integer_gram_error: float
    kernel_at_zero: float
    maximum_kernel_modulus_ratio: float
    lambda_at_zero: float
    minimum_lambda_frequency: float
    minimum_lambda: float
    maximum_lambda_frequency: float
    maximum_lambda: float
    sign_change_intervals: tuple[tuple[float, float], ...]


def qh_compact_profile(
    value: float, base_step: float, order: int, q_step: float
) -> float:
    """Return the exact three-translate Q_h image of the compact window."""

    if not math.isfinite(base_step) or base_step <= 0.0:
        raise ValueError("base_step must be finite and positive")
    if not isinstance(order, int) or isinstance(order, bool) or order < 1:
        raise ValueError("order must be a positive integer")
    if not math.isfinite(q_step) or q_step <= 0.0:
        raise ValueError("q_step must be finite and positive")
    coefficient = math.exp(q_step / 2.0)
    return (
        compact_window(value + 2.0 * q_step, base_step, order)
        - 2.0
        * coefficient
        * compact_window(value + q_step, base_step, order)
        + coefficient * coefficient * compact_window(value, base_step, order)
    )


def _localizer_quadrature(
    half_width: float, gaussian_order: int
) -> tuple[np.ndarray, np.ndarray]:
    if not math.isfinite(half_width) or half_width <= 0.0:
        raise ValueError("localizer_half_width must be finite and positive")
    if gaussian_order < 4:
        raise ValueError("localizer_order must be at least four")
    nodes, weights = leggauss(gaussian_order)
    nodes = half_width * nodes
    weights = half_width * weights
    taper = np.maximum(0.0, 1.0 - (nodes / half_width) ** 2) ** 2
    weights *= taper
    weights /= float(np.sum(weights))
    return nodes, weights


def primitive_mellin_audit(
    base_step: float = 0.2,
    order: int = 4,
    q_step: float = 0.2,
    localizer_half_width: float = 0.03,
    ratio_half_width: float = math.log(2.0),
    localizer_order: int = 10,
    ratio_nodes: int = 3001,
    tau_maximum: float = 30.0,
    tau_count: int = 151,
) -> PrimitiveMellinAudit:
    """Evaluate the actual primitive multiplier on one full ratio shell."""

    if not math.isfinite(ratio_half_width) or ratio_half_width <= 0.0:
        raise ValueError("ratio_half_width must be finite and positive")
    if ratio_nodes < 101 or ratio_nodes % 2 == 0:
        raise ValueError("ratio_nodes must be an odd integer at least 101")
    if not math.isfinite(tau_maximum) or tau_maximum <= 0.0:
        raise ValueError("tau_maximum must be finite and positive")
    if tau_count < 3:
        raise ValueError("tau_count must be at least three")

    output_nodes, output_weights = _localizer_quadrature(
        localizer_half_width, localizer_order
    )
    width = order * base_step
    profile_lower = -width - 2.0 * q_step
    profile_upper = width

    log_ratio = np.linspace(-ratio_half_width, ratio_half_width, ratio_nodes)
    hermitian_kernel = np.zeros(ratio_nodes, dtype=float)
    phi_at_one = 0.0
    integer_gram = 0.0
    maximum_integer_samples = 0

    for output, output_weight in zip(output_nodes, output_weights):
        physical_lower = math.exp(float(output) - profile_upper)
        physical_upper = math.exp(float(output) - profile_lower)
        first_integer = max(1, math.ceil(physical_lower))
        last_integer = math.floor(physical_upper)

        def profile(physical: float) -> float:
            if physical <= 0.0:
                return 0.0
            logarithmic = float(output) - math.log(physical)
            if logarithmic <= profile_lower or logarithmic >= profile_upper:
                return 0.0
            return physical ** (-0.5) * qh_compact_profile(
                logarithmic, base_step, order, q_step
            )

        integer_samples = tuple(
            (integer, profile(float(integer)))
            for integer in range(first_integer, last_integer + 1)
            if abs(profile(float(integer))) > 1.0e-14
        )
        maximum_integer_samples = max(
            maximum_integer_samples, len(integer_samples)
        )
        integer_sum = math.fsum(value for _, value in integer_samples)
        integer_gram += float(output_weight) * integer_sum * integer_sum

        def phi(ratio: float) -> float:
            terms: list[float] = []
            for integer, sample in integer_samples:
                lower_ell = math.ceil(integer * ratio + physical_lower)
                upper_ell = math.floor(integer * ratio + physical_upper)
                for ell in range(lower_ell, upper_ell + 1):
                    terms.append(profile(ell - integer * ratio) * sample)
            return math.fsum(terms)

        phi_one_at_output = phi(1.0)
        phi_at_one += float(output_weight) * phi_one_at_output
        for index, logarithmic_ratio in enumerate(log_ratio):
            ratio = math.exp(float(logarithmic_ratio))
            forward = ratio ** (-0.5) * phi(ratio)
            reverse = ratio ** 0.5 * phi(1.0 / ratio)
            hermitian_kernel[index] += (
                0.5 * float(output_weight) * (forward + reverse)
            )

    integration_weights = np.ones(ratio_nodes, dtype=float)
    integration_weights[0] = integration_weights[-1] = 0.5
    integration_weights *= log_ratio[1] - log_ratio[0]
    frequencies = np.linspace(0.0, tau_maximum, tau_count)
    multiplier = np.cos(np.outer(frequencies, log_ratio)) @ (
        integration_weights * hermitian_kernel
    )
    sign_changes: list[tuple[float, float]] = []
    for left, right, left_value, right_value in zip(
        frequencies[:-1], frequencies[1:], multiplier[:-1], multiplier[1:]
    ):
        if left_value * right_value < 0.0:
            sign_changes.append((float(left), float(right)))

    minimum_index = int(np.argmin(multiplier))
    maximum_index = int(np.argmax(multiplier))
    kernel_at_zero = float(hermitian_kernel[ratio_nodes // 2])
    if kernel_at_zero <= 0.0:
        modulus_ratio = math.inf
    else:
        modulus_ratio = float(
            np.max(np.abs(hermitian_kernel)) / kernel_at_zero
        )
    return PrimitiveMellinAudit(
        base_step=base_step,
        order=order,
        q_step=q_step,
        localizer_half_width=localizer_half_width,
        ratio_half_width=ratio_half_width,
        integer_sample_count=maximum_integer_samples,
        phi_at_one=phi_at_one,
        integer_gram_value=integer_gram,
        integer_gram_error=abs(phi_at_one - integer_gram),
        kernel_at_zero=kernel_at_zero,
        maximum_kernel_modulus_ratio=modulus_ratio,
        lambda_at_zero=float(multiplier[0]),
        minimum_lambda_frequency=float(frequencies[minimum_index]),
        minimum_lambda=float(multiplier[minimum_index]),
        maximum_lambda_frequency=float(frequencies[maximum_index]),
        maximum_lambda=float(multiplier[maximum_index]),
        sign_change_intervals=tuple(sign_changes),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-step", type=float, default=0.2)
    parser.add_argument("--order", type=int, default=4)
    parser.add_argument("--q-step", type=float, default=0.2)
    parser.add_argument("--localizer-half-width", type=float, default=0.03)
    parser.add_argument("--ratio-half-width", type=float, default=math.log(2.0))
    parser.add_argument("--localizer-order", type=int, default=10)
    parser.add_argument("--ratio-nodes", type=int, default=3001)
    parser.add_argument("--tau-maximum", type=float, default=30.0)
    parser.add_argument("--tau-count", type=int, default=151)
    args = parser.parse_args()
    audit = primitive_mellin_audit(
        base_step=args.base_step,
        order=args.order,
        q_step=args.q_step,
        localizer_half_width=args.localizer_half_width,
        ratio_half_width=args.ratio_half_width,
        localizer_order=args.localizer_order,
        ratio_nodes=args.ratio_nodes,
        tau_maximum=args.tau_maximum,
        tau_count=args.tau_count,
    )
    print("rating=D floating sign diagnostic; no arithmetic estimate")
    print(
        f"base-step={audit.base_step:g} order={audit.order} "
        f"Q-step={audit.q_step:g} output-half-width="
        f"{audit.localizer_half_width:g} ratio-half-width="
        f"{audit.ratio_half_width:.9g}"
    )
    print(
        f"Phi(1)={audit.phi_at_one:+.12g} "
        f"integer-Gram={audit.integer_gram_value:+.12g} "
        f"closure={audit.integer_gram_error:.3e} "
        f"integer-samples<={audit.integer_sample_count}"
    )
    print(
        f"k_H(0)={audit.kernel_at_zero:+.12g} "
        f"max|k_H|/k_H(0)={audit.maximum_kernel_modulus_ratio:.9g}"
    )
    print(
        f"lambda(0)={audit.lambda_at_zero:+.12g} "
        f"minimum=lambda({audit.minimum_lambda_frequency:.6g})="
        f"{audit.minimum_lambda:+.12g} "
        f"maximum=lambda({audit.maximum_lambda_frequency:.6g})="
        f"{audit.maximum_lambda:+.12g}"
    )
    print(f"sampled sign-change intervals={audit.sign_change_intervals}")


if __name__ == "__main__":
    main()
