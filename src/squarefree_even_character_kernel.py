#!/usr/bin/env python3
"""Exact primitive-even character kernels for odd squarefree moduli.

This module proves no reciprocity theorem and no zero-free region. It isolates
the character-orthogonality algebra that a general-squarefree extension of the
prime-twist reciprocity formula would have to use.
"""

from __future__ import annotations

import cmath
import itertools
import math
from fractions import Fraction

from prime_reciprocity_sieve_kernel import primitive_root, primes_up_to


def odd_squarefree_prime_factors(modulus: int) -> tuple[int, ...]:
    """Return prime factors, rejecting nonpositive, even, or nonsquarefree input."""

    if (
        not isinstance(modulus, int)
        or isinstance(modulus, bool)
        or modulus < 1
        or modulus % 2 == 0
    ):
        raise ValueError("modulus must be a positive odd squarefree integer")
    if modulus == 1:
        return ()
    remaining = modulus
    factors: list[int] = []
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            factors.append(p)
            remaining //= p
            if remaining % p == 0:
                raise ValueError("modulus must be squarefree")
        p += 2
    if remaining > 1:
        factors.append(remaining)
    product = math.prod(factors)
    if product != modulus:
        raise ValueError("modulus must be squarefree")
    return tuple(factors)


def squarefree_phi(modulus: int) -> int:
    factors = odd_squarefree_prime_factors(modulus)
    return math.prod(p - 1 for p in factors)


def squarefree_mobius(modulus: int) -> int:
    factors = odd_squarefree_prime_factors(modulus)
    return -1 if len(factors) % 2 else 1


def primitive_character_sum(modulus: int, value: int) -> int:
    r"""Return ``sum_{chi primitive mod q} chi(value)`` for squarefree odd q.

    Characters are extended by zero to nonunits. For squarefree q the sum
    factors into the local nonprincipal-character sums.
    """

    factors = odd_squarefree_prime_factors(modulus)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError("value must be an integer")
    if math.gcd(value, modulus) != 1:
        return 0
    answer = 1
    for p in factors:
        answer *= (p - 1) * int(value % p == 1) - 1
    return answer


def primitive_even_character_sum(modulus: int, value: int) -> Fraction:
    r"""Return ``sum_{chi primitive, chi(-1)=1} chi(value)`` exactly."""

    return Fraction(
        primitive_character_sum(modulus, value)
        + primitive_character_sum(modulus, -value),
        2,
    )


def normalized_primitive_even_character_sum(
    modulus: int, value: int
) -> Fraction:
    """Normalize the primitive-even sum by ``phi(modulus)``."""

    return primitive_even_character_sum(modulus, value) / squarefree_phi(modulus)


def mobius_weighted_even_kernel(modulus: int, value: int) -> Fraction:
    r"""Return ``mu(q)/phi(q) * sum_{chi primitive even} chi(value)``."""

    return (
        squarefree_mobius(modulus)
        * primitive_even_character_sum(modulus, value)
        / squarefree_phi(modulus)
    )


def local_product_even_kernel(modulus: int, value: int) -> Fraction:
    r"""Equivalent two-branch local product formula.

    For units ``a`` modulo ``q`` this is

      1/2 prod_{p|q} [1/(p-1)-1_(a=1 mod p)]
    + 1/2 prod_{p|q} [1/(p-1)-1_(a=-1 mod p)].
    """

    factors = odd_squarefree_prime_factors(modulus)
    if math.gcd(value, modulus) != 1:
        return Fraction(0)
    plus = Fraction(1)
    minus = Fraction(1)
    for p in factors:
        plus *= Fraction(1, p - 1) - int(value % p == 1)
        minus *= Fraction(1, p - 1) - int(value % p == p - 1)
    return (plus + minus) / 2


def explicit_primitive_even_character_sum(modulus: int, value: int) -> complex:
    """Directly enumerate local primitive-character tuples for tests."""

    factors = odd_squarefree_prime_factors(modulus)
    if math.gcd(value, modulus) != 1:
        return 0.0j
    if not factors:
        return 1.0 + 0.0j
    local_logs: list[int] = []
    for p in factors:
        generator = primitive_root(p)
        residue = value % p
        current = 1
        lookup = {}
        for exponent in range(p - 1):
            lookup[current] = exponent
            current = current * generator % p
        local_logs.append(lookup[residue])
    total = 0.0j
    local_indices = [range(1, p - 1) for p in factors]
    for indices in itertools.product(*local_indices):
        if sum(indices) % 2:
            continue
        phase = sum(
            index * exponent / (p - 1)
            for p, index, exponent in zip(factors, indices, local_logs)
        )
        total += cmath.exp(2j * math.pi * phase)
    return total


def complete_local_euler_product(
    prime_limit: int, value: int, sign: int
) -> Fraction:
    r"""Product of ``1+c_p`` for one of the two congruence branches.

    Here ``c_p=0`` if ``p|value`` and otherwise
    ``c_p=1/(p-1)-1_(value=sign mod p)``.
    """

    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or 1")
    answer = Fraction(1)
    for p in primes_up_to(prime_limit):
        if p == 2:
            continue
        if value % p == 0:
            continue
        indicator = int(value % p == sign % p)
        answer *= 1 + Fraction(1, p - 1) - indicator
    return answer


def radical_factorized_euler_product(
    prime_limit: int, value: int, sign: int
) -> Fraction:
    r"""Equivalent base Mertens product times reciprocal radical suppression."""

    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or 1")
    base = Fraction(1)
    suppression = Fraction(1)
    for p in primes_up_to(prime_limit):
        if p == 2 or value % p == 0:
            continue
        base *= Fraction(p, p - 1)
        if (value - sign) % p == 0:
            suppression /= p
    return base * suppression


def truncated_squarefree_kernel_sum(
    modulus_limit: int, value: int
) -> Fraction:
    """Sum the Mobius-weighted even kernel over odd squarefree moduli <= Q."""

    if (
        not isinstance(modulus_limit, int)
        or isinstance(modulus_limit, bool)
        or modulus_limit < 1
    ):
        raise ValueError("modulus_limit must be a positive integer")
    answer = Fraction(0)
    for modulus in range(1, modulus_limit + 1, 2):
        try:
            odd_squarefree_prime_factors(modulus)
        except ValueError:
            continue
        answer += mobius_weighted_even_kernel(modulus, value)
    return answer
