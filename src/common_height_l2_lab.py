#!/usr/bin/env python3
"""Summarize bands-first selected physical L2 energy from selector-lab JSON."""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

from common_height_l2_bridge import maximum_closing_l2_exponent


def summarize(payload: dict[str, Any]) -> list[dict[str, float | int]]:
    block_sums: dict[tuple[int, float, int], complex] = defaultdict(complex)
    block_meta: dict[tuple[int, float, int], tuple[int, int]] = {}
    for row in payload["rows"]:
        key = (int(row["Y"]), float(row["height_exponent"]), int(row["block_id"]))
        block_sums[key] += complex(
            float(row["logarithmic_normalized_real"]),
            float(row["logarithmic_normalized_imag"]),
        )
        block_meta[key] = (int(row["Y"]), int(row["H"]))

    grouped: dict[tuple[int, float], list[tuple[complex, int]]] = defaultdict(list)
    for key, value in block_sums.items():
        y, tau, _ = key
        _, h = block_meta[key]
        grouped[(y, tau)].append((value, h))

    threshold = float(maximum_closing_l2_exponent())
    output: list[dict[str, float | int]] = []
    for (y, tau), entries in sorted(grouped.items()):
        h_values = {h for _, h in entries}
        if len(h_values) != 1:
            raise ValueError("group has nonconstant block length")
        h = h_values.pop()
        mean_normalized_square = sum(abs(value) ** 2 for value, _ in entries) / len(entries)
        projected_l2 = y * h * mean_normalized_square
        effective_exponent = math.log(max(projected_l2, 1e-300), y)
        output.append(
            {
                "Y": y,
                "height_exponent": tau,
                "H": h,
                "sampled_blocks": len(entries),
                "mean_normalized_square": mean_normalized_square,
                "projected_l2": projected_l2,
                "effective_l2_exponent": effective_exponent,
                "closing_l2_frontier": threshold,
                "projected_ratio_to_frontier": projected_l2 / y**threshold,
            }
        )
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path", type=Path)
    args = parser.parse_args()
    with args.json_path.open(encoding="utf-8") as stream:
        payload = json.load(stream)
    print(json.dumps(summarize(payload), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
