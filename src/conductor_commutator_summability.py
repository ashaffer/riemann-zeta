"""Prime-cutoff summability audit for Burnol's local H_p and K_p.

On the unramified radial basis eta_j, j in Z,

  (H_p)_{j0} = -log(p) p^(-|j|/2), j != 0,
  (K_p)_{j0} = i log(p)^2 j p^(-|j|/2), j != 0.

The script sums their exact squared vacuum fluctuations over p <= X.
"""

from __future__ import annotations

import argparse
import math


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [number for number in range(2, limit + 1) if sieve[number]]


def h_vacuum_variance(prime: int) -> float:
    logarithm = math.log(prime)
    return 2.0 * logarithm**2 / (prime - 1.0)


def k_vacuum_variance(prime: int) -> float:
    logarithm = math.log(prime)
    reciprocal = 1.0 / prime
    geometric_second_moment = reciprocal * (1.0 + reciprocal) / (1.0 - reciprocal) ** 3
    return 2.0 * logarithm**4 * geometric_second_moment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=2_000_000)
    parser.add_argument(
        "--checkpoints", type=int, nargs="+", default=[10, 100, 1_000, 10_000, 100_000, 1_000_000]
    )
    args = parser.parse_args()
    checkpoints = sorted(point for point in args.checkpoints if point <= args.limit)
    checkpoint_index = 0
    h_sum = 0.0
    k_sum = 0.0
    for prime in primes_up_to(args.limit):
        while checkpoint_index < len(checkpoints) and prime > checkpoints[checkpoint_index]:
            print(f"X={checkpoints[checkpoint_index]:>8}  H={h_sum: .9e}  K={k_sum: .9e}")
            checkpoint_index += 1
        h_sum += h_vacuum_variance(prime)
        k_sum += k_vacuum_variance(prime)
    while checkpoint_index < len(checkpoints):
        print(f"X={checkpoints[checkpoint_index]:>8}  H={h_sum: .9e}  K={k_sum: .9e}")
        checkpoint_index += 1


if __name__ == "__main__":
    main()
