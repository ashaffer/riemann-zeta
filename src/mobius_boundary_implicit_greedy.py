#!/usr/bin/env python3
"""Memory-bounded deterministic greedy scout for the Mobius collar graph.

Even-omega vertices are processed by increasing integer value.  Each is paired
with the smallest currently unused odd-omega neighbor under a valid
one-prime-for-two-primes exchange.  The rule never inspects M(N), the two
global color counts, or a maximum matching.

Unlike ``mobius_boundary_exchange.py``, this script hashes only odd-side
common-core buckets and does not materialize the dense edge set.  It is still
a diagnostic: proving an RH-scale unmatched bound is the substantive theorem.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from itertools import combinations
from typing import DefaultDict, Iterable

from mobius_boundary_exchange import smallest_prime_factors, squarefree_factorization


Entry = tuple[int, tuple[int, ...]]
CoreBuckets = DefaultDict[tuple[int, ...], list[Entry]]


def odd_side_buckets(
    vertices: Iterable[tuple[int, tuple[int, ...]]],
) -> tuple[list[tuple[int, tuple[int, ...]]], int, CoreBuckets, CoreBuckets]:
    even_vertices: list[tuple[int, tuple[int, ...]]] = []
    odd_count = 0
    removed_one: CoreBuckets = defaultdict(list)
    removed_two: CoreBuckets = defaultdict(list)

    for value, factors in vertices:
        if len(factors) % 2 == 0:
            even_vertices.append((value, factors))
            continue
        odd_count += 1
        for i, p in enumerate(factors):
            removed_one[factors[:i] + factors[i + 1 :]].append((value, (p,)))
        for i, j in combinations(range(len(factors)), 2):
            core = tuple(
                p for k, p in enumerate(factors) if k != i and k != j
            )
            removed_two[core].append((value, (factors[i], factors[j])))
    return even_vertices, odd_count, removed_one, removed_two


def first_available(
    buckets: CoreBuckets,
    pointers: DefaultDict[tuple[int, ...], int],
    core: tuple[int, ...],
    forbidden: set[int],
    used: set[int],
) -> int | None:
    entries = buckets.get(core, ())
    index = pointers[core]
    while index < len(entries) and entries[index][0] in used:
        index += 1
    pointers[core] = index

    # A forbidden overlap cannot actually survive the common collar (the two
    # values would have ratio at least 3), but the explicit check protects the
    # graph definition if the window is changed later.
    for value, extra in entries[index:]:
        if value not in used and forbidden.isdisjoint(extra):
            return value
    return None


def run(limit: int) -> dict[str, int | bool]:
    if limit < 2:
        raise ValueError("N must be at least 2")
    spf = smallest_prime_factors(limit)

    mertens = 0
    vertices: list[tuple[int, tuple[int, ...]]] = []
    lower = limit // 2
    for value in range(1, limit + 1):
        factors = squarefree_factorization(value, spf)
        if factors is None:
            continue
        mobius = -1 if len(factors) & 1 else 1
        mertens += mobius
        if value > lower and value & 1:
            vertices.append((value, factors))

    collar_sum = sum(-1 if len(factors) & 1 else 1 for _, factors in vertices)
    if collar_sum != mertens:
        raise AssertionError("the exact Mobius collar identity failed")

    even, odd_count, removed_one, removed_two = odd_side_buckets(vertices)
    pointers_one: DefaultDict[tuple[int, ...], int] = defaultdict(int)
    pointers_two: DefaultDict[tuple[int, ...], int] = defaultdict(int)
    used_odd: set[int] = set()
    matched = 0

    for _, factors in even:
        best: int | None = None

        # This even vertex is C union {p}; seek an odd C union {q,r}.
        for i, p in enumerate(factors):
            core = factors[:i] + factors[i + 1 :]
            candidate = first_available(
                removed_two, pointers_two, core, {p}, used_odd
            )
            if candidate is not None and (best is None or candidate < best):
                best = candidate

        # This even vertex is C union {q,r}; seek an odd C union {p}.
        for i, j in combinations(range(len(factors)), 2):
            core = tuple(
                p for k, p in enumerate(factors) if k != i and k != j
            )
            candidate = first_available(
                removed_one,
                pointers_one,
                core,
                {factors[i], factors[j]},
                used_odd,
            )
            if candidate is not None and (best is None or candidate < best):
                best = candidate

        if best is not None:
            used_odd.add(best)
            matched += 1

    even_count = len(even)
    vertex_count = len(vertices)
    unmatched = vertex_count - 2 * matched
    return {
        "N": limit,
        "vertices": vertex_count,
        "even_omega": even_count,
        "odd_omega": odd_count,
        "M_N": mertens,
        "matched": matched,
        "unmatched": unmatched,
        "excess_over_abs_M": unmatched - abs(mertens),
        "collar_identity_verified": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", nargs="*", type=int, default=[10000, 100000, 200000])
    parser.add_argument(
        "--allow-large",
        action="store_true",
        help="allow N>200000; factor tables and buckets can still use substantial memory",
    )
    args = parser.parse_args()
    for limit in args.N:
        if limit > 200000 and not args.allow_large:
            parser.error("N>200000 requires --allow-large")
        print(json.dumps(run(limit), sort_keys=True))


if __name__ == "__main__":
    main()
