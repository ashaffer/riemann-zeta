"""Exact exponent ledger for the Burgess determinant-band synthesis.

The accompanying report proves that Burgess's ``r=2`` character-sum
estimate replaces the fourth-moment determinant-band error by

    D^(1/2) q^(3/16) = D^(227/256)

at the project scale ``D=q^(16/33)``.  The broad completion cap and the
singleton part of the parabolic occupied-line theorem both cost
``D^(5/16)``.  The resulting trace exponent is ``307/256``; the already
proved parabolic curvature exponent ``37/32`` is smaller.  Large
coefficient-height bins are covered by the diffuse estimate at support
exponent ``461/256``.

This module records only exact rational arithmetic and the optimization
logic.  The character-sum and sector arguments are mathematical inputs
proved and cited in the report.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class BurgessSynthesisLedger:
    """All D-power exponents in the uniform synthesis."""

    d_exponent_in_q: Fraction
    burgess_parameter: int
    burgess_short_sum_exponent_in_d: Fraction
    broad_and_singleton_cap: Fraction
    parabolic_curvature: Fraction
    support_crossover: Fraction
    principal_trace_at_crossover: Fraction
    diffuse_trace_at_crossover: Fraction
    uniform_trace: Fraction
    uniform_operator: Fraction
    previous_trace: Fraction
    trace_gain: Fraction
    distance_from_sharp_trace: Fraction
    transverse_exponent: Fraction


def burgess_short_sum_exponent_in_d(r: int) -> Fraction:
    """Return the D-exponent in the classical Burgess bound.

    Burgess gives ``N^(1-1/r) q^((r+1)/(4r^2)+o(1))``.  Substituting
    ``N=D`` and ``q=D^(33/16)`` gives the returned exponent.
    """

    if r < 2:
        raise ValueError("the synthesis uses Burgess parameters r>=2")
    return (
        Fraction(r - 1, r)
        + Fraction(33 * (r + 1), 64 * r * r)
    )


def burgess_flat_mass_exponent(mu: Fraction) -> Fraction:
    """Return the determinant-mass exponent for ``M=D^mu``.

    The two terms are the principal contribution ``MD/q`` and the
    nonprincipal Burgess contribution ``D^(227/256)``.
    """

    if mu < 0 or mu > Fraction(33, 16):
        raise ValueError("support exponent lies outside the project shell")
    principal = mu + 1 - Fraction(33, 16)
    return max(principal, burgess_short_sum_exponent_in_d(2))


def small_bin_trace_exponent(mu: Fraction) -> Fraction:
    """Return the small-bin trace exponent after sector decomposition."""

    cap = Fraction(5, 16)
    singleton = burgess_flat_mass_exponent(mu) + cap
    curvature = Fraction(37, 32)
    repeated = Fraction(1)
    return max(singleton, curvature, repeated)


def diffuse_trace_exponent(mu: Fraction) -> Fraction:
    """Return the exponent in ``D + D^3/M`` for ``M=D^mu``."""

    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return max(Fraction(1), 3 - mu)


def burgess_synthesis_ledger() -> BurgessSynthesisLedger:
    """Return the optimized exact ledger."""

    short = burgess_short_sum_exponent_in_d(2)
    cap = Fraction(5, 16)
    trace = short + cap
    crossover = 3 - trace
    principal_trace = (
        crossover + 1 - Fraction(33, 16) + cap
    )
    previous = Fraction(5, 4)
    return BurgessSynthesisLedger(
        d_exponent_in_q=Fraction(16, 33),
        burgess_parameter=2,
        burgess_short_sum_exponent_in_d=short,
        broad_and_singleton_cap=cap,
        parabolic_curvature=Fraction(37, 32),
        support_crossover=crossover,
        principal_trace_at_crossover=principal_trace,
        diffuse_trace_at_crossover=diffuse_trace_exponent(crossover),
        uniform_trace=trace,
        uniform_operator=trace / 4,
        previous_trace=previous,
        trace_gain=previous - trace,
        distance_from_sharp_trace=trace - 1,
        transverse_exponent=Fraction(1, 2) + Fraction(4, 33) * trace,
    )
