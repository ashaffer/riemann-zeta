"""Exact ledger and finite algebra checks for the transverse L4 gain.

The mathematical proof is in
``results/ZETA23-QP-TRANSVERSE-FOURTH-MOMENT-GAIN-2026-08-15.md``.
This module deliberately checks only exact exponent arithmetic and the two
finite inequalities used in the proof; it is not a numerical proof of an
asymptotic prime theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import sqrt
from typing import Mapping


@dataclass(frozen=True)
class FourthMomentLedger:
    """Power ledger for a band ``B=Y**aperture`` with ``1<A<2``."""

    aperture: Fraction

    def __post_init__(self) -> None:
        if not Fraction(1) < self.aperture < Fraction(2):
            raise ValueError("the fourth-moment ledger requires 1 < A < 2")

    @property
    def unresolved_pair_exponent(self) -> Fraction:
        return Fraction(2) - self.aperture

    @property
    def kurtosis_exponent(self) -> Fraction:
        return self.unresolved_pair_exponent

    @property
    def transverse_depth_exponent(self) -> Fraction:
        # 1/sqrt(M K), with M=Y^(1+o(1)).
        return (Fraction(1) + self.kurtosis_exponent) / 2

    @property
    def gain_over_dimension_floor(self) -> Fraction:
        return Fraction(1) - self.transverse_depth_exponent

    def even_moment_packet_exponent(self, moment_order: int) -> Fraction:
        """Return the product-packet exponent for the ``2k``-th moment."""

        if not isinstance(moment_order, int) or moment_order < 2:
            raise ValueError("moment_order must be an integer k >= 2")
        return Fraction(moment_order) - self.aperture

    def even_moment_depth_exponent(self, moment_order: int) -> Fraction:
        """Return the transverse exponent delivered by the ``2k`` method.

        The packet factor is ``Y**(k-A)``.  L1--L2--L(2k)
        interpolation costs its ``1/(2(k-1))`` power, and point evaluation
        contributes ``Y**(1/2)``.
        """

        packet = self.even_moment_packet_exponent(moment_order)
        return Fraction(1, 2) + packet / (2 * (moment_order - 1))


def centered_positive_cap_lower(variance: float, fourth_moment: float) -> float:
    """Return the L1-L2-L4 lower bound for ``sup Z`` when ``E Z=0``.

    Interpolation gives ``E|Z| >= variance**(3/2)/sqrt(fourth_moment)``;
    the positive and negative L1 masses are equal.
    """

    if variance < 0.0:
        raise ValueError("variance must be nonnegative")
    if fourth_moment < 0.0:
        raise ValueError("fourth moment must be nonnegative")
    if variance == 0.0:
        return 0.0
    if fourth_moment == 0.0:
        raise ValueError("positive variance cannot have zero fourth moment")
    return variance ** 1.5 / (2.0 * sqrt(fourth_moment))


def ordered_product_convolution(
    coefficients: Mapping[int, float],
) -> dict[int, float]:
    """Return ``b[k]=sum_(nm=k) a[n]a[m]`` over ordered support pairs."""

    result: dict[int, float] = {}
    for n, a_n in coefficients.items():
        if n <= 0:
            raise ValueError("indices must be positive integers")
        for m, a_m in coefficients.items():
            product = n * m
            result[product] = result.get(product, 0.0) + a_n * a_m
    return result


def product_representation_counts(indices: list[int]) -> dict[int, int]:
    """Count ordered representations ``k=nm`` from a finite support."""

    if any(index <= 0 for index in indices):
        raise ValueError("indices must be positive integers")
    result: dict[int, int] = {}
    for n in indices:
        for m in indices:
            product = n * m
            result[product] = result.get(product, 0) + 1
    return result


def convolution_cauchy_bound(coefficients: Mapping[int, float]) -> tuple[float, float]:
    """Compute both sides of the finite convolution Cauchy inequality.

    The returned pair is

    ``(sum_k |b_k|^2, max_k r(k) * (sum_n |a_n|^2)^2)``.
    """

    if not coefficients:
        return 0.0, 0.0
    convolution = ordered_product_convolution(coefficients)
    counts = product_representation_counts(list(coefficients))
    lhs = sum(value * value for value in convolution.values())
    square_mass = sum(value * value for value in coefficients.values())
    rhs = max(counts.values()) * square_mass * square_mass
    return lhs, rhs


def active_ledger() -> FourthMomentLedger:
    return FourthMomentLedger(aperture=Fraction(50, 33))


if __name__ == "__main__":
    ledger = active_ledger()
    print(
        {
            "aperture": str(ledger.aperture),
            "unresolved_pair_exponent": str(ledger.unresolved_pair_exponent),
            "kurtosis_exponent": str(ledger.kurtosis_exponent),
            "transverse_depth_exponent": str(ledger.transverse_depth_exponent),
            "gain_over_dimension_floor": str(ledger.gain_over_dimension_floor),
        }
    )
