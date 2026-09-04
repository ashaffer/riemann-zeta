"""Exact SL2 ledger for fixed-defect QP wedges.

For a wedge

``a*c-a_prime*c_prime=h``

we use the integral matrix ``[[a,a_prime],[c_prime,c]]``.  Choosing one
base matrix on a nonzero defect level translates that level into
``SL_2(Q)``.  The routines below distinguish two notions which must not be
conflated:

* a determinant-level square function only pairs matrices having the same
  determinant;
* noncommutative Balog--Szemeredi--Gowers requires collisions of the full
  quotients ``G_1 G_2^{-1}``.

The module also supplies a sharp quotient-Sidon countermodel in a free
subgroup of ``SL_2(Z)`` and audits the literal prime-power/product-window
wedges without completing their mask.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import sqrt
from typing import Sequence

from qp_finite_carrier_relative_trace import ActualCarrierMatrix
from qp_fixed_defect_graph_cycles import DefectBlock, all_fixed_defect_blocks


Matrix2 = tuple[int, int, int, int]


def determinant(matrix: Matrix2) -> int:
    """Return the determinant of a row-major integral ``2 by 2`` matrix."""

    first, second, third, fourth = matrix
    return first * fourth - second * third


def wedge_matrix(a: int, a_prime: int, c_prime: int, c: int) -> Matrix2:
    """Return ``[[a,a_prime],[c_prime,c]]`` in row-major order."""

    return (int(a), int(a_prime), int(c_prime), int(c))


def quotient_numerator(left: Matrix2, right: Matrix2) -> Matrix2:
    """Return ``left*adj(right)`` exactly.

    On one fixed nonzero determinant level ``h``, equality of these integer
    numerators is equivalent to equality of the rational quotients
    ``left*right^{-1}``; division by ``h`` is common to every pair.
    """

    a, b, c, d = left
    x, y, z, w = right
    return (
        a * w - b * z,
        -a * y + b * x,
        c * w - d * z,
        -c * y + d * x,
    )


def quotient_multiplicities(
    matrices: Sequence[Matrix2],
) -> Counter[Matrix2]:
    """Count every ordered quotient on one fixed determinant level."""

    items = tuple(matrices)
    if items:
        level = determinant(items[0])
        if level == 0 or any(determinant(item) != level for item in items):
            raise ValueError("matrices must have one common nonzero determinant")
    return Counter(
        quotient_numerator(left, right) for left in items for right in items
    )


def multiplicative_energy(matrices: Sequence[Matrix2]) -> int:
    r"""Return ``#{G1 G2^-1=G3 G4^-1}`` on a fixed level."""

    return sum(
        multiplicity * multiplicity
        for multiplicity in quotient_multiplicities(matrices).values()
    )


def minimum_distinct_quotient_energy(cardinality: int) -> int:
    """Return ``2*N^2-N``, the quotient-Sidon energy of ``N`` points.

    The identity quotient has multiplicity ``N``.  If every nonidentity
    ordered quotient is distinct, all remaining ``N*(N-1)`` fibres have
    multiplicity one.
    """

    count = int(cardinality)
    if count < 0:
        raise ValueError("cardinality must be nonnegative")
    return 2 * count * count - count


def is_quotient_sidon(matrices: Sequence[Matrix2]) -> bool:
    """Test whether all nonidentity ordered quotients are distinct."""

    original = tuple(matrices)
    items = tuple(dict.fromkeys(original))
    if len(items) != len(original):
        return False
    return multiplicative_energy(items) == minimum_distinct_quotient_energy(
        len(items)
    )


def free_conjugate(index: int) -> Matrix2:
    r"""Return ``U^index V U^-index`` in Sanov's free subgroup.

    Here ``U=[[1,2],[0,1]]`` and ``V=[[1,0],[2,1]]``.  For positive
    distinct indices the quotients of these conjugates are all distinct,
    apart from the unavoidable identity quotient.
    """

    value = int(index)
    if value <= 0:
        raise ValueError("index must be positive")
    return (1 + 4 * value, -8 * value * value, 2, 1 - 4 * value)


