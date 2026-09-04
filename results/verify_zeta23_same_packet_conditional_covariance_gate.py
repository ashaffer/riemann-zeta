#!/usr/bin/env python3
"""Replay the exact algebra in the same-packet covariance theorem card."""

from __future__ import annotations

import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from same_packet_conditional_covariance_gate import self_check  # noqa: E402


if __name__ == "__main__":
    print(json.dumps(self_check(), indent=2, sort_keys=True))
    print("PASS: finite nonlinear/contact and two-channel covariance ledgers")
