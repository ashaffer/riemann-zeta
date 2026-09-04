"""Adversarial numerical laboratory for the canonical self-orbit DRPLS.

The open estimate studied here is

    sum(K < h <= 2*K) |sum(t,j) e(h*q**3/(8*b_t*B_j))|**2
        << (q**2/K) q**o(1).

All orbit points and all phase residues are constructed with integer
arithmetic.  Floating point is used only to evaluate roots of unity after
``q**3 mod (8*b_t*B_j)`` has been taken, so there is no large-argument
range-reduction error.  This module is evidence and hostile testing, not a
proof of the displayed estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, exp, floor, gcd, isqrt
from random import Random
from typing import Iterable, Mapping, Sequence

import numpy as np

from qp_four_completion_bezout_token import BezoutTokenChart


Point = tuple[int, int]


def _ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def integer_shell_bounds(q: int, width: float = 0.2) -> tuple[int, int]:
    """Return the endpoints used by ``full_integer_shell`` without listing it."""

    if q <= 1 or width <= 0:
        raise ValueError("require q > 1 and positive shell width")
    return (
        ceil((q / 2.0) * exp(-width)),
        floor((q / 2.0) * exp(width)),
    )


def canonical_integer_orbit(
    q: int,
    D: int,
    anchor: Point,
    *,
    width: float = 0.2,
) -> dict[int, Point]:
    """Construct the complete integer-shell self-orbit for ``|t| <= D``.

    The implementation is the interval-shell specialization of
    ``physical_orbit_tokens``.  It avoids materializing a shell containing
    ``Theta(q)`` integers and checks the one-point-per-label assertion.
    """

    q, D = int(q), int(D)
    if D < 0:
        raise ValueError("D must be nonnegative")
    c, C = map(int, anchor)
    chart = BezoutTokenChart.canonical(c, C)
    lower, upper = integer_shell_bounds(q, width)
    answer: dict[int, Point] = {}
    for label in range(-D, D + 1):
        lower_n = max(
            _ceil_div(chart.u * label - upper, C),
            _ceil_div(chart.v * label - upper, c),
        )
        upper_n = min(
            (chart.u * label - lower) // C,
            (chart.v * label - lower) // c,
        )
        if lower_n > upper_n:
            continue
        if lower_n != upper_n:
            raise ValueError("one label has multiple points in the shell")
        point = chart.token_to_center((label, lower_n))
        if not (lower <= point[0] <= upper and lower <= point[1] <= upper):
            raise AssertionError("the interval orbit construction left the shell")
        answer[label] = point
    return answer


def adjacent_anchor(q: int, displacement: int = 0) -> Point:
    """Return ``(floor(q/2)+displacement, floor(q/2)+displacement+1)``."""

    first = q // 2 + int(displacement)
    return first, first + 1


def bezout_designed_anchor(
    q: int,
    direction: Point,
    remainder: int,
    *,
    first_target: int | None = None,
) -> Point:
    """Solve ``c*p-C*P=remainder`` with ``c`` nearest a target.

    This is a convenient generator for hostile continued-fraction packets.
    It does not assert that the returned anchor or its orbit lies in the
    project shell; callers should check those conditions.
    """

    p, P = map(int, direction)
    remainder = int(remainder)
    if p <= 0 or P <= 0 or gcd(p, P) != 1:
        raise ValueError("direction must be positive and primitive")
    target = q // 2 if first_target is None else int(first_target)
    if P == 1:
        residue = 0
    else:
        residue = (remainder * pow(p, -1, P)) % P
    shift = round((target - residue) / P)
    c = residue + shift * P
    C_numerator = c * p - remainder
    if C_numerator % P:
        raise AssertionError("the designed Bezout equation lost integrality")
    C = C_numerator // P
    if c * p - C * P != remainder:
        raise AssertionError("the designed anchor has the wrong remainder")
    if min(c, C) <= 1 or gcd(c, C) != 1:
        raise ValueError("the designed endpoint is not positive primitive")
    return c, C


def random_primitive_anchors(
    q: int,
    count: int,
    *,
    seed: int = 0,
    width: float = 0.2,
) -> tuple[Point, ...]:
    """Draw a deterministic sample of primitive ordered shell anchors."""

    lower, upper = integer_shell_bounds(q, width)
    rng = Random(seed)
    answer: list[Point] = []
    seen: set[Point] = set()
    while len(answer) < count:
        candidate = rng.randint(lower, upper), rng.randint(lower, upper)
        if candidate in seen or gcd(*candidate) != 1:
            continue
        seen.add(candidate)
        answer.append(candidate)
    return tuple(answer)


def _product_multiplicities(points: Sequence[Point]) -> tuple[np.ndarray, np.ndarray]:
    if not points:
        return np.array([], dtype=np.uint64), np.array([], dtype=np.int64)
    first = np.fromiter((point[0] for point in points), dtype=np.uint64)
    second = np.fromiter((point[1] for point in points), dtype=np.uint64)
    products = (first[:, None] * second[None, :]).reshape(-1)
    return np.unique(products, return_counts=True)


_TWO_PI_LONG = np.longdouble(
    "6.283185307179586476925286766559005768394338798750211641949889"
)


def _phase_residues(q: int, products: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return exact numerators and denominators of ``q^3/(8*n) mod 1``."""

    if not len(products):
        empty = np.array([], dtype=np.uint64)
        return empty, empty
    maximum_product = int(products[-1])
    if 8 * maximum_product > np.iinfo(np.uint64).max:
        raise OverflowError("8*b*B does not fit in uint64")
    denominators = products * np.uint64(8)
    q_cubed = int(q) ** 3
    if q_cubed <= np.iinfo(np.uint64).max:
        residues = np.uint64(q_cubed) % denominators
    else:
        residues = np.fromiter(
            (q_cubed % int(denominator) for denominator in denominators),
            dtype=np.uint64,
            count=len(denominators),
        )
    return residues, denominators


