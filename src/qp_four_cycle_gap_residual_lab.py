"""Finite residual-core diagnostics after the gap-projection theorem.

The theorem controls rectangles sector by sector.  This module removes the
covered rectangles and computes the exact degeneracy of the remaining local
completion-interaction graph.  Its output is diagnostic and has no
asymptotic force.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
import heapq

from qp_four_cycle_gap_projection import (
    CarrierGapSector,
    asymptotic_gap_scales,
)
from qp_four_cycle_h_graph_lab import RectangleRecord


CompletionVertex = tuple[int, int, int, int, int]


@dataclass(frozen=True)
class GapResidualCoreLedger:
    """Counts and a smallest deepest core of residual completion pairs."""

    generic_rectangles: int
    residual_rectangles: int
    completion_vertices: int
    degeneracy: int
    smallest_core_vertices: tuple[CompletionVertex, ...]
    smallest_core_edges: tuple[tuple[CompletionVertex, CompletionVertex], ...]


def gap_projection_ratio(rectangle: RectangleRecord, degree_scale: float) -> float:
    """Return the best asymptotic projection coefficient divided by ``D``."""

    if degree_scale <= 0.0:
        raise ValueError("degree_scale must be positive")
    sector = CarrierGapSector.from_carriers(
        (rectangle.first_row, rectangle.second_row),
        (rectangle.first_column, rectangle.second_column),
    )
    return asymptotic_gap_scales(sector).best / degree_scale


def completion_vertices(
    rectangle: RectangleRecord,
) -> tuple[CompletionVertex, CompletionVertex]:
    """Return the two carrier wedges paired by one original rectangle."""

    c11, c12, c21, c22 = rectangle.colors
    prefix = (rectangle.first_row, rectangle.second_row)
    return (
        prefix + (rectangle.first_column, c11, c21),
        prefix + (rectangle.second_column, c12, c22),
    )


def _degeneracy_and_smallest_core(
    edges: tuple[tuple[CompletionVertex, CompletionVertex], ...],
) -> tuple[
    int,
    int,
    tuple[CompletionVertex, ...],
    tuple[tuple[CompletionVertex, CompletionVertex], ...],
]:
    adjacency: dict[CompletionVertex, set[CompletionVertex]] = defaultdict(set)
    for first, second in edges:
        adjacency[first].add(second)
        adjacency[second].add(first)
    if not adjacency:
        return 0, 0, (), ()

    degrees = {vertex: len(neighbors) for vertex, neighbors in adjacency.items()}
    queue = [(degree, vertex) for vertex, degree in degrees.items()]
    heapq.heapify(queue)
    removed: set[CompletionVertex] = set()
    degeneracy = 0
    while queue:
        degree, vertex = heapq.heappop(queue)
        if vertex in removed or degree != degrees[vertex]:
            continue
        removed.add(vertex)
        degeneracy = max(degeneracy, degree)
        for neighbor in adjacency[vertex]:
            if neighbor not in removed:
                degrees[neighbor] -= 1
                heapq.heappush(queue, (degrees[neighbor], neighbor))

    active = set(adjacency)
    core_degrees = {vertex: len(adjacency[vertex]) for vertex in active}
    peel = deque(
        vertex
        for vertex in active
        if core_degrees[vertex] < degeneracy
    )
    while peel:
        vertex = peel.popleft()
        if vertex not in active:
            continue
        active.remove(vertex)
        for neighbor in adjacency[vertex]:
            if neighbor in active:
                core_degrees[neighbor] -= 1
                if core_degrees[neighbor] < degeneracy:
                    peel.append(neighbor)

    components: list[set[CompletionVertex]] = []
    unvisited = set(active)
    while unvisited:
        root = min(unvisited)
        unvisited.remove(root)
        component = {root}
        stack = [root]
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor in unvisited:
                    unvisited.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        components.append(component)
    chosen = min(components, key=lambda item: (len(item), sorted(item)))
    core_edges = tuple(
        edge for edge in edges if edge[0] in chosen and edge[1] in chosen
    )
    return (
        degeneracy,
        len(adjacency),
        tuple(sorted(chosen)),
        core_edges,
    )


def gap_residual_core_ledger(
    rectangles: tuple[RectangleRecord, ...],
    *,
    degree_scale: float,
    constant: float,
    generic_only: bool = True,
) -> GapResidualCoreLedger:
    """Delete gap-covered rectangles and audit the remaining local core."""

    if constant <= 0.0:
        raise ValueError("constant must be positive")
    generic = tuple(
        rectangle
        for rectangle in rectangles
        if not generic_only
        or (
            rectangle.distinct_node_count == 8
            and rectangle.distinct_unordered_hyperedges == 4
        )
    )
    residual = tuple(
        rectangle
        for rectangle in generic
        if gap_projection_ratio(rectangle, degree_scale) > constant
    )
    edges = tuple(completion_vertices(rectangle) for rectangle in residual)
    degeneracy, vertex_count, core_vertices, core_edges = (
        _degeneracy_and_smallest_core(edges)
    )
    return GapResidualCoreLedger(
        generic_rectangles=len(generic),
        residual_rectangles=len(residual),
        completion_vertices=vertex_count,
        degeneracy=degeneracy,
        smallest_core_vertices=core_vertices,
        smallest_core_edges=core_edges,
    )
