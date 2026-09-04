"""Exact arithmetic replay for the dyadic outer-fan audit."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import exp, gcd


@dataclass(frozen=True)
class DyadicOuterFanLedger:
    degree: Fraction
    low_frequency: Fraction
    top_frequency: Fraction
    fan_size: Fraction
    alias_threshold: Fraction
    top_alias_multiplicity: Fraction
    full_lattice_dual_branches: Fraction


def dyadic_outer_fan_ledger() -> DyadicOuterFanLedger:
    """Return the active q-exponents at D=q^(16/33)."""

    degree = Fraction(16, 33)
    fan = degree / 2
    top = 1 - degree
    return DyadicOuterFanLedger(
        degree=degree,
        low_frequency=1 - 2 * degree,
        top_frequency=top,
        fan_size=fan,
        alias_threshold=fan,
        top_alias_multiplicity=top - fan,
        full_lattice_dual_branches=top,
    )


@dataclass(frozen=True)
class ActualReferenceAliasFixture:
    q: int
    fan_size: int
    frequency: int
    row_step: int
    color_step: int
    bezout: tuple[int, int]
    reference: tuple[int, int]
    determinant: int
    alias_increment: Fraction


def actual_reference_alias_fixture() -> ActualReferenceAliasFixture:
    """Return and internally verify the finite fixture in (4.2)--(4.4)."""

    q = 159_779
    fan_size = 16
    frequency = 312
    color_step = frequency * fan_size
    row_step = color_step + 1
    bezout = (1, 1)
    reference = (
        fan_size * row_step + bezout[0],
        fan_size * color_step + bezout[1],
    )

    if gcd(row_step, color_step) != 1:
        raise AssertionError("the direction is not primitive")
    if row_step * bezout[1] - color_step * bezout[0] != 1:
        raise AssertionError("the displayed Bezout identity failed")
    determinant = row_step * reference[1] - color_step * reference[0]
    if determinant != 1:
        raise AssertionError("the reference is not in quotient class one")
    lower = q * exp(-0.2) / 2
    upper = q * exp(0.2) / 2
    if not all(lower < value < upper for value in reference):
        raise AssertionError("the reference left the project shell")

    # d=frequency, A=fan_size, Delta=g=1, S=color_step.
    alias_increment = Fraction(-frequency * fan_size, color_step)
    return ActualReferenceAliasFixture(
        q=q,
        fan_size=fan_size,
        frequency=frequency,
        row_step=row_step,
        color_step=color_step,
        bezout=bezout,
        reference=reference,
        determinant=determinant,
        alias_increment=alias_increment,
    )

