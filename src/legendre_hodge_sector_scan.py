"""Low-old-sector Hodge contraction in compact Legendre bump spaces.

This is an independent-basis companion to ``hodge_sector_scan.py``.  The
old interval and the two collar components use the smooth polynomial bump
bases from ``event_cross_ratio.py``; no hat basis or hat Gram matrix enters.
The Weil form is assembled from its Fourier multiplier, so the exact fact
that a newly activated shift has no old--old overlap is also reported as the
``shell_isometry_error`` truncation diagnostic.

For the enlarged Weil block ``[[A,X],[X*,C]]`` and Hodge trace ``T``, the
row contraction is

    X* A^-1 X + T* T <= C.

After eliminating all old modes above ``low_count``, the script reports the
largest generalized eigenvalue of the remaining low-mode cost against the
remaining collar budget.  Values below one are positive finite-section
evidence only; neither frequency truncation nor quadrature is certified.
"""
from __future__ import annotations

import argparse
import math

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from scipy.linalg import eigvalsh as generalized_eigvalsh
from scipy.special import digamma, spherical_jn

from event_cross_ratio import combined_basis, prime_powers, weil_matrix
from hodge_event_scan import event_catalog
from incidence_poincare_ratio import degree_deficit
from legendre_hodge_crosscheck import relative_coordinates


_GL_CACHE: dict[int, tuple[np.ndarray, np.ndarray]] = {}


def _gl_rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    if order not in _GL_CACHE:
        _GL_CACHE[order] = leggauss(order)
    return _GL_CACHE[order]


def _interval_spec(left: float, right: float, degree: int,
                   smooth_power: int, xquad: int):
    """Return data needed to evaluate one whitened polynomial bump block."""
    t, wt = _gl_rule(xquad)
    half = (right - left) / 2
    center = (right + left) / 2
    envelope = np.maximum(0.0, 1.0 - t * t) ** smooth_power
    raw = legvander(t, degree - 1) * envelope[:, None]
    gram = raw.T @ ((half * wt)[:, None] * raw)
    values, vectors = np.linalg.eigh((gram + gram.T) / 2)
    transform = vectors @ np.diag(values ** -0.5) @ vectors.T
    return (left, right, center, half, degree, transform)


def _evaluate_spec(spec, x: np.ndarray,
                   smooth_power: int) -> np.ndarray:
    _, _, center, half, degree, transform = spec
    t = (x - center) / half
    envelope = np.maximum(0.0, 1.0 - t * t) ** smooth_power
    return (legvander(t, degree - 1) * envelope[:, None]) @ transform


def _shift_adjacency_from_specs(specs, offsets: np.ndarray,
                                smooth_power: int,
                                shift: float) -> np.ndarray:
    dimension = int(offsets[-1])
    forward = np.zeros((dimension, dimension))
    for i, target in enumerate(specs):
        left_i, right_i, _, _, degree_i, _ = target
        for j, source in enumerate(specs):
            left_j, right_j, _, _, degree_j, _ = source
            left = max(left_i, left_j + shift)
            right = min(right_i, right_j + shift)
            if right <= left:
                continue
            quadrature = max(degree_i, degree_j) + 2 * smooth_power + 4
            t, wt = _gl_rule(quadrature)
            half = (right - left) / 2
            center = (right + left) / 2
            x = center + half * t
            target_values = _evaluate_spec(target, x, smooth_power)
            source_values = _evaluate_spec(source, x - shift,
                                           smooth_power)
            block = target_values.T @ (
                (half * wt)[:, None] * source_values)
            forward[offsets[i]:offsets[i + 1],
                    offsets[j]:offsets[j + 1]] = block
    return forward + forward.T


def exact_shift_adjacency(old_radius: float, new_radius: float,
                          old_degree: int, collar_degree: int,
                          smooth_power: int, xquad: int,
                          shift: float) -> np.ndarray:
    """Return ``U_shift + U_shift.T`` by exact polynomial quadrature.

    Here ``(U_shift)_ij = integral phi_i(x) phi_j(x-shift) dx``.
    Each integrand is polynomial on the relevant overlap, so the local
    Gauss rule is exact up to floating-point whitening error.
    """
    specs = [
        _interval_spec(-old_radius, old_radius, old_degree,
                       smooth_power, xquad),
        _interval_spec(-new_radius, -old_radius, collar_degree,
                       smooth_power, xquad),
        _interval_spec(old_radius, new_radius, collar_degree,
                       smooth_power, xquad),
    ]
    offsets = np.cumsum([0, old_degree, collar_degree,
                         collar_degree])
    return _shift_adjacency_from_specs(
        specs, offsets, smooth_power, shift)


