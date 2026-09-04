"""Scale and finite ledgers for the QP Peller/log-Hankel audit.

The routines here do not assert the uniform four-cycle conjecture.  They
record three exact facts used in the accompanying report:

* a classical Hankel matrix with one nonzero anti-diagonal has fourth
  Schatten mass equal to the length of that anti-diagonal;
* the normalized continuous box pulse has a fourth-trace lower bound of
  order the inverse pulse width;
* support at the two ends of a centered affine packet forces both a small
  stationarity defect and the sharp quadratic curvature budget.

There is also a purely operator-theoretic degree-stratified upper ledger.
It follows from ``S4^4 <= op^2 * HS^2`` and the fact that every color layer
is a partial permutation.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Mapping, Sequence

import numpy as np


@dataclass(frozen=True)
class PellerScaleLedger:
    q: float
    degree: float
    log_pulse_width: float
    log_node_gap: float
    pulse_to_gap_ratio: float
    tangent_packet_order: float
    uniform_hankel_fourth_mass: float
    continuum_pulse_fourth_lower: float
    uniform_to_actual_loss: float
    continuum_to_actual_loss: float


def peller_scale_ledger(q: float, degree: float) -> PellerScaleLedger:
    """Return the hostile normalization scales for ``D=degree``.

    Harmless fixed shell constants are omitted, exactly as in the exponent
    audit.  The continuous lower bound includes the explicit factor ``1/16``
    from the rectangular subregion used in the fourth-trace integral.
    """

    if q <= 1.0 or not 0.0 < degree < q:
        raise ValueError("require q>1 and 0<degree<q")
    epsilon = degree / (q * q)
    gap = 1.0 / q
    return PellerScaleLedger(
        q=q,
        degree=degree,
        log_pulse_width=epsilon,
        log_node_gap=gap,
        pulse_to_gap_ratio=degree / q,
        tangent_packet_order=math.sqrt(degree),
        uniform_hankel_fourth_mass=q,
        continuum_pulse_fourth_lower=1.0 / (16.0 * epsilon),
        uniform_to_actual_loss=q / degree,
        continuum_to_actual_loss=1.0 / (16.0 * epsilon * degree),
    )


def anti_diagonal_matrix(order: int, diagonal: int) -> np.ndarray:
    """Return ``1_(i+j=diagonal)`` on an ``order`` square."""

    if order <= 0 or not 0 <= diagonal <= 2 * order - 2:
        raise ValueError("invalid order or anti-diagonal")
    rows, columns = np.indices((order, order))
    return (rows + columns == diagonal).astype(float)


def schatten_fourth_power(matrix: np.ndarray) -> float:
    """Return ``tr((A A*)^2)``."""

    values = np.asarray(matrix, dtype=complex)
    gram = values @ values.conjugate().T
    return float(np.real(np.vdot(gram, gram)))


def anti_diagonal_fourth_mass(order: int, diagonal: int) -> int:
    """Return the exact fourth Schatten mass of one anti-diagonal.

    The matrix is a partial permutation, so every nonzero singular value is
    one.  Its mass is therefore just its number of entries.
    """

    if order <= 0 or not 0 <= diagonal <= 2 * order - 2:
        raise ValueError("invalid order or anti-diagonal")
    return min(diagonal + 1, 2 * order - 1 - diagonal)


def continuum_box_pulse_fourth_lower(epsilon: float) -> float:
    """The rigorous lower bound ``1/(16 epsilon)`` from the report."""

    if not 0.0 < epsilon < 0.125:
        raise ValueError("epsilon must lie in (0,1/8)")
    return 1.0 / (16.0 * epsilon)


def log_linearization_error(center: int, offset: int) -> float:
    """Return ``|log((center+offset)/center)-offset/center|``."""

    if center <= 0 or center + offset <= 0:
        raise ValueError("the logarithms must have positive arguments")
    return abs(math.log1p(offset / center) - offset / center)


@dataclass(frozen=True)
class AffineAxisLedger:
    base: int
    carrier_base: int
    color_base: int
    row_step: int
    color_step: int
    radius: int
    plus_increment: int
    minus_increment: int
    stationarity_defect: int
    curvature_term: int
    recovered_stationarity_numerator: int
    recovered_curvature_numerator: int


def affine_axis_ledger(
    base: int,
    carrier_base: int,
    color_base: int,
    row_step: int,
    color_step: int,
    radius: int,
) -> AffineAxisLedger:
    r"""Return exact endpoint identities for a centered affine packet.

    Put

    ``a_i=A+P*i, b=B, c_i=C-S*i`` for ``i=+-L``.

    Relative to the central product ``A*B*C``, the two increments are

    ``B*(+-L*(P*C-A*S)-P*S*L^2)``.

    Their difference recovers ``2*B*L*(P*C-A*S)`` and their sum recovers
    ``-2*B*P*S*L^2`` exactly.
    """

    values = (base, carrier_base, color_base, row_step, color_step, radius)
    if any(value <= 0 for value in values):
        raise ValueError("all packet parameters must be positive")
    A, B, C, P, S, L = values
    center_product = A * B * C
    plus = (A + P * L) * B * (C - S * L) - center_product
    minus = (A - P * L) * B * (C + S * L) - center_product
    defect = P * C - A * S
    curvature = P * S * L * L
    return AffineAxisLedger(
        base=A,
        carrier_base=B,
        color_base=C,
        row_step=P,
        color_step=S,
        radius=L,
        plus_increment=plus,
        minus_increment=minus,
        stationarity_defect=defect,
        curvature_term=curvature,
        recovered_stationarity_numerator=plus - minus,
        recovered_curvature_numerator=plus + minus,
    )


@dataclass(frozen=True)
class ApproximatePacketPackingLedger:
    degree_budget: float
    row_step: int
    color_step: int
    radius: int
    center_interval_length: float
    disjoint_center_spacing: int
    maximum_disjoint_packets: int
    packet_count_times_radius_sq: int
    curvature_admissible: bool


@dataclass(frozen=True)
class FixedSlopePacketTheoremLedger:
    window_radius: float
    carrier_lower_bound: float
    row_step: int
    color_step: int
    radius: int
    stationarity_defect_bound: float
    curvature_term_bound: float
    center_interval_length: float
    interval_disjoint_packet_bound: int
    node_disjoint_packet_bound: int
    interval_disjoint_budget: int
    node_disjoint_budget: int
    proved_interval_budget_upper: float
    proved_node_budget_upper: float


def fixed_slope_packet_theorem_ledger(
    window_radius: float,
    carrier_lower_bound: float,
    row_step: int,
    color_step: int,
    radius: int,
) -> FixedSlopePacketTheoremLedger:
    r"""Return the constants in the approximate fixed-slope packet lemma.

    For every packet assume

    ``|(A+P*i) B (C-S*i)-X| <= H`` for ``i in {-L,0,L}``

    and ``B>=B_min``.  The endpoint identities imply

    ``|P*C-A*S| <= 2H/(B_min L)`` and
    ``P*S*L^2 <= 2H/B_min``.

    For fixed ``(P,S,C)``, all centers ``A`` lie in an interval of length
    ``4H/(B_min S L)``.  Two packing notions are recorded.

    * ``interval_disjoint``: the convex hulls ``[A-PL,A+PL]`` are disjoint;
    * ``node_disjoint``: only the arithmetic progressions themselves are
      disjoint.  Partitioning by ``A mod P`` handles their interleaving.

    The proved real-valued budget uppers are respectively

    ``4H/(B_min P S)`` and ``4H/(B_min S)``.

    Floors in the explicit integer counts can only make those bounds
    smaller when the curvature hypothesis is satisfied.
    """

    H = float(window_radius)
    B_min = float(carrier_lower_bound)
    P, S, L = int(row_step), int(color_step), int(radius)
    if H <= 0.0 or B_min <= 0.0 or P <= 0 or S <= 0 or L <= 0:
        raise ValueError("all packet parameters must be positive")
    center_length = 4.0 * H / (B_min * S * L)
    interval_spacing = 2 * P * L
    interval_count = 1 + math.floor(center_length / interval_spacing)
    node_spacing_in_residue = (2 * L + 1) * P
    node_count = P * (
        1 + math.floor(center_length / node_spacing_in_residue)
    )
    return FixedSlopePacketTheoremLedger(
        window_radius=H,
        carrier_lower_bound=B_min,
        row_step=P,
        color_step=S,
        radius=L,
        stationarity_defect_bound=2.0 * H / (B_min * L),
        curvature_term_bound=2.0 * H / B_min,
        center_interval_length=center_length,
        interval_disjoint_packet_bound=interval_count,
        node_disjoint_packet_bound=node_count,
        interval_disjoint_budget=interval_count * L * L,
        node_disjoint_budget=node_count * L * L,
        proved_interval_budget_upper=4.0 * H / (B_min * P * S),
        proved_node_budget_upper=4.0 * H / (B_min * S),
    )


def dyadic_reciprocal_step_sum(lower_step: int) -> float:
    r"""Return ``sum_(P,S in [R,2R)) 1/(P*S)`` exactly in float.

    It is the square of a short harmonic sum and is at most one.  Therefore
    summing the interval-disjoint packet budget over comparable dyadic step
    pairs costs only one constant per dyadic scale.
    """

    R = int(lower_step)
    if R <= 0:
        raise ValueError("lower_step must be positive")
    harmonic_slice = sum(1.0 / value for value in range(R, 2 * R))
    return harmonic_slice * harmonic_slice


@dataclass(frozen=True)
class UnstratifiedTradeoffObstruction:
    degree_budget: int
    packet_order: int
    matching_mass_fraction: float
    hilbert_schmidt_sq: float
    operator_norm_sq: float
    schatten_fourth: float
    operator_hs_product: float
    fourth_to_degree_ratio: float
    product_to_degree_ratio: float


def unstratified_tradeoff_obstruction(
    packet_order: int, matching_mass_fraction: float = 0.5
) -> UnstratifiedTradeoffObstruction:
    r"""Return an exact abstract obstruction to mixing degree scales.

    Put ``D=L^2``.  One block is ``sqrt(x) I_D`` and the other is

    ``sqrt((1-x)/L) J_L``.

    The first block is one color of degree ``D``.  The second can be colored
    by a cyclic Latin square with ``L`` colors, each of degree ``L``.  The
    total color vector has squared norm one.  Both blocks together have
    fourth Schatten mass at most ``D``, while ``op^2 * HS^2`` is of order
    ``D^(3/2)`` when ``x`` is bounded away from zero and one.

    This is a proof-method countermodel, not a QP-shell realization.
    """

    L = int(packet_order)
    x = float(matching_mass_fraction)
    if L <= 1 or not 0.0 < x < 1.0:
        raise ValueError("require packet_order>1 and mass fraction in (0,1)")
    D = L * L
    hs_sq = x * D + (1.0 - x) * L
    op_sq = max(x, (1.0 - x) * L)
    fourth = x * x * D + (1.0 - x) ** 2 * L * L
    product = hs_sq * op_sq
    return UnstratifiedTradeoffObstruction(
        degree_budget=D,
        packet_order=L,
        matching_mass_fraction=x,
        hilbert_schmidt_sq=hs_sq,
        operator_norm_sq=op_sq,
        schatten_fourth=fourth,
        operator_hs_product=product,
        fourth_to_degree_ratio=fourth / D,
        product_to_degree_ratio=product / D,
    )


def approximate_packet_packing_ledger(
    degree_budget: float,
    row_step: int,
    color_step: int,
    radius: int,
    *,
    stationarity_constant: float = 2.0,
) -> ApproximatePacketPackingLedger:
    r"""Return the schematic convex-hull-disjoint packet packing bound.

    Endpoint support in a product window of scale ``D`` gives schematically

    ``|P*C-A*S| <= stationarity_constant*D/L``.

    For fixed ``(P,S,C)``, the possible centers ``A`` occupy an interval of
    length at most ``2*stationarity_constant*D/(S*L)``.  Centered row
    packets whose *convex hull intervals* are pairwise disjoint have center
    spacing at least ``2*P*L+1``.  This function records the resulting exact
    integer packing ceiling.  For merely node-disjoint, interleaved
    progressions use :func:`fixed_slope_packet_theorem_ledger` instead.

    The separate curvature condition is ``P*S*L^2 <= 2D`` with the same
    harmless shell normalization used by the report.
    """

    if degree_budget <= 0.0 or stationarity_constant <= 0.0:
        raise ValueError("budgets and constants must be positive")
    if row_step <= 0 or color_step <= 0 or radius <= 0:
        raise ValueError("steps and radius must be positive")
    length = (
        2.0 * stationarity_constant * degree_budget / (color_step * radius)
    )
    spacing = 2 * row_step * radius + 1
    count = 1 + math.floor(length / spacing)
    return ApproximatePacketPackingLedger(
        degree_budget=degree_budget,
        row_step=row_step,
        color_step=color_step,
        radius=radius,
        center_interval_length=length,
        disjoint_center_spacing=spacing,
        maximum_disjoint_packets=count,
        packet_count_times_radius_sq=count * radius * radius,
        curvature_admissible=(
            row_step * color_step * radius * radius <= 2.0 * degree_budget
        ),
    )


def dyadic_degree_schatten_bound(
    color_degrees: Mapping[int, float],
    color_weights: Mapping[int, complex],
) -> float:
    r"""Return the degree-stratified upper bound for ``||A_z||_S4^4``.

    Colors with degrees in ``(2^(j-1),2^j]`` are grouped together.  On one
    group, color layers are partial permutations, whence

    ``||A||_op <= ||z||_1`` and ``||A||_HS^2 <= 2^j ||z||_2^2``.

    The fourth power of the triangle inequality over ``r`` nonempty groups
    costs at most ``r^3``.  The returned quantity is therefore

    ``r^3 sum_j 2^j ||z_j||_2^2 ||z_j||_1^2``.

    It is a universal upper ledger, not an assertion that the underlying QP
    matrix attains it.
    """

    bins: dict[int, list[complex]] = {}
    for color, weight in color_weights.items():
        degree = float(color_degrees.get(color, 0.0))
        if degree <= 0.0 or weight == 0:
            continue
        ceiling = math.ceil(math.log2(degree))
        bins.setdefault(ceiling, []).append(complex(weight))
    if not bins:
        return 0.0
    subtotal = 0.0
    for ceiling, weights in bins.items():
        values = np.asarray(weights, dtype=complex)
        l2_sq = float(np.vdot(values, values).real)
        l1_sq = float(np.sum(np.abs(values)) ** 2)
        subtotal += (2.0**ceiling) * l2_sq * l1_sq
    return len(bins) ** 3 * subtotal


def direct_single_bin_bound(
    maximum_degree: float, color_weights: Sequence[complex]
) -> float:
    """Return ``M ||z||_2^2 ||z||_1^2`` for one degree bin."""

    if maximum_degree < 0.0:
        raise ValueError("maximum degree must be nonnegative")
    values = np.asarray(color_weights, dtype=complex)
    l2_sq = float(np.vdot(values, values).real)
    l1_sq = float(np.sum(np.abs(values)) ** 2)
    return maximum_degree * l2_sq * l1_sq
