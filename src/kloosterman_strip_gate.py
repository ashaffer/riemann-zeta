#!/usr/bin/env python3
"""Conditional exponent gate from a bilinear Kloosterman saving.

This module proves no Kloosterman reduction, no mollified-moment estimate, and
no zero-free region. It records the exact exponent arithmetic that would apply
if the completed long-mollifier reciprocity remainder of nominal size ``Y^2``
were reduced to bilinear Kloosterman forms with a net saving ``Y**(-delta)``.

At the critical length ``N=sqrt(c)``, Blomer--Pascadi's Theorem 1.1 gives
``delta=1/32`` for the isolated bilinear form. Transferring that saving to the
completed reciprocity remainder is an open compatibility problem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class ConditionalKloostermanStripGate:
    """Exact strip ledger for an assumed net remainder saving."""

    saving: Fraction
    maximum_theta: Fraction
    natural_moment_exponent: Fraction
    right_zero_boundary: Fraction
    strip_width: Fraction


def _require_fraction_between_zero_and_one(value: Fraction, name: str) -> None:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a Fraction")
    if not 0 < value < 1:
        raise ValueError(f"{name} must lie strictly between zero and one")


def conditional_strip_gate(saving: Fraction) -> ConditionalKloostermanStripGate:
    r"""Convert a net ``Y**(-saving)`` remainder gain into a strip ledger.

    The absolute barrier ``Y^2`` becomes ``Y^(2-saving)``. Requiring this to
    be at most the long-mollifier target ``T*Y``, with ``Y=T^theta``, gives

        theta * (1-saving) <= 1.

    At equality ``theta=1/(1-saving)``. The averaged long-mollifier criterion
    would then give strip width ``saving/2``.
    """

    _require_fraction_between_zero_and_one(saving, "saving")
    maximum_theta = 1 / (1 - saving)
    return ConditionalKloostermanStripGate(
        saving=saving,
        maximum_theta=maximum_theta,
        natural_moment_exponent=maximum_theta + 1,
        right_zero_boundary=1 - saving / 2,
        strip_width=saving / 2,
    )


def remainder_exponent_in_t(theta: Fraction, saving: Fraction) -> Fraction:
    """Exponent of ``Y^(2-saving)`` after substituting ``Y=T^theta``."""

    if not isinstance(theta, Fraction):
        raise TypeError("theta must be a Fraction")
    if theta <= 0:
        raise ValueError("theta must be positive")
    _require_fraction_between_zero_and_one(saving, "saving")
    return theta * (2 - saving)


def target_exponent_in_t(theta: Fraction) -> Fraction:
    """Exponent of the natural long-mollifier target ``T*Y``."""

    if not isinstance(theta, Fraction):
        raise TypeError("theta must be a Fraction")
    if theta <= 0:
        raise ValueError("theta must be positive")
    return 1 + theta


def remainder_surplus(theta: Fraction, saving: Fraction) -> Fraction:
    """Remainder exponent minus target exponent; nonpositive is admissible."""

    return remainder_exponent_in_t(theta, saving) - target_exponent_in_t(theta)


def blomer_pascadi_term_exponents(length_exponent: Fraction) -> tuple[Fraction, ...]:
    r"""The three ``c`` exponents in Theorem 1.1 for ``N=c^nu``.

    Omitting the common sequence norms and ``c^o(1)``, they are

      1 + nu/8 - 3/32,
      1 + 5nu/16 - 3/16,
      1 + 2nu/3 - 7/18.
    """

    if not isinstance(length_exponent, Fraction):
        raise TypeError("length_exponent must be a Fraction")
    if not 0 <= length_exponent <= 1:
        raise ValueError("length_exponent must lie in [0,1]")
    nu = length_exponent
    return (
        1 + nu / 8 - Fraction(3, 32),
        1 + 5 * nu / 16 - Fraction(3, 16),
        1 + 2 * nu / 3 - Fraction(7, 18),
    )


def trivial_bilinear_exponent(length_exponent: Fraction) -> Fraction:
    r"""Exponent of ``min(c,N sqrt(c))`` for ``N=c^nu``."""

    if not isinstance(length_exponent, Fraction):
        raise TypeError("length_exponent must be a Fraction")
    if not 0 <= length_exponent <= 1:
        raise ValueError("length_exponent must lie in [0,1]")
    return min(Fraction(1), length_exponent + Fraction(1, 2))


def theorem_saving_at_length(length_exponent: Fraction) -> Fraction:
    """Power saving supplied by Theorem 1.1 relative to the trivial bound."""

    theorem_exponent = max(blomer_pascadi_term_exponents(length_exponent))
    saving = trivial_bilinear_exponent(length_exponent) - theorem_exponent
    return max(Fraction(0), saving)


def critical_blomer_pascadi_gate() -> ConditionalKloostermanStripGate:
    """Conditional strip gate from the critical ``c^(-1/32)`` saving."""

    saving = theorem_saving_at_length(Fraction(1, 2))
    if saving != Fraction(1, 32):
        raise AssertionError(f"unexpected critical saving: {saving}")
    return conditional_strip_gate(saving)
