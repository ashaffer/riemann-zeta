"""Exact finite ledgers for dyadic localization and packet participation.

The routines here prove only bucketing and abstract weighted-Cauchy ledgers.
They do not prove a cell estimate, arithmetic packet participation, the pair
endpoint, PAC, or the sharp four-cycle bound.

The two hypotheses which matter are deliberately enforced:

* weights are nonnegative, so localization does not destroy cancellation;
* both scale variables are nonzero integers, so their signed dyadic cells
  form a disjoint partition.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from typing import Hashable, Iterable, Mapping, Sequence


Cell = tuple[int, int, int, int]
WeightedPeak = tuple[int, int, Fraction]
ColorMatrix = tuple[int, int, int, int]
Completion = tuple[int, int, int, int]


def signed_dyadic_index(value: int) -> tuple[int, int]:
    """Return ``(sign, j)`` with ``2**j <= abs(value) < 2**(j+1)``."""

    value = int(value)
    if value == 0:
        raise ValueError("a dyadic peak variable must be nonzero")
    return (1 if value > 0 else -1, abs(value).bit_length() - 1)


def signed_dyadic_cell(first: int, second: int) -> Cell:
    """Return the unique signed dyadic cell of two nonzero integers."""

    first_sign, first_level = signed_dyadic_index(first)
    second_sign, second_level = signed_dyadic_index(second)
    return first_sign, second_sign, first_level, second_level


def completion_secant_peaks(
    first: Completion, second: Completion
) -> tuple[int, int]:
    """Return the signed carrier determinants ``(A, B)`` of a pair."""

    a1, a2, b1, b2 = (int(value) for value in first)
    other_a1, other_a2, other_b1, other_b2 = (
        int(value) for value in second
    )
    return (
        a1 * other_a2 - a2 * other_a1,
        b1 * other_b2 - b2 * other_b1,
    )


@dataclass(frozen=True)
class CollectiveDyadicLedger:
    """Exact bookkeeping for one nonnegative weighted collection."""

    item_count: int
    occupied_cells: int
    total_weight: Fraction
    maximum_cell_weight: Fraction
    sum_of_cell_weights: Fraction
    first_levels: int
    second_levels: int
    admissible_cell_count: int
    pigeonhole_upper_bound: Fraction
    cell_weights: tuple[tuple[Cell, Fraction], ...]

    @property
    def partition_is_exact(self) -> bool:
        return self.total_weight == self.sum_of_cell_weights

    @property
    def pigeonhole_bound_holds(self) -> bool:
        return self.total_weight <= self.pigeonhole_upper_bound


def collective_dyadic_ledger(
    items: Iterable[WeightedPeak],
) -> CollectiveDyadicLedger:
    """Bucket ``(first_peak, second_peak, weight)`` triples exactly.

    Repeated triples are retained.  This is intentional: in the pair
    endpoint their multiplicity is part of the nonnegative weight.
    """

    cells: dict[Cell, Fraction] = defaultdict(Fraction)
    total = Fraction(0)
    item_count = 0
    maximum_first_level = -1
    maximum_second_level = -1

    for first, second, raw_weight in items:
        weight = Fraction(raw_weight)
        if weight < 0:
            raise ValueError("collective localization requires nonnegative weights")
        cell = signed_dyadic_cell(first, second)
        cells[cell] += weight
        total += weight
        item_count += 1
        maximum_first_level = max(maximum_first_level, cell[2])
        maximum_second_level = max(maximum_second_level, cell[3])

    first_levels = maximum_first_level + 1
    second_levels = maximum_second_level + 1
    # There are two signs for each nonzero variable.  Empty input has no
    # admissible cells and is handled without a special fake level.
    admissible_cells = (
        4 * first_levels * second_levels if item_count else 0
    )
    maximum = max(cells.values(), default=Fraction(0))
    cell_sum = sum(cells.values(), Fraction(0))

    return CollectiveDyadicLedger(
        item_count=item_count,
        occupied_cells=len(cells),
        total_weight=total,
        maximum_cell_weight=maximum,
        sum_of_cell_weights=cell_sum,
        first_levels=first_levels,
        second_levels=second_levels,
        admissible_cell_count=admissible_cells,
        pigeonhole_upper_bound=admissible_cells * maximum,
        cell_weights=tuple(sorted(cells.items())),
    )


def completion_pair_dyadic_ledger(
    groups: Mapping[ColorMatrix, Sequence[Completion]],
    group_weights: Mapping[ColorMatrix, Fraction] | None = None,
) -> CollectiveDyadicLedger:
    """Localize the exact ordered off-diagonal completion-pair mass.

    A group of size ``m`` contributes its color weight exactly ``m*(m-1)``
    times.  The generic-sector hypothesis that both secant determinants are
    nonzero is checked by :func:`collective_dyadic_ledger` rather than hidden.
    """

    def weighted_peaks() -> Iterable[WeightedPeak]:
        for raw_colors, raw_completions in groups.items():
            colors = tuple(int(value) for value in raw_colors)
            if len(colors) != 4:
                raise ValueError("a color matrix must have four entries")
            color_key: ColorMatrix = colors  # type: ignore[assignment]
            weight = (
                Fraction(1)
                if group_weights is None
                else Fraction(group_weights[color_key])
            )
            completions = tuple(
                tuple(int(value) for value in completion)
                for completion in raw_completions
            )
            if any(len(completion) != 4 for completion in completions):
                raise ValueError("a carrier completion must have four entries")
            for first_index, first in enumerate(completions):
                for second_index, second in enumerate(completions):
                    if first_index == second_index:
                        continue
                    first_peak, second_peak = completion_secant_peaks(
                        first, second  # type: ignore[arg-type]
                    )
                    yield first_peak, second_peak, weight

    return collective_dyadic_ledger(weighted_peaks())


@dataclass(frozen=True)
class RootedSurrogateLedger:
    """Quantify the loss in replacing a collective sum by its largest root."""

    root_count: int
    total_weight: Fraction
    maximum_root_weight: Fraction
    replacement_factor: Fraction


def rooted_surrogate_ledger(
    weights_by_root: Mapping[object, Fraction],
) -> RootedSurrogateLedger:
    """Return the exact gap between a root sum and a maximum over roots."""

    weights = [Fraction(weight) for weight in weights_by_root.values()]
    if any(weight < 0 for weight in weights):
        raise ValueError("the rooted surrogate ledger expects nonnegative weights")
    total = sum(weights, Fraction(0))
    maximum = max(weights, default=Fraction(0))
    factor = total / maximum if maximum else Fraction(0)
    return RootedSurrogateLedger(
        root_count=len(weights),
        total_weight=total,
        maximum_root_weight=maximum,
        replacement_factor=factor,
    )


@dataclass(frozen=True)
class WeightedPacketOverlapLedger:
    """Participation loads in the abstract packet-overlap lemma.

    If packet ``t`` has operator norm at most ``a_t`` and is supported on
    ``L_t x R_t``, the squared norm of their sum is at most the product of
    the two maximum weighted vertex-participation loads recorded here.
    """

    packet_count: int
    total_local_bound: Fraction
    maximum_left_load: Fraction
    maximum_right_load: Fraction
    squared_operator_bound: Fraction


@dataclass(frozen=True)
class BalancedPacketOverlapLedger:
    """Loads for the freely balanced packet-overlap inequality."""

    packet_count: int
    maximum_left_load: Fraction
    maximum_right_load: Fraction
    squared_operator_bound: Fraction


def weighted_packet_overlap_ledger(
    packets: Iterable[
        tuple[Fraction, Iterable[Hashable], Iterable[Hashable]]
    ],
) -> WeightedPacketOverlapLedger:
    """Return the exact loads in the weighted packet-overlap inequality."""

    left_loads: dict[Hashable, Fraction] = defaultdict(Fraction)
    right_loads: dict[Hashable, Fraction] = defaultdict(Fraction)
    total = Fraction(0)
    packet_count = 0
    for raw_bound, raw_left, raw_right in packets:
        local_bound = Fraction(raw_bound)
        if local_bound < 0:
            raise ValueError("packet operator bounds must be nonnegative")
        left = frozenset(raw_left)
        right = frozenset(raw_right)
        for vertex in left:
            left_loads[vertex] += local_bound
        for vertex in right:
            right_loads[vertex] += local_bound
        total += local_bound
        packet_count += 1

    maximum_left = max(left_loads.values(), default=Fraction(0))
    maximum_right = max(right_loads.values(), default=Fraction(0))
    return WeightedPacketOverlapLedger(
        packet_count=packet_count,
        total_local_bound=total,
        maximum_left_load=maximum_left,
        maximum_right_load=maximum_right,
        squared_operator_bound=maximum_left * maximum_right,
    )


def balanced_packet_overlap_ledger(
    packets: Iterable[
        tuple[
            Fraction,
            Fraction,
            Iterable[Hashable],
            Iterable[Hashable],
        ]
    ],
) -> BalancedPacketOverlapLedger:
    """Return packet loads for arbitrary positive balancing parameters.

    A tuple is ``(a_t, lambda_t, L_t, R_t)``.  Weighted Cauchy--Schwarz
    charges ``lambda_t`` on the left and ``a_t**2/lambda_t`` on the right.
    The symmetric specialization ``lambda_t=a_t`` is the simpler ledger
    above (zero-norm packets may simply be omitted).
    """

    left_loads: dict[Hashable, Fraction] = defaultdict(Fraction)
    right_loads: dict[Hashable, Fraction] = defaultdict(Fraction)
    packet_count = 0
    for raw_bound, raw_balance, raw_left, raw_right in packets:
        local_bound = Fraction(raw_bound)
        balance = Fraction(raw_balance)
        if local_bound < 0:
            raise ValueError("packet operator bounds must be nonnegative")
        if balance <= 0:
            raise ValueError("packet balancing parameters must be positive")
        right_charge = local_bound * local_bound / balance
        for vertex in frozenset(raw_left):
            left_loads[vertex] += balance
        for vertex in frozenset(raw_right):
            right_loads[vertex] += right_charge
        packet_count += 1

    maximum_left = max(left_loads.values(), default=Fraction(0))
    maximum_right = max(right_loads.values(), default=Fraction(0))
    return BalancedPacketOverlapLedger(
        packet_count=packet_count,
        maximum_left_load=maximum_left,
        maximum_right_load=maximum_right,
        squared_operator_bound=maximum_left * maximum_right,
    )
