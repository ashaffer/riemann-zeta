"""Finite replay and combinatorial ledgers for the QP four-cycle spectral gate.

The exact routines below verify the row-pair Gram factorization and its
common-column diagonal correction.  The scalar ledgers record the proved
restricted-color sparsity estimate.  They do not assert the missing uniform
``sqrt(D)`` local-degree theorem.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import heapq
import math
from typing import Iterable, Mapping


Triple = tuple[int, int, int]
Cell = tuple[int, int]
Pair = tuple[int, int]
Incidence = dict[Pair, dict[Pair, complex]]


@dataclass(frozen=True)
class DegreeLedger:
    """Absolute left/right degrees of the row-pair/color-pair incidence."""

    maximum_left: float
    maximum_right: float
    total_weight: float


@dataclass(frozen=True)
class RestrictedColorLedger:
    """Actual finite counts entering the restricted-color proof."""

    support_size: int
    triple_count: int
    incidence_count: int
    maximum_carrier_degree: int
    maximum_row_pair_degree: int
    row_degree_square_sum: int


@dataclass(frozen=True)
class TwoStepTransportLedger:
    """Exact residual transport through two carrier-labelled triples."""

    first_residual: int
    second_residual: int
    drift: int
    identity_left: int
    identity_right: int
    drift_left: int
    drift_right: int


@dataclass(frozen=True)
class ClosedWalkProductLedger:
    """Alternating products attached to one even closed coordinate walk."""

    residuals: tuple[int, ...]
    odd_carrier_product: int
    even_carrier_product: int
    odd_factor_product: int
    even_factor_product: int
    identity_left: int
    identity_right: int


@dataclass(frozen=True)
class FiveDistinctIncidenceSplit:
    """Carrier wedges split by whether all five node labels are distinct."""

    generic: Incidence
    exceptional: Incidence


@dataclass(frozen=True)
class ThreeByThreeRigidityLedger:
    """Determinant bounds in the completed ``3 x 3`` product-grid lemma."""

    determinant_upper_bound: int
    nonzero_color_lower_bound: int
    forces_zero_color_determinant: bool


@dataclass(frozen=True)
class FactorizationResourceLedger:
    """Resource audit for the tempting one-factorization construction.

    Reusing the same ``2D`` colors in ``R`` matching components, with ``T``
    row-pair clones per component, gives every color degree ``R*T``.  Thus
    the actual color-degree cap ``D`` forces its flat rank-one output to be
    at most ``D/4``.  This records why the construction is not an FC
    countermodel under the full hypotheses.
    """

    degree_cap: int
    matching_components: int
    clones_per_component: int
    colors: int
    left_vertices: int
    right_vertices: int
    incidence_edges: int
    fresh_carriers: int
    color_degree: int
    obeys_color_degree_cap: bool
    rank_one_output_squared: Fraction
    ratio_to_fc_scale: Fraction


def validate_pair_uniqueness(triples: Iterable[Triple]) -> None:
    """Raise if two coordinates fail to determine the third coordinate."""

    seen_ab: dict[Cell, int] = {}
    seen_ac: dict[Cell, int] = {}
    seen_bc: dict[Cell, int] = {}
    for a, b, c in triples:
        tests = (
            (seen_ab, (a, b), c),
            (seen_ac, (a, c), b),
            (seen_bc, (b, c), a),
        )
        for table, key, value in tests:
            previous = table.setdefault(key, value)
            if previous != value:
                raise ValueError("the triple system is not pair-unique")


def coefficient_matrix(
    triple_weights: Mapping[Triple, complex],
    color_weights: Mapping[int, complex],
) -> dict[Cell, complex]:
    """Return ``A_z(a,b)=sum_c z_c*kappa(a,b,c)``."""

    validate_pair_uniqueness(triple_weights)
    matrix: dict[Cell, complex] = defaultdict(complex)
    for (a, b, c), weight in triple_weights.items():
        matrix[a, b] += color_weights.get(c, 0.0) * weight
    return dict(matrix)


def row_pair_incidence(triple_weights: Mapping[Triple, complex]) -> Incidence:
    """Build the exact weighted incidence ``H``.

    Its left vertices are ordered distinct row pairs, its right vertices are
    ordered color pairs, and an ordered pair of triples sharing a carrier
    contributes ``conj(kappa_1)*kappa_2``.
    """

    validate_pair_uniqueness(triple_weights)
    by_carrier: dict[int, list[tuple[int, int, complex]]] = defaultdict(list)
    for (a, b, c), weight in triple_weights.items():
        by_carrier[b].append((a, c, weight))

    incidence: dict[Pair, dict[Pair, complex]] = defaultdict(
        lambda: defaultdict(complex)
    )
    seen_edges: set[tuple[Pair, Pair]] = set()
    for entries in by_carrier.values():
        for a, c, weight in entries:
            for other_a, other_c, other_weight in entries:
                if a == other_a:
                    continue
                left = (a, other_a)
                right = (c, other_c)
                edge = (left, right)
                if edge in seen_edges:
                    raise ValueError("one incidence has more than one carrier")
                seen_edges.add(edge)
                incidence[left][right] += weight.conjugate() * other_weight
    return {left: dict(row) for left, row in incidence.items()}


def split_five_distinct_incidence(
    triple_weights: Mapping[Triple, complex],
) -> FiveDistinctIncidenceSplit:
    """Split ``H`` into all-five-distinct and repeated-node wedges.

    A wedge consists of ``(a,b,c)`` and ``(a',b,c')``.  It is generic when
    ``a,a',b,c,c'`` are pairwise distinct.  This routine retains the exact
    weighted incidence and rejects a repeated incidence carrier just as
    :func:`row_pair_incidence` does.
    """

    validate_pair_uniqueness(triple_weights)
    by_carrier: dict[int, list[tuple[int, int, complex]]] = defaultdict(list)
    for (a, b, c), weight in triple_weights.items():
        by_carrier[b].append((a, c, weight))

    generic: dict[Pair, dict[Pair, complex]] = defaultdict(
        lambda: defaultdict(complex)
    )
    exceptional: dict[Pair, dict[Pair, complex]] = defaultdict(
        lambda: defaultdict(complex)
    )
    seen_edges: set[tuple[Pair, Pair]] = set()
    for carrier, entries in by_carrier.items():
        for a, c, weight in entries:
            for other_a, other_c, other_weight in entries:
                if a == other_a:
                    continue
                left = (a, other_a)
                right = (c, other_c)
                edge = (left, right)
                if edge in seen_edges:
                    raise ValueError("one incidence has more than one carrier")
                seen_edges.add(edge)
                target = (
                    generic
                    if len({a, other_a, carrier, c, other_c}) == 5
                    else exceptional
                )
                target[left][right] += weight.conjugate() * other_weight

    return FiveDistinctIncidenceSplit(
        generic={left: dict(row) for left, row in generic.items()},
        exceptional={left: dict(row) for left, row in exceptional.items()},
    )


def row_pair_gram(matrix: Mapping[Cell, complex]) -> dict[Pair, complex]:
    """Return all nonzero ordered distinct-row Gram entries."""

    by_column: dict[int, list[tuple[int, complex]]] = defaultdict(list)
    for (a, b), value in matrix.items():
        if value:
            by_column[b].append((a, value))
    gram: dict[Pair, complex] = defaultdict(complex)
    for entries in by_column.values():
        for a, value in entries:
            for other_a, other_value in entries:
                if a != other_a:
                    gram[a, other_a] += value.conjugate() * other_value
    return dict(gram)


def apply_incidence(
    incidence: Mapping[Pair, Mapping[Pair, complex]],
    color_weights: Mapping[int, complex],
) -> dict[Pair, complex]:
    """Apply ``H`` to ``conjugate(z) tensor z``."""

    answer: dict[Pair, complex] = {}
    for left, row in incidence.items():
        answer[left] = sum(
            value
            * color_weights.get(c, 0.0).conjugate()
            * color_weights.get(other_c, 0.0)
            for (c, other_c), value in row.items()
        )
    return answer


def common_column_diagonal_mass(matrix: Mapping[Cell, complex]) -> float:
    """Return the ``a!=a', b=b'`` part of the fourth trace."""

    by_column: dict[int, list[float]] = defaultdict(list)
    for (_, b), value in matrix.items():
        if value:
            by_column[b].append(abs(value) ** 2)
    return sum(
        sum(values) ** 2 - sum(value**2 for value in values)
        for values in by_column.values()
    )


def nondegenerate_four_cycle(matrix: Mapping[Cell, complex]) -> float:
    """Return the signed nondegenerate fourth-cycle sum via the Gram identity."""

    gram_square = sum(abs(value) ** 2 for value in row_pair_gram(matrix).values())
    return gram_square - common_column_diagonal_mass(matrix)


def degree_ledger(incidence: Mapping[Pair, Mapping[Pair, complex]]) -> DegreeLedger:
    """Return the absolute Schur degrees and total absolute edge weight."""

    left_degrees = {
        left: sum(abs(value) for value in row.values())
        for left, row in incidence.items()
    }
    right_degrees: dict[Pair, float] = defaultdict(float)
    for row in incidence.values():
        for right, value in row.items():
            right_degrees[right] += abs(value)
    return DegreeLedger(
        maximum_left=max(left_degrees.values(), default=0.0),
        maximum_right=max(right_degrees.values(), default=0.0),
        total_weight=sum(left_degrees.values()),
    )


def support_graph_degeneracy(
    incidence: Mapping[Pair, Mapping[Pair, complex]],
) -> int:
    """Return the degeneracy of the unweighted bipartite support graph."""

    adjacency: dict[tuple[str, Pair], set[tuple[str, Pair]]] = defaultdict(set)
    for left, row in incidence.items():
        left_vertex = ("L", left)
        adjacency.setdefault(left_vertex, set())
        for right, value in row.items():
            if not value:
                continue
            right_vertex = ("R", right)
            adjacency[left_vertex].add(right_vertex)
            adjacency[right_vertex].add(left_vertex)

    degrees = {vertex: len(neighbors) for vertex, neighbors in adjacency.items()}
    heap = [(degree, vertex) for vertex, degree in degrees.items()]
    heapq.heapify(heap)
    removed: set[tuple[str, Pair]] = set()
    degeneracy = 0
    while heap:
        degree, vertex = heapq.heappop(heap)
        if vertex in removed or degree != degrees[vertex]:
            continue
        removed.add(vertex)
        degeneracy = max(degeneracy, degree)
        for neighbor in adjacency[vertex]:
            if neighbor not in removed:
                degrees[neighbor] -= 1
                heapq.heappush(heap, (degrees[neighbor], neighbor))
    return degeneracy


def degeneracy_operator_bound(maximum_degree: float, degeneracy: int) -> float:
    """Return the oriented-Schur bound ``2*sqrt(kappa*Delta)``."""

    if maximum_degree < 0 or degeneracy < 0:
        raise ValueError("degree parameters must be nonnegative")
    return 2 * math.sqrt(maximum_degree * degeneracy)


def two_step_transport_ledger(
    center: int,
    first_node: int,
    first_carrier: int,
    middle_node: int,
    second_carrier: int,
    last_node: int,
    *,
    multiplier: int = 8,
) -> TwoStepTransportLedger:
    """Replay the exact two-step near-dilation identity.

    If the two triples are ``(x,b,c)`` and ``(c,d,y)``, write
    ``Q+r=m*x*b*c`` and ``Q+s=m*c*d*y``.  Cancelling the middle node gives

    ``d*y*(Q+r) = b*x*(Q+s)``

    and hence

    ``(d*y-b*x)*(Q+r) = b*x*(s-r)``.

    No inequality or asymptotic assertion is encoded in this finite replay.
    """

    if center <= 0 or multiplier <= 0:
        raise ValueError("center and multiplier must be positive")
    values = (
        first_node,
        first_carrier,
        middle_node,
        second_carrier,
        last_node,
    )
    if any(value <= 0 for value in values):
        raise ValueError("walk labels must be positive")
    first_residual = (
        multiplier * first_node * first_carrier * middle_node - center
    )
    second_residual = (
        multiplier * middle_node * second_carrier * last_node - center
    )
    drift = second_carrier * last_node - first_carrier * first_node
    return TwoStepTransportLedger(
        first_residual=first_residual,
        second_residual=second_residual,
        drift=drift,
        identity_left=(
            second_carrier * last_node * (center + first_residual)
        ),
        identity_right=(
            first_carrier * first_node * (center + second_residual)
        ),
        drift_left=drift * (center + first_residual),
        drift_right=(
            first_carrier
            * first_node
            * (second_residual - first_residual)
        ),
    )


def closed_walk_product_ledger(
    center: int,
    nodes: Iterable[int],
    carriers: Iterable[int],
    *,
    multiplier: int = 8,
) -> ClosedWalkProductLedger:
    """Replay the alternating-product identity for an even closed walk.

    For edges ``(x_(j-1), b_j, x_j)`` put
    ``Q+r_j=m*x_(j-1)*b_j*x_j``.  Odd and even edges each contain every
    node of the closed walk exactly once, so

    ``prod_odd(b_j) / prod_even(b_j)``

    equals the corresponding ratio of the ``Q+r_j`` factors.  The returned
    cross-products are exact integers.  Importantly, the identity does not
    assert equality of the two carrier products.
    """

    node_tuple = tuple(nodes)
    carrier_tuple = tuple(carriers)
    if center <= 0 or multiplier <= 0:
        raise ValueError("center and multiplier must be positive")
    if not carrier_tuple or len(carrier_tuple) % 2:
        raise ValueError("a closed walk must have positive even length")
    if len(node_tuple) != len(carrier_tuple) + 1:
        raise ValueError("nodes must list both endpoints of every edge")
    if node_tuple[0] != node_tuple[-1]:
        raise ValueError("the coordinate walk is not closed")
    if any(value <= 0 for value in node_tuple + carrier_tuple):
        raise ValueError("walk labels must be positive")

    residuals = tuple(
        multiplier * node_tuple[index] * carrier * node_tuple[index + 1]
        - center
        for index, carrier in enumerate(carrier_tuple)
    )
    odd_carriers = math.prod(carrier_tuple[0::2])
    even_carriers = math.prod(carrier_tuple[1::2])
    odd_factors = math.prod(center + residual for residual in residuals[0::2])
    even_factors = math.prod(center + residual for residual in residuals[1::2])
    return ClosedWalkProductLedger(
        residuals=residuals,
        odd_carrier_product=odd_carriers,
        even_carrier_product=even_carriers,
        odd_factor_product=odd_factors,
        even_factor_product=even_factors,
        identity_left=odd_factors * even_carriers,
        identity_right=even_factors * odd_carriers,
    )


def determinant_three(matrix: Iterable[Iterable[int]]) -> int:
    """Return the exact determinant of a ``3 x 3`` integer matrix."""

    rows = tuple(tuple(row) for row in matrix)
    if len(rows) != 3 or any(len(row) != 3 for row in rows):
        raise ValueError("the matrix must be 3 x 3")
    (a, b, c), (d, e, f), (g, h, i) = rows
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def completed_grid_determinant_identity(
    row_nodes: Iterable[int],
    carrier_nodes: Iterable[int],
    colors: Iterable[Iterable[int]],
    *,
    multiplier: int = 8,
) -> tuple[int, int]:
    """Return both exact sides of ``det(N)=m^3 prod(a_i b_j) det(C)``."""

    rows = tuple(row_nodes)
    carriers = tuple(carrier_nodes)
    color_matrix = tuple(tuple(row) for row in colors)
    if len(rows) != 3 or len(carriers) != 3:
        raise ValueError("three row nodes and three carriers are required")
    if any(value <= 0 for value in rows + carriers) or multiplier <= 0:
        raise ValueError("nodes and multiplier must be positive")
    if len(color_matrix) != 3 or any(len(row) != 3 for row in color_matrix):
        raise ValueError("the color matrix must be 3 x 3")
    product_matrix = tuple(
        tuple(
            multiplier * rows[i] * carriers[j] * color_matrix[i][j]
            for j in range(3)
        )
        for i in range(3)
    )
    left = determinant_three(product_matrix)
    right = (
        multiplier**3
        * math.prod(rows)
        * math.prod(carriers)
        * determinant_three(color_matrix)
    )
    return left, right


def three_by_three_rigidity_ledger(
    center: int,
    residual_bound: int,
    shell_minimum: int,
    *,
    multiplier: int = 8,
) -> ThreeByThreeRigidityLedger:
    """Return the sufficient determinant-zero test for a completed grid.

    If every entry of ``N=Q*J+R`` has ``|R_ij|<=H``, expansion of the
    determinant shows ``|det(N)|<=18*Q*H^2+6*H^3``.  If also
    ``N_ij=m*a_i*b_j*c_ij`` and every row/carrier node is at least ``L``, a
    nonzero integral ``det(C)`` would give
    ``|det(N)|>=m^3*L^6``.  Strict separation of these two bounds therefore
    forces ``det(C)=0``.
    """

    if center <= 0 or shell_minimum <= 0 or multiplier <= 0:
        raise ValueError("center, shell minimum, and multiplier must be positive")
    if residual_bound < 0:
        raise ValueError("the residual bound must be nonnegative")
    upper = 18 * center * residual_bound**2 + 6 * residual_bound**3
    lower = multiplier**3 * shell_minimum**6
    return ThreeByThreeRigidityLedger(
        determinant_upper_bound=upper,
        nonzero_color_lower_bound=lower,
        forces_zero_color_determinant=upper < lower,
    )


def factorization_resource_ledger(
    degree_cap: int,
    matching_components: int,
    clones_per_component: int,
) -> FactorizationResourceLedger:
    """Audit the node/color budget in a one-factorization block family.

    Every component uses one perfect matching on the same ``2D`` colors and
    joins each of its ``T`` private row-pair clones to all ``D`` matching
    pairs.  With a fresh carrier per incidence the construction is linear
    and grid-free, but each color occurs once for every clone in every
    component.  For the flat vector on the ``2D`` colors, each left output
    is ``1/2`` and hence the squared output is ``R*T/4``.
    """

    if degree_cap <= 0:
        raise ValueError("the degree cap must be positive")
    if matching_components <= 0 or matching_components > 2 * degree_cap - 1:
        raise ValueError("invalid number of one-factorization components")
    if clones_per_component <= 0:
        raise ValueError("the clone count must be positive")
    left_vertices = matching_components * clones_per_component
    right_vertices = matching_components * degree_cap
    incidences = left_vertices * degree_cap
    color_degree = matching_components * clones_per_component
    output_squared = Fraction(left_vertices, 4)
    return FactorizationResourceLedger(
        degree_cap=degree_cap,
        matching_components=matching_components,
        clones_per_component=clones_per_component,
        colors=2 * degree_cap,
        left_vertices=left_vertices,
        right_vertices=right_vertices,
        incidence_edges=incidences,
        fresh_carriers=incidences,
        color_degree=color_degree,
        obeys_color_degree_cap=color_degree <= degree_cap,
        rank_one_output_squared=output_squared,
        ratio_to_fc_scale=output_squared / degree_cap,
    )


def restricted_color_ledger(
    triples: Iterable[Triple], colors: Iterable[int]
) -> RestrictedColorLedger:
    """Count the incidences induced by a specified color support."""

    triple_set = tuple(triples)
    validate_pair_uniqueness(triple_set)
    color_set = set(colors)
    by_carrier: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for a, b, c in triple_set:
        if c in color_set:
            by_carrier[b].append((a, c))

    row_degrees: dict[Pair, int] = defaultdict(int)
    incidence_count = 0
    for entries in by_carrier.values():
        incidence_count += len(entries) * (len(entries) - 1)
        for a, _ in entries:
            for other_a, _ in entries:
                if a != other_a:
                    row_degrees[a, other_a] += 1

    return RestrictedColorLedger(
        support_size=len(color_set),
        triple_count=sum(map(len, by_carrier.values())),
        incidence_count=incidence_count,
        maximum_carrier_degree=max(map(len, by_carrier.values()), default=0),
        maximum_row_pair_degree=max(row_degrees.values(), default=0),
        row_degree_square_sum=sum(value**2 for value in row_degrees.values()),
    )


def restricted_combinatorial_bounds(support_size: int, degree_cap: int) -> dict[str, int]:
    """Return the proved support-sensitive incidence bounds.

    The hypotheses are: every supported color occurs in at most ``D``
    triples, every carrier contains at most ``D`` triples, and the triple
    system is pair-unique.  Here ``M=support_size`` and ``D=degree_cap``.
    """

    if support_size < 0 or degree_cap < 0:
        raise ValueError("support size and degree cap must be nonnegative")
    local_cap = min(support_size, degree_cap)
    return {
        "triple_count": support_size * degree_cap,
        "incidence_count": support_size * degree_cap * local_cap,
        "maximum_carrier_degree": local_cap,
        "maximum_row_pair_degree": local_cap,
        "row_degree_square_sum": support_size * degree_cap * local_cap**2,
    }


def weighted_restricted_gram_bound(
    support_size: int, degree_cap: int, coefficient_maximum: float
) -> float:
    """Bound ``||H(conj(z) tensor z)||_2^2`` on a color support."""

    if coefficient_maximum < 0:
        raise ValueError("the coefficient maximum must be nonnegative")
    square_sum = restricted_combinatorial_bounds(
        support_size, degree_cap
    )["row_degree_square_sum"]
    return coefficient_maximum**4 * square_sum


def fourth_norm_gram_bound(degree_cap: int, fourth_power_sum: float) -> float:
    """Return the participation-ratio bound ``D^3 sum_c |z_c|^4``.

    Besides pair uniqueness, this uses the same cap ``D`` for a row-pair
    degree, a carrier degree, and a one-color triple degree.
    """

    if degree_cap < 0 or fourth_power_sum < 0:
        raise ValueError("the degree cap and fourth-power sum must be nonnegative")
    return degree_cap**3 * fourth_power_sum


def fourth_norm_fc_threshold(degree_cap: int) -> float:
    """Return the sufficient unit-vector threshold ``sum |z_c|^4<=D^-2``."""

    if degree_cap <= 0:
        raise ValueError("the degree cap must be positive")
    return degree_cap**-2


def uniform_support_gram_bound(support_size: int, degree_cap: int) -> float:
    """Specialize the weighted bound to ``|z_c|=M^(-1/2)``."""

    if support_size <= 0:
        raise ValueError("a uniform support must be nonempty")
    return weighted_restricted_gram_bound(
        support_size, degree_cap, support_size ** -0.5
    )


def flat_fc_threshold(degree_cap: int) -> int:
    """Return the sufficient uniform-support threshold ``M>=D^2``."""

    if degree_cap < 0:
        raise ValueError("the degree cap must be nonnegative")
    return degree_cap**2


def weighted_multiplicity_cauchy_bound(
    weighted_second_moment: float, weighted_color_mass: float
) -> float:
    """Cauchy bound for ``sum_C m(C) w(C)`` with measure ``w(C)``.

    The two inputs are ``sum_C m(C)^2 w(C)`` and ``sum_C w(C)``.
    This is the exact closure mechanism for the proposed fixed-color
    multiplicity second moment; it does not assert that the first input has
    the required arithmetic bound.
    """

    if weighted_second_moment < 0 or weighted_color_mass < 0:
        raise ValueError("weighted moments must be nonnegative")
    return math.sqrt(weighted_second_moment * weighted_color_mass)


def active_exponent_ledger() -> dict[str, Fraction]:
    """Return exact exponents for the active ``D=q^(16/33+o(1))`` scale."""

    d = Fraction(16, 33)
    shell = Fraction(1, 1)
    return {
        "D": d,
        "D_squared": 2 * d,
        "mean_degree": 2 * d - shell,
        "flat_full_gram": 3 * d - shell,
        "flat_full_saving_from_D": shell - 2 * d,
        "uniform_support_threshold": 2 * d,
    }


def kloosterman_active_range_ledger() -> dict[str, Fraction]:
    """Return exact active exponents in the bilinear-Kloosterman audits."""

    d = Fraction(16, 33)
    half_d = d / 2
    return {
        "D": d,
        "mohammadi_D_box_product_margin": 2 * d - Fraction(1, 2),
        "mohammadi_sqrt_D_box_product_deficit": Fraction(1, 2) - d,
        "mqw_balanced_threshold_margin": d - Fraction(10, 21),
        "mqw_first_term_saving": d / 2 - Fraction(1, 6),
        "mqw_second_term_saving": Fraction(21, 50) * d - Fraction(1, 5),
        "mqw_third_term_saving": Fraction(3, 8) * d - Fraction(11, 64),
        "mqw_sqrt_D_first_term_growth": Fraction(1, 6) - half_d / 2,
        "bp_balanced_threshold_margin": d - Fraction(13, 28),
        "bp_first_term_saving": Fraction(7, 8) * d - Fraction(13, 32),
        "bp_second_term_saving": Fraction(11, 16) * d - Fraction(5, 16),
        "bp_third_term_saving": d / 3 - Fraction(1, 9),
        "bp_saving_over_sqrt_shortfall": (
            Fraction(7, 8) * d - Fraction(13, 32) - Fraction(1, 66)
        ),
    }
