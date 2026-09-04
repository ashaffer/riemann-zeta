#!/usr/bin/env python3
"""Sharp pair-energy gates for remote QP atomic interpolation.

The exact QP feature vector is ``a(t)=(cos(t*u_j))_j`` and

    K(s,t) = <a(s),a(t)> = (S(t-s)+S(t+s))/2.

If a signed measure ``mu`` represents the principal carrier ``q0`` with
total variation ``C``, polarize it as ``mu=C*epsilon*nu``.  The oriented
normalized kernel

    G(s,t) = epsilon(s)*epsilon(t)*K(s,t)/M

then has expectation ``1/C**2``.  This module records the sharp elementary
consequences, the exponent ledger after the actual-prime large-value cover,
and two countermodels showing why pair energy alone does not imply a global
rank-one additive representation.

The countermodels are logical stress tests.  They are not actual-prime
cosine nullers.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from dataclasses import asdict, dataclass

import numpy as np


KAPPA_PROMOTE = 0.0180303234
FULL_APERTURE_EXPONENT = 50.0 / 33.0


def upper_tail_lower_bound(mean: float, threshold: float) -> float:
    """Best bound on ``P(X >= threshold)`` using only ``X <= 1`` and E X.

    The result is ``max(0,(mean-threshold)/(1-threshold))``.  It is sharp
    as an infimum (put the lower atom just below ``threshold`` and let it
    approach the threshold).  No lower bound on ``X`` is used.
    """
    if not -1.0 <= mean <= 1.0:
        raise ValueError("mean must lie in [-1,1]")
    if threshold >= 1.0:
        raise ValueError("threshold must be less than one")
    return max(0.0, (mean - threshold) / (1.0 - threshold))


def pair_concentration(cost: float) -> tuple[float, float]:
    """Canonical pair threshold and its exact normalized-mass lower bound."""
    if cost < 1.0:
        raise ValueError("a carrier representation has cost at least one")
    threshold = 1.0 / (2.0 * cost * cost)
    return threshold, 1.0 / (2.0 * cost * cost - 1.0)


def carrier_concentration(cost: float) -> tuple[float, float]:
    """Positive-polarity one-point carrier threshold and mass lower bound."""
    if cost < 1.0:
        raise ValueError("a carrier representation has cost at least one")
    threshold = 1.0 / (2.0 * cost)
    return threshold, 1.0 / (2.0 * cost - 1.0)


def rooted_neighbor_concentration(cost: float) -> tuple[float, float]:
    """High-pair mass seen from every canonical carrier-aligned root.

    If ``epsilon(t)S(t)/M >= 1/(2C)``, then the conditional mean of the
    oriented kernel from that root is at least ``1/(2C**2)``.  Thresholding
    at half this conditional mean gives the returned bound.
    """
    if cost < 1.0:
        raise ValueError("a carrier representation has cost at least one")
    threshold = 1.0 / (4.0 * cost * cost)
    return threshold, 1.0 / (4.0 * cost * cost - 1.0)


def restricted_relation_l2_lower(pair_mass: float, bin_count: int) -> float:
    """Lower bound on sum of squared atom/bin weights from a lag relation.

    If a probability weight ``w`` on a discrete abelian group has pair mass
    ``delta`` on ``R`` allowed sums or differences, then each convolution
    coefficient is at most ``||w||_2**2``.  Hence
    ``||w||_2**2 >= delta/R``.
    """
    if not 0.0 <= pair_mass <= 1.0 or bin_count <= 0:
        raise ValueError("pair mass must be in [0,1] and bin count positive")
    return pair_mass / float(bin_count)


def restricted_relation_energy_lower(pair_mass: float, bin_count: int) -> float:
    """Cauchy lower bound on weighted additive energy from a lag relation."""
    if not 0.0 <= pair_mass <= 1.0 or bin_count <= 0:
        raise ValueError("pair mass must be in [0,1] and bin count positive")
    return pair_mass * pair_mass / float(bin_count)


def packet_mass_l2_lower(mass: float, packet_count: int) -> float:
    """L2 lower bound when mass ``alpha`` is carried by ``R`` packets."""
    if not 0.0 <= mass <= 1.0 or packet_count <= 0:
        raise ValueError("mass must be in [0,1] and packet count positive")
    return mass * mass / float(packet_count)


def cosine_sum(nodes: np.ndarray, value: float) -> float:
    """The actual finite cosine sum ``S(value)`` for supplied nodes."""
    return float(np.sum(np.cos(value * np.asarray(nodes, dtype=float))))


def cosine_kernel(nodes: np.ndarray, left: float, right: float) -> float:
    """Evaluate the cosine Gram kernel directly."""
    values = np.asarray(nodes, dtype=float)
    return float(np.dot(np.cos(left * values), np.cos(right * values)))


def cosine_kernel_via_sum(nodes: np.ndarray, left: float, right: float) -> float:
    """Evaluate ``K=(S(right-left)+S(right+left))/2``."""
    return 0.5 * (
        cosine_sum(nodes, right - left) + cosine_sum(nodes, right + left)
    )


def oriented_energy(
    atoms: np.ndarray, coefficients: np.ndarray
) -> tuple[float, float, np.ndarray]:
    """Return cost, oriented pair expectation, and represented vector.

    Rows of ``atoms`` are feature vectors and ``coefficients`` are signed
    atomic masses.  The expectation uses the polar probability
    ``abs(coefficients)/cost`` and the normalized row Gram matrix.
    """
    matrix = np.asarray(atoms, dtype=float)
    weights = np.asarray(coefficients, dtype=float)
    if matrix.ndim != 2 or weights.shape != (matrix.shape[0],):
        raise ValueError("one coefficient is required for every atom row")
    cost = float(np.sum(np.abs(weights)))
    if cost == 0.0:
        raise ValueError("the coefficient vector must be nonzero")
    dimension = matrix.shape[1]
    represented = weights @ matrix
    normalized_energy = float(np.dot(represented, represented)) / (
        dimension * cost * cost
    )
    return cost, normalized_energy, represented


def regular_hadamard_simplex_rows(cost: int) -> np.ndarray:
    """Minimal-coordinate sign simplex when ``cost`` is a power of two.

    The regular order-four Hadamard matrix ``J_4-2I_4`` has every row and
    column sum two.  Its ``log2(cost)``-fold Kronecker power has order
    ``cost**2``, normalized row Gram the identity, and every row and column
    sum ``cost``.
    """
    if isinstance(cost, bool) or int(cost) != cost or cost < 2:
        raise ValueError("cost must be a power of two at least two")
    cost = int(cost)
    if cost & (cost - 1):
        raise ValueError("cost must be a power of two")
    base = np.ones((4, 4), dtype=np.int8) - 2 * np.eye(4, dtype=np.int8)
    matrix = np.asarray([[1]], dtype=np.int8)
    for _ in range(int(math.log2(cost))):
        matrix = np.kron(matrix, base)
    return matrix


def sign_simplex_rows(cost: int) -> np.ndarray:
    """Bounded-coordinate orthogonal-simplex countermodel.

    Put ``L=C**2``.  Columns range over all sign vectors in ``{+1,-1}^L``
    having coordinate sum ``C``.  The returned ``L`` rows have normalized
    Gram matrix exactly the identity and coordinatewise row-average
    ``1/C``.  Negating the rows therefore gives an exact positive antipode
    of depth ``1/C`` with all off-diagonal pair energy zero.

    For power-of-two ``C`` a regular Hadamard construction uses the minimal
    ``M=L=C**2`` coordinates.  For other small integers the complete block
    design below supplies an exact (but combinatorially large) witness.
    """
    if isinstance(cost, bool) or int(cost) != cost or cost < 1:
        raise ValueError("cost must be a positive integer")
    cost = int(cost)
    if cost >= 2 and not (cost & (cost - 1)):
        return regular_hadamard_simplex_rows(cost)
    row_count = cost * cost
    plus_count = (row_count + cost) // 2
    columns: list[np.ndarray] = []
    for plus_positions in itertools.combinations(range(row_count), plus_count):
        column = -np.ones(row_count, dtype=np.int8)
        column[np.fromiter(plus_positions, dtype=int)] = 1
        columns.append(column)
    return np.stack(columns, axis=1)


@dataclass(frozen=True)
class SignSimplexAudit:
    cost: int
    atom_count: int
    coordinate_count: int
    antipode_depth: float
    representation_tv: float
    representation_residual: float
    row_mean_error: float
    gram_error: float
    high_pair_mass: float


def audit_sign_simplex(cost: int) -> SignSimplexAudit:
    """Check every exact identity in :func:`sign_simplex_rows`."""
    rows = sign_simplex_rows(cost).astype(float)
    atom_count, coordinate_count = rows.shape
    target = np.ones(coordinate_count)
    row_mean_error = float(np.max(np.abs(np.mean(rows, axis=0) - target / cost)))
    gram = rows @ rows.T / coordinate_count
    gram_error = float(np.max(np.abs(gram - np.eye(atom_count))))

    atoms = -rows
    coefficients = -np.full(atom_count, 1.0 / cost)
    tv, energy, represented = oriented_energy(atoms, coefficients)
    residual = float(np.max(np.abs(represented - target)))
    threshold, _ = pair_concentration(float(cost))
    oriented_gram = gram
    high_pair_mass = float(np.mean(oriented_gram >= threshold))
    if abs(energy - 1.0 / (cost * cost)) > 1e-12:
        raise ArithmeticError("the exact pair identity failed numerically")
    return SignSimplexAudit(
        cost=cost,
        atom_count=atom_count,
        coordinate_count=coordinate_count,
        antipode_depth=1.0 / cost,
        representation_tv=tv,
        representation_residual=residual,
        row_mean_error=row_mean_error,
        gram_error=gram_error,
        high_pair_mass=high_pair_mass,
    )


def multi_island_positions(cost: int, island_size: int | None = None) -> tuple[np.ndarray, np.ndarray, float]:
    """Real-line many-island model saturating the pair L2 scale.

    There are ``C**2`` AP islands, each with ``m`` points and probability
    mass ``C**-2``.  Every island has common step ``h``; the bases are spaced
    so no cross-island difference lies within distance one of ``h*Z``.
    One irrational perturbation makes the union impossible to contain in a
    single exact affine lattice.
    """
    if isinstance(cost, bool) or int(cost) != cost or cost < 2:
        raise ValueError("cost must be an integer at least two")
    cost = int(cost)
    island_count = cost * cost
    if island_size is None:
        island_size = cost**4
    if island_size <= 1:
        raise ValueError("island_size must exceed one")
    step = float(4 * island_count + 4)
    bases = 4.0 * np.arange(island_count, dtype=float)
    bases[2] += 0.1 * math.sqrt(2.0)
    positions = (
        bases[:, None] + step * np.arange(island_size, dtype=float)[None, :]
    ).reshape(-1)
    labels = np.repeat(np.arange(island_count), island_size)
    return positions, labels, step


@dataclass(frozen=True)
class MultiIslandAudit:
    cost: int
    island_count: int
    island_size: int
    atom_count: int
    good_pair_mass: float
    allowed_difference_bins: int
    weight_l2: float
    relation_l2_bound: float
    l2_ratio_to_bound: float
    relation_energy: float
    relation_energy_bound: float
    energy_ratio_to_bound: float
    minimum_cross_distance_to_allowed_lag: float
    first_three_lattice_ratio: float
    first_three_lattice_ratio_distance_to_rational_grid: float


def audit_multi_island(cost: int, island_size: int | None = None) -> MultiIslandAudit:
    """Audit the exact scales and separation in the real-line island model."""
    positions, labels, step = multi_island_positions(cost, island_size)
    island_count = cost * cost
    size = int(np.sum(labels == 0))
    atom_count = len(positions)
    good_pair_mass = 1.0 / island_count
    allowed_bins = 2 * size - 1
    weight_l2 = 1.0 / atom_count
    l2_bound = restricted_relation_l2_lower(good_pair_mass, allowed_bins)
    multiplicities = np.arange(1, size + 1, dtype=float)
    squared_triangle_sum = size * size + 2.0 * float(
        np.sum(multiplicities[:-1] ** 2)
    )
    relation_energy = squared_triangle_sum / (
        island_count * island_count * size**4
    )
    energy_bound = restricted_relation_energy_lower(good_pair_mass, allowed_bins)

    bases = positions.reshape(island_count, size)[:, 0]
    cross_residues = []
    for left in range(island_count):
        for right in range(left):
            difference = bases[left] - bases[right]
            cross_residues.append(abs(difference - step * round(difference / step)))
    minimum_cross = min(cross_residues)
    lattice_ratio = (bases[2] - bases[0]) / (bases[1] - bases[0])
    # A finite diagnostic only: the proof of nonlattice containment is that
    # this ratio equals 2+sqrt(2)/40 and is irrational.
    max_denominator = 10_000
    rational_dist = min(
        abs(lattice_ratio - round(lattice_ratio * q) / q)
        for q in range(1, max_denominator + 1)
    )
    return MultiIslandAudit(
        cost=cost,
        island_count=island_count,
        island_size=size,
        atom_count=atom_count,
        good_pair_mass=good_pair_mass,
        allowed_difference_bins=allowed_bins,
        weight_l2=weight_l2,
        relation_l2_bound=l2_bound,
        l2_ratio_to_bound=weight_l2 / l2_bound,
        relation_energy=relation_energy,
        relation_energy_bound=energy_bound,
        energy_ratio_to_bound=relation_energy / energy_bound,
        minimum_cross_distance_to_allowed_lag=minimum_cross,
        first_three_lattice_ratio=lattice_ratio,
        first_three_lattice_ratio_distance_to_rational_grid=rational_dist,
    )


@dataclass(frozen=True)
class PairExponentLedger:
    kappa: float
    one_point_packet_count: float
    one_point_mass: float
    one_point_l2_lower: float
    pair_packet_count: float
    pair_mass: float
    pair_l2_lower: float
    pair_energy_lower: float
    gm_pair_second_term: float
    gm_pair_third_term: float
    gm_pair_third_margin_below_main: float
    aperture: float


def pair_exponent_ledger(kappa: float = KAPPA_PROMOTE) -> PairExponentLedger:
    """Return all fixed-power exponents in the pair-versus-carrier audit."""
    pair_main = 4.0 * kappa
    pair_second = -2.0 / 5.0 + 8.0 * kappa
    pair_third = FULL_APERTURE_EXPONENT - 8.0 / 5.0 + 8.0 * kappa
    return PairExponentLedger(
        kappa=kappa,
        one_point_packet_count=2.0 * kappa,
        one_point_mass=-kappa,
        one_point_l2_lower=-4.0 * kappa,
        pair_packet_count=pair_main,
        pair_mass=-2.0 * kappa,
        pair_l2_lower=-6.0 * kappa,
        pair_energy_lower=-8.0 * kappa,
        gm_pair_second_term=pair_second,
        gm_pair_third_term=pair_third,
        gm_pair_third_margin_below_main=pair_third - pair_main,
        aperture=FULL_APERTURE_EXPONENT,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cost", type=int, default=3)
    parser.add_argument("--island-size", type=int, default=40)
    args = parser.parse_args()
    payload = {
        "verdict": (
            "pair energy is exact but two C-powers weaker than the one-point "
            "packet gate; simplex and multi-island models block a generic "
            "sparse-versus-rank-one inverse theorem"
        ),
        "ledger": asdict(pair_exponent_ledger()),
        "sign_simplex": asdict(audit_sign_simplex(args.cost)),
        "multi_island": asdict(audit_multi_island(args.cost, args.island_size)),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
