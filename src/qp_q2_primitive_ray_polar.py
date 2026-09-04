"""Exact primitive ``q^2`` ray polar and matching-stability identities.

The conductor-``q^2`` additive frequencies form a multiplicative
autocorrelation kernel.  For the aligned residual interval this kernel is
an exactly centered quotient count, not merely an estimate.  The module
also records the finite projection model for two residual triangle
matchings.  It is intended as an algebraic certificate; it does not claim
the missing transverse large-sieve bound.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import log, prod
from typing import Hashable, Iterable, Sequence

import numpy as np


def aligned_unit_residuals(q: int, degree: int) -> tuple[int, ...]:
    """Return signed representatives of the aligned unit residual set.

    The hypotheses ensure that reduction modulo ``q**2`` is injective on
    the returned interval.
    """

    modulus_root = int(q)
    radius_parameter = int(degree)
    if modulus_root <= 2 or modulus_root % 2 == 0:
        raise ValueError("q must be an odd integer greater than two")
    if radius_parameter <= 0 or 2 * radius_parameter >= modulus_root:
        raise ValueError("require 0 < 2D < q")
    radius = modulus_root * radius_parameter
    return tuple(
        value
        for value in range(-radius, radius + 1)
        if value and value % modulus_root
    )


def ray_pair_counts(q: int, degree: int, ratio: int) -> tuple[int, int]:
    r"""Return ``(N_(q^2)(t),N_q(t))`` for the residual quotient ``t``.

    Here

    ``N_m(t)=#{(r,s) in R^2:r=t*s (mod m)}``.
    """

    modulus_root = int(q)
    modulus = modulus_root**2
    unit_ratio = int(ratio) % modulus
    if unit_ratio % modulus_root == 0:
        raise ValueError("ratio must be a unit modulo q^2")
    residuals = aligned_unit_residuals(modulus_root, degree)
    residues_mod_q2 = {value % modulus for value in residuals}
    count_q2 = sum(
        (unit_ratio * value) % modulus in residues_mod_q2 for value in residuals
    )

    counts_mod_q = Counter(value % modulus_root for value in residuals)
    ratio_mod_q = unit_ratio % modulus_root
    count_q = sum(
        multiplicity * counts_mod_q[(ratio_mod_q * residue) % modulus_root]
        for residue, multiplicity in counts_mod_q.items()
    )
    return int(count_q2), int(count_q)


def full_ray_correlation(q: int, degree: int, ratio: int) -> Fraction:
    r"""Return the full additive-frequency ray correlation ``N_(q^2)/q^2``."""

    count_q2, _ = ray_pair_counts(q, degree, ratio)
    return Fraction(count_q2, int(q) ** 2)


def primitive_ray_correlation(q: int, degree: int, ratio: int) -> Fraction:
    r"""Return the exact primitive-frequency autocorrelation.

    If

    ``alpha_h=q^-2 sum_(r in R)e(-h*r/q^2)``, ``q not|h``, then this is

    ``sum_(q not|h) conjugate(alpha_h)*alpha_(t*h)``.
    """

    modulus_root = int(q)
    count_q2, count_q = ray_pair_counts(modulus_root, degree, ratio)
    return Fraction(count_q2, modulus_root**2) - Fraction(
        count_q, modulus_root**3
    )


def primitive_coarse_baseline(q: int, degree: int) -> Fraction:
    """Return the ratio-independent conductor-at-most-``q`` baseline."""

    modulus_root = int(q)
    radius_parameter = int(degree)
    return Fraction(
        4 * radius_parameter**2 * (modulus_root - 1), modulus_root**3
    )


def ramanujan_prime_square(q: int, value: int) -> int:
    """Return the Ramanujan sum ``c_(q^2)(value)`` for prime ``q``."""

    modulus_root = int(q)
    integer = int(value)
    if integer % (modulus_root**2) == 0:
        return modulus_root * (modulus_root - 1)
    if integer % modulus_root == 0:
        return -modulus_root
    return 0


def primitive_ray_correlation_via_ramanujan(
    q: int, degree: int, ratio: int
) -> Fraction:
    """Replay the primitive correlation from its Ramanujan-sum expansion."""

    modulus_root = int(q)
    unit_ratio = int(ratio) % (modulus_root**2)
    if unit_ratio % modulus_root == 0:
        raise ValueError("ratio must be a unit modulo q^2")
    residuals = aligned_unit_residuals(modulus_root, degree)
    numerator = sum(
        ramanujan_prime_square(modulus_root, first - unit_ratio * second)
        for first in residuals
        for second in residuals
    )
    return Fraction(numerator, modulus_root**4)


@dataclass(frozen=True)
class CommonCarrierRayWitness:
    """The exact quotient-ray identity for two edges sharing a carrier."""

    first_residual: int
    second_residual: int
    cross_difference: int
    expected_cross_difference: int

    @property
    def identity_holds(self) -> bool:
        return self.cross_difference == self.expected_cross_difference

    def vanishes_mod_q_squared(self, q: int) -> bool:
        return self.cross_difference % (int(q) ** 2) == 0


def common_carrier_ray_witness(
    q: int,
    carrier: int,
    first_row: int,
    first_colour: int,
    second_row: int,
    second_colour: int,
) -> CommonCarrierRayWitness:
    r"""Return

    ``rho_1*a_2*c_2-rho_2*a_1*c_1=q^3(a_1*c_1-a_2*c_2)``.
    """

    modulus_root = int(q)
    b = int(carrier)
    first_product = int(first_row) * int(first_colour)
    second_product = int(second_row) * int(second_colour)
    first_residual = 8 * b * first_product - modulus_root**3
    second_residual = 8 * b * second_product - modulus_root**3
    cross_difference = (
        first_residual * second_product - second_residual * first_product
    )
    expected = modulus_root**3 * (first_product - second_product)
    return CommonCarrierRayWitness(
        first_residual=first_residual,
        second_residual=second_residual,
        cross_difference=cross_difference,
        expected_cross_difference=expected,
    )


@dataclass(frozen=True)
class LogTrianglePolarIdentity:
    """Exact log-coordinate identity on one product triangle."""

    coordinates: tuple[float, float, float]
    coordinate_sum: float
    residual_log: float
    adjacency_quadratic: float
    polar_quadratic: float


def log_triangle_polar_identity(
    q: int, first: int, second: int, third: int
) -> LogTrianglePolarIdentity:
    r"""Replay the exact identities

    ``sum x_p=log(8abc/q^3)`` and
    ``x^T A_(K3)x=(sum x_p)^2-sum x_p^2``.
    """

    modulus_root = int(q)
    nodes = (int(first), int(second), int(third))
    coordinates = tuple(log(2 * node / modulus_root) for node in nodes)
    coordinate_sum = sum(coordinates)
    residual_log = log(8 * prod(nodes) / modulus_root**3)
    adjacency_quadratic = 2 * (
        coordinates[0] * coordinates[1]
        + coordinates[0] * coordinates[2]
        + coordinates[1] * coordinates[2]
    )
    polar_quadratic = coordinate_sum**2 - sum(
        coordinate**2 for coordinate in coordinates
    )
    return LogTrianglePolarIdentity(
        coordinates=coordinates,
        coordinate_sum=coordinate_sum,
        residual_log=residual_log,
        adjacency_quadratic=adjacency_quadratic,
        polar_quadratic=polar_quadratic,
    )


@dataclass(frozen=True)
class CoarsePrincipalWeightedBounds:
    """Schur/HS/Schatten bounds for the weighted coarse principal block."""

    hilbert_schmidt_squared_factor: Fraction
    operator_squared_factor: Fraction
    schatten_fourth_factor: Fraction


def coarse_principal_weighted_bounds(
    q: int,
    degree: int,
    shell_size: int,
    coefficient_support: int,
) -> CoarsePrincipalWeightedBounds:
    r"""Return exact coefficient factors for ``||z||_2=1`` and ``||W||_inf<=1``.

    The geometric input is that fixing any two shell variables leaves fewer
    than one integer choice for the third throughout ``|X|<q^2/2``.  Then

    ``||A_0||_HS^2 <= (2D/q)^2 |S|``,
    ``||A_0||_op^2 <= (2D/q)^2 |supp z|``.
    """

    modulus_root = int(q)
    radius_parameter = int(degree)
    node_count = int(shell_size)
    support_size = int(coefficient_support)
    if min(modulus_root, radius_parameter, node_count) <= 0:
        raise ValueError("q, D, and shell_size must be positive")
    if not 0 <= support_size <= node_count:
        raise ValueError("coefficient support must lie in the shell")
    density_squared = Fraction(4 * radius_parameter**2, modulus_root**2)
    hs_squared = density_squared * node_count
    operator_squared = density_squared * support_size
    return CoarsePrincipalWeightedBounds(
        hilbert_schmidt_squared_factor=hs_squared,
        operator_squared_factor=operator_squared,
        schatten_fourth_factor=hs_squared * operator_squared,
    )


def triangle_intersection_matrix(
    first: Sequence[Sequence[Hashable]],
    second: Sequence[Sequence[Hashable]],
) -> np.ndarray:
    """Return the shared-vertex matrix of two triple matchings.

    The function verifies that each input is a vertex matching.  If the
    union hypergraph is linear, every returned entry is zero or one.
    """

    left = [tuple(edge) for edge in first]
    right = [tuple(edge) for edge in second]
    for matching in (left, right):
        if any(len(edge) != 3 or len(set(edge)) != 3 for edge in matching):
            raise ValueError("every matching edge must contain three distinct nodes")
        flattened = [node for edge in matching for node in edge]
        if len(flattened) != len(set(flattened)):
            raise ValueError("each family must be a vertex matching")
    answer = np.empty((len(left), len(right)), dtype=np.int64)
    for row, edge in enumerate(left):
        edge_set = set(edge)
        for column, other in enumerate(right):
            answer[row, column] = len(edge_set.intersection(other))
    return answer


def normalized_triangle_projection_overlap(
    first: Sequence[Sequence[Hashable]],
    second: Sequence[Sequence[Hashable]],
) -> float:
    r"""Return ``||E_first E_second||=||M||/3`` for triangle averages."""

    intersection = triangle_intersection_matrix(first, second)
    if not intersection.size:
        return 0.0
    return float(np.linalg.norm(intersection, ord=2) / 3.0)


def near_regular_intersection_matrix(size: int) -> np.ndarray:
    """A connected almost-3-regular overlap with one deleted incidence.

    Its normalized norm is at least ``1-1/(3*size)``, yet it has no
    3-regular connected component.  It is realizable as the intersection
    graph of two triangle matchings by adding private boundary vertices.
    """

    dimension = int(size)
    if dimension < 5:
        raise ValueError("size must be at least five")
    matrix = np.zeros((dimension, dimension), dtype=np.int64)
    for row in range(dimension):
        for shift in (0, 1, 2):
            matrix[row, (row + shift) % dimension] = 1
    matrix[0, 0] = 0
    return matrix


def near_regular_overlap_lower_bound(size: int) -> Fraction:
    """Rayleigh lower bound for ``near_regular_intersection_matrix/3``."""

    dimension = int(size)
    if dimension < 5:
        raise ValueError("size must be at least five")
    return Fraction(3 * dimension - 1, 3 * dimension)


def vertex_multiset_product(edges: Iterable[Sequence[int]]) -> int:
    """Multiply every vertex occurrence in a family of triples."""

    return prod(int(node) for edge in edges for node in edge)


def identical_cover_product_identity(
    first: Sequence[Sequence[int]], second: Sequence[Sequence[int]]
) -> bool:
    """Return the exact product identity forced by an identical cover.

    If the two matchings cover the same vertex multiset, the product of
    their triple products is identical.  Consequently they cannot lie in
    two strictly ordered, disjoint product intervals.
    """

    if len(first) != len(second):
        return False
    first_nodes = Counter(int(node) for edge in first for node in edge)
    second_nodes = Counter(int(node) for edge in second for node in edge)
    return first_nodes == second_nodes and vertex_multiset_product(
        first
    ) == vertex_multiset_product(second)


@dataclass(frozen=True)
class HypotheticalDrzLedger:
    """Exponent ledger for the withdrawn Dong--Robles--Zeindler claim.

    This records only what the *stated* v1 bound would give under two
    hypothetical parameter substitutions.  It deliberately does not mark
    either substitution as a valid application: the paper was withdrawn,
    and the QP kernel has moving, nonseparable coefficients.
    """

    fixed_layer_bound: Fraction
    fixed_layer_dense_trivial: Fraction
    fixed_layer_dense_saving: Fraction
    top_dfi_balanced_saving: Fraction
    required_qp_saving: Fraction
    top_dfi_margin: Fraction


def hypothetical_drz_ledger(
    degree_exponent: Fraction = Fraction(16, 33),
    dfi_modulus_exponent: Fraction = Fraction(25, 33),
    required_saving: Fraction = Fraction(2, 33),
) -> HypotheticalDrzLedger:
    r"""Return the exact power ledger for the withdrawn v1 estimate.

    For the fixed-modulus inversion layer the only formal substitution is
    ``M=D,N=q``.  The stated v1 factor then has exponent

    ``1/3+(7/12) log_q(D)``,

    compared with the dense Cauchy exponent ``(1+log_q(D))/2``.  This is
    not useful for the actual layer, whose inverse-permutation norm is one.

    At the top DFI scale, the most optimistic balanced fantasy has both
    variables of length ``C`` and hence saving ``C^(-1/12)``.  The returned
    margin compares that formal saving with the QP target ``q^(-2/33)``.
    """

    d_exponent = Fraction(degree_exponent)
    c_exponent = Fraction(dfi_modulus_exponent)
    target = Fraction(required_saving)
    fixed_bound = Fraction(1, 3) + Fraction(7, 12) * d_exponent
    fixed_trivial = (1 + d_exponent) / 2
    fixed_saving = fixed_trivial - fixed_bound
    top_saving = c_exponent / 12
    return HypotheticalDrzLedger(
        fixed_layer_bound=fixed_bound,
        fixed_layer_dense_trivial=fixed_trivial,
        fixed_layer_dense_saving=fixed_saving,
        top_dfi_balanced_saving=top_saving,
        required_qp_saving=target,
        top_dfi_margin=top_saving - target,
    )


@dataclass(frozen=True)
class WrightFixedFactorLedger:
    """Power ledger for Wright's fixed-denominator-factor theorem.

    The fields use exponents of the ambient prime ``q``.  They distinguish
    the attractive but false ``R=1`` substitution from the literal
    reciprocity substitution, for which ``R=R_step*S_step``.
    """

    true_l2_trivial: Fraction
    literal_base_with_fixed_factor: Fraction
    literal_bracket_terms: tuple[Fraction, ...]
    literal_bound: Fraction
    literal_loss: Fraction
    no_fixed_factor_saving: Fraction
    required_qp_saving: Fraction
    no_fixed_factor_margin: Fraction
    scaled_inverse_m_exponent: Fraction
    scaled_inverse_n_squared_exponent: Fraction


def wright_fixed_factor_ledger(
    degree_exponent: Fraction = Fraction(16, 33),
    dfi_modulus_exponent: Fraction = Fraction(25, 33),
    fixed_factor_exponent: Fraction = Fraction(50, 33),
    required_saving: Fraction = Fraction(2, 33),
) -> WrightFixedFactorLedger:
    r"""Return the exact exponents in the two possible reciprocity maps.

    Wright's Theorem 2.1 has prefactor

    ``(AMN)^(1/2) R^(1/4)``

    and the five bracket terms recorded below.  In the QP top block,
    ``M=N=C``, ``A=D``, and literal additive reciprocity forces
    ``R=R_step*S_step`` with exponent ``2 log_q C``.  The alternative
    ``R=1`` map replaces the inverse variable by ``R_step*S_step*x``;
    its length is ``C^3`` and violates the theorem's ``M << N^2`` range.
    """

    a = Fraction(degree_exponent)
    m = Fraction(dfi_modulus_exponent)
    n = m
    r = Fraction(fixed_factor_exponent)
    target = Fraction(required_saving)
    trivial = (a + m + n) / 2
    base = trivial + r / 4
    terms = (
        -n / 8,
        r / 8 + n / 8 - m / 4,
        m / 10 - 3 * r / 20 - a / 20 - 3 * n / 20,
        3 * n / 20 - 3 * a / 20 - m / 5,
        3 * n / 8 - m / 2,
    )
    literal_bound = base + max(terms)

    no_fixed_terms = (
        -n / 8,
        n / 8 - m / 4,
        m / 10 - a / 20 - 3 * n / 20,
        3 * n / 20 - 3 * a / 20 - m / 5,
        3 * n / 8 - m / 2,
    )
    fantasy_saving = -max(no_fixed_terms)
    scaled_inverse_m = r + m
    scaled_inverse_n_squared = 2 * n
    return WrightFixedFactorLedger(
        true_l2_trivial=trivial,
        literal_base_with_fixed_factor=base,
        literal_bracket_terms=terms,
        literal_bound=literal_bound,
        literal_loss=literal_bound - trivial,
        no_fixed_factor_saving=fantasy_saving,
        required_qp_saving=target,
        no_fixed_factor_margin=fantasy_saving - target,
        scaled_inverse_m_exponent=scaled_inverse_m,
        scaled_inverse_n_squared_exponent=scaled_inverse_n_squared,
    )
