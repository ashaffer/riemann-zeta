"""Exact valuation algebra for lcm/factorial ramp certificates.

Finite searches in this module are identity discovery tools.  The exact
Möbius inversion shows that signed factorial ratios can realize any finite
prime-power layer profile; it does not estimate the von Mangoldt ramp.
"""

from __future__ import annotations

import math
from collections.abc import Sequence


def mobius_sieve(limit: int) -> list[int]:
    """Return mu(0),...,mu(limit) by a linear sieve."""

    if limit < 1:
        raise ValueError("limit must be positive")
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for prime in primes:
            if n * prime > limit:
                break
            composite[n * prime] = True
            if n % prime == 0:
                mu[n * prime] = 0
                break
            mu[n * prime] = -mu[n]
    return mu


def primes_up_to(limit: int) -> list[int]:
    """Return all primes at most ``limit``."""

    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def prime_powers(prime: int, limit: int) -> list[int]:
    """Return prime, prime**2, ... through ``limit``."""

    if prime < 2 or limit < 1:
        raise ValueError("prime and limit must be positive with prime >= 2")
    output: list[int] = []
    power = prime
    while power <= limit:
        output.append(power)
        if power > limit // prime:
            break
        power *= prime
    return output


def lcm_ratio_layer(N: int, prime_power: int) -> int:
    """The layer 2q-N in v_p(Q_N) belonging to q=p**k."""

    if not 1 <= prime_power <= N:
        raise ValueError("prime_power must lie in [1,N]")
    return 2 * prime_power - N


def lcm_ratio_valuation(N: int, prime: int) -> int:
    """Exact v_p(Q_N), Q_N=L_N**N/prod_{m<N} L_m**2."""

    return sum(lcm_ratio_layer(N, power) for power in prime_powers(prime, N))


def factorial_valuation(n: int, prime: int) -> int:
    """Legendre's formula for v_p(n!)."""

    total = 0
    power = prime
    while power <= n:
        total += n // power
        if power > n // prime:
            break
        power *= prime
    return total


def canonical_certificate_layer(N: int, prime_power: int) -> int:
    """Prime-power layer in the canonical factorial/lcm integer.

    For N=a*q+r this equals (a-1)(2q-r), and is nonnegative.
    """

    if not 1 <= prime_power <= N:
        raise ValueError("prime_power must lie in [1,N]")
    quotient, remainder = divmod(N, prime_power)
    return (quotient - 1) * (2 * prime_power - remainder)


def canonical_certificate_valuation(N: int, prime: int) -> int:
    """Valuation of

    ((N!/L_N)**N) / prod_{m<N} ((m!/L_m)**2).
    """

    return sum(
        canonical_certificate_layer(N, power)
        for power in prime_powers(prime, N)
    )


def factorial_layer_profile(exponents: Sequence[int]) -> list[int]:
    """Return W(q)=sum_d c_d floor(d/q) for a factorial ratio.

    ``exponents[d]`` is the exponent of d!, and index zero is ignored.
    """

    N = len(exponents) - 1
    if N < 1:
        raise ValueError("exponents must have indices 0,...,N with N>=1")
    return [0] + [
        sum(exponents[d] * (d // q) for d in range(q, N + 1))
        for q in range(1, N + 1)
    ]


def mobius_inverted_factorial_exponents(
    layer_profile: Sequence[int],
) -> tuple[list[int], list[int]]:
    """Invert the factorial layer transform over the integers.

    If h(q) is ``layer_profile[q]``, set

        C(d)=sum_{m<=N/d} mu(m) h(md),
        c(d)=C(d)-C(d+1).

    Then sum_d c(d) floor(d/q)=h(q) for every q.  The returned pair is
    ``(c,C)`` with sentinel index N+1 included in C.
    """

    N = len(layer_profile) - 1
    if N < 1:
        raise ValueError("layer_profile must have indices 0,...,N with N>=1")
    mu = mobius_sieve(N)
    cumulative = [0] * (N + 2)
    for d in range(1, N + 1):
        cumulative[d] = sum(
            mu[m] * layer_profile[m * d] for m in range(1, N // d + 1)
        )
    exponents = [0] * (N + 1)
    for d in range(1, N + 1):
        exponents[d] = cumulative[d] - cumulative[d + 1]
    return exponents, cumulative


def truncated_inverse_profile(N: int, cutoff: int) -> list[int]:
    """The layer profile (N-2q) 1_{q>cutoff}."""

    if not 1 <= cutoff < N:
        raise ValueError("cutoff must lie in [1,N)")
    return [0] + [N - 2 * q if q > cutoff else 0 for q in range(1, N + 1)]


def truncated_residual_valuation(N: int, cutoff: int, prime: int) -> int:
    """v_p((Q_N P_{N,cutoff})^{-1}); nonnegative if cutoff<N/2."""

    return sum(
        N - 2 * power
        for power in prime_powers(prime, min(N, cutoff))
    )


def factorial_ratio_log(exponents: Sequence[int]) -> float:
    """Floating evaluation of log prod_d (d!)**c_d for diagnostics."""

    return sum(
        exponent * math.lgamma(d + 1)
        for d, exponent in enumerate(exponents)
        if d >= 1 and exponent
    )


def layer_profile_log(layer_profile: Sequence[int]) -> float:
    """Evaluate sum_q h(q)Lambda(q) directly from prime powers."""

    N = len(layer_profile) - 1
    total = 0.0
    for prime in primes_up_to(N):
        logarithm = math.log(prime)
        total += sum(layer_profile[q] * logarithm for q in prime_powers(prime, N))
    return total


def direct_integer_multiplier_valuation(
    N: int, prime: int, *, reciprocal: bool = False
) -> int:
    """Minimal v_p of an integer multiplying Q_N (or 1/Q_N) to integrality."""

    valuation = lcm_ratio_valuation(N, prime)
    return max(valuation if reciprocal else -valuation, 0)


def divisibility_non_tu_minor() -> tuple[tuple[int, ...], ...]:
    """A determinant -2 minor of the divisibility incidence matrix.

    Rows are divisors (2,3,5), columns are integers (6,10,15).
    """

    rows = (2, 3, 5)
    columns = (6, 10, 15)
    return tuple(tuple(int(column % row == 0) for column in columns) for row in rows)


def determinant_3_by_3(matrix: Sequence[Sequence[int]]) -> int:
    """Exact determinant of a 3 by 3 integer matrix."""

    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("matrix must be 3 by 3")
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )
