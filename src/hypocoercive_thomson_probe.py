#!/usr/bin/env python3
"""Fail-fast gates for two global-transport attacks on the R71 energy.

The first attack combines factor-assignment dissipation with a skew
arithmetic transport.  The finite Vaughan state is kept *before* grouping:

    (n,d,b,m),  n=d*b*m,  d,b>Y,

with weight ``mu(d)*Lambda(b)``.  On each fixed-product fiber the strongest
normalized reversible dissipator is the orthogonal projection away from the
constant vector.  We then give the transport every available prime dilation
in each of ``d,b,m`` as an independently controlled skew edge.  Closing the
dissipative row space under all those generators is stronger than choosing
one fixed linear combination of them.  A large remaining kernel therefore
kills this transport topology, although it does not rule out an unrelated
global coupling.

The genuinely noncommuting local alternative inside the Ward connected
channel is its mandatory factor-ratio twist.  It is not the physical phase
of the full grouped Vaughan field.  On the two assignments of ``p*q`` it has velocity
``+/- log(q/p)``.  The exact two-by-two bracket and generator gaps are
reported, together with the exact null fiber at ``p^2``.

The second attack is signed Thomson transport.  A positive incidence graph
realizes the ungrouped Vaughan coefficient exactly, but column orientations
do not affect its Laplacian.  Thomson minimization consequently forgets the
Mobius signs and separates over total products.  The probe also verifies the
finite divisor-poset zeta/Mobius inverse and the cutoff-independent Laurent
residue of the completed tail at the first zeta zero.

These are scoped mechanism tests, not evidence for or against RH.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import mpmath as mp
import numpy as np

from type2_block_mechanism_probe import _arithmetic_sieve
from ward_nonlocal_covariance_probe import (
    _center_parameters,
    _grouped_tail_coefficients,
    _terminal_quadrature,
    audit_nonlocal_covariance,
    compact_profile,
)


@dataclass(frozen=True)
class VaughanAssignment:
    product: int
    divisor: int
    mangoldt_index: int
    cofactor: int
    weight: float


@dataclass(frozen=True)
class DilationEdge:
    lower: int
    upper: int
    coordinate: str
    prime: int
    weight: float


def enumerate_vaughan_assignments(
    cutoff: int, limit: int
) -> tuple[VaughanAssignment, ...]:
    """Enumerate every pre-grouping tail assignment through ``limit``."""

    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    if limit <= cutoff * cutoff:
        raise ValueError("limit must exceed cutoff squared")
    mu, _, mangoldt, _ = _arithmetic_sieve(limit)
    states: list[VaughanAssignment] = []
    for divisor in range(cutoff + 1, limit + 1):
        if not mu[divisor]:
            continue
        for b_value in range(cutoff + 1, limit // divisor + 1):
            if not mangoldt[b_value]:
                continue
            base = divisor * b_value
            for cofactor in range(1, limit // base + 1):
                states.append(
                    VaughanAssignment(
                        base * cofactor,
                        divisor,
                        b_value,
                        cofactor,
                        mu[divisor] * mangoldt[b_value],
                    )
                )
    return tuple(states)


def group_assignment_weights(
    states: tuple[VaughanAssignment, ...], limit: int
) -> np.ndarray:
    """Push pre-grouping weights to their total products."""

    answer = np.zeros(limit + 1)
    for state in states:
        answer[state.product] += state.weight
    return answer


def _fibers(
    states: tuple[VaughanAssignment, ...],
) -> dict[int, list[int]]:
    answer: dict[int, list[int]] = {}
    for index, state in enumerate(states):
        answer.setdefault(state.product, []).append(index)
    return answer


def fiber_projection(states: tuple[VaughanAssignment, ...]) -> np.ndarray:
    """Return the strongest normalized within-product dissipator."""

    dimension = len(states)
    projection = np.zeros((dimension, dimension))
    for indices in _fibers(states).values():
        size = len(indices)
        block = np.eye(size) - np.ones((size, size)) / size
        projection[np.ix_(indices, indices)] = block
    return projection


def coordinate_dilation_edges(
    states: tuple[VaughanAssignment, ...], limit: int
) -> tuple[DilationEdge, ...]:
    """Return every available one-prime dilation in ``d,b,m``.

    Each edge is arithmetic: its upper state is obtained by multiplying
    exactly one coordinate by one prime while retaining a valid Vaughan
    assignment.  The logarithmic edge weight is immaterial for structural
    rank but records the natural scale generator.
    """

    _, _, _, prime_indicator = _arithmetic_sieve(limit)
    lookup = {
        (state.divisor, state.mangoldt_index, state.cofactor): index
        for index, state in enumerate(states)
    }
    coordinate_names = ("d", "b", "m")
    edges: list[DilationEdge] = []
    for lower, state in enumerate(states):
        values = (
            state.divisor,
            state.mangoldt_index,
            state.cofactor,
        )
        maximum_multiplier = limit // state.product
        for coordinate in range(3):
            for prime in range(2, maximum_multiplier + 1):
                if not prime_indicator[prime]:
                    continue
                target = list(values)
                target[coordinate] *= prime
                upper = lookup.get(tuple(target))
                if upper is not None and lower < upper:
                    edges.append(
                        DilationEdge(
                            lower,
                            upper,
                            coordinate_names[coordinate],
                            prime,
                            math.log(prime),
                        )
                    )
    return tuple(edges)


def skew_edge_generator(dimension: int, edge: DilationEdge) -> np.ndarray:
    """Return the real skew generator supported on one dilation edge."""

    generator = np.zeros((dimension, dimension))
    generator[edge.lower, edge.upper] = edge.weight
    generator[edge.upper, edge.lower] = -edge.weight
    return generator


def _orthonormal_row_basis(
    matrix: np.ndarray, relative_tolerance: float = 2.0e-11
) -> np.ndarray:
    if matrix.ndim != 2:
        raise ValueError("matrix must be two-dimensional")
    if not matrix.size:
        return np.empty((0, matrix.shape[1]))
    _, singular_values, right = np.linalg.svd(matrix, full_matrices=False)
    if not len(singular_values) or singular_values[0] == 0.0:
        return np.empty((0, matrix.shape[1]))
    rank = int(
        np.count_nonzero(
            singular_values > relative_tolerance * singular_values[0]
        )
    )
    return right[:rank]


def controlled_row_closure(
    dissipator: np.ndarray,
    edges: tuple[DilationEdge, ...],
) -> tuple[np.ndarray, tuple[int, ...]]:
    """Close ``row(S)`` under every available skew edge independently."""

    if dissipator.ndim != 2 or dissipator.shape[0] != dissipator.shape[1]:
        raise ValueError("dissipator must be square")
    dimension = dissipator.shape[0]
    basis = _orthonormal_row_basis(dissipator)
    ranks = [len(basis)]
    while True:
        candidates = [basis]
        for edge in edges:
            generator = skew_edge_generator(dimension, edge)
            candidates.append(basis @ generator)
        enlarged = _orthonormal_row_basis(np.vstack(candidates))
        if len(enlarged) == len(basis):
            break
        basis = enlarged
        ranks.append(len(basis))
    return basis, tuple(ranks)


def _uncontrolled_fraction(vector: np.ndarray, row_basis: np.ndarray) -> float:
    norm_squared = float(np.vdot(vector, vector).real)
    if norm_squared == 0.0:
        return 0.0
    controlled = row_basis.T.conj() @ (row_basis @ vector)
    remainder = vector - controlled
    return float(np.vdot(remainder, remainder).real / norm_squared)


@dataclass(frozen=True)
class HypocoerciveTransportAudit:
    scale: float
    cutoff: int
    step: float
    limit: int
    assignments: int
    product_fibers: int
    dilation_edges: int
    initial_rank: int
    closure_ranks: tuple[int, ...]
    closure_rank: int
    nullity: int
    active_products: tuple[int, ...]
    regrouping_error: float
    dissipator_projection_error: float
    maximum_skew_error: float
    raw_uncontrolled_fraction: float
    critical_uncontrolled_fraction: float
    coherent_raw_uncontrolled_fraction: float
    coherent_critical_uncontrolled_fraction: float


@dataclass(frozen=True)
class CutoffDiracAudit:
    scale: float
    cutoffs: tuple[int, ...]
    step: float
    quadrature_points: int
    vertex_dimension: int
    edge_dimension: int
    skew_error: float
    bracket_minimum_eigenvalue: float
    bracket_nullity: int
    smallest_positive_bracket_eigenvalue: float
    exact_cutoff_difference_norm: float
    approximate_cutoff_difference_norm: float
    euler_difference_norm: float
    source_identity_error: float
    common_carrier_residual: float


def audit_cutoff_dirac(
    scale: float = 25.0,
    cutoffs: tuple[int, ...] = (2, 3),
    step: float = 0.04,
    input_order: int = 1,
    macro_order: int = 1,
    gaussian_order: int = 16,
    carrier_exponent: complex = 0.1 + 14.0j,
) -> CutoffDiracAudit:
    """Build the exact completed cutoff-Dirac hypocoercive gate.

    A common quadrature is mandatory: otherwise cutoff-dependent sampling
    can create a fake difference.  The exact-head field is the same full
    von Mangoldt coboundary at every cutoff.  The explicit-center field
    differs only by its Euler evaluation defect.
    """

    if len(cutoffs) < 2 or any(value < 1 for value in cutoffs):
        raise ValueError("provide at least two positive cutoffs")
    if any(left >= right for left, right in zip(cutoffs, cutoffs[1:])):
        raise ValueError("cutoffs must be strictly increasing")
    if step <= 0.0 or input_order < 1 or macro_order < 1:
        raise ValueError("invalid step or order")
    coboundary_width = input_order * step
    if cutoffs[-1] ** 2 > scale * math.exp(-coboundary_width):
        raise ValueError("largest cutoff violates the support condition")

    logarithmic_center = math.log(scale)
    limit = math.ceil(scale * math.exp(coboundary_width)) + 2
    mu, _, mangoldt, _ = _arithmetic_sieve(limit)
    tails = {
        cutoff: _grouped_tail_coefficients(
            cutoff, limit, mu, mangoldt
        )
        for cutoff in cutoffs
    }
    relevant = {
        value for value in range(2, limit + 1) if mangoldt[value]
    }
    for tail in tails.values():
        relevant.update(int(value) for value in np.flatnonzero(tail))

    profile_knots = {
        index * step for index in range(input_order + 1)
    }
    profile_knots.update(
        index * step - coboundary_width
        for index in range(input_order + 1)
    )
    terminal_upper = macro_order * step
    breakpoints: set[float] = set()
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
    profiles = {
        value: compact_profile(
            shifted_scales,
            math.log(value),
            step,
            input_order,
            coboundary_width,
            1.0 / math.sqrt(value),
        )
        for value in relevant
    }

    j_zero = _center_parameters(
        cutoffs[0], step, input_order, mu, mangoldt
    )[0]
    full_atoms = np.zeros_like(shifts)
    for value in relevant:
        if mangoldt[value]:
            full_atoms += mangoldt[value] * profiles[value]
    pole = j_zero * (
        np.exp((shifted_scales + coboundary_width) / 2.0)
        - np.exp(shifted_scales / 2.0)
    )
    exact_field = full_atoms - pole

    approximate_fields: list[np.ndarray] = []
    euler_defects: list[np.ndarray] = []
    for cutoff in cutoffs:
        tail_values = np.zeros_like(shifts)
        for value in relevant:
            coefficient = tails[cutoff][value]
            if coefficient:
                tail_values += coefficient * profiles[value]
        local_j, p_value, q_value = _center_parameters(
            cutoff, step, input_order, mu, mangoldt
        )

        def center(values: np.ndarray) -> np.ndarray:
            return np.exp(values / 2.0) * (
                local_j - p_value * values - q_value
            )

        analytic_center = (
            center(shifted_scales + coboundary_width)
            - center(shifted_scales)
        )
        approximate = tail_values - analytic_center
        approximate_fields.append(approximate)
        euler_defects.append(approximate - exact_field)

    square_root_weights = np.sqrt(weights)
    exact_vertices = np.concatenate(
        [square_root_weights * exact_field for _ in cutoffs]
    )
    approximate_vertices = np.concatenate(
        [square_root_weights * field for field in approximate_fields]
    )
    euler_vertices = np.concatenate(
        [square_root_weights * field for field in euler_defects]
    )

    cutoff_incidence = np.zeros((len(cutoffs) - 1, len(cutoffs)))
    for index in range(len(cutoffs) - 1):
        cutoff_incidence[index, index] = -1.0
        cutoff_incidence[index, index + 1] = 1.0
    differential = np.kron(cutoff_incidence, np.eye(len(shifts)))
    vertex_dimension = differential.shape[1]
    edge_dimension = differential.shape[0]
    dissipator = np.zeros(
        (vertex_dimension + edge_dimension,) * 2
    )
    dissipator[vertex_dimension:, vertex_dimension:] = np.eye(
        edge_dimension
    )
    skew = np.block(
        [
            [
                np.zeros((vertex_dimension, vertex_dimension)),
                -differential.T,
            ],
            [
                differential,
                np.zeros((edge_dimension, edge_dimension)),
            ],
        ]
    )
    bracket = dissipator + skew @ dissipator @ skew.T
    bracket_values = np.linalg.eigvalsh(bracket)
    tolerance = 2.0e-11 * max(1.0, float(bracket_values[-1]))
    positive = bracket_values[bracket_values > tolerance]

    exact_difference = differential @ exact_vertices
    approximate_difference = differential @ approximate_vertices
    euler_difference = differential @ euler_vertices
    carrier_profile = square_root_weights * np.exp(
        carrier_exponent * shifted_scales
    )
    carrier = np.concatenate(
        [np.tile(carrier_profile, len(cutoffs)), np.zeros(edge_dimension)]
    )
    carrier_norm = float(np.linalg.norm(carrier))
    return CutoffDiracAudit(
        scale,
        cutoffs,
        step,
        len(shifts),
        vertex_dimension,
        edge_dimension,
        float(np.max(np.abs(skew + skew.T))),
        float(bracket_values[0]),
        int(np.count_nonzero(bracket_values <= tolerance)),
        float(positive[0]),
        float(np.linalg.norm(exact_difference)),
        float(np.linalg.norm(approximate_difference)),
        float(np.linalg.norm(euler_difference)),
        float(np.linalg.norm(approximate_difference - euler_difference)),
        float(np.linalg.norm(bracket @ carrier) / carrier_norm),
    )


def audit_hypocoercive_transport(
    scale: float = 59.0,
    cutoff: int = 4,
    step: float = 0.04,
    input_order: int = 1,
    macro_order: int = 1,
) -> HypocoerciveTransportAudit:
    """Run the strongest independently-controlled dilation closure."""

    base = audit_nonlocal_covariance(
        scale,
        cutoff,
        step,
        input_order,
        macro_order,
        spectral_frequencies=(0.0,),
    )
    limit = base.arithmetic_limit
    states = enumerate_vaughan_assignments(cutoff, limit)
    mu, _, mangoldt, _ = _arithmetic_sieve(limit)
    grouped = group_assignment_weights(states, limit)
    expected = _grouped_tail_coefficients(cutoff, limit, mu, mangoldt)
    regrouping_error = float(np.max(np.abs(grouped - expected)))

    dissipator = fiber_projection(states)
    projection_error = float(
        max(
            np.max(np.abs(dissipator - dissipator.T)),
            np.max(np.abs(dissipator @ dissipator - dissipator)),
        )
    )
    edges = coordinate_dilation_edges(states, limit)
    skew_error = max(
        (
            float(
                np.max(
                    np.abs(
                        skew_edge_generator(len(states), edge)
                        + skew_edge_generator(len(states), edge).T
                    )
                )
            )
            for edge in edges
        ),
        default=0.0,
    )
    controlled, ranks = controlled_row_closure(dissipator, edges)

    active = set(base.active_tail_product_values)
    raw = np.asarray(
        [state.weight if state.product in active else 0.0 for state in states]
    )
    critical = np.asarray(
        [
            state.weight / math.sqrt(state.product)
            if state.product in active
            else 0.0
            for state in states
        ]
    )

    def coherent(vector: np.ndarray) -> np.ndarray:
        answer = np.zeros_like(vector)
        for indices in _fibers(states).values():
            answer[indices] = float(np.mean(vector[indices]))
        return answer

    coherent_raw = coherent(raw)
    coherent_critical = coherent(critical)
    return HypocoerciveTransportAudit(
        scale,
        cutoff,
        step,
        limit,
        len(states),
        len(_fibers(states)),
        len(edges),
        ranks[0],
        ranks,
        len(controlled),
        len(states) - len(controlled),
        base.active_tail_product_values,
        regrouping_error,
        projection_error,
        skew_error,
        _uncontrolled_fraction(raw, controlled),
        _uncontrolled_fraction(critical, controlled),
        _uncontrolled_fraction(coherent_raw, controlled),
        _uncontrolled_fraction(coherent_critical, controlled),
    )


@dataclass(frozen=True)
class RatioFiberAudit:
    prime: int
    other_prime: int
    frequency: float
    assignments: int
    log_ratio: float
    twist_size: float
    bracket_eigenvalues: tuple[float, ...]
    generator_gap: float
    coherent_weight_fraction: float
    dissipator_rank: int
    bracket_rank: int


def _validate_prime(value: int) -> None:
    if value < 2:
        raise ValueError("prime must be at least two")
    _, _, _, indicator = _arithmetic_sieve(value)
    if not indicator[value]:
        raise ValueError(f"{value} is not prime")


def ratio_fiber_audit(
    prime: int,
    other_prime: int,
    frequency: float = 1.0,
) -> RatioFiberAudit:
    """Audit the Ward-channel factor-ratio bracket on ``p*q`` or ``p^2``."""

    _validate_prime(prime)
    _validate_prime(other_prime)
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    if prime == other_prime:
        return RatioFiberAudit(
            prime,
            other_prime,
            frequency,
            1,
            0.0,
            0.0,
            (0.0,),
            0.0,
            1.0,
            0,
            0,
        )

    logarithm = abs(math.log(other_prime / prime))
    twist = abs(frequency) * logarithm
    dissipator = np.asarray([[0.5, -0.5], [-0.5, 0.5]])
    skew = 1j * frequency * np.diag((-logarithm, logarithm))
    bracket = dissipator + skew.conj().T @ dissipator @ skew
    bracket_values = tuple(float(value) for value in np.linalg.eigvalsh(bracket))

    # The eigenvalues of S+A solve lambda^2-lambda+twist^2=0.
    if 2.0 * twist >= 1.0:
        gap = 0.5
    else:
        root = math.sqrt(1.0 - 4.0 * twist * twist)
        # Stable form of (1-root)/2 near twist=0.
        gap = 2.0 * twist * twist / (1.0 + root)

    x_value = math.log(prime)
    y_value = math.log(other_prime)
    coherent_fraction = (x_value + y_value) ** 2 / (
        2.0 * (x_value * x_value + y_value * y_value)
    )
    tolerance = 2.0e-12 * max(1.0, bracket_values[-1])
    return RatioFiberAudit(
        prime,
        other_prime,
        frequency,
        2,
        logarithm,
        twist,
        bracket_values,
        gap,
        coherent_fraction,
        1,
        sum(value > tolerance for value in bracket_values),
    )


def prime_pair_bottleneck(
    limit: int, frequency: float = 1.0
) -> RatioFiberAudit:
    """Return the closest consecutive-prime ratio in the upper half."""

    if limit < 8:
        raise ValueError("limit must be at least eight")
    _, _, _, indicator = _arithmetic_sieve(limit)
    primes = [
        value
        for value in range(max(2, limit // 2), limit + 1)
        if indicator[value]
    ]
    if len(primes) < 2:
        raise RuntimeError("upper half contains fewer than two primes")
    pairs = zip(primes, primes[1:])
    prime, other = min(pairs, key=lambda pair: math.log(pair[1] / pair[0]))
    return ratio_fiber_audit(prime, other, frequency)


def divisor_convolution_matrix(values: np.ndarray) -> np.ndarray:
    """Matrix of truncated Dirichlet convolution by ``values``."""

    limit = len(values) - 1
    matrix = np.zeros((limit, limit))
    for output in range(1, limit + 1):
        for input_value in range(1, output + 1):
            if output % input_value == 0:
                matrix[output - 1, input_value - 1] = values[
                    output // input_value
                ]
    return matrix


@dataclass(frozen=True)
class ThomsonIncidenceAudit:
    limit: int
    cutoff: int
    assignments: int
    mobius_inverse_error: float
    tail_regrouping_error: float
    vaughan_completion_error: float
    divergence_error: float
    orientation_laplacian_error: float
    canonical_flow_energy: float
    minimum_flow_energy: float
    pseudoinverse_energy: float
    fiber_formula_error: float
    grouped_coefficient_energy: float
    mellin_identity_error: float


def audit_thomson_incidence(
    limit: int = 30,
    cutoff: int = 2,
    mellin_point: complex = 1.3 + 0.7j,
) -> ThomsonIncidenceAudit:
    """Verify the natural positive Vaughan incidence and its collapse."""

    states = enumerate_vaughan_assignments(cutoff, limit)
    mu, _, mangoldt, _ = _arithmetic_sieve(limit)
    one = np.ones(limit + 1)
    one[0] = 0.0
    mu_array = np.asarray(mu, dtype=float)
    mangoldt_array = np.asarray(mangoldt, dtype=float)
    logarithm = np.zeros(limit + 1)
    logarithm[1:] = np.log(np.arange(1, limit + 1))

    zeta_matrix = divisor_convolution_matrix(one)
    mobius_matrix = divisor_convolution_matrix(mu_array)
    identity = np.eye(limit)
    mobius_inverse_error = float(
        max(
            np.max(np.abs(mobius_matrix @ zeta_matrix - identity)),
            np.max(np.abs(zeta_matrix @ mobius_matrix - identity)),
        )
    )

    mu_tail = mu_array.copy()
    mu_tail[: cutoff + 1] = 0.0
    lambda_tail = mangoldt_array.copy()
    lambda_tail[: cutoff + 1] = 0.0
    mu_head = mu_array - mu_tail
    lambda_head = mangoldt_array - lambda_tail
    tail_operator = (
        divisor_convolution_matrix(mu_tail)
        @ divisor_convolution_matrix(lambda_tail)
        @ zeta_matrix
    )
    head_operator = (
        divisor_convolution_matrix(mu_head)
        @ divisor_convolution_matrix(logarithm)
        + divisor_convolution_matrix(lambda_head)
        - divisor_convolution_matrix(mu_head)
        @ divisor_convolution_matrix(lambda_head)
        @ zeta_matrix
    )
    lambda_operator = divisor_convolution_matrix(mangoldt_array)
    basis_one = np.zeros(limit)
    basis_one[0] = 1.0
    grouped = _grouped_tail_coefficients(cutoff, limit, mu, mangoldt)
    tail_regrouping_error = float(
        np.max(np.abs(tail_operator @ basis_one - grouped[1:]))
    )
    completion_error = float(
        np.max(np.abs(tail_operator + head_operator - lambda_operator))
    )

    incidence = np.zeros((limit + 1, len(states)))
    unsigned_incidence = np.zeros_like(incidence)
    current = np.zeros(len(states))
    target = np.zeros(limit + 1)
    counts: dict[int, int] = {}
    for edge, state in enumerate(states):
        orientation = 1.0 if state.weight > 0.0 else -1.0
        incidence[state.product - 1, edge] = orientation
        incidence[limit, edge] = -orientation
        unsigned_incidence[state.product - 1, edge] = 1.0
        unsigned_incidence[limit, edge] = -1.0
        current[edge] = abs(state.weight) / math.sqrt(state.product)
        counts[state.product] = counts.get(state.product, 0) + 1
    target[:limit] = grouped[1:] / np.sqrt(np.arange(1, limit + 1))
    target[limit] = -math.fsum(float(value) for value in target[:limit])
    divergence_error = float(np.max(np.abs(incidence @ current - target)))
    orientation_error = float(
        np.max(
            np.abs(
                incidence @ incidence.T
                - unsigned_incidence @ unsigned_incidence.T
            )
        )
    )

    canonical_energy = float(np.dot(current, current))
    minimum_energy = math.fsum(
        float(target[product - 1] ** 2 / count)
        for product, count in counts.items()
    )
    laplacian = incidence @ incidence.T
    pseudoinverse_energy = float(target @ np.linalg.pinv(laplacian) @ target)
    grouped_energy = float(np.dot(target[:limit], target[:limit]))

    state_mellin = sum(
        state.weight * state.product ** (-mellin_point) for state in states
    )
    grouped_mellin = sum(
        grouped[value] * value ** (-mellin_point)
        for value in range(1, limit + 1)
    )
    return ThomsonIncidenceAudit(
        limit,
        cutoff,
        len(states),
        mobius_inverse_error,
        tail_regrouping_error,
        completion_error,
        divergence_error,
        orientation_error,
        canonical_energy,
        minimum_energy,
        pseudoinverse_energy,
        abs(minimum_energy - pseudoinverse_energy),
        grouped_energy,
        abs(state_mellin - grouped_mellin),
    )


@dataclass(frozen=True)
class LaurentResidueAudit:
    cutoffs: tuple[int, ...]
    epsilon: float
    residues: tuple[complex, ...]
    maximum_unit_residue_error: float


def audit_common_laurent_residue(
    cutoffs: tuple[int, ...] = (1, 2, 3, 5, 10),
    epsilon: float = 1.0e-6,
    dps: int = 45,
) -> LaurentResidueAudit:
    """Check ``(s-rho) A_Y(s) -> -1`` at the first simple zero."""

    if not cutoffs or min(cutoffs) < 1:
        raise ValueError("cutoffs must be positive")
    if epsilon <= 0.0:
        raise ValueError("epsilon must be positive")
    mu, _, mangoldt, _ = _arithmetic_sieve(max(cutoffs))
    with mp.workdps(dps):
        rho = mp.zetazero(1)
        displacement = mp.mpf(str(epsilon))
        point = rho + displacement
        zeta_value = mp.zeta(point)
        logarithmic_derivative = -mp.zeta(point, derivative=1) / zeta_value
        residues: list[complex] = []
        for cutoff in cutoffs:
            m_value = mp.fsum(
                mu[value] * mp.power(value, -point)
                for value in range(1, cutoff + 1)
            )
            l_value = mp.fsum(
                mangoldt[value] * mp.power(value, -point)
                for value in range(1, cutoff + 1)
            )
            tail = (1 - zeta_value * m_value) * (
                logarithmic_derivative - l_value
            )
            residues.append(complex(displacement * tail))
    maximum_error = max(abs(value + 1.0) for value in residues)
    return LaurentResidueAudit(
        cutoffs,
        epsilon,
        tuple(residues),
        maximum_error,
    )


def center_scale_generator() -> np.ndarray:
    """Generator on ``span(e^(R/2), R e^(R/2))`` in coefficient order."""

    return np.asarray([[0.5, 1.0], [0.0, 0.5]])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=float, default=59.0)
    parser.add_argument("--cutoff", type=int, default=4)
    parser.add_argument("--step", type=float, default=0.04)
    parser.add_argument(
        "--frequency", type=float, default=14.134725141734693
    )
    parser.add_argument(
        "--prime-limits",
        nargs="+",
        type=int,
        default=(100, 1000, 10000, 100000),
    )
    args = parser.parse_args()

    cutoff_dirac = audit_cutoff_dirac()
    print(
        "exact cutoff-Dirac gate: "
        f"Y={cutoff_dirac.cutoffs} nodes={cutoff_dirac.quadrature_points} "
        f"nullity={cutoff_dirac.bracket_nullity} "
        f"exact-difference={cutoff_dirac.exact_cutoff_difference_norm:.3g} "
        f"carrier-residual={cutoff_dirac.common_carrier_residual:.3g}"
    )
    transport = audit_hypocoercive_transport(
        args.scale, args.cutoff, args.step
    )
    print(
        "controlled dilation closure: "
        f"X={transport.scale:g} Y={transport.cutoff} "
        f"N={transport.limit} states={transport.assignments} "
        f"fibers={transport.product_fibers} edges={transport.dilation_edges}"
    )
    print(
        f"ranks={transport.closure_ranks} nullity={transport.nullity}; "
        f"uncontrolled raw={transport.raw_uncontrolled_fraction:.9%} "
        f"coherent={transport.coherent_raw_uncontrolled_fraction:.9%}"
    )
    print("factor-ratio bottlenecks:")
    for limit in args.prime_limits:
        ratio = prime_pair_bottleneck(limit, args.frequency)
        print(
            f"  P<={limit}: ({ratio.prime},{ratio.other_prime}) "
            f"log-ratio={ratio.log_ratio:.6g} "
            f"gap={ratio.generator_gap:.6g} "
            f"coherent={ratio.coherent_weight_fraction:.9%}"
        )
    square = ratio_fiber_audit(97, 97, args.frequency)
    print(
        f"prime-square p=97: bracket-rank={square.bracket_rank} "
        f"gap={square.generator_gap:g}"
    )

    thomson = audit_thomson_incidence()
    print(
        "Thomson incidence: "
        f"N={thomson.limit} Y={thomson.cutoff} "
        f"edges={thomson.assignments} "
        f"canonical={thomson.canonical_flow_energy:.12g} "
        f"minimum={thomson.minimum_flow_energy:.12g} "
        f"grouped-L2={thomson.grouped_coefficient_energy:.12g}"
    )
    residue = audit_common_laurent_residue()
    print(
        "Laurent residues: "
        + ", ".join(
            f"Y={cutoff}:{value.real:+.8f}{value.imag:+.2g}i"
            for cutoff, value in zip(residue.cutoffs, residue.residues)
        )
    )


if __name__ == "__main__":
    main()
