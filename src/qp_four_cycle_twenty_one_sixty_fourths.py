"""Exact exponent ledger for the D^(21/16) four-cycle theorem."""

from __future__ import annotations

from fractions import Fraction


Q_IN_D = Fraction(33, 16)
MAX_TWO_MINIMUM_PRODUCT = Fraction(2, 3) * Q_IN_D
MAX_SLICE_EXPONENT = 1 + MAX_TWO_MINIMUM_PRODUCT - Q_IN_D
FOURTH_TRACE_EXPONENT = 1 + MAX_SLICE_EXPONENT
OPERATOR_EXPONENT = FOURTH_TRACE_EXPONENT / 4
TRANSVERSE_EXPONENT = Fraction(1, 2) + OPERATOR_EXPONENT * Fraction(16, 33)


def curvature_times_gap_mass_exponent(height_exponent: Fraction) -> Fraction:
    """Return the exponent of ``sqrt(D/H)*sqrt(DH)``."""

    return (1 - height_exponent) / 2 + (1 + height_exponent) / 2

