#!/usr/bin/env python3
"""Exact constants and logic for the candidate-centred strip assembly.

This module deliberately separates a QP promotion theorem from the OD2
dual-antenna theorem.  The latter is a no-go for one optional construction;
it is not a zero-exclusion statement.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


ALPHA_0 = Fraction(49, 100)
BETA_0 = Fraction(1, 2) + ALPHA_0
ZF_DELTA = Fraction(1) - BETA_0
D = Fraction(33, 50)
RAW_CARRIER_X_EXPONENT = ALPHA_0 * D

# Conservative rounded Green--Poisson base used by the GP ledger.
GREEN_BASE_X_EXPONENT = Fraction(298_008_745, 1_000_000_000)
GP_SURCHARGE = RAW_CARRIER_X_EXPONENT - GREEN_BASE_X_EXPONENT

# The published decimal promotion threshold at alpha=.49,d=.66 and the
# deliberately larger hostile CH4 bill.
KAPPA_PROMOTE = Fraction(180_303_234, 10_000_000_000)
KAPPA_HOSTILE = Fraction(1_974_048_259, 100_000_000_000)
H_MIN_EXPONENT = Fraction(8, 33)
LONG_EDGE_EXPONENT = Fraction(797, 5000)


def zf_delta(alpha0: Fraction = ALPHA_0) -> Fraction:
    """Width of the strip obtained by excluding beta>=1/2+alpha0."""

    if not Fraction(0) < alpha0 < Fraction(1, 2):
        raise ValueError("alpha0 must lie in (0,1/2)")
    return Fraction(1, 2) - alpha0


def od2_epsilon_frontier(
    kappa: Fraction = KAPPA_HOSTILE,
    h_min: Fraction = H_MIN_EXPONENT,
    long_edge: Fraction = LONG_EDGE_EXPONENT,
) -> Fraction:
    """Strict Y-exponent slack delivered by diagonal-scale OD2."""

    return (h_min - 4 * kappa - long_edge) / 4


OD2_EPSILON_FRONTIER = od2_epsilon_frontier()


def od2_closes_ch4(epsilon_od2: Fraction) -> bool:
    """The CH4 implication is strict at the exponent frontier."""

    return Fraction(0) < epsilon_od2 < OD2_EPSILON_FRONTIER


def od2_dual_antenna_exponent(epsilon_od2: Fraction) -> Fraction:
    """Exponent c in the post-q CH4/dual contribution Y^(-c+o(1)).

    Promoting this to a full antenna also requires every low/mid, boundary,
    and companion transfer term at exponent at least c.
    """

    if not od2_closes_ch4(epsilon_od2):
        raise ValueError("epsilon_od2 must be strictly inside the frontier")
    return KAPPA_HOSTILE + epsilon_od2


def qp_promote_upper_exponent(eta: Fraction) -> Fraction:
    """Exponent in the sufficient cheap-nuller target C<=Y^(kappa-eta)."""

    if not Fraction(0) < eta < KAPPA_PROMOTE:
        raise ValueError("eta must lie strictly between zero and kappa_promote")
    return KAPPA_PROMOTE - eta


def asymptotic_cost_bounds_compatible(
    upper_exponent: Fraction, lower_exponent: Fraction
) -> bool:
    """Can C<=Y^(upper+o(1)) and C>=Y^(lower-o(1)) coexist?"""

    return lower_exponent <= upper_exponent


def gp_budget_after_y_loss(y_loss_exponent: Fraction) -> Fraction:
    """Remaining X-exponent after a multiplicative Y^{-loss} step."""

    return GP_SURCHARGE - D * y_loss_exponent


MAX_COUNTERFACTUAL_OD2_Y_BILL = KAPPA_HOSTILE + OD2_EPSILON_FRONTIER
MAX_COUNTERFACTUAL_OD2_X_BILL = D * MAX_COUNTERFACTUAL_OD2_Y_BILL
RESIDUAL_GP_BUDGET_AFTER_COUNTERFACTUAL_OD2 = gp_budget_after_y_loss(
    MAX_COUNTERFACTUAL_OD2_Y_BILL
)


def budgeted_gp_is_compatible(
    gp_retained_x_exponent: Fraction, qp_loss_y_exponent: Fraction
) -> bool:
    """A pre-QP GP state must retain more than the subsequent QP loss."""

    return gp_retained_x_exponent > D * qp_loss_y_exponent


def same_packet_sign_contradiction(
    gp_other_upper_fraction: Fraction,
    ga_reserve_lower_fraction: Fraction,
    *,
    same_packet: bool,
) -> bool:
    """Check R_other<=uK and R_other>=gK on one and the same K."""

    return same_packet and ga_reserve_lower_fraction > gp_other_upper_fraction


@dataclass(frozen=True)
class AssemblyHypotheses:
    """Logical hypotheses of the corrected conditional strip theorem."""

    low_height_base_case: bool
    budgeted_gp: bool
    qp_promote: bool
    ga2_scalar_reserve: bool
    same_packet_compatibility: bool
    gp_other_upper_fraction: Fraction = Fraction(0)
    ga_reserve_lower_fraction: Fraction = Fraction(1, 100)


def corrected_package_proves_strip(hypotheses: AssemblyHypotheses) -> bool:
    """Pure implication audit; it does not assert that a hypothesis is proved."""

    return (
        hypotheses.low_height_base_case
        and hypotheses.budgeted_gp
        and hypotheses.qp_promote
        and hypotheses.ga2_scalar_reserve
        and hypotheses.same_packet_compatibility
        and same_packet_sign_contradiction(
            hypotheses.gp_other_upper_fraction,
            hypotheses.ga_reserve_lower_fraction,
            same_packet=hypotheses.same_packet_compatibility,
        )
    )


def stated_gp_od2_ga2_package_proves_strip() -> bool:
    """GP+OD2+GA2 lacks QP-PROMOTE and therefore has no strip implication."""

    return False


def audit() -> dict[str, str | bool]:
    sample_epsilon = OD2_EPSILON_FRONTIER / 2
    promotion_eta = Fraction(1, 100_000)
    promotion_upper = qp_promote_upper_exponent(promotion_eta)
    dual_lower = od2_dual_antenna_exponent(sample_epsilon)
    return {
        "alpha0": str(ALPHA_0),
        "beta0": str(BETA_0),
        "zf_delta": str(ZF_DELTA),
        "d": str(D),
        "raw_carrier_x_exponent": str(RAW_CARRIER_X_EXPONENT),
        "gp_surcharge": str(GP_SURCHARGE),
        "kappa_promote": str(KAPPA_PROMOTE),
        "kappa_hostile": str(KAPPA_HOSTILE),
        "od2_epsilon_frontier": str(OD2_EPSILON_FRONTIER),
        "max_counterfactual_od2_y_bill": str(MAX_COUNTERFACTUAL_OD2_Y_BILL),
        "max_counterfactual_od2_x_bill": str(MAX_COUNTERFACTUAL_OD2_X_BILL),
        "residual_gp_budget_after_counterfactual_od2": str(
            RESIDUAL_GP_BUDGET_AFTER_COUNTERFACTUAL_OD2
        ),
        "sample_promotion_upper_exponent": str(promotion_upper),
        "sample_od2_dual_lower_exponent": str(dual_lower),
        "promotion_and_od2_compatible": asymptotic_cost_bounds_compatible(
            promotion_upper, dual_lower
        ),
        "gp_od2_ga2_proves_strip": stated_gp_od2_ga2_package_proves_strip(),
    }


if __name__ == "__main__":
    print(audit())
