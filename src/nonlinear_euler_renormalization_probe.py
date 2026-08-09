"""Exact local algebra for nonlinear Euler/prime-zeta renormalization.

The routines here are deliberately finite and symbolic.  They certify the
local coefficient identities used in
``R97-NONLINEAR-EULER-PRIME-ZETA-RIGIDITY-GATE.md``; they do not search for
zeta zeros or claim a zero-free region.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from numbers import Number


def gc_local_coefficient(c: Number, k: int) -> Number:
    """Coefficient of z**k in (1-z) exp(c*z)."""

    if k < 0:
        raise ValueError("k must be nonnegative")
    if k == 0:
        return 1
    if k == 1:
        return c - 1
    return (c ** (k - 1)) * (c - k) / factorial(k)


def higher_renormalized_local_coefficients(r: int, degree: int) -> list[Fraction]:
    """Taylor coefficients through ``degree`` of

        exp(-sum_{m>=r} z**m/m).

    Terms above ``degree`` cannot affect the requested truncation.  The
    exponential-series recurrence keeps the calculation exact over Q.
    """

    if r < 2:
        raise ValueError("r must be at least 2")
    if degree < 0:
        raise ValueError("degree must be nonnegative")

    coefficients = [Fraction(0) for _ in range(degree + 1)]
    coefficients[0] = Fraction(1)
    for n in range(1, degree + 1):
        # If E=exp(L), then n E_n=sum_{k=1}^n k L_k E_{n-k}.
        # Here k L_k=-1 for k>=r and zero otherwise.
        coefficients[n] = -sum(
            (coefficients[n - k] for k in range(r, n + 1)),
            start=Fraction(0),
        ) / n
    return coefficients


def scalar_squarefree_layer_coefficient(b_r: Number, r: int) -> Number:
    """Coefficient on a squarefree product of exactly r primes in b_r U**r.

    Here U=sum_{n>=2} mu(n)n^{-s}; each of the r prime factors can be
    assigned to the r ordered convolution slots in r! ways.
    """

    if r < 1:
        raise ValueError("r must be positive")
    return b_r * ((-1) ** r) * factorial(r)


def zero_preserving_example_taylor(degree: int) -> list[Fraction]:
    """Taylor coefficients of (1+u)exp(-u) through ``degree``."""

    if degree < 0:
        raise ValueError("degree must be nonnegative")
    output: list[Fraction] = []
    for j in range(degree + 1):
        if j == 0:
            output.append(Fraction(1))
        else:
            output.append(Fraction(((-1) ** j) * (1 - j), factorial(j)))
    return output
