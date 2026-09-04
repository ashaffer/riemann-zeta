#!/usr/bin/env python3
"""Read-only verifier for the canonical p=2 generation snapshot.

The output directory may be either the checked-in RHBridge source directory or
a scratch directory populated by the replay recipe.  Scratch files are hashed
under their canonical checked-in path labels, so a byte-for-byte replay has the
same aggregate digest without first overwriting repository sources.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


SCRIPT = Path(__file__).resolve()
REPOSITORY = SCRIPT.parent.parent
DEFAULT_MANIFEST = SCRIPT.with_name(
    "P2-CERTIFICATE-GENERATION-MANIFEST-2026-08-11.json"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_label(canonical_directory: str, path: Path) -> str:
    return f"{canonical_directory.rstrip('/')}/{path.name}"


def summarize(
    paths: list[Path], canonical_directory: str
) -> dict[str, int | str]:
    ordered = sorted(paths, key=lambda path: canonical_label(canonical_directory, path))
    path_set = hashlib.sha256()
    content_manifest = hashlib.sha256()
    byte_count = 0
    for path in ordered:
        label = canonical_label(canonical_directory, path)
        file_sha = sha256(path)
        path_set.update(f"{label}\n".encode("utf-8"))
        content_manifest.update(f"{file_sha}  {label}\n".encode("utf-8"))
        byte_count += path.stat().st_size
    return {
        "count": len(ordered),
        "bytes": byte_count,
        "path_set_sha256": path_set.hexdigest(),
        "content_manifest_sha256": content_manifest.hexdigest(),
    }


def compare_fields(
    scope: str,
    expected: dict[str, Any],
    observed: dict[str, Any],
    fields: tuple[str, ...],
    mismatches: list[dict[str, Any]],
) -> None:
    for field in fields:
        if expected[field] != observed[field]:
            mismatches.append(
                {
                    "scope": scope,
                    "field": field,
                    "expected": expected[field],
                    "observed": observed[field],
                }
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help=f"manifest to verify (default: {DEFAULT_MANIFEST})",
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        help=(
            "generated Lean directory; defaults to the manifest's canonical "
            "checked-in directory"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    output = manifest["expected_output"]
    canonical_directory = output["canonical_directory"]
    explicit_source_directory = args.source_dir is not None
    source_directory = (
        args.source_dir.resolve()
        if explicit_source_directory
        else (REPOSITORY / canonical_directory).resolve()
    )

    mismatches: list[dict[str, Any]] = []
    provenance_results: list[dict[str, Any]] = []
    for item in manifest["provenance_files"]:
        path = REPOSITORY / item["path"]
        observed = {
            "path": item["path"],
            "exists": path.is_file(),
            "bytes": path.stat().st_size if path.is_file() else None,
            "sha256": sha256(path) if path.is_file() else None,
        }
        provenance_results.append(observed)
        if not observed["exists"]:
            mismatches.append(
                {"scope": "provenance", "path": item["path"], "error": "missing"}
            )
            continue
        compare_fields(
            f"provenance:{item['path']}",
            item,
            observed,
            ("bytes", "sha256"),
            mismatches,
        )

    if not source_directory.is_dir():
        mismatches.append(
            {
                "scope": "outputs",
                "path": str(source_directory),
                "error": "source directory missing",
            }
        )
        lean_files: list[Path] = []
    else:
        lean_files = [
            path
            for path in source_directory.iterdir()
            if path.is_file() and path.suffix == ".lean"
        ]

    group_results: list[dict[str, Any]] = []
    membership: dict[str, list[str]] = {}
    aggregate_files: dict[str, Path] = {}
    summary_fields = (
        "count",
        "bytes",
        "path_set_sha256",
        "content_manifest_sha256",
    )
    for group in output["groups"]:
        pattern = re.compile(group["filename_regex"])
        paths = [path for path in lean_files if pattern.fullmatch(path.name)]
        observed = {"name": group["name"], **summarize(paths, canonical_directory)}
        group_results.append(observed)
        compare_fields(
            f"output_group:{group['name']}",
            group,
            observed,
            summary_fields,
            mismatches,
        )
        for path in paths:
            membership.setdefault(path.name, []).append(group["name"])
            aggregate_files[path.name] = path

    overlaps = {
        name: groups for name, groups in membership.items() if len(groups) != 1
    }
    if overlaps:
        mismatches.append(
            {"scope": "outputs", "field": "disjoint_groups", "observed": overlaps}
        )

    unmatched_lean_files = sorted(
        path.name for path in lean_files if path.name not in membership
    )
    if explicit_source_directory and unmatched_lean_files:
        mismatches.append(
            {
                "scope": "outputs",
                "field": "unmatched_lean_files",
                "error": (
                    "an explicit replay directory must contain only the "
                    "manifested generated Lean families"
                ),
                "observed": unmatched_lean_files,
            }
        )

    aggregate = summarize(list(aggregate_files.values()), canonical_directory)
    compare_fields(
        "output_aggregate",
        output["aggregate"],
        aggregate,
        summary_fields,
        mismatches,
    )

    report = {
        "schema_version": 1,
        "status": "ok" if not mismatches else "mismatch",
        "manifest": str(manifest_path),
        "source_directory": str(source_directory),
        "canonical_path_labels": canonical_directory,
        "explicit_source_directory": explicit_source_directory,
        "unmatched_lean_files_ignored": (
            0 if explicit_source_directory else len(unmatched_lean_files)
        ),
        "provenance_files_checked": len(provenance_results),
        "groups": group_results,
        "aggregate": aggregate,
        "mismatches": mismatches,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not mismatches else 1


if __name__ == "__main__":
    sys.exit(main())
