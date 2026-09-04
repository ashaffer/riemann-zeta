#!/usr/bin/env python3
"""Replay the numerical and algebraic ledgers in the companion report."""

from __future__ import annotations

import json

from qp_actual_multiplicative_gate import (
    kmt_rank_tax,
    limiting_turan_strip_width,
    negative_zero_pole_residue,
    square_reweight_termwise_bound,
    turan_band_ledger,
)


def main() -> None:
    beta = 0.0125
    ledger = turan_band_ledger(beta)
    payload = {
        "turan_beta": beta,
        "turan_ledger": ledger.__dict__,
        "turan_admissible": ledger.admissible,
        "limiting_strip_width": limiting_turan_strip_width(),
        "kmt_rank_tax_Y_1e100": kmt_rank_tax(1.0e100),
        "two_term_square_bound_at_delta_1e_3": square_reweight_termwise_bound(
            1.0e-3, [1.0, 1.0]
        ),
        "matching_zero_mellin_residue_beta_3_4": negative_zero_pole_residue(
            0.75
        ),
    }
    if not ledger.admissible:
        raise SystemExit("Turan exponent ledger failed")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
