#!/usr/bin/env python3
"""Exact projected-neighbor-line and lift-conflict diagnostic.

For an edge of the all-five-distinct ordered-pair graph

    (b, B) -- (c, C),  carrier a,

the neighbors ``(d,D)`` of ``(b,B)`` have unique carriers ``x`` and encode
the two source triples ``(x,b,d),(x,B,D)``.  This script finds every affine
line with at least three projected neighbor points.  For each such line it
checks, using integer arithmetic,

* whether the witnesses x are affine in the primitive line parameter;
* whether (xd,xD,x) lie in the forced homogeneous plane;
* whether the six-or-more source triples lie in one affine plane; and
* whether a deterministic local line peel assigns one graph edge from both
  its left and right anchors.

The shell support still inherits ``build_four_cycle_core``'s documented
floating nearest-integer trust boundary.  All graph, line, lift, rank, and
overlap calculations after support materialization are exact.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations
from math import gcd
from pathlib import Path
import gc
import sys
from typing import Iterable, Sequence

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_actual_prime_nds import exact_balanced_degree  # noqa: E402
from qp_four_cycle_h_graph_lab import (  # noqa: E402
    build_pair_incidence_graph,
    decode_pair,
    filtered_pair_incidence_graph,
)
from qp_four_cycle_hostile_lab import build_four_cycle_core  # noqa: E402


Point = tuple[int, int]
Edge = tuple[int, int]
LineKey = tuple[int, int, int]


FIXTURES = (
    (12_853, 12.0),
    (25_013, 12.0),
    (50_021, 12.0),
    (25_013, 24.0),
    (11_801, 35.0),
    (11_801, 44.0),
    (25_013, 40.0),
    (50_021, 40.0),
)


@dataclass(frozen=True)
class NeighborEntry:
    neighbor_index: int
    point: Point
    witness: int
    edge: Edge


@dataclass(frozen=True)
class ProjectedLine:
    side: str
    anchor: Point
    key: LineKey
    entries: tuple[NeighborEntry, ...]


@dataclass(frozen=True)
class SideScan:
    counts: Counter[str]
    rich_memberships: dict[Edge, int]
    selected_memberships: dict[Edge, int]
    selected_lines: tuple[ProjectedLine, ...]
    first_nonaffine: ProjectedLine | None


@dataclass(frozen=True)
class FixtureSummary:
    q: int
    cutoff: int
    degree: int
    shell_nodes: int
    source_triples: int
    graph_edges: int
    maximum_left_degree: int
    maximum_right_degree: int
    rich_anchors: int
    rich_lines: int
    maximum_line_size: int
    nonaffine_witness_lines: int
    nonplanar_source_lines: int
    homogeneous_lift_failures: int
    rich_edges: int
    same_side_multiple_assignments: int
    dual_anchor_rich_edges: int
    selected_lines: int
    selected_edge_incidences: int
    selected_edges: int
    residual_edges: int
    dual_anchor_selected_edges: int
    first_nonaffine: ProjectedLine | None
    first_dual: tuple[Edge, ProjectedLine, ProjectedLine] | None


def line_key(first: Point, second: Point) -> LineKey:
    dx, dy = second[0] - first[0], second[1] - first[1]
    divisor = gcd(abs(dx), abs(dy))
    if not divisor:
        raise ValueError("two distinct points are required")
    direction_x, direction_y = dx // divisor, dy // divisor
    if direction_x < 0 or (direction_x == 0 and direction_y < 0):
        direction_x, direction_y = -direction_x, -direction_y
    constant = -direction_y * first[0] + direction_x * first[1]
    return direction_x, direction_y, constant


def line_parameters(line: ProjectedLine) -> tuple[tuple[int, int], ...]:
    direction_x, direction_y, constant = line.key
    base = min(entry.point for entry in line.entries)
    answer: list[tuple[int, int]] = []
    for entry in line.entries:
        x_difference = entry.point[0] - base[0]
        y_difference = entry.point[1] - base[1]
        if direction_x:
            if x_difference % direction_x:
                raise AssertionError("nonintegral primitive line parameter")
            parameter = x_difference // direction_x
            if y_difference != parameter * direction_y:
                raise AssertionError("point misses its recorded line")
        else:
            if y_difference % direction_y:
                raise AssertionError("nonintegral primitive line parameter")
            parameter = y_difference // direction_y
            if x_difference:
                raise AssertionError("point misses its vertical line")
        if -direction_y * entry.point[0] + direction_x * entry.point[1] != constant:
            raise AssertionError("line constant mismatch")
        answer.append((parameter, entry.witness))
    return tuple(sorted(answer))


def witnesses_are_affine(line: ProjectedLine) -> bool:
    values = line_parameters(line)
    first_t, first_x = values[0]
    second_t, second_x = values[1]
    return all(
        (witness - first_x) * (second_t - first_t)
        == (second_x - first_x) * (parameter - first_t)
        for parameter, witness in values[2:]
    )


def source_points(line: ProjectedLine) -> tuple[tuple[int, int, int], ...]:
    first_anchor, second_anchor = line.anchor
    if line.side == "L":
        return tuple(
            point
            for entry in line.entries
            for point in (
                (entry.witness, first_anchor, entry.point[0]),
                (entry.witness, second_anchor, entry.point[1]),
            )
        )
    if line.side == "R":
        return tuple(
            point
            for entry in line.entries
            for point in (
                (entry.witness, entry.point[0], first_anchor),
                (entry.witness, entry.point[1], second_anchor),
            )
        )
    raise ValueError("unknown graph side")


def cross(
    first: Sequence[int], second: Sequence[int]
) -> tuple[int, int, int]:
    return (
        first[1] * second[2] - first[2] * second[1],
        first[2] * second[0] - first[0] * second[2],
        first[0] * second[1] - first[1] * second[0],
    )


def affine_rank_three(points: Sequence[Sequence[int]]) -> int:
    anchor = points[0]
    differences = tuple(
        tuple(point[index] - anchor[index] for index in range(3))
        for point in points[1:]
    )
    first = next((value for value in differences if any(value)), None)
    if first is None:
        return 0
    normal = next(
        (
            cross(first, value)
            for value in differences
            if any(cross(first, value))
        ),
        None,
    )
    if normal is None:
        return 1
    if all(
        sum(normal[index] * value[index] for index in range(3)) == 0
        for value in differences
    ):
        return 2
    return 3


def homogeneous_lift_holds(line: ProjectedLine) -> bool:
    direction_x, direction_y, constant = line.key
    return all(
        -direction_y * (entry.witness * entry.point[0])
        + direction_x * (entry.witness * entry.point[1])
        - constant * entry.witness
        == 0
        for entry in line.entries
    )


def physical_pair(codes: np.ndarray, index: int, core: object) -> Point:
    first, second = decode_pair(int(codes[index]), core.dimension)
    return int(core.values[first]), int(core.values[second])


def scan_side(core: object, graph: object, side: str) -> SideScan:
    if side == "L":
        support = graph.support
        carriers = graph.carriers
        neighbor_codes = graph.right_pair_codes
        anchor_codes = graph.left_pair_codes
        side_number = 1
    elif side == "R":
        support = graph.support.T.tocsr()
        carriers = graph.carriers.T.tocsr()
        neighbor_codes = graph.left_pair_codes
        anchor_codes = graph.right_pair_codes
        side_number = 2
    else:
        raise ValueError("unknown graph side")
    if not np.array_equal(support.indptr, carriers.indptr) or not np.array_equal(
        support.indices, carriers.indices
    ):
        raise AssertionError("support/carrier sparse layouts differ")

    counts: Counter[str] = Counter()
    rich_memberships: dict[Edge, int] = defaultdict(int)
    selected_memberships: dict[Edge, int] = defaultdict(int)
    selected_lines: list[ProjectedLine] = []
    first_nonaffine: ProjectedLine | None = None
    for anchor_index in range(support.shape[0]):
        start, stop = support.indptr[anchor_index : anchor_index + 2]
        if stop - start < 3:
            continue
        local: list[NeighborEntry] = []
        for position in range(start, stop):
            neighbor_index = int(support.indices[position])
            edge = (
                (anchor_index, neighbor_index)
                if side == "L"
                else (neighbor_index, anchor_index)
            )
            local.append(
                NeighborEntry(
                    neighbor_index=neighbor_index,
                    point=physical_pair(neighbor_codes, neighbor_index, core),
                    witness=int(carriers.data[position]),
                    edge=edge,
                )
            )
        candidates: dict[LineKey, set[int]] = defaultdict(set)
        for first, second in combinations(range(len(local)), 2):
            candidates[line_key(local[first].point, local[second].point)].update(
                (first, second)
            )
        rich = {
            key: members
            for key, members in candidates.items()
            if len(members) >= 3
        }
        if not rich:
            continue
        counts["anchors"] += 1
        anchor = physical_pair(anchor_codes, anchor_index, core)
        for key, members in rich.items():
            line = ProjectedLine(
                side,
                anchor,
                key,
                tuple(local[index] for index in sorted(members)),
            )
            counts["lines"] += 1
            counts["maximum_line_size"] = max(
                counts["maximum_line_size"], len(line.entries)
            )
            witness_affine = witnesses_are_affine(line)
            if witness_affine:
                counts["affine_witness"] += 1
            else:
                counts["nonaffine_witness"] += 1
                if first_nonaffine is None:
                    first_nonaffine = line
            if affine_rank_three(source_points(line)) <= 2:
                counts["planar_source"] += 1
            else:
                counts["nonplanar_source"] += 1
            if homogeneous_lift_holds(line):
                counts["homogeneous_lift"] += 1
            else:
                counts["homogeneous_lift_failure"] += 1
            for entry in line.entries:
                rich_memberships[entry.edge] += side_number

        remaining = set(range(len(local)))
        while True:
            options = tuple(
                (len(members & remaining), key, members & remaining)
                for key, members in rich.items()
                if len(members & remaining) >= 3
            )
            if not options:
                break
            _size, key, members = min(
                options,
                key=lambda option: (
                    -option[0],
                    option[1],
                    tuple(sorted(option[2])),
                ),
            )
            line = ProjectedLine(
                side,
                anchor,
                key,
                tuple(local[index] for index in sorted(members)),
            )
            record_index = len(selected_lines)
            selected_lines.append(line)
            counts["selected_lines"] += 1
            counts["selected_edges"] += len(members)
            for member in members:
                edge = local[member].edge
                if edge in selected_memberships:
                    raise AssertionError("one side assigned an edge twice")
                selected_memberships[edge] = record_index
            remaining.difference_update(members)
    return SideScan(
        counts,
        dict(rich_memberships),
        dict(selected_memberships),
        tuple(selected_lines),
        first_nonaffine,
    )


def analyze_fixture(q: int, cutoff: float) -> FixtureSummary:
    core = build_four_cycle_core(
        q,
        width=0.2,
        cutoff=cutoff,
        kind="prime_powers",
        quadrature_order=8,
    )
    graph = filtered_pair_incidence_graph(
        core,
        build_pair_incidence_graph(core),
        keep="all_five_distinct",
    )
    left_degrees = np.asarray(graph.support.getnnz(axis=1)).ravel()
    right_degrees = np.asarray(graph.support.getnnz(axis=0)).ravel()
    left = scan_side(core, graph, "L")
    right = scan_side(core, graph, "R")
    counts = left.counts + right.counts

    rich_edges = set(left.rich_memberships) | set(right.rich_memberships)
    same_side_multiple = sum(
        left.rich_memberships.get(edge, 0) > 1
        or right.rich_memberships.get(edge, 0) > 2
        for edge in rich_edges
    )
    dual_rich = sum(
        edge in left.rich_memberships and edge in right.rich_memberships
        for edge in rich_edges
    )
    dual_selected_edges = sorted(
        set(left.selected_memberships) & set(right.selected_memberships)
    )
    first_dual = None
    if dual_selected_edges:
        edge = dual_selected_edges[0]
        first_dual = (
            edge,
            left.selected_lines[left.selected_memberships[edge]],
            right.selected_lines[right.selected_memberships[edge]],
        )
    first_nonaffine = left.first_nonaffine or right.first_nonaffine
    answer = FixtureSummary(
        q=q,
        cutoff=int(cutoff),
        degree=exact_balanced_degree(q),
        shell_nodes=core.dimension,
        source_triples=len(core.rows),
        graph_edges=graph.support.nnz,
        maximum_left_degree=int(left_degrees.max(initial=0)),
        maximum_right_degree=int(right_degrees.max(initial=0)),
        rich_anchors=counts["anchors"],
        rich_lines=counts["lines"],
        maximum_line_size=max(
            left.counts["maximum_line_size"],
            right.counts["maximum_line_size"],
        ),
        nonaffine_witness_lines=counts["nonaffine_witness"],
        nonplanar_source_lines=counts["nonplanar_source"],
        homogeneous_lift_failures=counts["homogeneous_lift_failure"],
        rich_edges=len(rich_edges),
        same_side_multiple_assignments=same_side_multiple,
        dual_anchor_rich_edges=dual_rich,
        selected_lines=counts["selected_lines"],
        selected_edge_incidences=counts["selected_edges"],
        selected_edges=len(
            set(left.selected_memberships) | set(right.selected_memberships)
        ),
        residual_edges=graph.support.nnz
        - len(set(left.selected_memberships) | set(right.selected_memberships)),
        dual_anchor_selected_edges=len(dual_selected_edges),
        first_nonaffine=first_nonaffine,
        first_dual=first_dual,
    )
    del graph, core, left, right
    gc.collect()
    return answer


def determinant(first: Sequence[int], second: Sequence[int], third: Sequence[int]) -> int:
    return (
        first[0] * (second[1] * third[2] - second[2] * third[1])
        - first[1] * (second[0] * third[2] - second[2] * third[0])
        + first[2] * (second[0] * third[1] - second[1] * third[0])
    )


def nonplanarity_certificate(
    points: Sequence[Sequence[int]],
) -> tuple[tuple[int, int, int, int], int] | None:
    anchor = points[0]
    for indices in combinations(range(1, len(points)), 3):
        differences = tuple(
            tuple(points[index][coordinate] - anchor[coordinate] for coordinate in range(3))
            for index in indices
        )
        value = determinant(*differences)
        if value:
            return (0, *indices), value
    return None


def line_payload(line: ProjectedLine) -> str:
    return (
        f"side={line.side} anchor={line.anchor} line={line.key} "
        f"parameter_witness={line_parameters(line)} "
        f"point_witness={tuple((entry.point, entry.witness) for entry in line.entries)}"
    )


def main() -> None:
    summaries = tuple(analyze_fixture(q, cutoff) for q, cutoff in FIXTURES)
    if any(value.homogeneous_lift_failures for value in summaries):
        raise AssertionError("the forced homogeneous lift failed")
    hostile = next(
        value for value in summaries if (value.q, value.cutoff) == (11_801, 44)
    )
    if hostile.first_nonaffine is None or hostile.first_dual is None:
        raise AssertionError("the hostile projected-line certificates disappeared")

    print("PASS projected-neighbor lift/conflict diagnostic")
    print(
        "q U D nodes triples edges degL degR anchors lines maxline nonaff "
        "nonplane liftfail rich_edges same_side_multi dual_rich selected_lines "
        "selected_mass selected_edges residual_edges dual_selected dual_selected/D2"
    )
    for value in summaries:
        print(
            value.q,
            value.cutoff,
            value.degree,
            value.shell_nodes,
            value.source_triples,
            value.graph_edges,
            value.maximum_left_degree,
            value.maximum_right_degree,
            value.rich_anchors,
            value.rich_lines,
            value.maximum_line_size,
            value.nonaffine_witness_lines,
            value.nonplanar_source_lines,
            value.homogeneous_lift_failures,
            value.rich_edges,
            value.same_side_multiple_assignments,
            value.dual_anchor_rich_edges,
            value.selected_lines,
            value.selected_edge_incidences,
            value.selected_edges,
            value.residual_edges,
            value.dual_anchor_selected_edges,
            f"{value.dual_anchor_selected_edges / value.degree**2:.9g}",
        )

    nonaffine = hostile.first_nonaffine
    points = source_points(nonaffine)
    certificate = nonplanarity_certificate(points)
    print("NONAFFINE_WITNESS", line_payload(nonaffine))
    print(
        "NONPLANAR_SOURCE_CERTIFICATE",
        f"points={points}",
        f"minor={certificate}",
        f"lifted={tuple((entry.witness * entry.point[0], entry.witness * entry.point[1], entry.witness) for entry in nonaffine.entries)}",
    )
    edge, left, right = hostile.first_dual
    carrier = next(
        entry.witness for entry in left.entries if entry.edge == edge
    )
    print(
        "DUAL_CANONICAL_ASSIGNMENT",
        f"edge={edge}",
        f"central_left={left.anchor}",
        f"central_right={right.anchor}",
        f"carrier={carrier}",
    )
    print("DUAL_LEFT_PACKET", line_payload(left))
    print("DUAL_RIGHT_PACKET", line_payload(right))


if __name__ == "__main__":
    main()
