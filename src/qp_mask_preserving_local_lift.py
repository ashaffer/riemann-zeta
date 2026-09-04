"""Exact finite tests for the proposed mask-preserving local lift.

The functions in this module isolate three algebraic facts which do not
depend on asymptotics or on a choice of Bessel majorant.

* Fundamental first-Poisson CRT phase ranges for two coprime moduli meet
  only on the coherent ``k = t*c`` residue.
* Deleting that residue does not change the nonzero part of the complete
  bilinear Gauss sum used by the second Poisson transform.
* The resulting Kloosterman index is a *difference of products*.  Grouping
  it into one Hecke polynomial produces additive-autocorrelation
  coefficients, whose l2 norm is not bounded by the tensor input norm.

This is a method-level obstruction.  It does not disprove an estimate that
uses additional cancellation in the full DFI modulus sum.
"""

from __future__ import annotations

import cmath
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, pi
from typing import Mapping, Sequence


def centered_residue(value: int, modulus: int) -> int:
    """Return the standard centered representative modulo ``modulus``."""

    if modulus <= 0:
        raise ValueError("modulus must be positive")
    residue = int(value) % modulus
    if 2 * residue > modulus:
        residue -= modulus
    return residue


def normalized_crt_phase(
    row_step: int,
    row_bezout: int,
    modulus: int,
    numerator: int,
    row_fan: int,
    residue_frequency: int,
) -> Fraction:
    """Return ``U*r/R-a*k0/c`` in ``Q/Z`` as a fraction in ``[0,1)``."""

    R = int(row_step)
    U = int(row_bezout)
    c = int(modulus)
    a = int(numerator)
    r = int(row_fan)
    k0 = int(residue_frequency)
    if R <= 0 or c <= 0:
        raise ValueError("periods must be positive")
    if gcd(U, R) != 1 or gcd(a, c) != 1 or gcd(c, R) != 1:
        raise ValueError("CRT parameters must be units in their periods")
    if not 0 <= r < R or not 0 <= k0 < c:
        raise ValueError("indices must be fundamental residues")
    phase = Fraction(U * r, R) - Fraction(a * k0, c)
    return phase % 1


def cross_modulus_phase_intersections(
    row_step: int,
    row_bezout: int,
    first_modulus: int,
    first_numerator: int,
    second_modulus: int,
    second_numerator: int,
) -> tuple[tuple[int, int, int, int], ...]:
    """Enumerate exact intersections of two fundamental CRT phase ranges.

    When the two moduli are pairwise coprime with ``R``, the theorem-level
    answer is exactly ``(r,0,r,0)`` for ``r mod R``.  Enumeration is useful
    as a finite regression test for the denominator argument.
    """

    R = int(row_step)
    c = int(first_modulus)
    cp = int(second_modulus)
    if gcd(c, cp) != 1:
        raise ValueError("the two moduli must be coprime")
    intersections: list[tuple[int, int, int, int]] = []
    first: dict[Fraction, list[tuple[int, int]]] = defaultdict(list)
    for r in range(R):
        for k0 in range(c):
            phase = normalized_crt_phase(
                R, row_bezout, c, first_numerator, r, k0
            )
            first[phase].append((r, k0))
    for rp in range(R):
        for kp0 in range(cp):
            phase = normalized_crt_phase(
                R, row_bezout, cp, second_numerator, rp, kp0
            )
            for r, k0 in first.get(phase, ()):
                intersections.append((r, k0, rp, kp0))
    return tuple(intersections)


def _additive_character(value: int, modulus: int) -> complex:
    return cmath.exp(2j * pi * (int(value) % int(modulus)) / int(modulus))


def complete_bilinear_sum(
    modulus: int,
    numerator: int,
    row_frequency: int,
    color_frequency: int,
    *,
    delete_row_zero: bool = False,
    delete_color_zero: bool = False,
) -> complex:
    """Brute-force ``sum e_c(a*x*y+u*x+v*y)`` with optional zero deletion."""

    c = int(modulus)
    a = int(numerator)
    u = int(row_frequency)
    v = int(color_frequency)
    if c <= 1 or gcd(a, c) != 1:
        raise ValueError("numerator must be a unit modulo a nontrivial modulus")
    return sum(
        _additive_character(a * x * y + u * x + v * y, c)
        for x in range(c)
        if not (delete_row_zero and x == 0)
        for y in range(c)
        if not (delete_color_zero and y == 0)
    )


