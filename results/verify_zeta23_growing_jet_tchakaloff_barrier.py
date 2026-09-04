#!/usr/bin/env python3
"""Replay the growing-jet/Tchakaloff depth and conditioning barriers."""

import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from growing_jet_tchakaloff_barrier import self_check  # noqa: E402


print(json.dumps(self_check(), indent=2, sort_keys=True))
print("growing-jet Tchakaloff barrier: PASS")
