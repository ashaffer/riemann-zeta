#!/usr/bin/env python3
"""Read the compressed ZETA23 research cache without loading the history.

Usage:
  python3 src/zeta23_context_cache.py
  python3 src/zeta23_context_cache.py live hypotheses thresholds
  python3 src/zeta23_context_cache.py --json live
  python3 src/zeta23_context_cache.py --pretty
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "results/context/zeta23_context_cache_v1.json.gz"
DEFAULT = ("goal", "status", "core", "thresholds", "live", "hypotheses")
SUPERSESSION_WARNING = (
    "WARNING: zeta23_context_cache_v1 is a historical August snapshot; "
    "use `python3 src/zeta23_correction_context.py resume` for current routing."
)


def load() -> dict[str, Any]:
    with gzip.open(CACHE, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def compact(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, separators=(",", ":"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sections", nargs="*", help="top-level cache keys")
    parser.add_argument("--json", action="store_true", help="emit one JSON object")
    parser.add_argument(
        "--pretty", action="store_true", help="decode as indented human-readable JSON"
    )
    args = parser.parse_args()
    print(SUPERSESSION_WARNING, file=sys.stderr)
    data = load()
    sections = tuple(args.sections) or DEFAULT
    missing = [key for key in sections if key not in data]
    if missing:
        raise SystemExit("unknown cache key(s): " + ", ".join(missing))
    selected = {key: data[key] for key in sections}
    if args.pretty:
        print(json.dumps(selected, ensure_ascii=False, indent=2))
        return
    if args.json:
        print(compact(selected))
        return
    for key, value in selected.items():
        print(f"{key}={compact(value)}")


if __name__ == "__main__":
    main()
