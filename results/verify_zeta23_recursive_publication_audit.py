#!/usr/bin/env python3
"""Structural checks for the recursive publication-theorem audit.

This checks the inventory and claim-state discipline.  It does not certify a
mathematical proof or establish literature novelty.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "results/ZETA23-RECURSIVE-PUBLICATION-THEOREM-AUDIT-2026-09-02.md"
CACHE = ROOT / "results/context/zeta23_recursive_publication_audit_v1.json"
REGISTRY = ROOT / "results/REDUCTION-REGISTRY.md"

ALLOWED_NOVELTY = {
    "IMPORTED",
    "LOCAL_PREDECESSOR",
    "PROJECT_SYNTHESIS",
    "NOVELTY_UNRESOLVED",
    "CANDIDATE_NEW",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CACHE.read_text(encoding="utf-8"))
    report = AUDIT.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")

    require(data["schema"] == "zeta23_recursive_publication_audit_v1", "bad schema")
    require(set(data["controlled_novelty_labels"]) == ALLOWED_NOVELTY, "label drift")

    global_status = data["global_status"]
    for key in ("riemann_hypothesis", "uniform_zero_free_strip", "sharp_four_cycle_bound"):
        require(global_status[key] == "OPEN", f"global claim drift: {key}")

    ids = [int(match.group(1)) for match in re.finditer(r"^\| R(\d+) \|", registry, re.M)]
    require(ids == list(range(1, 181)), "registry is not exactly contiguous R1-R180")
    inv = data["inventory"]
    require(inv["registry_rows"] == len(ids) == 180, "inventory row count drift")
    require(inv["first_id"] == "R1" and inv["last_id"] == "R180", "inventory endpoints drift")
    require(inv["ids_contiguous"] is True, "contiguity flag drift")

    packages = data["fixed_point_packages"]
    package_ids = [item["id"] for item in packages]
    require(len(package_ids) == len(set(package_ids)), "duplicate package id")
    require(len(packages) == 9, "fixed-point package count drift")

    for item in packages:
        require(item["novelty_status"] in ALLOWED_NOVELTY, f"bad novelty label: {item['id']}")
        require(item["nonclaim"].strip(), f"missing nonclaim: {item['id']}")
        for source in item["sources"]:
            require((ROOT / source).exists(), f"missing source for {item['id']}: {source}")
        if item["novelty_status"] == "CANDIDATE_NEW":
            require(item["requires_specialist_review"] is True, f"uncaveated candidate: {item['id']}")
        if item["mathematical_status"] == "PROOF_DRAFT":
            require(item["publication_tier"] == "INCUBATOR", f"proof draft promoted: {item['id']}")

    ranks = [item["rank"] for item in data["next_actions"]]
    require(ranks == list(range(1, len(ranks) + 1)), "next-action ranking drift")
    require("not a novelty certificate" in report.lower(), "report lost novelty disclaimer")
    for phrase in ("does **not** presently contain a proof of RH", "uniform zero-free", "sharp four-cycle"):
        require(phrase.lower() in report.lower(), f"report lost global nonclaim: {phrase}")

    print("PASS: recursive publication audit structure and claim-state discipline")
    print("NOTE: this checker does not validate theorem proofs or literature novelty")


if __name__ == "__main__":
    main()
