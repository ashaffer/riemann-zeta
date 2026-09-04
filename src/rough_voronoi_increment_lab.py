#!/usr/bin/env python3
"""Finite lab for dyadic increments of rough Voronoi measures.

For ``R_z={n: P^-(n)>z}`` on a finite shell, let ``nu_z`` be the
endpoint-trapezoid (Voronoi) mass measure.  The post-q SPF telescope groups
exactly into increments ``nu_{2P}-nu_P``.  This program computes their exact
residue vectors modulo every requested ``q`` and reports primitive Fourier
L2/L4 moments and the worst reduced numerator.

It is deliberately a finite diagnostic.  In particular, a stable numerical
``1/q`` profile is not an asymptotic residue-dispersion theorem.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

from prime_gap_sieve_deletion import smallest_prime_factors
from spf_residue_transport import moment_ledger


SCHEMA = "zeta23.rough-voronoi-increment-lab.v1"
BETA_MIN = Fraction(1537, 10_000)
BETA_MAX = Fraction(31, 125)


def _is_prime(value: int, spf: list[int]) -> bool:
    return value >= 2 and spf[value] == value


def prime_barriers(lo: int, hi: int, spf: list[int]) -> tuple[int, int]:
    """Return prime endpoints inside ``[lo,hi]``."""

    left = next(value for value in range(lo, hi + 1) if _is_prime(value, spf))
    right = next(
        value for value in range(hi, left, -1) if _is_prime(value, spf)
    )
    return left, right


def rough_points(
    left: int, right: int, threshold: int, spf: list[int]
) -> list[int]:
    """Return points rough after every stage ``p<=threshold``.

    Thus an interior point survives exactly when ``P^-(n)>threshold``.
    The strict inequality is what makes ``nu_(2P)-nu_P`` telescope the
    stages ``P<p<=2P``, including the upper endpoint and excluding the
    lower endpoint when either cutoff happens to be prime.
    """

    if not 2 <= threshold < left:
        raise ValueError("require 2<=threshold<left")
    return [
        value
        for value in range(left, right + 1)
        if value in (left, right) or spf[value] > threshold
    ]


def twice_trapezoid_residues(points: Iterable[int], q: int) -> list[int]:
    """Return twice the endpoint-trapezoid mass vector modulo ``q``."""

    ordered = list(points)
    if ordered != sorted(set(ordered)) or len(ordered) < 2:
        raise ValueError("points must be a strictly increasing list")
    result = [0] * q
    for left, right in zip(ordered, ordered[1:]):
        gap = right - left
        result[left % q] += gap
        result[right % q] += gap
    return result


def dyadic_increment_vector(
    left: int, right: int, threshold: int, q: int, spf: list[int]
) -> tuple[list[int], int, int]:
    """Return ``2*(nu_{2P}-nu_P)`` modulo q and both set sizes."""

    coarse = rough_points(left, right, 2 * threshold, spf)
    fine = rough_points(left, right, threshold, spf)
    coarse_mass = twice_trapezoid_residues(coarse, q)
    fine_mass = twice_trapezoid_residues(fine, q)
    delta = [new - old for new, old in zip(coarse_mass, fine_mass)]
    if sum(delta) != 0:
        raise AssertionError("rough Voronoi increment must have total mass zero")
    return delta, len(fine), len(coarse)


@dataclass(frozen=True)
class Row:
    y: int
    left: int
    right: int
    q: int
    threshold: int
    fine_points: int
    coarse_points: int
    ledger: dict[str, object]

    def as_json(self) -> dict[str, object]:
        maximum = self.ledger["reduced_maximum"]
        normalized = float(maximum["normalized_abs"])
        parseval_2_scale = max(
            1.0,
            self.q * float(self.ledger["twice_mass_l2_squared"]) / 4.0,
        )
        parseval_4_scale = max(
            1.0,
            self.q * float(self.ledger["correlation_l2_squared"]) / 16.0,
        )
        exponent = (
            -math.log(normalized) / math.log(self.y) if normalized > 0 else None
        )
        return {
            "Y": self.y,
            "shell": [self.left, self.right],
            "length": self.right - self.left,
            "q": self.q,
            "threshold_P": self.threshold,
            "P_exponent": math.log(self.threshold) / math.log(self.y),
            "q_exponent": math.log(self.q) / math.log(self.y),
            "fine_points": self.fine_points,
            "coarse_points": self.coarse_points,
            "twice_mass_l1_normalized": (
                float(self.ledger["twice_mass_l1"]) / (self.right - self.left)
            ),
            "reduced_rms_normalized": self.ledger["reduced_rms_normalized"],
            "reduced_l2_envelope_normalized": self.ledger[
                "reduced_l2_envelope_normalized"
            ],
            "reduced_l4_envelope_normalized": self.ledger[
                "reduced_l4_envelope_normalized"
            ],
            "reduced_maximum": maximum,
            "empirical_max_saving_exponent": exponent,
            "certificates": {
                "zero_total_mass": self.ledger["twice_mass_sum"] == 0,
                "parseval_second": (
                    float(self.ledger["parseval_second_error"])
                    <= 1e-9 * parseval_2_scale
                ),
                "parseval_fourth": (
                    float(self.ledger["parseval_fourth_error"])
                    <= 2e-9 * parseval_4_scale
                ),
            },
        }


def analyze_row(y: int, q: int, threshold: int, spf: list[int]) -> Row:
    left, right = prime_barriers(y, 2 * y, spf)
    delta, fine_count, coarse_count = dyadic_increment_vector(
        left, right, threshold, q, spf
    )
    return Row(
        y=y,
        left=left,
        right=right,
        q=q,
        threshold=threshold,
        fine_points=fine_count,
        coarse_points=coarse_count,
        ledger=moment_ledger(delta, right - left),
    )


def _candidate_moduli(y: int, spf: list[int], exhaustive: bool) -> list[int]:
    low = max(3, math.ceil(y ** float(BETA_MIN)))
    high = max(low, math.floor(y ** float(BETA_MAX)))
    values = [q for q in range(low, high + 1) if _is_prime(q, spf)]
    if not values:
        values = [next(q for q in range(low, high + 20) if _is_prime(q, spf))]
    if exhaustive or len(values) <= 3:
        return values
    return sorted({values[0], values[len(values) // 2], values[-1]})


def _candidate_thresholds(y: int, q: int) -> list[int]:
    upper = max(q + 1, math.floor(y ** float(BETA_MAX)))
    value = max(q + 1, math.ceil(y ** float(BETA_MIN)))
    result: list[int] = []
    while value <= upper:
        result.append(value)
        value *= 2
    if not result:
        result.append(q + 1)
    return result


def analyze(scales: Iterable[int], exhaustive_q: bool = False) -> dict[str, object]:
    scales = sorted(set(scales))
    if not scales or scales[0] < 100:
        raise ValueError("all scales must be at least 100")
    spf = smallest_prime_factors(2 * scales[-1] + 100)
    rows: list[dict[str, object]] = []
    for y in scales:
        for q in _candidate_moduli(y, spf, exhaustive_q):
            for threshold in _candidate_thresholds(y, q):
                rows.append(analyze_row(y, q, threshold, spf).as_json())
    return {
        "schema": SCHEMA,
        "parameters": {
            "scales": scales,
            "beta_min": str(BETA_MIN),
            "beta_max": str(BETA_MAX),
            "exhaustive_q": exhaustive_q,
        },
        "rows": rows,
        "scope": (
            "finite whole-shell, early-band diagnostic with prime moduli for "
            "primitive Fourier moments of nu_(2P)-nu_P; Fourier fields use "
            "actual mass although the internal residue vector stores twice "
            "mass; no curvature-block, full-tail, asymptotic dispersion, or "
            "zeta-strip claim"
        ),
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument(
        "--scales", default="10000,30000,100000,300000,1000000"
    )
    result.add_argument("--exhaustive-q", action="store_true")
    result.add_argument("--output", type=Path)
    return result


def main() -> None:
    args = parser().parse_args()
    scales = [int(item) for item in args.scales.split(",") if item]
    encoded = json.dumps(
        analyze(scales, exhaustive_q=args.exhaustive_q), indent=2, sort_keys=True
    ) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
