"""Exact adversarial scans for the rooted Bezout-token NDS gate.

The routines in this module are finite diagnostics, not an asymptotic NDS
theorem.  They retain the literal hard window

    abs(8*a*b*c-q**3) <= q*D

and enumerate a rooted two-step path without completing the selected carrier
to an ambient box.  The two supplied fixtures illustrate the same phenomenon
on the full integer shell and on the full actual-prime-power shell: every
path of the relatively rich root is carried by a pair of parallel affine
lines in the lossless Bezout-token chart.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import ceil, exp, floor, gcd, isqrt
from random import Random
from typing import Iterable

from qp_actual_prime_nds import exact_balanced_degree
from qp_four_completion_bezout_token import BezoutTokenChart
from qp_four_cycle_hostile_lab import shell_values


Pair = tuple[int, int]
Line = tuple[int, int, int]


def full_integer_shell(q: int, width: float = 0.2) -> tuple[int, ...]:
    """Return the project's full integer shell around ``q/2``."""

    lower = ceil((q / 2.0) * exp(-width))
    upper = floor((q / 2.0) * exp(width))
    return tuple(range(lower, upper + 1))


def full_prime_power_shell(q: int, width: float = 0.2) -> tuple[int, ...]:
    """Return the full selected prime-power shell used by the project."""

    return tuple(map(int, shell_values(q / 2.0, width, "prime_powers")))


def normalized_line(first: Pair, second: Pair) -> Line:
    """Return the primitive signed equation of the line through two points."""

    if first == second:
        raise ValueError("two distinct points are needed to determine a line")
    x1, y1 = first
    x2, y2 = second
    A, B = y2 - y1, x1 - x2
    C = -(A * x1 + B * y1)
    content = gcd(gcd(abs(A), abs(B)), abs(C))
    A, B, C = A // content, B // content, C // content
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def best_weighted_line(points: Counter[Pair]) -> tuple[int, Line | None]:
    """Return the largest weighted affine-line concentration."""

    distinct = tuple(points)
    total = sum(points.values())
    if len(distinct) < 2:
        return total, None
    lines = {
        normalized_line(distinct[i], distinct[j])
        for i in range(len(distinct))
        for j in range(i)
    }
    best = max(
        lines,
        key=lambda line: sum(
            weight
            for point, weight in points.items()
            if line[0] * point[0] + line[1] * point[1] + line[2] == 0
        ),
    )
    mass = sum(
        weight
        for point, weight in points.items()
        if best[0] * point[0] + best[1] * point[1] + best[2] == 0
    )
    return mass, best


@dataclass(frozen=True)
class OrbitReflectionLedger:
    """The exact centre-orbit reflection behind every endpoint token."""

    h: int
    center_token_at_minus_h: Pair
    center_at_minus_h: Pair
    endpoint_at_h: Pair
    endpoint_token_at_h: Pair


def orbit_reflection_ledger(
    chart: BezoutTokenChart, h: int, n_at_minus_h: int
) -> OrbitReflectionLedger:
    """Verify ``eta_h=(B_-h,b_-h)`` and ``R_h=(h,-n_-h)``.

    If the centre orbit has token ``P_-h=(-h,n_-h)``, swapping its two
    physical coordinates gives the endpoint orbit.  In token coordinates the
    operation is simply negation.  This is an identity on ``Z^2`` and uses no
    hard-window approximation or carrier completion.
    """

    source_token = (-h, n_at_minus_h)
    b_at_minus_h, B_at_minus_h = chart.token_to_center(source_token)
    endpoint = (B_at_minus_h, b_at_minus_h)
    endpoint_token = chart.endpoint_to_token(endpoint)
    expected = (h, -n_at_minus_h)
    if endpoint_token != expected:
        raise AssertionError("the centre/endpoint orbit reflection failed")
    return OrbitReflectionLedger(
        h=h,
        center_token_at_minus_h=source_token,
        center_at_minus_h=(b_at_minus_h, B_at_minus_h),
        endpoint_at_h=endpoint,
        endpoint_token_at_h=endpoint_token,
    )


