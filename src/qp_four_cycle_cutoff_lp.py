"""Exact exponent LP for the QP four-cycle two-minimum-product split.

All exponents are powers of ``D`` and are represented by ``Fraction``.
The analytic derivation is in the accompanying report.
"""

from __future__ import annotations

from fractions import Fraction


Q_EXPONENT = Fraction(33, 16)
SLICE_THRESHOLD = Fraction(17, 16)
BALANCED_PEAK = Fraction(5, 4)
MAX_PRODUCT_EXPONENT = Fraction(11, 8)


def positive_part(value: Fraction) -> Fraction:
    return max(Fraction(0), value)


def feasible_second_minimum_interval(
    product_exponent: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return the exact feasible interval for ``b=log_D(lambda_2)``."""

    p = product_exponent
    if p < 0 or p > MAX_PRODUCT_EXPONENT:
        raise ValueError("product exponent is outside the minima range")
    return p / 2, min(p, Q_EXPONENT - p)


def pointwise_multiplicity_exponent(
    product_exponent: Fraction,
    second_minimum_exponent: Fraction,
) -> Fraction:
    """Best current pointwise exponent at fixed ``p,b``.

    This is the minimum of the universal shear bound ``D/lambda_2`` and
    the multi-slice parabolic bound
    ``K sqrt(D/lambda_1)``, including the bare ``+1`` terms.
    """

    p = product_exponent
    b = second_minimum_exponent
    lower, upper = feasible_second_minimum_interval(p)
    if b < lower or b > upper:
        raise ValueError("second minimum is infeasible")
    a = p - b
    kappa = positive_part(p - SLICE_THRESHOLD)
    universal = positive_part(Fraction(1) - b)
    parabolic = kappa + positive_part(Fraction(1) - a) / 2
    return min(universal, parabolic)


def worst_pointwise_multiplicity_at_product(
    product_exponent: Fraction,
) -> Fraction:
    """Solve the one-dimensional pointwise LP exactly."""

    p = product_exponent
    feasible_second_minimum_interval(p)
    if p <= Fraction(1, 2):
        return Fraction(1, 2)
    if p <= SLICE_THRESHOLD:
        return (2 - p) / 3
    if p <= BALANCED_PEAK:
        return (p - Fraction(1, 8)) / 3
    return 1 - p / 2


def tail_pointwise_multiplicity(cutoff_exponent: Fraction) -> Fraction:
    """Return ``sup_{p>=tau} mu(p)`` for a nonempty high branch."""

    tau = cutoff_exponent
    if tau < 0 or tau > MAX_PRODUCT_EXPONENT:
        raise ValueError("cutoff exponent is outside the product range")
    if tau <= Fraction(1, 2):
        return Fraction(1, 2)
    if tau <= Fraction(7, 8):
        return (2 - tau) / 3
    if tau <= BALANCED_PEAK:
        return Fraction(3, 8)
    return 1 - tau / 2


def aggregate_low_trace_exponent(cutoff_exponent: Fraction) -> Fraction:
    """New aggregate low-branch trace exponent ``5/4+kappa(tau)``."""

    tau = cutoff_exponent
    if tau < 0 or tau > MAX_PRODUCT_EXPONENT:
        raise ValueError("cutoff exponent is outside the product range")
    return Fraction(5, 4) + positive_part(tau - SLICE_THRESHOLD)


def cutoff_trace_exponent(cutoff_exponent: Fraction) -> Fraction:
    """Trace exponent delivered by the aggregate-low/pointwise-high split."""

    return max(
        aggregate_low_trace_exponent(cutoff_exponent),
        1 + tail_pointwise_multiplicity(cutoff_exponent),
    )

