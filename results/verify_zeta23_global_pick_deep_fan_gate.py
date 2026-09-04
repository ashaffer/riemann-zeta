#!/usr/bin/env python3
"""Replay the global Pick deep-fan normalization ledger."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from global_pick_deep_fan_gate import self_check  # noqa: E402


result = self_check()
assert not result["gp_closed"]
print("global compact Pick deep-fan gate: PASS")
print(result)
