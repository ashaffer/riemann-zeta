"""Exact exponent ledger for the central/one-sided sector combination gate."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class SectorCombinationLedger:
    """Power exponents in the prime-half-center sector classification."""

    aperture: Fraction
    packet_exponent: Fraction

    def __post_init__(self) -> None:
        if not Fraction(3, 2) < self.aperture < Fraction(2):
            raise ValueError("require 3/2 < aperture < 2")
        if not Fraction(0) <= self.packet_exponent < Fraction(1, 2):
            raise ValueError("require 0 <= packet_exponent < 1/2")

    @property
    def residual_exponent(self) -> Fraction:
        return Fraction(2) - self.aperture

    @property
    def raw_skew_exponent(self) -> Fraction:
        return self.residual_exponent / 2

    @property
    def full_shell_baseline(self) -> Fraction:
        return Fraction(1, 2) + self.raw_skew_exponent

    @property
    def burgess_skew_exponent(self) -> Fraction:
        return self.residual_exponent / 4 + Fraction(3, 32)

    @property
    def burgess_threshold(self) -> Fraction:
        """Amplitude-purity exponent needed to reach the Burgess plateau."""

        return self.raw_skew_exponent - self.burgess_skew_exponent

    def side_dominant_exponent(self, purity: Fraction) -> Fraction:
        if purity < 0:
            raise ValueError("purity must be nonnegative")
        return Fraction(1, 2) + max(
            self.burgess_skew_exponent,
            self.raw_skew_exponent - purity,
        )

    def central_dominant_exponent(self, purity: Fraction) -> Fraction:
        if purity < 0:
            raise ValueError("purity must be nonnegative")
        leverage = max(
            self.packet_exponent / 2,
            Fraction(1, 2) - purity,
        )
        skew = max(Fraction(0), self.raw_skew_exponent - purity)
        return leverage + skew


def active_ledger(epsilon: Fraction = Fraction(1, 100)) -> SectorCombinationLedger:
    return SectorCombinationLedger(
        aperture=Fraction(50, 33),
        packet_exponent=Fraction(1, 2) - epsilon,
    )
