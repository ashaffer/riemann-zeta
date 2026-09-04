"""Exponent ledger for the exact DFI band-pass zero-arc collapse.

The mathematical proof is recorded in
``results/ZETA23-QP-EXACT-DFI-BANDPASS-ZERO-ARC-COLLAPSE-2026-08-22.md``.
This module keeps the scale comparisons exact and machine-checkable.
"""

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class DFIBandpassZeroArcLedger:
    degree_exponent: Fraction
    delta_modulus_exponent: Fraction
    stationary_frequency_exponent: Fraction
    product_exponent: Fraction
    mismatch_exponent: Fraction
    transition_modulus_exponent: Fraction
    mismatch_over_delta_modulus_exponent: Fraction
    mismatch_over_delta_modulus_in_degree: Fraction
    maximal_positive_frozen_extension_in_degree: Fraction
    endpoint_positive_frozen_loss_in_degree: Fraction
    nonzero_farey_sector_rapidly_decaying: bool
    noncoprime_sector_requires_separate_poisson: bool
    ramanujan_axis_requires_separate_absolute_bound: bool
    zero_arc_bound_proved: bool
    four_cycle_improvement_proved: bool


def dfi_bandpass_zero_arc_ledger() -> DFIBandpassZeroArcLedger:
    """Return the balanced exact exponents and proof-status flags."""

    degree = Fraction(16, 33)
    delta_modulus = Fraction(25, 33)
    stationary_frequency = Fraction(17, 33)
    product = Fraction(84, 33)
    mismatch = Fraction(34, 33)
    transition = mismatch - delta_modulus
    gap = mismatch - delta_modulus
    return DFIBandpassZeroArcLedger(
        degree_exponent=degree,
        delta_modulus_exponent=delta_modulus,
        stationary_frequency_exponent=stationary_frequency,
        product_exponent=product,
        mismatch_exponent=mismatch,
        transition_modulus_exponent=transition,
        mismatch_over_delta_modulus_exponent=gap,
        mismatch_over_delta_modulus_in_degree=gap / degree,
        maximal_positive_frozen_extension_in_degree=Fraction(1, 16),
        endpoint_positive_frozen_loss_in_degree=Fraction(5, 8),
        nonzero_farey_sector_rapidly_decaying=True,
        noncoprime_sector_requires_separate_poisson=False,
        ramanujan_axis_requires_separate_absolute_bound=False,
        zero_arc_bound_proved=False,
        four_cycle_improvement_proved=False,
    )
