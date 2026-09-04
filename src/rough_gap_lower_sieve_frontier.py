#!/usr/bin/env python3
"""Exact exponent ledger for a lower-sieve attack on rough gaps.

The arithmetic input is the general Type-II inequality proved in Kaisa
Matomaki, *Almost primes in almost all very short intervals*, Lemma 5.4
(``typeIIClaim`` in the arXiv TeX source).  This
module does not numerically test that theorem.  It checks, with exact rational
arithmetic, what the theorem gives after the following specialization:

* roughness cutoff ``z = X**b`` with ``b <= 799/5000``;
* medium linear-sieve level ``D = X**(1/3)``;
* small beta-sieve level ``E = X**(1/1000)``;
* a ``1:2`` well-factorization of the complete vector-sieve level.

The lower linear-sieve main term is positive because ``D > z**2``.  The
resulting empty-interval estimate, combined with the exact empty-start gap
identity, turns a Type-II convolution exponent ``L(h)`` into a gap-square
exponent ``max(1, 2*h, L(h))``.  Iwaniec's Jacobsthal theorem bounds every
rough gap by ``O(z**2)``.  At the hostile endpoint ``h=2*(799/5000)``, the
Type-II exponent is ``84457/90000<1`` and the gap-square exponent is therefore
exactly ``1+o(1)``.

This is an exponent/checking tool, not a replacement for the imported sieve
and prime-gap theorems.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


Rational = Fraction | int


def _q(value: Rational) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


@dataclass(frozen=True)
class LowerSieveParameters:
    """Power exponents in the lower-sieve specialization."""

    roughness_max: Fraction = Fraction(799, 5000)
    linear_level: Fraction = Fraction(1, 3)
    beta_level: Fraction = Fraction(1, 1000)

    @property
    def linear_sieve_ratio(self) -> Fraction:
        """``log D/log z`` at the hostile (largest) roughness cutoff."""

        return self.linear_level / self.roughness_max

    @property
    def main_term_power_margin(self) -> Fraction:
        """Power margin in ``D/z**2``.

        A positive value is exactly the dimension-one lower-sieve condition
        ``log D/log z > 2``.  The numerical value of the sieve function is
        not needed for the exponent ledger.
        """

        return self.linear_level - 2 * self.roughness_max

    @property
    def first_factor(self) -> Fraction:
        """Larger factor after adjoining the small beta-sieve weight.

        Put ``L=linear_level+beta_level``.  Factor the medium linear weight at
        levels ``L/3`` and ``linear_level-L/3`` and adjoin the beta weight to
        the latter.  The resulting total factors have exponents ``L/3`` and
        ``2L/3``.
        """

        return 2 * self.total_weight_level / 3

    @property
    def second_factor(self) -> Fraction:
        return self.total_weight_level / 3

    @property
    def total_weight_level(self) -> Fraction:
        return self.linear_level + self.beta_level

    @property
    def jacobsthal_gap_cutoff(self) -> Fraction:
        """Largest rough-gap power supplied by ``J(z) << z**2``."""

        return 2 * self.roughness_max

    @property
    def type_ii_poisson_range(self) -> Fraction:
        """Largest ``h`` for which the raw Type-II convolution is ``X^(1-o)``.

        With factor exponents ``2L/3,L/3,L``, both branches of the max-plus
        Type-II bound equal ``1/2+h/2+5L/6`` while
        ``h <= 1-5L/3``.  The latter endpoint is returned here.
        """

        return 1 - 5 * self.total_weight_level / 3

    def validate(self) -> None:
        if self.roughness_max <= 0:
            raise ValueError("roughness exponent must be positive")
        if self.main_term_power_margin <= 0:
            raise ValueError("the lower linear-sieve main term is not positive")
        if self.beta_level <= 0:
            raise ValueError("the small beta-sieve level must be positive")
        if self.jacobsthal_gap_cutoff >= self.type_ii_poisson_range:
            raise ValueError("Jacobsthal gaps leave the Type-II Poisson range")
        if self.jacobsthal_gap_cutoff >= Fraction(1, 2):
            raise ValueError("the H^3 endpoint error is no longer subdiagonal")


@dataclass(frozen=True)
class TypeIIExponentCertificate:
    """Max-plus expansion of Matomaki's general Type-II inequality."""

    interval: Fraction
    first_factor: Fraction
    second_factor: Fraction
    other_weight: Fraction
    shifted_product: Fraction
    shifted_or_second: Fraction
    q_or_second_square: Fraction
    inner_first: Fraction
    inner_second: Fraction
    convolution_first: Fraction
    convolution_second: Fraction
    convolution: Fraction


