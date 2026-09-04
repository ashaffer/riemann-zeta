from __future__ import annotations

import math
from fractions import Fraction

import mpmath as mp
import pytest

from pole_killing_boundary_calculus import (
    associated_laguerre_endpoint_flat_kernel,
    coefficient_signs,
    compact_chebyshev_pole_killer_kernel,
    compact_chebyshev_notch_residuals,
    compact_chebyshev_polynomial_coefficients,
    compact_linear_pole_killer_kernel,
    compact_linear_pole_killer_laplace,
    compact_linear_pole_killer_parameter,
    confluent_germ_surrogate,
    confluent_laguerre_kernel,
    exact_anchored_laplace_target,
    exact_anchored_scaled_multiplier,
    exact_associated_laguerre_scaled_multiplier,
    exact_confluent_scaled_multiplier,
    exact_endpoint_mass,
    exact_endpoint_flat_fixed_singularity_multiplier,
    exact_endpoint_flat_laplace_target,
    exact_endpoint_flat_scaled_multiplier,
    exact_fixed_singularity_multiplier,
    exact_laplace_kernel,
    exact_laplace_target,
    exact_multi_anchor_laplace_target,
    exact_multi_anchor_scaled_multiplier,
    exact_pole_moment,
    exact_scaled_multiplier,
    exponential_germ_surrogate,
    exponential_kernel,
    endpoint_flat_exponential_coefficients,
    fractional_laguerre_endpoint_kernel,
    fractional_laguerre_scaled_multiplier,
    inverse_bridge_leading_tail,
    inverse_unstable_polynomial,
    minimal_anchored_exponential_coefficients,
    minimal_exponential_coefficients,
    moment_boundary_expansion,
    multiple_front_splitting_polynomial,
    multi_anchor_exponential_coefficients,
    one_minus_derivative_kernel,
    sigma_minus_derivative_kernel,
)


def test_order_one_specializes_to_the_two_scale_kernel() -> None:
    rate = Fraction(7, 3)
    coefficients = minimal_exponential_coefficients((0, rate))
    assert coefficients == (-1 / rate, (1 + rate) / rate)


def test_order_zero_and_empty_rate_validation() -> None:
    rate = Fraction(7, 3)
    assert minimal_anchored_exponential_coefficients((rate,), Fraction(5, 4)) == (
        Fraction(1),
    )
    assert exact_anchored_laplace_target(
        Fraction(2), (rate,), Fraction(5, 4)
    ) == 1 / (Fraction(2) + rate)
    with pytest.raises(ValueError, match="at least one rate"):
        minimal_anchored_exponential_coefficients(())
    with pytest.raises(ValueError, match="at least one rate"):
        multi_anchor_exponential_coefficients((), ())
    with pytest.raises(ValueError, match="positive integers"):
        multi_anchor_exponential_coefficients(
            (Fraction(0), Fraction(1)), ((Fraction(1), 0),)
        )
    with pytest.raises(ValueError, match="positive integers"):
        exact_multi_anchor_laplace_target(
            Fraction(2),
            (Fraction(0), Fraction(1)),
            ((Fraction(1), 0.5),),  # type: ignore[arg-type]
        )
    with pytest.raises(ValueError, match="at least one rate"):
        exact_laplace_target(Fraction(2), ())
    with pytest.raises(ValueError, match="at least one rate"):
        exact_scaled_multiplier(Fraction(2), Fraction(1, 10), ())
    with pytest.raises(ValueError, match="at least one rate"):
        inverse_unstable_polynomial(Fraction(1, 10), ())
    with pytest.raises(ValueError, match="anchor must be positive"):
        exact_anchored_laplace_target(Fraction(2), (rate,), 0)
    with pytest.raises(ValueError, match="equal length"):
        exact_endpoint_mass((Fraction(0), Fraction(1)), (Fraction(1),))
    with pytest.raises(ValueError, match="nonnegative integer"):
        exact_pole_moment((Fraction(0), Fraction(1)), 0.5)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="nonnegative integer"):
        exact_confluent_scaled_multiplier(
            Fraction(2), Fraction(1, 10), Fraction(0), 0.5  # type: ignore[arg-type]
        )
    with pytest.raises(ValueError, match="nonnegative integer"):
        sigma_minus_derivative_kernel(
            mp.mpf(0), 0.5, (mp.mpf(0),), (mp.mpf(1),)  # type: ignore[arg-type]
        )
    with pytest.raises(ValueError, match="nonnegative integer"):
        confluent_germ_surrogate(
            mp.mpf("0.1"),
            mp.mpf(1),
            0.5,  # type: ignore[arg-type]
            mp.mpf(0),
            lambda _order, value: value,
        )


