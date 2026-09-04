"""Finite identities for critical-cube affine rank rigidity."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable


Point = tuple[int, int, int]


@dataclass(frozen=True)
class CriticalCubeLedger:
    point_count: int
    affine_rank: int
    maximum_linearized_error: int
    maximum_difference_determinant: int
    cramer_upper_bound: int
    gradient_minimum: int


def _det3(rows: tuple[Point, Point, Point]) -> int:
    (a, b, c), (d, e, f), (g, h, i) = rows
    return (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )


def product_linearization(
    base: Point, point: Point
) -> tuple[int, int, int]:
    """Return product difference, linear term, and nonlinear remainder."""

    a, b, c = base
    other_a, other_b, other_c = point
    x, y, z = other_a - a, other_b - b, other_c - c
    difference = other_a * other_b * other_c - a * b * c
    linear = b * c * x + a * c * y + a * b * z
    remainder = c * x * y + b * x * z + a * y * z + x * y * z
    if difference != linear + remainder:
        raise AssertionError("product Taylor identity failed")
    return difference, linear, remainder


def critical_cube_ledger(
    points: Iterable[Point],
    *,
    target: int,
    residual_half_width: int,
    cube_side: int,
) -> CriticalCubeLedger:
    """Audit one finite critical cube and compute its affine rank."""

    point_set = tuple(sorted(set(points)))
    if not point_set:
        raise ValueError("the critical cube must be nonempty")
    if residual_half_width < 0 or cube_side < 0:
        raise ValueError("invalid cube parameters")
    for coordinate in range(3):
        values = [point[coordinate] for point in point_set]
        if max(values) - min(values) > cube_side:
            raise ValueError("the points do not lie in the stated cube")
    for point in point_set:
        if abs(8 * point[0] * point[1] * point[2] - target) > residual_half_width:
            raise ValueError("a point is outside the product window")

    base = point_set[0]
    differences: list[Point] = []
    maximum_error = 0
    for point in point_set[1:]:
        difference = tuple(
            value - origin for value, origin in zip(point, base)
        )
        differences.append(difference)  # type: ignore[arg-type]
        _, linear, _ = product_linearization(base, point)
        maximum_error = max(maximum_error, abs(linear))

    maximum_determinant = 0
    for rows in combinations(differences, 3):
        maximum_determinant = max(
            maximum_determinant,
            abs(_det3(rows)),  # type: ignore[arg-type]
        )
    if maximum_determinant:
        affine_rank = 3
    elif any(
        first[coordinate] * second[other_coordinate]
        != first[other_coordinate] * second[coordinate]
        for first, second in combinations(differences, 2)
        for coordinate, other_coordinate in ((0, 1), (0, 2), (1, 2))
    ):
        affine_rank = 2
    elif any(difference != (0, 0, 0) for difference in differences):
        affine_rank = 1
    else:
        affine_rank = 0

    a, b, c = base
    gradient_minimum = min(a * b, a * c, b * c)
    # If a nonzero determinant existed, Cramer's rule would bound every
    # gradient coordinate by six times this quantity.
    cramer_upper_bound = 6 * maximum_error * cube_side**2
    return CriticalCubeLedger(
        point_count=len(point_set),
        affine_rank=affine_rank,
        maximum_linearized_error=maximum_error,
        maximum_difference_determinant=maximum_determinant,
        cramer_upper_bound=cramer_upper_bound,
        gradient_minimum=gradient_minimum,
    )

