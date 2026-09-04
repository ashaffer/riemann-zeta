"""Exact ledger for the nonuniform top-k/tail four-cycle refinement.

The determinant band is a three-coordinate matching.  Besides its
``L^(4/3)`` endpoint, multilinear interpolation therefore gives the mixed
endpoints ``(6/5,6/5,6/5,2)`` and ``(1,1,2,2)``.  They control terms with
one and two tail coordinates.  Polarization of the proved sectorwise
``L^2`` bounds is used only for terms with at least three tail coordinates.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence


PARABOLIC_POINTWISE_EXPONENT = Fraction(1, 2)
PARABOLIC_UNIFORM_EXPONENT = Fraction(5, 4)
BROAD_POINTWISE_EXPONENT = Fraction(5, 16)
BROAD_UNIFORM_EXPONENT = Fraction(21, 16)


ONE_TAIL_RECIPROCALS = (
    Fraction(5, 6),
    Fraction(5, 6),
    Fraction(5, 6),
    Fraction(1, 2),
)
TWO_TAIL_RECIPROCALS = (
    Fraction(1),
    Fraction(1),
    Fraction(1, 2),
    Fraction(1, 2),
)


@dataclass(frozen=True)
class TopKTailLedger:
    """Power thresholds in the sufficient nonuniform FC condition.

    If ``k <= D^top_cutoff`` and the normalized squared ``L^2`` mass
    outside the largest ``k`` coordinates is at most
    ``D^(-tail_decay_required)``, then the four-cycle trace is
    ``D^(1+o(1))``.  This is a sufficient profile theorem, not a uniform
    estimate.
    """

    top_cutoff: Fraction
    parabolic_tail_decay_required: Fraction
    broad_tail_decay_required: Fraction
    tail_decay_required: Fraction
    flat_on_degree_support_is_closed: bool
    iteration_removes_flat_barrier: bool


def topk_tail_ledger() -> TopKTailLedger:
    """Return the exact sharp-threshold ledger for this argument."""

    parabolic_tail = (PARABOLIC_UNIFORM_EXPONENT - 1) * Fraction(2, 3)
    broad_tail = (BROAD_UNIFORM_EXPONENT - 1) * Fraction(2, 3)
    return TopKTailLedger(
        top_cutoff=Fraction(1, 2),
        parabolic_tail_decay_required=parabolic_tail,
        broad_tail_decay_required=broad_tail,
        tail_decay_required=max(parabolic_tail, broad_tail),
        flat_on_degree_support_is_closed=False,
        iteration_removes_flat_barrier=False,
    )


def normalized_topk_tail_mass(weights: Sequence[complex], k: int) -> float:
    """Return squared ``L^2`` mass outside the largest ``k`` coordinates."""

    if k < 0:
        raise ValueError("k must be nonnegative")
    masses = sorted((abs(value) ** 2 for value in weights), reverse=True)
    total = sum(masses)
    if total == 0:
        return 0.0
    return sum(masses[k:]) / total


def topk_tail_trace_exponent(kappa: Fraction, nu: Fraction) -> Fraction:
    """Return the trace exponent from ``k=D^kappa, tau_k=D^(-nu)``.

    Constants and ``D^o(1)`` factors are suppressed.  The returned maximum
    includes the already sharp repeated-coordinate floor ``D``.
    """

    if kappa < 0 or nu < 0:
        raise ValueError("kappa and nu must be nonnegative")

    parabolic_top = min(
        PARABOLIC_UNIFORM_EXPONENT,
        PARABOLIC_POINTWISE_EXPONENT + kappa,
    )
    parabolic_tail = PARABOLIC_UNIFORM_EXPONENT - Fraction(3, 2) * nu
    broad_top = min(
        BROAD_UNIFORM_EXPONENT,
        BROAD_POINTWISE_EXPONENT + kappa,
    )
    broad_tail = BROAD_UNIFORM_EXPONENT - Fraction(3, 2) * nu
    return max(
        Fraction(1),
        parabolic_top,
        parabolic_tail,
        broad_top,
        broad_tail,
    )


def flat_topk_tail_mass(support: int, k: int) -> Fraction:
    """Exact tail mass for an ``L^2``-normalized vector flat on its support."""

    if support <= 0:
        raise ValueError("support must be positive")
    if k < 0:
        raise ValueError("k must be nonnegative")
    retained = min(k, support)
    return Fraction(support - retained, support)