def complete_bilinear_prediction(
    modulus: int,
    numerator: int,
    row_frequency: int,
    color_frequency: int,
    *,
    delete_row_zero: bool = False,
    delete_color_zero: bool = False,
) -> complex:
    """Return the exact closed form for :func:`complete_bilinear_sum`.

    In particular, deleting only the color zero residue gives

    ``c*(e_c(-a_bar*u*v)-1_(u=0 mod c))``.

    Thus the coherent projection is literally invisible whenever ``u`` is
    nonzero.  Deleting both zero residues adds only the displayed
    axis/Ramanujan corrections.
    """

    c = int(modulus)
    a = int(numerator)
    u = int(row_frequency)
    v = int(color_frequency)
    if c <= 1 or gcd(a, c) != 1:
        raise ValueError("numerator must be a unit modulo a nontrivial modulus")
    a_bar = pow(a, -1, c)
    value = c * _additive_character(-a_bar * u * v, c)
    if delete_color_zero:
        value -= c * int(u % c == 0)
    if delete_row_zero:
        value -= c * int(v % c == 0)
    if delete_row_zero and delete_color_zero:
        value += 1
    return value


def transformed_frequency(
    fan: int, modulus: int, step: int, bezout: int
) -> int:
    """Return the centered dual frequency ``bezout*fan*c (mod step)``."""

    return centered_residue(int(bezout) * int(fan) * int(modulus), int(step))


def physical_tuple_delta_profile(
    row_step: int,
    color_step: int,
    row_bezout: int,
    color_bezout: int,
    row_fan: int,
    second_row_fan: int,
    color_fan: int,
    second_color_fan: int,
    moduli: Sequence[int],
) -> tuple[tuple[int, int, int, int, int, int], ...]:
    """Return ``(c,nu,mu,nu',mu',Delta_c)`` for one physical four-tuple."""

    profile = []
    for modulus in moduli:
        nu = transformed_frequency(row_fan, modulus, row_step, row_bezout)
        nu_prime = transformed_frequency(
            second_row_fan, modulus, row_step, row_bezout
        )
        mu = transformed_frequency(color_fan, modulus, color_step, color_bezout)
        mu_prime = transformed_frequency(
            second_color_fan, modulus, color_step, color_bezout
        )
        profile.append(
            (
                int(modulus),
                nu,
                mu,
                nu_prime,
                mu_prime,
                nu * mu - nu_prime * mu_prime,
            )
        )
    return tuple(profile)


def product_convolution(
    first: Mapping[int, complex], second: Mapping[int, complex]
) -> dict[int, complex]:
    """Return ``g(m)=sum_(u*v=m) first[u]*second[v]``."""

    result: dict[int, complex] = defaultdict(complex)
    for u, first_value in first.items():
        for v, second_value in second.items():
            result[int(u) * int(v)] += first_value * second_value
    return dict(result)


def additive_autocorrelation(values: Mapping[int, complex]) -> dict[int, complex]:
    """Return ``c_delta=sum_m g(m)*conj(g(m-delta))``."""

    result: dict[int, complex] = defaultdict(complex)
    items = tuple((int(index), value) for index, value in values.items())
    for first_index, first_value in items:
        for second_index, second_value in items:
            result[first_index - second_index] += first_value * second_value.conjugate()
    return dict(result)


def flat_product_autocorrelation(length: int) -> dict[int, int]:
    """Return the exact correlation coefficients for two flat ``[1,L]`` inputs."""

    L = int(length)
    if L <= 0:
        raise ValueError("length must be positive")
    products = Counter(u * v for u in range(1, L + 1) for v in range(1, L + 1))
    correlation: Counter[int] = Counter()
    for first_product, first_count in products.items():
        for second_product, second_count in products.items():
            correlation[first_product - second_product] += first_count * second_count
    return dict(correlation)


