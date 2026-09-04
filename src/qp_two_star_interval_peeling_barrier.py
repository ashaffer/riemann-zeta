"""Finite Latin-block obstruction to local two-star interval peeling.

The construction has the same three pair-uniqueness properties as the QP
triple incidence and can place each row-pair's common carriers in distinct
short intervals.  It deliberately does not assert the reciprocal product
equations or the actual-prime-power mask.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Iterable

import numpy as np


Triple = tuple[int, int, int]
Pair = tuple[int, int]


@dataclass(frozen=True)
class LatinTwoStarFixture:
    groups: int
    degree: int
    interval_count: int
    triples: tuple[Triple, ...]
    carrier_interval: tuple[int, ...]

    @property
    def support_size(self) -> int:
        return self.groups * self.degree


def latin_two_star_fixture(
    groups: int, degree: int, interval_count: int
) -> LatinTwoStarFixture:
    """Build the cyclic fixture ``c=i+s`` in each disjoint group.

    Carrier ``(g,s)`` is assigned interval ``g*degree+s mod Q``.  Since
    ``degree<=Q``, the carriers of one group occupy distinct intervals.
    Integer labels for the three vertex classes are disjoint.
    """

    if groups <= 0 or degree <= 1 or interval_count < degree:
        raise ValueError("need groups>0, degree>1, and Q>=degree")
    block = groups * degree
    triples: list[Triple] = []
    intervals = [0] * block
    for g in range(groups):
        for s in range(degree):
            carrier = g * degree + s
            intervals[carrier] = (g * degree + s) % interval_count
            for i in range(degree):
                row = g * degree + i
                color = 2 * block + g * degree + (i + s) % degree
                triples.append((row, block + carrier, color))
    return LatinTwoStarFixture(
        groups=groups,
        degree=degree,
        interval_count=interval_count,
        triples=tuple(triples),
        carrier_interval=tuple(intervals),
    )


def pair_multiplicities(triples: Iterable[Triple]) -> dict[str, Counter[Pair]]:
    """Return multiplicities of all three coordinate-pair projections."""

    counters = {"row_carrier": Counter(), "carrier_color": Counter(), "row_color": Counter()}
    for row, carrier, color in triples:
        counters["row_carrier"][(row, carrier)] += 1
        counters["carrier_color"][(carrier, color)] += 1
        counters["row_color"][(row, color)] += 1
    return counters


def carrier_degrees(fixture: LatinTwoStarFixture) -> Counter[int]:
    answer: Counter[int] = Counter()
    for _, carrier, _ in fixture.triples:
        answer[carrier] += 1
    return answer


def two_star_count(fixture: LatinTwoStarFixture) -> int:
    return sum(value * (value - 1) for value in carrier_degrees(fixture).values())


def row_pair_interval_loads(
    fixture: LatinTwoStarFixture,
) -> Counter[tuple[Pair, int]]:
    """Count common carriers of each ordered row pair in each interval."""

    rows_by_carrier: dict[int, list[int]] = defaultdict(list)
    block = fixture.support_size
    for row, carrier, _ in fixture.triples:
        rows_by_carrier[carrier].append(row)
    answer: Counter[tuple[Pair, int]] = Counter()
    for carrier, rows in rows_by_carrier.items():
        local = carrier - block
        interval = fixture.carrier_interval[local]
        for row1 in rows:
            for row2 in rows:
                if row1 != row2:
                    answer[((row1, row2), interval)] += 1
    return answer


def pair_incidence_matrix(fixture: LatinTwoStarFixture) -> np.ndarray:
    """Return the binary row-pair/color-pair matrix ``B``."""

    rows_by_carrier: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for row, carrier, color in fixture.triples:
        rows_by_carrier[carrier].append((row, color))

    row_pairs: set[Pair] = set()
    color_pairs: set[Pair] = set()
    edges: list[tuple[Pair, Pair]] = []
    for entries in rows_by_carrier.values():
        for row1, color1 in entries:
            for row2, color2 in entries:
                if row1 == row2:
                    continue
                alpha = (row1, row2)
                gamma = (color1, color2)
                row_pairs.add(alpha)
                color_pairs.add(gamma)
                edges.append((alpha, gamma))

    row_index = {value: index for index, value in enumerate(sorted(row_pairs))}
    color_index = {value: index for index, value in enumerate(sorted(color_pairs))}
    matrix = np.zeros((len(row_index), len(color_index)), dtype=int)
    for alpha, gamma in edges:
        matrix[row_index[alpha], color_index[gamma]] += 1
    if np.any(matrix > 1):
        raise ValueError("pair uniqueness failed in the fixture")
    return matrix


def factorial_row_count(matrix: np.ndarray) -> int:
    row_degrees = np.asarray(matrix, dtype=int).sum(axis=1)
    return int(sum(value * (value - 1) for value in row_degrees))


def triangular_tangent_two_star(length: int) -> int:
    """Return the exact count ``L(L+1)(2L+1)/3`` from Section 5."""

    if length <= 0:
        raise ValueError("length must be positive")
    return length * (length + 1) * (2 * length + 1) // 3


def integer_tangent_packet(center: int, length: int) -> tuple[Triple, ...]:
    """Return the two full-integer triples in (5.2) for every ``(i,u)``."""

    if length <= 0 or center <= 10 * length:
        raise ValueError("need a positive length and a sufficiently large center")
    answer: set[Triple] = set()
    for i in range(length):
        for u in range(length):
            j = 2 * length + u
            carrier = center - i - j - 1
            answer.add((center + i, carrier, center + j + 1))
            answer.add((center + i + 1, carrier, center + j))
    return tuple(sorted(answer))


def cyclic_second_determinants(values: Iterable[int]) -> tuple[int, ...]:
    """Return ``c_j*c_(j+2)-c_(j+1)^2`` with cyclic indexing."""

    sequence = tuple(int(value) for value in values)
    if len(sequence) < 3 or any(value <= 0 for value in sequence):
        raise ValueError("need at least three positive values")
    size = len(sequence)
    return tuple(
        sequence[j] * sequence[(j + 2) % size] - sequence[(j + 1) % size] ** 2
        for j in range(size)
    )