@dataclass(frozen=True)
class OneOrbitMiddleLedger:
    """One middle pair written as cross-products of the centre orbit."""

    center_token: Pair
    reflected_source_token: Pair
    endpoint_token: Pair
    center: Pair
    reflected_source_center: Pair
    endpoint: Pair
    left_product: int
    right_product: int


def one_orbit_middle_ledger(
    chart: BezoutTokenChart, center_token: Pair, reflected_source_token: Pair
) -> OneOrbitMiddleLedger:
    """Express a middle edge using two points of one centre-token orbit.

    For ``P_delta`` with physical centre ``(b_delta,B_delta)`` and
    ``P_-h`` with centre ``(b_-h,B_-h)``, the reflected endpoint is

    ``eta_h=(B_-h,b_-h)``, ``R_h=-P_-h``.

    Hence the two middle products are exactly

    ``b_delta*B_-h`` and ``B_delta*b_-h``.
    """

    center = chart.token_to_center(center_token)
    source_center = chart.token_to_center(reflected_source_token)
    endpoint = source_center[1], source_center[0]
    endpoint_token = chart.endpoint_to_token(endpoint)
    expected_endpoint_token = (
        -reflected_source_token[0],
        -reflected_source_token[1],
    )
    if endpoint_token != expected_endpoint_token:
        raise AssertionError("the reflected endpoint token is not the negative source")
    transition = chart.transition_ledger(center, endpoint)
    left_product = center[0] * source_center[1]
    right_product = center[1] * source_center[0]
    if transition.physical_difference != left_product - right_product:
        raise AssertionError("the one-orbit cross-product difference failed")
    if transition.physical_sum != left_product + right_product:
        raise AssertionError("the one-orbit cross-product sum failed")
    return OneOrbitMiddleLedger(
        center_token=center_token,
        reflected_source_token=reflected_source_token,
        endpoint_token=endpoint_token,
        center=center,
        reflected_source_center=source_center,
        endpoint=endpoint,
        left_product=left_product,
        right_product=right_product,
    )


@dataclass(frozen=True)
class DigitalStripAudit:
    """Direction count for the universal physical centre-token strip."""

    q: int
    D: int
    gamma: Pair
    points: tuple[Pair, ...]
    distinct_difference_directions: int
    maximum_affine_line_size: int
    affine_line_cover_lower_bound: int
    maximizing_line: Line | None


