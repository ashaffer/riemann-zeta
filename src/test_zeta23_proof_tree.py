#!/usr/bin/env python3
"""Regression checks for the self-contained Z23P continuation cache."""

from __future__ import annotations

import lzma
import subprocess
import sys

import zeta23_proof_tree as zpt


def main() -> None:
    current = zpt.current_routing_packet()
    assert current["date"] == "2026-09-02"
    assert current["global_status"]["uniform_zero_free_strip"] == "OPEN"
    assert current["global_status"]["riemann_hypothesis"] == "OPEN"
    assert current["s0"] == "COMPLETE_GO_FAILED_BRANCH_SWITCH_FIRED"
    assert current["s1"] == "RAW_CANDIDATE_A0_FAILED_BOTH_MECHANISM_CLASSES_UNFORMULATED"
    assert current["endpoint_status"] == "OPEN_STRIP_EQUIVALENT_ENDPOINT"

    # The binary remains reproducible, but it is explicitly historical and
    # must not be mistaken for the default continuation route.
    seed = zpt.load_seed()
    zpt.validate(seed)
    assert zpt.compile_tree(seed) == lzma.decompress(zpt.CACHE.read_bytes())
    graph = zpt.decode()
    by_id = {node["id"]: i for i, node in enumerate(graph["nodes"])}
    packet = zpt.closure(graph, [by_id["QP"]])
    ids = {graph["nodes"][index]["id"] for index in packet}
    assert {
        "G", "INV", "RC", "FPR", "QP", "FD", "FEX", "FH", "FV", "FRA", "FHC", "FGN", "FGT4", "FIC", "FCR", "FSG", "FRCN", "FCA", "FCB", "FRM", "FPO", "FDT", "FNP", "FCH", "FDM", "FUR", "NM", "FCP", "F4",
        "FAS", "FAT", "FLB", "FGD", "FNEU", "FDD", "FNL",
        "FQPP", "FQPD", "FQPA", "FQPG", "FQPW", "FQPX", "FQPK", "FQPB",
    } <= ids
    assert "QT" not in ids and "QA" not in ids
    q_records = graph["nodes"][by_id["QP"]]["records"]
    tags = {tag for tag, _ in q_records}
    assert zpt.REQUIRED_OPEN_GATE_TAGS <= tags
    assert any(
        tag == "DIR"
        and "PROMOTE" in text
        and "kappa_min" in text
        and "kappa_max" in text
        for tag, text in q_records
    )
    bridge = graph["nodes"][by_id["FQPB"]]
    assert bridge["state"] == "proved" and bridge["kind"] == "fact"
    assert any(
        tag == "SCOPE"
        and "both QP and the strip remain open" in text
        and "not a QP equivalence" in text
        for tag, text in bridge["records"]
    )
    assert all(tag != "REF" for index in packet for tag, _ in graph["nodes"][index]["records"])
    print(
        f"PASS current={current['date']} historical_nodes={len(graph['nodes'])} "
        f"historical_packet={len(packet)} bytes={graph['bytes']}"
    )


def test_proof_tree_and_current_routing() -> None:
    main()


def test_bare_resume_labels_route_as_superseded_snapshot() -> None:
    completed = subprocess.run(
        [sys.executable, "src/zeta23_proof_tree.py", "resume"],
        cwd=zpt.ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "VERIFIED ROUTING SNAPSHOT 2026-09-02" in completed.stdout
    assert "SUPERSEDED NEXT R182" in completed.stdout
    assert "zeta23_correction_context.py resume" in completed.stdout


if __name__ == "__main__":
    main()
