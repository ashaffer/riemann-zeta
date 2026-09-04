"""Repeated-node classification for symmetric carry four-cycles.

The product carry tensor is symmetric in its three coordinates.  This module
records the finite combinatorics behind the repeated-node sector of its
ordered rectangle expansion.  It deliberately does not assert the remaining
all-distinct four-cycle estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, Mapping, Sequence


Node = int
Hyperedge = tuple[Node, Node, Node]


def canonical_hyperedge(x: Node, y: Node, z: Node) -> Hyperedge:
    """Return the unordered triple, retaining repeated coordinates."""

    return tuple(sorted((x, y, z)))


def pair_unique(hyperedges: Iterable[Hyperedge]) -> bool:
    """Whether every unordered two-submultiset determines the third node."""

    third_by_pair: dict[tuple[Node, Node], Node] = {}
    for raw_edge in hyperedges:
        edge = canonical_hyperedge(*raw_edge)
        for removed in range(3):
            pair = tuple(edge[index] for index in range(3) if index != removed)
            third = edge[removed]
            previous = third_by_pair.setdefault(pair, third)
            if previous != third:
                return False
    return True


@dataclass(frozen=True)
class Rectangle:
    """One ordered nondegenerate four-cycle support pattern."""

    a1: Node
    a2: Node
    b1: Node
    b2: Node
    c11: Node
    c12: Node
    c21: Node
    c22: Node

    @property
    def nondegenerate(self) -> bool:
        return self.a1 != self.a2 and self.b1 != self.b2

    @property
    def colors(self) -> tuple[Node, Node, Node, Node]:
        return self.c11, self.c12, self.c21, self.c22

    @property
    def hyperedges(self) -> tuple[Hyperedge, Hyperedge, Hyperedge, Hyperedge]:
        return (
            canonical_hyperedge(self.a1, self.b1, self.c11),
            canonical_hyperedge(self.a1, self.b2, self.c12),
            canonical_hyperedge(self.a2, self.b1, self.c21),
            canonical_hyperedge(self.a2, self.b2, self.c22),
        )

    @property
    def all_labels(self) -> tuple[Node, ...]:
        return (
            self.a1,
            self.a2,
            self.b1,
            self.b2,
            self.c11,
            self.c12,
            self.c21,
            self.c22,
        )


@dataclass(frozen=True)
class RepeatedNodeClassification:
    """The three affordable repeated-node mechanisms."""

    repeated_node: bool
    adjacent_identical_hyperedge: bool
    square_hyperedge: bool
    opposite_color_equality: bool
    four_distinct_hyperedges: bool
    eight_distinct_labels: bool

    @property
    def affordable_sector(self) -> bool:
        return (
            self.adjacent_identical_hyperedge
            or self.square_hyperedge
            or self.opposite_color_equality
        )


def classify_repeated_nodes(rectangle: Rectangle) -> RepeatedNodeClassification:
    """Classify repetitions in a pair-unique symmetric rectangle.

    For a nondegenerate rectangle whose four unordered hyperedges are
    pair-unique, every repeated label belongs to at least one of the three
    returned affordable mechanisms.  A failed assertion indicates that the
    hypotheses were not met or that the finite classification regressed.
    """

    if not rectangle.nondegenerate:
        raise ValueError("the rectangle must have two rows and two columns")
    edges = rectangle.hyperedges
    if not pair_unique(edges):
        raise ValueError("the four hyperedges are not pair-unique")

    adjacent_pairs = ((0, 1), (2, 3), (0, 2), (1, 3))
    adjacent_identical = any(edges[i] == edges[j] for i, j in adjacent_pairs)
    square = any(len(set(edge)) < 3 for edge in edges)
    opposite_color = (
        rectangle.c11 == rectangle.c22 or rectangle.c12 == rectangle.c21
    )
    repeated = len(set(rectangle.all_labels)) < 8
    classification = RepeatedNodeClassification(
        repeated_node=repeated,
        adjacent_identical_hyperedge=adjacent_identical,
        square_hyperedge=square,
        opposite_color_equality=opposite_color,
        four_distinct_hyperedges=len(set(edges)) == 4,
        eight_distinct_labels=not repeated,
    )
    if repeated and not classification.affordable_sector:
        raise AssertionError("unclassified repeated-node rectangle")
    return classification


def oriented_node_degree(hyperedges: Iterable[Hyperedge]) -> int:
    """Maximum number of ordered partner pairs incident to one node."""

    edges = {canonical_hyperedge(*edge) for edge in hyperedges}
    nodes = sorted({node for edge in edges for node in edge})
    maximum = 0
    for node in nodes:
        partners: set[tuple[Node, Node]] = set()
        for edge in edges:
            # Remove one occurrence of ``node``.  Repeated occurrences give
            # the same partner pair and are intentionally counted once.
            for index, value in enumerate(edge):
                if value == node:
                    rest = [edge[j] for j in range(3) if j != index]
                    partners.add((rest[0], rest[1]))
                    partners.add((rest[1], rest[0]))
                    break
        maximum = max(maximum, len(partners))
    return maximum


def square_root_multiplicity(hyperedges: Iterable[Hyperedge]) -> int:
    """Maximum number of square roots ``x`` in hyperedges ``{x,x,y}``."""

    roots: dict[Node, set[Node]] = {}
    for raw_edge in hyperedges:
        x, y, z = canonical_hyperedge(*raw_edge)
        if x == y:
            roots.setdefault(z, set()).add(x)
        if y == z:
            roots.setdefault(x, set()).add(y)
    return max((len(values) for values in roots.values()), default=0)


def absolute_color_monomial(
    rectangle: Rectangle,
    weights: Mapping[Node, complex],
) -> float:
    """Absolute value of the four color factors in one rectangle."""

    answer = 1.0
    for color in rectangle.colors:
        answer *= abs(weights.get(color, 0.0))
    return answer


def repeated_sector_ledger(
    rectangles: Sequence[Rectangle],
    weights: Mapping[Node, complex],
) -> dict[str, float | int]:
    """Finite replay of the repeated-node bound.

    The theorem proved in the companion report is

    ``mass <= C * Delta * sqrt(max(1, sigma)) * ||z||_2^4``

    for an absolute finite case-count constant ``C``.  We use ``C=18``:
    four adjacent permutation events, twelve oriented square events, and two
    opposite-color events.  Overlaps are harmlessly counted by the union
    bound.  This function computes the left side and its certified envelope.
    """

    unique_rectangles = tuple(dict.fromkeys(rectangles))
    if any(not rectangle.nondegenerate for rectangle in unique_rectangles):
        raise ValueError("all rectangles must be nondegenerate")
    hyperedges = {
        edge for rectangle in unique_rectangles for edge in rectangle.hyperedges
    }
    if not pair_unique(hyperedges):
        raise ValueError("the ambient hypergraph is not pair-unique")
    selected = [
        rectangle
        for rectangle in unique_rectangles
        if classify_repeated_nodes(rectangle).repeated_node
    ]
    mass = sum(absolute_color_monomial(rectangle, weights) for rectangle in selected)
    norm_sq = sum(abs(value) ** 2 for value in weights.values())
    degree = oriented_node_degree(hyperedges)
    square_multiplicity = max(1, square_root_multiplicity(hyperedges))
    bound = 18.0 * degree * square_multiplicity**0.5 * norm_sq**2
    return {
        "rectangles": len(unique_rectangles),
        "repeated_rectangles": len(selected),
        "degree": degree,
        "square_root_multiplicity": square_multiplicity,
        "absolute_mass": mass,
        "certified_bound": bound,
    }

