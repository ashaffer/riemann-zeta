#!/usr/bin/env python3
"""Verify and summarize the local rough-Voronoi selector diagnostic."""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from local_rough_voronoi_selector_lab import (  # noqa: E402
    BETA,
    BETA_MAX,
    KAPPA,
    SCHEMA,
    analyze,
    rational_power_floor,
    residue_moment_ledger,
)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def _close(left: float, right: float, scale: float = 1.0) -> bool:
    return abs(left - right) <= 2e-9 * max(scale, abs(left), abs(right))


def validate(payload: dict[str, object]) -> None:
    assert payload["schema"] == SCHEMA
    blocks = payload["blocks"]
    rows = payload["rows"]
    assert isinstance(blocks, list) and isinstance(rows, list)
    by_id: dict[int, dict[str, object]] = {}
    for block in blocks:
        block_id = int(block["block_id"])
        assert block_id not in by_id
        by_id[block_id] = block
        y = int(block["Y"])
        h = int(block["H"])
        q = int(block["q"])
        q_floor = max(2, rational_power_floor(y, BETA))
        q_cap = max(q_floor, rational_power_floor(y, BETA_MAX))
        assert int(block["q_floor"]) == q_floor
        assert int(block["q_cap"]) == q_cap
        assert q_floor < q <= min(h, q_cap)
        assert math.gcd(int(block["a"]), q) == 1
        assert int(block["lifted_a"]) % q == int(block["a"])
        reconstructed = abs(
            float(block["derivative_alpha"]) - int(block["lifted_a"]) / q
        )
        assert _close(
            reconstructed,
            float(block["dirichlet_error"]),
            float(block["dirichlet_bound"]),
        )
        assert reconstructed <= 1.0000002 * float(block["dirichlet_bound"])
        assert float(block["low_major_distance"]) > 1.0 / h
        shell = block["shell"]
        support = block["tent_support"]
        assert _is_prime(int(shell[0])) and _is_prime(int(shell[1]))
        assert float(shell[0]) <= float(support[0])
        assert float(support[1]) <= float(shell[1])
        assert all(bool(value) for value in block["certificates"].values())
        assert all(int(p) >= q for p in block["complete_cutoffs_P"])
        assert all(
            int(p) < q <= 2 * int(p)
            for p in block["included_crossing_cutoffs_P"]
        )

    row_cutoffs: dict[int, list[int]] = defaultdict(list)
    for row in rows:
        block = by_id[int(row["block_id"])]
        q = int(row["q"])
        h = int(row["H"])
        y = int(row["Y"])
        cutoff = int(row["cutoff_P"])
        row_cutoffs[int(row["block_id"])].append(cutoff)
        band_kind = str(row["band_kind"])
        if band_kind == "complete":
            assert cutoff >= q
        elif band_kind == "crossing":
            assert cutoff < q <= 2 * cutoff
        else:
            raise AssertionError("unknown band kind")
        assert q == int(block["q"])
        assert int(row["a"]) == int(block["a"])
        assert int(row["lifted_a"]) == int(block["lifted_a"])
        rational_abs = math.hypot(
            float(row["rational_normalized_real"]),
            float(row["rational_normalized_imag"]),
        )
        logarithmic_abs = math.hypot(
            float(row["logarithmic_normalized_real"]),
            float(row["logarithmic_normalized_imag"]),
        )
        assert _close(rational_abs, float(row["rational_normalized_abs"]))
        assert _close(
            logarithmic_abs, float(row["logarithmic_normalized_abs"])
        )
        l2 = float(row["residue_l2_squared_actual_mass"])
        corr_l2 = float(
            row["cyclic_correlation_l2_squared_actual_mass"]
        )
        assert _close(
            l2, float(row["zero_shift_correlation_actual_mass"])
        )
        assert _close(
            q * l2,
            float(row["all_frequency_second_moment_actual_mass"]),
        )
        assert _close(
            q * corr_l2,
            float(row["all_frequency_fourth_moment_actual_mass"]),
        )
        assert _close(q / h * l2, float(row["target_weighted_l2"]))
        assert _close(
            q / h**3 * corr_l2, float(row["target_weighted_l4"])
        )
        assert _close(
            rational_abs * y**KAPPA,
            float(row["target_scaled_rational"]),
        )
        assert _close(
            logarithmic_abs * y**KAPPA,
            float(row["target_scaled_logarithmic"]),
        )
        assert float(row["selected_fourier_from_residue_error"]) <= 1e-8

    for block_id, block in by_id.items():
        expected = [int(value) for value in block["complete_cutoffs_P"]]
        expected += [
            int(value) for value in block["included_crossing_cutoffs_P"]
        ]
        assert sorted(row_cutoffs[block_id]) == sorted(expected)

    # Independent normalization check for both finite Fourier identities.
    vector = [1.0, -2.0, 0.5, 0.5]
    ledger = residue_moment_ledger(vector)
    transforms = [
        sum(
            value
            * complex(
                math.cos(2.0 * math.pi * a * r / len(vector)),
                math.sin(2.0 * math.pi * a * r / len(vector)),
            )
            for r, value in enumerate(vector)
        )
        for a in range(len(vector))
    ]
    assert _close(
        sum(abs(value) ** 2 for value in transforms),
        len(vector) * ledger["residue_l2_squared"],
    )
    assert _close(
        sum(abs(value) ** 4 for value in transforms),
        len(vector) * ledger["cyclic_correlation_l2_squared"],
    )