@pytest.mark.parametrize(
    "rates",
    [
        (Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(2)),
        (Fraction(0), Fraction(1), Fraction(3), Fraction(5)),
        (Fraction(1, 4), Fraction(2, 3), Fraction(7, 5), Fraction(9, 4)),
    ],
)
def test_exact_rational_laplace_identity(rates: tuple[Fraction, ...]) -> None:
    coefficients = minimal_exponential_coefficients(rates)
    order = len(rates) - 1
    assert exact_endpoint_mass(rates, coefficients) == 1
    for derivative_order in range(order):
        assert exact_pole_moment(rates, derivative_order, coefficients) == 0
    for s in (Fraction(3, 2), Fraction(7, 3), Fraction(11, 4)):
        assert exact_laplace_kernel(s, rates, coefficients) == exact_laplace_target(
            s, rates
        )


def test_scaled_multiplier_has_the_claimed_order() -> None:
    rates = (Fraction(0), Fraction(1), Fraction(3), Fraction(5))
    delta = Fraction(2, 7)
    assert exact_scaled_multiplier(delta, delta, rates) == 0
    q = Fraction(11, 7)
    expected = (q - delta) ** 3
    for rate in rates:
        expected /= q + rate * delta
    assert exact_scaled_multiplier(q, delta, rates) == expected


def test_order_two_filter_and_its_two_positive_roots() -> None:
    mp.mp.dps = 60
    rates = (0, 1, 2)
    coefficients = minimal_exponential_coefficients(rates)
    assert coefficients == (Fraction(1, 2), Fraction(-4), Fraction(9, 2))
    roots_in_y = ((4 + mp.sqrt(7)) / 9, (4 - mp.sqrt(7)) / 9)
    roots = tuple(-mp.log(value) for value in roots_in_y)
    assert all(root > 0 for root in roots)
    assert all(abs(exponential_kernel(root, rates)) < mp.mpf("1e-55") for root in roots)


def test_order_three_coefficients_alternate() -> None:
    rates = (0, 1, 2, 3)
    assert minimal_exponential_coefficients(rates) == (
        Fraction(-1, 6),
        Fraction(4),
        Fraction(-27, 2),
        Fraction(32, 3),
    )
    assert coefficient_signs(rates) == (-1, 1, -1, 1)


def test_inverse_has_polynomial_exponential_instability() -> None:
    delta = Fraction(1, 10)
    for order in range(1, 5):
        rates = tuple(Fraction(index) for index in range(order + 1))
        polynomial = inverse_unstable_polynomial(delta, rates)
        assert len(polynomial) == order
        assert polynomial[-1] > 0
        expected_leading = delta ** (order + 1)
        for rate in rates:
            expected_leading *= 1 + rate
        expected_leading /= math.factorial(order - 1)
        assert polynomial[-1] == expected_leading


def test_inverse_principal_part_is_exact_in_every_degree() -> None:
    delta = Fraction(2, 17)
    q = Fraction(13, 11)
    for anchor in (Fraction(1), Fraction(3, 2)):
        for order in range(1, 7):
            rates = tuple(Fraction(index) for index in range(order + 1))
            h = q - anchor * delta
            left = math.prod(
                (q + rate * delta for rate in rates), start=Fraction(1)
            ) / h**order
            polynomial = inverse_unstable_polynomial(delta, rates, anchor)
            right = h + delta * sum(
                (anchor + rate for rate in rates), Fraction(0)
            )
            right += sum(
                coefficient * math.factorial(power) / h ** (power + 1)
                for power, coefficient in enumerate(polynomial)
            )
            assert left == right


def test_kernel_jet_specializes_to_the_known_fixed_ratio_coefficient() -> None:
    mp.mp.dps = 50
    ratio = mp.mpf("2.5")
    c = mp.mpf("0.8")
    rates = (mp.mpf(0), ratio)
    coefficients = (-1 / ratio, (1 + ratio) / ratio)
    for power in range(1, 5):
        expected = ((1 + ratio) ** (power + 1) * mp.e ** (-ratio * c) - 1) / ratio
        assert mp.almosteq(
            one_minus_derivative_kernel(c, power, rates, coefficients),
            expected,
        )