def _phase_roots(
    q: int,
    products: np.ndarray,
    *,
    method: str,
) -> np.ndarray:
    """Evaluate exact-residue roots ``e(q^3/(8*n))``."""

    if method not in {"complex128", "clongdouble"}:
        raise ValueError("method must be 'complex128' or 'clongdouble'")
    if not len(products):
        dtype = np.complex128 if method == "complex128" else np.clongdouble
        return np.array([], dtype=dtype)
    residues, denominators = _phase_residues(q, products)
    if method == "complex128":
        angles = (2.0 * np.pi) * (
            residues.astype(np.float64) / denominators.astype(np.float64)
        )
        return np.exp(1j * angles)
    fractions = residues.astype(np.longdouble) / denominators.astype(np.longdouble)
    return np.exp(np.clongdouble(1j) * _TWO_PI_LONG * fractions)


def _exact_phase_alias_square(
    q: int,
    products: np.ndarray,
    multiplicities: np.ndarray,
) -> int:
    """Return the squared weights of exact modulo-one reciprocal classes."""

    if not len(products):
        return 0
    residues, denominators = _phase_residues(q, products)
    common = np.gcd(residues, denominators)
    reduced_numerators = residues // common
    reduced_denominators = denominators // common
    order = np.lexsort((reduced_denominators, reduced_numerators))
    sorted_numerators = reduced_numerators[order]
    sorted_denominators = reduced_denominators[order]
    starts = np.r_[
        0,
        1
        + np.nonzero(
            (sorted_numerators[1:] != sorted_numerators[:-1])
            | (sorted_denominators[1:] != sorted_denominators[:-1])
        )[0],
    ]
    class_weights = np.add.reduceat(multiplicities[order], starts)
    return int(np.dot(class_weights, class_weights))


@dataclass(frozen=True)
class FrequencySquareProfile:
    q: int
    D: int
    anchor: Point
    point_count: int
    distinct_product_count: int
    equal_product_multiplicity_square: int
    exact_phase_alias_multiplicity_square: int
    method: str
    squares: tuple[float, ...]


