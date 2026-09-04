#!/usr/bin/env python3
"""R188 exact guards for the proposed R71 principal-band serialization.

This module deliberately proves only finite or elementary algebraic facts.
It does not estimate the completed R71 energy.

The useful exact scale family is

    X = M**100,              B = X**(-99/100) = M**(-99).

It avoids floating-point powers.  A nonzero rational ``a/q`` can lie in the
core principal band only when ``q >= M**99`` (and in the transition support
``|a/q| <= 2 B`` only when ``q >= ceil(M**99/2)``).  Nevertheless the core
contains coprime denominator pairs of size ``X`` with determinant of size
``X``.  Thus principal-band localization is not a low-determinant
localization, and it does not remove the ``j*theta ~ X**2`` top box audited
in R105.

Two other bookkeeping facts are replayed here.

* A common-g primitive mask forbids at most two line residues modulo every
  prime dividing g.  Its normalized Fourier-algebra norm is at most
  ``3**omega(g) = g**o(1)``.  Hence that particular mask is not a polynomial
  projective-cost obstruction.
* An affine center has two independent zero-character channels.  A scalar
  cofactor zero mode can match it on an interval only when the logarithmic
  coefficient vanishes.  The complete square therefore has to retain every
  packet--packet, packet--reducible, packet--center, reducible--center, and
  center--center cross term.

The asymptotic arithmetic obstruction recorded by the mathematical audit is
not proved by this script: the actual top-semiprime ``a=1`` channel has
coherent energy ``X/log(X)**2 = X**(1-o(1))`` by the prime number theorem.
That lower bound rules out estimating the literal channel separately at the
``X**0.98`` target, but it is not a lower bound for the completed energy,
because the omitted channels may cancel it.
"""

from __future__ import annotations

import argparse
import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Mapping


TOTAL_POWER = 100
CORE_DENOMINATOR_POWER = 99


