#!/usr/bin/env python3
"""Exact integer-base deletion telescope for one rational denominator.

Fix an interval with prime endpoints and an integer modulus ``q`` smaller
than the interval.  Start with every integer node, delete every interior
multiple of ``q`` simultaneously, and only then delete all remaining
composites.  For the additive character ``exp(2*pi*i*a*n/q)`` the first
group is completely explicit: each deleted center has unit phase and two
unit gaps, so its contribution is ``cos(2*pi*a/q)-1``.

The module stores *twice* each trapezoid coefficient as an integer residue
vector.  Consequently the telescope, Parseval identity, and fourth moment
are exact before the final floating-point Fourier diagnostic.  This is a
finite frozen-additive laboratory; it does not prove cancellation for the
logarithmic prime antenna.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path

from prime_gap_sieve_deletion import smallest_prime_factors
from spf_residue_transport import _fourier, moment_ledger


SCHEMA = "zeta23.universal-q-reorder-transport.v1"


def _trapezoid_twice_mass(points: list[int], q: int) -> list[int]:
    """Return twice the endpoint trapezoid weights, folded modulo ``q``."""

    answer = [0] * q
    for left, right in zip(points, points[1:]):
        gap = right - left
        answer[left % q] += gap
        answer[right % q] += gap
    return answer


def _difference(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Coordinatewise ``right-left``."""

    return tuple(b - a for a, b in zip(left, right))


@dataclass(frozen=True)
class UniversalReorder:
    lo: int
    hi: int
    q: int
    q_multiple_count: int
    initial_twice_mass: tuple[int, ...]
    after_q_twice_mass: tuple[int, ...]
    final_twice_mass: tuple[int, ...]
    resonant_twice_mass: tuple[int, ...]
    nonresonant_twice_mass: tuple[int, ...]

    @property
    def length(self) -> int:
        return self.hi - self.lo

    def identity_error_vector(self) -> list[int]:
        return [
            final - initial - resonant - tail
            for final, initial, resonant, tail in zip(
                self.final_twice_mass,
                self.initial_twice_mass,
                self.resonant_twice_mass,
                self.nonresonant_twice_mass,
            )
        ]


def decompose_universal(lo: int, hi: int, q: int) -> UniversalReorder:
    """Build the exact integer -> no-q-multiples -> primes telescope."""

    if lo < 2 or hi <= lo + 1:
        raise ValueError("require 2 <= lo < hi-1")
    if q <= 2 or q >= lo:
        raise ValueError("require 2 < q < lo")

    spf = smallest_prime_factors(hi)
    if spf[lo] != lo or spf[hi] != hi:
        raise ValueError("lo and hi must be prime permanent endpoints")

    initial_points = list(range(lo, hi + 1))
    q_multiples = [value for value in range(lo + 1, hi) if value % q == 0]
    after_q_points = [
        value for value in initial_points if value in (lo, hi) or value % q != 0
    ]
    final_points = [
        value
        for value in initial_points
        if value in (lo, hi) or spf[value] == value
    ]

    initial = tuple(_trapezoid_twice_mass(initial_points, q))
    after_q = tuple(_trapezoid_twice_mass(after_q_points, q))
    final = tuple(_trapezoid_twice_mass(final_points, q))
    resonant = _difference(initial, after_q)
    nonresonant = _difference(after_q, final)
    result = UniversalReorder(
        lo=lo,
        hi=hi,
        q=q,
        q_multiple_count=len(q_multiples),
        initial_twice_mass=initial,
        after_q_twice_mass=after_q,
        final_twice_mass=final,
        resonant_twice_mass=resonant,
        nonresonant_twice_mass=nonresonant,
    )
    if any(result.identity_error_vector()):
        raise AssertionError("universal deletion telescope failed")

    expected = [0] * q
    expected[0] = -2 * len(q_multiples)
    expected[1] = len(q_multiples)
    expected[-1] = len(q_multiples)
    if list(result.resonant_twice_mass) != expected:
        raise AssertionError("explicit q-multiple residue vector failed")
    return result


