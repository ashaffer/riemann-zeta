#!/usr/bin/env python3
"""Exact algebra for scaled pole-killing kernels and boundary expansions.

The analytic theorem is stated and proved in the companion report.  This
module provides exact rational replay for its minimal exponential filters and
high-precision evaluation of the associated kernel jets.  The numerical
evaluators are deliberately real-scalar; complex continuation is represented
by the exact transfer formulas in the report rather than by this replay API.

For distinct rates ``a_0,...,a_m`` and a positive anchor ``sigma``, define

    phi(z) = sum_j c_j exp(-a_j z),
    c_j = (sigma+a_j)^m / product_{l != j}(a_j-a_l).

Then ``phi(0)=1`` and

    Laplace(phi)(s) = (s-sigma)^m / product_j (s+a_j).

Thus the scaled multiplier ``delta^(-1) Laplace(phi)(q/delta)`` has an
order-``m`` zero at ``q=sigma*delta``.  Functions without an explicit anchor
retain the historical normalization ``sigma=1``.
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Callable, Sequence

import mpmath as mp


Rational = int | Fraction
Anchor = tuple[Rational, int]


def _as_fractions(values: Sequence[Rational]) -> tuple[Fraction, ...]:
    return tuple(Fraction(value) for value in values)


def _as_mpf(value: object) -> mp.mpf:
    if isinstance(value, Fraction):
        return mp.mpf(value.numerator) / value.denominator
    return mp.mpf(value)  # type: ignore[arg-type]


def _parse_anchors(anchors: Sequence[Anchor]) -> tuple[tuple[Fraction, int], ...]:
    parsed: list[tuple[Fraction, int]] = []
    for anchor, multiplicity in anchors:
        if type(multiplicity) is not int or multiplicity <= 0:
            raise ValueError("anchor multiplicities must be positive integers")
        anchor_value = Fraction(anchor)
        if anchor_value <= 0:
            raise ValueError("anchors must be positive")
        parsed.append((anchor_value, multiplicity))
    return tuple(parsed)


def _validate_nonnegative_integer(value: object, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _finite_mpf(value: object, name: str) -> mp.mpf:
    parsed = _as_mpf(value)
    if not mp.isfinite(parsed):
        raise ValueError(f"{name} must be finite")
    return parsed


def _parse_numeric_anchors(
    anchors: Sequence[tuple[float | mp.mpf, int]],
) -> tuple[tuple[mp.mpf, int], ...]:
    parsed: list[tuple[mp.mpf, int]] = []
    for anchor, multiplicity in anchors:
        anchor_value = _finite_mpf(anchor, "anchors")
        if anchor_value <= 0:
            raise ValueError("anchors must be positive")
        if type(multiplicity) is not int or multiplicity <= 0:
            raise ValueError("anchor multiplicities must be positive integers")
        if any(anchor_value == previous for previous, _ in parsed):
            raise ValueError("anchors must be distinct")
        parsed.append((anchor_value, multiplicity))
    return tuple(parsed)


def minimal_exponential_coefficients(
    rates: Sequence[Rational],
) -> tuple[Fraction, ...]:
    """Return the unique minimal order-``m`` pole-killing coefficients.

    There must be ``m+1`` distinct rates.  The coefficients are the Lagrange
    interpolation weights at zero for the nodes ``1/(1+a_j)``.
    """
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    if min(rational_rates) < 0:
        raise ValueError("rates must be nonnegative")
    if len(set(rational_rates)) != len(rational_rates):
        raise ValueError("rates must be distinct")
    order = len(rational_rates) - 1
    coefficients: list[Fraction] = []
    for index, rate in enumerate(rational_rates):
        denominator = Fraction(1)
        for other_index, other_rate in enumerate(rational_rates):
            if index != other_index:
                denominator *= rate - other_rate
        coefficients.append((1 + rate) ** order / denominator)
    return tuple(coefficients)


def minimal_anchored_exponential_coefficients(
    rates: Sequence[Rational], anchor: Rational = 1
) -> tuple[Fraction, ...]:
    """Return the unique minimal coefficients for a zero at ``anchor``.

    With ``m+1`` rates the returned kernel has Laplace transform

        (s-anchor)^m / product_j (s+a_j).
    """
    if not rates:
        raise ValueError("at least one rate is required")
    if Fraction(anchor) <= 0:
        raise ValueError("anchor must be positive")
    anchors: tuple[Anchor, ...]
    if len(rates) == 1:
        anchors = ()
    else:
        anchors = ((anchor, len(rates) - 1),)
    return multi_anchor_exponential_coefficients(rates, anchors)


def endpoint_flat_exponential_coefficients(
    rates: Sequence[Rational],
    notch_order: int,
    anchor: Rational = 1,
) -> tuple[Fraction, ...]:
    r"""Return the minimal joint notch/endpoint-flat coefficients.

    If there are ``N`` rates and ``m=notch_order``, the endpoint flatness is
    ``r=N-m-1``.  The kernel has ``k^(ell)(0)=0`` for ``ell<r`` and
    ``k^(r)(0)=1``, while its Laplace transform is

        (s-anchor)^m / product_j(s+a_j).
    """
    order = _validate_nonnegative_integer(notch_order, "notch_order")
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    if order >= len(rational_rates):
        raise ValueError("notch_order must be smaller than the number of rates")
    anchor_value = Fraction(anchor)
    if anchor_value <= 0:
        raise ValueError("anchor must be positive")
    if min(rational_rates) < 0 or len(set(rational_rates)) != len(rational_rates):
        raise ValueError("rates must be distinct and nonnegative")
    flat_order = len(rational_rates) - order - 1
    coefficients: list[Fraction] = []
    for index, rate in enumerate(rational_rates):
        denominator = math.prod(
            (
                rate - other_rate
                for other_index, other_rate in enumerate(rational_rates)
                if other_index != index
            ),
            start=Fraction(1),
        )
        coefficients.append(
            (-1) ** flat_order * (anchor_value + rate) ** order / denominator
        )
    return tuple(coefficients)


def multi_anchor_exponential_coefficients(
    rates: Sequence[Rational], anchors: Sequence[Anchor]
) -> tuple[Fraction, ...]:
    r"""Return residues for a finite constellation of multiplier zeros.

    If ``M=sum multiplicities`` and there are ``M+1`` distinct rates, these
    coefficients realize

        sum_j c_j/(s+a_j)
          = product_i (s-sigma_i)^m_i / product_j (s+a_j).
    """
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    parsed_anchors = _parse_anchors(anchors)
    total_order = sum(multiplicity for _, multiplicity in parsed_anchors)
    if len(rational_rates) != total_order + 1:
        raise ValueError("the number of rates must be total zero order plus one")
    if min(rational_rates) < 0 or len(set(rational_rates)) != len(rational_rates):
        raise ValueError("rates must be distinct and nonnegative")
    coefficients: list[Fraction] = []
    for index, rate in enumerate(rational_rates):
        numerator = math.prod(
            ((rate + anchor) ** multiplicity for anchor, multiplicity in parsed_anchors),
            start=Fraction(1),
        )
        denominator = math.prod(
            (
                rate - other_rate
                for other_index, other_rate in enumerate(rational_rates)
                if other_index != index
            ),
            start=Fraction(1),
        )
        coefficients.append(numerator / denominator)
    return tuple(coefficients)


def exact_endpoint_mass(
    rates: Sequence[Rational], coefficients: Sequence[Rational] | None = None
) -> Fraction:
    """Return ``phi(0)=sum c_j`` exactly."""
    if coefficients is None:
        coefficients = minimal_exponential_coefficients(rates)
    if len(rates) != len(coefficients):
        raise ValueError("rates and coefficients must have equal length")
    return sum(_as_fractions(coefficients), Fraction(0))


def exact_pole_moment(
    rates: Sequence[Rational],
    derivative_order: int,
    coefficients: Sequence[Rational] | None = None,
) -> Fraction:
    r"""Return the denominator-free order condition at ``s=1``.

    Up to the nonzero factor ``(-1)^ell ell!``, this is the ``ell``-th
    derivative of ``Laplace(phi)`` at one:

        sum_j c_j / (1+a_j)^(ell+1).
    """
    derivative_order = _validate_nonnegative_integer(
        derivative_order, "derivative_order"
    )
    rational_rates = _as_fractions(rates)
    if coefficients is None:
        coefficients = minimal_exponential_coefficients(rational_rates)
    rational_coefficients = _as_fractions(coefficients)
    if len(rational_rates) != len(rational_coefficients):
        raise ValueError("rates and coefficients must have equal length")
    return sum(
        (
            coefficient / (1 + rate) ** (derivative_order + 1)
            for rate, coefficient in zip(
                rational_rates, rational_coefficients, strict=True
            )
        ),
        Fraction(0),
    )


def exact_laplace_kernel(
    s: Rational,
    rates: Sequence[Rational],
    coefficients: Sequence[Rational] | None = None,
) -> Fraction:
    """Evaluate ``sum c_j/(s+a_j)`` exactly."""
    s_value = Fraction(s)
    rational_rates = _as_fractions(rates)
    if coefficients is None:
        coefficients = minimal_exponential_coefficients(rational_rates)
    rational_coefficients = _as_fractions(coefficients)
    return sum(
        (
            coefficient / (s_value + rate)
            for rate, coefficient in zip(
                rational_rates, rational_coefficients, strict=True
            )
        ),
        Fraction(0),
    )


def exact_laplace_target(s: Rational, rates: Sequence[Rational]) -> Fraction:
    """Evaluate ``(s-1)^m/product_j(s+a_j)`` exactly."""
    s_value = Fraction(s)
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    order = len(rational_rates) - 1
    denominator = math.prod(
        (s_value + rate for rate in rational_rates), start=Fraction(1)
    )
    return (s_value - 1) ** order / denominator


def exact_anchored_laplace_target(
    s: Rational,
    rates: Sequence[Rational],
    anchor: Rational = 1,
) -> Fraction:
    """Evaluate the single-anchor rational target exactly."""
    if not rates:
        raise ValueError("at least one rate is required")
    if Fraction(anchor) <= 0:
        raise ValueError("anchor must be positive")
    anchors: tuple[Anchor, ...]
    if len(rates) == 1:
        anchors = ()
    else:
        anchors = ((anchor, len(rates) - 1),)
    return exact_multi_anchor_laplace_target(s, rates, anchors)


def exact_endpoint_flat_laplace_target(
    s: Rational,
    rates: Sequence[Rational],
    notch_order: int,
    anchor: Rational = 1,
) -> Fraction:
    """Evaluate the minimal joint notch/endpoint-flat target exactly."""
    order = _validate_nonnegative_integer(notch_order, "notch_order")
    rational_rates = _as_fractions(rates)
    if not rational_rates or order >= len(rational_rates):
        raise ValueError("notch_order must be smaller than the number of rates")
    s_value = Fraction(s)
    anchor_value = Fraction(anchor)
    if anchor_value <= 0:
        raise ValueError("anchor must be positive")
    denominator = math.prod(
        (s_value + rate for rate in rational_rates), start=Fraction(1)
    )
    return (s_value - anchor_value) ** order / denominator


def exact_multi_anchor_laplace_target(
    s: Rational, rates: Sequence[Rational], anchors: Sequence[Anchor]
) -> Fraction:
    """Evaluate the rational target for multiple prescribed zeros."""
    s_value = Fraction(s)
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    parsed_anchors = _parse_anchors(anchors)
    if len(rational_rates) != 1 + sum(m for _, m in parsed_anchors):
        raise ValueError("the number of rates must be total zero order plus one")
    numerator = math.prod(
        (
            (s_value - anchor) ** multiplicity
            for anchor, multiplicity in parsed_anchors
        ),
        start=Fraction(1),
    )
    denominator = math.prod(
        (s_value + rate for rate in rational_rates),
        start=Fraction(1),
    )
    return numerator / denominator


def exact_scaled_multiplier(
    q: Rational, delta: Rational, rates: Sequence[Rational]
) -> Fraction:
    """Evaluate the order-``m`` scaled pole-killing multiplier exactly."""
    q_value = Fraction(q)
    delta_value = Fraction(delta)
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    if delta_value <= 0:
        raise ValueError("delta must be positive")
    order = len(rational_rates) - 1
    denominator = math.prod(
        (q_value + rate * delta_value for rate in rational_rates),
        start=Fraction(1),
    )
    return (q_value - delta_value) ** order / denominator


def exact_anchored_scaled_multiplier(
    q: Rational,
    delta: Rational,
    rates: Sequence[Rational],
    anchor: Rational = 1,
) -> Fraction:
    """Evaluate the scaled multiplier with a general positive anchor."""
    q_value = Fraction(q)
    delta_value = Fraction(delta)
    anchor_value = Fraction(anchor)
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    if delta_value <= 0 or anchor_value <= 0:
        raise ValueError("delta and anchor must be positive")
    order = len(rational_rates) - 1
    denominator = math.prod(
        (q_value + rate * delta_value for rate in rational_rates),
        start=Fraction(1),
    )
    return (q_value - anchor_value * delta_value) ** order / denominator


def exact_multi_anchor_scaled_multiplier(
    q: Rational,
    delta: Rational,
    rates: Sequence[Rational],
    anchors: Sequence[Anchor],
) -> Fraction:
    """Evaluate a scaled multiplier with several prescribed zero modes."""
    q_value = Fraction(q)
    delta_value = Fraction(delta)
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    if delta_value <= 0:
        raise ValueError("delta must be positive")
    parsed_anchors = _parse_anchors(anchors)
    if len(rational_rates) != 1 + sum(m for _, m in parsed_anchors):
        raise ValueError("the number of rates must be total zero order plus one")
    numerator = math.prod(
        (
            (q_value - anchor * delta_value) ** multiplicity
            for anchor, multiplicity in parsed_anchors
        ),
        start=Fraction(1),
    )
    denominator = math.prod(
        (q_value + rate * delta_value for rate in rational_rates),
        start=Fraction(1),
    )
    return numerator / denominator


def exact_endpoint_flat_scaled_multiplier(
    q: Rational,
    delta: Rational,
    rates: Sequence[Rational],
    notch_order: int,
    anchor: Rational = 1,
) -> Fraction:
    """Evaluate the scaled joint notch/endpoint-flat multiplier exactly."""
    order = _validate_nonnegative_integer(notch_order, "notch_order")
    rational_rates = _as_fractions(rates)
    if not rational_rates or order >= len(rational_rates):
        raise ValueError("notch_order must be smaller than the number of rates")
    flat_order = len(rational_rates) - order - 1
    q_value = Fraction(q)
    delta_value = Fraction(delta)
    anchor_value = Fraction(anchor)
    if delta_value <= 0 or anchor_value <= 0:
        raise ValueError("delta and anchor must be positive")
    denominator = math.prod(
        (q_value + rate * delta_value for rate in rational_rates),
        start=Fraction(1),
    )
    return (
        delta_value**flat_order
        * (q_value - anchor_value * delta_value) ** order
        / denominator
    )


def exact_endpoint_flat_fixed_singularity_multiplier(
    singularity_offset: Rational,
    delta: Rational,
    rates: Sequence[Rational],
    notch_order: int,
    anchor: Rational = 1,
) -> Fraction:
    """Evaluate an endpoint-flat filter on a fixed non-pole singularity."""
    offset = Fraction(singularity_offset)
    if offset == 0:
        raise ValueError("singularity_offset must be nonzero")
    return exact_endpoint_flat_scaled_multiplier(
        offset + Fraction(anchor) * Fraction(delta),
        delta,
        rates,
        notch_order,
        anchor,
    )


def exact_fixed_singularity_multiplier(
    singularity_offset: Rational,
    delta: Rational,
    rates: Sequence[Rational],
    anchor: Rational = 1,
) -> Fraction:
    r"""Evaluate a minimal filter on a fixed non-pole singularity.

    ``singularity_offset`` is ``rho-sigma_0``.  The corresponding Laplace
    frequency is ``q=rho-sigma_0+anchor*delta``, so the pole-killing
    multiplier is

        offset^m / product_j(offset + (anchor+a_j)*delta).

    For fixed nonzero offset this tends to ``1/offset`` as ``delta`` tends to
    zero, independently of the order and rates.
    """
    offset = Fraction(singularity_offset)
    delta_value = Fraction(delta)
    anchor_value = Fraction(anchor)
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    if offset == 0:
        raise ValueError("singularity_offset must be nonzero")
    if delta_value <= 0 or anchor_value <= 0:
        raise ValueError("delta and anchor must be positive")
    order = len(rational_rates) - 1
    denominator = math.prod(
        (
            offset + (anchor_value + rate) * delta_value
            for rate in rational_rates
        ),
        start=Fraction(1),
    )
    return offset**order / denominator


def exponential_kernel(
    z: float | mp.mpf,
    rates: Sequence[float | mp.mpf],
    coefficients: Sequence[float | mp.mpf] | None = None,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    """Evaluate the minimal exponential kernel at ``z``."""
    if coefficients is None:
        exact = minimal_anchored_exponential_coefficients(
            tuple(Fraction(str(rate)) for rate in rates),
            Fraction(str(anchor)),
        )
        coefficients = tuple(_as_mpf(value) for value in exact)
    if len(rates) != len(coefficients):
        raise ValueError("rates and coefficients must have equal length")
    z_value = mp.mpf(z)
    return mp.fsum(
        _as_mpf(coefficient) * mp.e ** (-_as_mpf(rate) * z_value)
        for rate, coefficient in zip(rates, coefficients, strict=True)
    )


def one_minus_derivative_kernel(
    z: float | mp.mpf,
    power: int,
    rates: Sequence[float | mp.mpf],
    coefficients: Sequence[float | mp.mpf] | None = None,
) -> mp.mpf:
    r"""Evaluate ``(1-d/dz)^power phi(z)`` for an exponential kernel."""
    return sigma_minus_derivative_kernel(
        z, power, rates, coefficients, anchor=1
    )


def sigma_minus_derivative_kernel(
    z: float | mp.mpf,
    power: int,
    rates: Sequence[float | mp.mpf],
    coefficients: Sequence[float | mp.mpf] | None = None,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Evaluate ``(anchor-d/dz)^power phi(z)``."""
    power = _validate_nonnegative_integer(power, "power")
    if coefficients is None:
        exact = minimal_anchored_exponential_coefficients(
            tuple(Fraction(str(rate)) for rate in rates),
            Fraction(str(anchor)),
        )
        coefficients = tuple(_as_mpf(value) for value in exact)
    z_value = _as_mpf(z)
    anchor_value = _as_mpf(anchor)
    if anchor_value <= 0:
        raise ValueError("anchor must be positive")
    return mp.fsum(
        _as_mpf(coefficient)
        * (anchor_value + _as_mpf(rate)) ** power
        * mp.e ** (-_as_mpf(rate) * z_value)
        for rate, coefficient in zip(rates, coefficients, strict=True)
    )


