"""Exact Pluecker and tangent-ruling algebra for QP four-cycles.

The routines here are finite integer identities.  They distinguish the
genuine tangent degeneracy (a rank-one ruling direction in a fixed
common-level/determinant quadric) from the nonzero fixed-secant conic
invariant ``L**2 + det(K)*det(E)``.

Nothing in this module asserts the still-open global four-cycle estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt
from typing import Iterable, Sequence


Vector2 = tuple[int, int]
Matrix2 = tuple[int, int, int, int]


def determinant(matrix: Sequence[int]) -> int:
    """Return the determinant of a row-major two-by-two matrix."""

    if len(matrix) != 4:
        raise ValueError("a two-by-two matrix needs four entries")
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def outer(left: Vector2, right: Vector2) -> Matrix2:
    """Return the row-major outer product ``left*right^T``."""

    return (
        left[0] * right[0],
        left[0] * right[1],
        left[1] * right[0],
        left[1] * right[1],
    )


def subtract(left: Sequence[int], right: Sequence[int]) -> Matrix2:
    """Subtract two two-by-two matrices entrywise."""

    if len(left) != 4 or len(right) != 4:
        raise ValueError("two two-by-two matrices are required")
    return tuple(x - y for x, y in zip(left, right))  # type: ignore[return-value]


def add_scaled(base: Sequence[int], direction: Sequence[int], scale: int) -> Matrix2:
    """Return ``base + scale*direction`` entrywise."""

    if len(base) != 4 or len(direction) != 4:
        raise ValueError("two two-by-two matrices are required")
    return tuple(x + scale * y for x, y in zip(base, direction))  # type: ignore[return-value]


def frobenius(left: Sequence[int], right: Sequence[int]) -> int:
    """Return the entrywise pairing of two matrices."""

    if len(left) != 4 or len(right) != 4:
        raise ValueError("two two-by-two matrices are required")
    return sum(x * y for x, y in zip(left, right))


def determinant_polar(left: Sequence[int], right: Sequence[int]) -> int:
    """Return the polarization of the two-by-two determinant.

    It is the coefficient of ``t`` in ``det(left+t*right)``.
    """

    if len(left) != 4 or len(right) != 4:
        raise ValueError("two two-by-two matrices are required")
    a, b, c, d = left
    x, y, z, w = right
    return a * w + x * d - b * z - y * c


def bilinear(matrix: Sequence[int], left: Vector2, right: Vector2) -> int:
    """Return ``left^T matrix right``."""

    if len(matrix) != 4:
        raise ValueError("a two-by-two matrix is required")
    a, b, c, d = matrix
    return left[0] * (a * right[0] + b * right[1]) + left[1] * (
        c * right[0] + d * right[1]
    )


def signed_color_form(colors: Sequence[int]) -> Matrix2:
    """Return ``K=(c11,-c12;-c21,c22)``."""

    if len(colors) != 4:
        raise ValueError("four oriented colors are required")
    c11, c12, c21, c22 = colors
    return (c11, -c12, -c21, c22)


@dataclass(frozen=True)
class PluckerLedger:
    """The exact two-by-two bilinear Pluecker ledger."""

    first_level: int
    second_level: int
    first_cross_level: int
    second_cross_level: int
    color_determinant: int
    row_determinant: int
    column_determinant: int
    energy_determinant: int
    plucker_left: int
    plucker_right: int
    full_conic_parameter: int


def plucker_ledger(
    matrix: Matrix2,
    first_row: Vector2,
    second_row: Vector2,
    first_column: Vector2,
    second_column: Vector2,
) -> PluckerLedger:
    """Compute and fail-closed verify the bilinear Pluecker identities."""

    first_level = bilinear(matrix, first_row, first_column)
    second_level = bilinear(matrix, second_row, second_column)
    first_cross = bilinear(matrix, first_row, second_column)
    second_cross = bilinear(matrix, second_row, first_column)
    row_det = first_row[0] * second_row[1] - first_row[1] * second_row[0]
    column_det = (
        first_column[0] * second_column[1]
        - first_column[1] * second_column[0]
    )
    energy = subtract(
        outer(first_row, first_column), outer(second_row, second_column)
    )
    energy_det = determinant(energy)
    color_det = determinant(matrix)
    left = first_level * second_level - first_cross * second_cross
    right = color_det * row_det * column_det
    if left != right:
        raise AssertionError("the bilinear Pluecker identity failed")
    if energy_det != -row_det * column_det:
        raise AssertionError("the product-difference determinant failed")
    full_parameter = first_cross * second_cross
    if first_level == second_level:
        if full_parameter != first_level * first_level + color_det * energy_det:
            raise AssertionError("the equal-level cross-factor identity failed")
    return PluckerLedger(
        first_level=first_level,
        second_level=second_level,
        first_cross_level=first_cross,
        second_cross_level=second_cross,
        color_determinant=color_det,
        row_determinant=row_det,
        column_determinant=column_det,
        energy_determinant=energy_det,
        plucker_left=left,
        plucker_right=right,
        full_conic_parameter=full_parameter,
    )


@dataclass(frozen=True)
class RulingCertificate:
    """Exact invariants of an affine line in a determinant layer."""

    base_level: int
    direction_level: int
    base_determinant: int
    direction_determinant: int
    determinant_polar: int
    sampled_determinants: tuple[int, int, int]

    @property
    def is_tangent_ruling(self) -> bool:
        return (
            self.direction_level == 0
            and self.direction_determinant == 0
            and self.determinant_polar == 0
            and len(set(self.sampled_determinants)) == 1
        )


def ruling_certificate(
    matrix: Matrix2, base: Matrix2, direction: Matrix2
) -> RulingCertificate:
    """Return the tangent-ruling invariants for ``base+t*direction``."""

    sampled = tuple(
        determinant(add_scaled(base, direction, parameter))
        for parameter in (0, 1, 2)
    )
    certificate = RulingCertificate(
        base_level=frobenius(matrix, base),
        direction_level=frobenius(matrix, direction),
        base_determinant=determinant(base),
        direction_determinant=determinant(direction),
        determinant_polar=determinant_polar(base, direction),
        sampled_determinants=sampled,  # type: ignore[arg-type]
    )
    # Three equal samples of the quadratic determinant force both its linear
    # and quadratic coefficients to vanish.
    if len(set(sampled)) == 1 and (
        certificate.direction_determinant != 0
        or certificate.determinant_polar != 0
    ):
        raise AssertionError("three-point determinant ruling inverse failed")
    return certificate


@dataclass(frozen=True)
class SecantMidpointCertificate:
    """Midpoint normal form for two points on one determinant quadric."""

    determinant_level: int
    displacement_determinant: int
    midpoint_determinant: int
    expected_midpoint_determinant: int
    midpoint_level: int
    midpoint_displacement_polar: int


def secant_midpoint_certificate(
    matrix: Matrix2, base: Matrix2, displacement: Matrix2
) -> SecantMidpointCertificate:
    """Certify the binary-norm midpoint reduction for a quadric secant.

    The hypotheses are

    ``<K,E>=<K,V>=0`` and ``det(E+V)=det(E)=Delta``.

    For ``Y=2E+V`` the exact conclusions are

    ``<K,Y>=0``, ``B_det(Y,V)=0``, and
    ``det(Y)=4*Delta-det(V)``.

    If ``det(K)*det(V)`` and the final right side are nonzero, the remaining
    two-dimensional lattice equation is a nondegenerate binary norm
    equation.  The analytic ``q^o(1)`` count is intentionally not encoded in
    this finite routine.
    """

    if frobenius(matrix, base) != 0 or frobenius(matrix, displacement) != 0:
        raise ValueError("the base and displacement must lie on the K-level")
    translated = add_scaled(base, displacement, 1)
    delta = determinant(base)
    if determinant(translated) != delta:
        raise ValueError("the translated point has a different determinant")
    midpoint = tuple(2 * x + y for x, y in zip(base, displacement))
    displacement_det = determinant(displacement)
    certificate = SecantMidpointCertificate(
        determinant_level=delta,
        displacement_determinant=displacement_det,
        midpoint_determinant=determinant(midpoint),
        expected_midpoint_determinant=4 * delta - displacement_det,
        midpoint_level=frobenius(matrix, midpoint),
        midpoint_displacement_polar=determinant_polar(
            midpoint, displacement
        ),
    )
    if certificate.midpoint_determinant != certificate.expected_midpoint_determinant:
        raise AssertionError("the secant midpoint determinant identity failed")
    if certificate.midpoint_level != 0:
        raise AssertionError("the midpoint left the K-level")
    if certificate.midpoint_displacement_polar != 0:
        raise AssertionError("the midpoint is not polar-orthogonal to the displacement")
    return certificate


def antipodal_degenerate_fiber(parameter: int) -> tuple[Matrix2, Matrix2, Matrix2]:
    """Return an exact ``det(V)=4*Delta`` tangent-line fiber.

    With ``K=(1,0;0,-1)``, ``Delta=1``, and ``V=2I``, the matrices

    ``E_t=(-1,t;0,-1)`` and ``E_t+V=(1,t;0,1)``

    both have determinant one and level zero.  As ``t`` varies, the fiber is
    one of the tangent lines appearing when the midpoint norm right side
    ``4*Delta-det(V)`` vanishes.
    """

    matrix = (1, 0, 0, -1)
    base = (-1, parameter, 0, -1)
    displacement = (2, 0, 0, 2)
    certificate = secant_midpoint_certificate(matrix, base, displacement)
    if certificate.determinant_level != 1:
        raise AssertionError("the antipodal fiber has the wrong determinant")
    if certificate.displacement_determinant != 4:
        raise AssertionError("the antipodal displacement has the wrong determinant")
    if certificate.midpoint_determinant != 0:
        raise AssertionError("the antipodal midpoint is not null")
    return matrix, base, displacement


@dataclass(frozen=True)
class SharedEdgeCrossCertificate:
    """Six-product certificate for one Cartesian pair of edge neighbors."""

    target: int
    residual_cap: int
    residuals: tuple[int, int, int, int, int, int]
    cross_determinant: int
    identity_left: int
    identity_right: int
    telescoping_upper_bound: int
    determinant_coefficient: int
    cross_determinant_upper_bound: int


def shared_edge_cross_certificate(
    q: int,
    D_window: int,
    *,
    base_row: int,
    first_center: int,
    second_center: int,
    first_color: int,
    second_color: int,
    left_row: int,
    left_first_color: int,
    left_second_color: int,
    right_row: int,
    right_first_center: int,
    right_second_center: int,
) -> SharedEdgeCrossCertificate:
    """Certify the cross-neighbor determinant strip around one edge.

    The three physical transitions are

    ``(a,b,c),(a,B,C)``, ``(x,b,d),(x,B,D)``, and
    ``(y,e,c),(y,E,C)``.

    Multiplying the first entry from the left and right arms with the second
    base entry, and subtracting the opposite product, gives exactly

    ``512*a*x*y*b*B*c*C*(d*e-D*E)``.

    Thus six hard-window inequalities force ``|d*e-D*E|=O(D_window)`` for
    *every* Cartesian pair of left and right neighbors, whether or not the
    missing cross transition is present.
    """

    coordinates = (
        q,
        base_row,
        first_center,
        second_center,
        first_color,
        second_color,
        left_row,
        left_first_color,
        left_second_color,
        right_row,
        right_first_center,
        right_second_center,
    )
    if min(coordinates) <= 0 or D_window < 0:
        raise ValueError("physical coordinates must be positive")
    target = q**3
    cap = q * D_window
    products = (
        8 * base_row * first_center * first_color,
        8 * base_row * second_center * second_color,
        8 * left_row * first_center * left_first_color,
        8 * left_row * second_center * left_second_color,
        8 * right_row * right_first_center * first_color,
        8 * right_row * right_second_center * second_color,
    )
    residuals = tuple(value - target for value in products)
    if any(abs(value) > cap for value in residuals):
        raise ValueError("one of the three transitions leaves the hard window")
    r_bc, r_BC, r_bd, r_BD, r_ec, r_EC = residuals
    identity_left = (
        (target + r_bd) * (target + r_ec) * (target + r_BC)
        - (target + r_BD) * (target + r_EC) * (target + r_bc)
    )
    cross = (
        left_first_color * right_first_center
        - left_second_color * right_second_center
    )
    coefficient = (
        512
        * base_row
        * left_row
        * right_row
        * first_center
        * second_center
        * first_color
        * second_color
    )
    identity_right = coefficient * cross
    if identity_left != identity_right:
        raise AssertionError("the six-product cross identity failed")
    # Three-factor telescoping, with each paired residual difference at most
    # 2*cap and every product factor at most target+cap.
    telescoping = 6 * cap * (target + cap) ** 2
    if abs(identity_left) > telescoping:
        raise AssertionError("the telescoping hard-window bound failed")
    cross_upper_bound = (telescoping + coefficient - 1) // coefficient
    if abs(cross) > cross_upper_bound:
        raise AssertionError("the cross determinant escaped its certified bound")
    return SharedEdgeCrossCertificate(
        target=target,
        residual_cap=cap,
        residuals=residuals,  # type: ignore[arg-type]
        cross_determinant=cross,
        identity_left=identity_left,
        identity_right=identity_right,
        telescoping_upper_bound=telescoping,
        determinant_coefficient=coefficient,
        cross_determinant_upper_bound=cross_upper_bound,
    )


@dataclass(frozen=True)
class SharedEdgeArmLedger:
    """Completed versus open Cartesian arm pairs at one graph edge."""

    left_degree: int
    right_degree: int
    edge_degree_product: int
    noncentral_arm_pairs: int
    completed_noncentral_arm_pairs: int


def shared_edge_arm_ledger(
    edges: Iterable[tuple[Vector2, Vector2]], central: tuple[Vector2, Vector2]
) -> SharedEdgeArmLedger:
    """Count the arm pairs visible and invisible to four-cycle Pluecker."""

    support = set(edges)
    if central not in support:
        raise ValueError("the central edge is absent")
    center_vertex, color_vertex = central
    color_neighbors = {gamma for p, gamma in support if p == center_vertex}
    center_neighbors = {p for p, gamma in support if gamma == color_vertex}
    left_arms = color_neighbors - {color_vertex}
    right_arms = center_neighbors - {center_vertex}
    completed = sum((p, gamma) in support for p in right_arms for gamma in left_arms)
    return SharedEdgeArmLedger(
        left_degree=len(color_neighbors),
        right_degree=len(center_neighbors),
        edge_degree_product=len(color_neighbors) * len(center_neighbors),
        noncentral_arm_pairs=len(left_arms) * len(right_arms),
        completed_noncentral_arm_pairs=completed,
    )


@dataclass(frozen=True)
class AffineArmFiberCertificate:
    """One-sided affine-packet closure of a determinant-strip product."""

    packet_length: int
    cross_determinant_cap: int
    direction_fiber_radius: int
    direction_fiber_count: int
    maximum_fiber_occupancy: int
    opposite_population: int
    population_ceiling: int
    degree_product: int
    degree_product_ceiling: int


def _cross_form(left: Vector2, right: Vector2) -> int:
    """Return the shared-edge cross determinant ``d*e-D*E``."""

    return left[0] * right[0] - left[1] * right[1]


def affine_arm_fiber_certificate(
    affine_arm: Sequence[Vector2], opposite_arm: Sequence[Vector2]
) -> AffineArmFiberCertificate:
    """Prove RDP for one affine arm modulo parallel-fiber occupancy.

    The affine arm must be the complete arithmetic progression
    ``u_t=u_0+t*p``.  Put

    ``K=max_(u,v)|u_1*v_1-u_2*v_2|``.

    For every opposite vector ``v``, subtracting the two endpoint values
    gives

    ``(L-1)*|p_1*v_1-p_2*v_2| <= 2K``.

    Hence the opposite arm occupies at most
    ``2*floor(2K/(L-1))+1`` integral direction fibers.  If each fiber has
    occupancy at most ``R``, then

    ``L*|V| <= L*R*(2*floor(2K/(L-1))+1)=O(KR)``.

    A high-occupancy fiber is an affine line whose direction ``w`` satisfies
    ``p_1*w_1-p_2*w_2=0``: precisely the parallel/rank-one ruling that must be
    merged.  This theorem does not treat two scattered arms.
    """

    arm = tuple(affine_arm)
    opposite = tuple(opposite_arm)
    if len(arm) < 2:
        raise ValueError("the affine arm needs at least two points")
    direction = (arm[1][0] - arm[0][0], arm[1][1] - arm[0][1])
    if direction == (0, 0):
        raise ValueError("the affine direction must be nonzero")
    if any(
        point
        != (
            arm[0][0] + index * direction[0],
            arm[0][1] + index * direction[1],
        )
        for index, point in enumerate(arm)
    ):
        raise ValueError("the first arm is not a complete affine progression")
    cross_cap = max(
        (abs(_cross_form(left, right)) for left in arm for right in opposite),
        default=0,
    )
    radius = (2 * cross_cap) // (len(arm) - 1)
    fibers: dict[int, int] = {}
    for vector in opposite:
        token = _cross_form(direction, vector)
        if abs(token) > radius:
            raise AssertionError("endpoint subtraction failed")
        fibers[token] = fibers.get(token, 0) + 1
    fiber_count = 2 * radius + 1
    maximum_fiber = max(fibers.values(), default=0)
    population_ceiling = maximum_fiber * fiber_count
    if len(opposite) > population_ceiling:
        raise AssertionError("the affine fiber population bound failed")
    return AffineArmFiberCertificate(
        packet_length=len(arm),
        cross_determinant_cap=cross_cap,
        direction_fiber_radius=radius,
        direction_fiber_count=fiber_count,
        maximum_fiber_occupancy=maximum_fiber,
        opposite_population=len(opposite),
        population_ceiling=population_ceiling,
        degree_product=len(arm) * len(opposite),
        degree_product_ceiling=len(arm) * population_ceiling,
    )


@dataclass(frozen=True)
class PhysicalAffineTransitionGrid:
    """A literal hard-window affine transition biclique."""

    q: int
    D_window: int
    packet_length: int
    witnesses: tuple[tuple[Vector2, Vector2, int], ...]
    maximum_product_residual: int
    maximum_transition_determinant: int

    @property
    def edges(self) -> tuple[tuple[Vector2, Vector2], ...]:
        return tuple((centers, colors) for centers, colors, _ in self.witnesses)


def physical_affine_transition_grid(
    packet_length: int, *, midpoint: int | None = None
) -> PhysicalAffineTransitionGrid:
    """Construct a complete physical ``L``-by-``L`` affine packet.

    Put ``D=512 L^2``, ``q=2m`` and, for
    ``0<=i<L``, ``2L<=j<3L``,

    ``p_i=(m+2i,m+2i+1)``,
    ``gamma_j=(m+2j+2,m+2j+1)``,
    ``a_ij=m-2i-2j-2``.

    Both triples on every transition have coordinate sum ``3m``.  Their
    product errors are inside the literal window, while

    ``det_transition=2(i-j)-1``

    is always nonzero.  The construction is a full-integer physical model,
    not an actual-prime-power model.
    """

    if packet_length < 2:
        raise ValueError("packet_length must be at least two")
    L = packet_length
    D_window = 512 * L * L
    m = midpoint if midpoint is not None else D_window * D_window
    if m <= 100 * L:
        raise ValueError("the midpoint must dominate the affine offsets")
    q = 2 * m
    target = q**3
    cap = q * D_window
    witnesses: list[tuple[Vector2, Vector2, int]] = []
    maximum_residual = 0
    maximum_transition = 0
    for i in range(L):
        centers = (m + 2 * i, m + 2 * i + 1)
        for j in range(2 * L, 3 * L):
            colors = (m + 2 * j + 2, m + 2 * j + 1)
            row = m - 2 * i - 2 * j - 2
            residuals = (
                8 * row * centers[0] * colors[0] - target,
                8 * row * centers[1] * colors[1] - target,
            )
            if max(abs(value) for value in residuals) > cap:
                raise AssertionError("the affine packet escaped the hard window")
            transition = centers[0] * colors[0] - centers[1] * colors[1]
            if transition != 2 * (i - j) - 1 or transition == 0:
                raise AssertionError("the affine transition determinant is wrong")
            maximum_residual = max(
                maximum_residual, *(abs(value) for value in residuals)
            )
            maximum_transition = max(maximum_transition, abs(transition))
            witnesses.append((centers, colors, row))
    return PhysicalAffineTransitionGrid(
        q=q,
        D_window=D_window,
        packet_length=L,
        witnesses=tuple(witnesses),
        maximum_product_residual=maximum_residual,
        maximum_transition_determinant=maximum_transition,
    )


def affine_double_star(
    grid: PhysicalAffineTransitionGrid,
) -> tuple[tuple[Vector2, Vector2], ...]:
    """Delete a physical affine biclique down to its central double star."""

    first_centers, first_colors, _ = grid.witnesses[0]
    return tuple(
        (centers, colors)
        for centers, colors, _ in grid.witnesses
        if centers == first_centers or colors == first_colors
    )


@dataclass(frozen=True)
class RankOneDoubleStarLedger:
    """A mask-preserving no-go to necessity of edge degree-product.

    The central left vertex has ``left_degree`` directed-matching color
    neighbors.  The central color pair has ``right_degree`` left neighbors;
    all remaining vertices are leaves.  Thus all off-diagonal codegrees are
    at most one, while the central edge-degree product can be arbitrarily
    large.
    """

    left_degree: int
    right_degree: int
    central_degree_product: int
    maximum_left_codegree: int
    maximum_right_codegree: int
    maximum_neighbor_degree_sum: int
    edges: tuple[tuple[int, int], ...]
    color_pairs: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class AnchoredCodegreeLedger:
    """First and second anchored codegree moments in a bipartite mask."""

    anchor: Vector2
    partner_count: int
    first_moment: int
    second_moment: int
    maximum_codegree: int
    determinant_layers: tuple[int, ...]
    determinant_layers_are_distinct: bool


@dataclass(frozen=True)
class TaggedParabolaProjectionLedger:
    """Exact no-go for projecting away a convolution tag coordinate."""

    tag_count: int
    fiber_size: int
    total_points: int
    tagged_additive_energy: int
    zero_tag_off_diagonal_mass: int
    projected_off_diagonal_mass: int
    projection_multiplicity_loss: int


def tagged_parabola_projection_ledger(
    tag_count: int, fiber_size: int
) -> TaggedParabolaProjectionLedger:
    """Return the product-of-parabolas projection obstruction.

    Use the finite set

    ``S={(r,r^2,t,t^2):0<=r<P, 0<=t<K}``.

    A one-dimensional parabola has additive energy ``2*n^2-n`` because
    its sum and sum of squares determine the unordered input pair.  Hence
    ``S`` has near-diagonal energy, while the zero-tag difference slice has
    ``P*K*(K-1)`` ordered off-diagonal pairs.  Projecting away the first
    two coordinates turns the indicator into the multiplicity-``P``
    function and multiplies that slice by another factor ``P``.
    """

    if tag_count < 1 or fiber_size < 1:
        raise ValueError("tag_count and fiber_size must be positive")
    tagged_energy = (
        (2 * tag_count * tag_count - tag_count)
        * (2 * fiber_size * fiber_size - fiber_size)
    )
    zero_tag = tag_count * fiber_size * (fiber_size - 1)
    projected = tag_count * tag_count * fiber_size * (fiber_size - 1)
    return TaggedParabolaProjectionLedger(
        tag_count=tag_count,
        fiber_size=fiber_size,
        total_points=tag_count * fiber_size,
        tagged_additive_energy=tagged_energy,
        zero_tag_off_diagonal_mass=zero_tag,
        projected_off_diagonal_mass=projected,
        projection_multiplicity_loss=tag_count,
    )


def anchored_codegree_ledger(
    edges: Iterable[tuple[Vector2, Vector2]], anchor: Vector2
) -> AnchoredCodegreeLedger:
    """Compute ``sum codeg`` and ``sum codeg^2`` at one right vertex."""

    support = set(edges)
    anchor_left = {left for left, right in support if right == anchor}
    if not anchor_left:
        raise ValueError("the anchor has no incident edge")
    partners = sorted(
        {right for left, right in support if left in anchor_left}
    )
    codegrees = tuple(
        len(anchor_left & {left for left, edge_right in support if edge_right == right})
        for right in partners
    )
    layers = tuple(
        anchor[0] * right[1] - anchor[1] * right[0]
        for right in partners
    )
    return AnchoredCodegreeLedger(
        anchor=anchor,
        partner_count=len(partners),
        first_moment=sum(codegrees),
        second_moment=sum(value * value for value in codegrees),
        maximum_codegree=max(codegrees),
        determinant_layers=layers,
        determinant_layers_are_distinct=len(set(layers)) == len(layers),
    )


def rank_one_double_star_ledger(
    left_degree: int, right_degree: int
) -> RankOneDoubleStarLedger:
    """Construct the exact directed-matching double-star certificate."""

    if left_degree < 1 or right_degree < 1:
        raise ValueError("both central degrees must be positive")
    edges = tuple(
        sorted(
            {(0, gamma) for gamma in range(left_degree)}
            | {(left, 0) for left in range(right_degree)}
        )
    )
    color_pairs = tuple(
        (gamma, left_degree + gamma) for gamma in range(left_degree)
    )
    left_neighbors = {
        left: {gamma for edge_left, gamma in edges if edge_left == left}
        for left in range(right_degree)
    }
    right_neighbors = {
        gamma: {left for left, edge_gamma in edges if edge_gamma == gamma}
        for gamma in range(left_degree)
    }
    maximum_left_codegree = max(
        (
            len(left_neighbors[first] & left_neighbors[second])
            for first in range(right_degree)
            for second in range(first + 1, right_degree)
        ),
        default=0,
    )
    maximum_right_codegree = max(
        (
            len(right_neighbors[first] & right_neighbors[second])
            for first in range(left_degree)
            for second in range(first + 1, left_degree)
        ),
        default=0,
    )
    left_degrees = {left: len(neighbors) for left, neighbors in left_neighbors.items()}
    maximum_neighbor_degree_sum = max(
        sum(left_degrees[left] for left in neighbors)
        for neighbors in right_neighbors.values()
    )
    return RankOneDoubleStarLedger(
        left_degree=left_degree,
        right_degree=right_degree,
        central_degree_product=left_degree * right_degree,
        maximum_left_codegree=maximum_left_codegree,
        maximum_right_codegree=maximum_right_codegree,
        maximum_neighbor_degree_sum=maximum_neighbor_degree_sum,
        edges=edges,
        color_pairs=color_pairs,
    )


def rank_one_double_star_energy(
    coefficients: Sequence[complex], left_degree: int, right_degree: int
) -> float:
    """Evaluate the exact rank-one energy of the double-star ledger.

    Color neighbor ``gamma`` is the directed pair
    ``(gamma,left_degree+gamma)``.  The returned energy is

    ``|sum_gamma conj(z_gamma) z_(L+gamma)|^2
      +(R-1)|z_0|^2|z_L|^2``.
    """

    if left_degree < 1 or right_degree < 1:
        raise ValueError("both central degrees must be positive")
    if len(coefficients) < 2 * left_degree:
        raise ValueError("the directed matching needs 2*left_degree colors")
    central = sum(
        complex(coefficients[index]).conjugate()
        * complex(coefficients[left_degree + index])
        for index in range(left_degree)
    )
    leaf = (
        abs(complex(coefficients[0])) ** 2
        * abs(complex(coefficients[left_degree])) ** 2
    )
    return abs(central) ** 2 + (right_degree - 1) * leaf


def three_term_ruling_certificate(
    matrix: Matrix2, first: Matrix2, middle: Matrix2, last: Matrix2
) -> RulingCertificate:
    """Certify a same-level, same-determinant matrix three-term progression.

    If ``first+last=2*middle``, the direction is ``middle-first``.  Equal
    levels and determinants at the three points force a rank-one direction
    orthogonal to ``matrix`` and tangent to the determinant quadric.
    """

    if any(x + z != 2 * y for x, y, z in zip(first, middle, last)):
        raise ValueError("the three matrices are not an affine three-term progression")
    if len({frobenius(matrix, item) for item in (first, middle, last)}) != 1:
        raise ValueError("the three matrices do not have one common level")
    if len({determinant(item) for item in (first, middle, last)}) != 1:
        raise ValueError("the three matrices do not have one determinant")
    direction = subtract(middle, first)
    certificate = ruling_certificate(matrix, first, direction)
    if not certificate.is_tangent_ruling:
        raise AssertionError("the three-term progression is not a tangent ruling")
    return certificate


def tangent_colors(m: int, h: int) -> tuple[Matrix2, tuple[int, int, int, int]]:
    """Return the signed color form and colors of the integer tangent family."""

    if h < 1 or m <= 20 * h:
        raise ValueError("require h>=1 and m>20h")
    colors = (m, m - 2 * h, m - h, m - 3 * h)
    return signed_color_form(colors), colors


def tangent_carriers(m: int, h: int, parameter: int) -> tuple[Vector2, Vector2]:
    """Return the row and column carrier vectors in the tangent witness."""

    return (
        (m + h + parameter, m + 2 * h + parameter),
        (m - h - parameter, m + h - parameter),
    )


def tangent_secant(
    m: int, h: int, base_parameter: int, gap: int
) -> tuple[Matrix2, Matrix2, Matrix2]:
    """Return ``(K,E,V)`` for a fixed-gap tangent secant and its translate.

    ``E`` is the product difference at ``base_parameter`` and ``V`` is the
    change in ``E`` when both endpoints are translated by one.
    """

    if gap == 0:
        raise ValueError("the secant gap must be nonzero")
    matrix, _ = tangent_colors(m, h)
    row, column = tangent_carriers(m, h, base_parameter)
    other_row, other_column = tangent_carriers(m, h, base_parameter + gap)
    energy = subtract(outer(row, column), outer(other_row, other_column))
    next_row, next_column = tangent_carriers(m, h, base_parameter + 1)
    next_other_row, next_other_column = tangent_carriers(
        m, h, base_parameter + gap + 1
    )
    next_energy = subtract(
        outer(next_row, next_column), outer(next_other_row, next_other_column)
    )
    direction = subtract(next_energy, energy)
    certificate = ruling_certificate(matrix, energy, direction)
    if not certificate.is_tangent_ruling:
        raise AssertionError("the tangent witness did not produce a ruling")
    return matrix, energy, direction


@dataclass(frozen=True)
class ResidualSecantModel:
    """A fixed-det, tangent-ruling-free algebraic secant family."""

    matrix: Matrix2
    color_determinant: int
    common_level: int
    secants: tuple[Matrix2, ...]
    first_rank_one_endpoints: tuple[Matrix2, ...]
    second_rank_one_endpoints: tuple[Matrix2, ...]
    maximum_entry: int


def _right_multiply_transpose(matrix: Matrix2, right: Matrix2) -> Matrix2:
    """Return ``matrix*right^T``."""

    a, b, c, d = matrix
    e, f, g, h = right
    return (a * e + b * f, a * g + b * h, c * e + d * f, c * g + d * h)


def residual_secant_model(
    count: int, *, common_level: int = 1000, color_scale: int = 5
) -> ResidualSecantModel:
    """Build ``count`` fixed-det secants with no rank-one chord.

    Start with

    ``E_t=(t,1; -t^2-1,-t)``, ``det(E_t)=1``, ``tr(E_t)=0``.

    To make the signed color form have four distinct positive magnitudes,
    put ``n=k^2-1`` and

    ``K=(n,-(n+k); -(n-k),n-1)``, ``det(K)=1``.

    Its positive integral inverse is used as a right change of variables.
    Each transformed secant remains the difference of two rank-one integer
    matrices on the same fixed ``K``-level.  Distinct secants have a
    full-rank chord of determinant ``-(s-t)^2``; hence no tangent ruling
    contains even two of them.  This is an algebraic no-go, not an
    actual-shell construction.
    """

    if count < 1:
        raise ValueError("count must be positive")
    if color_scale < 3:
        raise ValueError("color_scale must be at least three")
    if common_level <= count:
        raise ValueError("the common level should exceed the parameter range")
    k = color_scale
    n = k * k - 1
    matrix = (n, -(n + k), -(n - k), n - 1)
    inverse = (n - 1, n + k, n - k, n)
    if determinant(matrix) != 1 or determinant(inverse) != 1:
        raise AssertionError("the unimodular color transform failed")

    secants: list[Matrix2] = []
    first_endpoints: list[Matrix2] = []
    second_endpoints: list[Matrix2] = []
    for parameter in range(count):
        t = parameter
        base_secant = (t, 1, -t * t - 1, -t)
        first = (
            t,
            1,
            t * (common_level - t),
            common_level - t,
        )
        second = (0, 0, t * common_level + 1, common_level)
        if subtract(first, second) != base_secant:
            raise AssertionError("the isolated secant factorization failed")
        transformed_secant = _right_multiply_transpose(base_secant, inverse)
        transformed_first = _right_multiply_transpose(first, inverse)
        transformed_second = _right_multiply_transpose(second, inverse)
        if determinant(transformed_secant) != 1:
            raise AssertionError("the transformed determinant changed")
        if frobenius(matrix, transformed_secant) != 0:
            raise AssertionError("the transformed secant left the common level")
        if determinant(transformed_first) or determinant(transformed_second):
            raise AssertionError("an endpoint is not rank one")
        if frobenius(matrix, transformed_first) != common_level:
            raise AssertionError("the first endpoint has the wrong level")
        if frobenius(matrix, transformed_second) != common_level:
            raise AssertionError("the second endpoint has the wrong level")
        secants.append(transformed_secant)
        first_endpoints.append(transformed_first)
        second_endpoints.append(transformed_second)

    for index, first in enumerate(secants):
        for second in secants[index + 1 :]:
            chord = subtract(second, first)
            if determinant(chord) == 0:
                raise AssertionError("two residual secants share a tangent ruling")

    return ResidualSecantModel(
        matrix=matrix,
        color_determinant=determinant(matrix),
        common_level=common_level,
        secants=tuple(secants),
        first_rank_one_endpoints=tuple(first_endpoints),
        second_rank_one_endpoints=tuple(second_endpoints),
        maximum_entry=max(abs(value) for item in secants for value in item),
    )


def determinant_sensitive_bound_gap(h: int) -> tuple[int, int, float]:
    """Return the tangent witness's gap over ``sqrt(D/|det C|)``.

    The family has ``D=h^2``, ``|det C|=2D``, and ``h-1`` completions, so
    the proposed determinant-sensitive cap would be constant while the
    actual integer family grows like ``sqrt(D)``.
    """

    if h < 2:
        raise ValueError("h must be at least two")
    D = h * h
    multiplicity = h - 1
    proposed_scale = (D / (2 * D)) ** 0.5
    return D, multiplicity, multiplicity / proposed_scale


def square_box_population(model: ResidualSecantModel) -> tuple[int, int]:
    """Return ``(population, floor(sqrt(max_entry)))`` for diagnostics."""

    return len(model.secants), isqrt(model.maximum_entry)


def all_same(values: Iterable[int]) -> bool:
    """Small exact helper used by hostile tests."""

    items = tuple(values)
    return not items or all(value == items[0] for value in items)
