from fractions import Fraction
from math import sqrt

import pytest

from qp_phase_jet_bessel_inverse import (
    abel_variation,
    derivative_test_decay_window,
    derivative_test_saving_exponent,
    endpoint_phase_jet_ledger,
    forward_difference,
    integer_affine_alias_packets,
    integer_binomial,
    integer_newton_polynomial,
    inverse_near_degree_floor,
    jet_schur_audit,
    normalized_packet,
    quotient_curvature_jet_invariants,
    quotient_by_integer_newton_phase,
    recover_stationary_action_from_three_jet,
    sampled_exponential,
    stationary_action_jet,
)


def test_newton_basis_has_exact_finite_differences() -> None:
    coefficients = (7, -3, 5, 2)
    values = tuple(integer_newton_polynomial(n, coefficients) for n in range(12))
    for order, coefficient in enumerate(coefficients):
        assert forward_difference(values, order)[0] == coefficient
    assert integer_binomial(-3, 2) == 6
    assert integer_binomial(-3, 3) == -10


def test_integer_newton_quotient_is_invisible_at_every_sample() -> None:
    phases = tuple(Fraction(3 * n * n + n, 17) for n in range(15))
    quotient = quotient_by_integer_newton_phase(phases, (5, -7, 3, 11))
    original = sampled_exponential(phases)
    reduced = sampled_exponential(quotient)
    assert max(abs(left - right) for left, right in zip(original, reduced)) < 1.0e-12


def test_finite_abel_variation_has_the_normalized_flat_scale() -> None:
    count = 23
    flat = tuple(complex(Fraction(1, count)) for _ in range(count))
    assert abs(abel_variation(flat) - 1 / count) < 1.0e-15
    tapered = (0j, 0.1 + 0j, 0.2 + 0j, 0.1 + 0j, 0j)
    assert abs(abel_variation(tapered) - 0.4) < 1.0e-15


def test_discrete_fourier_packets_have_bessel_constant_one() -> None:
    size = 13
    packets = tuple(
        normalized_packet(tuple(Fraction(label * sample, size) for sample in range(size)))
        for label in range(size)
    )
    audit = jet_schur_audit(packets, (), 1.0e-12)
    assert audit.maximum_near_degree == 0
    assert audit.maximum_off_near_correlation < 1.0e-12
    assert abs(audit.actual_bessel_squared - 1) < 1.0e-10
    assert abs(audit.schur_bessel_squared_bound - 1) < 2.0e-11


def test_integral_affine_wrap_labels_are_one_major_arc_cluster() -> None:
    packets = integer_affine_alias_packets(9, 17)
    near = tuple((first, second) for first in range(9) for second in range(first + 1, 9))
    audit = jet_schur_audit(packets, near, 0.0)
    assert audit.maximum_near_degree == 8
    assert abs(audit.actual_bessel_squared - 9) < 1.0e-10
    assert audit.schur_bessel_squared_bound == 9
    with pytest.raises(ValueError, match="off-near"):
        jet_schur_audit(packets, (), 0.5)


def test_inverse_theorem_forces_a_large_near_jet_star() -> None:
    # If K=100 packets have Bessel quotient 31 and off-major-arc correlation
    # at most 1/10, some packet has at least 23 near-jet neighbors.
    assert inverse_near_degree_floor(Fraction(31), 100, Fraction(1, 10)) == 23
    assert inverse_near_degree_floor(Fraction(1), 100, Fraction(1, 10)) == 0


