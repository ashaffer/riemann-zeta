from fractions import Fraction

import pytest

from qp_uniform_thirty_seven_thirty_seconds import (
    convolution_square_norm,
    diffuse_trace_exponent,
    large_sieve_mass_exponent,
    old_character_mass_exponent,
    principal_mass_exponent,
    shell_product_convolution_is_sidon,
    singleton_character_trace_exponent,
    uniform_bin_trace_exponent,
    uniform_thirty_seven_ledger,
)


def test_exact_uniform_ledger():
    ledger = uniform_thirty_seven_ledger()
    assert ledger.d_exponent_in_q == Fraction(16, 33)
    assert ledger.q_exponent_in_d == Fraction(33, 16)
    assert ledger.old_large_value_crossover == Fraction(11, 8)
    assert ledger.old_mass_at_crossover == Fraction(27, 32)
    assert ledger.large_sieve_mass_at_crossover == Fraction(27, 32)
    assert ledger.slice_cap == Fraction(5, 16)
    assert ledger.singleton_trace_at_crossover == Fraction(37, 32)
    assert ledger.parabolic_curvature_trace == Fraction(37, 32)
    assert ledger.principal_safe_endpoint == Fraction(61, 32)
    assert ledger.diffuse_switch == Fraction(59, 32)
    assert ledger.principal_diffuse_overlap == Fraction(1, 16)
    assert ledger.uniform_trace == Fraction(37, 32)
    assert ledger.uniform_operator == Fraction(37, 128)
    assert ledger.previous_trace == Fraction(5, 4)
    assert ledger.trace_gain == Fraction(3, 32)
    assert ledger.transverse_exponent == Fraction(169, 264)


def test_character_bounds_cross_at_eleven_eighths():
    mu = Fraction(11, 8)
    assert old_character_mass_exponent(mu) == Fraction(27, 32)
    assert large_sieve_mass_exponent(mu) == Fraction(27, 32)
    assert singleton_character_trace_exponent(mu) == Fraction(37, 32)
    assert old_character_mass_exponent(mu - Fraction(1, 8)) < large_sieve_mass_exponent(
        mu - Fraction(1, 8)
    )
    assert large_sieve_mass_exponent(mu + Fraction(1, 8)) < old_character_mass_exponent(
        mu + Fraction(1, 8)
    )


def test_principal_and_diffuse_ranges_overlap():
    assert principal_mass_exponent(Fraction(61, 32)) + Fraction(5, 16) == Fraction(
        37, 32
    )
    assert diffuse_trace_exponent(Fraction(59, 32)) == Fraction(37, 32)
    assert singleton_character_trace_exponent(Fraction(59, 32)) <= Fraction(37, 32)


def test_uniform_profile_never_exceeds_thirty_seven_thirty_seconds():
    # The physical shell has M<=D^(33/16).  A denominator 256 grid includes
    # every rational breakpoint used by the proof.
    values = [
        uniform_bin_trace_exponent(Fraction(index, 256))
        for index in range(0, 33 * 16 + 1)
    ]
    assert max(values) == Fraction(37, 32)


def test_product_convolution_is_exactly_sidon():
    shell = (101, 103, 107, 109)
    residuals = tuple(range(-20, 0)) + tuple(range(1, 21))
    assert shell_product_convolution_is_sidon(shell, residuals)
    assert convolution_square_norm(shell, residuals) == len(shell) * len(residuals)


def test_sidon_hypotheses_are_enforced():
    with pytest.raises(ValueError):
        shell_product_convolution_is_sidon((101, 202), (1, 2, 3))
    with pytest.raises(ValueError):
        shell_product_convolution_is_sidon((101, 103), (101,))

