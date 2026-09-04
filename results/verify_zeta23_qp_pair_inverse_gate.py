#!/usr/bin/env python3
"""Replay the numerical/algebraic ledger for the QP pair inverse gate."""

from __future__ import annotations

import json
import math
import pathlib
import sys
from dataclasses import asdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_pair_inverse_gate import (  # noqa: E402
    KAPPA_PROMOTE,
    audit_multi_island,
    audit_sign_simplex,
    pair_exponent_ledger,
)


def main() -> None:
    simplex = audit_sign_simplex(3)
    islands = audit_multi_island(3, island_size=40)
    ledger = pair_exponent_ledger(KAPPA_PROMOTE)

    assert simplex.representation_residual < 1e-12
    assert simplex.gram_error < 1e-12
    assert math.isclose(simplex.high_pair_mass, 1.0 / 9.0)
    assert islands.minimum_cross_distance_to_allowed_lag > 1.0
    assert 1.9 < islands.l2_ratio_to_bound < 2.1
    assert ledger.gm_pair_third_margin_below_main < 0.0
    assert ledger.one_point_l2_lower > ledger.pair_l2_lower

    print(
        json.dumps(
            {
                "status": "PASS",
                "claim": (
                    "pair concentration is valid, but its C^-6 packet-L2 "
                    "scale is weaker than the one-point C^-4 scale and is "
                    "saturated by non-global additive models"
                ),
                "ledger": asdict(ledger),
                "sign_simplex": asdict(simplex),
                "multi_island": asdict(islands),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
