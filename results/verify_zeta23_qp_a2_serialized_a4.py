#!/usr/bin/env python3
"""Build literal A2 packet cells and replay the exact A4 certificate.

Two sources are checked.

* A compact all-prime four-completion fixture gives twelve ordered positive
  factorial atoms and is convenient for inspecting JSON round trips.
* The full materialized q=25013, U=40 actual-prime-power diagnostic core
  gives 5,604 generic ordered atoms across 308 signed dyadic cells.

The packetization is by exact carrier secant inside each cell.  This is a
legal fixed-layer A2 baseline, not the open affine/Hankel inverse theorem.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_a2_packet_serialization import (  # noqa: E402
    deserialize_a2_packet_cell,
    extract_exact_secant_a2_cells,
    serialize_a2_packet_cell,
    validate_a2_packet_cell,
)
from qp_a4_serialized_participation import (  # noqa: E402
    bracket_a4,
    certify_a4_dual,
    certify_a4_primal,
    summarize_a4_unit_balances,
)
from qp_actual_prime_nds import exact_balanced_degree  # noqa: E402
from qp_four_cycle_h_graph_lab import enumerate_rectangles  # noqa: E402
from qp_four_cycle_hostile_lab import (  # noqa: E402
    build_four_cycle_core,
    is_prime,
)
from qp_four_cycle_weighted_secant_lab import (  # noqa: E402
    completion_groups_from_generic_rectangles,
)


COMPACT_Q = 25_013
COMPACT_COLORS = (13_103, 12_659, 10_799, 10_433)
COMPACT_COMPLETIONS = (
    (10_903, 13_229, 13_693, 14_173),
    (11_483, 13_933, 13_001, 13_457),
    (11_681, 14_173, 12_781, 13_229),
    (11_743, 14_249, 12_713, 13_159),
)


def exact_hard_window_radius(
    q: int,
    colors: tuple[int, int, int, int],
    completions: tuple[tuple[int, int, int, int], ...],
) -> tuple[int, int]:
    """Return the largest residual and its least integral q-normalization."""

    c11, c12, c21, c22 = colors
    residuals: list[int] = []
    for a1, a2, b1, b2 in completions:
        residuals.extend(
            (
                abs(8 * a1 * b1 * c11 - q**3),
                abs(8 * a1 * b2 * c12 - q**3),
                abs(8 * a2 * b1 * c21 - q**3),
                abs(8 * a2 * b2 * c22 - q**3),
            )
        )
    maximum = max(residuals)
    return maximum, (maximum + q - 1) // q


def main() -> None:
    degree = exact_balanced_degree(COMPACT_Q)
    compact_nodes = COMPACT_COLORS + tuple(
        value for completion in COMPACT_COMPLETIONS for value in completion
    )
    if any(
        len(set(COMPACT_COLORS + completion)) != 8
        for completion in COMPACT_COMPLETIONS
    ):
        raise SystemExit("FAIL: a compact completion left the generic sector")
    if not all(is_prime(value) for value in compact_nodes):
        raise SystemExit("FAIL: the compact fixture contains a nonprime node")
    maximum_residual, compact_radius = exact_hard_window_radius(
        COMPACT_Q, COMPACT_COLORS, COMPACT_COMPLETIONS
    )
    if (maximum_residual, compact_radius) != (342_803_781, 13_706):
        raise SystemExit("FAIL: the compact hard-window radius changed")

    compact_cells = extract_exact_secant_a2_cells(
        q=COMPACT_Q,
        degree_parameter=degree,
        completion_groups={COMPACT_COLORS: COMPACT_COMPLETIONS},
        source_id="literal-all-prime-q25013-four-completion-fibre",
    )
    compact_summary = summarize_a4_unit_balances(compact_cells)
    if compact_cells[0].hard_window_radius != compact_radius:
        raise SystemExit("FAIL: the compact serialized hard window changed")
    if (
        compact_summary.cell_count,
        compact_summary.term_count,
        compact_summary.packet_count,
        compact_summary.worst_upper_bound,
    ) != (8, 12, 12, Fraction(4)):
        raise SystemExit("FAIL: the compact A2/A4 profile changed")
    for cell in compact_cells:
        serialized = serialize_a2_packet_cell(cell)
        if deserialize_a2_packet_cell(serialized) != cell:
            raise SystemExit("FAIL: compact A2 JSON did not round-trip")
    compact_worst = next(
        cell
        for cell in compact_cells
        if certify_a4_primal(cell).upper_bound == 4
    )
    common_left = compact_worst.packets[0].left_support[0]
    common_right = compact_worst.packets[0].right_support[0]
    common_packets = {
        packet.packet_id: Fraction(1)
        for packet in compact_worst.packets
        if common_left in packet.left_support
        and common_right in packet.right_support
    }
    compact_bracket = bracket_a4(
        certify_a4_primal(compact_worst),
        certify_a4_dual(
            compact_worst,
            left_probabilities={common_left: Fraction(1)},
            right_probabilities={common_right: Fraction(1)},
            packet_slacks=common_packets,
        ),
    )
    if compact_bracket.lower_bound != compact_bracket.upper_bound or (
        compact_bracket.upper_bound != 4
    ):
        raise SystemExit("FAIL: the compact worst-cell A4 optimum changed")

    core = build_four_cycle_core(
        COMPACT_Q,
        width=0.2,
        cutoff=40.0,
        kind="prime_powers",
        quadrature_order=32,
    )
    rectangles = enumerate_rectangles(core)
    groups = completion_groups_from_generic_rectangles(rectangles)
    if groups.get(COMPACT_COLORS) != COMPACT_COMPLETIONS:
        raise SystemExit("FAIL: the compact fibre is not exhaustive in the full core")
    multiplicities = Counter(map(len, groups.values()))
    repeated_groups = {
        colors: completions
        for colors, completions in groups.items()
        if len(completions) >= 2
    }
    expected_terms = sum(
        len(completions) * (len(completions) - 1)
        for completions in groups.values()
    )
    full_cells = extract_exact_secant_a2_cells(
        q=COMPACT_Q,
        degree_parameter=degree,
        completion_groups=groups,
        source_id="materialized-actual-prime-power-q25013-U40-generic-core",
        parent_masks=(core.values, core.values, core.values, core.values),
    )
    ledgers = tuple(validate_a2_packet_cell(cell) for cell in full_cells)
    full_summary = summarize_a4_unit_balances(full_cells)

    if len(rectangles) != 150_672 or len(groups) != 127_092:
        raise SystemExit("FAIL: the materialized rectangle source changed")
    if len(repeated_groups) != 2_712:
        raise SystemExit("FAIL: the repeated color-fibre count changed")
    if {
        multiplicity: count
        for multiplicity, count in multiplicities.items()
        if multiplicity >= 2
    } != {2: 2_670, 3: 40, 4: 2}:
        raise SystemExit("FAIL: the completion multiplicity histogram changed")
    if expected_terms != 5_604 or expected_terms != full_summary.term_count:
        raise SystemExit("FAIL: A2 did not retain every ordered generic atom")
    if any(ledger.remainder_weight for ledger in ledgers):
        raise SystemExit("FAIL: the full A2 generic-sector cover has a remainder")
    if any(
        packet.norm_bound_squared != 1
        for cell in full_cells
        for packet in cell.packets
    ):
        raise SystemExit("FAIL: a fixed-secant packet lost its unit Schur bound")
    if (
        full_summary.cell_count,
        full_summary.packet_count,
        full_summary.maximum_packet_terms,
        full_summary.worst_upper_bound,
        full_summary.target,
    ) != (308, 5_596, 2, Fraction(4), Fraction(18_225)):
        raise SystemExit("FAIL: the full serialized A4 profile changed")
    if not full_summary.every_cell_meets_target:
        raise SystemExit("FAIL: a serialized actual cell violates A4")
    if any(cell.hard_window_radius != 15_506 for cell in full_cells):
        raise SystemExit("FAIL: the full exact hard-window radius changed")

    full_exact_worst = None
    for cell in full_cells:
        primal = certify_a4_primal(cell)
        if primal.upper_bound != full_summary.worst_upper_bound:
            continue
        for left in sorted(
            {vertex for packet in cell.packets for vertex in packet.left_support}
        ):
            for right in sorted(
                {vertex for packet in cell.packets for vertex in packet.right_support}
            ):
                common = {
                    packet.packet_id: Fraction(1)
                    for packet in cell.packets
                    if packet.norm_bound_squared == 1
                    and left in packet.left_support
                    and right in packet.right_support
                }
                if len(common) != 2:
                    continue
                candidate = bracket_a4(
                    primal,
                    certify_a4_dual(
                        cell,
                        left_probabilities={left: Fraction(1)},
                        right_probabilities={right: Fraction(1)},
                        packet_slacks=common,
                    ),
                )
                if candidate.lower_bound == candidate.upper_bound == 4:
                    full_exact_worst = candidate
                    break
            if full_exact_worst is not None:
                break
        if full_exact_worst is not None:
            break
    if full_exact_worst is None:
        raise SystemExit("FAIL: no exact full-core worst-cell dual was found")

    largest = max(full_cells, key=lambda cell: len(cell.terms))
    if len(largest.terms) != 186 or len(largest.packets) != 185:
        raise SystemExit("FAIL: the largest serialized cell changed")
    largest_json = serialize_a2_packet_cell(largest)
    if deserialize_a2_packet_cell(largest_json) != largest:
        raise SystemExit("FAIL: the largest A2 JSON did not round-trip")

    print("PASS literal A2 serialization and exact A4 replay")
    print(
        "compact all-prime fibre: "
        f"q={COMPACT_Q}, D0={degree}, hard_D={compact_radius}, "
        f"terms={compact_summary.term_count}, cells={compact_summary.cell_count}, "
        f"packets={compact_summary.packet_count}, "
        f"exact_worst_A4={compact_bracket.upper_bound}/{compact_summary.target}"
    )
    print(
        "full actual-prime-power core: "
        f"rectangles={len(rectangles)}, color_fibres={len(groups)}, "
        f"repeated_fibres={len(repeated_groups)}, "
        f"multiplicities={dict(sorted(multiplicities.items()))}"
    )
    print(
        "serialized generic sector: "
        f"hard_D={full_cells[0].hard_window_radius}, "
        f"terms={full_summary.term_count}, cells={full_summary.cell_count}, "
        f"packets={full_summary.packet_count}, "
        f"max_packet_terms={full_summary.maximum_packet_terms}, "
        f"zero_remainder={sum(ledger.remainder_weight for ledger in ledgers) == 0}"
    )
    print(
        "A4 unit-balance certificate: "
        f"max_left={full_summary.maximum_left_load}, "
        f"max_right={full_summary.maximum_right_load}, "
        f"exact_worst={full_exact_worst.upper_bound}, "
        f"target={full_summary.target}, "
        f"ratio={full_summary.worst_target_ratio}, "
        f"passes={full_summary.every_cell_meets_target}"
    )
    print(
        "largest JSON round-trip: "
        f"cell={largest.signed_cell}, terms={len(largest.terms)}, "
        f"packets={len(largest.packets)}, bytes={len(largest_json)}"
    )


if __name__ == "__main__":
    main()