def test_simple_front_shift_is_kernel_independent_to_first_order() -> None:
    mp.mp.dps = 50
    constant = mp.mpf("0.7")
    moment = mp.mpf("0.2")
    delta = mp.mpf("1e-7")
    for ratio in (mp.mpf("0.5"), mp.mpf("2"), mp.mpf("7")):
        rates = (mp.mpf(0), ratio)
        coefficients = (-1 / ratio, (1 + ratio) / ratio)
        root = mp.log(1 + ratio) / ratio
        shifted = root + delta * moment / constant
        value = moment_boundary_expansion(
            delta,
            shifted,
            constant,
            (moment,),
            rates,
            coefficients,
        )
        assert abs(value) < mp.mpf("1e-13")


def test_confluent_laguerre_kernel_has_exact_transform() -> None:
    mp.mp.dps = 50
    s = mp.mpf("1.7")
    rate = mp.mpf("0.4")
    for order in range(1, 5):
        integral = mp.quad(
            lambda z: mp.e ** (-s * z)
            * confluent_laguerre_kernel(z, order, rate),
            [0, mp.inf],
        )
        expected = (s - 1) ** order / (s + rate) ** (order + 1)
        assert abs(integral - expected) < mp.mpf("1e-45")


def test_order_two_laguerre_fronts_are_positive_and_exact() -> None:
    mp.mp.dps = 50
    rate = mp.mpf("0.7")
    roots = (
        (2 - mp.sqrt(2)) / (1 + rate),
        (2 + mp.sqrt(2)) / (1 + rate),
    )
    assert all(root > 0 for root in roots)
    assert all(
        abs(confluent_laguerre_kernel(root, 2, rate)) < mp.mpf("1e-48")
        for root in roots
    )


def test_confluent_scaled_multiplier_zero_order() -> None:
    q = Fraction(5, 7)
    delta = Fraction(1, 7)
    rate = Fraction(3, 2)
    for order in range(1, 6):
        assert exact_confluent_scaled_multiplier(
            delta, delta, rate, order
        ) == 0
        assert exact_confluent_scaled_multiplier(
            q, delta, rate, order
        ) == (q - delta) ** order / (q + rate * delta) ** (order + 1)


def test_multi_anchor_hermite_filter_identity() -> None:
    anchors = ((Fraction(1), 2), (Fraction(3, 2), 1))
    rates = (Fraction(0), Fraction(1), Fraction(2), Fraction(4))
    coefficients = multi_anchor_exponential_coefficients(rates, anchors)
    assert sum(coefficients) == 1
    for s in (Fraction(4, 3), Fraction(7, 4), Fraction(5, 2)):
        assert exact_laplace_kernel(s, rates, coefficients) == (
            exact_multi_anchor_laplace_target(s, rates, anchors)
        )
    # The value and first derivative vanish at the double anchor; the value
    # vanishes at the simple anchor.
    assert sum(
        coefficient / (Fraction(1) + rate)
        for rate, coefficient in zip(rates, coefficients, strict=True)
    ) == 0
    assert sum(
        coefficient / (Fraction(1) + rate) ** 2
        for rate, coefficient in zip(rates, coefficients, strict=True)
    ) == 0
    assert sum(
        coefficient / (Fraction(3, 2) + rate)
        for rate, coefficient in zip(rates, coefficients, strict=True)
    ) == 0


def test_general_anchor_and_scaled_multi_anchor_identities() -> None:
    anchor = Fraction(3, 2)
    rates = (Fraction(0), Fraction(1), Fraction(3))
    coefficients = minimal_anchored_exponential_coefficients(rates, anchor)
    for s in (Fraction(2), Fraction(7, 3), Fraction(11, 4)):
        assert exact_laplace_kernel(s, rates, coefficients) == (
            exact_anchored_laplace_target(s, rates, anchor)
        )
    delta = Fraction(2, 9)
    assert exact_anchored_scaled_multiplier(
        anchor * delta, delta, rates, anchor
    ) == 0

    anchors = ((Fraction(1), 2), (Fraction(3, 2), 1))
    multi_rates = (Fraction(0), Fraction(1), Fraction(2), Fraction(4))
    for q in (Fraction(5, 7), Fraction(11, 9)):
        direct = exact_multi_anchor_scaled_multiplier(
            q, delta, multi_rates, anchors
        )
        expected = math.prod(
            (
                (q - sigma * delta) ** multiplicity
                for sigma, multiplicity in anchors
            ),
            start=Fraction(1),
        ) / math.prod(
            (q + rate * delta for rate in multi_rates), start=Fraction(1)
        )
        assert direct == expected


