#!/usr/bin/env python3
"""Finite exact audit of the anchored codegree tail on log-window fixtures.

This is a diagnostic, not an asymptotic GP_R theorem.  The support-selection
step inherits the floating boundary of ``build_four_cycle_core``; after the
support is materialized, all Gram products and counts are exact integers.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from verify_zeta23_qp_remote_parallel_null_fan_falsifier_affine_falsifier import (
    logarithmic_prime_power_graph,
)


FIXTURES = ((11_801, 35.0), (11_801, 44.0), (25_013, 40.0), (50_021, 40.0))


@dataclass(frozen=True)
class TailLedger:
    q: int
    cutoff: int
    degree_parameter: int
    maximum_off_diagonal_codegree: int
    maximum_anchored_sum: int
    best_bin_mass: int
    best_bin_scale: int
    best_bin_population: int
    best_tail_mass: int
    best_tail_scale: int
    best_tail_population: int


def audit(q: int, cutoff: float) -> TailLedger:
    graph = logarithmic_prime_power_graph(q, cutoff)
    support = graph.support.astype(np.int64)
    gram = (support.T @ support).tocsr()
    maximum_codegree = 0
    maximum_sum = 0
    best_bin = (0, 0, 0)
    best_tail = (0, 0, 0)
    for gamma in range(gram.shape[0]):
        start, stop = gram.indptr[gamma : gamma + 2]
        values: list[int] = []
        anchored_sum = 0
        for position in range(start, stop):
            eta = int(gram.indices[position])
            codegree = int(gram.data[position])
            anchored_sum += codegree
            if eta != gamma:
                values.append(codegree)
                maximum_codegree = max(maximum_codegree, codegree)
        maximum_sum = max(maximum_sum, anchored_sum)
        scale = 1
        while scale <= max(values, default=0):
            bin_population = sum(scale <= value < 2 * scale for value in values)
            tail_population = sum(value >= scale for value in values)
            best_bin = max(best_bin, (scale * bin_population, scale, bin_population))
            best_tail = max(
                best_tail, (scale * tail_population, scale, tail_population)
            )
            scale *= 2
    return TailLedger(
        q=q,
        cutoff=int(cutoff),
        degree_parameter=graph.degree,
        maximum_off_diagonal_codegree=maximum_codegree,
        maximum_anchored_sum=maximum_sum,
        best_bin_mass=best_bin[0],
        best_bin_scale=best_bin[1],
        best_bin_population=best_bin[2],
        best_tail_mass=best_tail[0],
        best_tail_scale=best_tail[1],
        best_tail_population=best_tail[2],
    )


def main() -> None:
    ledgers = tuple(audit(*fixture) for fixture in FIXTURES)
    observed = tuple(
        (
            item.q,
            item.cutoff,
            item.degree_parameter,
            item.maximum_off_diagonal_codegree,
            item.maximum_anchored_sum,
            item.best_bin_mass,
            item.best_bin_scale,
            item.best_bin_population,
            item.best_tail_mass,
            item.best_tail_scale,
            item.best_tail_population,
        )
        for item in ledgers
    )
    expected = (
        (11_801, 35, 94, 4, 39, 24, 1, 24, 26, 1, 26),
        (11_801, 44, 94, 4, 63, 32, 1, 32, 39, 1, 39),
        (25_013, 40, 135, 6, 37, 23, 1, 23, 25, 1, 25),
        (50_021, 40, 189, 4, 33, 20, 1, 20, 23, 1, 23),
    )
    if observed != expected:
        raise AssertionError((observed, expected))
    print("PASS finite anchored GP-tail diagnostic")
    print("q U D maxcodeg maxW bestbin(scale,pop,mass) besttail(scale,pop,mass)")
    for item in ledgers:
        print(
            item.q,
            item.cutoff,
            item.degree_parameter,
            item.maximum_off_diagonal_codegree,
            item.maximum_anchored_sum,
            (item.best_bin_scale, item.best_bin_population, item.best_bin_mass),
            (item.best_tail_scale, item.best_tail_population, item.best_tail_mass),
        )


if __name__ == "__main__":
    main()
