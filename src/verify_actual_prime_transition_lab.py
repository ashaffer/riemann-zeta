#!/usr/bin/env python3
"""Deterministically replay an actual-prime transition laboratory JSON file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from actual_prime_transition_lab import verify_result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    verify_result(report, recompute=True)
    print(f"PASS {args.report} {report['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
