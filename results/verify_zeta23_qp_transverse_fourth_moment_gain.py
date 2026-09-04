#!/usr/bin/env python3
"""Independent finite replay for the transverse fourth-moment ledger.

This checks exact exponent algebra, the interpolation inequality, finite
product convolution, and sample prime-power product multiplicities.  The
asymptotic analytic proof remains the accompanying Markdown argument.
"""

from __future__ import annotations

import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_transverse_fourth_moment_gate import (  # noqa: E402
    active_ledger,
    centered_positive_cap_lower,
    convolution_cauchy_bound,
)


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p in range(2, limit + 1) if sieve[p]]


def shell_prime_powers(center: float, width: float) -> list[int]:
    lower = center * math.exp(-width)
    upper = center * math.exp(width)
    nodes: set[int] = set()
    for prime in primes_up_to(int(upper)):
        power = prime
        while power < upper:
            if power > lower:
                nodes.add(power)
            power *= prime
    return sorted(nodes)


def maximum_ordered_product_multiplicity(nodes: list[int]) -> int:
    counts = Counter(n * m for n in nodes for m in nodes)
    return max(counts.values(), default=0)


def main() -> None:
    ledger = active_ledger()
    assert ledger.aperture == Fraction(50, 33)
    assert ledger.unresolved_pair_exponent == Fraction(16, 33)
    assert ledger.transverse_depth_exponent == Fraction(49, 66)

    moment_exponents = [ledger.even_moment_depth_exponent(k) for k in range(2, 9)]
    assert moment_exponents == sorted(moment_exponents)
    assert all(value > moment_exponents[0] for value in moment_exponents[1:])

    lhs, rhs = convolution_cauchy_bound(
        {6: 1.0, 10: -2.0, 21: 0.5, 35: 3.0}
    )
    assert 0.0 < lhs <= rhs + 1e-12
    assert centered_positive_cap_lower(1.0, 1.0) == 0.5

    width = 0.4
    safe_pair_bound = max(2, math.floor(2 * width / math.log(2)) + 2)
    sample_multiplicities: dict[str, int] = {}
    for center in (50.5, 100.5, 500.5, 1000.5):
        multiplicity = maximum_ordered_product_multiplicity(
            shell_prime_powers(center, width)
        )
        assert multiplicity <= safe_pair_bound
        sample_multiplicities[str(center)] = multiplicity

    print(
        json.dumps(
            {
                "status": "PASS",
                "aperture": str(ledger.aperture),
                "fourth_moment_exponent": str(moment_exponents[0]),
                "higher_even_moment_exponents": [
                    str(value) for value in moment_exponents[1:]
                ],
                "safe_sample_pair_bound": safe_pair_bound,
                "sample_pair_multiplicities": sample_multiplicities,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
