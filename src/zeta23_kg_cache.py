#!/usr/bin/env python3
"""Compile and query the compact Z23G theorem graph.

The binary format uses interned UTF-8 strings, varints, packed enum bytes,
integer graph IDs, and LZMA2 compression.  It is losslessly decoded by this
file and needs no third-party package.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import lzma
import struct
import sys
from collections import deque
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/context/zeta23_kg_v2.source.json"
CACHE = ROOT / "results/context/zeta23_kg_v2.zkg"
MAGIC = b"Z23G"
SUPERSESSION_WARNING = (
    "WARNING: zeta23_kg_v2 is a historical August graph; "
    "use `python3 src/zeta23_correction_context.py resume` for current routing."
)

KINDS = ("goal", "invariant", "law", "theorem", "nogo", "gate", "hypothesis")
STATUS = ("proved", "open", "closed", "conditional")
STRENGTH = ("finite", "candidate", "coefficient", "equivalent", "meta")
RELATIONS = ("requires", "narrows", "blocked_by", "implies", "contradicts", "evidence", "supersedes", "alternative", "resolves")


def put_uvarint(out: bytearray, value: int) -> None:
    if value < 0:
        raise ValueError("uvarint is negative")
    while value >= 0x80:
        out.append((value & 0x7F) | 0x80)
        value >>= 7
    out.append(value)


def get_uvarint(data: bytes, pos: int) -> tuple[int, int]:
    value = 0
    shift = 0
    while True:
        byte = data[pos]
        pos += 1
        value |= (byte & 0x7F) << shift
        if byte < 0x80:
            return value, pos
        shift += 7
        if shift > 63:
            raise ValueError("oversize varint")


def zigzag(value: int) -> int:
    return value * 2 if value >= 0 else -value * 2 - 1


def unzigzag(value: int) -> int:
    return value // 2 if value % 2 == 0 else -(value // 2) - 1


def source() -> dict[str, Any]:
    with SOURCE.open(encoding="utf-8") as stream:
        return json.load(stream)


def validate(obj: dict[str, Any]) -> None:
    codes = [node[0] for node in obj["nodes"]]
    if len(codes) != len(set(codes)):
        raise ValueError("duplicate node code")
    known = set(codes)
    for node in obj["nodes"]:
        if node[1] not in KINDS or node[2] not in STATUS or node[3] not in STRENGTH:
            raise ValueError(f"bad enum in node {node[0]}")
    for left, relation, right in obj["edges"]:
        if left not in known or right not in known or relation not in RELATIONS:
            raise ValueError(f"bad edge {left},{relation},{right}")
    for key in ("live", "portfolio"):
        if not set(obj[key]) <= known:
            raise ValueError(f"unknown node in {key}")
    if not {row[0] for row in obj.get("priors_bp", [])} <= known:
        raise ValueError("unknown node in priors_bp")


def compile_graph(obj: dict[str, Any]) -> bytes:
    validate(obj)
    strings: list[str] = []
    string_id: dict[str, int] = {}

    def sid(value: str) -> int:
        if value not in string_id:
            string_id[value] = len(strings)
            strings.append(value)
        return string_id[value]

    for key, value in obj["meta"].items():
        sid(key)
        sid(value)
    for code, _, _, unit in obj["constants"]:
        sid(code)
        sid(unit)
    for code, path in obj["artifacts"]:
        sid(code)
        sid(path)
    for code, _, _, _, claim, note, artifact in obj["nodes"]:
        sid(code)
        sid(claim)
        sid(note)
        sid(artifact)

    out = bytearray(MAGIC)
    put_uvarint(out, obj["version"])
    put_uvarint(out, len(strings))
    for value in strings:
        raw = value.encode("utf-8")
        put_uvarint(out, len(raw))
        out.extend(raw)

    put_uvarint(out, len(obj["meta"]))
    for key, value in obj["meta"].items():
        put_uvarint(out, sid(key))
        put_uvarint(out, sid(value))

    put_uvarint(out, len(obj["constants"]))
    for code, numerator, denominator, unit in obj["constants"]:
        put_uvarint(out, sid(code))
        put_uvarint(out, zigzag(numerator))
        put_uvarint(out, denominator)
        put_uvarint(out, sid(unit))

    put_uvarint(out, len(obj["artifacts"]))
    for code, path in obj["artifacts"]:
        put_uvarint(out, sid(code))
        put_uvarint(out, sid(path))

    node_index = {node[0]: i for i, node in enumerate(obj["nodes"])}
    put_uvarint(out, len(obj["nodes"]))
    for code, kind, status, strength, claim, note, artifact in obj["nodes"]:
        put_uvarint(out, sid(code))
        flags = KINDS.index(kind) | (STATUS.index(status) << 3) | (STRENGTH.index(strength) << 5)
        out.extend(struct.pack("<H", flags))
        put_uvarint(out, sid(claim))
        put_uvarint(out, sid(note))
        put_uvarint(out, sid(artifact))

    put_uvarint(out, len(obj["edges"]))
    for left, relation, right in obj["edges"]:
        put_uvarint(out, node_index[left])
        out.append(RELATIONS.index(relation))
        put_uvarint(out, node_index[right])

    for key in ("live", "portfolio"):
        put_uvarint(out, len(obj[key]))
        for code in obj[key]:
            put_uvarint(out, node_index[code])
    put_uvarint(out, len(obj.get("priors_bp", [])))
    for code, truth_bp, accessible_bp in obj.get("priors_bp", []):
        put_uvarint(out, node_index[code])
        put_uvarint(out, truth_bp)
        put_uvarint(out, accessible_bp)
    return bytes(out)


def build() -> None:
    raw = compile_graph(source())
    payload = lzma.compress(raw, format=lzma.FORMAT_XZ, preset=9 | lzma.PRESET_EXTREME)
    CACHE.write_bytes(payload)
    print(f"built {CACHE.relative_to(ROOT)} raw={len(raw)} compressed={len(payload)} sha256={hashlib.sha256(payload).hexdigest()}")


def decode() -> dict[str, Any]:
    packed = CACHE.read_bytes()
    data = lzma.decompress(packed)
    if not data.startswith(MAGIC):
        raise ValueError("bad Z23G magic")
    pos = len(MAGIC)
    version, pos = get_uvarint(data, pos)
    count, pos = get_uvarint(data, pos)
    strings: list[str] = []
    for _ in range(count):
        size, pos = get_uvarint(data, pos)
        strings.append(data[pos : pos + size].decode("utf-8"))
        pos += size

    meta_count, pos = get_uvarint(data, pos)
    meta: dict[str, str] = {}
    for _ in range(meta_count):
        key, pos = get_uvarint(data, pos)
        value, pos = get_uvarint(data, pos)
        meta[strings[key]] = strings[value]

    constant_count, pos = get_uvarint(data, pos)
    constants = []
    for _ in range(constant_count):
        code, pos = get_uvarint(data, pos)
        numerator, pos = get_uvarint(data, pos)
        denominator, pos = get_uvarint(data, pos)
        unit, pos = get_uvarint(data, pos)
        constants.append([strings[code], unzigzag(numerator), denominator, strings[unit]])

    artifact_count, pos = get_uvarint(data, pos)
    artifacts: dict[str, str] = {}
    for _ in range(artifact_count):
        code, pos = get_uvarint(data, pos)
        path, pos = get_uvarint(data, pos)
        artifacts[strings[code]] = strings[path]

    node_count, pos = get_uvarint(data, pos)
    nodes = []
    for _ in range(node_count):
        code, pos = get_uvarint(data, pos)
        flags = struct.unpack_from("<H", data, pos)[0]
        pos += 2
        claim, pos = get_uvarint(data, pos)
        note, pos = get_uvarint(data, pos)
        artifact, pos = get_uvarint(data, pos)
        nodes.append({
            "code": strings[code],
            "kind": KINDS[flags & 0x7],
            "status": STATUS[(flags >> 3) & 0x3],
            "strength": STRENGTH[(flags >> 5) & 0x7],
            "claim": strings[claim],
            "note": strings[note],
            "artifact": strings[artifact],
        })

    edge_count, pos = get_uvarint(data, pos)
    edges = []
    for _ in range(edge_count):
        left, pos = get_uvarint(data, pos)
        relation = data[pos]
        pos += 1
        right, pos = get_uvarint(data, pos)
        edges.append([left, RELATIONS[relation], right])

    groups = []
    for _ in range(2):
        size, pos = get_uvarint(data, pos)
        group = []
        for _ in range(size):
            index, pos = get_uvarint(data, pos)
            group.append(index)
        groups.append(group)
    prior_count, pos = get_uvarint(data, pos)
    priors: dict[int, list[int]] = {}
    for _ in range(prior_count):
        index, pos = get_uvarint(data, pos)
        truth_bp, pos = get_uvarint(data, pos)
        accessible_bp, pos = get_uvarint(data, pos)
        priors[index] = [truth_bp, accessible_bp]
    if pos != len(data):
        raise ValueError(f"trailing bytes: {len(data)-pos}")
    return {
        "version": version,
        "meta": meta,
        "constants": constants,
        "artifacts": artifacts,
        "nodes": nodes,
        "edges": edges,
        "live": groups[0],
        "portfolio": groups[1],
        "priors_bp": priors,
        "sha256": hashlib.sha256(packed).hexdigest(),
        "bytes": len(packed),
    }


def selected_indices(graph: dict[str, Any], codes: Iterable[str], use_live: bool, use_portfolio: bool, closure: bool) -> list[int]:
    by_code = {node["code"]: i for i, node in enumerate(graph["nodes"])}
    chosen = set(graph["live"] if use_live else []) | set(graph["portfolio"] if use_portfolio else [])
    for code in codes:
        if code not in by_code:
            raise SystemExit(f"unknown node: {code}")
        chosen.add(by_code[code])
    if not chosen:
        chosen.update(graph["live"])
    if closure:
        outgoing: dict[int, list[int]] = {}
        for left, _, right in graph["edges"]:
            outgoing.setdefault(left, []).append(right)
        queue = deque(chosen)
        while queue:
            left = queue.popleft()
            for right in outgoing.get(left, []):
                if right not in chosen:
                    chosen.add(right)
                    queue.append(right)
    return sorted(chosen)


def render(graph: dict[str, Any], indices: list[int], as_json: bool) -> None:
    wanted = set(indices)
    nodes = [graph["nodes"][i] for i in indices]
    edges = [
        [graph["nodes"][left]["code"], relation, graph["nodes"][right]["code"]]
        for left, relation, right in graph["edges"]
        if left in wanted and right in wanted
    ]
    if as_json:
        print(json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, separators=(",", ":")))
        return
    for node in nodes:
        print(f"[{node['code']}] {node['kind']}/{node['status']}/{node['strength']}")
        print(f"  {node['claim']}")
        if node["note"]:
            print(f"  NOTE: {node['note']}")
        if node["artifact"]:
            print(f"  REF: {graph['artifacts'].get(node['artifact'], node['artifact'])}")
        index = next(i for i, candidate in enumerate(graph["nodes"]) if candidate is node)
        if index in graph["priors_bp"]:
            truth_bp, accessible_bp = graph["priors_bp"][index]
            print(f"  PRIOR: truth={truth_bp/100:.2f}% accessible={accessible_bp/100:.2f}%")
        for left, relation, right in edges:
            if left == node["code"]:
                print(f"  {relation.upper()}: {right}")


def verify() -> None:
    graph = decode()
    obj = source()
    validate(obj)
    expected = compile_graph(obj)
    actual = lzma.decompress(CACHE.read_bytes())
    if expected != actual:
        raise SystemExit("cache is stale: run `python3 src/zeta23_kg_cache.py build`")
    print(f"OK version={graph['version']} nodes={len(graph['nodes'])} edges={len(graph['edges'])} bytes={graph['bytes']} sha256={graph['sha256']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build")
    sub.add_parser("verify")
    query = sub.add_parser("query")
    query.add_argument("codes", nargs="*")
    query.add_argument("--live", action="store_true")
    query.add_argument("--portfolio", action="store_true")
    query.add_argument("--closure", action="store_true")
    query.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.command == "build":
        build()
    elif args.command == "verify":
        verify()
    else:
        print(SUPERSESSION_WARNING, file=sys.stderr)
        graph = decode()
        indices = selected_indices(graph, args.codes, args.live, args.portfolio, args.closure)
        render(graph, indices, args.json)


if __name__ == "__main__":
    main()
