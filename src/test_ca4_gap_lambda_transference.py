from fractions import Fraction

from ca4_gap_lambda_transference import (
    audit,
    cyclic_gaps,
    density_ratios,
    exact_zero_certificates,
    gram_counterexample,
    hat_structure,
    natural_structure,
    voronoi_weights,
)


def test_periodic_motif_and_density_bounds() -> None:
    assert cyclic_gaps() == (1, 1, 1, 1, 1, 1, 2, 8, 2)
    assert sum(voronoi_weights()) == 18
    assert min(density_ratios()) == Fraction(1, 2)
    assert max(density_ratios()) == Fraction(5, 2)


def test_natural_zeros_but_hat_alias_survives() -> None:
    assert all(exact_zero_certificates().values())
    assert max(abs(natural_structure(k)) for k in (2, 3, 4)) < 2e-15
    assert abs(hat_structure(2)) > 0.4


def test_rank_one_psd_change_of_measure_failure() -> None:
    result = gram_counterexample(Fraction(1, 4))
    assert result["natural_form"] == 0
    assert result["reweighted_form"] == Fraction(1, 4)
    assert result["minimum_density"] == Fraction(3, 4)
    assert result["maximum_density"] == Fraction(5, 4)


def test_audit_runs() -> None:
    assert audit()["natural_zero_certificates"]["harmonic_3"]
