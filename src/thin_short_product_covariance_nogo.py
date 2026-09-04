#!/usr/bin/env python3
"""Exact thin-fibre obstruction for block-dependent product coefficients.

The late Buchstab reduction has products ``p*r`` in a block of length H with
H < r.  Hence a fixed r occurs with at most one p in a block.  If the
one-variable coefficient beta is allowed to depend arbitrarily on the block,
it can conjugate every selected additive/logarithmic phase.  This module
checks that algebra exactly on finite prime products.

This is not a counterexample for the actual first-return coefficient beta.
It rules out only a theorem uniform over arbitrary block-dependent beta from
size or L2 norms alone.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction


KAPPA = Fraction(1_974_048_259, 100_000_000_000)
H_MIN = Fraction(8, 33)
EDGE_EXPONENT = Fraction(797, 5000)


def primes_up_to(limit: int) -> list[int]:
    """Return all primes at most ``limit`` by an elementary sieve."""

    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def voronoi_masses(points: list[int]) -> dict[int, Fraction]:
    """Return endpoint-trapezoid masses on a finite ordered node set."""

    if len(points) < 2 or points != sorted(set(points)):
        raise ValueError("points must be a strictly increasing finite set")
    masses = {point: Fraction(0) for point in points}
    for left, right in zip(points, points[1:]):
        half_gap = Fraction(right - left, 2)
        masses[left] += half_gap
        masses[right] += half_gap
    return masses


def voronoi_difference_diagonal(
    coarse_points: list[int], fine_points: list[int]
) -> tuple[Fraction, Fraction]:
    """Return exact squared energy and the max-gap/total-mass upper bound.

    The sets need only have the same endpoints.  If G is the larger maximal
    gap, then every atom of either positive measure is at most G, so

        sum |mu-nu|^2 <= 2 G (mu(R)+nu(R)).
    """

    if coarse_points[0] != fine_points[0] or coarse_points[-1] != fine_points[-1]:
        raise ValueError("the node sets must have common endpoints")
    coarse = voronoi_masses(coarse_points)
    fine = voronoi_masses(fine_points)
    keys = coarse.keys() | fine.keys()
    energy = sum((coarse.get(n, 0) - fine.get(n, 0)) ** 2 for n in keys)
    maximum_gap = max(
        max(right - left for left, right in zip(points, points[1:]))
        for points in (coarse_points, fine_points)
    )
    bound = 2 * maximum_gap * (sum(coarse.values()) + sum(fine.values()))
    return energy, bound


def prime_product_blocks(
    y: int, p_lo: int, p_hi: int, block_length: int
) -> tuple[list[list[tuple[int, int]]], bool]:
    """Partition prime products in ``[y,2y)`` into physical blocks.

    The boolean certifies the unique-large-factor property: within each
    block, no value of r occurs with two different p values.
    """

    if not (2 <= p_lo < p_hi < y and 1 <= block_length < y):
        raise ValueError("invalid product-block parameters")
    primes = primes_up_to(2 * y)
    prime_set = set(primes)
    small = [p for p in primes if p_lo <= p < p_hi]
    block_count = (y + block_length - 1) // block_length
    blocks: list[list[tuple[int, int]]] = [[] for _ in range(block_count)]
    for p in small:
        r_lo = (y + p - 1) // p
        r_hi = (2 * y - 1) // p
        for r in range(r_lo, r_hi + 1):
            if r not in prime_set:
                continue
            n = p * r
            block = (n - y) // block_length
            blocks[block].append((p, r))

    unique = True
    for pairs in blocks:
        seen: set[int] = set()
        for _, r in pairs:
            if r in seen:
                unique = False
            seen.add(r)
    return blocks, unique


@dataclass(frozen=True)
class AlignmentAudit:
    total_pairs: int
    block_count: int
    nonempty_blocks: int
    direct_energy: float
    count_energy: int
    cauchy_floor: float
    maximum_beta_modulus_error: float
    unique_large_factor: bool


def aligned_block_energy(
    blocks: list[list[tuple[int, int]]],
    y: int,
    block_length: int,
    modulus: int = 13,
    height: float = 37.0,
) -> AlignmentAudit:
    """Align every fibre with a bounded block-dependent beta coefficient.

    On block I use a primitive numerator depending on I and include both the
    rational carrier and a unit residual logarithmic chirp.  The constructed
    beta has modulus one and makes the product sum exactly its support size.
    """

    if modulus < 2:
        raise ValueError("modulus must be at least two")
    direct_energy = 0.0
    count_energy = 0
    beta_error = 0.0
    total_pairs = 0
    nonempty = 0
    for index, pairs in enumerate(blocks):
        if not pairs:
            continue
        nonempty += 1
        numerator = 1 + (index % (modulus - 1))
        while math.gcd(numerator, modulus) != 1:
            numerator = 1 + (numerator % (modulus - 1))
        value = 0j
        for p, r in pairs:
            n = p * r
            carrier = cmath.exp(2j * math.pi * numerator * n / modulus)
            residual = cmath.exp(1j * height * math.log(n / y))
            beta = (carrier * residual).conjugate()
            beta_error = max(beta_error, abs(abs(beta) - 1.0))
            value += beta * carrier * residual
        direct_energy += abs(value) ** 2
        count_energy += len(pairs) ** 2
        total_pairs += len(pairs)
    cauchy_floor = total_pairs**2 / len(blocks) if blocks else 0.0
    unique = all(len({r for _, r in pairs}) == len(pairs) for pairs in blocks)
    return AlignmentAudit(
        total_pairs=total_pairs,
        block_count=len(blocks),
        nonempty_blocks=nonempty,
        direct_energy=direct_energy,
        count_energy=count_energy,
        cauchy_floor=cauchy_floor,
        maximum_beta_modulus_error=beta_error,
        unique_large_factor=unique,
    )


def closing_eta_frontier(
    h: Fraction, kappa: Fraction = KAPPA
) -> Fraction:
    """Largest physical-L2 excess eta allowed at block exponent h."""

    return h - 4 * kappa


def adversarial_eta(h: Fraction) -> Fraction:
    """Power excess of the aligned block-dependent-beta construction."""

    return h


def diagonal_delta_frontier(
    h: Fraction = H_MIN,
    edge_exponent: Fraction = EDGE_EXPONENT,
    kappa: Fraction = KAPPA,
) -> Fraction:
    """CH4 delta if total covariance stays at the retained diagonal scale."""

    return (h - 4 * kappa - edge_exponent) / 4


def audit() -> dict[str, str | int | float | bool]:
    y = 20_000
    blocks, unique = prime_product_blocks(y, 23, 59, 100)
    result = aligned_block_energy(blocks, y, 100)
    diagonal, diagonal_bound = voronoi_difference_diagonal(
        [0, 7, 12], [0, 2, 5, 7, 9, 12]
    )
    return {
        "Y": y,
        "block_length": 100,
        "total_pairs": result.total_pairs,
        "nonempty_blocks": result.nonempty_blocks,
        "unique_large_factor": unique and result.unique_large_factor,
        "direct_minus_count_energy": result.direct_energy
        - result.count_energy,
        "cauchy_margin": result.count_energy - result.cauchy_floor,
        "maximum_beta_modulus_error": result.maximum_beta_modulus_error,
        "global_closing_eta_frontier": str(closing_eta_frontier(H_MIN)),
        "adversarial_eta": str(adversarial_eta(H_MIN)),
        "fixed_exponent_miss": str(4 * KAPPA),
        "retained_edge_exponent": str(EDGE_EXPONENT),
        "diagonal_delta_frontier": str(diagonal_delta_frontier()),
        "finite_diagonal_energy": str(diagonal),
        "finite_diagonal_bound": str(diagonal_bound),
    }


if __name__ == "__main__":
    print(audit())
