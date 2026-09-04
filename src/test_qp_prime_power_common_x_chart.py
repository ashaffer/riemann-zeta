from fractions import Fraction

import pytest

from qp_prime_power_common_x_chart import (
    common_x_exponent_ledger,
    compatible_common_x,
    cross_gcd_divides_x,
    nonprincipal_singleton_exponent,
    principal_upper_pair,
)


def test_cross_gcd_forced_into_common_x() -> None:
    # r=(1,6), s=(1,10), eta=theta=1.  Compatibility forces X=2 mod 6
    # and X=6 mod 10; X=26 is one solution and gcd(6,10)=2 divides it.
    assert compatible_common_x(26, 1, 6, 1, 10, 1, 1)
    assert cross_gcd_divides_x(26, 1, 6, 1, 10, 1, 1)
    assert not compatible_common_x(17, 1, 6, 1, 10, 1, 1)


def test_nonprimitive_directions_are_rejected() -> None:
    with pytest.raises(ValueError):
        compatible_common_x(4, 2, 6, 1, 5, 1, 1)


def test_primitive_critical_face_is_far_below_one() -> None:
    ledger = common_x_exponent_ledger(
        e=Fraction(1, 2),
        t=Fraction(1, 2),
        r=Fraction(7, 16),
        s=Fraction(7, 16),
        mu=Fraction(15, 8),
        kappa=Fraction(5, 16),
    )
    assert ledger.chart_count == Fraction(44, 16)
    assert ledger.chart_length == Fraction(19, 16)
    assert ledger.color_mass == Fraction(3, 16)
    assert ledger.singleton_trace == Fraction(1, 2)


def test_principal_envelope_equality() -> None:
    mu = Fraction(41, 24)
    chart, principal = principal_upper_pair(mu)
    assert chart == principal == Fraction(23, 24)


def test_nonprincipal_envelope_equality() -> None:
    assert nonprincipal_singleton_exponent(Fraction(33, 32)) == Fraction(
        137, 128
    )
