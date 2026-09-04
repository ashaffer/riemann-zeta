#!/usr/bin/env python3
"""Verify that the unrecoverable V4 digest record cannot certify live files."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POSTFLIGHT = ROOT / "results/context/zeta23_recursive_fixed_point_postflight_v1.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(POSTFLIGHT.read_text(encoding="utf-8"))
    snapshot = data["frozen_terminal_snapshot"]
    require(
        data["status"] == "HISTORICAL_COMPLETE_SNAPSHOT_UNATTACHED",
        "unattached V4 status drift",
    )
    require(snapshot["snapshot_scope"] == "HISTORICAL_UNATTACHED_DIGESTS", "scope drift")
    require(snapshot["archive_or_commit_id"] is None, "unverified archive identifier added")
    require("NOT_RECOVERABLE" in snapshot["attachment_status"], "recoverability drift")
    require("DO_NOT_COMPARE" in snapshot["current_file_policy"], "current-file firewall missing")
    require("not a replayable integrity certificate" in data["nonclaim"], "nonclaim missing")
    for name, digest in snapshot["sha256"].items():
        require(isinstance(name, str) and name, "unlabeled digest")
        require(
            isinstance(digest, str)
            and len(digest) == 64
            and all(character in "0123456789abcdef" for character in digest),
            f"invalid historical digest for {name}",
        )
    print("PASS: V4 digests are explicitly historical and unattached")
    print("NOTE: no current-file or frozen-byte integrity is certified")


if __name__ == "__main__":
    main()
