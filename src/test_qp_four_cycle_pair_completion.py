from qp_four_cycle_pair_completion import (
    carrier_product_matrix,
    completion_level,
    energy_determinant_factorization,
    energy_difference,
    energy_linear_form,
    flat_completion_energy,
    pair_completion_ledger,
    translation_grid_completion,
    translation_pair_energy_parameters,
)


def test_exact_level_and_determinant_identities() -> None:
    colors = (19, 17, 13, 11)
    first = (23, 29, 31, 37)
    second = (41, 43, 47, 53)
    energy = energy_difference(first, second)
    assert energy_linear_form(colors, energy) == (
        completion_level(colors, first) - completion_level(colors, second)
    )
    assert energy_determinant_factorization(first, second)[0] == (
        energy_determinant_factorization(first, second)[1]
    )
    assert carrier_product_matrix(first) == (713, 851, 899, 1073)


def test_pair_ledger_separates_oriented_and_d4_counts() -> None:
    first_colors = (101, 103, 107, 109)
    reflected_colors = (107, 109, 101, 103)
    groups = {
        first_colors: ((11, 13, 17, 19), (23, 29, 31, 37)),
        reflected_colors: ((41, 43, 47, 53),),
    }
    ledger = pair_completion_ledger(groups)
    assert ledger.completions == 3
    assert ledger.oriented_color_matrices == 2
    assert ledger.d4_color_orbits == 1
    assert ledger.maximum_oriented_completion_multiplicity == 2
    assert ledger.maximum_d4_completion_multiplicity == 3
    assert ledger.ordered_completion_pairs == 5
    assert ledger.nonzero_energy_ordered_pairs == 2


def test_translation_energy_is_injective_off_the_diagonal() -> None:
    colors = (40042793, 40042695, 40042688, 40042590)
    completions = tuple(
        translation_grid_completion(5_720_399, 8, 15, 14, translation)
        for translation in range(-10, 11)
    )
    ledger = pair_completion_ledger({colors: completions})
    assert ledger.oriented_colors_with_multiple_levels == 0
    assert ledger.maximum_nonzero_fixed_color_energy_multiplicity == 1
    assert ledger.colliding_nonzero_fixed_color_energy_keys == 0
    energy = flat_completion_energy({colors: completions})
    assert energy.active_colors == 4
    assert energy.raw_completion_square_sum == 21**2
    assert energy.weighted_completion_square_sum == 21**2 / 16


def test_translation_parameter_recovery_in_both_step_cases() -> None:
    assert translation_pair_energy_parameters(
        row_ratio=8,
        row_step=15,
        column_step=14,
        first_translation=37,
        second_translation=-11,
    ) == (48, 26, 48, 26)
    assert translation_pair_energy_parameters(
        row_ratio=8,
        row_step=15,
        column_step=15,
        first_translation=37,
        second_translation=-11,
    ) == (48, 26, 48, 26)
