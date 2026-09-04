"""Exact exponent ledger for Blomer--Pascadi versus the QP HSM interfaces."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class ShellModulusLedger:
    length: Fraction
    first_relative_exponent: Fraction
    second_relative_exponent: Fraction
    third_relative_exponent: Fraction
    dominant_saving: Fraction
    required_saving: Fraction
    conditional_margin: Fraction


def shell_modulus_ledger() -> ShellModulusLedger:
    """BP Theorem 1.1 with modulus ``q`` and length ``D=q^(16/33)``."""

    length = Fraction(16, 33)
    first = Fraction(13, 32) - Fraction(7, 8) * length
    second = Fraction(5, 16) - Fraction(11, 16) * length
    third = Fraction(1, 9) - Fraction(1, 3) * length
    # These are negative exponents; the least negative term dominates.
    dominant = -max(first, second, third)
    required = Fraction(1, 66)
    return ShellModulusLedger(
        length=length,
        first_relative_exponent=first,
        second_relative_exponent=second,
        third_relative_exponent=third,
        dominant_saving=dominant,
        required_saving=required,
        conditional_margin=dominant - required,
    )


@dataclass(frozen=True)
class TopDFILedger:
    modulus_in_q: Fraction
    fan_in_modulus: Fraction
    product_difference_in_modulus: Fraction
    fan_below_lower_threshold: Fraction
    critical_saving_in_modulus: Fraction
    product_block_count_in_modulus: Fraction
    one_long_axis_cauchy_cost_in_modulus: Fraction
    one_long_axis_net_loss_in_modulus: Fraction
    unequal_theorem_bad_term_in_modulus: Fraction


def top_dfi_ledger() -> TopDFILedger:
    """The exact top-DFI scales ``c=C``, fan ``V``, and ``Delta``.

    ``C=q^(25/33)``, ``V=q^(8/33)=C^(8/25)``, and
    ``|Delta|<=V^2=q^(16/33)=C^(16/25)``.
    """

    fan = Fraction(8, 25)
    product = Fraction(16, 25)
    block_count = product - Fraction(1, 2)
    cauchy_cost = block_count / 2
    critical_saving = Fraction(1, 32)
    return TopDFILedger(
        modulus_in_q=Fraction(25, 33),
        fan_in_modulus=fan,
        product_difference_in_modulus=product,
        fan_below_lower_threshold=Fraction(13, 28) - fan,
        critical_saving_in_modulus=critical_saving,
        product_block_count_in_modulus=block_count,
        one_long_axis_cauchy_cost_in_modulus=cauchy_cost,
        one_long_axis_net_loss_in_modulus=cauchy_cost - critical_saving,
        # Theorem 5.5 contains N^(1/3)/C^(1/5).
        unequal_theorem_bad_term_in_modulus=product / 3 - Fraction(1, 5),
    )