def exact_prime_weil_matrix(old_radius: float, new_radius: float,
                            active: list[tuple[int, float]],
                            old_degree: int, collar_degree: int,
                            smooth_power: int, xquad: int,
                            xmax: float, dxi: float,
                            chunk: int) -> np.ndarray:
    """Assemble gamma/pole by Fourier and every prime shift in space."""
    if smooth_power == 0:
        matrix = plain_legendre_spatial_gamma_pole_matrix(
            old_radius, new_radius, old_degree, collar_degree,
            xquad)
    else:
        matrix = weil_matrix(
            old_radius, new_radius, [], old_degree, collar_degree,
            smooth_power, xquad, xmax, dxi, chunk)
    for n, logp in active:
        adjacency = exact_shift_adjacency(
            old_radius, new_radius, old_degree, collar_degree,
            smooth_power, xquad, math.log(n))
        matrix -= (logp / math.sqrt(n)) * adjacency
    return (matrix + matrix.T) / 2


def _plain_legendre_fourier_block(xi: np.ndarray,
                                  left: float, right: float,
                                  degree: int) -> np.ndarray:
    """Analytic Fourier transforms of an L2-normalized Legendre block."""
    length = right - left
    half = length / 2
    center = (right + left) / 2
    orders = np.arange(degree)
    z = 2 * math.pi * np.abs(xi) * half
    bessel = spherical_jn(orders[:, None], z[None, :]).T
    negative = np.where(xi < 0, -1.0, 1.0)
    parity = negative[:, None] ** orders[None, :]
    normalization = np.sqrt(length * (2 * orders + 1))
    phase = np.exp(-2j * math.pi * xi * center)
    order_phase = (-1j) ** orders
    return (phase[:, None] * bessel * parity
            * (normalization * order_phase)[None, :])


def plain_legendre_gamma_pole_matrix(old_radius: float,
                                     new_radius: float,
                                     old_degree: int,
                                     collar_degree: int,
                                     xquad: int, xmax: float,
                                     dxi: float, chunk: int) -> np.ndarray:
    """Gamma/pole matrix using exact transforms of plain polynomials.

    This avoids aliasing the 1/xi Fourier tails of zero-extended Legendre
    polynomials.  The only truncation is the explicit ``[-xmax,xmax]``
    frequency cutoff itself.
    """
    intervals = [
        (-old_radius, old_radius, old_degree),
        (-new_radius, -old_radius, collar_degree),
        (old_radius, new_radius, collar_degree),
    ]
    dimension = old_degree + 2 * collar_degree
    matrix = np.zeros((dimension, dimension))
    xis = np.arange(-xmax, xmax + dxi / 2, dxi)
    weights = np.full(len(xis), dxi)
    weights[[0, -1]] *= 0.5
    for start in range(0, len(xis), chunk):
        xi = xis[start:start + chunk]
        fourier = np.column_stack([
            _plain_legendre_fourier_block(xi, left, right, degree)
            for left, right, degree in intervals])
        symbol = (np.real(digamma(0.25 + 1j * math.pi * xi))
                  - math.log(math.pi))
        weighted_symbol = weights[start:start + chunk] * symbol
        matrix += np.real(
            fourier.conj().T
            @ (weighted_symbol[:, None] * fourier))

    # Gauss--Legendre evaluates the two exponential moment vectors to far
    # beyond the precision relevant here.
    x, wx, basis = combined_basis(
        old_radius, new_radius, old_degree, collar_degree, 0, xquad)
    pole_plus = (wx * np.exp(x / 2)) @ basis
    pole_minus = (wx * np.exp(-x / 2)) @ basis
    matrix += (np.outer(pole_plus, pole_minus)
               + np.outer(pole_minus, pole_plus))
    return (matrix + matrix.T) / 2


def _kernel_tail(start: float) -> float:
    total = 0.0
    index = 0
    while True:
        exponent = 2 * index + 0.5
        term = math.exp(-exponent * start) / exponent
        total += term
        if term < 1e-17:
            return total
        index += 1