def free_quotient_sidon_set(cardinality: int, *, defect: int = 1) -> tuple[Matrix2, ...]:
    """Return an exact quotient-Sidon set of determinant ``defect``.

    Right multiplication by ``diag(defect,1)`` preserves every relative
    quotient and changes the common determinant from one to ``defect``.
    The construction is a group-theoretic obstruction, not a QP shell
    construction: its entries need not be positive or comparable.
    """

    count = int(cardinality)
    level = int(defect)
    if count < 1:
        raise ValueError("cardinality must be positive")
    if level == 0:
        raise ValueError("defect must be nonzero")
    answer = []
    for index in range(1, count + 1):
        a, b, c, d = free_conjugate(index)
        answer.append((level * a, b, level * c, d))
    return tuple(answer)


def quotient_sidon_star(cardinality: int, *, defect: int = 1) -> tuple[Matrix2, ...]:
    r"""Return a fixed-defect star whose wedge matrices are quotient-Sidon.

    For ``x_i=i`` and ``y_i=i+1`` use

    ``G_i=[[defect+x_i*y_i,x_i],[y_i,1]]``.

    All wedges share the source colour ``c=1`` and have private target
    colours ``c_prime=y_i``.  For two indices ``i,j``, the bottom-left,
    top-left, and bottom-right entries of ``G_i adj(G_j)`` are respectively

    ``y_i-y_j``, ``defect+x_i*(y_i-y_j)``, and
    ``defect-x_j*(y_i-y_j)``.

    Hence every nonidentity quotient recovers ``x_i,x_j`` and is unique.
    The directed colour graph is nevertheless a star of singular norm
    ``sqrt(cardinality)`` and numerical radius ``sqrt(cardinality)/2``.
    This is the exact normalized-operator obstruction missing from the
    simpler coherent-mass countermodel.
    """

    count = int(cardinality)
    level = int(defect)
    if count < 1:
        raise ValueError("cardinality must be positive")
    if level == 0:
        raise ValueError("defect must be nonzero")
    return tuple(
        (level + index * (index + 1), index, index + 1, 1)
        for index in range(1, count + 1)
    )


def star_numerical_radius(cardinality: int) -> float:
    """Return the numerical radius of a directed unit-weight star."""

    count = int(cardinality)
    if count < 1:
        raise ValueError("cardinality must be positive")
    return sqrt(count) / 2.0


def centered_star_rayleigh(cardinality: int, reservoir_size: int) -> float:
    r"""Return an exact mean-zero star Rayleigh quotient construction.

    Start with central amplitude ``1``, each of ``N`` leaf amplitudes
    ``1/sqrt(N)``, and ``L`` isolated coordinates each equal to
    ``-(1+sqrt(N))/L``.  The vector sums to zero.  After normalization its
    directed-star quadratic is the returned value, tending to ``sqrt(N)/2``
    as the isolated reservoir grows.
    """

    count = int(cardinality)
    reservoir = int(reservoir_size)
    if count < 1 or reservoir < 1:
        raise ValueError("cardinality and reservoir_size must be positive")
    root = sqrt(count)
    norm_square = 2.0 + (1.0 + root) ** 2 / reservoir
    return root / norm_square


def centered_star_family_moment(
    level_count: int,
    cardinality: int,
    reservoir_size: int,
    moment: int,
) -> float:
    r"""Return ``sum_h |<K_h z,z>|^(2m)`` for the shared-star family.

    Use :func:`quotient_sidon_star` with the same source and target colours
    on every determinant ``h=1,...,H``.  Only the top-left label changes, so
    every ``K_h`` is the same directed star and the one mean-zero vector
    from :func:`centered_star_rayleigh` works simultaneously on all levels.
    """

    levels = int(level_count)
    power = int(moment)
    if levels < 1 or power < 1:
        raise ValueError("level_count and moment must be positive")
    rayleigh = centered_star_rayleigh(cardinality, reservoir_size)
    return levels * rayleigh ** (2 * power)


def star_relative_commutator_trace(defect: int) -> Fraction:
    r"""Return the trace of the first two nontrivial relative commutators.

    Anchor the star at ``G_1`` and put ``A_i=G_i G_1^{-1}``.  Direct
    multiplication gives

    ``tr([A_2,A_3])=2-4/defect^3``.

    This is never two.  Hence ``A_2,A_3`` are not simultaneously
    triangularizable over ``C``; the first three star matrices do not lie
    in one translated Borel, and a fortiori not in one translated torus or
    unipotent subgroup.
    """

    level = int(defect)
    if level == 0:
        raise ValueError("defect must be nonzero")
    return Fraction(2 * level**3 - 4, level**3)


