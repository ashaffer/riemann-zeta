#!/usr/bin/env python3
"""D-rated near-product cell audit for the completed R71 fourth moment.

Let the faithful completed transform from ``r71_fixed_strip_moment_probe`` be

    F(t) = sum_j F_j(t),

where every boundary-truncated grouped product is a separate channel and the
last channel is the *signed* full rank-two center.  The exact unordered pair
ledger is

    F(t)^2 = sum_(i<=j) m_(ij) F_i(t)F_j(t),
    m_(ij) = 1 if i=j and 2 otherwise.                  (1)

Consequently, on the sampled finite frequency window,

    U_4 = integral |F|^4
        = D_atom + I_within(C) + I_across(C),           (2)

for every partition ``C`` of the pair channels.  Here ``D_atom`` is the sum
of individual pair-channel energies, ``I_within`` is the interference gained
by grouping pairs inside cells, and ``I_across`` is the remaining cross-cell
interference.  Identity (2) is algebraic; only Fourier quadrature and the
finite frequency integral are numerical.

On the full real line this is the physical convolution identity

    U_4 = 2*pi ||g*g||_2^2,
    g = sum_n p_n - z_c,
    g*g = sum_(n,m) p_n*p_m - 2 sum_n p_n*z_c + z_c*z_c. (3)

The columns in (1) are precisely the Fourier transforms of the signed
convolution summands in (3).  Thus no boundary atom or center term is removed;
the finite-height implementation is a direct spectral quadrature of the same
ledger.

Tail atoms receive centered carrier coordinates ``log(n/X)`` and the center
receives diagnostic coordinate zero.  Near-product cells bin sums of these
coordinates.  This assignment organizes the exact pair ledger but does not
turn the continuum center into a Dirichlet atom.  A second partition groups
formal integer products, with center label one; as explained in the imported
moment probe, that is only a finite multiplicative-energy comparator.

All output is D-rated finite evidence.  Cell signs, sampled-offset verdicts,
and fitted scales are not asymptotic estimates and prove no zero-free region.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field

import numpy as np

from r71_fixed_strip_moment_probe import completed_channel_transforms
from r71_large_value_width_probe import build_completed_microblock


PAIR_SECTORS = ("tail-tail", "tail-center", "center-center")


def _trapezoid_weights(points: np.ndarray) -> np.ndarray:
    points = np.asarray(points, dtype=float)
    if points.ndim != 1 or len(points) < 2:
        raise ValueError("at least two one-dimensional integration points are required")
    differences = np.diff(points)
    if not np.all(np.isfinite(points)) or np.any(differences <= 0.0):
        raise ValueError("integration points must be finite and strictly increasing")
    weights = np.empty_like(points)
    weights[0] = differences[0] / 2.0
    weights[-1] = differences[-1] / 2.0
    if len(points) > 2:
        weights[1:-1] = (points[2:] - points[:-2]) / 2.0
    return weights


def _energy(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.dot(weights, np.abs(values) ** 2))


def _real_cross(
    left: np.ndarray, right: np.ndarray, weights: np.ndarray
) -> float:
    return float(2.0 * np.dot(weights, np.real(left * np.conj(right))))


@dataclass(frozen=True)
class PairChannelSystem:
    """Exact pair expansion of one finite completed transform."""

    scale: float
    cutoff: int
    height: float
    frequency_step: float
    active_product_values: tuple[int, ...]
    channel_count: int
    pair_count: int
    direct_square_completion_error: float
    frequencies: np.ndarray = field(repr=False, compare=False)
    integration_weights: np.ndarray = field(repr=False, compare=False)
    channel_values: np.ndarray = field(repr=False, compare=False)
    pair_values: np.ndarray = field(repr=False, compare=False)
    pair_coordinates: np.ndarray = field(repr=False, compare=False)
    pair_formal_products: tuple[int, ...] = field(repr=False, compare=False)
    pair_sectors: tuple[str, ...] = field(repr=False, compare=False)

    @property
    def completed_square(self) -> np.ndarray:
        return np.sum(self.channel_values, axis=1) ** 2

    @property
    def completed_fourth_moment(self) -> float:
        return _energy(self.completed_square, self.integration_weights)

    @property
    def atomic_pair_diagonal(self) -> float:
        return float(
            sum(
                _energy(self.pair_values[:, index], self.integration_weights)
                for index in range(self.pair_count)
            )
        )


@dataclass(frozen=True)
class PairSectorAudit:
    """Exact signed tail/center ledger for ``F^2``."""

    completed_fourth_moment: float
    tail_tail_energy: float
    tail_center_energy: float
    center_center_energy: float
    tail_tail_tail_center_cross: float
    tail_tail_center_center_cross: float
    tail_center_center_center_cross: float
    center_net_contribution: float
    ledger_error: float


@dataclass(frozen=True)
class PairCellAudit:
    """Identity (2) for one exact or near-product partition."""

    partition_kind: str
    cell_width: float | None
    offset_fraction: float
    cell_count: int
    completed_fourth_moment: float
    atomic_pair_diagonal: float
    cell_diagonal: float
    within_cell_interference: float
    cross_cell_interference: float
    positive_cross_cell_interference: float
    negative_cross_cell_interference: float
    completed_to_cell_diagonal_ratio: float
    largest_cell_energy_fraction: float
    cell_completion_error: float

    @property
    def cell_diagonal_dominates(self) -> bool:
        tolerance = 1.0e-12 * max(1.0, self.completed_fourth_moment)
        return self.completed_fourth_moment <= self.cell_diagonal + tolerance


@dataclass(frozen=True)
class CellScaleEnvelope:
    """Offset sensitivity at one near-product cell width."""

    cell_width: float
    offset_count: int
    minimum_cell_count: int
    maximum_cell_count: int
    minimum_completed_to_diagonal_ratio: float
    maximum_completed_to_diagonal_ratio: float
    minimum_within_interference_over_atomic: float
    maximum_within_interference_over_atomic: float
    minimum_cross_interference_over_atomic: float
    maximum_cross_interference_over_atomic: float
    domination_fails_at_every_sampled_offset: bool
    domination_holds_at_every_sampled_offset: bool


@dataclass(frozen=True)
class PairCellScan:
    """Completed sector, exact-product, and near-cell diagnostics."""

    system: PairChannelSystem
    sector_audit: PairSectorAudit
    atomic_audit: PairCellAudit
    exact_product_audit: PairCellAudit
    near_audits: tuple[PairCellAudit, ...]
    scale_envelopes: tuple[CellScaleEnvelope, ...]
    sampled_falsifications: tuple[str, ...]


def build_pair_channel_system(
    scale: float = 127.0,
    cutoff: int = 8,
    height: float = 80.0,
    frequency_step: float = 0.1,
    step: float = 0.04,
    order: int = 1,
    half_width: float | None = None,
    taper_power: int = 2,
    gaussian_order: int = 16,
) -> PairChannelSystem:
    """Build every unordered pair channel, including signed center pairs."""

    if not math.isfinite(height) or height <= 0.0:
        raise ValueError("height must be finite and positive")
    if not math.isfinite(frequency_step) or frequency_step <= 0.0:
        raise ValueError("frequency_step must be finite and positive")
    model = build_completed_microblock(
        scale=scale,
        cutoff=cutoff,
        step=step,
        order=order,
        half_width=half_width,
        taper_power=taper_power,
        gaussian_order=gaussian_order,
    )
    half_count = math.ceil(height / frequency_step)
    regular = frequency_step * np.arange(-half_count, half_count + 1, dtype=float)
    frequencies = np.unique(np.concatenate([regular, np.array([-height, height])]))
    weights = _trapezoid_weights(frequencies)
    channels = completed_channel_transforms(
        model, frequencies, gaussian_order=gaussian_order
    )

    centered_coordinates = tuple(
        math.log(product) - model.logarithmic_center
        for product in model.active_product_values
    ) + (0.0,)
    formal_labels = model.active_product_values + (1,)
    center_index = len(formal_labels) - 1
    pair_columns: list[np.ndarray] = []
    pair_coordinates: list[float] = []
    pair_products: list[int] = []
    pair_sectors: list[str] = []
    for left in range(len(formal_labels)):
        for right in range(left, len(formal_labels)):
            multiplicity = 1.0 if left == right else 2.0
            pair_columns.append(
                multiplicity * channels[:, left] * channels[:, right]
            )
            pair_coordinates.append(
                centered_coordinates[left] + centered_coordinates[right]
            )
            pair_products.append(formal_labels[left] * formal_labels[right])
            if left == center_index and right == center_index:
                pair_sectors.append("center-center")
            elif right == center_index:
                pair_sectors.append("tail-center")
            else:
                pair_sectors.append("tail-tail")
    pair_values = np.column_stack(pair_columns)
    direct_square = np.sum(channels, axis=1) ** 2
    completion_error = float(
        np.max(np.abs(np.sum(pair_values, axis=1) - direct_square))
    )
    return PairChannelSystem(
        scale=scale,
        cutoff=cutoff,
        height=height,
        frequency_step=frequency_step,
        active_product_values=model.active_product_values,
        channel_count=channels.shape[1],
        pair_count=pair_values.shape[1],
        direct_square_completion_error=completion_error,
        frequencies=frequencies,
        integration_weights=weights,
        channel_values=channels,
        pair_values=pair_values,
        pair_coordinates=np.asarray(pair_coordinates),
        pair_formal_products=tuple(pair_products),
        pair_sectors=tuple(pair_sectors),
    )


def audit_pair_sectors(system: PairChannelSystem) -> PairSectorAudit:
    """Expand ``||TT+TC+CC||_2^2`` with every signed cross term."""

    sector_values = {
        sector: np.sum(
            system.pair_values[
                :, [value == sector for value in system.pair_sectors]
            ],
            axis=1,
        )
        for sector in PAIR_SECTORS
    }
    tail_tail = _energy(
        sector_values["tail-tail"], system.integration_weights
    )
    tail_center = _energy(
        sector_values["tail-center"], system.integration_weights
    )
    center_center = _energy(
        sector_values["center-center"], system.integration_weights
    )
    tt_tc = _real_cross(
        sector_values["tail-tail"],
        sector_values["tail-center"],
        system.integration_weights,
    )
    tt_cc = _real_cross(
        sector_values["tail-tail"],
        sector_values["center-center"],
        system.integration_weights,
    )
    tc_cc = _real_cross(
        sector_values["tail-center"],
        sector_values["center-center"],
        system.integration_weights,
    )
    completed = system.completed_fourth_moment
    ledger_sum = tail_tail + tail_center + center_center + tt_tc + tt_cc + tc_cc
    return PairSectorAudit(
        completed_fourth_moment=completed,
        tail_tail_energy=tail_tail,
        tail_center_energy=tail_center,
        center_center_energy=center_center,
        tail_tail_tail_center_cross=tt_tc,
        tail_tail_center_center_cross=tt_cc,
        tail_center_center_center_cross=tc_cc,
        center_net_contribution=completed - tail_tail,
        ledger_error=abs(completed - ledger_sum),
    )


def _audit_partition(
    system: PairChannelSystem,
    keys: tuple[object, ...],
    partition_kind: str,
    cell_width: float | None,
    offset_fraction: float,
    gram_cell_limit: int,
) -> PairCellAudit:
    if len(keys) != system.pair_count:
        raise ValueError("partition keys must match the pair count")
    grouped_indices: dict[object, list[int]] = {}
    for index, key in enumerate(keys):
        grouped_indices.setdefault(key, []).append(index)
    cell_values = np.column_stack(
        [
            np.sum(system.pair_values[:, indices], axis=1)
            for indices in grouped_indices.values()
        ]
    )
    cell_energies = np.asarray(
        [
            _energy(cell_values[:, index], system.integration_weights)
            for index in range(cell_values.shape[1])
        ]
    )
    cell_diagonal = float(np.sum(cell_energies))
    completed = system.completed_fourth_moment
    atomic = system.atomic_pair_diagonal
    cross = completed - cell_diagonal
    positive_cross = math.nan
    negative_cross = math.nan
    if cell_values.shape[1] <= gram_cell_limit:
        weighted = system.integration_weights[:, np.newaxis] * cell_values
        gram = np.real(np.conj(cell_values).T @ weighted)
        upper = gram[np.triu_indices(len(gram), 1)]
        positive_cross = float(2.0 * np.sum(upper[upper > 0.0]))
        negative_cross = float(2.0 * np.sum(upper[upper < 0.0]))
    completion_error = float(
        np.max(
            np.abs(
                np.sum(cell_values, axis=1)
                - np.sum(system.pair_values, axis=1)
            )
        )
    )
    return PairCellAudit(
        partition_kind=partition_kind,
        cell_width=cell_width,
        offset_fraction=offset_fraction,
        cell_count=cell_values.shape[1],
        completed_fourth_moment=completed,
        atomic_pair_diagonal=atomic,
        cell_diagonal=cell_diagonal,
        within_cell_interference=cell_diagonal - atomic,
        cross_cell_interference=cross,
        positive_cross_cell_interference=positive_cross,
        negative_cross_cell_interference=negative_cross,
        completed_to_cell_diagonal_ratio=completed / cell_diagonal,
        largest_cell_energy_fraction=(
            float(np.max(cell_energies) / cell_diagonal)
            if cell_diagonal > 0.0
            else math.nan
        ),
        cell_completion_error=completion_error,
    )


def atomic_pair_audit(
    system: PairChannelSystem, gram_cell_limit: int = 512
) -> PairCellAudit:
    """Use one cell per unordered pair channel."""

    return _audit_partition(
        system,
        tuple(range(system.pair_count)),
        "atomic-pairs",
        None,
        0.0,
        gram_cell_limit,
    )


def exact_product_cell_audit(
    system: PairChannelSystem, gram_cell_limit: int = 512
) -> PairCellAudit:
    """Group equal formal integer products, retaining signed center pairs."""

    return _audit_partition(
        system,
        system.pair_formal_products,
        "exact-products-formal-center",
        0.0,
        0.0,
        gram_cell_limit,
    )


def near_product_cell_audit(
    system: PairChannelSystem,
    cell_width: float,
    offset_fraction: float = 0.0,
    gram_cell_limit: int = 512,
) -> PairCellAudit:
    """Bin centered pair coordinates in cells of a chosen log width."""

    if not math.isfinite(cell_width) or cell_width <= 0.0:
        raise ValueError("cell_width must be finite and positive")
    if (
        not math.isfinite(offset_fraction)
        or not 0.0 <= offset_fraction < 1.0
    ):
        raise ValueError("offset_fraction must lie in [0,1)")
    offset = offset_fraction * cell_width
    keys = tuple(
        int(math.floor((coordinate - offset) / cell_width))
        for coordinate in system.pair_coordinates
    )
    return _audit_partition(
        system,
        keys,
        "near-products",
        cell_width,
        offset_fraction,
        gram_cell_limit,
    )


def _cell_scale_envelope(
    audits: tuple[PairCellAudit, ...]
) -> CellScaleEnvelope:
    atomic = audits[0].atomic_pair_diagonal
    ratios = [audit.completed_to_cell_diagonal_ratio for audit in audits]
    within = [audit.within_cell_interference / atomic for audit in audits]
    across = [audit.cross_cell_interference / atomic for audit in audits]
    tolerance = 1.0e-12
    return CellScaleEnvelope(
        cell_width=float(audits[0].cell_width),
        offset_count=len(audits),
        minimum_cell_count=min(audit.cell_count for audit in audits),
        maximum_cell_count=max(audit.cell_count for audit in audits),
        minimum_completed_to_diagonal_ratio=min(ratios),
        maximum_completed_to_diagonal_ratio=max(ratios),
        minimum_within_interference_over_atomic=min(within),
        maximum_within_interference_over_atomic=max(within),
        minimum_cross_interference_over_atomic=min(across),
        maximum_cross_interference_over_atomic=max(across),
        domination_fails_at_every_sampled_offset=(
            min(ratios) > 1.0 + tolerance
        ),
        domination_holds_at_every_sampled_offset=(
            max(ratios) <= 1.0 + tolerance
        ),
    )


def scan_pair_cells(
    scale: float = 127.0,
    cutoff: int = 8,
    height: float = 80.0,
    frequency_step: float = 0.1,
    cell_widths: tuple[float, ...] | None = None,
    offset_count: int = 16,
    step: float = 0.04,
    order: int = 1,
    half_width: float | None = None,
    taper_power: int = 2,
    gaussian_order: int = 16,
    gram_cell_limit: int = 512,
) -> PairCellScan:
    """Scan exact and near-product pair partitions on one finite block."""

    if offset_count < 1:
        raise ValueError("offset_count must be positive")
    if gram_cell_limit < 1:
        raise ValueError("gram_cell_limit must be positive")
    if cell_widths is None:
        resolution = 1.0 / height
        cell_widths = tuple(
            sorted(
                {
                    resolution / 5.0,
                    resolution / 2.5,
                    resolution / 2.0,
                    resolution / 1.25,
                    resolution,
                    2.0 * resolution,
                    step,
                    4.0 * resolution,
                    8.0 * resolution,
                    16.0 * resolution,
                }
            )
        )
    if (
        not cell_widths
        or tuple(sorted(set(cell_widths))) != cell_widths
        or any(not math.isfinite(width) or width <= 0.0 for width in cell_widths)
    ):
        raise ValueError("cell_widths must be finite, positive, and increasing")

    system = build_pair_channel_system(
        scale=scale,
        cutoff=cutoff,
        height=height,
        frequency_step=frequency_step,
        step=step,
        order=order,
        half_width=half_width,
        taper_power=taper_power,
        gaussian_order=gaussian_order,
    )
    sector = audit_pair_sectors(system)
    atomic = atomic_pair_audit(system, gram_cell_limit)
    exact = exact_product_cell_audit(system, gram_cell_limit)
    near_audits: list[PairCellAudit] = []
    envelopes: list[CellScaleEnvelope] = []
    for width in cell_widths:
        width_audits = tuple(
            near_product_cell_audit(
                system,
                width,
                offset_fraction=index / offset_count,
                gram_cell_limit=gram_cell_limit,
            )
            for index in range(offset_count)
        )
        near_audits.extend(width_audits)
        envelopes.append(_cell_scale_envelope(width_audits))

    falsifications: list[str] = []
    if not atomic.cell_diagonal_dominates:
        falsifications.append("atomic pair-diagonal domination")
    if not exact.cell_diagonal_dominates:
        falsifications.append("exact-product cell-diagonal domination")
    for envelope in envelopes:
        if envelope.domination_fails_at_every_sampled_offset:
            falsifications.append(
                "near-cell domination at width "
                f"{envelope.cell_width:.8g} for every sampled offset"
            )

    # With offset zero, dyadic widths define nested partitions.  A decrease
    # of the cell diagonal after coarsening exactly falsifies monotone positive
    # merge energy; the merge increment is a signed cross inner product.
    zero_offset = {
        audit.cell_width: audit
        for audit in near_audits
        if audit.offset_fraction == 0.0
    }
    for width, audit in zero_offset.items():
        coarser = zero_offset.get(2.0 * width)
        if coarser is not None and coarser.cell_diagonal < (
            audit.cell_diagonal - 1.0e-12 * max(1.0, audit.cell_diagonal)
        ):
            falsifications.append(
                "monotone nonnegative dyadic cell merging at widths "
                f"{width:.8g}->{2.0 * width:.8g}"
            )
            break

    return PairCellScan(
        system=system,
        sector_audit=sector,
        atomic_audit=atomic,
        exact_product_audit=exact,
        near_audits=tuple(near_audits),
        scale_envelopes=tuple(envelopes),
        sampled_falsifications=tuple(falsifications),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=float, default=127.0)
    parser.add_argument("--cutoff", type=int, default=8)
    parser.add_argument("--height", type=float, default=80.0)
    parser.add_argument("--frequency-step", type=float, default=0.1)
    parser.add_argument("--cell-widths", nargs="+", type=float)
    parser.add_argument("--offset-count", type=int, default=16)
    parser.add_argument("--step", type=float, default=0.04)
    parser.add_argument("--order", type=int, default=1)
    parser.add_argument("--half-width", type=float)
    parser.add_argument("--taper-power", type=int, default=2)
    parser.add_argument("--gaussian-order", type=int, default=16)
    args = parser.parse_args()
    widths = tuple(args.cell_widths) if args.cell_widths is not None else None
    scan = scan_pair_cells(
        scale=args.scale,
        cutoff=args.cutoff,
        height=args.height,
        frequency_step=args.frequency_step,
        cell_widths=widths,
        offset_count=args.offset_count,
        step=args.step,
        order=args.order,
        half_width=args.half_width,
        taper_power=args.taper_power,
        gaussian_order=args.gaussian_order,
    )
    system = scan.system
    sector = scan.sector_audit
    print("rating=D finite pair-cell diagnostic; no asymptotic claim")
    print(
        f"X={system.scale:g} Y={system.cutoff} T={system.height:g} "
        f"channels={system.channel_count} pairs={system.pair_count} "
        f"square-closure={system.direct_square_completion_error:.3e}"
    )
    print(
        f"U4={sector.completed_fourth_moment:.9g} "
        f"TT={sector.tail_tail_energy:.9g} "
        f"TC={sector.tail_center_energy:.9g} "
        f"CC={sector.center_center_energy:.9g}"
    )
    print(
        "sector crosses: "
        f"2<TT,TC>={sector.tail_tail_tail_center_cross:+.9g} "
        f"2<TT,CC>={sector.tail_tail_center_center_cross:+.9g} "
        f"2<TC,CC>={sector.tail_center_center_center_cross:+.9g}"
    )
    print(
        "finite domination ratios: "
        f"atomic={scan.atomic_audit.completed_to_cell_diagonal_ratio:.6g} "
        f"exact-product={scan.exact_product_audit.completed_to_cell_diagonal_ratio:.6g}"
    )
    print("near-product offset envelopes")
    for envelope in scan.scale_envelopes:
        print(
            f"  width={envelope.cell_width:.8g} "
            f"cells={envelope.minimum_cell_count}-{envelope.maximum_cell_count} "
            f"U4/D={envelope.minimum_completed_to_diagonal_ratio:.6g}.."
            f"{envelope.maximum_completed_to_diagonal_ratio:.6g} "
            f"within/atom={envelope.minimum_within_interference_over_atomic:+.6g}.."
            f"{envelope.maximum_within_interference_over_atomic:+.6g} "
            f"across/atom={envelope.minimum_cross_interference_over_atomic:+.6g}.."
            f"{envelope.maximum_cross_interference_over_atomic:+.6g}"
        )
    print("sampled candidate inequalities falsified:")
    for item in scan.sampled_falsifications:
        print(f"  - {item}")
    print("interpretation=D-rated finite ledger only")


if __name__ == "__main__":
    main()
