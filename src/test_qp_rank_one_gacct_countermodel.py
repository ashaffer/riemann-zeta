from fractions import Fraction

import pytest

from qp_rank_one_gacct_countermodel import (
    projective_normals,
    rank_one_gacct_countermodel_ledger,
    rank_one_masses,
)


def test_projective_and_affine_counts() -> None:
    assert len(projective_normals(2)) == 15
    ledger = rank_one_gacct_countermodel_ledger(2)
    assert ledger.row_count == 16
    assert ledger.column_count == 30
    assert ledger.column_degree == 8
    assert ledger.dyadic_multiplicity == 4
    assert ledger.gacct_allowance == 4
    assert ledger.high_partner_count == 28
    assert ledger.gacct_failure_factor == Fraction(7, 1)


def test_codegree_law_at_three() -> None:
    ledger = rank_one_gacct_countermodel_ledger(3)
    assert ledger.row_count == 81
    assert ledger.column_count == 120
    assert ledger.column_degree == 27
    assert ledger.dyadic_multiplicity == 9
    assert ledger.high_partner_count == 117
    assert ledger.gacct_failure_factor == 13


def test_exact_rank_one_energy_and_hc_bounds() -> None:
    column_count = rank_one_gacct_countermodel_ledger(
        2, verify_intersections=False
    ).column_count
    left = tuple(complex(index + 1, -(index % 3)) for index in range(column_count))
    right = tuple(complex(2 - index % 5, index + 1) for index in range(column_count))
    ledger = rank_one_masses(2, left, right)
    assert ledger.exact_incidence_energy <= ledger.energy_upper * (1 + 1e-12)
    assert ledger.dyadic_hc_weight <= ledger.hc_upper * (1 + 1e-12)


def test_validation() -> None:
    with pytest.raises(ValueError):
        projective_normals(4)
    with pytest.raises(ValueError):
        rank_one_masses(2, (1,), (1,))
