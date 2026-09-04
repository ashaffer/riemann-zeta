"""Exact finite checks for the balanced broad rank-two chart gate.

The accompanying report proves the arithmetic and lattice statements.
This module only replays the projection index, divided-second-difference,
and rational-exponent ledgers; it does not claim the sharp four-cycle
bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd
from typing import Iterable, Sequence


Vector4 = tuple[int, int, int, int]


def _det2(a: Sequence[int], b: Sequence[int], i: int, j: int) -> int:
    return a[i] * b[j] - a[j] * b[i]


def two_by_two_minors(a: Vector4, b: Vector4) -> tuple[int, ...]:
    """Return the six Pluecker coordinates of two integral rows."""

    return tuple(_det2(a, b, i, j) for i, j in combinations(range(4), 2))


def minor_content(a: Vector4, b: Vector4) -> int:
    """Return the gcd of the six two-by-two minors."""

    content = 0
    for value in two_by_two_minors(a, b):
        content = gcd(content, abs(value))
    return content


def max_complementary_projection_index(a: Vector4, b: Vector4) -> int:
    """Return the largest absolute two-by-two minor.

    For a primitive row plane this is the exact index of the complementary
    coordinate projection of its integral orthogonal lattice.
    """

    if minor_content(a, b) != 1:
        raise ValueError("the row plane must be primitive")
    index = max(abs(value) for value in two_by_two_minors(a, b))
    if not index:
        raise ValueError("the two rows must be independent")
    return index


def divided_second_difference(
    p0: Vector4,
    p1: Vector4,
    p2: Vector4,
    t0: int,
    t1: int,
    t2: int,
) -> Vector4:
    """Return ``h1*(p1-p0)-h0*(p2-p1)``.

    If the points have the form ``base+t*V3+w`` with ``w`` in one fixed
    plane, the returned vector lies in that plane.
    """

    h0 = t1 - t0
    h1 = t2 - t1
    if h0 <= 0 or h1 <= 0:
        raise ValueError("slice coordinates must be strictly increasing")
    e0 = tuple(p1[i] - p0[i] for i in range(4))
    e1 = tuple(p2[i] - p1[i] for i in range(4))
    return tuple(h1 * e0[i] - h0 * e1[i] for i in range(4))  # type: ignore[return-value]


def four_point_plane_vectors(
    points: Sequence[Vector4], times: Sequence[int]
) -> tuple[Vector4, Vector4]:
    """Return the two transverse-cancelled vectors from four slices.

    For ``P_j=base+t_j*V3+w_j`` both output vectors lie in the plane of
    the ``w_j``.  They are independent exactly when the four points are
    affinely independent.
    """

    if len(points) != 4 or len(times) != 4:
        raise ValueError("exactly four points and four times are required")
    if len(set(times)) != 4:
        raise ValueError("slice coordinates must be distinct")
    h1 = times[1] - times[0]
    if not h1:
        raise ValueError("the first two slice coordinates must differ")
    e1 = tuple(points[1][i] - points[0][i] for i in range(4))
    output: list[Vector4] = []
    for j in (2, 3):
        ej = tuple(points[j][i] - points[0][i] for i in range(4))
        hj = times[j] - times[0]
        output.append(
            tuple(h1 * ej[i] - hj * e1[i] for i in range(4))  # type: ignore[arg-type]
        )
    return output[0], output[1]


def dot(a: Sequence[int], b: Sequence[int]) -> int:
    return sum(x * y for x, y in zip(a, b, strict=True))


@dataclass(frozen=True)
class BalancedBroadLedger:
    plane_covolume: Fraction
    slice_cap: Fraction
    fixed_plane_colors: Fraction
    fixed_plane_mass: Fraction
    total_colors: Fraction
    trivial_slice_incidence: Fraction
    target_slice_incidence: Fraction
    missing_power: Fraction
    saturated_plane_labels: Fraction
    required_plane_labels: Fraction


def balanced_broad_ledger() -> BalancedBroadLedger:
    """Return the exact powers of ``D`` at the balanced flat endpoint."""

    q = Fraction(33, 16)
    lam = Fraction(11, 16)
    support = Fraction(15, 8)
    plane_covolume = 2 * lam
    slice_cap = 1 - lam
    fixed_plane_colors = support + q - plane_covolume
    fixed_plane_mass = fixed_plane_colors - 2 * support
    total_colors = 3 * support + 1 - q
    trivial = total_colors + slice_cap
    target = 1 + 2 * support
    saturated_labels = total_colors - fixed_plane_colors
    required_labels = target - slice_cap - fixed_plane_colors
    return BalancedBroadLedger(
        plane_covolume=plane_covolume,
        slice_cap=slice_cap,
        fixed_plane_colors=fixed_plane_colors,
        fixed_plane_mass=fixed_plane_mass,
        total_colors=total_colors,
        trivial_slice_incidence=trivial,
        target_slice_incidence=target,
        missing_power=trivial - target,
        saturated_plane_labels=saturated_labels,
        required_plane_labels=required_labels,
    )


def prime_lattice_pair_upper_bound(
    support_size: int, shell_diameter: int, lattice_index: int
) -> int:
    """Integer version of ``M*(1+q/Delta)`` with harmless rounding."""

    if support_size < 0 or shell_diameter < 0 or lattice_index <= 0:
        raise ValueError("invalid lattice-count parameters")
    return support_size * (1 + shell_diameter // lattice_index)
