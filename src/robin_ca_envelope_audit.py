"""Variational-envelope audit for colossally abundant exponent transitions."""

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
    parser.add_argument("--prime-limit", type=int, default=20_000)
    parser.add_argument("--epsilon-floor", type=float, default=1e-12)
    args = parser.parse_args()

    events: list[tuple[float, int, int, float, float]] = []
    for prime in primes_up_to(args.prime_limit):
        log_prime = math.log(prime)
        exponent = 1
        while True:
            gain = math.log1p(-prime ** (-(exponent + 1))) - math.log1p(
                -prime ** (-exponent)
            )
            epsilon = gain / log_prime
            if epsilon < args.epsilon_floor:
                break
            events.append((epsilon, prime, exponent, gain, log_prime))
            exponent += 1
    events.sort(reverse=True)

    # Above this threshold, no omitted prime can have its first exponent event.
    trusted_epsilon = math.log1p(1.0 / (args.prime_limit + 1)) / math.log(
        args.prime_limit + 1
    )
    log_n = 0.0
    abundance_log = 0.0
    scores: list[float] = []
    trusted_events = 0
    for epsilon, _prime, _exponent, gain, log_prime in events:
        if epsilon < trusted_epsilon:
            break
        trusted_events += 1
        log_n += log_prime
        abundance_log += gain
        if log_n > math.log(5040):
            scores.append(abundance_log - EULER_GAMMA - math.log(math.log(log_n)))

    increments = [scores[index + 1] - scores[index] for index in range(len(scores) - 1)]
    sign_changes = sum(
        increments[index - 1] * increments[index] < 0
        for index in range(1, len(increments))
    )
    print(f"trusted epsilon floor: {trusted_epsilon:.12e}")
    print(f"trusted exponent events: {trusted_events}")
    print(f"Robin-score events above 5040: {len(scores)}")
    print(f"positive score increments: {sum(value > 0 for value in increments)}")
    print(f"negative score increments: {sum(value < 0 for value in increments)}")
    print(f"increment sign changes: {sign_changes}")
    print(f"increment range: [{min(increments):.12e}, {max(increments):.12e}]")
    print(f"largest sampled Robin log-margin: {max(scores):.12e}")
    print(f"final sampled Robin log-margin: {scores[-1]:.12e}")


if __name__ == "__main__":
    main()