def plain_legendre_spatial_gamma_pole_matrix(
        old_radius: float, new_radius: float,
        old_degree: int, collar_degree: int,
        xquad: int) -> np.ndarray:
    """Untruncated gamma/pole matrix from the Gauss digamma identity.

    The frequency tail of a zero-extended polynomial only decays like
    ``log(xi)/xi`` at the quadratic-form level.  Integrating in translation
    space avoids extrapolating that delicate tail.  On each interval between
    endpoint differences the shifted overlaps are polynomial in the shift;
    Gauss--Legendre therefore resolves the only non-polynomial factor, the
    analytic digamma kernel.
    """
    specs = [
        _interval_spec(-old_radius, old_radius, old_degree, 0, xquad),
        _interval_spec(-new_radius, -old_radius, collar_degree, 0, xquad),
        _interval_spec(old_radius, new_radius, collar_degree, 0, xquad),
    ]
    offsets = np.cumsum([0, old_degree, collar_degree,
                         collar_degree])
    dimension = int(offsets[-1])
    identity = np.eye(dimension)
    endpoints = [-new_radius, -old_radius, old_radius, new_radius]
    breakpoints = sorted({
        0.0, 2 * new_radius,
        *(right - left for left in endpoints for right in endpoints
          if right > left),
    })
    u_nodes, u_weights = _gl_rule(max(96, xquad))
    integral = np.zeros((dimension, dimension))
    for left, right in zip(breakpoints[:-1], breakpoints[1:]):
        half = (right - left) / 2
        center = (right + left) / 2
        shifts = center + half * u_nodes
        for shift, weight in zip(shifts, u_weights):
            adjacency = _shift_adjacency_from_specs(
                specs, offsets, 0, float(shift))
            sym_overlap = adjacency / 2
            kernel_times_shift = (
                shift * math.exp(-shift / 2)
                / (-math.expm1(-2 * shift)))
            integral += (half * weight * kernel_times_shift
                         * ((identity - sym_overlap) / shift))
    diagonal = (float(digamma(0.25)) - math.log(math.pi)
                + 2 * _kernel_tail(2 * new_radius))
    matrix = 2 * integral + diagonal * identity

    x, wx, basis = combined_basis(
        old_radius, new_radius, old_degree, collar_degree, 0, xquad)
    pole_plus = (wx * np.exp(x / 2)) @ basis
    pole_minus = (wx * np.exp(-x / 2)) @ basis
    matrix += (np.outer(pole_plus, pole_minus)
               + np.outer(pole_minus, pole_plus))
    return (matrix + matrix.T) / 2


def _largest_ratio(numerator: np.ndarray,
                   denominator: np.ndarray) -> float:
    numerator = (numerator + numerator.T) / 2
    denominator = (denominator + denominator.T) / 2
    if np.linalg.eigvalsh(denominator)[0] <= 0:
        return math.inf
    return float(generalized_eigvalsh(
        numerator, denominator,
        subset_by_index=[len(denominator) - 1,
                         len(denominator) - 1])[0])


