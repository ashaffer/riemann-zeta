#!/usr/bin/env python3
"""Audit what the value-ordered Mobius collar greedy actually controls.

The underlying greedy is defined in ``mobius_boundary_implicit_greedy.py``.
This companion deliberately stays memory bounded: it reuses the common-core
buckets, never materializes the dense exchange graph, and refuses N > 200000
without an explicit opt-in.

For a bipartite matching with even-omega side E, odd-omega side O, and m
matched pairs, the unmatched count has the exact decomposition

    R = |E-O| + 2 (min(E,O)-m).

On the Mobius collar E-O=M(N).  Thus blocker and augmenting-path analysis can
remove the nonnegative greedy deficiency, but the residual after complete
saturation is exactly |M(N)|.  The optional length-three scan constructs
explicit augmenting-path certificates for the deficiency without building the
full graph.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import DefaultDict, Iterable

from mobius_boundary_exchange import (
    smallest_prime_factors,
    squarefree_factorization,
)
from mobius_boundary_implicit_greedy import (
    CoreBuckets,
    first_available,
    odd_side_buckets,
)


Factors = tuple[int, ...]


@dataclass
class GreedyState:
    limit: int
    vertices: list[tuple[int, Factors]]
    factors: dict[int, Factors]
    even_vertices: list[tuple[int, Factors]]
    odd_count: int
    removed_one: CoreBuckets
    removed_two: CoreBuckets
    even_match: dict[int, int]
    odd_owner: dict[int, int]


def build_state(limit: int) -> GreedyState:
    """Run the exact value/value greedy while retaining its certificate."""

    if limit < 2:
        raise ValueError("N must be at least 2")
    spf = smallest_prime_factors(limit)
    vertices: list[tuple[int, Factors]] = []
    direct_mertens = 0
    lower = limit // 2

    for value in range(1, limit + 1):
        factors = squarefree_factorization(value, spf)
        if factors is None:
            continue
        direct_mertens += -1 if len(factors) & 1 else 1
        if value > lower and value & 1:
            vertices.append((value, factors))

    even, odd_count, removed_one, removed_two = odd_side_buckets(vertices)
    if len(even) - odd_count != direct_mertens:
        raise AssertionError("the exact Mobius collar identity failed")

    pointers_one: DefaultDict[Factors, int] = defaultdict(int)
    pointers_two: DefaultDict[Factors, int] = defaultdict(int)
    used_odd: set[int] = set()
    even_match: dict[int, int] = {}
    odd_owner: dict[int, int] = {}

    for value, factors in even:
        best: int | None = None

        for index, prime in enumerate(factors):
            core = factors[:index] + factors[index + 1 :]
            candidate = first_available(
                removed_two, pointers_two, core, {prime}, used_odd
            )
            if candidate is not None and (best is None or candidate < best):
                best = candidate

        for first, second in combinations(range(len(factors)), 2):
            core = tuple(
                prime
                for index, prime in enumerate(factors)
                if index != first and index != second
            )
            candidate = first_available(
                removed_one,
                pointers_one,
                core,
                {factors[first], factors[second]},
                used_odd,
            )
            if candidate is not None and (best is None or candidate < best):
                best = candidate

        if best is not None:
            used_odd.add(best)
            even_match[value] = best
            odd_owner[best] = value

    return GreedyState(
        limit=limit,
        vertices=vertices,
        factors=dict(vertices),
        even_vertices=even,
        odd_count=odd_count,
        removed_one=removed_one,
        removed_two=removed_two,
        even_match=even_match,
        odd_owner=odd_owner,
    )


def adjacent(left: Factors, right: Factors) -> bool:
    """Whether two factor sets differ by an admissible 1-for-2 exchange."""

    left_set = set(left)
    right_set = set(right)
    difference = (len(left_set - right_set), len(right_set - left_set))
    return difference == (1, 2) or difference == (2, 1)


def odd_neighbors(state: GreedyState, factors: Factors) -> set[int]:
    """Generate all odd neighbors of one even vertex from common-core buckets."""

    neighbors: set[int] = set()

    for index, prime in enumerate(factors):
        core = factors[:index] + factors[index + 1 :]
        for value, extra in state.removed_two.get(core, ()):
            if prime not in extra:
                neighbors.add(value)

    for first, second in combinations(range(len(factors)), 2):
        core = tuple(
            prime
            for index, prime in enumerate(factors)
            if index != first and index != second
        )
        forbidden = {factors[first], factors[second]}
        for value, extra in state.removed_one.get(core, ()):
            if forbidden.isdisjoint(extra):
                neighbors.add(value)

    return neighbors


def length_three_augmentations(
    state: GreedyState,
    unmatched_even: Iterable[int],
    unmatched_odd: Iterable[int],
    needed: int,
    scan_cap: int,
) -> tuple[list[tuple[int, int, int, int]], int, bool]:
    """Greedily construct disjoint paths u--r--e--v.

    Here u and v are unmatched endpoints, r is a matched odd vertex, and e is
    its even owner.  Every returned path is an independently checkable
    augmentation certificate.  Failure to find ``needed`` paths is not a
    no-go theorem: this is a certificate search, not a complete 3-matching
    solver.
    """

    if needed == 0:
        return [], 0, True

    paths: list[tuple[int, int, int, int]] = []
    used: set[int] = set()
    tests = 0
    complete = True

    for left in sorted(unmatched_even):
        if len(paths) == needed:
            break
        if left in used:
            continue
        neighbors = sorted(odd_neighbors(state, state.factors[left]))

        found: tuple[int, int, int, int] | None = None
        for right_endpoint in sorted(unmatched_odd):
            if right_endpoint in used:
                continue
            for matched_right in neighbors:
                owner = state.odd_owner.get(matched_right)
                if owner is None or matched_right in used or owner in used:
                    continue
                tests += 1
                if tests > scan_cap:
                    complete = False
                    break
                if adjacent(state.factors[owner], state.factors[right_endpoint]):
                    found = (left, matched_right, owner, right_endpoint)
                    break
            if not complete or found is not None:
                break
        if not complete:
            break
        if found is not None:
            paths.append(found)
            used.update(found)

    for left, matched_right, owner, right_endpoint in paths:
        if left in state.even_match or right_endpoint in state.odd_owner:
            raise AssertionError("augmentation endpoint is not unmatched")
        if state.even_match.get(owner) != matched_right:
            raise AssertionError("middle edge is not in the greedy matching")
        if not adjacent(state.factors[left], state.factors[matched_right]):
            raise AssertionError("left exchange edge is invalid")
        if not adjacent(state.factors[owner], state.factors[right_endpoint]):
            raise AssertionError("right exchange edge is invalid")

    return paths, tests, complete


def audit(limit: int, scan_cap: int) -> tuple[dict[str, object], list[tuple[int, int, int, int]]]:
    state = build_state(limit)
    even_count = len(state.even_vertices)
    odd_count = state.odd_count
    matched = len(state.even_match)
    mertens = even_count - odd_count

    unmatched_even = [
        value for value, _ in state.even_vertices if value not in state.even_match
    ]
    unmatched_odd = [
        value
        for value, factors in state.vertices
        if len(factors) & 1 and value not in state.odd_owner
    ]

    deficiency = min(even_count, odd_count) - matched
    unmatched = len(unmatched_even) + len(unmatched_odd)
    if unmatched != abs(mertens) + 2 * deficiency:
        raise AssertionError("matching-deficiency decomposition failed")
    if len(unmatched_even) - len(unmatched_odd) != mertens:
        raise AssertionError("unmatched signed sum does not equal M(N)")

    paths, tests, scan_complete = length_three_augmentations(
        state,
        unmatched_even,
        unmatched_odd,
        deficiency,
        scan_cap,
    )
    augmented_matching = matched + len(paths)
    all_unmatched = unmatched_even + unmatched_odd

    result: dict[str, object] = {
        "N": limit,
        "vertices": len(state.vertices),
        "even_omega": even_count,
        "odd_omega": odd_count,
        "M_N": mertens,
        "greedy_matched": matched,
        "greedy_unmatched": unmatched,
        "greedy_deficiency": deficiency,
        "decomposition_verified": True,
        "unmatched_even": len(unmatched_even),
        "unmatched_odd": len(unmatched_odd),
        "unmatched_even_ranks": dict(
            sorted(Counter(len(state.factors[value]) for value in unmatched_even).items())
        ),
        "unmatched_odd_ranks": dict(
            sorted(Counter(len(state.factors[value]) for value in unmatched_odd).items())
        ),
        "earliest_unmatched": min(all_unmatched) if all_unmatched else None,
        "terminal_gap": limit - min(all_unmatched) if all_unmatched else 0,
        "length3_paths_found": len(paths),
        "length3_paths_needed_for_saturation": deficiency,
        "length3_scan_tests": tests,
        "length3_scan_complete": scan_complete,
        "smaller_side_saturated_after_paths": (
            augmented_matching == min(even_count, odd_count)
        ),
        "residual_after_paths": len(state.vertices) - 2 * augmented_matching,
    }
    return result, paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "N", nargs="*", type=int, default=[10000, 20000, 50000, 100000]
    )
    parser.add_argument(
        "--scan-cap",
        type=int,
        default=5_000_000,
        help="maximum factor-set adjacency tests in the length-three scan",
    )
    parser.add_argument(
        "--show-paths",
        action="store_true",
        help="include every constructed augmentation certificate",
    )
    parser.add_argument(
        "--allow-large",
        action="store_true",
        help="allow N>200000; this is intentionally opt-in",
    )
    args = parser.parse_args()

    for limit in args.N:
        if limit > 200000 and not args.allow_large:
            parser.error("N>200000 requires --allow-large")
        result, paths = audit(limit, args.scan_cap)
        if args.show_paths:
            result["length3_paths"] = paths
        print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
