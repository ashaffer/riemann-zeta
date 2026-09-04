from fractions import Fraction
from math import sqrt

import pytest

from qp_determinant_band_sumproduct_audit import (
    all_distinct_tangent_packet_count,
    determinant,
    determinant_band_exponent_ledger,
    dyadic_minimum_sum_ratio,
    flat_support_character_bound_exponent,
    flat_support_character_profile_exponent,
    local_additive_balance_is_forced,
    parallelogram_determinant_factorization,
    modular_energy_promotion_exponent,
    slope_bin_collision_lower_bound,
    uniform_five_fourths_ledger,
    weighted_determinant_band_mass,
    weighted_hyperbolic_parallelogram_mass,
)


def test_project_exponent_ledger():
    ledger = determinant_band_exponent_ledger()
    assert ledger.d_exponent_in_q == Fraction(16, 33)
    assert ledger.full_shell_r43_exponent_in_d == Fraction(33, 16)
    assert ledger.global_flat_prime_lower_exponent_in_d == 1
    assert ledger.localized_upper_exponent_in_d == Fraction(1, 2)
    assert ledger.flat_support_at_most_d_upper_exponent_in_d == Fraction(3, 4)
    assert ledger.conditional_modular_energy_upper_exponent_in_d == Fraction(1, 2)
    assert ledger.localized_four_cycle_trace_exponent_in_d == 1
    assert ledger.localized_d_prime_span_squared_exponent_in_q == Fraction(32, 33)
    assert ledger.localized_span_condition_has_power_margin
    assert not ledger.uniform_positive_power_saving_is_possible


def test_flat_support_and_modular_energy_profiles():
    assert flat_support_character_bound_exponent() == Fraction(3, 4)
    assert flat_support_character_profile_exponent(Fraction(1, 2)) == Fraction(1, 2)
    assert flat_support_character_profile_exponent(1) == Fraction(3, 4)
    assert modular_energy_promotion_exponent(3) == Fraction(3, 4)
    assert modular_energy_promotion_exponent(2) == Fraction(1, 2)


def test_uniform_five_fourths_crossover_ledger():
    ledger = uniform_five_fourths_ledger()
    assert ledger.support_crossover == Fraction(7, 4)
    assert ledger.flat_character_mass_at_crossover == Fraction(15, 16)
    assert ledger.broad_pointwise_cap == Fraction(5, 16)
    assert ledger.small_bin_trace == Fraction(5, 4)
    assert ledger.diffuse_trace_at_crossover == Fraction(5, 4)
    assert ledger.parabolic_trace == Fraction(5, 4)
    assert ledger.uniform_trace == Fraction(5, 4)
    assert ledger.uniform_operator == Fraction(5, 16)
    assert ledger.previous_uniform_trace == Fraction(21, 16)
    assert ledger.trace_gain == Fraction(1, 16)
    assert ledger.transverse_exponent == Fraction(43, 66)


def test_local_balance_and_factorization_exhaustively():
    x = 1000
    length = 12
    band = 20
    assert band + length * length < x
    for a in range(x, x + length + 1):
        for b in range(x, x + length + 1):
            for c in range(x, x + length + 1):
                for d in range(x, x + length + 1):
                    assert local_additive_balance_is_forced(
                        a,
                        b,
                        c,
                        d,
                        interval_left=x,
                        interval_length=length,
                        band=band,
                    )
                    if abs(determinant(a, b, c, d)) <= band:
                        assert parallelogram_determinant_factorization(a, b, c, d)


def test_local_determinant_form_equals_gap_form():
    coordinates = list(range(1000, 1011))
    raw = [1, 3, 2, 4, 1, 5, 2, 1, 3, 2, 4]
    norm = sqrt(sum(value * value for value in raw))
    weights = [value / norm for value in raw]
    band = 25
    assert band + 10**2 < 1000
    determinant_mass = weighted_determinant_band_mass(
        coordinates, weights, band, nonzero=True
    )
    gap_mass = weighted_hyperbolic_parallelogram_mass(
        dict(zip(coordinates, weights)), band, nonzero=True
    )
    assert determinant_mass == pytest.approx(gap_mass, rel=1e-12, abs=1e-12)


def test_dyadic_ledger_is_uniformly_square_root_size():
    # The exact ratio tends to a bounded sawtooth.  A generous fixed bound
    # verifies the summation mechanism over many scales.
    assert max(dyadic_minimum_sum_ratio(2**n) for n in range(1, 25)) < 12


def test_collision_subtraction_and_tangent_scaling():
    assert slope_bin_collision_lower_bound(1000, 100) > 0
    counts = [all_distinct_tangent_packet_count(length) for length in (64, 128, 256)]
    assert counts[1] >= 7 * counts[0]
    assert counts[2] >= 7 * counts[1]
