#!/usr/bin/env python3
"""Literal affine-compression diagnostics for the q=25013, U=40 A2 source.

This verifier deliberately does not add a new packet certificate kind to the
production A2 schema.  It asks what several natural *candidate* affine
equivalence relations do to the serialized positive factorial atoms, and it
replays the same Schur/A4 arithmetic independently.

The two serious candidates are:

* one exact primitive four-carrier secant direction; and
* one primitive row direction together with one primitive column direction,
  with their relative scale forgotten (the optimistic rank-one direction).

Groups of size one are the uncompressed remainder.  The sign-cone and
whole-cell controls demonstrate that a permissive data-fitted packet class
can compress this finite sparse fixture while saying no affine mathematics.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd
from pathlib import Path
import sys
from typing import Callable, Hashable, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_a2_packet_serialization import (  # noqa: E402
    A2CompletionPairAtom,
    A2PacketCell,
    extract_exact_secant_a2_cells,
)
from qp_actual_prime_nds import exact_balanced_degree  # noqa: E402
from qp_four_cycle_h_graph_lab import enumerate_rectangles  # noqa: E402
from qp_four_cycle_hostile_lab import build_four_cycle_core  # noqa: E402
from qp_four_cycle_weighted_secant_lab import (  # noqa: E402
    completion_groups_from_generic_rectangles,
)


Q = 25_013


def primitive(vector: Sequence[int], *, canonical_sign: bool = False) -> tuple[int, ...]:
    """Return the primitive integer vector, optionally modulo overall sign."""

    divisor = reduce(gcd, (abs(value) for value in vector if value), 0)
    if not divisor:
        raise ValueError("a direction must be nonzero")
    answer = tuple(value // divisor for value in vector)
    if canonical_sign and next(value for value in answer if value) < 0:
        answer = tuple(-value for value in answer)
    return answer


def completion_difference(term: A2CompletionPairAtom) -> tuple[int, int, int, int]:
    return tuple(
        second - first
        for first, second in zip(
            term.first_completion, term.second_completion, strict=True
        )
    )  # type: ignore[return-value]


def exact_direction(term: A2CompletionPairAtom) -> Hashable:
    return primitive(completion_difference(term))


def rank_one_direction(term: A2CompletionPairAtom) -> Hashable:
    difference = completion_difference(term)
    return primitive(difference[:2]), primitive(difference[2:])


def sign_cone(term: A2CompletionPairAtom) -> Hashable:
    return tuple((value > 0) - (value < 0) for value in completion_difference(term))


def one_cell_packet(_term: A2CompletionPairAtom) -> Hashable:
    return 0


def rational_rank(rows: Iterable[Sequence[int]]) -> int:
    """Exact row rank over Q for the four-dimensional completion points."""

    matrix = [[Fraction(value) for value in row] for row in rows]
    pivot_row = 0
    for column in range(4):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(matrix))
                if matrix[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / value for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            value = matrix[row][column]
            matrix[row] = [
                entry - value * pivot_entry
                for entry, pivot_entry in zip(
                    matrix[row], matrix[pivot_row], strict=True
                )
            ]
        pivot_row += 1
    return pivot_row


def affine_rank(points: Sequence[Sequence[int]]) -> int:
    anchor = points[0]
    return rational_rank(
        tuple(value - base for value, base in zip(point, anchor, strict=True))
        for point in points[1:]
    )


def line_signature(term: A2CompletionPairAtom) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Canonical Pluecker-style key for the affine line through an atom."""

    direction = primitive(completion_difference(term), canonical_sign=True)
    point = term.first_completion
    wedge = tuple(
        point[first] * direction[second] - point[second] * direction[first]
        for first, second in combinations(range(4), 2)
    )
    return direction, wedge


@dataclass(frozen=True)
class CandidateSummary:
    name: str
    cell_packet_pieces: int
    nontrivial_packet_pieces: int
    retained_nontrivial_mass: int
    singleton_remainder_mass: int
    maximum_packet_terms: int
    maximum_schur_bound_squared: int
    unit_balance_a4_upper: int

    @property
    def retained_fraction(self) -> Fraction:
        return Fraction(
            self.retained_nontrivial_mass,
            self.retained_nontrivial_mass + self.singleton_remainder_mass,
        )


