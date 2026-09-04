from fractions import Fraction

from qp_nonzero_poisson_cubic_saddle import (
    centered_cusp_coordinates,
    cubic_dyadic_exponent_ledger,
    exact_integer_cubic_parameters,
    is_rational_cubic_pair,
    phase_derivative_numerators_at_cubic,
    verify_centered_phase_identity,
)


def test_exact_symmetric_integer_cubic_saddle() -> None:
    Q, t = 101, 7
    h, k, x, m = exact_integer_cubic_parameters(t, 1, 1, Q * Q, 2 * Q)
    assert (h, k, x, m) == (t, -t, Fraction(Q), Fraction(-2 * t))
    derivatives = phase_derivative_numerators_at_cubic(t, 1, 1, Q * Q, 2 * Q)
    assert derivatives["first"] == derivatives["second"] == 0
    assert derivatives["third"] != 0


def test_rational_caustics_are_exactly_common_cube_kernel_pairs() -> None:
    assert is_rational_cubic_pair(5 * 2**3, 5 * 3**3) == (True, 5, 2, 3)
    assert is_rational_cubic_pair(17, 17) == (True, 17, 1, 1)
    assert is_rational_cubic_pair(2, 3) == (False, 0, 0, 0)


def test_centered_cusp_normal_form_is_exact() -> None:
    for data in ((7, -7, -14, 101, 9), (5, 11, -3, 97, -12)):
        assert verify_centered_phase_identity(*data)
    coords = centered_cusp_coordinates(7, -7, -14, 101)
    assert coords.p == 0
    assert coords.ell == 0
    assert coords.d == -14


def test_dyadic_exponents_distinguish_sparse_cubics_from_regular_modes() -> None:
    ledger = cubic_dyadic_exponent_ledger()
    assert ledger["exact_cubic_family"] == Fraction(-1, 24)
    assert ledger["one_airymode_per_pair"] == Fraction(49, 48)
    assert ledger["regular_dual_modes"] == Fraction(25, 16)
    assert ledger["crude_uniform_cubic_for_every_mode"] == Fraction(25, 12)
    assert ledger["remaining_regular_gap"] == Fraction(17, 16)
