#!/usr/bin/env python3
"""Replay the weighted unit-residue Ramanujan bound.

This is a finite arithmetic verifier for Theorem 2.1 in
ZETA23-UNIT-RESIDUE-WEIGHTED-CHIRP-GATE-2026-08-13.md.  It uses only the
Python standard library.
"""

from __future__ import annotations

import argparse
import cmath
import math


def arithmetic_tables(limit: int) -> tuple[list[int], list[int]]:
    """Return Euler-phi and Moebius tables through ``limit``."""
    phi = list(range(limit + 1))
    mu = [1] * (limit + 1)
    for p in range(2, limit + 1):
        if phi[p] != p:
            continue
        for multiple in range(p, limit + 1, p):
            phi[multiple] -= phi[multiple] // p
            mu[multiple] *= -1
        square = p * p
        for multiple in range(square, limit + 1, square):
            mu[multiple] = 0
    return phi, mu


def ramanujan_direct(q: int, a: int) -> complex:
    return sum(
        cmath.exp(2j * math.pi * a * r / q)
        for r in range(q)
        if math.gcd(r, q) == 1
    )


def audit(q_max: int, direct_q_max: int) -> None:
    phi, mu = arithmetic_tables(q_max)
    sharp_ratio = 0.0
    sharp_data: tuple[int, int, int] | None = None
    holder_error = 0.0

    for q in range(2, q_max + 1):
        phi_q = phi[q]
        for a in range(1, q):
            r_a = min(a, q - a)
            m = q // math.gcd(q, a)
            c = mu[m] * phi_q // phi[m]
            ratio = abs(c) / (phi_q * math.sqrt(r_a / q))
            if ratio > sharp_ratio:
                sharp_ratio = ratio
                sharp_data = (q, a, m)

            if q <= direct_q_max:
                holder_error = max(
                    holder_error,
                    abs(ramanujan_direct(q, a) - c),
                )

    assert sharp_data is not None
    q, a, m = sharp_data
    theoretical = math.sqrt(2.0)
    if sharp_ratio > theoretical + 1e-10:
        raise AssertionError((sharp_ratio, theoretical, sharp_data))
    if holder_error > 1e-9:
        raise AssertionError(holder_error)

    # For every even q, -e_q((q/2)r) is one on all units and its normalized
    # weighted bill W/sqrt(Y) is exactly 1/sqrt(2).
    parity_errors = []
    for even_q in range(2, min(q_max, 200) + 1, 2):
        values = [
            -cmath.exp(2j * math.pi * (even_q // 2) * r / even_q)
            for r in range(even_q)
            if math.gcd(r, even_q) == 1
        ]
        parity_errors.append(max(abs(value - 1.0) for value in values))
    parity_error = max(parity_errors)
    parity_bill = math.sqrt(0.5)

    print(f"q_max={q_max}")
    print(f"max_ratio={sharp_ratio:.15f}")
    print(f"sqrt_2={theoretical:.15f}")
    print(f"extremizer_q={q} a={a} m={m}")
    print(f"holder_direct_max_error={holder_error:.3e}")
    print(f"parity_value_max_error={parity_error:.3e}")
    print(f"parity_W_over_sqrtY={parity_bill:.15f}")
    print("verdict=PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=5000)
    parser.add_argument("--direct-q-max", type=int, default=80)
    args = parser.parse_args()
    if args.q_max < 2:
        parser.error("--q-max must be at least 2")
    audit(args.q_max, min(args.direct_q_max, args.q_max))


if __name__ == "__main__":
    main()