def moment_boundary_expansion(
    delta: float | mp.mpf,
    c: float | mp.mpf,
    constant: float | mp.mpf,
    discrepancy_moments: Sequence[float | mp.mpf],
    rates: Sequence[float | mp.mpf],
    coefficients: Sequence[float | mp.mpf] | None = None,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Evaluate the retained abstract boundary expansion.

    The formula is

        -C phi(c)
        - sum_k delta^(k+1)/k! (anchor-D)^(k+1)phi(c) K_k.
    """
    delta_value = mp.mpf(delta)
    c_value = mp.mpf(c)
    if delta_value <= 0 or c_value <= 0:
        raise ValueError("delta and c must be positive")
    if coefficients is None:
        exact = minimal_anchored_exponential_coefficients(
            tuple(Fraction(str(rate)) for rate in rates),
            Fraction(str(anchor)),
        )
        coefficients = tuple(_as_mpf(value) for value in exact)
    total = -_as_mpf(constant) * exponential_kernel(
        c_value, rates, coefficients, anchor=anchor
    )
    for index, moment in enumerate(discrepancy_moments):
        total -= (
            delta_value ** (index + 1)
            / mp.factorial(index)
            * sigma_minus_derivative_kernel(
                c_value,
                index + 1,
                rates,
                coefficients,
                anchor=anchor,
            )
            * _as_mpf(moment)
        )
    return total


def exponential_germ_surrogate(
    delta: float | mp.mpf,
    c: float | mp.mpf,
    regular_germ: Callable[[mp.mpf], float | mp.mpf],
    rates: Sequence[float | mp.mpf],
    coefficients: Sequence[float | mp.mpf] | None = None,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Evaluate the finite-mode Laurent-germ functional calculus.

    If ``H(w)`` is the regular germ of a centered Dirichlet transform, this
    returns

        [H(-delta*(anchor-D)) phi](c)
          = sum_j c_j exp(-a_j*c) H(-delta*(anchor+a_j)).

    Under rapid discrepancy decay this matches the hard-cutoff boundary
    response to every fixed algebraic order; it is not asserted to be exact.
    """
    delta_value = _as_mpf(delta)
    c_value = _as_mpf(c)
    anchor_value = _as_mpf(anchor)
    if coefficients is None:
        exact = minimal_anchored_exponential_coefficients(
            tuple(Fraction(str(rate)) for rate in rates),
            Fraction(str(anchor)),
        )
        coefficients = tuple(_as_mpf(value) for value in exact)
    return mp.fsum(
        _as_mpf(coefficient)
        * mp.e ** (-_as_mpf(rate) * c_value)
        * _as_mpf(
            regular_germ(-delta_value * (anchor_value + _as_mpf(rate)))
        )
        for rate, coefficient in zip(rates, coefficients, strict=True)
    )


def confluent_germ_surrogate(
    delta: float | mp.mpf,
    c: float | mp.mpf,
    order: int,
    rate: float | mp.mpf,
    germ_derivative: Callable[[int, mp.mpf], float | mp.mpf],
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Evaluate the exact Jordan/Laguerre form of the germ surrogate.

    ``germ_derivative(r, w)`` must return ``H^(r)(w)``.  Nilpotence of the
    derivative on degree-``order`` polynomials makes the displayed sum finite.
    """
    order = _validate_nonnegative_integer(order, "order")
    delta_value = _as_mpf(delta)
    c_value = _as_mpf(c)
    rate_value = _as_mpf(rate)
    anchor_value = _as_mpf(anchor)
    if rate_value < 0 or anchor_value <= 0:
        raise ValueError("rate must be nonnegative and anchor positive")
    scale = rate_value + anchor_value
    base = -delta_value * scale
    polynomial = mp.fsum(
        (-delta_value * scale) ** derivative_order
        / mp.factorial(derivative_order)
        * _as_mpf(germ_derivative(derivative_order, base))
        * mp.laguerre(
            order - derivative_order,
            derivative_order,
            scale * c_value,
        )
        for derivative_order in range(order + 1)
    )
    return mp.e ** (-rate_value * c_value) * polynomial


def confluent_laguerre_kernel(
    z: float | mp.mpf,
    order: int,
    rate: float | mp.mpf = 0,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Return the confluent order-``m`` kernel.

    Coalescing all ``m+1`` exponential rates at ``a`` gives

        exp(-a*z) L_m((anchor+a)z),

    whose Laplace transform is ``(s-anchor)^m/(s+a)^(m+1)``.
    """
    order = _validate_nonnegative_integer(order, "order")
    z_value = _as_mpf(z)
    rate_value = _as_mpf(rate)
    anchor_value = _as_mpf(anchor)
    if rate_value < 0:
        raise ValueError("rate must be nonnegative")
    if anchor_value <= 0:
        raise ValueError("anchor must be positive")
    return mp.e ** (-rate_value * z_value) * mp.laguerre(
        order, 0, (anchor_value + rate_value) * z_value
    )


def associated_laguerre_endpoint_flat_kernel(
    z: float | mp.mpf,
    notch_order: int,
    flat_order: int,
    rate: float | mp.mpf = 0,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Return the confluent joint notch/endpoint-flat normal form.

    The normalization is ``k^(flat_order)(0)=1`` and

        Laplace(k)(s) = (s-anchor)^notch_order
                        / (s+rate)^(notch_order+flat_order+1).
    """
    notch = _validate_nonnegative_integer(notch_order, "notch_order")
    flat = _validate_nonnegative_integer(flat_order, "flat_order")
    z_value = _as_mpf(z)
    rate_value = _as_mpf(rate)
    anchor_value = _as_mpf(anchor)
    if rate_value < 0 or anchor_value <= 0:
        raise ValueError("rate must be nonnegative and anchor positive")
    scale = rate_value + anchor_value
    normalization = mp.factorial(notch) / mp.factorial(notch + flat)
    return (
        normalization
        * z_value**flat
        * mp.e ** (-rate_value * z_value)
        * mp.laguerre(notch, flat, scale * z_value)
    )


def fractional_laguerre_endpoint_kernel(
    z: float | mp.mpf,
    notch_order: int,
    flatness: float | mp.mpf,
    rate: float | mp.mpf = 0,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Return the fractional endpoint-flat Laguerre normal form.

    For ``alpha=flatness>=0`` its Laplace transform is

        (s-anchor)^m / (s+rate)^(m+alpha+1),

    and near zero it is ``z^alpha/Gamma(alpha+1)``.  Integer ``alpha``
    specializes to :func:`associated_laguerre_endpoint_flat_kernel`.
    """
    notch = _validate_nonnegative_integer(notch_order, "notch_order")
    alpha = _as_mpf(flatness)
    z_value = _as_mpf(z)
    rate_value = _as_mpf(rate)
    anchor_value = _as_mpf(anchor)
    if alpha < 0:
        raise ValueError("flatness must be nonnegative")
    if rate_value < 0 or anchor_value <= 0:
        raise ValueError("rate must be nonnegative and anchor positive")
    scale = rate_value + anchor_value
    normalization = mp.factorial(notch) / mp.gamma(notch + alpha + 1)
    return (
        normalization
        * z_value**alpha
        * mp.e ** (-rate_value * z_value)
        * mp.laguerre(notch, alpha, scale * z_value)
    )


def fractional_laguerre_scaled_multiplier(
    q: float | mp.mpf,
    delta: float | mp.mpf,
    rate: float | mp.mpf,
    notch_order: int,
    flatness: float | mp.mpf,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    """Evaluate the scaled fractional-Laguerre multiplier."""
    notch = _validate_nonnegative_integer(notch_order, "notch_order")
    q_value = _as_mpf(q)
    delta_value = _as_mpf(delta)
    rate_value = _as_mpf(rate)
    alpha = _as_mpf(flatness)
    anchor_value = _as_mpf(anchor)
    if alpha < 0 or rate_value < 0:
        raise ValueError("flatness and rate must be nonnegative")
    if delta_value <= 0 or anchor_value <= 0:
        raise ValueError("delta and anchor must be positive")
    return (
        delta_value**alpha
        * (q_value - anchor_value * delta_value) ** notch
        / (q_value + rate_value * delta_value) ** (notch + alpha + 1)
    )


def compact_linear_pole_killer_parameter(
    support: float | mp.mpf,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Return ``lambda`` for a compact first-order pole killer.

    On ``0<=z<=T`` the kernel is

        (1-z/T) (1-lambda*z),

    and is zero outside.  ``lambda`` is chosen so that its Laplace transform
    vanishes at ``anchor``.
    """
    support_value = _as_mpf(support)
    anchor_value = _as_mpf(anchor)
    if support_value <= 0 or anchor_value <= 0:
        raise ValueError("support and anchor must be positive")
    first = mp.quad(
        lambda z: mp.e ** (-anchor_value * z) * (1 - z / support_value),
        [0, support_value],
    )
    second = mp.quad(
        lambda z: z
        * mp.e ** (-anchor_value * z)
        * (1 - z / support_value),
        [0, support_value],
    )
    return first / second


def compact_linear_pole_killer_kernel(
    z: float | mp.mpf,
    support: float | mp.mpf,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    """Evaluate the compact first-order pole-killing kernel."""
    z_value = _as_mpf(z)
    support_value = _as_mpf(support)
    if z_value < 0 or z_value > support_value:
        return mp.mpf(0)
    parameter = compact_linear_pole_killer_parameter(support_value, anchor)
    return (1 - z_value / support_value) * (1 - parameter * z_value)


def compact_linear_pole_killer_laplace(
    s: float | mp.mpf,
    support: float | mp.mpf,
    anchor: float | mp.mpf = 1,
) -> mp.mpf:
    """Numerically evaluate the compact kernel's entire Laplace transform."""
    s_value = _as_mpf(s)
    support_value = _as_mpf(support)
    parameter = compact_linear_pole_killer_parameter(support_value, anchor)
    return mp.quad(
        lambda z: mp.e ** (-s_value * z)
        * (1 - z / support_value)
        * (1 - parameter * z),
        [0, support_value],
    )


def _compact_unit_moment(
    alpha_left: mp.mpf,
    alpha_right: mp.mpf,
    decay: mp.mpf,
    power: int,
) -> mp.mpf:
    """Return an exponentially tilted beta moment on the unit interval."""
    first = alpha_left + power + 1
    second = alpha_right + 1
    return mp.beta(first, second) * mp.hyp1f1(
        first, first + second, -decay
    )


def _compact_guard_digits(
    support: mp.mpf,
    anchors: Sequence[tuple[mp.mpf, int]],
    dimension: int,
) -> int:
    """Choose guard digits for nearly confluent dimensionless anchors."""
    separation_loss = 0
    if len(anchors) > 1:
        scaled_separation = min(
            support * abs(left[0] - right[0])
            for index, left in enumerate(anchors)
            for right in anchors[index + 1 :]
        )
        if scaled_separation < 1:
            separation_loss = int(mp.ceil(-mp.log10(scaled_separation)))
    return 40 + 8 * dimension + (dimension + 1) * separation_loss


def compact_chebyshev_polynomial_coefficients(
    support: float | mp.mpf,
    anchors: Sequence[tuple[float | mp.mpf, int]],
    left_order: float | mp.mpf = 0,
    right_order: float | mp.mpf = 0,
    rate: float | mp.mpf = 0,
) -> tuple[mp.mpf, ...]:
    r"""Numerically construct the monic compact multi-notch polynomial.

    If ``M=sum multiplicities``, the returned ascending coefficients define
    the monic degree-``M`` dimensionless polynomial ``Q(x)`` whose exact
    mathematical counterpart satisfies

        integral_0^1 x^(left_order+j) (1-x)^right_order
            exp(-(rate+anchor_h)T*x) Q(x) dx = 0

    for every ``0 <= j < multiplicity_h``.  For distinct real anchors these
    functions form an extended Chebyshev system, so the mixed moment matrix
    is nonsingular and the exact ``Q`` has exactly ``M`` simple roots in
    ``(0,1)``.  The solve uses beta--hypergeometric moments, the scale-free
    coordinate ``x=v/T``, and guard digits.  It remains a numerical replay:
    callers should raise ``mp.mp.dps`` and inspect
    :func:`compact_chebyshev_notch_residuals` for ill-conditioned high orders.
    """
    support_value = _finite_mpf(support, "support")
    alpha_left = _finite_mpf(left_order, "left_order")
    alpha_right = _finite_mpf(right_order, "right_order")
    rate_value = _finite_mpf(rate, "rate")
    if support_value <= 0:
        raise ValueError("support must be positive")
    if alpha_left < 0 or alpha_right < 0 or rate_value < 0:
        raise ValueError("endpoint orders and rate must be nonnegative")

    parsed = _parse_numeric_anchors(anchors)

    conditions = tuple(
        (anchor, derivative_order)
        for anchor, multiplicity in parsed
        for derivative_order in range(multiplicity)
    )
    dimension = len(conditions)
    if dimension == 0:
        return (mp.mpf(1),)

    guard_digits = _compact_guard_digits(support_value, parsed, dimension)
    with mp.workdps(mp.mp.dps + guard_digits):
        matrix = mp.matrix(dimension, dimension)
        target = mp.matrix(dimension, 1)
        moment_cache: dict[tuple[mp.mpf, int], mp.mpf] = {}

        def moment(decay: mp.mpf, power: int) -> mp.mpf:
            key = (decay, power)
            if key not in moment_cache:
                moment_cache[key] = _compact_unit_moment(
                    alpha_left, alpha_right, decay, power
                )
            return moment_cache[key]

        for row, (anchor, derivative_order) in enumerate(conditions):
            decay = (rate_value + anchor) * support_value
            for column in range(dimension):
                matrix[row, column] = moment(
                    decay, derivative_order + column
                )
            target[row] = -moment(decay, derivative_order + dimension)
        solution = mp.lu_solve(matrix, target)
        return tuple(+solution[index] for index in range(dimension)) + (
            mp.mpf(1),
        )


def compact_chebyshev_notch_residuals(
    support: float | mp.mpf,
    anchors: Sequence[tuple[float | mp.mpf, int]],
    coefficients: Sequence[float | mp.mpf],
    left_order: float | mp.mpf = 0,
    right_order: float | mp.mpf = 0,
    rate: float | mp.mpf = 0,
) -> tuple[mp.mpf, ...]:
    """Return scale-free relative residuals for every notch condition."""
    support_value = _finite_mpf(support, "support")
    alpha_left = _finite_mpf(left_order, "left_order")
    alpha_right = _finite_mpf(right_order, "right_order")
    rate_value = _finite_mpf(rate, "rate")
    parsed = _parse_numeric_anchors(anchors)
    if support_value <= 0:
        raise ValueError("support must be positive")
    if alpha_left < 0 or alpha_right < 0 or rate_value < 0:
        raise ValueError("endpoint orders and rate must be nonnegative")
    polynomial = tuple(
        _finite_mpf(value, "coefficients") for value in coefficients
    )
    dimension = sum(multiplicity for _, multiplicity in parsed)
    if len(polynomial) != dimension + 1:
        raise ValueError("coefficient count must be total notch order plus one")
    if not any(coefficient != 0 for coefficient in polynomial):
        raise ValueError("coefficient vector must be nonzero")

    residuals: list[mp.mpf] = []
    for anchor, multiplicity in parsed:
        decay = (rate_value + anchor) * support_value
        for derivative_order in range(multiplicity):
            terms = tuple(
                coefficient
                * _compact_unit_moment(
                    alpha_left,
                    alpha_right,
                    decay,
                    derivative_order + power,
                )
                for power, coefficient in enumerate(polynomial)
            )
            scale = mp.fsum(abs(term) for term in terms)
            if scale == 0:
                raise ValueError("notch residual has zero normalization scale")
            residuals.append(abs(mp.fsum(terms)) / scale)
    return tuple(residuals)


def compact_chebyshev_pole_killer_kernel(
    z: float | mp.mpf,
    support: float | mp.mpf,
    anchors: Sequence[tuple[float | mp.mpf, int]],
    left_order: float | mp.mpf = 0,
    right_order: float | mp.mpf = 0,
    rate: float | mp.mpf = 0,
    coefficients: Sequence[float | mp.mpf] | None = None,
    validate_coefficients: bool = True,
) -> mp.mpf:
    r"""Evaluate the normalized fractional two-edge multi-notch kernel.

    The support convention is half-open.  The left coefficient is normalized
    to ``1/Gamma(left_order+1)`` so its positive-ray symbol starts with
    ``s^(-left_order-1)``.  Supplied coefficients are interpreted as a
    polynomial in ``x=z/support``.  By default their notch residuals are
    checked.  Set ``validate_coefficients=False`` only for a certificate
    already returned by :func:`compact_chebyshev_polynomial_coefficients`,
    typically to avoid repeating the check inside numerical quadrature.
    """
    z_value = _finite_mpf(z, "z")
    support_value = _finite_mpf(support, "support")
    alpha_left = _finite_mpf(left_order, "left_order")
    alpha_right = _finite_mpf(right_order, "right_order")
    rate_value = _finite_mpf(rate, "rate")
    if support_value <= 0:
        raise ValueError("support must be positive")
    if alpha_left < 0 or alpha_right < 0 or rate_value < 0:
        raise ValueError("endpoint orders and rate must be nonnegative")
    if type(validate_coefficients) is not bool:
        raise ValueError("validate_coefficients must be boolean")
    parsed = _parse_numeric_anchors(anchors)
    total_order = sum(multiplicity for _, multiplicity in parsed)
    supplied_coefficients = coefficients is not None
    if coefficients is None:
        coefficients = compact_chebyshev_polynomial_coefficients(
            support_value, anchors, alpha_left, alpha_right, rate_value
        )
    polynomial_coefficients = tuple(
        _finite_mpf(value, "coefficients") for value in coefficients
    )
    expected_length = 1 + total_order
    if len(polynomial_coefficients) != expected_length:
        raise ValueError("coefficient count must be total notch order plus one")
    left_coefficient = support_value**alpha_right * polynomial_coefficients[0]
    if left_coefficient == 0:
        raise ValueError("the polynomial must have nonzero constant term")
    if supplied_coefficients and validate_coefficients:
        residuals = compact_chebyshev_notch_residuals(
            support_value,
            anchors,
            polynomial_coefficients,
            alpha_left,
            alpha_right,
            rate_value,
        )
        tolerance = 1000 * mp.sqrt(mp.eps)
        if any(residual > tolerance for residual in residuals):
            raise ValueError("supplied coefficients fail the notch conditions")
    if z_value < 0 or z_value >= support_value:
        return mp.mpf(0)
    coordinate = z_value / support_value
    polynomial = mp.polyval(tuple(reversed(polynomial_coefficients)), coordinate)
    normalization = 1 / (mp.gamma(alpha_left + 1) * left_coefficient)
    return (
        normalization
        * z_value**alpha_left
        * (support_value - z_value) ** alpha_right
        * mp.e ** (-rate_value * z_value)
        * polynomial
    )


def exact_confluent_scaled_multiplier(
    q: Rational,
    delta: Rational,
    rate: Rational,
    order: int,
    anchor: Rational = 1,
) -> Fraction:
    """Return the scaled multiplier of the confluent Laguerre kernel."""
    order = _validate_nonnegative_integer(order, "order")
    q_value = Fraction(q)
    delta_value = Fraction(delta)
    rate_value = Fraction(rate)
    anchor_value = Fraction(anchor)
    if rate_value < 0:
        raise ValueError("rate must be nonnegative")
    if delta_value <= 0 or anchor_value <= 0:
        raise ValueError("delta and anchor must be positive")
    return (q_value - anchor_value * delta_value) ** order / (
        q_value + rate_value * delta_value
    ) ** (order + 1)


def exact_associated_laguerre_scaled_multiplier(
    q: Rational,
    delta: Rational,
    rate: Rational,
    notch_order: int,
    flat_order: int,
    anchor: Rational = 1,
) -> Fraction:
    """Return the scaled multiplier of the associated-Laguerre kernel."""
    notch = _validate_nonnegative_integer(notch_order, "notch_order")
    flat = _validate_nonnegative_integer(flat_order, "flat_order")
    q_value = Fraction(q)
    delta_value = Fraction(delta)
    rate_value = Fraction(rate)
    anchor_value = Fraction(anchor)
    if rate_value < 0:
        raise ValueError("rate must be nonnegative")
    if delta_value <= 0 or anchor_value <= 0:
        raise ValueError("delta and anchor must be positive")
    return (
        delta_value**flat
        * (q_value - anchor_value * delta_value) ** notch
        / (q_value + rate_value * delta_value) ** (notch + flat + 1)
    )


def inverse_unstable_polynomial(
    delta: Rational,
    rates: Sequence[Rational],
    anchor: Rational = 1,
) -> tuple[Fraction, ...]:
    r"""Return coefficients of the unstable inverse impulse polynomial.

    If ``M(q)=(q-anchor*delta)^m/product_j(q+a_j delta)``, the principal part
    of ``1/M`` at ``q=anchor*delta`` has inverse Laplace transform

        exp(anchor*delta*t) * sum_{k=0}^{m-1} result[k] * t^k.

    Polynomial/Dirac terms from the improper rational quotient are omitted.
    """
    delta_value = Fraction(delta)
    anchor_value = Fraction(anchor)
    rational_rates = _as_fractions(rates)
    if not rational_rates:
        raise ValueError("at least one rate is required")
    if delta_value <= 0 or anchor_value <= 0:
        raise ValueError("delta and anchor must be positive")
    if min(rational_rates) < 0:
        raise ValueError("rates must be nonnegative")
    order = len(rational_rates) - 1
    if order == 0:
        return ()
    shifted = tuple(
        delta_value * (anchor_value + rate) for rate in rational_rates
    )
    # Ascending coefficients of product_j(h+shifted_j), in O(m^2) time.
    product_coefficients = [Fraction(1)]
    for shift in shifted:
        updated = [Fraction(0)] * (len(product_coefficients) + 1)
        for degree, coefficient in enumerate(product_coefficients):
            updated[degree] += shift * coefficient
            updated[degree + 1] += coefficient
        product_coefficients = updated
    t_coefficients = [Fraction(0)] * order
    for ell in range(order):
        t_power = order - ell - 1
        t_coefficients[t_power] = (
            product_coefficients[ell] / math.factorial(t_power)
        )
    return tuple(t_coefficients)


def inverse_bridge_leading_tail(
    delta: Rational,
    rates: Sequence[Rational],
    anchor: Rational = 1,
) -> Fraction:
    r"""Return the leading unstable coefficient for triangular inversion.

    For

        R(q) = product_j(q+a_j*delta) / (q^2 (q-anchor*delta)^m),

    the inverse Laplace transform has leading tail

        result * t^(m-1) exp(anchor*delta*t).
    """
    rational_rates = _as_fractions(rates)
    order = len(rational_rates) - 1
    if order < 1:
        raise ValueError("at least two rates are required")
    delta_value = Fraction(delta)
    anchor_value = Fraction(anchor)
    if delta_value <= 0 or anchor_value <= 0:
        raise ValueError("delta and anchor must be positive")
    if min(rational_rates) < 0:
        raise ValueError("rates must be nonnegative")
    numerator = delta_value ** (order - 1) * math.prod(
        (anchor_value + rate for rate in rational_rates), start=Fraction(1)
    )
    return numerator / (anchor_value**2 * math.factorial(order - 1))


def multiple_front_splitting_polynomial(
    constant: Rational,
    discrepancy_moments: Sequence[Rational],
) -> tuple[Fraction, ...]:
    r"""Return the leading displacement polynomial for a multiple front.

    If ``k`` has a zero of multiplicity ``m`` and ``c=c_0+d*delta``, then the
    leading boundary equation, after removing a nonzero common derivative, is

        C*d^m + m*sum_{r=0}^{m-1} (-1)^(r+1)
            binom(m-1,r) K_r d^(m-1-r) = 0.

    Coefficients are returned in ascending powers of ``d``.
    """
    moments = _as_fractions(discrepancy_moments)
    order = len(moments)
    if order < 1:
        raise ValueError("at least one moment is required")
    coefficients = [Fraction(0)] * (order + 1)
    coefficients[order] = Fraction(constant)
    for moment_order, moment in enumerate(moments):
        degree = order - 1 - moment_order
        coefficients[degree] += (
            order
            * (-1) ** (moment_order + 1)
            * math.comb(order - 1, moment_order)
            * moment
        )
    return tuple(coefficients)


def coefficient_signs(rates: Sequence[Rational]) -> tuple[int, ...]:
    """Return signs of the exact minimal coefficients."""
    signs: list[int] = []
    for coefficient in minimal_exponential_coefficients(rates):
        signs.append(1 if coefficient > 0 else -1 if coefficient < 0 else 0)
    return tuple(signs)


def main() -> None:
    for order in range(1, 6):
        rates = tuple(Fraction(index) for index in range(order + 1))
        coefficients = minimal_exponential_coefficients(rates)
        print(
            f"order={order} rates={rates} coefficients={coefficients} "
            f"signs={coefficient_signs(rates)}"
        )


if __name__ == "__main__":
    main()
