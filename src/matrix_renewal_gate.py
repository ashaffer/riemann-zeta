"""Exact ledgers for the R98 positive matrix-renewal gate.

The functions are finite algebra checks supporting the proof report
``results/R98-POSITIVE-MATRIX-RENEWAL-BOSONIC-GATE.md``.  They do not
numerically search for zeta zeros.
"""

from __future__ import annotations

from fractions import Fraction
from numbers import Number


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def mobius(n: int) -> int:
    """Return the Moebius function of a positive integer."""

    if n < 1:
        raise ValueError("n must be positive")
    value = 1
    remaining = n
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            value = -value
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        value = -value
    return value


def reciprocal_eta_coefficient(q: int, n: int) -> int:
    """Coefficient of n**(-s) in 1/[(1-q**(1-s))*zeta(s)].

    Absolute convergence for ``Re(s)>1`` gives

        sum_{j>=0, q**j | n} q**j mu(n/q**j).
    """

    if q < 2 or n < 1:
        raise ValueError("q must be at least 2 and n must be positive")
    coefficient = 0
    power = 1
    while n % power == 0:
        coefficient += power * mobius(n // power)
        if power > n // q:
            break
        power *= q
    return coefficient


def eta_coefficient(q: int, n: int) -> int:
    """Coefficient of n**(-s) in (1-q**(1-s))*zeta(s)."""

    if q < 2 or n < 1:
        raise ValueError("q must be at least 2 and n must be positive")
    return 1 - (q if n % q == 0 else 0)


def primitive_characteristic_coefficient(trace_a: Number) -> Number:
    """Prime/indecomposable coefficient in det(I-K): ``-Tr(A)``."""

    return -trace_a


def _matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def _trace(matrix: Matrix2) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def rank_one_matrix(vector: tuple[int, int]) -> Matrix2:
    """The exact positive-semidefinite matrix ``v v^T``."""

    x, y = map(Fraction, vector)
    return ((x * x, x * y), (x * y, y * y))


def noncommuting_cubic_cycle_traces() -> tuple[Fraction, ...]:
    """Traces over all six words ABC for a PSD noncommuting example.

    The vectors are a=(1,0), b=(1,1), c=(-1,2).  For rank-one matrices,
    every cyclic/reversed word with one of each has trace

        (a.b)(b.c)(c.a) = -1.

    This shows that individual logarithmic cycle weights need not be
    positive under Loewner positivity, even though the bosonic reciprocal
    determinant remains a positive Laplace transform.
    """

    matrices = [
        rank_one_matrix((1, 0)),
        rank_one_matrix((1, 1)),
        rank_one_matrix((-1, 2)),
    ]
    permutations = (
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
    )
    traces = []
    for i, j, k in permutations:
        traces.append(_trace(_matmul(_matmul(matrices[i], matrices[j]), matrices[k])))
    return tuple(traces)


def symmetrized_cubic_log_mass() -> Fraction:
    """The coefficient contributed by the six ABC words in Tr(K^3)/3."""

    return sum(noncommuting_cubic_cycle_traces(), start=Fraction(0)) / 3


def exponential_renewal_characteristic(z: complex, rate: float) -> complex:
    """Return 1-rate/(rate+z)=z/(rate+z) for exponential delays."""

    if rate <= 0:
        raise ValueError("rate must be positive")
    if z == -rate:
        raise ZeroDivisionError("the renewal transform has a pole at -rate")
    return z / (rate + z)


def diagonal_bosonic_coefficient(
    a: Number, b: Number, exponent_2: int, exponent_3: int
) -> Number:
    """Coefficient in 1/[(1-a 2^-s)(1-b 3^-s)]."""

    if exponent_2 < 0 or exponent_3 < 0:
        raise ValueError("exponents must be nonnegative")
    return (a**exponent_2) * (b**exponent_3)