def flat_product_energy_ledger(length: int) -> dict[str, int | Fraction]:
    """Return exact norms and the elementary Cauchy lower bound.

    The expected sharp tensor RHS is

    ``(||p||_2^2 ||q||_2^2)^2=L^4``.

    Even after deleting ``Delta=0``, the actual squared coefficient norm is
    at least ``L^4*(L-1)^2/2``.  Hence the ratio is at least
    ``(L-1)^2/2``.
    """

    L = int(length)
    if L <= 1:
        raise ValueError("length must be at least two")
    correlation = flat_product_autocorrelation(L)
    diagonal = correlation.get(0, 0)
    off_diagonal_l1 = sum(
        coefficient for delta, coefficient in correlation.items() if delta
    )
    off_diagonal_l2_squared = sum(
        coefficient * coefficient
        for delta, coefficient in correlation.items()
        if delta
    )
    tensor_rhs = L**4
    cauchy_lower_bound = Fraction(L**4 * (L - 1) ** 2, 2)
    return {
        "length": L,
        "diagonal": diagonal,
        "off_diagonal_l1": off_diagonal_l1,
        "off_diagonal_l2_squared": off_diagonal_l2_squared,
        "tensor_rhs": tensor_rhs,
        "cauchy_lower_bound": cauchy_lower_bound,
        "lower_bound_ratio": Fraction((L - 1) ** 2, 2),
    }