def candidate_summary(
    cells: Sequence[A2PacketCell],
    *,
    name: str,
    signature: Callable[[A2CompletionPairAtom], Hashable],
) -> CandidateSummary:
    """Group within signed cells and replay exact Schur and unit A4 loads."""

    packet_pieces = 0
    nontrivial_pieces = 0
    retained = 0
    remainder = 0
    maximum_terms = 0
    maximum_bound_squared = 0
    worst_a4 = 0
    for cell in cells:
        grouped: dict[Hashable, list[A2CompletionPairAtom]] = defaultdict(list)
        for term in cell.terms:
            grouped[signature(term)].append(term)
        packet_pieces += len(grouped)
        left_a4: Counter[tuple[int, int]] = Counter()
        right_a4: Counter[tuple[int, int]] = Counter()
        for terms in grouped.values():
            size = len(terms)
            maximum_terms = max(maximum_terms, size)
            if size >= 2:
                nontrivial_pieces += 1
                retained += size
            else:
                remainder += 1
            left_degrees = Counter(term.left_vertex for term in terms)
            right_degrees = Counter(term.right_vertex for term in terms)
            bound_squared = max(left_degrees.values()) * max(right_degrees.values())
            maximum_bound_squared = max(maximum_bound_squared, bound_squared)
            for vertex in left_degrees:
                left_a4[vertex] += 1
            for vertex in right_degrees:
                right_a4[vertex] += bound_squared
        worst_a4 = max(
            worst_a4,
            max(left_a4.values(), default=0) * max(right_a4.values(), default=0),
        )
    return CandidateSummary(
        name=name,
        cell_packet_pieces=packet_pieces,
        nontrivial_packet_pieces=nontrivial_pieces,
        retained_nontrivial_mass=retained,
        singleton_remainder_mass=remainder,
        maximum_packet_terms=maximum_terms,
        maximum_schur_bound_squared=maximum_bound_squared,
        unit_balance_a4_upper=worst_a4,
    )