def gap_sector_ledger(lo: int, hi: int, q: int, a: int) -> dict[str, object]:
    """Decompose the nonresonant tail by terminal prime-gap length.

    Each prime edge is compared with the punctured integer lattice obtained
    after deleting the interior multiples of ``q``.  The edgewise differences
    sum exactly to the global nonresonant tail.  Grouping by the gap length
    isolates the fixed-pair sectors (gap four, gap six, and so on) without
    replacing consecutiveness by a prime-pair majorant.
    """

    if math.gcd(a, q) != 1:
        raise ValueError("a must be a reduced numerator modulo q")
    result = decompose_universal(lo, hi, q)
    spf = smallest_prime_factors(hi)
    primes = [value for value in range(lo, hi + 1) if spf[value] == value]

    def phase(value: int) -> complex:
        angle = 2.0 * math.pi * a * (value % q) / q
        return complex(math.cos(angle), math.sin(angle))

    sectors: dict[int, complex] = {}
    counts: dict[int, int] = {}
    for left, right in zip(primes, primes[1:]):
        gap = right - left
        final_edge = 0.5 * gap * (phase(left) + phase(right))
        base_points = [left]
        base_points.extend(
            value
            for value in range(left + 1, right)
            if value % q != 0
        )
        base_points.append(right)
        base_edge = sum(
            0.5 * (y - x) * (phase(x) + phase(y))
            for x, y in zip(base_points, base_points[1:])
        )
        sectors[gap] = sectors.get(gap, 0j) + final_edge - base_edge
        counts[gap] = counts.get(gap, 0) + 1

    expected = _fourier(list(result.nonresonant_twice_mass), a)
    reconstructed = sum(sectors.values(), 0j)
    rows = [
        {
            "gap": gap,
            "count": counts[gap],
            "real": value.real,
            "imag": value.imag,
            "abs": abs(value),
            "normalized_abs": abs(value) / result.length,
        }
        for gap, value in sectors.items()
    ]
    rows.sort(key=lambda row: float(row["abs"]), reverse=True)
    return {
        "q": q,
        "a": a,
        "sector_count": len(rows),
        "reconstruction_error": abs(reconstructed - expected),
        "coherent_tail": {
            "real": reconstructed.real,
            "imag": reconstructed.imag,
            "abs": abs(reconstructed),
            "normalized_abs": abs(reconstructed) / result.length,
        },
        "sector_variation_normalized": sum(abs(value) for value in sectors.values())
        / result.length,
        "sectors": rows,
    }


def analyze(lo: int, hi: int, q: int) -> dict[str, object]:
    """Return exact vector moments and all-numerator maxima."""

    result = decompose_universal(lo, hi, q)
    resonant = list(result.resonant_twice_mass)
    tail = list(result.nonresonant_twice_mass)
    transforms = [_fourier(tail, a) for a in range(q)]
    candidates = [a for a in range(1, q) if math.gcd(a, q) == 1]
    worst_tail_a = max(candidates, key=lambda a: abs(transforms[a]))

    explicit_errors = []
    for a in candidates:
        expected = result.q_multiple_count * (
            math.cos(2.0 * math.pi * a / q) - 1.0
        )
        explicit_errors.append(abs(_fourier(resonant, a) - expected))

    return {
        "schema": SCHEMA,
        "lo": lo,
        "hi": hi,
        "length": result.length,
        "q": q,
        "q_multiple_count": result.q_multiple_count,
        "identity_error_vector": result.identity_error_vector(),
        "explicit_resonant_formula_max_error": max(explicit_errors, default=0.0),
        "initial": moment_ledger(list(result.initial_twice_mass), result.length),
        "resonant_q_group": moment_ledger(resonant, result.length),
        "nonresonant_tail": moment_ledger(tail, result.length),
        "final": moment_ledger(list(result.final_twice_mass), result.length),
        "worst_reduced_nonresonant_tail": {
            "a": worst_tail_a,
            "normalized_abs": abs(transforms[worst_tail_a]) / result.length,
            "q_times_normalized_abs": (
                q * abs(transforms[worst_tail_a]) / result.length
            ),
        },
        "worst_tail_gap_sectors": gap_sector_ledger(
            lo, hi, q, worst_tail_a
        ),
        "scope": (
            "exact finite frozen-additive integer-base reorder; the initial "
            "lattice mode and logarithmic/taper transfer remain separate"
        ),
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--lo", type=int, default=100_003)
    result.add_argument("--hi", type=int, default=199_999)
    result.add_argument("--q", type=int, default=59)
    result.add_argument("--output", type=Path)
    return result


def main() -> None:
    args = parser().parse_args()
    encoded = json.dumps(analyze(args.lo, args.hi, args.q), indent=2, sort_keys=True)
    encoded += "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
