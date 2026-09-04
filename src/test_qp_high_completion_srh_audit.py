from fractions import Fraction

from qp_high_completion_srh_audit import (
    actual_q25013_scattered_fixture,
    primitive_relation,
    srh_capacity_ledger,
)


def test_capacity_closes_exactly_at_subpower_union_and_relations() -> None:
    ledger = srh_capacity_ledger(
        multiplicity=Fraction(5, 16),
        residual_union=Fraction(5, 16),
        relation_multiplicity=Fraction(0),
    )
    assert ledger.reciprocal_height_exponent == Fraction(5, 8)
    assert ledger.tail_exponent == ledger.desired_tail_exponent == Fraction(11, 16)
    assert ledger.excess_exponent == 0


def test_capacity_records_both_union_and_plane_losses() -> None:
    ledger = srh_capacity_ledger(
        multiplicity=Fraction(5, 16),
        residual_union=Fraction(6, 16),
        relation_multiplicity=Fraction(3, 16),
    )
    assert ledger.excess_exponent == Fraction(3, 16)


def test_actual_scattered_fixture_has_four_distinct_relations() -> None:
    ledger = actual_q25013_scattered_fixture()
    assert ledger.determinant == -942
    assert len(ledger.completions) == 4
    assert ledger.affine_rank == 3
    assert sorted(ledger.relation_heights) == [215, 301, 482, 725]
    assert len(set(ledger.relation_vectors)) == 4
    assert abs(ledger.reciprocal_height_mass - 0.011427421068418382) < 1.0e-15


def test_primitive_relation_is_scale_invariant() -> None:
    relation, height = primitive_relation(((2, 3), (5, 7), (11, 13)))
    scaled, scaled_height = primitive_relation(((4, 6), (10, 14), (22, 26)))
    assert scaled == relation
    assert scaled_height == height
