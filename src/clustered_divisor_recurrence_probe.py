#!/usr/bin/env python3
"""Clustered-divisor stress test for completed-detector recurrence.

This module adapts the R5 symmetric clustered divisor to the fixed triangular
detector

    B(R) = sum_z H_ell(z) exp(-i z R),
    H_ell(z) = 4 sin(ell z/2)^2 / (ell z^2).

Pairs of consecutive critical-line quantile nodes are replaced by simple
quartets ``{+/-gamma +/- i Delta}`` at their midpoint.  This preserves the
functional/conjugation symmetries and changes the positive-height counting
staircase by at most one.  One designated quartet is the fixed carrier; later
quartets may be arranged in sparse clusters as in the R5 countermodel.

For the R5 construction every displaced node has the same outer width
``Delta``.  Riemann--von Mangoldt counting and ``H_ell(z)=O((1+|z|)^-2)``
make all detector coefficients absolutely summable.  Splitting the divisor
into its upper, critical, and lower layers gives exactly

    B(R) = exp(Delta R) A(R) + C(R) + exp(-Delta R) D(R),

where ``A`` is an absolutely convergent Bohr series.  Hence

    exp(-Delta R) B(R) -> A(R)                         (1)

uniformly.  Distinct real frequencies are orthogonal in Bohr mean, so

    M(|A|^2) = sum_lambda |a_lambda|^2 >= M_carrier > 0. (2)

If ``S=sum |a_lambda|`` and ``theta=M_carrier/2``, then

    lower_density{|A|^2 >= theta}
      >= (M(|A|^2)-theta)/(S^2-theta) > 0.              (3)

The same calculation applies to any fixed regular-block weight.  For the
rectangular block ``[R,R+L]``, put

    K=(exp(2 Delta L)-1)/(2 Delta).

The normalized block energy converges uniformly to

    J_L(R)=integral_0^L exp(2 Delta u)|A(R+u)|^2 du,

whose mean is ``K*M(|A|^2)`` and supremum is at most ``K*S^2``.  Thus (3)
also bounds the lower density of ``J_L >= K*M_carrier/2``; by (1), the actual
completed energy eventually exceeds ``K*M_carrier/4`` on that set.

Therefore the faithful fixed-width R5 clustered model cannot realize the
proposed zero-lower-density cancellation when the outer displacement is
attained by a fixed carrier.  A non-attained displacement supremum or an
adversarial sampling schedule is outside this theorem.  Numerical output is
only a D-rated finite illustration of the exact analytic argument.
"""

from __future__ import annotations

import argparse
import cmath
import math
from dataclasses import dataclass, field
from typing import Iterable

import numpy as np

from model_zeros import smooth_zeros


def triangular_transform(value: complex, length: float = 1.0) -> complex:
    """Return the entire triangular multiplier ``H_ell``."""

    if not math.isfinite(length) or length <= 0.0:
        raise ValueError("length must be finite and positive")
    value = complex(value)
    if not math.isfinite(value.real) or not math.isfinite(value.imag):
        raise ValueError("value must be finite")
    if abs(value) < 1.0e-12:
        return complex(length)
    return 4.0 * cmath.sin(length * value / 2.0) ** 2 / (
        length * value**2
    )


@dataclass(frozen=True)
class ClusteredSymmetricDivisor:
    """A finite quantile divisor with count-preserving off-line quartets."""

    base_positive_ordinates: tuple[float, ...]
    displacement: float
    moved_pair_starts: tuple[int, ...]
    moved_midpoints: tuple[float, ...]
    nodes: tuple[complex, ...]
    maximum_counting_discrepancy: int

    @property
    def fixed_carrier_midpoint(self) -> float:
        return self.moved_midpoints[0]

    @property
    def is_simple(self) -> bool:
        return len(set(self.nodes)) == len(self.nodes)

    @property
    def has_exact_symmetries(self) -> bool:
        node_set = set(self.nodes)
        return all(-node in node_set and node.conjugate() in node_set for node in node_set)


