"""Exact ``q^2`` packet atoms and the short-residual matching identity.

This module keeps the finite algebra behind the coarse ``q^2`` lift
literal.  On the narrow prime-power shell, every occupied coarse residual

    r = 8*a*b*c - q**3,              2*abs(r) < q**2,

determines one unordered triple.  Its carrier--colour matrix is therefore
one triangle atom (with the evident loop modifications when nodes repeat).

Two consequences are useful and deliberately separated here.

* The Fourier packet Gram has an exact low-rank ANOVA correction after
  physical double centering.  This is a Hilbert--Schmidt identity, not the
  desired operator large sieve.
* If residuals are put in half-open intervals of length ``8*min(shell)``,
  the triangle atoms in every interval are vertex-disjoint.  Thus every
  short block has norm at most two.  The cross-block products, however,
  are exactly the common-neighbour covariance.  In the all-distinct sector
  the square function even contains the original carrier:

      sum_I B_I**2 = 2*diag(hyperedge_degrees) + T.

The last identity is an exact circularity test for a proposed automatic
matrix-Carleson argument.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from math import ceil, prod
from typing import Mapping, Sequence

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import LinearOperator, eigsh

from qp_finite_carrier_relative_trace import exact_balanced_degree
from qp_four_cycle_hostile_lab import shell_values


@dataclass(frozen=True)
class ResidueTriangleAtom:
    """One unordered product triple and all of its ordered matrix entries."""

    residual: int
    node_indices: tuple[int, int, int]
    support: csr_matrix

    @property
    def orbit_size(self) -> int:
        return int(self.support.nnz)

    @property
    def all_nodes_distinct(self) -> bool:
        return len(set(self.node_indices)) == 3

    @property
    def vertex_set(self) -> frozenset[int]:
        return frozenset(self.node_indices)


@dataclass(frozen=True)
class Q2ResidueAtomModel:
    """The exact coarse carrier resolved into centered integer residuals."""

    q: int
    degree_parameter: int
    width: float
    values: np.ndarray
    atoms: tuple[ResidueTriangleAtom, ...]

    @property
    def dimension(self) -> int:
        return int(self.values.size)

    @property
    def modulus(self) -> int:
        return self.q * self.q

    @property
    def coarse_edge_count(self) -> int:
        return sum(atom.orbit_size for atom in self.atoms)

    @property
    def selected_atoms(self) -> tuple[ResidueTriangleAtom, ...]:
        bound = self.q * self.degree_parameter
        return tuple(
            atom
            for atom in self.atoms
            if 0 < abs(atom.residual) <= bound and atom.residual % self.q
        )


def _ordered_orbit(nodes: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    return set(permutations(nodes))


def build_q2_residue_atom_model(
    q: int,
    *,
    degree_parameter: int | None = None,
    width: float = 0.2,
) -> Q2ResidueAtomModel:
    r"""Resolve the exact coarse window ``2*|8abc-q^3|<q^2``.

    The routine uses only integer comparisons.  It also verifies the
    unique-factorization conclusion rather than silently assuming it: every
    residual must consist of the complete ordered orbit of one unordered
    shell triple.
    """

    modulus_root = int(q)
    if modulus_root <= 2 or modulus_root % 2 == 0:
        raise ValueError("q must be an odd integer greater than two")
    if width <= 0:
        raise ValueError("width must be positive")
    if modulus_root**3 > np.iinfo(np.int64).max:
        raise ValueError("q is too large for the vectorized exact builder")
    degree = (
        exact_balanced_degree(modulus_root)
        if degree_parameter is None
        else int(degree_parameter)
    )
    if degree <= 0 or 2 * modulus_root * degree >= modulus_root**2:
        raise ValueError("the fine residual interval must fit in the coarse lift")

    values = shell_values(modulus_root / 2.0, width, "prime_powers")
    if values.size == 0:
        raise ValueError("the requested shell is empty")
    dimension = int(values.size)
    lower = int(values[0])
    upper = int(values[-1])
    lookup = np.full(upper + 2, -1, dtype=np.int32)
    lookup[values] = np.arange(dimension, dtype=np.int32)

    target = modulus_root**3
    modulus = modulus_root**2
    ordered_by_residual: dict[int, set[tuple[int, int, int]]] = defaultdict(set)
    canonical_by_residual: dict[int, tuple[int, int, int]] = {}

    for row_index, raw_carrier in enumerate(values):
        carrier = int(raw_carrier)
        denominators = 8 * carrier * values
        floors = target // denominators
        for candidates in (floors, floors + 1):
            inside = (candidates >= lower) & (candidates <= upper)
            label_ids = np.full(dimension, -1, dtype=np.int32)
            label_ids[inside] = lookup[candidates[inside]]
            residuals = denominators * candidates - target
            accepted = (label_ids >= 0) & (2 * np.abs(residuals) < modulus)
            for column_index in np.flatnonzero(accepted):
                label_index = int(label_ids[column_index])
                residual = int(residuals[column_index])
                ordered = (label_index, row_index, int(column_index))
                canonical = tuple(sorted(ordered))
                previous = canonical_by_residual.setdefault(residual, canonical)
                if previous != canonical:
                    raise AssertionError(
                        "one coarse residual acquired two unordered triples"
                    )
                ordered_by_residual[residual].add(ordered)

    atoms: list[ResidueTriangleAtom] = []
    occupied_cells: set[tuple[int, int]] = set()
    for residual in sorted(ordered_by_residual):
        canonical = canonical_by_residual[residual]
        ordered = ordered_by_residual[residual]
        expected = _ordered_orbit(canonical)
        if ordered != expected:
            raise AssertionError("a residual does not contain its full permutation orbit")
        rows = [triple[1] for triple in sorted(ordered)]
        columns = [triple[2] for triple in sorted(ordered)]
        cells = set(zip(rows, columns))
        if occupied_cells.intersection(cells):
            raise AssertionError("two residue atoms overlap in a physical matrix cell")
        occupied_cells.update(cells)
        support = coo_matrix(
            (np.ones(len(rows), dtype=np.int8), (rows, columns)),
            shape=(dimension, dimension),
        ).tocsr()
        if (support - support.T).nnz:
            raise AssertionError("a residue triangle must be symmetric")
        atoms.append(
            ResidueTriangleAtom(
                residual=residual,
                node_indices=canonical,
                support=support,
            )
        )
    return Q2ResidueAtomModel(
        q=modulus_root,
        degree_parameter=degree,
        width=float(width),
        values=values,
        atoms=tuple(atoms),
    )


def weighted_atom_matrix(
    model: Q2ResidueAtomModel,
    weights: Mapping[int, complex | float | Fraction],
) -> np.ndarray:
    """Return ``sum_r weights[r] A_r`` as a dense complex matrix."""

    answer = np.zeros((model.dimension, model.dimension), dtype=complex)
    for atom in model.atoms:
        weight = complex(weights.get(atom.residual, 0.0))
        if weight:
            answer += weight * atom.support.toarray()
    return answer


def coarse_label_slices(model: Q2ResidueAtomModel) -> tuple[csr_matrix, ...]:
    r"""Return the coarse partial-permutation slice for every third label.

    ``P_c(a,b)`` is one when ``(a,b,c)`` lies in the coarse product window.
    The interval in ``b`` has total length below one, so every ``P_c`` has
    at most one entry in each row and column.  The corresponding interval
    in ``c`` also has length below one, so the physical supports of the
    different label slices are disjoint.
    """

    rows: list[list[int]] = [[] for _ in range(model.dimension)]
    columns: list[list[int]] = [[] for _ in range(model.dimension)]
    for atom in model.atoms:
        for label, row, column in _ordered_orbit(atom.node_indices):
            rows[label].append(row)
            columns[label].append(column)
    slices: list[csr_matrix] = []
    occupied: set[tuple[int, int]] = set()
    for label in range(model.dimension):
        cells = set(zip(rows[label], columns[label]))
        if len(cells) != len(rows[label]):
            raise AssertionError("one label slice contains a duplicate cell")
        if occupied.intersection(cells):
            raise AssertionError("coarse label slices overlap")
        occupied.update(cells)
        matrix = coo_matrix(
            (
                np.ones(len(rows[label]), dtype=np.int8),
                (rows[label], columns[label]),
            ),
            shape=(model.dimension, model.dimension),
        ).tocsr()
        row_degrees = np.asarray(matrix.sum(axis=1)).reshape(-1)
        column_degrees = np.asarray(matrix.sum(axis=0)).reshape(-1)
        if np.max(row_degrees, initial=0) > 1 or np.max(column_degrees, initial=0) > 1:
            raise AssertionError("a coarse label slice is not a partial permutation")
        slices.append(matrix)
    return tuple(slices)


def weighted_coarse_principal_matrix(
    model: Q2ResidueAtomModel, coefficients: Sequence[complex]
) -> np.ndarray:
    r"""Return ``(2D/q) sum_c z_c P_c`` for the coarse principal block."""

    vector = np.asarray(coefficients, dtype=complex).reshape(-1)
    if vector.size != model.dimension:
        raise ValueError("the coefficient vector has the wrong dimension")
    density = 2.0 * model.degree_parameter / model.q
    answer = np.zeros((model.dimension, model.dimension), dtype=complex)
    for coefficient, matrix in zip(vector, coarse_label_slices(model)):
        if coefficient:
            answer += density * coefficient * matrix.toarray()
    return answer


@dataclass(frozen=True)
class WeightedPrincipalLedger:
    q: int
    degree_parameter: int
    dimension: int
    coefficient_l2_squared: float
    maximum_slice_entries: int
    maximum_slice_row_degree: int
    maximum_slice_column_degree: int
    maximum_physical_support_overlap: int
    hilbert_schmidt_squared: float
    hilbert_schmidt_squared_bound: float
    operator_norm: float
    operator_norm_bound: float
    schatten_fourth_power: float
    schatten_fourth_power_bound: float


def weighted_principal_ledger(
    model: Q2ResidueAtomModel, coefficients: Sequence[complex]
) -> WeightedPrincipalLedger:
    r"""Certify the weighted coarse-principal Schatten bounds.

    The exact disjoint-support formula is

    ``||A_0(z)||_HS^2=(2D/q)^2 sum_c |z_c|^2 |P_c|``.

    Since every ``P_c`` is a partial permutation with at most ``n`` entries,

    ``||A_0(z)||_op <= ||A_0(z)||_HS <= (2D/q)*sqrt(n)||z||_2``

    and ``||A_0(z)||_S4^4`` is at most the square of that HS budget.  With
    ``n<=q`` these are ``O(D/sqrt(q))`` and ``O(D^4/q^2)`` respectively.
    """

    vector = np.asarray(coefficients, dtype=complex).reshape(-1)
    if vector.size != model.dimension:
        raise ValueError("the coefficient vector has the wrong dimension")
    slices = coarse_label_slices(model)
    density = 2.0 * model.degree_parameter / model.q
    coefficient_norm_squared = float(np.vdot(vector, vector).real)
    sizes = np.asarray([matrix.nnz for matrix in slices], dtype=float)
    exact_hs_squared = density**2 * float(np.dot(np.abs(vector) ** 2, sizes))
    hs_bound = density**2 * model.dimension * coefficient_norm_squared

    weighted = np.zeros((model.dimension, model.dimension), dtype=complex)
    support_count = np.zeros((model.dimension, model.dimension), dtype=np.int16)
    maximum_row = 0
    maximum_column = 0
    for coefficient, matrix in zip(vector, slices):
        dense = matrix.toarray()
        support_count += dense
        if coefficient:
            weighted += density * coefficient * dense
        maximum_row = max(
            maximum_row,
            int(np.max(np.asarray(matrix.sum(axis=1)).reshape(-1), initial=0)),
        )
        maximum_column = max(
            maximum_column,
            int(np.max(np.asarray(matrix.sum(axis=0)).reshape(-1), initial=0)),
        )
    singular_values = np.linalg.svd(weighted, compute_uv=False)
    observed_hs_squared = float(np.sum(singular_values**2))
    if not np.isclose(observed_hs_squared, exact_hs_squared, rtol=1e-10, atol=1e-12):
        raise AssertionError("the disjoint-support Hilbert--Schmidt identity failed")
    return WeightedPrincipalLedger(
        q=model.q,
        degree_parameter=model.degree_parameter,
        dimension=model.dimension,
        coefficient_l2_squared=coefficient_norm_squared,
        maximum_slice_entries=int(np.max(sizes, initial=0)),
        maximum_slice_row_degree=maximum_row,
        maximum_slice_column_degree=maximum_column,
        maximum_physical_support_overlap=int(np.max(support_count, initial=0)),
        hilbert_schmidt_squared=observed_hs_squared,
        hilbert_schmidt_squared_bound=hs_bound,
        operator_norm=float(np.max(singular_values, initial=0.0)),
        operator_norm_bound=float(np.sqrt(hs_bound)),
        schatten_fourth_power=float(np.sum(singular_values**4)),
        schatten_fourth_power_bound=hs_bound**2,
    )


def coarse_packet_matrix(model: Q2ResidueAtomModel, frequency: int) -> np.ndarray:
    r"""Return ``C_h=sum_r exp(2*pi*i*h*r/q^2) A_r``."""

    modulus = model.modulus
    h = int(frequency) % modulus
    weights = {
        atom.residual: np.exp(2j * np.pi * h * atom.residual / modulus)
        for atom in model.atoms
    }
    return weighted_atom_matrix(model, weights)


def aligned_residual_indicator(q: int, degree: int) -> np.ndarray:
    """Return the exact unit residual selector on ``Z/q^2 Z``."""

    modulus_root = int(q)
    radius = modulus_root * int(degree)
    modulus = modulus_root**2
    if radius <= 0 or 2 * radius >= modulus:
        raise ValueError("require 0<qD<q^2/2")
    indicator = np.zeros(modulus, dtype=float)
    for residual in range(-radius, radius + 1):
        if residual and residual % modulus_root:
            indicator[residual % modulus] = 1.0
    return indicator


def aligned_packet_coefficients(q: int, degree: int) -> np.ndarray:
    r"""Return ``alpha_h=q^-2 sum_(r in R) exp(-2*pi*i*h*r/q^2)``."""

    indicator = aligned_residual_indicator(q, degree)
    return np.fft.fft(indicator) / indicator.size


def primitive_reconstruction_values(model: Q2ResidueAtomModel) -> np.ndarray:
    """Reconstruct the fine selector on every occupied coarse residue.

    Frequencies divisible by ``q`` are replaced by their exact conditional
    expectation ``2D/q``.  The returned values should therefore be zero or
    one up to floating-point replay error.
    """

    coefficients = aligned_packet_coefficients(model.q, model.degree_parameter)
    frequencies = np.flatnonzero(np.arange(model.modulus) % model.q)
    residuals = np.asarray([atom.residual for atom in model.atoms], dtype=np.int64)
    if not residuals.size:
        return np.empty(0, dtype=complex)
    phases = np.exp(
        2j
        * np.pi
        * frequencies[:, None]
        * (residuals[None, :] % model.modulus)
        / model.modulus
    )
    return (
        Fraction(2 * model.degree_parameter, model.q).__float__()
        + coefficients[frequencies] @ phases
    )


def physical_primitive_weights(model: Q2ResidueAtomModel) -> dict[int, Fraction]:
    r"""Return the exact physical weights ``1_R(r)-2D/q`` on coarse atoms."""

    density = Fraction(2 * model.degree_parameter, model.q)
    radius = model.q * model.degree_parameter
    return {
        atom.residual: Fraction(
            int(
                0 < abs(atom.residual) <= radius
                and atom.residual % model.q != 0
            ),
            1,
        )
        - density
        for atom in model.atoms
    }


def _degree_vector(atom: ResidueTriangleAtom) -> np.ndarray:
    return np.asarray(atom.support.sum(axis=1), dtype=np.int64).reshape(-1)


def centered_atom_gram_numerator(model: Q2ResidueAtomModel) -> np.ndarray:
    r"""Return ``n^2 <P A_r P,P A_s P>_HS`` as an integer matrix.

    Since distinct residue atoms have disjoint physical entries, the exact
    formula is

    ``n^2 delta_rs |A_r| - 2n <d_r,d_s> + |A_r||A_s|``.
    """

    atom_count = len(model.atoms)
    if atom_count == 0:
        return np.zeros((0, 0), dtype=np.int64)
    dimension = model.dimension
    degrees = np.vstack([_degree_vector(atom) for atom in model.atoms])
    sizes = np.asarray([atom.orbit_size for atom in model.atoms], dtype=np.int64)
    answer = -2 * dimension * (degrees @ degrees.T) + np.outer(sizes, sizes)
    answer[np.diag_indices(atom_count)] += dimension * dimension * sizes
    return answer


def balanced_distinct_flow_dimension_lower_bound(model: Q2ResidueAtomModel) -> int:
    r"""Dimension of an exact flat packet-Gram eigenspace.

    Put one incidence column on every shell vertex and one row on every
    all-distinct residue triangle.  Any coefficient vector in the left
    kernel has zero degree at every vertex.  The centered correction then
    vanishes, so it is an exact eigenvector of the normalized atom Gram with
    eigenvalue six.  The returned nullity is computed exactly over the
    reals (the incidence matrix has integer entries).
    """

    distinct = tuple(atom for atom in model.atoms if atom.all_nodes_distinct)
    if not distinct:
        return 0
    incidence = np.zeros((len(distinct), model.dimension), dtype=float)
    for row, atom in enumerate(distinct):
        incidence[row, tuple(atom.vertex_set)] = 1.0
    return len(distinct) - int(np.linalg.matrix_rank(incidence))


def packet_hilbert_schmidt_gram(
    model: Q2ResidueAtomModel, frequencies: Sequence[int]
) -> np.ndarray:
    """Return the doubly-centered packet Hilbert--Schmidt Gram exactly via atoms."""

    chosen = np.asarray(tuple(int(value) % model.modulus for value in frequencies))
    residuals = np.asarray([atom.residual for atom in model.atoms], dtype=np.int64)
    transform = np.exp(
        2j
        * np.pi
        * residuals[:, None]
        * chosen[None, :]
        / model.modulus
    )
    atom_gram = centered_atom_gram_numerator(model) / model.dimension**2
    return transform.conj().T @ atom_gram @ transform


@dataclass(frozen=True)
class ResidualMatchingBlock:
    """One half-open short residual interval and its vertex-disjoint atoms."""

    index: int
    lower: int
    upper: int
    atoms: tuple[ResidueTriangleAtom, ...]


def short_residual_matching_blocks(
    model: Q2ResidueAtomModel,
    *,
    selected_only: bool = True,
) -> tuple[ResidualMatchingBlock, ...]:
    r"""Partition atoms into intervals of length ``8*min(shell)``.

    If two different atoms in one interval shared a node ``v``, their
    residual difference would be a nonzero multiple of ``8v`` and hence
    have magnitude at least the interval length.  The function verifies the
    resulting vertex-disjointness explicitly.
    """

    atoms = model.selected_atoms if selected_only else model.atoms
    if not atoms:
        return ()
    block_width = 8 * int(model.values[0])
    origin = (
        -model.q * model.degree_parameter
        if selected_only
        else min(atom.residual for atom in atoms)
    )
    grouped: dict[int, list[ResidueTriangleAtom]] = defaultdict(list)
    for atom in atoms:
        grouped[(atom.residual - origin) // block_width].append(atom)

    answer: list[ResidualMatchingBlock] = []
    for index in sorted(grouped):
        block_atoms = tuple(sorted(grouped[index], key=lambda atom: atom.residual))
        used: set[int] = set()
        for atom in block_atoms:
            if used.intersection(atom.vertex_set):
                raise AssertionError("one short residual block is not a matching")
            used.update(atom.vertex_set)
        lower = origin + index * block_width
        answer.append(
            ResidualMatchingBlock(
                index=index,
                lower=lower,
                upper=lower + block_width,
                atoms=block_atoms,
            )
        )
    return tuple(answer)


def block_matrix(block: ResidualMatchingBlock, dimension: int) -> csr_matrix:
    """Return the direct sum of triangle atoms in one matching block."""

    if not block.atoms:
        return csr_matrix((dimension, dimension), dtype=np.int64)
    answer = sum(
        (atom.support.astype(np.int64) for atom in block.atoms),
        start=csr_matrix((dimension, dimension), dtype=np.int64),
    )
    return answer.tocsr()


def block_vertex_overlap_matrix(
    blocks: Sequence[ResidualMatchingBlock], dimension: int
) -> np.ndarray:
    """Return the Gram of block vertex-incidence vectors."""

    incidence = np.zeros((len(blocks), int(dimension)), dtype=np.int64)
    for block_index, block in enumerate(blocks):
        for atom in block.atoms:
            incidence[block_index, tuple(atom.vertex_set)] = 1
    return incidence @ incidence.T


@dataclass(frozen=True)
class BlockProductConservation:
    """Exact product and boundary identities for two matching blocks."""

    first_edge_count: int
    second_edge_count: int
    shared_vertex_count: int
    first_boundary_count: int
    second_boundary_count: int
    first_residual_product: int
    second_residual_product: int
    first_vertex_product: int
    second_vertex_product: int
    first_boundary_product: int
    second_boundary_product: int
    individual_product_identities_hold: bool
    cancelled_boundary_identity_holds: bool
    residual_order_forces_boundary_order: bool


def block_product_conservation(
    model: Q2ResidueAtomModel,
    first: ResidualMatchingBlock,
    second: ResidualMatchingBlock,
) -> BlockProductConservation:
    r"""Cancel the common vertices in two residual-block product identities.

    For an all-distinct matching block ``I`` with ``k`` atoms,

    ``prod_(e in I)(q^3+r_e)=8^k prod_(v in V(I)) v``.

    If two such blocks have the same number of atoms and the first lies
    strictly below the second, cancellation shows that the product of the
    second boundary vertices is strictly larger.  In particular, distinct
    ordered blocks cannot cover exactly the same vertex multiset.
    """

    if any(not atom.all_nodes_distinct for atom in first.atoms + second.atoms):
        raise ValueError("product conservation currently requires distinct nodes")

    def vertex_indices(block: ResidualMatchingBlock) -> set[int]:
        return set().union(*(set(atom.vertex_set) for atom in block.atoms))

    first_vertices = vertex_indices(first)
    second_vertices = vertex_indices(second)
    shared = first_vertices.intersection(second_vertices)
    first_boundary = first_vertices - shared
    second_boundary = second_vertices - shared

    first_residual_product = prod(model.q**3 + atom.residual for atom in first.atoms)
    second_residual_product = prod(model.q**3 + atom.residual for atom in second.atoms)
    first_vertex_product = prod(int(model.values[index]) for index in first_vertices)
    second_vertex_product = prod(int(model.values[index]) for index in second_vertices)
    first_boundary_product = prod(int(model.values[index]) for index in first_boundary)
    second_boundary_product = prod(int(model.values[index]) for index in second_boundary)
    first_identity = first_residual_product == 8 ** len(first.atoms) * first_vertex_product
    second_identity = second_residual_product == 8 ** len(second.atoms) * second_vertex_product
    equal_counts = len(first.atoms) == len(second.atoms)
    boundary_identity = (
        not equal_counts
        or second_residual_product * first_boundary_product
        == first_residual_product * second_boundary_product
    )
    ordered = first.upper <= second.lower
    forced_order = (
        not (ordered and equal_counts)
        or second_boundary_product > first_boundary_product
    )
    return BlockProductConservation(
        first_edge_count=len(first.atoms),
        second_edge_count=len(second.atoms),
        shared_vertex_count=len(shared),
        first_boundary_count=len(first_boundary),
        second_boundary_count=len(second_boundary),
        first_residual_product=first_residual_product,
        second_residual_product=second_residual_product,
        first_vertex_product=first_vertex_product,
        second_vertex_product=second_vertex_product,
        first_boundary_product=first_boundary_product,
        second_boundary_product=second_boundary_product,
        individual_product_identities_hold=first_identity and second_identity,
        cancelled_boundary_identity_holds=boundary_identity,
        residual_order_forces_boundary_order=forced_order,
    )


def one_boundary_minimum_edge_count(q: int, degree: int, shell_maximum: int) -> int:
    r"""Necessary block size when ordered equal blocks differ by one vertex.

    If the earlier and later ``k``-triangle blocks share ``3k-1`` vertices,
    their unmatched vertices ``x,y`` obey

    ``y/x = prod(q^3+s_i)/prod(q^3+r_i)`` and ``y>=x+1``.

    Since ``x<=U`` and ``|r_i|,|s_i|<=qD``, necessarily

    ``(U+1)/U <= ((q^2+D)/(q^2-D))^k``.

    This routine returns the least integer ``k`` satisfying the cleared
    inequality.  It uses arbitrary-size integers throughout.
    """

    modulus_root = int(q)
    degree_parameter = int(degree)
    upper = int(shell_maximum)
    if modulus_root <= 1 or not 0 < degree_parameter < modulus_root**2:
        raise ValueError("require q>1 and 0<D<q^2")
    if upper <= 0:
        raise ValueError("shell_maximum must be positive")
    lower_base = modulus_root**2 - degree_parameter
    upper_base = modulus_root**2 + degree_parameter
    count = 0
    lower_power = 1
    upper_power = 1
    while (upper + 1) * lower_power > upper * upper_power:
        count += 1
        lower_power *= lower_base
        upper_power *= upper_base
    return count


def distinct_block_square_identity(
    model: Q2ResidueAtomModel,
    blocks: Sequence[ResidualMatchingBlock] | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    r"""Return the two sides of ``sum B_I^2=2 diag(d)+T``.

    Repeated-node atoms are omitted on both sides.  The identity applies to
    any partition into vertex-disjoint blocks, in particular the canonical
    short-residual partition.
    """

    chosen_blocks = (
        short_residual_matching_blocks(model) if blocks is None else tuple(blocks)
    )
    dimension = model.dimension
    left = np.zeros((dimension, dimension), dtype=np.int64)
    carrier = np.zeros_like(left)
    degrees = np.zeros(dimension, dtype=np.int64)
    for block in chosen_blocks:
        distinct_atoms = tuple(atom for atom in block.atoms if atom.all_nodes_distinct)
        matrix = sum(
            (atom.support.astype(np.int64) for atom in distinct_atoms),
            start=csr_matrix((dimension, dimension), dtype=np.int64),
        ).toarray()
        left += matrix @ matrix
        for atom in distinct_atoms:
            carrier += atom.support.toarray()
            degrees[list(atom.vertex_set)] += 1
    right = carrier + 2 * np.diag(degrees)
    return left, right


@dataclass(frozen=True)
class Q2PacketDiscoveryLedger:
    q: int
    degree_parameter: int
    dimension: int
    coarse_atoms: int
    selected_atoms: int
    matching_blocks: int
    maximum_atoms_per_block: int
    cross_block_vertex_overlaps: int
    occupied_block_span: int
    fine_doubly_centered_norm: float
    primitive_doubly_centered_norm: float
    maximum_block_norm: float
    centered_atom_gram_correction_rank: int


def _double_center(matrix: np.ndarray) -> np.ndarray:
    dimension = matrix.shape[0]
    projection = np.eye(dimension) - np.ones((dimension, dimension)) / dimension
    return projection @ matrix @ projection


def q2_packet_discovery_ledger(model: Q2ResidueAtomModel) -> Q2PacketDiscoveryLedger:
    """Compute the finite spectra after principal and degree subtraction."""

    selected = {atom.residual: 1.0 for atom in model.selected_atoms}
    fine = weighted_atom_matrix(model, selected).real
    primitive = weighted_atom_matrix(model, physical_primitive_weights(model)).real
    blocks = short_residual_matching_blocks(model)
    block_norms = [
        float(np.linalg.norm(block_matrix(block, model.dimension).toarray(), ord=2))
        for block in blocks
    ]
    overlaps = block_vertex_overlap_matrix(blocks, model.dimension)
    cross_overlaps = int((np.sum(overlaps) - np.trace(overlaps)) // 2)

    atom_gram = centered_atom_gram_numerator(model)
    sizes = np.asarray([atom.orbit_size for atom in model.atoms], dtype=np.int64)
    uncentered = np.diag(model.dimension**2 * sizes)
    correction_rank = int(np.linalg.matrix_rank((atom_gram - uncentered).astype(float)))
    occupied_span = 0 if not blocks else blocks[-1].index - blocks[0].index + 1
    return Q2PacketDiscoveryLedger(
        q=model.q,
        degree_parameter=model.degree_parameter,
        dimension=model.dimension,
        coarse_atoms=len(model.atoms),
        selected_atoms=len(model.selected_atoms),
        matching_blocks=len(blocks),
        maximum_atoms_per_block=max((len(block.atoms) for block in blocks), default=0),
        cross_block_vertex_overlaps=cross_overlaps,
        occupied_block_span=occupied_span,
        fine_doubly_centered_norm=float(np.linalg.norm(_double_center(fine), ord=2)),
        primitive_doubly_centered_norm=float(
            np.linalg.norm(_double_center(primitive), ord=2)
        ),
        maximum_block_norm=max(block_norms, default=0.0),
        centered_atom_gram_correction_rank=correction_rank,
    )


def primitive_atomic_inverse_budget(q: int) -> tuple[Fraction, Fraction]:
    r"""Return the norm budget of a primitive inverse-DFT residue atom.

    For ``alpha_h=q^-2 e(-h r0/q^2)`` on ``q not| h``, one has

    ``sum |alpha_h|^2=(q-1)/q^3`` and
    ``q sum |alpha_h|^2=(q-1)/q^2``.

    Its physical synthesis is the delta at ``r0`` minus the average on the
    additive fibre ``r=r0 (mod q)``.  Thus a coefficient-uniform square
    theorem with only the second displayed budget cannot hold before an
    atomic/polar term is charged.
    """

    modulus_root = int(q)
    if modulus_root <= 2:
        raise ValueError("q must exceed two")
    energy = Fraction(modulus_root - 1, modulus_root**3)
    return energy, modulus_root * energy


def empirical_log_polynomial_basis(
    values: Sequence[int], q: int, maximum_degree: int
) -> np.ndarray:
    r"""Orthonormalize ``1,x,...,x^d`` for ``x=log(2p/q)`` on the shell."""

    nodes = np.asarray(values, dtype=float).reshape(-1)
    degree = int(maximum_degree)
    if nodes.size == 0 or degree < 0 or degree >= nodes.size:
        raise ValueError("require 0<=degree<number of shell nodes")
    coordinate = np.log(2.0 * nodes / int(q))
    vandermonde = np.column_stack([coordinate**power for power in range(degree + 1)])
    basis, _ = np.linalg.qr(vandermonde)
    return basis


def projected_symmetric_eigenpairs(
    matrix: csr_matrix | np.ndarray,
    removed_basis: np.ndarray,
    *,
    count: int = 6,
) -> tuple[np.ndarray, np.ndarray]:
    """Largest-magnitude eigenpairs of ``P matrix P``."""

    dimension = int(matrix.shape[0])
    if matrix.shape != (dimension, dimension):
        raise ValueError("matrix must be square")
    basis = np.asarray(removed_basis, dtype=float)
    if basis.ndim != 2 or basis.shape[0] != dimension:
        raise ValueError("removed_basis has the wrong shape")
    if not np.allclose(basis.T @ basis, np.eye(basis.shape[1]), atol=1e-10):
        raise ValueError("removed_basis must have orthonormal columns")

    def project(vector: np.ndarray) -> np.ndarray:
        return vector - basis @ (basis.T @ vector)

    def matvec(vector: np.ndarray) -> np.ndarray:
        projected = project(np.asarray(vector, dtype=float).reshape(-1))
        return project(np.asarray(matrix @ projected).reshape(-1))

    number = min(max(1, int(count)), dimension)
    if dimension <= 64 or number >= dimension:
        dense = np.column_stack(
            [matvec(np.eye(dimension)[:, index]) for index in range(dimension)]
        )
        eigenvalues, eigenvectors = np.linalg.eigh(dense)
        order = np.argsort(np.abs(eigenvalues))[::-1][:number]
        return eigenvalues[order], eigenvectors[:, order]
    operator = LinearOperator(
        (dimension, dimension), matvec=matvec, rmatvec=matvec, dtype=float
    )
    number = min(number, dimension - 1)
    eigenvalues, eigenvectors = eigsh(
        operator,
        k=number,
        which="LM",
        v0=np.linspace(1.0, 2.0, dimension),
        tol=1e-10,
        maxiter=30_000,
    )
    order = np.argsort(np.abs(eigenvalues))[::-1]
    return eigenvalues[order], eigenvectors[:, order]


@dataclass(frozen=True)
class LogPolarSpectralLedger:
    dimension: int
    centered_norm: float
    linear_projected_norm: float
    quadratic_projected_norm: float
    most_linear_correlated_eigenvalue: float
    most_linear_correlation_squared: float
    corresponding_degree_eight_polynomial_mass: float


def log_polar_spectral_ledger(
    matrix: csr_matrix | np.ndarray,
    values: Sequence[int],
    q: int,
    *,
    eigen_count: int = 10,
) -> LogPolarSpectralLedger:
    """Measure whether centered extreme modes lie in the logarithmic polar."""

    dimension = len(values)
    maximum_degree = min(8, dimension - 1)
    basis = empirical_log_polynomial_basis(values, q, maximum_degree)
    centered_values, centered_vectors = projected_symmetric_eigenpairs(
        matrix, basis[:, :1], count=eigen_count
    )
    linear_values, _ = projected_symmetric_eigenpairs(
        matrix, basis[:, : min(2, basis.shape[1])], count=1
    )
    quadratic_values, _ = projected_symmetric_eigenpairs(
        matrix, basis[:, : min(3, basis.shape[1])], count=1
    )
    if basis.shape[1] < 2:
        correlations = np.zeros(centered_vectors.shape[1])
    else:
        correlations = np.abs(basis[:, 1] @ centered_vectors) ** 2
    chosen = int(np.argmax(correlations))
    polynomial_mass = float(
        np.sum(np.abs(basis[:, 1:].T @ centered_vectors[:, chosen]) ** 2)
    )
    return LogPolarSpectralLedger(
        dimension=dimension,
        centered_norm=float(np.max(np.abs(centered_values), initial=0.0)),
        linear_projected_norm=float(np.max(np.abs(linear_values), initial=0.0)),
        quadratic_projected_norm=float(np.max(np.abs(quadratic_values), initial=0.0)),
        most_linear_correlated_eigenvalue=float(centered_values[chosen]),
        most_linear_correlation_squared=float(correlations[chosen]),
        corresponding_degree_eight_polynomial_mass=polynomial_mass,
    )


@dataclass(frozen=True)
class BlockLogPolarLedger:
    q: int
    blocks: int
    constant_projected_carrier_norm: float
    linear_projected_carrier_norm: float
    constant_projected_square_function_norm: float
    linear_projected_square_function_norm: float
    constant_projected_ratio: float
    linear_projected_ratio: float
    maximum_constant_projected_cross_norm: float
    maximum_linear_projected_cross_norm: float


def block_log_polar_ledger(model: Q2ResidueAtomModel) -> BlockLogPolarLedger:
    """Compare the unsigned block sum to its square function off ``1,x``."""

    blocks = short_residual_matching_blocks(model)
    matrices = [block_matrix(block, model.dimension).toarray().astype(float) for block in blocks]
    carrier = sum(matrices, start=np.zeros((model.dimension, model.dimension)))
    basis = empirical_log_polynomial_basis(model.values, model.q, 1)

    def one_projection(column_count: int) -> tuple[float, float, float, float]:
        projection = np.eye(model.dimension) - basis[:, :column_count] @ basis[
            :, :column_count
        ].T
        projected_blocks = [projection @ matrix @ projection for matrix in matrices]
        projected_carrier = projection @ carrier @ projection
        square = sum(
            (matrix @ matrix for matrix in projected_blocks),
            start=np.zeros_like(carrier),
        )
        carrier_norm = float(np.linalg.norm(projected_carrier, ord=2))
        square_norm = float(np.sqrt(max(np.linalg.eigvalsh(square)[-1], 0.0)))
        cross_norm = 0.0
        for first_index, first in enumerate(matrices):
            for second in matrices[first_index + 1 :]:
                cross_norm = max(
                    cross_norm,
                    float(
                        np.linalg.norm(
                            projection
                            @ first
                            @ projection
                            @ second
                            @ projection,
                            ord=2,
                        )
                    ),
                )
        ratio = carrier_norm / square_norm if square_norm else 0.0
        return carrier_norm, square_norm, ratio, cross_norm

    constant = one_projection(1)
    linear = one_projection(2)
    return BlockLogPolarLedger(
        q=model.q,
        blocks=len(blocks),
        constant_projected_carrier_norm=constant[0],
        linear_projected_carrier_norm=linear[0],
        constant_projected_square_function_norm=constant[1],
        linear_projected_square_function_norm=linear[1],
        constant_projected_ratio=constant[2],
        linear_projected_ratio=linear[2],
        maximum_constant_projected_cross_norm=constant[3],
        maximum_linear_projected_cross_norm=linear[3],
    )


def matching_block_count_upper_bound(q: int, degree: int, shell_minimum: int) -> int:
    """Number of length-``8m`` blocks meeting ``[-qD,qD]``."""

    if q <= 0 or degree <= 0 or shell_minimum <= 0:
        raise ValueError("all parameters must be positive")
    return ceil((2 * q * degree + 1) / (8 * shell_minimum))