def test_joint_notch_and_endpoint_flat_classification() -> None:
    anchor = Fraction(3, 2)
    notch_order = 2
    rates = (
        Fraction(0),
        Fraction(1),
        Fraction(2),
        Fraction(4),
        Fraction(7),
    )
    flat_order = len(rates) - notch_order - 1
    coefficients = endpoint_flat_exponential_coefficients(
        rates, notch_order, anchor
    )
    for derivative_order in range(flat_order):
        assert sum(
            coefficient * (-rate) ** derivative_order
            for rate, coefficient in zip(rates, coefficients, strict=True)
        ) == 0
    assert sum(
        coefficient * (-rate) ** flat_order
        for rate, coefficient in zip(rates, coefficients, strict=True)
    ) == 1
    for pole_derivative in range(notch_order):
        assert sum(
            coefficient / (anchor + rate) ** (pole_derivative + 1)
            for rate, coefficient in zip(rates, coefficients, strict=True)
        ) == 0
    for s in (Fraction(2), Fraction(5, 2), Fraction(11, 3)):
        assert exact_laplace_kernel(s, rates, coefficients) == (
            exact_endpoint_flat_laplace_target(
                s, rates, notch_order, anchor
            )
        )
    delta = Fraction(2, 101)
    q = Fraction(7, 5)
    assert exact_endpoint_flat_scaled_multiplier(
        q, delta, rates, notch_order, anchor
    ) == delta**flat_order * (q - anchor * delta) ** notch_order / math.prod(
        (q + rate * delta for rate in rates), start=Fraction(1)
    )


def test_general_anchor_confluent_kernel_and_jet() -> None:
    mp.mp.dps = 50
    anchor = mp.mpf("1.7")
    rate = mp.mpf("0.4")
    s = mp.mpf("2.3")
    order = 3
    integral = mp.quad(
        lambda z: mp.e ** (-s * z)
        * confluent_laguerre_kernel(z, order, rate, anchor),
        [0, mp.inf],
    )
    expected = (s - anchor) ** order / (s + rate) ** (order + 1)
    assert abs(integral - expected) < mp.mpf("1e-45")

    rates = (mp.mpf(0), mp.mpf(1), mp.mpf(3))
    exact_coefficients = minimal_anchored_exponential_coefficients(
        (Fraction(0), Fraction(1), Fraction(3)), Fraction(17, 10)
    )
    coefficients = tuple(mp.mpf(c.numerator) / c.denominator for c in exact_coefficients)
    z = mp.mpf("0.8")
    power = 4
    direct = sigma_minus_derivative_kernel(
        z, power, rates, coefficients, anchor
    )
    expected_jet = mp.fsum(
        coefficient
        * (anchor + local_rate) ** power
        * mp.e ** (-local_rate * z)
        for local_rate, coefficient in zip(rates, coefficients, strict=True)
    )
    assert mp.almosteq(direct, expected_jet)


def test_associated_laguerre_endpoint_flat_normal_form() -> None:
    mp.mp.dps = 60
    notch_order = 3
    flat_order = 2
    rate = mp.mpf("0.4")
    anchor = mp.mpf("1.7")
    s = mp.mpf("2.6")
    integral = mp.quad(
        lambda z: mp.e ** (-s * z)
        * associated_laguerre_endpoint_flat_kernel(
            z, notch_order, flat_order, rate, anchor
        ),
        [0, mp.inf],
    )
    expected = (s - anchor) ** notch_order / (
        s + rate
    ) ** (notch_order + flat_order + 1)
    assert abs(integral - expected) < mp.mpf("1e-50")
    for derivative_order in range(flat_order):
        derivative = mp.diff(
            lambda z: associated_laguerre_endpoint_flat_kernel(
                z, notch_order, flat_order, rate, anchor
            ),
            0,
            derivative_order,
        )
        assert abs(derivative) < mp.mpf("1e-50")
    derivative = mp.diff(
        lambda z: associated_laguerre_endpoint_flat_kernel(
            z, notch_order, flat_order, rate, anchor
        ),
        0,
        flat_order,
    )
    assert abs(derivative - 1) < mp.mpf("1e-50")

    q = Fraction(7, 5)
    delta = Fraction(2, 101)
    rational_rate = Fraction(2, 5)
    rational_anchor = Fraction(17, 10)
    assert exact_associated_laguerre_scaled_multiplier(
        q,
        delta,
        rational_rate,
        notch_order,
        flat_order,
        rational_anchor,
    ) == delta**flat_order * (q - rational_anchor * delta) ** notch_order / (
        q + rational_rate * delta
    ) ** (notch_order + flat_order + 1)


