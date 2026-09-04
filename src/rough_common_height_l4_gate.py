#!/usr/bin/env python3
"""Exact normalization ledger for the surviving common-height L4 target."""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction


KAPPA = Fraction(1_974_048_259, 100_000_000_000)
SHALLOW_H = Fraction(33, 133)
COMPANION_H_MIN = Fraction(1, 2)
LOW_DENOMINATOR_BETA = Fraction(1537, 10_000)
COUNTERMODEL_B = Fraction(39, 250)
GAP_CUTOFF_THETA = Fraction(797, 5000)
THIRD_MOMENT_EXPONENT = Fraction(84_549, 65_000)


def fourier(vector: list[complex], a: int) -> complex:
    q = len(vector)
    return sum(
        value * cmath.exp(2j * math.pi * a * residue / q)
        for residue, value in enumerate(vector)
    )


def cyclic_correlation(vector: list[complex]) -> list[complex]:
    q = len(vector)
    return [
        sum(vector[r] * vector[(r + shift) % q].conjugate() for r in range(q))
        for shift in range(q)
    ]


def ramanujan_sum(q: int, n: int) -> complex:
    return sum(
        cmath.exp(2j * math.pi * a * n / q)
        for a in range(q)
        if math.gcd(a, q) == 1
    )


def fourth_moment_ledger(vector: list[complex]) -> dict[str, float]:
    """Check full and primitive fourth moments for an actual-mass vector."""

    q = len(vector)
    if q < 2:
        raise ValueError("modulus must be at least two")
    correlation = cyclic_correlation(vector)
    full_direct = sum(abs(fourier(vector, a)) ** 4 for a in range(q))
    full_corr = q * sum(abs(value) ** 2 for value in correlation)
    primitive_direct = sum(
        abs(fourier(vector, a)) ** 4
        for a in range(q)
        if math.gcd(a, q) == 1
    )
    primitive_corr = sum(
        correlation[s]
        * correlation[t].conjugate()
        * ramanujan_sum(q, t - s)
        for s in range(q)
        for t in range(q)
    ).real
    return {
        "full_direct": full_direct,
        "full_correlation": full_corr,
        "primitive_direct": primitive_direct,
        "primitive_correlation": primitive_corr,
    }


def band_recombination_ratio(charges: list[complex]) -> float:
    """Ratio in |sum D_P|^4 <= L^3 sum |D_P|^4."""

    if not charges:
        return 0.0
    denominator = len(charges) ** 3 * sum(abs(value) ** 4 for value in charges)
    if denominator == 0:
        return 0.0
    ratio = abs(sum(charges)) ** 4 / denominator
    if ratio > 1 + 1e-12:
        raise AssertionError("band Holder inequality failed")
    return ratio


def weighted_block_holder_ratio(
    charges: list[complex], lengths: list[float]
) -> float:
    """Ratio in (sum |B_I|)^4 <= (sum H_I)^3 sum |B_I|^4/H_I^3."""

    if len(charges) != len(lengths):
        raise ValueError("charges and lengths must have the same size")
    if any(length <= 0 for length in lengths):
        raise ValueError("all block lengths must be positive")
    if not charges:
        return 0.0
    denominator = sum(lengths) ** 3 * sum(
        abs(charge) ** 4 / length**3
        for charge, length in zip(charges, lengths)
    )
    if denominator == 0:
        return 0.0
    ratio = sum(abs(charge) for charge in charges) ** 4 / denominator
    if ratio > 1 + 1e-12:
        raise AssertionError("weighted block Holder inequality failed")
    return ratio


