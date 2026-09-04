"""Finite identities behind the primitive-conductor q^3 carry block.

The accompanying report contains the analytic argument.  This module keeps
the additive-fibre projection, the aligned-window Fourier factorisation,
the depth-two p-adic logarithm, and the active exponent ledger executable.
It does not claim the missing Schatten restriction estimate.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


def additive_character(modulus: int, value: int) -> complex:
    return cmath.exp(2j * math.pi * (value % modulus) / modulus)


def symmetric_aligned_unit_window(prime: int, blocks: int) -> set[int]:
    """Return ``{0 < |r| <= p*J, p does not divide r}`` modulo ``p^3``."""

    if prime <= 2 or blocks <= 0 or blocks >= prime:
        raise ValueError("require an odd prime scale and 0 < blocks < prime")
    modulus = prime**3
    positive = {
        prime * v + u
        for v in range(blocks)
        for u in range(1, prime)
    }
    return positive | {(-value) % modulus for value in positive}


def additive_fourier_coefficient(
    modulus: int, residues: Iterable[int], frequency: int
) -> complex:
    residue_set = {value % modulus for value in residues}
    return sum(
        additive_character(modulus, -frequency * value)
        for value in residue_set
    )


def factored_aligned_window_coefficient(
    prime: int, blocks: int, frequency: int
) -> complex:
    """Factor the Fourier coefficient into two Dirichlet kernels.

    On the positive half write ``r=p*v+u`` with ``0<=v<J`` and
    ``1<=u<p``.  The symmetric coefficient is twice the real part of the
    product of the ``u`` and ``v`` sums.
    """

    modulus = prime**3
    unit_sum = sum(
        additive_character(modulus, -frequency * u)
        for u in range(1, prime)
    )
    block_sum = sum(
        additive_character(prime**2, -frequency * v)
        for v in range(blocks)
    )
    return 2.0 * (unit_sum * block_sum).real + 0j


def additive_fibre_average(
    prime: int, values: dict[int, complex], residue: int
) -> complex:
    """Average a function modulo ``p^3`` over its additive ``p^2`` fibre."""

    modulus = prime**3
    residue %= modulus
    return sum(
        values.get((residue + k * prime**2) % modulus, 0j)
        for k in range(prime)
    ) / prime


def primitive_kernel_by_fibres(
    prime: int, residues: Iterable[int], value: int
) -> complex:
    """Evaluate ``(I-E_{p^2}) 1_R`` at one residue.

    On units this is exactly projection onto multiplicative characters of
    conductor ``p^3``.  The equality follows because multiplication by
    ``1+p^2*t`` permutes the additive fibre modulo ``p^2``.
    """

    modulus = prime**3
    indicator = {residue % modulus: 1.0 + 0j for residue in residues}
    value %= modulus
    return indicator.get(value, 0j) - additive_fibre_average(
        prime, indicator, value
    )


def primitive_kernel_by_unit_frequencies(
    prime: int, residues: Iterable[int], value: int
) -> complex:
    """Evaluate the same projection using only additive unit frequencies."""

    modulus = prime**3
    residue_set = {residue % modulus for residue in residues}
    total = 0j
    for frequency in range(modulus):
        if frequency % prime == 0:
            continue
        coefficient = additive_fourier_coefficient(
            modulus, residue_set, frequency
        )
        total += coefficient * additive_character(
            modulus, frequency * value
        )
    return total / modulus


def teichmuller_lift(prime: int, value: int) -> int:
    """Return the Teichmueller lift of a unit modulo ``p`` in ``Z/p^3``."""

    modulus = prime**3
    value %= modulus
    if value % prime == 0:
        raise ValueError("value must be a unit")
    return pow(value, prime**2, modulus)


def wild_log_coordinate(prime: int, value: int) -> int:
    """Return ``log(<value>)/p mod p^2``.

    If ``<value>=1+p*x``, the truncated logarithm is
    ``x-p*x^2/2 (mod p^2)``.  This identifies the wild unit group
    ``(1+p Z)/(1+p^3 Z)`` with the additive group modulo ``p^2``.
    """

    modulus = prime**3
    value %= modulus
    if value % prime == 0:
        raise ValueError("value must be a unit")
    omega = teichmuller_lift(prime, value)
    principal = value * pow(omega, -1, modulus) % modulus
    if (principal - 1) % prime:
        raise AssertionError("Teichmueller quotient is not a principal unit")
    x = ((principal - 1) // prime) % (prime**2)
    inverse_two = pow(2, -1, prime**2)
    return (x - prime * inverse_two * x * x) % (prime**2)


def second_fermat_quotient(prime: int, value: int) -> int:
    """Return ``(value^(p-1)-1)/p mod p^2``."""

    modulus = prime**3
    value %= modulus
    if value % prime == 0:
        raise ValueError("value must be a unit")
    lifted_power = pow(value, prime - 1, modulus)
    return ((lifted_power - 1) // prime) % (prime**2)


def wild_log_from_second_fermat(prime: int, value: int) -> int:
    """Recover the wild logarithm from the second Fermat quotient."""

    quotient = second_fermat_quotient(prime, value)
    modulus = prime**2
    inverse_two = pow(2, -1, modulus)
    numerator = (quotient - prime * inverse_two * quotient * quotient) % modulus
    return numerator * pow(prime - 1, -1, modulus) % modulus


def postnikov_increment(prime: int, unit: int, lift: int) -> int:
    """Return the exact wild-log increment from ``u`` to ``u+p*v``.

    It is ``x-p*x^2/2 mod p^2`` with ``x=v/u mod p^2``.
    """

    if unit % prime == 0:
        raise ValueError("unit must be nonzero modulo p")
    modulus = prime**2
    x = lift * pow(unit, -1, modulus) % modulus
    inverse_two = pow(2, -1, modulus)
    return (x - prime * inverse_two * x * x) % modulus


@dataclass(frozen=True)
class PrimitiveQ3ExponentLedger:
    degree: Fraction
    residual_length: Fraction
    additive_unit_band_length: Fraction
    additive_fourier_height: Fraction
    normalized_flat_coefficient: Fraction
    reciprocal_resonance_count: Fraction
    reciprocal_coherent_count: Fraction
    critical_box_size: Fraction
    entropy_deficit: Fraction


def active_exponent_ledger() -> PrimitiveQ3ExponentLedger:
    """Return all exponents in base ``q`` at ``D=q^(16/33)``."""

    degree = Fraction(16, 33)
    unit_band = 2 - degree
    return PrimitiveQ3ExponentLedger(
        degree=degree,
        residual_length=1 + degree,
        additive_unit_band_length=unit_band,
        additive_fourier_height=1 + degree,
        normalized_flat_coefficient=-unit_band,
        reciprocal_resonance_count=1 - degree,
        reciprocal_coherent_count=1 - 2 * degree,
        critical_box_size=unit_band + 3 * degree,
        entropy_deficit=3 - (unit_band + 3 * degree),
    )
