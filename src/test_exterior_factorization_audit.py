from fractions import Fraction

from exterior_factorization_audit import (
    audit_ledger,
    closed_unbounded_coordinate,
    dense_core_false_positive,
    nonclosable_psd_sequence,
    same_old_block_different_charge,
    scalar_contact,
    uniform_factor_blowup,
)


Q = Fraction


def test_same_old_and_collar_blocks_do_not_determine_charge() -> None:
    ledger = same_old_block_different_charge()
    assert ledger.old_positive_value == 1
    assert ledger.old_null_value == 0
    assert ledger.collar_value == 1
    assert ledger.uncharged_null_charge == 0
    assert ledger.charged_null_charge == 1
    assert ledger.charged_null_collar_determinant == -1
    assert ledger.charged_negative_direction_value == -1


def test_scalar_contact_is_psd_schur_equality() -> None:
    for epsilon in (Q(3, 5), Q(1, 10), Q(0)):
        ledger = scalar_contact(epsilon)
        assert ledger.old_block >= 0
        assert ledger.collar_block >= 0
        assert ledger.determinant == 0
        assert ledger.schur_square_root_identity_defect == 0


def test_linear_factor_through_a_blows_up_at_contact() -> None:
    epsilons = (Q(1, 2), Q(1, 4), Q(1, 8))
    assert uniform_factor_blowup(epsilons) == (Q(2), Q(4), Q(8))
    # At the limit the charge is zero and factors exist nonuniquely; only
    # the unique reciprocal formula from nonzero epsilon disappears.
    assert scalar_contact(0).unique_nonzero_factor_norm is None
    assert scalar_contact(0).charge == 0


def test_nonclosed_range_psd_quotient_is_not_closable() -> None:
    for length in (1, 10, 100, 1000):
        ledger = nonclosable_psd_sequence(5, length)
        assert ledger.input_norm_squared == Q(1, length)
        assert ledger.quotient_output == 1
        assert ledger.finite_schur_completion_defect == 0
        # The formal preimage of the charge has one unit entry per tested
        # coordinate, so its squared norm diverges with the truncation.
        assert ledger.charge_preimage_square_sum == length


def test_closed_unbounded_square_root_factor_has_exact_coordinate_ratio() -> None:
    for coordinate in (1, 2, 10, 1000):
        ledger = closed_unbounded_coordinate(coordinate)
        assert ledger.schur_defect == 0
        assert ledger.factor_ratio == 2**coordinate


def test_dense_core_identity_can_miss_the_charged_nullvector() -> None:
    for length in (1, 10, 1000):
        ledger = dense_core_false_positive(length)
        assert ledger.distance_to_charged_null_squared == Q(1, length)
        assert ledger.a_image_norm_squared == Q(1, length)
        assert ledger.core_charge == 1
        assert ledger.actual_null_charge == 1


def test_compact_replay_ledger_has_no_rh_or_strip_claim() -> None:
    ledger = audit_ledger()
    assert ledger["scope"] == "ABSTRACT_PROOF_CLASS_ONLY"
    assert ledger["claims_rh_or_strip"] is False
