from fractions import Fraction

import pytest

from qp_character_mellin_hecke_gate import (
    autocorrelation_exponent_ledger,
    character_prime_fan_fiber,
    classical_kloosterman_sum,
    crt_forced_hou_pan_indices,
    dfi_lower_block_ledger,
    direct_prime_fan_fiber,
    flat_autocorrelation_barrier,
    gl3_whittaker_torus_coordinates,
    hou_pan_balanced_ledger,
    hou_pan_factor_exponent,
    hou_pan_scope,
    maximal_eisenstein_boundary_convolution,
    opposite_cusp_nebentypus_factor,
    parity_twist_main_barrier,
    prime_character_parseval,
    spherical_gl3_prime_corner,
    suvitie_mean_square_scope,
    two_spike_hecke_fold_counterexample,
    yang_type_i_scope,
)


def test_character_transform_removes_the_moving_prime_fan_permutation() -> None:
    prime, unit = 11, 7
    coefficients = {
        residue: complex(residue - 3, (residue * residue + 1) % 7 - 2)
        for residue in range(1, prime)
    }
    for modulus in range(1, prime):
        for frequency in range(prime):
            assert character_prime_fan_fiber(
                coefficients, prime, unit, modulus, frequency
            ) == pytest.approx(
                direct_prime_fan_fiber(
                    coefficients, prime, unit, modulus, frequency
                ),
                abs=2e-12,
            )


def test_character_transform_is_unitary() -> None:
    coefficients = {
        residue: complex((3 * residue) % 5 - 2, (residue * residue) % 7 - 3)
        for residue in range(1, 13)
    }
    physical, spectral = prime_character_parseval(coefficients, 13)
    assert spectral == pytest.approx(physical, abs=2e-11)


def test_opposite_cusp_factor_is_a_character_of_the_delta_modulus() -> None:
    kwargs = dict(
        row_prime=11,
        row_character=3,
        color_prime=13,
        color_character=7,
    )
    first = opposite_cusp_nebentypus_factor(modulus=2, **kwargs)
    second = opposite_cusp_nebentypus_factor(modulus=5, **kwargs)
    product = opposite_cusp_nebentypus_factor(modulus=10, **kwargs)
    assert product == pytest.approx(first * second, abs=2e-12)


@pytest.mark.parametrize("length", [3, 4, 5, 8, 11])
def test_two_spike_autocorrelation_index_cannot_come_from_short_hecke_fold(
    length: int,
) -> None:
    fixture = two_spike_hecke_fold_counterexample(length)
    assert dict(fixture.product_coefficients) == {1: 1, length * length: -1}
    assert fixture.forbidden_additive_index == length * length - 1
    assert fixture.autocorrelation_coefficient == -1
    assert not fixture.occurs_in_short_hecke_support


@pytest.mark.parametrize("length", [3, 5, 8, 12])
def test_punctured_flat_autocorrelation_has_exact_d_cubed_barrier(
    length: int,
) -> None:
    ledger = flat_autocorrelation_barrier(length)
    assert ledger.zero_shift <= length**3
    assert ledger.exact_nonzero_support < 2 * length**2
    assert ledger.off_diagonal_l1 == length**4 - ledger.zero_shift
    assert ledger.off_diagonal_l2_squared >= ledger.theorem_lower_bound
    assert ledger.theorem_lower_bound == Fraction(length**4 * (length - 1) ** 2, 2)
    assert ledger.tensor_squared_norm == length**4


def test_lower_dfi_blocks_lie_below_the_first_nonzero_poisson_block() -> None:
    ledger = dfi_lower_block_ledger()
    assert ledger.local_constancy_cutoff_exponent == Fraction(9, 33)
    assert ledger.nonzero_poisson_cutoff_exponent == Fraction(17, 33)
    assert ledger.cutoff_separation_exponent == Fraction(8, 33)
    assert ledger.nonzero_blocks_have_constant_mismatch_weight


def test_autocorrelation_loss_is_exactly_square_root_degree() -> None:
    ledger = autocorrelation_exponent_ledger()
    assert ledger.barrier_squared_data_exponent == Fraction(182, 33)
    assert ledger.target_final_exponent == Fraction(100, 33)
    assert ledger.barrier_final_exponent == Fraction(108, 33)
    assert ledger.missing_exponent == Fraction(8, 33)
    assert ledger.missing_power_in_degree == Fraction(1, 2)


def test_yang_type_i_is_relevant_but_not_an_automatic_vector_valued_bound() -> None:
    scope = yang_type_i_scope()
    assert scope.general_generic_gl3
    assert scope.includes_noncuspidal_gl3
    assert scope.includes_gl2_continuous_spectrum
    assert scope.includes_singular_degenerate_and_residue_terms
    assert scope.scalar_input_is_one_gl3_vector
    assert not scope.arbitrary_mask_interpolation_proved
    assert not scope.vector_valued_character_square_function_proved
    assert not scope.automatic_qp_closure


