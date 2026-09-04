from qp_four_cycle_pair_energy_audit import (
    color_energy_factorization,
    common_modulus_ledger,
    fixed_energy_norm_ledger,
    off_diagonal_bootstrap_bound,
    pair_identity_ledger,
    projection_countermodel_ledger,
)
from qp_fixed_color_tangent_countermodel import fixed_color_tangent_family


def test_pair_secant_and_lagrange_identities_are_exact() -> None:
    colors = (19, 17, 13, 11)
    first = (23, 29, 31, 37)
    second = (41, 43, 47, 53)
    ledger = pair_identity_ledger(colors, first, second)
    assert ledger.energy_linear_form == (
        ledger.first_level - ledger.second_level
    )
    assert ledger.energy_determinant == -(
        ledger.row_cross_determinant * ledger.column_cross_determinant
    )
    assert ledger.lagrange_defect == 0
    assert ledger.elimination_defect == 0


def test_common_modulus_relation_is_the_reduction_of_an_equality() -> None:
    colors = (19, 17, 13, 11)
    completion = (23, 29, 31, 37)
    ledger = common_modulus_ledger(colors, completion)
    assert ledger.first_product_defect == 0
    assert ledger.second_product_defect == 0
    assert ledger.common_modulus_defect == 0


def test_fixed_energy_binary_norm_reduction_on_tangent_family() -> None:
    family = fixed_color_tangent_family(100_000, 100)
    colors = (
        family.colors[0][0],
        family.colors[0][1],
        family.colors[1][0],
        family.colors[1][1],
    )
    first_item = family.completions[3]
    second_item = family.completions[71]
    first = (*first_item.rows, *first_item.columns)
    second = (*second_item.rows, *second_item.columns)
    ledger = fixed_energy_norm_ledger(colors, first, second)
    assert ledger.energy_determinant != 0
    assert ledger.norm_rhs > 0
    assert ledger.color_energy_trace == 0
    assert ledger.energy_involution_trace == 0
    assert ledger.mixed_trace == 2 * ledger.level * ledger.energy_determinant
    assert ledger.color_energy_square_defect == (0, 0, 0, 0)
    assert ledger.energy_involution_square_defect == (0, 0, 0, 0)
    assert ledger.anticommutator_defect == (0, 0, 0, 0)
    assert ledger.norm_square_defect == (0, 0, 0, 0)


def test_color_energy_factorization_needs_the_common_level() -> None:
    colors = (19, 17, 13, 11)
    energy = (1, 1, 1, 1)
    assert 19 + 11 - 17 - 13 == 0
    assert color_energy_factorization(colors, energy)[0] == (
        color_energy_factorization(colors, energy)[1]
    )


def test_projection_fibre_can_be_cubic_under_degree_caps() -> None:
    ledger = projection_countermodel_ledger(101)
    assert ledger.maximum_node_degree == 101
    assert ledger.completion_multiplicity == 100
    assert ledger.top_projection_square_fibre == 1_000_000


def test_off_diagonal_D_bound_bootstraps_to_constant_times_D() -> None:
    degree = 121.0
    bound = off_diagonal_bootstrap_bound(degree, degree)
    assert degree < bound < 2.0 * degree
