"""Exact exponent and hypothesis checks for the weighted near-determinant gate.

This module deliberately does not encode a literature theorem as applicable.
It records the power ledger and the elementary revival obstruction to a
putative absolute third-moment estimate.  The accompanying report gives the
source-by-source hypothesis audit.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class NearDeterminantLedger:
    """Power ledger for ``B=Y**aperture`` with ``1<aperture<2``."""

    aperture: Fraction

    def __post_init__(self) -> None:
        if not Fraction(1) < self.aperture < Fraction(2):
            raise ValueError("require 1 < aperture < 2")

    @property
    def residual_exponent(self) -> Fraction:
        """Exponent of ``H=Y**2/B``."""

        return Fraction(2) - self.aperture

    @property
    def schur_skew_exponent(self) -> Fraction:
        return self.residual_exponent / 2

    @property
    def current_transverse_exponent(self) -> Fraction:
        return Fraction(1, 2) + self.schur_skew_exponent

    @property
    def conjectural_quarter_skew_exponent(self) -> Fraction:
        """Exponent if the signed rank-one norm were ``H**(1/4+o(1))``."""

        return self.residual_exponent / 4

    @property
    def conjectural_quarter_transverse_exponent(self) -> Fraction:
        return Fraction(1, 2) + self.conjectural_quarter_skew_exponent

    @property
    def revival_window_exponent(self) -> Fraction:
        """Exponent of ``L=Y/sqrt(B)`` in the absolute-L3 obstruction."""

        return Fraction(1) - self.aperture / 2

    @property
    def revival_l3_gain_exponent(self) -> Fraction:
        """Power gain in ``B*sqrt(L)/(log Y)**(3/2)`` over ``B``."""

        return self.revival_window_exponent / 2

    @property
    def formal_bettin_chandee_saving(self) -> Fraction:
        """Formal balanced saving if their theorem could be applied.

        With reciprocal-phase variables of lengths ``H,Y,Y``, Theorem 1 of
        Bettin--Chandee saves

            min(H**(3/20) Y**(1/20), Y**(1/8)).

        The report explains why the quotient weight prevents this mapping.
        """

        first = (3 * self.residual_exponent + 1) / 20
        return min(first, Fraction(1, 8))

    @property
    def formal_bettin_chandee_transverse_exponent(self) -> Fraction:
        return self.current_transverse_exponent - self.formal_bettin_chandee_saving


def active_ledger() -> NearDeterminantLedger:
    return NearDeterminantLedger(Fraction(50, 33))


def revival_lower_bound_scale(
    bandwidth: float, window_length: float, prime_count: int
) -> float:
    """Peak-neighborhood lower bound ``(B/L) K**(3/2)``.

    Coefficients are normalized to have l2 norm one on ``K`` nodes.
    Constants from the phase aperture are intentionally omitted.
    """

    if bandwidth <= 0.0:
        raise ValueError("bandwidth must be positive")
    if window_length <= 0.0:
        raise ValueError("window_length must be positive")
    if prime_count <= 0:
        raise ValueError("prime_count must be positive")
    return bandwidth * prime_count**1.5 / window_length


def centered_linear_phase_is_integral(prime: int, twice_center: int, revival: int) -> bool:
    """Check exact alignment at ``t=4*pi*revival*Y``.

    ``twice_center`` is the odd integer ``2Y``.  The linear Taylor phase in
    units of ``2*pi`` is ``revival * (2*prime-twice_center)``.
    """

    if twice_center <= 0 or twice_center % 2 == 0:
        raise ValueError("twice_center must be a positive odd integer")
    if revival < 0:
        raise ValueError("revival must be nonnegative")
    return isinstance(revival * (2 * prime - twice_center), int)


def robert_sargos_curvature(exponent: Fraction) -> Fraction:
    """The curvature factor ``alpha(alpha-1)`` in their Theorem 1."""

    return exponent * (exponent - 1)
