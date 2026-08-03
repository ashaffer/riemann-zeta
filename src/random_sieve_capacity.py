"""Numerical scale check for the random-sieve resonance capacity."""
from __future__ import annotations

import argparse
import math

import numpy as np


def primes_up_to(limit: int) -> np.ndarray:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return np.flatnonzero(sieve)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", type=float, default=0.75)
    parser.add_argument("--a", type=float, default=0.35)
    parser.add_argument("--limits", nargs="+", type=int,
                        default=[1000, 10000, 100000, 1000000])
    args = parser.parse_args()
    if not (0.5 < args.beta < 1.0 and 1.0 - args.beta < args.a < 1.0):
        raise ValueError("require 1/2 < beta < 1 and 1-beta < a < 1")

    primes = primes_up_to(max(args.limits)).astype(float)
    print("y,entropy,cost,entropy_over_cost,expected_density_log_loss,"
          "expected_euler_variation")
    for limit in args.limits:
        ps = primes[primes <= limit]
        theta = ps ** (-args.a)
        entropy = float(np.sum(-theta * np.log(theta)
                               - (1.0 - theta) * np.log1p(-theta)))
        cost = float(np.sum(theta * np.log(ps)))
        density_loss = float(-np.sum(theta * np.log1p(-1.0 / ps)))
        euler_variation = float(np.sum(theta * ps ** (-args.beta)))
        print(f"{limit},{entropy:.12g},{cost:.12g},{entropy/cost:.12g},"
              f"{density_loss:.12g},{euler_variation:.12g}")


if __name__ == "__main__":
    main()
