#!/usr/bin/env python3
"""Exact continued-fraction falsification scan for the primitive shifted cube.

The default scan is deliberately small.  Use --max-p 20000 to reproduce the
full consecutive scan reported in the accompanying audit; --cases accepts
additional comma-separated values of P.
"""

from __future__ import annotations

import argparse
from math import gcd


def floor_nth_root(n: int, k: int) -> int:
    lo, hi = 0, 1
    while hi**k <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return lo


def ceil_nth_root(n: int, k: int) -> int:
    r = floor_nth_root(n, k)
    return r if r**k == n else r + 1


def convergents(num: int, den: int):
    """Yield numerator, denominator pairs for the canonical regular CF."""
    p_m2, p_m1 = 0, 1
    q_m2, q_m1 = 1, 0
    while den:
        a, rem = divmod(num, den)
        p_now = a * p_m1 + p_m2
        q_now = a * q_m1 + q_m2
        yield p_now, q_now
        p_m2, p_m1 = p_m1, p_now
        q_m2, q_m1 = q_m1, q_now
        num, den = den, rem


def shell(P: int) -> tuple[int, int, int]:
    # Integers A with P^(9/16) <= A < 2 P^(9/16).
    a_lo = ceil_nth_root(P**9, 16)
    a_hi = ceil_nth_root((2**16) * P**9, 16)
    # Integers |D| <= P^(7/16).
    h_floor = floor_nth_root(P**7, 16)
    return a_lo, a_hi, h_floor


def scan_one(P: int):
    a_lo, a_hi, h_floor = shell(P)
    u = P
    while u**3 < 2 * P**3:
        d = gcd(u, P)
        v, p = u // d, P // d
        for B, A in convergents(v**3, p**3):
            if A < a_lo or A >= a_hi:
                continue
            if B < a_lo or B >= a_hi or gcd(A, B) != 1:
                continue
            D = A * u**3 - B * P**3
            if 0 < abs(D) <= h_floor:
                yield P, A, B, u, D
        u += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--cases", default="")
    args = parser.parse_args()

    cases = set(range(2, args.max_p + 1))
    if args.cases:
        cases.update(int(x) for x in args.cases.split(",") if x.strip())

    found = []
    for P in sorted(cases):
        found.extend(scan_one(P))

    if found:
        for row in found:
            print("solution", *row)
        raise SystemExit(1)
    print(f"no primitive nonzero solutions in {len(cases)} tested P-values")


if __name__ == "__main__":
    main()
