"""Exact ledgers for the narrow-token and anchored row-sum gate.

This module records finite identities only.  In particular, it does not
assert the open anchored codegree-Carleson estimate described in the
matching research note.

The Cramer convention is

``delta = det(p,q), k = det(p,u), r = det(u,q)``.

It gives ``delta*u = r*p+k*q`` and, for two physical vectors,

``det((k1,r1),(k2,r2)) = -delta*det(u1,u2)``.

If ``u`` is primitive, ``gcd(k,r)`` divides ``delta``.  These facts show
that the token plane retains, rather than improves, the physical
determinant scale.

For a bipartite incidence ``T``, the neighbor-degree sum at a right vertex
``gamma`` is exactly the L1 mass of its anchored codegree profile:

``sum_(p~gamma) deg(p) = sum_eta codeg(gamma,eta)``.

This is the exact positive row-sum left after the rank-one Cauchy step.
"""

from __future__ import annotations

from collections import defaultdict
from math import gcd
from typing import Hashable, Iterable, Mapping, Sequence


Vector = tuple[int, int]
Edge = tuple[Hashable, Hashable]


def determinant(first: Vector, second: Vector) -> int:
    """Return the oriented two-dimensional determinant."""

    return first[0] * second[1] - first[1] * second[0]


def cramer_token(p: Vector, q: Vector, u: Vector) -> tuple[int, int]:
    """Return ``(det(p,u),det(u,q))`` and check Cramer reconstruction."""

    delta = determinant(p, q)
    if delta == 0:
        raise ValueError("the Cramer base must be independent")
    k = determinant(p, u)
    r = determinant(u, q)
    if (delta * u[0], delta * u[1]) != (
        r * p[0] + k * q[0],
        r * p[1] + k * q[1],
    ):
        raise AssertionError("Cramer reconstruction failed")
    return k, r


def primitive_token_content(p: Vector, q: Vector, u: Vector) -> int:
    """Return the token content and verify that it divides the base minor.

    The assertion uses only ``gcd(u_1,u_2)=1``.  Indeed the token content
    divides both coordinates of ``delta*u`` by Cramer reconstruction, and
    Bezout then makes it divide ``delta``.
    """

    if gcd(abs(u[0]), abs(u[1])) != 1:
        raise ValueError("the physical vector must be primitive")
    delta = determinant(p, q)
    k, r = cramer_token(p, q, u)
    content = gcd(abs(k), abs(r))
    if content == 0:
        # A primitive u cannot have both tokens zero when delta is nonzero.
        raise AssertionError("an independent base produced the zero token")
    if delta % content:
        raise AssertionError("primitive token content did not divide delta")
    return content


def token_pair_determinant(
    p: Vector, q: Vector, first: Vector, second: Vector
) -> int:
    """Return and verify the exact token/physical area transference."""

    delta = determinant(p, q)
    first_token = cramer_token(p, q, first)
    second_token = cramer_token(p, q, second)
    token_area = determinant(first_token, second_token)
    expected = -delta * determinant(first, second)
    if token_area != expected:
        raise AssertionError("token determinant transference failed")
    return token_area


