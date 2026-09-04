"""Exact ledgers for reducing mixed reciprocal restriction to self restriction.

The only analytic input represented here is the hypothetical diagonal bound

    ||z*z||_2^2 <= (D U)^(1/2) ||z||_2^4,

for every sequence supported on the width-``U`` reciprocal strip.  Fourier
Cauchy then gives the mixed constant ``D^(1/2) (UV)^(1/4)``.  The routines
below replay the resulting Fejer exponents and a finite countermodel showing
why scalar restriction alone does not control a general pair-space tensor.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import sqrt
from typing import Sequence


def self_to_mixed_constant_exponent(
    u: Fraction, v: Fraction
) -> Fraction:
    """Power of ``D`` in ``D^(1/2)(UV)^(1/4)`` for ``U=D^u,V=D^v``."""

    return Fraction(1, 2) + (u + v) / 4


def flat_mixed_energy_exponent(u: Fraction, v: Fraction) -> Fraction:
    """Power in the flat mixed energy after ``|A_U|<=D U``.

    The mixed restriction constant is multiplied by
    ``|A_U| |A_V| <= D^2 U V``.
    """

    return Fraction(5, 2) + Fraction(5, 4) * (u + v)


def weighted_fejer_norm_exponent(u: Fraction, v: Fraction) -> Fraction:
    """Power in one weighted dyadic contribution to the convolution norm.

    Taking the square root of ``flat_mixed_energy_exponent`` and multiplying
    by the two height-one Fejer weights ``U^-2 V^-2`` gives

        D^(5/4) U^(-11/8) V^(-11/8).
    """

    return Fraction(5, 4) - Fraction(11, 8) * (u + v)


def sharp_min_weighted_norm_exponent(
    smaller: Fraction, larger: Fraction
) -> Fraction:
    """Old sharp-min RSR ledger for comparison, assuming ``smaller<=larger``."""

    if smaller > larger:
        raise ValueError("require smaller <= larger")
    return Fraction(5, 4) - Fraction(5, 4) * smaller - Fraction(3, 2) * larger


def symmetric_over_sharp_norm_gap(
    smaller: Fraction, larger: Fraction
) -> Fraction:
    """Extra ``D`` exponent paid by Fourier Cauchy: ``(larger-smaller)/8``."""

    if smaller > larger:
        raise ValueError("require smaller <= larger")
    return weighted_fejer_norm_exponent(
        smaller, larger
    ) - sharp_min_weighted_norm_exponent(smaller, larger)


def dyadic_fejer_sum(number_of_scales: int) -> float:
    """Return ``sum_{j<scales} (2^j)^(-11/8)``.

    This is the one-variable factor in the double Fejer sum.  It is uniformly
    bounded by the infinite geometric sum.
    """

    if number_of_scales < 0:
        raise ValueError("number_of_scales must be nonnegative")
    return sum(2.0 ** (-11 * j / 8) for j in range(number_of_scales))


def infinite_dyadic_fejer_sum() -> float:
    """The exact numerical value of the limiting geometric sum."""

    return 1.0 / (1.0 - 2.0 ** (-11 / 8))


def convolution_energy(left: Sequence[complex], right: Sequence[complex]) -> float:
    """Return the ordinary zero-extended convolution ``l2`` energy."""

    if not left or not right:
        return 0.0
    output = [0j] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
    return float(sum(abs(value) ** 2 for value in output))


def fourier_cauchy_ratio(left: Sequence[complex], right: Sequence[complex]) -> float:
    """Return ``E(left,right)/sqrt(E(left,left)E(right,right))``.

    Fourier Cauchy says this ratio is at most one.
    """

    mixed = convolution_energy(left, right)
    denominator = sqrt(
        convolution_energy(left, left) * convolution_energy(right, right)
    )
    return 0.0 if denominator == 0 else mixed / denominator


def additive_energy(values: Sequence[int]) -> int:
    """Ordered additive energy of a finite set represented without repeats."""

    counts = Counter(x + y for x in values for y in values)
    return sum(multiplicity * multiplicity for multiplicity in counts.values())


def sidon_nonfactorable_gap(size: int) -> tuple[Fraction, int]:
    """Return a scalar-self constant and an uncontrolled pair-block norm.

    Take ``A={1,2,4,...,2^(size-1)}`` and ``B=-A``.  Its normalized scalar
    self energy is ``(2 size^2-size)/size^2<2``.  On pair space, however, the
    completion fiber ``{(a,-a):a in A}`` has ``size`` coordinates; the
    all-ones mask on that fiber has operator norm ``size``.  This shows that
    a scalar theorem for factorable pair weights cannot, by itself, control
    a general nonfactorable pair tensor.
    """

    if size <= 0:
        raise ValueError("size must be positive")
    values = tuple(1 << j for j in range(size))
    energy = additive_energy(values)
    assert energy == 2 * size * size - size
    return Fraction(energy, size * size), size

