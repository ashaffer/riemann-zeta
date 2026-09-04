"""Certified A4 participation bounds for serialized A2 packet cells.

Every value returned here is an exact :class:`fractions.Fraction`.  A primal
certificate is already enough to prove that one finite packet family meets
the A4 target.  Optional dual data implement the reusable lower certificate

    L R >= (sum_t s_t)^2,
    s_t^2 <= b_t p_t r_t,

where ``b_t=a_t^2`` is the serialized squared packet bound.  Numerical
optimizers may propose balances or dual weights, but only this exact replay
is trusted.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Sequence

from qp_a2_packet_serialization import (
    A2PacketCell,
    Pair,
    validate_a2_packet_cell,
)


@dataclass(frozen=True)
class A4PrimalCertificate:
    """An exact feasible packet-balancing certificate."""

    signed_cell: tuple[int, int, int, int]
    source_manifest_sha256: str
    balances: tuple[tuple[str, Fraction], ...]
    left_loads: tuple[tuple[Pair, Fraction], ...]
    right_loads: tuple[tuple[Pair, Fraction], ...]
    maximum_left_load: Fraction
    maximum_right_load: Fraction
    upper_bound: Fraction
    target: Fraction
    target_ratio: Fraction
    meets_target: bool


@dataclass(frozen=True)
class A4DualCertificate:
    """An exact weak-dual lower certificate for the A4 infimum."""

    signed_cell: tuple[int, int, int, int]
    source_manifest_sha256: str
    left_probabilities: tuple[tuple[Pair, Fraction], ...]
    right_probabilities: tuple[tuple[Pair, Fraction], ...]
    packet_slacks: tuple[tuple[str, Fraction], ...]
    lower_bound: Fraction


@dataclass(frozen=True)
class A4CertifiedBracket:
    """A rigorously replayed lower/upper bracket for one packet cell."""

    lower_bound: Fraction
    upper_bound: Fraction
    target: Fraction
    lower_does_not_exceed_upper: bool
    upper_meets_target: bool


@dataclass(frozen=True)
class A4FamilySummary:
    """The exact unit-balance rerun over a family of signed cells."""

    q: int
    degree_parameter: int
    cell_count: int
    term_count: int
    packet_count: int
    maximum_packet_terms: int
    maximum_left_load: Fraction
    maximum_right_load: Fraction
    worst_upper_bound: Fraction
    target: Fraction
    worst_target_ratio: Fraction
    worst_cells: tuple[tuple[int, int, int, int], ...]
    every_cell_meets_target: bool


def certify_a4_primal(
    cell: A2PacketCell,
    balances: Mapping[str, Fraction] | None = None,
) -> A4PrimalCertificate:
    """Replay an exact feasible A4 upper certificate.

    If balances are omitted, ``lambda_t=1`` is used.  This is the symmetric
    choice for the exact-secant packets emitted by the baseline A2 extractor,
    since all of their squared norm bounds are one.
    """

    validation = validate_a2_packet_cell(cell)
    if validation.remainder_weight:
        raise ValueError("A4 requires a zero-remainder A2 packet cover")
    packet_ids = {packet.packet_id for packet in cell.packets}
    if balances is None:
        normalized = {packet_id: Fraction(1) for packet_id in packet_ids}
    else:
        normalized = {
            str(packet_id): Fraction(value)
            for packet_id, value in balances.items()
        }
        if set(normalized) != packet_ids:
            raise ValueError("A4 balances must name every packet exactly once")
    if any(value <= 0 for value in normalized.values()):
        raise ValueError("A4 balancing parameters must be positive")

    left_loads: dict[Pair, Fraction] = defaultdict(Fraction)
    right_loads: dict[Pair, Fraction] = defaultdict(Fraction)
    for packet in cell.packets:
        balance = normalized[packet.packet_id]
        right_charge = packet.norm_bound_squared / balance
        for vertex in packet.left_support:
            left_loads[vertex] += balance
        for vertex in packet.right_support:
            right_loads[vertex] += right_charge
    maximum_left = max(left_loads.values(), default=Fraction(0))
    maximum_right = max(right_loads.values(), default=Fraction(0))
    upper = maximum_left * maximum_right
    target = Fraction(cell.degree_parameter**2)
    return A4PrimalCertificate(
        signed_cell=cell.signed_cell,
        source_manifest_sha256=cell.source_manifest_sha256,
        balances=tuple(sorted(normalized.items())),
        left_loads=tuple(sorted(left_loads.items())),
        right_loads=tuple(sorted(right_loads.items())),
        maximum_left_load=maximum_left,
        maximum_right_load=maximum_right,
        upper_bound=upper,
        target=target,
        target_ratio=upper / target,
        meets_target=upper <= target,
    )


def certify_a4_dual(
    cell: A2PacketCell,
    *,
    left_probabilities: Mapping[Pair, Fraction],
    right_probabilities: Mapping[Pair, Fraction],
    packet_slacks: Mapping[str, Fraction],
) -> A4DualCertificate:
    """Verify a rational weak-dual certificate exactly."""

    validation = validate_a2_packet_cell(cell)
    if validation.remainder_weight:
        raise ValueError("A4 duality applies only after the remainder is removed")
    alpha = {tuple(vertex): Fraction(value) for vertex, value in left_probabilities.items()}
    beta = {tuple(vertex): Fraction(value) for vertex, value in right_probabilities.items()}
    if any(len(vertex) != 2 for vertex in (*alpha, *beta)):
        raise ValueError("A4 probability vertices must be ordered pairs")
    if any(value < 0 for value in (*alpha.values(), *beta.values())):
        raise ValueError("A4 dual probabilities must be nonnegative")
    if sum(alpha.values(), Fraction(0)) != 1:
        raise ValueError("left A4 dual probabilities must sum to one")
    if sum(beta.values(), Fraction(0)) != 1:
        raise ValueError("right A4 dual probabilities must sum to one")
    known_left = {vertex for packet in cell.packets for vertex in packet.left_support}
    known_right = {vertex for packet in cell.packets for vertex in packet.right_support}
    if not set(alpha) <= known_left or not set(beta) <= known_right:
        raise ValueError("A4 dual probabilities contain an unknown vertex")
    slacks = {
        str(packet_id): Fraction(value)
        for packet_id, value in packet_slacks.items()
    }
    packet_ids = {packet.packet_id for packet in cell.packets}
    if not set(slacks) <= packet_ids or any(value < 0 for value in slacks.values()):
        raise ValueError("A4 dual slacks must be nonnegative and name known packets")
    for packet in cell.packets:
        p_value = sum(
            (alpha.get(vertex, Fraction(0)) for vertex in packet.left_support),
            Fraction(0),
        )
        r_value = sum(
            (beta.get(vertex, Fraction(0)) for vertex in packet.right_support),
            Fraction(0),
        )
        slack = slacks.get(packet.packet_id, Fraction(0))
        if slack * slack > packet.norm_bound_squared * p_value * r_value:
            raise ValueError("an A4 dual packet slack violates its quadratic bound")
    lower = sum(slacks.values(), Fraction(0)) ** 2
    return A4DualCertificate(
        signed_cell=cell.signed_cell,
        source_manifest_sha256=cell.source_manifest_sha256,
        left_probabilities=tuple(sorted(alpha.items())),
        right_probabilities=tuple(sorted(beta.items())),
        packet_slacks=tuple(sorted(slacks.items())),
        lower_bound=lower,
    )


def bracket_a4(
    primal: A4PrimalCertificate, dual: A4DualCertificate
) -> A4CertifiedBracket:
    """Combine exact primal and dual certificates and check weak duality."""

    if (
        primal.signed_cell != dual.signed_cell
        or primal.source_manifest_sha256 != dual.source_manifest_sha256
    ):
        raise ValueError("A4 primal and dual certificates name different cells")
    if dual.lower_bound > primal.upper_bound:
        raise ValueError("the supplied A4 certificates violate weak duality")
    return A4CertifiedBracket(
        lower_bound=dual.lower_bound,
        upper_bound=primal.upper_bound,
        target=primal.target,
        lower_does_not_exceed_upper=True,
        upper_meets_target=primal.meets_target,
    )


def summarize_a4_unit_balances(
    cells: Sequence[A2PacketCell],
) -> A4FamilySummary:
    """Run the exact unit-balance A4 certificate on every supplied cell."""

    if not cells:
        raise ValueError("at least one serialized A2 cell is required")
    q = cells[0].q
    degree = cells[0].degree_parameter
    if any(cell.q != q or cell.degree_parameter != degree for cell in cells):
        raise ValueError("an A4 family summary needs a common q and degree")
    validations = [validate_a2_packet_cell(cell) for cell in cells]
    certificates = [certify_a4_primal(cell) for cell in cells]
    worst = max(certificate.upper_bound for certificate in certificates)
    worst_cells = tuple(
        certificate.signed_cell
        for certificate in certificates
        if certificate.upper_bound == worst
    )
    maximum_left = max(
        certificate.maximum_left_load for certificate in certificates
    )
    maximum_right = max(
        certificate.maximum_right_load for certificate in certificates
    )
    target = Fraction(degree**2)
    return A4FamilySummary(
        q=q,
        degree_parameter=degree,
        cell_count=len(cells),
        term_count=sum(ledger.term_count for ledger in validations),
        packet_count=sum(ledger.packet_count for ledger in validations),
        maximum_packet_terms=max(
            ledger.maximum_packet_terms for ledger in validations
        ),
        maximum_left_load=maximum_left,
        maximum_right_load=maximum_right,
        worst_upper_bound=worst,
        target=target,
        worst_target_ratio=worst / target,
        worst_cells=worst_cells,
        every_cell_meets_target=all(
            certificate.meets_target for certificate in certificates
        ),
    )
