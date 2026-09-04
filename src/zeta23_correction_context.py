#!/usr/bin/env python3
"""Compile, verify, and selectively read the canonical Z23C correction ledger.

The UTF-8 ``.zctx`` file is the model-readable reload artifact.  JSON is a
deterministic interoperability mirror; Z23V is an uncompressed random-access
integer-vector runtime index.  Neither mirror is an independent mathematical
authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

from zeta23_vector_context import (
    K_INVARIANTS,
    K_NEXT_TARGETS,
    K_OPERATIONAL_DEBT,
    K_PROOF_DEBTS,
    K_SOURCES,
    Z23VReader,
    encode_z23v,
)


ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT / "results/context"
SOURCE = CONTEXT / "zeta23_correction_bundle_v1.zctx"
JSON_MIRROR = CONTEXT / "zeta23_correction_bundle_v1.json"
VECTOR_INDEX = CONTEXT / "zeta23_correction_bundle_v1.z23v"

MAGIC = "Z23C"
FORMAT_VERSION = "1"
PAYLOAD_SCHEMA = "zeta23_correction_bundle_v1"
GENERATOR_VERSION = "zeta23_correction_context.py/1"
PATH_ALIASES = {"R": "results/", "L": "lean/rhbridge/"}
CORRECTION_STATES = {
    "FIXED",
    "FIXED_WITH_RELEASE_DEBT",
    "FIXED_AS_NONCLAIM",
    "FIXED_LOCALLY_WITH_DURABILITY_DEBT",
}
GLOBAL_KEYS = (
    "uniform_zero_free_strip",
    "riemann_hypothesis",
    "strip_to_rh_amplifier",
    "sharp_four_cycle_bound",
)
TOP_LEVEL_KEYS = (
    "schema",
    "date",
    "human_authority",
    "lean_authorities",
    "global_status",
    "sync_contract",
    "corrections",
    "surviving_exact_invariants",
    "open_proof_debts",
    "next_admissible_targets",
    "operational_debt",
    "resumption_state",
    "reload_vectors",
    "verification",
    "sources",
)
CORRECTION_OPTION_KEYS = {
    "trust",
    "analytic_classification_source",
    "formal_scope",
    "remaining",
}
THEOREM_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
CORRECTION_RE = re.compile(r"C[0-9]{2}\Z")
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
RESUMPTION_KEYS = (
    "objective",
    "analytic_target",
    "active_frontier",
    "frontier_status",
    "route_invariant",
    "representation_status",
    "working_hypotheses",
    "prohibitions",
    "selection_policy",
)
RELOAD_VECTOR_NAMES = ("resume", "math", "ops", "formal", "sources", "all")
STATIC_RECORD_REFS = {"M", "G", "Y", "R", "I", "D", "N", "O", "V", "S"}


class ContextFormatError(ValueError):
    """The compact ledger or one of its generated mirrors is invalid."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ContextFormatError(message)


def _escape(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("\t", "\\t")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
    )


def _unescape(value: str, line_number: int) -> str:
    output: list[str] = []
    index = 0
    escapes = {"\\": "\\", "t": "\t", "n": "\n", "r": "\r"}
    while index < len(value):
        character = value[index]
        if character != "\\":
            output.append(character)
            index += 1
            continue
        _require(index + 1 < len(value), f"line {line_number}: trailing escape")
        escaped = value[index + 1]
        _require(
            escaped in escapes,
            f"line {line_number}: unknown escape \\{escaped}",
        )
        output.append(escapes[escaped])
        index += 2
    return "".join(output)


def _fields(line: str, line_number: int) -> list[str]:
    return [_unescape(field, line_number) for field in line.split("\t")]


def _line(*fields: str) -> str:
    return "\t".join(_escape(field) for field in fields)


def _expand_path(value: str, aliases: dict[str, str], line_number: int) -> str:
    if value.startswith("="):
        expanded = value[1:]
    else:
        match = re.fullmatch(r"@([A-Z]):(.+)", value)
        _require(match is not None, f"line {line_number}: malformed path reference")
        alias, suffix = match.groups()
        _require(alias in aliases, f"line {line_number}: undefined path alias {alias}")
        expanded = aliases[alias] + suffix
    path = PurePosixPath(expanded)
    _require(expanded != "", f"line {line_number}: empty path")
    _require(not path.is_absolute(), f"line {line_number}: absolute path forbidden")
    _require(".." not in path.parts, f"line {line_number}: path traversal forbidden")
    _require(path.as_posix() == expanded, f"line {line_number}: noncanonical path")
    return expanded