def type_ii_exponent(
    interval: Rational,
    first_factor: Rational,
    second_factor: Rational,
    other_weight: Rational,
) -> TypeIIExponentCertificate:
    """Evaluate the Type-II bound over power scales exactly.

    For ``H=X**h, M=X**m, N=X**n, Q=X**q``, Matomaki's bound is

    ``H^(1/2) X^(1/2+o(1)) [A+B]^(1/4)``

    with

    ``A=(MQ)^2`` and
    ``B=(HMNQ/X+N) * [MQ(HMNQ/X+N)(Q+N^2)
                       + H(MN)^3 Q/X]``.

    Sums become maxima of exponents.  The return value records every max-plus
    node so a verifier can audit the wiring rather than only the final number.
    """

    h = _q(interval)
    m = _q(first_factor)
    n = _q(second_factor)
    q = _q(other_weight)
    if min(h, m, n, q) < 0:
        raise ValueError("power exponents must be nonnegative")
    if n > m:
        raise ValueError("the Type-II convention requires N <= M")

    shifted_product = h + m + n + q - 1
    shifted_or_second = max(shifted_product, n)
    q_or_second_square = max(q, 2 * n)
    inner_first = m + q + shifted_or_second + q_or_second_square
    inner_second = h + 3 * (m + n) + q - 1
    outside = h / 2 + Fraction(1, 2)
    convolution_first = outside + (m + q) / 2
    convolution_second = outside + (
        shifted_or_second + max(inner_first, inner_second)
    ) / 4
    convolution = max(convolution_first, convolution_second)

    return TypeIIExponentCertificate(
        interval=h,
        first_factor=m,
        second_factor=n,
        other_weight=q,
        shifted_product=shifted_product,
        shifted_or_second=shifted_or_second,
        q_or_second_square=q_or_second_square,
        inner_first=inner_first,
        inner_second=inner_second,
        convolution_first=convolution_first,
        convolution_second=convolution_second,
        convolution=convolution,
    )


@dataclass(frozen=True)
class RoughGapMomentCertificate:
    """Exact endpoint certificate for the rough-gap second moment."""

    parameters: LowerSieveParameters
    type_ii: TypeIIExponentCertificate
    diagonal_gap_square: Fraction
    geometric_error_gap_square: Fraction
    type_ii_gap_square: Fraction
    final_gap_square: Fraction
    excess: Fraction


def rough_gap_moment_certificate(
    parameters: LowerSieveParameters = LowerSieveParameters(),
) -> RoughGapMomentCertificate:
    """Return the uniform dyadic rough-gap exponent certificate.

    The empty-interval Chebyshev argument converts the three variance terms

    * ``X H`` (diagonal),
    * ``H^3`` (sharp-endpoint geometric error), and
    * ``H X**L(h)`` (Type-II off diagonal)

    into gap-square exponents ``1``, ``2h`` and ``L(h)`` respectively.
    Every max-plus expression in ``L(h)`` is nondecreasing in ``h``, so the
    largest legal gap scale is the only endpoint that must be checked.
    """

    parameters.validate()
    h = parameters.jacobsthal_gap_cutoff
    cert = type_ii_exponent(
        h,
        parameters.first_factor,
        parameters.second_factor,
        parameters.total_weight_level,
    )
    diagonal = Fraction(1)
    geometric = 2 * h
    off_diagonal = cert.convolution
    final = max(diagonal, geometric, off_diagonal)
    return RoughGapMomentCertificate(
        parameters=parameters,
        type_ii=cert,
        diagonal_gap_square=diagonal,
        geometric_error_gap_square=geometric,
        type_ii_gap_square=off_diagonal,
        final_gap_square=final,
        excess=final - 1,
    )


def required_excess(
    denominator_exponent: Rational, target_saving: Rational
) -> Fraction:
    """Strict rough-gap excess frontier ``rho < b-2*kappa``."""

    return _q(denominator_exponent) - 2 * _q(target_saving)


def closes_required_frontier(
    parameters: LowerSieveParameters,
    denominator_exponent: Rational,
    target_saving: Rational,
) -> bool:
    return (
        rough_gap_moment_certificate(parameters).excess
        < required_excess(denominator_exponent, target_saving)
    )


def _format_fraction(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}={float(value):.12f}"


def main() -> None:
    parameters = LowerSieveParameters()
    result = rough_gap_moment_certificate(parameters)
    hostile_kappa = Fraction(19740482582942, 10**15)
    frontier = required_excess(parameters.roughness_max, hostile_kappa)
    print(f"linear_sieve_ratio={_format_fraction(parameters.linear_sieve_ratio)}")
    print(f"main_term_power_margin={_format_fraction(parameters.main_term_power_margin)}")
    print(f"type_ii_convolution={_format_fraction(result.type_ii.convolution)}")
    print(f"rough_gap_excess={_format_fraction(result.excess)}")
    print(f"required_excess_frontier={_format_fraction(frontier)}")
    print(f"margin={float(frontier-result.excess):.12f}")


if __name__ == "__main__":
    main()
