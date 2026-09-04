#!/usr/bin/env python3
"""Replay the exact QP pair-energy/BSG hostile-audit fixtures."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_pair_energy_bsg_audit import (  # noqa: E402
    ap_islands_model,
    audit_snapshot,
    orientation_countermodel,
    orthogonal_antipode_model,
    pair_ledger,
    rank_two_gap_model,
    sum_matching_model,
)


def main() -> None:
    cost = 10
    ledger = pair_ledger(cost)
    assert ledger.one_point_heavy_cell_lower > ledger.cell_l2_mass_lower

    orthogonal = orthogonal_antipode_model(cost)
    assert orthogonal.good_pair_probability * cost**2 == 1
    assert orthogonal.unnormalized_good_pair_mass == 1
    assert orthogonal.normalized_off_diagonal_kernel == 0

    islands = ap_islands_model(cost)
    assert islands.allowed_within_difference_count <= cost**4
    assert islands.good_pair_probability * cost**2 == 1
    assert not islands.contained_in_rank_one_progression
    assert islands.weighted_additive_energy * cost**8 > 0

    rank_two = rank_two_gap_model(cost)
    assert rank_two.difference_span_rank == 2
    assert not rank_two.contained_in_rank_one_progression

    matching = sum_matching_model(cost**2)
    assert matching.edge_density * cost**2 == 1
    assert matching.restricted_sumset_size == 1

    orientation = orientation_countermodel()
    assert orientation.represented_carrier == 1
    assert orientation.kernel_value > orientation.kernel_threshold
    assert not orientation.convex_hull_hits_negative_carrier_ray

    print(json.dumps(audit_snapshot(cost), indent=2, sort_keys=True))
    print("QP pair-energy/BSG hostile audit: PASS")


if __name__ == "__main__":
    main()
