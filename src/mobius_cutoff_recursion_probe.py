#!/usr/bin/env python3
"""Finite falsifier for local Mobius cutoff and scale recursions.

The surviving R73 target permits a genuinely Mobius-specific two-shift
theorem.  A tempting cheaper route is to expose the cutoff one integer at a
time and treat the completed Vaughan field as a martingale or contracting
recursion.  This module tests that idea while retaining every grouped total
product and regenerating the explicit Type-I center at each cutoff.

For ``q=Y+1``, the exact coefficient update is

    a_q-a_Y
      = -mu(q) delta_q * Lambda_(>Y) * 1
        -Lambda(q) mu_(>Y) * delta_q * 1
        +mu(q)Lambda(q) delta_(q^2) * 1.                 (1)

The last term is the intersection restoration required when both cutoffs
move.  The probe verifies (1) coefficientwise, then tests raw energy,
terminal covariance, the zero mode, and their ``1+D`` normalizations.

With the exact unevaluated Type-I head, Vaughan completion makes the field
cutoff-independent; the probe verifies this in the covariance channel.  With
the explicit asymptotic Type-I center used by R71, the finite Euler defect
makes the local steps nonmonotone.  These failures exclude cutoff
monotonicity, a conditional-Pythagorean contraction, and any monotonicity
restored merely by multiplying by a scale-only polynomial or subexponential
factor (the scale is fixed across a cutoff step).  They do *not* exclude the
direct bound ``E <= R^A(1+D)``, a recursion with an additive source comparable
to the new completed energy, or the fixed-exponent R73 two-shift estimate.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np

from type2_block_mechanism_probe import _arithmetic_sieve
from ward_nonlocal_covariance_probe import (
    NonlocalCovarianceAudit,
    _grouped_tail_coefficients,
    audit_nonlocal_covariance,
)


@dataclass(frozen=True)
class CoefficientShellCheck:
    cutoff: int
    next_cutoff: int
    limit: int
    maximum_error: float
    worst_product: int
    changed_products: tuple[int, ...]


def verify_cutoff_shell_identity(
    cutoff: int, limit: int
) -> CoefficientShellCheck:
    """Verify the exact simultaneous-cutoff update (1) through ``limit``."""

    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    if limit <= cutoff + 1:
        raise ValueError("limit must exceed the next cutoff")
    q_value = cutoff + 1
    mu, _, mangoldt, _ = _arithmetic_sieve(limit)
    old = _grouped_tail_coefficients(cutoff, limit, mu, mangoldt)
    new = _grouped_tail_coefficients(q_value, limit, mu, mangoldt)
    predicted = np.zeros(limit + 1)

    mu_q = mu[q_value]
    lambda_q = mangoldt[q_value]
    if mu_q:
        for b_value in range(cutoff + 1, limit // q_value + 1):
            if not mangoldt[b_value]:
                continue
            product = q_value * b_value
            predicted[product : limit + 1 : product] += (
                -mu_q * mangoldt[b_value]
            )
    if lambda_q:
        for divisor in range(cutoff + 1, limit // q_value + 1):
            if not mu[divisor]:
                continue
            product = q_value * divisor
            predicted[product : limit + 1 : product] += (
                -lambda_q * mu[divisor]
            )
    square = q_value * q_value
    if mu_q and lambda_q and square <= limit:
        predicted[square : limit + 1 : square] += mu_q * lambda_q

    actual = new - old
    errors = np.abs(actual - predicted)
    worst_product = int(np.argmax(errors))
    changed = tuple(
        int(value)
        for value in np.flatnonzero(np.abs(actual) > 2.0e-15)
    )
    return CoefficientShellCheck(
        cutoff,
        q_value,
        limit,
        float(errors[worst_product]),
        worst_product,
        changed,
    )


def _normalized(energy: float, diagonal: float) -> float:
    return energy / (1.0 + diagonal)


@dataclass(frozen=True)
class CutoffRecursionAudit:
    lower: NonlocalCovarianceAudit
    upper: NonlocalCovarianceAudit
    shell: CoefficientShellCheck
    raw_energy_ratio: float
    normalized_raw_ratio: float
    normalized_covariance_ratio: float
    normalized_zero_mode_ratio: float
    exact_covariance_ratio: float
    exact_covariance_difference: float
    raw_contraction_margin: float
    normalized_raw_contraction_margin: float
    normalized_covariance_contraction_margin: float
    normalized_zero_mode_contraction_margin: float


def audit_cutoff_step(
    scale: float = 25.0,
    cutoff: int = 2,
    step: float = 0.04,
    input_order: int = 1,
    macro_order: int = 1,
    gaussian_order: int = 16,
) -> CutoffRecursionAudit:
    """Audit ``Y -> Y+1`` at one fixed scale with full completion."""

    coboundary_width = input_order * step
    if (cutoff + 1) ** 2 > scale * math.exp(-coboundary_width):
        raise ValueError("upper cutoff violates the support condition")
    arguments = dict(
        scale=scale,
        step=step,
        input_order=input_order,
        macro_order=macro_order,
        gaussian_order=gaussian_order,
        spectral_frequencies=(0.0,),
    )
    lower = audit_nonlocal_covariance(cutoff=cutoff, **arguments)
    upper = audit_nonlocal_covariance(cutoff=cutoff + 1, **arguments)
    shell = verify_cutoff_shell_identity(cutoff, lower.arithmetic_limit)

    lower_raw = _normalized(lower.raw_energy, lower.tail_diagonal_raw)
    upper_raw = _normalized(upper.raw_energy, upper.tail_diagonal_raw)
    lower_covariance = _normalized(
        lower.full_innovation, lower.tail_diagonal_covariance
    )
    upper_covariance = _normalized(
        upper.full_innovation, upper.tail_diagonal_covariance
    )
    lower_zero = _normalized(
        lower.retained_energy, lower.tail_diagonal_retained
    )
    upper_zero = _normalized(
        upper.retained_energy, upper.tail_diagonal_retained
    )
    return CutoffRecursionAudit(
        lower,
        upper,
        shell,
        upper.raw_energy / lower.raw_energy,
        upper_raw / lower_raw,
        upper_covariance / lower_covariance,
        upper_zero / lower_zero,
        upper.exact_full_innovation / lower.exact_full_innovation,
        upper.exact_full_innovation - lower.exact_full_innovation,
        lower.raw_energy - upper.raw_energy,
        lower_raw - upper_raw,
        lower_covariance - upper_covariance,
        lower_zero - upper_zero,
    )


@dataclass(frozen=True)
class ScaleRecursionAudit:
    lower: NonlocalCovarianceAudit
    upper: NonlocalCovarianceAudit
    normalized_raw_ratio: float
    normalized_covariance_ratio: float
    normalized_zero_mode_ratio: float


def audit_scale_step(
    lower_scale: float,
    upper_scale: float,
    cutoff: int,
    step: float = 0.04,
    input_order: int = 1,
    macro_order: int = 1,
    gaussian_order: int = 16,
) -> ScaleRecursionAudit:
    """Compare two adjacent scales with one genuinely frozen cutoff."""

    if not lower_scale < upper_scale:
        raise ValueError("require lower_scale < upper_scale")
    arguments = dict(
        cutoff=cutoff,
        step=step,
        input_order=input_order,
        macro_order=macro_order,
        gaussian_order=gaussian_order,
        spectral_frequencies=(0.0,),
    )
    lower = audit_nonlocal_covariance(scale=lower_scale, **arguments)
    upper = audit_nonlocal_covariance(scale=upper_scale, **arguments)

    def ratios(left: NonlocalCovarianceAudit, right: NonlocalCovarianceAudit):
        return (
            _normalized(right.raw_energy, right.tail_diagonal_raw)
            / _normalized(left.raw_energy, left.tail_diagonal_raw),
            _normalized(
                right.full_innovation, right.tail_diagonal_covariance
            )
            / _normalized(
                left.full_innovation, left.tail_diagonal_covariance
            ),
            _normalized(
                right.retained_energy, right.tail_diagonal_retained
            )
            / _normalized(
                left.retained_energy, left.tail_diagonal_retained
            ),
        )

    raw_ratio, covariance_ratio, zero_ratio = ratios(lower, upper)
    return ScaleRecursionAudit(
        lower,
        upper,
        raw_ratio,
        covariance_ratio,
        zero_ratio,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=float, default=25.0)
    parser.add_argument("--cutoff", type=int, default=2)
    parser.add_argument("--step", type=float, default=0.04)
    parser.add_argument("--input-order", type=int, default=1)
    parser.add_argument("--macro-order", type=int, default=1)
    args = parser.parse_args()
    audit = audit_cutoff_step(
        args.scale,
        args.cutoff,
        args.step,
        args.input_order,
        args.macro_order,
    )
    lower = audit.lower
    upper = audit.upper
    print(
        f"X={lower.scale:g} h={lower.step:g} "
        f"Y={lower.cutoff}->{upper.cutoff}"
    )
    print(
        f"products {lower.active_tail_product_values} -> "
        f"{upper.active_tail_product_values}"
    )
    print(
        f"D_raw {lower.tail_diagonal_raw:.12g} -> "
        f"{upper.tail_diagonal_raw:.12g}; "
        f"E_raw {lower.raw_energy:.12g} -> {upper.raw_energy:.12g}"
    )
    print(
        f"ratios raw={audit.raw_energy_ratio:.9g} "
        f"normalized={audit.normalized_raw_ratio:.9g} "
        f"covariance={audit.normalized_covariance_ratio:.9g} "
        f"zero={audit.normalized_zero_mode_ratio:.9g} "
        f"exact-covariance={audit.exact_covariance_ratio:.9g}"
    )
    print(
        f"shell max error={audit.shell.maximum_error:.3g}; "
        f"changed products={audit.shell.changed_products}"
    )


if __name__ == "__main__":
    main()