def _quantile(values: list[float], probability: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    position = probability * (len(ordered) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return ordered[lower] * (1.0 - fraction) + ordered[upper] * fraction


def summarize(payload: dict[str, object]) -> list[dict[str, float | int]]:
    blocks_by_group: dict[tuple[int, float], list[dict[str, object]]] = (
        defaultdict(list)
    )
    rows_by_group: dict[tuple[int, float], list[dict[str, object]]] = (
        defaultdict(list)
    )
    rows_by_block: dict[int, list[dict[str, object]]] = defaultdict(list)
    for block in payload["blocks"]:
        blocks_by_group[(int(block["Y"]), float(block["height_exponent"]))].append(
            block
        )
    for row in payload["rows"]:
        key = (int(row["Y"]), float(row["height_exponent"]))
        rows_by_group[key].append(row)
        rows_by_block[int(row["block_id"])].append(row)

    result: list[dict[str, float | int]] = []
    for key in sorted(blocks_by_group):
        y, exponent = key
        blocks = blocks_by_group[key]
        rows = rows_by_group[key]
        h = float(blocks[0]["H"])
        q_over_h = [float(block["q"]) / float(block["H"]) for block in blocks]
        rational_tail: list[float] = []
        logarithmic_tail: list[float] = []
        block_l2: list[float] = []
        block_l4: list[float] = []
        for block in blocks:
            block_rows = rows_by_block[int(block["block_id"])]
            rational = sum(
                complex(
                    float(row["rational_normalized_real"]),
                    float(row["rational_normalized_imag"]),
                )
                for row in block_rows
            )
            logarithmic = sum(
                complex(
                    float(row["logarithmic_normalized_real"]),
                    float(row["logarithmic_normalized_imag"]),
                )
                for row in block_rows
            )
            rational_tail.append(abs(rational) * y**KAPPA)
            logarithmic_tail.append(abs(logarithmic) * y**KAPPA)
            block_l2.append(
                sum(float(row["target_weighted_l2"]) for row in block_rows)
            )
            block_l4.append(
                sum(float(row["target_weighted_l4"]) for row in block_rows)
            )
        projected_blocks = y / h
        projected_l2_ratio = (
            projected_blocks
            * (sum(block_l2) / len(block_l2))
            / y ** (1.0 - 2.0 * KAPPA)
        )
        projected_l4_ratio = (
            projected_blocks
            * (sum(block_l4) / len(block_l4))
            / y ** (1.0 - 4.0 * KAPPA)
        )
        result.append(
            {
                "Y": y,
                "height_exponent": exponent,
                "H": int(h),
                "blocks": len(blocks),
                "bands": len(rows),
                "empty_blocks": sum(not rows_by_block[int(b["block_id"])] for b in blocks),
                "q_over_H_p50": _quantile(q_over_h, 0.5),
                "q_over_H_p90": _quantile(q_over_h, 0.9),
                "q_over_H_max": max(q_over_h),
                "tail_rational_scaled_p50": _quantile(rational_tail, 0.5),
                "tail_rational_scaled_p90": _quantile(rational_tail, 0.9),
                "tail_rational_scaled_max": max(rational_tail),
                "tail_log_scaled_p50": _quantile(logarithmic_tail, 0.5),
                "tail_log_scaled_p90": _quantile(logarithmic_tail, 0.9),
                "tail_log_scaled_max": max(logarithmic_tail),
                "representative_projection_l2_target_ratio": projected_l2_ratio,
                "representative_projection_l4_target_ratio": projected_l4_ratio,
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    fresh = analyze([3000], [0.9, 1.2], block_samples=3)
    validate(fresh)
    if args.json:
        payload = json.loads(args.json.read_text(encoding="utf-8"))
        validate(payload)
        print(json.dumps(summarize(payload), indent=2, sort_keys=True))
    print("PASS: local rough-Voronoi selector normalization and scope")


if __name__ == "__main__":
    main()
