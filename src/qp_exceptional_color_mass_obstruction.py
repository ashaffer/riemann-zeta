"""Exact additive-color obstruction to a bare exceptional-mass bound.

This module concerns color matrices only.  It does not assert that the
matrices have carrier completions.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import math
from typing import Iterable


@dataclass(frozen=True)
class AdditiveExceptionalLedger:
    colors: tuple[int, int, int, int]
    color_determinant: int
    first_kernel_vector: tuple[int, int, int, int]
    second_kernel_vector: tuple[int, int, int, int]
    successive_product_envelope: float


def additive_exceptional_ledger(
    a: int,
    b: int,
    c: int,
    d: int,
) -> AdditiveExceptionalLedger:
    """Return the two explicit short relations when ``a+d=b+c``."""

    if a + d != b + c:
        raise ValueError("the four colors must obey a+d=b+c")
    if len({a, b, c, d}) < 4:
        raise ValueError("the replay requires four distinct colors")
    # Taking the left endpoint to be zero is harmless because only
    # differences enter the second vector.
    first = (1, 1, 1, 1)
    second = (d - b, d - a, 0, b - a)
    normal = (a, -b, -c, d)
    if sum(x * y for x, y in zip(normal, first)) != 0:
        raise AssertionError("the additive relation failed")
    if sum(x * y for x, y in zip(normal, second)) != 0:
        raise AssertionError("the second short relation failed")
    if second == (0, 0, 0, 0):
        raise AssertionError("the second relation is not independent")
    first_norm = math.sqrt(sum(value * value for value in first))
    second_norm = math.sqrt(sum(value * value for value in second))
    return AdditiveExceptionalLedger(
        colors=(a, b, c, d),
        color_determinant=a * d - b * c,
        first_kernel_vector=first,
        second_kernel_vector=second,
        successive_product_envelope=first_norm * second_norm,
    )


@dataclass(frozen=True)
class FlatAdditiveMass:
    support_size: int
    additive_quadruples: int
    all_distinct_quadruples: int
    flat_all_distinct_mass: float
    maximum_absolute_determinant: int


def flat_additive_mass(values: Iterable[int]) -> FlatAdditiveMass:
    """Enumerate the flat-weighted all-distinct additive color mass."""

    support = tuple(sorted(set(values)))
    pairs: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for left in support:
        for right in support:
            pairs[left + right].append((left, right))
    total = sum(len(items) ** 2 for items in pairs.values())
    distinct = 0
    maximum_determinant = 0
    for items in pairs.values():
        for a, d in items:
            for b, c in items:
                if len({a, b, c, d}) != 4:
                    continue
                distinct += 1
                maximum_determinant = max(
                    maximum_determinant,
                    abs(a * d - b * c),
                )
    size = len(support)
    return FlatAdditiveMass(
        support_size=size,
        additive_quadruples=total,
        all_distinct_quadruples=distinct,
        flat_all_distinct_mass=distinct / size**2 if size else 0.0,
        maximum_absolute_determinant=maximum_determinant,
    )
