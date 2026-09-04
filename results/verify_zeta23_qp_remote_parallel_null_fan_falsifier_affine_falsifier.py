#!/usr/bin/env python3
"""Falsification audit for the physical remote parallel-null fan gate.

The script searches literal critical hard-window integer and prime-power
graphs, plus the materialized actual-prime-power logarithmic fixtures, for
two rich neighbor lines based at one residual transition edge.  It records
only line pairs whose primitive directions are null for

    F((d,D),(e,E)) = d*e-D*E.

It checks witness nonaffinity, remote curvature scale, the stationary line
constants h_U,h_V, central-edge deletion, and population/D.  On the actual
prime-power fixtures it also tests the strengthened whole-star inverse

    |U_e||V_e| <= C (D + R_U R_V),

where R_U,R_V are maximum affine-line occupancies, and computes exact
minimum affine-line covers of the small finite neighborhoods.

These are finite diagnostics.  Logarithmic fixtures inherit the support
builder's floating nearest-integer boundary; literal fixtures and every
post-materialization invariant use exact integer arithmetic.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import ceil, gcd
from pathlib import Path
import gc
import sys
from typing import Sequence

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_actual_prime_nds import (  # noqa: E402
    actual_prime_residual_double_star,
    exact_balanced_degree,
)
from qp_four_cycle_h_graph_lab import (  # noqa: E402
    build_pair_incidence_graph,
    decode_pair,
    filtered_pair_incidence_graph,
)
from qp_four_cycle_hostile_lab import build_four_cycle_core  # noqa: E402
from qp_rank_one_h_tangent_residual import (  # noqa: E402
    literal_hard_window_triples,
    transition_witnesses,
)
from qp_scattered_token_search import (  # noqa: E402
    full_integer_shell,
    full_prime_power_shell,
)
from qp_tangent_plucker_inverse import physical_affine_transition_grid  # noqa: E402


Point = tuple[int, int]
Edge = tuple[int, int]
LineKey = tuple[int, int, int]


STRICT_INTEGER_FIXTURES = (809, 1_400, 3_500, 10_000, 20_000)
STRICT_PRIME_POWER_FIXTURES = (11_801, 25_013, 100_003, 200_003)
LOG_PRIME_POWER_FIXTURES = (
    (11_801, 35.0),
    (11_801, 44.0),
    (25_013, 40.0),
    (50_021, 40.0),
)


@dataclass(frozen=True)
class CompactGraph:
    label: str
    q: int
    degree: int
    left_pairs: np.ndarray
    right_pairs: np.ndarray
    support: csr_matrix
    carriers: csr_matrix
    maximum_source_residual: int


@dataclass(frozen=True)
class NeighborEntry:
    point: Point
    witness: int
    edge: Edge


@dataclass(frozen=True)
class RichLine:
    side: str
    anchor_index: int
    key: LineKey
    entries: tuple[NeighborEntry, ...]
    witness_affine: bool
    parameter_span: int

    @property
    def direction(self) -> Point:
        return self.key[0], self.key[1]

    @property
    def population(self) -> int:
        return len(self.entries)

    @property
    def remote_numerator(self) -> int:
        nonzero = tuple(abs(value) for value in self.direction if value)
        return min(nonzero) ** 2 * self.parameter_span**3


@dataclass(frozen=True)
class NullFan:
    edge: Edge
    left: RichLine
    right: RichLine
    h_left: int
    h_right: int

    @property
    def population_product(self) -> int:
        return self.left.population * self.right.population


@dataclass(frozen=True)
class NullFanSummary:
    rich_left_anchors: int
    rich_right_anchors: int
    null_fans: int
    both_nonaffine_fans: int
    both_remote_fans: int
    zero_zero_fans: int
    maximum_population_product: int
    maximum_both_nonaffine_product: int
    maximum_trimmed_both_nonaffine_product: int
    maximum_fan: NullFan | None
    maximum_nonaffine_fan: NullFan | None
    h_strata: tuple[tuple[str, int, int, int], ...]
    left_lines: dict[int, tuple[RichLine, ...]]
    right_lines: dict[int, tuple[RichLine, ...]]


@dataclass(frozen=True)
class DominantFanSummary:
    maximum_ratio: Fraction
    maximum_edge: Edge
    left_degree: int
    right_degree: int
    left_line_occupancy: int
    right_line_occupancy: int
    left_line_cover: int
    right_line_cover: int
    maximum_line_cover: int


def primitive_line_key(first: Point, second: Point) -> LineKey:
    dx, dy = second[0] - first[0], second[1] - first[1]
    divisor = gcd(abs(dx), abs(dy))
    if not divisor:
        raise ValueError("a line needs distinct points")
    direction_x, direction_y = dx // divisor, dy // divisor
    if direction_x < 0 or (direction_x == 0 and direction_y < 0):
        direction_x, direction_y = -direction_x, -direction_y
    return (
        direction_x,
        direction_y,
        -direction_y * first[0] + direction_x * first[1],
    )


def parameter_witnesses(
    key: LineKey, entries: Sequence[NeighborEntry]
) -> tuple[tuple[int, int], ...]:
    direction_x, direction_y, constant = key
    base = min(entry.point for entry in entries)
    answer: list[tuple[int, int]] = []
    for entry in entries:
        difference_x = entry.point[0] - base[0]
        difference_y = entry.point[1] - base[1]
        if direction_x:
            if difference_x % direction_x:
                raise AssertionError("nonintegral line parameter")
            parameter = difference_x // direction_x
            if difference_y != parameter * direction_y:
                raise AssertionError("point misses line")
        else:
            if difference_y % direction_y or difference_x:
                raise AssertionError("point misses vertical line")
            parameter = difference_y // direction_y
        if -direction_y * entry.point[0] + direction_x * entry.point[1] != constant:
            raise AssertionError("line constant mismatch")
        answer.append((parameter, entry.witness))
    return tuple(sorted(answer))


def witnesses_affine(key: LineKey, entries: Sequence[NeighborEntry]) -> bool:
    values = parameter_witnesses(key, entries)
    first_t, first_x = values[0]
    second_t, second_x = values[1]
    return all(
        (witness - first_x) * (second_t - first_t)
        == (second_x - first_x) * (parameter - first_t)
        for parameter, witness in values[2:]
    )


def exact_graph(
    q: int,
    values: Sequence[int],
    *,
    label: str,
    degree: int | None = None,
) -> CompactGraph:
    radius = exact_balanced_degree(q) if degree is None else degree
    triples = literal_hard_window_triples(q, radius, tuple(values))
    raw = transition_witnesses(triples)
    edges = tuple(
        (left, right, witness)
        for (left, right), witness in raw.items()
        if left[0] != left[1]
        and right[0] != right[1]
        and len({*left, *right, witness}) == 5
        and left[0] * right[0] != left[1] * right[1]
    )
    left_pairs = tuple(sorted({left for left, _right, _witness in edges}))
    right_pairs = tuple(sorted({right for _left, right, _witness in edges}))
    left_index = {pair: index for index, pair in enumerate(left_pairs)}
    right_index = {pair: index for index, pair in enumerate(right_pairs)}
    rows = [left_index[left] for left, _right, _witness in edges]
    columns = [right_index[right] for _left, right, _witness in edges]
    witnesses = [witness for _left, _right, witness in edges]
    shape = (len(left_pairs), len(right_pairs))
    support = coo_matrix(
        (np.ones(len(edges), dtype=np.int8), (rows, columns)), shape=shape
    ).tocsr()
    carriers = coo_matrix((witnesses, (rows, columns)), shape=shape).tocsr()
    if support.nnz != len(edges) or np.any(support.data != 1):
        raise AssertionError("one exact transition has multiple witnesses")
    maximum_residual = max(
        (abs(8 * a * b * c - q**3) for a, b, c in triples), default=0
    )
    return CompactGraph(
        label,
        q,
        radius,
        np.asarray(left_pairs, dtype=np.int64).reshape((-1, 2)),
        np.asarray(right_pairs, dtype=np.int64).reshape((-1, 2)),
        support,
        carriers,
        maximum_residual,
    )


def logarithmic_prime_power_graph(q: int, cutoff: float) -> CompactGraph:
    core = build_four_cycle_core(
        q,
        cutoff=cutoff,
        kind="prime_powers",
        quadrature_order=8,
    )
    graph = filtered_pair_incidence_graph(
        core,
        build_pair_incidence_graph(core),
        keep="all_five_distinct",
    )

    def pairs(codes: np.ndarray) -> np.ndarray:
        answer = np.empty((len(codes), 2), dtype=np.int64)
        for index, code in enumerate(codes):
            first, second = decode_pair(int(code), core.dimension)
            answer[index] = (int(core.values[first]), int(core.values[second]))
        return answer

    residuals = np.abs(8 * core.values[core.rows] * core.values[core.columns] * core.values[core.colors] - q**3)
    return CompactGraph(
        f"prime-power-log-U{int(cutoff)}",
        q,
        exact_balanced_degree(q),
        pairs(graph.left_pair_codes),
        pairs(graph.right_pair_codes),
        graph.support,
        graph.carriers,
        int(residuals.max(initial=0)),
    )


def extract_rich_lines(
    graph: CompactGraph, side: str
) -> dict[int, tuple[RichLine, ...]]:
    if side == "L":
        support = graph.support
        carriers = graph.carriers
        neighbor_pairs = graph.right_pairs
    elif side == "R":
        support = graph.support.T.tocsr()
        carriers = graph.carriers.T.tocsr()
        neighbor_pairs = graph.left_pairs
    else:
        raise ValueError("unknown side")
    if not np.array_equal(support.indptr, carriers.indptr) or not np.array_equal(
        support.indices, carriers.indices
    ):
        raise AssertionError("support/carrier layouts differ")
    answer: dict[int, tuple[RichLine, ...]] = {}
    for anchor in range(support.shape[0]):
        start, stop = support.indptr[anchor : anchor + 2]
        if stop - start < 3:
            continue
        entries: list[NeighborEntry] = []
        for position in range(start, stop):
            neighbor = int(support.indices[position])
            edge = (anchor, neighbor) if side == "L" else (neighbor, anchor)
            entries.append(
                NeighborEntry(
                    tuple(map(int, neighbor_pairs[neighbor])),
                    int(carriers.data[position]),
                    edge,
                )
            )
        candidates: dict[LineKey, set[int]] = defaultdict(set)
        for first, second in combinations(range(len(entries)), 2):
            candidates[
                primitive_line_key(entries[first].point, entries[second].point)
            ].update((first, second))
        lines: list[RichLine] = []
        for key, members in sorted(candidates.items()):
            if len(members) < 3:
                continue
            selected = tuple(entries[index] for index in sorted(members))
            parameters = parameter_witnesses(key, selected)
            lines.append(
                RichLine(
                    side,
                    anchor,
                    key,
                    selected,
                    witnesses_affine(key, selected),
                    parameters[-1][0] - parameters[0][0],
                )
            )
        if lines:
            answer[anchor] = tuple(lines)
    return answer


def h_bin(h_left: int, h_right: int) -> str:
    height = max(abs(h_left), abs(h_right))
    for ceiling_value in (0, 1, 2, 4, 8, 16, 32, 64):
        if height <= ceiling_value:
            return str(ceiling_value)
    return ">64"


def trimmed_nonaffine(line: RichLine, edge: Edge) -> tuple[int, bool]:
    entries = tuple(entry for entry in line.entries if entry.edge != edge)
    return (
        len(entries),
        len(entries) >= 3 and not witnesses_affine(line.key, entries),
    )


def fan_better(candidate: NullFan, current: NullFan | None) -> bool:
    if current is None:
        return True
    return (
        candidate.population_product,
        candidate.edge,
        candidate.left.key,
        candidate.right.key,
    ) > (
        current.population_product,
        current.edge,
        current.left.key,
        current.right.key,
    )


def null_fan_summary(graph: CompactGraph) -> NullFanSummary:
    left_lines = extract_rich_lines(graph, "L")
    right_lines = extract_rich_lines(graph, "R")
    counts: Counter[str] = Counter()
    strata: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    maximum: NullFan | None = None
    maximum_nonaffine: NullFan | None = None
    maximum_trimmed = 0
    coordinates = graph.support.tocoo()
    for raw_left, raw_right in zip(coordinates.row, coordinates.col, strict=True):
        edge = int(raw_left), int(raw_right)
        for left in left_lines.get(edge[0], ()):
            p1, p2 = left.direction
            for right in right_lines.get(edge[1], ()):
                r1, r2 = right.direction
                if p1 * r1 - p2 * r2:
                    continue
                h_left = p2 * left.entries[0].point[0] - p1 * left.entries[0].point[1]
                h_right = p1 * right.entries[0].point[0] - p2 * right.entries[0].point[1]
                fan = NullFan(edge, left, right, h_left, h_right)
                counts["fans"] += 1
                if h_left == h_right == 0:
                    counts["zero_zero"] += 1
                both_nonaffine = not left.witness_affine and not right.witness_affine
                both_remote = (
                    left.remote_numerator >= graph.q
                    and right.remote_numerator >= graph.q
                )
                counts["both_nonaffine"] += both_nonaffine
                counts["both_remote"] += both_remote
                bucket = strata[h_bin(h_left, h_right)]
                bucket[0] += 1
                bucket[1] = max(bucket[1], fan.population_product)
                if both_nonaffine:
                    bucket[2] = max(bucket[2], fan.population_product)
                if fan_better(fan, maximum):
                    maximum = fan
                if both_nonaffine and fan_better(fan, maximum_nonaffine):
                    maximum_nonaffine = fan
                left_trim, left_nonaffine = trimmed_nonaffine(left, edge)
                right_trim, right_nonaffine = trimmed_nonaffine(right, edge)
                if left_nonaffine and right_nonaffine:
                    maximum_trimmed = max(maximum_trimmed, left_trim * right_trim)
    order = ("0", "1", "2", "4", "8", "16", "32", "64", ">64")
    return NullFanSummary(
        rich_left_anchors=len(left_lines),
        rich_right_anchors=len(right_lines),
        null_fans=counts["fans"],
        both_nonaffine_fans=counts["both_nonaffine"],
        both_remote_fans=counts["both_remote"],
        zero_zero_fans=counts["zero_zero"],
        maximum_population_product=maximum.population_product if maximum else 0,
        maximum_both_nonaffine_product=(
            maximum_nonaffine.population_product if maximum_nonaffine else 0
        ),
        maximum_trimmed_both_nonaffine_product=maximum_trimmed,
        maximum_fan=maximum,
        maximum_nonaffine_fan=maximum_nonaffine,
        h_strata=tuple((key, *strata[key]) for key in order if strata[key][0]),
        left_lines=left_lines,
        right_lines=right_lines,
    )


def line_geometry(points: Sequence[Point]) -> tuple[int, int]:
    count = len(points)
    if count == 0:
        return 0, 0
    if count <= 2:
        return count, 1
    candidates: dict[LineKey, int] = defaultdict(int)
    for first, second in combinations(range(count), 2):
        key = primitive_line_key(points[first], points[second])
        candidates[key] |= (1 << first) | (1 << second)
    masks = set(candidates.values())
    occupancy = max(mask.bit_count() for mask in masks)
    by_point: list[list[int]] = [[] for _ in range(count)]
    for mask in masks:
        for index in range(count):
            if mask & (1 << index):
                by_point[index].append(mask)

    @lru_cache(maxsize=None)
    def cover(remaining: int) -> int:
        if not remaining:
            return 0
        index = (remaining & -remaining).bit_length() - 1
        return 1 + min(
            cover(remaining & ~mask) for mask in by_point[index]
        )

    return occupancy, cover((1 << count) - 1)


def side_geometry(
    support: csr_matrix, neighbor_pairs: np.ndarray
) -> tuple[tuple[int, int, int], ...]:
    answer: list[tuple[int, int, int]] = []
    for anchor in range(support.shape[0]):
        points = tuple(
            tuple(map(int, neighbor_pairs[int(support.indices[position])]))
            for position in range(support.indptr[anchor], support.indptr[anchor + 1])
        )
        occupancy, cover = line_geometry(points)
        answer.append((len(points), occupancy, cover))
    return tuple(answer)


def dominant_fan_summary(graph: CompactGraph) -> DominantFanSummary:
    left = side_geometry(graph.support, graph.right_pairs)
    right = side_geometry(graph.support.T.tocsr(), graph.left_pairs)
    best_ratio = Fraction(-1)
    best: tuple[int, ...] | None = None
    coordinates = graph.support.tocoo()
    for raw_left, raw_right in zip(coordinates.row, coordinates.col, strict=True):
        left_index, right_index = int(raw_left), int(raw_right)
        left_degree, left_occupancy, left_cover = left[left_index]
        right_degree, right_occupancy, right_cover = right[right_index]
        numerator = left_degree * right_degree
        denominator = graph.degree + left_occupancy * right_occupancy
        ratio = Fraction(numerator, denominator)
        if ratio > best_ratio:
            best_ratio = ratio
            best = (
                left_index,
                right_index,
                left_degree,
                right_degree,
                left_occupancy,
                right_occupancy,
                left_cover,
                right_cover,
            )
    if best is None:
        return DominantFanSummary(Fraction(0), (0, 0), 0, 0, 0, 0, 0, 0, 0)
    return DominantFanSummary(
        best_ratio,
        (best[0], best[1]),
        *best[2:],
        max(
            max((value[2] for value in left), default=0),
            max((value[2] for value in right), default=0),
        ),
    )


def physical_pair(array: np.ndarray, index: int) -> Point:
    return tuple(map(int, array[index]))


def fan_payload(graph: CompactGraph, fan: NullFan) -> str:
    left_anchor = physical_pair(graph.left_pairs, fan.edge[0])
    right_anchor = physical_pair(graph.right_pairs, fan.edge[1])
    carrier = int(graph.carriers[fan.edge])
    cross_values = tuple(
        left.point[0] * right.point[0] - left.point[1] * right.point[1]
        for left in fan.left.entries
        for right in fan.right.entries
    )
    triples = (
        (carrier, left_anchor[0], right_anchor[0]),
        (carrier, left_anchor[1], right_anchor[1]),
        *(
            triple
            for entry in fan.left.entries
            for triple in (
                (entry.witness, left_anchor[0], entry.point[0]),
                (entry.witness, left_anchor[1], entry.point[1]),
            )
        ),
        *(
            triple
            for entry in fan.right.entries
            for triple in (
                (entry.witness, entry.point[0], right_anchor[0]),
                (entry.witness, entry.point[1], right_anchor[1]),
            )
        ),
    )
    residuals = tuple(8 * a * b * c - graph.q**3 for a, b, c in triples)
    return (
        f"edge=({left_anchor},{right_anchor}) carrier={carrier} "
        f"left_key={fan.left.key} left_tw={parameter_witnesses(fan.left.key, fan.left.entries)} "
        f"right_key={fan.right.key} right_tw={parameter_witnesses(fan.right.key, fan.right.entries)} "
        f"h=({fan.h_left},{fan.h_right}) product={fan.population_product} "
        f"remote_num=({fan.left.remote_numerator},{fan.right.remote_numerator}) "
        f"cross_range=({min(cross_values)},{max(cross_values)}) "
        f"max_abs_residual={max(map(abs, residuals))}"
    )


def print_fixture(graph: CompactGraph, *, dominant: bool) -> tuple[NullFanSummary, DominantFanSummary | None]:
    fan = null_fan_summary(graph)
    whole = dominant_fan_summary(graph) if dominant else None
    print(
        "FIXTURE",
        graph.label,
        graph.q,
        graph.degree,
        graph.support.nnz,
        fan.rich_left_anchors,
        fan.rich_right_anchors,
        fan.null_fans,
        fan.both_nonaffine_fans,
        fan.both_remote_fans,
        fan.zero_zero_fans,
        fan.maximum_population_product,
        f"{fan.maximum_population_product / graph.degree:.9g}",
        fan.maximum_both_nonaffine_product,
        fan.maximum_trimmed_both_nonaffine_product,
        fan.h_strata,
    )
    if whole is not None:
        left_anchor = physical_pair(graph.left_pairs, whole.maximum_edge[0])
        right_anchor = physical_pair(graph.right_pairs, whole.maximum_edge[1])
        print(
            "DOMINANT",
            graph.label,
            graph.q,
            f"{whole.maximum_ratio.numerator}/{whole.maximum_ratio.denominator}",
            f"{float(whole.maximum_ratio):.9g}",
            (left_anchor, right_anchor),
            (whole.left_degree, whole.right_degree),
            (whole.left_line_occupancy, whole.right_line_occupancy),
            (whole.left_line_cover, whole.right_line_cover),
            whole.maximum_line_cover,
        )
    return fan, whole


def parametric_affine_saturation() -> None:
    length = 8
    window = 512 * length * length
    approximate_q = int(window ** (33 / 16))
    midpoint = max(101 * length, (approximate_q + 1) // 2)
    grid = physical_affine_transition_grid(length, midpoint=midpoint)
    critical = exact_balanced_degree(grid.q)
    if grid.packet_length**2 * 512 != grid.D_window:
        raise AssertionError("unexpected affine saturation scale")
    print(
        "PARAMETRIC_AFFINE_NULL_FAN",
        f"L={length}",
        f"q={grid.q}",
        f"Dwindow={grid.D_window}",
        f"Dcritical={critical}",
        f"product={length**2}",
        f"product/Dwindow={Fraction(length**2, grid.D_window)}",
        "directions=((1,1),(1,1))",
        "h=(1,-1)",
        "witnesses=affine",
        f"max_residual={grid.maximum_product_residual}",
    )


def main() -> None:
    print("PASS remote parallel-null fan falsification audit")
    print(
        "FIXTURE columns: label q D edges richL richR null bothnon bothremote "
        "h00 maxprod maxprod/D maxnon maxtrim hstrata"
    )
    q809_graph: CompactGraph | None = None
    q809_fan: NullFanSummary | None = None
    for q in STRICT_INTEGER_FIXTURES:
        graph = exact_graph(q, full_integer_shell(q), label="integer-literal")
        summary, _whole = print_fixture(graph, dominant=False)
        if q == 809:
            q809_graph, q809_fan = graph, summary
        else:
            del graph, summary
            gc.collect()

    for q in STRICT_PRIME_POWER_FIXTURES:
        graph = exact_graph(q, full_prime_power_shell(q), label="prime-power-literal")
        print_fixture(graph, dominant=True)
        del graph
        gc.collect()

    fixed = actual_prime_residual_double_star()
    graph = exact_graph(
        fixed.q,
        fixed.primes,
        label="seven-prime-literal",
        degree=fixed.D,
    )
    print_fixture(graph, dominant=True)
    del graph
    gc.collect()

    actual_hostile: tuple[CompactGraph, NullFanSummary] | None = None
    for q, cutoff in LOG_PRIME_POWER_FIXTURES:
        graph = logarithmic_prime_power_graph(q, cutoff)
        summary, _whole = print_fixture(graph, dominant=True)
        if (q, int(cutoff)) == (11_801, 44):
            actual_hostile = graph, summary
        else:
            del graph, summary
            gc.collect()

    if q809_graph is None or q809_fan is None or q809_fan.maximum_nonaffine_fan is None:
        raise AssertionError("the literal q=809 remote null fan disappeared")
    exact_fan = q809_fan.maximum_nonaffine_fan
    if exact_fan.population_product != 12 or (
        abs(exact_fan.h_left), abs(exact_fan.h_right)
    ) != (1, 1):
        raise AssertionError("the literal q=809 certificate changed")
    print("LITERAL_REMOTE_CERTIFICATE", fan_payload(q809_graph, exact_fan))

    if actual_hostile is None or actual_hostile[1].maximum_nonaffine_fan is None:
        raise AssertionError("the actual-prime-power remote null fan disappeared")
    actual_graph, actual_summary = actual_hostile
    print(
        "ACTUAL_PRIME_POWER_REMOTE_CERTIFICATE",
        fan_payload(actual_graph, actual_summary.maximum_nonaffine_fan),
    )
    if any(
        summary[1] > 0
        for summary in actual_summary.h_strata
        if summary[0] == "0"
    ):
        raise AssertionError("an unexpected exact-zero actual rich fan appeared")
    parametric_affine_saturation()


if __name__ == "__main__":
    main()