def test_fractional_laguerre_endpoint_flat_normal_form() -> None:
    mp.mp.dps = 60
    notch_order = 3
    alpha = mp.mpf("0.7")
    rate = mp.mpf("0.4")
    anchor = mp.mpf("1.7")
    s = mp.mpf("2.6")
    integral = mp.quad(
        lambda z: mp.e ** (-s * z)
        * fractional_laguerre_endpoint_kernel(
            z, notch_order, alpha, rate, anchor
        ),
        [0, mp.inf],
    )
    expected = (s - anchor) ** notch_order / (
        s + rate
    ) ** (notch_order + alpha + 1)
    assert abs(integral - expected) < mp.mpf("1e-50")

    tiny = mp.mpf("1e-20")
    endpoint_ratio = fractional_laguerre_endpoint_kernel(
        tiny, notch_order, alpha, rate, anchor
    ) / tiny**alpha
    assert abs(endpoint_ratio - 1 / mp.gamma(alpha + 1)) < mp.mpf("1e-18")

    q = mp.mpf("1.4")
    delta = mp.mpf("0.02")
    multiplier = fractional_laguerre_scaled_multiplier(
        q, delta, rate, notch_order, alpha, anchor
    )
    expected_multiplier = delta**alpha * (q - anchor * delta) ** notch_order / (
        q + rate * delta
    ) ** (notch_order + alpha + 1)
    assert abs(multiplier - expected_multiplier) < mp.mpf("1e-55")

    integer_alpha = 2
    z = mp.mpf("0.8")
    assert mp.almosteq(
        fractional_laguerre_endpoint_kernel(
            z, notch_order, integer_alpha, rate, anchor
        ),
        associated_laguerre_endpoint_flat_kernel(
            z, notch_order, integer_alpha, rate, anchor
        ),
    )


def test_compact_pole_killer_and_far_edge_symbol() -> None:
    mp.mp.dps = 70
    support = mp.mpf(1)
    anchor = mp.mpf(1)
    parameter = compact_linear_pole_killer_parameter(support, anchor)
    assert 0 < 1 / parameter < support
    assert compact_linear_pole_killer_kernel(0, support, anchor) == 1
    assert compact_linear_pole_killer_kernel(support, support, anchor) == 0
    assert abs(
        compact_linear_pole_killer_laplace(anchor, support, anchor)
    ) < mp.mpf("1e-65")

    right_derivative = parameter - 1 / support
    omega = mp.mpf("-0.4")
    errors = []
    for epsilon in (mp.mpf("0.04"), mp.mpf("0.02"), mp.mpf("0.01")):
        s = anchor + omega / epsilon
        transform = compact_linear_pole_killer_laplace(s, support, anchor)
        far_edge = -right_derivative * mp.e ** (-s * support) / s**2
        errors.append(abs(transform / far_edge - 1))
    assert errors[2] < errors[1] < errors[0]


