#!/usr/bin/env python3
"""Standalone replay of the rough first-return/rank ledger."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rough_first_return_rank_gate import self_check  # noqa: E402


result = self_check()
assert result["prefix_kernel_rank_12"] == 12
print("rough first-return low-rank gate: PASS")
print(result["ledger"])