def frequency_square_profile(
    q: int,
    D: int,
    anchor: Point,
    maximum_frequency: int,
    *,
    points: Mapping[int, Point] | None = None,
    method: str = "complex128",
    rephase_interval: int = 256,
) -> FrequencySquareProfile:
    """Evaluate ``|S(h)|^2`` for every ``0 <= h <= maximum_frequency``.

    Equal products are grouped before exponentiation.  Consequently the
    equal-product and exact modulo-one phase-alias terms in the expanded
    moment are both recorded.
    """

    maximum_frequency = int(maximum_frequency)
    if maximum_frequency < 0:
        raise ValueError("maximum_frequency must be nonnegative")
    orbit = canonical_integer_orbit(q, D, anchor) if points is None else dict(points)
    ordered_points = tuple(orbit[label] for label in sorted(orbit))
    products, multiplicities = _product_multiplicities(ordered_points)
    roots = _phase_roots(q, products, method=method)
    real_dtype = np.float64 if method == "complex128" else np.longdouble
    weights = multiplicities.astype(real_dtype)
    square_values = np.empty(maximum_frequency + 1, dtype=real_dtype)
    square_values[0] = len(ordered_points) ** 4
    current = roots.copy()
    for frequency in range(1, maximum_frequency + 1):
        value = np.dot(weights, current)
        square_values[frequency] = value.real * value.real + value.imag * value.imag
        current *= roots
        if rephase_interval and frequency % rephase_interval == 0:
            current = np.power(roots, frequency + 1)
    return FrequencySquareProfile(
        q=int(q),
        D=int(D),
        anchor=tuple(map(int, anchor)),
        point_count=len(ordered_points),
        distinct_product_count=len(products),
        equal_product_multiplicity_square=int(
            np.dot(multiplicities, multiplicities)
        ),
        exact_phase_alias_multiplicity_square=_exact_phase_alias_square(
            q, products, multiplicities
        ),
        method=method,
        squares=tuple(map(float, square_values)),
    )


@dataclass(frozen=True)
class DyadicMomentAudit:
    K: int
    mass: float
    normalized_mass: float
    strict_diagonal_mass: int
    equal_product_alias_mass: int
    exact_alias_mass: int
    normalized_strict_diagonal: float
    normalized_equal_product_alias: float
    normalized_exact_alias: float
    signed_nonalias_mass: float
    normalized_signed_nonalias: float
    peak_frequency: int
    peak_square: float


def dyadic_moment_from_profile(
    profile: FrequencySquareProfile,
    K: int,
) -> DyadicMomentAudit:
    """Extract the sharp block ``K < h <= 2K`` from a computed profile."""

    K = int(K)
    if K <= 0 or 2 * K >= len(profile.squares):
        raise ValueError("the frequency profile does not contain this dyadic block")
    block = profile.squares[K + 1 : 2 * K + 1]
    mass = float(sum(block))
    target = profile.q**2 / K
    diagonal = K * profile.point_count**2
    equal_product_aliases = K * profile.equal_product_multiplicity_square
    aliases = K * profile.exact_phase_alias_multiplicity_square
    peak_offset = max(range(len(block)), key=block.__getitem__)
    return DyadicMomentAudit(
        K=K,
        mass=mass,
        normalized_mass=mass / target,
        strict_diagonal_mass=diagonal,
        equal_product_alias_mass=equal_product_aliases,
        exact_alias_mass=aliases,
        normalized_strict_diagonal=diagonal / target,
        normalized_equal_product_alias=equal_product_aliases / target,
        normalized_exact_alias=aliases / target,
        signed_nonalias_mass=mass - aliases,
        normalized_signed_nonalias=(mass - aliases) / target,
        peak_frequency=K + 1 + peak_offset,
        peak_square=float(block[peak_offset]),
    )


@dataclass(frozen=True)
class DyadicRangeScan:
    profile: FrequencySquareProfile
    lower_K: int
    upper_K: int
    audits: tuple[DyadicMomentAudit, ...]
    worst: DyadicMomentAudit


def selberg_truncated_upper_K(q: int, D: int) -> int:
    """Largest ``K`` for which ``K<h<=2K`` stays below ``q/D``."""

    if q <= 0 or D <= 0:
        raise ValueError("q and D must be positive")
    return q // (2 * D)


