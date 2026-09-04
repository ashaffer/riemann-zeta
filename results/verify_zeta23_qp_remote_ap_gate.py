#!/usr/bin/env python3
"""Replay the remote-AP directional and dilation-shadow ledger."""

from __future__ import annotations

import json
import math
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_remote_ap_gate import (  # noqa: E402
    KAPPA_PROMOTE,
    ap_shadow_exponents,
    scan_ap_steps,
)


def main() -> None:
    exponents = ap_shadow_exponents()
    assert exponents["packet_shadow"] < exponents["legal_step_interval"]
    assert exponents["relative_density"] < -0.47
    diagnostics = [
        scan_ap_steps(y, 0.2, samples=1500, refinements=16)
        for y in (100.0, 300.0, 1000.0)
    ]
    for item in diagnostics:
        assert item.node_count > 0
        assert item.top_frequency <= item.y ** (50.0 / 33.0) * (1.0 + 1e-12)
        assert item.interpolation_residual < 1e-8
        assert item.nodal_polynomial_residual < 1e-10
        assert not item.beats_promotion_budget
        assert not item.positive_beats_promotion_budget
        if item.best_positive_depth > 0.0:
            assert math.isclose(
                item.best_positive_cost,
                1.0 / item.best_positive_depth,
                rel_tol=1e-12,
            )
    print(
        json.dumps(
            {
                "schema": "verify-zeta23-qp-remote-ap-gate-v1",
                "kappa_promote": KAPPA_PROMOTE,
                "shadow_exponents": exponents,
                "diagnostics": [asdict(item) for item in diagnostics],
                "verdict": (
                    "AP dilation shadow has zero relative measure at the "
                    "promotion cost, but exceptional steps remain"
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
