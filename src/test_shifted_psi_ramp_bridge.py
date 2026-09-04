from __future__ import annotations

import math
from fractions import Fraction

import mpmath as mp
import pytest

from shifted_psi_ramp_bridge import (
    centered_triangular_ramp,
    completed_archimedean_ramp,
    exact_bridge_multiplier_product,
    exact_general_bridge_multiplier_product,
    exact_general_mertens_deformation_partial_fractions,
    exact_mertens_deformation_multiplier_product,
    euler_boundary_crossing,
    euler_boundary_profile,
    euler_boundary_profile_two_term,
    inverse_bridge_kernel,
    shifted_bounded_ramp,
    shifted_bounded_ramp_from_moments,
    shifted_suzuki_psi,
    two_scale_pole_killing_ramp,
    von_mangoldt_table,
    weighted_mertens_integral_constant,
    weighted_mertens_error,
)


def test_von_mangoldt_table_includes_exact_prime_powers() -> None:
    table = von_mangoldt_table(16)
    assert table[2] == pytest.approx(math.log(2))
    assert table[4] == pytest.approx(math.log(2))
    assert table[8] == pytest.approx(math.log(2))
    assert table[9] == pytest.approx(math.log(3))
    assert table[12] == 0


def test_prime_only_table_deletes_proper_powers() -> None:
    table = von_mangoldt_table(16, prime_only=True)
    assert table[2] == pytest.approx(math.log(2))
    assert table[4] == 0
    assert table[9] == 0


def test_two_moment_formula_matches_direct_ramp() -> None:
    alpha = 0.83
    x = 97.0
    table = von_mangoldt_table(97)
    lower = sum(table[n] * n ** (-alpha) for n in range(2, 98))
    upper = sum(table[n] * n ** (1 - 2 * alpha) for n in range(2, 98))
    assert shifted_bounded_ramp(alpha, x, table) == pytest.approx(
        shifted_bounded_ramp_from_moments(alpha, x, lower, upper),
        abs=2e-14,
    )


def test_exact_bridge_multiplier_is_double_integration() -> None:
    for q, kappa in (
        (Fraction(7, 5), Fraction(1, 5)),
        (Fraction(11, 7), Fraction(2, 7)),
    ):
        assert exact_bridge_multiplier_product(q, kappa) == 1 / q**2


def test_exact_general_bridge_multiplier_is_double_integration() -> None:
    for q, kappa, decay in (
        (Fraction(7, 5), Fraction(1, 5), Fraction(3, 10)),
        (Fraction(11, 7), Fraction(2, 7), Fraction(5, 9)),
    ):
        assert exact_general_bridge_multiplier_product(
            q, kappa, decay
        ) == 1 / q**2


def test_exact_mertens_deformation_partial_fractions() -> None:
    for q, kappa in (
        (Fraction(7, 5), Fraction(1, 5)),
        (Fraction(11, 7), Fraction(2, 7)),
    ):
        assert exact_mertens_deformation_multiplier_product(q, kappa) == 0


def test_general_mertens_deformation_partial_fractions() -> None:
    for q, kappa, decay in (
        (Fraction(7, 5), Fraction(1, 5), Fraction(3, 10)),
        (Fraction(11, 7), Fraction(2, 7), Fraction(5, 9)),
    ):
        assert (
            exact_general_mertens_deformation_partial_fractions(
                q, kappa, decay
            )
            == 0
        )


def test_general_ramp_specializes_to_symmetric_ramp() -> None:
    alpha = 0.83
    x = 97.0
    table = von_mangoldt_table(97)
    assert two_scale_pole_killing_ramp(
        alpha, 1 - alpha, x, table
    ) == pytest.approx(shifted_bounded_ramp(alpha, x, table), abs=2e-14)


def test_euler_boundary_layer_constants_and_crossing() -> None:
    mp.mp.dps = 50
    constant = weighted_mertens_integral_constant()
    assert mp.almosteq(
        constant,
        mp.mpf("0.18754623284036522459720338460544158838394446358095"),
    )
    assert abs(euler_boundary_profile(mp.log(2))) < mp.mpf("1e-49")
    kappa = mp.mpf("1e-6")
    crossing = euler_boundary_crossing(kappa)
    assert crossing > mp.log(2)
    assert euler_boundary_profile_two_term(kappa, crossing) == pytest.approx(
        0.0, abs=1e-12
    )


def test_general_boundary_profile_crosses_at_kernel_sign_change() -> None:
    mp.mp.dps = 50
    for ratio in (mp.mpf("0.5"), mp.mpf("2"), mp.mpf("7")):
        crossing = mp.log(ratio + 1) / ratio
        assert abs(euler_boundary_profile(crossing, ratio)) < mp.mpf("1e-49")