def scan_active_dyadic_range(
    q: int,
    D: int,
    anchor: Point,
    *,
    points: Mapping[int, Point] | None = None,
    method: str = "complex128",
    lower_K: int | None = None,
    upper_K: int | None = None,
) -> DyadicRangeScan:
    """Scan every integral ``K`` in a requested DRPLS range.

    The default ``K<=q/D`` is the deliberately stronger diagnostic used in
    the closeout report; its last block reaches frequency ``2q/D``.  For the
    actually truncated Selberg range pass
    ``upper_K=selberg_truncated_upper_K(q,D)``.
    """

    lower = ceil(q / D**2) if lower_K is None else int(lower_K)
    upper = q // D if upper_K is None else int(upper_K)
    if lower <= 0 or upper < lower:
        raise ValueError("the active dyadic range is empty")
    profile = frequency_square_profile(
        q,
        D,
        anchor,
        2 * upper,
        points=points,
        method=method,
    )
    audits = tuple(
        dyadic_moment_from_profile(profile, K) for K in range(lower, upper + 1)
    )
    return DyadicRangeScan(
        profile=profile,
        lower_K=lower,
        upper_K=upper,
        audits=audits,
        worst=max(audits, key=lambda audit: audit.normalized_mass),
    )


class _DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first: int, second: int) -> None:
        first, second = self.find(first), self.find(second)
        if first == second:
            return
        if self.rank[first] < self.rank[second]:
            first, second = second, first
        self.parent[second] = first
        if self.rank[first] == self.rank[second]:
            self.rank[first] += 1


@dataclass(frozen=True)
class EmpiricalPacket:
    labels: tuple[int, ...]
    direction: Point | None
    remainder: int | None
    affine: bool
    small_remainder: bool
    small_step: bool

    @property
    def small_small(self) -> bool:
        return self.affine and self.small_remainder and self.small_step


def exact_radius_packets(
    q: int,
    D: int,
    K: int,
    anchor: Point,
    points: Mapping[int, Point],
) -> tuple[EmpiricalPacket, ...]:
    """Return exact radius-graph components and their small-small flags.

    Adjacency is tested without square roots:
    ``K*||v-w||_infinity**2 <= q``.  The small-small cutoff uses constant
    one in both inequalities from (5.12):

    ``|r|*q <= D**2*K`` and ``||U||_infinity**2*q <= D**2*K``.

    At currently feasible critical parameters the asymptotic collinearity
    hypothesis need not hold, so ``affine`` is explicitly audited rather
    than assumed.
    """

    labels = tuple(sorted(points, key=lambda label: points[label]))
    dsu = _DisjointSet(len(labels))
    for right in range(len(labels)):
        right_point = points[labels[right]]
        for left in range(right - 1, -1, -1):
            left_point = points[labels[left]]
            dx = right_point[0] - left_point[0]
            if K * dx * dx > q:
                break
            dy = right_point[1] - left_point[1]
            distance = max(abs(dx), abs(dy))
            if K * distance * distance <= q:
                dsu.union(left, right)
    grouped: dict[int, list[int]] = {}
    for index, label in enumerate(labels):
        grouped.setdefault(dsu.find(index), []).append(label)

    c, C = anchor
    cutoff = D * D * K
    answer: list[EmpiricalPacket] = []
    for component_labels in grouped.values():
        component_labels.sort(key=lambda label: points[label])
        if len(component_labels) == 1:
            answer.append(
                EmpiricalPacket(
                    labels=tuple(component_labels),
                    direction=None,
                    remainder=None,
                    affine=True,
                    small_remainder=False,
                    small_step=False,
                )
            )
            continue
        first, second = (points[label] for label in component_labels[:2])
        dx, dy = second[0] - first[0], second[1] - first[1]
        content = gcd(abs(dx), abs(dy))
        p, P = dx // content, dy // content
        if P < 0 or (P == 0 and p < 0):
            p, P = -p, -P
        affine = all(
            (point[0] - first[0]) * P == (point[1] - first[1]) * p
            for point in (points[label] for label in component_labels[2:])
        )
        remainder = c * p - C * P
        small_remainder = affine and abs(remainder) * q <= cutoff
        step = max(abs(p), abs(P))
        small_step = affine and step * step * q <= cutoff
        answer.append(
            EmpiricalPacket(
                labels=tuple(component_labels),
                direction=(p, P),
                remainder=remainder,
                affine=affine,
                small_remainder=small_remainder,
                small_step=small_step,
            )
        )
    answer.sort(key=lambda packet: points[packet.labels[0]])
    return tuple(answer)


