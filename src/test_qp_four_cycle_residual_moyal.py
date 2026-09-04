import numpy as np

from qp_four_cycle_residual_moyal import (
    affine_fourier_matrix_unit,
    affine_permutation,
    centered_affine_permutation,
    cyclic_zero_mode_ledger,
    residual_shift,
    strict_shell_collision_forces_equality,
)


def test_centered_affine_gram_is_orthogonal_across_slopes() -> None:
    prime = 7
    for slope in range(1, prime):
        for shift in range(prime):
            left = centered_affine_permutation(prime, slope, shift)
            for other_slope in range(1, prime):
                for other_shift in range(prime):
                    right = centered_affine_permutation(
                        prime, other_slope, other_shift
                    )
                    gram = np.vdot(left, right)
                    expected = (
                        prime * (slope == other_slope and shift == other_shift)
                        - (slope == other_slope)
                    )
                    assert abs(gram - expected) < 1.0e-12


def test_affine_shift_fourier_transform_is_a_matrix_unit() -> None:
    prime = 7
    slope = 3
    frequency = 2
    direct = sum(
        np.exp(-2j * np.pi * frequency * shift / prime)
        * affine_permutation(prime, slope, shift)
        for shift in range(prime)
    ) / prime
    closed = affine_fourier_matrix_unit(prime, slope, frequency)
    assert np.max(np.abs(direct - closed)) < 1.0e-12
    assert abs(np.vdot(closed, closed) - 1.0) < 1.0e-12
    assert np.linalg.matrix_rank(closed, tol=1.0e-10) == 1


def test_nonzero_affine_fourier_units_are_orthonormal() -> None:
    prime = 5
    units = [
        affine_fourier_matrix_unit(prime, slope, frequency)
        for slope in range(1, prime)
        for frequency in range(1, prime)
    ]
    gram = np.asarray([[np.vdot(left, right) for right in units] for left in units])
    assert np.max(np.abs(gram - np.eye(len(units)))) < 1.0e-12


def test_strict_shell_shift_collision_is_injective() -> None:
    fixed = (11, 13)
    first = (17, 19)
    assert residual_shift(fixed, first) == 11 * 17 - 13 * 19
    assert strict_shell_collision_forces_equality(
        fixed,
        first,
        first,
        shell_minimum=11,
        shell_maximum=19,
    )


def test_cyclic_zero_mode_loses_one_full_matching_factor() -> None:
    ledger = cyclic_zero_mode_ledger(5)
    assert ledger.ordered_distinct_color_pairs == 20
    assert ledger.matching_layers == ledger.maximum_degree == 20
    assert ledger.tensor_pair_norm_squared == 0.8
    assert ledger.averaged_modulated_energy == 16.0
    assert ledger.zero_modulation_energy == 320.0
    assert ledger.zero_to_average_ratio == 20.0
    assert ledger.desired_bound_violation_ratio == 16.0
