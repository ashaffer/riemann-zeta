"""Exact-transition diagnostics for the Nicolas primorial criterion."""

from __future__ import annotations

import argparse
import math


EULER_GAMMA = 0.577215664901532860606512090082402431


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=2_000_000)
    args = parser.parse_args()

    theta = 0.0
    log_mertens_product = 0.0
    records: list[tuple[int, float, float]] = []
    for prime in primes_up_to(args.limit):
        theta += math.log(prime)
        log_mertens_product -= math.log1p(-1.0 / prime)
        if theta > 1.0:
            # log u_k, where u_k=N_k/(phi(N_k) log log N_k).
            log_u = log_mertens_product - math.log(math.log(theta))
            records.append((prime, theta, log_u))

    increments = [records[index + 1][2] - records[index][2] for index in range(len(records) - 1)]
    curvatures = [increments[index + 1] - increments[index] for index in range(len(increments) - 1)]
    curvature_sign_changes = sum(
        curvatures[index - 1] * curvatures[index] < 0
        for index in range(1, len(curvatures))
    )

    final_prime, final_theta, final_log_u = records[-1]
    print(f"primes audited: {len(records) + 1}")
    print(f"final prime: {final_prime}")
    print(f"theta(final prime): {final_theta:.12f}")
    print(f"log(u)-gamma: {final_log_u - EULER_GAMMA:.12e}")
    print(f"positive first differences: {sum(value > 0 for value in increments)}")
    print(f"negative first differences: {sum(value < 0 for value in increments)}")
    print(f"positive second differences: {sum(value > 0 for value in curvatures)}")
    print(f"negative second differences: {sum(value < 0 for value in curvatures)}")
    print(f"second-difference sign changes: {curvature_sign_changes}")
    print(f"first-difference range: [{min(increments):.12e}, {max(increments):.12e}]")


if __name__ == "__main__":
    main()