def _maximum_counting_discrepancy(
    base: tuple[float, ...], nodes: tuple[complex, ...]
) -> int:
    positive_model = sorted(node.real for node in nodes if node.real > 0.0)
    events = sorted(set(base) | set(positive_model))
    probes: list[float] = []
    if events:
        probes.append(events[0] - 1.0)
        probes.extend(events)
        probes.extend(
            (left + right) / 2.0 for left, right in zip(events, events[1:])
        )
        probes.append(events[-1] + 1.0)
    discrepancy = 0
    for point in probes:
        base_count = sum(value <= point for value in base)
        model_count = sum(value <= point for value in positive_model)
        discrepancy = max(discrepancy, abs(base_count - model_count))
    return discrepancy


def build_clustered_symmetric_divisor(
    positive_ordinates: Iterable[float],
    displacement: float,
    moved_pair_starts: Iterable[int],
) -> ClusteredSymmetricDivisor:
    """Move disjoint consecutive pairs to symmetric off-line quartets."""

    base = tuple(float(value) for value in positive_ordinates)
    if len(base) < 2 or any(
        not math.isfinite(value) or value <= 0.0 for value in base
    ):
        raise ValueError("positive ordinates must be finite and positive")
    if tuple(sorted(set(base))) != base:
        raise ValueError("positive ordinates must be strictly increasing")
    if not math.isfinite(displacement) or not 0.0 < displacement < 0.5:
        raise ValueError("displacement must lie strictly between zero and one half")
    pair_starts = tuple(int(index) for index in moved_pair_starts)
    if not pair_starts or tuple(sorted(set(pair_starts))) != pair_starts:
        raise ValueError("moved pair starts must be nonempty and increasing")
    if any(index < 0 or index + 1 >= len(base) for index in pair_starts):
        raise ValueError("a moved pair lies outside the positive ordinates")
    if any(right <= left + 1 for left, right in zip(pair_starts, pair_starts[1:])):
        raise ValueError("moved consecutive pairs must be disjoint")

    start_set = set(pair_starts)
    nodes: list[complex] = []
    midpoints: list[float] = []
    index = 0
    while index < len(base):
        if index in start_set:
            midpoint = (base[index] + base[index + 1]) / 2.0
            midpoints.append(midpoint)
            for real_sign in (-1.0, 1.0):
                for imaginary_sign in (-1.0, 1.0):
                    nodes.append(
                        complex(
                            real_sign * midpoint,
                            imaginary_sign * displacement,
                        )
                    )
            index += 2
        else:
            nodes.extend((complex(-base[index]), complex(base[index])))
            index += 1
    node_tuple = tuple(sorted(nodes, key=lambda node: (node.real, node.imag)))
    return ClusteredSymmetricDivisor(
        base_positive_ordinates=base,
        displacement=displacement,
        moved_pair_starts=pair_starts,
        moved_midpoints=tuple(midpoints),
        nodes=node_tuple,
        maximum_counting_discrepancy=_maximum_counting_discrepancy(
            base, node_tuple
        ),
    )


def quantile_clustered_divisor(
    node_count: int = 80,
    displacement: float = 0.2,
    moved_pair_starts: tuple[int, ...] = (0, 20, 22, 50, 52, 54),
) -> ClusteredSymmetricDivisor:
    """Build the finite diagnostic from the repository's smooth RvM nodes."""

    if node_count < 2:
        raise ValueError("node_count must be at least two")
    ordinates = tuple(float(value) for value in smooth_zeros(node_count))
    return build_clustered_symmetric_divisor(
        ordinates, displacement, moved_pair_starts
    )


def _evaluate_real_frequency_series(
    frequencies: np.ndarray,
    coefficients: np.ndarray,
    points: np.ndarray,
    chunk_size: int = 4096,
) -> np.ndarray:
    answer = np.empty(len(points), dtype=complex)
    for start in range(0, len(points), chunk_size):
        local = points[start : start + chunk_size]
        answer[start : start + len(local)] = (
            np.exp(-1j * local[:, np.newaxis] * frequencies) @ coefficients
        )
    return answer