def event_blocks(old_support: float, new_support: float,
                 old_degree: int, collar_degree: int,
                 smooth_power: int, xquad: int,
                 xmax: float, dxi: float, chunk: int):
    old_radius = old_support / 4
    new_radius = new_support / 4
    powers = prime_powers(math.ceil(math.exp(new_support / 2)) + 10)
    active_old = [(n, logp) for n, logp in powers
                  if 2 * math.log(n) < old_support]
    active_new = [(n, logp) for n, logp in powers
                  if 2 * math.log(n) < new_support]

    coordinates, coordinate_error = relative_coordinates(
        old_support, new_support, old_degree, collar_degree,
        smooth_power, xquad)
    x, wx, basis = combined_basis(
        old_radius, new_radius, old_degree, collar_degree,
        smooth_power, xquad)
    old_matrix = exact_prime_weil_matrix(
        old_radius, new_radius, active_old,
        old_degree, collar_degree, smooth_power,
        xquad, xmax, dxi, chunk)
    new_matrix = old_matrix.copy()
    old_names = {n for n, _ in active_old}
    for n, logp in active_new:
        if n in old_names:
            continue
        adjacency = exact_shift_adjacency(
            old_radius, new_radius, old_degree, collar_degree,
            smooth_power, xquad, math.log(n))
        new_matrix -= (logp / math.sqrt(n)) * adjacency
    old_form = coordinates.T @ old_matrix @ coordinates
    new_form = coordinates.T @ new_matrix @ coordinates

    old_dimension = old_degree - 2
    total_dimension = coordinates.shape[1]
    old_slice = slice(0, old_dimension)
    collar_slice = slice(old_dimension, total_dimension)
    old_scalar = float(degree_deficit(old_support))
    new_scalar = float(degree_deficit(new_support))
    event_scalar = new_scalar - old_scalar
    identity = np.eye(total_dimension)
    old_gradient = old_form + old_scalar * identity
    shell_gradient = new_form - old_form + event_scalar * identity

    incidence_old = old_gradient[old_slice, old_slice]
    shell_isometry_error = float(np.linalg.norm(
        shell_gradient[old_slice, old_slice]
        - event_scalar * np.eye(old_dimension), ord=2))
    old_cross = old_gradient[collar_slice, old_slice]
    shell_cross = shell_gradient[collar_slice, old_slice]
    edge_p = (math.sqrt(old_scalar) * old_cross
              @ np.linalg.inv(incidence_old))
    edge_q = shell_cross / math.sqrt(event_scalar)
    shell_ratio = math.sqrt(event_scalar / old_scalar)
    return_map = edge_q - shell_ratio * edge_p
    s_values, s_vectors = np.linalg.eigh(
        (incidence_old + incidence_old.T) / 2)
    tau_values = np.sqrt(s_values / (s_values + event_scalar))
    tau = (s_vectors * tau_values) @ s_vectors.T
    return_factor = tau @ return_map.T
    trace = (np.eye(old_dimension) - tau) @ return_factor

    # The activated translation is disjoint from the old interval, hence its
    # old--old block is *exactly* zero.  Enforce that exact support identity
    # here rather than letting a truncated Fourier representation of the new
    # prime term perturb eigenvalues as small as 1e-9.  The size of the
    # discarded perturbation remains visible as shell_isometry_error.
    old_weil = (old_form[old_slice, old_slice]
                + old_form[old_slice, old_slice].T) / 2
    cross = new_form[old_slice, collar_slice]
    collar = (new_form[collar_slice, collar_slice]
              + new_form[collar_slice, collar_slice].T) / 2

    # Reflection is evaluated independently on the quadrature nodes.  Each
    # local Gauss--Legendre grid is ordered left to right.
    q = xquad
    reflection_indices = np.concatenate([
        np.arange(q - 1, -1, -1),
        2 * q + np.arange(q - 1, -1, -1),
        q + np.arange(q - 1, -1, -1),
    ])
    reflection = basis.T @ (wx[:, None] * basis[reflection_indices])
    relative_reflection = coordinates.T @ reflection @ coordinates
    old_reflection = relative_reflection[old_slice, old_slice]
    collar_reflection = relative_reflection[collar_slice, collar_slice]
    reflection_error = float(np.linalg.norm(
        relative_reflection @ relative_reflection
        - np.eye(total_dimension), ord=2))
    return (old_weil, cross, collar, trace, incidence_old,
            old_reflection, collar_reflection, old_scalar, event_scalar,
            coordinate_error, reflection_error, shell_isometry_error)


