"""Exact ledgers for the uniform ``D^(37/32)`` four-cycle theorem.

The analytic input is the primitive multiplicative-character large sieve.
This module does not reprove that imported theorem.  It records the exact
normalizations used in its application, checks the collision-free
multiplicative convolution behind the coefficient norm, and replays every
rational exponent in the flat-bin/parabolic synthesis.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Sequence


D_IN_Q = Fraction(16, 33)
Q_IN_D = Fraction(33, 16)
SLICE_CAP = Fraction(5, 16)
PARABOLIC_CURVATURE = Fraction(37, 32)


@dataclass(frozen=True)
class UniformThirtySevenLedger:
    """Power ledger for the primitive-character large-sieve synthesis."""

    d_exponent_in_q: Fraction
    q_exponent_in_d: Fraction
    old_large_value_crossover: Fraction
    old_mass_at_crossover: Fraction
    large_sieve_mass_at_crossover: Fraction
    slice_cap: Fraction
    singleton_trace_at_crossover: Fraction
    parabolic_curvature_trace: Fraction
    principal_safe_endpoint: Fraction
    diffuse_switch: Fraction
    principal_diffuse_overlap: Fraction
    uniform_trace: Fraction
    uniform_operator: Fraction
    previous_trace: Fraction
    trace_gain: Fraction
    transverse_exponent: Fraction


def uniform_thirty_seven_ledger() -> UniformThirtySevenLedger:
    """Return all exact exponents in the ``37/32`` argument.

    If ``M=D^mu``, the old character fourth-moment mass has exponent
    ``1/2+mu/4``, while the primitive-large-sieve mass has exponent
    ``49/32-mu/2``.  They meet at ``mu=11/8`` with mass ``D^(27/32)``.
    The third-slice cap ``D^(5/16)`` raises this to ``D^(37/32)``, exactly
    the already proved occupied-line curvature exponent.
    """

    crossover = Fraction(11, 8)
    old_mass = old_character_mass_exponent(crossover)
    sieve_mass = large_sieve_mass_exponent(crossover)
    trace = Fraction(37, 32)
    principal_safe = Fraction(61, 32)
    diffuse_switch = Fraction(59, 32)
    previous = Fraction(5, 4)
    return UniformThirtySevenLedger(
        d_exponent_in_q=D_IN_Q,
        q_exponent_in_d=Q_IN_D,
        old_large_value_crossover=crossover,
        old_mass_at_crossover=old_mass,
        large_sieve_mass_at_crossover=sieve_mass,
        slice_cap=SLICE_CAP,
        singleton_trace_at_crossover=old_mass + SLICE_CAP,
        parabolic_curvature_trace=PARABOLIC_CURVATURE,
        principal_safe_endpoint=principal_safe,
        diffuse_switch=diffuse_switch,
        principal_diffuse_overlap=principal_safe - diffuse_switch,
        uniform_trace=trace,
        uniform_operator=trace / 4,
        previous_trace=previous,
        trace_gain=previous - trace,
        transverse_exponent=Fraction(1, 2) + D_IN_Q * (trace / 4),
    )


def old_character_mass_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``D^(1/2) M^(1/4)`` for ``M=D^mu``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("the support exponent must be nonnegative")
    return Fraction(1, 2) + mu / 4


def large_sieve_mass_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``sqrt(q*D/M)`` in powers of ``D``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("the support exponent must be nonnegative")
    return (Q_IN_D + 1 - mu) / 2


def principal_mass_exponent(mu: Fraction) -> Fraction:
    """Exponent of the normalized principal term ``M*D/q``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("the support exponent must be nonnegative")
    return mu + 1 - Q_IN_D


def singleton_character_trace_exponent(mu: Fraction) -> Fraction:
    """Best singleton trace exponent supplied by the two character bounds.

    The principal character and nonprincipal characters are added, so their
    exponents are combined by taking a maximum.  The common third-slice cap
    ``D^(5/16)`` is then included.
    """

    nonprincipal = min(
        old_character_mass_exponent(mu), large_sieve_mass_exponent(mu)
    )
    return SLICE_CAP + max(principal_mass_exponent(mu), nonprincipal)


def diffuse_trace_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``D + D^3/M`` for a factor-two height bin."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("the support exponent must be nonnegative")
    return max(Fraction(1), 3 - mu)


def uniform_bin_trace_exponent(mu: Fraction) -> Fraction:
    """Best complete trace exponent for one factor-two coefficient bin."""

    character_route = max(
        Fraction(1), PARABOLIC_CURVATURE, singleton_character_trace_exponent(mu)
    )
    return min(character_route, diffuse_trace_exponent(mu))


def multiplicative_convolution_counts(
    shell_values: Sequence[int], residuals: Iterable[int]
) -> Counter[int]:
    """Return coefficients of ``1_shell *_times 1_residual`` exactly."""

    values = tuple(int(value) for value in shell_values)
    shifts = tuple(int(value) for value in residuals)
    if not values or any(value <= 0 for value in values):
        raise ValueError("shell values must be positive and nonempty")
    if not shifts or any(value == 0 for value in shifts):
        raise ValueError("residuals must be nonzero and nonempty")
    return Counter(value * shift for value in values for shift in shifts)


def shell_product_convolution_is_sidon(
    shell_values: Sequence[int], residuals: Iterable[int]
) -> bool:
    """Check the exact collision-free product property used by the proof.

    A sufficient structural hypothesis is also checked: distinct shell
    values are pairwise coprime and every residual has modulus smaller than
    the least shell value.  Under it, ``b1*h1=b2*h2`` forces ``b1=b2`` and
    then ``h1=h2``.
    """

    values = tuple(int(value) for value in shell_values)
    shifts = tuple(int(value) for value in residuals)
    if not values or not shifts:
        raise ValueError("both factors must be nonempty")
    if any(value <= 0 for value in values) or any(value == 0 for value in shifts):
        raise ValueError("invalid shell value or residual")
    if max(abs(value) for value in shifts) >= min(values):
        raise ValueError("the residual interval is not shorter than the shell")
    if any(gcd(left, right) != 1 for index, left in enumerate(values) for right in values[index + 1 :]):
        raise ValueError("distinct shell values must be pairwise coprime")
    counts = multiplicative_convolution_counts(values, shifts)
    return max(counts.values(), default=0) == 1


def convolution_square_norm(
    shell_values: Sequence[int], residuals: Iterable[int]
) -> int:
    """Return ``sum_n |(1_A *_times 1_I)(n)|^2`` exactly."""

    counts = multiplicative_convolution_counts(shell_values, residuals)
    return sum(value * value for value in counts.values())