def formal_hecke_product_support(length: int) -> frozenset[int]:
    """Return indices obtainable from two Hecke polynomials of length ``Y``.

    The formal unramified relation is

    ``lambda(m)lambda(n)=sum_(d|(m,n))lambda(m*n/d^2)``.
    """

    Y = int(length)
    if Y <= 0:
        raise ValueError("length must be positive")
    support: set[int] = set()
    for m in range(1, Y + 1):
        for n in range(1, Y + 1):
            common = gcd(m, n)
            for divisor in range(1, common + 1):
                if common % divisor == 0:
                    support.add(m * n // (divisor * divisor))
    return frozenset(support)


def difference_of_products_prime_fixture(length: int, prime: int) -> tuple[int, int, int, int]:
    """Realize ``prime=Y*2-1*(2Y-prime)`` inside the ``Y`` dual box."""

    Y = int(length)
    p = int(prime)
    remainder = 2 * Y - p
    if not (Y < p < 2 * Y) or not (1 <= remainder <= Y):
        raise ValueError("prime must lie strictly between Y and 2Y")
    return Y, 2, 1, remainder


def separated_product_support_fixture(
    ambient_length: int,
    interval_length: int,
    branch_count: int,
    modulation: int = 0,
) -> tuple[dict[int, complex], dict[int, complex]]:
    """Return a separable nonzero fixture with an isolated short-shift branch.

    Put ``U=[Y/2,Y/2+L)`` and

    ``V={1,2L,4L,...,2KL}``.

    Provided ``K<=Y/(4L)``, the product intervals ``v*U`` for distinct
    ``v`` are separated by more than ``L``.  Products within a branch
    ``v>=2L`` differ either by zero or by at least ``2L``.  Consequently,
    for every ``0<|h|<L``, the autocorrelation comes only from the
    nonzero branch ``v=1`` and equals a modulated triangular vector.
    """

    Y = int(ambient_length)
    L = int(interval_length)
    K = int(branch_count)
    j = int(modulation) % L
    if Y < 8 or L < 2 or K < 1:
        raise ValueError("need Y>=8, L>=2, and at least one separated branch")
    if L > Y // 4 or K > Y // (4 * L):
        raise ValueError("the separated product blocks do not fit in the ambient box")
    start = Y // 2
    first = {
        u: cmath.exp(2j * pi * j * u / L)
        for u in range(start, start + L)
    }
    second = {1: 1.0 + 0.0j}
    second.update({2 * L * index: 1.0 + 0.0j for index in range(1, K + 1)})
    if max(first) > Y or max(second) > Y:
        raise AssertionError("fixture escaped the ambient dual box")
    return first, second


def separated_short_shift_coefficients(
    ambient_length: int,
    interval_length: int,
    branch_count: int,
    modulation: int = 0,
) -> dict[int, complex]:
    """Return the positive short shifts of the separated fixture."""

    first, second = separated_product_support_fixture(
        ambient_length, interval_length, branch_count, modulation
    )
    correlation = additive_autocorrelation(product_convolution(first, second))
    return {
        shift: correlation.get(shift, 0.0 + 0.0j)
        for shift in range(1, int(interval_length))
    }


def polar_projection_frame_ledger(
    interval_length: int,
    polar_rank: int,
) -> dict[str, int | Fraction]:
    """Return the exact Fourier-frame obstruction to finite-rank subtraction.

    For ``j=0,...,L-1`` set

    ``b_j(h)=(L-h)e(j*h/L)``, ``1<=h<L``.

    The average Gram operator is ``diag((L-h)^2)``.  Therefore for every
    orthogonal projection of rank ``d`` at least one modulation satisfies

    ``||(1-P)b_j||_2^2 >= sum_(n=1)^(L-d-1)n^2``.

    This is the exact Ky Fan trace bound; the weaker but convenient lower
    bound ``S-d*(L-1)^2`` is also returned.  The result applies to any
    prescribed finite-dimensional polar/main-term space, not merely a
    coordinate projection.
    """

    L = int(interval_length)
    d = int(polar_rank)
    if L < 2 or not 0 <= d < L:
        raise ValueError("need L>=2 and 0<=rank<L")
    norm_squared = (L - 1) * L * (2 * L - 1) // 6
    crude_projection_upper_bound = d * (L - 1) ** 2
    # The eigenvalues of the averaged frame operator are
    # (L-1)^2,(L-2)^2,...,1.  Ky Fan's principle makes the following
    # upper bound exact among all rank-d orthogonal projections.
    ky_fan_projection_upper_bound = sum(
        value * value for value in range(L - d, L)
    )
    exact_residual_lower_bound = sum(
        value * value for value in range(1, L - d)
    )
    assert norm_squared == (
        ky_fan_projection_upper_bound + exact_residual_lower_bound
    )
    crude_residual_lower_bound = max(
        0, norm_squared - crude_projection_upper_bound
    )
    return {
        "length": L,
        "polar_rank": d,
        "modulation_count": L,
        "one_vector_norm_squared": norm_squared,
        "projection_average_upper_bound": crude_projection_upper_bound,
        "ky_fan_projection_average_upper_bound": ky_fan_projection_upper_bound,
        "some_residual_norm_squared": exact_residual_lower_bound,
        "crude_residual_norm_squared": crude_residual_lower_bound,
        "residual_fraction_lower_bound": Fraction(
            exact_residual_lower_bound, norm_squared
        ),
    }


def minimum_polar_rank_for_residual(
    interval_length: int,
    residual_budget: int,
) -> int:
    """Return the minimum rank allowed by the exact Fourier-frame trace test.

    If one fixed rank-``d`` space is to leave squared residual at most ``T``
    for *every* modulation, the Ky Fan trace identity forces

    ``sum_(n=1)^(L-d-1)n^2 <= T``.

    This function returns the least ``d`` satisfying that necessary
    condition.  It does not assert that a space of that rank controls each
    modulation individually.
    """

    L = int(interval_length)
    T = int(residual_budget)
    if L < 2 or T < 0:
        raise ValueError("need L>=2 and a nonnegative residual budget")

    def square_pyramid(height: int) -> int:
        return height * (height + 1) * (2 * height + 1) // 6

    # Maximize m=L-d-1 subject to square_pyramid(m)<=T.
    low, high = 0, L - 1
    while low < high:
        middle = (low + high + 1) // 2
        if square_pyramid(middle) <= T:
            low = middle
        else:
            high = middle - 1
    return L - 1 - low


def separated_short_shift_energy_ledger(
    interval_length: int,
    branch_count: int,
) -> dict[str, int | Fraction]:
    """Return the exact normalization and required polar rank of the fixture.

    The positive short-shift energy is

    ``S_L=sum_(h=1)^(L-1)(L-h)^2``

    while the proposed tensor-scale squared bound is

    ``T=(||p||_2^2||q||_2^2)^2=L^2(K+1)^2``.
    """

    L = int(interval_length)
    K = int(branch_count)
    if L < 2 or K < 1:
        raise ValueError("need L>=2 and at least one separated branch")
    short_shift_energy = (L - 1) * L * (2 * L - 1) // 6
    tensor_rhs = L * L * (K + 1) ** 2
    return {
        "length": L,
        "branch_count": K,
        "short_shift_energy": short_shift_energy,
        "tensor_rhs": tensor_rhs,
        "energy_ratio": Fraction(short_shift_energy, tensor_rhs),
        "minimum_rank_from_trace": minimum_polar_rank_for_residual(
            L, tensor_rhs
        ),
    }
