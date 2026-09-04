"""Exact ledgers for the mixed-``H^2`` product-large-sieve improvement.

The analytic input is the primitive multiplicative-character large sieve
applied to ``B(chi) H(chi)^2``.  This module records the exact rational
exponents, checks the finite coefficient-energy identity, and separates the
improved broad/singleton route from the unchanged parabolic curvature term.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Sequence


Q_IN_D = Fraction(33, 16)
SLICE_CAP = Fraction(5, 16)
PARABOLIC_CURVATURE = Fraction(37, 32)


@dataclass(frozen=True)
class MixedH2Ledger:
    crossover_support: Fraction
    old_mass_at_crossover: Fraction
    mixed_mass_at_crossover: Fraction
    nonprincipal_singleton: Fraction
    principal_diffuse_crossover: Fraction
    broad_singleton_trace: Fraction
    parabolic_curvature_trace: Fraction
    complete_trace: Fraction
    complete_operator: Fraction


def old_mass_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``D^(1/2) M^(1/4)`` when ``M=D^mu``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return Fraction(1, 2) + mu / 4


def mixed_h2_mass_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``q^(1/4) D^(1/2) M^(-1/4)``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return Fraction(1, 2) + Q_IN_D / 4 - mu / 4


def principal_singleton_exponent(mu: Fraction) -> Fraction:
    """Principal flat mass followed by the third-slice cap."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return mu - Fraction(3, 4)


def nonprincipal_singleton_exponent(mu: Fraction) -> Fraction:
    """Best old/mixed nonprincipal mass followed by the slice cap."""

    return SLICE_CAP + min(old_mass_exponent(mu), mixed_h2_mass_exponent(mu))


def diffuse_trace_exponent(mu: Fraction) -> Fraction:
    """Exponent of the positive diffuse bound ``D+D^3/M``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return max(Fraction(1), 3 - mu)


def broad_singleton_bin_exponent(mu: Fraction) -> Fraction:
    """Best character/diffuse exponent, excluding parabolic curvature."""

    character = max(
        Fraction(1),
        principal_singleton_exponent(mu),
        nonprincipal_singleton_exponent(mu),
    )
    return min(character, diffuse_trace_exponent(mu))


def complete_bin_exponent(mu: Fraction) -> Fraction:
    """Full exponent after restoring occupied-line parabolic curvature."""

    return max(PARABOLIC_CURVATURE, broad_singleton_bin_exponent(mu))


def mixed_h2_ledger() -> MixedH2Ledger:
    crossover = Fraction(33, 32)
    old = old_mass_exponent(crossover)
    mixed = mixed_h2_mass_exponent(crossover)
    broad = Fraction(9, 8)
    complete = PARABOLIC_CURVATURE
    return MixedH2Ledger(
        crossover_support=crossover,
        old_mass_at_crossover=old,
        mixed_mass_at_crossover=mixed,
        nonprincipal_singleton=old + SLICE_CAP,
        principal_diffuse_crossover=Fraction(15, 8),
        broad_singleton_trace=broad,
        parabolic_curvature_trace=PARABOLIC_CURVATURE,
        complete_trace=complete,
        complete_operator=complete / 4,
    )


def two_interval_product_counts(residuals: Iterable[int]) -> Counter[int]:
    """Coefficients of the ordered two-fold multiplicative convolution."""

    values = tuple(int(value) for value in residuals)
    if not values or any(value == 0 for value in values):
        raise ValueError("residuals must be nonzero and nonempty")
    return Counter(left * right for left in values for right in values)


def bh2_product_counts(
    shell_values: Sequence[int], residuals: Iterable[int]
) -> Counter[int]:
    """Return the exact coefficients of ``1_A *_times 1_I *_times 1_I``."""

    shell = tuple(int(value) for value in shell_values)
    shifts = tuple(int(value) for value in residuals)
    if not shell or any(value <= 0 for value in shell):
        raise ValueError("shell values must be positive and nonempty")
    interval_counts = two_interval_product_counts(shifts)
    result: Counter[int] = Counter()
    for value in shell:
        for product, multiplicity in interval_counts.items():
            result[value * product] += multiplicity
    return result


def bh2_square_norm(
    shell_values: Sequence[int], residuals: Iterable[int]
) -> int:
    """Compute ``sum_n |alpha_n|^2`` for the mixed-``H^2`` coefficient."""

    counts = bh2_product_counts(shell_values, residuals)
    return sum(multiplicity * multiplicity for multiplicity in counts.values())


def bh2_has_unique_shell_factor(
    shell_values: Sequence[int], residuals: Iterable[int]
) -> bool:
    """Check the sufficient structural hypotheses and exact shell uniqueness."""

    shell = tuple(int(value) for value in shell_values)
    shifts = tuple(int(value) for value in residuals)
    if not shell or not shifts:
        raise ValueError("both factors must be nonempty")
    if any(value <= 0 for value in shell) or any(value == 0 for value in shifts):
        raise ValueError("invalid shell value or residual")
    if max(abs(value) for value in shifts) ** 2 >= min(shell):
        raise ValueError("the residual product is not shorter than the shell")
    if any(
        gcd(left, right) != 1
        for index, left in enumerate(shell)
        for right in shell[index + 1 :]
    ):
        raise ValueError("distinct shell values must be pairwise coprime")

    owners: dict[int, int] = {}
    products = two_interval_product_counts(shifts)
    for shell_value in shell:
        for product in products:
            combined = shell_value * product
            previous = owners.setdefault(combined, shell_value)
            if previous != shell_value:
                return False
    return True

