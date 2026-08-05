#!/usr/bin/env python3
"""Finite scout for the Selberg--Delange obstruction to a Mobius inverse gate.

The proof in the accompanying report is analytic.  This script only displays
finite partial sums of

    f_z(n) = mu(n)^2 z^omega(n),       |z| <= 1, z != -1,

and the exact prime-distance growth.  The default cutoff is deliberately
small: the repository has previously encountered memory pressure, and no
large computation is needed for the counterexample.
"""

from __future__ import annotations

import argparse
import cmath
import math

import numpy as np


def primes_up_to(limit: int) -> np.ndarray:
    """Return the primes up to ``limit`` using one byte per candidate."""
    sieve = np.ones(limit + 1, dtype=np.bool_)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return np.flatnonzero(sieve)


def partial_sums(limit: int, z: complex, primes: np.ndarray) -> np.ndarray:
    """Return in-place cumulative sums of mu(n)^2 z^omega(n)."""
    values = np.ones(limit + 1, dtype=np.complex128)
    values[0] = 0.0
    for raw_p in primes:
        p = int(raw_p)
        values[p::p] *= z
        if p * p <= limit:
            values[p * p :: p * p] = 0.0
    np.cumsum(values, out=values)
    return values


def checkpoint_indices(limit: int, count: int) -> np.ndarray:
    start = min(limit, 1_000)
    points = np.geomspace(start, limit, num=count).astype(np.int64)
    return np.unique(points)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=250_000)
    parser.add_argument(
        "--theta",
        type=float,
        default=0.0,
        help="prime phase in radians: z=radius*exp(i*theta); pi at radius 1 is Mobius",
    )
    parser.add_argument(
        "--radius",
        type=float,
        default=0.5,
        help="modulus of z; use a value below 1 for a uniform distance bound",
    )
    parser.add_argument(
        "--beta",
        type=float,
        default=0.6,
        help="super-square-root comparison exponent",
    )
    parser.add_argument("--checkpoints", type=int, default=8)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.limit < 1_000:
        raise SystemExit("--limit must be at least 1000")
    if not 0.5 < args.beta < 1.0:
        raise SystemExit("--beta must lie strictly between 1/2 and 1")
    if args.checkpoints < 2:
        raise SystemExit("--checkpoints must be at least 2")

    if not 0.0 < args.radius <= 1.0:
        raise SystemExit("--radius must lie in (0,1]")
    z = args.radius * cmath.exp(1j * args.theta)
    if abs(z + 1.0) < 1e-12:
        raise SystemExit("theta=pi is the singular Mobius endpoint; choose z != -1")

    primes = primes_up_to(args.limit)
    sums = partial_sums(args.limit, z, primes)
    reciprocal_primes = np.cumsum(1.0 / primes.astype(np.float64))

    print(f"limit={args.limit}  z={z.real:+.6f}{z.imag:+.6f}i  beta={args.beta}")
    print("x          |sum f_z|/x^beta   SD modulus normalization   D(f_z,1;x)^2")
    for x in checkpoint_indices(args.limit, args.checkpoints):
        prime_count = int(np.searchsorted(primes, x, side="right"))
        prime_harmonic = float(reciprocal_primes[prime_count - 1])
        total = sums[int(x)]
        threshold_ratio = abs(total) / float(x) ** args.beta
        sd_scale = float(x) * math.log(float(x)) ** (z.real - 1.0)
        sd_normalized = abs(total) / sd_scale
        distance_sq = (1.0 - z.real) * prime_harmonic
        print(
            f"{int(x):<10d} {threshold_ratio:>17.8f}"
            f" {sd_normalized:>26.8f} {distance_sq:>18.8f}"
        )

    print()
    print("The theorem, not this finite scout, is decisive:")
    print("  sum_{n<=x} f_z(n) ~ C_z x (log x)^(z-1), C_z != 0.")
    print("Thus its modulus eventually exceeds x^beta for every fixed beta<1,")
    print("while the displayed pretentious distance diverges like log log x.")
    if abs(z) < 1.0:
        print(
            "Moreover D(f_z,chi*n^it;x)^2 >= (1-|z|) sum_{p<=x}1/p "
            "uniformly in chi,t."
        )


if __name__ == "__main__":
    main()
