"""Exact-alias-quotiented Gram audit for the balanced self-orbit tower.

This is a finite hostile test of the packet aggregation step, not a proof.
All phase aliases are decided from reduced integer residue pairs.  Floating
point enters only after exact reduction modulo one, when roots of unity and
the residual Gram matrix are evaluated.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

import numpy as np

from qp_canonical_self_orbit_drpls_lab import (
    Point,
    _phase_residues,
    _phase_roots,
    balanced_tower_rectangle_audit,
)


def critical_balanced_radius(F: int) -> int:
    """Return the exact integer ``ceil(F**(25/8))`` used in scaled towers."""

    F = int(F)
    if F <= 1:
        raise ValueError("F must exceed one")
    target = F**25
    lower, upper = 0, 1
    while upper**8 < target:
        upper *= 2
    while upper - lower > 1:
        middle = (lower + upper) // 2
        if middle**8 < target:
            lower = middle
        else:
            upper = middle
    return upper


@dataclass(frozen=True)
class PacketGramDiagnostics:
    """Diagnostics for one choice of packet-pair columns."""

    column_count: int
    packet_diagonal_mass: float
    exact_cross_alias_mass: int
    signed_nonalias_cross_mass: float
    normalized_packet_diagonal_mass: float
    translate_aggregation_ratio: float
    alias_quotiented_aggregation_ratio: float
    signed_nonalias_cross_over_diagonal: float
    exact_cross_alias_over_diagonal: float
    whitened_residual_spectral_radius: float
    whitened_residual_largest_eigenvalue: float
    whitened_residual_maximum_absolute_row_sum: float
    whitened_residual_mean_absolute_row_sum: float
    maximum_absolute_pair_correlation: float
    maximum_correlation_column_ids: tuple[int, int]
    top_absolute_pair_correlations: tuple[tuple[float, int, int], ...]
    maximum_row_column_id: int


@dataclass(frozen=True)
class TransposeHingeCorrelationAudit:
    """Two-column audit for ``{a,b}`` and ``{b,c}`` after transposition."""

    F: int
    R: int
    q: int
    D: int
    K: int
    lane_triple: tuple[int, int, int]
    exact_cross_alias_mass: int
    first_column_mass: float
    second_column_mass: float
    raw_absolute_correlation: float
    alias_removed_absolute_correlation: float
    alias_removed_correlation_real: float
    alias_removed_correlation_imaginary: float


@dataclass(frozen=True)
class BalancedTowerAliasGramAudit:
    F: int
    R: int
    q: int
    D: int
    K: int
    lane_parameters: tuple[int, ...]
    point_count: int
    ordered_packet_pair_count: int
    phase_alias_class_count: int
    nontrivial_phase_alias_class_count: int
    maximum_phase_alias_class_size: int
    target: float
    total_mass: float
    packet_pair_diagonal_mass: float
    exact_cross_packet_alias_mass: int
    signed_nonalias_cross_mass: float
    normalized_total_mass: float
    normalized_packet_pair_diagonal_mass: float
    translate_aggregation_ratio: float
    alias_quotiented_aggregation_ratio: float
    signed_nonalias_cross_over_diagonal: float
    exact_cross_alias_over_diagonal: float
    whitened_residual_spectral_radius: float
    whitened_residual_largest_eigenvalue: float
    whitened_residual_maximum_absolute_row_sum: float
    whitened_residual_mean_absolute_row_sum: float
    maximum_absolute_pair_correlation: float
    maximum_correlation_packet_pair_ids: tuple[int, int]
    maximum_row_packet_pair_id: int
    transpose_quotient_columns: tuple[tuple[int, int], ...]
    transpose_quotient: PacketGramDiagnostics


def _reduced_phase_keys(
    q: int, products: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Return exact reduced numerator/denominator keys for all cells."""

    distinct_products, inverse = np.unique(products, return_inverse=True)
    residues, denominators = _phase_residues(q, distinct_products)
    common = np.gcd(residues, denominators)
    return (residues // common)[inverse], (denominators // common)[inverse]


def _phase_and_packet_alias_data(
    q: int,
    products: np.ndarray,
    packet_pair_ids: np.ndarray,
    packet_pair_count: int,
    K: int,
    *,
    phase_keys: tuple[np.ndarray, np.ndarray] | None = None,
) -> tuple[int, int, int, int, np.ndarray]:
    """Return exact alias statistics and the cross-packet alias Gram.

    A cell with product ``n`` has the exact phase

        (q^3 mod 8n)/(8n)  (mod 1).

    The numerator and denominator are reduced before equality testing.  If
    ``a[P,theta]`` is the number of cells of ordered packet pair ``P`` with
    phase ``theta``, the returned off-diagonal matrix is exactly

        K * sum_theta a[P,theta] a[Q,theta],  P != Q.
    """

    if phase_keys is None:
        phase_keys = _reduced_phase_keys(q, products)
    numerators, reduced_denominators = phase_keys

    phase_order = np.lexsort((reduced_denominators, numerators))
    sorted_num = numerators[phase_order]
    sorted_den = reduced_denominators[phase_order]
    phase_starts = np.r_[
        0,
        1
        + np.nonzero(
            (sorted_num[1:] != sorted_num[:-1])
            | (sorted_den[1:] != sorted_den[:-1])
        )[0],
    ]
    phase_counts = np.diff(np.r_[phase_starts, len(products)]).astype(np.int64)
    global_square = int(sum(int(value) ** 2 for value in phase_counts))

    # Sort first by exact phase and then by packet id.  Each run is one
    # a[P,theta]; this simultaneously gives the within-packet alias square
    # and the sparse exact cross-packet alias Gram.
    joint_order = np.lexsort(
        (packet_pair_ids, reduced_denominators, numerators)
    )
    joint_num = numerators[joint_order]
    joint_den = reduced_denominators[joint_order]
    joint_packet = packet_pair_ids[joint_order]
    joint_starts = np.r_[
        0,
        1
        + np.nonzero(
            (joint_num[1:] != joint_num[:-1])
            | (joint_den[1:] != joint_den[:-1])
            | (joint_packet[1:] != joint_packet[:-1])
        )[0],
    ]
    joint_counts = np.diff(np.r_[joint_starts, len(products)]).astype(np.int64)
    within_square = int(sum(int(value) ** 2 for value in joint_counts))
    exact_cross_mass = K * (global_square - within_square)

    representative = joint_order[joint_starts]
    run_num = numerators[representative]
    run_den = reduced_denominators[representative]
    run_packet = packet_pair_ids[representative]
    exact_cross_gram = np.zeros(
        (packet_pair_count, packet_pair_count), dtype=np.float64
    )
    phase_run_starts = np.r_[
        0,
        1
        + np.nonzero(
            (run_num[1:] != run_num[:-1])
            | (run_den[1:] != run_den[:-1])
        )[0],
    ]
    phase_run_ends = np.r_[phase_run_starts[1:], len(run_num)]
    for start, end in zip(phase_run_starts, phase_run_ends):
        if end - start < 2:
            continue
        ids = run_packet[start:end]
        weights = joint_counts[start:end]
        contribution = K * np.outer(weights, weights)
        contribution[np.diag_indices_from(contribution)] = 0
        exact_cross_gram[np.ix_(ids, ids)] += contribution

    # This is also an exact-integer consistency check on the sparse matrix.
    if round(float(exact_cross_gram.sum())) != exact_cross_mass:
        raise AssertionError("exact cross-alias ledger is inconsistent")
    return (
        len(phase_counts),
        int(np.count_nonzero(phase_counts > 1)),
        int(phase_counts.max(initial=0)),
        exact_cross_mass,
        exact_cross_gram,
    )


def _gram_diagnostics(
    packet_sums: np.ndarray,
    total_mass: float,
    target: float,
    exact_cross_alias_mass: int,
    exact_cross_alias_gram: np.ndarray,
    *,
    compute_spectrum: bool,
) -> PacketGramDiagnostics:
    """Compute residual Gram data after an exact cross-alias subtraction."""

    gram = np.asarray(packet_sums.conj().T @ packet_sums, dtype=np.complex128)
    diagonal = np.maximum(gram.diagonal().real, 0.0)
    packet_diagonal_mass = float(diagonal.sum())
    signed_nonalias_cross = (
        total_mass - packet_diagonal_mass - exact_cross_alias_mass
    )
    scale = np.sqrt(diagonal[:, None] * diagonal[None, :])
    residual = gram - exact_cross_alias_gram
    np.fill_diagonal(residual, 0.0)
    whitened = np.divide(
        residual,
        scale,
        out=np.zeros_like(residual),
        where=scale > 0,
    )
    whitened = (whitened + whitened.conj().T) / 2
    absolute_whitened = np.abs(whitened)
    maximum_flat = int(absolute_whitened.argmax())
    maximum_pair = tuple(
        map(int, np.unravel_index(maximum_flat, whitened.shape))
    )
    upper_triangle = np.triu(absolute_whitened, k=1)
    number_of_pairs = packet_sums.shape[1] * (packet_sums.shape[1] - 1) // 2
    top_count = min(10, number_of_pairs)
    if top_count:
        candidate_flat = np.argpartition(
            upper_triangle.reshape(-1), -top_count
        )[-top_count:]
        top_correlations = tuple(
            (
                float(upper_triangle.reshape(-1)[flat_id]),
                *map(int, np.unravel_index(int(flat_id), upper_triangle.shape)),
            )
            for flat_id in sorted(
                candidate_flat,
                key=lambda index: upper_triangle.reshape(-1)[index],
                reverse=True,
            )
        )
    else:
        top_correlations = ()
    row_sums = absolute_whitened.sum(axis=1)
    maximum_row = int(row_sums.argmax())
    if compute_spectrum:
        eigenvalues = np.linalg.eigvalsh(whitened)
        spectral_radius = float(np.max(np.abs(eigenvalues), initial=0.0))
        largest_eigenvalue = float(eigenvalues[-1]) if len(eigenvalues) else 0.0
    else:
        spectral_radius = largest_eigenvalue = float("nan")
    return PacketGramDiagnostics(
        column_count=packet_sums.shape[1],
        packet_diagonal_mass=packet_diagonal_mass,
        exact_cross_alias_mass=exact_cross_alias_mass,
        signed_nonalias_cross_mass=signed_nonalias_cross,
        normalized_packet_diagonal_mass=packet_diagonal_mass / target,
        translate_aggregation_ratio=total_mass / packet_diagonal_mass,
        alias_quotiented_aggregation_ratio=(
            total_mass - exact_cross_alias_mass
        )
        / packet_diagonal_mass,
        signed_nonalias_cross_over_diagonal=(
            signed_nonalias_cross / packet_diagonal_mass
        ),
        exact_cross_alias_over_diagonal=(
            exact_cross_alias_mass / packet_diagonal_mass
        ),
        whitened_residual_spectral_radius=spectral_radius,
        whitened_residual_largest_eigenvalue=largest_eigenvalue,
        whitened_residual_maximum_absolute_row_sum=float(row_sums.max(initial=0.0)),
        whitened_residual_mean_absolute_row_sum=float(row_sums.mean()),
        maximum_absolute_pair_correlation=float(
            absolute_whitened.max(initial=0.0)
        ),
        maximum_correlation_column_ids=maximum_pair,
        top_absolute_pair_correlations=top_correlations,
        maximum_row_column_id=maximum_row,
    )


def balanced_tower_alias_gram_audit(
    F: int,
    R: int | None = None,
    *,
    K: int | None = None,
    method: str = "complex128",
    compute_spectrum: bool = True,
) -> BalancedTowerAliasGramAudit:
    r"""Audit the guaranteed lane rectangle at the actual truncated top band.

    The default ``R`` is ``ceil(F^(25/8))`` and the default
    ``K=floor(q/(2D))=floor(R/F)``.  The latter is the top scale present in
    the truncated Selberg reduction; it is half the stronger formal scan
    endpoint ``q/D``.

    Each lane is a packet.  For an ordered lane pair ``P=(a,b)``, set

        G_P(h) = sum_{i in a, j in b} e(h q^3/(8 b_i B_j)).

    The packet-pair diagonal is ``sum_P,h |G_P(h)|^2``.  Exact aliases
    between distinct ``P`` are then removed cell-by-cell using reduced
    integer phase residues before the residual Gram diagnostics are formed.
    """

    F = int(F)
    R = critical_balanced_radius(F) if R is None else int(R)
    rectangle = balanced_tower_rectangle_audit(F, R)
    if not rectangle.rectangle_is_contained:
        raise AssertionError("the guaranteed tower rectangle is absent")
    q, D = rectangle.q, rectangle.D
    K = R // F if K is None else int(K)
    if K <= 0:
        raise ValueError("K must be positive")

    lanes = rectangle.lane_parameters
    lane_count = len(lanes)
    n_parameters = rectangle.rectangle_n_parameters
    points: tuple[Point, ...] = tuple(
        (m * R - n, m * (R + 1) - n)
        for m in lanes
        for n in n_parameters
    )
    point_count = len(points)
    if point_count == 0:
        raise ValueError("the balanced rectangle has no admissible lanes")
    first = np.fromiter((point[0] for point in points), dtype=np.uint64)
    second = np.fromiter((point[1] for point in points), dtype=np.uint64)
    product_matrix = first[:, None] * second[None, :]
    products = product_matrix.reshape(-1)
    distinct_products, inverse = np.unique(products, return_inverse=True)
    roots = _phase_roots(q, distinct_products, method=method)[inverse]
    root_matrix = roots.reshape(point_count, point_count)

    packet_ids = np.repeat(np.arange(lane_count, dtype=np.int64), F)
    packet_pair_count = lane_count**2
    packet_pair_ids = (
        packet_ids[:, None] * lane_count + packet_ids[None, :]
    ).reshape(-1)
    phase_keys = _reduced_phase_keys(q, products)
    (
        alias_class_count,
        nontrivial_alias_class_count,
        maximum_alias_class_size,
        exact_cross_alias_mass,
        exact_cross_alias_gram,
    ) = _phase_and_packet_alias_data(
        q,
        products,
        packet_pair_ids,
        packet_pair_count,
        K,
        phase_keys=phase_keys,
    )

    # Rows are frequencies K<h<=2K; columns are ordered packet pairs P.
    dtype = np.complex128 if method == "complex128" else np.clongdouble
    packet_sums = np.empty((K, packet_pair_count), dtype=dtype)
    current = np.power(root_matrix, K + 1)
    for offset in range(K):
        packet_sums[offset] = current.reshape(
            lane_count, F, lane_count, F
        ).sum(axis=(1, 3)).reshape(-1)
        current *= root_matrix
        if (offset + 1) % 256 == 0:
            current = np.power(root_matrix, K + offset + 2)

    total_by_frequency = packet_sums.sum(axis=1)
    total_mass = float(np.vdot(total_by_frequency, total_by_frequency).real)
    target = q**2 / K
    ordered_diagnostics = _gram_diagnostics(
        packet_sums,
        total_mass,
        target,
        exact_cross_alias_mass,
        exact_cross_alias_gram,
        compute_spectrum=compute_spectrum,
    )

    # Quotient the exact packet-level transpose involution.  The column for
    # an unordered pair {a,b} is G_(a,b)+G_(b,a), with G_(a,a) included once.
    quotient_lane_indices = tuple(
        (left, right)
        for left in range(lane_count)
        for right in range(left, lane_count)
    )
    quotient_lookup = {
        lane_pair: column_id
        for column_id, lane_pair in enumerate(quotient_lane_indices)
    }
    ordered_to_quotient = np.fromiter(
        (
            quotient_lookup[(min(left, right), max(left, right))]
            for left in range(lane_count)
            for right in range(lane_count)
        ),
        dtype=np.int64,
        count=packet_pair_count,
    )
    quotient_column_count = len(quotient_lane_indices)
    quotient_sums = np.zeros((K, quotient_column_count), dtype=dtype)
    for ordered_id, quotient_id in enumerate(ordered_to_quotient):
        quotient_sums[:, quotient_id] += packet_sums[:, ordered_id]
    quotient_cell_ids = ordered_to_quotient[packet_pair_ids]
    (
        quotient_alias_class_count,
        quotient_nontrivial_alias_count,
        quotient_maximum_alias_size,
        quotient_exact_cross_alias_mass,
        quotient_exact_cross_alias_gram,
    ) = _phase_and_packet_alias_data(
        q,
        products,
        quotient_cell_ids,
        quotient_column_count,
        K,
        phase_keys=phase_keys,
    )
    if (
        quotient_alias_class_count != alias_class_count
        or quotient_nontrivial_alias_count != nontrivial_alias_class_count
        or quotient_maximum_alias_size != maximum_alias_class_size
    ):
        raise AssertionError("a packet quotient changed the global phase classes")
    quotient_total = quotient_sums.sum(axis=1)
    if not np.allclose(quotient_total, total_by_frequency, rtol=2e-14, atol=2e-9):
        raise AssertionError("the transpose quotient changed the all-one sum")
    quotient_diagnostics = _gram_diagnostics(
        quotient_sums,
        total_mass,
        target,
        quotient_exact_cross_alias_mass,
        quotient_exact_cross_alias_gram,
        compute_spectrum=compute_spectrum,
    )

    return BalancedTowerAliasGramAudit(
        F=F,
        R=R,
        q=q,
        D=D,
        K=K,
        lane_parameters=lanes,
        point_count=point_count,
        ordered_packet_pair_count=packet_pair_count,
        phase_alias_class_count=alias_class_count,
        nontrivial_phase_alias_class_count=nontrivial_alias_class_count,
        maximum_phase_alias_class_size=maximum_alias_class_size,
        target=target,
        total_mass=total_mass,
        packet_pair_diagonal_mass=ordered_diagnostics.packet_diagonal_mass,
        exact_cross_packet_alias_mass=exact_cross_alias_mass,
        signed_nonalias_cross_mass=ordered_diagnostics.signed_nonalias_cross_mass,
        normalized_total_mass=total_mass / target,
        normalized_packet_pair_diagonal_mass=(
            ordered_diagnostics.normalized_packet_diagonal_mass
        ),
        translate_aggregation_ratio=ordered_diagnostics.translate_aggregation_ratio,
        alias_quotiented_aggregation_ratio=(
            ordered_diagnostics.alias_quotiented_aggregation_ratio
        ),
        signed_nonalias_cross_over_diagonal=(
            ordered_diagnostics.signed_nonalias_cross_over_diagonal
        ),
        exact_cross_alias_over_diagonal=(
            ordered_diagnostics.exact_cross_alias_over_diagonal
        ),
        whitened_residual_spectral_radius=(
            ordered_diagnostics.whitened_residual_spectral_radius
        ),
        whitened_residual_largest_eigenvalue=(
            ordered_diagnostics.whitened_residual_largest_eigenvalue
        ),
        whitened_residual_maximum_absolute_row_sum=(
            ordered_diagnostics.whitened_residual_maximum_absolute_row_sum
        ),
        whitened_residual_mean_absolute_row_sum=(
            ordered_diagnostics.whitened_residual_mean_absolute_row_sum
        ),
        maximum_absolute_pair_correlation=(
            ordered_diagnostics.maximum_absolute_pair_correlation
        ),
        maximum_correlation_packet_pair_ids=(
            ordered_diagnostics.maximum_correlation_column_ids
        ),
        maximum_row_packet_pair_id=ordered_diagnostics.maximum_row_column_id,
        transpose_quotient_columns=tuple(
            (lanes[left], lanes[right]) for left, right in quotient_lane_indices
        ),
        transpose_quotient=quotient_diagnostics,
    )


def decode_packet_pair(packet_pair_id: int, lane_count: int) -> tuple[int, int]:
    """Decode the flattened ordered lane-pair id used by the audit."""

    return divmod(int(packet_pair_id), int(lane_count))


def transpose_hinge_correlation_audit(
    F: int,
    lane_triple: tuple[int, int, int],
    R: int | None = None,
    *,
    K: int | None = None,
    method: str = "complex128",
) -> TransposeHingeCorrelationAudit:
    r"""Audit two merged columns ``{a,b}`` and ``{b,c}`` efficiently.

    This isolates a packet-level hinge without constructing the full
    ``Theta(F^2)``-column Gram.  Exact aliases are removed using the same
    reduced residue keys as :func:`balanced_tower_alias_gram_audit`.
    """

    F = int(F)
    a, b, c = map(int, lane_triple)
    if not a < b < c:
        raise ValueError("lane_triple must be strictly increasing")
    R = critical_balanced_radius(F) if R is None else int(R)
    rectangle = balanced_tower_rectangle_audit(F, R)
    if not {a, b, c} <= set(rectangle.lane_parameters):
        raise ValueError("the hinge lanes are not in the guaranteed rectangle")
    q, D = rectangle.q, rectangle.D
    K = R // F if K is None else int(K)
    if K <= 0:
        raise ValueError("K must be positive")
    n_parameters = np.arange(F, dtype=np.uint64)

    def products(left_lane: int, right_lane: int) -> np.ndarray:
        left = np.uint64(left_lane * R) - n_parameters
        right = np.uint64(right_lane * (R + 1)) - n_parameters
        if int(left.max()) * int(right.max()) > np.iinfo(np.uint64).max:
            raise OverflowError("a hinge cell product does not fit in uint64")
        return (left[:, None] * right[None, :]).reshape(-1)

    cell_products = np.concatenate(
        (
            products(a, b),
            products(b, a),
            products(b, c),
            products(c, b),
        )
    )
    distinct_products, inverse = np.unique(cell_products, return_inverse=True)
    roots = _phase_roots(q, distinct_products, method=method)[inverse]
    dtype = np.complex128 if method == "complex128" else np.clongdouble
    column_sums = np.empty((K, 2), dtype=dtype)
    current = np.power(roots, K + 1)
    for offset in range(K):
        ordered_sums = current.reshape(4, F * F).sum(axis=1)
        column_sums[offset] = (
            ordered_sums[0] + ordered_sums[1],
            ordered_sums[2] + ordered_sums[3],
        )
        current *= roots
        if (offset + 1) % 256 == 0:
            current = np.power(roots, K + offset + 2)

    hinge_ids = np.repeat(np.array((0, 0, 1, 1), dtype=np.int64), F * F)
    _, _, _, exact_cross_alias_mass, exact_cross_alias_gram = (
        _phase_and_packet_alias_data(
            q,
            cell_products,
            hinge_ids,
            2,
            K,
            phase_keys=_reduced_phase_keys(q, cell_products),
        )
    )
    if round(2 * exact_cross_alias_gram[0, 1]) != exact_cross_alias_mass:
        raise AssertionError("the two-column alias ledger is inconsistent")
    gram = np.asarray(column_sums.conj().T @ column_sums, dtype=np.complex128)
    scale = float(np.sqrt(gram[0, 0].real * gram[1, 1].real))
    residual_correlation = (
        gram[0, 1] - exact_cross_alias_gram[0, 1]
    ) / scale
    return TransposeHingeCorrelationAudit(
        F=F,
        R=R,
        q=q,
        D=D,
        K=K,
        lane_triple=(a, b, c),
        exact_cross_alias_mass=exact_cross_alias_mass,
        first_column_mass=float(gram[0, 0].real),
        second_column_mass=float(gram[1, 1].real),
        raw_absolute_correlation=float(abs(gram[0, 1]) / scale),
        alias_removed_absolute_correlation=float(abs(residual_correlation)),
        alias_removed_correlation_real=float(residual_correlation.real),
        alias_removed_correlation_imaginary=float(residual_correlation.imag),
    )
