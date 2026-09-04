"""Walsh and defect coordinates for residual-block four-cycle energy.

The physical weighted carry matrix attached to a linear triple system has

    A[x,y] = z[a]  when {x,y,a} is an accepted triple.

If the triples are partitioned into matching classes and one puts an
independent sign on every class, the signs seen by a two-step walk form a
Walsh character.  Grouping two-step walks by that character gives exact
finite formulas for both the unsigned and randomized Schatten-fourth
traces.

For the QP product mask, a nontrivial two-step walk with fixed endpoints
``x,y`` and intermediate vertex ``v`` has completions ``a,b`` and the
integer defect

    h = x*a - y*b = (rho(v,x,a)-rho(v,y,b))/(8*v).

On the actual narrow prime-power shell, a fixed ``(x,y,h)`` determines at
most one such walk.  Thus a polynomial unsigned/randomized gap forces a
polynomial-size *defect fan*.  It does not, by itself, force that fan into
one affine tangent chart.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from math import ceil, floor, gcd, log2, sqrt
from typing import Mapping, Sequence

import numpy as np


Edge = tuple[int, int, int]
Signature = tuple[int, ...]


@dataclass(frozen=True)
class EntryRecord:
    """The unique class and completion attached to one directed entry."""

    block: int
    completion: int


@dataclass(frozen=True)
class WalshFourthLedger:
    """Exact all-plus and Rademacher fourth traces.

    ``groups[(x,y)][signature]`` is the coefficient of the Walsh character
    seen in the ``(x,y)`` entry of ``A^*A``.  A signature is empty when the
    two matrix entries lie in the same residual block and otherwise is the
    sorted pair of their two block indices.
    """

    groups: Mapping[tuple[int, int], Mapping[Signature, complex]]
    all_plus_fourth: float
    rademacher_fourth: float
    fibre_all_plus: Mapping[tuple[int, int], float]
    fibre_rademacher: Mapping[tuple[int, int], float]


@dataclass(frozen=True)
class EffectiveMultiplicityExtraction:
    """The deterministic high-Walsh-multiplicity extraction ledger."""

    global_effective_multiplicity: float
    threshold: float
    high_fibres: tuple[tuple[int, int], ...]
    high_all_plus_mass: float
    total_all_plus_mass: float
    minimum_signature_support: int


@dataclass(frozen=True)
class CarlesonLayer:
    """One dyadic effective-multiplicity layer."""

    scale: int
    fibres: int
    randomized_mass: float
    all_plus_mass: float


@dataclass(frozen=True)
class FullIntegerTangentWalshLedger:
    """A full-integer tangent packet hostile test.

    This is not an actual odd-prime shell.  It obeys the exact cubic
    product window and residual-block matching rules and has an
    unsigned/randomized gap of order ``order`` while its unsigned fourth
    trace remains of order ``degree_scale=100*order**2``.
    """

    order: int
    center: int
    q: int
    degree_scale: int
    vertices: int
    occupied_blocks: int
    maximum_hyperedge_degree: int
    all_plus_fourth: float
    rademacher_fourth: float
    exact_all_plus_fourth: float
    proved_gap_lower_bound: float
    q_exceeds_degree_squared: bool


@dataclass(frozen=True)
class SupportSensitiveCarlesonLedger:
    """The automatic and genuinely open multiplicity ranges on one bin."""

    degree_scale: int
    support_size: int
    squared_comparability: float
    randomized_scale_factor: float
    automatic_multiplicity_threshold: float
    maximum_defect_multiplicity_scale: int
    high_tail_is_nonempty: bool


@dataclass(frozen=True)
class DefectFanTranslationLedger:
    """A fixed-endpoint defect fan and its most popular translation plane."""

    endpoints: tuple[int, int]
    fan_size: int
    defect_span: int
    freiman_two_isomorphism_certified: bool
    popular_defect_difference: int
    popular_translation_vector: tuple[int, int]
    popular_translation_multiplicity: int
    pigeonhole_multiplicity_lower_bound: int
    affine_color_plane_dimension: int
    all_four_colors_distinct: bool
    all_eight_nodes_distinct: bool


def validate_and_index_classes(
    number_of_vertices: int,
    classes: Sequence[Sequence[Sequence[int]]],
) -> dict[tuple[int, int], EntryRecord]:
    """Index the physical entries of a linear matching partition.

    Each class must be a vertex matching and no unordered vertex pair may
    occur in two hyperedges.  The returned dictionary contains both
    orientations of every off-diagonal matrix entry.
    """

    if number_of_vertices < 0:
        raise ValueError("the number of vertices must be nonnegative")
    entries: dict[tuple[int, int], EntryRecord] = {}
    for block, matching in enumerate(classes):
        used_vertices: set[int] = set()
        for raw_edge in matching:
            edge = tuple(int(value) for value in raw_edge)
            if len(edge) != 3 or len(set(edge)) != 3:
                raise ValueError("every hyperedge must have three distinct vertices")
            if min(edge) < 0 or max(edge) >= number_of_vertices:
                raise ValueError("a hyperedge vertex is outside the ambient set")
            if used_vertices.intersection(edge):
                raise ValueError("every class must be a vertex matching")
            used_vertices.update(edge)
            for first, second in combinations(edge, 2):
                completion = next(value for value in edge if value not in (first, second))
                for directed_pair in ((first, second), (second, first)):
                    if directed_pair in entries:
                        raise ValueError("the triple system is not linear")
                    entries[directed_pair] = EntryRecord(block, completion)
    return entries


def weighted_matrix_from_entries(
    number_of_vertices: int,
    entries: Mapping[tuple[int, int], EntryRecord],
    weights: Sequence[complex],
) -> np.ndarray:
    """Build the full physical weighted matrix from an entry index."""

    z = np.asarray(weights, dtype=complex)
    if z.size != number_of_vertices:
        raise ValueError("weights must have one entry per vertex")
    matrix = np.zeros((number_of_vertices, number_of_vertices), dtype=complex)
    for (first, second), record in entries.items():
        matrix[first, second] = z[record.completion]
    return matrix


def _signature(first_block: int, second_block: int) -> Signature:
    if first_block == second_block:
        return ()
    return tuple(sorted((int(first_block), int(second_block))))


def walsh_fourth_ledger(
    number_of_vertices: int,
    classes: Sequence[Sequence[Sequence[int]]],
    weights: Sequence[complex],
) -> WalshFourthLedger:
    """Return the exact class-sign Walsh decomposition of ``||A||_S4^4``."""

    entries = validate_and_index_classes(number_of_vertices, classes)
    z = np.asarray(weights, dtype=complex)
    if z.size != number_of_vertices:
        raise ValueError("weights must have one entry per vertex")

    grouped: dict[tuple[int, int], dict[Signature, complex]] = {}
    fibre_all_plus: dict[tuple[int, int], float] = {}
    fibre_rademacher: dict[tuple[int, int], float] = {}
    all_plus = 0.0
    randomized = 0.0
    for first in range(number_of_vertices):
        for second in range(number_of_vertices):
            local: defaultdict[Signature, complex] = defaultdict(complex)
            for middle in range(number_of_vertices):
                left = entries.get((middle, first))
                right = entries.get((middle, second))
                if left is None or right is None:
                    continue
                character = _signature(left.block, right.block)
                local[character] += (
                    np.conjugate(z[left.completion]) * z[right.completion]
                )
            if not local:
                continue
            key = (first, second)
            materialized = dict(local)
            grouped[key] = materialized
            unsigned_value = float(abs(sum(materialized.values())) ** 2)
            random_value = float(sum(abs(value) ** 2 for value in materialized.values()))
            fibre_all_plus[key] = unsigned_value
            fibre_rademacher[key] = random_value
            all_plus += unsigned_value
            randomized += random_value
    return WalshFourthLedger(
        groups=grouped,
        all_plus_fourth=all_plus,
        rademacher_fourth=randomized,
        fibre_all_plus=fibre_all_plus,
        fibre_rademacher=fibre_rademacher,
    )


def absolute_weight_fourth_domination(
    number_of_vertices: int,
    classes: Sequence[Sequence[Sequence[int]]],
    weights: Sequence[complex],
) -> tuple[float, float]:
    """Return ``(||A_z||_S4^4, ||A_|z|||_S4^4)``.

    Entrywise triangle inequality in every entry of ``A^*A`` proves that
    the first quantity never exceeds the second.
    """

    entries = validate_and_index_classes(number_of_vertices, classes)
    z = np.asarray(weights, dtype=complex)
    matrix = weighted_matrix_from_entries(number_of_vertices, entries, z)
    positive = weighted_matrix_from_entries(number_of_vertices, entries, np.abs(z))

    def fourth(array: np.ndarray) -> float:
        gram = array.conjugate().T @ array
        return float(np.vdot(gram, gram).real)

    return fourth(matrix), fourth(positive)


def extract_high_effective_multiplicity(
    ledger: WalshFourthLedger,
) -> EffectiveMultiplicityExtraction:
    """Extract fibres above half the global all-plus/randomized ratio.

    For nonnegative physical weights all Walsh coefficients are
    nonnegative.  If ``F=sum F_x`` and ``R=sum R_x``, put ``K=F/R``.
    Fibres with ``F_x/R_x>=K/2`` carry at least ``F/2``.  Cauchy also says
    that each such fibre has at least ``ceil(K/2)`` active signatures.
    """

    total_f = ledger.all_plus_fourth
    total_r = ledger.rademacher_fourth
    if total_r <= 0.0:
        return EffectiveMultiplicityExtraction(0.0, 0.0, (), 0.0, total_f, 0)
    # The extraction is used only after absolute-value domination.  Refuse
    # complex cancellations rather than silently asserting positivity.
    for local in ledger.groups.values():
        if any(abs(value.imag) > 1.0e-10 or value.real < -1.0e-10 for value in local.values()):
            raise ValueError("effective-multiplicity extraction requires nonnegative weights")

    effective = total_f / total_r
    threshold = effective / 2.0
    high: list[tuple[int, int]] = []
    high_mass = 0.0
    minimum_support: int | None = None
    for key, fibre_f in ledger.fibre_all_plus.items():
        fibre_r = ledger.fibre_rademacher[key]
        if fibre_r <= 0.0 or fibre_f / fibre_r + 1.0e-12 < threshold:
            continue
        high.append(key)
        high_mass += fibre_f
        support = sum(abs(value) > 0.0 for value in ledger.groups[key].values())
        minimum_support = support if minimum_support is None else min(minimum_support, support)
    return EffectiveMultiplicityExtraction(
        global_effective_multiplicity=effective,
        threshold=threshold,
        high_fibres=tuple(high),
        high_all_plus_mass=high_mass,
        total_all_plus_mass=total_f,
        minimum_signature_support=minimum_support or 0,
    )


def carleson_layers(ledger: WalshFourthLedger) -> tuple[CarlesonLayer, ...]:
    """Group fibres by dyadic effective Walsh multiplicity.

    On nonnegative weights the sharp fourth-trace theorem is equivalent,
    up to logarithms, to the tail estimate

    ``sum_(m_x in [H,2H)) R_x << D/H``.

    This routine returns the exact finite left sides.
    """

    layers: defaultdict[int, list[float]] = defaultdict(lambda: [0.0, 0.0, 0.0])
    for key, fibre_f in ledger.fibre_all_plus.items():
        fibre_r = ledger.fibre_rademacher[key]
        if fibre_r <= 0.0 or fibre_f <= 0.0:
            continue
        effective = max(1.0, fibre_f / fibre_r)
        scale = 2 ** floor(log2(effective))
        layers[scale][0] += 1.0
        layers[scale][1] += fibre_r
        layers[scale][2] += fibre_f
    return tuple(
        CarlesonLayer(
            scale=scale,
            fibres=int(values[0]),
            randomized_mass=values[1],
            all_plus_mass=values[2],
        )
        for scale, values in sorted(layers.items())
    )


def support_sensitive_carleson_ledger(
    degree_scale: int,
    support_size: int,
    *,
    squared_comparability: float = 4.0,
) -> SupportSensitiveCarlesonLedger:
    """Return the range made automatic by the flat-bin randomized bound.

    Suppressing absolute constants, a comparable bin has randomized budget

    ``D*delta`` with ``delta=min(1,kappa*D/M)``.

    Therefore the desired Carleson estimate ``R_H<=D/H`` is automatic for
    ``H<=1/delta=max(1,M/(kappa*D))``.  Since a physical defect fan has only
    ``O(D)`` possible nonzero defects, there is no open tail when
    ``M>=kappa*D^2``.
    """

    degree = int(degree_scale)
    support = int(support_size)
    kappa = float(squared_comparability)
    if degree <= 0 or support <= 0 or kappa < 1.0:
        raise ValueError("degree, support, and comparability must be positive")
    delta = min(1.0, kappa * degree / support)
    threshold = 1.0 / delta
    return SupportSensitiveCarlesonLedger(
        degree_scale=degree,
        support_size=support,
        squared_comparability=kappa,
        randomized_scale_factor=delta,
        automatic_multiplicity_threshold=threshold,
        maximum_defect_multiplicity_scale=degree,
        high_tail_is_nonempty=threshold < degree,
    )


def schatten_bin_recombination_bound(bin_fourth_powers: Sequence[float]) -> float:
    """Return ``J^3 sum_j ||A_j||_S4^4`` for ``J`` coefficient bins."""

    values = tuple(float(value) for value in bin_fourth_powers)
    if any(value < 0.0 for value in values):
        raise ValueError("fourth powers must be nonnegative")
    return len(values) ** 3 * sum(values)


def defect_fan_translation_ledger(
    first_endpoint: int,
    second_endpoint: int,
    points: Sequence[Sequence[int]],
    *,
    shell_minimum: int,
    shell_maximum: int,
) -> DefectFanTranslationLedger:
    """Certify the Freiman lift and extract a popular translation plane.

    Every point is either ``(h,a,b)`` or ``(h,v,a,b)``, with middle vertex
    ``v`` optional, and satisfies ``h=x*a-y*b``.  Under
    ``2*diam(shell)<min(shell)`` and ``gcd(x,y)=1``, equality of two defect
    differences forces equality of the corresponding vector differences.
    Thus the map ``h -> (a,b)`` is a Freiman two-isomorphism on the fan.

    The first and second completion coordinates are separately injective.
    Deleting cross-coordinate coincidences removes at most ``2N`` ordered
    pairs.  Pigeonholing the remaining at least ``N(N-3)`` four-distinct
    chords among at most ``2*span`` defect differences produces a fixed
    vector translation.  Their row-major color matrices lie in the affine
    two-plane

    ``c11-c21=delta_a, c12-c22=delta_b``.
    """

    x = int(first_endpoint)
    y = int(second_endpoint)
    lower = int(shell_minimum)
    upper = int(shell_maximum)
    if min(x, y, lower) <= 0 or upper < lower or x == y:
        raise ValueError("endpoints and shell must be positive and nondegenerate")
    if not lower <= x <= upper or not lower <= y <= upper:
        raise ValueError("endpoints must lie in the shell")
    if gcd(x, y) != 1:
        raise ValueError("the endpoints must be coprime")
    diameter = upper - lower
    if 2 * diameter >= lower:
        raise ValueError("the doubled shell diameter must be below its minimum")
    raw_points = tuple(tuple(int(value) for value in point) for point in points)
    if any(len(point) not in (3, 4) for point in raw_points):
        raise ValueError("points must be (h,a,b) or (h,v,a,b)")
    has_middles = all(len(point) == 4 for point in raw_points)
    if not has_middles and any(len(point) == 4 for point in raw_points):
        raise ValueError("middle vertices must be supplied for every point or none")
    materialized = tuple(
        (point[0], point[-2], point[-1]) for point in raw_points
    )
    middles = tuple(point[1] for point in raw_points) if has_middles else ()
    if len(materialized) < 2:
        raise ValueError("a defect fan needs at least two points")
    defects = [item[0] for item in materialized]
    if len(set(defects)) != len(defects):
        raise ValueError("defects must be distinct")
    for h, a, b in materialized:
        if not lower <= a <= upper or not lower <= b <= upper:
            raise ValueError("a completion lies outside the shell")
        if x * a - y * b != h:
            raise ValueError("a point does not satisfy its defect equation")

    first_coordinates = [item[1] for item in materialized]
    second_coordinates = [item[2] for item in materialized]
    if len(set(first_coordinates)) != len(first_coordinates):
        raise ValueError("first completion coordinates must be distinct")
    if len(set(second_coordinates)) != len(second_coordinates):
        raise ValueError("second completion coordinates must be distinct")
    if any(first == second for first, second in zip(first_coordinates, second_coordinates)):
        raise ValueError("the two completions in one wedge must be distinct")
    if has_middles:
        if len(set(middles)) != len(middles):
            raise ValueError("middle vertices must be distinct")
        for middle, (_, first, second) in zip(middles, materialized):
            if not lower <= middle <= upper:
                raise ValueError("a middle vertex lies outside the shell")
            if len({x, y, middle, first, second}) != 5:
                raise ValueError("each nontrivial wedge must have five distinct nodes")

    translations: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    four_distinct: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    eight_distinct: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for first_index, first in enumerate(materialized):
        for second_index, second in enumerate(materialized):
            if first_index == second_index:
                continue
            h1, a1, b1 = first
            h2, a2, b2 = second
            translations[h1 - h2].append((a1 - a2, b1 - b2))
            if len({a1, b1, a2, b2}) == 4:
                four_distinct[h1 - h2].append((a1 - a2, b1 - b2))
                if has_middles and len(
                    {x, y, middles[first_index], middles[second_index], a1, b1, a2, b2}
                ) == 8:
                    eight_distinct[h1 - h2].append((a1 - a2, b1 - b2))
    for vectors in translations.values():
        if len(set(vectors)) != 1:
            raise AssertionError("the defect map failed its Freiman difference lift")
    if not four_distinct:
        raise ValueError("the fan has no four-distinct ordered chord")
    eligible = eight_distinct if has_middles else four_distinct
    if has_middles and not eight_distinct:
        raise ValueError("the fan has no all-eight-distinct ordered chord")
    popular_difference, vectors = max(eligible.items(), key=lambda item: len(item[1]))
    popular_vector = vectors[0]
    span = max(defects) - min(defects)
    if span <= 0:
        raise AssertionError("distinct defects must have positive span")
    # Cross equalities a_i=b_j and b_i=a_j remove at most N pairs each.
    # With middles, four additional ordered cross-equalities v_i=a_j,
    # a_i=v_j, v_i=b_j, b_i=v_j each remove at most N more.
    deletion_constant = 7 if has_middles else 3
    good_pair_lower_bound = max(
        0, len(materialized) * (len(materialized) - deletion_constant)
    )
    lower_bound = ceil(good_pair_lower_bound / (2 * span))
    if len(vectors) < lower_bound:
        raise AssertionError("difference pigeonhole lower bound failed")
    return DefectFanTranslationLedger(
        endpoints=(x, y),
        fan_size=len(materialized),
        defect_span=span,
        freiman_two_isomorphism_certified=True,
        popular_defect_difference=popular_difference,
        popular_translation_vector=popular_vector,
        popular_translation_multiplicity=len(vectors),
        pigeonhole_multiplicity_lower_bound=lower_bound,
        affine_color_plane_dimension=2,
        all_four_colors_distinct=True,
        all_eight_nodes_distinct=has_middles,
    )


def translation_plane_weight_mass(
    weights: Mapping[int, complex], first_shift: int, second_shift: int
) -> tuple[float, float]:
    """Return one affine translation-plane mass and its ``||z||_2^4`` bound.

    The plane is

    ``c11-c21=first_shift, c12-c22=second_shift``.

    Extending the weights by zero, its full positive quartic factors into
    two autocorrelations.  Cauchy bounds each by ``||z||_2^2``.
    """

    absolute = {int(index): abs(complex(value)) for index, value in weights.items()}
    norm_squared = sum(value * value for value in absolute.values())

    def correlation(shift: int) -> float:
        return sum(
            value * absolute.get(index + int(shift), 0.0)
            for index, value in absolute.items()
        )

    mass = correlation(first_shift) * correlation(second_shift)
    return mass, norm_squared * norm_squared


def full_integer_tangent_walsh_fixture(
    order: int, center: int
) -> FullIntegerTangentWalshLedger:
    """Build the exact affine tangent packet in residual-block coordinates.

    For ``0<=i,j<L`` use

    ``a_i=m+i, b_j=m+2L+j, c_ij=m-2L-i-j``.

    The coefficient vector is flat on the ``2L-1`` color vertices and zero
    on the row and column vertices.  The all-plus matrix is therefore the
    symmetric bipartization of an ``L`` square constant matrix.
    """

    length = int(order)
    m = int(center)
    if length < 2 or m <= 4 * length:
        raise ValueError("the order must be at least two and the center large")
    q = 2 * m
    degree = 100 * length * length
    raw_edges: list[tuple[tuple[int, int, int], int]] = []
    values: set[int] = set()
    color_values: set[int] = set()
    residual_limit = q * degree
    for row_offset in range(length):
        first = m + row_offset
        for column_offset in range(length):
            second = m + 2 * length + column_offset
            completion = m - 2 * length - row_offset - column_offset
            edge = tuple(sorted((first, second, completion)))
            residual = product_residual(q, *edge)
            if abs(residual) > residual_limit:
                raise AssertionError("the tangent edge escaped the product window")
            raw_edges.append((edge, residual // q))
            values.update(edge)
            color_values.add(completion)

    ordered_values = tuple(sorted(values))
    index = {value: position for position, value in enumerate(ordered_values)}
    grouped_edges: defaultdict[int, list[Edge]] = defaultdict(list)
    degrees = np.zeros(len(ordered_values), dtype=int)
    for edge, block in raw_edges:
        indexed = tuple(index[value] for value in edge)
        grouped_edges[block].append(indexed)
        for vertex in indexed:
            degrees[vertex] += 1
    classes = tuple(tuple(edges) for _, edges in sorted(grouped_edges.items()))
    weights = np.zeros(len(ordered_values), dtype=float)
    normalization = sqrt(len(color_values))
    for value in color_values:
        weights[index[value]] = 1.0 / normalization

    replay = walsh_fourth_ledger(len(ordered_values), classes, weights)
    exact_all_plus = 2.0 * length**4 / (2 * length - 1) ** 2
    if not np.isclose(replay.all_plus_fourth, exact_all_plus):
        raise AssertionError("the tangent bipartization identity failed")
    maximum_degree = int(degrees.max(initial=0))
    # The universal Rademacher theorem gives R<=42*Delta for ||z||_2=1.
    proved_gap = exact_all_plus / (42.0 * maximum_degree)
    return FullIntegerTangentWalshLedger(
        order=length,
        center=m,
        q=q,
        degree_scale=degree,
        vertices=len(ordered_values),
        occupied_blocks=len(classes),
        maximum_hyperedge_degree=maximum_degree,
        all_plus_fourth=replay.all_plus_fourth,
        rademacher_fourth=replay.rademacher_fourth,
        exact_all_plus_fourth=exact_all_plus,
        proved_gap_lower_bound=proved_gap,
        q_exceeds_degree_squared=q > degree * degree,
    )


def product_residual(q: int, first: int, second: int, completion: int) -> int:
    """Return ``8*first*second*completion-q^3``."""

    return 8 * int(first) * int(second) * int(completion) - int(q) ** 3


def physical_wedge_defect(
    q: int,
    middle: int,
    first_endpoint: int,
    second_endpoint: int,
    first_completion: int,
    second_completion: int,
) -> tuple[int, int, int]:
    """Return ``(h, r-s, 8*middle*h)`` for one physical two-step walk."""

    h = int(first_endpoint) * int(first_completion) - int(second_endpoint) * int(
        second_completion
    )
    first_residual = product_residual(
        q, middle, first_endpoint, first_completion
    )
    second_residual = product_residual(
        q, middle, second_endpoint, second_completion
    )
    return h, first_residual - second_residual, 8 * int(middle) * h


def fixed_endpoint_defect_is_injective(
    first_endpoint: int,
    second_endpoint: int,
    first_pair: tuple[int, int],
    second_pair: tuple[int, int],
    *,
    shell_diameter: int,
    shell_minimum: int,
) -> bool:
    """Certify uniqueness of completions at a fixed endpoint defect.

    The proof uses ``gcd(x,y)=1`` and ``diam(shell)<min(shell)``.  If two
    completion pairs have the same defect, their difference is an integer
    multiple of ``(y,x)``, too long to remain in the shell unless it is
    zero.
    """

    x = int(first_endpoint)
    y = int(second_endpoint)
    if x <= 0 or y <= 0 or x == y:
        raise ValueError("endpoints must be distinct and positive")
    if np.gcd(x, y) != 1:
        raise ValueError("the two endpoints must be coprime")
    if shell_diameter < 0 or shell_minimum <= 0 or shell_diameter >= shell_minimum:
        raise ValueError("the shell must have diameter smaller than its minimum")
    a, b = (int(value) for value in first_pair)
    c, d = (int(value) for value in second_pair)
    first_defect = x * a - y * b
    second_defect = x * c - y * d
    if first_defect != second_defect:
        return True
    if max(abs(a - c), abs(b - d)) > shell_diameter:
        raise ValueError("the supplied pairs do not lie in the advertised shell")
    return (a, b) == (c, d)
