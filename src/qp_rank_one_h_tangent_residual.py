"""Exact tangent/residual split for the rank-one fourth-trace incidence.

This module is deliberately finite.  It preserves the original row-pair
coordinate (equivalently, after cyclically permuting the three factors, the
center-pair coordinate) and never groups row pairs by their sum.

For triples ``(a,b,c)`` define the transition incidence

``T[((b,b'),(c,c'))] = sum_a 1_(a,b,c) 1_(a,b',c')``.

Under physical pair uniqueness its entries are zero or one, and for
``xi_(c,c') = conj(z_c) z_c'`` one has

``||T xi||_2^2 = ||A_z||_S4^4``.

The split ``b*c == b'*c'`` is the exact multiplicative tangent.  The helper
routines below replay the split, the reduced-ratio parametrization, the
edgewise degree-product certificate for the residual graph, and exact small
hard-window diagnostics.  They do not assert the still-open uniform
residual degree-product theorem.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, lcm
from typing import Iterable, Mapping, Sequence


Triple = tuple[int, int, int]
Pair = tuple[int, int]
Transition = dict[tuple[Pair, Pair], int]


def determinant(first: Pair, second: Pair) -> int:
    """The oriented integral determinant of two ordered pairs."""

    return first[0] * second[1] - first[1] * second[0]


def endpoint_gcd_lcm_divisor(centers: Pair, colors: Pair) -> int:
    """Return the endpoint-gcd lcm, which always divides the determinant.

    If ``G=gcd(b,B)`` and ``H=gcd(c,C)``, then both ``G`` and ``H`` divide
    ``b*c-B*C``; hence so does ``lcm(G,H)``.  This exact divisibility can be
    vacuous: the physical affine extremizers have ``G=H=1``.
    """

    if min(*centers, *colors) <= 0:
        raise ValueError("coordinates must be positive")
    divisor = lcm(gcd(*centers), gcd(*colors))
    delta = centers[0] * colors[0] - centers[1] * colors[1]
    if delta % divisor:
        raise AssertionError("endpoint gcd lcm failed to divide determinant")
    return divisor


def literal_hard_window_triples(
    q: int, D: int, values: Sequence[int]
) -> tuple[Triple, ...]:
    """Enumerate ``|8abc-q^3|<=qD`` without a cubic search.

    The physical range used by the project has ``D<q`` and hence at most one
    selected third coordinate for a fixed pair.  The implementation still
    checks both adjacent quotients and rejects a failure of that uniqueness.
    """

    if q <= 0 or D < 0 or any(value <= 0 for value in values):
        raise ValueError("q and the coordinates must be positive, D nonnegative")
    allowed = set(values)
    triples: list[Triple] = []
    seen_ab: dict[tuple[int, int], int] = {}
    seen_ac: dict[tuple[int, int], int] = {}
    seen_bc: dict[tuple[int, int], int] = {}
    target = q**3
    for a in values:
        for b in values:
            denominator = 8 * a * b
            quotient = target // denominator
            selected = [
                c
                for c in {quotient, quotient + 1}
                if c in allowed and abs(denominator * c - target) <= q * D
            ]
            if len(selected) > 1:
                raise ValueError("the hard window is not pair-unique")
            if selected:
                c = selected[0]
                triples.append((a, b, c))
                if (a, b) in seen_ab and seen_ab[a, b] != c:
                    raise ValueError("(a,b) does not determine c")
                if (a, c) in seen_ac and seen_ac[a, c] != b:
                    raise ValueError("(a,c) does not determine b")
                if (b, c) in seen_bc and seen_bc[b, c] != a:
                    raise ValueError("(b,c) does not determine a")
                seen_ab[a, b] = c
                seen_ac[a, c] = b
                seen_bc[b, c] = a
    return tuple(triples)


def transition_incidence(triples: Iterable[Triple]) -> Transition:
    """Build the exact center-pair/color-pair incidence with row witnesses."""

    by_row: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    seen_cells: set[tuple[int, int, int]] = set()
    for a, b, c in triples:
        if (a, b, c) in seen_cells:
            raise ValueError("a triple was repeated")
        seen_cells.add((a, b, c))
        by_row[a].append((b, c))

    answer: Transition = {}
    for entries in by_row.values():
        for b, c in entries:
            for other_b, other_c in entries:
                key = ((b, other_b), (c, other_c))
                if key in answer:
                    raise ValueError("one transition has two row witnesses")
                answer[key] = 1
    return answer


def transition_witnesses(triples: Iterable[Triple]) -> dict[tuple[Pair, Pair], int]:
    """As :func:`transition_incidence`, retaining the unique common row."""

    by_row: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for a, b, c in triples:
        by_row[a].append((b, c))
    answer: dict[tuple[Pair, Pair], int] = {}
    for a, entries in by_row.items():
        for b, c in entries:
            for other_b, other_c in entries:
                key = ((b, other_b), (c, other_c))
                if key in answer:
                    raise ValueError("one transition has two row witnesses")
                answer[key] = a
    return answer


def split_tangent_residual(
    incidence: Mapping[tuple[Pair, Pair], int]
) -> tuple[Transition, Transition]:
    """Split by the exact determinant ``b*c-b'*c'``."""

    tangent: Transition = {}
    residual: Transition = {}
    for (centers, colors), value in incidence.items():
        target = (
            tangent
            if centers[0] * colors[0] == centers[1] * colors[1]
            else residual
        )
        target[(centers, colors)] = int(value)
    return tangent, residual


def bipartite_degrees(
    incidence: Mapping[tuple[Pair, Pair], int]
) -> tuple[dict[Pair, int], dict[Pair, int]]:
    """Return exact left and right support degrees."""

    left: defaultdict[Pair, int] = defaultdict(int)
    right: defaultdict[Pair, int] = defaultdict(int)
    for (first, second), value in incidence.items():
        if value:
            left[first] += 1
            right[second] += 1
    return dict(left), dict(right)


def maximum_edge_degree_product(
    incidence: Mapping[tuple[Pair, Pair], int]
) -> tuple[int, tuple[Pair, Pair] | None]:
    """Return ``max_(edge xy) deg(x)deg(y)`` and a maximizing edge."""

    left, right = bipartite_degrees(incidence)
    if not incidence:
        return 0, None
    edge = max(
        incidence,
        key=lambda item: left[item[0]] * right[item[1]],
    )
    return left[edge[0]] * right[edge[1]], edge


def edge_degree_spectral_ceiling(
    incidence: Mapping[tuple[Pair, Pair], int]
) -> int:
    """The squared spectral ceiling from the edge-degree theorem.

    For every finite bipartite graph ``G`` with biadjacency ``B``, Perron--
    Frobenius applied to the full adjacency matrix gives

    ``||B||^2 <= max_(xy in E(G)) deg(x)deg(y)``.

    This function returns the right side.  It is an exact certificate, not
    a numerical singular-value calculation.
    """

    return maximum_edge_degree_product(incidence)[0]


@dataclass(frozen=True)
class SharedEdgePalette:
    """Exact Cramer/Pluecker data around one residual transition edge.

    For the base edge ``((b,B),(c,C))`` use the oriented vectors

    ``p=(b,B), q=(C,c), u=(D,d), v=(e,E)``.

    Here ``(d,D)`` ranges over the full left neighborhood and ``(e,E)``
    over the full right neighborhood.  The two Cramer coordinates of a
    left vector are ``k=det(p,u), r=det(u,q)`` and those of a right vector
    are ``ell=det(v,q), t=det(p,v)``.  They obey, for every Cartesian pair,

    ``delta*det(u,v) = r*t-k*ell``.

    Thus this object preserves the original transition coordinate and does
    not assert that a Cartesian cross pair is itself a transition edge.
    """

    base_edge: tuple[Pair, Pair]
    base_determinant: int
    left_degree: int
    right_degree: int
    left_cramer_coordinates: tuple[tuple[Pair, int, int], ...]
    right_cramer_coordinates: tuple[tuple[Pair, int, int], ...]
    cross_determinant_multiplicities: tuple[tuple[int, int], ...]


def shared_edge_palette(
    incidence: Mapping[tuple[Pair, Pair], int],
    edge: tuple[Pair, Pair],
) -> SharedEdgePalette:
    """Return and internally verify the exact shared-edge transference.

    The cross palette counts all ``left_degree * right_degree`` pairs, not
    merely the edges present in ``incidence``.  Consequently it is the
    correct finite diagnostic for a proposed Cartesian determinant inverse
    theorem behind the residual degree-product gate.
    """

    if not incidence.get(edge, 0):
        raise ValueError("the selected base pair is not an incidence edge")
    centers, colors = edge
    b, other_b = centers
    c, other_c = colors
    p = centers
    q_vector = (other_c, c)
    delta = determinant(p, q_vector)
    if delta == 0:
        raise ValueError("shared-edge residual transference requires delta != 0")

    left_colors = sorted(
        candidate_colors
        for (candidate_centers, candidate_colors), value in incidence.items()
        if value and candidate_centers == centers
    )
    right_centers = sorted(
        candidate_centers
        for (candidate_centers, candidate_colors), value in incidence.items()
        if value and candidate_colors == colors
    )

    left_data: list[tuple[Pair, int, int]] = []
    for d, other_d in left_colors:
        u = (other_d, d)
        k = determinant(p, u)
        r = determinant(u, q_vector)
        if (delta * u[0], delta * u[1]) != (
            r * p[0] + k * q_vector[0],
            r * p[1] + k * q_vector[1],
        ):
            raise AssertionError("left Cramer reconstruction failed")
        left_data.append(((d, other_d), k, r))

    right_data: list[tuple[Pair, int, int]] = []
    for e, other_e in right_centers:
        v = (e, other_e)
        ell = determinant(v, q_vector)
        t = determinant(p, v)
        if (delta * v[0], delta * v[1]) != (
            ell * p[0] + t * q_vector[0],
            ell * p[1] + t * q_vector[1],
        ):
            raise AssertionError("right Cramer reconstruction failed")
        right_data.append(((e, other_e), ell, t))

    multiplicities: defaultdict[int, int] = defaultdict(int)
    for (left_pair, k, r) in left_data:
        d, other_d = left_pair
        u = (other_d, d)
        for (right_pair, ell, t) in right_data:
            v = right_pair
            cross = determinant(u, v)
            if delta * cross != r * t - k * ell:
                raise AssertionError("shared-edge Pluecker identity failed")
            multiplicities[cross] += 1

    return SharedEdgePalette(
        base_edge=edge,
        base_determinant=delta,
        left_degree=len(left_data),
        right_degree=len(right_data),
        left_cramer_coordinates=tuple(left_data),
        right_cramer_coordinates=tuple(right_data),
        cross_determinant_multiplicities=tuple(sorted(multiplicities.items())),
    )


@dataclass(frozen=True)
class SharedEdgeProductLedger:
    """The exact physical-error ledger giving the cross determinant bound."""

    base_determinant: int
    cross_determinant: int
    left_first_error: int
    left_second_error: int
    right_first_error: int
    right_second_error: int
    scaled_cross_determinant: int
    expanded_ledger: int


def shared_edge_product_ledger(
    base_row: int,
    centers: Pair,
    colors: Pair,
    left_row: int,
    left_colors: Pair,
    right_row: int,
    right_centers: Pair,
) -> SharedEdgeProductLedger:
    """Verify the exact product-error identity for a left/right cross pair.

    The intended input consists of the base triples
    ``(a,b,c),(a,B,C)``, a left neighbor ``(x,b,d),(x,B,D)``, and a right
    neighbor ``(y,e,c),(y,E,C)``.  The identity itself is polynomial, so
    this routine does not need a window parameter.
    """

    a, x, y = base_row, left_row, right_row
    b, other_b = centers
    c, other_c = colors
    d, other_d = left_colors
    e, other_e = right_centers
    if min(a, x, y, b, other_b, c, other_c, d, other_d, e, other_e) <= 0:
        raise ValueError("all physical coordinates must be positive")

    left_first = x * d - a * c
    left_second = x * other_d - a * other_c
    right_first = y * e - a * b
    right_second = y * other_e - a * other_b
    delta = b * c - other_b * other_c
    cross = d * e - other_d * other_e
    expanded = (
        a * a * delta
        + a * c * right_first
        + a * b * left_first
        + left_first * right_first
        - a * other_c * right_second
        - a * other_b * left_second
        - left_second * right_second
    )
    scaled = x * y * cross
    if scaled != expanded:
        raise AssertionError("shared-edge product ledger failed")
    return SharedEdgeProductLedger(
        base_determinant=delta,
        cross_determinant=cross,
        left_first_error=left_first,
        left_second_error=left_second,
        right_first_error=right_first,
        right_second_error=right_second,
        scaled_cross_determinant=scaled,
        expanded_ledger=expanded,
    )


def shared_edge_cross_determinant_ceiling(
    q: int, D: int, shell_minimum: int, shell_maximum: int
) -> int:
    """A rigorous shell-uniform ceiling for every physical cross determinant.

    Assume all eleven coordinates in :func:`shared_edge_product_ledger` lie
    in ``[shell_minimum,shell_maximum]`` and all six displayed triples obey
    ``|8uvw-q^3|<=qD``.  Pairwise subtraction bounds each comparison error
    and the base determinant by ``qD/(4*shell_minimum)``.  The exact ledger
    then gives the returned integer ceiling for ``|d*e-D*E|``.
    """

    if q <= 0 or D < 0 or shell_minimum <= 0 or shell_maximum < shell_minimum:
        raise ValueError("invalid window or shell parameters")
    first_order = Fraction(
        5 * shell_maximum**2 * q * D,
        4 * shell_minimum**3,
    )
    second_order = Fraction(q**2 * D**2, 8 * shell_minimum**4)
    bound = first_order + second_order
    return (bound.numerator + bound.denominator - 1) // bound.denominator


def opposite_token_population_ceiling(
    first_left_token: Pair,
    second_left_token: Pair,
    cross_cap: int,
) -> int:
    """Bound an opposite token arm from two independent left tokens.

    Tokens are ordered as ``(k,r)`` on the left and ``(ell,t)`` on the
    right, with cross form ``r*t-k*ell``.  If this form has magnitude at
    most ``cross_cap`` against both supplied left tokens, then the total
    number of distinct integral right tokens is at most the returned value.

    Put ``g=gcd(k_1,r_1)`` and
    ``Delta=|k_1*r_2-r_1*k_2|``.  The first cross token has at most
    ``2 floor(cross_cap/g)+1`` values.  In one such fiber, the second cross
    token advances in steps ``Delta/g``, giving the second factor below.
    This is a genuine broad-token sector bound; it is deliberately silent
    when the two anchors are collinear.
    """

    if cross_cap < 0:
        raise ValueError("the cross cap must be nonnegative")
    k1, r1 = first_left_token
    k2, r2 = second_left_token
    content = gcd(abs(k1), abs(r1))
    separation = abs(k1 * r2 - r1 * k2)
    if content == 0:
        raise ValueError("the first token must be nonzero")
    if separation == 0:
        raise ValueError("the two tokens must be linearly independent")
    level_count = 2 * (cross_cap // content) + 1
    fiber_count = (2 * cross_cap * content) // separation + 1
    return level_count * fiber_count


@dataclass(frozen=True)
class InverseStepTransference:
    """Exact modular-inverse transport across one residual base edge."""

    center_gap: int
    color_gap: int
    center_inverse_step: int
    color_inverse_step: int
    center_lift: int
    color_lift: int
    coupling_factor: int


def inverse_step_transference(centers: Pair, colors: Pair) -> InverseStepTransference:
    """Transport the two least-absolute signed gap inverses through ``delta``.

    With ``g=B-b``, ``h=c-C`` and ``delta=bc-BC``, choose

    ``g*U == -1 (mod b)``, ``h*V == -1 (mod C)``.

    Then exactly ``delta*U=C+b*r`` and ``delta*V=-b+C*s``.  This is the
    shared-edge reciprocal identity; it requires the indicated coprimality
    and is meaningful independently of any unproved degree estimate.
    """

    b, other_b = centers
    c, other_c = colors
    if min(b, other_b, c, other_c) <= 1:
        raise ValueError("moduli and coordinates must exceed one")
    g = other_b - b
    h = c - other_c
    if gcd(g, b) != 1 or gcd(h, other_c) != 1:
        raise ValueError("the signed gaps must be invertible in the two charts")
    U = (-pow(g % b, -1, b)) % b
    V = (-pow(h % other_c, -1, other_c)) % other_c
    if 2 * U > b:
        U -= b
    if 2 * V > other_c:
        V -= other_c
    delta = b * c - other_b * other_c
    if (delta * U - other_c) % b or (delta * V + b) % other_c:
        raise AssertionError("inverse-step transference congruence failed")
    center_lift = (delta * U - other_c) // b
    color_lift = (delta * V + b) // other_c
    coupling = 1 + center_lift * color_lift
    if b * coupling != delta * (color_lift * U - V):
        raise AssertionError("first inverse-lift coupling identity failed")
    if other_c * coupling != delta * (U + center_lift * V):
        raise AssertionError("second inverse-lift coupling identity failed")
    return InverseStepTransference(
        center_gap=g,
        color_gap=h,
        center_inverse_step=U,
        color_inverse_step=V,
        center_lift=center_lift,
        color_lift=color_lift,
        coupling_factor=coupling,
    )


def near_determinant_cartesian_countermodel(
    scale: int, length: int
) -> tuple[tuple[Pair, ...], tuple[Pair, ...]]:
    """A shell-local no-go for using the cross determinant band alone.

    The returned oriented vectors are

    ``u_i=(scale+i+1,scale+i)``, ``v_j=(scale+j+1,scale+j)``.

    Hence ``det(u_i,v_j)=j-i`` for all Cartesian pairs.  There are
    ``length^2`` pairs but their determinants have magnitude below
    ``length``.  These vectors are *not* asserted to be physical hard-window
    neighborhoods; the construction isolates precisely why the shared-edge
    determinant transference still needs the reciprocal product curves.
    """

    if scale <= 0 or length <= 0:
        raise ValueError("scale and length must be positive")
    vectors = tuple((scale + index + 1, scale + index) for index in range(length))
    return vectors, vectors


def apply_transition_rank_one(
    incidence: Mapping[tuple[Pair, Pair], int],
    z: Mapping[int, complex],
) -> dict[Pair, complex]:
    """Apply ``T`` to ``xi_(c,c')=conj(z_c)z_c'``."""

    answer: defaultdict[Pair, complex] = defaultdict(complex)
    for (centers, colors), value in incidence.items():
        answer[centers] += (
            value * z.get(colors[0], 0j).conjugate() * z.get(colors[1], 0j)
        )
    return dict(answer)


def rank_one_energy(
    incidence: Mapping[tuple[Pair, Pair], int],
    z: Mapping[int, complex],
) -> float:
    """Return ``||T(conj(z) tensor z)||_2^2``."""

    return float(sum(abs(value) ** 2 for value in apply_transition_rank_one(incidence, z).values()))


def direct_schatten_fourth(triples: Iterable[Triple], z: Mapping[int, complex]) -> float:
    """Compute the same fourth power directly from ``A_z(a,b)``."""

    matrix: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    rows: set[int] = set()
    centers: set[int] = set()
    for a, b, c in triples:
        matrix[a, b] += z.get(c, 0j)
        rows.add(a)
        centers.add(b)
    total = 0.0
    for b in centers:
        for other_b in centers:
            inner = sum(
                matrix[a, b].conjugate() * matrix[a, other_b] for a in rows
            )
            total += abs(inner) ** 2
    return float(total)


@dataclass(frozen=True)
class TangentCoordinates:
    gcd: int
    first_reduced_center: int
    second_reduced_center: int
    common_color_parameter: int


def tangent_coordinates(centers: Pair, colors: Pair) -> TangentCoordinates:
    """Return ``b=gu,b'=gv,c=vd,c'=ud`` on an exact tangent edge."""

    b, other_b = centers
    c, other_c = colors
    if min(b, other_b, c, other_c) <= 0:
        raise ValueError("coordinates must be positive")
    if b * c != other_b * other_c:
        raise ValueError("the edge is not tangent")
    common = gcd(b, other_b)
    u, v = b // common, other_b // common
    if c % v or other_c % u or c // v != other_c // u:
        raise AssertionError("coprime tangent parametrization failed")
    return TangentCoordinates(common, u, v, c // v)


def tangent_ratio_blocks(
    incidence: Mapping[tuple[Pair, Pair], int]
) -> dict[Pair, set[Pair]]:
    """Return tangent blocks ``(u,v) -> {(g,d)}``.

    The input must contain only tangent edges.  Repeated ``(g,d)`` in one
    reduced-ratio block would be the same physical transition and is
    rejected by the set representation.
    """

    answer: defaultdict[Pair, set[Pair]] = defaultdict(set)
    for (centers, colors), value in incidence.items():
        if not value:
            continue
        coordinates = tangent_coordinates(centers, colors)
        answer[
            (
                coordinates.first_reduced_center,
                coordinates.second_reduced_center,
            )
        ].add((coordinates.gcd, coordinates.common_color_parameter))
    return dict(answer)


def tangent_l1_certificate(
    incidence: Mapping[tuple[Pair, Pair], int],
    z: Mapping[int, complex],
) -> float:
    """Return the exact reduced-ratio ``l1`` upper bound for tangent energy.

    If ``R_(u,v)(g,d)`` is one tangent block and
    ``w_d=conj(z_(v*d))*z_(u*d)``, then

    ``||R w||_2^2 <= (max_d deg_R(d))*||w||_1^2``.

    Summing this expression over the disjoint reduced-ratio blocks gives the
    returned certificate.
    """

    total = 0.0
    for (u, v), edges in tangent_ratio_blocks(incidence).items():
        column_degrees: defaultdict[int, int] = defaultdict(int)
        active_d: set[int] = set()
        for _, d in edges:
            column_degrees[d] += 1
            active_d.add(d)
        maximum = max(column_degrees.values(), default=0)
        mass = sum(
            abs(z.get(v * d, 0j) * z.get(u * d, 0j)) for d in active_d
        )
        total += maximum * mass * mass
    return float(total)


def _affinely_collinear(points: Sequence[tuple[int, int, int]]) -> bool:
    """Whether all integer points lie on one affine line."""

    if len(points) <= 2:
        return True
    anchor = points[0]
    direction = tuple(points[1][i] - anchor[i] for i in range(3))
    for point in points[2:]:
        displacement = tuple(point[i] - anchor[i] for i in range(3))
        if any(
            direction[i] * displacement[j] != direction[j] * displacement[i]
            for i in range(3)
            for j in range(i + 1, 3)
        ):
            return False
    return True


def affine_packet_vertices(
    witnesses: Mapping[tuple[Pair, Pair], int], *, minimum_degree: int = 3
) -> tuple[set[Pair], set[Pair]]:
    """Detect exact affine row or column neighborhoods in the residual graph.

    A left neighborhood is represented by points ``(a,c,c')``; a right
    neighborhood by ``(a,b,b')``.  This is only a diagnostic peeling rule.
    """

    left_points: defaultdict[Pair, list[tuple[int, int, int]]] = defaultdict(list)
    right_points: defaultdict[Pair, list[tuple[int, int, int]]] = defaultdict(list)
    for (centers, colors), row in witnesses.items():
        left_points[centers].append((row, colors[0], colors[1]))
        right_points[colors].append((row, centers[0], centers[1]))
    left = {
        vertex
        for vertex, points in left_points.items()
        if len(points) >= minimum_degree and _affinely_collinear(sorted(points))
    }
    right = {
        vertex
        for vertex, points in right_points.items()
        if len(points) >= minimum_degree and _affinely_collinear(sorted(points))
    }
    return left, right


def peel_affine_packets(
    incidence: Mapping[tuple[Pair, Pair], int],
    witnesses: Mapping[tuple[Pair, Pair], int],
    *,
    minimum_degree: int = 3,
) -> Transition:
    """Delete edges incident to an exactly affine high-degree neighborhood."""

    left, right = affine_packet_vertices(witnesses, minimum_degree=minimum_degree)
    return {
        edge: int(value)
        for edge, value in incidence.items()
        if edge[0] not in left and edge[1] not in right
    }


@dataclass(frozen=True)
class HardWindowAudit:
    triples: int
    transition_edges: int
    tangent_edges: int
    residual_edges: int
    residual_edge_degree_product: int
    peeled_residual_edges: int
    peeled_edge_degree_product: int
    flat_total_energy: float
    flat_tangent_energy: float
    flat_residual_energy: float


def hard_window_audit(q: int, D: int, values: Sequence[int]) -> HardWindowAudit:
    """Return exact original-H diagnostics on one finite shell."""

    triples = literal_hard_window_triples(q, D, values)
    incidence = transition_incidence(triples)
    witnesses = transition_witnesses(triples)
    tangent, residual = split_tangent_residual(incidence)
    residual_witnesses = {edge: witnesses[edge] for edge in residual}
    peeled = peel_affine_packets(residual, residual_witnesses)
    norm = len(values) ** -0.5 if values else 0.0
    z = {value: complex(norm) for value in values}
    return HardWindowAudit(
        triples=len(triples),
        transition_edges=len(incidence),
        tangent_edges=len(tangent),
        residual_edges=len(residual),
        residual_edge_degree_product=maximum_edge_degree_product(residual)[0],
        peeled_residual_edges=len(peeled),
        peeled_edge_degree_product=maximum_edge_degree_product(peeled)[0],
        flat_total_energy=rank_one_energy(incidence, z),
        flat_tangent_energy=rank_one_energy(tangent, z),
        flat_residual_energy=rank_one_energy(residual, z),
    )
