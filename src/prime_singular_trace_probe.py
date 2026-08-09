"""Finite normalization checks for the prime singular-trace boundary gate.

The limits are deliberately slow (their scale is log log N).  This script
checks formulas and trends only; it makes no asymptotic or zeta-zero claim.
"""

from __future__ import annotations

import argparse
import cmath
import math
from dataclasses import dataclass


def primes_up_to(limit: int) -> list[int]:
    """Return all primes at most ``limit`` by an elementary byte sieve."""
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


def psi_scale(count: int) -> float:
    """Prime-adapted Marcinkiewicz scale used in the report."""
    if count <= 0:
        raise ValueError("count must be positive")
    return math.log(math.log(math.e**math.e + count)) - 1.0


@dataclass(frozen=True)
class Residues:
    count: int
    prime_residue: float
    ordinary_dixmier_ratio: float
    horizontal_distance: float
    vertical_distance: float
    vertical_complex_abs: float


def residues(primes: list[int], epsilon: float, height: float) -> Residues:
    """Compute finite spectral residues on the supplied prime prefix."""
    if not primes:
        raise ValueError("at least one prime is required")
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    if height == 0:
        raise ValueError("height must be nonzero")

    scale = psi_scale(len(primes))
    harmonic = sum(1.0 / p for p in primes)
    horizontal = sum((1.0 - p ** (-epsilon)) / p for p in primes)
    phases = [cmath.exp(-1j * height * math.log(p)) for p in primes]
    vertical = sum(abs(1.0 - phase) / p for p, phase in zip(primes, phases))
    complex_sum = sum(phase / p for p, phase in zip(primes, phases))
    return Residues(
        count=len(primes),
        prime_residue=harmonic / scale,
        ordinary_dixmier_ratio=harmonic / math.log(len(primes) + 1.0),
        horizontal_distance=horizontal / scale,
        vertical_distance=vertical / scale,
        vertical_complex_abs=abs(complex_sum) / scale,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=2_000_000)
    parser.add_argument("--epsilon", type=float, default=0.08)
    parser.add_argument("--height", type=float, default=0.7)
    args = parser.parse_args()

    primes = primes_up_to(args.limit)
    row = residues(primes, args.epsilon, args.height)
    print(f"prime count                 {row.count}")
    print(f"prime log-log residue       {row.prime_residue:.12f}  -> 1")
    print(f"ordinary Dixmier ratio      {row.ordinary_dixmier_ratio:.12f}  -> 0")
    print(f"horizontal ideal distance   {row.horizontal_distance:.12f}  -> 1")
    print(
        f"vertical ideal distance     {row.vertical_distance:.12f}"
        f"  -> {4 / math.pi:.12f}"
    )
    print(f"vertical complex residue    {row.vertical_complex_abs:.12f}  -> 0")


if __name__ == "__main__":
    main()