def test_single_atom_bridge_is_triangular_ramp() -> None:
    mp.mp.dps = 50
    for kappa, duration in ((mp.mpf("0.1"), mp.mpf("0.2")), (mp.mpf("0.3"), mp.mpf("2"))):
        integral = mp.quad(
            lambda elapsed: inverse_bridge_kernel(kappa, duration - elapsed)
            * (2 * mp.e ** (-kappa * elapsed) - 1),
            [0, duration],
        )
        assert mp.almosteq(integral, duration)


def test_continuum_bridge_is_negative_pole_ramp() -> None:
    mp.mp.dps = 50
    kappa = mp.mpf("0.17")
    t = mp.mpf("1.3")
    integral = mp.quad(
        lambda u: inverse_bridge_kernel(kappa, t - u)
        * (-(1 - mp.e ** (-kappa * u)) / kappa),
        [0, t],
    )
    expected = -(mp.e ** (kappa * t) - 1 - kappa * t) / kappa**2
    assert abs(integral - expected) < mp.mpf("1e-45")


def test_weighted_mertens_boundary_identity_keeps_endpoint_exponential() -> None:
    """A one-atom Stieltjes model catches a missing ``exp(kappa*t)``."""
    mp.mp.dps = 50
    kappa = mp.mpf("0.17")
    t = mp.mpf("1.3")
    atom_time = mp.mpf("0.4")
    atom_mass = mp.mpf("0.7")

    direct = atom_mass * (
        2 * mp.e ** (-kappa * t + 2 * kappa * atom_time)
        - mp.e ** (kappa * atom_time)
    ) - (1 - mp.e ** (-kappa * t)) / kappa

    def remainder(u: mp.mpf, *, after_atom: bool) -> mp.mpf:
        cumulative = atom_mass if after_atom else 0
        return cumulative - u + mp.euler

    def integrand(u: mp.mpf, *, after_atom: bool) -> mp.mpf:
        kernel_derivative = (
            4 * mp.e ** (-kappa * t + 2 * kappa * u)
            - mp.e ** (kappa * u)
        )
        return kernel_derivative * remainder(u, after_atom=after_atom)

    integral = mp.quad(
        lambda u: integrand(u, after_atom=False), [0, atom_time]
    ) + mp.quad(
        lambda u: integrand(u, after_atom=True), [atom_time, t]
    )
    endpoint_remainder = remainder(t, after_atom=True)
    reconstructed = (
        mp.euler * (1 - 2 * mp.e ** (-kappa * t))
        + mp.e ** (kappa * t) * endpoint_remainder
        - kappa * integral
    )
    assert abs(direct - reconstructed) < mp.mpf("1e-45")


def test_shifted_psi_is_archimedean_minus_centered_prime_ramp() -> None:
    mp.mp.dps = 50
    alpha = mp.mpf("0.9")
    t = mp.log(100)
    table = von_mangoldt_table(100)
    atoms = [(n, mp.mpf(table[n])) for n in range(2, 101) if table[n]]
    psi_value = shifted_suzuki_psi(alpha, t, atoms)
    assert mp.almosteq(
        psi_value,
        completed_archimedean_ramp(alpha, t)
        - centered_triangular_ramp(alpha, t, atoms),
    )
    assert mp.isfinite(psi_value)


def test_shifted_psi_matches_suzuki_published_explicit_expression() -> None:
    mp.mp.dps = 60
    alpha = mp.mpf("0.9")
    t = mp.log(100)
    table = von_mangoldt_table(100)
    atoms = [(n, mp.mpf(table[n])) for n in range(2, 101) if table[n]]

    def e_term(parameter: mp.mpf) -> mp.mpf:
        return (
            mp.e ** (-parameter * t) - 1 + parameter * t
        ) / parameter**2

    published_poles = e_term(alpha - 1) + e_term(alpha)
    published_gamma = (
        t * (mp.digamma(alpha / 2) - mp.log(mp.pi)) / 2
        + (
            mp.polygamma(1, alpha / 2)
            - mp.e ** (-alpha * t)
            * mp.lerchphi(mp.e ** (-2 * t), 2, alpha / 2)
        )
        / 4
    )
    published_prime_ramp = mp.fsum(
        weight * mp.power(integer, -alpha) * (t - mp.log(integer))
        for integer, weight in atoms
    )
    published = published_poles + published_gamma - published_prime_ramp
    assert abs(shifted_suzuki_psi(alpha, t, atoms) - published) < mp.mpf(
        "1e-55"
    )


def test_shifted_ramp_tends_to_weighted_mertens_at_fixed_x() -> None:
    x = 100.0
    table = von_mangoldt_table(100)
    target = weighted_mertens_error(x, table)
    near_endpoint = shifted_bounded_ramp(1 - 1e-7, x, table)
    assert near_endpoint == pytest.approx(target, abs=3e-6)


def test_invalid_alpha_is_rejected() -> None:
    table = von_mangoldt_table(10)
    with pytest.raises(ValueError):
        shifted_bounded_ramp(0.5, 10, table)
    with pytest.raises(ValueError):
        shifted_bounded_ramp(1.0, 10, table)
