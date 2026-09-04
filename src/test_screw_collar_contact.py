from fractions import Fraction

import pytest

from screw_collar_contact import (
    hostile_block_determinant,
    hostile_collar_energy,
    hostile_cross,
    hostile_cross_expanded,
    hostile_cross_from_integrand,
    shell_collar_charge_squared,
    shell_potential,
)


@pytest.mark.parametrize(
    "delta", [Fraction(1, 4), Fraction(1, 8), Fraction(3, 20), Fraction(1, 64)]
)
def test_c1_hostile_cross_is_exactly_negative(delta: Fraction) -> None:
    assert hostile_cross(delta) == hostile_cross_expanded(delta)
    assert hostile_cross(delta) == hostile_cross_from_integrand(delta)
    assert hostile_cross(delta) < 0
    assert hostile_collar_energy(delta) > 0
    assert hostile_block_determinant(delta) == -(hostile_cross(delta) ** 2)
    assert hostile_block_determinant(delta) < 0


def test_c1_hostile_cross_vanishes_only_at_zero_on_replay_range() -> None:
    assert hostile_cross(Fraction(0)) == 0
    for numerator in range(1, 17):
        delta = Fraction(numerator, 64)
        assert 0 < delta <= Fraction(1, 4)
        assert hostile_cross(delta) < 0


@pytest.mark.parametrize("power", [1, 2, 3, 8, 20])
def test_shell_model_is_arbitrarily_flat_but_charged(power: int) -> None:
    width = Fraction(1, 8)
    assert shell_potential(power, Fraction(0)) == 0
    assert shell_potential(power, width) < 0
    assert shell_collar_charge_squared(power, width) > 0


def test_quadratic_shell_closed_form() -> None:
    s = Fraction(1, 5)
    assert shell_potential(2, s) == s**3 * (s - 4) / 12
    d = Fraction(1, 3)
    expected = Fraction(1, 72) * (
        d**9 / 9 - d**8 + Fraction(16, 7) * d**7
    )
    assert shell_collar_charge_squared(2, d) == expected


@pytest.mark.parametrize("bad", [-1, 2])
def test_shell_replay_rejects_out_of_range_widths(bad: int) -> None:
    with pytest.raises(ValueError):
        shell_potential(2, bad)
    with pytest.raises(ValueError):
        shell_collar_charge_squared(2, bad)