def subdivide_packet_at_radius(
    q: int,
    K: int,
    packet: EmpiricalPacket,
    points: Mapping[int, Point],
) -> tuple[tuple[int, ...], ...]:
    """Greedily split one affine line into physical-diameter ``R_K`` blocks."""

    if not packet.affine:
        raise ValueError("only affine packets can be subdivided")
    labels = tuple(sorted(packet.labels, key=lambda label: points[label]))
    blocks: list[list[int]] = []
    current: list[int] = []
    origin: Point | None = None
    for label in labels:
        point = points[label]
        if origin is not None:
            distance = max(abs(point[0] - origin[0]), abs(point[1] - origin[1]))
            if K * distance * distance > q:
                blocks.append(current)
                current = []
                origin = None
        if origin is None:
            origin = point
        current.append(label)
    if current:
        blocks.append(current)
    return tuple(tuple(block) for block in blocks)


@dataclass(frozen=True)
class SmallSmallSectorAudit:
    q: int
    D: int
    K: int
    anchor: Point
    affine_integrality_hypothesis: bool
    radius_floor: int
    radius_component_count: int
    nonaffine_component_count: int
    small_small_component_count: int
    small_small_block_count: int
    small_small_point_count: int
    directions: tuple[Point, ...]
    restricted_mass: float
    normalized_restricted_mass: float
    packet_square_mass: float
    normalized_packet_square_mass: float
    translate_aggregation_ratio: float


