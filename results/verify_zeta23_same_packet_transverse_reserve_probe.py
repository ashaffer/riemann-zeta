#!/usr/bin/env python3
"""Replay a small actual-coefficient transverse-reserve diagnostic."""

from __future__ import annotations

import json
import math
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from same_packet_transverse_reserve_probe import run_sequence  # noqa: E402


def verify() -> list[dict[str, object]]:
    rows = run_sequence([32.0, 64.0, 128.0], alpha=0.49, eta=0.5)
    for row in rows:
        assert row["candidate_is_asserted_zero"] is False
        assert row["K_selected"] > 0
        assert row["transverse_dimension"] >= 1
        assert math.isfinite(row["conditional_schur_residual_over_K"])
        assert math.isfinite(row["transverse_lambda_max_over_K"])
        for residual in row["checks"].values():
            assert residual < 1e-8
        for channel in row["channels"]:
            assert math.isfinite(channel["optimized_reserve_over_eta_K"])
    return rows


if __name__ == "__main__":
    payload = verify()
    summary = [
        {
            "height_T": row["height_T"],
            "K_selected": row["K_selected"],
            "r_over_K": row["r_over_K"],
            "schur_residual_over_K": row["conditional_schur_residual_over_K"],
            "transverse_top_over_K": row["transverse_lambda_max_over_K"],
        }
        for row in payload
    ]
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("PASS: actual-Lambda transverse probe (floating, nonzero candidate not asserted)")
