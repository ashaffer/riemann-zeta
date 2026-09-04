"""The selected-support K_(3,2) gate for residual QP blocks.

Put an edge ``x--y`` in the selected support graph when the unique
completion of ``{x,y}`` belongs to the coefficient support.  A high Walsh
fibre is then contained in a high-codegree pair of this graph.

This module records two exact facts.

* The usual K_(3,2) double count exchanges endpoint-pair codegrees with
  pairs of common endpoints of a pivot triple.
* In the scalar QP product window, all common endpoints of three fixed
  pivots lie in one primitive short-relation plane.  If its primitive
  normal has height ``H``, their number is ``O(D/H)``.

The second fact does not by itself aggregate the relation labels.  The
exponent ledger at the end records the exact missing saving: at support
``M=D^(15/8)`` and codegree ``T=D^(7/8)``, a reciprocal-height argument
must save at least ``D^(1/4)`` over the trivial anchored triple count merely
to match the elementary codegree first moment.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb, gcd
from typing import Sequence


Triple = tuple[int, int, int]


def _cross(left: Sequence[int], right: Sequence[int]) -> Triple:
    if len(left) != 3 or len(right) != 3:
        raise ValueError("the cross product requires two triples")
    return (
        int(left[1]) * int(right[2]) - int(left[2]) * int(right[1]),
        int(left[2]) * int(right[0]) - int(left[0]) * int(right[2]),
        int(left[0]) * int(right[1]) - int(left[1]) * int(right[0]),
    )


def _dot(left: Sequence[int], right: Sequence[int]) -> int:
    if len(left) != 3 or len(right) != 3:
        raise ValueError("the dot product requires two triples")
    return sum(int(x) * int(y) for x, y in zip(left, right, strict=True))


def _content(vector: Sequence[int]) -> int:
    answer = 0
    for value in vector:
        answer = gcd(answer, abs(int(value)))
    return answer


def _primitive(vector: Sequence[int]) -> tuple[Triple, int]:
    values = tuple(int(value) for value in vector)
    divisor = _content(values)
    if divisor == 0:
        raise ValueError("the zero vector has no primitive direction")
    primitive = tuple(value // divisor for value in values)
    first = next(value for value in primitive if value)
    if first < 0:
        primitive = tuple(-value for value in primitive)
        divisor = -divisor
    return primitive, divisor  # type: ignore[return-value]


@dataclass(frozen=True)
class ScalarThreePivotLedger:
    """One exact scalar-QP common-endpoint height certificate."""

    q: int
    degree_scale: int
    pivots: Triple
    endpoints: tuple[int, ...]
    completion_vectors: tuple[Triple, ...]
    maximum_absolute_residual: int
    universal_cross_product_bound: int
    observed_cross_product_bound: int
    primitive_normal: Triple
    primitive_height: int
    normal_multipliers: tuple[int, ...]
    common_endpoint_upper_bound: int
    short_orthogonal_collinearity_certified: bool


def scalar_qp_three_pivot_ledger(
    q: int,
    degree_scale: int,
    pivots: Sequence[int],
    endpoints: Sequence[int],
    completion_vectors: Sequence[Sequence[int]],
    *,
    shell_minimum: int,
    shell_maximum: int,
) -> ScalarThreePivotLedger:
    """Certify the three-pivot common-endpoint height lemma.

    For every endpoint ``x`` and pivot ``p_i`` the supplied completion
    ``a_i(x)`` must satisfy

    ``|8*p_i*x*a_i(x)-q^3| <= q*D``.

    Actual prime-power shell vectors are primitive and coordinatewise
    injective; these two consequences are checked directly here.  Put
    ``a=a(x_0)``.  For every other endpoint ``y``, subtraction of product
    residuals gives a vector ``e=x_0*a-y*a(y)`` of size at most
    ``qD/(4*shell_minimum)``.  Hence

    ``a cross a(y)=-(a cross e)/y``

    has sup norm at most

    ``W=floor(shell_maximum*q*D/(2*shell_minimum^2))``.

    If ``2*W^2<shell_minimum``, any two such integral normals are
    collinear: their cross product is an integral multiple of the primitive
    positive vector ``a`` but is too short to be nonzero.  If ``h_0`` is
    the common primitive normal and ``H=||h_0||_infinity``, distinct common
    endpoints give distinct nonzero multipliers of ``h_0``.  Therefore

    ``t_3 <= 1+2*floor(W/H)``.
    """

    modulus = int(q)
    degree = int(degree_scale)
    lower = int(shell_minimum)
    upper = int(shell_maximum)
    pivot_tuple = tuple(int(value) for value in pivots)
    endpoint_tuple = tuple(int(value) for value in endpoints)
    vectors = tuple(tuple(int(value) for value in row) for row in completion_vectors)
    if modulus <= 0 or degree <= 0:
        raise ValueError("q and the degree scale must be positive")
    if lower <= 0 or upper < lower or upper - lower >= lower:
        raise ValueError("the shell must have diameter smaller than its minimum")
    if len(pivot_tuple) != 3 or len(set(pivot_tuple)) != 3:
        raise ValueError("three distinct pivots are required")
    if len(endpoint_tuple) < 2 or len(set(endpoint_tuple)) != len(endpoint_tuple):
        raise ValueError("at least two distinct common endpoints are required")
    if len(vectors) != len(endpoint_tuple) or any(len(row) != 3 for row in vectors):
        raise ValueError("one completion triple is required per endpoint")
    if any(not lower <= value <= upper for value in pivot_tuple + endpoint_tuple):
        raise ValueError("a pivot or endpoint lies outside the shell")
    if set(pivot_tuple).intersection(endpoint_tuple):
        raise ValueError("pivots and common endpoints must be disjoint")
    if any(not lower <= value <= upper for row in vectors for value in row):
        raise ValueError("a completion lies outside the shell")
    if any(len(set(row)) != 3 for row in vectors):
        raise ValueError("each completion vector must have distinct coordinates")
    if any(
        gcd(row[first], row[second]) != 1
        for row in vectors
        for first, second in combinations(range(3), 2)
    ):
        raise ValueError("completion coordinates must be pairwise coprime")
    for coordinate in range(3):
        column = [row[coordinate] for row in vectors]
        if len(set(column)) != len(column):
            raise ValueError("completion coordinates must be endpoint-injective")
    for endpoint, row in zip(endpoint_tuple, vectors, strict=True):
        for pivot, completion in zip(pivot_tuple, row, strict=True):
            if len({endpoint, pivot, completion}) != 3:
                raise ValueError("every physical triple must have distinct nodes")

    residuals = tuple(
        8 * pivot * endpoint * completion - modulus**3
        for endpoint, row in zip(endpoint_tuple, vectors, strict=True)
        for pivot, completion in zip(pivot_tuple, row, strict=True)
    )
    maximum_residual = max(abs(value) for value in residuals)
    if maximum_residual > modulus * degree:
        raise ValueError("a supplied triple escapes the qD product window")

    universal_bound = (upper * modulus * degree) // (2 * lower * lower)
    if 2 * universal_bound * universal_bound >= lower:
        raise ValueError("the D^2<q short-orthogonal separation is not certified")

    base = vectors[0]
    normals = tuple(_cross(base, row) for row in vectors[1:])
    if any(normal == (0, 0, 0) for normal in normals):
        raise ValueError("distinct endpoints produced proportional completions")
    observed_bound = max(abs(value) for normal in normals for value in normal)
    if observed_bound > universal_bound:
        raise AssertionError("the residual-to-cross-product bound failed")
    primitive_normal, _ = _primitive(normals[0])
    height = max(abs(value) for value in primitive_normal)
    if any(value == 0 for value in primitive_normal):
        # If, say, h_3=0, pairwise coprimality forces the primitive pair
        # (h_1,h_2) to have height at least min(a_1,a_2)>W.
        raise AssertionError("a short relation normal has a zero coordinate")

    multipliers: list[int] = []
    pivot_coordinate = next(
        index for index, value in enumerate(primitive_normal) if value
    )
    for normal in normals:
        if _dot(normal, base):
            raise AssertionError("a cross product is not orthogonal to its base")
        cross_of_normals = _cross(normals[0], normal)
        if cross_of_normals != (0, 0, 0):
            raise AssertionError("short orthogonals failed to be collinear")
        numerator = normal[pivot_coordinate]
        denominator = primitive_normal[pivot_coordinate]
        if numerator % denominator:
            raise AssertionError("a normal is not an integral primitive multiple")
        multiplier = numerator // denominator
        if tuple(multiplier * value for value in primitive_normal) != normal:
            raise AssertionError("the primitive-normal reconstruction failed")
        multipliers.append(multiplier)
    if len(set(multipliers)) != len(multipliers) or any(value == 0 for value in multipliers):
        raise AssertionError("distinct endpoints did not give distinct multipliers")

    endpoint_cap = 1 + 2 * (universal_bound // height)
    if len(endpoint_tuple) > endpoint_cap:
        raise AssertionError("the three-pivot height cap failed")
    return ScalarThreePivotLedger(
        q=modulus,
        degree_scale=degree,
        pivots=pivot_tuple,  # type: ignore[arg-type]
        endpoints=endpoint_tuple,
        completion_vectors=vectors,  # type: ignore[arg-type]
        maximum_absolute_residual=maximum_residual,
        universal_cross_product_bound=universal_bound,
        observed_cross_product_bound=observed_bound,
        primitive_normal=primitive_normal,
        primitive_height=height,
        normal_multipliers=tuple(multipliers),
        common_endpoint_upper_bound=endpoint_cap,
        short_orthogonal_collinearity_certified=True,
    )


@dataclass(frozen=True)
class SupportGraphK23Ledger:
    """Exact codegrees and the K_(3,2) double count for one graph."""

    vertices: int
    edges: int
    maximum_degree: int
    threshold: int
    high_pair_count: int
    high_codegree_first_moment: int
    high_codegree_second_moment: int
    high_codegree_third_factorial_moment: int
    total_codegree_first_moment: int
    pivot_triple_pair_moment: int
    k23_identity_holds: bool


def support_graph_k23_ledger(
    adjacency: Sequence[Sequence[int]], threshold: int
) -> SupportGraphK23Ledger:
    """Return the exact K_(3,2) ledger of a finite simple graph.

    If ``mu_uv=|N(u) intersect N(v)|`` and
    ``t_3(X)=|intersection_(x in X) N(x)|``, then

    ``sum_(u<v) binom(mu_uv,3)=sum_(|X|=3) binom(t_3(X),2)``.
    """

    matrix = tuple(tuple(int(value) for value in row) for row in adjacency)
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("the adjacency matrix must be square")
    if any(value not in (0, 1) for row in matrix for value in row):
        raise ValueError("the adjacency matrix must be binary")
    if any(matrix[index][index] for index in range(size)):
        raise ValueError("the graph must have no loops")
    if any(matrix[i][j] != matrix[j][i] for i in range(size) for j in range(size)):
        raise ValueError("the graph must be undirected")
    cutoff = int(threshold)
    if cutoff < 3:
        raise ValueError("the third-factorial threshold must be at least three")

    neighborhoods = [
        {neighbor for neighbor, value in enumerate(row) if value}
        for row in matrix
    ]
    degrees = [len(neighborhood) for neighborhood in neighborhoods]
    codegrees = {
        pair: len(neighborhoods[pair[0]] & neighborhoods[pair[1]])
        for pair in combinations(range(size), 2)
    }
    high = [value for value in codegrees.values() if value >= cutoff]
    left = sum(comb(value, 3) for value in codegrees.values())
    right = sum(
        comb(len(neighborhoods[i] & neighborhoods[j] & neighborhoods[k]), 2)
        for i, j, k in combinations(range(size), 3)
    )
    if left != right:
        raise AssertionError("the K_(3,2) double count failed")
    return SupportGraphK23Ledger(
        vertices=size,
        edges=sum(degrees) // 2,
        maximum_degree=max(degrees, default=0),
        threshold=cutoff,
        high_pair_count=len(high),
        high_codegree_first_moment=sum(high),
        high_codegree_second_moment=sum(value * value for value in high),
        high_codegree_third_factorial_moment=sum(comb(value, 3) for value in high),
        total_codegree_first_moment=sum(codegrees.values()),
        pivot_triple_pair_moment=right,
        k23_identity_holds=True,
    )


@dataclass(frozen=True)
class RelationLabelLedger:
    """Raw three-dimensional normal-label count in a sup-norm ball."""

    radius: int
    nonzero_raw_labels: int
    raw_reciprocal_height_mass: Fraction


def _det2(left: Sequence[int], right: Sequence[int]) -> int:
    if len(left) != 2 or len(right) != 2:
        raise ValueError("det2 requires two pairs")
    return int(left[0]) * int(right[1]) - int(left[1]) * int(right[0])


def _divisor_count(value: int) -> int:
    target = abs(int(value))
    if target == 0:
        raise ValueError("zero has no finite divisor count")
    answer = 0
    divisor = 1
    while divisor * divisor <= target:
        if target % divisor == 0:
            answer += 1 if divisor * divisor == target else 2
        divisor += 1
    return answer


@dataclass(frozen=True)
class FixedPairHeightBinLedger:
    """Third rows in one primitive-cross-product height bin."""

    first_row: tuple[int, int]
    second_row: tuple[int, int]
    anchor_determinant: int
    height_lower_bound: int
    third_row_count: int
    contents: tuple[int, ...]
    primitive_heights: tuple[int, ...]
    second_row_determinants: tuple[int, ...]
    divisor_count: int
    fixed_determinant_injective: bool
    upper_bound: int


def fixed_pair_height_bin_ledger(
    first_row: Sequence[int],
    second_row: Sequence[int],
    third_rows: Sequence[Sequence[int]],
    height_lower_bound: int,
    *,
    shell_minimum: int,
    shell_maximum: int,
) -> FixedPairHeightBinLedger:
    r"""Certify the fixed-pair ``O(R*tau(delta))`` height-bin lemma.

    For primitive shell pairs ``p_y,p_z,p_w``, the raw cross product of the
    two coordinate triples is

    ``(det(p_z,p_w), det(p_w,p_y), det(p_y,p_z))``.

    If its content is ``g`` and its primitive height lies in ``[R,2R)``,
    then ``g`` divides the fixed nonzero determinant ``delta=det(p_y,p_z)``
    and ``det(p_z,p_w)/g`` has fewer than ``4R`` signed possibilities.
    A fixed determinant ``det(p_z,p_w)`` determines ``p_w``: two solutions
    differ by an integral multiple of primitive ``p_z``, which cannot fit
    inside a shell whose diameter is below its minimum.  Hence the bin has
    at most ``(4R-1)*tau(|delta|)`` rows.
    """

    first = tuple(int(value) for value in first_row)
    second = tuple(int(value) for value in second_row)
    rows = tuple(tuple(int(value) for value in row) for row in third_rows)
    lower = int(shell_minimum)
    upper = int(shell_maximum)
    scale = int(height_lower_bound)
    if len(first) != 2 or len(second) != 2 or any(len(row) != 2 for row in rows):
        raise ValueError("all rows must be integer pairs")
    if scale <= 0:
        raise ValueError("the height lower bound must be positive")
    if lower <= 0 or upper < lower or upper - lower >= lower:
        raise ValueError("the shell diameter must be below its minimum")
    all_rows = (first, second, *rows)
    if len(set(all_rows)) != len(all_rows):
        raise ValueError("all row pairs must be distinct")
    for row in all_rows:
        if any(not lower <= value <= upper for value in row):
            raise ValueError("a row coordinate lies outside the shell")
        if gcd(abs(row[0]), abs(row[1])) != 1:
            raise ValueError("every row pair must be primitive")

    anchor_determinant = _det2(first, second)
    if anchor_determinant == 0:
        raise ValueError("distinct primitive shell rows cannot be parallel")
    contents: list[int] = []
    heights: list[int] = []
    fixed_determinants: list[int] = []
    for row in rows:
        raw = (
            _det2(second, row),
            _det2(row, first),
            anchor_determinant,
        )
        content = _content(raw)
        if content == 0:
            raise AssertionError("a nonzero anchor determinant has zero content")
        height = max(abs(value) for value in raw) // content
        if not scale <= height < 2 * scale:
            raise ValueError("a third row lies outside the requested height bin")
        if anchor_determinant % content:
            raise AssertionError("the cross-product content does not divide the anchor")
        contents.append(content)
        heights.append(height)
        fixed_determinants.append(raw[0])
    injective = len(fixed_determinants) == len(set(fixed_determinants))
    if not injective:
        raise AssertionError("fixed determinant failed to determine the third shell row")
    divisor_count = _divisor_count(anchor_determinant)
    upper_bound = (4 * scale - 1) * divisor_count
    if len(rows) > upper_bound:
        raise AssertionError("the fixed-pair height-bin bound failed")
    return FixedPairHeightBinLedger(
        first_row=first,  # type: ignore[arg-type]
        second_row=second,  # type: ignore[arg-type]
        anchor_determinant=anchor_determinant,
        height_lower_bound=scale,
        third_row_count=len(rows),
        contents=tuple(contents),
        primitive_heights=tuple(heights),
        second_row_determinants=tuple(fixed_determinants),
        divisor_count=divisor_count,
        fixed_determinant_injective=True,
        upper_bound=upper_bound,
    )


@dataclass(frozen=True)
class HighPartnerExponentLedger:
    """Consequences of the fixed-pair ``t_3`` budget on one dyadic layer."""

    codegree: Fraction
    partner_count: Fraction
    weighted_uncompleted_tail: Fraction
    completed_trace: Fraction
    previous_uncompleted_tail: Fraction
    previous_completed_trace: Fraction
    desired_uncompleted_tail: Fraction
    desired_completed_trace: Fraction
    improvement_over_previous: Fraction
    remaining_trace_gap: Fraction
    square_root_degree_spectral_scale: Fraction
    spectral_saving_needed_from_schur: Fraction
    improves_previous_high_tail: bool
    proves_sharp_trace: bool
    packet_free_spectral_theorem_proved: bool


@dataclass(frozen=True)
class UniformSubsetPartnerSaturationLedger:
    """Exact method-saturator for the high-partner convexity argument."""

    scale: int
    rows: int
    subset_size: int
    row_degree: int
    pair_codegree: int
    triple_codegree: int
    high_partners_per_anchor: int
    fixed_pair_triple_sum: int
    partner_bound_scale: Fraction
    partner_to_bound_ratio: Fraction
    maximum_primitive_height: int
    triple_height_cap_certified: bool


def uniform_subset_partner_saturation(
    scale: int,
) -> UniformSubsetPartnerSaturationLedger:
    r"""Return an exact saturation model for ``L << D^2/H^2``.

    Put ``n=s^2`` and let the right vertices be all ``s``-subsets of an
    ``n``-element row set, with incidence given by membership.  Then

    ``D=C(n-1,s-1)``, ``H=C(n-2,s-2)``, ``t_3=C(n-3,s-3)``.

    Every pair of rows has codegree ``H`), so every anchor has ``n-1`` high
    partners.  Give row ``i`` the primitive shell pair
    ``p_i=(m+3i,m+3i+1)``.  The displayed coordinates are pairwise
    distinct across rows, and a triple ``i<j<k`` has primitive height
    ``(k-i)/gcd(j-i,k-j)<=n-1``.  The displayed ``t_3`` is at most
    ``D/(n-1)``, so the arithmetic height cap and the fixed-pair total
    ``sum_w t_3<=D`` both hold.  Finally

    ``D^2/H^2=(s+1)^2`` and ``L=s^2-1``,

    whose ratio tends to one.  The high-partner graph is complete, so its
    adjacency norm also equals ``L``.  This is not an actual QP product
    mask; it shows that the proved inequalities alone cannot improve the
    partner exponent.
    """

    parameter = int(scale)
    if parameter < 3:
        raise ValueError("the subset saturator needs scale at least three")
    rows = parameter * parameter
    subset = parameter
    degree = comb(rows - 1, subset - 1)
    pair = comb(rows - 2, subset - 2)
    triple = comb(rows - 3, subset - 3)
    partners = rows - 1
    triple_sum = (rows - 2) * triple
    partner_scale = Fraction(degree * degree, pair * pair)
    ratio = Fraction(partners, 1) / partner_scale
    height_cap = triple * (rows - 1) <= degree
    if triple_sum > degree:
        raise AssertionError("the fixed-pair triple sum escaped the degree budget")
    if not height_cap:
        raise AssertionError("the uniform-subset triple codegree escaped the height cap")
    return UniformSubsetPartnerSaturationLedger(
        scale=parameter,
        rows=rows,
        subset_size=subset,
        row_degree=degree,
        pair_codegree=pair,
        triple_codegree=triple,
        high_partners_per_anchor=partners,
        fixed_pair_triple_sum=triple_sum,
        partner_bound_scale=partner_scale,
        partner_to_bound_ratio=ratio,
        maximum_primitive_height=rows - 1,
        triple_height_cap_certified=True,
    )


def high_partner_exponent_ledger(codegree: Fraction) -> HighPartnerExponentLedger:
    r"""Return powers of ``D`` from ``L_H << D^2/H^2``.

    On a dyadic layer ``H=D^tau``, the graph of high partners has maximum
    degree ``D^(2-2*tau)``.  Schur on the pair-weight vector therefore gives
    the same exponent for the uncompleted weighted tail and exponent
    ``2-tau`` after multiplying by the completion multiplicity ``H``.

    The previous uniform direct theorem gives respectively
    ``D^(5/4-tau)`` and ``D^(5/4)``.  Thus the new estimate improves it
    exactly for ``tau>3/4``, but reaches the sharp completed exponent one
    only at ``tau=1``.
    """

    tau = Fraction(codegree)
    if tau < 0 or tau > 1:
        raise ValueError("the codegree exponent must lie in [0,1]")
    partner = 2 - 2 * tau
    completed = 2 - tau
    old_uncompleted = Fraction(5, 4) - tau
    improvement = max(Fraction(0), old_uncompleted - partner)
    return HighPartnerExponentLedger(
        codegree=tau,
        partner_count=partner,
        weighted_uncompleted_tail=partner,
        completed_trace=completed,
        previous_uncompleted_tail=old_uncompleted,
        previous_completed_trace=Fraction(5, 4),
        desired_uncompleted_tail=1 - tau,
        desired_completed_trace=Fraction(1),
        improvement_over_previous=improvement,
        remaining_trace_gap=max(Fraction(0), completed - 1),
        # H*sqrt(L_H), with L_H=D^(2-2*tau), is exactly D.
        square_root_degree_spectral_scale=Fraction(1),
        # Schur pays H*L_H=D^(2-tau), so the missing gain is sqrt(L_H).
        spectral_saving_needed_from_schur=max(Fraction(0), 1 - tau),
        improves_previous_high_tail=partner < old_uncompleted,
        proves_sharp_trace=completed <= 1,
        packet_free_spectral_theorem_proved=False,
    )


def relation_label_ledger(radius: int) -> RelationLabelLedger:
    """Count raw normal vectors before primitivity and sign quotienting.

    The shell ``||h||_infinity=r`` has exactly ``24*r^2+2`` integral
    vectors.  Hence the reciprocal label mass is

    ``sum_(r<=R) (24*r^2+2)/r = 12*R*(R+1)+2*H_R``.

    Primitive unoriented labels form a subset, so this is a safe exact
    union-bound budget.  Its order ``R^2`` explains why summing relation
    directions separately cannot supply the missing Carleson gain.
    """

    bound = int(radius)
    if bound < 1:
        raise ValueError("the label radius must be positive")
    reciprocal = sum(
        (Fraction(24 * height * height + 2, height) for height in range(1, bound + 1)),
        Fraction(0),
    )
    return RelationLabelLedger(
        radius=bound,
        nonzero_raw_labels=(2 * bound + 1) ** 3 - 1,
        raw_reciprocal_height_mass=reciprocal,
    )


@dataclass(frozen=True)
class CriticalK23ExponentLedger:
    """Power-of-D ledger for the selected-support K_(3,2) attempt."""

    support: Fraction
    codegree: Fraction
    reciprocal_saving: Fraction
    elementary_high_pair_bound: Fraction
    k23_high_pair_bound: Fraction
    k23_minus_elementary: Fraction
    dyadic_codegree_second_moment_bound: Fraction
    dyadic_carleson_second_moment_target: Fraction
    target_gap: Fraction
    saving_needed_to_match_elementary: Fraction
    saving_needed_for_carleson_layer: Fraction
    k23_improves_elementary: bool
    carleson_second_moment_closes: bool


def critical_k23_exponent_ledger(
    support: Fraction,
    codegree: Fraction,
    reciprocal_saving: Fraction = Fraction(0),
) -> CriticalK23ExponentLedger:
    """Return the exact stopping exponents for the K_(3,2) route.

    Write ``M=D^m``, ``T=D^tau``.  The support graph has ``E<<MD`` and
    maximum degree ``O(D)``, so the elementary first moment gives

    ``# {mu>=T} << M*D^2/T``.

    The anchored reciprocal-height mass is trivially ``O(MD^3)``.  If a
    theorem saves ``D^alpha`` from this, the three-pivot height lemma and
    the K_(3,2) identity give

    ``# {mu>=T} << M*D^(4-alpha)/T^3``.

    On a dyadic codegree layer ``T<=mu<2T``, the codegree second moment
    sufficient for the flat-bin Carleson estimate is ``O(D*M^2)``.  All
    returned values are its exact power exponents.  A further dyadic split
    is necessary because the effective Walsh multiplicity can be smaller
    than the raw codegree.
    """

    m = Fraction(support)
    tau = Fraction(codegree)
    alpha = Fraction(reciprocal_saving)
    elementary = m + 2 - tau
    k23 = m + 4 - alpha - 3 * tau
    second = k23 + 2 * tau
    target = 1 + 2 * m
    elementary_needed = max(Fraction(0), 2 - 2 * tau)
    carleson_needed = max(Fraction(0), 3 - tau - m)
    return CriticalK23ExponentLedger(
        support=m,
        codegree=tau,
        reciprocal_saving=alpha,
        elementary_high_pair_bound=elementary,
        k23_high_pair_bound=k23,
        k23_minus_elementary=k23 - elementary,
        dyadic_codegree_second_moment_bound=second,
        dyadic_carleson_second_moment_target=target,
        target_gap=second - target,
        saving_needed_to_match_elementary=elementary_needed,
        saving_needed_for_carleson_layer=carleson_needed,
        k23_improves_elementary=k23 < elementary,
        carleson_second_moment_closes=second <= target,
    )