def diagnose(old_support: float, new_support: float,
             old_degree: int, collar_degree: int,
             smooth_power: int, xquad: int,
             xmax: float, dxi: float, chunk: int,
             low_counts: list[int]) -> list[dict[str, float | int]]:
    (A, X, C, T, S, old_reflection, collar_reflection,
     old_scalar, event_scalar, basis_error, reflection_error,
     shell_isometry_error) = event_blocks(
        old_support, new_support, old_degree, collar_degree,
        smooth_power, xquad, xmax, dxi, chunk)
    a_values, vectors = np.linalg.eigh(A)
    if a_values[0] <= 0:
        raise ValueError(f"old Weil block is not positive: {a_values[0]}")
    diagonalization_error = float(np.linalg.norm(
        vectors.T @ S @ vectors
        - np.diag(a_values + old_scalar), ord=2))
    x_modes = vectors.T @ X
    t_modes = vectors.T @ T
    old_parities = np.diag(vectors.T @ old_reflection @ vectors)
    collar_parities, collar_vectors = np.linalg.eigh(
        (collar_reflection + collar_reflection.T) / 2)
    even_collar = collar_vectors[:, collar_parities > 0]
    odd_collar = collar_vectors[:, collar_parities < 0]
    cross_costs = [np.outer(row, row) / value
                   for row, value in zip(x_modes, a_values)]
    trace_costs = [np.outer(row, row) for row in t_modes]
    costs = [cross_cost + trace_cost for cross_cost, trace_cost
             in zip(cross_costs, trace_costs)]
    zero = np.zeros_like(C)
    total_cost = sum(costs, zero)
    total_cross_cost = sum(cross_costs, zero)
    total_trace_cost = sum(trace_costs, zero)
    ordinary_surplus = (C - total_cross_cost
                        + (C - total_cross_cost).T) / 2
    ordinary_surplus_minimum = float(
        np.linalg.eigvalsh(ordinary_surplus)[0])
    hodge_loss_ratio = _largest_ratio(
        total_trace_cost, ordinary_surplus)
    rows: list[dict[str, float | int]] = []

    def parity_ratio(cost: np.ndarray, budget: np.ndarray,
                     parity_basis: np.ndarray) -> float:
        if parity_basis.shape[1] == 0:
            return 0.0
        return _largest_ratio(parity_basis.T @ cost @ parity_basis,
                              parity_basis.T @ budget @ parity_basis)

    eigenvalue_slots = [
        float(a_values[j]) if j < len(a_values) else math.nan
        for j in range(5)]
    for requested in low_counts:
        low_count = min(max(0, requested), len(a_values))
        low_cost = sum(costs[:low_count], zero)
        low_cross = sum(cross_costs[:low_count], zero)
        low_trace = sum(trace_costs[:low_count], zero)
        high_cost = total_cost - low_cost
        after_high = (C - high_cost + (C - high_cost).T) / 2
        minimum = float(np.linalg.eigvalsh(after_high)[0])
        low_ratio = _largest_ratio(low_cost, after_high)
        rows.append({
            "old_degree": old_degree,
            "collar_degree": collar_degree,
            "smooth_power": smooth_power,
            "xquad": xquad,
            "xmax": xmax,
            "dxi": dxi,
            "low_count": low_count,
            "high_count": len(a_values) - low_count,
            "eigenvalue_0": eigenvalue_slots[0],
            "eigenvalue_1": eigenvalue_slots[1],
            "eigenvalue_2": eigenvalue_slots[2],
            "eigenvalue_3": eigenvalue_slots[3],
            "eigenvalue_4": eigenvalue_slots[4],
            "low_cutoff": (float(a_values[low_count - 1])
                           if low_count else 0.0),
            "next_eigenvalue": (float(a_values[low_count])
                                if low_count < len(a_values) else math.inf),
            "low_contraction_after_high": low_ratio,
            "low_reserve_after_high": (1 / low_ratio
                                       if low_ratio > 0 else math.inf),
            "low_cross_only_after_high": _largest_ratio(
                low_cross, after_high),
            "low_trace_only_after_high": _largest_ratio(
                low_trace, after_high),
            "low_even_contraction": parity_ratio(
                low_cost, after_high, even_collar),
            "low_odd_contraction": parity_ratio(
                low_cost, after_high, odd_collar),
            "low_even_count": int(np.sum(old_parities[:low_count] > 0)),
            "low_odd_count": int(np.sum(old_parities[:low_count] < 0)),
            "after_high_minimum": minimum,
            "total_row_ratio": _largest_ratio(total_cost, C),
            "ordinary_row_ratio": _largest_ratio(total_cross_cost, C),
            "hodge_trace_over_ordinary_surplus": hodge_loss_ratio,
            "hodge_domination_constant": (
                1 / hodge_loss_ratio if hodge_loss_ratio > 0
                else math.inf),
            "ordinary_row_surplus_minimum": ordinary_surplus_minimum,
            "full_row_surplus_minimum": float(np.linalg.eigvalsh(
                (C - total_cost + (C - total_cost).T) / 2)[0]),
            "basis_gram_error": basis_error,
            "reflection_error": reflection_error,
            "shell_isometry_error": shell_isometry_error,
            "diagonalization_error": diagonalization_error,
            "old_scalar": old_scalar,
            "event_scalar": event_scalar,
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-power", type=int, default=5)
    parser.add_argument("--old-degree", type=int, default=44)
    parser.add_argument("--collar-degrees", nargs="+", type=int,
                        default=[8, 12, 16])
    parser.add_argument("--smooth-power", type=int, default=2)
    parser.add_argument("--xquad", type=int, default=480)
    parser.add_argument("--xmax", type=float, default=140.0)
    parser.add_argument("--dxi", type=float, default=0.02)
    parser.add_argument("--chunk", type=int, default=256)
    parser.add_argument("--low-counts", nargs="+", type=int,
                        default=[1, 2, 4])
    args = parser.parse_args()

    catalog = event_catalog()
    positions = {n: index for index, (_, n, _, _) in enumerate(catalog)}
    position = positions[args.prime_power]
    event_support = catalog[position][3]
    old_support = (catalog[position - 1][3] + event_support) / 2
    new_support = (event_support + catalog[position + 1][3]) / 2
    header_printed = False
    for collar_degree in args.collar_degrees:
        rows = diagnose(
            old_support, new_support, args.old_degree, collar_degree,
            args.smooth_power, args.xquad, args.xmax, args.dxi,
            args.chunk, args.low_counts)
        fields = list(rows[0])
        if not header_printed:
            print(",".join(fields))
            header_printed = True
        for row in rows:
            print(",".join(
                str(row[field]) if isinstance(row[field], int)
                else f"{row[field]:.12e}"
                for field in fields), flush=True)


if __name__ == "__main__":
    main()
