"""Exact finite identities for the selected twisted cousin-prime sector.

The routines in this module are diagnostics, not asymptotic prime theorems.
They keep the selected modulus and frequency fixed, expose the additive
zero/diagonal modes, and verify the exact one-step Buchstab bilinearization.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction

from prime_gap_sieve_deletion import smallest_prime_factors


def character_mod_four(value: int) -> int:
    """Return the real primitive character modulo four."""

    residue = value % 4
    if residue == 1:
        return 1
    if residue == 3:
        return -1
    return 0


def additive_character(numerator: int, denominator: int, value: int) -> complex:
    return cmath.exp(2j * math.pi * numerator * value / denominator)


def cousin_lower_endpoints(lo: int, hi: int) -> list[int]:
    """Lower endpoints p for which p and p+4 are prime and lie in [lo, hi]."""

    if lo > hi - 4:
        return []
    spf = smallest_prime_factors(hi)
    return [
        value
        for value in range(max(2, lo), hi - 3)
        if spf[value] == value and spf[value + 4] == value + 4
    ]


def residue_counts(values: list[int], modulus: int) -> list[int]:
    counts = [0] * modulus
    for value in values:
        counts[value % modulus] += 1
    return counts


def cyclic_correlation(values: list[int]) -> list[int]:
    modulus = len(values)
    return [
        sum(values[r] * values[(r + shift) % modulus] for r in range(modulus))
        for shift in range(modulus)
    ]


@dataclass(frozen=True)
class SelectedDispersionAudit:
    lo: int
    hi: int
    modulus: int
    numerator: int
    pair_count: int
    twisted_sum: complex
    additive_sum: complex
    selected_square_from_differences: complex
    centered_variance: Fraction
    centered_variance_from_q_shifts: Fraction
    centered_additive_energy: Fraction
    parseval_second_lhs: float
    parseval_second_rhs: float
    parseval_fourth_lhs: float
    parseval_fourth_rhs: float
    positive_q_shift_pairs: int


def selected_dispersion_audit(lo: int, hi: int, modulus: int) -> SelectedDispersionAudit:
    """Compute every exact selected-q identity for one physical interval."""

    if modulus <= 4 or modulus % 4 != 3:
        raise ValueError("modulus must be >4 and congruent to 3 modulo 4")
    numerator = (modulus + 1) // 4
    if math.gcd(numerator, modulus) != 1:
        raise AssertionError("the near-quarter numerator must be reduced")

    pairs = cousin_lower_endpoints(lo, hi)
    count = len(pairs)
    counts = residue_counts(pairs, modulus)
    additive_sum = sum(
        additive_character(numerator, modulus, value) for value in pairs
    )
    twisted_sum = sum(
        character_mod_four(value)
        * cmath.exp(2j * math.pi * value / (4 * modulus))
        for value in pairs
    )

    # |sum e_q(ap)|^2, grouped by the literal integer difference p-p'.
    selected_square_from_differences = sum(
        additive_character(numerator, modulus, left - right)
        for left in pairs
        for right in pairs
    )

    centered_variance = sum(
        (Fraction(value, 1) - Fraction(count, modulus)) ** 2 for value in counts
    )
    positive_q_shift_pairs = sum(
        1
        for index, left in enumerate(pairs)
        for right in pairs[index + 1 :]
        if (right - left) % modulus == 0
    )
    centered_variance_from_q_shifts = (
        Fraction(count, 1)
        - Fraction(count * count, modulus)
        + 2 * positive_q_shift_pairs
    )

    transforms = [
        sum(
            value * additive_character(frequency, modulus, residue)
            for residue, value in enumerate(counts)
        )
        for frequency in range(modulus)
    ]
    parseval_second_lhs = sum(abs(value) ** 2 for value in transforms[1:])
    parseval_second_rhs = float(modulus * centered_variance)

    correlation = cyclic_correlation(counts)
    centered_energy = sum(
        (Fraction(value, 1) - Fraction(count * count, modulus)) ** 2
        for value in correlation
    )
    parseval_fourth_lhs = sum(abs(value) ** 4 for value in transforms[1:])
    parseval_fourth_rhs = float(modulus * centered_energy)

    return SelectedDispersionAudit(
        lo=lo,
        hi=hi,
        modulus=modulus,
        numerator=numerator,
        pair_count=count,
        twisted_sum=twisted_sum,
        additive_sum=additive_sum,
        selected_square_from_differences=selected_square_from_differences,
        centered_variance=centered_variance,
        centered_variance_from_q_shifts=centered_variance_from_q_shifts,
        centered_additive_energy=centered_energy,
        parseval_second_lhs=parseval_second_lhs,
        parseval_second_rhs=parseval_second_rhs,
        parseval_fourth_lhs=parseval_fourth_lhs,
        parseval_fourth_rhs=parseval_fourth_rhs,
        positive_q_shift_pairs=positive_q_shift_pairs,
    )


def least_prime_factor(value: int, spf: list[int]) -> int:
    if value <= 1:
        return math.inf  # type: ignore[return-value]
    return spf[value]


@dataclass(frozen=True)
class BuchstabAudit:
    lo: int
    hi: int
    modulus: int
    cutoff: int
    direct: complex
    rough_term: complex
    subtraction_term: complex
    transformed_bilinear_term: complex
    subtraction_rows: int


def buchstab_bilinear_audit(
    lo: int, hi: int, modulus: int, cutoff: int
) -> BuchstabAudit:
    """Verify the exact one-step Buchstab split of the second prime condition.

    The split uses P^-(n+4)>=cutoff.  Every composite surviving this roughness
    condition is removed exactly once, at its least prime factor r.  Since r
    and m=(n+4)/r are odd, chi_4(rm-4)=chi_4(r)chi_4(m), which exposes the
    bilinear phase e(rm/(4q)) without separating the shifted-prime condition
    rm-4 prime.
    """

    if modulus <= 4 or modulus % 4 != 3:
        raise ValueError("modulus must be >4 and congruent to 3 modulo 4")
    if cutoff < 3:
        raise ValueError("use an odd-prime Buchstab cutoff of at least 3")

    spf = smallest_prime_factors(hi + 4)
    primes = [value for value in range(2, hi + 5) if spf[value] == value]
    prime_set = set(primes)

    def weight(value: int) -> complex:
        return character_mod_four(value) * cmath.exp(
            2j * math.pi * value / (4 * modulus)
        )

    direct = 0j
    rough_term = 0j
    subtraction = 0j
    transformed = 0j
    rows = 0
    for n in range(max(2, lo), hi - 3):
        if n not in prime_set:
            continue
        target = n + 4
        direct += weight(n) * int(target in prime_set)
        if least_prime_factor(target, spf) >= cutoff:
            rough_term += weight(n)
        for r in primes:
            if r < cutoff:
                continue
            if r * r > target:
                break
            if target % r:
                continue
            m = target // r
            if least_prime_factor(m, spf) < r:
                continue
            rows += 1
            subtraction += weight(n)
            transformed += (
                cmath.exp(-2j * math.pi / modulus)
                * character_mod_four(r)
                * character_mod_four(m)
                * cmath.exp(2j * math.pi * r * m / (4 * modulus))
            )

    return BuchstabAudit(
        lo=lo,
        hi=hi,
        modulus=modulus,
        cutoff=cutoff,
        direct=direct,
        rough_term=rough_term,
        subtraction_term=subtraction,
        transformed_bilinear_term=transformed,
        subtraction_rows=rows,
    )


@dataclass(frozen=True)
class BilinearCauchyAudit:
    direct_form: complex
    cauchy_energy: float
    expanded_energy: complex
    diagonal_zero_mode: int
    outer_rows: int


@dataclass(frozen=True)
class EndpointParityCountermodel:
    lo: int
    modulus: int
    residue_mod_twelve: int
    support_size: int
    twisted_sum: complex
    arc_width_radians: float
    geometric_lower_bound: float


def endpoint_parity_countermodel(
    lo: int, modulus: int
) -> EndpointParityCountermodel:
    """A locally admissible, non-prime countermodel for coefficient-blind bounds.

    On an interval of diameter below q, retain every n=1 (mod 12).  Then n and
    n+4 avoid 2 and 3, chi_4(n)=1, and the slow phases e(n/(4q)) occupy an arc
    shorter than pi/2.  This is not a sieve-axiom counterexample for the actual
    primes; it only proves that local admissibility, total mass, and the L2
    diagonal do not force selected-frequency cancellation.
    """

    if modulus <= 4 or modulus % 4 != 3:
        raise ValueError("modulus must be >4 and congruent to 3 modulo 4")
    values = [
        value
        for value in range(lo, lo + modulus)
        if value % 12 == 1
    ]
    phases = [2 * math.pi * value / (4 * modulus) for value in values]
    width = max(phases) - min(phases) if phases else 0.0
    twisted = sum(cmath.exp(1j * phase) for phase in phases)
    lower = len(values) * math.cos(width / 2)
    return EndpointParityCountermodel(
        lo=lo,
        modulus=modulus,
        residue_mod_twelve=1,
        support_size=len(values),
        twisted_sum=twisted,
        arc_width_radians=width,
        geometric_lower_bound=lower,
    )


def buchstab_sector_cauchy_audit(
    lo: int,
    hi: int,
    modulus: int,
    cutoff: int,
    r_lo: int,
    r_hi: int,
) -> BilinearCauchyAudit:
    """Expand the first Cauchy energy of one exact Buchstab r-sector."""

    spf = smallest_prime_factors(hi + 4)
    primes = [value for value in range(2, hi + 5) if spf[value] == value]
    prime_set = set(primes)
    rows: dict[int, list[int]] = {}
    for r in primes:
        if r < max(cutoff, r_lo) or r >= r_hi:
            continue
        entries: list[int] = []
        m_start = max(r, (lo + 4 + r - 1) // r)
        m_stop = (hi + 3) // r
        for m in range(m_start, m_stop + 1):
            n = r * m - 4
            if n < lo or n + 4 > hi:
                continue
            if n not in prime_set or least_prime_factor(m, spf) < r:
                continue
            entries.append(m)
        if entries:
            rows[r] = entries

    inner: dict[int, complex] = {}
    for r, entries in rows.items():
        inner[r] = sum(
            character_mod_four(m)
            * cmath.exp(2j * math.pi * r * m / (4 * modulus))
            for m in entries
        )
    direct_form = sum(character_mod_four(r) * value for r, value in inner.items())
    cauchy_energy = sum(abs(value) ** 2 for value in inner.values())
    expanded = 0j
    diagonal = 0
    for r, entries in rows.items():
        for left in entries:
            for right in entries:
                expanded += (
                    character_mod_four(left)
                    * character_mod_four(right)
                    * cmath.exp(2j * math.pi * r * (left - right) / (4 * modulus))
                )
                diagonal += int(left == right)

    return BilinearCauchyAudit(
        direct_form=direct_form,
        cauchy_energy=cauchy_energy,
        expanded_energy=expanded,
        diagonal_zero_mode=diagonal,
        outer_rows=len(rows),
    )
