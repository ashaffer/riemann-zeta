#!/usr/bin/env python3
"""Replay the exact common-height rough L4 normalization ledger."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rough_common_height_l4_gate import self_check  # noqa: E402


result = self_check()
assert result["moment_identities"]
assert result["band_holder"]
assert result["block_holder"]
print("common-height rough L4 gate: PASS")
print(result["ledger"])
print(result["countermodel"])
