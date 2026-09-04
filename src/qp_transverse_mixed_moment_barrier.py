"""Exact checks for the transverse mixed-cubic moment frontier."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import sqrt


@dataclass(frozen=True)
class MixedMomentLedger:
    """Power ledger for ``B=Y**A`` and the cubic incidence argument."""

    aperture: Fraction

    def __post_init__(self) -> None:
        if not Fraction(1) < self.aperture < Fraction(2):
            raise ValueError("require 1 < aperture < 2")

    @property
    def packet_exponent(self) -> Fraction:
        return Fraction(2) - self.aperture

    @property
    def cubic_schur_exponent(self) -> Fraction:
        return self.packet_exponent / 2

    @property
    def generic_leverage_exponent(self) -> Fraction:
        return Fraction(1, 2)

    @property
    def transverse_exponent(self) -> Fraction:
        return self.generic_leverage_exponent + self.cubic_schur_exponent


def endpoint_ratio_from_skewness(skewness: float) -> float:
    """Sharp lower bound for ``ess_sup(Z)/sqrt(Var Z)`` from skewness."""

    return (skewness + sqrt(skewness * skewness + 4.0)) / 2.0


def endpoint_ratio_from_negative_skew_bound(bound: float) -> float:
    """Sharp endpoint ratio when standardized skewness is at least ``-bound``."""

    if bound < 0.0:
        raise ValueError("bound must be nonnegative")
    return endpoint_ratio_from_skewness(-bound)


def minimum_bin_collision_count(item_count: int, bin_count: int) -> int:
    """Minimum possible ``sum count_i**2`` for items placed in bins.

    The balanced placement realizes the minimum, giving an exact integer
    version of the Cauchy--Schwarz packing estimate.
    """

    if item_count < 0:
        raise ValueError("item_count must be nonnegative")
    if bin_count <= 0:
        raise ValueError("bin_count must be positive")
    quotient, remainder = divmod(item_count, bin_count)
    return remainder * (quotient + 1) ** 2 + (bin_count - remainder) * quotient**2


def uniform_pair_energy_floor(node_count: int, bin_count: int) -> float:
    """Packing floor for uniform normalized coefficients on ordered pairs."""

    if node_count <= 0:
        raise ValueError("node_count must be positive")
    collisions = minimum_bin_collision_count(node_count * node_count, bin_count)
    return collisions / float(node_count * node_count)


def two_point_standardized_moments(positive_probability: float) -> tuple[float, float]:
    """Return endpoint ratio and skewness for a mean-zero two-point law.

    The positive atom is set to one.  The negative atom is then chosen to
    make the mean zero.
    """

    probability = positive_probability
    if not 0.0 < probability < 1.0:
        raise ValueError("probability must lie strictly between zero and one")
    negative_atom = probability / (1.0 - probability)
    variance = probability + (1.0 - probability) * negative_atom**2
    third = probability - (1.0 - probability) * negative_atom**3
    return 1.0 / sqrt(variance), third / variance**1.5


def active_ledger() -> MixedMomentLedger:
    return MixedMomentLedger(Fraction(50, 33))