def test_two_gl3_indices_retain_total_product_and_common_carrier_geometrically() -> None:
    assert gl3_whittaker_torus_coordinates(17, 35) == (17 * 35, 17, 1)


def test_spherical_gl3_hecke_relation_forbids_an_arbitrary_flat_prime_corner() -> None:
    # A normalized two-index array that is one at (p,1), (1,p), and (p,p)
    # cannot be the spherical coefficient array: the first two values force
    # A(p,p)=1*1-1=0.
    assert spherical_gl3_prime_corner(1, 1) == 0
    assert spherical_gl3_prime_corner(1, 1) != 1


def test_maximal_eisenstein_boundary_is_a_fixed_dirichlet_convolution() -> None:
    character = {index: 1 for index in range(1, 13)}
    hecke = {1: 1, 2: 3, 3: -2, 4: 5, 6: 7, 12: 11}
    assert maximal_eisenstein_boundary_convolution(character, hecke, 12) == (
        hecke[12] + hecke[6] + hecke[4] + hecke[3] + hecke[2] + hecke[1]
    )


def test_suvitie_does_not_supply_the_masked_fixed_window_square_function() -> None:
    scope = suvitie_mean_square_scope()
    assert scope.fixed_divisor_coefficients
    assert scope.averages_over_shift
    assert scope.averages_over_translation
    assert not scope.uniform_fixed_window
    assert not scope.arbitrary_factorization_mask
    assert not scope.retains_common_carrier_fiber
    assert not scope.reaches_full_endpoint_shift_range
    assert not scope.implies_qp_vector_square_function


@pytest.mark.parametrize("length", [4, 7, 10])
def test_one_coefficient_blind_main_cannot_cancel_flat_and_parity_twisted_data(
    length: int,
) -> None:
    barrier = parity_twist_main_barrier(length)
    assert barrier.odd_shift_l1 == 2 * barrier.odd_products * barrier.even_products
    assert barrier.odd_shift_l2_squared >= barrier.cauchy_lower_bound
    assert barrier.guaranteed_one_residual_squared_norm == barrier.odd_shift_l2_squared


def test_crt_rewriting_forces_joint_modulus_dependent_hou_pan_indices() -> None:
    first, second, first_modulus, second_modulus = 2, 3, 5, 7
    first_index, second_index = crt_forced_hou_pan_indices(
        first, second, first_modulus, second_modulus
    )
    whole = classical_kloosterman_sum(
        first, second, first_modulus * second_modulus
    )
    rewritten = classical_kloosterman_sum(
        first_index, second_modulus, first_modulus
    ) * classical_kloosterman_sum(
        second_index, first_modulus, second_modulus
    )
    assert rewritten == pytest.approx(whole, abs=2e-12)

    # Changing either original argument changes both nominal sequence indices.
    changed_first = crt_forced_hou_pan_indices(
        3, second, first_modulus, second_modulus
    )
    changed_second = crt_forced_hou_pan_indices(
        first, 4, first_modulus, second_modulus
    )
    assert changed_first[0] != first_index and changed_first[1] != second_index
    assert changed_second[0] != first_index and changed_second[1] != second_index


def test_hou_pan_balanced_fantasy_and_one_modulus_endpoint_ledgers() -> None:
    ledger = hou_pan_balanced_ledger()
    assert ledger.trivial_factor_exponent == Fraction(100, 66)
    assert ledger.hypothetical_two_factor_exponent == Fraction(59, 66)
    assert ledger.hypothetical_two_factor_saving == Fraction(41, 66)
    assert ledger.one_modulus_endpoint_exponent == Fraction(91, 66)
    assert ledger.one_modulus_endpoint_saving == Fraction(9, 66)
    assert ledger.required_saving_exponent == Fraction(16, 66)
    assert ledger.one_modulus_saving_deficit == Fraction(7, 66)
    assert ledger.deficit_power_in_degree == Fraction(7, 32)

    # The optimum is flat from the equal split through the length-matched split.
    for first_modulus in (Fraction(25, 66), Fraction(30, 66), Fraction(34, 66)):
        assert hou_pan_factor_exponent(
            first_modulus,
            Fraction(25, 33) - first_modulus,
            Fraction(34, 33),
            Fraction(16, 33),
        ) == Fraction(59, 66)


def test_hou_pan_scope_is_scalar_two_modulus_not_the_qp_vector_kernel() -> None:
    scope = hou_pan_scope()
    assert scope.fixed_prime_automorphic_level
    assert scope.boundary_coefficient_is_one_index
    assert scope.long_weyl_has_two_moduli
    assert scope.theorem_13_moduli_are_coprime
    assert scope.theorem_13_coefficients_are_separated
    assert not scope.arbitrary_two_index_whittaker_tensor
    assert not scope.one_modulus_dfi_kernel
    assert not scope.common_carrier_vector_square_function
    assert not scope.automatic_after_polar_subtraction
