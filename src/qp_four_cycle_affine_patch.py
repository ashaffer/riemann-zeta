"""Exact ledgers for the affine/Hankel four-cycle patch theorems.

The theorem itself is elementary: in a pair-unique triple system, each
fixed-color slice is a partial matching.  If a patch uses ``M`` colors and
each such matching has at most ``L`` edges, its weighted fourth trace is at
most ``L*min(L,M)*||z||_2^4``.  An affine-plane equation is a convenient geometric
way to bound ``L`` and to recognize a whole union of tangent charts as one
coherence patch.  The parallel-line ledger at the end records the stronger
product-band mechanism: rich rational lines of one fixed direction merge
even when their intercepts do not lie in one affine three-variable plane.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from math import gcd, isqrt
from typing import Iterable, Mapping


Triple = tuple[int, int, int]


@dataclass(frozen=True)
class AffinePatchLedger:
    edge_count: int
    color_support_size: int
    maximum_color_matching_size: int
    fourth_trace_coefficient: int
    affine_level: int


@dataclass(frozen=True)
class SharedProgressionPinningLedger:
    first_anchor_residual: int
    second_anchor_residual: int
    slope_product_difference: int
    pinning_quantum: int
    residual_budget: int


@dataclass(frozen=True)
class LinearGridIdentityLedger:
    row_endpoint_defect: int
    column_endpoint_defect: int
    row_curvature_defect: int
    column_curvature_defect: int
    anchor_factorization_defect: int


@dataclass(frozen=True)
class ParallelProductBandLineLedger:
    """Exact invariants of one rich opposite-slope product-band line."""

    primitive_row_step: int
    primitive_column_step: int
    direction_product: int
    line_invariant: int
    occupied_points: int
    branch_span_lower_bound: int
    curvature_quantity: int
    curvature_upper_bound: int
    invariant_square_defect: int
    invariant_square_error_bound: int
    consecutive_square_gap: int

    @property
    def invariant_is_pinned(self) -> bool:
        """Whether the error interval contains at most one positive square."""

        return self.consecutive_square_gap > 2 * self.invariant_square_error_bound


@dataclass(frozen=True)
class FixedDirectionMergerLedger:
    """Degree and fourth-trace envelope after parallel-line pinning."""

    projected_direction_products: tuple[int, int, int, int]
    projected_point_caps: tuple[int, int, int, int]
    color_degree_bound: int
    fourth_trace_coefficient: int


def affine_patch_ledger(
    triples: Iterable[Triple],
    coefficients: tuple[int, int, int],
) -> AffinePatchLedger:
    """Validate a pair-unique affine patch and return its trace coefficient.

    Every retained triple must have the same value of
    ``alpha*a+beta*b+gamma*c``.  Pair uniqueness is checked in all three
    coordinate projections.
    """

    edge_set = set(triples)
    if not edge_set:
        raise ValueError("an affine patch must contain an edge")
    alpha, beta, gamma = coefficients
    if alpha == beta == gamma == 0:
        raise ValueError("the affine normal must be nonzero")

    levels = {
        alpha * a + beta * b + gamma * c for a, b, c in edge_set
    }
    if len(levels) != 1:
        raise ValueError("the triples do not lie in one affine plane")

    projections: tuple[tuple[int, int, int], ...] = (
        (0, 1, 2),
        (0, 2, 1),
        (1, 2, 0),
    )
    for first, second, third in projections:
        fibers: dict[tuple[int, int], int] = {}
        for edge in edge_set:
            key = (edge[first], edge[second])
            value = edge[third]
            old = fibers.setdefault(key, value)
            if old != value:
                raise ValueError("the patch is not pair-unique")

    color_degrees: dict[int, int] = defaultdict(int)
    for _, _, color in edge_set:
        color_degrees[color] += 1
    support_size = len(color_degrees)
    maximum_degree = max(color_degrees.values())
    return AffinePatchLedger(
        edge_count=len(edge_set),
        color_support_size=support_size,
        maximum_color_matching_size=maximum_degree,
        fourth_trace_coefficient=(
            maximum_degree * min(maximum_degree, support_size)
        ),
        affine_level=next(iter(levels)),
    )


def weighted_fourth_trace(
    triples: Iterable[Triple],
    weights: Mapping[int, complex],
) -> float:
    """Compute ``tr((A A*)^2)`` for the unphased finite patch."""

    entries: dict[tuple[int, int], complex] = {}
    rows: set[int] = set()
    columns: set[int] = set()
    for row, column, color in set(triples):
        key = (row, column)
        value = weights.get(color, 0j)
        if key in entries and entries[key] != value:
            raise ValueError("two colors occupy one matrix cell")
        entries[key] = value
        rows.add(row)
        columns.add(column)

    trace = 0.0
    for row in rows:
        for other_row in rows:
            gram = sum(
                entries.get((row, column), 0j).conjugate()
                * entries.get((other_row, column), 0j)
                for column in columns
            )
            trace += abs(gram) ** 2
    return trace


def coherence_trace_coefficient(
    color_support_size: int,
    maximum_color_matching_size: int,
) -> int:
    """Return the universal ``L*min(L,M)`` patch trace coefficient."""

    if color_support_size < 0 or maximum_color_matching_size < 0:
        raise ValueError("support and matching sizes must be nonnegative")
    return maximum_color_matching_size * min(
        maximum_color_matching_size, color_support_size
    )


def _ceil_sqrt_ratio(numerator: int, denominator: int) -> int:
    """Return ``ceil(sqrt(numerator / denominator))`` exactly."""

    if numerator < 0 or denominator <= 0:
        raise ValueError("invalid square-root ratio")
    if numerator == 0:
        return 0
    return isqrt((numerator - 1) // denominator) + 1


def parallel_product_band_point_cap(
    product_half_width: int,
    primitive_row_step: int,
    primitive_column_step: int,
) -> int:
    """Return a point cap for an opposite-slope line in a product band.

    On ``(a,b)=(a0+p*t,b0-s*t)``, the product is a concave quadratic with
    curvature ``p*s``.  The inverse image of an interval of half-width
    ``Delta`` has at most two components.  The returned conservative bound
    is ``2+2*ceil(sqrt(2*Delta/(p*s)))``.
    """

    if product_half_width < 0:
        raise ValueError("the product half-width must be nonnegative")
    if min(primitive_row_step, primitive_column_step) <= 0:
        raise ValueError("primitive steps must be positive")
    direction_product = primitive_row_step * primitive_column_step
    radius = _ceil_sqrt_ratio(2 * product_half_width, direction_product)
    return 2 + 2 * radius


def parallel_product_band_line_ledger(
    points: Iterable[tuple[int, int]],
    *,
    product_center: int,
    product_half_width: int,
) -> ParallelProductBandLineLedger:
    """Validate a rich integer line in one product band.

    At least three distinct positive points are required.  The line must
    have opposite-sign coordinate direction.  After primitive orientation

    ``(a,b)=(a0+p*t,b0-s*t)``, ``p,s>0``,

    the invariant ``W=s*a+p*b`` is constant and

    ``4*p*s*a*b = W^2-(s*a-p*b)^2``.

    Pigeonholing the occupied parameters between the two branches of the
    quadratic gives the exact conservative bounds recorded below.  Missing
    parameters are allowed: only occupied integer spans are used.
    """

    frozen = tuple(sorted(set((int(a), int(b)) for a, b in points)))
    if len(frozen) < 3:
        raise ValueError("parallel-line pinning needs at least three points")
    if product_half_width < 0:
        raise ValueError("the product half-width must be nonnegative")
    if any(min(point) <= 0 for point in frozen):
        raise ValueError("product-band coordinates must be positive")

    anchor = frozen[0]
    row_difference = frozen[1][0] - anchor[0]
    column_difference = frozen[1][1] - anchor[1]
    if row_difference == 0 or column_difference == 0:
        raise ValueError("an axis-parallel product-band line is not rich")
    if row_difference * column_difference >= 0:
        raise ValueError("a rich product-band line must have opposite slope")
    divisor = gcd(abs(row_difference), abs(column_difference))
    signed_row_step = row_difference // divisor
    signed_column_step = column_difference // divisor
    if signed_row_step < 0:
        signed_row_step = -signed_row_step
        signed_column_step = -signed_column_step
    if signed_column_step >= 0:
        raise AssertionError("the opposite-slope orientation failed")
    row_step = signed_row_step
    column_step = -signed_column_step

    invariants: set[int] = set()
    for row, column in frozen:
        row_offset = row - anchor[0]
        column_offset = column - anchor[1]
        if row_offset % row_step or column_offset % column_step:
            raise ValueError("a point is not integral on the primitive line")
        row_parameter = row_offset // row_step
        column_parameter = -column_offset // column_step
        if row_parameter != column_parameter:
            raise ValueError("the supplied points are not collinear")
        if abs(row * column - product_center) > product_half_width:
            raise ValueError("a point lies outside the product band")
        invariants.add(column_step * row + row_step * column)
    if len(invariants) != 1:
        raise AssertionError("the line invariant is not constant")

    branch_occupancy = (len(frozen) + 1) // 2
    branch_span = branch_occupancy - 1
    if branch_span <= 0:
        raise AssertionError("three points did not leave a two-point branch")
    direction_product = row_step * column_step
    curvature_quantity = direction_product * branch_span * branch_span
    curvature_bound = 8 * product_half_width
    if curvature_quantity > curvature_bound:
        raise AssertionError("the rich-line curvature bound failed")

    invariant = next(iter(invariants))
    square_defect = abs(
        invariant * invariant
        - 4 * direction_product * product_center
    )
    square_error = (
        48 * product_half_width * product_half_width
        // (branch_span * branch_span)
    )
    if square_defect > square_error:
        raise AssertionError("the tangent-invariant error bound failed")
    return ParallelProductBandLineLedger(
        primitive_row_step=row_step,
        primitive_column_step=column_step,
        direction_product=direction_product,
        line_invariant=invariant,
        occupied_points=len(frozen),
        branch_span_lower_bound=branch_span,
        curvature_quantity=curvature_quantity,
        curvature_upper_bound=curvature_bound,
        invariant_square_defect=square_defect,
        invariant_square_error_bound=square_error,
        consecutive_square_gap=2 * invariant - 1,
    )


def fixed_direction_merger_ledger(
    raw_direction: tuple[int, int, int, int],
    *,
    product_half_width: int,
) -> FixedDirectionMergerLedger:
    """Return the fixed-four-carrier-direction merger envelope.

    The first two coordinates are row steps and the last two are column
    steps.  Every cell projection must have opposite sign; otherwise a line
    with three occupied product-band points is impossible.  This routine
    assumes the scale-separation hypothesis has already pinned ``O(1)``
    geometric line invariants per color and cell position.
    """

    if len(raw_direction) != 4 or any(value == 0 for value in raw_direction):
        raise ValueError("the four-carrier direction must have nonzero entries")
    row_steps = raw_direction[:2]
    column_steps = raw_direction[2:]
    products: list[int] = []
    caps: list[int] = []
    for row_step in row_steps:
        for column_step in column_steps:
            if row_step * column_step >= 0:
                raise ValueError("every rich cell projection must have opposite sign")
            divisor = gcd(abs(row_step), abs(column_step))
            primitive_row = abs(row_step) // divisor
            primitive_column = abs(column_step) // divisor
            products.append(primitive_row * primitive_column)
            caps.append(
                parallel_product_band_point_cap(
                    product_half_width,
                    primitive_row,
                    primitive_column,
                )
            )
    degree = sum(caps)
    return FixedDirectionMergerLedger(
        projected_direction_products=tuple(products),  # type: ignore[arg-type]
        projected_point_caps=tuple(caps),  # type: ignore[arg-type]
        color_degree_bound=degree,
        fourth_trace_coefficient=degree * degree,
    )


def shared_progression_slope_pinning(
    *,
    target: int,
    residual_half_width: int,
    color_anchor: int,
    color_step: int,
    first_steps: tuple[int, int],
    second_steps: tuple[int, int],
) -> SharedProgressionPinningLedger:
    """Replay the exact slope-product pinning for two linearized blocks.

    Exact first-order cancellation forces

    ``A=R*C/U`` and ``B=S*C/U``.

    If both anchor products lie in the same target window, subtraction gives

    ``8*C^3*|R*S-R'*S'| <= 2*H*U^2``.

    Therefore a quantum larger than the residual budget pins the two slope
    products.  The function raises if divisibility or window membership
    fails, and raises an assertion if the exact implication fails.
    """

    if residual_half_width < 0 or color_anchor <= 0 or color_step <= 0:
        raise ValueError("invalid target window or color progression")
    r, s = first_steps
    other_r, other_s = second_steps
    if min(r, s, other_r, other_s) <= 0:
        raise ValueError("tangent steps must be positive")
    numerators = (
        r * color_anchor,
        s * color_anchor,
        other_r * color_anchor,
        other_s * color_anchor,
    )
    if any(value % color_step for value in numerators):
        raise ValueError("the cancellation centers are not integral")
    first_a, first_b, second_a, second_b = (
        value // color_step for value in numerators
    )
    first_residual = 8 * first_a * first_b * color_anchor - target
    second_residual = 8 * second_a * second_b * color_anchor - target
    if max(abs(first_residual), abs(second_residual)) > residual_half_width:
        raise ValueError("an anchor lies outside the common product window")
    difference = abs(r * s - other_r * other_s)
    quantum = 8 * color_anchor**3
    budget = 2 * residual_half_width * color_step**2
    if quantum > budget and difference != 0:
        raise AssertionError("the pinned slope products differ")
    return SharedProgressionPinningLedger(
        first_anchor_residual=first_residual,
        second_anchor_residual=second_residual,
        slope_product_difference=difference,
        pinning_quantum=quantum,
        residual_budget=budget,
    )


def linear_grid_identity_ledger(
    *,
    row_base: int,
    column_base: int,
    color_anchor: int,
    row_step: int,
    column_step: int,
    color_step: int,
    length: int,
) -> LinearGridIdentityLedger:
    """Replay the endpoint, curvature, and thickened-anchor identities."""

    if min(
        row_base,
        column_base,
        color_anchor,
        row_step,
        column_step,
        color_step,
        length,
    ) <= 0:
        raise ValueError("linear-grid parameters must be positive")
    a = row_base
    b = column_base
    c = color_anchor
    r = row_step
    s = column_step
    u = color_step
    n = length
    endpoint_color = c - u * n
    delta_a = u * a - r * endpoint_color
    delta_b = u * b - s * endpoint_color

    row_endpoint = (a + r * n) * b * endpoint_color - a * b * c
    column_endpoint = a * (b + s * n) * endpoint_color - a * b * c
    k = n // 2
    if k == 0:
        row_curvature_defect = 0
        column_curvature_defect = 0
    else:
        row_values = tuple(
            b * (a + r * index) * (c - u * index)
            for index in (0, k, 2 * k)
        )
        column_values = tuple(
            a * (b + s * index) * (c - u * index)
            for index in (0, k, 2 * k)
        )
        row_curvature_defect = (
            row_values[0]
            - 2 * row_values[1]
            + row_values[2]
            + 2 * b * r * u * k * k
        )
        column_curvature_defect = (
            column_values[0]
            - 2 * column_values[1]
            + column_values[2]
            + 2 * a * s * u * k * k
        )
    anchor_factorization_defect = (
        u * u * a * b * c
        - c
        * (r * endpoint_color + delta_a)
        * (s * endpoint_color + delta_b)
    )
    return LinearGridIdentityLedger(
        row_endpoint_defect=row_endpoint + b * n * delta_a,
        column_endpoint_defect=column_endpoint + a * n * delta_b,
        row_curvature_defect=row_curvature_defect,
        column_curvature_defect=column_curvature_defect,
        anchor_factorization_defect=anchor_factorization_defect,
    )