def centered_level_moment(level_count: int, support_size: int, moment: int) -> int:
    r"""Return the exact moment of the balanced ``+N/-N`` level profile.

    On an even number ``H`` of determinant levels, put ``kappa_h=N`` on
    half and ``kappa_h=-N`` on half.  Its mean is zero and

    ``sum_h |kappa_h|^(2m)=H*N^(2m)``.

    Each level may independently use :func:`free_quotient_sidon_set`, whose
    multiplicative-energy density is only ``(2*N^2-N)/N^3``.  Thus taking
    higher scalar moments amplifies the determinant profile but does not
    create quotient collisions.
    """

    levels = int(level_count)
    size = int(support_size)
    power = int(moment)
    if levels < 2 or levels % 2:
        raise ValueError("level_count must be a positive even integer")
    if size < 1 or power < 1:
        raise ValueError("support_size and moment must be positive")
    return levels * size ** (2 * power)


def wedge_matrices_from_blocks(
    core: ActualCarrierMatrix,
    blocks: Sequence[DefectBlock],
) -> tuple[Matrix2, ...]:
    """Recover every literal oriented wedge matrix from defect blocks.

    No interval or prime mask is completed.  A product state may have its
    two prime-power factor orientations, and all of them are retained.
    """

    if not blocks:
        return ()
    level = blocks[0].defect
    if level == 0 or any(block.defect != level for block in blocks):
        raise ValueError("blocks must have one common nonzero defect")
    values = core.values
    answer: list[Matrix2] = []
    for block in blocks:
        for source_index in block.source_colours:
            c = int(values[source_index])
            if block.source_product % c:
                raise AssertionError("source colour does not divide its product")
            a = block.source_product // c
            for target_index in block.target_colours:
                c_prime = int(values[target_index])
                if block.target_product % c_prime:
                    raise AssertionError("target colour does not divide its product")
                a_prime = block.target_product // c_prime
                matrix = wedge_matrix(a, a_prime, c_prime, c)
                if determinant(matrix) != level:
                    raise AssertionError("wedge determinant reconstruction failed")
                answer.append(matrix)
    # Repeated matrices would mean the same literal oriented wedge was
    # reached from two product blocks.  Deduplication keeps the group audit
    # well-defined while the assertion exposes such a bookkeeping failure.
    unique = tuple(dict.fromkeys(answer))
    if len(unique) != len(answer):
        raise AssertionError("a literal wedge occurred in two defect blocks")
    return unique


@dataclass(frozen=True)
class ActualPrimeSL2Audit:
    q: int
    degree_parameter: int
    level_count: int
    maximum_block_count: int
    maximum_wedge_count: int
    every_level_quotient_sidon: bool
    maximum_energy: int
    maximum_energy_denominator_cube: int


def actual_prime_sl2_audit(q: int) -> ActualPrimeSL2Audit:
    """Audit quotient collisions on every literal prime-power defect ray."""

    # Importing here avoids making the finite carrier builder part of the
    # algebra-only module import path for callers using just the countermodel.
    from qp_finite_carrier_relative_trace import build_actual_carrier_matrix

    core = build_actual_carrier_matrix(int(q))
    rays = all_fixed_defect_blocks(core)
    maximum_blocks = 0
    maximum_wedges = 0
    maximum_energy_value = 0
    maximum_energy_cube = 1
    all_sidon = True
    for blocks in rays.values():
        matrices = wedge_matrices_from_blocks(core, blocks)
        count = len(matrices)
        energy = multiplicative_energy(matrices)
        maximum_blocks = max(maximum_blocks, len(blocks))
        maximum_wedges = max(maximum_wedges, count)
        all_sidon = all_sidon and (
            energy == minimum_distinct_quotient_energy(count)
        )
        if energy > maximum_energy_value:
            maximum_energy_value = energy
            maximum_energy_cube = count**3
    return ActualPrimeSL2Audit(
        q=core.q,
        degree_parameter=core.degree_parameter,
        level_count=len(rays),
        maximum_block_count=maximum_blocks,
        maximum_wedge_count=maximum_wedges,
        every_level_quotient_sidon=all_sidon,
        maximum_energy=maximum_energy_value,
        maximum_energy_denominator_cube=maximum_energy_cube,
    )
