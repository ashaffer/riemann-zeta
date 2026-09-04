"""Exact ledgers for the balanced joint-character/additive-product gate.

This module certifies only finite Fourier identities and exponent arithmetic.
It does not certify any imported analytic estimate or a transverse theorem.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True)
class JointCharacterLedger:
    """Power ledger in the base prime ``q`` for ``Q=q^3``."""

    h: Fraction

    @property
    def A(self) -> Fraction:
        return Fraction(2) - self.h

    @property
    def residual_exponent(self) -> Fraction:
        """Exponent of ``H=qR``."""

        return Fraction(1) + self.h

    @property
    def dual_length_exponent(self) -> Fraction:
        """Exponent of ``K=Q/H``."""

        return Fraction(2) - self.h

    @property
    def critical_box_q_exponent(self) -> Fraction:
        """Exponent of ``K R^3`` in base ``q``."""

        return Fraction(2) + 2 * self.h

    @property
    def critical_box_Q_exponent(self) -> Fraction:
        return self.critical_box_q_exponent / 3

    @property
    def entropy_deficit_q_exponent(self) -> Fraction:
        return Fraction(3) - self.critical_box_q_exponent

    @property
    def entropy_deficit_Q_exponent(self) -> Fraction:
        return self.entropy_deficit_q_exponent / 3

    @property
    def required_relative_saving_Q_exponent(self) -> Fraction:
        """Saving needed to reduce ``R^(3/2)`` to ``R^(1/2)``."""

        return self.h / 3

    @property
    def grouped_u_q_exponent(self) -> Fraction:
        """Size exponent of the product support ``u=ma``."""

        return self.dual_length_exponent + self.h

    @property
    def grouped_v_q_exponent(self) -> Fraction:
        """Size exponent of the product support ``v=bc``."""

        return 2 * self.h


def dft_indicator(modulus: int, residues: Iterable[int], n: int) -> complex:
    """Recover an indicator by the exact finite additive DFT."""

    residue_set = {r % modulus for r in residues}
    total = 0j
    for m in range(modulus):
        ihat = sum(
            cmath.exp(-2j * math.pi * m * r / modulus) for r in residue_set
        )
        total += ihat * cmath.exp(2j * math.pi * m * n / modulus)
    return total / modulus


def _prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


def primitive_root_prime_cube(prime: int) -> int:
    """Find a primitive root modulo an odd prime cube (small-test utility)."""

    if prime < 3:
        raise ValueError("prime must be odd")
    modulus = prime**3
    phi = prime**2 * (prime - 1)
    for candidate in range(2, modulus):
        if math.gcd(candidate, modulus) != 1:
            continue
        if all(
            pow(candidate, phi // factor, modulus) != 1
            for factor in _prime_factors(phi)
        ):
            return candidate
    raise RuntimeError("no primitive root found")


def primitive_character_projection(
    prime: int, residues: Iterable[int], n: int
) -> complex:
    """Compute ``phi(Q)^-1 sum_primitive conjugate(D) chi(n)``.

    For a cyclic parametrization ``chi_k(g)=exp(2*pi*i*k/phi(Q))``, a
    character modulo ``p^3`` is primitive exactly when ``p`` does not divide
    ``k``.
    """

    modulus = prime**3
    phi = prime**2 * (prime - 1)
    generator = primitive_root_prime_cube(prime)
    discrete_log: dict[int, int] = {}
    value = 1
    for exponent in range(phi):
        discrete_log[value] = exponent
        value = value * generator % modulus

    residue_set = {r % modulus for r in residues}

    def character(index: int, value_: int) -> complex:
        value_ %= modulus
        if value_ % prime == 0:
            return 0j
        exponent = discrete_log[value_]
        return cmath.exp(2j * math.pi * index * exponent / phi)

    total = 0j
    for index in range(phi):
        if index % prime == 0:
            continue
        d_value = sum(character(index, r) for r in residue_set)
        total += d_value.conjugate() * character(index, n)
    return total / phi


def unit_frequency_projection(
    prime: int, residues: Iterable[int], n: int
) -> complex:
    """Compute the unit-frequency part of additive Fourier inversion."""

    modulus = prime**3
    residue_set = {r % modulus for r in residues}
    total = 0j
    for m in range(modulus):
        if m % prime == 0:
            continue
        ihat = sum(
            cmath.exp(-2j * math.pi * m * r / modulus) for r in residue_set
        )
        total += ihat * cmath.exp(2j * math.pi * m * n / modulus)
    return total / modulus


ACTIVE_LEDGER = JointCharacterLedger(Fraction(16, 33))

