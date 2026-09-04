from fractions import Fraction

import pytest

from qp_phase_jet_inverse import (
    action_jet_inverse_determinant,
    critical_action_jet,
    distinguished_affine_height_probes,
    fold_height_branch_exponent_ledger,
    fold_height_zero_parametrization,
    nonlinear_action_quotient_rigidity,
    recover_regular_packet_from_action_jet,
    scaled_cusp_affine_defects,
    second_third_jet_mirror,
    square_content_from_double_intercept_collision,
)


def test_generic_first_three_action_derivatives_recover_the_packet() -> None:
    C, S, p, d = 101**2, 202, 5, 2
    h, k, m = 2 * 7**2, 5 * 3**2, 3 * 5**2
    jet = critical_action_jet(C, S, p, d, h, k, m)
    recovered = recover_regular_packet_from_action_jet(
        C, S, jet["first"], jet["second"], jet["third"]
    )
    assert recovered["a"] == Fraction(707, 5)
    assert recovered["b"] == Fraction(303, 5)
    assert recovered["h"] == h
    assert recovered["k"] == k
    assert recovered["m"] == m


def test_action_jet_retains_exact_completion_ratio_dependence() -> None:
    C, S, p, d = 11**2, 30, 5, 2
    r, s = p + d, p - d
    h, k = 2 * r * r, 5 * s * s
    m = Fraction(4 * C * p * p, S * S) * (
        Fraction(k, s * s) - Fraction(h, r * r)
    )
    jet = critical_action_jet(C, S, p, d, h, k, m)
    fold = h * s**3 + k * r**3
    assert jet["action"] == Fraction(4 * C * p, S) * (
        Fraction(h, r) - Fraction(k * d, s * s)
    )
    assert jet["first"] == -Fraction(4 * C * p * p * k, S * S * s * s)
    assert jet["second"] == Fraction(
        16 * C * p**3 * h * k, S**3 * fold
    )
    assert jet["third"] == -Fraction(
        96 * C * p**4 * h * k * (k * k * r**5 + h * h * s**5),
        S**4 * fold**3,
    )


def test_inverse_determinant_is_exactly_the_zero_poisson_factor() -> None:
    C, S, p, d = 101**2, 202, 5, 2
    data = action_jet_inverse_determinant(
        C, S, p, d, 2 * 7**2, 5 * 3**2, 3 * 5**2
    )
    assert data["direct"] == data["square"] == data["poisson"]
    assert data["direct"] > 0

    zero = critical_action_jet(C, S, p, d, 7**2, 3**2, 0)
    c = (zero["second"] / (2 * C)) / (-zero["first"] / C)
    R = -zero["third"] / (3 * zero["second"])
    assert c * S == 1
    assert R + c * c * S - 2 * c == 0
    with pytest.raises(ValueError, match="zero-Poisson"):
        recover_regular_packet_from_action_jet(
            C, S, zero["first"], zero["second"], zero["third"]
        )


def test_orders_two_through_four_recover_geometry_up_to_reflection() -> None:
    C, S, p, d = 101**2, 202, 5, 2
    h, k, m = 98, 45, 75
    original = critical_action_jet(C, S, p, d, h, k, m)
    reflected = critical_action_jet(C, S, p, -d, k, h, -m)
    for name in ("second", "third", "fourth"):
        assert reflected[name] == original[name]
    assert reflected["action"] == original["action"] + m * S
    assert reflected["first"] == original["first"] + m

    quotient = nonlinear_action_quotient_rigidity(C, S, p, d, h, k, m)
    reflected_quotient = nonlinear_action_quotient_rigidity(
        C, S, p, -d, k, h, -m
    )
    assert reflected_quotient["t"] == quotient["reflected_t"]
    assert reflected_quotient["u"] == quotient["reflected_u"]
    assert reflected_quotient["A"] == quotient["A"]
    assert reflected_quotient["B"] == quotient["B"]
    assert quotient["jacobian"] > 0


def test_second_and_third_derivatives_alone_have_an_exact_mirror() -> None:
    C, S, p, d = 101**2, 202, 5, 2
    data = second_third_jet_mirror(C, S, p, d, 98, 45)
    assert data["second"] != 0
    assert data["third"] != 0
    assert (data["mirror_h"], data["mirror_k"]) != (98, 45)
    assert data["mirror_first"] != data["first"]
    assert data["mirror_rho"] == 2 * Fraction(7, 10) - data["rho"]


def test_scaled_cusp_factors_are_exact_affine_intercept_defects() -> None:
    # The non-square-content residual family with m=2,d=3 from the audit.
    data = scaled_cusp_affine_defects(Q=93, y=40, g=6, p=7, d=3)
    assert data["U"] == 0
    assert data["H"] == -6
    assert data["j_minus"] == data["j_plus"] == -6
    assert data["delta_alpha"] == Fraction(-3, 100)
    assert data["delta_beta"] == Fraction(-3, 16)
    assert data["z"] == 6


def test_physical_reflection_swaps_the_two_affine_axes() -> None:
    original = scaled_cusp_affine_defects(Q=30, y=11, g=2, p=5, d=2)
    reflected = scaled_cusp_affine_defects(Q=30, y=-11, g=2, p=5, d=-2)
    assert reflected["U"] == original["U"]
    assert reflected["H"] == original["H"]
    assert reflected["j_minus"] == original["j_plus"]
    assert reflected["j_plus"] == original["j_minus"]
    assert reflected["delta_alpha"] == original["delta_beta"]
    assert reflected["delta_beta"] == original["delta_alpha"]


def test_distinguished_normals_probe_the_three_axes_and_fold_height() -> None:
    data = distinguished_affine_height_probes(Q=93, y=40, g=6, p=7, d=3)
    assert data["left_probe"] == -3
    assert data["right_probe"] == -3
    assert data["zero_probe"] == -6
    assert data["fold_invariant"] == -6
    assert data["fold_probe"] == -18


def test_double_intercept_collision_forces_square_content() -> None:
    # Exact cusp: ell=21, g=8, p=5, d=2, Q=105, y=42.
    assert square_content_from_double_intercept_collision(105, 42, 8, 5, 2)
    data = distinguished_affine_height_probes(105, 42, 8, 5, 2)
    assert data["H"] == data["U"] == 0
    assert data["left_probe"] == data["right_probe"] == 0


def test_fold_height_zero_is_a_real_nonsquare_content_branch() -> None:
    # p=5,d=2,Q=30,g=2,y=11 gives H=pU but d^2 does not divide g.
    data = fold_height_zero_parametrization(30, 11, 2, 5, 2)
    assert data["fold_invariant"] == 0
    assert data["j_minus"] == 6
    assert data["j_plus"] == 14
    assert (data["w"], data["M"], data["a_scale"]) == (1, 6, 1)
    assert (data["n"], data["e"], data["f"]) == (-5, 2, 12)
    assert data["eta"] == 8
    assert data["divisor_factorization"] == data["divisor_target"] == 84
    assert not data["square_content"]


def test_fold_height_branch_closes_inside_the_square_root_budget() -> None:
    ledger = fold_height_branch_exponent_ledger()
    assert ledger["low_w_d_count"] == Fraction(23, 64)
    assert ledger["low_w_saving"] == Fraction(9, 64)
    assert ledger["w_spacing_floor"] > ledger["sqrt_A_ceiling"]
