"""Exact bulk saturator for the difference-of-products autocorrelation.

The construction uses two separated subintervals in each fan.  Its
autocorrelation energy lies at macroscopic nonzero product differences, so
it survives deletion of the coherent axes, ``Delta=0``, and any cutoff
``|Delta| <= 3*L^2/2``.  A finite prime-modulus Parseval identity shows that
the normalized Kloosterman square function preserves this energy, up to
the single omitted constant Fourier mode.
"""

from __future__ import annotations

import cmath
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, pi
from typing import Mapping


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def separated_support(length: int) -> tuple[int, ...]:
    """Return two length-``L/4`` intervals inside ``[L,2L]``."""

    L = int(length)
    if L < 4 or L % 4:
        raise ValueError("length must be a positive multiple of four")
    quarter = L // 4
    low = tuple(range(L, L + quarter))
    high = tuple(range(2 * L - quarter + 1, 2 * L + 1))
    return low + high


def product_convolution(
    first: Mapping[int, complex], second: Mapping[int, complex]
) -> dict[int, complex]:
    """Return ``g(t)=sum_(u*v=t) first[u] second[v]``."""

    answer: dict[int, complex] = defaultdict(complex)
    for u, first_value in first.items():
        for v, second_value in second.items():
            answer[int(u) * int(v)] += first_value * second_value
    return dict(answer)


def additive_autocorrelation(values: Mapping[int, complex]) -> dict[int, complex]:
    """Return ``B_Delta=sum_t g(t+Delta) conjugate(g(t))``."""

    answer: dict[int, complex] = defaultdict(complex)
    items = tuple((int(index), value) for index, value in values.items())
    for first_index, first_value in items:
        for second_index, second_value in items:
            answer[first_index - second_index] += (
                first_value * second_value.conjugate()
            )
    return dict(answer)


def normalized_separated_autocorrelation(length: int) -> dict[int, complex]:
    """Return the autocorrelation for unit ``l2`` separated fan inputs."""

    support = separated_support(length)
    coefficient = len(support) ** -0.5
    inputs = {index: coefficient for index in support}
    return additive_autocorrelation(product_convolution(inputs, inputs))


@dataclass(frozen=True)
class BulkAutocorrelationLedger:
    length: int
    fan_norm_squared: Fraction
    tensor_input_norm_squared: Fraction
    lower_band_left: Fraction
    lower_band_right: int
    designated_quadruples: int
    difference_slots_upper_bound: int
    raw_bulk_energy_lower_bound: Fraction
    normalized_bulk_energy_lower_bound: Fraction
    normalized_total_mass: Fraction


def bulk_autocorrelation_ledger(length: int) -> BulkAutocorrelationLedger:
    """Return the exact Cauchy lower bound for the separated packet.

    High--high products minus low--low products lie in

    ``(3*L^2/2, 3*L^2]``.

    There are ``(L/4)^4`` designated ordered quadruples in this band and at
    most ``2*L^2`` possible integer differences.  After normalizing each
    fan vector to unit ``l2`` norm, Cauchy gives bulk squared energy at
    least ``L^2/8192``.
    """

    L = int(length)
    support = separated_support(L)
    quarter = L // 4
    support_size = len(support)
    designated = quarter**4
    difference_slots = 2 * L * L
    raw_lower = Fraction(designated**2, difference_slots)
    # Each B coefficient is scaled by support_size^(-2), hence its square by
    # support_size^(-4).
    normalized_lower = raw_lower / support_size**4
    return BulkAutocorrelationLedger(
        length=L,
        fan_norm_squared=Fraction(1),
        tensor_input_norm_squared=Fraction(1),
        lower_band_left=Fraction(3 * L * L, 2),
        lower_band_right=3 * L * L,
        designated_quadruples=designated,
        difference_slots_upper_bound=difference_slots,
        raw_bulk_energy_lower_bound=raw_lower,
        normalized_bulk_energy_lower_bound=normalized_lower,
        # sum_Delta B_Delta=|sum_t g(t)|^2=(support_size)^2 after
        # unit-l2 normalization of the two identical inputs.
        normalized_total_mass=Fraction(support_size**2),
    )


@dataclass(frozen=True)
class AlignedPhysicalBulkLedger:
    """Bulk packet pulled back through ``nu=-2r, mu=-s``."""

    length: int
    row_support_size: int
    color_support_size: int
    designated_quadruples: int
    normalized_bulk_energy_lower_bound: Fraction
    normalized_total_mass: Fraction
    raw_determinant_lower_bound: Fraction
    raw_determinant_upper_bound: Fraction


