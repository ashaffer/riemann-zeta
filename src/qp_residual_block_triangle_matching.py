"""Residual-block matching identities for the QP carrier hypergraph.

This module records an exact elementary observation.  If actual product
residuals

    rho(a,b,c) = 8*a*b*c - q**3

are partitioned into half-open intervals shorter than ``8*min(shell)``, then
no two distinct unordered triples in one interval can share a shell node.
Consequently every residual block is a disjoint union of 3-vertex edges.

The second half of the module supplies the affine-plane Steiner triple
system on nine points.  Its four parallel classes are residual-block-like
matchings, but their union has a large constant mode.  It certifies that the
matching lemma alone is not the missing expansion theorem.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from typing import Iterable, Sequence

import numpy as np


Triple = tuple[int, int, int]


def product_residual(q: int, triple: Sequence[int]) -> int:
    """Return ``8*prod(triple)-q^3`` for a three-element sequence."""

    if len(triple) != 3:
        raise ValueError("triple must have exactly three entries")
    a, b, c = (int(x) for x in triple)
    return 8 * a * b * c - int(q) ** 3


def same_short_block_forces_disjoint_or_equal(
    q: int,
    first: Sequence[int],
    second: Sequence[int],
    block_width: int,
) -> bool:
    """Check the exact divisibility conclusion for one pair of triples.

    The return value is true precisely when triples in the same sufficiently
    short residual block are either equal as multisets or vertex-disjoint.
    A ``ValueError`` is raised when the requested width is not below the
    theorem's divisibility threshold.
    """

    x = tuple(sorted(int(v) for v in first))
    y = tuple(sorted(int(v) for v in second))
    minimum = min(x + y)
    if not 0 < block_width < 8 * minimum:
        raise ValueError("block_width must be smaller than 8*min(nodes)")
    rx = product_residual(q, x)
    ry = product_residual(q, y)
    if rx // block_width != ry // block_width:
        return True
    return x == y or set(x).isdisjoint(y)


def residual_blocks(
    q: int,
    triples: Iterable[Sequence[int]],
    block_width: int,
) -> dict[int, list[Triple]]:
    """Group unordered triples by their exact residual block."""

    if block_width <= 0:
        raise ValueError("block_width must be positive")
    blocks: dict[int, list[Triple]] = defaultdict(list)
    for raw in triples:
        triple = tuple(sorted(int(v) for v in raw))
        if len(triple) != 3:
            raise ValueError("every edge must have three entries")
        blocks[product_residual(q, triple) // block_width].append(triple)
    return dict(blocks)


def blocks_are_vertex_matchings(
    q: int,
    triples: Iterable[Sequence[int]],
    block_width: int,
) -> bool:
    """Return whether every block is a vertex-disjoint triple matching."""

    materialized = [tuple(sorted(int(v) for v in t)) for t in triples]
    if materialized and block_width >= 8 * min(min(t) for t in materialized):
        raise ValueError("block_width is outside the proved range")
    for edges in residual_blocks(q, materialized, block_width).values():
        used: set[int] = set()
        for edge in edges:
            if used.intersection(edge):
                return False
            used.update(edge)
    return True


def affine_plane_sts9_parallel_classes() -> list[list[tuple[int, int, int]]]:
    """Return the four parallel classes of the affine plane over F_3.

    Points ``(x,y)`` are encoded as ``3*x+y``.  Lines of each of the four
    slopes form one class of three disjoint triples.  Every unordered pair of
    points lies on exactly one returned line.
    """

    points = [(x, y) for x in range(3) for y in range(3)]
    encode = lambda p: 3 * p[0] + p[1]
    classes: list[list[tuple[int, int, int]]] = []
    # Vertical lines x=b.
    classes.append(
        [tuple(sorted(encode((b, y)) for y in range(3))) for b in range(3)]
    )
    # The other slopes are y=m*x+b.
    for slope in range(3):
        classes.append(
            [
                tuple(
                    sorted(
                        encode((x, (slope * x + intercept) % 3))
                        for x in range(3)
                    )
                )
                for intercept in range(3)
            ]
        )
    return classes


def weighted_steiner_adjacency(
    classes: Sequence[Sequence[Sequence[int]]],
    weights: Sequence[float],
) -> np.ndarray:
    """Build ``A[i,j]=weight[k]`` when ``{i,j,k}`` is a triple."""

    z = np.asarray(weights, dtype=float)
    matrix = np.zeros((z.size, z.size), dtype=float)
    for parallel_class in classes:
        for raw_edge in parallel_class:
            edge = tuple(int(v) for v in raw_edge)
            if len(edge) != 3:
                raise ValueError("all hyperedges must be triples")
            for i, j in combinations(edge, 2):
                k = next(v for v in edge if v not in (i, j))
                matrix[i, j] = z[k]
                matrix[j, i] = z[k]
    return matrix


def schatten_fourth_power(matrix: np.ndarray) -> float:
    """Return ``tr((A* A)^2)`` for a real or complex matrix."""

    gram = np.asarray(matrix).conj().T @ np.asarray(matrix)
    return float(np.trace(gram @ gram).real)