def _abbreviate_path(value: str) -> str:
    path = PurePosixPath(value)
    _require(not path.is_absolute() and ".." not in path.parts, f"unsafe path: {value}")
    for alias, prefix in PATH_ALIASES.items():
        if value.startswith(prefix) and len(value) > len(prefix):
            return f"@{alias}:{value[len(prefix):]}"
    return f"={value}"


def _semantic_bytes(data: dict[str, Any]) -> bytes:
    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def semantic_sha256(data: dict[str, Any]) -> str:
    return hashlib.sha256(_semantic_bytes(data)).hexdigest()


def _validate_date(value: str, label: str) -> None:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise ContextFormatError(f"invalid {label}: {value}") from error
    _require(parsed.isoformat() == value, f"noncanonical {label}: {value}")


def _validate_root_path(value: str, label: str) -> None:
    path = PurePosixPath(value)
    _require(value != "", f"empty {label}")
    _require(not path.is_absolute(), f"absolute {label} forbidden")
    _require(".." not in path.parts, f"path traversal in {label}")
    _require(path.as_posix() == value, f"noncanonical {label}")
    _require(
        value.startswith("results/") or value.startswith("lean/rhbridge/"),
        f"{label} lies outside licensed roots",
    )


def validate_semantics(data: dict[str, Any]) -> None:
    """Reject lossy, ambiguous, or path-unsafe semantic packets."""

    _require(tuple(data) == TOP_LEVEL_KEYS, "top-level key/order drift")
    _require(data["schema"] == PAYLOAD_SCHEMA, "payload schema drift")
    _validate_date(data["date"], "bundle date")

    _validate_root_path(data["human_authority"], "human authority")
    _require(len(data["lean_authorities"]) > 0, "no Lean authorities")
    _require(
        len(data["lean_authorities"]) == len(set(data["lean_authorities"])),
        "duplicate Lean authority",
    )
    for path in data["lean_authorities"]:
        _validate_root_path(path, "Lean authority")

    _require(tuple(data["global_status"]) == GLOBAL_KEYS, "global-status key drift")
    sync = data["sync_contract"]
    _require(
        tuple(sync) == ("correction_ids", "formal_scope", "nonclaim", "verifier"),
        "sync-contract key/order drift",
    )
    _validate_root_path(sync["verifier"], "synchronization verifier")

    corrections = data["corrections"]
    ids = [correction["id"] for correction in corrections]
    _require(ids == sync["correction_ids"], "correction ID ledger drift")
    _require(len(ids) == len(set(ids)), "duplicate correction ID")
    _require(all(CORRECTION_RE.fullmatch(item) for item in ids), "bad correction ID")
    for correction in corrections:
        allowed = {"id", "state", "claim", "lean"} | CORRECTION_OPTION_KEYS
        _require(set(correction) <= allowed, f"unknown key in {correction['id']}")
        _require(correction["state"] in CORRECTION_STATES, f"bad state in {correction['id']}")
        _require(correction["claim"] != "", f"empty claim in {correction['id']}")
        _require("lean" in correction, f"missing Lean list in {correction['id']}")
        _require(
            len(correction["lean"]) == len(set(correction["lean"])),
            f"duplicate Lean theorem in {correction['id']}",
        )
        _require(
            all(THEOREM_RE.fullmatch(name) for name in correction["lean"]),
            f"bad Lean theorem in {correction['id']}",
        )
        if "analytic_classification_source" in correction:
            _validate_root_path(
                correction["analytic_classification_source"],
                f"analytic source for {correction['id']}",
            )

    for key in (
        "surviving_exact_invariants",
        "open_proof_debts",
        "next_admissible_targets",
        "operational_debt",
        "sources",
    ):
        values = data[key]
        _require(all(isinstance(value, str) and value for value in values), f"bad {key}")
        _require(len(values) == len(set(values)), f"duplicate entry in {key}")
    for path in data["sources"]:
        _validate_root_path(path, "source")

    resumption = data["resumption_state"]
    _require(tuple(resumption) == RESUMPTION_KEYS, "resumption-state key/order drift")
    for key in (
        "objective",
        "analytic_target",
        "active_frontier",
        "frontier_status",
        "route_invariant",
        "representation_status",
        "selection_policy",
    ):
        _require(isinstance(resumption[key], str) and resumption[key], f"bad resumption {key}")
    for key in ("working_hypotheses", "prohibitions"):
        values = resumption[key]
        _require(all(isinstance(value, str) and value for value in values), f"bad resumption {key}")
        _require(len(values) == len(set(values)) and values, f"duplicate/empty resumption {key}")

    reload_vectors = data["reload_vectors"]
    _require(tuple(reload_vectors) == RELOAD_VECTOR_NAMES, "reload-vector name/order drift")
    for name, references in reload_vectors.items():
        _require(references and len(references) == len(set(references)), f"bad reload vector {name}")
        for reference in references:
            _require(
                reference == "*"
                or reference in STATIC_RECORD_REFS
                or CORRECTION_RE.fullmatch(reference) is not None,
                f"bad record reference {reference} in reload vector {name}",
            )
    _require(reload_vectors["all"] == ["*"], "all reload vector must use the wildcard")
    for required in ("G", "Y", "R", "D", "N"):
        _require(required in reload_vectors["resume"], f"resume vector omits {required}")

    verification = data["verification"]
    _require(
        tuple(verification)
        == (
            "observed_date",
            "synchronization_verifier",
            "current_authority_manifest_verifier",
            "focused_pytest",
            "full_pytest",
            "lean_aggregate",
            "correction_guard_axioms",
        ),
        "verification key/order drift",
    )
    _validate_date(verification["observed_date"], "verification date")
    axioms = verification["correction_guard_axioms"]
    _require(len(axioms) == len(set(axioms)) and len(axioms) > 0, "bad axiom ledger")


