from fractions import Fraction

from qp_approximate_tangent_character_stability import (
    dyadic_wrap_coherence_loss,
    finite_wrapped_fold_fixture,
    high_p_stability_exponent_ledger,
    integer_poisson_alias_gram,
    no_wrap_curvature_lower_bound,
    normalized_fejer_coefficient,
    opposite_sign_joint_identity,
    regular_plateau_near_character,
    wrap_resonance_form,
)


def test_regular_singleton_is_exact_and_lives_on_the_fejer_plateau() -> None:
    data = regular_plateau_near_character(100, 3)
    assert (data["h"], data["k"], data["m"]) == (26, 24, 1)
    assert data["stationary_error"] == Fraction(-81, 99820081)
    assert data["second_derivative"] > 0
    assert normalized_fejer_coefficient(235, 26) > Fraction(1, 2 * 235)
    assert normalized_fejer_coefficient(235, 24) > Fraction(1, 2 * 235)


def test_joint_residue_fold_identity_and_no_wrap_bound_are_exact() -> None:
    # This family has an exceptionally small stationary residue but is forced
    # away from the fold by curvature of constant size.
    p, d, h, v = 1000, 1, 2003, 1997
    data = opposite_sign_joint_identity(p, d, h, v)
    A = data["A"]
    tolerance = abs(A - 4000)
    assert tolerance == Fraction(4000, (p * p - 1) ** 2)
    lower = no_wrap_curvature_lower_bound(p, d, h, v, tolerance)
    assert abs(data["second_derivative"]) >= lower
    assert lower > 11


def test_wrap_equation_is_linear_with_only_the_parity_gcd_exception() -> None:
    for p, d, h, v, wrap in (
        (100, 3, 26, 24, 1),
        (11, 2, 7, 5, -2),
        (8, 3, 9, 4, 0),
    ):
        data = wrap_resonance_form(p, d, h, v, wrap)
        assert data["gcd"] in (d, 2 * d, 4 * d)
        assert data["b"] // data["gcd"] > 0
        assert data["a"] // data["gcd"] > 0


def test_high_p_counterwindow_and_corrected_curvature_ledger() -> None:
    ledger = high_p_stability_exponent_ledger()
    assert ledger["P_f"] == Fraction(43, 48)
    assert ledger["H_to_five_sixths"] == Fraction(85, 96)
    assert ledger["counter_window"] == Fraction(1, 96)
    assert ledger["counterexample_factor"] == Fraction(1, 32)
    assert ledger["fold_offset_X"] == Fraction(-5, 48)
    assert ledger["slope_tolerance_mu"] == Fraction(-35, 48)
    assert ledger["X_over_mu"] == Fraction(5, 8)
    assert ledger["forced_curvature"] == Fraction(23, 48)
    assert ledger["curved_amplitude"] == Fraction(19, 24)
    assert ledger["no_wrap_total"] == Fraction(55, 96)
    assert ledger["endpoint_sqrt_A_over_B_gain"] > ledger["anisotropic_gain_needed"]


def test_wrapped_fold_fixture_is_simultaneously_near_and_cubic() -> None:
    data = finite_wrapped_fold_fixture()
    assert abs(data["stationary_error"]) < data["tolerance"]
    assert abs(data["second_derivative"]) < 1
    assert abs(data["third_derivative"]) > data["H"]
    assert data["X"] > Fraction(9, 10)


def test_wrap_labels_alias_exactly_on_the_integer_carrier() -> None:
    gram = integer_poisson_alias_gram((101, 103, 107), (7, 8, 11, 15))
    assert gram == ((3, 3, 3, 3),) * 4
    assert dyadic_wrap_coherence_loss(32) == 32
