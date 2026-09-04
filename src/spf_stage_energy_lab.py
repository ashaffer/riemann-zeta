#!/usr/bin/env python3
"""Selected-numerator energy laboratory for exact SPF deletion stages.

The prime-gap trapezoid admits an exact decomposition into least-prime-factor
deletion stages.  This module asks a deliberately narrower question than the
decomposition itself: after removing the uniquely resonant stage ``p=q``, do
the stages in a dyadic ``p`` range cancel at the *same selected numerator*?

The output keeps three quantities distinct:

* ``coherent``: the modulus of the signed sum of the stages;
* ``energy``: the square root of the sum of their squared moduli; and
* ``variation``: the sum of their moduli.

Finite computations are conjecture-discovery/falsification tools.  They are
not asymptotic estimates for primes.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from prime_gap_sieve_deletion import decompose, rational_mode


SCHEMA = "zeta23.spf-stage-energy-lab.v1"


@dataclass(frozen=True)
class StageEnergy:
    """Coherent, quadratic, and total-variation ledgers for some stages."""

    stage_count: int
    deleted: int
    coherent: complex
    energy: float
    variation: float

    @classmethod
    def from_primes(cls, result, primes: Iterable[int]) -> "StageEnergy":
        selected = tuple(primes)
        values = tuple(result.stages[p] for p in selected)
        return cls(
            stage_count=len(selected),
            deleted=sum(result.deleted_by_stage[p] for p in selected),
            coherent=sum(values, 0j),
            energy=math.sqrt(sum(abs(value) ** 2 for value in values)),
            variation=sum(abs(value) for value in values),
        )

    def encoded(self, length: int) -> dict[str, object]:
        scale = float(length)
        coherent_abs = abs(self.coherent)
        return {
            "stage_count": self.stage_count,
            "deleted": self.deleted,
            "coherent": {
                "real": self.coherent.real,
                "imag": self.coherent.imag,
                "abs": coherent_abs,
                "normalized_abs": coherent_abs / scale,
            },
            "energy": self.energy,
            "normalized_energy": self.energy / scale,
            "variation": self.variation,
            "normalized_variation": self.variation / scale,
            "coherent_over_energy": coherent_abs / max(self.energy, 1e-300),
            "energy_over_variation": self.energy / max(self.variation, 1e-300),
        }


def _post_q_bins(primes: Iterable[int], q: int) -> dict[int, list[int]]:
    """Group p>q by floor(log2(p/q)); bin zero is q<p<2q."""

    bins: dict[int, list[int]] = {}
    for prime in primes:
        if prime <= q:
            continue
        index = (prime // q).bit_length() - 1
        bins.setdefault(index, []).append(prime)
    return bins


def analyze_numerator(lo: int, hi: int, q: int, a: int) -> dict[str, object]:
    """Return the exact stage-energy ledger for one rational mode."""

    result = decompose(lo, hi, rational_mode(a, q))
    ordered = sorted(result.stages)
    pre = [p for p in ordered if p < q]
    at = [p for p in ordered if p == q]
    post = [p for p in ordered if p > q]
    bins = _post_q_bins(post, q)

    post_rows = []
    for index in sorted(bins):
        ledger = StageEnergy.from_primes(result, bins[index])
        row = ledger.encoded(result.length)
        row.update(
            {
                "index": index,
                "p_min_inclusive": q * (1 << index),
                "p_max_exclusive": q * (1 << (index + 1)),
            }
        )
        post_rows.append(row)

    pre_energy = StageEnergy.from_primes(result, pre)
    at_energy = StageEnergy.from_primes(result, at)
    post_energy = StageEnergy.from_primes(result, post)
    final_scale = abs(result.final) / result.length
    q_inverse = 1.0 / q
    return {
        "q": q,
        "a": a,
        "lo": lo,
        "hi": hi,
        "length": result.length,
        "identity_error": result.identity_error,
        "initial_normalized_abs": abs(result.initial) / result.length,
        "final_normalized_abs": final_scale,
        "q_times_final_normalized_abs": q * final_scale,
        "q_inverse": q_inverse,
        "pre_q": pre_energy.encoded(result.length),
        "at_q": at_energy.encoded(result.length),
        "post_q": post_energy.encoded(result.length),
        "post_q_bins": post_rows,
    }


def analyze_modulus(
    lo: int,
    hi: int,
    q: int,
    numerators: Iterable[int] | None = None,
) -> dict[str, object]:
    """Scan reduced numerators and identify the worst coherent post-q tail."""

    if q <= 2:
        raise ValueError("q must exceed two")
    candidates = (
        tuple(a for a in range(1, q) if math.gcd(a, q) == 1)
        if numerators is None
        else tuple(numerators)
    )
    if not candidates:
        raise ValueError("at least one numerator is required")
    if any(a <= 0 or a >= q or math.gcd(a, q) != 1 for a in candidates):
        raise ValueError("numerators must be reduced residues in [1,q)")

    rows = [analyze_numerator(lo, hi, q, a) for a in candidates]
    worst_post = max(
        rows,
        key=lambda row: float(row["post_q"]["coherent"]["normalized_abs"]),
    )
    worst_final = max(rows, key=lambda row: float(row["final_normalized_abs"]))
    worst_bin: tuple[float, int, int] | None = None
    for row in rows:
        for bin_row in row["post_q_bins"]:
            candidate = (
                float(bin_row["coherent"]["normalized_abs"]),
                int(row["a"]),
                int(bin_row["index"]),
            )
            if worst_bin is None or candidate > worst_bin:
                worst_bin = candidate

    def spectral_moments(values: Iterable[float]) -> dict[str, object]:
        samples = tuple(float(value) for value in values)
        maximum = max(samples, default=0.0)
        moments: dict[str, float] = {}
        for order in (2, 4, 6, 8):
            mean = sum(value**order for value in samples) / len(samples)
            moments[str(order)] = mean ** (1.0 / order)
        return {
            "maximum": maximum,
            "root_mean_powers": moments,
            "maximum_over_rms": maximum / max(moments["2"], 1e-300),
        }

    post_spectrum = spectral_moments(
        float(row["post_q"]["coherent"]["normalized_abs"]) for row in rows
    )
    final_spectrum = spectral_moments(
        float(row["final_normalized_abs"]) for row in rows
    )

    return {
        "schema": SCHEMA,
        "lo": lo,
        "hi": hi,
        "length": hi - lo,
        "q": q,
        "numerator_count": len(candidates),
        "worst_post_q": {
            "a": worst_post["a"],
            "normalized_abs": worst_post["post_q"]["coherent"]["normalized_abs"],
            "coherent_over_energy": worst_post["post_q"]["coherent_over_energy"],
            "q_times_normalized_abs": q
            * float(worst_post["post_q"]["coherent"]["normalized_abs"]),
        },
        "worst_final": {
            "a": worst_final["a"],
            "normalized_abs": worst_final["final_normalized_abs"],
            "q_times_normalized_abs": worst_final["q_times_final_normalized_abs"],
        },
        "worst_post_q_bin": (
            None
            if worst_bin is None
            else {
                "a": worst_bin[1],
                "index": worst_bin[2],
                "normalized_abs": worst_bin[0],
            }
        ),
        "selected_numerator_moments": {
            "post_q": post_spectrum,
            "final": final_spectrum,
        },
        "rows": rows,
        "scope": (
            "finite exact SPF telescope; numerical scan only, with no "
            "asymptotic prime-distribution claim"
        ),
    }


def _parse_numerators(value: str | None) -> tuple[int, ...] | None:
    if value is None or value == "all":
        return None
    return tuple(int(item) for item in value.split(",") if item)


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--lo", type=int, default=100_000)
    result.add_argument("--hi", type=int, default=200_000)
    result.add_argument("--q", type=int, default=59)
    result.add_argument(
        "--numerators",
        help="comma-separated reduced numerators, or 'all' (default)",
    )
    result.add_argument("--output", type=Path)
    return result


def main() -> None:
    args = parser().parse_args()
    payload = analyze_modulus(
        args.lo,
        args.hi,
        args.q,
        _parse_numerators(args.numerators),
    )
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