def parse_zctx(text: str) -> dict[str, Any]:
    """Decode and validate one self-checking Z23C/1 text ledger."""

    _require(text.endswith("\n"), "Z23C source must end with LF")
    _require("\r" not in text, "Z23C source must use LF, not CRLF")
    raw_lines = text[:-1].split("\n")
    _require(raw_lines and all(raw_lines), "blank or missing Z23C record")
    records = [_fields(line, index) for index, line in enumerate(raw_lines, 1)]

    header = records[0]
    _require(len(header) == 4, "bad Z23C header arity")
    _require(
        header[:3] == [MAGIC, FORMAT_VERSION, PAYLOAD_SCHEMA],
        "bad Z23C magic/version/schema header",
    )
    bundle_date = header[3]
    _validate_date(bundle_date, "bundle date")

    aliases: dict[str, str] = {}
    human_authority: str | None = None
    lean_authorities: list[str] | None = None
    global_status: dict[str, str] | None = None
    sync_contract: dict[str, Any] | None = None
    raw_corrections: list[dict[str, Any]] = []
    correction_index: dict[str, dict[str, Any]] = {}
    invariants: list[str] = []
    proof_debts: list[str] = []
    next_targets: list[str] = []
    operational_debt: list[str] = []
    resumption_state: dict[str, Any] | None = None
    working_hypotheses: list[str] = []
    prohibitions: list[str] = []
    reload_vectors: dict[str, list[str]] = {}
    verification: dict[str, Any] | None = None
    sources: list[str] = []
    expected_semantic_sha: str | None = None

    singleton_tags: set[str] = set()
    list_targets = {
        "I": invariants,
        "D": proof_debts,
        "N": next_targets,
        "O": operational_debt,
    }

    for line_number, fields in enumerate(records[1:], 2):
        tag = fields[0]
        _require(tag != MAGIC, f"line {line_number}: duplicate header")
        if tag == "P":
            _require(len(fields) == 3, f"line {line_number}: bad P arity")
            alias, prefix = fields[1:]
            _require(re.fullmatch(r"[A-Z]", alias) is not None, f"line {line_number}: bad alias")
            _require(alias not in aliases, f"line {line_number}: duplicate alias")
            _require(prefix.endswith("/"), f"line {line_number}: alias must end in /")
            _require(".." not in PurePosixPath(prefix).parts, f"line {line_number}: unsafe alias")
            aliases[alias] = prefix
        elif tag == "H":
            _require(len(fields) == 2, f"line {line_number}: bad H arity")
            _require(tag not in singleton_tags, f"line {line_number}: duplicate H")
            human_authority = _expand_path(fields[1], aliases, line_number)
            singleton_tags.add(tag)
        elif tag == "LA":
            _require(len(fields) >= 2, f"line {line_number}: empty LA")
            _require(tag not in singleton_tags, f"line {line_number}: duplicate LA")
            lean_authorities = [
                _expand_path(value, aliases, line_number) for value in fields[1:]
            ]
            singleton_tags.add(tag)
        elif tag == "G":
            _require(len(fields) == 5, f"line {line_number}: bad G arity")
            _require(tag not in singleton_tags, f"line {line_number}: duplicate G")
            global_status = dict(zip(GLOBAL_KEYS, fields[1:], strict=True))
            singleton_tags.add(tag)
        elif tag == "Y":
            _require(len(fields) == 4, f"line {line_number}: bad Y arity")
            _require(tag not in singleton_tags, f"line {line_number}: duplicate Y")
            sync_contract = {
                "correction_ids": [],
                "formal_scope": fields[1],
                "nonclaim": fields[2],
                "verifier": _expand_path(fields[3], aliases, line_number),
            }
            singleton_tags.add(tag)
        elif tag == "YI":
            _require(len(fields) >= 2, f"line {line_number}: empty YI")
            _require(tag not in singleton_tags, f"line {line_number}: duplicate YI")
            _require(sync_contract is not None, f"line {line_number}: YI before Y")
            sync_contract["correction_ids"] = fields[1:]
            singleton_tags.add(tag)
        elif tag == "C":
            _require(len(fields) == 4, f"line {line_number}: bad C arity")
            correction_id, state, claim = fields[1:]
            _require(CORRECTION_RE.fullmatch(correction_id) is not None, f"line {line_number}: bad C ID")
            _require(correction_id not in correction_index, f"line {line_number}: duplicate C ID")
            correction = {
                "id": correction_id,
                "state": state,
                "claim": claim,
                "modifiers": {},
                "lean": None,
            }
            raw_corrections.append(correction)
            correction_index[correction_id] = correction
        elif tag in {"CT", "CA", "CF", "CR"}:
            _require(len(fields) == 3, f"line {line_number}: bad {tag} arity")
            correction_id, value = fields[1:]
            _require(correction_id in correction_index, f"line {line_number}: modifier before C")
            key = {
                "CT": "trust",
                "CA": "analytic_classification_source",
                "CF": "formal_scope",
                "CR": "remaining",
            }[tag]
            modifiers = correction_index[correction_id]["modifiers"]
            _require(key not in modifiers, f"line {line_number}: duplicate {tag}")
            if tag == "CA":
                value = _expand_path(value, aliases, line_number)
            modifiers[key] = value
        elif tag == "CL":
            _require(len(fields) >= 3, f"line {line_number}: empty CL")
            correction_id = fields[1]
            _require(correction_id in correction_index, f"line {line_number}: CL before C")
            correction = correction_index[correction_id]
            _require(correction["lean"] is None, f"line {line_number}: duplicate CL")
            correction["lean"] = fields[2:]
        elif tag in list_targets:
            _require(len(fields) == 2, f"line {line_number}: bad {tag} arity")
            list_targets[tag].append(fields[1])
        elif tag == "RS":
            _require(len(fields) == 8, f"line {line_number}: bad RS arity")
            _require(tag not in singleton_tags, f"line {line_number}: duplicate RS")
            resumption_state = {
                "objective": fields[1],
                "analytic_target": fields[2],
                "active_frontier": fields[3],
                "frontier_status": fields[4],
                "route_invariant": fields[5],
                "representation_status": fields[6],
                "working_hypotheses": working_hypotheses,
                "prohibitions": prohibitions,
                "selection_policy": fields[7],
            }
            singleton_tags.add(tag)
        elif tag == "RH":
            _require(len(fields) == 2, f"line {line_number}: bad RH arity")
            _require(resumption_state is not None, f"line {line_number}: RH before RS")
            working_hypotheses.append(fields[1])
        elif tag == "RX":
            _require(len(fields) == 2, f"line {line_number}: bad RX arity")
            _require(resumption_state is not None, f"line {line_number}: RX before RS")
            prohibitions.append(fields[1])
        elif tag == "RV":
            _require(len(fields) >= 3, f"line {line_number}: empty RV")
            name = fields[1]
            _require(name not in reload_vectors, f"line {line_number}: duplicate RV {name}")
            reload_vectors[name] = fields[2:]
        elif tag == "V":
            _require(len(fields) == 7, f"line {line_number}: bad V arity")
            _require(tag not in singleton_tags, f"line {line_number}: duplicate V")
            verification = {
                "observed_date": fields[1],
                "synchronization_verifier": fields[2],
                "current_authority_manifest_verifier": fields[3],
                "focused_pytest": fields[4],
                "full_pytest": fields[5],
                "lean_aggregate": fields[6],
                "correction_guard_axioms": [],
            }
            singleton_tags.add(tag)
        elif tag == "VA":
            _require(len(fields) >= 2, f"line {line_number}: empty VA")
            _require(verification is not None, f"line {line_number}: VA before V")
            _require(not verification["correction_guard_axioms"], f"line {line_number}: duplicate VA")
            verification["correction_guard_axioms"] = fields[1:]
        elif tag == "S":
            _require(len(fields) == 2, f"line {line_number}: bad S arity")
            sources.append(_expand_path(fields[1], aliases, line_number))
        elif tag == "X":
            _require(len(fields) == 2, f"line {line_number}: bad X arity")
            _require(line_number == len(records), f"line {line_number}: trailing record after X")
            _require(expected_semantic_sha is None, f"line {line_number}: duplicate X")
            _require(SHA256_RE.fullmatch(fields[1]) is not None, f"line {line_number}: bad X digest")
            expected_semantic_sha = fields[1]
        else:
            raise ContextFormatError(f"line {line_number}: unknown opcode {tag!r}")

    _require(aliases == PATH_ALIASES, "path-alias table drift")
    _require(human_authority is not None, "missing H record")
    _require(lean_authorities is not None, "missing LA record")
    _require(global_status is not None, "missing G record")
    _require(sync_contract is not None and "YI" in singleton_tags, "missing Y/YI record")
    _require(resumption_state is not None, "missing RS record")
    _require(working_hypotheses and prohibitions, "empty RH/RX resumption ledger")
    _require(reload_vectors, "missing RV records")
    _require(verification is not None and verification["correction_guard_axioms"], "missing V/VA record")
    _require(expected_semantic_sha is not None, "missing terminal X record")

    corrections: list[dict[str, Any]] = []
    for raw in raw_corrections:
        correction = {
            "id": raw["id"],
            "state": raw["state"],
            "claim": raw["claim"],
        }
        correction.update(raw["modifiers"])
        correction["lean"] = raw["lean"] or []
        corrections.append(correction)

    data = {
        "schema": PAYLOAD_SCHEMA,
        "date": bundle_date,
        "human_authority": human_authority,
        "lean_authorities": lean_authorities,
        "global_status": global_status,
        "sync_contract": sync_contract,
        "corrections": corrections,
        "surviving_exact_invariants": invariants,
        "open_proof_debts": proof_debts,
        "next_admissible_targets": next_targets,
        "operational_debt": operational_debt,
        "resumption_state": resumption_state,
        "reload_vectors": reload_vectors,
        "verification": verification,
        "sources": sources,
    }
    validate_semantics(data)
    actual_semantic_sha = semantic_sha256(data)
    _require(
        actual_semantic_sha == expected_semantic_sha,
        f"semantic digest mismatch: expected {expected_semantic_sha}, got {actual_semantic_sha}",
    )
    return data