def main() -> None:
    degree = exact_balanced_degree(Q)
    core = build_four_cycle_core(
        Q,
        width=0.2,
        cutoff=40.0,
        kind="prime_powers",
        quadrature_order=32,
    )
    groups = completion_groups_from_generic_rectangles(enumerate_rectangles(core))
    repeated = {
        colors: tuple(completions)
        for colors, completions in groups.items()
        if len(completions) >= 2
    }
    cells = extract_exact_secant_a2_cells(
        q=Q,
        degree_parameter=degree,
        completion_groups=groups,
        source_id="affine-compression-falsifier-q25013-U40",
        parent_masks=(core.values, core.values, core.values, core.values),
    )
    atoms = tuple(term for cell in cells for term in cell.terms)

    multiplicities = Counter(map(len, repeated.values()))
    ranks = Counter((len(points), affine_rank(points)) for points in repeated.values())
    rich_lines = sum(
        1
        for points in repeated.values()
        if len(points) >= 3 and affine_rank(points) == 1
    )
    if multiplicities != Counter({2: 2_670, 3: 40, 4: 2}):
        raise SystemExit("FAIL: repeated-fibre histogram changed")
    if ranks != Counter({(2, 1): 2_670, (3, 2): 40, (4, 3): 2}):
        raise SystemExit("FAIL: exact affine-rank profile changed")
    if rich_lines:
        raise SystemExit("FAIL: a rich completion line unexpectedly appeared")

    # A nontrivial affine two-plane is pinned by three noncollinear points.
    # Every multiplicity-three fibre supplies one such plane.  Each of the
    # rank-three four-point fibres supplies four distinct triangle planes;
    # every point belongs to three of them and every ordered pair to two.
    direct_completion_occurrences = sum(map(len, repeated.values()))
    rich_plane_candidates = multiplicities[3] + 4 * multiplicities[4]
    rich_plane_direct_incidences = 3 * rich_plane_candidates
    rich_plane_unique_direct_mass = 3 * multiplicities[3] + 4 * multiplicities[4]
    rich_plane_unique_factorial_mass = (
        6 * multiplicities[3] + 12 * multiplicities[4]
    )
    if (
        direct_completion_occurrences,
        rich_plane_candidates,
        rich_plane_direct_incidences,
        rich_plane_unique_direct_mass,
        rich_plane_unique_factorial_mass,
    ) != (5_468, 48, 144, 128, 264):
        raise SystemExit("FAIL: pre-factorial plane profile changed")

    # A genuine stopping-time cannot keep all four triangle planes at full
    # weight.  Choosing one maximal plane per high-multiplicity fibre keeps
    # three completion occurrences and the six ordered pairs internal to it.
    one_plane_direct_mass = 3 * (multiplicities[3] + multiplicities[4])
    one_plane_factorial_mass = 6 * (multiplicities[3] + multiplicities[4])
    if (one_plane_direct_mass, one_plane_factorial_mass) != (126, 252):
        raise SystemExit("FAIL: one-plane stopping profile changed")

    unoriented_atoms: dict[
        tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]],
        A2CompletionPairAtom,
    ] = {}
    for term in atoms:
        first, second = sorted((term.first_completion, term.second_completion))
        unoriented_atoms.setdefault((term.colors, first, second), term)
    line_counts = Counter(line_signature(term) for term in unoriented_atoms.values())
    if len(unoriented_atoms) != 2_802 or len(line_counts) != 2_802:
        raise SystemExit("FAIL: two distinct unoriented atoms now share an affine line")

    summaries = (
        candidate_summary(cells, name="exact primitive 4-direction", signature=exact_direction),
        candidate_summary(cells, name="optimistic rank-one direction", signature=rank_one_direction),
        candidate_summary(cells, name="sign-cone control", signature=sign_cone),
        candidate_summary(cells, name="whole-cell control", signature=one_cell_packet),
    )
    exact, rank_one, sign_control, cell_control = summaries
    expected = (
        (5_580, 8, 32, 5_572, 10, 2, 4),
        (5_556, 12, 60, 5_544, 10, 2, 4),
        (490, 370, 5_484, 120, 102, 4, 6),
        (308, 240, 5_536, 68, 186, 4, 4),
    )
    actual = tuple(
        (
            summary.cell_packet_pieces,
            summary.nontrivial_packet_pieces,
            summary.retained_nontrivial_mass,
            summary.singleton_remainder_mass,
            summary.maximum_packet_terms,
            summary.maximum_schur_bound_squared,
            summary.unit_balance_a4_upper,
        )
        for summary in summaries
    )
    if actual != expected:
        raise SystemExit(f"FAIL: candidate profiles changed: {actual!r}")

    largest = max(cells, key=lambda cell: len(cell.terms))
    largest_groups: dict[Hashable, list[A2CompletionPairAtom]] = defaultdict(list)
    for term in largest.terms:
        largest_groups[rank_one_direction(term)].append(term)
    largest_affine = max(map(len, largest_groups.values()))
    if (
        len(largest.terms),
        len(largest_groups),
        largest_affine,
    ) != (186, 177, 10):
        raise SystemExit("FAIL: largest-cell affine profile changed")

    # For the nontrivial rank-one packets alone, unit balance gives two.
    # A packet with squared Schur charge two also forces a lower bound two,
    # so this worst extracted-packet A4 value is exact.
    extracted_worst_a4 = 0
    for cell in cells:
        grouped: dict[Hashable, list[A2CompletionPairAtom]] = defaultdict(list)
        for term in cell.terms:
            grouped[rank_one_direction(term)].append(term)
        left: Counter[tuple[int, int]] = Counter()
        right: Counter[tuple[int, int]] = Counter()
        for terms in grouped.values():
            if len(terms) < 2:
                continue
            left_degrees = Counter(term.left_vertex for term in terms)
            right_degrees = Counter(term.right_vertex for term in terms)
            bound_squared = max(left_degrees.values()) * max(right_degrees.values())
            for vertex in left_degrees:
                left[vertex] += 1
            for vertex in right_degrees:
                right[vertex] += bound_squared
        extracted_worst_a4 = max(
            extracted_worst_a4,
            max(left.values(), default=0) * max(right.values(), default=0),
        )
    if extracted_worst_a4 != 2:
        raise SystemExit("FAIL: extracted affine-packet A4 profile changed")

    # Remove the union of all nontrivially pinned plane fibres.  The exact
    # residual is the multiplicity-two sector.  It still has a raw cell above
    # D0, but its A4 coefficient is tiny and hence it is not a certified
    # all-plus excess core.
    residual_cells = tuple(
        replace(
            cell,
            terms=tuple(
                term for term in cell.terms if len(groups[term.colors]) == 2
            ),
        )
        for cell in cells
        if any(len(groups[term.colors]) == 2 for term in cell.terms)
    )
    residual_mass = sum(len(cell.terms) for cell in residual_cells)
    residual_rank_one = candidate_summary(
        residual_cells,
        name="post-rich-plane rank-one residual",
        signature=rank_one_direction,
    )
    residual_largest = max(residual_cells, key=lambda cell: len(cell.terms))
    residual_projection_sizes = tuple(
        len({term.colors[position] for term in residual_largest.terms})
        for position in range(4)
    )
    if (
        residual_mass,
        len(residual_cells),
        len(residual_largest.terms),
        residual_rank_one.cell_packet_pieces,
        residual_rank_one.nontrivial_packet_pieces,
        residual_rank_one.retained_nontrivial_mass,
        residual_rank_one.singleton_remainder_mass,
        residual_rank_one.unit_balance_a4_upper,
        residual_projection_sizes,
    ) != (5_340, 298, 176, 5_300, 12, 52, 5_288, 4, (72, 134, 134, 70)):
        raise SystemExit("FAIL: post-plane residual profile changed")

    # Combine all pinned planes (half weight on the four-point triangle
    # planes) with nontrivial parallel rank-one directions in the remaining
    # multiplicity-two sector.  This is the strongest literal structured
    # candidate produced by the audit.  Packet pieces are intersected with
    # signed cells exactly as A4 requires.
    structured_weight = Fraction(0)
    structured_unique_terms: Counter[tuple[tuple[int, int, int, int], int]] = Counter()
    structured_piece_count = 0
    plane_piece_count = 0
    direction_piece_count = 0
    structured_allocations = 0
    structured_maximum_terms = 0
    structured_maximum_bound_squared = Fraction(0)
    structured_a4_upper = Fraction(0)
    final_residual_terms: list[A2CompletionPairAtom] = []
    for cell in cells:
        packet_allocations: dict[
            Hashable, list[tuple[A2CompletionPairAtom, Fraction]]
        ] = defaultdict(list)
        for term in cell.terms:
            completions = tuple(groups[term.colors])
            if len(completions) == 3:
                packet_allocations[
                    ("plane", term.colors, completions)
                ].append((term, Fraction(1)))
            elif len(completions) == 4:
                for triangle in combinations(completions, 3):
                    if (
                        term.first_completion in triangle
                        and term.second_completion in triangle
                    ):
                        packet_allocations[
                            ("plane", term.colors, triangle)
                        ].append((term, Fraction(1, 2)))
        residual_by_direction: dict[
            Hashable, list[A2CompletionPairAtom]
        ] = defaultdict(list)
        for term in cell.terms:
            if len(groups[term.colors]) == 2:
                residual_by_direction[rank_one_direction(term)].append(term)
        for direction, terms in residual_by_direction.items():
            if len(terms) >= 2:
                packet_allocations[("direction", direction)].extend(
                    (term, Fraction(1)) for term in terms
                )
            else:
                final_residual_terms.extend(terms)

        structured_piece_count += len(packet_allocations)
        plane_piece_count += sum(
            packet_id[0] == "plane" for packet_id in packet_allocations
        )
        direction_piece_count += sum(
            packet_id[0] == "direction" for packet_id in packet_allocations
        )
        left_a4: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
        right_a4: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
        for allocations in packet_allocations.values():
            structured_allocations += len(allocations)
            structured_maximum_terms = max(
                structured_maximum_terms, len(allocations)
            )
            edge_weights: dict[
                tuple[tuple[int, int], tuple[int, int]], Fraction
            ] = defaultdict(Fraction)
            for term, weight in allocations:
                structured_weight += weight
                structured_unique_terms[(cell.signed_cell, term.term_id)] += 1
                edge_weights[term.left_vertex, term.right_vertex] += weight
            left_sums: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
            right_sums: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
            for (left, right), weight in edge_weights.items():
                left_sums[left] += weight
                right_sums[right] += weight
            bound_squared = max(left_sums.values()) * max(right_sums.values())
            structured_maximum_bound_squared = max(
                structured_maximum_bound_squared, bound_squared
            )
            for vertex in left_sums:
                left_a4[vertex] += 1
            for vertex in right_sums:
                right_a4[vertex] += bound_squared
        structured_a4_upper = max(
            structured_a4_upper,
            max(left_a4.values(), default=Fraction(0))
            * max(right_a4.values(), default=Fraction(0)),
        )

    final_residual_a4 = 0
    for cell in cells:
        terms = [
            term
            for term in final_residual_terms
            if term in cell.terms
        ]
        left = Counter(term.left_vertex for term in terms)
        right = Counter(term.right_vertex for term in terms)
        final_residual_a4 = max(
            final_residual_a4,
            max(left.values(), default=0) * max(right.values(), default=0),
        )
    if (
        structured_piece_count,
        plane_piece_count,
        direction_piece_count,
        structured_allocations,
        structured_weight,
        len(structured_unique_terms),
        Counter(structured_unique_terms.values()),
        structured_maximum_terms,
        structured_maximum_bound_squared,
        structured_a4_upper,
        len(final_residual_terms),
        final_residual_a4,
    ) != (
        292,
        280,
        12,
        340,
        Fraction(316),
        316,
        Counter({1: 292, 2: 24}),
        10,
        Fraction(2),
        Fraction(9, 2),
        5_288,
        4,
    ):
        raise SystemExit("FAIL: combined structured decomposition changed")

    print("PASS literal affine-compression candidate/falsifier audit")
    print(
        "source: "
        f"q={Q}, D0={degree}, cells={len(cells)}, atoms={len(atoms)}, "
        f"repeated_fibres={len(repeated)}, multiplicities={dict(multiplicities)}"
    )
    print(
        "affine ranks: "
        f"{dict(sorted(ranks.items()))}, rich_lines={rich_lines}, "
        f"unoriented_atoms={len(unoriented_atoms)}, distinct_exact_lines={len(line_counts)}"
    )
    print(
        "pre-factorial pinned planes: "
        f"direct_occurrences={direct_completion_occurrences}, "
        f"candidate_planes={rich_plane_candidates}, "
        f"direct_incidences={rich_plane_direct_incidences}, "
        f"unique_direct_mass={rich_plane_unique_direct_mass}, "
        f"unique_factorial_mass={rich_plane_unique_factorial_mass}, "
        "max_direct_overlap=3, max_factorial_overlap=2"
    )
    print(
        "one-plane stopping split: "
        f"direct_mass={one_plane_direct_mass}/{direct_completion_occurrences}, "
        f"factorial_mass={one_plane_factorial_mass}/{len(atoms)}, "
        f"factorial_remainder={len(atoms) - one_plane_factorial_mass}"
    )
    for summary in summaries:
        print(
            f"{summary.name}: pieces={summary.cell_packet_pieces}, "
            f"nontrivial_pieces={summary.nontrivial_packet_pieces}, "
            f"retained={summary.retained_nontrivial_mass}/{len(atoms)} "
            f"({float(summary.retained_fraction):.9f}), "
            f"remainder={summary.singleton_remainder_mass}, "
            f"max_terms={summary.maximum_packet_terms}, "
            f"max_a2={summary.maximum_schur_bound_squared}, "
            f"unit_A4={summary.unit_balance_a4_upper}/{degree**2}"
        )
    print(
        "largest raw-count cell: "
        f"cell={largest.signed_cell}, atoms={len(largest.terms)}>D0={degree}, "
        f"rank-one pieces={len(largest_groups)}, largest_piece={largest_affine}, "
        f"retained_fraction={Fraction(largest_affine, len(largest.terms))}"
    )
    print(
        "nontrivial rank-one extraction: "
        f"packets={rank_one.nontrivial_packet_pieces}, "
        f"mass={rank_one.retained_nontrivial_mass}, "
        f"compression={Fraction(rank_one.retained_nontrivial_mass, rank_one.nontrivial_packet_pieces)}, "
        f"overlap=1, exact_worst_A4={extracted_worst_a4}/{degree**2}"
    )
    print(
        "post-rich-plane residual: "
        f"mass={residual_mass}, cells={len(residual_cells)}, "
        f"largest_cell={len(residual_largest.terms)}>D0={degree}, "
        f"largest_projection_sizes={residual_projection_sizes}, "
        f"rank-one_retained={residual_rank_one.retained_nontrivial_mass}, "
        f"rank-one_remainder={residual_rank_one.singleton_remainder_mass}, "
        f"unit_A4={residual_rank_one.unit_balance_a4_upper}/{degree**2}"
    )
    print(
        "combined plane+direction split: "
        f"structured_mass={structured_weight}, unique_terms={len(structured_unique_terms)}, "
        f"cell_packet_pieces={structured_piece_count} "
        f"(plane={plane_piece_count}, direction={direction_piece_count}), "
        f"allocations={structured_allocations}, overlap_hist={dict(Counter(structured_unique_terms.values()))}, "
        f"unit_A4={structured_a4_upper}/{degree**2}, "
        f"final_residual={len(final_residual_terms)}, residual_A4={final_residual_a4}/{degree**2}"
    )


if __name__ == "__main__":
    main()
