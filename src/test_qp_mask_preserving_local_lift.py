from fractions import Fraction
from math import gcd

import pytest

from qp_mask_preserving_local_lift import (
    complete_bilinear_prediction,
    complete_bilinear_sum,
    cross_modulus_phase_intersections,
    difference_of_products_prime_fixture,
    flat_product_energy_ledger,
    formal_hecke_product_support,
    polar_projection_frame_ledger,
    physical_tuple_delta_profile,
    separated_short_shift_energy_ledger,
    separated_product_support_fixture,
    separated_short_shift_coefficients,
)


def test_first_poisson_ranges_intersect_only_on_coherent_residues() -> None:
    intersections = cross_modulus_phase_intersections(5, 2, 7, 3, 11, 7)
    assert intersections == tuple((r, 0, r, 0) for r in range(5))


@pytest.mark.parametrize("u,v", [(1, 1), (2, 3), (4, 7), (8, 5)])
def test_coherent_projection_preserves_every_nonzero_complete_phase(
    u: int, v: int
) -> None:
    c, a = 11, 2
    full = complete_bilinear_sum(c, a, u, v)
    projected = complete_bilinear_sum(
        c, a, u, v, delete_color_zero=True
    )
    assert full == pytest.approx(complete_bilinear_prediction(c, a, u, v))
    assert projected == pytest.approx(
        complete_bilinear_prediction(
            c, a, u, v, delete_color_zero=True
        )
    )
    assert projected == pytest.approx(full)


def test_two_zero_projections_leave_only_an_axis_ramanujan_correction() -> None:
    c, a, u, v = 11, 2, 3, 4
    projected = complete_bilinear_sum(
        c, a, u, v, delete_row_zero=True, delete_color_zero=True
    )
    predicted = complete_bilinear_prediction(
        c, a, u, v, delete_row_zero=True, delete_color_zero=True
    )
    assert projected == pytest.approx(predicted)
    assert projected - complete_bilinear_sum(c, a, u, v) == pytest.approx(1)


def test_full_double_poisson_index_is_not_physical_tuple_invariant() -> None:
    # 5*3-7*2=1, so these are exact opposite-cusp Bezout data.
    profile = physical_tuple_delta_profile(
        5, 7, 2, 3, 1, 2, 1, 2, (11, 13, 17, 19)
    )
    assert profile == (
        (11, 2, -2, -1, 3, -1),
        (13, 1, -3, 2, 1, -5),
        (17, -1, 2, -2, -3, -8),
        (19, -2, 1, 1, 2, -4),
    )
    assert all(gcd(c, 5 * 7) == 1 for c, *_ in profile)
    assert all(all(value != 0 for value in row[1:]) for row in profile)


def test_additive_autocorrelation_defeats_the_sharp_tensor_norm() -> None:
    ledger = flat_product_energy_ledger(8)
    assert ledger["diagonal"] <= 8**3
    assert ledger["off_diagonal_l1"] == 8**4 - ledger["diagonal"]
    assert ledger["off_diagonal_l2_squared"] >= ledger["cauchy_lower_bound"]
    assert ledger["tensor_rhs"] == 8**4
    assert ledger["lower_bound_ratio"] == Fraction(49, 2)
    assert ledger["off_diagonal_l2_squared"] > 20 * ledger["tensor_rhs"]


def test_difference_index_is_not_a_product_of_two_short_hecke_indices() -> None:
    Y, prime = 5, 7
    nu, mu, nu_prime, mu_prime = difference_of_products_prime_fixture(Y, prime)
    assert nu * mu - nu_prime * mu_prime == prime
    assert max(nu, mu, nu_prime, mu_prime) <= Y
    # A prime p>Y cannot divide either m or n<=Y, so the formal Hecke
    # product relation never creates lambda(p).
    assert prime not in formal_hecke_product_support(Y)


def test_separated_nonzero_support_has_an_exact_modulated_triangular_tail() -> None:
    Y, L, K, modulation = 256, 16, 3, 5
    first, second = separated_product_support_fixture(Y, L, K, modulation)
    assert min(first) > 0 and min(second) > 0
    assert len(first) == L and len(second) == K + 1
    coefficients = separated_short_shift_coefficients(Y, L, K, modulation)
    for shift, coefficient in coefficients.items():
        expected = (L - shift) * __import__("cmath").exp(
            2j * __import__("math").pi * modulation * shift / L
        )
        assert coefficient == pytest.approx(expected)
    short_energy = sum(abs(value) ** 2 for value in coefficients.values())
    tensor_rhs = (len(first) * len(second)) ** 2
    assert short_energy == pytest.approx(sum(value * value for value in range(1, L)))
    assert tensor_rhs == L**2 * (K + 1) ** 2


def test_separated_tail_has_polynomial_excess_at_asymptotic_scale() -> None:
    # Here K=L^(1/4).  The exact energy ratio is asymptotic to L^(1/2)/3.
    length = 1 << 24
    ledger = separated_short_shift_energy_ledger(length, 64)
    assert ledger["short_shift_energy"] > 1000 * ledger["tensor_rhs"]
    assert ledger["energy_ratio"] > 1000
    assert ledger["minimum_rank_from_trace"] > 9 * length // 10
    rank = ledger["minimum_rank_from_trace"]
    remaining = length - rank - 1
    square_pyramid = lambda value: value * (value + 1) * (2 * value + 1) // 6
    assert square_pyramid(remaining) <= ledger["tensor_rhs"]
    assert square_pyramid(remaining + 1) > ledger["tensor_rhs"]


def test_modulated_triangles_have_the_exact_diagonal_frame_operator() -> None:
    import cmath
    import math

    length = 9
    vectors = [
        {
            shift: (length - shift)
            * cmath.exp(2j * math.pi * modulation * shift / length)
            for shift in range(1, length)
        }
        for modulation in range(length)
    ]
    for first_shift in range(1, length):
        for second_shift in range(1, length):
            frame_entry = sum(
                vector[first_shift] * vector[second_shift].conjugate()
                for vector in vectors
            ) / length
            expected = (
                (length - first_shift) ** 2
                if first_shift == second_shift
                else 0
            )
            assert frame_entry == pytest.approx(expected)


def test_subpower_rank_polar_projection_cannot_remove_all_modulations() -> None:
    ledger = polar_projection_frame_ledger(256, 4)
    assert ledger["one_vector_norm_squared"] == sum(
        value * value for value in range(1, 256)
    )
    assert ledger["projection_average_upper_bound"] == 4 * 255**2
    assert ledger["ky_fan_projection_average_upper_bound"] == sum(
        value * value for value in range(252, 256)
    )
    assert ledger["some_residual_norm_squared"] == sum(
        value * value for value in range(1, 252)
    )
    assert ledger["some_residual_norm_squared"] > (
        9 * ledger["one_vector_norm_squared"] // 10
    )
