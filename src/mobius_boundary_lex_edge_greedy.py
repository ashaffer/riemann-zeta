#!/usr/bin/env python3
"""Streaming lexicographic-edge greedy scout for the Mobius collar.

For ``S_N = {m : N/2 < m <= N, m odd and squarefree}``, every exchange
edge has a unique representation

    C * p  <->  C * q * r,

where ``q < r < p`` are distinct odd primes, ``C`` is odd and squarefree,
and ``gcd(C, p*q*r) = 1``.  The rule scans these edges in lexicographic
``(q, r, p, C)`` order and accepts an edge exactly when both endpoints are
still unmatched.

The implementation stores sieves and one matched bit per integer, but never
materializes the edge set or adjacency lists.  Its state is therefore O(N),
although its running time still scales with the number of exchange edges.
This is a diagnostic only: a small unmatched count at finite N is not an
estimate for the Mertens function.
"""

from __future__ import annotations

import argparse
import bisect
import json
from collections import Counter
from math import gcd

from mobius_boundary_exchange import smallest_prime_factors, squarefree_factorization


def run(limit: int) -> dict[str, object]:
    """Run the streaming greedy rule and return an auditable summary."""

    if limit < 2:
        raise ValueError("N must be at least 2")

    spf = smallest_prime_factors(limit)
    primes = [p for p in range(3, limit + 1, 2) if spf[p] == p]

    # This bitset recognizes precisely the admissible common cores.  The
    # factorization tuples used to fill it are transient rather than stored.
    odd_squarefree = bytearray(limit + 1)
    mertens = 0
    for value in range(1, limit + 1):
        factors = squarefree_factorization(value, spf)
        if factors is None:
            continue
        mertens += -1 if len(factors) & 1 else 1
        if value & 1:
            odd_squarefree[value] = 1

    matched = bytearray(limit + 1)
    edge_count = 0
    matching_size = 0

    # The inequalities qr < 2p and p < 2qr are exactly the requirement that
    # the two endpoints can occur in the same dyadic collar.  Requiring p > r
    # loses no edges: if p < r, then qr/p > q >= 3, contradicting that ratio.
    for q_index, q in enumerate(primes):
        for r in primes[q_index + 1 :]:
            qr = q * r
            if qr > limit:
                break

            first_p = bisect.bisect_right(primes, max(r, qr // 2))
            after_last_p = bisect.bisect_left(primes, min(limit + 1, 2 * qr))
            for p in primes[first_p:after_last_p]:
                # Both C*p and C*q*r must lie in (N/2, N].
                first_core = max(limit // (2 * p), limit // (2 * qr)) + 1
                last_core = min(limit // p, limit // qr)
                pqr = p * qr

                for core in range(first_core, last_core + 1):
                    if not odd_squarefree[core] or gcd(core, pqr) != 1:
                        continue

                    single_value = core * p
                    pair_value = core * qr
                    edge_count += 1
                    if not matched[single_value] and not matched[pair_value]:
                        matched[single_value] = 1
                        matched[pair_value] = 1
                        matching_size += 1

    lower = limit // 2
    vertex_count = 0
    collar_sum = 0
    unmatched: list[int] = []
    unmatched_by_omega: Counter[int] = Counter()
    for value in range(lower + 1, limit + 1):
        if not (value & 1 and odd_squarefree[value]):
            continue
        factors = squarefree_factorization(value, spf)
        if factors is None:  # Guard the bitset/factorization invariant.
            raise AssertionError("odd-squarefree bitset contained a nonsquarefree value")
        vertex_count += 1
        collar_sum += -1 if len(factors) & 1 else 1
        if not matched[value]:
            unmatched.append(value)
            unmatched_by_omega[len(factors)] += 1

    if collar_sum != mertens:
        raise AssertionError("the exact Mobius collar identity failed")

    unmatched_count = len(unmatched)
    return {
        "N": limit,
        "vertices": vertex_count,
        "M_N": mertens,
        "abs_M_N": abs(mertens),
        "edges_scanned": edge_count,
        "matching_size": matching_size,
        "unmatched": unmatched_count,
        "excess_over_abs_M": unmatched_count - abs(mertens),
        "unmatched_by_omega": dict(sorted(unmatched_by_omega.items())),
        "min_unmatched": min(unmatched) if unmatched else None,
        "max_unmatched": max(unmatched) if unmatched else None,
        "collar_identity_verified": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", nargs="*", type=int, default=[1000, 10000, 30000])
    parser.add_argument(
        "--allow-large",
        action="store_true",
        help="allow N>50000; memory remains linear but edge enumeration is expensive",
    )
    args = parser.parse_args()

    for limit in args.N:
        if limit > 50000 and not args.allow_large:
            parser.error("N>50000 requires --allow-large")
        print(json.dumps(run(limit), sort_keys=True))


if __name__ == "__main__":
    main()
