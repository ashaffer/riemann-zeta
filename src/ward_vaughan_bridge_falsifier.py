#!/usr/bin/env python3
"""Exact finite gate for a Ward--Markov lift of the Vaughan tail.

The decisive fiber is a distinct semiprime ``n = p*q`` with both primes
above the frozen Vaughan cutoffs.  Write ``x = log(p)`` and ``y = log(q)``.
The two tail assignments have weights ``-y`` and ``-x`` and, after grouping
by total product, the coefficient is ``-(x+y)``.

This module keeps the quadratic coefficients formal.  It also applies a
finite Markov average to an arbitrary common scale profile.  The calculation
distinguishes three operations which must not be conflated:

* scale averaging acts identically on the two assignments and therefore
  sees the coherent square ``(x+y)^2``;
* the natural factor-assignment swap has innovation ``(x-y)^2/4``;
* the proposed Ward-connected term is ``2*(Lambda*Lambda)(pq)=4*x*y``.

An additional exact one-tail/one-center Gram model varies the admissible
tail--center correlation while leaving every scalar Ward coefficient fixed.
It makes both the global remainder and its Ward-renormalized version change
sign, proving that positive covariance plus the coefficient identity cannot
orient the nonlocal term.

Thus the natural assignment cross supplies only one copy of
``(Lambda*Lambda)(pq)=2*x*y``.  At fixed scale, a smooth center has degree at
most one in this individual fiber and cannot supply the missing quadratic
copy locally.  This does *not* exclude a global redistribution involving the
support relation, other total products, and the center.  Keeping the exact
Type-I head instead cancels the entire tail coefficient before the energy is
formed.  These are exact finite algebra statements, not numerical evidence
about zeta zeros.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Quadratic:
    """Coefficients of ``x^2, x*y, y^2``."""

    x2: Fraction
    xy: Fraction
    y2: Fraction

    def __add__(self, other: "Quadratic") -> "Quadratic":
        return Quadratic(
            self.x2 + other.x2,
            self.xy + other.xy,
            self.y2 + other.y2,
        )

    def __sub__(self, other: "Quadratic") -> "Quadratic":
        return Quadratic(
            self.x2 - other.x2,
            self.xy - other.xy,
            self.y2 - other.y2,
        )

    def scale(self, scalar: Fraction | int) -> "Quadratic":
        scalar = Fraction(scalar)
        return Quadratic(
            scalar * self.x2,
            scalar * self.xy,
            scalar * self.y2,
        )


ZERO = Quadratic(Fraction(0), Fraction(0), Fraction(0))


@dataclass(frozen=True)
class SemiprimePolynomialAudit:
    tail_square: Quadratic
    assignment_self: Quadratic
    assignment_cross: Quadratic
    lambda_convolution: Quadratic
    ward_connected: Quadratic
    anisotropy: Quadratic
    swap_innovation: Quadratic
    swap_retained: Quadratic
    fixed_fiber_center_quadratic: Quadratic
    exact_head_square: Quadratic
    head_tail_cross: Quadratic
    exact_full_square: Quadratic


def semiprime_polynomial_audit() -> SemiprimePolynomialAudit:
    """Return the exact formal audit on the central ``p*q`` fiber.

    The exact Type-I head coefficient is ``x+y`` and the grouped tail
    coefficient is ``-(x+y)``.  A cutoff-dependent smooth center can create
    a term linear in ``x+y`` through its cross term at fixed ``R``, but it has
    no quadratic coefficient on that one fixed fiber; this is recorded as
    ``ZERO``.  Summing over fibers while tying ``R`` to their support is a
    different, genuinely global calculation and is not ruled out here.
    """

    tail_square = Quadratic(Fraction(1), Fraction(2), Fraction(1))
    assignment_self = Quadratic(Fraction(1), Fraction(0), Fraction(1))
    assignment_cross = Quadratic(Fraction(0), Fraction(2), Fraction(0))
    lambda_convolution = assignment_cross
    ward_connected = lambda_convolution.scale(2)
    anisotropy = Quadratic(Fraction(1), Fraction(-2), Fraction(1))
    swap_innovation = anisotropy.scale(Fraction(1, 4))
    swap_retained = tail_square.scale(Fraction(1, 4))
    exact_head_square = tail_square
    head_tail_cross = tail_square.scale(-2)
    exact_full_square = tail_square + exact_head_square + head_tail_cross
    return SemiprimePolynomialAudit(
        tail_square,
        assignment_self,
        assignment_cross,
        lambda_convolution,
        ward_connected,
        anisotropy,
        swap_innovation,
        swap_retained,
        ZERO,
        exact_head_square,
        head_tail_cross,
        exact_full_square,
    )


@dataclass(frozen=True)
class BinaryMacroAudit:
    """Exact one-step scale average on the profile ``(0,1)``."""

    raw_kernel: Fraction
    innovation_kernel: Fraction
    retained_kernel: Fraction
    raw_diagonal: Quadratic
    subtracted_innovation: Quadratic
    retained_diagonal: Quadratic
    retained_connected: Quadratic


def binary_macro_audit() -> BinaryMacroAudit:
    """Give the smallest exact terminal-macro countercheck.

    For the two-point Markov average and the common profile ``(0,1)``, the
    raw, innovation, and retained scalar kernels are ``1/2, 1/4, 1/4``.
    Hence subtracting the complete innovation leaves one quarter of
    ``(x+y)^2``.  In particular it leaves a nonzero connected ``x*y`` term;
    it does not leave the anisotropy alone.
    """

    polynomial = semiprime_polynomial_audit()
    raw_kernel = Fraction(1, 2)
    innovation_kernel = Fraction(1, 4)
    retained_kernel = Fraction(1, 4)
    raw = polynomial.tail_square.scale(raw_kernel)
    innovation = polynomial.tail_square.scale(innovation_kernel)
    retained = raw - innovation
    retained_connected = polynomial.ward_connected.scale(retained_kernel)
    return BinaryMacroAudit(
        raw_kernel,
        innovation_kernel,
        retained_kernel,
        raw,
        innovation,
        retained,
        retained_connected,
    )


@dataclass(frozen=True)
class GlobalCovarianceSignAudit:
    """Exact one-tail/one-center positive-semidefinite Gram model."""

    factor_log_x: Fraction
    factor_log_y: Fraction
    correlation: Fraction
    gram_determinant: Fraction
    tail_diagonal: Fraction
    ward_connected: Fraction
    global_remainder: Fraction
    ward_renormalized_remainder: Fraction
    completed_energy: Fraction


def global_covariance_sign_audit(
    factor_log_x: Fraction | int = 1,
    factor_log_y: Fraction | int = 2,
    correlation: Fraction | int = 1,
) -> GlobalCovarianceSignAudit:
    """Return the exact abstract sign gate for equation (7.1).

    Normalize ``K(phi,phi)=K(psi,psi)=1`` and
    ``K(phi,psi)=correlation``.  Put
    ``T=(x+y)phi`` and ``Z=(x+y)psi``.  The Gram matrix is positive
    semidefinite exactly when ``abs(correlation)<=1``.  Selberg's scalar
    Ward identities fix the tail diagonal and connected counterterm but do
    not fix this correlation.
    """

    x_value = Fraction(factor_log_x)
    y_value = Fraction(factor_log_y)
    rho = Fraction(correlation)
    if x_value <= 0 or y_value <= 0:
        raise ValueError("formal factor logarithms must be positive")
    if abs(rho) > 1:
        raise ValueError("correlation must define a PSD Gram matrix")

    diagonal = (x_value + y_value) ** 2
    connected = 4 * x_value * y_value
    remainder = diagonal * (1 - 2 * rho)
    return GlobalCovarianceSignAudit(
        x_value,
        y_value,
        rho,
        1 - rho**2,
        diagonal,
        connected,
        remainder,
        remainder + connected,
        diagonal + remainder,
    )


@dataclass(frozen=True)
class PrimePowerAudit:
    exponent: int
    tail_square_coefficient: int
    lambda_log_coefficient: int
    lambda_convolution_coefficient: int
    ward_sum_coefficient: int
    mobius_log_square_coefficient: int
    residual_after_twice_connected: int


def prime_power_audit(exponent: int) -> PrimePowerAudit:
    """Audit the Ward companion on ``p^exponent`` above both cutoffs.

    All entries are coefficients of ``log(p)^2``.  The tail coefficient is
    ``-(exponent-1)log(p)``.  In particular, extracting
    ``2*(Lambda*Lambda)`` from its square leaves a negative residual at
    ``p^2``; the semiprime anisotropy decomposition is not a global positive
    identity.
    """

    if exponent < 2:
        raise ValueError("exponent must be at least two")
    tail_square = (exponent - 1) ** 2
    lambda_log = exponent
    lambda_convolution = exponent - 1
    ward_sum = lambda_log + lambda_convolution
    mobius_log_square = 2 * exponent - 1
    residual = tail_square - 2 * lambda_convolution
    return PrimePowerAudit(
        exponent,
        tail_square,
        lambda_log,
        lambda_convolution,
        ward_sum,
        mobius_log_square,
        residual,
    )


@dataclass(frozen=True)
class HigherWardCutoffAudit:
    """Cutoff-complete squarefree coefficient and its higher Ward term.

    ``tail_log_multiplicities[i]`` is the exact integer multiplying
    ``log(primes[i])`` in ``(mu_(>Y) * Lambda_(>Y) * 1)(n)``.  The
    remaining fields evaluate the logarithms in floating point.
    """

    primes: tuple[int, ...]
    cutoff: int
    tail_log_multiplicities: tuple[int, ...]
    ward_product_multiplier: int
    tail_coefficient: float
    ward_coefficient: float
    amgm_connected: float
    remainder: float


def squarefree_tail_log_multiplicities(
    primes: tuple[int, ...], cutoff: int
) -> tuple[int, ...]:
    """Return the exact log multiplicities of the grouped Vaughan tail.

    For ``n=product(primes)`` the coefficient is

    ``sum_i log(p_i) 1_(p_i>Y) sum_(d|n/p_i,d>Y) mu(d)``.

    Subsets of the remaining distinct primes enumerate the squarefree
    divisors ``d`` and make the inner Mobius sum an exact integer.
    """

    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    if len(primes) < 2 or len(set(primes)) != len(primes):
        raise ValueError("provide at least two distinct prime factors")
    if any(prime < 2 for prime in primes):
        raise ValueError("prime factors must be at least two")

    answer: list[int] = []
    for index, prime in enumerate(primes):
        if prime <= cutoff:
            answer.append(0)
            continue
        remaining = primes[:index] + primes[index + 1 :]
        multiplicity = 0
        for mask in range(1, 1 << len(remaining)):
            divisor = 1
            cardinality = 0
            for bit, factor in enumerate(remaining):
                if mask & (1 << bit):
                    divisor *= factor
                    cardinality += 1
            if divisor > cutoff:
                multiplicity += -1 if cardinality % 2 else 1
        answer.append(multiplicity)
    return tuple(answer)


def higher_ward_cutoff_audit(
    primes: tuple[int, ...], cutoff: int
) -> HigherWardCutoffAudit:
    """Compare the actual grouped tail square with the order-``r`` Ward term.

    At a squarefree product of ``r`` primes,
    ``(mu * log^r)(n)=r!*product(log(p))``.  Its degree-two AM--GM
    normalization is ``r^r*product(log(p))/(log(n)^(r-2))``.
    """

    multiplicities = squarefree_tail_log_multiplicities(primes, cutoff)
    logs = tuple(math.log(prime) for prime in primes)
    order = len(primes)
    tail = math.fsum(
        multiplicity * value
        for multiplicity, value in zip(multiplicities, logs)
    )
    log_product = math.prod(logs)
    ward_multiplier = math.factorial(order)
    ward = ward_multiplier * log_product
    connected = order**order * log_product / math.fsum(logs) ** (order - 2)
    return HigherWardCutoffAudit(
        primes,
        cutoff,
        multiplicities,
        ward_multiplier,
        tail,
        ward,
        connected,
        tail * tail - connected,
    )


def _markov_average(values: list[float], width: int) -> list[float]:
    if width < 1 or width > len(values):
        raise ValueError("invalid averaging width")
    return [
        math.fsum(values[index : index + width]) / width
        for index in range(len(values) - width + 1)
    ]


def _markov_power(values: list[float], width: int, order: int) -> list[float]:
    answer = values
    for _ in range(order):
        answer = _markov_average(answer, width)
    return answer


def _macro_innovation(
    values: list[float], width: int, order: int
) -> list[float]:
    averaged_square = _markov_power(
        [value * value for value in values], width, order
    )
    averaged = _markov_power(values, width, order)
    return [
        left - right * right
        for left, right in zip(averaged_square, averaged)
    ]


@dataclass(frozen=True)
class ScaleFiberAudit:
    prime: int
    other_prime: int
    minimum_kernel: float
    grouped_rank_one_error: float
    natural_cross_error: float
    missing_connected_copy: float
    exact_head_completion_error: float


def scale_fiber_audit(
    prime: int = 5,
    other_prime: int = 7,
    profile: list[float] | None = None,
    width: int = 3,
    order: int = 2,
) -> ScaleFiberAudit:
    """Apply a terminal macro innovation to the two ``p*q`` assignments.

    Both assignments have the same profile because their total product is
    the same.  Consequently their covariance is rank one.  The natural
    cross term is exactly one ``Lambda*Lambda`` copy, not the two copies in
    the proposed connected subtraction.
    """

    if prime < 2 or other_prime < 2 or prime == other_prime:
        raise ValueError("provide two distinct integers greater than one")
    if order < 1:
        raise ValueError("order must be positive")
    if profile is None:
        profile = [0.0, 0.15, 0.65, 1.0, 0.8, 0.25, 0.0, 0.4, 0.9]
    if len(profile) <= order * (width - 1):
        raise ValueError("profile is too short for the requested average")

    x = math.log(prime)
    y = math.log(other_prime)
    kernel = _macro_innovation(profile, width, order)
    first = _macro_innovation([-y * value for value in profile], width, order)
    second = _macro_innovation([-x * value for value in profile], width, order)
    grouped = _macro_innovation(
        [-(x + y) * value for value in profile], width, order
    )
    completed = _macro_innovation(
        [(-(x + y) + (x + y)) * value for value in profile], width, order
    )

    rank_one_error = max(
        abs(value - (x + y) ** 2 * base)
        for value, base in zip(grouped, kernel)
    )
    natural_cross = [
        total - left - right
        for total, left, right in zip(grouped, first, second)
    ]
    natural_cross_error = max(
        abs(value - 2.0 * x * y * base)
        for value, base in zip(natural_cross, kernel)
    )
    # The desired connected coefficient is 4*x*y.  The positive maximum is
    # the one-copy deficit after the naturally generated assignment cross.
    missing_connected_copy = max(
        4.0 * x * y * base - value
        for value, base in zip(natural_cross, kernel)
    )
    return ScaleFiberAudit(
        prime,
        other_prime,
        min(kernel),
        rank_one_error,
        natural_cross_error,
        missing_connected_copy,
        max(abs(value) for value in completed),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=5)
    parser.add_argument("--other-prime", type=int, default=7)
    args = parser.parse_args()

    polynomial = semiprime_polynomial_audit()
    print("central p*q formal coefficients (x^2, xy, y^2)")
    print(f"  tail square:          {polynomial.tail_square}")
    print(f"  assignment cross:     {polynomial.assignment_cross}")
    print(f"  Ward connected:       {polynomial.ward_connected}")
    print(f"  swap innovation:      {polynomial.swap_innovation}")
    print(f"  exact full square:     {polynomial.exact_full_square}")
    binary = binary_macro_audit()
    print("exact binary terminal macro")
    print(f"  raw diagonal:          {binary.raw_diagonal}")
    print(f"  subtracted innovation: {binary.subtracted_innovation}")
    print(f"  retained diagonal:     {binary.retained_diagonal}")
    print(f"  retained connected:    {binary.retained_connected}")
    scale = scale_fiber_audit(args.prime, args.other_prime)
    print("terminal scale innovation")
    print(f"  rank-one error:        {scale.grouped_rank_one_error:.3g}")
    print(f"  natural-cross error:   {scale.natural_cross_error:.3g}")
    print(f"  missing Ward copy:     {scale.missing_connected_copy:.9g}")
    print(f"  exact-head completion: {scale.exact_head_completion_error:.3g}")
    square = prime_power_audit(2)
    print("p^2 companion")
    print(f"  Ward closure:          {square.ward_sum_coefficient}")
    print(f"  residual after 2LL:    {square.residual_after_twice_connected}")
    print("higher-Ward cutoff counterexamples")
    for factors in ((2, 11, 13), (2, 3, 11, 13), (2, 7, 11), (2, 7, 1009)):
        higher = higher_ward_cutoff_audit(factors, 10)
        print(
            f"  n factors={factors}: multiplicities="
            f"{higher.tail_log_multiplicities}, remainder="
            f"{higher.remainder:.9g}"
        )


if __name__ == "__main__":
    main()
