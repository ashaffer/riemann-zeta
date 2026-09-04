from fractions import Fraction

from qp_burgess_307_256_synthesis import (
    burgess_flat_mass_exponent,
    burgess_short_sum_exponent_in_d,
    burgess_synthesis_ledger,
    diffuse_trace_exponent,
    small_bin_trace_exponent,
)


def test_burgess_r2_is_the_active_integer_parameter():
    assert burgess_short_sum_exponent_in_d(2) == Fraction(227, 256)
    assert burgess_short_sum_exponent_in_d(2) < burgess_short_sum_exponent_in_d(3)
    assert burgess_short_sum_exponent_in_d(2) < burgess_short_sum_exponent_in_d(4)


def test_exact_uniform_ledger():
    ledger = burgess_synthesis_ledger()
    assert ledger.d_exponent_in_q == Fraction(16, 33)
    assert ledger.burgess_parameter == 2
    assert ledger.burgess_short_sum_exponent_in_d == Fraction(227, 256)
    assert ledger.broad_and_singleton_cap == Fraction(5, 16)
    assert ledger.parabolic_curvature == Fraction(37, 32)
    assert ledger.support_crossover == Fraction(461, 256)
    assert ledger.principal_trace_at_crossover == Fraction(269, 256)
    assert ledger.diffuse_trace_at_crossover == Fraction(307, 256)
    assert ledger.uniform_trace == Fraction(307, 256)
    assert ledger.uniform_operator == Fraction(307, 1024)
    assert ledger.previous_trace == Fraction(5, 4)
    assert ledger.trace_gain == Fraction(13, 256)
    assert ledger.distance_from_sharp_trace == Fraction(51, 256)
    assert ledger.transverse_exponent == Fraction(1363, 2112)


def test_small_and_large_support_profiles_meet_below_target():
    crossover = Fraction(461, 256)
    assert burgess_flat_mass_exponent(crossover) == Fraction(227, 256)
    assert small_bin_trace_exponent(crossover) == Fraction(307, 256)
    assert diffuse_trace_exponent(crossover) == Fraction(307, 256)

    # Below the crossover the Burgess singleton term is the active ceiling.
    for mu in (Fraction(0), Fraction(1), Fraction(3, 2), crossover):
        assert small_bin_trace_exponent(mu) <= Fraction(307, 256)

    # Above it the diffuse exponent only decreases.
    for mu in (crossover, Fraction(15, 8), Fraction(2), Fraction(33, 16)):
        assert diffuse_trace_exponent(mu) <= Fraction(307, 256)