def _correction_lines(correction: dict[str, Any]) -> list[str]:
    correction_id = correction["id"]
    lines = [_line("C", correction_id, correction["state"], correction["claim"])]
    if "trust" in correction:
        lines.append(_line("CT", correction_id, correction["trust"]))
    if "analytic_classification_source" in correction:
        lines.append(
            _line(
                "CA",
                correction_id,
                _abbreviate_path(correction["analytic_classification_source"]),
            )
        )
    if "formal_scope" in correction:
        lines.append(_line("CF", correction_id, correction["formal_scope"]))
    if "remaining" in correction:
        lines.append(_line("CR", correction_id, correction["remaining"]))
    if correction["lean"]:
        lines.append(_line("CL", correction_id, *correction["lean"]))
    return lines


def render_zctx(data: dict[str, Any]) -> str:
    """Render canonical Z23C/1 bytes from a semantic packet."""

    validate_semantics(data)
    lines = [_line(MAGIC, FORMAT_VERSION, PAYLOAD_SCHEMA, data["date"])]
    for alias, prefix in PATH_ALIASES.items():
        lines.append(_line("P", alias, prefix))
    lines.append(_line("H", _abbreviate_path(data["human_authority"])))
    lines.append(
        _line("LA", *(_abbreviate_path(path) for path in data["lean_authorities"]))
    )
    lines.append(_line("G", *(data["global_status"][key] for key in GLOBAL_KEYS)))
    sync = data["sync_contract"]
    lines.append(
        _line(
            "Y",
            sync["formal_scope"],
            sync["nonclaim"],
            _abbreviate_path(sync["verifier"]),
        )
    )
    lines.append(_line("YI", *sync["correction_ids"]))
    for correction in data["corrections"]:
        lines.extend(_correction_lines(correction))
    for value in data["surviving_exact_invariants"]:
        lines.append(_line("I", value))
    for value in data["open_proof_debts"]:
        lines.append(_line("D", value))
    for value in data["next_admissible_targets"]:
        lines.append(_line("N", value))
    for value in data["operational_debt"]:
        lines.append(_line("O", value))
    resumption = data["resumption_state"]
    lines.append(
        _line(
            "RS",
            resumption["objective"],
            resumption["analytic_target"],
            resumption["active_frontier"],
            resumption["frontier_status"],
            resumption["route_invariant"],
            resumption["representation_status"],
            resumption["selection_policy"],
        )
    )
    for value in resumption["working_hypotheses"]:
        lines.append(_line("RH", value))
    for value in resumption["prohibitions"]:
        lines.append(_line("RX", value))
    for name, references in data["reload_vectors"].items():
        lines.append(_line("RV", name, *references))
    verification = data["verification"]
    lines.append(
        _line(
            "V",
            verification["observed_date"],
            verification["synchronization_verifier"],
            verification["current_authority_manifest_verifier"],
            verification["focused_pytest"],
            verification["full_pytest"],
            verification["lean_aggregate"],
        )
    )
    lines.append(_line("VA", *verification["correction_guard_axioms"]))
    for path in data["sources"]:
        lines.append(_line("S", _abbreviate_path(path)))
    lines.append(_line("X", semantic_sha256(data)))
    return "\n".join(lines) + "\n"


