#!/usr/bin/env python3
"""Dyadic SPF-tail square-function gate and coherent deletion model.

The analytic part of the companion report is elementary.  If a fixed base
set ``B`` is thinned simultaneously and its deleted centres are partitioned
by labels ``p``, split the positive transport from each deleted Voronoi cell
according to its label.  For ``|f| = 1`` this gives

    |R_p(f)|^2 <= N_p * sum_{x labelled p} (g_-(x) + g_+(x))^2.

Summing the incident gap squares costs at most four times ``G_2(B)``.  With
the upper-sieve count ``N_p << Y/(p log p)`` and the new rough-gap estimate,
this proves a dyadic square-function bound of order ``Y^(2+o(1))/P``.  The
number of primes in the band is ``P^(1+o(1))``, so Cauchy across the labels
returns the critical order ``Y^(1+o(1))``.

This module checks the exponent ledger and constructs a deliberately scoped
finite obstruction.  It is an exact simultaneous deletion from an integer
lattice; every deleted centre is nonzero modulo q, is divisible by its prime
label, respects an upper-sieve-shaped per-label cap, and the gap square is
``Y log(P)`` scale.  The labels are phase-selected, so their charges cohere.
The model is NOT claimed to be the actual set of P-rough integers: it shows
only that deletion algebra, gap energy, divisibility caps, and pointwise
nonresonance do not imply the missing residue-dispersion theorem.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from collections import Counter
from fractions import Fraction
from typing import Iterable


SCHEMA = "zeta23.spf-tail-large-sieve-gate.v1"


def primes_up_to(limit: int) -> list[int]:
    """Return all primes at most ``limit`` by a deterministic sieve."""

    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if not sieve[p]:
            continue
        start = p * p
        sieve[start : limit + 1 : p] = b"\x00" * (
            (limit - start) // p + 1
        )
    return [n for n in range(2, limit + 1) if sieve[n]]


def is_prime(value: int) -> bool:
    """Trial-division primality check for the small model parameters."""

    if value < 2:
        return False
    for p in primes_up_to(math.isqrt(value)):
        if value % p == 0:
            return value == p
    return True


def exponent_ledger(
    b: Fraction = Fraction(799, 5000),
    kappa: Fraction = Fraction(1974048259, 100000000000),
    band_exponent: Fraction | None = None,
) -> dict[str, object]:
    """Return the exact power ledger for a band ``P=Y^c``.

    Logarithms are recorded as ``o(1)``.  The proved square-function exponent
    is ``2-c``.  Cauchy over ``P^(1+o(1))`` labels returns exponent one, while
    a target ``Y^(1-kappa)`` would require energy exponent
    ``2-c-2*kappa``.
    """

    c = b if band_exponent is None else band_exponent
    energy = 2 - c
    required_energy = 2 - c - 2 * kappa
    aggregate_squared = c + energy
    assert aggregate_squared == 2
    assert energy - required_energy == 2 * kappa
    return {
        "q_exponent_b": str(b),
        "band_exponent_c": str(c),
        "carrier_kappa": str(kappa),
        "new_rough_gap_exponent": "1+o(1)",
        "per_label_count_exponent": str(1 - c),
        "proved_square_function_exponent": str(energy),
        "number_of_labels_exponent": str(c),
        "cauchy_aggregate_exponent": "1",
        "required_square_function_exponent": str(required_energy),
        "fixed_power_energy_deficit": str(2 * kappa),
        "decimal": {
            "b": float(b),
            "c": float(c),
            "kappa": float(kappa),
            "proved_square_function": float(energy),
            "required_square_function": float(required_energy),
            "energy_deficit": float(2 * kappa),
        },
    }


def _trapezoid(
    active: Iterable[int], values: list[complex], spacing: int
) -> complex:
    points = iter(active)
    try:
        left = next(points)
    except StopIteration:
        return 0j
    total = 0j
    for right in points:
        total += 0.5 * (right - left) * spacing * (
            values[left] + values[right]
        )
        left = right
    return total


def build_countermodel(
    *,
    q: int = 1019,
    p_floor: int = 2039,
    spacing: int = 10,
    gap_count: int = 200_000,
    x0: int = 1,
    arc_half_angle: float = math.pi / 6,
    cap_constant: float = 8.0,
) -> dict[str, object]:
    """Build and verify an exact coherent simultaneous-deletion model.

    ``q`` must be prime and 3 modulo 4.  The selected numerator is
    ``a=(q+1)/4``.  Taking ``spacing=2 mod 4`` makes the symmetric deletion
    multiplier close to ``-2*spacing``.  Deleted lattice indices are even,
    hence no two are adjacent.  A centre is labelled by its least prime
    divisor *inside* ``(p_floor, 2*p_floor]``.
    """

    if not is_prime(q) or q % 4 != 3:
        raise ValueError("q must be prime and congruent to 3 modulo 4")
    if spacing <= 0 or spacing % 4 != 2:
        raise ValueError("spacing must be positive and congruent to 2 mod 4")
    if math.gcd(spacing, q) != 1:
        raise ValueError("spacing must be coprime to q")
    if p_floor <= q:
        raise ValueError("the prime-label band must lie after q")
    if gap_count < 100:
        raise ValueError("gap_count is too small for the diagnostic")
    if not (0 < arc_half_angle < math.pi / 2):
        raise ValueError("arc_half_angle must lie in (0,pi/2)")

    band = [p for p in primes_up_to(2 * p_floor) if p_floor < p <= 2 * p_floor]
    if not band:
        raise ValueError("empty prime-label band")

    # Mark the least divisor in the dyadic band at every lattice node.  This
    # takes sum_p gap_count/p operations, not gap_count times #band.
    least_band_divisor = [0] * (gap_count + 1)
    for p in band:
        if math.gcd(spacing, p) != 1:
            continue
        first = (-x0 * pow(spacing, -1, p)) % p
        for index in range(first, gap_count + 1, p):
            if least_band_divisor[index] == 0:
                least_band_divisor[index] = p

    a = (q + 1) // 4
    theta = 2.0 * math.pi * a / q
    arc_cos = math.cos(arc_half_angle)
    length = gap_count * spacing
    candidates: dict[int, list[int]] = {p: [] for p in band}
    for index in range(2, gap_count - 1, 2):
        p = least_band_divisor[index]
        if p == 0:
            continue
        x = x0 + index * spacing
        residue = x % q
        if residue == 0:
            continue
        phase = cmath.exp(2j * math.pi * ((a * residue) % q) / q)
        if phase.real >= arc_cos:
            candidates[p].append(index)

    selected_by_prime: dict[int, list[int]] = {}
    cap_violations = 0
    for p in band:
        cap = max(1, math.floor(cap_constant * length / (p * math.log(p_floor))))
        chosen = candidates[p][:cap]
        if len(chosen) > cap:
            cap_violations += 1
        if chosen:
            selected_by_prime[p] = chosen

    selected = sorted(index for row in selected_by_prime.values() for index in row)
    if not selected:
        raise AssertionError("model selected no centres")
    if any(right - left < 2 for left, right in zip(selected, selected[1:])):
        raise AssertionError("selected deletions are adjacent")

    values = [
        cmath.exp(2j * math.pi * ((a * ((x0 + j * spacing) % q)) % q) / q)
        for j in range(gap_count + 1)
    ]
    before = _trapezoid(range(gap_count + 1), values, spacing)
    selected_set = set(selected)
    active_after = (j for j in range(gap_count + 1) if j not in selected_set)
    after = _trapezoid(active_after, values, spacing)

    multiplier = spacing * (math.cos(theta * spacing) - 1.0)
    stage_charges: dict[int, complex] = {}
    divisibility_violations = 0
    least_label_violations = 0
    nonresonance_violations = 0
    for p, indices in selected_by_prime.items():
        charge = 0j
        for index in indices:
            x = x0 + index * spacing
            divisibility_violations += int(x % p != 0)
            least_label_violations += int(least_band_divisor[index] != p)
            nonresonance_violations += int(x % q == 0)
            charge += multiplier * values[index]
        stage_charges[p] = charge
    aggregate = sum(stage_charges.values(), 0j)
    direct_error = abs((after - before) - aggregate)
    direct_scale = max(1.0, abs(aggregate), abs(after - before))

    initial_g2 = gap_count * spacing**2
    final_g2_formula = initial_g2 + 2 * len(selected) * spacing**2
    active_indices = [j for j in range(gap_count + 1) if j not in selected_set]
    final_g2_direct = sum(
        ((right - left) * spacing) ** 2
        for left, right in zip(active_indices, active_indices[1:])
    )

    counts = {p: len(indices) for p, indices in selected_by_prime.items()}
    cap_ratios = {
        p: count * p * math.log(p_floor) / length for p, count in counts.items()
    }
    stage_energy = sum(abs(value) ** 2 for value in stage_charges.values())
    stage_count = len(stage_charges)

    residue_counts = Counter((x0 + j * spacing) % q for j in selected)
    centre_fourier = sum(
        count * cmath.exp(2j * math.pi * ((a * residue) % q) / q)
        for residue, count in residue_counts.items()
    )
    parseval_mean_square = sum(count * count for count in residue_counts.values())
    convolution = [0] * q
    nonzero_residues = list(residue_counts.items())
    for r, cr in nonzero_residues:
        for s, cs in nonzero_residues:
            convolution[(r + s) % q] += cr * cs
    parseval_mean_fourth = sum(value * value for value in convolution)

    coherent_lower_bound = abs(multiplier) * len(selected) * arc_cos
    if abs(aggregate) + 1e-9 < coherent_lower_bound:
        raise AssertionError("phase-arc coherence lower bound failed")
    if direct_error > 2e-9 * direct_scale:
        raise AssertionError("simultaneous deletion identity failed")
    if final_g2_direct != final_g2_formula:
        raise AssertionError("gap-square formula failed")
    if cap_violations or divisibility_violations or least_label_violations:
        raise AssertionError("prime-label certificate failed")
    if nonresonance_violations:
        raise AssertionError("q-nonresonance certificate failed")
    if max(cap_ratios.values()) > cap_constant + 1e-12:
        raise AssertionError("upper-sieve-shaped count cap failed")
    if abs(centre_fourier * multiplier - aggregate) > 1e-9 * direct_scale:
        raise AssertionError("residue Fourier reconstruction failed")

    return {
        "schema": SCHEMA,
        "parameters": {
            "q": q,
            "a": a,
            "p_floor": p_floor,
            "p_ceiling": 2 * p_floor,
            "spacing": spacing,
            "gap_count": gap_count,
            "length_Y": length,
            "x0": x0,
            "arc_half_angle": arc_half_angle,
            "cap_constant": cap_constant,
        },
        "counts": {
            "prime_labels_in_band": len(band),
            "nonempty_prime_labels": stage_count,
            "deleted_centres": len(selected),
            "distinct_deleted_residues": len(residue_counts),
            "max_cap_ratio": max(cap_ratios.values()),
            "deleted_count_times_logP_squared_over_Y": (
                len(selected) * math.log(p_floor) ** 2 / length
            ),
        },
        "exact_deletion": {
            "before": [before.real, before.imag],
            "after": [after.real, after.imag],
            "aggregate": [aggregate.real, aggregate.imag],
            "aggregate_abs": abs(aggregate),
            "direct_identity_error": direct_error,
            "symmetric_multiplier": multiplier,
            "coherence_lower_bound": coherent_lower_bound,
            "aggregate_times_logP_over_Y": abs(aggregate)
            * math.log(p_floor)
            / length,
        },
        "gap_energy": {
            "initial_G2": initial_g2,
            "final_G2": final_g2_direct,
            "initial_G2_over_Y": initial_g2 / length,
            "final_G2_over_Y": final_g2_direct / length,
            "generic_4_N_G2_bound": 4 * len(selected) * initial_g2,
            "aggregate_square": abs(aggregate) ** 2,
        },
        "stage_square_function": {
            "energy": stage_energy,
            "energy_times_P_logP_over_Y_squared": stage_energy
            * p_floor
            * math.log(p_floor)
            / length**2,
            "cauchy_aggregate_bound": math.sqrt(stage_count * stage_energy),
            "coherent_over_cauchy_bound": abs(aggregate)
            / math.sqrt(stage_count * stage_energy),
        },
        "finite_group_spectrum": {
            "selected_centre_fourier_abs": abs(centre_fourier),
            "parseval_rms_over_all_numerators": math.sqrt(parseval_mean_square),
            "selected_over_parseval_rms": abs(centre_fourier)
            / math.sqrt(parseval_mean_square),
            "parseval_fourth_mean_root": parseval_mean_fourth ** 0.25,
            "selected_over_fourth_mean_root": abs(centre_fourier)
            / (parseval_mean_fourth ** 0.25),
        },
        "certificates": {
            "all_deleted_centres_q_nonzero": nonresonance_violations == 0,
            "all_labels_divide_their_centres": divisibility_violations == 0,
            "labels_are_least_divisors_inside_band": least_label_violations == 0,
            "per_label_count_caps_hold": max(cap_ratios.values()) <= cap_constant,
            "deletions_are_pairwise_nonadjacent": True,
            "exact_trapezoid_identity": direct_error <= 2e-9 * direct_scale,
            "exact_gap_square_formula": final_g2_direct == final_g2_formula,
            "phase_arc_coherence": abs(aggregate) >= coherent_lower_bound - 1e-9,
            "residue_fourier_reconstruction": True,
        },
        "scope": (
            "Exact finite simultaneous-deletion obstruction to deductions from "
            "gap energy, divisibility/count caps, and q-nonresonance alone; "
            "not an asymptotic model of the actual P-rough set."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q", type=int, default=1019)
    parser.add_argument("--p-floor", type=int, default=2039)
    parser.add_argument("--spacing", type=int, default=10)
    parser.add_argument("--gap-count", type=int, default=200_000)
    args = parser.parse_args()
    payload = {
        "schema": SCHEMA,
        "exponent_ledger": exponent_ledger(),
        "countermodel": build_countermodel(
            q=args.q,
            p_floor=args.p_floor,
            spacing=args.spacing,
            gap_count=args.gap_count,
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
