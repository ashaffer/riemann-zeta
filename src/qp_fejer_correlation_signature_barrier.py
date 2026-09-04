"""Sharp inverse bounds and counterexamples for triangular Fejer correlation.

The height-one normalized Fejer kernel is

    P_H(theta)=sum_{|j|<H} (1/H)(1-|j|/H)e(j theta)
              =|sum_{0<=r<H} e(r theta)|^2/H^2.

A large scalar Gram entry ``P_H(theta)>=eta`` localizes ``theta`` only to
scale ``1/(H*sqrt(eta))``.  It does not force the individual supported
harmonics to align.  The half-lobe fixtures below make this sharp and also
survive all dyadic-prefix Fejer tests.
"""

from __future__ import annotations

import cmath
from dataclasses import dataclass
from fractions import Fraction
from math import pi, sin


def triangular_fejer_coefficients(order: int) -> dict[int, Fraction]:
    """Return the exact Fourier coefficients of the height-one kernel."""

    if order <= 0:
        raise ValueError("order must be positive")
    return {
        index: Fraction(order - abs(index), order * order)
        for index in range(-order + 1, order)
    }


def torus_distance(theta: float | Fraction) -> float:
    """Return distance to the nearest integer."""

    value = float(theta)
    return abs(value - round(value))


def normalized_fejer_kernel(order: int, theta: float | Fraction) -> float:
    """Evaluate the normalized Fejer kernel by its sine quotient."""

    if order <= 0:
        raise ValueError("order must be positive")
    distance = torus_distance(theta)
    if distance == 0.0:
        return 1.0
    return (sin(pi * order * distance) / (order * sin(pi * distance))) ** 2


def normalized_dirichlet_amplitude(order: int, theta: float | Fraction) -> complex:
    """Return the Gram entry of the uniform Fejer--Riesz feature block."""

    if order <= 0:
        raise ValueError("order must be positive")
    value = float(theta)
    return sum(cmath.exp(2j * pi * index * value) for index in range(order)) / order


def normalized_fejer_direct(order: int, theta: float | Fraction) -> complex:
    """Evaluate the same kernel from its exact triangular coefficient list."""

    return sum(
        float(weight) * cmath.exp(2j * pi * index * float(theta))
        for index, weight in triangular_fejer_coefficients(order).items()
    )


def exact_linear_grid_row_sum(order: int, modulus: int) -> Fraction:
    """Return the exact Fejer row sum on ``Z/modulus Z``.

    When ``order<=modulus``, Fourier orthogonality leaves only the zero
    triangular coefficient, so every row sum is exactly ``modulus/order``.
    """

    if order <= 0 or modulus < order:
        raise ValueError("require 0<H<=Q")
    return Fraction(modulus, order)


def numerical_linear_grid_row_sum(order: int, modulus: int, anchor: int = 0) -> float:
    """Numerically replay one row of the exact linear-grid identity."""

    if order <= 0 or modulus < order or not 0 <= anchor < modulus:
        raise ValueError("invalid order, modulus, or anchor")
    return sum(
        normalized_fejer_kernel(order, Fraction(index - anchor, modulus))
        for index in range(modulus)
    )


def numerical_abs_dirichlet_row_sum(
    order: int, modulus: int, anchor: int = 0
) -> float:
    """Return the absolute Schur row sum for the Fejer--Riesz square root."""

    if order <= 0 or modulus < order or not 0 <= anchor < modulus:
        raise ValueError("invalid order, modulus, or anchor")
    return sum(
        abs(normalized_dirichlet_amplitude(order, Fraction(index - anchor, modulus)))
        for index in range(modulus)
    )


def left_newton_response(Q: int, y: int) -> Fraction:
    """First projective Newton coefficient of the supported ``h=1`` probe.

    Here ``t=(Q+y)/(2Q)`` and

    ``Theta_Q(t)=Delta[2Q/(4(t+s/(2Q)))]_(s=0)
                =-1/[4*t*(t+1/(2Q))]``.

    The response is strictly monotone with derivative bounded above and
    below on every fixed reciprocal collar.
    """

    if Q <= 0 or abs(y) >= Q:
        raise ValueError("require Q>0 and |y|<Q")
    t = Fraction(Q + y, 2 * Q)
    return -Fraction(1, 4) / (t * (t + Fraction(1, 2 * Q)))


def nonlinear_newton_grid_row_sum(
    order: int, Q: int, y_values: list[int] | tuple[int, ...], anchor: int
) -> float:
    """Return one Fejer Gram row for the physical first-Newton responses."""

    if anchor not in y_values:
        raise ValueError("the anchor must belong to the supplied grid")
    base = left_newton_response(Q, anchor)
    return sum(
        normalized_fejer_kernel(order, left_newton_response(Q, y) - base)
        for y in y_values
    )


@dataclass(frozen=True)
class HalfLobeCounterexample:
    order: int
    odd_lobe: int
    theta: Fraction
    response: float
    lower_bound: float
    upper_bound: float
    anti_aligned_harmonic: int
    anti_aligned_distance: Fraction


