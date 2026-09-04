"""Exact resource ledger for a weighted norm-graph countermodel.

The construction is an abstract linear, symmetric triple system.  It obeys
the same vertex/color degree budgets as the QP carry hypergraph and has no
completed 3-by-3 row/carrier grid, but its flat rank-one four-cycle mass is
larger than the degree cap by a power.  It deliberately does not satisfy the
cubic short-product equations.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


FieldElement = tuple[int, int]
Vertex = tuple[FieldElement, int]


@dataclass(frozen=True)
class NormGraphResourceLedger:
    """Exact counts for the bipartite projective norm graph over ``F_q``."""

    field_order: int
    vertices_per_side: int
    vertex_degree: int
    colors: int
    color_degree: int
    degree_cap: int
    unordered_four_cycles: int
    ordered_four_cycle_mass: Fraction
    repeated_color_ordered_upper_bound: int
    generic_ordered_lower_bound: int
    generic_rank_one_mass_lower_bound: Fraction
    generic_mass_to_degree_cap: Fraction


def norm_graph_resource_ledger(field_order: int) -> NormGraphResourceLedger:
    """Return the exact symbolic count for the norm-graph construction.

    There are ``n=q^2(q-1)`` vertices on each side and ``Delta=q^2-1``
    colors.  Every color is a perfect matching, so its degree is ``n``.
    Pair codegrees are zero, ``q``, or ``q+1`` and give the exact C4 count

    ``q^3(q-1)(q^2-1)(q^2-3)/4``.

    The canonical color of an edge is ``A+B`` in ``F_(q^2)^*``.  Adjacent
    edge colors on a rectangle are distinct.  A union bound over the two
    possible opposite-color coincidences leaves at least
    ``q^3(q-3)`` flat weighted generic mass.
    """

    q = field_order
    if q <= 3 or q % 2 == 0:
        raise ValueError("the ledger requires an odd field order greater than three")
    n = q * q * (q - 1)
    delta = q * q - 1
    four_cycles = q**3 * (q - 1) * delta * (q * q - 3) // 4
    ordered = 4 * four_cycles
    repeated_upper = 2 * q**4 * delta * (q - 1)
    generic_lower = ordered - repeated_upper
    expected_generic = q**3 * (q - 3) * delta**2
    if generic_lower != expected_generic:
        raise AssertionError("generic rectangle count did not simplify correctly")
    generic_mass = Fraction(generic_lower, delta**2)
    return NormGraphResourceLedger(
        field_order=q,
        vertices_per_side=n,
        vertex_degree=delta,
        colors=delta,
        color_degree=n,
        degree_cap=n,
        unordered_four_cycles=four_cycles,
        ordered_four_cycle_mass=Fraction(ordered, delta**2),
        repeated_color_ordered_upper_bound=repeated_upper,
        generic_ordered_lower_bound=generic_lower,
        generic_rank_one_mass_lower_bound=generic_mass,
        generic_mass_to_degree_cap=generic_mass / n,
    )


def _add(left: FieldElement, right: FieldElement, prime: int) -> FieldElement:
    return ((left[0] + right[0]) % prime, (left[1] + right[1]) % prime)


def _norm(value: FieldElement, prime: int) -> int:
    """Norm in ``F_p[i]`` when ``p=3 mod 4``."""

    return (value[0] * value[0] + value[1] * value[1]) % prime


def norm_graph_neighbors(prime: int, vertex: Vertex) -> dict[Vertex, FieldElement]:
    """Build one neighbor/color dictionary for the concrete ``p=3 mod 4`` model.

    The left vertex is ``(A,a)``.  For every nonzero color ``C`` there is one
    right neighbor ``(C-A,N(C)/a)``.  The return value maps that neighbor to
    its canonical color ``C=A+B``.
    """

    if prime <= 3 or prime % 4 != 3:
        raise ValueError("the concrete pair model requires a prime congruent to 3 mod 4")
    (ax, ay), scalar = vertex
    if not 0 < scalar < prime:
        raise ValueError("the scalar coordinate must be nonzero modulo the prime")
    inverse = pow(scalar, -1, prime)
    answer: dict[Vertex, FieldElement] = {}
    for cx in range(prime):
        for cy in range(prime):
            color = (cx, cy)
            if color == (0, 0):
                continue
            neighbor = (
                ((cx - ax) % prime, (cy - ay) % prime),
                _norm(color, prime) * inverse % prime,
            )
            if neighbor[1] == 0:
                raise AssertionError("a nonzero extension element had zero norm")
            answer[neighbor] = color
    return answer


def norm_graph_vertices(prime: int) -> tuple[Vertex, ...]:
    """Return all vertices in ``F_(p^2) x F_p^*`` for a small replay."""

    if prime <= 3 or prime % 4 != 3:
        raise ValueError("the concrete pair model requires a prime congruent to 3 mod 4")
    return tuple(
        ((x, y), scalar)
        for x in range(prime)
        for y in range(prime)
        for scalar in range(1, prime)
    )

