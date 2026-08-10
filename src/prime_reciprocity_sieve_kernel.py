#!/usr/bin/env python3
"""Finite prime-twist reciprocity and centered progression ledger.

This module proves no zero-free region. It records two exact algebraic facts
behind the prime-twist stress model for the long-mollifier reciprocity route.

1. After Khan's prime-twist dual prefactor is multiplied by the two mollifier
   coefficients, the q-variable is exactly a one-sided character mollifier.
2. Normalized primitive-even character orthogonality modulo an odd prime p is

       1/(p-1) sum_{chi primitive even mod p} chi(a)
       = 1/2 * 1_(a == +/-1 mod p) - 1/(p-1)

   when p does not divide a, and is zero otherwise.

Thus summing the dual character family first produces a centered pair of
residue classes, not an uncentered positive sector.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Mapping, Sequence


def _require_odd_prime(p: int) -> None:
    if not isinstance(p, int) or isinstance(p, bool) or p < 3:
        raise ValueError("p must be an odd prime")
    divisor = 2
    while divisor * divisor <= p:
        if p % divisor == 0:
            raise ValueError("p must be an odd prime")
        divisor += 1


def primes_up_to(limit: int) -> tuple[int, ...]:
    """Return all primes at most ``limit``."""

    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    if limit < 2:
        return ()
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return tuple(index for index in range(2, limit + 1) if sieve[index])


def logarithmic_taper(scale: float, n: int) -> float:
    """Return ``1_(n<=y) log(y/n)/log(y)``."""

    if not math.isfinite(scale) or scale <= 1.0:
        raise ValueError("scale must be finite and greater than one")
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    if n > scale:
        return 0.0
    return math.log(scale / n) / math.log(scale)


def normalized_primitive_even_character_sum(p: int, a: int) -> Fraction:
    r"""Return the exact normalized primitive-even character sum.

    For an odd prime ``p``, every nonprincipal character modulo ``p`` is
    primitive. Characters are extended by zero to multiples of ``p``.
    """

    _require_odd_prime(p)
    if not isinstance(a, int) or isinstance(a, bool):
        raise ValueError("a must be an integer")
    residue = a % p
    if residue == 0:
        return Fraction(0)
    hits = int(residue == 1) + int(residue == p - 1)
    return Fraction(hits, 2) - Fraction(1, p - 1)


def centered_progression_average(
    p: int, multiplier: int, coefficients: Mapping[int, Fraction]
) -> Fraction:
    r"""Evaluate the character-orthogonality side after summing the index.

    This equals

      1/2 sum_{multiplier*n == +/-1 mod p} a_n
        - 1/(p-1) sum_{p not divide multiplier*n} a_n.
    """

    _require_odd_prime(p)
    if not isinstance(multiplier, int) or isinstance(multiplier, bool):
        raise ValueError("multiplier must be an integer")
    total = Fraction(0)
    for n, coefficient in coefficients.items():
        if not isinstance(n, int) or isinstance(n, bool) or n < 1:
            raise ValueError("coefficient indices must be positive integers")
        if not isinstance(coefficient, Fraction):
            raise TypeError("coefficients must be Fraction values")
        total += coefficient * normalized_primitive_even_character_sum(
            p, multiplier * n
        )
    return total


def primitive_root(p: int) -> int:
    """Return the least primitive root modulo an odd prime."""

    _require_odd_prime(p)
    phi = p - 1
    factors = []
    remaining = phi
    q = 2
    while q * q <= remaining:
        if remaining % q == 0:
            factors.append(q)
            while remaining % q == 0:
                remaining //= q
        q += 1
    if remaining > 1:
        factors.append(remaining)
    for candidate in range(2, p):
        if all(pow(candidate, phi // factor, p) != 1 for factor in factors):
            return candidate
    raise RuntimeError("failed to find a primitive root")


def explicit_primitive_even_character_sum(p: int, a: int) -> complex:
    """Directly enumerate primitive even characters for regression tests."""

    _require_odd_prime(p)
    residue = a % p
    if residue == 0:
        return 0.0j
    generator = primitive_root(p)
    discrete_log = {}
    value = 1
    for exponent in range(p - 1):
        discrete_log[value] = exponent
        value = value * generator % p
    exponent_a = discrete_log[residue]
    total = 0.0j
    # Character index k is even exactly when chi_k(-1)=1. Exclude k=0.
    for k in range(2, p - 1, 2):
        total += cmath.exp(2j * math.pi * k * exponent_a / (p - 1))
    return total


def prime_dual_coefficient_direct(
    p: int,
    q: int,
    scale: float,
    height_parameter: float,
    dual_frequency: float,
    character_value: complex,
) -> complex:
    r"""Coefficient before factorization in the prime-twist dual term.

    It includes the two prime mollifier coefficients, Khan's
    ``sqrt(p)/(p-1)`` factor, and ``(T/(2q))**(it)``.
    """

    _require_odd_prime(p)
    _require_odd_prime(q)
    if p == q:
        raise ValueError("p and q must be distinct")
    if not math.isfinite(height_parameter) or height_parameter <= 0.0:
        raise ValueError("height_parameter must be finite and positive")
    if not math.isfinite(dual_frequency):
        raise ValueError("dual_frequency must be finite")
    wp = logarithmic_taper(scale, p)
    wq = logarithmic_taper(scale, q)
    mollifier_product = wp * wq / math.sqrt(p * q)
    dual_prefactor = math.sqrt(p) / (p - 1)
    phase = cmath.exp(
        1j * dual_frequency * math.log(height_parameter / (2.0 * q))
    )
    # mu(p)mu(q)=1 for distinct primes.
    return mollifier_product * dual_prefactor * character_value * phase


def prime_dual_coefficient_factorized(
    p: int,
    q: int,
    scale: float,
    height_parameter: float,
    dual_frequency: float,
    character_value: complex,
) -> complex:
    r"""Same coefficient as an outer modulus weight times character mollifier.

    The factorization is

      [-w(p)/(p-1)] * [-w(q) chi(q) q^(-1/2-it)]
        * (T/2)^(it).
    """

    _require_odd_prime(p)
    _require_odd_prime(q)
    if p == q:
        raise ValueError("p and q must be distinct")
    if not math.isfinite(height_parameter) or height_parameter <= 0.0:
        raise ValueError("height_parameter must be finite and positive")
    if not math.isfinite(dual_frequency):
        raise ValueError("dual_frequency must be finite")
    wp = logarithmic_taper(scale, p)
    wq = logarithmic_taper(scale, q)
    outer = -wp / (p - 1)
    inner = -wq * character_value / math.sqrt(q) * cmath.exp(
        -1j * dual_frequency * math.log(q)
    )
    common_phase = cmath.exp(
        1j * dual_frequency * math.log(height_parameter / 2.0)
    )
    return outer * inner * common_phase


def weighted_error_majorant_identity(
    primes: Sequence[int], weights: Mapping[int, Fraction]
) -> tuple[Fraction, Fraction]:
    r"""Return direct and factorized prime-pair error majorants.

    After multiplying Khan's schematic error
    ``sqrt(q/p)+sqrt(p/q)`` by ``1/sqrt(pq)``, the pair weight is
    ``1/p+1/q``. Hence

      sum_{p,q} w_p w_q (1/p+1/q)
      = 2 (sum_p w_p)(sum_p w_p/p).
    """

    for p in primes:
        _require_odd_prime(p)
        if p not in weights:
            raise ValueError("every prime must have a weight")
    direct = Fraction(0)
    for p in primes:
        for q in primes:
            direct += weights[p] * weights[q] * (
                Fraction(1, p) + Fraction(1, q)
            )
    factorized = 2 * sum((weights[p] for p in primes), Fraction(0)) * sum(
        (weights[p] / p for p in primes), Fraction(0)
    )
    return direct, factorized
