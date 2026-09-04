"""Exact audits for residual-block weighted ``S_4`` unconditionality.

The sharp Rademacher square-function estimate is elementary once residual
blocks are triangle matchings.  Passing from random block signs to the
all-plus operator is not: the difference is supported on nonzero color
determinants.  This module records that reduction and one reason the exact
integer tangent obstruction cannot be copied verbatim to the actual
prime-power shell.

Nothing here proves packet-free unconditionality.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import isqrt
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class RademacherPairingLedger:
    """The exact three-pairing expansion of a Rademacher fourth moment."""

    right_square: float
    left_square: float
    crossed_pairing: float
    repeated_correction: float
    expectation: float


@dataclass(frozen=True)
class FlatBinRademacherLedger:
    """Explicit constants in the diffuse-coefficient Rademacher bound."""

    maximum_degree: int
    support_size: int
    bin_constant: float
    coefficient_l2: float
    self_term_bound_per_orientation: float
    cross_term_bound_per_orientation: float
    square_function_bound_per_orientation: float
    rademacher_fourth_bound: float


def flat_bin_rademacher_bound(
    maximum_degree: int,
    support_size: int,
    coefficient_l2: float = 1.0,
    *,
    bin_constant: float = 4.0,
) -> FlatBinRademacherLedger:
    r"""Return a proved refined bound for one factor-comparable bin.

    The hypothesis encoded by ``bin_constant=K`` is

    ``||z||_infinity^2 <= K ||z||_2^2/M``.

    If the triple system is linear and has maximum hyperedge degree
    ``Delta``, then each of the left and right square functions is at most

    ``[12 K Delta/M + 2 Delta min(1,2 K Delta/M)] ||z||_2^4``.

    Consequently the Rademacher fourth moment is at most three times this
    quantity.  In exponent notation this is

    ``O_K(Delta min(1,Delta/M)) ||z||_2^4``.

    A factor-two magnitude bin has ``K<=4``.
    """

    degree = int(maximum_degree)
    support = int(support_size)
    norm = float(coefficient_l2)
    balance = float(bin_constant)
    if degree < 0 or support <= 0 or norm < 0 or balance <= 0:
        raise ValueError("invalid degree, support, norm, or bin constant")
    fourth_norm = norm**4
    self_bound = 12.0 * balance * degree / support * fourth_norm
    cross_bound = (
        2.0
        * degree
        * min(1.0, 2.0 * balance * degree / support)
        * fourth_norm
    )
    square_bound = self_bound + cross_bound
    return FlatBinRademacherLedger(
        maximum_degree=degree,
        support_size=support,
        bin_constant=balance,
        coefficient_l2=norm,
        self_term_bound_per_orientation=self_bound,
        cross_term_bound_per_orientation=cross_bound,
        square_function_bound_per_orientation=square_bound,
        rademacher_fourth_bound=3.0 * square_bound,
    )


def rademacher_pairing_ledger(
    matrices: Sequence[np.ndarray],
) -> RademacherPairingLedger:
    r"""Evaluate the exact sign-pairing identity.

    For ``S(eps)=sum_i eps_i A_i``, the four sign indices survive in the
    three pairings.  The all-equal terms occur three times and must be
    subtracted twice:

    ``E||S||_S4^4 = R + L + C - 2 U``.
    """

    if not matrices:
        return RademacherPairingLedger(0.0, 0.0, 0.0, 0.0, 0.0)
    arrays = [np.asarray(matrix, dtype=complex) for matrix in matrices]
    shape = arrays[0].shape
    if any(array.shape != shape for array in arrays):
        raise ValueError("all matrices must have one common shape")
    right = sum(
        (array.conj().T @ array for array in arrays),
        start=np.zeros((shape[1], shape[1]), dtype=complex),
    )
    left = sum(
        (array @ array.conj().T for array in arrays),
        start=np.zeros((shape[0], shape[0]), dtype=complex),
    )
    right_square = float(np.trace(right @ right).real)
    left_square = float(np.trace(left @ left).real)
    crossed = sum(
        np.trace(first.conj().T @ second @ first.conj().T @ second)
        for first in arrays
        for second in arrays
    )
    repeated = 2.0 * sum(
        float(
            np.trace(
                (array.conj().T @ array) @ (array.conj().T @ array)
            ).real
        )
        for array in arrays
    )
    expectation = right_square + left_square + float(crossed.real) - repeated
    return RademacherPairingLedger(
        right_square=right_square,
        left_square=left_square,
        crossed_pairing=float(crossed.real),
        repeated_correction=repeated,
        expectation=expectation,
    )


def block_pattern_survives_rademacher(labels: Sequence[int]) -> bool:
    """Return whether every block label has even multiplicity."""

    return all(multiplicity % 2 == 0 for multiplicity in Counter(labels).values())


@dataclass(frozen=True)
class ResidualExcessLedger:
    """Exact determinant identity and block-sign status of one rectangle."""

    q: int
    residuals: tuple[int, int, int, int]
    block_labels: tuple[int, int, int, int]
    color_determinant: int
    alternating_sum: int
    alternating_product: int
    determinant_identity_defect: int
    survives_rademacher: bool
    short_zero_mode_regime: bool


def residual_excess_ledger(
    q: int,
    rows: tuple[int, int],
    columns: tuple[int, int],
    colors: tuple[tuple[int, int], tuple[int, int]],
    *,
    block_width: int | None = None,
) -> ResidualExcessLedger:
    r"""Build the exact ledger behind the all-plus/random-sign difference.

    Residual order is ``(11,12,21,22)``.  With ``Q=q^3``, ``S`` the
    alternating residual sum, ``T`` the alternating residual product, and
    ``k=det(c_ij)``, the exact identity is

    ``Q*S + T = 64*k*a1*a2*b1*b2``.

    If ``k=0`` and ``2H^2<Q``, the two residual pairs coincide, so every
    width-block label occurs evenly.  Thus every term killed by block signs
    is necessarily in the nonzero-determinant sector.
    """

    modulus_root = int(q)
    if modulus_root <= 0:
        raise ValueError("q must be positive")
    width = modulus_root if block_width is None else int(block_width)
    if width <= 0:
        raise ValueError("block width must be positive")
    a1, a2 = (int(value) for value in rows)
    b1, b2 = (int(value) for value in columns)
    (c11, c12), (c21, c22) = colors
    entries = (
        (a1, b1, int(c11)),
        (a1, b2, int(c12)),
        (a2, b1, int(c21)),
        (a2, b2, int(c22)),
    )
    target = modulus_root**3
    residuals = tuple(8 * a * b * c - target for a, b, c in entries)
    r11, r12, r21, r22 = residuals
    alternating_sum = r11 + r22 - r12 - r21
    alternating_product = r11 * r22 - r12 * r21
    determinant = int(c11) * int(c22) - int(c12) * int(c21)
    defect = (
        target * alternating_sum
        + alternating_product
        - 64 * determinant * a1 * a2 * b1 * b2
    )
    labels = tuple(value // width for value in residuals)
    cap = max(abs(value) for value in residuals)
    short = 2 * cap * cap < target
    survives = block_pattern_survives_rademacher(labels)
    if defect:
        raise AssertionError("the determinant/residual identity failed")
    if determinant == 0 and short and not survives:
        raise AssertionError("a short zero determinant must survive block signs")
    return ResidualExcessLedger(
        q=modulus_root,
        residuals=residuals,
        block_labels=labels,
        color_determinant=determinant,
        alternating_sum=alternating_sum,
        alternating_product=alternating_product,
        determinant_identity_defect=defect,
        survives_rademacher=survives,
        short_zero_mode_regime=short,
    )


def _primes_up_to(limit: int) -> tuple[int, ...]:
    """Return the primes up to ``limit`` by an exact small sieve."""

    bound = int(limit)
    if bound < 2:
        return ()
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, isqrt(bound) + 1):
        if sieve[prime]:
            sieve[prime * prime : bound + 1 : prime] = b"\x00" * (
                (bound - prime * prime) // prime + 1
            )
    return tuple(index for index in range(2, bound + 1) if sieve[index])


def forced_prime_power_progression_step_divisor(length: int) -> int:
    r"""Return the primorial forced into a prime-power AP step.

    Suppose ``x_0,...,x_(L-1)`` is an arithmetic progression of positive
    prime powers with pairwise distinct prime bases.  For every prime
    ``p<=L/2``, if ``p`` did not divide the step, at least two progression
    terms would be divisible by ``p``.  Both would then be powers of the
    same base ``p``, a contradiction.  Hence

    ``prod_(p<=L/2) p | step``.
    """

    order = int(length)
    if order <= 0:
        raise ValueError("length must be positive")
    answer = 1
    for prime in _primes_up_to(order // 2):
        answer *= prime
    return answer


def prime_power_progression_step_passes(length: int, step: int) -> bool:
    """Check the necessary primorial divisibility from the AP lemma."""

    difference = abs(int(step))
    if difference == 0:
        return int(length) <= 1
    return difference % forced_prime_power_progression_step_divisor(length) == 0


@dataclass(frozen=True)
class CriticalTangentScaling:
    """An exact integer subsequence placing the tangent fixture at QP scale."""

    scale: int
    order: int
    center: int
    q: int
    degree_parameter: int
    center_condition_holds: bool


@dataclass(frozen=True)
class FanDeterminantCollisionLedger:
    """Equal-determinant endpoint quadruples forced by one defect fan."""

    fan_size: int
    determinant_cap: int
    pair_edges: int
    occupied_determinants: int
    maximum_determinant_multiplicity: int
    directed_partial_matching_certified: bool
    equal_determinant_edge_pairs: int
    disjoint_equal_determinant_edge_pairs: int
    distinct_endpoint_quadruples: int
    cauchy_disjoint_lower_bound: Fraction
    plucker_identities_certified: bool


def _determinant(first: tuple[int, int], second: tuple[int, int]) -> int:
    return int(first[0]) * int(second[1]) - int(first[1]) * int(second[0])


def fan_determinant_collision_ledger(
    completion_pairs: Sequence[tuple[int, int]],
    *,
    determinant_cap: int,
    shell_minimum: int,
    shell_maximum: int,
) -> FanDeterminantCollisionLedger:
    r"""Count the endpoint quadruples forced by determinant pigeonholing.

    The input points are completion pairs ``P_i=(a_i,b_i)`` in one fixed
    endpoint fan.  Actual all-distinct prime-power pairs are coprime.  If
    the shell diameter is below its minimum, a fixed signed determinant is
    a directed partial matching: for fixed ``P_i`` and ``k``, there is at
    most one ``P_j`` with ``det(P_i,P_j)=k``, and similarly backwards.

    With ``N`` fan points and ``|det(P_i,P_j)|<=K``, Cauchy forces

    ``Omega(N^4/K)``

    equal-determinant pairs once ``N^2>>K``.  Apart from ``O(N^2)`` adjacent
    pairs in the partial-matching paths, these use four distinct endpoints.
    Every such quadruple obeys the exact Pluecker identity

    ``k^2=Delta_13*Delta_24-Delta_14*Delta_23``.
    """

    points = tuple((int(a), int(b)) for a, b in completion_pairs)
    cap = int(determinant_cap)
    lower = int(shell_minimum)
    upper = int(shell_maximum)
    if len(points) < 2 or cap <= 0:
        raise ValueError("a fan needs two points and a positive determinant cap")
    if lower <= 0 or upper < lower or upper - lower >= lower:
        raise ValueError("the shell diameter must be below its minimum")
    if len(set(points)) != len(points):
        raise ValueError("fan completion pairs must be distinct")
    for first, second in points:
        if not lower <= first <= upper or not lower <= second <= upper:
            raise ValueError("a completion coordinate lies outside the shell")
        if np.gcd(first, second) != 1:
            raise ValueError("each completion pair must be coprime")

    by_determinant: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for first, second in combinations(range(len(points)), 2):
        value = _determinant(points[first], points[second])
        if value == 0 or abs(value) > cap:
            raise ValueError("a fan determinant is zero or outside the stated cap")
        by_determinant[value].append((first, second))

    directed_partial = True
    total_collisions = 0
    disjoint_collisions = 0
    quadruples: set[frozenset[int]] = set()
    plucker = True
    for value, edges in by_determinant.items():
        sources = [edge[0] for edge in edges]
        targets = [edge[1] for edge in edges]
        directed_partial &= len(sources) == len(set(sources))
        directed_partial &= len(targets) == len(set(targets))
        for first_edge, second_edge in combinations(edges, 2):
            total_collisions += 1
            i, j = first_edge
            k, ell = second_edge
            if len({i, j, k, ell}) < 4:
                continue
            disjoint_collisions += 1
            quadruples.add(frozenset((i, j, k, ell)))
            delta_ik = _determinant(points[i], points[k])
            delta_jell = _determinant(points[j], points[ell])
            delta_iell = _determinant(points[i], points[ell])
            delta_jk = _determinant(points[j], points[k])
            plucker &= value * value == (
                delta_ik * delta_jell - delta_iell * delta_jk
            )
    if not directed_partial:
        raise AssertionError("fixed determinant failed to be a directed partial matching")
    if not plucker:
        raise AssertionError("the equal-determinant Pluecker identity failed")

    edges = len(points) * (len(points) - 1) // 2
    possible_labels = 2 * cap
    # Total equal-label edge pairs are at least E^2/(2L)-E/2.  In a graph
    # with in/out degree at most one, at most E such pairs share a vertex.
    cauchy_disjoint = max(
        Fraction(0),
        Fraction(edges * edges, 2 * possible_labels) - Fraction(3 * edges, 2),
    )
    if Fraction(disjoint_collisions) < cauchy_disjoint:
        raise AssertionError("the determinant collision lower bound failed")
    return FanDeterminantCollisionLedger(
        fan_size=len(points),
        determinant_cap=cap,
        pair_edges=edges,
        occupied_determinants=len(by_determinant),
        maximum_determinant_multiplicity=max(
            (len(items) for items in by_determinant.values()), default=0
        ),
        directed_partial_matching_certified=True,
        equal_determinant_edge_pairs=total_collisions,
        disjoint_equal_determinant_edge_pairs=disjoint_collisions,
        distinct_endpoint_quadruples=len(quadruples),
        cauchy_disjoint_lower_bound=cauchy_disjoint,
        plucker_identities_certified=True,
    )


@dataclass(frozen=True)
class WeightedCompletionRecurrenceLedger:
    """Forced recurrent completion energy from excess over determinant mass."""

    trace_mass: float
    determinant_mass: float
    mean_completion_multiplicity: float
    mass_on_multiplicity_at_least_three_lower_bound: float
    ordered_recurrent_pair_mass_lower_bound: float
    ordered_distinct_quadruple_mass_lower_bound: float


def weighted_completion_recurrence_bounds(
    trace_mass: float, determinant_mass: float
) -> WeightedCompletionRecurrenceLedger:
    r"""Return consequences of ``F=sum_C m(C)w(C)`` and ``W=sum_C w(C)``.

    Cauchy gives

    ``sum_C (m(C))_2 w(C) >= F^2/W-F``.

    Also the part with ``m(C)<=2`` contributes at most ``2W``.  If
    ``lambda=F/W>=8``, thresholding at ``m>=lambda/2`` gives

    ``sum_C (m(C))_4 w(C) >=lambda^3 F/256``.

    The last expression counts ordered quadruples of distinct completions
    and is the entry point for the old exact volume-plane labels.
    """

    total = float(trace_mass)
    base = float(determinant_mass)
    if total < 0 or base <= 0:
        raise ValueError("trace mass must be nonnegative and determinant mass positive")
    ratio = total / base
    recurrent_mass = max(0.0, total - 2.0 * base)
    pair_mass = max(0.0, total * total / base - total)
    quadruple_mass = ratio**3 * total / 256.0 if ratio >= 8.0 else 0.0
    return WeightedCompletionRecurrenceLedger(
        trace_mass=total,
        determinant_mass=base,
        mean_completion_multiplicity=ratio,
        mass_on_multiplicity_at_least_three_lower_bound=recurrent_mass,
        ordered_recurrent_pair_mass_lower_bound=pair_mass,
        ordered_distinct_quadruple_mass_lower_bound=quadruple_mass,
    )


@dataclass(frozen=True)
class CriticalDefectFanExponentLedger:
    """The exact exponent gaps at the diffuse critical support."""

    randomized_budget: Fraction
    automatic_fan_threshold: Fraction
    close_endpoint_gap: Fraction
    endpoint_collision_quadruples: Fraction
    four_completion_plane_labels: Fraction
    fan_to_plane_label_gap: Fraction


@dataclass(frozen=True)
class PlaneLabelSquareFunctionLedger:
    """Exact all-plus/random-sign comparison for local volume-plane labels.

    Once an anchor triangle is fixed, every further completion has one
    integral volume label ``t``.  This ledger deliberately forgets all
    additional arithmetic and records exactly what randomizing those labels
    can prove.  It is therefore a hostile test for any argument which uses
    only the fixed-plane estimates and scalar ``t`` orthogonality.
    """

    point_count: int
    occupied_labels: int
    maximum_label_occupancy: int
    all_plus_square: int
    rademacher_square: int
    within_label_ordered_distinct_pairs: int
    cross_label_ordered_pairs: int
    unconditionality_ratio: Fraction


def plane_label_square_function_ledger(
    volume_labels: Sequence[int],
) -> PlaneLabelSquareFunctionLedger:
    r"""Return the exact scalar square-function ledger for plane labels.

    If ``r_t`` is the number of fourth completions in anchor plane ``t``,
    then

    ``(sum_t r_t)^2``

    is the all-plus square, while independent signs on the plane labels give

    ``E|sum_t eps_t r_t|^2=sum_t r_t^2``.

    The missing cross-plane term is exactly

    ``sum_(t!=u) r_t r_u``.

    In particular, bounded (or divisor-sized) occupancy of every fixed plane
    makes the ratio *larger*: it is at least ``N/max_t r_t``.  Thus fixed-
    plane conic bounds plus scalar label orthogonality cannot supply a
    global plane-packing theorem.
    """

    labels = tuple(int(label) for label in volume_labels)
    if not labels:
        raise ValueError("at least one volume label is required")
    counts = Counter(labels)
    point_count = len(labels)
    randomized = sum(value * value for value in counts.values())
    within = sum(value * (value - 1) for value in counts.values())
    all_plus = point_count * point_count
    cross = all_plus - randomized
    if point_count * (point_count - 1) != within + cross:
        raise AssertionError("within-plane and cross-plane pairs did not partition")
    return PlaneLabelSquareFunctionLedger(
        point_count=point_count,
        occupied_labels=len(counts),
        maximum_label_occupancy=max(counts.values()),
        all_plus_square=all_plus,
        rademacher_square=randomized,
        within_label_ordered_distinct_pairs=within,
        cross_label_ordered_pairs=cross,
        unconditionality_ratio=Fraction(all_plus, randomized),
    )


def critical_defect_fan_exponents() -> CriticalDefectFanExponentLedger:
    """Return the exponent ledger for ``M=D^(15/8)``."""

    return CriticalDefectFanExponentLedger(
        randomized_budget=Fraction(1, 8),
        automatic_fan_threshold=Fraction(7, 8),
        close_endpoint_gap=Fraction(3, 8),
        # H^4/D at H=D^(7/8).
        endpoint_collision_quadruples=Fraction(5, 2),
        four_completion_plane_labels=Fraction(15, 16),
        fan_to_plane_label_gap=Fraction(1, 16),
    )


def critical_tangent_scaling(scale: int) -> CriticalTangentScaling:
    r"""Take ``L=t^8`` and ``m=t^33``.

    Then ``D=100L^2`` is a constant multiple of ``q^(16/33)`` and the raw
    unconditionality loss is ``asymp L=q^(8/33)``.  This makes explicit that
    the integer tangent obstruction lies on the intended exponent scale.
    """

    parameter = int(scale)
    if parameter < 2:
        raise ValueError("scale must be at least two")
    order = parameter**8
    center = parameter**33
    q = 2 * center
    degree = 100 * order * order
    return CriticalTangentScaling(
        scale=parameter,
        order=order,
        center=center,
        q=q,
        degree_parameter=degree,
        center_condition_holds=center > 64 * order**3,
    )
