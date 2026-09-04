"""Finite certificates for the character--Mellin / Hecke-fold audit.

The accompanying report proves the general finite-group identities.  This
module keeps the parts that admit useful exact or finite regression tests:

* unitary character diagonalization of a moving fan congruence (on a prime
  unit stratum);
* the opposite-cusp nebentypus factor carried by the delta modulus;
* a two-spike counterexample to the proposed multiplicative Hecke fold;
* the exact ``D^3`` punctured additive-autocorrelation obstruction; and
* the balanced DFI and exponent ledgers; and
* the exact Hou--Pan long-Weyl/one-modulus mismatch ledger.

Nothing here asserts the missing vector-valued Motohashi estimate.
"""

from __future__ import annotations

import cmath
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt, pi, sqrt
from typing import Mapping


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def _prime_divisors(value: int) -> tuple[int, ...]:
    remaining = int(value)
    result: list[int] = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            result.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        result.append(remaining)
    return tuple(result)


@lru_cache(maxsize=None)
def prime_discrete_log_table(prime: int) -> tuple[int, tuple[int, ...]]:
    """Return a primitive root and its discrete-log table modulo ``prime``."""

    p = int(prime)
    if not _is_prime(p) or p == 2:
        raise ValueError("prime must be an odd prime")
    order = p - 1
    factors = _prime_divisors(order)
    generator = next(
        candidate
        for candidate in range(2, p)
        if all(pow(candidate, order // factor, p) != 1 for factor in factors)
    )
    logs = [-1] * p
    value = 1
    for exponent in range(order):
        logs[value] = exponent
        value = value * generator % p
    return generator, tuple(logs)


def prime_character(prime: int, character_index: int, value: int) -> complex:
    """Evaluate the indexed multiplicative character modulo an odd prime."""

    p = int(prime)
    residue = int(value) % p
    if residue == 0:
        return 0j
    _, logs = prime_discrete_log_table(p)
    exponent = (int(character_index) % (p - 1)) * logs[residue]
    return cmath.exp(2j * pi * exponent / (p - 1))


def unitary_prime_character_transform(
    coefficients: Mapping[int, complex], prime: int
) -> tuple[complex, ...]:
    r"""Return ``phi(p)^(-1/2) sum_r alpha(r) conjugate(chi(r))``."""

    p = int(prime)
    if not _is_prime(p) or p == 2:
        raise ValueError("prime must be an odd prime")
    normalization = sqrt(p - 1)
    return tuple(
        sum(
            coefficients.get(residue, 0j)
            * prime_character(p, character_index, residue).conjugate()
            for residue in range(1, p)
        )
        / normalization
        for character_index in range(p - 1)
    )


def direct_prime_fan_fiber(
    coefficients: Mapping[int, complex],
    prime: int,
    unit: int,
    modulus: int,
    frequency: int,
) -> complex:
    r"""Evaluate ``sum_r alpha(r) 1_(nu = U*r*c mod p)`` directly."""

    p = int(prime)
    U = int(unit) % p
    c = int(modulus) % p
    nu = int(frequency) % p
    if U == 0 or c == 0:
        raise ValueError("unit and modulus must be units modulo prime")
    if nu == 0:
        return 0j
    residue = nu * pow(U * c % p, -1, p) % p
    return complex(coefficients.get(residue, 0j))


def character_prime_fan_fiber(
    coefficients: Mapping[int, complex],
    prime: int,
    unit: int,
    modulus: int,
    frequency: int,
) -> complex:
    r"""Evaluate the same fan fiber by normalized character inversion.

    This is the finite prime-stratum version of

    ``phi(R)^(-1/2) sum_chi alpha_tilde(chi) chi(nu) overline(chi(U*c))``.
    """

    p = int(prime)
    U = int(unit) % p
    c = int(modulus) % p
    nu = int(frequency) % p
    if U == 0 or c == 0:
        raise ValueError("unit and modulus must be units modulo prime")
    if nu == 0:
        return 0j
    transformed = unitary_prime_character_transform(coefficients, p)
    return sum(
        transformed[index]
        * prime_character(p, index, nu)
        * prime_character(p, index, U * c).conjugate()
        for index in range(p - 1)
    ) / sqrt(p - 1)


def prime_character_parseval(
    coefficients: Mapping[int, complex], prime: int
) -> tuple[float, float]:
    """Return the physical and character squared norms."""

    p = int(prime)
    transformed = unitary_prime_character_transform(coefficients, p)
    physical = sum(abs(coefficients.get(residue, 0j)) ** 2 for residue in range(1, p))
    spectral = sum(abs(value) ** 2 for value in transformed)
    return physical, spectral


def opposite_cusp_nebentypus_factor(
    row_prime: int,
    row_character: int,
    color_prime: int,
    color_character: int,
    modulus: int,
) -> complex:
    r"""Return ``overline(chi_R(c))*chi_S(c)``."""

    return (
        prime_character(row_prime, row_character, modulus).conjugate()
        * prime_character(color_prime, color_character, modulus)
    )


def product_convolution(
    first: Mapping[int, complex], second: Mapping[int, complex]
) -> dict[int, complex]:
    """Return ``u(t)=sum_(m*n=t) first(m) second(n)``."""

    result: dict[int, complex] = defaultdict(complex)
    for first_index, first_value in first.items():
        for second_index, second_value in second.items():
            result[int(first_index) * int(second_index)] += first_value * second_value
    return {index: value for index, value in result.items() if value != 0}


def additive_autocorrelation(values: Mapping[int, complex]) -> dict[int, complex]:
    r"""Return ``B(Delta)=sum_t u(t+Delta) conjugate(u(t))``."""

    result: dict[int, complex] = defaultdict(complex)
    items = tuple((int(index), value) for index, value in values.items())
    for shifted_index, shifted_value in items:
        for base_index, base_value in items:
            result[shifted_index - base_index] += shifted_value * base_value.conjugate()
    return dict(result)


def formal_short_hecke_support(length: int) -> frozenset[int]:
    r"""Indices in ``lambda(m)lambda(n)``, for ``m,n<=length``.

    The unramified relation is
    ``lambda(m)lambda(n)=sum_(d|(m,n)) lambda(m*n/d^2)``.
    """

    Y = int(length)
    if Y <= 0:
        raise ValueError("length must be positive")
    support: set[int] = set()
    for first in range(1, Y + 1):
        for second in range(1, Y + 1):
            common = gcd(first, second)
            for divisor in range(1, common + 1):
                if common % divisor == 0:
                    support.add(first * second // (divisor * divisor))
    return frozenset(support)


@dataclass(frozen=True)
class HeckeFoldCounterexample:
    length: int
    forbidden_additive_index: int
    product_coefficients: tuple[tuple[int, complex], ...]
    autocorrelation_coefficient: complex
    occurs_in_short_hecke_support: bool


def two_spike_hecke_fold_counterexample(length: int) -> HeckeFoldCounterexample:
    r"""Return the exact fixture ``(delta_1+delta_Y)*(delta_1-delta_Y)``."""

    Y = int(length)
    if Y <= 2:
        raise ValueError("length must exceed two")
    first = {1: 1.0, Y: 1.0}
    second = {1: 1.0, Y: -1.0}
    product = product_convolution(first, second)
    correlation = additive_autocorrelation(product)
    forbidden = Y * Y - 1
    return HeckeFoldCounterexample(
        length=Y,
        forbidden_additive_index=forbidden,
        product_coefficients=tuple(sorted(product.items())),
        autocorrelation_coefficient=correlation[forbidden],
        occurs_in_short_hecke_support=forbidden in formal_short_hecke_support(Y),
    )


def flat_product_autocorrelation(length: int) -> dict[int, int]:
    """Exact additive autocorrelation of the truncated divisor sequence."""

    Y = int(length)
    if Y <= 0:
        raise ValueError("length must be positive")
    products = Counter(first * second for first in range(1, Y + 1) for second in range(1, Y + 1))
    correlation: Counter[int] = Counter()
    for shifted_index, shifted_count in products.items():
        for base_index, base_count in products.items():
            correlation[shifted_index - base_index] += shifted_count * base_count
    return dict(correlation)


@dataclass(frozen=True)
class FlatAutocorrelationBarrier:
    length: int
    degree: int
    zero_shift: int
    off_diagonal_l1: int
    off_diagonal_l2_squared: int
    exact_nonzero_support: int
    theorem_lower_bound: Fraction
    tensor_squared_norm: int


def flat_autocorrelation_barrier(length: int) -> FlatAutocorrelationBarrier:
    r"""Return the exact energy and the elementary ``asymp D^3`` bound.

    If ``Y=length`` and ``D=Y^2``, then ``B(0)<=Y^3`` and at most
    ``2Y^2`` nonzero shifts occur.  Cauchy therefore gives

    ``sum_(Delta!=0) B(Delta)^2 >= Y^4*(Y-1)^2/2``.
    """

    Y = int(length)
    if Y <= 1:
        raise ValueError("length must exceed one")
    correlation = flat_product_autocorrelation(Y)
    zero_shift = correlation[0]
    off_diagonal = {shift: value for shift, value in correlation.items() if shift}
    return FlatAutocorrelationBarrier(
        length=Y,
        degree=Y * Y,
        zero_shift=zero_shift,
        off_diagonal_l1=sum(off_diagonal.values()),
        off_diagonal_l2_squared=sum(value * value for value in off_diagonal.values()),
        exact_nonzero_support=len(off_diagonal),
        theorem_lower_bound=Fraction(Y**4 * (Y - 1) ** 2, 2),
        tensor_squared_norm=Y**4,
    )


@dataclass(frozen=True)
class CoefficientBlindMainBarrier:
    length: int
    odd_products: int
    even_products: int
    odd_shift_l1: int
    odd_shift_l2_squared: int
    cauchy_lower_bound: Fraction
    guaranteed_one_residual_squared_norm: int


def parity_twist_main_barrier(length: int) -> CoefficientBlindMainBarrier:
    r"""Certify that one fixed main term cannot cancel flat and parity-twisted data.

    If ``S`` multiplies lag ``Delta`` by ``(-1)^Delta``, then for every
    vector ``T`` one of ``||B-T||_2^2`` and ``||S B-T||_2^2`` is at least
    the odd-lag energy of ``B``, which is ``>>Y^6``.
    """

    Y = int(length)
    if Y <= 1:
        raise ValueError("length must exceed one")
    correlation = flat_product_autocorrelation(Y)
    odd_lags = [value for shift, value in correlation.items() if shift % 2]
    odd_products = ((Y + 1) // 2) ** 2
    even_products = Y * Y - odd_products
    odd_l1 = sum(odd_lags)
    odd_l2 = sum(value * value for value in odd_lags)
    return CoefficientBlindMainBarrier(
        length=Y,
        odd_products=odd_products,
        even_products=even_products,
        odd_shift_l1=odd_l1,
        odd_shift_l2_squared=odd_l2,
        cauchy_lower_bound=Fraction(4 * odd_products**2 * even_products**2, Y**2),
        guaranteed_one_residual_squared_norm=odd_l2,
    )


@dataclass(frozen=True)
class DFILowerBlockLedger:
    degree_exponent: Fraction
    dual_box_length_exponent: Fraction
    delta_modulus_exponent: Fraction
    mismatch_exponent: Fraction
    local_constancy_cutoff_exponent: Fraction
    nonzero_poisson_cutoff_exponent: Fraction
    cutoff_separation_exponent: Fraction
    nonzero_blocks_have_constant_mismatch_weight: bool


def dfi_lower_block_ledger() -> DFILowerBlockLedger:
    """Return the balanced lower-block cutoff comparison."""

    degree = Fraction(16, 33)
    dual_length = degree / 2
    delta_modulus = Fraction(25, 33)
    mismatch = Fraction(34, 33)
    local_constancy = delta_modulus - degree
    nonzero_poisson = delta_modulus - dual_length
    return DFILowerBlockLedger(
        degree_exponent=degree,
        dual_box_length_exponent=dual_length,
        delta_modulus_exponent=delta_modulus,
        mismatch_exponent=mismatch,
        local_constancy_cutoff_exponent=local_constancy,
        nonzero_poisson_cutoff_exponent=nonzero_poisson,
        cutoff_separation_exponent=nonzero_poisson - local_constancy,
        nonzero_blocks_have_constant_mismatch_weight=True,
    )


@dataclass(frozen=True)
class AutocorrelationExponentLedger:
    target_squared_data_exponent: Fraction
    barrier_squared_data_exponent: Fraction
    signed_shift_exponent: Fraction
    target_final_exponent: Fraction
    barrier_final_exponent: Fraction
    missing_exponent: Fraction
    missing_power_in_degree: Fraction


def autocorrelation_exponent_ledger() -> AutocorrelationExponentLedger:
    """Return the exact balanced ``sqrt(D)`` loss ledger."""

    target_squared = Fraction(166, 33)
    degree = Fraction(16, 33)
    barrier_squared = target_squared + degree
    signed_shift = Fraction(17, 33)
    target_final = target_squared / 2 + signed_shift
    barrier_final = barrier_squared / 2 + signed_shift
    return AutocorrelationExponentLedger(
        target_squared_data_exponent=target_squared,
        barrier_squared_data_exponent=barrier_squared,
        signed_shift_exponent=signed_shift,
        target_final_exponent=target_final,
        barrier_final_exponent=barrier_final,
        missing_exponent=barrier_final - target_final,
        missing_power_in_degree=(barrier_final - target_final) / degree,
    )


@dataclass(frozen=True)
class YangTypeIScope:
    general_generic_gl3: bool
    includes_noncuspidal_gl3: bool
    includes_gl2_continuous_spectrum: bool
    includes_singular_degenerate_and_residue_terms: bool
    scalar_input_is_one_gl3_vector: bool
    arbitrary_mask_interpolation_proved: bool
    vector_valued_character_square_function_proved: bool
    automatic_qp_closure: bool


def yang_type_i_scope() -> YangTypeIScope:
    """Record exactly what arXiv:2512.03305 supplies for this route."""

    return YangTypeIScope(
        general_generic_gl3=True,
        includes_noncuspidal_gl3=True,
        includes_gl2_continuous_spectrum=True,
        includes_singular_degenerate_and_residue_terms=True,
        scalar_input_is_one_gl3_vector=True,
        arbitrary_mask_interpolation_proved=False,
        vector_valued_character_square_function_proved=False,
        automatic_qp_closure=False,
    )


def gl3_whittaker_torus_coordinates(carrier: int, cofactor: int) -> tuple[int, int, int]:
    r"""Return the standard GL(3) torus point for indices ``(b, ac)``.

    With the convention ``(m,n) -> diag(m*n,m,1)``, the two Whittaker
    indices really do retain both the total product and the common carrier.
    """

    b = int(carrier)
    n = int(cofactor)
    if b <= 0 or n <= 0:
        raise ValueError("indices must be positive")
    return b * n, b, 1


def spherical_gl3_prime_corner(first_boundary: complex, second_boundary: complex) -> complex:
    r"""Force ``A(p,p)`` from the unramified GL(3) Hecke relation.

    For a normalized spherical eigenvector,

    ``A(p,1) A(1,p) = A(p,p) + A(1,1)`` and ``A(1,1)=1``.
    """

    return first_boundary * second_boundary - 1


def maximal_eisenstein_boundary_convolution(
    first: Mapping[int, complex], second: Mapping[int, complex], index: int
) -> complex:
    r"""Return the fixed boundary convolution ``sum_(a*c=n) chi(a)lambda(c)``.

    This models the standard ``L(s,chi)L(s,sigma)`` boundary coefficient of
    ``chi boxplus sigma``.  It is not an arbitrary factor mask.
    """

    n = int(index)
    if n <= 0:
        raise ValueError("index must be positive")
    return sum(
        first.get(divisor, 0j) * second.get(n // divisor, 0j)
        for divisor in range(1, n + 1)
        if n % divisor == 0
    )


@dataclass(frozen=True)
class SuvitieMeanSquareScope:
    fixed_divisor_coefficients: bool
    averages_over_shift: bool
    averages_over_translation: bool
    uniform_fixed_window: bool
    arbitrary_factorization_mask: bool
    retains_common_carrier_fiber: bool
    reaches_full_endpoint_shift_range: bool
    implies_qp_vector_square_function: bool


def suvitie_mean_square_scope() -> SuvitieMeanSquareScope:
    """Record the hypotheses of arXiv:1110.3950 relevant to this gate."""

    return SuvitieMeanSquareScope(
        fixed_divisor_coefficients=True,
        averages_over_shift=True,
        averages_over_translation=True,
        uniform_fixed_window=False,
        arbitrary_factorization_mask=False,
        retains_common_carrier_fiber=False,
        reaches_full_endpoint_shift_range=False,
        implies_qp_vector_square_function=False,
    )


def classical_kloosterman_sum(first: int, second: int, modulus: int) -> complex:
    r"""Return ``S(first,second;modulus)`` by its defining finite sum."""

    c = int(modulus)
    if c <= 0:
        raise ValueError("modulus must be positive")
    return sum(
        cmath.exp(
            2j
            * pi
            * (int(first) * residue + int(second) * pow(residue, -1, c))
            / c
        )
        for residue in range(c)
        if gcd(residue, c) == 1
    )


def crt_forced_hou_pan_indices(
    first: int, second: int, first_modulus: int, second_modulus: int
) -> tuple[int, int]:
    r"""Return the pointwise Hou--Pan indices forced by CRT factorization.

    Let ``(c1,c2)=1`` and suppose both Kloosterman arguments are units
    modulo ``c1*c2``.  CRT gives

    ``S(a,b;c1*c2) = S(a*c2bar,b*c2bar;c1)``
    ``                 * S(a*c1bar,b*c1bar;c2)``.

    Rewriting the factors in Hou--Pan's cross-modulus shape
    ``S(m,c2;c1) S(n,c1;c2)`` forces

    ``m = a*b*c2bar^3 (mod c1)``,
    ``n = a*b*c1bar^3 (mod c2)``.

    Thus both nominal sequence indices depend on both original arguments
    and on the other modulus.  The identity is pointwise, but it does not
    produce the modulus-independent separated coefficient sequences in
    Hou--Pan Theorem 1.3.
    """

    a = int(first)
    b = int(second)
    c1 = int(first_modulus)
    c2 = int(second_modulus)
    if c1 <= 1 or c2 <= 1 or gcd(c1, c2) != 1:
        raise ValueError("moduli must be coprime and exceed one")
    if gcd(a * b, c1 * c2) != 1:
        raise ValueError("both arguments must be units on this CRT stratum")
    c2_bar = pow(c2, -1, c1)
    c1_bar = pow(c1, -1, c2)
    return (
        a * b * pow(c2_bar, 3, c1) % c1,
        a * b * pow(c1_bar, 3, c2) % c2,
    )


def hou_pan_factor_exponent(
    first_modulus_exponent: Fraction,
    second_modulus_exponent: Fraction,
    first_length_exponent: Fraction,
    second_length_exponent: Fraction,
) -> Fraction:
    r"""Power exponent in the stated Hou--Pan Theorem 1.3 factor.

    This evaluates

    ``sqrt(Cmax/Cmin) sqrt(C1^2+M) sqrt(C2^2+N)``

    at the level of powers of the ambient QP prime.  Subpower factors are
    deliberately suppressed.
    """

    x = Fraction(first_modulus_exponent)
    y = Fraction(second_modulus_exponent)
    m = Fraction(first_length_exponent)
    n = Fraction(second_length_exponent)
    return abs(x - y) / 2 + max(2 * x, m) / 2 + max(2 * y, n) / 2


@dataclass(frozen=True)
class HouPanBalancedLedger:
    degree_exponent: Fraction
    dfi_modulus_exponent: Fraction
    first_length_exponent: Fraction
    second_length_exponent: Fraction
    required_saving_exponent: Fraction
    trivial_factor_exponent: Fraction
    hypothetical_two_factor_exponent: Fraction
    hypothetical_two_factor_saving: Fraction
    one_modulus_endpoint_exponent: Fraction
    one_modulus_endpoint_saving: Fraction
    one_modulus_saving_deficit: Fraction
    deficit_power_in_degree: Fraction


def hou_pan_balanced_ledger() -> HouPanBalancedLedger:
    r"""Return the balanced QP ledger for a hypothetical Hou--Pan use.

    The QP scales are

    ``D=Q^(16/33)``, ``C=Q^(25/33)``,
    ``M_h=C^2/D=Q^(34/33)``, and ``N_Delta=D``.

    If one *artificially* factors every DFI modulus as ``c=c1*c2`` with
    both factors power-sized, Theorem 1.3 would have exponent ``59/66``
    and more than enough saving.  A prime (or power-rough) DFI modulus
    forces the one-modulus endpoint ``(C1,C2)=(C,1)``.  Even formally
    extending the theorem to that excluded endpoint gives exponent
    ``91/66``, only ``9/66`` better than the Weil/triangle exponent
    ``100/66``.  The required saving is ``16/66``.
    """

    degree = Fraction(16, 33)
    modulus = Fraction(25, 33)
    first_length = Fraction(34, 33)
    second_length = degree
    required = degree / 2
    trivial = modulus + (first_length + second_length) / 2

    # One optimal power split is C1=Q^(17/33), C2=Q^(8/33).
    two_factor = hou_pan_factor_exponent(
        Fraction(17, 33), Fraction(8, 33), first_length, second_length
    )
    endpoint = hou_pan_factor_exponent(
        modulus, Fraction(0), first_length, second_length
    )
    endpoint_saving = trivial - endpoint
    deficit = required - endpoint_saving
    return HouPanBalancedLedger(
        degree_exponent=degree,
        dfi_modulus_exponent=modulus,
        first_length_exponent=first_length,
        second_length_exponent=second_length,
        required_saving_exponent=required,
        trivial_factor_exponent=trivial,
        hypothetical_two_factor_exponent=two_factor,
        hypothetical_two_factor_saving=trivial - two_factor,
        one_modulus_endpoint_exponent=endpoint,
        one_modulus_endpoint_saving=endpoint_saving,
        one_modulus_saving_deficit=deficit,
        deficit_power_in_degree=deficit / degree,
    )


@dataclass(frozen=True)
class HouPanScope:
    fixed_prime_automorphic_level: bool
    boundary_coefficient_is_one_index: bool
    long_weyl_has_two_moduli: bool
    theorem_13_moduli_are_coprime: bool
    theorem_13_coefficients_are_separated: bool
    arbitrary_two_index_whittaker_tensor: bool
    one_modulus_dfi_kernel: bool
    common_carrier_vector_square_function: bool
    automatic_after_polar_subtraction: bool


def hou_pan_scope() -> HouPanScope:
    """Record the exact scope of the December 2025 Hou--Pan preprint."""

    return HouPanScope(
        fixed_prime_automorphic_level=True,
        boundary_coefficient_is_one_index=True,
        long_weyl_has_two_moduli=True,
        theorem_13_moduli_are_coprime=True,
        theorem_13_coefficients_are_separated=True,
        arbitrary_two_index_whittaker_tensor=False,
        one_modulus_dfi_kernel=False,
        common_carrier_vector_square_function=False,
        automatic_after_polar_subtraction=False,
    )
