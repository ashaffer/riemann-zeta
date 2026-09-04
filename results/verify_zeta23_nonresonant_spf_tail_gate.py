#!/usr/bin/env python3
"""Independent replay entry point for the nonresonant SPF-tail gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from spf_tail_large_sieve_gate import build_countermodel, exponent_ledger  # noqa: E402


def main() -> None:
    ledger = exponent_ledger()
    model = build_countermodel()
    if ledger["cauchy_aggregate_exponent"] != "1":
        raise AssertionError("critical aggregate exponent changed")
    if not all(model["certificates"].values()):
        raise AssertionError("a finite-model certificate failed")
    if model["exact_deletion"]["aggregate_times_logP_over_Y"] <= 0.08:
        raise AssertionError("coherent obstruction is too small")
    if model["stage_square_function"]["coherent_over_cauchy_bound"] <= 0.7:
        raise AssertionError("stage Cauchy is not close enough to sharp")
    print("nonresonant SPF-tail information gate: PASS")
    print(
        json.dumps(
            {
                "energy_deficit": ledger["fixed_power_energy_deficit"],
                "deleted_centres": model["counts"]["deleted_centres"],
                "G2_over_Y": model["gap_energy"]["final_G2_over_Y"],
                "aggregate_logP_over_Y": model["exact_deletion"][
                    "aggregate_times_logP_over_Y"
                ],
                "coherent_over_stage_cauchy": model["stage_square_function"][
                    "coherent_over_cauchy_bound"
                ],
                "selected_over_frequency_rms": model["finite_group_spectrum"][
                    "selected_over_parseval_rms"
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
