"""Exact bookkeeping for the dyadic reciprocal-moment gate.

This module does not prove the gate.  It records two pieces which are easy
to confuse in the four-cycle reduction:

* deleting only the modes ``ell <= q / D**2`` does not make the unweighted
  second moment diagonal-sized; an odd-centre consecutive strip is still
  coherent on the next dyadic interval;
* a dyadic loss ``D**beta`` in the *primal* second moment is square-rooted
  by Cauchy--Schwarz before the Selberg coefficient is applied.  Thus it
  would give a local and fourth-trace exponent ``1 + beta/2`` in powers of
  ``D``.

All phase calculations below use :class:`fractions.Fraction`.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


def odd_centre_phase(q: int, x: int, y: int) -> Fraction:
    """Return ``q^3 / (8 (m+x) (m+y))`` for odd ``q=2m+1``."""

    q = int(q)
    x = int(x)
    y = int(y)
    if q <= 1 or q % 2 == 0:
        raise ValueError("q must be an odd integer greater than one")
    m = (q - 1) // 2
    if m + x <= 0 or m + y <= 0:
        raise ValueError("shifted factors must be positive")
    return Fraction(q**3, 8 * (m + x) * (m + y))


def odd_centre_reduced_phase(q: int, x: int, y: int) -> Fraction:
    """Remove the common and integral-linear phases at the odd centre.

    For integer ``ell``, the exponential of the original phase differs
    from the exponential of this value only by the common factor
    ``e(ell * odd_centre_phase(q, 0, 0))`` because ``x+y`` is integral.
    """

    return (
        odd_centre_phase(q, x, y)
        - odd_centre_phase(q, 0, 0)
        + x
        + y
    )


def consecutive_lift_determinant(m: int, shift: int) -> int:
    """Return ``det((m,m+1),(m+t,m+t+1))=-t`` exactly."""

    m = int(m)
    shift = int(shift)
    return m * (m + shift + 1) - (m + 1) * (m + shift)


@dataclass(frozen=True)
class DyadicMomentLossLedger:
    """Consequences of a primal dyadic moment loss ``D**beta``."""

    moment_loss_exponent_in_degree: Fraction
    l1_loss_exponent_in_degree: Fraction
    slope_block_exponent_in_degree: Fraction
    fourth_trace_exponent_in_degree: Fraction
    current_fourth_trace_exponent_in_degree: Fraction
    improvement_exponent_in_degree: Fraction
    improves_current_uniform_trace: bool


def dyadic_moment_loss_ledger(beta: Fraction | int) -> DyadicMomentLossLedger:
    """Map ``sum_{ell~K}|S_ell|^2 <= q^2 D^beta/K`` to FC.

    Dyadic Cauchy--Schwarz changes ``D^beta`` to ``D^(beta/2)``.
    Selberg then gives a slope-block cap ``D^(1+beta/2)``.  The standard
    restricted-type/slope-block chain is homogeneous in this cap, so the
    same exponent is the resulting fourth-trace exponent.
    """

    beta = Fraction(beta)
    if beta < 0:
        raise ValueError("beta must be nonnegative")
    current = Fraction(21, 16)
    l1_loss = beta / 2
    trace = 1 + l1_loss
    return DyadicMomentLossLedger(
        moment_loss_exponent_in_degree=beta,
        l1_loss_exponent_in_degree=l1_loss,
        slope_block_exponent_in_degree=trace,
        fourth_trace_exponent_in_degree=trace,
        current_fourth_trace_exponent_in_degree=current,
        improvement_exponent_in_degree=current - trace,
        improves_current_uniform_trace=trace < current,
    )


@dataclass(frozen=True)
class HostileCubicTransitionLedger:
    """Powers in the necessary balanced positive-diagonal transition."""

    fan_parameter_exponent_in_q: Fraction
    selberg_length_exponent_in_q: Fraction
    denominator_height_exponent_in_p: Fraction
    residual_height_exponent_in_p: Fraction
    target_count_exponent_in_p: Fraction
    audited_floor_exponent_in_p: Fraction
    audited_gap_exponent_in_p: Fraction


def hostile_cubic_transition_ledger() -> HostileCubicTransitionLedger:
    """Return powers for ``A u^3 - B P^3 = Delta`` at the HSM wall."""

    target = Fraction(9, 16)
    floor = Fraction(5, 8)
    return HostileCubicTransitionLedger(
        fan_parameter_exponent_in_q=Fraction(8, 33),
        selberg_length_exponent_in_q=Fraction(17, 33),
        denominator_height_exponent_in_p=target,
        residual_height_exponent_in_p=Fraction(7, 16),
        target_count_exponent_in_p=target,
        audited_floor_exponent_in_p=floor,
        audited_gap_exponent_in_p=floor - target,
    )
