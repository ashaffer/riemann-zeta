"""Exact ledgers for the packet-subtracted SRH high-completion audit."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd
from typing import Sequence


RowPair = tuple[int, int]


def primitive_relation(rows: Sequence[RowPair]) -> tuple[tuple[int, int, int], int]:
    """Return the primitive three-row cross product and its infinity height."""

    if len(rows) != 3:
        raise ValueError("exactly three row pairs are required")
    (a, A), (b, B), (c, C) = ((int(x), int(y)) for x, y in rows)
    raw = (b * C - c * B, c * A - a * C, a * B - b * A)
    content = gcd(gcd(abs(raw[0]), abs(raw[1])), abs(raw[2]))
    if content == 0:
        raise ValueError("the three row pairs have zero cross product")
    primitive = tuple(value // content for value in raw)
    for value in primitive:
        if value:
            if value < 0:
                primitive = tuple(-entry for entry in primitive)
            break
    return primitive, max(abs(value) for value in primitive)


def reciprocal_height(rows: Sequence[RowPair]) -> float:
    """Return the reciprocal-height sum over all row triples."""

    return sum(
        1.0 / primitive_relation(triple)[1]
        for triple in combinations(rows, 3)
    )


@dataclass(frozen=True)
class SRHCapacityLedger:
    multiplicity_exponent: Fraction
    residual_union_exponent: Fraction
    relation_multiplicity_exponent: Fraction
    reciprocal_height_exponent: Fraction
    tail_exponent: Fraction
    desired_tail_exponent: Fraction
    excess_exponent: Fraction


def srh_capacity_ledger(
    *,
    multiplicity: Fraction,
    residual_union: Fraction,
    relation_multiplicity: Fraction,
) -> SRHCapacityLedger:
    """Return exact powers in ``R<=M^(1/3)Y^2`` and its tail consequence."""

    k = multiplicity
    y = residual_union
    mu = relation_multiplicity
    reciprocal = mu / 3 + 2 * y
    tail = Fraction(1) + reciprocal - 3 * k
    desired = Fraction(1) - k
    return SRHCapacityLedger(
        multiplicity_exponent=k,
        residual_union_exponent=y,
        relation_multiplicity_exponent=mu,
        reciprocal_height_exponent=reciprocal,
        tail_exponent=tail,
        desired_tail_exponent=desired,
        excess_exponent=tail - desired,
    )


@dataclass(frozen=True)
class ActualScatteredFixtureLedger:
    colors: tuple[int, int, int, int]
    determinant: int
    completions: tuple[tuple[int, int, int, int], ...]
    relation_vectors: tuple[tuple[int, int, int], ...]
    relation_heights: tuple[int, ...]
    reciprocal_height_mass: float
    affine_rank: int


def actual_q25013_scattered_fixture() -> ActualScatteredFixtureLedger:
    """Return the exact four-completion actual-prime fixture from the scan."""

    colors = (13103, 12659, 10799, 10433)
    completions = (
        (10903, 13229, 13693, 14173),
        (11483, 13933, 13001, 13457),
        (11681, 14173, 12781, 13229),
        (11743, 14249, 12713, 13159),
    )
    rows = tuple((item[0], item[1]) for item in completions)
    relations = tuple(primitive_relation(triple) for triple in combinations(rows, 3))

    # Exact Gaussian elimination over rationals is unnecessary for this fixed
    # 3-by-4 difference matrix: the displayed 3-by-3 minor is nonzero.
    differences = tuple(
        tuple(completions[i][j] - completions[0][j] for j in range(4))
        for i in range(1, 4)
    )
    minor = (
        differences[0][0]
        * (differences[1][1] * differences[2][2] - differences[1][2] * differences[2][1])
        - differences[0][1]
        * (differences[1][0] * differences[2][2] - differences[1][2] * differences[2][0])
        + differences[0][2]
        * (differences[1][0] * differences[2][1] - differences[1][1] * differences[2][0])
    )
    return ActualScatteredFixtureLedger(
        colors=colors,
        determinant=colors[0] * colors[3] - colors[1] * colors[2],
        completions=completions,
        relation_vectors=tuple(item[0] for item in relations),
        relation_heights=tuple(item[1] for item in relations),
        reciprocal_height_mass=sum(1.0 / item[1] for item in relations),
        affine_rank=3 if minor else 2,
    )
