#!/usr/bin/env python3
"""Numerically probe the archimedean plus prime-activation defect symbol.

For a support step ``a -> b`` the cancellation-sensitive shell contribution is

    A(xi) + D[a,b](xi) - W[a,b]
      = A(xi) - sum_new 2 Lambda(n)/sqrt(n) cos(2 pi log(n) xi),

where ``A(xi) = Re psi(1/4 + i*pi*xi) - log(pi)``.  This script scans that
symbol.  It is diagnostic only: sampled positivity is not a proof.
"""

from __future__ import annotations

import argparse
import math

import mpmath as mp
from sympy import primerange


def prime_powers(limit: int) -> list[tuple[int, float]]:
    values: dict[int, float] = {}
    for p in primerange(2, limit + 1):
        q = p
        while q <= limit:
            values[q] = math.log(p)
            if q > limit // p:
                break
            q *= p
    return sorted(values.items())


def archimedean(xi: float) -> float:
    return float(mp.re(mp.digamma(mp.mpf("0.25") + 1j * mp.pi * xi)) - mp.log(mp.pi))


def active_shell(powers: list[tuple[int, float]], a: float, b: float) -> list[tuple[int, float]]:
    return [(n, logp) for n, logp in powers if 2.0 * a <= math.log(n) < 2.0 * b]


def symbol(xi: float, shell: list[tuple[int, float]]) -> float:
    prime_cos = sum(
        2.0 * logp / math.sqrt(n) * math.cos(2.0 * math.pi * math.log(n) * xi)
        for n, logp in shell
    )
    return archimedean(xi) - prime_cos


def scan_shell(shell: list[tuple[int, float]], xmax: float, dx: float) -> dict[str, float]:
    minimum = math.inf
    argmin = 0.0
    last_negative = 0.0
    minima_after = {1.0: math.inf, 2.0: math.inf, 5.0: math.inf}
    count = int(xmax / dx) + 1
    for k in range(count):
        xi = k * dx
        value = symbol(xi, shell)
        if value < minimum:
            minimum, argmin = value, xi
        if value < 0.0:
            last_negative = xi
        for cutoff in minima_after:
            if xi >= cutoff:
                minima_after[cutoff] = min(minima_after[cutoff], value)
    return {
        "minimum": minimum,
        "argmin": argmin,
        "last_negative": last_negative,
        **{f"min_after_{cutoff:g}": value for cutoff, value in minima_after.items()},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=float, default=7.0 / 16.0)
    parser.add_argument("--stop", type=float, default=6.0)
    parser.add_argument("--step", type=float, default=0.1)
    parser.add_argument("--xmax", type=float, default=20.0)
    parser.add_argument("--dx", type=float, default=0.01)
    parser.add_argument("--event", action="store_true",
                        help="scan one prime-power activation at a time")
    args = parser.parse_args()

    limit = math.ceil(math.exp(2.0 * args.stop))
    powers = prime_powers(limit)
    print("a,b,count,weight,min,argmin,last_negative,min_after_1,min_after_2,min_after_5")
    if args.event:
        for n, logp in powers:
            threshold = math.log(n) / 2.0
            if threshold < args.start or threshold > args.stop:
                continue
            shell = [(n, logp)]
            weight = 2.0 * logp / math.sqrt(n)
            result = scan_shell(shell, args.xmax, args.dx)
            print(
                f"{threshold:.9g},{threshold:.9g},1,{weight:.9g},"
                f"{result['minimum']:.9g},{result['argmin']:.6g},"
                f"{result['last_negative']:.6g},{result['min_after_1']:.9g},"
                f"{result['min_after_2']:.9g},{result['min_after_5']:.9g}"
            )
        return
    a = args.start
    while a < args.stop:
        b = min(a + args.step, args.stop)
        shell = active_shell(powers, a, b)
        weight = sum(2.0 * logp / math.sqrt(n) for n, logp in shell)
        result = scan_shell(shell, args.xmax, args.dx)
        print(
            f"{a:.6g},{b:.6g},{len(shell)},{weight:.9g},"
            f"{result['minimum']:.9g},{result['argmin']:.6g},"
            f"{result['last_negative']:.6g},{result['min_after_1']:.9g},"
            f"{result['min_after_2']:.9g},{result['min_after_5']:.9g}"
        )
        a = b


if __name__ == "__main__":
    main()
