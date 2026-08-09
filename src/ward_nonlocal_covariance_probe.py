#!/usr/bin/env python3
"""Complete finite audit of the nonlocal Ward--innovation remainder.

This probe tests equation (7.1) of
``results/WARD-INNOVATION-SCREENING-CANDIDATE.md`` without deleting the
unequal-total-product or center terms.  For frozen equal Vaughan cutoffs
``U=V=Y`` it forms the grouped coefficient

    a_Y(n) = (mu_(>Y) * Lambda_(>Y) * 1)(n),

the order-``j`` fixed-step coboundary profiles, and the explicit Type-I
center ``Z_Y`` from the Vaughan reduction.  A terminal order-``m`` Markov
covariance is integrated against the exact Irwin--Hall density.  Gaussian
quadrature intervals are split at every arithmetic spline knot; the purely
discrete products are therefore integrated exactly up to floating-point
roundoff, while the exponential center is evaluated to high precision.

If ``K`` is the terminal covariance, the complete nonlocal remainder is

    G = K(Z,Z) - 2 sum_n a_n K(phi_n,Z)
        + sum_(n != r) a_n a_r K(phi_n,phi_r).

The code audits all natural orientations: ``G >= M``, ``G <= -M``, full
innovation at least the connected diagonal, and retained nonlocal remainder
at most minus the retained connected diagonal.  Here ``M`` is the one
missing ``Lambda*Lambda`` copy on distinct central semiprimes.

It also replaces the smooth Type-I evaluation by the exact finite head.
Then ``B-Z_exact`` is exactly the full von Mangoldt coboundary, making clear
which cancellations are merely polarization of ``F_Y=C_full+E_Y``.  This is
a finite mechanism falsifier, not an asymptotic estimate or proof about RH.
Its counterexamples exclude a cutoff-uniform algebraic sign law.  They do
not exclude an inequality restricted to a large-scale, growing-order
schedule with separately proved boundary and Euler-error estimates.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from numpy.polynomial.legendre import leggauss

from type2_block_mechanism_probe import _arithmetic_sieve


def bspline_cdf(values: np.ndarray, step: float, order: int) -> np.ndarray:
    """CDF of a sum of ``order`` uniforms on ``[0,step]``."""

    if step <= 0.0:
        raise ValueError("step must be positive")
    if order < 1:
        raise ValueError("order must be positive")
    scaled = np.asarray(values, dtype=float) / step
    answer = np.zeros_like(scaled)
    for index in range(order + 1):
        answer += (
            (-1.0) ** index
            * math.comb(order, index)
            * np.maximum(scaled - index, 0.0) ** order
        )
    answer /= math.factorial(order)
    return np.clip(answer, 0.0, 1.0)


def compact_profile(
    logarithmic_scale: np.ndarray,
    logarithm: float,
    step: float,
    order: int,
    coboundary_width: float,
    inverse_square_root: float,
) -> np.ndarray:
    """Evaluate the normalized arithmetic coboundary profile ``phi_n``."""

    gap = logarithmic_scale - logarithm
    return inverse_square_root * (
        bspline_cdf(gap + coboundary_width, step, order)
        - bspline_cdf(gap, step, order)
    )


def _terminal_quadrature(
    step: float,
    macro_order: int,
    gaussian_order: int,
    breakpoints: set[float],
) -> tuple[np.ndarray, np.ndarray]:
    """Integrate the sum-of-uniforms law, split at all supplied knots."""

    if macro_order < 1:
        raise ValueError("macro_order must be positive")
    if gaussian_order < 4:
        raise ValueError("gaussian_order must be at least four")
    upper = macro_order * step
    points = {0.0, upper}
    points.update(index * step for index in range(1, macro_order))
    points.update(value for value in breakpoints if 0.0 < value < upper)
    boundaries = sorted(points)
    base_nodes, base_weights = leggauss(gaussian_order)
    nodes: list[np.ndarray] = []
    weights: list[np.ndarray] = []
    factorial = math.factorial(macro_order - 1)
    for left, right in zip(boundaries, boundaries[1:]):
        if right - left <= 2.0e-14 * max(1.0, upper):
            continue
        midpoint = (left + right) / 2.0
        radius = (right - left) / 2.0
        local_nodes = midpoint + radius * base_nodes
        scaled = local_nodes / step
        segment = min(macro_order - 1, int(midpoint / step))
        density = np.zeros_like(local_nodes)
        for index in range(segment + 1):
            density += (
                (-1.0) ** index
                * math.comb(macro_order, index)
                * (scaled - index) ** (macro_order - 1)
            )
        density /= step * factorial
        nodes.append(local_nodes)
        weights.append(radius * base_weights * density)
    all_nodes = np.concatenate(nodes)
    all_weights = np.concatenate(weights)
    mass = math.fsum(float(value) for value in all_weights)
    if not math.isclose(mass, 1.0, rel_tol=2.0e-13, abs_tol=2.0e-13):
        raise RuntimeError(f"terminal quadrature mass is {mass!r}, not one")
    all_weights /= mass
    return all_nodes, all_weights


def _grouped_tail_coefficients(
    cutoff: int,
    limit: int,
    mu: list[int],
    mangoldt: list[float],
) -> np.ndarray:
    coefficients = np.zeros(limit + 1)
    active_b = [
        value
        for value in range(cutoff + 1, limit + 1)
        if mangoldt[value]
    ]
    for divisor in range(cutoff + 1, limit + 1):
        if not mu[divisor]:
            continue
        for b_value in active_b:
            product = divisor * b_value
            if product > limit:
                break
            coefficients[product : limit + 1 : product] += (
                mu[divisor] * mangoldt[b_value]
            )
    return coefficients


def _center_parameters(
    cutoff: int,
    step: float,
    order: int,
    mu: list[int],
    mangoldt: list[float],
) -> tuple[float, float, float]:
    """Return ``J0,P,Q`` in ``Z(R)=e^(R/2)(J0-P R-Q)-I0``."""

    m_one = math.fsum(mu[d] / d for d in range(1, cutoff + 1))
    m_one_prime = math.fsum(
        -mu[d] * math.log(d) / d for d in range(1, cutoff + 1)
    )
    l_one = math.fsum(
        mangoldt[b] / b for b in range(2, cutoff + 1)
    )
    half = 0.5
    one_step = -math.expm1(-step * half) / (step * half)
    j_zero = one_step**order / half
    logarithmic_derivative = (
        order * step / math.expm1(step * half)
        - (order + 1) / half
    )
    j_one = j_zero * logarithmic_derivative
    p_value = j_zero * m_one
    q_value = (
        j_one * m_one
        + j_zero * (m_one_prime - m_one * l_one)
    )
    return j_zero, p_value, q_value


def _covariance(
    left: np.ndarray, right: np.ndarray, weights: np.ndarray
) -> float:
    return float(
        np.dot(weights, left * right)
        - np.dot(weights, left) * np.dot(weights, right)
    )


@dataclass(frozen=True)
class NonlocalCovarianceAudit:
    scale: float
    cutoff: int
    step: float
    input_order: int
    macro_order: int
    coboundary_width: float
    arithmetic_limit: int
    active_tail_products: int
    active_central_semiprimes: int
    active_tail_product_values: tuple[int, ...]
    active_central_semiprime_values: tuple[int, ...]
    tail_diagonal_covariance: float
    missing_ward_covariance: float
    connected_covariance: float
    unequal_product_covariance: float
    center_covariance: float
    global_covariance_remainder: float
    full_innovation: float
    raw_energy: float
    retained_energy: float
    raw_nonlocal_remainder: float
    retained_nonlocal_remainder: float
    raw_connected_diagonal: float
    retained_connected_diagonal: float
    exact_head_global_remainder: float
    exact_full_innovation: float
    euler_innovation_correction: float
    coordinate_polarization_error: float
    covariance_closure_error: float
    positive_supply_margin: float
    negative_supply_margin: float
    innovation_dominates_connected_margin: float
    retained_cancels_connected_margin: float
    tail_diagonal_raw: float
    tail_diagonal_retained: float
    raw_unequal_product: float
    raw_center_completion: float
    retained_unequal_product: float
    retained_center_completion: float
    spectral_frequencies: tuple[float, ...]
    spectral_diagonal: tuple[float, ...]
    spectral_energy: tuple[float, ...]
    spectral_remainder: tuple[float, ...]


def audit_nonlocal_covariance(
    scale: float = 500.0,
    cutoff: int = 5,
    step: float = 0.4,
    input_order: int = 2,
    macro_order: int = 2,
    coboundary_width: float | None = None,
    gaussian_order: int = 16,
    spectral_frequencies: tuple[float, ...] = (0.0, 0.25, 0.5, 1.0),
) -> NonlocalCovarianceAudit:
    """Evaluate the complete finite version of equation (7.1).

    The cutoffs remain frozen over every terminal shift.  A common positive
    ``L2`` normalization of the compact window is omitted because it scales
    every reported quadratic quantity by the same factor and cannot change
    any sign audit.
    """

    if scale <= 4.0:
        raise ValueError("scale must exceed four")
    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    if step <= 0.0:
        raise ValueError("step must be positive")
    if input_order < 1 or macro_order < 1:
        raise ValueError("orders must be positive")
    if coboundary_width is None:
        coboundary_width = input_order * step
    if coboundary_width <= 0.0:
        raise ValueError("coboundary_width must be positive")

    logarithmic_center = math.log(scale)
    limit = math.ceil(scale * math.exp(coboundary_width)) + 2
    mu, _, mangoldt, prime_indicator = _arithmetic_sieve(limit)
    tail = _grouped_tail_coefficients(cutoff, limit, mu, mangoldt)

    # Split the terminal integral at every knot of every potentially active
    # arithmetic profile.  This retains all total products before energy is
    # formed and makes the polynomial part of the integration exact.
    breakpoints: set[float] = set()
    relevant = {
        int(value) for value in np.flatnonzero(tail)
    }
    relevant.update(
        value for value in range(2, limit + 1) if mangoldt[value]
    )
    profile_knots = {
        index * step for index in range(input_order + 1)
    }
    profile_knots.update(
        index * step - coboundary_width
        for index in range(input_order + 1)
    )
    terminal_upper = macro_order * step
    for value in relevant:
        base = logarithmic_center - math.log(value)
        for knot in profile_knots:
            shift = base - knot
            if 0.0 < shift < terminal_upper:
                breakpoints.add(shift)
    shifts, weights = _terminal_quadrature(
        step, macro_order, gaussian_order, breakpoints
    )
    shifted_scales = logarithmic_center - shifts
    frequency_array = np.asarray(spectral_frequencies, dtype=float)
    if frequency_array.ndim != 1 or not np.all(np.isfinite(frequency_array)):
        raise ValueError("spectral_frequencies must be a finite tuple")
    phases = np.exp(
        -1j * frequency_array[:, np.newaxis]
        * shifted_scales[np.newaxis, :]
    )

    j_zero, p_value, q_value = _center_parameters(
        cutoff, step, input_order, mu, mangoldt
    )

    def center(values: np.ndarray) -> np.ndarray:
        return np.exp(values / 2.0) * (
            j_zero - p_value * values - q_value
        )

    analytic_center = (
        center(shifted_scales + coboundary_width)
        - center(shifted_scales)
    )

    tail_values = np.zeros_like(shifts)
    full_atom_values = np.zeros_like(shifts)
    tail_diagonal_covariance = 0.0
    tail_diagonal_raw = 0.0
    tail_diagonal_retained = 0.0
    missing_covariance = 0.0
    connected_raw = 0.0
    connected_retained = 0.0
    active_tail_products = 0
    active_central_semiprimes = 0
    active_tail_product_values: list[int] = []
    active_central_semiprime_values: list[int] = []
    tail_transform = np.zeros(len(frequency_array), dtype=complex)
    spectral_diagonal = np.zeros(len(frequency_array))

    semiprime_weights: dict[int, float] = {}
    primes = [
        value
        for value in range(cutoff + 1, limit + 1)
        if prime_indicator[value]
    ]
    for index, prime in enumerate(primes):
        for other in primes[index + 1 :]:
            product = prime * other
            if product > limit:
                break
            semiprime_weights[product] = (
                2.0 * math.log(prime) * math.log(other)
            )

    for value in sorted(relevant):
        profile = compact_profile(
            shifted_scales,
            math.log(value),
            step,
            input_order,
            coboundary_width,
            1.0 / math.sqrt(value),
        )
        mean = float(np.dot(weights, profile))
        second_moment = float(np.dot(weights, profile * profile))
        variance = max(0.0, second_moment - mean * mean)
        coefficient = tail[value]
        if coefficient:
            tail_values += coefficient * profile
            profile_transform = phases @ (weights * profile)
            tail_transform += coefficient * profile_transform
            spectral_diagonal += coefficient**2 * np.abs(
                profile_transform
            ) ** 2
            tail_diagonal_covariance += coefficient**2 * variance
            tail_diagonal_raw += coefficient**2 * second_moment
            tail_diagonal_retained += coefficient**2 * mean**2
            if variance > 2.0e-16:
                active_tail_products += 1
                active_tail_product_values.append(value)
            ward_weight = semiprime_weights.get(value, 0.0)
            if ward_weight:
                missing_covariance += ward_weight * variance
                connected_raw += 2.0 * ward_weight * second_moment
                connected_retained += 2.0 * ward_weight * mean**2
                if variance > 2.0e-16:
                    active_central_semiprimes += 1
                    active_central_semiprime_values.append(value)
        if mangoldt[value]:
            full_atom_values += mangoldt[value] * profile

    pole = j_zero * (
        np.exp((shifted_scales + coboundary_width) / 2.0)
        - np.exp(shifted_scales / 2.0)
    )
    full_coboundary = full_atom_values - pole
    centered_tail = tail_values - analytic_center
    exact_center = tail_values - full_coboundary
    exact_centered_tail = tail_values - exact_center
    euler_defect = centered_tail - full_coboundary

    tail_variance = _covariance(tail_values, tail_values, weights)
    unequal_covariance = tail_variance - tail_diagonal_covariance
    center_covariance = (
        _covariance(analytic_center, analytic_center, weights)
        - 2.0 * _covariance(tail_values, analytic_center, weights)
    )
    global_remainder = unequal_covariance + center_covariance
    full_innovation = _covariance(centered_tail, centered_tail, weights)
    exact_full_innovation = _covariance(
        exact_centered_tail, exact_centered_tail, weights
    )
    exact_head_global_remainder = (
        exact_full_innovation - tail_diagonal_covariance
    )

    raw_energy = float(np.dot(weights, centered_tail * centered_tail))
    retained_energy = float(np.dot(weights, centered_tail) ** 2)
    tail_raw_energy = float(np.dot(weights, tail_values * tail_values))
    tail_retained_energy = float(np.dot(weights, tail_values) ** 2)
    raw_unequal = tail_raw_energy - tail_diagonal_raw
    raw_center_completion = float(
        np.dot(weights, analytic_center * analytic_center)
        - 2.0 * np.dot(weights, tail_values * analytic_center)
    )
    retained_unequal = tail_retained_energy - tail_diagonal_retained
    retained_center_completion = float(
        np.dot(weights, analytic_center) ** 2
        - 2.0
        * np.dot(weights, tail_values)
        * np.dot(weights, analytic_center)
    )
    raw_nonlocal = raw_energy - tail_diagonal_raw
    retained_nonlocal = retained_energy - tail_diagonal_retained
    center_transform = phases @ (weights * analytic_center)
    completed_transform = tail_transform - center_transform
    spectral_energy = np.abs(completed_transform) ** 2
    spectral_remainder = spectral_energy - spectral_diagonal
    connected_covariance = connected_raw - connected_retained
    euler_correction = (
        2.0 * _covariance(full_coboundary, euler_defect, weights)
        + _covariance(euler_defect, euler_defect, weights)
    )
    polarization_error = (
        full_innovation - exact_full_innovation - euler_correction
    )
    closure_error = global_remainder - (
        full_innovation - tail_diagonal_covariance
    )

    return NonlocalCovarianceAudit(
        scale,
        cutoff,
        step,
        input_order,
        macro_order,
        coboundary_width,
        limit,
        active_tail_products,
        active_central_semiprimes,
        tuple(active_tail_product_values),
        tuple(active_central_semiprime_values),
        tail_diagonal_covariance,
        missing_covariance,
        connected_covariance,
        unequal_covariance,
        center_covariance,
        global_remainder,
        full_innovation,
        raw_energy,
        retained_energy,
        raw_nonlocal,
        retained_nonlocal,
        connected_raw,
        connected_retained,
        exact_head_global_remainder,
        exact_full_innovation,
        euler_correction,
        polarization_error,
        closure_error,
        global_remainder - missing_covariance,
        -missing_covariance - global_remainder,
        full_innovation - connected_covariance,
        -connected_retained - retained_nonlocal,
        tail_diagonal_raw,
        tail_diagonal_retained,
        raw_unequal,
        raw_center_completion,
        retained_unequal,
        retained_center_completion,
        tuple(float(value) for value in frequency_array),
        tuple(float(value) for value in spectral_diagonal),
        tuple(float(value) for value in spectral_energy),
        tuple(float(value) for value in spectral_remainder),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=float, default=500.0)
    parser.add_argument("--cutoff", type=int, default=5)
    parser.add_argument("--step", type=float, default=0.4)
    parser.add_argument("--input-order", type=int, default=2)
    parser.add_argument("--macro-order", type=int, default=2)
    parser.add_argument("--gaussian-order", type=int, default=16)
    args = parser.parse_args()
    audit = audit_nonlocal_covariance(
        args.scale,
        args.cutoff,
        args.step,
        args.input_order,
        args.macro_order,
        gaussian_order=args.gaussian_order,
    )
    print(
        f"X={audit.scale:g} Y={audit.cutoff} h={audit.step:g} "
        f"j={audit.input_order} m={audit.macro_order} "
        f"products={audit.active_tail_products} "
        f"central_pq={audit.active_central_semiprimes}"
    )
    if audit.active_tail_products <= 20:
        print(f"active products: {audit.active_tail_product_values}")
        print(
            "central semiprimes: "
            f"{audit.active_central_semiprime_values}"
        )
    print(
        f"D={audit.tail_diagonal_covariance:.12g} "
        f"M={audit.missing_ward_covariance:.12g} "
        f"C={audit.connected_covariance:.12g}"
    )
    print(
        f"unequal={audit.unequal_product_covariance:+.12g} "
        f"center={audit.center_covariance:+.12g} "
        f"G={audit.global_covariance_remainder:+.12g} "
        f"Gamma={audit.full_innovation:.12g}"
    )
    print(
        f"margins: G>=M {audit.positive_supply_margin:+.12g}; "
        f"G<=-M {audit.negative_supply_margin:+.12g}; "
        f"Gamma>=C {audit.innovation_dominates_connected_margin:+.12g}; "
        f"Gret<=-Cret {audit.retained_cancels_connected_margin:+.12g}"
    )
    print(
        f"exact-head G={audit.exact_head_global_remainder:+.12g} "
        f"Gamma={audit.exact_full_innovation:.12g}; "
        f"Euler polarization={audit.euler_innovation_correction:+.3g}; "
        f"closure={audit.covariance_closure_error:+.3g}"
    )


if __name__ == "__main__":
    main()
