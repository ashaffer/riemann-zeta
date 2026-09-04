"""Finite replay for the global actual-node antenna capacity gate."""

from __future__ import annotations

import argparse
import math


def distinct_prime_factor_count(n: int) -> int:
    """Return omega(n) by exact trial division (fixtures are deliberately small)."""
    if n < 1:
        raise ValueError("n must be positive")
    count = 0
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            count += 1
            while n % divisor == 0:
                n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        count += 1
    return count


def global_peak_bound_for_half_integer(n_center: int) -> int:
    """Theorem (0.2) for Y=n_center+1/2."""
    if n_center < 1:
        raise ValueError("n_center must be positive")
    four_y = 4 * n_center + 2
    return max(2, 1 + 2 * distinct_prime_factor_count(four_y))


def shell_contains_at_most_one_power(base: int, width: float = 0.2) -> bool:
    """Check the exact ratio criterion used in Section 1."""
    if base < 2 or width <= 0:
        raise ValueError("invalid base or width")
    return math.exp(2.0 * width) < base


def affine_peak_bound(internal_count: int, external_l1: float) -> float:
    """Right side of (3.7), before maximizing over 0 <= L <= 1."""
    if internal_count < 0 or not 0.0 <= external_l1 <= 1.0:
        raise ValueError("invalid theorem parameters")
    return 1.0 + external_l1 + 2.0 * internal_count * (1.0 - external_l1)


def verify() -> None:
    assert shell_contains_at_most_one_power(2)
    assert math.exp(0.4) < 2.0

    # Y=15/2: 4Y=30 has three distinct prime factors.
    assert distinct_prime_factor_count(30) == 3
    assert global_peak_bound_for_half_integer(7) == 7

    for internal_count in range(0, 12):
        values = [affine_peak_bound(internal_count, k / 1000.0) for k in range(1001)]
        expected = 2.0 if internal_count == 0 else 1.0 + 2.0 * internal_count
        assert abs(max(values) - expected) < 1e-12

    # The elementary omega bound used in (0.2).
    for n in range(1, 5000):
        assert distinct_prime_factor_count(n) <= math.log2(n) if n > 1 else True

    # A logarithm is eventually smaller than every fixed power.  This is a
    # numerical replay at a large log-scale, not the proof of the limit.
    log_y = 10_000.0
    log_logarithmic_bound = math.log(4.0 * log_y / math.log(2.0))
    assert log_logarithmic_bound < 0.019 * log_y


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify()
        print("global antenna capacity gate: verified")


if __name__ == "__main__":
    main()

