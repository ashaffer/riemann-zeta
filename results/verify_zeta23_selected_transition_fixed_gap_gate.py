#!/usr/bin/env python3
"""Verify the finite-group thresholds and the gap-four reduction.

This checker is deliberately finite.  It verifies exact Fourier identities,
the exponent ledger, and the reduction of the near-quarter gap-four sector to
a twisted cousin-prime sum.  It does not assert an asymptotic prime-pair
estimate.
"""

from __future__ import annotations

import cmath
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from prime_gap_sieve_deletion import smallest_prime_factors  # noqa: E402
from universal_q_reorder_transport import gap_sector_ledger  # noqa: E402


KAPPA = Fraction(1974048259, 100000000000)
BETA_MIN = Fraction(1537, 10000)
H_TOP = Fraction(33, 133)


def close(left: float, right: float, scale: float = 1.0) -> None:
    assert abs(left - right) <= 2e-9 * max(scale, 1.0)


def finite_group_check() -> None:
    vector = [3, -2, 0, 4, -5, 1, -1]
    q = len(vector)
    assert sum(vector) == 0
    transforms = [
        0.5
        * sum(
            value * cmath.exp(2j * math.pi * a * residue / q)
            for residue, value in enumerate(vector)
        )
        for a in range(q)
    ]
    correlation = [
        sum(
            vector[residue] * vector[(residue + shift) % q]
            for residue in range(q)
        )
        for shift in range(q)
    ]
    lhs2 = sum(abs(value) ** 2 for value in transforms)
    rhs2 = q * sum(value * value for value in vector) / 4
    lhs4 = sum(abs(value) ** 4 for value in transforms)
    rhs4 = q * sum(value * value for value in correlation) / 16
    close(lhs2, rhs2, rhs2)
    close(lhs4, rhs4, rhs4)


def exponent_check() -> dict[str, Fraction]:
    # Per-block sufficient thresholds when H=Y^h and q=Y^b:
    # sum_r |v_r|^2 <= 4 Y^(2h-b-2kappa),
    # sum_s |C(s)|^2 <= 16 Y^(4h-b-4kappa).
    l2_at_small_q = 2 * H_TOP - BETA_MIN - 2 * KAPPA
    l2_at_large_q = H_TOP - 2 * KAPPA
    l4_at_small_q = 4 * H_TOP - BETA_MIN - 4 * KAPPA
    l4_at_large_q = 3 * H_TOP - 4 * KAPPA
    delta_required = KAPPA / BETA_MIN
    eighth_deficit = KAPPA - BETA_MIN / 8
    assert l2_at_small_q > l2_at_large_q > 0
    assert l4_at_small_q > l4_at_large_q > 0
    assert delta_required > Fraction(1, 8)
    assert eighth_deficit > 0
    return {
        "l2_at_small_q": l2_at_small_q,
        "l2_at_large_q": l2_at_large_q,
        "l4_at_small_q": l4_at_small_q,
        "l4_at_large_q": l4_at_large_q,
        "delta_required": delta_required,
        "eighth_deficit": eighth_deficit,
        "aggregate_l2_weighted": 1 + H_TOP - 2 * KAPPA,
        "aggregate_l4_weighted": 1 + 3 * H_TOP - 4 * KAPPA,
    }


def character_mod_four(value: int) -> int:
    residue = value % 4
    if residue == 1:
        return 1
    if residue == 3:
        return -1
    return 0


def fixed_gap_check(lo: int, hi: int, q: int) -> dict[str, float | int]:
    assert q % 4 == 3
    a = (q + 1) // 4
    z = cmath.exp(2j * math.pi * a / q)
    spf = smallest_prime_factors(hi)
    primes = [value for value in range(lo, hi + 1) if spf[value] == value]
    pairs = [(left, right) for left, right in zip(primes, primes[1:]) if right - left == 4]
    assert pairs

    # Every prime pair p,p+4 above 3 is consecutive: among p,p+2,p+4 one
    # member is divisible by 3, and it cannot be either prime endpoint.
    for left, right in pairs:
        assert left > 3 and right == left + 4
        assert (left + 2) % 3 == 0
        assert spf[left + 2] != left + 2

    direct = 0j
    exceptional_edges = 0
    for left, right in pairs:
        final_edge = 2 * (z**left + z**right)
        base_points = [left]
        base_points.extend(
            value
            for value in range(left + 1, right)
            if value % q != 0
        )
        base_points.append(right)
        exceptional_edges += int(len(base_points) != 5)
        base_edge = sum(
            0.5 * (y - x) * (z**x + z**y)
            for x, y in zip(base_points, base_points[1:])
        )
        direct += final_edge - base_edge

    ledger = gap_sector_ledger(lo, hi, q, a)
    row = next(item for item in ledger["sectors"] if item["gap"] == 4)
    recorded = complex(float(row["real"]), float(row["imag"]))
    close(abs(direct - recorded), 0.0, abs(direct))

    twisted_cousin = sum(
        character_mod_four(left)
        * cmath.exp(2j * math.pi * left / (4 * q))
        for left, _ in pairs
    )
    main = 2j * (1 + cmath.exp(2j * math.pi / q)) * twisted_cousin

    # B_4(z)=.5(1+z^4)+z+z^2+z^3 vanishes at z=i.  Its derivative has
    # modulus at most 8 on the unit circle, while |z-i|<=pi/(2q).
    # A q-puncture changes one integer trapezoid by at most 2.
    error_bound = 4 * math.pi * len(pairs) / q + 2 * exceptional_edges + 1e-8
    assert abs(direct - main) <= error_bound
    assert exceptional_edges <= (hi - lo) // q + 2

    return {
        "q": q,
        "a": a,
        "gap_four_pairs": len(pairs),
        "exceptional_q_punctured_edges": exceptional_edges,
        "gap_four_normalized_abs": abs(direct) / (hi - lo),
        "full_tail_normalized_abs": float(
            ledger["coherent_tail"]["normalized_abs"]
        ),
        "reduction_error": abs(direct - main),
        "certified_error_bound": error_bound,
    }


def main() -> None:
    finite_group_check()
    exponents = exponent_check()
    rows = [fixed_gap_check(100003, 199999, q) for q in (43, 59, 83)]
    print("selected transition fixed-gap gate: PASS")
    print(f"kappa_max={float(KAPPA):.12f}")
    print(f"required q-decay delta>{float(exponents['delta_required']):.12f}")
    print(f"q^(-1/8) saving deficit={float(exponents['eighth_deficit']):.12f}")
    for name, value in exponents.items():
        if name not in {"delta_required", "eighth_deficit"}:
            print(f"{name} exponent={float(value):.12f}")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
