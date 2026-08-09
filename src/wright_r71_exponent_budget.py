#!/usr/bin/env python3
"""Exponent audit for a *hypothetical* Wright-to-R71 reduction.

This module does not construct that reduction.  It only substitutes the
retreated proportional-order scales into Theorem 2.1 of Wright's
``Trilinear Kloosterman fractions I``.  Keeping this calculation separate is
useful because Wright's fixed denominator is a power of ``x`` at every fixed
detector slope, not ``x**o(1)``.

All returned numbers are exponents of ``x``.  A positive ``net_saving`` is
the nominal power left relative to the theorem's Cauchy baseline, before any
unrecorded losses needed to derive or sum R71 modes.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class WrightBudget:
    """Power exponents in Wright's five-term bracket and its prefactors."""

    factor_exponent: float
    fixed_denominator_exponent: float
    product_shell_excess: float
    numerator_length_exponent: float
    phase_ratio_exponent: float
    bracket_exponents: tuple[float, float, float, float, float]
    prefactor_loss: float
    mode_loss: float
    net_saving: float


@dataclass(frozen=True)
class DampedCofactorTradeoff:
    """Optimistic balance between damping tail and native Wright gain."""

    damping_exponent: float
    cutoff_exponent: float
    tail_saving: float
    wright_saving: float
    gross_saving: float
    original_zero_strip: float


def wright_budget(
    slope: float,
    cutoff_retreat: float,
    *,
    product_shell_excess: float = 0.0,
    numerator_length_exponent: float = 0.0,
    phase_integer_exponent: float = 0.0,
    mode_loss: float = 0.0,
) -> WrightBudget:
    """Substitute the schematic balanced retreated-cutoff scales.

    The substitution is

    ``M=N=x**((1-cutoff_retreat*slope)/2)`` and
    ``R0=x**(cutoff_retreat*slope+product_shell_excess)``.

    The central product shell has ``product_shell_excess=0``.  The top of a
    proportional window of half-width ``h*slope`` has
    ``product_shell_excess=h*slope``.

    Wright's numerator variable has length ``x**a`` and the nonzero integer
    phase is at most ``x**v``.  The factor
    ``(1+|vartheta| A/(MN))**(1/4)`` therefore costs the positive part of
    ``v+a-2m``, divided by four.
    """

    values = (
        slope,
        cutoff_retreat,
        product_shell_excess,
        numerator_length_exponent,
        phase_integer_exponent,
        mode_loss,
    )
    if not all(math.isfinite(value) for value in values):
        raise ValueError("all parameters must be finite")
    if slope <= 0.0 or cutoff_retreat <= 0.0:
        raise ValueError("slope and cutoff_retreat must be positive")
    if product_shell_excess < 0.0:
        raise ValueError("product_shell_excess must be nonnegative")
    if numerator_length_exponent < 0.0 or phase_integer_exponent < 0.0:
        raise ValueError("length and phase exponents must be nonnegative")
    if mode_loss < 0.0:
        raise ValueError("mode_loss must be nonnegative")

    cutoff_gap = cutoff_retreat * slope
    fixed = cutoff_gap + product_shell_excess
    factor = (1.0 - cutoff_gap) / 2.0
    if factor <= 0.0:
        raise ValueError("cutoff_retreat*slope must be less than one")

    a_exp = numerator_length_exponent
    # Exponents of the five terms in Wright's Theorem 2.1 bracket.
    terms = (
        -factor / 8.0,
        fixed / 8.0 + factor / 8.0 - factor / 4.0,
        factor / 10.0 - 3.0 * fixed / 20.0
        - a_exp / 20.0 - 3.0 * factor / 20.0,
        3.0 * factor / 20.0 - 3.0 * a_exp / 20.0
        - factor / 5.0,
        3.0 * factor / 8.0 - factor / 2.0,
    )
    phase_ratio = max(
        0.0,
        phase_integer_exponent + a_exp - 2.0 * factor,
    )
    prefactor_loss = fixed / 4.0 + phase_ratio / 4.0
    net_saving = -(prefactor_loss + max(terms)) - mode_loss
    return WrightBudget(
        factor_exponent=factor,
        fixed_denominator_exponent=fixed,
        product_shell_excess=product_shell_excess,
        numerator_length_exponent=a_exp,
        phase_ratio_exponent=phase_ratio,
        bracket_exponents=terms,
        prefactor_loss=prefactor_loss,
        mode_loss=mode_loss,
        net_saving=net_saving,
    )


def damped_cofactor_tradeoff(epsilon: float) -> DampedCofactorTradeoff:
    """Optimize the idealized epsilon-damped componentwise ledger.

    At a cofactor cutoff ``Q=x**A``, absolute tail control gives amplitude
    saving ``A*epsilon``.  Even granting the favorable central Wright budget,
    the oscillatory saving is at most ``(1-11*A)/40``.  The common maximum of
    their minimum occurs at ``A=1/(40*epsilon+11)``.  The detector shifts every
    original zero left by ``epsilon``, so only ``gross_saving-epsilon`` could
    become a zero-free width.

    This is deliberately optimistic: it ignores the zero/axis sectors and
    the coupled amplitude, and therefore can only falsify the separated
    damping strategy, not certify a Wright application.
    """

    if not math.isfinite(epsilon) or epsilon <= 0.0:
        raise ValueError("epsilon must be finite and positive")
    cutoff = 1.0 / (40.0 * epsilon + 11.0)
    tail = cutoff * epsilon
    wright = (1.0 - 11.0 * cutoff) / 40.0
    gross = min(tail, wright)
    return DampedCofactorTradeoff(
        damping_exponent=epsilon,
        cutoff_exponent=cutoff,
        tail_saving=tail,
        wright_saving=wright,
        gross_saving=gross,
        original_zero_strip=gross - epsilon,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slope", type=float, default=0.001)
    parser.add_argument("--retreat", type=float, default=3.0)
    parser.add_argument("--shell-excess", type=float, default=0.0)
    parser.add_argument("--numerator-exponent", type=float, default=0.0)
    parser.add_argument("--phase-exponent", type=float, default=0.0)
    parser.add_argument("--mode-loss", type=float, default=0.0)
    parser.add_argument("--damping-epsilon", type=float)
    args = parser.parse_args()
    budget = wright_budget(
        args.slope,
        args.retreat,
        product_shell_excess=args.shell_excess,
        numerator_length_exponent=args.numerator_exponent,
        phase_integer_exponent=args.phase_exponent,
        mode_loss=args.mode_loss,
    )
    print(f"factor_exponent={budget.factor_exponent:.12g}")
    print(
        "fixed_denominator_exponent="
        f"{budget.fixed_denominator_exponent:.12g}"
    )
    print(
        "bracket_exponents="
        + ",".join(f"{value:.12g}" for value in budget.bracket_exponents)
    )
    print(f"phase_ratio_exponent={budget.phase_ratio_exponent:.12g}")
    print(f"prefactor_loss={budget.prefactor_loss:.12g}")
    print(f"net_saving={budget.net_saving:.12g}")
    if args.damping_epsilon is not None:
        tradeoff = damped_cofactor_tradeoff(args.damping_epsilon)
        print(
            "damped_optimal_cutoff="
            f"{tradeoff.cutoff_exponent:.12g}"
        )
        print(f"damped_gross_saving={tradeoff.gross_saving:.12g}")
        print(
            "damped_original_zero_strip="
            f"{tradeoff.original_zero_strip:.12g}"
        )


if __name__ == "__main__":
    main()
