"""Exact serialization for candidate A2 packet decompositions.

The unresolved QP packet program needs more information than the historical
``DynamicAffineComponent`` objects retain.  This module keeps the positive
ordered completion-pair atoms, their four physical masks, the packet
allocations, a replayable Schur certificate, and any unallocated remainder.

The concrete extractor implemented here is deliberately modest.  Inside one
signed dyadic cell it groups atoms by their exact carrier secant ``(A,B)``.
The resulting color-pair relation is checked to be a weighted partial
matching and hence has a certified local operator bound.  This is a legal A2
serialization baseline; it is not the open excess-implies-affine-packet
theorem and makes no asymptotic assertion.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from typing import Iterable, Mapping, Sequence

from qp_collective_dyadic_gate import (
    completion_secant_peaks,
    signed_dyadic_cell,
)


SCHEMA_VERSION = "qp-a2-packet-cell/v1"

Pair = tuple[int, int]
Cell = tuple[int, int, int, int]
ColorMatrix = tuple[int, int, int, int]
Completion = tuple[int, int, int, int]
CartesianMasks = tuple[
    tuple[int, ...], tuple[int, ...], tuple[int, ...], tuple[int, ...]
]


@dataclass(frozen=True)
class A2CompletionPairAtom:
    """One occurrence of the positive off-diagonal factorial form."""

    term_id: int
    colors: ColorMatrix
    first_completion: Completion
    second_completion: Completion
    secants: Pair
    source_weight: Fraction

    @property
    def left_vertex(self) -> Pair:
        return self.colors[0], self.colors[1]

    @property
    def right_vertex(self) -> Pair:
        return self.colors[2], self.colors[3]


@dataclass(frozen=True)
class A2PacketAllocation:
    """The exact part of one source atom assigned to one packet."""

    term_id: int
    weight: Fraction


@dataclass(frozen=True)
class A2RemainderAllocation:
    """The exact part of one source atom left outside the packet family."""

    term_id: int
    weight: Fraction
    reason: str


@dataclass(frozen=True)
class A2Packet:
    """One packet with an explicitly replayable weighted-Schur bound."""

    packet_id: str
    kind: str
    secants: Pair | None
    allocations: tuple[A2PacketAllocation, ...]
    left_support: tuple[Pair, ...]
    right_support: tuple[Pair, ...]
    schur_max_left_sum: Fraction
    schur_max_right_sum: Fraction
    norm_bound_squared: Fraction


@dataclass(frozen=True)
class A2PacketCell:
    """A complete serialized A2 candidate on one signed dyadic cell."""

    schema_version: str
    source_id: str
    source_manifest_sha256: str
    q: int
    hard_window_radius: int
    degree_parameter: int
    signed_cell: Cell
    sector: str
    external_sectors: tuple[str, ...]
    masks: CartesianMasks
    terms: tuple[A2CompletionPairAtom, ...]
    packets: tuple[A2Packet, ...]
    remainder: tuple[A2RemainderAllocation, ...]
    overlap_multiplicities: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class A2ValidationLedger:
    """Exact completeness and certificate statistics for one packet cell."""

    term_count: int
    packet_count: int
    packet_allocations: int
    remainder_allocations: int
    source_weight: Fraction
    packet_weight: Fraction
    remainder_weight: Fraction
    maximum_overlap_multiplicity: int
    maximum_packet_terms: int
    all_source_weight_accounted_for: bool
    all_schur_certificates_replayed: bool


def _fraction_payload(value: Fraction) -> list[int]:
    value = Fraction(value)
    return [value.numerator, value.denominator]


def _fraction_from_payload(raw: object) -> Fraction:
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError("an exact rational must be [numerator, denominator]")
    numerator, denominator = raw
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise ValueError("rational numerator and denominator must be integers")
    if denominator <= 0:
        raise ValueError("a rational denominator must be positive")
    value = Fraction(numerator, denominator)
    if [value.numerator, value.denominator] != raw:
        raise ValueError("serialized rationals must be reduced and normalized")
    return value


def _integer_tuple(raw: object, length: int, label: str) -> tuple[int, ...]:
    if (
        not isinstance(raw, list)
        or len(raw) != length
        or any(not isinstance(value, int) for value in raw)
    ):
        raise ValueError(f"{label} must be a list of {length} integers")
    return tuple(raw)


def _term_payload(term: A2CompletionPairAtom) -> dict[str, object]:
    return {
        "term_id": term.term_id,
        "colors": list(term.colors),
        "first_completion": list(term.first_completion),
        "second_completion": list(term.second_completion),
        "secants": list(term.secants),
        "source_weight": _fraction_payload(term.source_weight),
    }


def _manifest_digest(terms: Sequence[A2CompletionPairAtom]) -> str:
    payload = [_term_payload(term) for term in terms]
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return sha256(encoded).hexdigest()


def _cell_payload(cell: A2PacketCell) -> dict[str, object]:
    return {
        "schema_version": cell.schema_version,
        "source_id": cell.source_id,
        "source_manifest_sha256": cell.source_manifest_sha256,
        "q": cell.q,
        "hard_window_radius": cell.hard_window_radius,
        "degree_parameter": cell.degree_parameter,
        "signed_cell": list(cell.signed_cell),
        "sector": cell.sector,
        "external_sectors": list(cell.external_sectors),
        "masks": [list(mask) for mask in cell.masks],
        "terms": [_term_payload(term) for term in cell.terms],
        "packets": [
            {
                "packet_id": packet.packet_id,
                "kind": packet.kind,
                "secants": (
                    None if packet.secants is None else list(packet.secants)
                ),
                "allocations": [
                    {
                        "term_id": allocation.term_id,
                        "weight": _fraction_payload(allocation.weight),
                    }
                    for allocation in packet.allocations
                ],
                "left_support": [list(pair) for pair in packet.left_support],
                "right_support": [list(pair) for pair in packet.right_support],
                "schur_max_left_sum": _fraction_payload(
                    packet.schur_max_left_sum
                ),
                "schur_max_right_sum": _fraction_payload(
                    packet.schur_max_right_sum
                ),
                "norm_bound_squared": _fraction_payload(
                    packet.norm_bound_squared
                ),
            }
            for packet in cell.packets
        ],
        "remainder": [
            {
                "term_id": allocation.term_id,
                "weight": _fraction_payload(allocation.weight),
                "reason": allocation.reason,
            }
            for allocation in cell.remainder
        ],
        "overlap_multiplicities": [
            [term_id, multiplicity]
            for term_id, multiplicity in cell.overlap_multiplicities
        ],
    }


def serialize_a2_packet_cell(cell: A2PacketCell, *, indent: int | None = None) -> str:
    """Return a hash-protected, deterministic JSON representation."""

    validate_a2_packet_cell(cell)
    payload = _cell_payload(cell)
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    envelope = {
        "payload_sha256": sha256(canonical.encode("ascii")).hexdigest(),
        "payload": payload,
    }
    return json.dumps(
        envelope,
        sort_keys=True,
        separators=(",", ":") if indent is None else None,
        indent=indent,
        ensure_ascii=True,
    )


def _term_from_payload(raw: object) -> A2CompletionPairAtom:
    if not isinstance(raw, dict):
        raise ValueError("a term payload must be an object")
    term_id = raw.get("term_id")
    if not isinstance(term_id, int):
        raise ValueError("term_id must be an integer")
    return A2CompletionPairAtom(
        term_id=term_id,
        colors=_integer_tuple(raw.get("colors"), 4, "colors"),  # type: ignore[arg-type]
        first_completion=_integer_tuple(
            raw.get("first_completion"), 4, "first_completion"
        ),  # type: ignore[arg-type]
        second_completion=_integer_tuple(
            raw.get("second_completion"), 4, "second_completion"
        ),  # type: ignore[arg-type]
        secants=_integer_tuple(raw.get("secants"), 2, "secants"),  # type: ignore[arg-type]
        source_weight=_fraction_from_payload(raw.get("source_weight")),
    )


def deserialize_a2_packet_cell(serialized: str) -> A2PacketCell:
    """Parse JSON, verify its content hash, and replay every certificate."""

    try:
        envelope = json.loads(serialized)
    except json.JSONDecodeError as error:
        raise ValueError("invalid A2 JSON") from error
    if not isinstance(envelope, dict) or set(envelope) != {
        "payload_sha256",
        "payload",
    }:
        raise ValueError("an A2 envelope needs exactly payload and payload_sha256")
    digest = envelope["payload_sha256"]
    payload = envelope["payload"]
    if not isinstance(digest, str) or not isinstance(payload, dict):
        raise ValueError("invalid A2 envelope field types")
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    if sha256(canonical.encode("ascii")).hexdigest() != digest:
        raise ValueError("the A2 payload hash does not match")

    packets_raw = payload.get("packets")
    remainder_raw = payload.get("remainder")
    terms_raw = payload.get("terms")
    masks_raw = payload.get("masks")
    overlaps_raw = payload.get("overlap_multiplicities")
    external_raw = payload.get("external_sectors")
    if not isinstance(terms_raw, list) or not isinstance(packets_raw, list):
        raise ValueError("terms and packets must be lists")
    if not isinstance(remainder_raw, list) or not isinstance(masks_raw, list):
        raise ValueError("remainder and masks must be lists")
    if len(masks_raw) != 4:
        raise ValueError("exactly four Cartesian masks are required")
    if not isinstance(overlaps_raw, list) or not isinstance(external_raw, list):
        raise ValueError("overlap and external-sector fields must be lists")

    terms = tuple(_term_from_payload(raw) for raw in terms_raw)
    packets: list[A2Packet] = []
    for raw in packets_raw:
        if not isinstance(raw, dict):
            raise ValueError("a packet payload must be an object")
        packet_id, kind = raw.get("packet_id"), raw.get("kind")
        if not isinstance(packet_id, str) or not isinstance(kind, str):
            raise ValueError("packet id and kind must be strings")
        raw_secants = raw.get("secants")
        secants = (
            None
            if raw_secants is None
            else _integer_tuple(raw_secants, 2, "packet secants")
        )
        allocations_raw = raw.get("allocations")
        if not isinstance(allocations_raw, list):
            raise ValueError("packet allocations must be a list")
        allocations: list[A2PacketAllocation] = []
        for allocation in allocations_raw:
            if not isinstance(allocation, dict):
                raise ValueError("a packet allocation must be an object")
            term_id = allocation.get("term_id")
            if not isinstance(term_id, int):
                raise ValueError("an allocation term_id must be an integer")
            allocations.append(
                A2PacketAllocation(
                    term_id=term_id,
                    weight=_fraction_from_payload(allocation.get("weight")),
                )
            )
        left_raw, right_raw = raw.get("left_support"), raw.get("right_support")
        if not isinstance(left_raw, list) or not isinstance(right_raw, list):
            raise ValueError("packet supports must be lists")
        packets.append(
            A2Packet(
                packet_id=packet_id,
                kind=kind,
                secants=secants,  # type: ignore[arg-type]
                allocations=tuple(allocations),
                left_support=tuple(
                    _integer_tuple(pair, 2, "left support pair")  # type: ignore[arg-type]
                    for pair in left_raw
                ),
                right_support=tuple(
                    _integer_tuple(pair, 2, "right support pair")  # type: ignore[arg-type]
                    for pair in right_raw
                ),
                schur_max_left_sum=_fraction_from_payload(
                    raw.get("schur_max_left_sum")
                ),
                schur_max_right_sum=_fraction_from_payload(
                    raw.get("schur_max_right_sum")
                ),
                norm_bound_squared=_fraction_from_payload(
                    raw.get("norm_bound_squared")
                ),
            )
        )

    remainder: list[A2RemainderAllocation] = []
    for raw in remainder_raw:
        if not isinstance(raw, dict):
            raise ValueError("a remainder payload must be an object")
        term_id, reason = raw.get("term_id"), raw.get("reason")
        if not isinstance(term_id, int) or not isinstance(reason, str):
            raise ValueError("invalid remainder term id or reason")
        remainder.append(
            A2RemainderAllocation(
                term_id=term_id,
                weight=_fraction_from_payload(raw.get("weight")),
                reason=reason,
            )
        )

    overlaps: list[tuple[int, int]] = []
    for raw in overlaps_raw:
        pair = _integer_tuple(raw, 2, "overlap multiplicity")
        overlaps.append((pair[0], pair[1]))
    if any(not isinstance(value, str) for value in external_raw):
        raise ValueError("external sector labels must be strings")
    source_id = payload.get("source_id")
    manifest = payload.get("source_manifest_sha256")
    sector = payload.get("sector")
    version = payload.get("schema_version")
    q = payload.get("q")
    hard_window_radius = payload.get("hard_window_radius")
    degree = payload.get("degree_parameter")
    if not all(isinstance(value, str) for value in (source_id, manifest, sector, version)):
        raise ValueError("invalid A2 string metadata")
    if (
        not isinstance(q, int)
        or not isinstance(hard_window_radius, int)
        or not isinstance(degree, int)
    ):
        raise ValueError("q, hard_window_radius, and degree_parameter must be integers")
    cell = A2PacketCell(
        schema_version=version,
        source_id=source_id,
        source_manifest_sha256=manifest,
        q=q,
        hard_window_radius=hard_window_radius,
        degree_parameter=degree,
        signed_cell=_integer_tuple(
            payload.get("signed_cell"), 4, "signed_cell"
        ),  # type: ignore[arg-type]
        sector=sector,
        external_sectors=tuple(external_raw),
        masks=tuple(
            tuple(_integer_tuple(mask, len(mask), "Cartesian mask"))
            if isinstance(mask, list)
            else ()
            for mask in masks_raw
        ),  # type: ignore[arg-type]
        terms=terms,
        packets=tuple(packets),
        remainder=tuple(remainder),
        overlap_multiplicities=tuple(overlaps),
    )
    validate_a2_packet_cell(cell)
    return cell


def _schur_data(
    allocations: Sequence[A2PacketAllocation],
    terms_by_id: Mapping[int, A2CompletionPairAtom],
) -> tuple[tuple[Pair, ...], tuple[Pair, ...], Fraction, Fraction]:
    edge_weights: dict[tuple[Pair, Pair], Fraction] = defaultdict(Fraction)
    for allocation in allocations:
        term = terms_by_id[allocation.term_id]
        edge_weights[term.left_vertex, term.right_vertex] += allocation.weight
    left_sums: dict[Pair, Fraction] = defaultdict(Fraction)
    right_sums: dict[Pair, Fraction] = defaultdict(Fraction)
    for (left, right), weight in edge_weights.items():
        left_sums[left] += weight
        right_sums[right] += weight
    return (
        tuple(sorted(left_sums)),
        tuple(sorted(right_sums)),
        max(left_sums.values(), default=Fraction(0)),
        max(right_sums.values(), default=Fraction(0)),
    )


def validate_a2_packet_cell(cell: A2PacketCell) -> A2ValidationLedger:
    """Replay source coverage, masks, cells, supports, and Schur bounds."""

    if cell.schema_version != SCHEMA_VERSION:
        raise ValueError("unsupported A2 schema version")
    if cell.q <= 2 or cell.hard_window_radius <= 0 or cell.degree_parameter <= 0:
        raise ValueError("q, the hard-window radius, and degree must be positive")
    first_sign, second_sign, first_level, second_level = cell.signed_cell
    if first_sign not in (-1, 1) or second_sign not in (-1, 1):
        raise ValueError("signed-cell signs must be plus or minus one")
    if first_level < 0 or second_level < 0:
        raise ValueError("signed-cell levels must be nonnegative")
    if not cell.source_id or not cell.sector:
        raise ValueError("source and sector labels must be nonempty")
    normalized_masks = tuple(tuple(sorted(set(mask))) for mask in cell.masks)
    if normalized_masks != cell.masks:
        raise ValueError("Cartesian masks must be sorted and duplicate-free")
    if any(not mask for mask in cell.masks):
        raise ValueError("all four Cartesian masks must be nonempty")

    terms_by_id = {term.term_id: term for term in cell.terms}
    if len(terms_by_id) != len(cell.terms):
        raise ValueError("term ids must be unique")
    if tuple(sorted(terms_by_id)) != tuple(range(len(cell.terms))):
        raise ValueError("term ids must be the canonical consecutive range")
    if _manifest_digest(cell.terms) != cell.source_manifest_sha256:
        raise ValueError("the source-term manifest digest does not match")
    for term in cell.terms:
        if term.source_weight <= 0:
            raise ValueError("source atom weights must be positive")
        if term.first_completion == term.second_completion:
            raise ValueError("A2 terms must be off-diagonal completion pairs")
        if completion_secant_peaks(
            term.first_completion, term.second_completion
        ) != term.secants:
            raise ValueError("a term has incorrect secants")
        if signed_dyadic_cell(*term.secants) != cell.signed_cell:
            raise ValueError("a term lies outside the declared signed cell")
        if any(
            color not in mask
            for color, mask in zip(term.colors, cell.masks, strict=True)
        ):
            raise ValueError("a term violates one of the four Cartesian masks")
        if len(set(term.colors + term.first_completion)) != 8:
            raise ValueError("the first completion is outside the generic sector")
        if len(set(term.colors + term.second_completion)) != 8:
            raise ValueError("the second completion is outside the generic sector")
        for completion in (term.first_completion, term.second_completion):
            a1, a2, b1, b2 = completion
            c11, c12, c21, c22 = term.colors
            triples = (
                (a1, b1, c11),
                (a1, b2, c12),
                (a2, b1, c21),
                (a2, b2, c22),
            )
            if any(
                abs(8 * a * b * c - cell.q**3)
                > cell.q * cell.hard_window_radius
                for a, b, c in triples
            ):
                raise ValueError("a completion violates the serialized hard window")

    packet_ids = [packet.packet_id for packet in cell.packets]
    if len(set(packet_ids)) != len(packet_ids) or any(not value for value in packet_ids):
        raise ValueError("packet ids must be unique and nonempty")
    allocated_by_term: dict[int, Fraction] = defaultdict(Fraction)
    overlap_by_term: dict[int, int] = defaultdict(int)
    packet_weight = Fraction(0)
    for packet in cell.packets:
        if not packet.allocations:
            raise ValueError("empty packets are not serializable A2 pieces")
        allocation_ids = [allocation.term_id for allocation in packet.allocations]
        if len(set(allocation_ids)) != len(allocation_ids):
            raise ValueError("one packet may allocate each source term only once")
        for allocation in packet.allocations:
            if allocation.term_id not in terms_by_id:
                raise ValueError("a packet references an unknown source term")
            if allocation.weight <= 0:
                raise ValueError("packet allocation weights must be positive")
            allocated_by_term[allocation.term_id] += allocation.weight
            overlap_by_term[allocation.term_id] += 1
            packet_weight += allocation.weight
        left, right, maximum_left, maximum_right = _schur_data(
            packet.allocations, terms_by_id
        )
        if packet.left_support != left or packet.right_support != right:
            raise ValueError("a packet support does not equal its term projection")
        if packet.schur_max_left_sum != maximum_left:
            raise ValueError("a packet has an incorrect left Schur sum")
        if packet.schur_max_right_sum != maximum_right:
            raise ValueError("a packet has an incorrect right Schur sum")
        if packet.norm_bound_squared != maximum_left * maximum_right:
            raise ValueError("a packet has an incorrect squared Schur bound")
        if packet.norm_bound_squared <= 0:
            raise ValueError("positive packets need a positive norm bound")
        packet_terms = tuple(terms_by_id[index] for index in allocation_ids)
        if packet.kind == "exact_secant_partial_matching":
            if packet.secants is None or any(
                term.secants != packet.secants for term in packet_terms
            ):
                raise ValueError("an exact-secant packet mixed secant layers")
            if len(packet.left_support) != len(packet.allocations):
                raise ValueError("an exact-secant packet repeated a left vertex")
            if len(packet.right_support) != len(packet.allocations):
                raise ValueError("an exact-secant packet repeated a right vertex")
        else:
            raise ValueError("unsupported A2 packet certificate kind")

    remainder_by_term: dict[int, Fraction] = defaultdict(Fraction)
    remainder_weight = Fraction(0)
    for allocation in cell.remainder:
        if allocation.term_id not in terms_by_id:
            raise ValueError("the remainder references an unknown source term")
        if allocation.weight <= 0 or not allocation.reason:
            raise ValueError("remainder allocations need positive weight and a reason")
        remainder_by_term[allocation.term_id] += allocation.weight
        remainder_weight += allocation.weight

    declared_overlap = dict(cell.overlap_multiplicities)
    if len(declared_overlap) != len(cell.overlap_multiplicities):
        raise ValueError("overlap multiplicities must have unique term ids")
    if set(declared_overlap) != set(terms_by_id):
        raise ValueError("overlap multiplicities must name every source term")
    if any(declared_overlap[index] != overlap_by_term[index] for index in terms_by_id):
        raise ValueError("declared packet-overlap multiplicities are incorrect")

    source_weight = sum(
        (term.source_weight for term in cell.terms), Fraction(0)
    )
    for term in cell.terms:
        if allocated_by_term[term.term_id] + remainder_by_term[term.term_id] != (
            term.source_weight
        ):
            raise ValueError("packet allocations and remainder do not conserve a term")
    return A2ValidationLedger(
        term_count=len(cell.terms),
        packet_count=len(cell.packets),
        packet_allocations=sum(
            len(packet.allocations) for packet in cell.packets
        ),
        remainder_allocations=len(cell.remainder),
        source_weight=source_weight,
        packet_weight=packet_weight,
        remainder_weight=remainder_weight,
        maximum_overlap_multiplicity=max(overlap_by_term.values(), default=0),
        maximum_packet_terms=max(
            (len(packet.allocations) for packet in cell.packets), default=0
        ),
        all_source_weight_accounted_for=(
            source_weight == packet_weight + remainder_weight
        ),
        all_schur_certificates_replayed=True,
    )


def _exact_secant_packet(
    packet_id: str,
    secants: Pair,
    allocations: Sequence[A2PacketAllocation],
    terms_by_id: Mapping[int, A2CompletionPairAtom],
) -> A2Packet:
    left, right, maximum_left, maximum_right = _schur_data(
        allocations, terms_by_id
    )
    return A2Packet(
        packet_id=packet_id,
        kind="exact_secant_partial_matching",
        secants=secants,
        allocations=tuple(allocations),
        left_support=left,
        right_support=right,
        schur_max_left_sum=maximum_left,
        schur_max_right_sum=maximum_right,
        norm_bound_squared=maximum_left * maximum_right,
    )


def extract_exact_secant_a2_cells(
    *,
    q: int,
    degree_parameter: int,
    completion_groups: Mapping[ColorMatrix, Sequence[Completion]],
    source_id: str,
    parent_masks: Sequence[Iterable[int]] | None = None,
) -> tuple[A2PacketCell, ...]:
    """Serialize the generic off-diagonal form by signed cell and secant.

    ``completion_groups`` must retain the physical orientation of every
    color matrix and completion.  No D4 canonicalization is performed.
    Completions outside the eight-distinct sector and zero-secant pairs are
    explicitly outside this extractor's source sector.
    """

    if q <= 2 or degree_parameter <= 0 or not source_id:
        raise ValueError("q, degree_parameter, and source_id are required")
    normalized_groups: list[tuple[ColorMatrix, tuple[Completion, ...]]] = []
    for raw_colors, raw_completions in completion_groups.items():
        if len(raw_colors) != 4:
            raise ValueError("a color matrix must have four entries")
        colors: ColorMatrix = tuple(map(int, raw_colors))  # type: ignore[assignment]
        completions = tuple(
            tuple(map(int, completion)) for completion in raw_completions
        )
        if any(len(completion) != 4 for completion in completions):
            raise ValueError("a completion must have four entries")
        if len(set(completions)) != len(completions):
            raise ValueError("completion occurrence identities must be unique")
        normalized_groups.append((colors, tuple(sorted(completions))))
    normalized_groups.sort()

    maximum_residual = 0
    for colors, completions in normalized_groups:
        c11, c12, c21, c22 = colors
        for a1, a2, b1, b2 in completions:
            maximum_residual = max(
                maximum_residual,
                abs(8 * a1 * b1 * c11 - q**3),
                abs(8 * a1 * b2 * c12 - q**3),
                abs(8 * a2 * b1 * c21 - q**3),
                abs(8 * a2 * b2 * c22 - q**3),
            )
    hard_window_radius = max(1, (maximum_residual + q - 1) // q)

    raw_by_cell: dict[
        Cell, list[tuple[ColorMatrix, Completion, Completion, Pair]]
    ] = defaultdict(list)
    for colors, completions in normalized_groups:
        generic = tuple(
            completion
            for completion in completions
            if len(set(colors + completion)) == 8
        )
        for first in generic:
            for second in generic:
                if first == second:
                    continue
                secants = completion_secant_peaks(first, second)
                if not secants[0] or not secants[1]:
                    continue
                cell = signed_dyadic_cell(*secants)
                raw_by_cell[cell].append((colors, first, second, secants))

    supplied_masks: CartesianMasks | None = None
    if parent_masks is not None:
        if len(parent_masks) != 4:
            raise ValueError("parent_masks must contain exactly four masks")
        supplied_masks = tuple(
            tuple(sorted(set(map(int, mask)))) for mask in parent_masks
        )  # type: ignore[assignment]

    answer: list[A2PacketCell] = []
    for cell in sorted(raw_by_cell):
        rows = sorted(raw_by_cell[cell])
        terms = tuple(
            A2CompletionPairAtom(
                term_id=index,
                colors=colors,
                first_completion=first,
                second_completion=second,
                secants=secants,
                source_weight=Fraction(1),
            )
            for index, (colors, first, second, secants) in enumerate(rows)
        )
        terms_by_id = {term.term_id: term for term in terms}
        if supplied_masks is None:
            masks: CartesianMasks = tuple(
                tuple(sorted({term.colors[position] for term in terms}))
                for position in range(4)
            )  # type: ignore[assignment]
        else:
            masks = supplied_masks

        ids_by_secant: dict[Pair, list[int]] = defaultdict(list)
        for term in terms:
            ids_by_secant[term.secants].append(term.term_id)
        packets: list[A2Packet] = []
        for packet_index, (secants, term_ids) in enumerate(
            sorted(ids_by_secant.items())
        ):
            allocations = tuple(
                A2PacketAllocation(term_id=term_id, weight=Fraction(1))
                for term_id in term_ids
            )
            packets.append(
                _exact_secant_packet(
                    packet_id=f"secant-{packet_index:06d}",
                    secants=secants,
                    allocations=allocations,
                    terms_by_id=terms_by_id,
                )
            )
        overlap = tuple((term.term_id, 1) for term in terms)
        packet_cell = A2PacketCell(
            schema_version=SCHEMA_VERSION,
            source_id=source_id,
            source_manifest_sha256=_manifest_digest(terms),
            q=q,
            hard_window_radius=hard_window_radius,
            degree_parameter=degree_parameter,
            signed_cell=cell,
            sector="generic_eight_distinct_offdiagonal_nonzero_secants",
            external_sectors=(
                "diagonal completion pairs",
                "non-eight-distinct completion rectangles",
                "zero carrier-secants",
            ),
            masks=masks,
            terms=terms,
            packets=tuple(packets),
            remainder=(),
            overlap_multiplicities=overlap,
        )
        validate_a2_packet_cell(packet_cell)
        answer.append(packet_cell)
    return tuple(answer)
