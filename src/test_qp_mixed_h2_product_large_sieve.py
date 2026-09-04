from fractions import Fraction

import pytest

from qp_mixed_h2_product_large_sieve import (
    PARABOLIC_CURVATURE,
    bh2_has_unique_shell_factor,
    bh2_product_counts,
    bh2_square_norm,
    broad_singleton_bin_exponent,
    complete_bin_exponent,
    diffuse_trace_exponent,
    mixed_h2_ledger,
    mixed_h2_mass_exponent,
    nonprincipal_singleton_exponent,
    old_mass_exponent,
    principal_singleton_exponent,
    two_interval_product_counts,
)


def test_exact_crossover_and_trace_ledger() -> None:
    ledger = mixed_h2_ledger()
    assert ledger.crossover_support == Fraction(33, 32)
    assert ledger.old_mass_at_crossover == Fraction(97, 128)
    assert ledger.mixed_mass_at_crossover == Fraction(97, 128)
    assert ledger.nonprincipal_singleton == Fraction(137, 128)
    assert ledger.principal_diffuse_crossover == Fraction(15, 8)
    assert ledger.broad_singleton_trace == Fraction(9, 8)
    assert ledger.complete_trace == Fraction(37, 32)
    assert ledger.complete_operator == Fraction(37, 128)


def test_old_and_mixed_profiles_cross_only_at_33_over_32() -> None:
    crossover = Fraction(33, 32)
    assert old_mass_exponent(crossover) == mixed_h2_mass_exponent(crossover)
    assert old_mass_exponent(Fraction(1)) < mixed_h2_mass_exponent(Fraction(1))
    assert old_mass_exponent(Fraction(3, 2)) > mixed_h2_mass_exponent(
        Fraction(3, 2)
    )


def test_principal_diffuse_envelope_is_nine_eighths() -> None:
    crossover = Fraction(15, 8)
    assert principal_singleton_exponent(crossover) == Fraction(9, 8)
    assert diffuse_trace_exponent(crossover) == Fraction(9, 8)
    assert nonprincipal_singleton_exponent(crossover) < Fraction(9, 8)
    grid = (Fraction(index, 128) for index in range(0, 257))
    assert max(broad_singleton_bin_exponent(mu) for mu in grid) == Fraction(9, 8)


def test_curvature_restores_thirty_seven_thirty_seconds() -> None:
    grid = tuple(Fraction(index, 128) for index in range(0, 257))
    assert all(complete_bin_exponent(mu) >= PARABOLIC_CURVATURE for mu in grid)
    assert max(complete_bin_exponent(mu) for mu in grid) == Fraction(37, 32)


def test_exact_two_interval_energy_and_shell_factorization() -> None:
    residuals = (1, 2, 3, 4)
    interval = two_interval_product_counts(residuals)
    assert interval[1] == 1
    assert interval[4] == 3
    assert interval[12] == 2

    shell = (101, 103, 107)
    assert bh2_has_unique_shell_factor(shell, residuals)
    counts = bh2_product_counts(shell, residuals)
    interval_norm = sum(value * value for value in interval.values())
    assert bh2_square_norm(shell, residuals) == len(shell) * interval_norm
    assert sum(counts.values()) == len(shell) * len(residuals) ** 2


def test_structural_hypotheses_are_enforced() -> None:
    with pytest.raises(ValueError, match="not shorter"):
        bh2_has_unique_shell_factor((101, 103), (1, 11))
    with pytest.raises(ValueError, match="pairwise coprime"):
        bh2_has_unique_shell_factor((105, 115), (1, 2, 3))
    with pytest.raises(ValueError, match="nonzero"):
        two_interval_product_counts((0, 1))