def physical_center_digital_strip(
    q: int, D: int, gamma: Pair, *, delta_radius: int | None = None
) -> DigitalStripAudit:
    """Audit the width-``<1`` token graph before either hard diamond.

    Both inverse physical coordinates ``(b,B)`` are required to lie in the
    full integer shell.  The first coordinate identity

    ``n-(u/C)delta=-b/C``

    gives at most one integer ``n`` for each ``delta`` because the shell
    diameter is smaller than ``C`` in the supplied project fixtures.  The
    routine counts how many *exact affine* directions this digital graph can
    nevertheless support.
    """

    lower, upper = full_integer_shell(q)[0], full_integer_shell(q)[-1]
    chart = BezoutTokenChart.canonical(*gamma)
    radius = D if delta_radius is None else int(delta_radius)
    points: list[Pair] = []

    def ceil_div(numerator: int, denominator: int) -> int:
        return -((-numerator) // denominator)

    for delta in range(-radius, radius + 1):
        n_min = ceil_div(chart.u * delta - upper, chart.C)
        n_max = (chart.u * delta - lower) // chart.C
        accepted = []
        for n in range(n_min, n_max + 1):
            b, B = chart.token_to_center((delta, n))
            if lower <= b <= upper and lower <= B <= upper:
                if chart.C * n - chart.u * delta != -b:
                    raise AssertionError("the digital-strip identity failed")
                accepted.append((delta, n))
        if len(accepted) > 1:
            raise AssertionError("the physical token strip is not one point wide")
        points.extend(accepted)

    directions: set[Pair] = set()
    line_pairs: Counter[Line] = Counter()
    for index, point in enumerate(points):
        for earlier in points[:index]:
            dx, dy = point[0] - earlier[0], point[1] - earlier[1]
            content = gcd(abs(dx), abs(dy))
            dx, dy = dx // content, dy // content
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            directions.add((dx, dy))
            line_pairs[normalized_line(point, earlier)] += 1

    if line_pairs:
        maximizing_line, pair_count = line_pairs.most_common(1)[0]
        maximum_line_size = (1 + isqrt(1 + 8 * pair_count)) // 2
        if maximum_line_size * (maximum_line_size - 1) // 2 != pair_count:
            raise AssertionError("a line pair count was not triangular")
    else:
        maximizing_line = None
        maximum_line_size = len(points)
    cover_lower = (
        (len(points) + maximum_line_size - 1) // maximum_line_size
        if maximum_line_size
        else 0
    )
    return DigitalStripAudit(
        q=q,
        D=D,
        gamma=gamma,
        points=tuple(points),
        distinct_difference_directions=len(directions),
        maximum_affine_line_size=maximum_line_size,
        affine_line_cover_lower_bound=cover_lower,
        maximizing_line=maximizing_line,
    )


@dataclass(frozen=True)
class TokenPath:
    base_row: int
    center: Pair
    center_token: Pair
    next_row: int
    endpoint: Pair
    endpoint_token: Pair


@dataclass(frozen=True)
class RootPathAudit:
    q: int
    D: int
    node_count: int
    gamma: Pair
    root_degree: int
    maximum_neighbor_degree: int
    neighbourhood_degree_sum: int
    nonreturn_paths: int
    center_line_mass: int
    center_line: Line | None
    endpoint_line_mass: int
    endpoint_line: Line | None
    paths: tuple[TokenPath, ...]

    @property
    def parallel_carriers(self) -> bool:
        """Whether the two maximizing token lines have the same direction."""

        if self.center_line is None or self.endpoint_line is None:
            return False
        return self.center_line[:2] == self.endpoint_line[:2]


class RootedTokenScanner:
    """Losslessly enumerate rooted paths on one finite selected carrier."""

    def __init__(self, q: int, D: int, nodes: Iterable[int]):
        if q <= 0 or D <= 0:
            raise ValueError("q and D must be positive")
        self.q = int(q)
        self.D = int(D)
        self.nodes = tuple(sorted(set(map(int, nodes))))
        self.allowed = frozenset(self.nodes)
        self.target = self.q**3
        self._completion_cache: dict[int, dict[int, int]] = {}

    def completion(self, first: int, second: int) -> int | None:
        """Return the unique selected hard-window completion, if it exists."""

        denominator = 8 * first * second
        quotient = self.target // denominator
        accepted = tuple(
            candidate
            for candidate in (quotient, quotient + 1)
            if candidate in self.allowed
            and abs(denominator * candidate - self.target) <= self.q * self.D
        )
        if len(accepted) > 1:
            raise ValueError("the supplied carrier is outside the unique-completion range")
        return accepted[0] if accepted else None

    def completion_map(self, second: int) -> dict[int, int]:
        """Map every selected first coordinate having a completion."""

        if second not in self._completion_cache:
            answer: dict[int, int] = {}
            for first in self.nodes:
                completion = self.completion(first, second)
                if completion is not None:
                    answer[first] = completion
            self._completion_cache[second] = answer
        return self._completion_cache[second]

    def root_audit(self, gamma: Pair) -> RootPathAudit:
        """Enumerate the exact residual paths based at primitive ``gamma``."""

        c, C = gamma
        chart = BezoutTokenChart.canonical(c, C)
        first = self.completion_map(c)
        second = self.completion_map(C)
        paths: list[TokenPath] = []
        neighbor_degrees: list[int] = []

        for base_row in sorted(first.keys() & second.keys()):
            b, B = first[base_row], second[base_row]
            if b * c == B * C:
                continue
            left = self.completion_map(b)
            right = self.completion_map(B)
            center_token = chart.center_to_token((b, B))
            degree = 0
            for next_row in sorted(left.keys() & right.keys()):
                d, E = left[next_row], right[next_row]
                if b * d == B * E:
                    continue
                paths.append(
                    TokenPath(
                        base_row=base_row,
                        center=(b, B),
                        center_token=center_token,
                        next_row=next_row,
                        endpoint=(d, E),
                        endpoint_token=chart.endpoint_to_token((d, E)),
                    )
                )
                degree += 1
            neighbor_degrees.append(degree)

        center_weights: Counter[Pair] = Counter()
        endpoint_weights: Counter[Pair] = Counter()
        for path in paths:
            center_weights[path.center_token] += 1
            endpoint_weights[path.endpoint_token] += 1
        center_mass, center_line = best_weighted_line(center_weights)
        endpoint_mass, endpoint_line = best_weighted_line(endpoint_weights)
        return RootPathAudit(
            q=self.q,
            D=self.D,
            node_count=len(self.nodes),
            gamma=gamma,
            root_degree=len(neighbor_degrees),
            maximum_neighbor_degree=max(neighbor_degrees, default=0),
            neighbourhood_degree_sum=len(paths),
            nonreturn_paths=sum(path.endpoint != gamma for path in paths),
            center_line_mass=center_mass,
            center_line=center_line,
            endpoint_line_mass=endpoint_mass,
            endpoint_line=endpoint_line,
            paths=tuple(paths),
        )


def integer_parallel_fixture() -> RootPathAudit:
    """The full-integer ``q=200000`` root with ``W=271``."""

    q = 200_000
    scanner = RootedTokenScanner(
        q, exact_balanced_degree(q), full_integer_shell(q)
    )
    return scanner.root_audit((100_000, 100_001))


def broad_scattered_fixture() -> RootPathAudit:
    """A deterministic broad-shell root from the scattered sample."""

    q = 200_000
    scanner = RootedTokenScanner(
        q, exact_balanced_degree(q), full_integer_shell(q)
    )
    return scanner.root_audit((108_551, 111_297))


def actual_prime_parallel_fixture() -> RootPathAudit:
    """A full prime-power-shell fixture beyond the earlier ``q=5868182`` one."""

    q = 10_604_226
    scanner = RootedTokenScanner(
        q, exact_balanced_degree(q), full_prime_power_shell(q)
    )
    return scanner.root_audit((5_302_109, 5_302_103))


def deterministic_broad_candidates(q: int = 200_000) -> tuple[Pair, ...]:
    """Reproduce the bounded 11-row broad-direction candidate family.

    For each of eleven evenly spaced rows, take all fixed index gaps in the
    accepted color list and 300 pseudorandom pairs (seed one).  Only primitive
    ordered endpoints are retained.  At ``q=200000`` this returns 3927 roots.
    Calling ``root_audit`` on them is intentionally left explicit because it
    is a finite search, not part of a proof or an import-time computation.
    """

    D = exact_balanced_degree(q)
    nodes = full_integer_shell(q)
    scanner = RootedTokenScanner(q, D, nodes)
    lower, upper = nodes[0], nodes[-1]
    rows = tuple((lower * (10 - i) + upper * i) // 10 for i in range(11))
    gaps = (1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
    rng = Random(1)
    candidates: set[Pair] = set()
    for row in rows:
        colors = tuple(
            color for color in nodes if scanner.completion(row, color) is not None
        )
        for gap in gaps:
            for index in range(max(0, len(colors) - gap)):
                pair = colors[index], colors[index + gap]
                if gcd(*pair) == 1:
                    candidates.add(pair)
        for _ in range(300):
            if len(colors) < 2:
                break
            first, second = rng.sample(range(len(colors)), 2)
            pair = colors[first], colors[second]
            if gcd(*pair) == 1:
                candidates.add(pair)
    return tuple(sorted(candidates))
