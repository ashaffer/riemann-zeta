"""Hostile checks for the QP nondegenerate four-cycle proposal.

The finite computations in this module are diagnostics.  The exact routines
``blocked_latin_invariants`` and ``rectangle_value_and_gradient`` are also
used to replay two algebraic facts:

* fourth-trace control is stronger than the desired operator-norm control;
* the centered phase of a symmetric time bump is removable by diagonal and
  color unitary changes.

No finite computation in this file is used as evidence for an asymptotic
four-cycle estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Literal, Sequence

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.sparse import coo_matrix


FULL_APERTURE = 50.0 / 33.0
PROJECT_WIDTH = 0.2


@dataclass(frozen=True)
class BlockedLatinInvariants:
    order: int
    blocks: int
    color_degree: int
    frobenius_sq: float
    operator_norm: float
    fourth_trace: float
    nondegenerate_four_cycle: float


def blocked_latin_invariants(order: int, blocks: int | None = None) -> BlockedLatinInvariants:
    """Return exact invariants of repeated disjoint Latin blocks.

    Each block has ``order`` rows and columns, is colored by one Latin square
    on the same ``order`` colors, and uses ``z_c=order**(-1/2)``.  The row and
    column vertices of different blocks are disjoint, while the colors are
    reused.  Hence every color has degree ``blocks * order``.

    Taking ``blocks=order=L`` gives degree cap ``D=L**2`` and operator norm
    ``D**(1/4)``, but a nondegenerate fourth-trace contribution asymptotic to
    ``D**(3/2)``.
    """

    if order <= 0:
        raise ValueError("order must be positive")
    if blocks is None:
        blocks = order
    if blocks <= 0:
        raise ValueError("blocks must be positive")
    return BlockedLatinInvariants(
        order=order,
        blocks=blocks,
        color_degree=blocks * order,
        frobenius_sq=float(blocks * order),
        operator_norm=math.sqrt(order),
        fourth_trace=float(blocks * order * order),
        nondegenerate_four_cycle=float(blocks * (order - 1) ** 2),
    )


def centered_bump_quadrature(order: int = 128) -> tuple[np.ndarray, np.ndarray]:
    """Quadrature for a fixed legal smooth bump centered at time ``1/2``.

    The bump is supported in ``(1/3,2/3)``.  In the centered coordinate
    ``u=t-1/2`` it is proportional to

    ``exp(-1/(1-(6u)**2)) 1_(|u|<1/6)``.

    Returned weights are normalized to sum to one.
    """

    if order < 8:
        raise ValueError("quadrature order must be at least eight")
    nodes, weights = leggauss(order)
    radius = 1.0 / 6.0
    centered = radius * nodes
    bump = np.exp(-1.0 / (1.0 - nodes * nodes))
    normalized = radius * weights * bump
    normalized /= np.sum(normalized)
    return centered, normalized


def centered_fourier_amplitude(
    frequencies: Sequence[float] | np.ndarray,
    *,
    quadrature_order: int = 128,
    batch_size: int = 100_000,
) -> np.ndarray:
    """Evaluate the real centered transform ``Phi(xi)`` of the fixed bump."""

    values = np.asarray(frequencies, dtype=float)
    flat = values.ravel()
    centered, weights = centered_bump_quadrature(quadrature_order)
    answer = np.empty_like(flat)
    for start in range(0, flat.size, batch_size):
        stop = min(flat.size, start + batch_size)
        answer[start:stop] = np.cos(np.outer(flat[start:stop], centered)) @ weights
    return answer.reshape(values.shape)


def dephasing_error(frequency: float, quadrature_order: int = 256) -> float:
    """Numerically replay ``hat psi(xi)=exp(i xi/2) Phi(xi)``.

    This is a diagnostic of the quadrature implementation, not a proof of the
    elementary identity.
    """

    centered, weights = centered_bump_quadrature(quadrature_order)
    direct = np.sum(weights * np.exp(1j * frequency * (0.5 + centered)))
    amplitude = np.sum(weights * np.cos(frequency * centered))
    return float(abs(direct - np.exp(0.5j * frequency) * amplitude))


def primes_up_to(limit: int) -> np.ndarray:
    if limit < 2:
        return np.empty(0, dtype=np.int64)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = False
    return np.flatnonzero(sieve).astype(np.int64)


def shell_values(
    center: float,
    width: float,
    kind: Literal["prime_powers", "integers"] = "prime_powers",
) -> np.ndarray:
    """Return either the actual prime-power shell or the full integer shell."""

    lower = math.ceil(center * math.exp(-width))
    upper = math.floor(center * math.exp(width))
    if lower > upper:
        return np.empty(0, dtype=np.int64)
    if kind == "integers":
        return np.arange(lower, upper + 1, dtype=np.int64)
    if kind != "prime_powers":
        raise ValueError("unknown shell kind")
    values: set[int] = set()
    for raw_prime in primes_up_to(upper):
        prime = int(raw_prime)
        power = prime
        while power <= upper:
            if power >= lower:
                values.add(power)
            if power > upper // prime:
                break
            power *= prime
    return np.asarray(sorted(values), dtype=np.int64)


@dataclass(frozen=True)
class FourCycleCore:
    q: int
    aperture: float
    width: float
    cutoff: float
    values: np.ndarray
    rows: np.ndarray
    columns: np.ndarray
    colors: np.ndarray
    weights: np.ndarray

    @property
    def dimension(self) -> int:
        return int(self.values.size)

    @property
    def geometric_degree_cap(self) -> float:
        # The report's D=U*q^2/B, with harmless fixed shell constants omitted.
        bandwidth = (self.q / 2.0) ** self.aperture
        return self.cutoff * self.q * self.q / bandwidth

    @property
    def weighted_color_degrees(self) -> np.ndarray:
        return np.bincount(
            self.colors,
            weights=self.weights * self.weights,
            minlength=self.dimension,
        )


def build_four_cycle_core(
    q: int,
    *,
    aperture: float = FULL_APERTURE,
    width: float = PROJECT_WIDTH,
    cutoff: float = 12.0,
    kind: Literal["prime_powers", "integers"] = "prime_powers",
    quadrature_order: int = 128,
) -> FourCycleCore:
    """Build the dephased, smoothly weighted truncated carry core.

    Pair uniqueness holds at the intended asymptotic scale.  This routine
    nevertheless checks the nearest integer only and then checks the exact
    logarithmic cutoff.  It is intended for the prime values used by the
    diagnostic report (up to a few hundred thousand), where double precision
    identifies the nearest integer unambiguously.
    """

    if q <= 2 or q % 2 == 0:
        raise ValueError("q must be an odd integer greater than two")
    if not 1.0 < aperture < 2.0:
        raise ValueError("aperture must lie in (1,2)")
    if width <= 0.0 or cutoff <= 0.0:
        raise ValueError("width and cutoff must be positive")
    center = q / 2.0
    bandwidth = center**aperture
    values = shell_values(center, width, kind)
    dimension = int(values.size)
    if dimension == 0:
        raise ValueError("empty shell")
    lower = int(values[0])
    upper = int(values[-1])
    lookup = np.full(upper + 1, -1, dtype=np.int32)
    lookup[values] = np.arange(dimension, dtype=np.int32)
    numerator = q**3

    row_list: list[int] = []
    column_list: list[int] = []
    color_list: list[int] = []
    frequency_list: list[float] = []

    values_float = values.astype(float)
    for row, raw_a in enumerate(values):
        a = int(raw_a)
        # Safe in the finite range of the diagnostic.  The exact cutoff below
        # is computed from the integer residual with log1p.
        candidates = np.rint(numerator / (8.0 * a * values_float)).astype(np.int64)
        inside = (candidates >= lower) & (candidates <= upper)
        color_ids = np.full(dimension, -1, dtype=np.int32)
        color_ids[inside] = lookup[candidates[inside]]
        residuals = 8 * a * values * candidates - numerator
        frequencies = bandwidth * np.log1p(residuals.astype(float) / numerator)
        columns = np.flatnonzero((color_ids >= 0) & (np.abs(frequencies) <= cutoff))
        row_list.extend([row] * len(columns))
        column_list.extend(columns.tolist())
        color_list.extend(color_ids[columns].tolist())
        frequency_list.extend(frequencies[columns].tolist())

    frequencies_array = np.asarray(frequency_list, dtype=float)
    weights = centered_fourier_amplitude(
        frequencies_array, quadrature_order=quadrature_order
    )
    return FourCycleCore(
        q=q,
        aperture=aperture,
        width=width,
        cutoff=cutoff,
        values=values,
        rows=np.asarray(row_list, dtype=np.int32),
        columns=np.asarray(column_list, dtype=np.int32),
        colors=np.asarray(color_list, dtype=np.int32),
        weights=weights,
    )


def rectangle_value_and_gradient(
    core: FourCycleCore,
    colors_vector: Sequence[float] | np.ndarray,
    *,
    with_gradient: bool = True,
) -> tuple[float, float, np.ndarray | None]:
    """Compute ``Q_nd``, the full fourth trace, and its real gradient.

    The identity used is

    ``Q_nd=tr((A^T A)^2)-sum(row_mass^2)-sum(column_mass^2)+sum(A_e^4)``.

    For the positive inner core and a nonnegative color vector this is also
    the unsigned nondegenerate rectangle mass.
    """

    vector = np.asarray(colors_vector, dtype=float)
    if vector.shape != (core.dimension,):
        raise ValueError("color vector has the wrong dimension")
    data = core.weights * vector[core.colors]
    matrix = coo_matrix(
        (data, (core.rows, core.columns)),
        shape=(core.dimension, core.dimension),
    ).tocsr()
    squares = matrix.power(2)
    row_mass = np.asarray(squares.sum(axis=1)).ravel()
    column_mass = np.asarray(squares.sum(axis=0)).ravel()
    gram = matrix.T @ matrix
    fourth_trace = float(gram.multiply(gram).sum())
    value = float(
        fourth_trace
        - np.dot(row_mass, row_mass)
        - np.dot(column_mass, column_mass)
        + np.sum(data**4)
    )
    if not with_gradient:
        return value, fourth_trace, None

    cubic = (matrix @ gram).tocsr()
    cubic_on_edges = np.asarray(cubic[core.rows, core.columns]).ravel()
    entry_gradient = 4.0 * (
        cubic_on_edges
        - data * row_mass[core.rows]
        - data * column_mass[core.columns]
        + data**3
    )
    gradient = np.bincount(
        core.colors,
        weights=core.weights * entry_gradient,
        minlength=core.dimension,
    )
    return value, fourth_trace, gradient


@dataclass(frozen=True)
class FourCycleDiagnostic:
    q: int
    nodes: int
    entries: int
    geometric_degree_cap: float
    maximum_weighted_color_degree: float
    best_value: float
    best_fourth_trace: float
    active_colors: int


@dataclass(frozen=True)
class PrimeRectangleFixture:
    """An exact all-prime nondegenerate carry rectangle."""

    q: int
    rows: tuple[int, int]
    columns: tuple[int, int]
    colors: tuple[tuple[int, int], tuple[int, int]]
    residuals: tuple[int, int, int, int]
    frequencies: tuple[float, float, float, float]
    color_determinant: int


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, math.isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def exact_prime_rectangle_fixture(
    aperture: float = FULL_APERTURE,
) -> PrimeRectangleFixture:
    """Return a prime rectangle at ``q=50021`` with determinant six.

    Every displayed integer is prime and lies in the project shell of width
    ``0.2``.  All four normalized logarithmic residuals have absolute value
    below one.  Thus a proof of the four-cycle estimate cannot use a lower
    bound ``|Delta| >= q**eta`` for individual rectangles.
    """

    q = 50_021
    rows = (21_277, 22_741)
    columns = (28_277, 28_793)
    colors = ((26_003, 25_537), (24_329, 23_893))
    triples = (
        (rows[0], columns[0], colors[0][0]),
        (rows[0], columns[1], colors[0][1]),
        (rows[1], columns[0], colors[1][0]),
        (rows[1], columns[1], colors[1][1]),
    )
    numerator = q**3
    bandwidth = (q / 2.0) ** aperture
    residuals = tuple(8 * a * b * c - numerator for a, b, c in triples)
    frequencies = tuple(
        bandwidth * math.log1p(residual / numerator) for residual in residuals
    )
    determinant = colors[0][0] * colors[1][1] - colors[0][1] * colors[1][0]
    return PrimeRectangleFixture(
        q=q,
        rows=rows,
        columns=columns,
        colors=colors,
        residuals=residuals,
        frequencies=frequencies,
        color_determinant=determinant,
    )


@dataclass(frozen=True)
class ColorBlockDiagnostic:
    coordinate: str
    coherence_length: int
    support_size: int
    left_color: int
    span: int
    value: float


def contiguous_color_block_search(
    core: FourCycleCore,
    *,
    coordinate: Literal["value", "index"] = "value",
    span_multipliers: Sequence[int] = (1, 2, 4, 8),
    maximum_starts: int = 200,
) -> ColorBlockDiagnostic:
    """Sample nonnegative vectors supported on local color blocks.

    ``coordinate='value'`` uses integer intervals of length ``m*sqrt(R)``.
    ``coordinate='index'`` uses that many consecutive prime-power nodes.
    The search is sampled when there are more than ``maximum_starts`` nodes;
    its output is only a finite lower-bound diagnostic.
    """

    if coordinate not in {"value", "index"}:
        raise ValueError("coordinate must be 'value' or 'index'")
    if maximum_starts <= 0 or any(multiplier <= 0 for multiplier in span_multipliers):
        raise ValueError("invalid scan parameters")
    # Remove the deliberately chosen Fourier cutoff U from D=UR.
    base_degree = core.geometric_degree_cap / core.cutoff
    coherence = max(1, int(round(math.sqrt(base_degree))))
    stride = max(1, math.ceil(core.dimension / maximum_starts))
    best: ColorBlockDiagnostic | None = None
    for multiplier in span_multipliers:
        span = multiplier * coherence
        for start in range(0, core.dimension, stride):
            if coordinate == "value":
                stop = int(
                    np.searchsorted(
                        core.values,
                        int(core.values[start]) + span,
                        side="right",
                    )
                )
            else:
                stop = min(core.dimension, start + span)
            support = stop - start
            if support <= 0:
                continue
            vector = np.zeros(core.dimension, dtype=float)
            vector[start:stop] = 1.0 / math.sqrt(support)
            value, _, _ = rectangle_value_and_gradient(
                core, vector, with_gradient=False
            )
            candidate = ColorBlockDiagnostic(
                coordinate=coordinate,
                coherence_length=coherence,
                support_size=support,
                left_color=int(core.values[start]),
                span=span,
                value=value,
            )
            if best is None or candidate.value > best.value:
                best = candidate
    if best is None:
        raise ValueError("block scan produced no supports")
    return best


def projected_four_cycle_search(
    core: FourCycleCore,
    *,
    iterations: int = 30,
) -> FourCycleDiagnostic:
    """Deterministic multistart projected ascent on nonnegative unit vectors.

    The returned value is a *lower bound* for the finite maximum.  It is not a
    certified optimizer and has no asymptotic force.
    """

    if iterations < 0:
        raise ValueError("iterations must be nonnegative")
    dimension = core.dimension
    degrees = core.weighted_color_degrees
    order = np.argsort(-degrees)
    cap = core.geometric_degree_cap
    support_sizes = {
        dimension,
        min(dimension, max(1, int(math.sqrt(cap)))),
        min(dimension, max(1, int(cap))),
    }
    starts: list[np.ndarray] = []
    for support in sorted(support_sizes):
        vector = np.zeros(dimension, dtype=float)
        vector[order[:support]] = 1.0 / math.sqrt(support)
        starts.append(vector)

    best_value = -math.inf
    best_trace = 0.0
    best_vector = starts[0]
    for initial in starts:
        vector = initial.copy()
        value, fourth_trace, gradient_raw = rectangle_value_and_gradient(core, vector)
        assert gradient_raw is not None
        gradient = gradient_raw
        for _ in range(iterations):
            projected = gradient - vector * float(np.dot(vector, gradient))
            norm = float(np.linalg.norm(projected))
            if norm < 1.0e-11:
                break
            step = 0.5 / max(1.0, norm)
            accepted = False
            slope = float(np.dot(projected, projected))
            for _ in range(18):
                candidate = np.maximum(vector + step * projected, 0.0)
                candidate_norm = float(np.linalg.norm(candidate))
                if candidate_norm == 0.0:
                    step *= 0.5
                    continue
                candidate /= candidate_norm
                candidate_value, candidate_trace, candidate_gradient = (
                    rectangle_value_and_gradient(core, candidate)
                )
                assert candidate_gradient is not None
                if candidate_value >= value + 1.0e-7 * step * slope:
                    vector = candidate
                    value = candidate_value
                    fourth_trace = candidate_trace
                    gradient = candidate_gradient
                    accepted = True
                    break
                step *= 0.5
            if not accepted:
                break
        if value > best_value:
            best_value = value
            best_trace = fourth_trace
            best_vector = vector

    return FourCycleDiagnostic(
        q=core.q,
        nodes=dimension,
        entries=int(core.rows.size),
        geometric_degree_cap=cap,
        maximum_weighted_color_degree=float(np.max(degrees, initial=0.0)),
        best_value=float(best_value),
        best_fourth_trace=float(best_trace),
        active_colors=int(np.count_nonzero(best_vector > 1.0e-4)),
    )