def test_fractional_two_edge_multi_anchor_chebyshev_kernel() -> None:
    mp.mp.dps = 70
    support = mp.mpf("1.8")
    anchors = ((mp.mpf("0.8"), 1), (mp.mpf("1.7"), 2))
    alpha_left = mp.mpf("0.4")
    alpha_right = mp.mpf("1.2")
    rate = mp.mpf("0.3")
    coefficients = compact_chebyshev_polynomial_coefficients(
        support, anchors, alpha_left, alpha_right, rate
    )
    assert len(coefficients) == 4
    assert coefficients[-1] == 1

    for anchor, multiplicity in anchors:
        for derivative_order in range(multiplicity):
            moment = mp.quad(
                lambda z: (-z) ** derivative_order
                * mp.e ** (-anchor * z)
                * compact_chebyshev_pole_killer_kernel(
                    z,
                    support,
                    anchors,
                    alpha_left,
                    alpha_right,
                    rate,
                    coefficients,
                    False,
                ),
                [0, support],
            )
            assert abs(moment) < mp.mpf("1e-60")

    roots = mp.polyroots(tuple(reversed(coefficients)), maxsteps=300)
    assert len(roots) == 3
    assert all(abs(mp.im(root)) < mp.mpf("1e-55") for root in roots)
    assert all(0 < mp.re(root) < 1 for root in roots)

    tiny = mp.mpf("1e-18")
    endpoint_ratio = compact_chebyshev_pole_killer_kernel(
        tiny,
        support,
        anchors,
        alpha_left,
        alpha_right,
        rate,
        coefficients,
        False,
    ) / tiny**alpha_left
    assert abs(endpoint_ratio - 1 / mp.gamma(alpha_left + 1)) < mp.mpf("1e-15")
    assert max(
        compact_chebyshev_notch_residuals(
            support,
            anchors,
            coefficients,
            alpha_left,
            alpha_right,
            rate,
        )
    ) < mp.mpf("1e-60")

    for anchor, multiplicity in anchors:
        next_derivative = mp.quad(
            lambda z: (-z) ** multiplicity
            * mp.e ** (-anchor * z)
            * compact_chebyshev_pole_killer_kernel(
                z,
                support,
                anchors,
                alpha_left,
                alpha_right,
                rate,
                coefficients,
                False,
            ),
            [0, support],
        )
        assert abs(next_derivative) > mp.mpf("1e-8")

    polynomial_at_one = mp.fsum(coefficients)
    kappa_right = (
        support ** (alpha_left - alpha_right)
        * mp.e ** (-rate * support)
        * polynomial_at_one
        / (mp.gamma(alpha_left + 1) * coefficients[0])
    )
    edge_errors = []
    for magnitude in (mp.mpf(20), mp.mpf(40), mp.mpf(80)):
        s = -magnitude
        scaled_transform = mp.quad(
            lambda z: mp.e ** (s * (support - z))
            * compact_chebyshev_pole_killer_kernel(
                z,
                support,
                anchors,
                alpha_left,
                alpha_right,
                rate,
                coefficients,
                False,
            ),
            [0, support],
        )
        leading_edge = (
            kappa_right * mp.gamma(alpha_right + 1) / (-s) ** (alpha_right + 1)
        )
        edge_errors.append(abs(scaled_transform / leading_edge - 1))
    assert edge_errors[2] < edge_errors[1] < edge_errors[0]


def test_compact_chebyshev_scaling_and_linear_regressions() -> None:
    mp.mp.dps = 60
    support = mp.mpf("1.3")
    anchor = mp.mpf("1.1")
    coefficients = compact_chebyshev_polynomial_coefficients(
        support, ((anchor, 1),), 0, 1, 0
    )
    for z in (mp.mpf(0), mp.mpf("0.2"), mp.mpf("0.9")):
        general = compact_chebyshev_pole_killer_kernel(
            z, support, ((anchor, 1),), 0, 1, 0, coefficients, False
        )
        assert abs(
            general - compact_linear_pole_killer_kernel(z, support, anchor)
        ) < mp.mpf("1e-50")

    anchors = ((mp.mpf("0.7"), 1), (mp.mpf("1.6"), 2))
    shift = mp.mpf("0.45")
    shifted_rate = compact_chebyshev_polynomial_coefficients(
        support, anchors, mp.mpf("0.3"), mp.mpf("0.8"), shift
    )
    shifted_anchors = compact_chebyshev_polynomial_coefficients(
        support,
        tuple((value + shift, order) for value, order in anchors),
        mp.mpf("0.3"),
        mp.mpf("0.8"),
        0,
    )
    assert all(
        abs(left - right) < mp.mpf("1e-50")
        for left, right in zip(shifted_rate, shifted_anchors, strict=True)
    )


