"""Exact ledgers for the balanced curved-incidence theorem-class barrier."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil, log
from typing import Iterable


@dataclass(frozen=True)
class CurvedIncidenceLedger:
    aperture: Fraction

    def __post_init__(self) -> None:
        if not Fraction(3, 2) < self.aperture < Fraction(2):
            raise ValueError("require 3/2 < aperture < 2")

    @property
    def residual_exponent(self) -> Fraction:
        return Fraction(2) - self.aperture

    @property
    def hard_width_exponent(self) -> Fraction:
        return Fraction(1) + self.residual_exponent

    @property
    def raw_tensor_exponent(self) -> Fraction:
        return self.residual_exponent / 2

    @property
    def lettington_curvature_exponent(self) -> Fraction:
        return Fraction(3, 2)

    @property
    def lettington_loss(self) -> Fraction:
        return self.lettington_curvature_exponent - self.hard_width_exponent


def active_ledger() -> CurvedIncidenceLedger:
    return CurvedIncidenceLedger(Fraction(50, 33))


def logarithmic_group_sum(a: float, b: float, c: float, residual: float, center: float) -> float:
    """The exceptional Elekes--Szabo coordinate sum for ``abc=center+residual``."""

    if min(a, b, c, center + residual) <= 0.0:
        raise ValueError("all logarithm arguments must be positive")
    return log(a) + log(b) + log(c) - log(center + residual)


def pigeonhole_pair_energy_floor(pair_count: int, ambient_length: int, bin_width: int) -> float:
    """Cauchy floor ``pair_count**2 / number_of_bins``."""

    if min(pair_count, ambient_length, bin_width) <= 0:
        raise ValueError("all inputs must be positive")
    bins = ceil(ambient_length / bin_width)
    return pair_count * pair_count / bins


def exact_binned_product_energy(nodes: Iterable[int], bin_width: int) -> int:
    """Sum of squared ordered-product occupancies in fixed integer bins."""

    if bin_width <= 0:
        raise ValueError("bin_width must be positive")
    values = tuple(nodes)
    if not values:
        raise ValueError("nodes must be nonempty")
    products = [left * right for left in values for right in values]
    origin = min(products)
    occupancies: dict[int, int] = {}
    for product in products:
        index = (product - origin) // bin_width
        occupancies[index] = occupancies.get(index, 0) + 1
    return sum(count * count for count in occupancies.values())