def small_small_sector_audit(
    q: int,
    D: int,
    anchor: Point,
    K: int,
    *,
    points: Mapping[int, Point] | None = None,
    method: str = "complex128",
) -> SmallSmallSectorAudit:
    """Measure the restricted moment and packet square sum in (5.12).

    The restricted moment first sums every selected small-small block and
    then squares.  The packet square mass instead squares each ordered block
    pair separately, matching the numerical form of ``(PS)``.  Their ratio
    is the observed translate-aggregation factor from ``(TB)``.
    """

    orbit = canonical_integer_orbit(q, D, anchor) if points is None else dict(points)
    packets = exact_radius_packets(q, D, K, anchor, orbit)
    selected_packets = [packet for packet in packets if packet.small_small]
    blocks = tuple(
        block
        for packet in selected_packets
        for block in subdivide_packet_at_radius(q, K, packet, orbit)
    )
    selected_labels = tuple(label for block in blocks for label in block)
    target = q**2 / K
    if not selected_labels:
        restricted_mass = packet_square_mass = 0.0
    else:
        ordered_points = tuple(orbit[label] for label in selected_labels)
        first = np.fromiter((point[0] for point in ordered_points), dtype=np.uint64)
        second = np.fromiter((point[1] for point in ordered_points), dtype=np.uint64)
        products = (first[:, None] * second[None, :]).reshape(-1)
        roots = _phase_roots(q, products, method=method)
        root_matrix = roots.reshape(len(selected_labels), len(selected_labels))

        block_of: dict[int, int] = {}
        for block_index, block in enumerate(blocks):
            for label in block:
                block_of[label] = block_index
        ids = np.fromiter(
            (block_of[label] for label in selected_labels), dtype=np.int64
        )
        number_of_blocks = len(blocks)
        pair_ids = (ids[:, None] * number_of_blocks + ids[None, :]).reshape(-1)
        current = np.power(root_matrix, K + 1)
        restricted_mass = 0.0
        packet_square_mass = 0.0
        for offset in range(K):
            flat = current.reshape(-1)
            total = flat.sum()
            restricted_mass += float(total.real * total.real + total.imag * total.imag)
            real_sums = np.bincount(
                pair_ids, weights=np.asarray(flat.real, dtype=np.float64),
                minlength=number_of_blocks**2,
            )
            imaginary_sums = np.bincount(
                pair_ids, weights=np.asarray(flat.imag, dtype=np.float64),
                minlength=number_of_blocks**2,
            )
            packet_square_mass += float(
                np.dot(real_sums, real_sums) + np.dot(imaginary_sums, imaginary_sums)
            )
            current *= root_matrix
            if (offset + 1) % 256 == 0:
                current = np.power(root_matrix, K + offset + 2)

    radius_floor = isqrt(q // K)
    legal = 64 * D * D * q < min(anchor) ** 2 * K
    return SmallSmallSectorAudit(
        q=int(q),
        D=int(D),
        K=int(K),
        anchor=tuple(map(int, anchor)),
        affine_integrality_hypothesis=legal,
        radius_floor=radius_floor,
        radius_component_count=len(packets),
        nonaffine_component_count=sum(not packet.affine for packet in packets),
        small_small_component_count=len(selected_packets),
        small_small_block_count=len(blocks),
        small_small_point_count=len(selected_labels),
        directions=tuple(
            sorted({packet.direction for packet in selected_packets if packet.direction})
        ),
        restricted_mass=restricted_mass,
        normalized_restricted_mass=restricted_mass / target,
        packet_square_mass=packet_square_mass,
        normalized_packet_square_mass=packet_square_mass / target,
        translate_aggregation_ratio=(
            restricted_mass / packet_square_mass if packet_square_mass else 0.0
        ),
    )


def sampled_anchor_scans(
    q: int,
    D: int,
    count: int,
    *,
    seed: int = 0,
    method: str = "complex128",
) -> tuple[DyadicRangeScan, ...]:
    """Convenience wrapper for a deterministic primitive-anchor hostile scan."""

    return tuple(
        scan_active_dyadic_range(q, D, anchor, method=method)
        for anchor in random_primitive_anchors(q, count, seed=seed)
    )


@dataclass(frozen=True)
class BalancedTowerRectangleAudit:
    F: int
    R: int
    q: int
    D: int
    anchor: Point
    orbit_point_count: int
    lane_parameters: tuple[int, ...]
    rectangle_n_parameters: tuple[int, ...]
    rectangle_point_count: int
    all_orbit_points_have_tower_coordinates: bool
    rectangle_is_contained: bool


def balanced_tower_rectangle_audit(
    F: int,
    R: int,
    *,
    width: float = 0.2,
) -> BalancedTowerRectangleAudit:
    r"""Audit the exact balanced small-small tower supplied by geometry.

    Put

    ``q=2*F*R, D=F^2, gamma=(F(R+1)-1,FR-1)``.

    Every orbit point has unique coordinates

    ``z(m,n)=(mR-n,m(R+1)-n),  t=m-Fn``.

    Moreover, for each lane parameter recorded below, all ``0<=n<F`` lie
    in the shell and label window.  This gives an explicit
    ``(#lanes)-by-F`` rectangle inside the canonical orbit; ``#lanes`` is
    asymptotic to a positive constant times ``F`` for the fixed shell.
    """

    F, R = int(F), int(R)
    if F <= 1 or R <= F:
        raise ValueError("require R > F > 1")
    q, D = 2 * F * R, F * F
    anchor = F * (R + 1) - 1, F * R - 1
    orbit = canonical_integer_orbit(q, D, anchor, width=width)
    all_tower = True
    tower_coordinates: set[tuple[int, int]] = set()
    for label, (b, B) in orbit.items():
        m = B - b
        n = m * R - b
        all_tower &= (
            (b, B) == (m * R - n, m * (R + 1) - n)
            and label == m - F * n
        )
        tower_coordinates.add((m, n))

    lower, upper = integer_shell_bounds(q, width)
    lane_parameters: list[int] = []
    # The shell forces m=Theta(F).  This wider harmless range avoids using
    # a floating asymptotic to identify the exact integral endpoints.
    for m in range(1, 3 * F + 1):
        candidate_points = (
            (m * R - n, m * (R + 1) - n) for n in range(F)
        )
        if all(
            lower <= b <= upper
            and lower <= B <= upper
            and abs(m - F * n) <= D
            for n, (b, B) in enumerate(candidate_points)
        ):
            lane_parameters.append(m)
    n_parameters = tuple(range(F))
    rectangle = {
        (m, n) for m in lane_parameters for n in n_parameters
    }
    return BalancedTowerRectangleAudit(
        F=F,
        R=R,
        q=q,
        D=D,
        anchor=anchor,
        orbit_point_count=len(orbit),
        lane_parameters=tuple(lane_parameters),
        rectangle_n_parameters=n_parameters,
        rectangle_point_count=len(rectangle),
        all_orbit_points_have_tower_coordinates=all_tower,
        rectangle_is_contained=rectangle <= tower_coordinates,
    )
