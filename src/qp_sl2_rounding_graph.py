"""Exact SL2 shell-rounding coordinates for the QP high-tail gate.

The routines in this module are integer identities and finite diagnostics.
They separate the partial Beatty graph forced by the common shell from the
additional (and essential) reciprocal-carrier/prime-power mask.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


def ceil_div(numerator: int, denominator: int) -> int:
    """Return ``ceil(numerator / denominator)`` for a positive denominator."""

    if denominator <= 0:
        raise ValueError("the denominator must be positive")
    return -((-numerator) // denominator)


@dataclass(frozen=True)
class UnimodularAnchor:
    """The canonical positive Bezout complement of ``g=(d,c)``."""

    d: int
    c: int
    u: int
    v: int

    @property
    def determinant(self) -> int:
        return self.d * self.v - self.c * self.u


def canonical_anchor(d: int, c: int) -> UnimodularAnchor:
    """Return ``s=(u,v)`` with ``d*v-c*u=1`` and ``0<u<d, 0<v<c``."""

    if min(d, c) <= 1 or gcd(d, c) != 1:
        raise ValueError("d and c must be coprime integers greater than one")
    u = (-pow(c, -1, d)) % d
    v = (1 + c * u) // d
    anchor = UnimodularAnchor(d=d, c=c, u=u, v=v)
    if not (0 < u < d and 0 < v < c and anchor.determinant == 1):
        raise AssertionError("canonical Bezout normalization failed")
    return anchor


@dataclass(frozen=True)
class ShellRoundingPoint:
    """One point ``x=R(t)g-t*s`` of the common partial Beatty graph."""

    label: int
    quotient: int
    first: int
    second: int


def shell_rounding_point(
    anchor: UnimodularAnchor,
    label: int,
    lower: int,
    upper: int,
) -> ShellRoundingPoint | None:
    """Return the unique shell point of determinant ``label``, if it exists.

    Thus, with ``g=(d,c)`` and ``s=(u,v)``, the answer is

    ``(first,second)=quotient*g-label*s``.

    The hypothesis ``upper-lower < min(c,d)`` makes the quotient unique.
    """

    if lower <= 0 or upper < lower:
        raise ValueError("invalid shell")
    if upper - lower >= min(anchor.c, anchor.d):
        raise ValueError("the shell is not short enough for uniqueness")

    lower_quotient = max(
        ceil_div(lower + label * anchor.u, anchor.d),
        ceil_div(lower + label * anchor.v, anchor.c),
    )
    upper_quotient = min(
        (upper + label * anchor.u) // anchor.d,
        (upper + label * anchor.v) // anchor.c,
    )
    if lower_quotient > upper_quotient:
        return None
    quotient = lower_quotient
    first = quotient * anchor.d - label * anchor.u
    second = quotient * anchor.c - label * anchor.v
    if not (lower <= first <= upper and lower <= second <= upper):
        raise AssertionError("shell reconstruction failed")
    if first * anchor.c - second * anchor.d != label:
        raise AssertionError("determinant label failed")
    return ShellRoundingPoint(label, quotient, first, second)


def shell_rounding_graph(
    anchor: UnimodularAnchor,
    labels: range,
    lower: int,
    upper: int,
) -> tuple[ShellRoundingPoint, ...]:
    """Enumerate the common row/color shell-rounding graph."""

    answer: list[ShellRoundingPoint] = []
    for label in labels:
        point = shell_rounding_point(anchor, label, lower, upper)
        if point is not None:
            answer.append(point)
    return tuple(answer)


def second_defect(first: ShellRoundingPoint, second: ShellRoundingPoint) -> int:
    """Return ``t*R(s)-s*R(t)`` for two rounding-graph points."""

    return (
        first.label * second.quotient
        - second.label * first.quotient
    )


def first_coordinate_defect(
    anchor: UnimodularAnchor,
    first: ShellRoundingPoint,
    second: ShellRoundingPoint,
) -> int:
    """Replay ``f=(t*a_s-s*a_t)/d`` exactly."""

    numerator = (
        first.label * second.first
        - second.label * first.first
    )
    if numerator % anchor.d:
        raise AssertionError("the first-coordinate numerator is not divisible by d")
    return numerator // anchor.d


@dataclass(frozen=True)
class CarrierInterval:
    """Integer endpoints after clearing the two reciprocal carry windows."""

    lower_numerators: tuple[int, int]
    upper_numerators: tuple[int, int]
    denominators: tuple[int, int]

    def integer_candidates(self, shell_lower: int, shell_upper: int) -> tuple[int, ...]:
        lower = max(
            shell_lower,
            ceil_div(self.lower_numerators[0], self.denominators[0]),
            ceil_div(self.lower_numerators[1], self.denominators[1]),
        )
        upper = min(
            shell_upper,
            self.upper_numerators[0] // self.denominators[0],
            self.upper_numerators[1] // self.denominators[1],
        )
        if lower > upper:
            return ()
        return tuple(range(lower, upper + 1))


def carrier_interval(
    *,
    target: int,
    tolerance: int,
    row: ShellRoundingPoint,
    first_color: int,
    second_color: int,
) -> CarrierInterval:
    """Return the exact common-carrier interval for two cubic windows.

    The two requirements are

    ``|8*row.first*b*first_color-target| <= tolerance`` and
    ``|8*row.second*b*second_color-target| <= tolerance``.
    """

    if target <= 0 or tolerance < 0 or min(first_color, second_color) <= 0:
        raise ValueError("invalid carrier parameters")
    denominators = (
        8 * row.first * first_color,
        8 * row.second * second_color,
    )
    return CarrierInterval(
        lower_numerators=(target - tolerance, target - tolerance),
        upper_numerators=(target + tolerance, target + tolerance),
        denominators=denominators,
    )


def max_collinear(points: tuple[ShellRoundingPoint, ...]) -> int:
    """Return the exact maximum number of graph points on one affine line."""

    if not points:
        return 0
    best = 1
    for index, point in enumerate(points):
        slopes: dict[tuple[int, int], int] = {}
        for other in points[index + 1 :]:
            dx = other.label - point.label
            dy = other.quotient - point.quotient
            divisor = gcd(abs(dx), abs(dy))
            dx //= divisor
            dy //= divisor
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            slope = (dx, dy)
            slopes[slope] = slopes.get(slope, 0) + 1
        if slopes:
            best = max(best, 1 + max(slopes.values()))
    return best


@dataclass(frozen=True)
class HostileRoundingAudit:
    anchor: UnimodularAnchor
    lower: int
    upper: int
    label_cap: int
    point_count: int
    maximum_collinear: int
    maximum_second_defect: int
    minimum_degree_at_cap: int


def hostile_rounding_audit() -> HostileRoundingAudit:
    """Replay a scattered exact-integer partial-Beatty obstruction.

    Both anchor coordinates are prime.  The remaining coordinates are
    unrestricted integers, so this is deliberately not an actual-QP
    counterexample.
    """

    anchor = canonical_anchor(d=6089, c=5179)
    lower, upper, label_cap = 4098, 6112, 1000
    points = shell_rounding_graph(anchor, range(1, label_cap + 1), lower, upper)
    defects = [abs(second_defect(left, right)) for left in points for right in points]
    degrees = [
        sum(abs(second_defect(left, right)) <= label_cap for right in points)
        for left in points
    ]
    return HostileRoundingAudit(
        anchor=anchor,
        lower=lower,
        upper=upper,
        label_cap=label_cap,
        point_count=len(points),
        maximum_collinear=max_collinear(points),
        maximum_second_defect=max(defects, default=0),
        minimum_degree_at_cap=min(degrees, default=0),
    )