def test_compact_chebyshev_validation_and_scale_conditioning() -> None:
    with pytest.raises(ValueError, match="finite"):
        compact_chebyshev_polynomial_coefficients(mp.nan, ((1, 1),))
    with pytest.raises(ValueError, match="finite"):
        compact_chebyshev_polynomial_coefficients(1, ((mp.inf, 1),))
    with pytest.raises(ValueError, match="distinct"):
        compact_chebyshev_polynomial_coefficients(1, ((1, 1), (1, 2)))
    with pytest.raises(ValueError, match="positive integers"):
        compact_chebyshev_polynomial_coefficients(
            1, ((1, 0.5),)  # type: ignore[arg-type]
        )
    with pytest.raises(ValueError, match="nonzero constant"):
        compact_chebyshev_pole_killer_kernel(
            2, 1, ((1, 1),), coefficients=(0, 1)
        )
    with pytest.raises(ValueError, match="fail the notch"):
        compact_chebyshev_pole_killer_kernel(
            mp.mpf("0.5"), 1, ((1, 1),), coefficients=(1, 1)
        )
    with pytest.raises(ValueError, match="must be nonzero"):
        compact_chebyshev_notch_residuals(1, ((1, 1),), (0, 0))

    assert compact_chebyshev_polynomial_coefficients(1, ()) == (mp.mpf(1),)
    assert compact_chebyshev_pole_killer_kernel(
        1, 1, (), coefficients=(1,)
    ) == 0

    tiny_support = mp.mpf("1e-12")
    anchors = ((mp.mpf(1), 1), (mp.mpf(2), 1), (mp.mpf(3), 1))
    coefficients = compact_chebyshev_polynomial_coefficients(
        tiny_support, anchors, mp.mpf("0.4"), mp.mpf("0.7"), mp.mpf("0.2")
    )
    roots = mp.polyroots(tuple(reversed(coefficients)), maxsteps=300)
    assert all(abs(mp.im(root)) < mp.mpf("1e-12") for root in roots)
    assert all(0 < mp.re(root) < 1 for root in roots)


def test_general_anchor_defaults_use_anchored_coefficients() -> None:
    mp.mp.dps = 50
    anchor = mp.mpf("1.5")
    rates = (mp.mpf(0), mp.mpf(1), mp.mpf(3))
    exact_coefficients = minimal_anchored_exponential_coefficients(
        (Fraction(0), Fraction(1), Fraction(3)), Fraction(3, 2)
    )
    coefficients = tuple(
        mp.mpf(value.numerator) / value.denominator
        for value in exact_coefficients
    )
    z = mp.mpf("0.7")
    assert mp.almosteq(
        exponential_kernel(z, rates, anchor=anchor),
        exponential_kernel(z, rates, coefficients),
    )
    assert mp.almosteq(
        sigma_minus_derivative_kernel(z, 3, rates, anchor=anchor),
        sigma_minus_derivative_kernel(z, 3, rates, coefficients, anchor),
    )
    moments = (mp.mpf("0.2"), mp.mpf("-0.05"))
    assert mp.almosteq(
        moment_boundary_expansion(
            mp.mpf("0.01"),
            z,
            mp.mpf("0.4"),
            moments,
            rates,
            anchor=anchor,
        ),
        moment_boundary_expansion(
            mp.mpf("0.01"),
            z,
            mp.mpf("0.4"),
            moments,
            rates,
            coefficients,
            anchor,
        ),
    )


def test_inverse_bridge_leading_tail_formula() -> None:
    delta = Fraction(2, 11)
    anchor = Fraction(3, 2)
    rates = (Fraction(0), Fraction(1), Fraction(4), Fraction(7))
    order = len(rates) - 1
    expected = delta ** (order - 1) * math.prod(
        (anchor + rate for rate in rates), start=Fraction(1)
    ) / (anchor**2 * math.factorial(order - 1))
    assert inverse_bridge_leading_tail(delta, rates, anchor) == expected


def test_fixed_singularity_response_is_order_independent_in_the_limit() -> None:
    offset = Fraction(-2, 5)
    anchor = Fraction(3, 2)
    for order in range(1, 5):
        rates = tuple(Fraction(index) for index in range(order + 1))
        errors = []
        for denominator in (10**2, 10**3, 10**4):
            value = exact_fixed_singularity_multiplier(
                offset, Fraction(1, denominator), rates, anchor
            )
            errors.append(abs(value - 1 / offset))
        assert errors[2] < errors[1] < errors[0]