@dataclass(frozen=True)
class CompletedExponentialDetector:
    """Upper/critical/lower decomposition of one finite completed detector."""

    divisor: ClusteredSymmetricDivisor
    length: float
    top_frequencies: np.ndarray = field(repr=False, compare=False)
    top_coefficients: np.ndarray = field(repr=False, compare=False)
    critical_frequencies: np.ndarray = field(repr=False, compare=False)
    critical_coefficients: np.ndarray = field(repr=False, compare=False)
    bottom_frequencies: np.ndarray = field(repr=False, compare=False)
    bottom_coefficients: np.ndarray = field(repr=False, compare=False)
    carrier_top_indices: tuple[int, ...]

    @property
    def displacement(self) -> float:
        return self.divisor.displacement

    @property
    def top_l1_norm(self) -> float:
        return float(np.sum(np.abs(self.top_coefficients)))

    @property
    def top_mean_square(self) -> float:
        return float(np.sum(np.abs(self.top_coefficients) ** 2))

    @property
    def carrier_mean_square(self) -> float:
        return float(
            np.sum(np.abs(self.top_coefficients[list(self.carrier_top_indices)]) ** 2)
        )

    @property
    def critical_l1_norm(self) -> float:
        return float(np.sum(np.abs(self.critical_coefficients)))

    @property
    def bottom_l1_norm(self) -> float:
        return float(np.sum(np.abs(self.bottom_coefficients)))

    def top_series(self, points: np.ndarray | Iterable[float]) -> np.ndarray:
        values = np.asarray(tuple(points), dtype=float)
        return _evaluate_real_frequency_series(
            self.top_frequencies, self.top_coefficients, values
        )

    def normalized_detector(
        self, points: np.ndarray | Iterable[float]
    ) -> np.ndarray:
        """Evaluate ``exp(-Delta R)B(R)`` without exponential overflow."""

        values = np.asarray(tuple(points), dtype=float)
        if values.ndim != 1 or not np.all(np.isfinite(values)):
            raise ValueError("points must be a finite one-dimensional iterable")
        top = _evaluate_real_frequency_series(
            self.top_frequencies, self.top_coefficients, values
        )
        critical = _evaluate_real_frequency_series(
            self.critical_frequencies, self.critical_coefficients, values
        )
        bottom = _evaluate_real_frequency_series(
            self.bottom_frequencies, self.bottom_coefficients, values
        )
        return (
            top
            + np.exp(-self.displacement * values) * critical
            + np.exp(-2.0 * self.displacement * values) * bottom
        )

    def uniform_normalization_error_bound(self, start: float) -> float:
        if not math.isfinite(start) or start < 0.0:
            raise ValueError("start must be finite and nonnegative")
        return (
            math.exp(-self.displacement * start) * self.critical_l1_norm
            + math.exp(-2.0 * self.displacement * start)
            * self.bottom_l1_norm
        )


def build_completed_detector(
    divisor: ClusteredSymmetricDivisor,
    length: float = 1.0,
) -> CompletedExponentialDetector:
    """Attach the fixed triangular multiplier to every divisor node."""

    if not math.isfinite(length) or length <= 0.0:
        raise ValueError("length must be finite and positive")
    tolerance = 1.0e-12
    top_nodes = [
        node
        for node in divisor.nodes
        if abs(node.imag - divisor.displacement) <= tolerance
    ]
    critical_nodes = [node for node in divisor.nodes if abs(node.imag) <= tolerance]
    bottom_nodes = [
        node
        for node in divisor.nodes
        if abs(node.imag + divisor.displacement) <= tolerance
    ]

    def arrays(nodes: list[complex]) -> tuple[np.ndarray, np.ndarray]:
        return (
            np.asarray([node.real for node in nodes], dtype=float),
            np.asarray(
                [triangular_transform(node, length) for node in nodes],
                dtype=complex,
            ),
        )

    top_frequencies, top_coefficients = arrays(top_nodes)
    critical_frequencies, critical_coefficients = arrays(critical_nodes)
    bottom_frequencies, bottom_coefficients = arrays(bottom_nodes)
    carrier = divisor.fixed_carrier_midpoint
    carrier_indices = tuple(
        index
        for index, frequency in enumerate(top_frequencies)
        if math.isclose(abs(float(frequency)), carrier, rel_tol=0.0, abs_tol=1.0e-10)
    )
    if len(carrier_indices) != 2:
        raise RuntimeError("the fixed carrier quartet was not retained")
    return CompletedExponentialDetector(
        divisor=divisor,
        length=length,
        top_frequencies=top_frequencies,
        top_coefficients=top_coefficients,
        critical_frequencies=critical_frequencies,
        critical_coefficients=critical_coefficients,
        bottom_frequencies=bottom_frequencies,
        bottom_coefficients=bottom_coefficients,
        carrier_top_indices=carrier_indices,
    )


