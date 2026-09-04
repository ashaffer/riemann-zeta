from fractions import Fraction
import math

from qp_four_cycle_bp_bridge import (
    active_bp_bridge_exponents,
    delta_frequency_block_loss,
    paley_mixed_block_loss,
    reciprocal_layer_identity,
    weighted_sparse_diffuse_bridge_ledger,
)
from qp_four_cycle_hostile_lab import exact_prime_rectangle_fixture


def test_actual_prime_rectangle_lies_on_the_exact_reciprocal_layer() -> None:
    fixture = exact_prime_rectangle_fixture()
    identity = reciprocal_layer_identity(
        center_prime=fixture.q,
        first_row=fixture.rows[0],
        second_row=fixture.rows[1],
        carrier=fixture.columns[0],
        first_color=fixture.colors[0][0],
        second_color=fixture.colors[1][0],
    )
    assert identity.residual == fixture.residuals[0]
    assert identity.shift == -42
    assert identity.unit_shift
    assert identity.congruence_error == 0
    assert (
        fixture.columns[0] % identity.modulus
        == identity.multiplier * pow(identity.shift, -1, identity.modulus)
        % identity.modulus
    )


def test_point_mass_has_full_frequency_support_and_block_loss() -> None:
    ledger = delta_frequency_block_loss(101, 10)
    assert ledger.blocks == 11
    assert ledger.global_delta_fourier_norm_squared == 101
    assert ledger.block_norm_sum_lower_bound == 10 * math.sqrt(10) + 1
    assert ledger.one_side_cauchy_loss_lower_bound > 3


def test_active_block_loss_is_far_larger_than_the_bp_bridge_budget() -> None:
    ledger = active_bp_bridge_exponents()
    assert ledger["frequency_blocks"] == Fraction(17, 33)
    assert ledger["one_side_block_loss"] == Fraction(17, 66)
    assert ledger["bp_saving"] == Fraction(19, 1056)
    assert ledger["allowed_bridge_loss"] == Fraction(1, 352)
    assert ledger["one_side_excess_over_allowed"] == Fraction(269, 1056)


def test_positive_diffuse_masks_can_retain_the_full_block_loss() -> None:
    atomic = paley_mixed_block_loss(103, 10, 0.9)
    diffuse = paley_mixed_block_loss(103, 10, 0.05)
    assert atomic.physical_participation < 2
    assert diffuse.physical_participation > 40
    assert abs(
        atomic.zero_frequency_energy
        + 102 * atomic.nonzero_frequency_energy
        - 103
    ) < 1e-9
    assert abs(
        diffuse.zero_frequency_energy
        + 102 * diffuse.nonzero_frequency_energy
        - 103
    ) < 1e-9
    assert atomic.normalized_block_loss > 3
    assert diffuse.normalized_block_loss > 2.5


def test_weighted_sparse_diffuse_split_leaves_the_middle_open() -> None:
    ledger = weighted_sparse_diffuse_bridge_ledger()
    assert ledger.aperture_exponent_in_q == Fraction(16, 33)
    assert ledger.degree_transition_exponent_in_q == Fraction(16, 33)
    assert ledger.diffuse_participation_cutoff_exponent_in_q == Fraction(32, 33)
    assert ledger.three_atom_tail_cutoff_exponent_in_degree == Fraction(-5, 8)
    assert ledger.three_atom_tail_cutoff_exponent_in_q == Fraction(-10, 33)
    assert ledger.one_side_block_loss_exponent_in_q == Fraction(17, 66)
    assert ledger.allowed_bp_bridge_loss_exponent_in_q == Fraction(1, 352)
    assert ledger.one_side_excess_over_allowed_exponent_in_q == Fraction(269, 1056)
    assert ledger.open_uniform_support_lower_exponent_in_q == 0
    assert ledger.open_uniform_support_upper_exponent_in_q == Fraction(32, 33)
    assert not ledger.global_participation_controls_each_layer
    assert not ledger.bp_bridge_shrinks_open_support_interval
    assert not ledger.arbitrary_coefficients_closed