def _vector_bytes(data: dict[str, Any], source_bytes: bytes) -> bytes:
    return encode_z23v(
        data,
        source_sha256=hashlib.sha256(source_bytes).hexdigest(),
        semantic_sha256=semantic_sha256(data),
    )


def mirror_object(
    data: dict[str, Any], source_bytes: bytes, vector_bytes: bytes
) -> dict[str, Any]:
    """Add derived generation metadata to the semantic JSON projection."""

    output: dict[str, Any] = {
        "schema": data["schema"],
        "date": data["date"],
        "generated": {
            "canonical_source": SOURCE.relative_to(ROOT).as_posix(),
            "canonical_sha256": hashlib.sha256(source_bytes).hexdigest(),
            "semantic_sha256": semantic_sha256(data),
            "format": f"{MAGIC}/{FORMAT_VERSION}",
            "generator": f"src/{Path(__file__).name}",
            "generator_version": GENERATOR_VERSION,
            "runtime_index": VECTOR_INDEX.relative_to(ROOT).as_posix(),
            "runtime_sha256": hashlib.sha256(vector_bytes).hexdigest(),
            "runtime_format": "Z23V/1",
            "runtime_access": "RANDOM_ACCESS_TYPED_INTEGER_VECTORS_NO_WHOLE_FILE_DECOMPRESSION",
        },
    }
    output.update({key: data[key] for key in TOP_LEVEL_KEYS[2:]})
    return output


