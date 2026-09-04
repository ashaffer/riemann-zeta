"""Adversarial finite checks for the symmetric Bezout self-orbit kernel.

Nothing in this module is an asymptotic incidence theorem.  The hard-kernel
routine keeps the actual carrier mask and the literal window

    abs(8*a*b*c-q**3) <= q*D.

It is used to distinguish three phenomena which can look similar in a
relaxed token picture:

* a large, but affine-coherent, full-integer self-orbit kernel;
* sparse broad actual/integer kernels;
* genuinely scattered prime cycles which occur only after a substantial
  enlargement of the critical hard window in the finite fixture below.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from math import gcd, isqrt, log
from typing import Iterable, Mapping

from qp_actual_prime_nds import exact_balanced_degree, in_hard_window
from qp_four_completion_bezout_token import BezoutTokenChart
from qp_four_cycle_hostile_lab import FULL_APERTURE
from qp_scattered_token_search import (
    Pair,
    RootPathAudit,
    RootedTokenScanner,
    best_weighted_line,
    full_integer_shell,
)


def _ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def physical_orbit_tokens(
    chart: BezoutTokenChart,
    labels: Iterable[int],
    nodes: Iterable[int],
) -> dict[int, Pair]:
    """Return every requested centre-orbit token surviving ``nodes``.

    The project shell is narrower than either coefficient of the supplied
    charts, so a determinant label has at most one physical point.  The
    implementation checks this rather than relying on it silently.
    """

    selected = tuple(sorted(set(map(int, nodes))))
    if not selected:
        return {}
    allowed = frozenset(selected)
    lower, upper = selected[0], selected[-1]
    answer: dict[int, Pair] = {}
    for label in labels:
        lower_n = max(
            _ceil_div(chart.u * label - upper, chart.C),
            _ceil_div(chart.v * label - upper, chart.c),
        )
        upper_n = min(
            (chart.u * label - lower) // chart.C,
            (chart.v * label - lower) // chart.c,
        )
        accepted: list[Pair] = []
        for quotient in range(lower_n, upper_n + 1):
            point = chart.token_to_center((label, quotient))
            if point[0] in allowed and point[1] in allowed:
                accepted.append(point)
        if len(accepted) > 1:
            raise ValueError("one determinant label has multiple shell points")
        if accepted:
            answer[int(label)] = accepted[0]
    return answer


@dataclass(frozen=True)
class ShortSelfOrbitKernelAudit:
    """Exact support statistics for ``X(t,j)`` on ``|t|,|j|<=D``."""

    q: int
    D: int
    gamma: Pair
    node_count: int
    physical_token_count: int
    incident_vertex_count: int
    directed_edge_count: int
    maximum_degree: int
    anchor_degree: int
    anchor_neighbour_degree_sum: int
    maximum_incident_affine_line_size: int
    adjacency: Mapping[int, frozenset[int]]
    points: Mapping[int, Pair]

    @property
    def edge_to_degree_ratio(self) -> float:
        return self.directed_edge_count / self.D


def short_self_orbit_kernel(
    q: int,
    D: int,
    nodes: Iterable[int],
    gamma: Pair,
    *,
    label_radius: int | None = None,
) -> ShortSelfOrbitKernelAudit:
    """Enumerate the entire short symmetric hard kernel, without completion.

    If ``P_t=(b_t,B_t)`` and ``P_j=(b_j,B_j)``, the endpoint paired with
    ``P_j`` is its reflection ``(B_j,b_j)``.  Therefore ``X(t,j)=1`` exactly
    when one selected row ``x`` obeys both middle windows for

    ``(b_t,x,B_j)`` and ``(B_t,x,b_j)``.

    Tangent transitions, for which the two products agree, are excluded just
    as they are in ``RootedTokenScanner.root_audit``.  Symmetry lets the
    routine test each unordered label pair only once.
    """

    selected = tuple(sorted(set(map(int, nodes))))
    radius = D if label_radius is None else int(label_radius)
    chart = BezoutTokenChart.canonical(*gamma)
    points = physical_orbit_tokens(chart, range(-radius, radius + 1), selected)
    scanner = RootedTokenScanner(q, D, selected)
    labels = tuple(sorted(points))
    adjacency: dict[int, set[int]] = {label: set() for label in labels}

    for first_index, first_label in enumerate(labels):
        b_first, B_first = points[first_label]
        for second_label in labels[first_index + 1 :]:
            b_second, B_second = points[second_label]
            if b_first * B_second == B_first * b_second:
                continue
            row = scanner.completion(b_first, B_second)
            if row is None or row != scanner.completion(B_first, b_second):
                continue
            adjacency[first_label].add(second_label)
            adjacency[second_label].add(first_label)

    incident = {label for label, neighbours in adjacency.items() if neighbours}
    if len(incident) >= 2:
        line_mass, _ = best_weighted_line(
            Counter(points[label] for label in incident)
        )
    else:
        line_mass = len(incident)
    frozen = {label: frozenset(neighbours) for label, neighbours in adjacency.items()}
    anchor_neighbours = frozen.get(0, frozenset())
    return ShortSelfOrbitKernelAudit(
        q=int(q),
        D=int(D),
        gamma=gamma,
        node_count=len(selected),
        physical_token_count=len(points),
        incident_vertex_count=len(incident),
        directed_edge_count=sum(map(len, frozen.values())),
        maximum_degree=max(map(len, frozen.values()), default=0),
        anchor_degree=len(anchor_neighbours),
        anchor_neighbour_degree_sum=sum(len(frozen[label]) for label in anchor_neighbours),
        maximum_incident_affine_line_size=line_mass,
        adjacency=frozen,
        points=points,
    )


def rooted_adjacency(audit: RootPathAudit) -> dict[int, frozenset[int]]:
    """Recover the anchored rows of ``X(t,j)`` from a rooted path audit."""

    answer: dict[int, set[int]] = {}
    for path in audit.paths:
        # The physical endpoint is the reflection of the source centre, so
        # its token is the negative of the source token.
        first = path.center_token[0]
        second = -path.endpoint_token[0]
        answer.setdefault(first, set()).add(second)
    return {row: frozenset(columns) for row, columns in answer.items()}


def rooted_vertex_points(audit: RootPathAudit) -> dict[int, Pair]:
    """Return physical source-orbit points for every displayed root row/column."""

    answer: dict[int, Pair] = {}
    for path in audit.paths:
        answer[path.center_token[0]] = path.center
        answer[-path.endpoint_token[0]] = tuple(reversed(path.endpoint))
    return answer


def interval_run_count(subset: Iterable[int], order: Iterable[int]) -> int:
    """Count maximal consecutive runs of ``subset`` in a prescribed order."""

    chosen = frozenset(subset)
    runs = 0
    previous = False
    for item in order:
        current = item in chosen
        runs += int(current and not previous)
        previous = current
    return runs


@dataclass(frozen=True)
class MultilevelSelfOrbitPacketAudit:
    """One fixed-anchor slice of the multilevel tangent construction."""

    m: int
    length: int
    step: int
    q: int
    D: int
    anchor: Pair
    center_labels: tuple[int, ...]
    source_labels: tuple[int, ...]
    undirected_biclique_edges: int
    directed_edge_lower_bound: int
    maximum_product_residual: int


def multilevel_self_orbit_packet(
    m: int = 20_000_000,
    length: int = 10,
    step: int = 11,
) -> MultilevelSelfOrbitPacketAudit:
    """Embed a full ``K_(L+1,L+1)`` in one symmetric self-orbit chart.

    This is the fixed-``h`` slice of ``qp_multilevel_translation_grid``.
    With anchor ``gamma=(m,m-h)``, its centre labels are ``h(h+t)`` and its
    reflected-source labels are ``0,-h*l``.  Thus all labels remain in the
    short window ``[-D,D]``, where ``D=2048L^2``.  The packet supplies
    ``2(L+1)^2`` directed edges, only a constant multiple of ``D`` from
    below; it is not a counterexample to an ``O(D polylog)`` total-edge
    theorem.
    """

    L, h = int(length), int(step)
    if L < 2 or h not in range(L, 2 * L + 1):
        raise ValueError("require L>=2 and L<=h<=2L")
    anchor = (int(m), int(m) - h)
    if gcd(*anchor) != 1:
        raise ValueError("the fixed-anchor slice must be primitive")
    q = 2 * int(m)
    D = 2048 * L * L
    chart = BezoutTokenChart.canonical(*anchor)
    translations = tuple(range(20 * L, 21 * L + 1))
    levels: tuple[int | None, ...] = (None,) + tuple(
        ell for ell in range(L, 2 * L + 1) if ell != h
    )
    center_labels: list[int] = []
    source_labels: set[int] = set()
    maximum_residual = 0

    for translation in translations:
        center = (m + translation, m + h + translation)
        center_label = chart.center_to_token(center)[0]
        if center_label != h * (h + translation) or abs(center_label) > D:
            raise AssertionError("the tangent centre escaped the short chart")
        center_labels.append(center_label)
        for level in levels:
            if level is None:
                endpoint = (m, m - h)
                row = m - translation
                expected_source_label = 0
            else:
                endpoint = (m - level, m - h - level)
                row = m + level - translation
                expected_source_label = -h * level
            source = tuple(reversed(endpoint))
            source_label = chart.center_to_token(source)[0]
            if source_label != expected_source_label or abs(source_label) > D:
                raise AssertionError("the tangent source escaped the short chart")
            source_labels.add(source_label)
            residuals = (
                abs(8 * row * center[0] * endpoint[0] - q**3),
                abs(8 * row * center[1] * endpoint[1] - q**3),
            )
            if not (
                in_hard_window(q, D, (center[0], row, endpoint[0]))
                and in_hard_window(q, D, (center[1], row, endpoint[1]))
            ):
                raise AssertionError("a multilevel packet edge escaped the hard window")
            if center[0] * endpoint[0] == center[1] * endpoint[1]:
                raise AssertionError("a purported packet edge is tangent-degenerate")
            maximum_residual = max(maximum_residual, *residuals)

    edge_count = len(center_labels) * len(source_labels)
    return MultilevelSelfOrbitPacketAudit(
        m=int(m),
        length=L,
        step=h,
        q=q,
        D=D,
        anchor=anchor,
        center_labels=tuple(center_labels),
        source_labels=tuple(sorted(source_labels)),
        undirected_biclique_edges=edge_count,
        directed_edge_lower_bound=2 * edge_count,
        maximum_product_residual=maximum_residual,
    )


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


@dataclass(frozen=True)
class ScatteredPrimeCycleAudit:
    """Exact verification data for an alternating prime self-orbit cycle."""

    q: int
    points: tuple[Pair, ...]
    carriers: tuple[int, ...]
    edge_triples: tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...]
    maximum_product_residual: int
    minimum_literal_D: int
    critical_D: int
    maximum_smooth_frequency: float
    distinct_edge_directions: int
    all_displayed_values_distinct: bool
    all_displayed_values_prime: bool
    no_three_points_collinear: bool


def audit_scattered_prime_cycle(
    q: int,
    points: Iterable[Pair],
    carriers: Iterable[int],
) -> ScatteredPrimeCycleAudit:
    """Verify a fixed alternating cycle by integer arithmetic where possible.

    Even-indexed points are left pair vertices.  Odd-indexed points are
    reflected right pair vertices.  Thus an edge from ``(a,a')`` to reflected
    ``(c',c)`` with carrier ``b`` consists of triples ``(a,b,c)`` and
    ``(a',b,c')``.

    The literal hard-window threshold, primality, distinctness, directions,
    and collinearity are exact.  ``maximum_smooth_frequency`` is only the
    double-precision replay of the older logarithmic-cutoff diagnostic.
    """

    vertices = tuple((int(x), int(y)) for x, y in points)
    rows = tuple(map(int, carriers))
    if len(vertices) < 4 or len(vertices) % 2 or len(vertices) != len(rows):
        raise ValueError("an even cycle needs one carrier per vertex")
    triples: list[tuple[tuple[int, int, int], tuple[int, int, int]]] = []
    residuals: list[int] = []
    frequencies: list[float] = []
    bandwidth = (q / 2.0) ** FULL_APERTURE

    for index, row in enumerate(rows):
        first = vertices[index]
        second = vertices[(index + 1) % len(vertices)]
        left, reflected = (first, second) if index % 2 == 0 else (second, first)
        pair = (
            (left[0], row, reflected[1]),
            (left[1], row, reflected[0]),
        )
        if pair[0][0] * pair[0][2] == pair[1][0] * pair[1][2]:
            raise AssertionError("the cycle contains a tangent-degenerate edge")
        triples.append(pair)
        for triple in pair:
            residual = 8 * triple[0] * triple[1] * triple[2] - q**3
            residuals.append(residual)
            frequencies.append(
                abs(bandwidth * log(1.0 + residual / q**3))
            )

    displayed = tuple(value for point in vertices for value in point) + rows
    no_collinear = all(
        (second[0] - first[0]) * (third[1] - first[1])
        != (second[1] - first[1]) * (third[0] - first[0])
        for first, second, third in combinations(vertices, 3)
    )
    directions: set[Pair] = set()
    for first, second in zip(vertices, vertices[1:] + vertices[:1]):
        dx, dy = second[0] - first[0], second[1] - first[1]
        content = gcd(abs(dx), abs(dy))
        dx, dy = dx // content, dy // content
        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy
        directions.add((dx, dy))
    maximum_residual = max(map(abs, residuals))
    return ScatteredPrimeCycleAudit(
        q=int(q),
        points=vertices,
        carriers=rows,
        edge_triples=tuple(triples),
        maximum_product_residual=maximum_residual,
        minimum_literal_D=(maximum_residual + q - 1) // q,
        critical_D=exact_balanced_degree(q),
        maximum_smooth_frequency=max(frequencies),
        distinct_edge_directions=len(directions),
        all_displayed_values_distinct=len(set(displayed)) == len(displayed),
        all_displayed_values_prime=all(map(_is_prime, displayed)),
        no_three_points_collinear=no_collinear,
    )


def first_scattered_prime_c6() -> ScatteredPrimeCycleAudit:
    """The first C6 in the audited ``q=25013`` cutoff filtration.

    The exhaustive double-precision filtration had no qualifying C6 below
    smooth cutoff ``21.518440849497075``.  The returned fixture itself has an
    exact literal threshold ``D=8344``; this is far wider than critical
    ``D=floor(q**(16/33))=135``.
    """

    return audit_scattered_prime_cycle(
        25_013,
        (
            (10_501, 10_631),
            (12_281, 12_433),
            (11_953, 12_101),
            (12_119, 12_269),
            (12_601, 12_757),
            (14_561, 14_741),
        ),
        (14_983, 13_163, 13_339, 12_653, 10_531, 12_637),
    )


def scattered_prime_c8() -> ScatteredPrimeCycleAudit:
    """A genuine all-distinct C8 found in the ``q=25013,U<=40`` scan."""

    return audit_scattered_prime_cycle(
        25_013,
        (
            (10_243, 10_337),
            (13_099, 13_219),
            (12_647, 12_763),
            (11_789, 11_897),
            (12_889, 13_007),
            (13_751, 13_877),
            (13_757, 13_883),
            (13_121, 13_241),
        ),
        (14_447, 11_701, 13_001, 12_757, 10_937, 10_247, 10_739, 14_423),
    )


def central_integer_kernel_fixture() -> ShortSelfOrbitKernelAudit:
    """Replay the richest complete short-kernel scan at ``q=200000``."""

    q = 200_000
    return short_self_orbit_kernel(
        q,
        exact_balanced_degree(q),
        full_integer_shell(q),
        (100_000, 100_001),
    )
