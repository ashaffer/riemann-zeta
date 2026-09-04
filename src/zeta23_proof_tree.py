#!/usr/bin/env python3
"""Compile and query the historical Z23P tree and dated routing snapshot.

The v3 Z23P records are a 2026-08-15 historical proof IR:
definitions, exact targets, implication directions, proof kernels, blockers,
audits, and then-admissible next actions.  A bare ``resume`` reads the
verified 2026-09-02 route snapshot; the live next action is in the canonical
correction context.  Explicit node/frontier queries still inspect v3.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import lzma
from collections import deque
from datetime import date
from pathlib import Path
from typing import Any, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "results/context/zeta23_proof_tree_v3.seed.json"
CACHE = ROOT / "results/context/zeta23_proof_tree_v3.zpt"
CURRENT_CACHES = {
    "route": ROOT / "results/context/zeta23_post_synthesis_decision_path_v1.json",
    "adapter": ROOT / "results/context/zeta23_r105_r116_r73_adapter_audit_v1.json",
    "closure": ROOT / "results/context/zeta23_correction_closure_v1.json",
}
CURRENT_REPORTS = {
    "route": ROOT / "results/ZETA23-POST-SYNTHESIS-DECISION-PATH-2026-09-02.md",
    "adapter": ROOT / "results/ZETA23-R105-R116-R73-ADAPTER-INTEGRITY-AUDIT-2026-09-02.md",
    "closure": ROOT / "results/ZETA23-CORRECTION-CLOSURE-AND-FAITHFULNESS-TRILEMMA-2026-09-02.md",
}
CURRENT_SCHEMAS = {
    "route": "zeta23_post_synthesis_decision_path_v1",
    "adapter": "zeta23_r105_r116_r73_adapter_audit_v1",
    "closure": "zeta23_correction_closure_v1",
}
CURRENT_ROUTING = CURRENT_CACHES["route"]
CURRENT_AUTHORITY_MANIFEST = ROOT / "results/context/zeta23_current_authority_manifest_v1.json"
CURRENT_RELOAD_INDEX = ROOT / "results/context/zeta23_correction_bundle_v1.z23v"
CURRENT_RELOAD_COMMAND = "python3 src/zeta23_correction_context.py resume"
MAGIC = b"Z23P"

KINDS = ("goal", "route", "gate", "fact", "nogo", "hypothesis", "invariant")
STATES = ("proved", "open", "closed", "conditional", "criterion")
TAGS = (
    "DEF", "TARGET", "CONST", "THM", "PF", "DIR", "KNOWN", "BLOCK",
    "NEXT", "CHECK", "COUNTER", "SCOPE", "PRIOR", "REF",
)
RELATIONS = ("requires", "alternative", "supports", "blocks", "narrows", "resolves", "implies", "audit")
REQUIRED_OPEN_GATE_TAGS = frozenset(("DEF", "TARGET", "KNOWN", "BLOCK", "NEXT", "CHECK"))


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def validate_current_authority_manifest(
    manifest_path: Path = CURRENT_AUTHORITY_MANIFEST,
    root: Path = ROOT,
) -> None:
    manifest = _load_json(manifest_path)
    if manifest.get("schema") != "zeta23_current_authority_manifest_v1":
        raise ValueError("current authority manifest schema drifted")
    if manifest.get("scope") != "LOCAL_WORKTREE_BYTES_NOT_COMMIT_BOUND":
        raise ValueError("current authority manifest scope drifted")
    artifacts = manifest.get("artifacts", [])
    expected_paths = {
        str(path.relative_to(root)) for path in (*CURRENT_CACHES.values(), *CURRENT_REPORTS.values())
    }
    if {item.get("path") for item in artifacts} != expected_paths:
        raise ValueError("current authority manifest path set drifted")
    if len({item.get("role") for item in artifacts}) != len(expected_paths):
        raise ValueError("current authority manifest roles are missing or duplicated")
    for item in artifacts:
        path = (root / item["path"]).resolve()
        if not _is_within(path, root) or not path.is_file():
            raise ValueError(f"current authority manifest target missing: {item['role']}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item.get("sha256"):
            raise ValueError(f"current authority manifest hash drift: {item['role']}")


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def _validate_declared_paths(
    role: str,
    cache: Path,
    data: dict[str, Any],
    root: Path,
) -> None:
    authority = data.get("human_authority")
    resolved_authority = (cache.parent / authority).resolve() if isinstance(authority, str) else None
    expected_authority = CURRENT_REPORTS[role].resolve()
    if (
        resolved_authority != expected_authority
        or not _is_within(expected_authority, root)
        or not expected_authority.is_file()
    ):
        raise ValueError(f"wrong or missing {role} human authority")
    for source in data.get("sources", []):
        resolved = (root / source).resolve() if isinstance(source, str) else root.parent
        if not _is_within(resolved, root) or not resolved.is_file():
            raise ValueError(f"missing source {source!r} declared by {cache.relative_to(root)}")


def validate_current_authority_bundle(
    bundle: Mapping[str, dict[str, Any]],
    cache_paths: Mapping[str, Path] = CURRENT_CACHES,
    root: Path = ROOT,
) -> None:
    if set(bundle) != set(CURRENT_SCHEMAS) or set(cache_paths) != set(CURRENT_SCHEMAS):
        raise ValueError("current authority bundle must contain route, adapter, and closure")
    for role, schema in CURRENT_SCHEMAS.items():
        if bundle[role].get("schema") != schema:
            raise ValueError(f"current {role} schema drifted")

    post, s0, closure = (bundle[role] for role in ("route", "adapter", "closure"))
    dates = {post.get("date"), s0.get("date"), closure.get("date")}
    if len(dates) != 1:
        raise ValueError("current authority caches have different dates")
    current_date = next(iter(dates))
    if not isinstance(current_date, str):
        raise ValueError("current authority date is not a string")
    try:
        parsed_date = date.fromisoformat(current_date)
    except ValueError as error:
        raise ValueError("current authority date is not ISO-8601") from error
    if parsed_date.isoformat() != current_date:
        raise ValueError("current authority date is not canonical ISO-8601")

    common_statuses = ("uniform_zero_free_strip", "riemann_hypothesis", "strip_to_rh_amplifier")
    for key in common_statuses:
        values = {data.get("global_status", {}).get(key) for data in (post, s0, closure)}
        if len(values) != 1:
            raise ValueError(f"current authority caches disagree on {key}")
    if post["global_status"]["uniform_zero_free_strip"] != "OPEN":
        raise ValueError("current authority bundle has an unsupported strip status")
    if post["global_status"]["riemann_hypothesis"] != "OPEN":
        raise ValueError("current authority bundle has an unsupported RH status")
    if post["global_status"]["strip_to_rh_amplifier"] != "ABSENT":
        raise ValueError("current authority bundle has an unsupported strip-to-RH status")

    stages = {stage["id"]: stage for stage in post["selected_strip_route"]["stages"]}
    if set(stages) != {"S0", "S1", "S2", "S3", "S4"}:
        raise ValueError("current route stage set drifted")
    if stages["S0"]["status"] != "COMPLETE_GO_FAILED_BRANCH_SWITCH_FIRED":
        raise ValueError("current S0 branch-switch status drifted")
    s0_verdict = s0["s0_verdict"]
    if s0_verdict["primitive_only_go_condition"] != "FAIL":
        raise ValueError("current S0 primitive-only verdict drifted")
    if s0_verdict["branch_switch"] != "FIRED":
        raise ValueError("current S0 branch switch drifted")
    if s0_verdict["first_open_edge"] != "COMPLETE_FIXED_WINDOW_QH_R71_ENERGY":
        raise ValueError("current S0 first-open edge drifted")
    if post["selected_strip_route"]["attack_surface"]["status"] != "OPEN_STRIP_EQUIVALENT_ENDPOINT":
        raise ValueError("current complete-energy endpoint status drifted")

    dependency_status = {item["source"]: item["status"] for item in s0["dependency_chain"]}
    route_disposition = {
        item["case"]: item["result"] for item in closure["tested_route_disposition"]
    }
    primitive_status = "NO_PROVED_ORDER_REFLECTING_MAP_ACTUAL_INDEFINITENESS_UNCERTIFIED"
    if dependency_status.get("R120_R124") != primitive_status:
        raise ValueError("adapter primitive-sign trust status drifted")
    if route_disposition.get("LOCAL_RESTRICTION") != primitive_status:
        raise ValueError("closure primitive-sign trust status drifted")
    if (
        closure["corrections"]["primitive_sign"]
        != "POSITIVE_NARROW_BAND_PROVED_FULL_SHELL_SIGN_CHANGE_D_RATED_NUMERICAL_NO_ORDER_REFLECTING_MAP"
    ):
        raise ValueError("closure primitive-sign evidence was promoted or drifted")
    if (
        post["selected_strip_route"]["attack_surface"]["local_r116_packet"]["status"]
        != "LOCAL_MEMBER_NO_PROVED_ORDER_REFLECTION_ACTUAL_INDEFINITENESS_UNCERTIFIED"
    ):
        raise ValueError("route primitive-sign trust status drifted")
    if not closure["exhaustiveness_status"].startswith("NOT_PROVED"):
        raise ValueError("tested-route disposition was promoted to an exhaustive classification")
    if len(route_disposition) != 3:
        raise ValueError("tested-route disposition no longer has exactly three tested cases")
    if closure["corrections"]["r128_global_result"] != "EXACT_EQUALS_ORIGINAL_R71_ENERGY":
        raise ValueError("R128 restoration status drifted")
    if closure["corrections"]["r123_r125_status"] != "EXACT_SCALE_REPLICATION_NOT_A_REDUCTION":
        raise ValueError("R123/R125 scale-replication status drifted")
    if (
        post["selected_strip_route"]["attack_surface"]["optional_r123_fixed_window_fork"]["status"]
        != "EXACT_SCALE_REPLICATION_NOT_A_REDUCTION"
    ):
        raise ValueError("route R123/R125 scale-replication status drifted")
    if closure["corrections"]["energy_map"] != "eta=kappa/2 for 0<kappa<=1":
        raise ValueError("complete-energy exponent map or domain drifted")
    if s0["exponent_maps"]["complete_energy"]["conclusion"] != "eta=kappa/2 for 0<kappa<=1":
        raise ValueError("adapter exponent map or domain drifted")
    if (
        post["selected_strip_route"]["attack_surface"]["normalization_map"]
        != "kappa=2*eta for 0<kappa<=1 in the R73 energy normalization"
    ):
        raise ValueError("route exponent map or domain drifted")

    s1 = closure["s1"]
    if stages["S1"]["candidate_a0_result"] != "FAIL_ADMISSION_TAUTOLOGICAL_C_STAR_ONE_EQUALS_LAMBDA_REEXPANSION":
        raise ValueError("route S1-A0 status drifted")
    if stages["S1"]["candidate_a_structural_class_status"] != "UNFORMULATED_NOT_CLOSED_BY_A0":
        raise ValueError("route structural S1-A class was closed without proof")
    if stages["S1"]["candidate_b_status"] != "UNFORMULATED_NOT_CLOSED":
        raise ValueError("route S1-B class was closed without proof")
    if s1["candidate_a_structural_inequality_class"] != "UNFORMULATED_NOT_CLOSED":
        raise ValueError("closure structural S1-A class was closed without proof")
    if s1["candidate_b_completed_source_factorization"] != "UNFORMULATED_NOT_CLOSED":
        raise ValueError("closure S1-B class was closed without proof")

    expected_families = {
        "fixed_total_width_near_square": "SINGLE_SCHEDULE_CONVERSE_OPEN",
        "fixed_step_sublinear": "SINGLE_SCHEDULE_CONVERSE_OPEN_AND_ONLY_SUBPOWER_BOUND",
        "proportional_order_dyadic_bank": "R80_MOVING_EDGE_CONVERSE_PROVED_GAP_VANISHES_AT_ZERO_SLOPE",
    }
    if closure["growing_families"] != expected_families:
        raise ValueError("growing detector families were conflated")
    if not isinstance(post.get("next_action"), str) or not post["next_action"].strip():
        raise ValueError("current route has no serialized next action")

    for role, data in bundle.items():
        _validate_declared_paths(role, cache_paths[role], data, root)


def load_current_authority_bundle(
    cache_paths: Mapping[str, Path] = CURRENT_CACHES,
    root: Path = ROOT,
) -> dict[str, dict[str, Any]]:
    bundle = {role: _load_json(path) for role, path in cache_paths.items()}
    validate_current_authority_bundle(bundle, cache_paths, root)
    if root.resolve() == ROOT.resolve() and cache_paths == CURRENT_CACHES:
        validate_current_authority_manifest(root=root)
    return bundle


def current_routing_packet() -> dict[str, Any]:
    """Return the cross-validated authority packet used by a bare ``resume``."""
    data = load_current_authority_bundle()["route"]
    if not CURRENT_RELOAD_INDEX.is_file():
        raise ValueError("current random-access reload index is missing")
    stages = {stage["id"]: stage for stage in data["selected_strip_route"]["stages"]}
    return {
        "date": data["date"],
        "authority": str(CURRENT_ROUTING.relative_to(ROOT)),
        "companion_authorities": [
            str(CURRENT_CACHES[role].relative_to(ROOT)) for role in ("adapter", "closure")
        ],
        "integrity_manifest": str(CURRENT_AUTHORITY_MANIFEST.relative_to(ROOT)),
        "global_status": data["global_status"],
        "endpoint": data["selected_strip_route"]["attack_surface"]["target_scale"],
        "endpoint_status": data["selected_strip_route"]["attack_surface"]["status"],
        "s0": stages["S0"]["status"],
        "s1": stages["S1"]["status"],
        "s2": stages["S2"]["status"],
        "next": data["next_action"],
        "reload_context": str(CURRENT_RELOAD_INDEX.relative_to(ROOT)),
        "reload_command": CURRENT_RELOAD_COMMAND,
        "historical_tree": str(CACHE.relative_to(ROOT)),
    }


def render_current_routing(as_json: bool = False) -> None:
    packet = current_routing_packet()
    if as_json:
        print(json.dumps(packet, ensure_ascii=False, separators=(",", ":")))
        return
    print(f"VERIFIED ROUTING SNAPSHOT {packet['date']} ({packet['authority']})")
    print(f"  companions {', '.join(packet['companion_authorities'])}")
    print(f"  manifest {packet['integrity_manifest']}")
    print(f"  endpoint [{packet['endpoint_status']}] {packet['endpoint']}")
    print(f"  S0 {packet['s0']}")
    print(f"  S1 {packet['s1']}")
    print(f"  S2 {packet['s2']}")
    print(f"  NEXT {packet['next']}")
    print("  SUPERSEDED NEXT R182 completed and parked QP/Turan; use LIVE RELOAD below")
    print(f"  RELOAD {packet['reload_command']} ({packet['reload_context']})")
    print(f"  NOTE explicit node/frontier queries use historical {packet['historical_tree']}")


def put_varint(out: bytearray, value: int) -> None:
    if value < 0:
        raise ValueError("negative varint")
    while value >= 0x80:
        out.append((value & 0x7F) | 0x80)
        value >>= 7
    out.append(value)


def get_varint(data: bytes, pos: int) -> tuple[int, int]:
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


def load_seed() -> dict[str, Any]:
    with SEED.open(encoding="utf-8") as stream:
        return json.load(stream)


def validate(obj: dict[str, Any]) -> None:
    ids = [node[0] for node in obj["nodes"]]
    known = set(ids)
    if len(ids) != len(known):
        raise ValueError("duplicate node id")
    by_id = {node[0]: node for node in obj["nodes"]}
    for node in obj["nodes"]:
        code, parent, kind, state, _, records, edges = node
        if parent and parent not in known:
            raise ValueError(f"unknown parent {parent} of {code}")
        if kind not in KINDS or state not in STATES:
            raise ValueError(f"bad enum in {code}")
        tags = set()
        for tag, payload in records:
            if tag not in TAGS or not isinstance(payload, str) or not payload:
                raise ValueError(f"bad record in {code}: {tag}")
            tags.add(tag)
        for relation, target in edges:
            if relation not in RELATIONS or target not in known:
                raise ValueError(f"bad edge {code}:{relation}:{target}")
        if kind == "gate" and state == "open" and not REQUIRED_OPEN_GATE_TAGS <= tags:
            missing = sorted(REQUIRED_OPEN_GATE_TAGS - tags)
            raise ValueError(f"open gate {code} is not resumable; missing {missing}")
        if state == "proved" and kind in ("fact", "invariant") and "THM" not in tags:
            raise ValueError(f"proved node {code} lacks THM")
    for key in ("frontier", "portfolio"):
        if not set(obj[key]) <= known:
            raise ValueError(f"unknown {key} node")
    if obj["goal"] not in known or obj["resume"] not in known:
        raise ValueError("unknown goal/resume node")
    # A resume packet must terminate in mathematical records, not references.
    resume = by_id[obj["resume"]]
    if all(tag == "REF" for tag, _ in resume[5]):
        raise ValueError("resume node is only a bibliography")


def compile_tree(obj: dict[str, Any]) -> bytes:
    validate(obj)
    strings: list[str] = []
    ids: dict[str, int] = {}

    def sid(value: str) -> int:
        if value not in ids:
            ids[value] = len(strings)
            strings.append(value)
        return ids[value]

    for key, value in obj["meta"].items():
        sid(key)
        sid(value)
    for code, parent, _, _, title, records, _ in obj["nodes"]:
        sid(code)
        sid(parent)
        sid(title)
        for _, payload in records:
            sid(payload)

    out = bytearray(MAGIC)
    put_varint(out, obj["version"])
    put_varint(out, len(strings))
    for value in strings:
        raw = value.encode("utf-8")
        put_varint(out, len(raw))
        out.extend(raw)
    put_varint(out, len(obj["meta"]))
    for key, value in obj["meta"].items():
        put_varint(out, sid(key))
        put_varint(out, sid(value))

    index = {node[0]: i for i, node in enumerate(obj["nodes"])}
    put_varint(out, len(obj["nodes"]))
    for code, parent, kind, state, title, records, edges in obj["nodes"]:
        put_varint(out, sid(code))
        put_varint(out, 0 if not parent else index[parent] + 1)
        out.append(KINDS.index(kind) | (STATES.index(state) << 3))
        put_varint(out, sid(title))
        put_varint(out, len(records))
        for tag, payload in records:
            out.append(TAGS.index(tag))
            put_varint(out, sid(payload))
        put_varint(out, len(edges))
        for relation, target in edges:
            out.append(RELATIONS.index(relation))
            put_varint(out, index[target])

    for key in ("frontier", "portfolio"):
        put_varint(out, len(obj[key]))
        for code in obj[key]:
            put_varint(out, index[code])
    put_varint(out, index[obj["goal"]])
    put_varint(out, index[obj["resume"]])
    return bytes(out)


def build() -> None:
    raw = compile_tree(load_seed())
    packed = lzma.compress(raw, format=lzma.FORMAT_XZ, preset=9 | lzma.PRESET_EXTREME)
    CACHE.write_bytes(packed)
    digest = hashlib.sha256(packed).hexdigest()
    print(f"built {CACHE.relative_to(ROOT)} raw={len(raw)} packed={len(packed)} sha256={digest}")


def decode() -> dict[str, Any]:
    packed = CACHE.read_bytes()
    data = lzma.decompress(packed)
    if not data.startswith(MAGIC):
        raise ValueError("bad Z23P magic")
    pos = len(MAGIC)
    version, pos = get_varint(data, pos)
    count, pos = get_varint(data, pos)
    strings: list[str] = []
    for _ in range(count):
        size, pos = get_varint(data, pos)
        strings.append(data[pos:pos + size].decode("utf-8"))
        pos += size
    meta_count, pos = get_varint(data, pos)
    meta: dict[str, str] = {}
    for _ in range(meta_count):
        key, pos = get_varint(data, pos)
        value, pos = get_varint(data, pos)
        meta[strings[key]] = strings[value]
    node_count, pos = get_varint(data, pos)
    nodes = []
    for _ in range(node_count):
        code, pos = get_varint(data, pos)
        parent, pos = get_varint(data, pos)
        flags = data[pos]
        pos += 1
        title, pos = get_varint(data, pos)
        record_count, pos = get_varint(data, pos)
        records = []
        for _ in range(record_count):
            tag = TAGS[data[pos]]
            pos += 1
            payload, pos = get_varint(data, pos)
            records.append([tag, strings[payload]])
        edge_count, pos = get_varint(data, pos)
        edges = []
        for _ in range(edge_count):
            relation = RELATIONS[data[pos]]
            pos += 1
            target, pos = get_varint(data, pos)
            edges.append([relation, target])
        nodes.append({
            "id": strings[code],
            "parent": None if parent == 0 else parent - 1,
            "kind": KINDS[flags & 0x7],
            "state": STATES[(flags >> 3) & 0x7],
            "title": strings[title],
            "records": records,
            "edges": edges,
        })
    groups = []
    for _ in range(2):
        size, pos = get_varint(data, pos)
        group = []
        for _ in range(size):
            item, pos = get_varint(data, pos)
            group.append(item)
        groups.append(group)
    goal, pos = get_varint(data, pos)
    resume, pos = get_varint(data, pos)
    if pos != len(data):
        raise ValueError(f"trailing bytes {len(data)-pos}")
    return {
        "version": version,
        "meta": meta,
        "nodes": nodes,
        "frontier": groups[0],
        "portfolio": groups[1],
        "goal": goal,
        "resume": resume,
        "bytes": len(packed),
        "sha256": hashlib.sha256(packed).hexdigest(),
    }


def closure(graph: dict[str, Any], seeds: Iterable[int], include_ancestors: bool = True) -> list[int]:
    chosen = set(seeds)
    # First follow proof dependencies from the requested nodes.  Ancestors are
    # added only as orientation; their alternative branches must not flood a
    # continuation packet with unrelated routes.
    queue = deque(chosen)
    while queue:
        current = queue.popleft()
        node = graph["nodes"][current]
        for _, target in node["edges"]:
            if target not in chosen:
                chosen.add(target)
                queue.append(target)
    if include_ancestors:
        for current in tuple(chosen):
            parent = graph["nodes"][current]["parent"]
            while parent is not None:
                chosen.add(parent)
                parent = graph["nodes"][parent]["parent"]
    return sorted(chosen)


def select(graph: dict[str, Any], codes: list[str], mode: str) -> list[int]:
    by_id = {node["id"]: i for i, node in enumerate(graph["nodes"])}
    if codes:
        try:
            seeds = [by_id[code] for code in codes]
        except KeyError as error:
            raise SystemExit(f"unknown node {error.args[0]}") from None
    elif mode == "frontier":
        seeds = graph["frontier"]
    elif mode == "portfolio":
        seeds = graph["portfolio"]
    else:
        seeds = [graph["resume"]]
    return closure(graph, seeds)


def render(graph: dict[str, Any], indices: list[int], show_refs: bool, as_json: bool) -> None:
    if as_json:
        payload = []
        for index in indices:
            node = dict(graph["nodes"][index])
            node["parent"] = None if node["parent"] is None else graph["nodes"][node["parent"]]["id"]
            node["edges"] = [[rel, graph["nodes"][target]["id"]] for rel, target in node["edges"]]
            if not show_refs:
                node["records"] = [record for record in node["records"] if record[0] != "REF"]
            payload.append(node)
        print(json.dumps({"nodes": payload}, ensure_ascii=False, separators=(",", ":")))
        return
    for index in indices:
        node = graph["nodes"][index]
        print(f"@{node['id']} <{node['kind']}:{node['state']}> {node['title']}")
        for tag, text in node["records"]:
            if tag == "REF" and not show_refs:
                continue
            print(f"  {tag} {text}")
        for relation, target in node["edges"]:
            print(f"  ->{relation} @{graph['nodes'][target]['id']}")


def verify() -> None:
    obj = load_seed()
    validate(obj)
    expected = compile_tree(obj)
    actual = lzma.decompress(CACHE.read_bytes())
    if expected != actual:
        raise SystemExit("stale proof tree; run build")
    graph = decode()
    current = current_routing_packet()
    print(
        f"OK historical_version={graph['version']} nodes={len(graph['nodes'])} "
        f"bytes={graph['bytes']} sha256={graph['sha256']} resume={graph['nodes'][graph['resume']]['id']}"
    )
    companions = ",".join(current["companion_authorities"])
    print(
        f"OK current_routing={current['date']} authority={current['authority']} "
        f"companions={companions}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build")
    sub.add_parser("verify")
    query = sub.add_parser("resume")
    query.add_argument("codes", nargs="*")
    query.add_argument("--frontier", action="store_true")
    query.add_argument("--portfolio", action="store_true")
    query.add_argument("--refs", action="store_true")
    query.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.command == "build":
        build()
    elif args.command == "verify":
        verify()
    else:
        if not args.codes and not args.frontier and not args.portfolio:
            render_current_routing(args.json)
            return
        graph = decode()
        mode = "frontier" if args.frontier else "portfolio" if args.portfolio else "resume"
        indices = select(graph, args.codes, mode)
        render(graph, indices, args.refs, args.json)


if __name__ == "__main__":
    main()