def test_endpoint_cubic_test_has_the_exact_small_margin() -> None:
    ledger = endpoint_phase_jet_ledger()
    assert ledger.block_length == Fraction(11, 16)
    assert ledger.full_pair_correlation_saving == Fraction(1, 6)
    assert ledger.closing_pair_correlation_saving == Fraction(7, 48)
    assert ledger.closing_cluster_ceiling == Fraction(49, 48)
    assert ledger.optimal_cubic_pair_saving == Fraction(11, 64)
    assert ledger.cubic_margin_for_full_gain == Fraction(1, 192)
    assert ledger.cubic_margin_for_closing_gain == Fraction(5, 192)
    assert ledger.full_first_window == (Fraction(), Fraction(25, 48))
    assert ledger.full_second_window == (Fraction(1, 3), Fraction(25, 24))
    assert ledger.full_third_window == (Fraction(1), Fraction(17, 16))
    assert ledger.closing_third_window == (Fraction(7, 8), Fraction(19, 16))


def test_derivative_envelopes_reach_their_stated_optima() -> None:
    block = Fraction(11, 16)
    assert derivative_test_saving_exponent(2, block, block) == Fraction(11, 32)
    assert derivative_test_saving_exponent(3, block, 3 * block / 2) == Fraction(11, 64)
    with pytest.raises(ValueError, match="exceeds"):
        derivative_test_decay_window(3, block, Fraction(1, 5))


def test_regular_stationary_action_is_recovered_from_three_derivatives() -> None:
    # C=1, S=10, a=4, b=6, u=3, v=2.  Thus h=48, k=72, m=-1.
    jet = stationary_action_jet(1, 10, 4, 48, 72, -1)
    assert jet.left_scaled_frequency == 3
    assert jet.right_scaled_frequency == 2
    assert jet.curvature_numerator == 26
    recovered = recover_stationary_action_from_three_jet(
        1, 10, jet.first, jet.second, jet.third
    )
    assert recovered.saddle == 4
    assert recovered.left_frequency == 48
    assert recovered.right_frequency == 72
    assert recovered.poisson_frequency == -1


def test_curvature_jet_is_affine_quotient_compatible_and_reflection_rigid() -> None:
    jet = stationary_action_jet(1, 10, 4, 48, 72, -1)
    reflected = stationary_action_jet(1, 10, 6, 72, 48, 1)
    assert (jet.second, jet.third, jet.fourth) == (
        reflected.second,
        reflected.third,
        reflected.fourth,
    )
    invariants = quotient_curvature_jet_invariants(
        10, jet.second, jet.third, jet.fourth
    )
    # t=2/5 and a'=4/13, hence x=-1/5 and y=-5/13.
    assert invariants.tangent_x_squared == Fraction(1, 25)
    assert invariants.speed_over_tangent == Fraction(25, 13)
    assert invariants.centered is False


def test_curvature_jet_central_reconstruction_has_only_reflection_ambiguity() -> None:
    # t=1/2, scaled frequencies U=3,V=2, so a'=2/5 and y^2=1/25.
    jet = stationary_action_jet(1, 10, 5, 75, 50, -1)
    invariants = quotient_curvature_jet_invariants(
        10, jet.second, jet.third, jet.fourth
    )
    assert invariants.centered is True
    assert invariants.tangent_x_squared == 0
    assert invariants.speed_y_squared_if_centered == Fraction(1, 25)


def test_zero_dual_reflections_have_the_same_full_stationary_action_jet() -> None:
    # For m=0 the action is C*(sqrt(h)+sqrt(k))^2/S.  The reflected pairs
    # (h,k)=(1,4) and (4,1) therefore agree for every S, not just to order 3.
    first = stationary_action_jet(1, 10, Fraction(10, 3), 1, 4, 0)
    second = stationary_action_jet(1, 10, Fraction(20, 3), 4, 1, 0)
    assert (first.first, first.second, first.third) == (
        second.first,
        second.second,
        second.third,
    )
    with pytest.raises(ValueError, match="zero-dual"):
        recover_stationary_action_from_three_jet(
            1, 10, first.first, first.second, first.third
        )


def test_cubic_fold_is_exactly_the_other_jet_singularity() -> None:
    # u=1, v=-1, S=10, a=5 gives w=0 and F_aa=0.
    with pytest.raises(ValueError, match="cubic fold"):
        stationary_action_jet(1, 10, 5, 25, -25, -2)