def mirror_json_bytes(
    data: dict[str, Any], source_bytes: bytes, vector_bytes: bytes
) -> bytes:
    return (
        json.dumps(
            mirror_object(data, source_bytes, vector_bytes),
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    ).encode("utf-8")


def _load_source() -> tuple[dict[str, Any], bytes]:
    source_bytes = SOURCE.read_bytes()
    try:
        source_text = source_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ContextFormatError("Z23C source is not UTF-8") from error
    data = parse_zctx(source_text)
    _require(render_zctx(data).encode("utf-8") == source_bytes, "noncanonical Z23C bytes")
    return data, source_bytes


def load_verified() -> dict[str, Any]:
    """Load the audit source after exact JSON and Z23V mirror checks."""

    data, source_bytes = _load_source()
    expected_vector = _vector_bytes(data, source_bytes)
    expected_json = mirror_json_bytes(data, source_bytes, expected_vector)
    _require(JSON_MIRROR.is_file(), "JSON mirror missing; run build")
    _require(JSON_MIRROR.read_bytes() == expected_json, "JSON mirror stale; run build")
    _require(VECTOR_INDEX.is_file(), "Z23V runtime index missing; run build")
    _require(VECTOR_INDEX.read_bytes() == expected_vector, "Z23V runtime index stale; run build")
    with Z23VReader(VECTOR_INDEX) as reader:
        decoded = reader.verify_full()
        _require(decoded == data, "Z23V full decode differs from Z23C semantics")
        _require(reader.source_sha256 == hashlib.sha256(source_bytes).digest(), "Z23V source digest drift")
    return data


def build_mirrors() -> tuple[int, int, int]:
    data, source_bytes = _load_source()
    vector_bytes = _vector_bytes(data, source_bytes)
    json_bytes = mirror_json_bytes(data, source_bytes, vector_bytes)
    JSON_MIRROR.write_bytes(json_bytes)
    VECTOR_INDEX.write_bytes(vector_bytes)
    return len(source_bytes), len(json_bytes), len(vector_bytes)


def _query_lines(reader: Z23VReader, correction_ids: Iterable[str]) -> str:
    requested = list(correction_ids)
    _require(requested, "query requires at least one correction ID")
    _require(len(requested) == len(set(requested)), "duplicate query correction ID")
    lines = [_line("Z23Q", FORMAT_VERSION, reader.semantic_sha256.hex())]
    global_status = reader.global_status()
    lines.append(_line("G", *(global_status[key] for key in GLOBAL_KEYS)))
    sync = reader.sync_contract()
    lines.append(_line("Y", sync["formal_scope"], sync["nonclaim"]))
    for correction_id in requested:
        _require(correction_id in sync["correction_ids"], f"unknown correction ID: {correction_id}")
        lines.extend(_correction_lines(reader.correction(correction_id)))
    return "\n".join(lines) + "\n"


def _resumption_lines(state: dict[str, Any]) -> list[str]:
    lines = [
        _line(
            "RS",
            state["objective"],
            state["analytic_target"],
            state["active_frontier"],
            state["frontier_status"],
            state["route_invariant"],
            state["representation_status"],
            state["selection_policy"],
        )
    ]
    lines.extend(_line("RH", value) for value in state["working_hypotheses"])
    lines.extend(_line("RX", value) for value in state["prohibitions"])
    return lines


def _selected_record_lines(reader: Z23VReader, reference: str) -> list[str]:
    if reference == "M":
        meta = reader.meta()
        return [
            _line("H", _abbreviate_path(meta["human_authority"])),
            _line("LA", *(_abbreviate_path(path) for path in meta["lean_authorities"])),
        ]
    if reference == "G":
        state = reader.global_status()
        return [_line("G", *(state[key] for key in GLOBAL_KEYS))]
    if reference == "Y":
        sync = reader.sync_contract()
        return [
            _line("Y", sync["formal_scope"], sync["nonclaim"]),
            _line("YI", *sync["correction_ids"]),
        ]
    if CORRECTION_RE.fullmatch(reference):
        return _correction_lines(reader.correction(reference))
    if reference == "I":
        return [_line("I", value) for value in reader.string_list(K_INVARIANTS)]
    if reference == "D":
        return [_line("D", value) for value in reader.string_list(K_PROOF_DEBTS)]
    if reference == "N":
        return [_line("N", value) for value in reader.string_list(K_NEXT_TARGETS)]
    if reference == "O":
        return [_line("O", value) for value in reader.string_list(K_OPERATIONAL_DEBT)]
    if reference == "R":
        return _resumption_lines(reader.resumption_state())
    if reference == "V":
        verification = reader.verification()
        return [
            _line(
                "V",
                verification["observed_date"],
                verification["synchronization_verifier"],
                verification["current_authority_manifest_verifier"],
                verification["focused_pytest"],
                verification["full_pytest"],
                verification["lean_aggregate"],
            ),
            _line("VA", *verification["correction_guard_axioms"]),
        ]
    if reference == "S":
        return [_line("S", _abbreviate_path(path)) for path in reader.string_list(K_SOURCES)]
    raise ContextFormatError(f"unsupported selected record reference: {reference}")


def _reload_vector_lines(reader: Z23VReader, name: str) -> str:
    vectors = reader.reload_vectors()
    _require(name in vectors, f"unknown reload vector: {name}")
    references = vectors[name]
    if references == ["*"]:
        return render_zctx(reader.decode_all())
    lines = [_line("Z23R", FORMAT_VERSION, name, reader.semantic_sha256.hex())]
    for reference in references:
        lines.extend(_selected_record_lines(reader, reference))
    return "\n".join(lines) + "\n"


def _report_selected_read(reader: Z23VReader, selection: str) -> None:
    print(
        f"Z23V selection={selection} verification_scope=SELECTED_RECORDS "
        f"bytes_read={reader.bytes_read}/{reader.file_size}",
        file=sys.stderr,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("build", help="regenerate JSON and Z23V mirrors")
    subparsers.add_parser("verify", help="check source and both mirrors exactly")
    subparsers.add_parser("show", help="print the canonical model-readable ledger")
    subparsers.add_parser("resume", help="load the small lossy working-state vector")
    query = subparsers.add_parser("query", help="random-access corrections or named vector")
    query.add_argument("correction_ids", nargs="*", metavar="CXX")
    query.add_argument("--vector", choices=RELOAD_VECTOR_NAMES)
    subparsers.add_parser("vectors", help="list named random-access reload vectors")
    subparsers.add_parser("stats", help="report encoded byte sizes")
    args = parser.parse_args()

    if args.command == "build":
        source_size, json_size, vector_size = build_mirrors()
        print(f"BUILT zctx={source_size} json={json_size} z23v={vector_size}")
    elif args.command == "verify":
        data = load_verified()
        print(
            f"PASS {MAGIC}/{FORMAT_VERSION} corrections={len(data['corrections'])} "
            f"semantic_sha256={semantic_sha256(data)}"
        )
    elif args.command == "show":
        data = load_verified()
        print(render_zctx(data), end="")
    elif args.command == "resume":
        with Z23VReader(VECTOR_INDEX) as reader:
            print(_reload_vector_lines(reader, "resume"), end="")
            _report_selected_read(reader, "resume")
    elif args.command == "query":
        _require(
            bool(args.vector) != bool(args.correction_ids),
            "query requires either correction IDs or --vector, but not both",
        )
        with Z23VReader(VECTOR_INDEX) as reader:
            if args.vector:
                print(_reload_vector_lines(reader, args.vector), end="")
                selection = args.vector
            else:
                print(_query_lines(reader, args.correction_ids), end="")
                selection = ",".join(args.correction_ids)
            _report_selected_read(reader, selection)
    elif args.command == "vectors":
        with Z23VReader(VECTOR_INDEX) as reader:
            for name, references in reader.reload_vectors().items():
                print(f"{name}={' '.join(references)}")
            _report_selected_read(reader, "vector-directory")
    elif args.command == "stats":
        load_verified()
        source_size = SOURCE.stat().st_size
        json_size = JSON_MIRROR.stat().st_size
        vector_size = VECTOR_INDEX.stat().st_size
        print(f"zctx_bytes={source_size}")
        print(f"json_bytes={json_size}")
        print(f"z23v_bytes={vector_size}")
        print(f"zctx_vs_json={source_size / json_size:.3f}")
        print(f"z23v_vs_json={vector_size / json_size:.3f}")


if __name__ == "__main__":
    main()
