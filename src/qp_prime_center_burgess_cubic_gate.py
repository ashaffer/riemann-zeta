"""Exact ledgers and finite checks for the prime-center Burgess cubic gate."""

from __future__ import annotations

import cmath
from dataclasses import dataclass
from fractions import Fraction
from math import sqrt
from typing import Iterable


@dataclass(frozen=True)
class PrimeCenterBurgessLedger:
    """Power ledger for the one-sided prime-center signed cubic theorem."""

    aperture: Fraction

    def __post_init__(self) -> None:
        if not Fraction(3, 2) < self.aperture < Fraction(2):
            raise ValueError("require 3/2 < aperture < 2")

    @property
    def residual_exponent(self) -> Fraction:
        return Fraction(2) - self.aperture

    @property
    def old_skew_exponent(self) -> Fraction:
        return self.residual_exponent / 2

    @property
    def burgess_character_exponent(self) -> Fraction:
        """Exponent in ``S_R << R**(1/2) q**(3/16+eps)``."""

        return self.residual_exponent / 2 + Fraction(3, 16)

    @property
    def burgess_skew_exponent(self) -> Fraction:
        return self.burgess_character_exponent / 2

    @property
    def burgess_transverse_exponent(self) -> Fraction:
        return Fraction(1, 2) + self.burgess_skew_exponent

    @property
    def burgess_saving(self) -> Fraction:
        return (
            Fraction(1, 2) + self.old_skew_exponent
            - self.burgess_transverse_exponent
        )

    @property
    def density_one_skew_exponent(self) -> Fraction:
        return self.residual_exponent / 4 + Fraction(1, 16)

    @property
    def density_one_transverse_exponent(self) -> Fraction:
        return Fraction(1, 2) + self.density_one_skew_exponent


def active_ledger() -> PrimeCenterBurgessLedger:
    return PrimeCenterBurgessLedger(Fraction(50, 33))


def restricted_weak_constant(
    residual_length: float, modulus: float, character_maximum: float
) -> float:
    """The proved set-incidence constant ``R/sqrt(q)+sqrt(S_R)``."""

    if residual_length <= 0.0:
        raise ValueError("residual_length must be positive")
    if modulus <= 0.0:
        raise ValueError("modulus must be positive")
    if character_maximum < 0.0:
        raise ValueError("character_maximum must be nonnegative")
    return residual_length / sqrt(modulus) + sqrt(character_maximum)


def cubic_endpoint_ratio(gamma: float) -> float:
    """Sharp lower bound for ``ess sup(Z)/sqrt(E Z**2)``.

    Here ``Z`` is real and mean zero and ``gamma=E Z**3/(E Z**2)**(3/2)``.
    """

    return (gamma + sqrt(gamma * gamma + 4.0)) / 2.0


def normalized_incidence_bounds(
    a_size: int,
    b_size: int,
    c_size: int,
    residual_length: float,
    modulus: float,
    character_maximum: float,
) -> tuple[float, float]:
    """Principal and nonprincipal interpolation bounds.

    The caller may interchange A and B first.  The returned quantities are
    the two terms after division by ``sqrt(|A||B||C|)``.
    """

    if min(a_size, b_size, c_size) <= 0:
        raise ValueError("set sizes must be positive")
    if a_size > b_size:
        a_size, b_size = b_size, a_size
    normalizer = sqrt(a_size * b_size * c_size)
    principal_character = residual_length * a_size * b_size / modulus
    fixed_c_fibre = residual_length * c_size
    nonprincipal_character = character_maximum * sqrt(a_size * b_size)
    pair_codegree = a_size * c_size
    principal = min(principal_character, fixed_c_fibre) / normalizer
    nonprincipal = min(nonprincipal_character, pair_codegree) / normalizer
    return principal, nonprincipal


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1
    return True


def primitive_root(prime: int) -> int:
    """Return the least primitive root modulo a small prime."""

    if not is_prime(prime):
        raise ValueError("modulus must be prime")
    phi = prime - 1
    factors: set[int] = set()
    value = phi
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.add(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    for candidate in range(2, prime):
        if all(pow(candidate, phi // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("a prime modulus must have a primitive root")


def multiplicative_character_spectrum(
    residues: Iterable[int], prime: int
) -> tuple[complex, ...]:
    """Unnormalised character sums over nonzero residues modulo ``prime``."""

    generator = primitive_root(prime)
    discrete_log: dict[int, int] = {}
    value = 1
    for exponent in range(prime - 1):
        discrete_log[value] = exponent
        value = value * generator % prime
    logs = [discrete_log[residue % prime] for residue in residues if residue % prime]
    return tuple(
        sum(
            cmath.exp(2j * cmath.pi * character * exponent / (prime - 1))
            for exponent in logs
        )
        for character in range(prime - 1)
    )


def product_residue_count(
    first: Iterable[int], second: Iterable[int], residues: Iterable[int], prime: int
) -> int:
    residue_set = {value % prime for value in residues}
    return sum(
        1
        for left in first
        for right in second
        if (left * right) % prime in residue_set
    )
