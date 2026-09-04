#!/usr/bin/env python3
"""Replay the exact exponent and finite-factor bridge ledgers."""

from __future__ import annotations

import json

from qp_strip_bridge import (
    QP_FIXED_SLICE_KAPPA_MAX,
    fejer_continuum_limit,
    fejer_exact_minimum_frequency,
    fejer_nonzero_cosine,
    matching_zero_mellin_residue,
    positive_coefficient_factor,
    positive_factor_zero_ordinate,
    strip_to_qp_ledger,
    support_preserving_factor,
    transferred_turan_strip_width,
)


def main() -> None:
    delta = 0.02
    c = (delta + QP_FIXED_SLICE_KAPPA_MAX) / 2.0
    ledger = strip_to_qp_ledger(delta, c)
    beta = 0.99
    ordinate = 100.0
    positive_factor_ordinate = positive_factor_zero_ordinate(1000)
    fejer_order = 1001
    fejer_width = 0.2
    fejer_minimum_frequency = fejer_exact_minimum_frequency(
        fejer_order, fejer_width, zero_index=503
    )
    payload = {
        "strip_to_qp": ledger.__dict__,
        "closes_fixed_slice": ledger.closes
        and c > QP_FIXED_SLICE_KAPPA_MAX,
        "matching_zero_residue_beta_0_99": matching_zero_mellin_residue(beta),
        "support_factor_at_prescribed_zero": abs(
            support_preserving_factor(beta + 1j * ordinate, beta, ordinate)
        ),
        "positive_coefficient_factor_high_zero": abs(
            positive_coefficient_factor(
                beta + 1j * positive_factor_ordinate, beta
            )
        ),
        "fejer_exact_floor": fejer_nonzero_cosine(
            fejer_minimum_frequency, fejer_order, fejer_width
        ),
        "fejer_fixed_ordinate_limit_t_1": fejer_continuum_limit(
            1.0, fejer_width
        ),
        "conditional_no_loss_turan_width_at_c_019": (
            transferred_turan_strip_width(0.019, 1.0)
        ),
    }
    if not payload["closes_fixed_slice"]:
        raise SystemExit("strip-to-QP exponent ledger failed")
    if payload["support_factor_at_prescribed_zero"] > 1.0e-12:
        raise SystemExit("finite Euler factor missed its prescribed zero")
    if payload["positive_coefficient_factor_high_zero"] > 1.0e-10:
        raise SystemExit("positive Dirichlet factor missed its high zero")
    if abs(payload["fejer_exact_floor"] + 1.0 / (fejer_order - 1)) > 1.0e-12:
        raise SystemExit("nonzero Fejer certificate missed its exact floor")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
