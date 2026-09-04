"""Exact ledgers for the balanced cross-side cubic character barrier.

At a prime half-centre ``Y=q/2`` the difficult cross-side cubic relation is

    |8*a*b*c - q**3| <= D,   D=q*R,   R=q**(2-A).

The routines below replay the exponent arithmetic and the two elementary
restricted-set interpolations.  They do not claim that the actual tensor
saturates the Schur bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import sqrt


@dataclass(frozen=True)
class BalancedCrossTensorLedger:
    """Power ledger for ``3/2 < A < 2``."""

    aperture: Fraction

    def __post_init__(self) -> None:
        if not Fraction(3, 2) < self.aperture < Fraction(2):
            raise ValueError("require 3/2 < aperture < 2")

    @property
    def row_exponent(self) -> Fraction:
        """Exponent ``h`` in the fixed-fibre size ``R=q**h``."""

        return Fraction(2) - self.aperture

    @property
    def residual_exponent(self) -> Fraction:
        """Exponent in ``D=qR=q**(3-A)``."""

        return Fraction(1) + self.row_exponent

    @property
    def schur_tensor_exponent(self) -> Fraction:
        return self.row_exponent / 2

    @property
    def full_transverse_exponent(self) -> Fraction:
        return Fraction(1, 2) + self.schur_tensor_exponent

    @property
    def q2_parseval_character_floor(self) -> Fraction:
        """Exponent forced on some nonprincipal interval character sum."""

        return self.residual_exponent / 2

    @property
    def character_to_schur_gap(self) -> Fraction:
        return self.q2_parseval_character_floor - self.schur_tensor_exponent

    @property
    def formal_principal_tensor_exponent(self) -> Fraction:
        """Best exponent if the nonprincipal discrepancy were absent."""

        return self.row_exponent - Fraction(1, 4)

    @property
    def formal_principal_transverse_exponent(self) -> Fraction:
        return Fraction(1, 2) + self.formal_principal_tensor_exponent

    @property
    def formal_principal_saving(self) -> Fraction:
        return (
            self.full_transverse_exponent
            - self.formal_principal_transverse_exponent
        )


def active_ledger() -> BalancedCrossTensorLedger:
    return BalancedCrossTensorLedger(Fraction(50, 33))


def normalized_fibre_pair_bound(
    first_size: float,
    second_size: float,
    third_size: float,
    row_length: float,
) -> float:
    """Return ``min(R*x,x*y)/sqrt(x*y*z)`` after sorting sizes."""

    if min(first_size, second_size, third_size, row_length) <= 0:
        raise ValueError("sizes and row_length must be positive")
    x, y, z = sorted((first_size, second_size, third_size))
    return min(row_length * x, x * y) / sqrt(x * y * z)


def normalized_principal_fibre_pair_bound(
    first_size: float,
    second_size: float,
    third_size: float,
    row_length: float,
    modulus_root: float,
) -> float:
    """Add the mod-``q^2`` principal incidence bound.

    The principal density is ``D/q^2=R/q``.
    """

    if min(
        first_size,
        second_size,
        third_size,
        row_length,
        modulus_root,
    ) <= 0:
        raise ValueError("all inputs must be positive")
    x, y, z = sorted((first_size, second_size, third_size))
    principal = (row_length / modulus_root) * x * y * z
    return min(principal, row_length * x, x * y) / sqrt(x * y * z)


def nonprincipal_parseval_floor(unit_interval_size: int, phi: int) -> float:
    """Exact lower bound for the largest nonprincipal Fourier coefficient.

    For a subset of ``L`` distinct units in a finite abelian group of order
    ``phi``, character Parseval gives total square mass ``phi*L``.  Removing
    the principal coefficient of size ``L`` leaves the displayed average.
    """

    if phi <= 1:
        raise ValueError("phi must exceed one")
    if not 0 < unit_interval_size < phi:
        raise ValueError("unit_interval_size must lie strictly between 0 and phi")
    remaining = phi * unit_interval_size - unit_interval_size**2
    return sqrt(remaining / (phi - 1))
