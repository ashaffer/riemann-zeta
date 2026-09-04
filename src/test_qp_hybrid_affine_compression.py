from fractions import Fraction

import pytest

from qp_hybrid_affine_compression import (
    AffinePatchProfile,
    CompletionFiber,
    affine_carleson_ledger,
    certify_affine_energy,
    hybrid_mass_ledger,
)
from qp_a2_packet_serialization import (
    extract_exact_secant_a2_cells,
    validate_a2_packet_cell,
)


def test_affine_carleson_certificate_sums_local_trace_majorants() -> None:
    profiles = (
        AffinePatchProfile("first", ((1, 3), (2, 1))),
        AffinePatchProfile("second", ((1, 1), (3, 4))),
    )
    ledger = affine_carleson_ledger(profiles)
    assert dict(ledger.color_loads) == {1: 8, 2: 2, 3: 8}
    assert ledger.maximum_color_load == 8

    certificate = certify_affine_energy(
        profiles,
        {1: Fraction(1, 4), 2: Fraction(1, 2), 3: Fraction(1, 4)},
    )
    assert certificate.total_color_energy == 1
    assert certificate.local_patch_majorant == Fraction(25, 8)
    assert certificate.carleson_majorant == 8
    assert certificate.local_does_not_exceed_carleson


def test_hybrid_split_is_exact_but_does_not_reconstruct_full_factorial_mass() -> None:
    ledger = hybrid_mass_ledger(
        (
            CompletionFiber(affine_count=5, residual_count=1, color_weight=Fraction(2)),
            CompletionFiber(affine_count=0, residual_count=3, color_weight=Fraction(1, 2)),
            CompletionFiber(affine_count=2, residual_count=0, color_weight=Fraction(3)),
        )
    )
    assert ledger.direct_mass == Fraction(39, 2)
    assert ledger.affine_direct_mass == 16
    assert ledger.residual_direct_mass == Fraction(7, 2)
    assert ledger.residual_presence_mass == Fraction(5, 2)
    assert ledger.residual_factorial_mass == 3
    assert ledger.residual_pointwise_majorant == 4
    assert ledger.full_factorial_mass == 69
    assert ledger.affine_factorial_mass == 46
    assert ledger.affine_residual_cross_mass == 20
    assert ledger.factorial_split_exact


def test_residual_pointwise_transfer_for_every_small_integer_count() -> None:
    for residual_count in range(101):
        ledger = hybrid_mass_ledger(
            (CompletionFiber(0, residual_count, Fraction(7, 11)),)
        )
        assert ledger.residual_direct_mass <= ledger.residual_pointwise_majorant


def test_a2_is_regenerated_on_residual_completions_before_factorialization() -> None:
    colors = (101, 103, 107, 109)
    completions = (
        (3, 5, 7, 11),
        (5, 8, 11, 17),
        (7, 11, 13, 19),
    )
    full = extract_exact_secant_a2_cells(
        q=10_007,
        degree_parameter=83,
        completion_groups={colors: completions},
        source_id="hybrid-full-source",
    )
    residual = extract_exact_secant_a2_cells(
        q=10_007,
        degree_parameter=83,
        completion_groups={colors: completions[1:]},
        source_id="hybrid-residual-source",
    )
    full_terms = tuple(term for cell in full for term in cell.terms)
    residual_terms = tuple(term for cell in residual for term in cell.terms)
    assert len(full_terms) == 3 * 2
    assert len(residual_terms) == 2 * 1
    assert all(
        term.first_completion in completions[1:]
        and term.second_completion in completions[1:]
        for term in residual_terms
    )
    assert all(cell.source_id == "hybrid-full-source" for cell in full)
    assert all(cell.source_id == "hybrid-residual-source" for cell in residual)
    assert {
        (term.colors, term.first_completion, term.second_completion)
        for term in residual_terms
    } < {
        (term.colors, term.first_completion, term.second_completion)
        for term in full_terms
    }
    assert all(validate_a2_packet_cell(cell).remainder_weight == 0 for cell in residual)


def test_invalid_profiles_and_fibers_are_rejected() -> None:
    with pytest.raises(ValueError):
        AffinePatchProfile("", ((1, 1),))
    with pytest.raises(ValueError):
        AffinePatchProfile("duplicate", ((1, 1), (1, 2)))
    with pytest.raises(ValueError):
        AffinePatchProfile("zero", ((1, 0),))
    with pytest.raises(ValueError):
        affine_carleson_ledger(
            (
                AffinePatchProfile("same", ((1, 1),)),
                AffinePatchProfile("same", ((2, 1),)),
            )
        )
    with pytest.raises(ValueError):
        CompletionFiber(-1, 0, Fraction(1))
    with pytest.raises(ValueError):
        certify_affine_energy(
            (AffinePatchProfile("p", ((1, 1),)),), {1: Fraction(-1)}
        )