def half_lobe_counterexample(order: int, odd_lobe: int) -> HalfLobeCounterexample:
    """Return a sharp side-lobe fixture with one maximally bad harmonic.

    Require odd ``L=odd_lobe`` to divide ``H=order`` and put
    ``theta=L/(2H)``.  Then

    ``4/(pi^2 L^2)<=P_H(theta)<=1/L^2``

    while the supported harmonic ``j=H/L`` has ``j*theta=1/2``.
    """

    if order <= 0 or odd_lobe <= 0 or odd_lobe % 2 == 0 or order % odd_lobe:
        raise ValueError("require a positive odd lobe dividing the order")
    theta = Fraction(odd_lobe, 2 * order)
    response = normalized_fejer_kernel(order, theta)
    lower = 4.0 / (pi * pi * odd_lobe * odd_lobe)
    upper = 1.0 / (odd_lobe * odd_lobe)
    harmonic = order // odd_lobe
    bad_distance = Fraction(1, 2)
    assert torus_distance(harmonic * theta) == 0.5
    assert lower <= response * (1.0 + 1.0e-12)
    assert response <= upper * (1.0 + 1.0e-12)
    return HalfLobeCounterexample(
        order=order,
        odd_lobe=odd_lobe,
        theta=theta,
        response=response,
        lower_bound=lower,
        upper_bound=upper,
        anti_aligned_harmonic=harmonic,
        anti_aligned_distance=bad_distance,
    )


def dyadic_prefix_responses(
    order: int, odd_lobe: int, depth: int
) -> tuple[float, ...]:
    """Return Fejer responses at all dyadic prefix scales.

    If ``2^depth|order``, every returned response is at least the full-scale
    response of the half-lobe fixture.  Thus simultaneous largeness of all
    dyadic-prefix correlations still does not imply harmonic alignment.
    """

    fixture = half_lobe_counterexample(order, odd_lobe)
    if depth < 0 or order % (2**depth):
        raise ValueError("require depth>=0 and 2^depth|order")
    responses = tuple(
        normalized_fejer_kernel(order // (2**level), fixture.theta)
        for level in range(depth + 1)
    )
    if any(value + 1.0e-12 < fixture.response for value in responses):
        raise AssertionError("the odd half-lobe should survive every dyadic prefix")
    return responses


def fejer_inverse_radius(order: int, threshold: float) -> float:
    """Sharp elementary radius forced by ``P_H(theta)>=threshold``."""

    if order <= 0 or not 0 < threshold <= 1:
        raise ValueError("require H>0 and 0<threshold<=1")
    return 1.0 / (2.0 * order * threshold**0.5)


def independent_factor_cluster_exponent(factor_count: int) -> Fraction:
    """Fixed-centre cluster exponent from ``factor_count`` independent kernels.

    If ``r`` comparable Fejer factors have product at least
    ``eta=D^(-7/48)``, their common one-parameter radius is
    ``H^(-1)*eta^(-1/(2r))``.  Since ``Q/H=D``, the resulting grid count has
    exponent ``1+7/(96r)``.
    """

    if factor_count <= 0:
        raise ValueError("factor_count must be positive")
    return Fraction(1, 1) + Fraction(7, 96 * factor_count)


def correlation_signature_exponent_ledger() -> dict[str, Fraction | int]:
    """Return the sharp project exponents for scalar/tensor Fejer inversion."""

    Q = Fraction(33, 16)
    H = Fraction(17, 16)
    eta = Fraction(7, 48)
    budget = Fraction(49, 48)
    scalar_radius_decay = H - eta / 2
    scalar_cluster = Q - scalar_radius_decay
    square_root_radius_decay = H - eta
    square_root_cluster = Q - square_root_radius_decay
    tensor_radius_decay = H - eta / 4
    tensor_cluster = Q - tensor_radius_decay
    desired_radius_decay = Q - budget
    scalar_miss = scalar_cluster - budget
    tensor_miss = tensor_cluster - budget
    required_scalar_eta_decay = 2 * (budget - (Q - H))
    required_tensor_eta_decay = 4 * (budget - (Q - H))
    minimum_independent_factors = 4
    weighted_block_cluster = Q - H
    weighted_block_margin = budget - weighted_block_cluster
    assert scalar_radius_decay == Fraction(95, 96)
    assert scalar_cluster == Fraction(103, 96)
    assert scalar_miss == Fraction(5, 96)
    assert square_root_radius_decay == Fraction(11, 12)
    assert square_root_cluster == Fraction(55, 48)
    assert tensor_radius_decay == Fraction(197, 192)
    assert tensor_cluster == Fraction(199, 192)
    assert tensor_miss == Fraction(1, 64)
    assert desired_radius_decay == Fraction(25, 24)
    assert required_scalar_eta_decay == Fraction(1, 24)
    assert required_tensor_eta_decay == Fraction(1, 12)
    assert independent_factor_cluster_exponent(3) > budget
    assert independent_factor_cluster_exponent(4) < budget
    assert weighted_block_cluster == 1
    assert weighted_block_margin == Fraction(1, 48)
    return {
        "Q": Q,
        "H": H,
        "eta_decay": eta,
        "cluster_budget": budget,
        "desired_radius_decay": desired_radius_decay,
        "scalar_radius_decay": scalar_radius_decay,
        "scalar_cluster": scalar_cluster,
        "scalar_miss": scalar_miss,
        "fejer_riesz_amplitude_radius_decay": square_root_radius_decay,
        "fejer_riesz_amplitude_cluster": square_root_cluster,
        "fejer_riesz_amplitude_miss": square_root_cluster - budget,
        "tensor_radius_decay": tensor_radius_decay,
        "tensor_cluster": tensor_cluster,
        "tensor_miss": tensor_miss,
        "required_scalar_eta_decay": required_scalar_eta_decay,
        "required_tensor_eta_decay": required_tensor_eta_decay,
        "minimum_independent_factors": minimum_independent_factors,
        "four_factor_cluster": independent_factor_cluster_exponent(4),
        "four_factor_margin": budget - independent_factor_cluster_exponent(4),
        "weighted_block_cluster": weighted_block_cluster,
        "weighted_block_margin": weighted_block_margin,
    }
