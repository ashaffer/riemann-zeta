#!/usr/bin/env python3
"""Replay a modest exact rough-Voronoi increment scan."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rough_voronoi_increment_lab import analyze  # noqa: E402


result = analyze([1_000, 3_000, 10_000], exhaustive_q=True)
assert result["rows"]
assert all(all(row["certificates"].values()) for row in result["rows"])
observed = max(
    row["reduced_maximum"]["q_times_normalized_abs"] for row in result["rows"]
)

print("rough-Voronoi increment lab: PASS")
print(f"rows={len(result['rows'])}")
print(f"finite max q*normalized primitive coefficient={observed:.12f}")
print("scope=finite diagnostic only")