def test_fixed_singularity_formula_matches_the_scaled_multiplier() -> None:
    offset = Fraction(-3, 7)
    delta = Fraction(2, 101)
    anchor = Fraction(4, 3)
    for order in range(1, 6):
        rates = tuple(Fraction(index) for index in range(order + 1))
        assert exact_fixed_singularity_multiplier(
            offset, delta, rates, anchor
        ) == exact_anchored_scaled_multiplier(
            offset + anchor * delta, delta, rates, anchor
        )


def test_endpoint_flat_fixed_singularity_relative_degree_law() -> None:
    offset = Fraction(-3, 7)
    anchor = Fraction(4, 3)
    notch_order = 2
    rates = (
        Fraction(0),
        Fraction(1),
        Fraction(2),
        Fraction(4),
        Fraction(7),
    )
    flat_order = len(rates) - notch_order - 1
    errors = []
    for denominator in (10**2, 10**3, 10**4):
        delta = Fraction(1, denominator)
        value = exact_endpoint_flat_fixed_singularity_multiplier(
            offset, delta, rates, notch_order, anchor
        )
        errors.append(abs(value / delta**flat_order - 1 / offset ** (flat_order + 1)))
    assert errors[2] < errors[1] < errors[0]


def test_growing_order_amplifies_a_fixed_left_singularity() -> None:
    offset = Fraction(-1)
    anchor = Fraction(1)
    for order in range(1, 21):
        rates = tuple(Fraction(index) for index in range(order + 1))
        delta = Fraction(1, 100 * order)
        assert all(
            0 < (anchor + rate) * delta < -2 * offset
            for rate in rates
        )
        multiplier = exact_fixed_singularity_multiplier(
            offset, delta, rates, anchor
        )
        assert abs(multiplier) > abs(1 / offset)


def test_finite_mode_germ_surrogate_matches_boundary_jet_calculus() -> None:
    mp.mp.dps = 60
    h = tuple(
        mp.mpf(value) for value in ("-0.7", "0.2", "-0.04", "0.003")
    )
    delta = mp.mpf("0.017")
    c = mp.mpf("0.8")
    anchor = mp.mpf("1.3")
    rates = (mp.mpf("0.1"), mp.mpf("0.9"), mp.mpf("2.2"))
    exact_coefficients = minimal_anchored_exponential_coefficients(
        (Fraction(1, 10), Fraction(9, 10), Fraction(11, 5)),
        Fraction(13, 10),
    )
    coefficients = tuple(
        mp.mpf(value.numerator) / value.denominator
        for value in exact_coefficients
    )

    def germ(w: mp.mpf) -> mp.mpf:
        return mp.fsum(
            coefficient * w**power
            for power, coefficient in enumerate(h)
        )

    moments = tuple(
        (-1) ** moment_order
        * mp.factorial(moment_order)
        * h[moment_order + 1]
        for moment_order in range(len(h) - 1)
    )
    direct_jet = moment_boundary_expansion(
        delta,
        c,
        -h[0],
        moments,
        rates,
        coefficients,
        anchor,
    )
    surrogate = exponential_germ_surrogate(
        delta, c, germ, rates, coefficients, anchor
    )
    assert abs(direct_jet - surrogate) < mp.mpf("1e-55")


def test_confluent_germ_surrogate_has_semigroup_form() -> None:
    mp.mp.dps = 50
    delta = mp.mpf("0.03")
    c = mp.mpf("1.1")
    anchor = mp.mpf("1.4")
    rate = mp.mpf("0.6")
    order = 4

    def exp_derivative(_: int, w: mp.mpf) -> mp.mpf:
        return mp.e**w

    surrogate = confluent_germ_surrogate(
        delta, c, order, rate, exp_derivative, anchor
    )
    expected = mp.e ** (-delta * anchor) * confluent_laguerre_kernel(
        c + delta, order, rate, anchor
    )
    assert abs(surrogate - expected) < mp.mpf("1e-45")


def test_multiple_front_splitting_polynomial() -> None:
    constant = Fraction(7, 5)
    k0 = Fraction(2, 9)
    k1 = Fraction(-3, 11)
    assert multiple_front_splitting_polynomial(constant, (k0,)) == (
        -k0,
        constant,
    )
    assert multiple_front_splitting_polynomial(constant, (k0, k1)) == (
        2 * k1,
        -2 * k0,
        constant,
    )
