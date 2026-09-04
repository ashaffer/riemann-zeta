"""Exact ledgers and countermodels for the QP pair-energy/BSG proposal.

The objects in this module are deliberately finite and rational.  They audit
what follows from pair concentration alone; they do *not* claim that the
abstract feature countermodels are points of the actual prime-log cosine
orbit.

There are three distinct checks.

* ``pair_ledger`` records the strongest elementary consequence of the exact
  Gram identity after normalizing ``nu = |mu| / C``.
* ``orthogonal_antipode_model`` is the Bessel-saturated positive-antipode
  model: ``C**2`` mutually orthogonal feature packets, with all good-pair
  mass on the diagonal.
* ``ap_islands_model`` is an exact torsion-free additive model with ``C**2``
  unrelated arithmetic-progression islands.  It saturates the pair-mass,
  packet-count, support-size, and weighted-energy scales but is not contained
  in a rank-one progression.

Only the Python standard library is used so that the verifier is replayable.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from typing import Any, Dict


def line_additive_energy(length: int) -> int:
    """Return ``E([0,length)) = sum_d r(d)^2`` exactly."""

    if length < 1:
        raise ValueError("length must be positive")
    return (2 * length**3 + length) // 3


@dataclass(frozen=True)
class PairLedger:
    cost: int
    packet_count: int
    normalized_good_pair_mass: Fraction
    branch_pair_mass: Fraction
    cell_l2_mass_lower: Fraction
    weighted_energy_lower: Fraction
    one_point_exceptional_mass: Fraction
    one_point_heavy_cell_lower: Fraction

    def to_dict(self) -> Dict[str, Any]:
        return {key: str(value) for key, value in asdict(self).items()}


def pair_ledger(cost: int, packet_count: int | None = None) -> PairLedger:
    """Exact normalized consequences of the proposed pair-energy lemma.

    If ``||mu|| = C`` then the exact threshold argument gives

    ``(nu x nu)(E) >= 1/(2*C**2 - 1)``.

    One of the sum and difference branches therefore has at least half that
    mass.  A radius-one packet meets at most five unit-cell offsets.  If that
    branch uses at most ``R`` packets, Cauchy gives

    ``sum_I nu(I)^2 >= branch_mass/(5*R)``

    and its weighted additive energy is at least

    ``branch_mass**2/(5*R)``.

    The default ``R=C**4`` records the exponent ledger; harmless absolute and
    ``Y**o(1)`` factors are intentionally omitted.
    """

    if cost < 1:
        raise ValueError("cost must be positive")
    c = cost
    r_packets = c**4 if packet_count is None else packet_count
    if r_packets < 1:
        raise ValueError("packet_count must be positive")

    good = Fraction(1, 2 * c**2 - 1)
    branch = good / 2
    cell_l2 = branch / (5 * r_packets)
    energy = branch**2 / (5 * r_packets)

    # The older one-point argument has |mu|(F) >= C/(2C-1), hence
    # nu(F) >= 1/(2C-1).  A radius-one packet meets at most three unit cells.
    one_point_mass = Fraction(1, 2 * c - 1)
    one_point_cell = one_point_mass / (3 * c**2)
    return PairLedger(
        cost=c,
        packet_count=r_packets,
        normalized_good_pair_mass=good,
        branch_pair_mass=branch,
        cell_l2_mass_lower=cell_l2,
        weighted_energy_lower=energy,
        one_point_exceptional_mass=one_point_mass,
        one_point_heavy_cell_lower=one_point_cell,
    )


@dataclass(frozen=True)
class OrthogonalAntipodeModel:
    cost: int
    packet_types: int
    feature_dimension: int
    antipode_depth: Fraction
    normalized_carrier_inner_product: Fraction
    normalized_diagonal_kernel: Fraction
    normalized_off_diagonal_kernel: Fraction
    normalized_kernel_threshold: Fraction
    good_pair_probability: Fraction
    unnormalized_good_pair_mass: Fraction
    one_point_exceptional_probability: Fraction

    def to_dict(self) -> Dict[str, Any]:
        return {key: str(value) for key, value in asdict(self).items()}


def orthogonal_antipode_model(cost: int) -> OrthogonalAntipodeModel:
    """Return the exact Bessel-saturated positive-antipode model.

    Put ``J=C**2``.  In a ``J``-dimensional Hilbert space take orthonormal
    ``x_j`` and the unit carrier

    ``e = -(1/C) * sum_j x_j``.

    The uniform probability on the ``x_j`` has barycenter ``-e/C``.  After
    scaling all feature vectors and the carrier by ``sqrt(M)``, this is the
    desired positive antipode, while the normalized Gram kernel is exactly
    the identity.  Thus the good-pair probability is precisely ``C**-2``
    and contains no off-diagonal additive information.
    """

    if cost < 1:
        raise ValueError("cost must be positive")
    c = cost
    j = c**2
    return OrthogonalAntipodeModel(
        cost=c,
        packet_types=j,
        feature_dimension=j,
        antipode_depth=Fraction(1, c),
        normalized_carrier_inner_product=Fraction(-1, c),
        normalized_diagonal_kernel=Fraction(1),
        normalized_off_diagonal_kernel=Fraction(0),
        normalized_kernel_threshold=Fraction(1, 2 * c**2),
        good_pair_probability=Fraction(1, j),
        # |mu| = C nu, so (|mu| x |mu|)(E) = C^2/J = 1.
        unnormalized_good_pair_mass=Fraction(c**2, j),
        one_point_exceptional_probability=Fraction(1),
    )


@dataclass(frozen=True)
class APIslandsModel:
    cost: int
    islands: int
    island_length: int
    support_size: int
    allowed_within_difference_count: int
    good_pair_probability: Fraction
    mass_per_island: Fraction
    unweighted_additive_energy: int
    weighted_additive_energy: Fraction
    bsg_energy_parameter: Fraction
    difference_span_rank: int
    contained_in_rank_one_progression: bool

    def to_dict(self) -> Dict[str, Any]:
        return {key: str(value) for key, value in asdict(self).items()}


def ap_islands_model(cost: int) -> APIslandsModel:
    r"""Construct ``C**2`` exact unrelated AP islands in a free abelian group.

    Work in ``Z e_0 direct_sum Z e_1 ... direct_sum Z e_J`` and take

    ``A_j = {k e_0 + e_j : 0 <= k < L}``,

    where ``J=C**2`` and ``L=floor((C**4+1)/2)``.  Pairs in one island have
    a common allowed difference set of cardinality ``2L-1 <= C**4`` and
    probability ``1/J=C**-2``.  The whole support has size asymptotic to
    ``C**6/2``.

    Its difference span has rank ``J`` (``e_0`` and ``e_j-e_1``), so the
    support cannot lie in a rank-one arithmetic progression.  The model
    embeds additively in the reals by mapping the basis to Q-linearly
    independent real numbers.
    """

    if cost < 2:
        raise ValueError("cost must be at least two")
    c = cost
    j = c**2
    length = (c**4 + 1) // 2
    support = j * length
    allowed = 2 * length - 1

    # Differences with zero transverse coordinate pool all J islands;
    # every ordered transverse pair contributes its own copy of the line
    # energy.  Hence E(A)=J^2 E_L+J(J-1)E_L.
    e_line = line_additive_energy(length)
    energy = j * (2 * j - 1) * e_line
    weighted = Fraction(energy, support**4)
    k_parameter = Fraction(support**3, energy)
    return APIslandsModel(
        cost=c,
        islands=j,
        island_length=length,
        support_size=support,
        allowed_within_difference_count=allowed,
        good_pair_probability=Fraction(1, j),
        mass_per_island=Fraction(1, j),
        unweighted_additive_energy=energy,
        weighted_additive_energy=weighted,
        bsg_energy_parameter=k_parameter,
        difference_span_rank=j,
        contained_in_rank_one_progression=False,
    )


@dataclass(frozen=True)
class RankTwoGAPModel:
    side_length: int
    support_size: int
    sumset_size: int
    additive_energy: int
    energy_density: Fraction
    difference_span_rank: int
    contained_in_rank_one_progression: bool

    def to_dict(self) -> Dict[str, Any]:
        return {key: str(value) for key, value in asdict(self).items()}


def rank_two_gap_model(side_length: int) -> RankTwoGAPModel:
    """A maximal-energy rank-two GAP that no rank-one AP contains.

    The set is ``[0,n)^2`` in ``Z^2`` (or its injective real image under
    ``(i,j) -> i*alpha+j*beta`` with ``alpha/beta`` irrational).
    """

    if side_length < 2:
        raise ValueError("side_length must be at least two")
    n = side_length
    size = n**2
    energy = line_additive_energy(n) ** 2
    return RankTwoGAPModel(
        side_length=n,
        support_size=size,
        sumset_size=(2 * n - 1) ** 2,
        additive_energy=energy,
        energy_density=Fraction(energy, size**3),
        difference_span_rank=2,
        contained_in_rank_one_progression=False,
    )


@dataclass(frozen=True)
class SumMatchingModel:
    side_size: int
    edge_count: int
    edge_density: Fraction
    restricted_sumset_size: int
    connected_component_size: int

    def to_dict(self) -> Dict[str, Any]:
        return {key: str(value) for key, value in asdict(self).items()}


def sum_matching_model(side_size: int) -> SumMatchingModel:
    r"""Exact bipartite obstruction for the ``t+s`` branch.

    In a free abelian group take ``A={e_i}`` and ``B={g-e_i}``, retaining
    only the matching edges ``(e_i,g-e_i)``.  The restricted sumset is the
    singleton ``{g}``, but the graph density is only ``1/N`` and every
    component is a single edge.  BSG can therefore extract a singleton
    scale object, not a same-side structured set of substantial mass.
    """

    if side_size < 1:
        raise ValueError("side_size must be positive")
    n = side_size
    return SumMatchingModel(
        side_size=n,
        edge_count=n,
        edge_density=Fraction(1, n),
        restricted_sumset_size=1,
        connected_component_size=2,
    )


@dataclass(frozen=True)
class OrientationCountermodel:
    feature_value: Fraction
    coefficient: Fraction
    represented_carrier: Fraction
    total_variation: Fraction
    kernel_value: Fraction
    kernel_threshold: Fraction
    convex_hull_hits_negative_carrier_ray: bool

    def to_dict(self) -> Dict[str, Any]:
        return {key: str(value) for key, value in asdict(self).items()}


def orientation_countermodel() -> OrientationCountermodel:
    """Signed representation and pair energy do not imply an antipode.

    In one feature dimension, ``a=1/2`` and ``mu=2 delta_a`` represent the
    carrier ``q=1`` at TV cost two.  The Gram identity is exact and the sole
    pair is above the proposed threshold, but ``conv{1/2}`` misses every
    negative multiple of ``q``.  The feature is a genuine cosine value
    (``cos(pi/3)=1/2``), and can be placed at arbitrarily high time by adding
    full periods.
    """

    a = Fraction(1, 2)
    coefficient = Fraction(2)
    c = abs(coefficient)
    return OrientationCountermodel(
        feature_value=a,
        coefficient=coefficient,
        represented_carrier=coefficient * a,
        total_variation=c,
        kernel_value=a * a,
        kernel_threshold=Fraction(1, 2 * c**2),
        convex_hull_hits_negative_carrier_ray=False,
    )


def audit_snapshot(cost: int = 10) -> Dict[str, Dict[str, Any]]:
    """Return all exact audit fixtures in a JSON-friendly dictionary."""

    return {
        "pair_ledger": pair_ledger(cost).to_dict(),
        "orthogonal_antipode": orthogonal_antipode_model(cost).to_dict(),
        "ap_islands": ap_islands_model(cost).to_dict(),
        "rank_two_gap": rank_two_gap_model(cost).to_dict(),
        "sum_matching": sum_matching_model(cost**2).to_dict(),
        "orientation": orientation_countermodel().to_dict(),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(audit_snapshot(), indent=2, sort_keys=True))
