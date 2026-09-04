"""Exact fiber ledgers for dyadic carrier-gap sectors.

The arithmetic theorem proved in the companion report uses only two inputs:

* pair uniqueness of the carry hypergraph; and
* the one-corner near-square localization bound.

This module records the resulting finite fiber envelopes.  It does not claim
that every rectangle is covered at the target ``D`` scale.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

from qp_fixed_color_tangent_countermodel import near_square_first_carrier_bound


@dataclass(frozen=True)
class CarrierGapSector:
    """Upper bounds defining one ordered carrier-gap sector."""

    row_gap: int
    column_gap: int
    cross_gaps: tuple[tuple[int, int], tuple[int, int]]

    def __post_init__(self) -> None:
        entries = (
            self.row_gap,
            self.column_gap,
            self.cross_gaps[0][0],
            self.cross_gaps[0][1],
            self.cross_gaps[1][0],
            self.cross_gaps[1][1],
        )
        if any(value < 0 for value in entries):
            raise ValueError("gap caps must be nonnegative")

    @classmethod
    def from_carriers(
        cls,
        rows: tuple[int, int],
        columns: tuple[int, int],
    ) -> "CarrierGapSector":
        return cls(
            row_gap=abs(rows[1] - rows[0]),
            column_gap=abs(columns[1] - columns[0]),
            cross_gaps=(
                (abs(rows[0] - columns[0]), abs(rows[0] - columns[1])),
                (abs(rows[1] - columns[0]), abs(rows[1] - columns[1])),
            ),
        )


@dataclass(frozen=True)
class GapProjectionFiberBounds:
    """Fiber bounds for the three complementary color-pair projections."""

    horizontal: tuple[int, int]
    vertical: tuple[int, int]
    opposite: tuple[int, int]

    @property
    def coefficient_squares(self) -> tuple[int, int, int]:
        """Squares of the three Cauchy--Schwarz coefficients."""

        return (
            self.horizontal[0] * self.horizontal[1],
            self.vertical[0] * self.vertical[1],
            self.opposite[0] * self.opposite[1],
        )

    @property
    def best_coefficient(self) -> float:
        return math.sqrt(min(self.coefficient_squares))


def gap_projection_fiber_bounds(
    *,
    residual_cap: int,
    color_lower_bound: int,
    carrier_lower_bound: int,
    sector: CarrierGapSector,
) -> GapProjectionFiberBounds:
    """Return rigorous finite projection-fiber envelopes.

    The entries are valid for an ordered rectangle sector in a pair-unique
    carry hypergraph with the supplied shell and residual bounds.  For
    example, fixing ``(c11,c12)`` gives at most

    ``(2*row_gap+1) * min(L11,L12)``

    rectangles, where ``Lij`` is the exact coarse one-corner count.  The
    other five entries follow by symmetry or by pairing opposite colors.
    """

    corner = tuple(
        tuple(
            near_square_first_carrier_bound(
                residual_cap,
                color_lower_bound,
                carrier_lower_bound,
                sector.cross_gaps[i][j],
            )
            for j in range(2)
        )
        for i in range(2)
    )
    row_choices = 2 * sector.row_gap + 1
    column_choices = 2 * sector.column_gap + 1
    opposite_choices = min(row_choices, column_choices)

    horizontal = (
        row_choices * min(corner[0][0], corner[0][1]),
        row_choices * min(corner[1][0], corner[1][1]),
    )
    vertical = (
        column_choices * min(corner[0][0], corner[1][0]),
        column_choices * min(corner[0][1], corner[1][1]),
    )
    opposite = (
        opposite_choices * min(corner[0][0], corner[1][1]),
        opposite_choices * min(corner[0][1], corner[1][0]),
    )
    return GapProjectionFiberBounds(
        horizontal=horizontal,
        vertical=vertical,
        opposite=opposite,
    )


@dataclass(frozen=True)
class AsymptoticGapScales:
    """Integer squares of the three asymptotic projection scales."""

    horizontal_square: int
    vertical_square: int
    opposite_square: int

    @property
    def best_square(self) -> int:
        return min(
            self.horizontal_square,
            self.vertical_square,
            self.opposite_square,
        )

    @property
    def best(self) -> float:
        return math.sqrt(self.best_square)

    def covered_at_scale(self, degree_scale: int, constant: int = 1) -> bool:
        """Whether one projection coefficient is at most ``constant*D``."""

        if degree_scale < 0 or constant <= 0:
            raise ValueError("invalid target scale")
        return self.best_square <= (constant * degree_scale) ** 2


def asymptotic_gap_scales(sector: CarrierGapSector) -> AsymptoticGapScales:
    """Return the ``(1+gap)`` scale ledger without hidden square roots.

    On a fixed-width shell with ``H=O(qD)`` and ``D<=q``, the exact fiber
    coefficient is bounded by a shell-dependent constant times the square
    root of one of these three integers.
    """

    alpha = 1 + sector.row_gap
    beta = 1 + sector.column_gap
    rho = tuple(tuple(1 + value for value in row) for row in sector.cross_gaps)
    horizontal_square = (
        alpha**2
        * min(rho[0][0], rho[0][1])
        * min(rho[1][0], rho[1][1])
    )
    vertical_square = (
        beta**2
        * min(rho[0][0], rho[1][0])
        * min(rho[0][1], rho[1][1])
    )
    opposite_square = (
        min(alpha, beta) ** 2
        * min(rho[0][0], rho[1][1])
        * min(rho[0][1], rho[1][0])
    )
    return AsymptoticGapScales(
        horizontal_square=horizontal_square,
        vertical_square=vertical_square,
        opposite_square=opposite_square,
    )
