#!/usr/bin/env python3
"""Lossless random-access typed-vector index for ZETA23 correction context.

``Z23V/1`` is deliberately uncompressed.  A reader seeks to a fixed directory
entry, reads one unsigned-integer vector, and resolves only the referenced
strings.  Exact equations and theorem names remain recoverable; no embedding
or other lossy representation is used.
"""

from __future__ import annotations

import hashlib
import json
import re
import struct
import zlib
from pathlib import Path
from typing import Any, BinaryIO, Iterable


MAGIC = b"Z23V"
VERSION = 1
FLAGS = 0
HEADER = struct.Struct("<4sHHIIIQQQQQ32s32s32s")
DIRECTORY_ENTRY = struct.Struct("<HHIQQQ")
STRING_ENTRY = struct.Struct("<QII")

K_META = 1
K_GLOBAL = 2
K_SYNC = 3
K_CORRECTION = 4
K_INVARIANTS = 5
K_PROOF_DEBTS = 6
K_NEXT_TARGETS = 7
K_OPERATIONAL_DEBT = 8
K_VERIFICATION = 9
K_SOURCES = 10
K_RESUMPTION = 11
K_RELOAD_VECTORS = 12

GLOBAL_KEYS = (
    "uniform_zero_free_strip",
    "riemann_hypothesis",
    "strip_to_rh_amplifier",
    "sharp_four_cycle_bound",
)
CORRECTION_RE = re.compile(r"C([0-9]{2})\Z")
STATIC_REFERENCE_KINDS = {
    "M": K_META,
    "G": K_GLOBAL,
    "Y": K_SYNC,
    "I": K_INVARIANTS,
    "D": K_PROOF_DEBTS,
    "N": K_NEXT_TARGETS,
    "O": K_OPERATIONAL_DEBT,
    "V": K_VERIFICATION,
    "S": K_SOURCES,
    "R": K_RESUMPTION,
}
KIND_REFERENCES = {kind: reference for reference, kind in STATIC_REFERENCE_KINDS.items()}


