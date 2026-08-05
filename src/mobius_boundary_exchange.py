#!/usr/bin/env python3
"""Small-N scout for the squarefree boundary-exchange reduction.

For N >= 2, the vertices are the odd squarefree integers in (N/2, N].
Two vertices are adjacent when their prime-factor sets differ by replacing
one prime with two primes.  Every edge therefore joins opposite Mobius signs.

The maximum matching is only a diagnostic.  Even when it saturates the
smaller color class, the number of unmatched vertices is then exactly
|M(N)|, so it does not prove a new bound for the Mertens function.

The graph becomes dense.  The command-line interface therefore refuses
N > 10000 unless ``--allow-dense`` is passed explicitly.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from dataclasses import dataclass
from itertools import combinations
from typing import DefaultDict, Iterable


@dataclass(frozen=True)
class Vertex:
    value: int
    factors: tuple[int, ...]

    @property
    def parity(self) -> int:
        return len(self.factors) & 1

    @property
    def mobius(self) -> int:
        return -1 if self.parity else 1


def smallest_prime_factors(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    p = 2
    while p * p <= limit:
        if spf[p] == p:
            for multiple in range(p * p, limit + 1, p):
                if spf[multiple] == multiple:
                    spf[multiple] = p
        p += 1
    return spf


def squarefree_factorization(n: int, spf: list[int]) -> tuple[int, ...] | None:
    factors: list[int] = []
    while n > 1:
        p = spf[n]
        n //= p
        if n % p == 0:
            return None
        factors.append(p)
    return tuple(factors)


def boundary_vertices(limit: int, spf: list[int]) -> list[Vertex]:
    vertices: list[Vertex] = []
    for value in range(limit // 2 + 1, limit + 1):
        if value % 2 == 0:
            continue
        factors = squarefree_factorization(value, spf)
        if factors is not None:
            vertices.append(Vertex(value, factors))
    return vertices


def direct_mertens(limit: int, spf: list[int]) -> int:
    total = 0
    for value in range(1, limit + 1):
        factors = squarefree_factorization(value, spf)
        if factors is not None:
            total += -1 if len(factors) & 1 else 1
    return total


def exchange_graph(
    vertices: list[Vertex],
) -> tuple[list[int], list[int], dict[int, list[int]], int, int]:
    """Build the parity-bipartite graph by common-core hashing.

    If A=C union {p} and B=C union {q,r}, the edge is admitted only when
    p,q,r are distinct.  In this particular collar the filter is automatic:
    a false nested pair would have ratio at least 3, while two collar values
    have ratio less than 2.  We retain the explicit check as an audit guard.
    """

    removed_one: DefaultDict[tuple[int, ...], list[tuple[int, int]]] = defaultdict(list)
    removed_two: DefaultDict[
        tuple[int, ...], list[tuple[int, tuple[int, int]]]
    ] = defaultdict(list)

    even: list[int] = []
    odd: list[int] = []
    for index, vertex in enumerate(vertices):
        (odd if vertex.parity else even).append(index)
        factors = vertex.factors
        for i, p in enumerate(factors):
            removed_one[factors[:i] + factors[i + 1 :]].append((index, p))
        for i, j in combinations(range(len(factors)), 2):
            core = tuple(
                p for k, p in enumerate(factors) if k != i and k != j
            )
            removed_two[core].append((index, (factors[i], factors[j])))

    adjacency: dict[int, list[int]] = {index: [] for index in even}
    degree = [0] * len(vertices)
    edge_count = 0
    rejected_nested = 0
    for core, one_entries in removed_one.items():
        two_entries = removed_two.get(core, ())
        for one_index, p in one_entries:
            for two_index, qr in two_entries:
                if p in qr:
                    rejected_nested += 1
                    continue
                if vertices[one_index].parity == 0:
                    left, right = one_index, two_index
                else:
                    left, right = two_index, one_index
                adjacency[left].append(right)
                degree[left] += 1
                degree[right] += 1
                edge_count += 1

    isolated = sum(d == 0 for d in degree)
    return even, odd, adjacency, edge_count, isolated


def hopcroft_karp(left: Iterable[int], adjacency: dict[int, list[int]]) -> int:
    left = list(left)
    pair_left: dict[int, int | None] = {u: None for u in left}
    pair_right: dict[int, int] = {}
    distance: dict[int, int] = {}
    infinity = len(left) + 1

    def breadth_first() -> bool:
        queue: deque[int] = deque()
        shortest = infinity
        for u in left:
            if pair_left[u] is None:
                distance[u] = 0
                queue.append(u)
            else:
                distance[u] = infinity
        while queue:
            u = queue.popleft()
            if distance[u] >= shortest:
                continue
            for v in adjacency[u]:
                mate = pair_right.get(v)
                if mate is None:
                    shortest = distance[u] + 1
                elif distance[mate] == infinity:
                    distance[mate] = distance[u] + 1
                    queue.append(mate)
        return shortest != infinity

    def depth_first(u: int) -> bool:
        for v in adjacency[u]:
            mate = pair_right.get(v)
            if mate is None or (
                distance.get(mate, infinity) == distance[u] + 1
                and depth_first(mate)
            ):
                pair_left[u] = v
                pair_right[v] = u
                return True
        distance[u] = infinity
        return False

    matching = 0
    while breadth_first():
        for u in left:
            if pair_left[u] is None and depth_first(u):
                matching += 1
    return matching


def greedy_matching(
    left: list[int], adjacency: dict[int, list[int]], vertices: list[Vertex], mode: str
) -> int:
    if mode == "value":
        order = sorted(left, key=lambda i: vertices[i].value)
    elif mode == "degree":
        order = sorted(left, key=lambda i: (len(adjacency[i]), vertices[i].value))
    else:
        raise ValueError(f"unknown greedy mode: {mode}")

    used_right: set[int] = set()
    matched = 0
    for u in order:
        candidates = (v for v in adjacency[u] if v not in used_right)
        try:
            v = min(candidates, key=lambda i: vertices[i].value)
        except ValueError:
            continue
        used_right.add(v)
        matched += 1
    return matched


def run(limit: int) -> dict[str, int | bool | dict[str, int]]:
    if limit < 2:
        raise ValueError("N must be at least 2")
    spf = smallest_prime_factors(limit)
    vertices = boundary_vertices(limit, spf)
    even, odd, adjacency, edges, isolated = exchange_graph(vertices)

    collar_sum = sum(vertex.mobius for vertex in vertices)
    mertens = direct_mertens(limit, spf)
    if collar_sum != mertens:
        raise AssertionError("the exact Mobius collar identity failed")

    maximum = hopcroft_karp(even, adjacency)
    greedy_value = greedy_matching(even, adjacency, vertices, "value")
    greedy_degree = greedy_matching(even, adjacency, vertices, "degree")
    vertex_count = len(vertices)
    return {
        "N": limit,
        "vertices": vertex_count,
        "even_omega": len(even),
        "odd_omega": len(odd),
        "M_N": mertens,
        "collar_identity_verified": True,
        "edges": edges,
        "isolated": isolated,
        "maximum_matching": maximum,
        "maximum_unmatched": vertex_count - 2 * maximum,
        "smaller_color_saturated": maximum == min(len(even), len(odd)),
        "greedy_unmatched": {
            "value": vertex_count - 2 * greedy_value,
            "degree_then_value": vertex_count - 2 * greedy_degree,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", nargs="*", type=int, default=[1000, 3000])
    parser.add_argument("--json", action="store_true", help="emit JSON lines")
    parser.add_argument(
        "--allow-dense",
        action="store_true",
        help="allow N>10000 even though explicit adjacency can use substantial memory",
    )
    args = parser.parse_args()

    for limit in args.N:
        if limit > 10000 and not args.allow_dense:
            parser.error("N>10000 requires --allow-dense (the exchange graph is dense)")
        result = run(limit)
        if args.json:
            print(json.dumps(result, sort_keys=True))
        else:
            print(
                "N={N} vertices={vertices} colors={even_omega}/{odd_omega} "
                "M(N)={M_N:+d} edges={edges} isolated={isolated} "
                "max_unmatched={maximum_unmatched} saturated={smaller_color_saturated} "
                "greedy(value/degree)={greedy_unmatched[value]}/"
                "{greedy_unmatched[degree_then_value]}".format(**result)
            )


if __name__ == "__main__":
    main()
