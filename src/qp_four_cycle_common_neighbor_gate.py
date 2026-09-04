"""Exact gcd reduction and finite diagnostics for common carry neighbors.

The arithmetic identity in this module isolates the small-denominator
integer resonance which is absent for two distinct prime-power rows in the
narrow project shell.  The sparse common-neighbor computations are finite
diagnostics only.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

import numpy as np
from scipy.sparse import coo_matrix

from qp_four_cycle_hostile_lab import FourCycleCore


@dataclass(frozen=True)
class ResidualDifference:
    first_residual: int
    second_residual: int
    cross_integer: int
    identity_error: int


def residual_difference(
    *,
    q: int,
    first_row: int,
    second_row: int,
    column: int,
    first_color: int,
    second_color: int,
) -> ResidualDifference:
    """Replay ``r2-r1=8*b*(a2*d-a1*c)`` exactly."""

    first = 8 * first_row * column * first_color - q**3
    second = 8 * second_row * column * second_color - q**3
    cross = second_row * second_color - first_row * first_color
    return ResidualDifference(
        first_residual=first,
        second_residual=second,
        cross_integer=cross,
        identity_error=(second - first) - 8 * column * cross,
    )


@dataclass(frozen=True)
class GcdReduction:
    gcd: int
    first_reduced_row: int
    second_reduced_row: int
    reduced_cross_integer: int
    resonant: bool
    resonance_parameter: int | None


def gcd_reduce_colors(
    first_row: int,
    second_row: int,
    first_color: int,
    second_color: int,
) -> GcdReduction:
    """Reduce ``a2*d-a1*c`` by ``gcd(a1,a2)``.

    If the reduced cross integer vanishes, coprimality gives
    ``first_color=r*h`` and ``second_color=s*h`` for a unique positive ``h``,
    where ``a1=s*g`` and ``a2=r*g``.
    """

    if min(first_row, second_row, first_color, second_color) <= 0:
        raise ValueError("all entries must be positive")
    gcd = math.gcd(first_row, second_row)
    s = first_row // gcd
    r = second_row // gcd
    cross = second_row * second_color - first_row * first_color
    if cross % gcd != 0:
        raise AssertionError("the cross integer must be divisible by the row gcd")
    reduced = cross // gcd
    resonant = reduced == 0
    parameter: int | None = None
    if resonant:
        if first_color % r or second_color % s:
            raise AssertionError("coprime resonance divisibility failed")
        first_parameter = first_color // r
        second_parameter = second_color // s
        if first_parameter != second_parameter:
            raise AssertionError("resonance parameters disagree")
        parameter = first_parameter
    return GcdReduction(
        gcd=gcd,
        first_reduced_row=s,
        second_reduced_row=r,
        reduced_cross_integer=reduced,
        resonant=resonant,
        resonance_parameter=parameter,
    )


def forced_resonance(
    *,
    row_gcd: int,
    residual_bound: float,
    minimum_column: int,
) -> bool:
    """Whether the residual window forces the reduced cross integer to zero.

    If both cubic residuals have modulus at most ``residual_bound``, then

    ``|a2*d-a1*c| <= residual_bound/(4*b)``.

    This integer is a multiple of ``row_gcd``.
    """

    if row_gcd <= 0 or residual_bound < 0 or minimum_column <= 0:
        raise ValueError("invalid forcing parameters")
    return row_gcd > residual_bound / (4.0 * minimum_column)


def resonant_product_residual(
    *,
    q: int,
    row_gcd: int,
    first_reduced_row: int,
    second_reduced_row: int,
    column: int,
    resonance_parameter: int,
) -> int:
    """Common residual after ``a1=sg,a2=rg,c=rh,d=sh``."""

    return (
        8
        * first_reduced_row
        * second_reduced_row
        * row_gcd
        * column
        * resonance_parameter
        - q**3
    )


def resonant_product_interval_length(
    *,
    residual_bound: float,
    row_gcd: int,
    first_reduced_row: int,
    second_reduced_row: int,
) -> float:
    """Full allowed length in the integer product ``column*h``."""

    denominator = (
        4.0 * row_gcd * first_reduced_row * second_reduced_row
    )
    if denominator <= 0 or residual_bound < 0:
        raise ValueError("invalid interval parameters")
    # |8srgbh-q^3|<=E gives total interval length 2E/(8srg).
    return residual_bound / denominator


@dataclass(frozen=True)
class CommonNeighborMaximum:
    degree: int
    first_row: int
    second_row: int
    row_gap: int
    row_gcd: int


def maximum_common_neighbor_degree(core: FourCycleCore) -> CommonNeighborMaximum:
    """Compute the exact maximum support intersection in a finite core."""

    dimension = core.dimension
    incidence = coo_matrix(
        (
            np.ones(core.rows.size, dtype=np.int32),
            (core.rows, core.columns),
        ),
        shape=(dimension, dimension),
    ).tocsr()
    common = (incidence @ incidence.T).tocoo()
    mask = common.row != common.col
    if not np.any(mask):
        return CommonNeighborMaximum(0, 0, 0, 0, 0)
    degrees = common.data[mask]
    position = int(np.argmax(degrees))
    first_index = int(common.row[mask][position])
    second_index = int(common.col[mask][position])
    first = int(core.values[first_index])
    second = int(core.values[second_index])
    return CommonNeighborMaximum(
        degree=int(degrees[position]),
        first_row=first,
        second_row=second,
        row_gap=abs(second - first),
        row_gcd=math.gcd(first, second),
    )


def common_neighbor_degree(
    core: FourCycleCore,
    first_row_value: int,
    second_row_value: int,
) -> int:
    """Common support degree of two specified finite rows."""

    lookup = {int(value): index for index, value in enumerate(core.values)}
    if first_row_value not in lookup or second_row_value not in lookup:
        raise ValueError("row is outside the core")
    first_index = lookup[first_row_value]
    second_index = lookup[second_row_value]
    first_columns = set(
        int(value) for value in core.columns[core.rows == first_index]
    )
    second_columns = set(
        int(value) for value in core.columns[core.rows == second_index]
    )
    return len(first_columns & second_columns)