def aligned_physical_bulk_ledger(length: int) -> AlignedPhysicalBulkLedger:
    """Return the exact broad packet for the aligned CRT fixture.

    In the exact choice

    ``S=R+1, c=R+2, U=R-1, V=R``

    the transformed frequencies are ``nu=-2r`` and ``mu=-s``.  Restrict
    the row-frequency support of :func:`separated_support` to even values
    and keep the full colour support.  Pullback is then integral and

    ``Delta=2*(r*s-r'*s')``.

    The packet remains on ``3*L^2/2<Delta<=3*L^2``, hence its raw fan
    determinant is between ``3*L^2/4`` and ``3*L^2/2`` and is never
    tangent.
    """

    L = int(length)
    if L < 8 or L % 8:
        raise ValueError("length must be a positive multiple of eight")
    quarter = L // 4
    row_per_block = quarter // 2
    color_per_block = quarter
    row_support_size = 2 * row_per_block
    color_support_size = 2 * color_per_block
    designated = (row_per_block * color_per_block) ** 2
    raw_energy = Fraction(designated**2, 2 * L * L)
    # Each B term has two row and two colour coefficients.  With unit-l2
    # inputs, its amplitude scale is
    # (row_support_size*color_support_size)^(-1), and the energy scale is
    # its square.
    normalized_energy = raw_energy / (
        row_support_size * color_support_size
    ) ** 2
    return AlignedPhysicalBulkLedger(
        length=L,
        row_support_size=row_support_size,
        color_support_size=color_support_size,
        designated_quadruples=designated,
        normalized_bulk_energy_lower_bound=normalized_energy,
        normalized_total_mass=Fraction(
            row_support_size * color_support_size
        ),
        raw_determinant_lower_bound=Fraction(3 * L * L, 4),
        raw_determinant_upper_bound=Fraction(3 * L * L, 2),
    )


def _additive_character(value: int, modulus: int) -> complex:
    return cmath.exp(2j * pi * (int(value) % int(modulus)) / int(modulus))


def kloosterman_square_function(
    coefficients: Mapping[int, complex], modulus: int, multiplier: int = 1
) -> tuple[float, float]:
    """Return both sides of the exact prime-modulus square-function identity.

    Define

    ``K(h)=c^(-1) sum_Delta B_Delta S(-h,-lambda*Delta;c)``.

    If the difference support is injective modulo the prime ``c``, then

    ``sum_h |K(h)|^2
      =sum_Delta |B_Delta|^2-c^(-1)|sum_Delta B_Delta|^2``.

    The first returned value is the directly evaluated left side and the
    second is the closed-form right side.
    """

    c = int(modulus)
    lam = int(multiplier) % c
    if not _is_prime(c) or not lam:
        raise ValueError("modulus must be prime and multiplier a unit")
    residues = [int(delta) % c for delta in coefficients]
    if len(set(residues)) != len(residues):
        raise ValueError("difference support must be injective modulo c")

    numerator_transform: dict[int, complex] = {}
    for numerator in range(1, c):
        inverse = pow(numerator, -1, c)
        numerator_transform[numerator] = sum(
            value * _additive_character(-inverse * lam * delta, c)
            for delta, value in coefficients.items()
        )
    left = 0.0
    for shift in range(c):
        transformed = sum(
            value * _additive_character(-numerator * shift, c)
            for numerator, value in numerator_transform.items()
        ) / c
        left += abs(transformed) ** 2
    total_l2 = sum(abs(value) ** 2 for value in coefficients.values())
    total_mass = sum(coefficients.values())
    right = total_l2 - abs(total_mass) ** 2 / c
    return left, right


def primitive_square_function_lower_bound(
    length: int, modulus: int
) -> Fraction:
    """Return a rigorous symbolic lower bound for the separated packet.

    It combines the bulk-band estimate with the one omitted constant mode:

    ``L^2/8192-L^4/(16*c)``.
    """

    ledger = bulk_autocorrelation_ledger(length)
    c = int(modulus)
    if not _is_prime(c) or c <= 6 * length * length:
        raise ValueError("prime modulus must separate every signed difference")
    correction = ledger.normalized_total_mass**2 / c
    return ledger.normalized_bulk_energy_lower_bound - correction