def two_anchor_integral_ceiling(
    first: Vector, second: Vector, cap: int
) -> int:
    """The elementary two-anchor population ceiling in the full Z^2 box.

    It counts the possible integer vectors ``v`` satisfying
    ``|det(first,v)|,|det(second,v)| <= cap``.  It deliberately does not
    claim sharpness after imposing the reciprocal mask.
    """

    if cap < 0:
        raise ValueError("the determinant cap must be nonnegative")
    content = gcd(abs(first[0]), abs(first[1]))
    area = abs(determinant(first, second))
    if content == 0 or area == 0:
        raise ValueError("the first anchor and the anchor pair must be nonzero")
    return (2 * (cap // content) + 1) * (2 * cap * content // area + 1)


def physical_two_anchor_floor(delta: int, D: int, internal_minor: int, content: int) -> int:
    """Verify the two-anchor ceiling is never a target-scale saving.

    In the physical token range

    ``cap=|delta|D, area=|delta|*internal_minor``

    with ``1<=internal_minor<=D`` and ``content | delta``.  The returned
    ceiling is at least ``3*(2D+1)``.  Thus this lattice count alone cannot
    supply the needed opposite degree ``D/|U|`` for a nontrivial arm.
    """

    delta = abs(delta)
    if delta == 0 or D <= 0:
        raise ValueError("delta and D must be positive")
    if not 1 <= internal_minor <= D:
        raise ValueError("the internal physical minor must lie in [1,D]")
    if content <= 0 or delta % content:
        raise ValueError("the token content must be a positive divisor of delta")
    cap = delta * D
    area = delta * internal_minor
    ceiling = (2 * (cap // content) + 1) * (
        2 * cap * content // area + 1
    )
    if ceiling < 3 * (2 * D + 1):
        raise AssertionError("the exact physical lower floor failed")
    return ceiling


def incidence_degrees(edges: Iterable[Edge]) -> tuple[dict[Hashable, int], dict[Hashable, int]]:
    """Return left and right degrees of a simple bipartite incidence."""

    left_neighbors: defaultdict[Hashable, set[Hashable]] = defaultdict(set)
    right_neighbors: defaultdict[Hashable, set[Hashable]] = defaultdict(set)
    for left, right in edges:
        left_neighbors[left].add(right)
        right_neighbors[right].add(left)
    return (
        {vertex: len(neighbors) for vertex, neighbors in left_neighbors.items()},
        {vertex: len(neighbors) for vertex, neighbors in right_neighbors.items()},
    )


def neighbor_degree_sums(edges: Iterable[Edge]) -> dict[Hashable, int]:
    """Return ``W(gamma)=sum_(p~gamma) deg(p)``."""

    materialized = set(edges)
    left_degrees, _ = incidence_degrees(materialized)
    answer: defaultdict[Hashable, int] = defaultdict(int)
    for left, right in materialized:
        answer[right] += left_degrees[left]
    return dict(answer)


def anchored_codegrees(
    edges: Iterable[Edge], anchor: Hashable
) -> dict[Hashable, int]:
    """Return ``eta -> # {p:p~anchor and p~eta}`` including ``eta=anchor``."""

    materialized = set(edges)
    by_left: defaultdict[Hashable, set[Hashable]] = defaultdict(set)
    for left, right in materialized:
        by_left[left].add(right)
    answer: defaultdict[Hashable, int] = defaultdict(int)
    for neighbors in by_left.values():
        if anchor in neighbors:
            for right in neighbors:
                answer[right] += 1
    return dict(answer)


def verify_row_sum_codegree_identity(edges: Iterable[Edge], anchor: Hashable) -> int:
    """Verify ``W(anchor)=sum_eta codeg(anchor,eta)`` and return it."""

    materialized = set(edges)
    row_sum = neighbor_degree_sums(materialized).get(anchor, 0)
    codegree_sum = sum(anchored_codegrees(materialized, anchor).values())
    if row_sum != codegree_sum:
        raise AssertionError("neighbor-degree/codegree L1 identity failed")
    return row_sum


def weighted_ordered_pair_form(
    weights: Mapping[tuple[Hashable, Hashable], float],
    vector: Mapping[Hashable, float],
) -> float:
    """Evaluate ``sum_(c,C) W(c,C)x_c x_C`` for nonnegative data."""

    if any(value < 0 for value in weights.values()) or any(
        value < 0 for value in vector.values()
    ):
        raise ValueError("the copositive ledger requires nonnegative data")
    return sum(
        value * vector.get(first, 0.0) * vector.get(second, 0.0)
        for (first, second), value in weights.items()
    )


def max_weight_sufficiency_ratio(
    weights: Mapping[tuple[Hashable, Hashable], float],
    vector: Mapping[Hashable, float],
) -> float:
    """Return the ratio bounded above by ``max W`` in the WNDS inequality."""

    mass = sum(vector.values())
    if mass <= 0:
        return 0.0
    ratio = weighted_ordered_pair_form(weights, vector) / mass**2
    ceiling = max(weights.values(), default=0.0)
    if ratio > ceiling + 1e-12:
        raise AssertionError("positivity failed to imply max-weight sufficiency")
    return ratio


def determinant_layer_support_ceiling(cap: int) -> int:
    """The number of possible integral determinant labels ``|h|<=cap``."""

    if cap < 0:
        raise ValueError("the cap must be nonnegative")
    return 2 * cap + 1


def dyadic_codegree_profile(codegrees: Mapping[Hashable, int]) -> dict[int, int]:
    """Count positive codegrees in dyadic bins labelled by their lower edge."""

    profile: defaultdict[int, int] = defaultdict(int)
    for value in codegrees.values():
        if value <= 0:
            continue
        lower = 1 << (value.bit_length() - 1)
        profile[lower] += 1
    return dict(sorted(profile.items()))


def carleson_tail_constant(codegrees: Mapping[Hashable, int], D: int) -> float:
    """Return ``max_R R*#{codeg>=R}/D`` over dyadic ``R``.

    A uniform ``q^o(1)`` bound for this quantity is the open anchored
    codegree-Carleson theorem.  Dyadic summation would give the desired
    neighbor-degree row sum ``D q^o(1)``.
    """

    if D <= 0:
        raise ValueError("D must be positive")
    maximum = max(codegrees.values(), default=0)
    if maximum <= 0:
        return 0.0
    answer = 0.0
    threshold = 1
    values = tuple(codegrees.values())
    while threshold <= maximum:
        population = sum(value >= threshold for value in values)
        answer = max(answer, threshold * population / D)
        threshold *= 2
    return answer


def four_completion_remainders(
    a: int,
    x: int,
    anchor: Vector,
    partner: Vector,
) -> tuple[int, int, int]:
    """Return and verify the exact short-remainder compatibility identity.

    With ``anchor=(c,C)`` and ``partner=(d,D)``, set

    ``r=x*d-a*c, s=x*D-a*C, h=C*d-c*D``.

    Then ``x*h=C*r-c*s`` exactly.
    """

    c, other_c = anchor
    d, other_d = partner
    r = x * d - a * c
    s = x * other_d - a * other_c
    h = other_c * d - c * other_d
    if x * h != other_c * r - c * s:
        raise AssertionError("four-completion remainder identity failed")
    return r, s, h


def rich_codegree_population_bound(
    anchor_degree: int,
    pointwise_offdiagonal_codegree: int,
    richness: int,
) -> int:
    """The dependent-pair ceiling for rich anchored codegrees.

    If every two distinct left neighbors of the anchor have codegree at
    most ``B``, then

    ``#{eta != anchor: codeg(anchor,eta)>=R} R(R-1)
       <=H(H-1)B``.
    """

    if anchor_degree < 0 or pointwise_offdiagonal_codegree < 0:
        raise ValueError("degrees and codegrees must be nonnegative")
    if richness < 2:
        raise ValueError("the dependent-pair bound requires richness at least two")
    numerator = (
        anchor_degree
        * max(anchor_degree - 1, 0)
        * pointwise_offdiagonal_codegree
    )
    return numerator // (richness * (richness - 1))


def verify_rich_codegree_population_bound(
    edges: Iterable[Edge], anchor: Hashable, richness: int
) -> tuple[int, int]:
    """Verify the rich-codegree dependent-pair inequality on a graph."""

    if richness < 2:
        raise ValueError("richness must be at least two")
    materialized = set(edges)
    by_left: defaultdict[Hashable, set[Hashable]] = defaultdict(set)
    by_right: defaultdict[Hashable, set[Hashable]] = defaultdict(set)
    for left, right in materialized:
        by_left[left].add(right)
        by_right[right].add(left)
    anchor_neighbors = by_right.get(anchor, set())
    ordered_neighbors = tuple(anchor_neighbors)
    maximum_pair_codegree = 0
    for first in ordered_neighbors:
        for second in ordered_neighbors:
            if first != second:
                maximum_pair_codegree = max(
                    maximum_pair_codegree,
                    len(by_left[first] & by_left[second]),
                )
    profile = anchored_codegrees(materialized, anchor)
    population = sum(
        right != anchor and value >= richness
        for right, value in profile.items()
    )
    ceiling = rich_codegree_population_bound(
        len(anchor_neighbors), maximum_pair_codegree, richness
    )
    if population > ceiling:
        raise AssertionError("the rich-codegree dependent-pair bound failed")
    return population, ceiling


def complete_biclique(left_size: int, right_size: int) -> set[tuple[int, int]]:
    """Return a finite biclique used to replay the sharp affine tail profile."""

    if left_size < 0 or right_size < 0:
        raise ValueError("biclique sizes must be nonnegative")
    return {
        (left, right)
        for left in range(left_size)
        for right in range(right_size)
    }
