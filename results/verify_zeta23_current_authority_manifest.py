#!/usr/bin/env python3
"""Verify local byte integrity for the six current authority artifacts."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "results/context/zeta23_current_authority_manifest_v1.json"
sys.path.insert(0, str(ROOT / "src"))
from zeta23_proof_tree import load_current_authority_bundle


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    require(data["schema"] == "zeta23_current_authority_manifest_v1", "schema drift")
    require(data["scope"] == "LOCAL_WORKTREE_BYTES_NOT_COMMIT_BOUND", "scope drift")
    require(data["tree_or_archive_binding"] is None, "unsupported tree binding")
    artifacts = data["artifacts"]
    require(len(artifacts) == 6, "authority artifact count drift")
    require(len({item["role"] for item in artifacts}) == 6, "duplicate authority role")
    require(len({item["path"] for item in artifacts}) == 6, "duplicate authority path")
    for item in artifacts:
        path = (ROOT / item["path"]).resolve()
        require(path.is_relative_to(ROOT.resolve()), f"path escaped worktree: {item['role']}")
        require(path.is_file(), f"authority missing: {item['role']}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == item["sha256"], f"authority hash drift: {item['role']}")
    load_current_authority_bundle()
    require("not preserved by the recorded base commit" in data["nonclaim"], "durability nonclaim missing")
    print("PASS: six 2026-09-02 authority snapshot artifacts match the local manifest")
    print("NOTE: local hashes only; no commit/archive durability is claimed")


if __name__ == "__main__":
    main()
