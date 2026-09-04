"""Exact projective-norm barrier for a scalar tagged-trace attack.

The fixed-anchor Bezout token change is a bijection on the centre and
endpoint lattices.  It therefore relabels, but does not lower the rank or
the singular values of, the selected incidence matrix.

This module records a sharp finite witness for the remaining scalarization
problem.  For a prime ``p == 3 (mod 4)``, the Paley difference mask

    W[i,j] = 1_{i-j is a nonzero square modulo p}

has constant column degree ``(p-1)/2`` and zero-tag factorial mass of the
target order.  Nevertheless its nuclear/projective norm is larger than its
Hilbert--Schmidt norm by order ``sqrt(p)``.  When ``p`` is the effective
``sqrt(D)`` token length, this is exactly a ``D**(1/4)`` scalar rank cost.

The same mask can be placed on a literal all-integer four-hard-window
principal chart by selecting row witnesses according to ``i-j mod p``.
That fixture is deliberately *not* an actual-prime-power counterexample:
it shows that the Bezout identities and all four product inequalities alone
do not make scalar Blomer--Pascadi tensorization lossless.  Any positive use
of primality has to enter before the joint row mask is scalarized.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt, sqrt


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _balanced_degree(q: int) -> int:
    """Return ``floor(q**(16/33))`` by exact integer comparisons."""

    target = q**16
    lower, upper = 0, 1
    while upper**33 <= target:
        upper *= 2
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if middle**33 <= target:
            lower = middle
        else:
            upper = middle
    return lower


def _critical_even_q(minimum_degree: int) -> int:
    """Return an even ``q`` whose exact balanced degree is at least the input."""

    lower, upper = 2, 2
    while upper**16 < minimum_degree**33:
        upper *= 2
    while lower + 2 < upper:
        middle = ((lower + upper) // 4) * 2
        if middle <= lower:
            middle = lower + 2
        if middle**16 >= minimum_degree**33:
            upper = middle
        else:
            lower = middle
    q = upper if upper % 2 == 0 else upper + 1
    while q**16 < minimum_degree**33:
        q += 2
    return q


def legendre_symbol(value: int, prime: int) -> int:
    """Return the Legendre symbol, with a checked odd-prime modulus."""

    if not _is_prime(prime) or prime == 2:
        raise ValueError("the modulus must be an odd prime")
    residue = value % prime
    if residue == 0:
        return 0
    power = pow(residue, (prime - 1) // 2, prime)
    return 1 if power == 1 else -1


def paley_difference_mask(prime: int) -> tuple[tuple[int, ...], ...]:
    """Return ``1_{chi(i-j)=1}`` on ``F_p x F_p``."""

    if prime % 4 != 3 or not _is_prime(prime):
        raise ValueError("require a prime congruent to 3 modulo 4")
    return tuple(
        tuple(int(legendre_symbol(i - j, prime) == 1) for j in range(prime))
        for i in range(prime)
    )


@dataclass(frozen=True)
class PaleyTaggedTraceLedger:
    prime: int
    column_degree: int
    entries: int
    zero_tag_factorial_mass: int
    rank: int
    frobenius_squared: int
    exceptional_singular_value: float
    repeated_singular_value: float
    nuclear_norm: float
    projective_to_hilbert_schmidt_ratio: float
    rigorous_ratio_lower_bound: float


def paley_tagged_trace_ledger(prime: int) -> PaleyTaggedTraceLedger:
    """Return the exact Paley degree, factorial, and singular-value ledger.

    For ``p == 3 (mod 4)``, the nontrivial Fourier eigenvalues of the
    quadratic-residue circulant all have modulus ``sqrt(p+1)/2``.  Hence the
    displayed nuclear norm is exact, not a numerical SVD estimate.
    """

    if prime % 4 != 3 or not _is_prime(prime):
        raise ValueError("require a prime congruent to 3 modulo 4")
    degree = (prime - 1) // 2
    entries = prime * degree
    factorial = prime * degree * (degree - 1)
    exceptional = float(degree)
    repeated = sqrt(prime + 1) / 2
    nuclear = exceptional + (prime - 1) * repeated
    frobenius = sqrt(entries)
    # Dropping the exceptional singular value gives the exact inequality
    # ratio^2 >= (p^2-1)/(2p) > (p-1)/2.
    lower = sqrt((prime * prime - 1) / (2 * prime))
    return PaleyTaggedTraceLedger(
        prime=prime,
        column_degree=degree,
        entries=entries,
        zero_tag_factorial_mass=factorial,
        rank=prime,
        frobenius_squared=entries,
        exceptional_singular_value=exceptional,
        repeated_singular_value=repeated,
        nuclear_norm=nuclear,
        projective_to_hilbert_schmidt_ratio=nuclear / frobenius,
        rigorous_ratio_lower_bound=lower,
    )


@dataclass(frozen=True)
class PrincipalPaleyEdge:
    row_index: int
    endpoint_index: int
    anchor: tuple[int, int]
    center: tuple[int, int]
    endpoint: tuple[int, int]
    base_row: int
    next_row: int
    residuals: tuple[int, int, int, int]


@dataclass(frozen=True)
class PrincipalPaleyFixture:
    prime: int
    q: int
    D: int
    middle: int
    edges: tuple[PrincipalPaleyEdge, ...]
    distinct_bands: bool


def principal_paley_hard_window_fixture(prime: int) -> PrincipalPaleyFixture:
    """Embed the Paley mask in four literal all-integer hard windows.

    The offsets occupy six disjoint bands:

    ``gamma ~ 0``, centres ``~-10p``, base rows ``~10p``, next rows
    ``~-20p``, and endpoints ``~30p``.  Every triple has offset sum zero,
    so its cubic residual is only quadratic in the offsets.  Taking
    a critical balanced degree at least ``20000*p^2`` gives a generous exact
    hard-window margin.  The returned parameters obey the literal project
    relation ``D=floor(q^(16/33))`` as well as ``D^2<q``.

    Rows are selected by a quadratic-residue mask.  They are ordinary
    integers, not asserted to be prime powers.
    """

    mask = paley_difference_mask(prime)
    q = _critical_even_q(20_000 * prime * prime)
    D = _balanced_degree(q)
    middle = q // 2
    anchor = (middle, middle + 1)
    answer: list[PrincipalPaleyEdge] = []
    all_distinct = True
    for i in range(prime):
        A = 10 * prime + i
        center = (middle - A, middle - A - 1)
        base_row = middle + A
        for j in range(prime):
            if not mask[i][j]:
                continue
            s = 30 * prime + j
            endpoint = (middle + s, middle + s + 1)
            next_row = middle + A - s
            triples = (
                (base_row, center[0], anchor[0]),
                (base_row, center[1], anchor[1]),
                (next_row, center[0], endpoint[0]),
                (next_row, center[1], endpoint[1]),
            )
            residuals = tuple(8 * a * b * c - q**3 for a, b, c in triples)
            if any(abs(residual) > q * D for residual in residuals):
                raise AssertionError("a Paley edge left the hard window")
            coordinates = (
                *anchor,
                *center,
                *endpoint,
                base_row,
                next_row,
            )
            all_distinct &= len(set(coordinates)) == len(coordinates)
            answer.append(
                PrincipalPaleyEdge(
                    row_index=i,
                    endpoint_index=j,
                    anchor=anchor,
                    center=center,
                    endpoint=endpoint,
                    base_row=base_row,
                    next_row=next_row,
                    residuals=(
                        residuals[0], residuals[1], residuals[2], residuals[3]
                    ),
                )
            )
    return PrincipalPaleyFixture(
        prime=prime,
        q=q,
        D=D,
        middle=middle,
        edges=tuple(answer),
        distinct_bands=all_distinct,
    )
