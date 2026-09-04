"""Exact checks for the balanced all-plus character-method barrier."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import sqrt
from typing import Iterable


@dataclass(frozen=True)
class BalancedAllPlusLedger:
    aperture: Fraction

    def __post_init__(self) -> None:
        if not Fraction(3, 2) < self.aperture < Fraction(2):
            raise ValueError("require 3/2 < aperture < 2")

    @property
    def residual_exponent(self) -> Fraction:
        return Fraction(2) - self.aperture

    @property
    def all_plus_width_exponent(self) -> Fraction:
        return Fraction(1) + self.residual_exponent

    @property
    def raw_schur_exponent(self) -> Fraction:
        return self.residual_exponent / 2

    @property
    def character_parseval_exponent(self) -> Fraction:
        return self.all_plus_width_exponent / 2

    @property
    def character_penalty(self) -> Fraction:
        return self.character_parseval_exponent - self.raw_schur_exponent

    @property
    def principal_exponent(self) -> Fraction:
        return self.residual_exponent - Fraction(1, 2)


def active_ledger() -> BalancedAllPlusLedger:
    return BalancedAllPlusLedger(Fraction(50, 33))


def nonprincipal_parseval_floor(group_order: int, set_size: int) -> float:
    """Floor for the largest nonprincipal Fourier coefficient of a set."""

    if group_order <= 1:
        raise ValueError("group_order must exceed one")
    if not 0 < set_size < group_order:
        raise ValueError("require 0 < set_size < group_order")
    return sqrt((group_order * set_size - set_size * set_size) / (group_order - 1))


def centered_residual_holds(product: int, prime: int, width: int) -> bool:
    return abs(8 * product - prime**3) <= width


def cubic_residue_holds(product: int, prime: int, width: int) -> bool:
    """Membership in the signed width window around zero modulo ``prime**3``."""

    modulus = prime**3
    residue = (8 * product) % modulus
    signed_distance = min(residue, modulus - residue)
    return signed_distance <= width


def residual_equivalence_on_nodes(
    nodes: Iterable[int], prime: int, width: int
) -> bool:
    values = tuple(nodes)
    return all(
        centered_residual_holds(a * b * c, prime, width)
        == cubic_residue_holds(a * b * c, prime, width)
        for a in values
        for b in values
        for c in values
    )


def latin_square_uniform_norm(order: int) -> float:
    """Trilinear value on normalized constants for ``a+b+c=0 mod order``."""

    if order <= 0:
        raise ValueError("order must be positive")
    edge_count = order * order
    return edge_count / order ** 1.5
