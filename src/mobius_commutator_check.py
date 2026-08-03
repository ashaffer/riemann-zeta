"""Finite verification of the additive--multiplicative commutator identity."""
from __future__ import annotations

import argparse

import numpy as np


def mobius_values(limit: int) -> np.ndarray:
    mu = np.ones(limit + 1, dtype=np.int64)
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        mu[p::p] *= -1
        p2 = p * p
        if p2 <= limit:
            mu[p2::p2] = 0
            prime[p2::p] = False
        if p <= limit // 2:
            prime[2 * p::p] = False
    mu[0] = 0
    return mu


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=300)
    parser.add_argument("--prime", type=int, default=3)
    args = parser.parse_args()

    nmax, p = args.limit, args.prime
    mu = mobius_values(nmax)
    f = {n: int(mu[n]) for n in range(1, nmax + 1)}
    value = 0
    for h in range(-p * nmax, nmax + 1):
        value += sum(f[n] * (f.get(p * n + h, 0)
                            - f.get(p * n + p * h, 0))
                     for n in range(1, nmax + 1))

    total = sum(f.values())
    p_total = sum(f.get(p * m, 0) for m in range(1, nmax // p + 1))
    expected = total * (total - p_total)
    print(f"aggregate={value}")
    print(f"factorized={expected}")
    print(f"identity_holds={value == expected}")


if __name__ == "__main__":
    main()