class VectorFormatError(ValueError):
    """The Z23V vector index is malformed or corrupt."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise VectorFormatError(message)


def record_reference_code(reference: str) -> int:
    """Encode a compact symbolic record reference as one integer."""

    if reference == "*":
        return 0
    if reference in STATIC_REFERENCE_KINDS:
        return STATIC_REFERENCE_KINDS[reference] << 16
    match = CORRECTION_RE.fullmatch(reference)
    _require(match is not None, f"bad record reference: {reference}")
    return (K_CORRECTION << 16) | int(match.group(1))


def code_record_reference(code: int) -> str:
    """Decode one integer record reference without touching string storage."""

    if code == 0:
        return "*"
    kind, key = code >> 16, code & 0xFFFF
    if kind == K_CORRECTION:
        _require(1 <= key <= 99, "bad correction reference key")
        return f"C{key:02d}"
    _require(key == 0 and kind in KIND_REFERENCES, "bad static record reference")
    return KIND_REFERENCES[kind]


def _semantic_bytes(data: dict[str, Any]) -> bytes:
    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _all_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _all_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from _all_strings(item)


def _uvarint(value: int) -> bytes:
    _require(value >= 0, "negative unsigned vector entry")
    output = bytearray()
    while value >= 0x80:
        output.append((value & 0x7F) | 0x80)
        value >>= 7
    output.append(value)
    return bytes(output)


def _vector(values: Iterable[int]) -> bytes:
    return b"".join(_uvarint(value) for value in values)


def _decode_vector(payload: bytes) -> list[int]:
    values: list[int] = []
    value = 0
    shift = 0
    for byte in payload:
        value |= (byte & 0x7F) << shift
        if byte & 0x80:
            shift += 7
            _require(shift <= 63, "uvarint exceeds 64 bits")
        else:
            values.append(value)
            value = 0
            shift = 0
    _require(shift == 0, "truncated uvarint")
    return values


def _record_digest(kind: int, key: int, payload: bytes) -> int:
    digest = hashlib.sha256(struct.pack("<HH", kind, key) + payload).digest()
    return int.from_bytes(digest[:8], "little")


def _list_vector(values: list[str], sid: dict[str, int]) -> list[int]:
    return [len(values), *(sid[value] for value in values)]


def _build_records(data: dict[str, Any], sid: dict[str, int]) -> list[tuple[int, int, bytes]]:
    records: list[tuple[int, int, bytes]] = []
    records.append(
        (
            K_META,
            0,
            _vector(
                [
                    sid[data["schema"]],
                    sid[data["date"]],
                    sid[data["human_authority"]],
                    *_list_vector(data["lean_authorities"], sid),
                ]
            ),
        )
    )
    records.append(
        (
            K_GLOBAL,
            0,
            _vector(sid[data["global_status"][key]] for key in GLOBAL_KEYS),
        )
    )
    sync = data["sync_contract"]
    records.append(
        (
            K_SYNC,
            0,
            _vector(
                [
                    sid[sync["formal_scope"]],
                    sid[sync["nonclaim"]],
                    sid[sync["verifier"]],
                    *_list_vector(sync["correction_ids"], sid),
                ]
            ),
        )
    )
    for correction in data["corrections"]:
        match = CORRECTION_RE.fullmatch(correction["id"])
        _require(match is not None, f"bad correction ID: {correction['id']}")
        ordinal = int(match.group(1))
        values = [
            sid[correction["state"]],
            sid[correction["claim"]],
            sid[correction["trust"]] if "trust" in correction else 0,
            (
                sid[correction["analytic_classification_source"]]
                if "analytic_classification_source" in correction
                else 0
            ),
            sid[correction["formal_scope"]] if "formal_scope" in correction else 0,
            sid[correction["remaining"]] if "remaining" in correction else 0,
            *_list_vector(correction["lean"], sid),
        ]
        records.append((K_CORRECTION, ordinal, _vector(values)))
    for kind, key in (
        (K_INVARIANTS, "surviving_exact_invariants"),
        (K_PROOF_DEBTS, "open_proof_debts"),
        (K_NEXT_TARGETS, "next_admissible_targets"),
        (K_OPERATIONAL_DEBT, "operational_debt"),
    ):
        records.append((kind, 0, _vector(_list_vector(data[key], sid))))
    verification = data["verification"]
    records.append(
        (
            K_VERIFICATION,
            0,
            _vector(
                [
                    sid[verification["observed_date"]],
                    sid[verification["synchronization_verifier"]],
                    sid[verification["current_authority_manifest_verifier"]],
                    sid[verification["focused_pytest"]],
                    sid[verification["full_pytest"]],
                    sid[verification["lean_aggregate"]],
                    *_list_vector(verification["correction_guard_axioms"], sid),
                ]
            ),
        )
    )
    records.append((K_SOURCES, 0, _vector(_list_vector(data["sources"], sid))))
    resumption = data["resumption_state"]
    records.append(
        (
            K_RESUMPTION,
            0,
            _vector(
                [
                    sid[resumption["objective"]],
                    sid[resumption["analytic_target"]],
                    sid[resumption["active_frontier"]],
                    sid[resumption["frontier_status"]],
                    sid[resumption["route_invariant"]],
                    sid[resumption["representation_status"]],
                    sid[resumption["selection_policy"]],
                    *_list_vector(resumption["working_hypotheses"], sid),
                    *_list_vector(resumption["prohibitions"], sid),
                ]
            ),
        )
    )
    reload_values: list[int] = [len(data["reload_vectors"])]
    for name, references in data["reload_vectors"].items():
        reload_values.extend(
            [
                sid[name],
                len(references),
                *(record_reference_code(reference) for reference in references),
            ]
        )
    records.append((K_RELOAD_VECTORS, 0, _vector(reload_values)))
    records.sort(key=lambda record: (record[0], record[1]))
    _require(
        len({(kind, key) for kind, key, _ in records}) == len(records),
        "duplicate typed-vector record",
    )
    return records


def encode_z23v(
    data: dict[str, Any], *, source_sha256: str, semantic_sha256: str
) -> bytes:
    """Compile semantic context into deterministic random-access vectors."""

    try:
        source_digest = bytes.fromhex(source_sha256)
        semantic_digest = bytes.fromhex(semantic_sha256)
    except ValueError as error:
        raise VectorFormatError("invalid input SHA-256") from error
    _require(len(source_digest) == 32 and len(semantic_digest) == 32, "bad SHA-256 length")
    _require(
        hashlib.sha256(_semantic_bytes(data)).digest() == semantic_digest,
        "semantic SHA-256 does not match data",
    )

    strings_found = set(_all_strings(data))
    strings_found.update(data["reload_vectors"])
    strings = sorted(strings_found)
    _require(strings and all(strings), "empty or absent vector string table")
    sid = {value: index + 1 for index, value in enumerate(strings)}
    records = _build_records(data, sid)
    payloads = [payload for _, _, payload in records]

    directory_offset = HEADER.size
    payload_offset = directory_offset + len(records) * DIRECTORY_ENTRY.size
    payload_cursor = payload_offset
    directory = bytearray()
    for kind, key, payload in records:
        directory.extend(
            DIRECTORY_ENTRY.pack(
                kind,
                key,
                0,
                payload_cursor,
                len(payload),
                _record_digest(kind, key, payload),
            )
        )
        payload_cursor += len(payload)
    payload_region = b"".join(payloads)

    string_index_offset = payload_cursor
    string_blob_offset = string_index_offset + len(strings) * STRING_ENTRY.size
    string_blob = bytearray()
    string_index = bytearray()
    for value in strings:
        encoded = value.encode("utf-8")
        absolute_offset = string_blob_offset + len(string_blob)
        string_index.extend(
            STRING_ENTRY.pack(absolute_offset, len(encoded), zlib.crc32(encoded))
        )
        string_blob.extend(encoded)

    body = bytes(directory) + payload_region + bytes(string_index) + bytes(string_blob)
    file_size = HEADER.size + len(body)
    header = HEADER.pack(
        MAGIC,
        VERSION,
        HEADER.size,
        FLAGS,
        len(records),
        len(strings),
        directory_offset,
        payload_offset,
        string_index_offset,
        string_blob_offset,
        file_size,
        source_digest,
        semantic_digest,
        hashlib.sha256(body).digest(),
    )
    return header + body


class Z23VReader:
    """Seek-based reader that decodes only requested typed vectors/strings."""

    def __init__(self, path: Path):
        self.path = path
        self._stream: BinaryIO = path.open("rb")
        self.bytes_read = 0
        self._entry_cache: dict[tuple[int, int], tuple[int, int, int]] = {}
        self._string_cache: dict[int, str] = {}
        raw_header = self._read_at(0, HEADER.size)
        (
            magic,
            version,
            header_size,
            flags,
            self.record_count,
            self.string_count,
            self.directory_offset,
            self.payload_offset,
            self.string_index_offset,
            self.string_blob_offset,
            self.file_size,
            self.source_sha256,
            self.semantic_sha256,
            self.body_sha256,
        ) = HEADER.unpack(raw_header)
        _require(magic == MAGIC, "bad Z23V magic")
        _require(version == VERSION, "unsupported Z23V version")
        _require(header_size == HEADER.size and flags == FLAGS, "bad Z23V header")
        _require(self.path.stat().st_size == self.file_size, "Z23V file-size mismatch")
        _require(self.record_count > 0 and self.string_count > 0, "empty Z23V index")
        _require(self.record_count <= 10000 and self.string_count <= 1000000, "Z23V count cap exceeded")
        _require(self.directory_offset == HEADER.size, "bad Z23V directory offset")
        _require(
            self.payload_offset
            == self.directory_offset + self.record_count * DIRECTORY_ENTRY.size,
            "bad Z23V payload offset",
        )
        _require(
            self.payload_offset <= self.string_index_offset <= self.string_blob_offset <= self.file_size,
            "nonmonotone Z23V regions",
        )
        _require(
            self.string_blob_offset
            == self.string_index_offset + self.string_count * STRING_ENTRY.size,
            "bad Z23V string-index extent",
        )

    def close(self) -> None:
        self._stream.close()

    def __enter__(self) -> "Z23VReader":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def _read_at(self, offset: int, length: int) -> bytes:
        _require(offset >= 0 and length >= 0, "negative Z23V read")
        self._stream.seek(offset)
        payload = self._stream.read(length)
        self.bytes_read += len(payload)
        _require(len(payload) == length, "truncated Z23V read")
        return payload

    def _entry_at(self, index: int) -> tuple[int, int, int, int, int, int]:
        _require(0 <= index < self.record_count, "directory index out of range")
        offset = self.directory_offset + index * DIRECTORY_ENTRY.size
        return DIRECTORY_ENTRY.unpack(self._read_at(offset, DIRECTORY_ENTRY.size))

    def _find_entry(self, kind: int, key: int) -> tuple[int, int, int]:
        cached = self._entry_cache.get((kind, key))
        if cached is not None:
            return cached
        low, high = 0, self.record_count
        target = (kind, key)
        while low < high:
            middle = (low + high) // 2
            entry = self._entry_at(middle)
            current = (entry[0], entry[1])
            if current < target:
                low = middle + 1
            else:
                high = middle
        _require(low < self.record_count, f"missing vector record {target}")
        kind_found, key_found, flags, offset, length, digest = self._entry_at(low)
        _require((kind_found, key_found) == target, f"missing vector record {target}")
        _require(flags == 0, f"unsupported vector record flags for {target}")
        _require(
            self.payload_offset <= offset
            and offset + length <= self.string_index_offset,
            f"vector record {target} escapes payload region",
        )
        result = (offset, length, digest)
        self._entry_cache[target] = result
        return result

    def vector(self, kind: int, key: int = 0) -> list[int]:
        offset, length, expected_digest = self._find_entry(kind, key)
        payload = self._read_at(offset, length)
        _require(
            _record_digest(kind, key, payload) == expected_digest,
            f"vector record {(kind, key)} digest mismatch",
        )
        return _decode_vector(payload)

    def string(self, string_id: int) -> str:
        cached = self._string_cache.get(string_id)
        if cached is not None:
            return cached
        _require(1 <= string_id <= self.string_count, "string ID out of range")
        index_offset = self.string_index_offset + (string_id - 1) * STRING_ENTRY.size
        offset, length, expected_crc = STRING_ENTRY.unpack(
            self._read_at(index_offset, STRING_ENTRY.size)
        )
        _require(
            self.string_blob_offset <= offset and offset + length <= self.file_size,
            "string entry escapes blob",
        )
        encoded = self._read_at(offset, length)
        _require(zlib.crc32(encoded) == expected_crc, "string CRC mismatch")
        try:
            value = encoded.decode("utf-8")
        except UnicodeDecodeError as error:
            raise VectorFormatError("vector string is not UTF-8") from error
        _require(value != "", "empty vector string")
        self._string_cache[string_id] = value
        return value

    def _strings(self, vector: list[int]) -> list[str]:
        return [self.string(string_id) for string_id in vector]

    def _counted_strings(self, vector: list[int], start: int) -> tuple[list[str], int]:
        _require(start < len(vector), "missing vector list count")
        count = vector[start]
        end = start + 1 + count
        _require(end <= len(vector), "truncated vector list")
        return self._strings(vector[start + 1 : end]), end

    def meta(self) -> dict[str, Any]:
        vector = self.vector(K_META)
        _require(len(vector) >= 4, "bad meta vector")
        lean, end = self._counted_strings(vector, 3)
        _require(end == len(vector), "trailing meta vector entries")
        schema, bundle_date, human = self._strings(vector[:3])
        return {
            "schema": schema,
            "date": bundle_date,
            "human_authority": human,
            "lean_authorities": lean,
        }

    def global_status(self) -> dict[str, str]:
        vector = self.vector(K_GLOBAL)
        _require(len(vector) == len(GLOBAL_KEYS), "bad global-status vector")
        return dict(zip(GLOBAL_KEYS, self._strings(vector), strict=True))

    def sync_contract(self) -> dict[str, Any]:
        vector = self.vector(K_SYNC)
        _require(len(vector) >= 4, "bad sync vector")
        ids, end = self._counted_strings(vector, 3)
        _require(end == len(vector), "trailing sync vector entries")
        formal_scope, nonclaim, verifier = self._strings(vector[:3])
        return {
            "correction_ids": ids,
            "formal_scope": formal_scope,
            "nonclaim": nonclaim,
            "verifier": verifier,
        }

    def correction(self, correction_id: str) -> dict[str, Any]:
        match = CORRECTION_RE.fullmatch(correction_id)
        _require(match is not None, f"bad correction ID: {correction_id}")
        vector = self.vector(K_CORRECTION, int(match.group(1)))
        _require(len(vector) >= 7, f"bad correction vector: {correction_id}")
        state, claim = self._strings(vector[:2])
        correction: dict[str, Any] = {"id": correction_id, "state": state, "claim": claim}
        for index, key in (
            (2, "trust"),
            (3, "analytic_classification_source"),
            (4, "formal_scope"),
            (5, "remaining"),
        ):
            if vector[index] != 0:
                correction[key] = self.string(vector[index])
        lean, end = self._counted_strings(vector, 6)
        _require(end == len(vector), f"trailing correction vector: {correction_id}")
        correction["lean"] = lean
        return correction

    def string_list(self, kind: int) -> list[str]:
        vector = self.vector(kind)
        values, end = self._counted_strings(vector, 0)
        _require(end == len(vector), f"trailing list vector: {kind}")
        return values

    def verification(self) -> dict[str, Any]:
        vector = self.vector(K_VERIFICATION)
        _require(len(vector) >= 7, "bad verification vector")
        axioms, end = self._counted_strings(vector, 6)
        _require(end == len(vector), "trailing verification vector entries")
        scalar = self._strings(vector[:6])
        return {
            "observed_date": scalar[0],
            "synchronization_verifier": scalar[1],
            "current_authority_manifest_verifier": scalar[2],
            "focused_pytest": scalar[3],
            "full_pytest": scalar[4],
            "lean_aggregate": scalar[5],
            "correction_guard_axioms": axioms,
        }

    def resumption_state(self) -> dict[str, Any]:
        vector = self.vector(K_RESUMPTION)
        _require(len(vector) >= 9, "bad resumption vector")
        scalar = self._strings(vector[:7])
        hypotheses, cursor = self._counted_strings(vector, 7)
        prohibitions, end = self._counted_strings(vector, cursor)
        _require(end == len(vector), "trailing resumption vector entries")
        return {
            "objective": scalar[0],
            "analytic_target": scalar[1],
            "active_frontier": scalar[2],
            "frontier_status": scalar[3],
            "route_invariant": scalar[4],
            "representation_status": scalar[5],
            "working_hypotheses": hypotheses,
            "prohibitions": prohibitions,
            "selection_policy": scalar[6],
        }

    def reload_vectors(self) -> dict[str, list[str]]:
        vector = self.vector(K_RELOAD_VECTORS)
        _require(vector, "empty reload-vector record")
        count = vector[0]
        cursor = 1
        output: dict[str, list[str]] = {}
        for _ in range(count):
            _require(cursor + 2 <= len(vector), "truncated named reload vector")
            name = self.string(vector[cursor])
            member_count = vector[cursor + 1]
            cursor += 2
            end = cursor + member_count
            _require(end <= len(vector), f"truncated reload vector {name}")
            _require(name not in output, f"duplicate reload vector {name}")
            output[name] = [code_record_reference(code) for code in vector[cursor:end]]
            cursor = end
        _require(cursor == len(vector), "trailing named reload-vector entries")
        return output

    def decode_all(self) -> dict[str, Any]:
        meta = self.meta()
        sync = self.sync_contract()
        data = {
            "schema": meta["schema"],
            "date": meta["date"],
            "human_authority": meta["human_authority"],
            "lean_authorities": meta["lean_authorities"],
            "global_status": self.global_status(),
            "sync_contract": sync,
            "corrections": [self.correction(item) for item in sync["correction_ids"]],
            "surviving_exact_invariants": self.string_list(K_INVARIANTS),
            "open_proof_debts": self.string_list(K_PROOF_DEBTS),
            "next_admissible_targets": self.string_list(K_NEXT_TARGETS),
            "operational_debt": self.string_list(K_OPERATIONAL_DEBT),
            "resumption_state": self.resumption_state(),
            "reload_vectors": self.reload_vectors(),
            "verification": self.verification(),
            "sources": self.string_list(K_SOURCES),
        }
        _require(
            hashlib.sha256(_semantic_bytes(data)).digest() == self.semantic_sha256,
            "decoded semantic SHA-256 mismatch",
        )
        return data

    def verify_full(self) -> dict[str, Any]:
        body = self._read_at(HEADER.size, self.file_size - HEADER.size)
        _require(hashlib.sha256(body).digest() == self.body_sha256, "Z23V body SHA-256 mismatch")
        previous = (-1, -1)
        for index in range(self.record_count):
            kind, key, flags, offset, length, digest = self._entry_at(index)
            _require((kind, key) > previous, "unsorted or duplicate Z23V directory")
            previous = (kind, key)
            _require(flags == 0, "unsupported Z23V directory flags")
            _require(
                self.payload_offset <= offset and offset + length <= self.string_index_offset,
                "Z23V directory record escapes payload region",
            )
            payload = self._read_at(offset, length)
            _require(_record_digest(kind, key, payload) == digest, "Z23V record digest mismatch")
        data = self.decode_all()
        expected_records = len(data["corrections"]) + 11
        _require(self.record_count == expected_records, "unexpected Z23V record set")
        return data
