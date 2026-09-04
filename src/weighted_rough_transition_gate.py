#!/usr/bin/env python3
"""Exact weighted rough-transition residue gate.

The post-``q`` SPF telescope has a canonical simultaneous-stage form.  Just
before the prime ``p`` stage the active integers are ``p``-rough; removing
the integers with smallest prime factor ``p`` leaves the next-prime-rough
set.  On every component between two surviving endpoints, the difference of
the two trapezoid rules is a signed measure of total mass zero.  Reducing
that measure modulo ``q`` and taking a finite Fourier transform recovers the
stage charge exactly.

This module checks three things used by the companion report:

* deleting all multiples of an arbitrary selected integer ``q`` first does
  not change any later SPF stage ``p>q``;
* the component transport formula and its finite-group L2/L4 identities are
  exact on a finite shell; and
* the elementary linear-sieve parameter for an unweighted centre ``x=pm``
  in one residue class is ``s=(1-u-b)/u`` when ``p=Y^u`` and ``q=Y^b``.

The code does not assert the missing asymptotic residue-dispersion theorem.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable

from prime_gap_sieve_deletion import smallest_prime_factors


SCHEMA = "zeta23.weighted-rough-transition-gate.v1"

B_MIN = Fraction(1537, 10_000)
# Exact shortest curvature-block exponent at the top legal aperture.
B_MAX = Fraction(33, 133)
THETA_GT = Fraction(797, 5000)
KAPPA_MAX = Fraction(1_974_048_259, 100_000_000_000)


def linear_sieve_frontier(b: Fraction, u: Fraction | None = None) -> dict[str, object]:
    """Return the exact one-residue linear-sieve frontier.

    For ``x=pm`` with ``p=Y^u`` and ``q=Y^b``, the cofactor progression has
    length ``Y^(1-u-b)``.  Taking the largest elementary sieve level gives
    ``s=log(D)/log(p)=(1-u-b)/u``.  A dimension-one lower linear sieve has a
    positive main term only for ``s>2``; the usual upper-sieve range starts
    at ``s>1``.  Fixed ``b,u`` make ``s`` fixed, so the fundamental lemma
    cannot by itself produce a ``Y^-delta`` relative discrepancy.
    """

    if not 0 < b < 1:
        raise ValueError("b must lie in (0,1)")
    if u is None:
        u = b
    if not 0 < u < 1 - b:
        raise ValueError("u must lie in (0,1-b)")

    progression_length = 1 - u - b
    s = progression_length / u
    lower_threshold = (1 - b) / 3
    upper_threshold = (1 - b) / 2
    return {
        "b": str(b),
        "u": str(u),
        "cofactor_progression_exponent": str(progression_length),
        "s": str(s),
        "lower_sieve_positive": s > 2,
        "upper_sieve_nontrivial": s > 1,
        "lower_u_threshold": str(lower_threshold),
        "upper_u_threshold": str(upper_threshold),
        "fixed_s_gives_power_discrepancy": False,
        "decimal": {
            "b": float(b),
            "u": float(u),
            "s": float(s),
            "lower_u_threshold": float(lower_threshold),
            "upper_u_threshold": float(upper_threshold),
        },
    }


def localized_sieve_parameter(h: Fraction, b: Fraction, u: Fraction) -> Fraction:
    """Return the per-block cofactor sieve parameter ``(h-u-b)/u``.

    A block of length ``H=Y^h`` leaves only ``H/(pq)=Y^(h-u-b)``
    cofactor candidates after fixing ``p=Y^u`` and one residue modulo
    ``q=Y^b``.  A nonpositive value means that even the first elementary
    remainder-summing level is unavailable before averaging in ``p`` or in
    the blocks.
    """

    if min(h, b, u) <= 0:
        raise ValueError("h, b and u must be positive")
    return (h - u - b) / u


def closure_exponent_ledger(
    kappa: Fraction = KAPPA_MAX,
    delta: Fraction = Fraction(1, 10_000),
) -> dict[str, object]:
    """Check the selector-stable L2 and L4 closing exponents.

    If the weighted L2 residue energy is ``Y^(1-2*kappa-2*delta)``, weighted
    Cauchy over physical blocks outputs ``Y^(1-kappa-delta)``.  If the
    correlation energy in the exact fourth-moment identity is
    ``Y^(1-4*kappa-4*delta)``, weighted Holder gives the same output.
    """

    if kappa <= 0 or delta <= 0:
        raise ValueError("kappa and delta must be positive")
    l2_input = 1 - 2 * kappa - 2 * delta
    l2_output = Fraction(1, 2) + l2_input / 2
    l4_input = 1 - 4 * kappa - 4 * delta
    l4_output = Fraction(3, 4) + l4_input / 4
    target = 1 - kappa - delta
    coefficient_blind_input = 1 + THETA_GT
    l2_current_deficit = THETA_GT + 2 * kappa
    l4_current_deficit = THETA_GT + 4 * kappa
    l2_near_linear_deficit = 2 * kappa
    l4_near_linear_deficit = 4 * kappa
    assert l2_output == target
    assert l4_output == target
    assert coefficient_blind_input - (1 - 2 * kappa) == l2_current_deficit
    assert coefficient_blind_input - (1 - 4 * kappa) == l4_current_deficit
    return {
        "kappa": str(kappa),
        "delta": str(delta),
        "l2_input_exponent": str(l2_input),
        "l2_output_exponent": str(l2_output),
        "l4_input_exponent": str(l4_input),
        "l4_output_exponent": str(l4_output),
        "target_exponent": str(target),
        "coefficient_blind_full_tail_input_exponent": str(
            coefficient_blind_input
        ),
        "l2_current_deficit_at_delta_zero": str(l2_current_deficit),
        "l4_current_deficit_at_delta_zero": str(l4_current_deficit),
        "l2_near_linear_deficit_at_delta_zero": str(l2_near_linear_deficit),
        "l4_near_linear_deficit_at_delta_zero": str(l4_near_linear_deficit),
        "decimal": {
            "kappa": float(kappa),
            "delta": float(delta),
            "l2_input": float(l2_input),
            "l4_input": float(l4_input),
            "target": float(target),
            "coefficient_blind_full_tail_input": float(coefficient_blind_input),
            "l2_current_deficit_at_delta_zero": float(l2_current_deficit),
            "l4_current_deficit_at_delta_zero": float(l4_current_deficit),
            "l2_near_linear_deficit_at_delta_zero": float(
                l2_near_linear_deficit
            ),
            "l4_near_linear_deficit_at_delta_zero": float(
                l4_near_linear_deficit
            ),
        },
    }


def _zero(q: int) -> list[int]:
    return [0] * q


def twice_trapezoid_mass(active: Iterable[int], q: int) -> list[int]:
    """Return twice the endpoint mass vector of the trapezoid rule."""

    points = list(active)
    result = _zero(q)
    for left, right in zip(points, points[1:]):
        gap = right - left
        result[left % q] += gap
        result[right % q] += gap
    return result


@dataclass(frozen=True)
class StageVectors:
    """Twice-mass vectors for one simultaneous deletion stage."""

    delta: tuple[int, ...]
    positive: tuple[int, ...]
    negative: tuple[int, ...]
    deleted: int
    components: int


def simultaneous_stage_vectors(
    active: Iterable[int], deleted: Iterable[int], q: int
) -> StageVectors:
    """Compute the exact component transport vector for one stage.

    A maximal deleted run ``x_1<...<x_k`` between surviving endpoints
    ``l<r`` contributes, in twice-mass normalization,

    ``(r-x_1) delta_l + (x_k-l) delta_r
       - sum_j (x_{j+1}-x_{j-1}) delta_{x_j}``,

    where ``x_0=l`` and ``x_{k+1}=r``.
    """

    points = list(active)
    if points != sorted(set(points)):
        raise ValueError("active points must be strictly increasing")
    deleted_set = set(deleted)
    if points and (points[0] in deleted_set or points[-1] in deleted_set):
        raise ValueError("the two barrier endpoints must survive")
    if not deleted_set.issubset(points):
        raise ValueError("deleted points must be active")

    positive = _zero(q)
    negative = _zero(q)
    components = 0
    index = 0
    while index < len(points):
        if points[index] not in deleted_set:
            index += 1
            continue
        start = index
        while index < len(points) and points[index] in deleted_set:
            index += 1
        stop = index
        if start == 0 or stop == len(points):
            raise AssertionError("deleted component lacks surviving barriers")
        left = points[start - 1]
        right = points[stop]
        run = points[start:stop]
        positive[left % q] += right - run[0]
        positive[right % q] += run[-1] - left
        augmented = [left, *run, right]
        for j, centre in enumerate(run, start=1):
            negative[centre % q] += augmented[j + 1] - augmented[j - 1]
        components += 1

    delta = [plus - minus for plus, minus in zip(positive, negative)]
    survivors = [point for point in points if point not in deleted_set]
    before = twice_trapezoid_mass(points, q)
    after = twice_trapezoid_mass(survivors, q)
    direct = [new - old for new, old in zip(after, before)]
    if delta != direct:
        raise AssertionError("component transport formula failed")
    if sum(positive) != sum(negative) or sum(delta) != 0:
        raise AssertionError("transport mass balance failed")
    return StageVectors(
        delta=tuple(delta),
        positive=tuple(positive),
        negative=tuple(negative),
        deleted=len(deleted_set),
        components=components,
    )


def _fourier(vector: Iterable[int], a: int) -> complex:
    values = list(vector)
    q = len(values)
    return 0.5 * sum(
        value * cmath.exp(2j * math.pi * a * residue / q)
        for residue, value in enumerate(values)
    )


def _correlation(vector: list[int]) -> list[int]:
    q = len(vector)
    return [
        sum(vector[r] * vector[(r + shift) % q] for r in range(q))
        for shift in range(q)
    ]


def finite_post_q_audit(
    *, lo: int = 211, hi: int = 1999, q: int = 12, band_lo: int = 13, band_hi: int = 43
) -> dict[str, object]:
    """Audit q-first invariance and finite Fourier identities on a shell."""

    if not (2 <= q < band_lo < band_hi < lo < hi):
        raise ValueError("require 2<=q<band_lo<band_hi<lo<hi")
    spf = smallest_prime_factors(hi)
    if spf[lo] != lo or spf[hi] != hi:
        raise ValueError("lo and hi must be prime barrier endpoints")

    labels = sorted(
        {
            spf[value]
            for value in range(lo + 1, hi)
            if spf[value] != value
        }
    )
    natural = list(range(lo, hi + 1))
    q_first = [
        value
        for value in natural
        if value in (lo, hi) or value % q != 0
    ]
    post_q_active_mismatches = 0
    post_q_stage_mismatches = 0
    aggregate = _zero(q)
    aggregate_positive = _zero(q)
    aggregate_negative = _zero(q)
    band_deleted = 0
    band_components = 0
    band_before: list[int] | None = None
    band_after: list[int] | None = None

    for prime in labels:
        if prime > q and natural != q_first:
            post_q_active_mismatches += 1
        natural_deleted = [
            value
            for value in natural[1:-1]
            if spf[value] == prime
        ]
        q_first_deleted = [
            value
            for value in q_first[1:-1]
            if spf[value] == prime
        ]
        natural_stage = simultaneous_stage_vectors(natural, natural_deleted, q)
        q_first_stage = simultaneous_stage_vectors(q_first, q_first_deleted, q)
        if prime > q and natural_stage.delta != q_first_stage.delta:
            post_q_stage_mismatches += 1

        if band_lo < prime <= band_hi:
            if band_before is None:
                band_before = twice_trapezoid_mass(natural, q)
            for target, source in (
                (aggregate, natural_stage.delta),
                (aggregate_positive, natural_stage.positive),
                (aggregate_negative, natural_stage.negative),
            ):
                for residue, value in enumerate(source):
                    target[residue] += value
            band_deleted += natural_stage.deleted
            band_components += natural_stage.components

        natural_deleted_set = set(natural_deleted)
        q_first_deleted_set = set(q_first_deleted)
        natural = [value for value in natural if value not in natural_deleted_set]
        q_first = [value for value in q_first if value not in q_first_deleted_set]
        if band_lo < prime <= band_hi:
            band_after = twice_trapezoid_mass(natural, q)

    transforms = [_fourier(aggregate, a) for a in range(q)]
    correlation = _correlation(aggregate)
    sum_fourier_2 = sum(abs(value) ** 2 for value in transforms)
    sum_fourier_4 = sum(abs(value) ** 4 for value in transforms)
    parseval_2 = q * sum(value * value for value in aggregate) / 4.0
    parseval_4 = q * sum(value * value for value in correlation) / 16.0
    scale_2 = max(1.0, parseval_2)
    scale_4 = max(1.0, parseval_4)

    if post_q_active_mismatches or post_q_stage_mismatches:
        raise AssertionError("q-first flow changed a stage p>q")
    if aggregate != [p - n for p, n in zip(aggregate_positive, aggregate_negative)]:
        raise AssertionError("band positive/negative decomposition failed")
    if band_before is None or band_after is None:
        raise AssertionError("finite shell contains no stage in the requested band")
    telescoped = [new - old for new, old in zip(band_after, band_before)]
    if aggregate != telescoped:
        raise AssertionError("dyadic rough-stage telescope failed")
    if sum(aggregate_positive) != sum(aggregate_negative):
        raise AssertionError("band transport masses differ")
    if abs(sum_fourier_2 - parseval_2) > 1e-9 * scale_2:
        raise AssertionError("finite Parseval identity failed")
    if abs(sum_fourier_4 - parseval_4) > 2e-9 * scale_4:
        raise AssertionError("finite fourth-moment identity failed")

    return {
        "schema": SCHEMA,
        "parameters": {
            "lo": lo,
            "hi": hi,
            "q": q,
            "band_lo": band_lo,
            "band_hi": band_hi,
        },
        "band": {
            "deleted_centres": band_deleted,
            "deleted_components": band_components,
            "twice_positive_mass": sum(aggregate_positive),
            "twice_negative_mass": sum(aggregate_negative),
            "delta_mass": sum(aggregate),
            "nonzero_residue_coordinates": sum(value != 0 for value in aggregate),
        },
        "fourier": {
            "parseval_second_error": abs(sum_fourier_2 - parseval_2),
            "parseval_fourth_error": abs(sum_fourier_4 - parseval_4),
            "maximum_nonzero_coefficient": max(
                (abs(value) for value in transforms[1:]), default=0.0
            ),
        },
        "certificates": {
            "q_first_active_sets_identical_for_every_p_gt_q": True,
            "q_first_stage_vectors_identical_for_every_p_gt_q": True,
            "component_transport_exact": True,
            "dyadic_band_telescopes_before_inequalities": True,
            "positive_negative_masses_equal": True,
            "band_vector_has_mass_zero": sum(aggregate) == 0,
            "finite_parseval_exact": abs(sum_fourier_2 - parseval_2) <= 1e-9 * scale_2,
            "finite_fourth_moment_exact": abs(sum_fourier_4 - parseval_4) <= 2e-9 * scale_4,
        },
        "scope": (
            "exact finite weighted rough-transition and Fourier audit; "
            "no asymptotic residue-dispersion estimate"
        ),
    }


def full_ledger() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "sieve_frontier": {
            "bottom": linear_sieve_frontier(B_MIN),
            "top": linear_sieve_frontier(B_MAX),
            "critical_block_bottom": str(
                localized_sieve_parameter(B_MAX, B_MIN, B_MIN)
            ),
            "critical_block_top": str(
                localized_sieve_parameter(B_MAX, B_MAX, B_MAX)
            ),
        },
        "closure": closure_exponent_ledger(),
        "finite_audit": finite_post_q_audit(),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(full_ledger(), indent=2, sort_keys=True))