def _positive_integer(value: int, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def in_principal_core(numerator: int, denominator: int, base: int) -> bool:
    """Return ``|a/q| <= M^-99`` using integer arithmetic only."""

    _positive_integer(denominator, "denominator")
    _positive_integer(base, "base")
    return abs(numerator) * base**CORE_DENOMINATOR_POWER <= denominator


def in_principal_support(numerator: int, denominator: int, base: int) -> bool:
    """Return ``|a/q| <= 2 M^-99`` using integer arithmetic only."""

    _positive_integer(denominator, "denominator")
    _positive_integer(base, "base")
    return abs(numerator) * base**CORE_DENOMINATOR_POWER <= 2 * denominator


@dataclass(frozen=True)
class PrincipalBandGeometry:
    """Exact denominator, numerator, and free-quotient scale ledger."""

    base: int
    shell_multiplier: int
    scale: int
    core_minimum_nonzero_denominator: int
    support_minimum_nonzero_denominator: int
    maximum_core_numerator: int
    maximum_support_numerator: int
    maximum_core_physical_quotient: int
    maximum_support_physical_quotient: int


def principal_band_geometry(
    base: int, *, shell_multiplier: int = 2
) -> PrincipalBandGeometry:
    """Return exact guards on a shell ``n <= shell_multiplier * X``.

    The quotient guards apply when the cofactor denominator divides the
    active integer ``n``.  Ceiling/floor choices are retained exactly.
    """

    _positive_integer(base, "base")
    _positive_integer(shell_multiplier, "shell_multiplier")
    scale = base**TOTAL_POWER
    core_minimum = base**CORE_DENOMINATOR_POWER
    support_minimum = (core_minimum + 1) // 2
    maximum_denominator = shell_multiplier * scale
    return PrincipalBandGeometry(
        base=base,
        shell_multiplier=shell_multiplier,
        scale=scale,
        core_minimum_nonzero_denominator=core_minimum,
        support_minimum_nonzero_denominator=support_minimum,
        maximum_core_numerator=maximum_denominator // core_minimum,
        maximum_support_numerator=(2 * maximum_denominator) // core_minimum,
        maximum_core_physical_quotient=maximum_denominator // core_minimum,
        maximum_support_physical_quotient=(
            maximum_denominator // support_minimum
        ),
    )


@dataclass(frozen=True)
class DeterminantWitness:
    """One exact rational-pair witness inside the principal core."""

    first_denominator: int
    second_denominator: int
    first_numerator: int
    second_numerator: int
    common_divisor: int
    first_reduced_denominator: int
    second_reduced_denominator: int
    determinant: int
    both_modes_in_core: bool


def determinant_witness(
    first_denominator: int,
    second_denominator: int,
    first_numerator: int,
    second_numerator: int,
    base: int,
) -> DeterminantWitness:
    """Compute ``theta = a*n-b*m`` after removing the common denominator."""

    _positive_integer(first_denominator, "first_denominator")
    _positive_integer(second_denominator, "second_denominator")
    _positive_integer(base, "base")
    common = math.gcd(first_denominator, second_denominator)
    first_reduced = first_denominator // common
    second_reduced = second_denominator // common
    determinant = (
        first_numerator * second_reduced
        - second_numerator * first_reduced
    )
    return DeterminantWitness(
        first_denominator=first_denominator,
        second_denominator=second_denominator,
        first_numerator=first_numerator,
        second_numerator=second_numerator,
        common_divisor=common,
        first_reduced_denominator=first_reduced,
        second_reduced_denominator=second_reduced,
        determinant=determinant,
        both_modes_in_core=(
            in_principal_core(first_numerator, first_denominator, base)
            and in_principal_core(second_numerator, second_denominator, base)
        ),
    )


@dataclass(frozen=True)
class PrincipalDeterminantExamples:
    """Low, high, and reducible sectors all retained by the same band."""

    low: DeterminantWitness
    high: DeterminantWitness
    reducible: DeterminantWitness


def principal_determinant_examples(base: int) -> PrincipalDeterminantExamples:
    """Construct exact witnesses showing that the band does not select a sector."""

    _positive_integer(base, "base")
    scale = base**TOTAL_POWER
    return PrincipalDeterminantExamples(
        low=determinant_witness(scale, scale + 1, 1, 1, base),
        high=determinant_witness(scale, 2 * scale - 1, 1, 1, base),
        reducible=determinant_witness(scale, 2 * scale, 1, 1, base),
    )


def distinct_prime_factors(value: int) -> tuple[int, ...]:
    """Return the distinct prime factors of a positive integer."""

    _positive_integer(value, "value")
    answer: list[int] = []
    remainder = value
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            answer.append(divisor)
            while remainder % divisor == 0:
                remainder //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        answer.append(remainder)
    return tuple(answer)


@dataclass(frozen=True)
class PrimitiveMaskFourierAudit:
    """Finite Fourier-algebra audit for a common-g line mask."""

    radical: int
    prime_count: int
    fourier_l1: float
    local_product_bound: int
    bound_error: float


def primitive_mask_fourier_audit(
    modulus: int,
    forbidden_residues: Mapping[int, Iterable[int]],
) -> PrimitiveMaskFourierAudit:
    """Compute the normalized DFT l1 norm of a CRT primitive-line mask.

    For every prime ``p | modulus``, ``forbidden_residues[p]`` may contain at
    most two residue classes.  This is the exact local form of the conditions
    that two affine line coordinates both remain units modulo the common
    factor.  Empty local masks and coincident forbidden residues are allowed.
    """

    primes = distinct_prime_factors(modulus)
    normalized: dict[int, frozenset[int]] = {}
    for prime in primes:
        residues = frozenset(
            int(residue) % prime for residue in forbidden_residues.get(prime, ())
        )
        if len(residues) > 2:
            raise ValueError("each prime may have at most two forbidden residues")
        normalized[prime] = residues
    unknown = set(forbidden_residues) - set(primes)
    if unknown:
        raise ValueError("forbidden-residue keys must divide the modulus")

    radical = math.prod(primes)
    values = [
        float(
            all(index % prime not in normalized[prime] for prime in primes)
        )
        for index in range(radical)
    ]
    coefficients: list[complex] = []
    for frequency in range(radical):
        coefficient = sum(
            value
            * cmath.exp(-2.0j * math.pi * frequency * index / radical)
            for index, value in enumerate(values)
        ) / radical
        coefficients.append(coefficient)
    fourier_l1 = sum(abs(coefficient) for coefficient in coefficients)
    bound = 3 ** len(primes)
    return PrimitiveMaskFourierAudit(
        radical=radical,
        prime_count=len(primes),
        fourier_l1=fourier_l1,
        local_product_bound=bound,
        bound_error=max(0.0, fourier_l1 - bound),
    )


@dataclass(frozen=True)
class AffineZeroModeAudit:
    """Exact obstruction to replacing an affine center by one scalar axis."""

    alpha: Fraction
    beta: Fraction
    normalization: Fraction
    zeroth_moment: Fraction
    first_sample: Fraction
    second_sample: Fraction
    matching_scalar_at_first_sample: Fraction
    normalized_residual_at_second_sample: Fraction
    scalar_axis_matches_both_samples: bool


def affine_zero_mode_audit(
    alpha: Fraction | int,
    beta: Fraction | int,
    normalization: Fraction | int,
    zeroth_moment: Fraction | int,
    first_sample: Fraction | int,
    second_sample: Fraction | int,
) -> AffineZeroModeAudit:
    """Match a scalar zero mode at one sample and expose the second mismatch.

    After dividing by ``exp(r/2)``, a scalar cofactor zero mode is ``S*J0``
    while the center is ``(alpha+beta*r)/N``.  The returned residual is exact.
    """

    alpha_q = Fraction(alpha)
    beta_q = Fraction(beta)
    normalization_q = Fraction(normalization)
    zeroth_q = Fraction(zeroth_moment)
    first_q = Fraction(first_sample)
    second_q = Fraction(second_sample)
    if normalization_q == 0 or zeroth_q == 0:
        raise ValueError("normalization and zeroth moment must be nonzero")
    matching_scalar = (
        alpha_q + beta_q * first_q
    ) / (normalization_q * zeroth_q)
    residual = (
        alpha_q + beta_q * second_q
    ) / normalization_q - matching_scalar * zeroth_q
    return AffineZeroModeAudit(
        alpha=alpha_q,
        beta=beta_q,
        normalization=normalization_q,
        zeroth_moment=zeroth_q,
        first_sample=first_q,
        second_sample=second_q,
        matching_scalar_at_first_sample=matching_scalar,
        normalized_residual_at_second_sample=residual,
        scalar_axis_matches_both_samples=(residual == 0),
    )


@dataclass(frozen=True)
class CompletedChannelLedger:
    """Exact real scalar expansion of packets + reducible - affine center."""

    packet_diagonal: Fraction
    packet_cross: Fraction
    packet_reducible: Fraction
    packet_center_constant: Fraction
    packet_center_logarithmic: Fraction
    reducible_square: Fraction
    reducible_center_constant: Fraction
    reducible_center_logarithmic: Fraction
    center_constant_square: Fraction
    center_internal_cross: Fraction
    center_logarithmic_square: Fraction
    expanded_total: Fraction
    completed_amplitude: Fraction
    completed_square: Fraction
    closure_error: Fraction

    @property
    def absolute_sector_sum(self) -> Fraction:
        return sum(
            (
                abs(self.packet_diagonal),
                abs(self.packet_cross),
                abs(self.packet_reducible),
                abs(self.packet_center_constant),
                abs(self.packet_center_logarithmic),
                abs(self.reducible_square),
                abs(self.reducible_center_constant),
                abs(self.reducible_center_logarithmic),
                abs(self.center_constant_square),
                abs(self.center_internal_cross),
                abs(self.center_logarithmic_square),
            ),
            Fraction(0),
        )


def completed_channel_ledger(
    packets: Iterable[Fraction | int],
    reducible: Fraction | int,
    center_constant: Fraction | int,
    center_logarithmic: Fraction | int,
) -> CompletedChannelLedger:
    """Expand the complete square without suppressing any cross term."""

    packet_values = tuple(Fraction(value) for value in packets)
    reducible_q = Fraction(reducible)
    center_constant_q = Fraction(center_constant)
    center_logarithmic_q = Fraction(center_logarithmic)
    packet_sum = sum(packet_values, Fraction(0))
    packet_diagonal = sum((value * value for value in packet_values), Fraction(0))
    packet_cross = 2 * sum(
        (
            packet_values[left] * packet_values[right]
            for left in range(len(packet_values))
            for right in range(left + 1, len(packet_values))
        ),
        Fraction(0),
    )
    terms = dict(
        packet_diagonal=packet_diagonal,
        packet_cross=packet_cross,
        packet_reducible=2 * packet_sum * reducible_q,
        packet_center_constant=-2 * packet_sum * center_constant_q,
        packet_center_logarithmic=-2 * packet_sum * center_logarithmic_q,
        reducible_square=reducible_q**2,
        reducible_center_constant=-2 * reducible_q * center_constant_q,
        reducible_center_logarithmic=-2 * reducible_q * center_logarithmic_q,
        center_constant_square=center_constant_q**2,
        center_internal_cross=2 * center_constant_q * center_logarithmic_q,
        center_logarithmic_square=center_logarithmic_q**2,
    )
    expanded_total = sum(terms.values(), Fraction(0))
    completed_amplitude = (
        packet_sum + reducible_q - center_constant_q - center_logarithmic_q
    )
    completed_square = completed_amplitude**2
    return CompletedChannelLedger(
        **terms,
        expanded_total=expanded_total,
        completed_amplitude=completed_amplitude,
        completed_square=completed_square,
        closure_error=expanded_total - completed_square,
    )


@dataclass(frozen=True)
class TopBoxExponentPassport:
    """Exact exponent comparison inherited from the R105 top box."""

    eta: Fraction
    target_energy_exponent: Fraction
    direct_energy_exponent: Fraction
    scalar_wright_exponent: Fraction
    wright_excess_over_direct: Fraction
    principal_high_k_witness_survives: bool


@dataclass(frozen=True)
class TargetMatchedCollarPassport:
    """Exact exponent ledger for the fifth-order Fourier collar."""

    eta: Fraction
    fourier_decay_order: int
    target_field_exponent: Fraction
    cofactor_exponent: Fraction
    physical_quotient_exponent: Fraction
    numerator_exponent: Fraction
    low_cofactor_error_exponent: Fraction
    large_numerator_error_exponent: Fraction


def target_matched_collar_passport() -> TargetMatchedCollarPassport:
    """Return the exact ``.998/.002/.0025`` target-matched ledger.

    The order-four project window has fifth-order Fourier decay.  Cofactors
    through ``X**(499/500)`` and numerators beyond ``X**(1/400)`` therefore
    each cost at most the target field exponent ``49/100``.  This is exponent
    bookkeeping only; it proves no analytic energy bound.
    """

    eta = Fraction(1, 100)
    decay = 5
    field_target = Fraction(1, 2) - eta
    cofactor = 1 - eta / decay
    numerator = eta / (decay - 1)
    return TargetMatchedCollarPassport(
        eta=eta,
        fourier_decay_order=decay,
        target_field_exponent=field_target,
        cofactor_exponent=cofactor,
        physical_quotient_exponent=1 - cofactor,
        numerator_exponent=numerator,
        low_cofactor_error_exponent=(
            Fraction(1, 2) + decay * (cofactor - 1)
        ),
        large_numerator_error_exponent=(
            Fraction(1, 2) - (decay - 1) * numerator
        ),
    )


def top_box_exponent_passport() -> TopBoxExponentPassport:
    """Record the frozen .98 target and R105's X^(15/8) high-k output."""

    eta = Fraction(1, 100)
    direct = Fraction(1)
    wright = Fraction(15, 8)
    examples = principal_determinant_examples(2)
    return TopBoxExponentPassport(
        eta=eta,
        target_energy_exponent=1 - 2 * eta,
        direct_energy_exponent=direct,
        scalar_wright_exponent=wright,
        wright_excess_over_direct=wright - direct,
        principal_high_k_witness_survives=(
            examples.high.both_modes_in_core
            and examples.high.determinant
            == examples.high.first_denominator - 1
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=int, default=2)
    args = parser.parse_args()

    geometry = principal_band_geometry(args.base)
    examples = principal_determinant_examples(args.base)
    mask = primitive_mask_fourier_audit(
        2 * 3 * 5 * 7,
        {2: (0,), 3: (0, 1), 5: (1, 3), 7: (2,)},
    )
    affine = affine_zero_mode_audit(3, 2, 5, 7, 0, 1)
    packet_count = 16
    ledger = completed_channel_ledger(
        [Fraction(1, packet_count)] * packet_count,
        1,
        Fraction(3, 2),
        Fraction(1, 2) - Fraction(1, packet_count),
    )
    passport = top_box_exponent_passport()
    collar = target_matched_collar_passport()

    print(
        "principal geometry: "
        f"X=M^100={geometry.scale} core-q>={geometry.core_minimum_nonzero_denominator} "
        f"support-q>={geometry.support_minimum_nonzero_denominator} "
        f"core |a|<={geometry.maximum_core_numerator} "
        f"free quotient<={geometry.maximum_core_physical_quotient}"
    )
    print(
        "determinants in the same core: "
        f"low={examples.low.determinant} high={examples.high.determinant} "
        f"reducible=(m,n)=({examples.reducible.first_reduced_denominator},"
        f"{examples.reducible.second_reduced_denominator})"
    )
    print(
        "common-g mask: "
        f"rad={mask.radical} Fourier-l1={mask.fourier_l1:.12g} "
        f"bound={mask.local_product_bound}"
    )
    print(
        "affine scalar-axis mismatch: "
        f"residual={affine.normalized_residual_at_second_sample}"
    )
    print(
        "completed coherent fixture: "
        f"square={ledger.completed_square} "
        f"absolute-sector-sum={ledger.absolute_sector_sum} "
        f"closure={ledger.closure_error}"
    )
    print(
        "exponents: "
        f"target={float(passport.target_energy_exponent):.2f} "
        f"direct={float(passport.direct_energy_exponent):.3f} "
        f"scalar-Wright={float(passport.scalar_wright_exponent):.3f}"
    )
    print(
        "target-matched collar: "
        f"q>X^{collar.cofactor_exponent} "
        f"quotient<=X^{collar.physical_quotient_exponent} "
        f"|a|<=X^{collar.numerator_exponent} "
        f"field-error=X^{collar.target_field_exponent}"
    )
    print("rating: exact algebra plus imported R105 exponent ledger; no strip bound")


if __name__ == "__main__":
    main()
