"""Exact arithmetic for the surviving large raw-chord gate.

The finite fixture in this module is not an asymptotic counterexample.  It
does show that an odd prime centre and globally distinct prime labels can
support two disconnected common-neighbour chords with the same color
translation but different carrier translations.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class CommonNeighbor:
    h: int
    carrier: int
    first_color: int
    second_color: int


@dataclass(frozen=True)
class ChordLedger:
    residual_shift: int
    carrier_drop: int
    first_color_rise: int
    second_color_rise: int
    direction_gcd: int
    color_line_invariant: int
    first_product_change: int
    second_product_change: int


FIXTURE_Q = 1_600_033
FIXTURE_ROWS = (791_563, 880_007)
FIXTURE_DEGREE = 69_885
FIXTURE_NEIGHBORS = (
    CommonNeighbor(-14_176, 806_801, 801_761, 721_181),
    CommonNeighbor(-8_274, 862_297, 750_161, 674_767),
    CommonNeighbor(578, 689_929, 937_577, 843_347),
    CommonNeighbor(6_480, 730_111, 885_977, 796_933),
)


def chord_ledger(source: CommonNeighbor, target: CommonNeighbor) -> ChordLedger:
    """Return the exact invariants of an oriented increasing-color chord."""

    u = source.carrier - target.carrier
    v = target.first_color - source.first_color
    w = target.second_color - source.second_color
    k = target.h - source.h
    if min(u, v, w) <= 0:
        raise ValueError("the chord is not in the decreasing-carrier orientation")
    g = math.gcd(v, w)
    lam = v * source.second_color - w * source.first_color
    s = target.carrier * target.first_color - source.carrier * source.first_color
    t = target.carrier * target.second_color - source.carrier * source.second_color
    if u * lam != w * s - v * t:
        raise AssertionError("the two-product chord identity failed")
    return ChordLedger(k, u, v, w, g, lam, s, t)


def cubic_residual(q: int, row: int, neighbor: CommonNeighbor, *, second: bool) -> int:
    """Return ``8*row*b*color-q**3`` at one common-neighbour corner."""

    color = neighbor.second_color if second else neighbor.first_color
    return 8 * row * neighbor.carrier * color - q**3


def fixture_labels() -> tuple[int, ...]:
    """Return every prime label used by the fixture, including ``q``."""

    labels = [FIXTURE_Q, *FIXTURE_ROWS]
    for item in FIXTURE_NEIGHBORS:
        labels.extend((item.carrier, item.first_color, item.second_color))
    return tuple(labels)


def literal_common_neighbors(
    q: int,
    degree: int,
    rows: tuple[int, int],
    shell: tuple[int, ...],
) -> tuple[CommonNeighbor, ...]:
    """Enumerate a fixed row pair in the exact ``q*degree`` hard window."""

    target = q**3
    a, a_prime = rows
    shell_set = set(shell)
    answer: list[CommonNeighbor] = []
    for carrier in shell:
        first_denominator = 8 * a * carrier
        second_denominator = 8 * a_prime * carrier
        first_color = (target + first_denominator // 2) // first_denominator
        second_color = (target + second_denominator // 2) // second_denominator
        if first_color not in shell_set or second_color not in shell_set:
            continue
        if abs(first_denominator * first_color - target) >= q * degree:
            continue
        if abs(second_denominator * second_color - target) >= q * degree:
            continue
        answer.append(
            CommonNeighbor(
                a_prime * second_color - a * first_color,
                carrier,
                first_color,
                second_color,
            )
        )
    return tuple(sorted(answer, key=lambda item: item.h))
