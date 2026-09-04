#!/usr/bin/env python3
"""Replay the global affine mixed-depth Pick-screen audit."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mixed_depth_pick_screen import self_check  # noqa: E402


result = self_check()
assert not result["obstruction_crosses_surcharge"]
assert not result["gp_closed"]
print("global affine mixed-depth Pick screen: PASS")
print(result)