@dataclass(frozen=True)
class CarrierRecurrenceBound:
    """Exact Bohr-mean lower-density ledger for a fixed carrier quartet."""

    displacement: float
    block_length: float
    carrier_mean_square: float
    top_mean_square: float
    top_l1_norm: float
    block_weight: float
    limiting_block_mean: float
    limiting_block_supremum_bound: float
    limiting_block_threshold: float
    eventual_completed_block_threshold: float
    lower_density_bound: float
    normalization_remainder_target: float
    sufficient_start_for_completed_threshold: float


def carrier_recurrence_bound(
    detector: CompletedExponentialDetector,
    block_length: float = 1.0,
) -> CarrierRecurrenceBound:
    """Return the quantitative form of (2)--(3) for one block length."""

    if not math.isfinite(block_length) or block_length <= 0.0:
        raise ValueError("block_length must be finite and positive")
    delta = detector.displacement
    carrier = detector.carrier_mean_square
    mean_square = detector.top_mean_square
    l1_norm = detector.top_l1_norm
    if not carrier > 0.0 or mean_square + 1.0e-30 < carrier:
        raise RuntimeError("the fixed carrier has no positive Bohr mass")
    threshold = carrier / 2.0
    denominator = l1_norm**2 - threshold
    density = (mean_square - threshold) / denominator
    block_weight = math.expm1(2.0 * delta * block_length) / (2.0 * delta)

    # If ||normalized detector-A|| <= r and ||A||_infinity <= S, then the
    # pointwise squared-modulus error is at most r(2S+r).  The target below
    # makes the integrated error at most K*carrier/4.
    remainder_target = math.sqrt(l1_norm**2 + carrier / 4.0) - l1_norm
    starts = [0.0]
    if detector.critical_l1_norm > 0.0:
        starts.append(
            math.log(2.0 * detector.critical_l1_norm / remainder_target) / delta
        )
    if detector.bottom_l1_norm > 0.0:
        starts.append(
            math.log(2.0 * detector.bottom_l1_norm / remainder_target)
            / (2.0 * delta)
        )
    sufficient_start = max(0.0, *starts)
    return CarrierRecurrenceBound(
        displacement=delta,
        block_length=block_length,
        carrier_mean_square=carrier,
        top_mean_square=mean_square,
        top_l1_norm=l1_norm,
        block_weight=block_weight,
        limiting_block_mean=block_weight * mean_square,
        limiting_block_supremum_bound=block_weight * l1_norm**2,
        limiting_block_threshold=block_weight * carrier / 2.0,
        eventual_completed_block_threshold=block_weight * carrier / 4.0,
        lower_density_bound=density,
        normalization_remainder_target=remainder_target,
        sufficient_start_for_completed_threshold=sufficient_start,
    )


@dataclass(frozen=True)
class FiniteRecurrenceDiagnostic:
    """D-rated sampled densities supporting the analytic recurrence bound."""

    grid_start: float
    grid_end: float
    grid_step: float
    grid_count: int
    sampled_top_superlevel_density: float
    sampled_limiting_block_density: float
    sampled_completed_block_density: float
    maximum_normalized_decomposition_error: float


