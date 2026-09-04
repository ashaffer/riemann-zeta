"""Finite algebra ledger for the transverse product-bin power barrier.

The asymptotic prime and analytic arguments are proved in
``results/ZETA23-QP-TRANSVERSE-PRODUCT-BIN-POWER-BARRIER-2026-08-15.md``.
This module checks only the exact exponent and pigeonhole arithmetic.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil


@dataclass(frozen=True)
class ProductBinBarrierLedger:
    """Power ledger for ``B=Y**A`` and ``Delta=Y**(2-A)``."""

    aperture: Fraction

    def __post_init__(self) -> None:
        if not Fraction(1) < self.aperture < Fraction(2):
            raise ValueError("the product-bin barrier requires 1 < A < 2")

    @property
    def product_bin_exponent(self) -> Fraction:
        return Fraction(2) - self.aperture

    @property
    def fourth_moment_transverse_exponent(self) -> Fraction:
        return (Fraction(1) + self.product_bin_exponent) / 2

    def proposed_saved_bin_exponent(self, saving: Fraction) -> Fraction:
        if not Fraction(0) < saving < Fraction(1):
            raise ValueError("saving must lie strictly between zero and one")
        return self.product_bin_exponent * (Fraction(1) - saving)


def pigeonhole_maximum(total_objects: int, number_of_bins: int) -> int:
    """Minimum possible largest bin occupancy."""

    if total_objects < 0:
        raise ValueError("total_objects must be nonnegative")
    if number_of_bins <= 0:
        raise ValueError("number_of_bins must be positive")
    return ceil(total_objects / number_of_bins)


def kurtosis_spike_lower(
    coordinate_count: int,
    band_scale: float,
    spike_height_fraction: float,
    spike_width: float,
    density_fraction: float,
    quadratic_upper_constant: float,
) -> float:
    """Return the deterministic local-spike lower bound on ``Q4/Q2**2``.

    The assumptions encoded here are ``|F| >= height_fraction*M`` on a
    time interval of the given width, ``rho >= density_fraction/B`` there,
    and ``Q2 <= quadratic_upper_constant*M``.
    """

    if coordinate_count <= 0 or band_scale <= 0.0:
        raise ValueError("coordinate_count and band_scale must be positive")
    values = (
        spike_height_fraction,
        spike_width,
        density_fraction,
        quadratic_upper_constant,
    )
    if any(value <= 0.0 for value in values):
        raise ValueError("all spike constants must be positive")
    fourth_lower = (
        spike_width
        * density_fraction
        * (spike_height_fraction * coordinate_count) ** 4
        / band_scale
    )
    quadratic_upper = quadratic_upper_constant * coordinate_count
    return fourth_lower / (quadratic_upper * quadratic_upper)


def active_ledger() -> ProductBinBarrierLedger:
    return ProductBinBarrierLedger(aperture=Fraction(50, 33))
