#!/usr/bin/env python3
"""Exact residue-vector form of the SPF deletion telescope.

For a modulus q, every trapezoid and deletion-stage functional is a linear
combination of the values f(r), r modulo q.  Physical gaps are integral, so
twice every coefficient is an integer.  This module records those integer
vectors once; all additive numerators are then their finite Fourier transform.

The representation makes Parseval and the fourth moment exact integer
identities.  It is a finite diagnostic, not an asymptotic theorem for primes.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from prime_gap_sieve_deletion import smallest_prime_factors


SCHEMA = "zeta23.spf-residue-transport.v1"


def _zero_vector(q: int) -> list[int]:
    return [0 for _ in range(q)]


def _add_vector(target: list[int], source: Iterable[int]) -> None:
    for index, value in enumerate(source):
        target[index] += value


def _fourier(twice_mass: list[int], a: int) -> complex:
    q = len(twice_mass)
    return 0.5 * sum(
        coefficient * cmath.exp(2j * math.pi * a * residue / q)
        for residue, coefficient in enumerate(twice_mass)
    )


def _cyclic_correlation(vector: list[int]) -> list[int]:
    q = len(vector)
    return [
        sum(vector[r] * vector[(r + shift) % q] for r in range(q))
        for shift in range(q)
    ]


@dataclass(frozen=True)
class ResidueTransport:
    lo: int
    hi: int
    q: int
    initial_twice_mass: tuple[int, ...]
    final_twice_mass: tuple[int, ...]
    stages_twice_mass: dict[int, tuple[int, ...]]
    deleted_by_stage: dict[int, int]

    @property
    def length(self) -> int:
        return self.hi - self.lo

    def aggregate(self, primes: Iterable[int]) -> list[int]:
        answer = _zero_vector(self.q)
        for prime in primes:
            _add_vector(answer, self.stages_twice_mass[prime])
        return answer

    def post_q_vector(self) -> list[int]:
        """Sum traditional SPF stages labelled by primes ``p>q``.

        This is not the tail left by deleting all multiples of an arbitrary
        (possibly composite) modulus ``q`` first; that object is implemented
        in ``universal_q_reorder_transport.py``.
        """

        return self.aggregate(p for p in self.stages_twice_mass if p > self.q)

    def pre_q_vector(self) -> list[int]:
        return self.aggregate(p for p in self.stages_twice_mass if p < self.q)

    def at_q_vector(self) -> list[int]:
        return self.aggregate(p for p in self.stages_twice_mass if p == self.q)

    def identity_error_vector(self) -> list[int]:
        total = list(self.initial_twice_mass)
        for vector in self.stages_twice_mass.values():
            _add_vector(total, vector)
        return [
            final - reconstructed
            for final, reconstructed in zip(self.final_twice_mass, total)
        ]


def decompose_residues(lo: int, hi: int, q: int) -> ResidueTransport:
    """Compute all exact twice-mass residue vectors for one finite shell."""

    if lo < 2 or hi <= lo + 1:
        raise ValueError("require 2 <= lo < hi-1")
    if q <= 1:
        raise ValueError("q must exceed one")

    spf = smallest_prime_factors(hi)
    size = hi - lo + 1
    active = [True] * size
    previous = [index - 1 for index in range(size)]
    following = [index + 1 for index in range(size)]
    following[-1] = -1

    initial = _zero_vector(q)
    for value in range(lo, hi):
        initial[value % q] += 1
        initial[(value + 1) % q] += 1

    buckets: dict[int, list[int]] = {}
    for value in range(lo + 1, hi):
        if spf[value] == value:
            continue
        buckets.setdefault(spf[value], []).append(value - lo)

    stages: dict[int, tuple[int, ...]] = {}
    deleted_by_stage: dict[int, int] = {}
    for prime in sorted(buckets):
        vector = _zero_vector(q)
        deleted = 0
        for index in buckets[prime]:
            if not active[index]:
                continue
            left = previous[index]
            right = following[index]
            if left < 0 or right < 0:
                raise AssertionError("endpoints must remain active")
            left_gap = index - left
            right_gap = right - index
            left_value = lo + left
            center_value = lo + index
            right_value = lo + right
            vector[left_value % q] += right_gap
            vector[right_value % q] += left_gap
            vector[center_value % q] -= left_gap + right_gap
            following[left] = right
            previous[right] = left
            active[index] = False
            deleted += 1
        stages[prime] = tuple(vector)
        deleted_by_stage[prime] = deleted

    points = [lo + index for index, flag in enumerate(active) if flag]
    final = _zero_vector(q)
    for left, right in zip(points, points[1:]):
        gap = right - left
        final[left % q] += gap
        final[right % q] += gap

    result = ResidueTransport(
        lo=lo,
        hi=hi,
        q=q,
        initial_twice_mass=tuple(initial),
        final_twice_mass=tuple(final),
        stages_twice_mass=stages,
        deleted_by_stage=deleted_by_stage,
    )
    if any(result.identity_error_vector()):
        raise AssertionError("residue-vector deletion identity failed")
    return result


def moment_ledger(twice_mass: list[int], length: int) -> dict[str, object]:
    """Return Parseval/fourth-moment data and deterministic envelopes.

    ``maximum`` ranges over every nonzero additive frequency.  A selected
    reduced rational numerator ranges only over ``gcd(a,q)=1``; the separate
    ``reduced_*`` fields avoid silently paying for imprimitive frequencies
    when ``q`` is composite.  The twice-mass convention accounts for every
    factor of two below.
    """

    q = len(twice_mass)
    transforms = [_fourier(twice_mass, a) for a in range(q)]
    nonzero = transforms[1:]
    reduced_indices = [a for a in range(1, q) if math.gcd(a, q) == 1]
    reduced = [transforms[a] for a in reduced_indices]
    correlation = _cyclic_correlation(twice_mass)
    sum_fourier_2 = sum(abs(value) ** 2 for value in transforms)
    sum_fourier_4 = sum(abs(value) ** 4 for value in transforms)
    sum_nonzero_2 = sum(abs(value) ** 2 for value in nonzero)
    sum_nonzero_4 = sum(abs(value) ** 4 for value in nonzero)
    sum_reduced_2 = sum(abs(value) ** 2 for value in reduced)
    sum_reduced_4 = sum(abs(value) ** 4 for value in reduced)
    parseval_2 = q * sum(value * value for value in twice_mass) / 4.0
    parseval_4 = q * sum(value * value for value in correlation) / 16.0
    principal = sum(twice_mass) / 2.0
    parseval_nonzero_2 = parseval_2 - principal**2
    parseval_nonzero_4 = parseval_4 - principal**4
    max_index = max(range(1, q), key=lambda a: abs(transforms[a])) if q > 1 else 0
    reduced_max_index = max(reduced_indices, key=lambda a: abs(transforms[a]))
    scale = float(length)
    return {
        "twice_mass_sum": sum(twice_mass),
        "twice_mass_l1": sum(abs(value) for value in twice_mass),
        "twice_mass_l2_squared": sum(value * value for value in twice_mass),
        "correlation_l2_squared": sum(value * value for value in correlation),
        "parseval_second_error": abs(sum_fourier_2 - parseval_2),
        "parseval_fourth_error": abs(sum_fourier_4 - parseval_4),
        "principal_abs": abs(transforms[0]),
        "nonzero_parseval_second_error": abs(
            sum_nonzero_2 - parseval_nonzero_2
        ),
        "nonzero_parseval_fourth_error": abs(
            sum_nonzero_4 - parseval_nonzero_4
        ),
        "nonzero_rms_normalized": (
            math.sqrt(sum_nonzero_2 / len(nonzero)) / scale
        ),
        "nonzero_fourth_root_normalized": (
            (sum_nonzero_4 / len(nonzero)) ** 0.25 / scale
        ),
        "nonzero_l2_envelope_normalized": math.sqrt(sum_nonzero_2) / scale,
        "nonzero_l4_envelope_normalized": sum_nonzero_4**0.25 / scale,
        "reduced_frequency_count": len(reduced),
        "reduced_rms_normalized": (
            math.sqrt(sum_reduced_2 / len(reduced)) / scale
        ),
        "reduced_fourth_root_normalized": (
            (sum_reduced_4 / len(reduced)) ** 0.25 / scale
        ),
        "reduced_l2_envelope_normalized": math.sqrt(sum_reduced_2) / scale,
        "reduced_l4_envelope_normalized": sum_reduced_4**0.25 / scale,
        "maximum": {
            "a": max_index,
            "abs": abs(transforms[max_index]),
            "normalized_abs": abs(transforms[max_index]) / scale,
            "q_times_normalized_abs": q * abs(transforms[max_index]) / scale,
        },
        "reduced_maximum": {
            "a": reduced_max_index,
            "abs": abs(transforms[reduced_max_index]),
            "normalized_abs": abs(transforms[reduced_max_index]) / scale,
            "q_times_normalized_abs": (
                q * abs(transforms[reduced_max_index]) / scale
            ),
        },
    }


def analyze(lo: int, hi: int, q: int) -> dict[str, object]:
    result = decompose_residues(lo, hi, q)
    return {
        "schema": SCHEMA,
        "lo": lo,
        "hi": hi,
        "length": result.length,
        "q": q,
        "identity_error_vector": result.identity_error_vector(),
        "pre_q": moment_ledger(result.pre_q_vector(), result.length),
        "at_q": moment_ledger(result.at_q_vector(), result.length),
        "post_q": moment_ledger(result.post_q_vector(), result.length),
        "final": moment_ledger(list(result.final_twice_mass), result.length),
        "scope": (
            "exact finite integer residue transport and Fourier moments; "
            "pre_q/at_q/post_q refer to traditional prime SPF stages, not "
            "the arbitrary-modulus q-first tail; no asymptotic prime theorem"
        ),
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--lo", type=int, default=100_000)
    result.add_argument("--hi", type=int, default=200_000)
    result.add_argument("--q", type=int, default=59)
    result.add_argument("--output", type=Path)
    return result


def main() -> None:
    args = parser().parse_args()
    encoded = json.dumps(analyze(args.lo, args.hi, args.q), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