@dataclass(frozen=True)
class Ledger:
    kappa: Fraction = KAPPA

    def l4_input_exponent(self, delta: Fraction = Fraction(0)) -> Fraction:
        return 1 - 4 * self.kappa - 4 * delta

    def holder_output_exponent(self, delta: Fraction = Fraction(0)) -> Fraction:
        return Fraction(3, 4) + self.l4_input_exponent(delta) / 4

    @staticmethod
    def injective_diagonal_floor(h: Fraction) -> Fraction:
        """q=H semiprime diagonal gives Y^(1-h-o(1))."""

        return 1 - h

    def injective_diagonal_margin(self, h: Fraction) -> Fraction:
        return self.l4_input_exponent() - self.injective_diagonal_floor(h)

    def abstract_common_height_saturation(self) -> Fraction:
        """Blocks with |B_I|~H_I Y^-kappa exactly saturate L4."""

        return 1 - 4 * self.kappa

    def as_dict(self) -> dict[str, str | bool]:
        return {
            "kappa": str(self.kappa),
            "l4_input_exponent": str(self.l4_input_exponent()),
            "holder_output_exponent": str(self.holder_output_exponent()),
            "shallow_diagonal_floor": str(self.injective_diagonal_floor(SHALLOW_H)),
            "shallow_diagonal_margin": str(self.injective_diagonal_margin(SHALLOW_H)),
            "companion_diagonal_margin": str(
                self.injective_diagonal_margin(COMPANION_H_MIN)
            ),
            "abstract_saturates_delta_zero": (
                self.abstract_common_height_saturation()
                == self.l4_input_exponent()
            ),
        }


@dataclass(frozen=True)
class IntegerCountermodelLedger:
    """Strict exponent checks for the exact-log odd-integer witness.

    The witness is an integral, prime-density-shaped node set selected by one
    height.  It is deliberately not asserted to be an SPF rough set.
    """

    kappa: Fraction = KAPPA
    beta: Fraction = LOW_DENOMINATOR_BETA
    b: Fraction = COUNTERMODEL_B
    theta: Fraction = GAP_CUTOFF_THETA

    @property
    def a(self) -> Fraction:
        return 1 - self.b

    @property
    def h(self) -> Fraction:
        return 1 - self.a / 2

    def gafni_tao_saving_at_b(self) -> Fraction:
        return Fraction(9, 13) * (self.b - Fraction(2, 15))

    def conditions(self) -> dict[str, bool]:
        return {
            "legal_scales": self.beta < self.b < self.theta < self.h,
            "low_q_phase_error": self.beta > self.kappa,
            "positive_global_gap_count": 1 - self.b - self.kappa > 0,
            "positive_per_block_gap_count": self.h - self.b - self.kappa > 0,
            "small_mesh_and_local_peano": 2 * self.b > self.kappa,
            "continuum_block_error": self.a / 2 > self.kappa,
            "gafni_tao_tail": self.kappa > self.gafni_tao_saving_at_b(),
            "gap_square": 1 + self.b - self.kappa < Fraction(123, 100),
            "third_gap_moment": (
                1 + 2 * self.b - self.kappa < THIRD_MOMENT_EXPONENT
            ),
        }

    def all_conditions_hold(self) -> bool:
        return all(self.conditions().values())

    def as_dict(self) -> dict[str, object]:
        return {
            "b": str(self.b),
            "a": str(self.a),
            "h": str(self.h),
            "global_gap_count_exponent": str(1 - self.b - self.kappa),
            "per_block_gap_count_exponent": str(self.h - self.b - self.kappa),
            "third_gap_moment_exponent": str(1 + 2 * self.b - self.kappa),
            "gafni_tao_saving_at_b": str(self.gafni_tao_saving_at_b()),
            "conditions": self.conditions(),
            "scope_is_actual_rough_set": False,
        }


def self_check() -> dict[str, object]:
    ledger = Ledger()
    countermodel = IntegerCountermodelLedger()
    assert ledger.holder_output_exponent() == 1 - ledger.kappa
    assert ledger.injective_diagonal_margin(SHALLOW_H) > 0
    assert ledger.injective_diagonal_margin(COMPANION_H_MIN) > 0
    vector = [2 + 1j, -1j, -3 + 2j, 1 - 4j, -2 + 2j, 3]
    moments = fourth_moment_ledger(vector)
    scale = max(1.0, moments["full_direct"])
    assert abs(moments["full_direct"] - moments["full_correlation"]) < 1e-10 * scale
    assert abs(
        moments["primitive_direct"] - moments["primitive_correlation"]
    ) < 1e-10 * scale
    assert band_recombination_ratio([1 + 2j, -3j, 4 - 1j, 2]) <= 1
    assert weighted_block_holder_ratio(
        [3 + 1j, -2j, 5 - 4j], [7.0, 11.0, 13.0]
    ) <= 1
    assert countermodel.all_conditions_hold()
    return {
        "ledger": ledger.as_dict(),
        "countermodel": countermodel.as_dict(),
        "moment_identities": True,
        "band_holder": True,
        "block_holder": True,
    }


if __name__ == "__main__":
    print(self_check())
