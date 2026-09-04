from __future__ import annotations

import pytest

from qp_center_fourier_large_sieve_audit import (
    averaged_frequency_convolution_energy,
    center_fourier_convolution,
    center_frequency_frame_energy,
    convolution_energy,
    density_lower_bound,
    hard_window_matrix,
    integer_log_shell,
    interval_additive_energy,
    maximum_cell_multiplicity,
    partial_matching_fixture,
    repeated_row_fixture,
    row_pair_energy,
    same_center_convolution,
    unitary_center_dft,
    unnormalized_center_dft,
)


def test_center_dft_is_only_a_unitary_rewriting_of_row_pair_energy() -> None:
    rows = [2, 5, 9]
    centers = [1, 3, 6]
    modulus = 11
    matrix = {
        (2, 1): 1 + 2j,
        (2, 6): -0.5j,
        (5, 3): 0.75 - 0.25j,
        (5, 6): -1.2,
        (9, 1): 0.3j,
        (9, 3): 2.0,
    }
    transformed = unitary_center_dft(matrix, rows, modulus)
    assert center_frequency_frame_energy(
        transformed, rows, modulus
    ) == pytest.approx(row_pair_energy(matrix, rows, centers), abs=1.0e-10)


def test_center_fourier_reconstructs_same_center_convolution_exactly() -> None:
    rows = [1, 4, 7]
    centers = [0, 2, 5]
    modulus = 13
    matrix = {
        (1, 0): 1.0,
        (4, 0): 0.4,
        (1, 2): -0.25,
        (7, 2): 1.3,
        (4, 5): 0.2,
        (7, 5): -0.8,
    }
    direct = same_center_convolution(matrix, rows, centers)
    transformed = unitary_center_dft(matrix, rows, modulus)
    reconstructed = center_fourier_convolution(transformed, rows, modulus)
    assert reconstructed == pytest.approx(direct, abs=1.0e-10)


def test_frequencywise_convexity_loses_one_full_matching_degree() -> None:
    size = 7
    rows = [2**index for index in range(size)]
    centers = list(range(size))
    modulus = 17
    matrix = partial_matching_fixture(size)
    direct = convolution_energy(same_center_convolution(matrix, rows, centers))
    transformed = unnormalized_center_dft(matrix, rows, modulus)
    frequencywise = averaged_frequency_convolution_energy(
        transformed, rows, modulus
    )
    assert direct == pytest.approx(size)
    assert row_pair_energy(matrix, rows, centers) == pytest.approx(size)
    assert frequencywise == pytest.approx(size**2, abs=1.0e-10)


def test_repeated_rows_expose_the_false_convolution_relaxation() -> None:
    row_count = 12
    center_count = 5
    rows = list(range(row_count))
    centers = list(range(center_count))
    matrix = repeated_row_fixture(row_count, center_count)
    coefficient_norm_squared = row_count * center_count
    ungrouped = row_pair_energy(matrix, rows, centers)
    grouped = convolution_energy(same_center_convolution(matrix, rows, centers))
    assert ungrouped == coefficient_norm_squared**2
    assert grouped == center_count**2 * interval_additive_energy(row_count)
    assert grouped > 7 * coefficient_norm_squared**2


def test_density_obstruction_is_an_exact_two_stage_cauchy_bound() -> None:
    rows = [0, 1, 2]
    centers = [0, 1]
    matrix = {
        (0, 0): 1.0,
        (1, 0): 2.0,
        (1, 1): 1.0,
        (2, 1): 3.0,
    }
    convolution = same_center_convolution(matrix, rows, centers)
    mass, first, second = density_lower_bound(matrix, rows, centers)
    assert sum(convolution.values()).real == pytest.approx(mass)
    assert convolution_energy(convolution) >= first - 1.0e-12
    assert first >= second - 1.0e-12


def test_exact_integer_hard_window_refutes_ccsr_but_not_row_pair_target() -> None:
    # This is an exact hard-window witness on every integer in the physical
    # logarithmic shell.  It is deliberately *not* an actual-prime-power or
    # critical-asymptotic counterexample.
    q = 80
    degree = 33
    nodes = integer_log_shell(q)
    assert nodes == list(range(33, 49))
    coefficients = {color: 1.0 for color in nodes}
    matrix = hard_window_matrix(q, degree, nodes, coefficients)
    grouped = convolution_energy(same_center_convolution(matrix, nodes, nodes))
    ungrouped = row_pair_energy(matrix, nodes, nodes)
    grouped_off_diagonal = convolution_energy(
        same_center_convolution(matrix, nodes, nodes, distinct_rows=True)
    )
    ungrouped_off_diagonal = row_pair_energy(
        matrix, nodes, nodes, distinct_rows=True
    )
    target = degree * len(nodes) ** 2
    assert maximum_cell_multiplicity(q, degree, nodes) == 1
    assert sum(value.real for value in matrix.values()) == 94
    assert grouped == 16060
    assert ungrouped == 2310
    assert grouped_off_diagonal == 12572
    assert ungrouped_off_diagonal == 1698
    assert grouped > target == 8448
    assert grouped_off_diagonal > target
    assert ungrouped < target
