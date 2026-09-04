#!/usr/bin/env python3
"""Replay the QP nodal-product cutoff ledger."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_nodal_product_gate import (  # noqa: E402
    KAPPA_MIN,
    continuum_potential_max,
    diagnose,
)


def main() -> None:
    potential, location, ratio = continuum_potential_max(0.2)
    assert abs(potential - (-1.8187266764709782)) < 1e-9
    assert abs(location - (-0.2)) < 1e-7
    assert abs(ratio - 2.267610596526286) < 1e-9

    rows = [diagnose(y, 0.2, 0.49, KAPPA_MIN) for y in (300.0, 1000.0, 3000.0)]
    for row in rows:
        assert row.low_cutoff_log_bound < row.target_log
        assert row.low_cutoff < row.cutoff_frontier < row.full_aperture
        assert row.cutoff_frontier_over_nodes > 1.0
        assert math.isfinite(row.max_log_product_per_node)

    print(
        json.dumps(
            {
                "status": "PASS",
                "polarity": "shallow-support upper bound obstructs PROMOTE; it is not a strip proof",
                "continuum_cutoff_over_M": ratio,
                "rows": [
                    {
                        "Y": row.y,
                        "M": row.node_count,
                        "D_frontier": row.cutoff_frontier,
                        "D_frontier_over_M": row.cutoff_frontier_over_nodes,
                        "low_log_bound_minus_target": row.low_cutoff_log_bound
                        - row.target_log,
                    }
                    for row in rows
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