def finite_recurrence_diagnostic(
    detector: CompletedExponentialDetector,
    bound: CarrierRecurrenceBound,
    grid_start: float = 0.0,
    grid_end: float = 200.0,
    grid_step: float = 0.01,
) -> FiniteRecurrenceDiagnostic:
    """Sample the top series and normalized completed block energies."""

    if (
        not math.isfinite(grid_start)
        or not math.isfinite(grid_end)
        or grid_end <= grid_start
        or not math.isfinite(grid_step)
        or grid_step <= 0.0
    ):
        raise ValueError("provide a finite increasing grid and positive step")
    block_steps_float = bound.block_length / grid_step
    block_steps = int(round(block_steps_float))
    if block_steps < 1 or not math.isclose(
        block_steps * grid_step,
        bound.block_length,
        rel_tol=0.0,
        abs_tol=1.0e-10,
    ):
        raise ValueError("block_length must be an integer multiple of grid_step")
    start_points = np.arange(grid_start, grid_end + grid_step / 2.0, grid_step)
    all_points = np.arange(
        grid_start,
        grid_end + bound.block_length + grid_step / 2.0,
        grid_step,
    )
    top_all = detector.top_series(all_points)
    normalized_all = detector.normalized_detector(all_points)
    remainder = normalized_all - top_all
    maximum_error = float(np.max(np.abs(remainder[: len(start_points)])))

    offsets = grid_step * np.arange(block_steps + 1)
    quadrature = np.exp(2.0 * detector.displacement * offsets)
    quadrature[[0, -1]] *= 0.5
    quadrature *= grid_step
    top_squared = np.abs(top_all) ** 2
    normalized_squared = np.abs(normalized_all) ** 2
    limiting_blocks = np.convolve(top_squared, quadrature[::-1], mode="valid")
    completed_blocks = np.convolve(
        normalized_squared, quadrature[::-1], mode="valid"
    )
    limiting_blocks = limiting_blocks[: len(start_points)]
    completed_blocks = completed_blocks[: len(start_points)]
    eligible = start_points >= bound.sufficient_start_for_completed_threshold
    completed_density = (
        float(
            np.mean(
                completed_blocks[eligible]
                >= bound.eventual_completed_block_threshold
            )
        )
        if np.any(eligible)
        else math.nan
    )
    return FiniteRecurrenceDiagnostic(
        grid_start=grid_start,
        grid_end=grid_end,
        grid_step=grid_step,
        grid_count=len(start_points),
        sampled_top_superlevel_density=float(
            np.mean(
                top_squared[: len(start_points)]
                >= bound.carrier_mean_square / 2.0
            )
        ),
        sampled_limiting_block_density=float(
            np.mean(limiting_blocks >= bound.limiting_block_threshold)
        ),
        sampled_completed_block_density=completed_density,
        maximum_normalized_decomposition_error=maximum_error,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", type=int, default=80)
    parser.add_argument("--delta", type=float, default=0.2)
    parser.add_argument("--length", type=float, default=1.0)
    parser.add_argument("--block-length", type=float, default=1.0)
    parser.add_argument(
        "--moved-pair-starts",
        nargs="+",
        type=int,
        default=[0, 20, 22, 50, 52, 54],
    )
    parser.add_argument("--grid-start", type=float, default=0.0)
    parser.add_argument("--grid-end", type=float, default=200.0)
    parser.add_argument("--grid-step", type=float, default=0.01)
    args = parser.parse_args()
    divisor = quantile_clustered_divisor(
        node_count=args.nodes,
        displacement=args.delta,
        moved_pair_starts=tuple(args.moved_pair_starts),
    )
    detector = build_completed_detector(divisor, length=args.length)
    bound = carrier_recurrence_bound(detector, args.block_length)
    diagnostic = finite_recurrence_diagnostic(
        detector,
        bound,
        grid_start=args.grid_start,
        grid_end=args.grid_end,
        grid_step=args.grid_step,
    )
    print("rating=D finite diagnostic supporting an exact recurrence lemma")
    print(
        f"nodes={len(divisor.nodes)} moved-pairs={len(divisor.moved_pair_starts)} "
        f"count-error={divisor.maximum_counting_discrepancy} "
        f"simple={divisor.is_simple} symmetric={divisor.has_exact_symmetries}"
    )
    print(
        f"carrier-M2={bound.carrier_mean_square:.9g} "
        f"top-M2={bound.top_mean_square:.9g} S={bound.top_l1_norm:.9g} "
        f"analytic-lower-density={bound.lower_density_bound:.9g}"
    )
    print(
        f"block-K={bound.block_weight:.9g} "
        f"limiting-threshold={bound.limiting_block_threshold:.9g} "
        f"completed-threshold={bound.eventual_completed_block_threshold:.9g} "
        f"safe-start={bound.sufficient_start_for_completed_threshold:.6g}"
    )
    print(
        f"sampled top density={diagnostic.sampled_top_superlevel_density:.6g} "
        f"limiting-block density={diagnostic.sampled_limiting_block_density:.6g} "
        f"completed-block density={diagnostic.sampled_completed_block_density:.6g}"
    )
    print(
        "verdict: attained-width clustered cancellations do not produce "
        "zero-lower-density carrier energy"
    )


if __name__ == "__main__":
    main()
