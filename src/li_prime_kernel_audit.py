"""Audit the renormalized Bombieri--Lagarias finite-prime contribution.

For K_n(x) = L_{n-1}^{(1)}(x), this computes

  S_f(n; N) = sum_{m <= N} Lambda(m)/m K_n(log m)
              - sum_{j=1}^n binom(n,j) (log N)^j/j!.

The limit as N tends to infinity is the finite-place term S_f(n).
"""

from __future__ import annotations

import argparse
import math


def von_mangoldt_table(limit: int) -> list[float]:
    values = [0.0] * (limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0
    for candidate in range(2, limit + 1):
        if not is_prime[candidate]:
            continue
        if candidate * candidate <= limit:
            is_prime[candidate * candidate : limit + 1 : candidate] = b"\x00" * (
                (limit - candidate * candidate) // candidate + 1
            )
        logarithm = math.log(candidate)
        power = candidate
        while power <= limit:
            values[power] = logarithm
            if power > limit // candidate:
                break
            power *= candidate
    return values


def li_prime_kernel(order: int, x: float) -> float:
    return sum(
        math.comb(order, j) * (-1) ** (j - 1) * x ** (j - 1) / math.factorial(j - 1)
        for j in range(1, order + 1)
    )


def counterterm(order: int, x: float) -> float:
    return sum(
        math.comb(order, j) * (-1) ** (j - 1) * x**j / math.factorial(j)
        for j in range(1, order + 1)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--orders", type=int, nargs="+", default=[1, 2, 4, 8])
    parser.add_argument(
        "--checkpoints", type=int, nargs="+", default=[10, 100, 1_000, 10_000, 100_000, 1_000_000]
    )
    args = parser.parse_args()
    if max(args.checkpoints) > args.limit:
        parser.error("all checkpoints must be at most limit")

    mangoldt = von_mangoldt_table(args.limit)
    checkpoints = set(args.checkpoints)
    partial = {order: 0.0 for order in args.orders}
    values: dict[tuple[int, int], float] = {}
    for integer in range(2, args.limit + 1):
        if mangoldt[integer]:
            logarithm = math.log(integer)
            for order in args.orders:
                partial[order] += (
                    mangoldt[integer] / integer * li_prime_kernel(order, logarithm)
                )
        if integer in checkpoints:
            logarithm = math.log(integer)
            for order in args.orders:
                values[order, integer] = partial[order] - counterterm(order, logarithm)

    for order in args.orders:
        print(f"order {order}")
        for checkpoint in args.checkpoints:
            print(f"  N={checkpoint:>8}: S_f(n;N)={values[order, checkpoint]: .12f}")


if __name__ == "__main__":
    main()
