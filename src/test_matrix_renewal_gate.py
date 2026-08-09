from fractions import Fraction

import pytest

from matrix_renewal_gate import (
    diagonal_bosonic_coefficient,
    eta_coefficient,
    exponential_renewal_characteristic,
    mobius,
    noncommuting_cubic_cycle_traces,
    primitive_characteristic_coefficient,
    rank_one_matrix,
    reciprocal_eta_coefficient,
    symmetrized_cubic_log_mass,
)


@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, 1), (2, -1), (3, -1), (4, 0), (6, 1), (12, 0), (30, -1)],
)
def test_mobius_exact(n: int, expected: int) -> None:
    assert mobius(n) == expected


@pytest.mark.parametrize("q, prime", [(2, 3), (2, 5), (3, 2), (3, 5), (7, 11)])
def test_reciprocal_eta_has_negative_untouched_prime_atom(q: int, prime: int) -> None:
    assert reciprocal_eta_coefficient(q, prime) == -1


@pytest.mark.parametrize("q, prime", [(2, 3), (2, 5), (3, 2), (3, 5)])
def test_eta_has_wrong_primitive_sign_for_positive_characteristic_determinant(
    q: int, prime: int
) -> None:
    assert eta_coefficient(q, prime) == 1
    assert primitive_characteristic_coefficient(Fraction(1)) == -1


def test_noncommuting_loewner_positive_cycles_can_have_negative_trace() -> None:
    matrices = [
        rank_one_matrix((1, 0)),
        rank_one_matrix((1, 1)),
        rank_one_matrix((-1, 2)),
    ]
    for matrix in matrices:
        assert matrix[0][0] >= 0
        assert matrix[1][1] >= 0
        assert matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2 == 0
    assert noncommuting_cubic_cycle_traces() == (Fraction(-1),) * 6
    assert symmetrized_cubic_log_mass() == Fraction(-2)


def test_exponential_delay_has_only_the_endpoint_characteristic_zero() -> None:
    rate = 2.5
    assert exponential_renewal_characteristic(0j, rate) == 0
    for z in [0.1, -0.2 + 3j, 1 + 20j, -2 + 0.25j]:
        assert exponential_renewal_characteristic(z, rate) != 0
    with pytest.raises(ZeroDivisionError):
        exponential_renewal_characteristic(complex(-rate), rate)


@pytest.mark.parametrize("j,k", [(0, 0), (1, 0), (0, 3), (4, 2)])
def test_diagonal_bosonic_partition_coefficients_are_nonnegative(j: int, k: int) -> None:
    assert diagonal_bosonic_coefficient(Fraction(1, 3), Fraction(2, 5), j, k) >= 0


def test_invalid_arguments_are_rejected() -> None:
    with pytest.raises(ValueError):
        reciprocal_eta_coefficient(1, 3)
    with pytest.raises(ValueError):
        eta_coefficient(2, 0)
    with pytest.raises(ValueError):
        exponential_renewal_characteristic(1, 0)
    with pytest.raises(ValueError):
        diagonal_bosonic_coefficient(1, 1, -1, 0)
