import json
from dataclasses import replace
from fractions import Fraction

import pytest

from qp_a2_packet_serialization import (
    A2Packet,
    A2PacketAllocation,
    A2RemainderAllocation,
    deserialize_a2_packet_cell,
    extract_exact_secant_a2_cells,
    serialize_a2_packet_cell,
    validate_a2_packet_cell,
)
from qp_a4_serialized_participation import (
    bracket_a4,
    certify_a4_dual,
    certify_a4_primal,
    summarize_a4_unit_balances,
)
from qp_actual_prime_nds import exact_balanced_degree


def _two_edge_exact_secant_cells():
    completions = ((3, 5, 7, 11), (5, 8, 11, 17))
    return extract_exact_secant_a2_cells(
        q=10_007,
        degree_parameter=exact_balanced_degree(10_007),
        completion_groups={
            (101, 103, 107, 109): completions,
            (113, 127, 131, 137): completions,
        },
        source_id="unit-two-edge-fixed-secant",
    )


def test_a2_exact_secant_extractor_preserves_atoms_masks_and_multiplicity() -> None:
    cells = _two_edge_exact_secant_cells()
    assert len(cells) == 2
    for cell in cells:
        ledger = validate_a2_packet_cell(cell)
        assert ledger.term_count == 2
        assert ledger.packet_count == 1
        assert ledger.packet_allocations == 2
        assert ledger.source_weight == 2
        assert ledger.packet_weight == 2
        assert ledger.remainder_weight == 0
        assert ledger.maximum_overlap_multiplicity == 1
        assert ledger.maximum_packet_terms == 2
        assert ledger.all_source_weight_accounted_for
        packet = cell.packets[0]
        assert packet.schur_max_left_sum == 1
        assert packet.schur_max_right_sum == 1
        assert packet.norm_bound_squared == 1
        assert len(packet.left_support) == len(packet.right_support) == 2
    assert cells[0].terms[0].first_completion == (
        cells[1].terms[0].second_completion
    )
    assert cells[0].terms[0].secants == tuple(
        -value for value in cells[1].terms[0].secants
    )


def test_a2_json_round_trip_is_exact_and_hash_protected() -> None:
    cell = _two_edge_exact_secant_cells()[0]
    serialized = serialize_a2_packet_cell(cell)
    assert deserialize_a2_packet_cell(serialized) == cell
    assert serialize_a2_packet_cell(deserialize_a2_packet_cell(serialized)) == serialized

    envelope = json.loads(serialized)
    envelope["payload"]["degree_parameter"] += 1
    with pytest.raises(ValueError, match="hash"):
        deserialize_a2_packet_cell(json.dumps(envelope))


def test_a2_validator_rejects_missing_mass_wrong_masks_and_bad_schur_data() -> None:
    cell = _two_edge_exact_secant_cells()[0]
    packet = cell.packets[0]
    missing = replace(
        cell,
        packets=(replace(packet, allocations=packet.allocations[:1]),),
    )
    with pytest.raises(ValueError):
        validate_a2_packet_cell(missing)

    masks = list(cell.masks)
    masks[0] = tuple(value for value in masks[0] if value != cell.terms[0].colors[0])
    with pytest.raises(ValueError, match="mask"):
        validate_a2_packet_cell(replace(cell, masks=tuple(masks)))

    bad_bound = replace(
        cell,
        packets=(
            replace(packet, norm_bound_squared=packet.norm_bound_squared + 1),
        ),
    )
    with pytest.raises(ValueError, match="Schur bound"):
        validate_a2_packet_cell(bad_bound)


def test_a2_records_fractional_overlap_and_explicit_remainder_exactly() -> None:
    cell = _two_edge_exact_secant_cells()[0]
    packet = cell.packets[0]
    first, second = packet.allocations
    split_packet = A2Packet(
        packet_id="split-copy",
        kind=packet.kind,
        secants=packet.secants,
        allocations=(A2PacketAllocation(first.term_id, Fraction(1, 2)),),
        left_support=(cell.terms[first.term_id].left_vertex,),
        right_support=(cell.terms[first.term_id].right_vertex,),
        schur_max_left_sum=Fraction(1, 2),
        schur_max_right_sum=Fraction(1, 2),
        norm_bound_squared=Fraction(1, 4),
    )
    retained = replace(
        packet,
        allocations=(
            A2PacketAllocation(first.term_id, Fraction(1, 2)),
            second,
        ),
    )
    overlap = replace(
        cell,
        packets=(retained, split_packet),
        overlap_multiplicities=((first.term_id, 2), (second.term_id, 1)),
    )
    ledger = validate_a2_packet_cell(overlap)
    assert ledger.maximum_overlap_multiplicity == 2
    assert ledger.packet_weight == ledger.source_weight == 2

    second_term = cell.terms[second.term_id]
    remainder_packet = replace(
        packet,
        allocations=(second,),
        left_support=(second_term.left_vertex,),
        right_support=(second_term.right_vertex,),
    )
    with_remainder = replace(
        cell,
        packets=(remainder_packet,),
        remainder=(
            A2RemainderAllocation(first.term_id, Fraction(1), "test remainder"),
        ),
        overlap_multiplicities=((first.term_id, 0), (second.term_id, 1)),
    )
    remainder_ledger = validate_a2_packet_cell(with_remainder)
    assert remainder_ledger.remainder_weight == 1
    with pytest.raises(ValueError, match="zero-remainder"):
        certify_a4_primal(with_remainder)


def test_a4_exact_primal_and_dual_certificates_match_on_one_packet() -> None:
    cell = _two_edge_exact_secant_cells()[0]
    primal = certify_a4_primal(cell)
    packet = cell.packets[0]
    dual = certify_a4_dual(
        cell,
        left_probabilities={packet.left_support[0]: Fraction(1)},
        right_probabilities={packet.right_support[0]: Fraction(1)},
        packet_slacks={packet.packet_id: Fraction(1)},
    )
    bracket = bracket_a4(primal, dual)
    assert bracket.lower_bound == bracket.upper_bound == 1
    assert bracket.upper_meets_target

    other_primal = certify_a4_primal(_two_edge_exact_secant_cells()[1])
    with pytest.raises(ValueError, match="different cells"):
        bracket_a4(other_primal, dual)

    with pytest.raises(ValueError, match="quadratic"):
        certify_a4_dual(
            cell,
            left_probabilities={packet.left_support[0]: Fraction(1)},
            right_probabilities={packet.right_support[0]: Fraction(1)},
            packet_slacks={packet.packet_id: Fraction(2)},
        )


def test_actual_prime_triangle_serializes_all_six_ordered_pairs() -> None:
    q = 11_801
    cells = extract_exact_secant_a2_cells(
        q=q,
        degree_parameter=exact_balanced_degree(q),
        completion_groups={
            (6337, 5717, 5479, 4943): (
                (5171, 5981, 6269, 6949),
                (5821, 6733, 5569, 6173),
                (5861, 6779, 5531, 6131),
            )
        },
        source_id="literal-all-prime-three-completion-fixture",
    )
    summary = summarize_a4_unit_balances(cells)
    assert summary.cell_count == 6
    assert summary.term_count == 6
    assert summary.packet_count == 6
    assert summary.maximum_packet_terms == 1
    assert summary.worst_upper_bound == 1
    assert summary.every_cell_meets_target
