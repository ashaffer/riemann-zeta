#!/usr/bin/env python3
"""Low-memory diagnostics for the R136 reciprocal Mertens tail.

The exact part sieves only through 200 and uses ``Fraction``.  For a cutoff
L, the omitted reciprocal mass is exactly 1/(L+1), so replacing all unseen
values by tail hits gives a rigorous upper bound.  The larger NumPy run is a
diagnostic, not an asymptotic certificate.

The script also evaluates the explicit centered test in Theorem 6.1 of
``results/R136-WEAK-TAIL-GOOD-LAMBDA-AUDIT.md``.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction

import numpy as np


def mobius_sieve(limit: int) -> np.ndarray:
    """Return mu(0),...,mu(limit) in a signed-byte NumPy array."""

    if limit < 2:
        raise ValueError("limit must be at least two")
    is_prime = np.ones(limit + 1, dtype=np.bool_)
    is_prime[:2] = False
    for prime in range(2, math.isqrt(limit) + 1):
        if is_prime[prime]:
            is_prime[prime * prime : limit + 1 : prime] = False

    mu = np.ones(limit + 1, dtype=np.int8)
    mu[0] = 0
    for prime_value in np.flatnonzero(is_prime):
        prime = int(prime_value)
        mu[prime : limit + 1 : prime] *= -1
        square = prime * prime
        if square <= limit:
            mu[square : limit + 1 : square] = 0
    return mu


def exact_tail(limit: int, threshold: int) -> Fraction:
    """Return sum_{n<=limit, |M(n)|>threshold} 1/[n(n+1)]."""

    mu = mobius_sieve(limit)
    mertens = 0
    total = Fraction(0)
    for n in range(1, limit + 1):
        mertens += int(mu[n])
        if abs(mertens) > threshold:
            total += Fraction(1, n * (n + 1))
    return total


def print_exact_certificates(limit: int = 200) -> None:
    """Certify G(2U)/G(U)<1 at the low thresholds where possible."""

    remainder = Fraction(1, limit + 1)
    tails = {u: exact_tail(limit, u) for u in (1, 2, 4)}
    print(f"exact cutoff={limit}; unseen reciprocal mass={remainder}")
    for threshold in (1, 2):
        lower_denominator = tails[threshold]
        upper_numerator = tails[2 * threshold] + remainder
        upper_ratio = 2 * upper_numerator / lower_denominator
        verdict = "CERTIFIED < 1" if upper_ratio < 1 else "not certified"
        print(
            f"  U={threshold}: G(2U)/G(U) <= "
            f"{float(upper_ratio):.12g} ({verdict})"
        )


def truncated_tail_table(limit: int) -> None:
    """Print empirical tail ratios and coarse full-tail enclosures."""

    mu = mobius_sieve(limit)
    mertens = np.cumsum(mu, dtype=np.int32)[1:]
    absolute = np.abs(mertens)
    indices = np.arange(1, limit + 1, dtype=np.float64)
    weights = 1.0 / (indices * (indices + 1.0))
    histogram = np.bincount(absolute, weights=weights)
    tails = np.cumsum(histogram[::-1])[::-1]
    remainder = 1.0 / (limit + 1.0)
    maximum = int(absolute.max())

    print(
        f"diagnostic cutoff={limit}; M(limit)={int(mertens[-1])}; "
        f"max |M|={maximum}; unseen mass<={remainder:.12g}"
    )
    threshold = 1
    while 2 * threshold + 1 < len(tails):
        tail_u = float(tails[threshold + 1])
        tail_2u = float(tails[2 * threshold + 1])
        if tail_u == 0.0:
            break
        ratio_lower = 2.0 * tail_2u / (tail_u + remainder)
        ratio_upper = 2.0 * (tail_2u + remainder) / tail_u
        if tail_2u > 0.0:
            effective_q = -math.log(tail_2u / tail_u, 2.0)
            q_text = f"{effective_q:.6g}"
        else:
            q_text = "infinite/truncated"
        print(
            f"  U={threshold:<5d} truncated T={tail_u:.12g}; "
            f"full G-ratio in [{ratio_lower:.6g}, {ratio_upper:.6g}]; "
            f"truncated q_eff={q_text}"
        )
        threshold *= 2


def print_centered_obstruction(q_value: float) -> None:
    """Evaluate the lower bound U^q nu(|Qf_N|>U) from Theorem 6.1."""

    if q_value <= 1.0:
        raise ValueError("q must exceed one")
    print(f"centered floor-recurrence obstruction, q={q_value:g}")
    for n_value in (10, 100, 1000, 10000):
        threshold = n_value * (n_value - 1) / 4.0
        atom = 1.0 / (2.0 * n_value * (2.0 * n_value + 1.0))
        lower_bound = threshold**q_value * atom
        print(f"  N={n_value:<5d} lower weak-tail functional={lower_bound:.12g}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--limit",
        type=int,
        default=1_000_000,
        help="cutoff for the floating diagnostic (default: 1000000)",
    )
    parser.add_argument(
        "--q",
        type=float,
        default=1.25,
        help="weak exponent used in the centered obstruction",
    )
    args = parser.parse_args()
    if args.limit < 200:
        parser.error("--limit must be at least 200")

    print_exact_certificates()
    truncated_tail_table(args.limit)
    print_centered_obstruction(args.q)


if __name__ == "__main__":
    main()
