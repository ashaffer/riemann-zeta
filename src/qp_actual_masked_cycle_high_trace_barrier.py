"""Exact ledgers for the masked-cycle/high-trace barrier.

The routines in this module separate two statements which are easy to
conflate:

* a cycle in the carrier--colour projection has an alternating *near*
  product identity for its edge labels;
* the stronger residual cancellation uses equality of the two alternating
  label products, which an unlabelled trace does not record.

The finite prime fixture is an exact actual-mask example.  The projective
plane ledger is deliberately only an incidence-category obstruction: it
matches the critical cardinalities, degrees, pair uniqueness, and centred
spectral excess, but not the cubic product window.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, exp, isqrt, log
from typing import Sequence


def is_prime(value: int) -> bool:
    """Return primality by deterministic trial division.

    The helper is used only for the five-digit fixture below.
    """

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


@dataclass(frozen=True)
class MaskedEdge:
    """One exact edge ``Q+r=8*a*b*c``."""

    label: int
    carrier: int
    colour: int
    residual: int


@dataclass(frozen=True)
class ActualMaskedCycleLedger:
    """The exact four-edge prime fixture at ``q=200003``."""

    q: int
    d_integer_lower_bound: int
    shell_width: float
    edges: tuple[MaskedEdge, MaskedEdge, MaskedEdge, MaskedEdge]
    maximum_absolute_residual: int
    integer_window_lower_bound: int
    alternating_label_determinant: int
    all_nodes_prime: bool
    all_nodes_in_shell: bool
    q_exceeds_d_squared: bool


def actual_masked_four_cycle() -> ActualMaskedCycleLedger:
    """Return a literal prime-power/product-window four-cycle.

    Rows are the carriers ``83777,101411`` and columns are the colours
    ``101411,117709``.  In row-major order the labels are

    ``[[117709,101411],[97241,83777]]``.

    We use the integer lower bound ``D>371`` for
    ``D=q**(16/33)``.  Hence checking ``|r|<371*q`` is stronger than the
    required window check and avoids a floating-point assertion.
    """

    q = 200_003
    q_cubed = q**3
    rows = (83_777, 101_411)
    colours = (101_411, 117_709)
    labels = ((117_709, 101_411), (97_241, 83_777))
    edges_list: list[MaskedEdge] = []
    for row_index, carrier in enumerate(rows):
        for column_index, colour in enumerate(colours):
            label = labels[row_index][column_index]
            residual = 8 * label * carrier * colour - q_cubed
            edges_list.append(MaskedEdge(label, carrier, colour, residual))
    edges = tuple(edges_list)
    if len(edges) != 4:
        raise AssertionError("the fixture must have four edges")

    nodes = {
        edge.label for edge in edges
    } | {edge.carrier for edge in edges} | {edge.colour for edge in edges}
    centre = q / 2.0
    width = 0.2
    lower = centre * exp(-width)
    upper = centre * exp(width)
    maximum_residual = max(abs(edge.residual) for edge in edges)
    d_lower = 371
    # 371^33 < q^16 proves 371 < q^(16/33) exactly.
    if not d_lower**33 < q**16:
        raise AssertionError("the advertised integer lower bound for D failed")
    return ActualMaskedCycleLedger(
        q=q,
        d_integer_lower_bound=d_lower,
        shell_width=width,
        edges=edges,  # type: ignore[arg-type]
        maximum_absolute_residual=maximum_residual,
        integer_window_lower_bound=q * d_lower,
        alternating_label_determinant=(
            labels[0][0] * labels[1][1]
            - labels[0][1] * labels[1][0]
        ),
        all_nodes_prime=all(is_prime(node) for node in nodes),
        all_nodes_in_shell=all(lower <= node <= upper for node in nodes),
        # If D=q^(16/33), then D^2=q^(32/33)<q for every q>1.
        q_exceeds_d_squared=q > 1,
    )


@dataclass(frozen=True)
class AlternatingCycleLedger:
    """Exact multiplicative data for one projected even cycle."""

    length: int
    unprimed_label_product: int
    primed_label_product: int
    unprimed_edge_product: int
    primed_edge_product: int
    residual_sum_difference: int
    cross_multiplication_defect: int


def alternating_cycle_ledger(
    q: int,
    unprimed_labels: Sequence[int],
    primed_labels: Sequence[int],
    unprimed_residuals: Sequence[int],
    primed_residuals: Sequence[int],
) -> AlternatingCycleLedger:
    """Return the exact alternating products attached to a cycle.

    For an actual cycle, cancellation of all carrier and colour vertices
    gives

    ``A' * prod(Q+r_i) = A * prod(Q+r'_i)``.

    The returned ``cross_multiplication_defect`` is therefore zero.  The
    function does not assume the cycle geometry, making it useful for exact
    replay of the arithmetic conclusion.
    """

    size = len(unprimed_labels)
    if not size or not (
        len(primed_labels)
        == len(unprimed_residuals)
        == len(primed_residuals)
        == size
    ):
        raise ValueError("all four cycle lists must have one common length")
    q_cubed = q**3

    def product(values: Sequence[int]) -> int:
        answer = 1
        for value in values:
            answer *= int(value)
        return answer

    unprimed_label_product = product(unprimed_labels)
    primed_label_product = product(primed_labels)
    unprimed_edge_product = product(
        tuple(q_cubed + int(value) for value in unprimed_residuals)
    )
    primed_edge_product = product(
        tuple(q_cubed + int(value) for value in primed_residuals)
    )
    return AlternatingCycleLedger(
        length=2 * size,
        unprimed_label_product=unprimed_label_product,
        primed_label_product=primed_label_product,
        unprimed_edge_product=unprimed_edge_product,
        primed_edge_product=primed_edge_product,
        residual_sum_difference=(
            sum(int(value) for value in unprimed_residuals)
            - sum(int(value) for value in primed_residuals)
        ),
        cross_multiplication_defect=(
            primed_label_product * unprimed_edge_product
            - unprimed_label_product * primed_edge_product
        ),
    )


@dataclass(frozen=True)
class ProjectivePlaneTraceLedger:
    """Critical-scale unlabelled high-trace incidence obstruction."""

    field_order: int
    components: int
    vertices_per_side_per_component: int
    degree: int
    total_vertices_per_side: int
    total_edges: int
    four_cycle_count: int
    centred_component_singular_value: int
    square_root_degree: float
    label_count_upper_bound: int
    maximum_label_degree: int
    unique_edge_label_count: int


def projective_plane_trace_ledger(
    field_order: int, components: int = 2
) -> ProjectivePlaneTraceLedger:
    """Return exact counts for disjoint projective-plane incidence graphs.

    ``field_order`` is required to be prime so that ``PG(2,p)`` exists.
    Its point--line incidence graph is ``(p+1)``-regular, has
    ``p^2+p+1`` vertices on each side, and has no four-cycle.  In a disjoint
    union of at least two copies, the difference of two component constants
    is killed by the global all-ones matrix and is a singular vector of
    value ``p+1``.

    A regular bipartite graph decomposes into perfect matchings.  Split each
    matching into pieces of at most ``degree`` edges and give each piece a
    fresh label.  This makes every two-coordinate projection injective,
    keeps label degree at most ``degree``, and uses the displayed number of
    labels.  It does *not* impose the cubic product equations.
    """

    if not is_prime(field_order):
        raise ValueError("field_order must be prime")
    if components < 2:
        raise ValueError("at least two components are required")
    p = field_order
    vertices = p * p + p + 1
    degree = p + 1
    labels_per_component = degree * ceil(vertices / degree)
    return ProjectivePlaneTraceLedger(
        field_order=p,
        components=components,
        vertices_per_side_per_component=vertices,
        degree=degree,
        total_vertices_per_side=components * vertices,
        total_edges=components * vertices * degree,
        four_cycle_count=0,
        centred_component_singular_value=degree,
        square_root_degree=degree**0.5,
        label_count_upper_bound=components * labels_per_component,
        maximum_label_degree=degree,
        unique_edge_label_count=components * vertices * degree,
    )


def critical_component_count(degree: int) -> int:
    """Return ``ceil(D^(1/16))``, the critical number of components."""

    if degree <= 0:
        raise ValueError("degree must be positive")
    return ceil(exp(log(degree) / 16.0))
