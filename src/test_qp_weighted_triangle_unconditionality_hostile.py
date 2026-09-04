import numpy as np
import pytest

from qp_residual_block_triangle_matching import affine_plane_sts9_parallel_classes
from qp_weighted_triangle_rademacher_square import (
    exact_rademacher_fourth_average,
    rademacher_upper_bound,
    validate_linear_matching_partition,
    weighted_class_matrices,
)
from qp_weighted_triangle_unconditionality_hostile import (
    actual_integer_c4_ledger,
    exact_rademacher_pairing_ledger,
    factor_two_square_ledger,
    tangent_grid_fixture,
    tangent_grid_ledger,
    weighted_cross_gram_multiplicity_ledger,
)


def test_complex_rademacher_pairing_and_constant_are_exactly_safe() -> None:
    classes = affine_plane_sts9_parallel_classes()
    z = np.array([1 + 2j, -3j, 2, 1 - 1j, 4j, -2, 3, 0.5j, -1])
    z = z / np.linalg.norm(z)
    matrices = weighted_class_matrices(9, classes, z)
    pairing = exact_rademacher_pairing_ledger(matrices)
    enumerated = exact_rademacher_fourth_average(matrices)
    assert pairing.exact_average_from_pairings == pytest.approx(enumerated)
    assert abs(pairing.transpose_pairing_real) <= pairing.transpose_absolute_bound + 1e-12
    assert pairing.transpose_absolute_bound == pytest.approx(pairing.left_square)
    assert enumerated <= pairing.proved_upper_bound + 1e-12

    _, degree = validate_linear_matching_partition(9, classes)
    assert enumerated <= rademacher_upper_bound(degree, np.linalg.norm(z)) + 1e-12


@pytest.mark.parametrize("order", [2, 3, 4])
def test_tangent_grid_is_a_legal_linear_matching_partition(order: int) -> None:
    fixture = tangent_grid_fixture(order)
    ledger = tangent_grid_ledger(fixture)
    assert ledger.vertices == 4 * order - 1
    assert ledger.edges == order**2
    assert ledger.maximum_hyperedge_degree == order
    assert ledger.maximum_absolute_residual <= ledger.fine_window_radius
    assert ledger.maximum_log_shell_coordinate < 0.2
    assert ledger.alternating_two_colour_rectangles == 0
    assert np.linalg.norm(fixture.coefficients) == pytest.approx(1.0)
    assert all(
        max(residual for edge, residual in fixture.residual_by_edge if edge in matching)
        - min(residual for edge, residual in fixture.residual_by_edge if edge in matching)
        < fixture.q
        for matching in fixture.classes
    )


@pytest.mark.parametrize("order", [2, 3, 4])
def test_tangent_grid_has_exact_sqrt_D_unconditionality_gap(order: int) -> None:
    ledger = tangent_grid_ledger(tangent_grid_fixture(order))
    assert ledger.all_plus_fourth_power == pytest.approx(ledger.exact_all_plus_formula)
    assert ledger.randomized_fourth_power == pytest.approx(
        ledger.exact_randomized_formula
    )
    assert ledger.unconditionality_ratio == pytest.approx(ledger.exact_ratio_formula)
    assert ledger.exact_ratio_formula == pytest.approx(order**2 / (2 * order - 1))
    # D=100L^2, so the ratio is asymptotic to sqrt(D)/20.
    assert ledger.ratio_as_fraction_of_sqrt_degree_parameter == pytest.approx(
        order / (10 * (2 * order - 1))
    )


def test_literal_integer_product_window_has_a_pure_weighted_c4() -> None:
    ledger = actual_integer_c4_ledger()
    assert ledger.residuals == (-28_225, -6_001, 5_615, 19_487)
    assert ledger.block_indices == (0, 6, 10, 14)
    assert max(abs(value) for value in ledger.residuals) <= (
        ledger.q * ledger.degree_parameter
    )
    assert ledger.all_plus_fourth_power == pytest.approx(2.0)
    assert ledger.randomized_fourth_power == pytest.approx(1.5)
    assert ledger.ratio == pytest.approx(4.0 / 3.0)


def test_factor_two_bin_has_the_refined_diffuse_square_budget() -> None:
    classes = affine_plane_sts9_parallel_classes()
    phases = np.exp(1j * np.arange(9))
    amplitudes = np.linspace(1.0, 1.9, 9)
    z = phases * amplitudes
    z = z / np.linalg.norm(z)
    ledger = factor_two_square_ledger(9, classes, z)
    matrices = weighted_class_matrices(9, classes, z)
    randomized = exact_rademacher_fourth_average(matrices)

    assert ledger.support_size == 9
    assert ledger.maximum_hyperedge_degree == 4
    assert ledger.maximum_pivot_mass <= min(
        ledger.coefficient_norm_squared,
        8
        * ledger.maximum_hyperedge_degree
        / ledger.support_size
        * ledger.coefficient_norm_squared,
    ) + 1e-12
    assert ledger.total_pivot_mass <= (
        2
        * ledger.maximum_hyperedge_degree
        * ledger.coefficient_norm_squared
        + 1e-12
    )
    assert ledger.right_square == pytest.approx(ledger.left_square)
    assert ledger.right_square <= ledger.proved_square_bound + 1e-12
    assert randomized <= ledger.proved_rademacher_bound + 1e-12


@pytest.mark.parametrize("order", [2, 3, 4, 5])
def test_tangent_packet_exactly_saturates_cross_gram_multiplicity(order: int) -> None:
    fixture = tangent_grid_fixture(order)
    ledger = weighted_cross_gram_multiplicity_ledger(
        len(fixture.node_values), fixture.classes, fixture.coefficients
    )
    weight_count = 2 * order - 1
    exact_atomic = 2 * order**2 * (order - 1) / weight_count**2
    exact_cross = order * exact_atomic

    assert ledger.maximum_output_cell_multiplicity == order
    assert ledger.weighted_atomic_energy == pytest.approx(exact_atomic)
    assert ledger.cross_gram_hilbert_schmidt_squared == pytest.approx(exact_cross)
    assert ledger.multiplicity_upper_bound == pytest.approx(exact_cross)
