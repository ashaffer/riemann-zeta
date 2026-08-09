import math
from fractions import Fraction

import pytest

from lcm_factorial_integrality_probe import (
    canonical_certificate_layer,
    canonical_certificate_valuation,
    determinant_3_by_3,
    direct_integer_multiplier_valuation,
    divisibility_non_tu_minor,
    factorial_layer_profile,
    factorial_ratio_log,
    lcm_ratio_valuation,
    layer_profile_log,
    mobius_inverted_factorial_exponents,
    mobius_sieve,
    prime_powers,
    primes_up_to,
    truncated_inverse_profile,
    truncated_residual_valuation,
)


def _lcm_upto(n: int) -> int:
    answer = 1
    for value in range(1, n + 1):
        answer = math.lcm(answer, value)
    return answer


def _valuation(integer: int, prime: int) -> int:
    answer = 0
    while integer % prime == 0:
        answer += 1
        integer //= prime
    return answer


def test_mobius_sieve_initial_values() -> None:
    assert mobius_sieve(12) == [0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0]


def test_lcm_ratio_valuation_matches_exact_fraction() -> None:
    N = 9
    lcms = [_lcm_upto(m) for m in range(1, N + 1)]
    ratio = Fraction(lcms[-1] ** N, math.prod(value**2 for value in lcms[:-1]))
    for prime in primes_up_to(N):
        exact = _valuation(ratio.numerator, prime) - _valuation(ratio.denominator, prime)
        assert lcm_ratio_valuation(N, prime) == exact


def test_canonical_factorial_lcm_certificate_is_integral() -> None:
    for N in range(3, 13):
        lcms = [_lcm_upto(m) for m in range(1, N + 1)]
        numerator = (math.factorial(N) // lcms[-1]) ** N
        denominator = math.prod(
            (math.factorial(m) // lcms[m - 1]) ** 2 for m in range(1, N)
        )
        assert numerator % denominator == 0
        for prime in primes_up_to(N):
            assert canonical_certificate_valuation(N, prime) >= 0


@pytest.mark.parametrize("N,q", [(20, 3), (20, 7), (21, 10), (64, 16), (64, 33)])
def test_closed_canonical_layer_formula(N: int, q: int) -> None:
    direct = N * (N // q - 1) - 2 * sum(
        max(m // q - 1, 0) for m in range(1, N)
    )
    assert canonical_certificate_layer(N, q) == direct


def test_factorial_layer_transform_has_exact_mobius_inverse() -> None:
    profile = [0, 0, 7, -3, 2, 0, -5, 4, 1, -2, 6, 0, -1]
    exponents, _ = mobius_inverted_factorial_exponents(profile)
    assert factorial_layer_profile(exponents) == profile


def test_truncated_inverse_leaves_only_small_prime_powers() -> None:
    N = 30
    cutoff = 5
    profile = truncated_inverse_profile(N, cutoff)
    exponents, _ = mobius_inverted_factorial_exponents(profile)
    assert factorial_layer_profile(exponents) == profile
    for prime in primes_up_to(N):
        factorial_valuation = sum(profile[q] for q in prime_powers(prime, N))
        combined = lcm_ratio_valuation(N, prime) + factorial_valuation
        assert combined == -truncated_residual_valuation(N, cutoff, prime)
        assert combined <= 0


def test_factorial_log_equals_von_mangoldt_layer_log() -> None:
    profile = truncated_inverse_profile(40, 6)
    exponents, _ = mobius_inverted_factorial_exponents(profile)
    assert factorial_ratio_log(exponents) == pytest.approx(
        layer_profile_log(profile), abs=2e-9
    )


def test_tail_cumulative_exponents_have_both_signs() -> None:
    N = 100
    profile = truncated_inverse_profile(N, 10)
    _, cumulative = mobius_inverted_factorial_exponents(profile)
    assert cumulative[40] == 80  # N/3 < 40 < N/2: h(40)-h(80)=2*40.
    assert cumulative[60] == -20  # N/2 < 60: only h(60) survives.


def test_direct_integer_multiplier_requires_exact_negative_valuation() -> None:
    N = 60
    prime = 17
    assert lcm_ratio_valuation(N, prime) == -26
    assert direct_integer_multiplier_valuation(N, prime) == 26
    assert direct_integer_multiplier_valuation(N, prime, reciprocal=True) == 0


def test_divisibility_incidence_is_not_totally_unimodular() -> None:
    minor = divisibility_non_tu_minor()
    assert minor == ((1, 1, 0), (1, 0, 1), (0, 1, 1))
    assert determinant_3_by_3(minor) == -2
