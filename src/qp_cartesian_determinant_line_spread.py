"""Exact diagnostics for the Cartesian determinant-strip line-spread theorem.

For finite nonzero integer-vector sets ``U,V`` put

    F(u,v) = u[0]*v[0] - u[1]*v[1].

If ``|F|<=K`` on the whole Cartesian product and no affine line contains
more than ``R_U`` points of ``U`` or ``R_V`` points of ``V``, then

    |U| |V| <= 162 max(1,K) R_U R_V.

The proof combines bilinear Pluecker with a two-dimensional lattice
line-spread lemma.  This module replays all finite invariants and hostile
examples; the proof is recorded in the companion result note.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt
from fractions import Fraction
from typing import Sequence


Vector2 = tuple[int, int]


def _rational_rank(rows: Sequence[Sequence[int]]) -> int:
    """Return the exact row rank of a small integer matrix."""

    matrix = [[Fraction(value) for value in row] for row in rows]
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix rows must have one common width")
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (index for index in range(pivot_row, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for index, row in enumerate(matrix):
            if index == pivot_row or not row[column]:
                continue
            multiplier = row[column]
            matrix[index] = [
                value - multiplier * pivot_value
                for value, pivot_value in zip(row, matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def determinant(first: Vector2, second: Vector2) -> int:
    return first[0] * second[1] - first[1] * second[0]


def cross_form(left: Vector2, right: Vector2) -> int:
    return left[0] * right[0] - left[1] * right[1]


def _primitive_direction(first: Vector2, second: Vector2) -> Vector2:
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    divisor = gcd(abs(dx), abs(dy))
    if not divisor:
        raise ValueError("affine-line directions require distinct points")
    dx //= divisor
    dy //= divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return dx, dy


def maximum_affine_line_occupancy(points: Sequence[Vector2]) -> int:
    """Return the exact maximum number of supplied points on one line."""

    support = tuple(points)
    if len(set(support)) != len(support):
        raise ValueError("line occupancy expects a set of distinct points")
    if len(support) <= 2:
        return len(support)
    answer = 2
    for index, anchor in enumerate(support):
        direction_counts: dict[Vector2, int] = {}
        for other_index, other in enumerate(support):
            if other_index == index:
                continue
            direction = _primitive_direction(anchor, other)
            direction_counts[direction] = direction_counts.get(direction, 0) + 1
        answer = max(answer, 1 + max(direction_counts.values(), default=0))
    return answer


def maximum_pair_determinant(points: Sequence[Vector2]) -> int:
    support = tuple(points)
    return max(
        (
            abs(determinant(support[first], support[second]))
            for first in range(len(support))
            for second in range(first + 1, len(support))
        ),
        default=0,
    )


def lattice_line_spread_ceiling(
    maximum_determinant: int, maximum_line_occupancy: int
) -> int:
    """Integral ceiling from the normalized-lattice proof.

    When ``Delta>0``, a determinant-maximizing pair maps the point set into
    ``[-1,1]^2`` in a lattice of covolume ``1/Delta``.  Minkowski supplies a
    primitive vector of sup norm at most ``2/sqrt(Delta)``.  At most

        2 floor(4 sqrt(Delta)) + 1

    parallel lattice lines meet the square.  For ``Delta=0`` the whole set
    lies on one line through the origin.
    """

    if maximum_determinant < 0 or maximum_line_occupancy < 0:
        raise ValueError("determinant and occupancy bounds must be nonnegative")
    if maximum_determinant == 0:
        return maximum_line_occupancy
    line_count = 2 * isqrt(16 * maximum_determinant) + 1
    return maximum_line_occupancy * line_count


@dataclass(frozen=True)
class CartesianLineSpreadCertificate:
    """Exact finite ledger for the determinant-strip inverse theorem."""

    left_population: int
    right_population: int
    cross_determinant_cap: int
    left_maximum_determinant: int
    right_maximum_determinant: int
    plucker_product: int
    plucker_ceiling: int
    left_maximum_line_occupancy: int
    right_maximum_line_occupancy: int
    left_line_spread_ceiling: int
    right_line_spread_ceiling: int
    population_product: int
    universal_population_ceiling: int


@dataclass(frozen=True)
class ProjectedLineLiftAudit:
    """Fail-closed audit of a projected neighbor line and its witnesses.

    A projected equation ``A*d+B*D+C=0`` always homogenizes to

        A*(x*d)+B*(x*D)+C*x=0.

    This is only a plane in product coordinates.  It need not make the
    original triples ``(x,b,d)`` and ``(x,B,D)`` coplanar, and therefore is
    not by itself an affine/Hankel completion-packet certificate.
    """

    q: int
    hard_window_radius: int
    center: Vector2
    projected_line_equation: tuple[int, int, int]
    neighbor_count: int
    determinant_tokens: tuple[int, ...]
    maximum_product_residual: int
    witness_graph_affine_rank: int
    product_lift_linear_rank: int
    original_triple_affine_rank: int

    @property
    def all_edges_are_residual(self) -> bool:
        return all(token != 0 for token in self.determinant_tokens)

    @property
    def witnesses_are_affine_on_projected_line(self) -> bool:
        return self.witness_graph_affine_rank <= 1

    @property
    def product_lift_is_planar(self) -> bool:
        return self.product_lift_linear_rank <= 2

    @property
    def original_triples_are_coplanar(self) -> bool:
        return self.original_triple_affine_rank <= 2


@dataclass(frozen=True)
class WitnessInterpolationCertificate:
    """Exact divided-difference ledger for a projected neighbor line.

    Samples are ``(t,x,d)`` with ``d=d_0+p*t`` and

        |8*b*x*d-q^3| <= q*D.

    For three parameters ``t_0<t_1<t_2``, with successive gaps ``a,c``,
    the integer affine defect

        J=c*x_0+a*x_2-(a+c)*x_1

    is split exactly into the reciprocal main term and the three hard-window
    errors.  A strict upper bound below one therefore forces ``J=0``.
    """

    q: int
    hard_window_radius: int
    fixed_column: int
    direction_step: int
    parameter_diameter: int
    maximum_product_residual: int
    maximum_affine_defect: int
    maximum_exact_defect_bound: Fraction
    every_exact_bound_is_subunit: bool
    witness_graph_is_affine: bool


def witness_interpolation_certificate(
    *,
    q: int,
    hard_window_radius: int,
    fixed_column: int,
    samples: Sequence[tuple[int, int, int]],
) -> WitnessInterpolationCertificate:
    """Replay the moderate-direction projected-witness lift exactly.

    No divisibility assumption on ``q^3/(8*b)`` is made: it is retained as
    a :class:`Fraction`.  Sparse parameter sets are allowed.
    """

    if q <= 0 or hard_window_radius < 0 or fixed_column <= 0:
        raise ValueError("q, D, and the fixed column must be valid")
    frozen = tuple(sorted(samples))
    if len(frozen) < 3 or len({item[0] for item in frozen}) != len(frozen):
        raise ValueError("interpolation needs at least three distinct parameters")
    if any(min(x, d) <= 0 for _t, x, d in frozen):
        raise ValueError("witnesses and projected colors must be positive")

    first_t, _first_x, first_d = frozen[0]
    second_t, _second_x, second_d = frozen[1]
    parameter_gap = second_t - first_t
    color_gap = second_d - first_d
    if color_gap % parameter_gap:
        raise ValueError("the projected colors do not have an integral line step")
    step = color_gap // parameter_gap
    if step == 0:
        raise ValueError("the selected projected coordinate must vary")
    intercept = first_d - step * first_t
    if any(d != intercept + step * t for t, _x, d in frozen):
        raise ValueError("the projected colors are not on the declared affine line")

    target = q**3
    residuals = tuple(
        8 * fixed_column * x * d - target for _t, x, d in frozen
    )
    maximum_residual = max(abs(value) for value in residuals)
    if maximum_residual > q * hard_window_radius:
        raise ValueError("a witness lies outside the literal hard window")

    reciprocal_center = Fraction(target, 8 * fixed_column)
    errors = {
        t: Fraction(x) - reciprocal_center / d for t, x, d in frozen
    }
    maximum_defect = 0
    maximum_bound = Fraction(0)
    all_subunit = True
    for first_index in range(len(frozen) - 2):
        for middle_index in range(first_index + 1, len(frozen) - 1):
            for last_index in range(middle_index + 1, len(frozen)):
                t0, x0, d0 = frozen[first_index]
                t1, x1, d1 = frozen[middle_index]
                t2, x2, d2 = frozen[last_index]
                first_gap = t1 - t0
                second_gap = t2 - t1
                total_gap = t2 - t0
                defect = second_gap * x0 + first_gap * x2 - total_gap * x1
                main_term = (
                    reciprocal_center
                    * step**2
                    * first_gap
                    * second_gap
                    * total_gap
                    / (d0 * d1 * d2)
                )
                error_term = (
                    second_gap * errors[t0]
                    + first_gap * errors[t2]
                    - total_gap * errors[t1]
                )
                if Fraction(defect) != main_term + error_term:
                    raise AssertionError("the reciprocal interpolation identity failed")
                exact_bound = abs(main_term) + (
                    second_gap * abs(errors[t0])
                    + first_gap * abs(errors[t2])
                    + total_gap * abs(errors[t1])
                )
                if abs(defect) > exact_bound:
                    raise AssertionError("the exact interpolation bound failed")
                maximum_defect = max(maximum_defect, abs(defect))
                maximum_bound = max(maximum_bound, exact_bound)
                all_subunit = all_subunit and exact_bound < 1
                if exact_bound < 1 and defect:
                    raise AssertionError("a subunit integer interpolation defect is nonzero")

    graph_anchor_t, graph_anchor_x, _ = frozen[0]
    graph_rank = _rational_rank(
        ((t - graph_anchor_t, x - graph_anchor_x) for t, x, _d in frozen[1:])
    )
    return WitnessInterpolationCertificate(
        q=q,
        hard_window_radius=hard_window_radius,
        fixed_column=fixed_column,
        direction_step=step,
        parameter_diameter=frozen[-1][0] - frozen[0][0],
        maximum_product_residual=maximum_residual,
        maximum_affine_defect=maximum_defect,
        maximum_exact_defect_bound=maximum_bound,
        every_exact_bound_is_subunit=all_subunit,
        witness_graph_is_affine=graph_rank <= 1,
    )


@dataclass(frozen=True)
class TransverseLinePairCertificate:
    """Exact mixed-difference bound for two projected affine lines."""

    left_population: int
    right_population: int
    left_parameter_span: int
    right_parameter_span: int
    direction_cross_form: int
    cross_determinant_cap: int
    mixed_difference: int
    population_product: int
    population_ceiling: int


def _affine_line_parameters(points: Sequence[Vector2]) -> tuple[Vector2, tuple[int, ...]]:
    support = tuple(points)
    if len(support) < 2 or len(set(support)) != len(support):
        raise ValueError("an affine-line arm needs at least two distinct points")
    direction = _primitive_direction(support[0], support[1])
    parameters: list[int] = []
    for point in support:
        dx = point[0] - support[0][0]
        dy = point[1] - support[0][1]
        if direction[0]:
            if dx % direction[0]:
                raise ValueError("a point is not integral on the affine line")
            parameter = dx // direction[0]
            if dy != parameter * direction[1]:
                raise ValueError("the supplied points are not collinear")
        else:
            if direction[1] == 0 or dy % direction[1]:
                raise ValueError("a point is not integral on the affine line")
            parameter = dy // direction[1]
            if dx:
                raise ValueError("the supplied points are not collinear")
        parameters.append(parameter)
    return direction, tuple(parameters)


def transverse_line_pair_certificate(
    left: Sequence[Vector2], right: Sequence[Vector2]
) -> TransverseLinePairCertificate:
    """Bound a full Cartesian pair of nonparallel projected lines.

    Write the arms as ``u(t)=u0+t*p`` and ``v(s)=v0+s*r``.  The alternating
    difference of the four corner cross forms at the parameter extrema is

        F(t0,s0)-F(t0,s1)-F(t1,s0)+F(t1,s1)
        = F(p,r) (t1-t0) (s1-s0).

    If ``F(p,r)`` is a nonzero integer and every Cartesian value has size at
    most ``K``, then both arms having at least two points implies

        |U| |V| <= 8 K / |F(p,r)| + 2 <= 8 K + 2.

    Hence a two-rich-line obstruction can survive only in the parallel-null
    branch ``F(p,r)=0``.
    """

    left_set = tuple(left)
    right_set = tuple(right)
    left_direction, left_parameters = _affine_line_parameters(left_set)
    right_direction, right_parameters = _affine_line_parameters(right_set)
    eta = cross_form(left_direction, right_direction)
    if eta == 0:
        raise ValueError("the two projected directions are cross-form null")
    left_min, left_max = min(left_parameters), max(left_parameters)
    right_min, right_max = min(right_parameters), max(right_parameters)
    left_span = left_max - left_min
    right_span = right_max - right_min
    left_extrema = (
        (
            left_set[0][0] + left_min * left_direction[0],
            left_set[0][1] + left_min * left_direction[1],
        ),
        (
            left_set[0][0] + left_max * left_direction[0],
            left_set[0][1] + left_max * left_direction[1],
        ),
    )
    right_extrema = (
        (
            right_set[0][0] + right_min * right_direction[0],
            right_set[0][1] + right_min * right_direction[1],
        ),
        (
            right_set[0][0] + right_max * right_direction[0],
            right_set[0][1] + right_max * right_direction[1],
        ),
    )
    corner_values = tuple(
        cross_form(u, v) for u in left_extrema for v in right_extrema
    )
    mixed = corner_values[0] - corner_values[1] - corner_values[2] + corner_values[3]
    expected = eta * left_span * right_span
    if mixed != expected:
        raise AssertionError("the affine mixed-difference identity failed")
    cross_cap = max(abs(cross_form(u, v)) for u in left_set for v in right_set)
    if abs(mixed) > 4 * cross_cap:
        raise AssertionError("the four-corner determinant-strip bound failed")
    product = len(left_set) * len(right_set)
    ceiling = (8 * cross_cap) // abs(eta) + 2
    if product > ceiling:
        raise AssertionError("the transverse line-pair population bound failed")
    return TransverseLinePairCertificate(
        left_population=len(left_set),
        right_population=len(right_set),
        left_parameter_span=left_span,
        right_parameter_span=right_span,
        direction_cross_form=eta,
        cross_determinant_cap=cross_cap,
        mixed_difference=mixed,
        population_product=product,
        population_ceiling=ceiling,
    )


def projected_line_lift_audit(
    *,
    q: int,
    hard_window_radius: int,
    center: Vector2,
    neighbors: Sequence[tuple[int, int, int]],
) -> ProjectedLineLiftAudit:
    """Audit the invalid implication projected line => physical plane.

    ``neighbors`` contains ``(x,d,D)``.  Both triples ``(x,b,d)`` and
    ``(x,B,D)`` must lie in the literal hard product window, all projected
    pairs must be distinct and collinear, and at least three are required.
    The returned exact ranks distinguish the automatic homogeneous product
    lift from an affine lift of the original triples.
    """

    if q <= 0 or hard_window_radius < 0:
        raise ValueError("q and the hard-window radius must be valid")
    if len(neighbors) < 3:
        raise ValueError("a projected rich-line audit needs at least three points")
    b, big_b = center
    if min(b, big_b) <= 0 or any(min(item) <= 0 for item in neighbors):
        raise ValueError("physical coordinates must be positive")
    projected = tuple((d, big_d) for _x, d, big_d in neighbors)
    if len(set(projected)) != len(projected):
        raise ValueError("projected neighbors must be distinct")

    direction = _primitive_direction(projected[0], projected[1])
    direction_x, direction_y = direction
    coefficient_a = direction_y
    coefficient_b = -direction_x
    coefficient_c = -(
        coefficient_a * projected[0][0] + coefficient_b * projected[0][1]
    )
    if any(
        coefficient_a * d + coefficient_b * big_d + coefficient_c
        for d, big_d in projected
    ):
        raise ValueError("the projected neighbors are not collinear")

    target = q**3
    residuals = tuple(
        residual
        for x, d, big_d in neighbors
        for residual in (
            8 * x * b * d - target,
            8 * x * big_b * big_d - target,
        )
    )
    maximum_residual = max(abs(value) for value in residuals)
    if maximum_residual > q * hard_window_radius:
        raise ValueError("a supplied triple lies outside the hard window")

    tokens = tuple(b * d - big_b * big_d for _x, d, big_d in neighbors)
    graph_anchor = neighbors[0]
    graph_differences = tuple(
        (x - graph_anchor[0], d - graph_anchor[1], big_d - graph_anchor[2])
        for x, d, big_d in neighbors[1:]
    )
    witness_rank = _rational_rank(graph_differences)

    lifted = tuple((x * d, x * big_d, x) for x, d, big_d in neighbors)
    lift_rank = _rational_rank(lifted)
    if lift_rank > 2:
        raise AssertionError("the automatic homogeneous product plane failed")

    original_triples = tuple(
        triple
        for x, d, big_d in neighbors
        for triple in ((x, b, d), (x, big_b, big_d))
    )
    triple_anchor = original_triples[0]
    triple_differences = tuple(
        tuple(point[index] - triple_anchor[index] for index in range(3))
        for point in original_triples[1:]
    )
    original_rank = _rational_rank(triple_differences)
    return ProjectedLineLiftAudit(
        q=q,
        hard_window_radius=hard_window_radius,
        center=center,
        projected_line_equation=(coefficient_a, coefficient_b, coefficient_c),
        neighbor_count=len(neighbors),
        determinant_tokens=tokens,
        maximum_product_residual=maximum_residual,
        witness_graph_affine_rank=witness_rank,
        product_lift_linear_rank=lift_rank,
        original_triple_affine_rank=original_rank,
    )


def cartesian_line_spread_certificate(
    left: Sequence[Vector2], right: Sequence[Vector2]
) -> CartesianLineSpreadCertificate:
    """Replay the line-spread theorem on one literal Cartesian product."""

    left_set = tuple(left)
    right_set = tuple(right)
    if not left_set or not right_set:
        raise ValueError("both determinant-strip arms must be nonempty")
    if len(set(left_set)) != len(left_set) or len(set(right_set)) != len(right_set):
        raise ValueError("determinant-strip arms must be sets")
    if any(point == (0, 0) for point in (*left_set, *right_set)):
        raise ValueError("the line-spread theorem requires nonzero vectors")

    cross_cap = max(
        abs(cross_form(u, v)) for u in left_set for v in right_set
    )
    left_delta = maximum_pair_determinant(left_set)
    right_delta = maximum_pair_determinant(right_set)
    plucker_product = left_delta * right_delta
    plucker_ceiling = 2 * cross_cap * cross_cap
    if plucker_product > plucker_ceiling:
        raise AssertionError("bilinear Pluecker determinant control failed")

    left_lines = maximum_affine_line_occupancy(left_set)
    right_lines = maximum_affine_line_occupancy(right_set)
    left_ceiling = lattice_line_spread_ceiling(left_delta, left_lines)
    right_ceiling = lattice_line_spread_ceiling(right_delta, right_lines)
    if len(left_set) > left_ceiling or len(right_set) > right_ceiling:
        raise AssertionError("the lattice line-spread population bound failed")

    population_product = len(left_set) * len(right_set)
    universal = (
        162
        * max(1, cross_cap)
        * left_lines
        * right_lines
    )
    if population_product > universal:
        raise AssertionError("the Cartesian line-spread theorem failed")
    return CartesianLineSpreadCertificate(
        left_population=len(left_set),
        right_population=len(right_set),
        cross_determinant_cap=cross_cap,
        left_maximum_determinant=left_delta,
        right_maximum_determinant=right_delta,
        plucker_product=plucker_product,
        plucker_ceiling=plucker_ceiling,
        left_maximum_line_occupancy=left_lines,
        right_maximum_line_occupancy=right_lines,
        left_line_spread_ceiling=left_ceiling,
        right_line_spread_ceiling=right_ceiling,
        population_product=population_product,
        universal_population_ceiling=universal,
    )
