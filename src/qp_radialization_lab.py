"""Finite-scale diagnostics for the corrected high-band radialization gate.

This module compares three quantities on actual prime-power logarithmic nodes:

* the high-subband positive-antipode radius on ``[N**.5, N**A']``;
* the full-QP positive-antipode radius on ``[Y**.01, Y**(50/33)]``;
* mass-normalized negative prime-interval excursions
  ``-N**-1 sum_{p in I} cos(t log(p/Y))``.

The semi-infinite antipode problem is approached by exchange.  A feasible
finite-pool antipode is a lower bound for the continuum radius.  A dual
polynomial, checked on a uniform validation grid and enlarged by its exact
derivative Lipschitz constant, is an upper bound up to floating-point LP
residuals.  The latter qualification is reported explicitly: this is a
diagnostic lab, not interval-arithmetic certification.

The directional scan likewise reports a sampled/refined lower value and an
analytic derivative-grid upper guard.  Singleton, long-interval, and whole-
shell normalizations are kept separate; probability-normalized singleton
depth is deliberately not used.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math
from typing import Iterable

import numpy as np
from scipy.optimize import linprog, minimize_scalar


def primes_up_to(limit: int) -> np.ndarray:
    """Return all primes at most ``limit`` by an elementary sieve."""

    if limit < 2:
        return np.empty(0, dtype=int)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    return np.flatnonzero(sieve)


def prime_powers_in_shell(Y: float, width: float) -> tuple[np.ndarray, np.ndarray]:
    """Return prime powers and their absolute nonzero log nodes."""

    lower = Y * math.exp(-width)
    upper = Y * math.exp(width)
    primes = primes_up_to(math.ceil(upper))
    values: list[int] = []
    for prime_raw in primes:
        prime = int(prime_raw)
        value = prime
        while value <= upper:
            if value >= lower:
                values.append(value)
            if value > upper / prime:
                break
            value *= prime
    values_array = np.array(sorted(set(values)), dtype=int)
    nodes = np.abs(np.log(values_array.astype(float) / Y))
    if np.any(nodes == 0.0):
        raise ValueError("the shell center must not be a prime power")
    return values_array, nodes


def primes_in_shell(Y: float, width: float) -> tuple[np.ndarray, np.ndarray]:
    """Return shell primes and signed centered logarithms."""

    lower = Y * math.exp(-width)
    upper = Y * math.exp(width)
    primes = primes_up_to(math.ceil(upper))
    mask = (primes >= lower) & (primes <= upper)
    selected = primes[mask].astype(int)
    return selected, np.log(selected.astype(float) / Y)


def cosine_atoms(nodes: np.ndarray, times: np.ndarray) -> np.ndarray:
    """Coordinate-by-time cosine atom matrix."""

    return np.cos(np.outer(np.asarray(nodes, dtype=float), np.asarray(times, dtype=float)))


def uniform_grid(left: float, right: float, max_node: float, phase_step: float) -> np.ndarray:
    """Grid whose fastest-node phase increment is at most ``phase_step``."""

    if not right > left or max_node <= 0.0 or phase_step <= 0.0:
        raise ValueError("invalid grid parameters")
    count = max(2, int(math.ceil((right - left) * max_node / phase_step)))
    return np.linspace(left, right, count + 1)


@dataclass(frozen=True)
class FiniteAntipodeSolution:
    depth: float
    weights: np.ndarray
    equality_residual: float
    success: bool


def solve_finite_antipode(nodes: np.ndarray, times: np.ndarray) -> FiniteAntipodeSolution:
    """Maximize antipode depth over a finite pool of heights."""

    atoms = cosine_atoms(nodes, times)
    coordinates, count = atoms.shape
    objective = np.zeros(count + 1)
    objective[-1] = -1.0
    equality = np.zeros((coordinates + 1, count + 1))
    equality[:coordinates, :count] = atoms
    equality[:coordinates, -1] = 1.0
    equality[-1, :count] = 1.0
    rhs = np.zeros(coordinates + 1)
    rhs[-1] = 1.0
    result = linprog(
        objective,
        A_eq=equality,
        b_eq=rhs,
        bounds=[(0.0, None)] * count + [(0.0, 1.0)],
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        return FiniteAntipodeSolution(0.0, np.zeros(count), math.inf, False)
    residual = float(np.max(np.abs(equality @ result.x - rhs)))
    return FiniteAntipodeSolution(float(result.x[-1]), result.x[:-1], residual, True)


@dataclass(frozen=True)
class FiniteDualSolution:
    level: float
    coefficients: np.ndarray
    equality_residual: float
    inequality_violation: float
    success: bool


def solve_finite_antipode_dual(nodes: np.ndarray, times: np.ndarray) -> FiniteDualSolution:
    """Solve ``inf_(sum y=-1) max_pool y.a(t)``."""

    atoms = cosine_atoms(nodes, times)
    coordinates, count = atoms.shape
    objective = np.r_[np.zeros(coordinates), 1.0]
    inequalities = np.c_[atoms.T, -np.ones(count)]
    equality = np.zeros((1, coordinates + 1))
    equality[0, :coordinates] = 1.0
    result = linprog(
        objective,
        A_ub=inequalities,
        b_ub=np.zeros(count),
        A_eq=equality,
        b_eq=np.array([-1.0]),
        bounds=[(None, None)] * coordinates + [(None, None)],
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        return FiniteDualSolution(math.inf, np.zeros(coordinates), math.inf, math.inf, False)
    y = result.x[:-1]
    level = float(result.x[-1])
    equality_residual = abs(float(np.sum(y)) + 1.0)
    inequality_violation = max(0.0, float(np.max(atoms.T @ y - level)))
    return FiniteDualSolution(level, y, equality_residual, inequality_violation, True)


def local_maxima_indices(values: np.ndarray) -> np.ndarray:
    """Indices of grid local maxima, including an endpoint when appropriate."""

    values = np.asarray(values, dtype=float)
    if len(values) < 2:
        return np.arange(len(values))
    middle = np.flatnonzero((values[1:-1] >= values[:-2]) & (values[1:-1] >= values[2:])) + 1
    endpoints: list[int] = []
    if values[0] >= values[1]:
        endpoints.append(0)
    if values[-1] >= values[-2]:
        endpoints.append(len(values) - 1)
    return np.array(endpoints + list(middle), dtype=int)


def refine_dual_maximum(
    nodes: np.ndarray,
    coefficients: np.ndarray,
    grid: np.ndarray,
    values: np.ndarray,
    candidates: int = 32,
) -> tuple[float, float]:
    """Refine the largest sampled local maxima for one dual polynomial."""

    maxima = local_maxima_indices(values)
    if len(maxima) == 0:
        index = int(np.argmax(values))
        return float(values[index]), float(grid[index])
    chosen = maxima[np.argsort(values[maxima])[-candidates:]]
    best_value = -math.inf
    best_time = float(grid[int(np.argmax(values))])

    def value_at(time: float) -> float:
        return float(np.dot(coefficients, np.cos(nodes * time)))

    for index in chosen:
        left = float(grid[max(0, index - 1)])
        right = float(grid[min(len(grid) - 1, index + 1)])
        if right == left:
            candidate_time = left
            candidate_value = value_at(left)
        else:
            optimized = minimize_scalar(
                lambda time: -value_at(float(time)),
                bounds=(left, right),
                method="bounded",
                options={"xatol": 1e-11},
            )
            candidate_time = float(optimized.x)
            candidate_value = -float(optimized.fun)
        if candidate_value > best_value:
            best_value = candidate_value
            best_time = candidate_time
    return best_value, best_time


@dataclass(frozen=True)
class AntipodeBracket:
    lower: float
    upper_guard: float
    finite_dual_level: float
    validation_maximum: float
    validation_argmax: float
    dual_lipschitz: float
    dual_curvature: float
    validation_step: float
    pool_size: int
    support_size: int
    support_time_min: float | None
    support_time_max: float | None
    support_times: tuple[float, ...]
    support_weights: tuple[float, ...]
    largest_support_times: tuple[float, ...]
    largest_support_weights: tuple[float, ...]
    primal_residual: float
    dual_equality_residual: float
    dual_inequality_violation: float
    exchange_iterations: int
    floating_point_only: bool = True


def antipode_exchange(
    nodes: np.ndarray,
    left: float,
    right: float,
    *,
    initial_factor: int = 8,
    validation_phase_step: float = 0.08,
    max_iterations: int = 8,
    relative_gap: float = 2e-3,
    seed_times: np.ndarray | None = None,
) -> AntipodeBracket:
    """Exchange bracket for the continuum positive-antipode radius."""

    nodes = np.asarray(nodes, dtype=float)
    maximum_node = float(np.max(nodes))
    initial_count = max(64, initial_factor * (len(nodes) + 1))
    pool = np.linspace(left, right, initial_count)
    if seed_times is not None:
        seeds = np.asarray(seed_times, dtype=float)
        seeds = seeds[(seeds >= left) & (seeds <= right)]
        pool = np.unique(np.r_[pool, seeds])
    validation = uniform_grid(left, right, maximum_node, validation_phase_step)
    validation_step = float(validation[1] - validation[0])
    primal = FiniteAntipodeSolution(0.0, np.zeros(len(pool)), math.inf, False)
    dual = FiniteDualSolution(math.inf, np.zeros(len(nodes)), math.inf, math.inf, False)
    refined_max = math.inf
    argmax = left
    upper = math.inf

    for iteration in range(1, max_iterations + 1):
        dual = solve_finite_antipode_dual(nodes, pool)
        primal = solve_finite_antipode(nodes, pool)
        if not dual.success or not primal.success:
            break
        values = cosine_atoms(nodes, validation).T @ dual.coefficients
        refined_max, argmax = refine_dual_maximum(nodes, dual.coefficients, validation, values)
        lipschitz = float(np.dot(np.abs(dual.coefficients), nodes))
        curvature = float(np.dot(np.abs(dual.coefficients), nodes * nodes))
        first_order_guard = float(np.max(values)) + 0.5 * lipschitz * validation_step
        # On each grid cell, interpolation between its endpoint values and
        # ``|f''|<=curvature`` gives a curvature remainder at most C*h^2/8.
        second_order_guard = float(np.max(values)) + curvature * validation_step**2 / 8.0
        grid_guard = min(first_order_guard, second_order_guard)
        upper = max(refined_max, grid_guard)
        gap = upper - primal.depth
        scale = max(abs(primal.depth), 1e-12)
        if gap <= relative_gap * scale + 1e-10:
            break
        # Add the worst refined point and the strongest sampled maxima.
        maxima = local_maxima_indices(values)
        extra = validation[maxima[np.argsort(values[maxima])[-min(2 * len(nodes), len(maxima)):]]]
        pool = np.unique(np.r_[pool, argmax, extra])

    lipschitz = float(np.dot(np.abs(dual.coefficients), nodes)) if dual.success else math.inf
    curvature = (
        float(np.dot(np.abs(dual.coefficients), nodes * nodes)) if dual.success else math.inf
    )
    support_size = int(np.sum(primal.weights > 1e-8)) if primal.success else 0
    support_indices = np.flatnonzero(primal.weights > 1e-8) if primal.success else np.array([])
    if len(support_indices):
        ordered = support_indices[np.argsort(primal.weights[support_indices])[-8:]][::-1]
        support_time_min: float | None = float(np.min(pool[support_indices]))
        support_time_max: float | None = float(np.max(pool[support_indices]))
        support_times = tuple(float(pool[index]) for index in support_indices)
        support_weights = tuple(float(primal.weights[index]) for index in support_indices)
        largest_support_times = tuple(float(pool[index]) for index in ordered)
        largest_support_weights = tuple(float(primal.weights[index]) for index in ordered)
    else:
        support_time_min = None
        support_time_max = None
        support_times = ()
        support_weights = ()
        largest_support_times = ()
        largest_support_weights = ()
    return AntipodeBracket(
        lower=float(primal.depth),
        upper_guard=float(upper),
        finite_dual_level=float(dual.level),
        validation_maximum=float(refined_max),
        validation_argmax=float(argmax),
        dual_lipschitz=lipschitz,
        dual_curvature=curvature,
        validation_step=validation_step,
        pool_size=len(pool),
        support_size=support_size,
        support_time_min=support_time_min,
        support_time_max=support_time_max,
        support_times=support_times,
        support_weights=support_weights,
        largest_support_times=largest_support_times,
        largest_support_weights=largest_support_weights,
        primal_residual=float(primal.equality_residual),
        dual_equality_residual=float(dual.equality_residual),
        dual_inequality_violation=float(dual.inequality_violation),
        exchange_iterations=iteration,
    )


def maximum_subarray(values: np.ndarray, minimum_length: int = 1) -> tuple[float, int, int]:
    """Maximum contiguous sum with at least ``minimum_length`` entries."""

    values = np.asarray(values, dtype=float)
    count = len(values)
    if minimum_length < 1 or minimum_length > count:
        return -math.inf, -1, -1
    prefix = np.r_[0.0, np.cumsum(values)]
    best = -math.inf
    best_left = 0
    best_right = minimum_length
    minimum_prefix = prefix[0]
    minimum_index = 0
    for right in range(minimum_length, count + 1):
        allowed = right - minimum_length
        if prefix[allowed] < minimum_prefix:
            minimum_prefix = float(prefix[allowed])
            minimum_index = allowed
        candidate = float(prefix[right] - minimum_prefix)
        if candidate > best:
            best = candidate
            best_left = minimum_index
            best_right = right
    return best, best_left, best_right


@dataclass(frozen=True)
class DirectionalValue:
    lower: float
    upper_guard: float
    time: float
    left_prime: int | None
    right_prime: int | None
    prime_count: int
    minimum_count: int
    lipschitz: float
    curvature: float
    grid_step: float
    available: bool


@dataclass(frozen=True)
class FixedCellFamily:
    """Maximum over one predetermined logarithmic partition of the shell."""

    lower: float
    upper_guard: float
    winning_cell: int
    cell_count: int
    nonempty_cell_count: int
    requested_log_width: float
    actual_log_width: float
    log_boundaries: tuple[float, ...]
    winning_direction: DirectionalValue


def refine_interval_value(
    logs: np.ndarray,
    normalization: float,
    grid: np.ndarray,
    index: int,
    left_index: int,
    right_index: int,
) -> tuple[float, float]:
    """Refine one fixed prime interval near a sampled maximum."""

    selected = logs[left_index:right_index]
    left = float(grid[max(0, index - 1)])
    right = float(grid[min(len(grid) - 1, index + 1)])

    def objective(time: float) -> float:
        return float(np.sum(np.cos(selected * time)) / normalization)

    optimized = minimize_scalar(
        objective,
        bounds=(left, right),
        method="bounded",
        options={"xatol": 1e-11},
    )
    return -float(optimized.fun), float(optimized.x)


def directional_interval_scan(
    primes: np.ndarray,
    logs: np.ndarray,
    normalization: float,
    left: float,
    right: float,
    *,
    minimum_count: int,
    phase_step: float = 0.06,
) -> DirectionalValue:
    """Scan the mass-normalized negative excursion over prime intervals."""

    if minimum_count > len(primes):
        return DirectionalValue(
            lower=0.0,
            upper_guard=0.0,
            time=left,
            left_prime=None,
            right_prime=None,
            prime_count=0,
            minimum_count=minimum_count,
            lipschitz=0.0,
            curvature=0.0,
            grid_step=0.0,
            available=False,
        )
    maximum_node = float(np.max(np.abs(logs)))
    grid = uniform_grid(left, right, maximum_node, phase_step)
    step = float(grid[1] - grid[0])
    best = -math.inf
    best_grid_index = 0
    best_left = 0
    best_right = minimum_count
    chunk = 4096
    for start in range(0, len(grid), chunk):
        times = grid[start : start + chunk]
        values = -np.cos(np.outer(times, logs))
        for local_index, row in enumerate(values):
            candidate, interval_left, interval_right = maximum_subarray(row, minimum_count)
            candidate /= normalization
            if candidate > best:
                best = candidate
                best_grid_index = start + local_index
                best_left = interval_left
                best_right = interval_right
    refined, refined_time = refine_interval_value(
        logs,
        normalization,
        grid,
        best_grid_index,
        best_left,
        best_right,
    )
    lower_value = max(best, refined)
    # Every admissible interval is a subset of the full shell, so this one
    # Lipschitz constant guards the maximum over all switching intervals.
    lipschitz = float(np.sum(np.abs(logs)) / normalization)
    curvature = float(np.sum(logs * logs) / normalization)
    first_order_guard = best + 0.5 * lipschitz * step
    second_order_guard = best + curvature * step * step / 8.0
    upper = max(lower_value, min(first_order_guard, second_order_guard))
    return DirectionalValue(
        lower=float(lower_value),
        upper_guard=float(upper),
        time=float(refined_time),
        left_prime=int(primes[best_left]),
        right_prime=int(primes[best_right - 1]),
        prime_count=best_right - best_left,
        minimum_count=minimum_count,
        lipschitz=lipschitz,
        curvature=curvature,
        grid_step=step,
        available=True,
    )


def full_shell_scan(
    primes: np.ndarray,
    logs: np.ndarray,
    normalization: float,
    left: float,
    right: float,
    *,
    phase_step: float = 0.06,
) -> DirectionalValue:
    """Mass-normalized excursion for the entire prime shell."""

    maximum_node = float(np.max(np.abs(logs)))
    grid = uniform_grid(left, right, maximum_node, phase_step)
    step = float(grid[1] - grid[0])
    values = np.empty(len(grid))
    chunk = 8192
    for start in range(0, len(grid), chunk):
        times = grid[start : start + chunk]
        values[start : start + len(times)] = -np.sum(
            np.cos(np.outer(times, logs)), axis=1
        ) / normalization
    index = int(np.argmax(values))
    refined, refined_time = refine_interval_value(logs, normalization, grid, index, 0, len(logs))
    lower_value = max(float(values[index]), refined)
    lipschitz = float(np.sum(np.abs(logs)) / normalization)
    curvature = float(np.sum(logs * logs) / normalization)
    first_order_guard = float(values[index]) + 0.5 * lipschitz * step
    second_order_guard = float(values[index]) + curvature * step * step / 8.0
    upper = max(lower_value, min(first_order_guard, second_order_guard))
    return DirectionalValue(
        lower=lower_value,
        upper_guard=upper,
        time=refined_time,
        left_prime=int(primes[0]),
        right_prime=int(primes[-1]),
        prime_count=len(primes),
        minimum_count=len(primes),
        lipschitz=lipschitz,
        curvature=curvature,
        grid_step=step,
        available=True,
    )


def fixed_log_partition_scan(
    primes: np.ndarray,
    logs: np.ndarray,
    normalization: float,
    left: float,
    right: float,
    *,
    shell_width: float,
    cell_log_width: float | None = None,
    phase_step: float = 0.06,
) -> FixedCellFamily:
    """Scan fixed shell cells of logarithmic width at most ``cell_log_width``.

    These cells are an optional diagnostic for the fixed logarithmic pieces
    occurring in the Turan phase bridge.  They are not a replacement for the
    exact threshold class ``#I >= N**(1-d)``: the original Turan interval may
    itself be short, and its partition need not align with this shell grid.
    """

    primes = np.asarray(primes)
    logs = np.asarray(logs, dtype=float)
    if len(primes) != len(logs) or len(primes) == 0:
        raise ValueError("fixed cell scan requires a nonempty prime shell")
    requested = shell_width / 2.0 if cell_log_width is None else cell_log_width
    if shell_width <= 0.0 or requested <= 0.0:
        raise ValueError("logarithmic widths must be positive")
    cell_count = max(1, int(math.ceil(2.0 * shell_width / requested)))
    boundaries = np.linspace(-shell_width, shell_width, cell_count + 1)
    directions: list[tuple[int, DirectionalValue]] = []
    for cell in range(cell_count):
        if cell + 1 == cell_count:
            mask = (logs >= boundaries[cell]) & (logs <= boundaries[cell + 1])
        else:
            mask = (logs >= boundaries[cell]) & (logs < boundaries[cell + 1])
        if not np.any(mask):
            continue
        direction = full_shell_scan(
            primes[mask],
            logs[mask],
            normalization,
            left,
            right,
            phase_step=phase_step,
        )
        directions.append((cell, direction))
    if not directions:
        raise ValueError("fixed logarithmic partition contains no shell primes")
    winning_cell, winner = max(directions, key=lambda item: item[1].lower)
    return FixedCellFamily(
        lower=max(direction.lower for _, direction in directions),
        upper_guard=max(direction.upper_guard for _, direction in directions),
        winning_cell=winning_cell,
        cell_count=cell_count,
        nonempty_cell_count=len(directions),
        requested_log_width=requested,
        actual_log_width=2.0 * shell_width / cell_count,
        log_boundaries=tuple(float(value) for value in boundaries),
        winning_direction=winner,
    )


def singleton_resonances(logs: np.ndarray, left: float, right: float) -> int:
    """Count prime nodes having an odd half-period inside the high band."""

    count = 0
    for node in np.abs(logs):
        lower_index = math.ceil((left * node / math.pi - 1.0) / 2.0)
        upper_index = math.floor((right * node / math.pi - 1.0) / 2.0)
        lower_index = max(lower_index, 0)
        if upper_index >= lower_index:
            count += 1
    return count


def effective_lambda(value: float, radius: float) -> float | None:
    """Return ``lambda`` in ``value=radius**lambda`` when meaningful."""

    if not 0.0 < value < 1.0 or not 0.0 < radius < 1.0:
        return None
    return math.log(value) / math.log(radius)


def ratio_to_power(value: float, radius: float, power: float) -> float | None:
    if value < 0.0 or radius <= 0.0 or power <= 0.0:
        return None
    return value / (radius**power)


def run_instance(
    N: int,
    *,
    center_offset: float = 0.5,
    width: float = 0.2,
    aperture: float = 1.5,
    full_lower_exponent: float = 0.01,
    full_aperture: float = 50.0 / 33.0,
    long_d: float = 0.019,
    antipode_phase_step: float = 0.08,
    directional_phase_step: float = 0.06,
    max_exchange_iterations: int = 8,
) -> dict:
    """Run one corrected ``E`` versus ``R`` radialization instance."""

    Y = N + center_offset
    if abs(2.0 * Y - round(2.0 * Y)) > 1e-12 or abs(Y - round(Y)) < 1e-12:
        raise ValueError("Y must be a nonintegral half-integer")
    powers, nodes = prime_powers_in_shell(Y, width)
    primes, prime_logs = primes_in_shell(Y, width)
    left = N**0.5
    right = N**aperture
    antipode = antipode_exchange(
        nodes,
        left,
        right,
        validation_phase_step=antipode_phase_step,
        max_iterations=max_exchange_iterations,
    )
    full_left = Y**full_lower_exponent
    full_right = Y**full_aperture
    full_antipode = antipode_exchange(
        nodes,
        full_left,
        full_right,
        validation_phase_step=antipode_phase_step,
        max_iterations=max_exchange_iterations,
        # The high band is contained in the full QP band.  Seeding with the
        # high-band finite pool prevents a coarse full-band initialization
        # from spuriously reporting finite-LP infeasibility.
        seed_times=np.r_[
            np.linspace(left, right, max(64, 8 * (len(nodes) + 1))),
            np.asarray(antipode.support_times),
        ],
    )
    any_interval = directional_interval_scan(
        primes,
        prime_logs,
        float(N),
        left,
        right,
        minimum_count=1,
        phase_step=directional_phase_step,
    )
    long_minimum = max(1, int(math.ceil(N ** (1.0 - long_d))))
    long_interval = directional_interval_scan(
        primes,
        prime_logs,
        float(N),
        left,
        right,
        minimum_count=long_minimum,
        phase_step=directional_phase_step,
    )
    shell = full_shell_scan(
        primes,
        prime_logs,
        float(N),
        left,
        right,
        phase_step=directional_phase_step,
    )
    fixed_cells = fixed_log_partition_scan(
        primes,
        prime_logs,
        float(N),
        left,
        right,
        shell_width=width,
        cell_log_width=width / 2.0,
        phase_step=directional_phase_step,
    )
    singleton_count = singleton_resonances(prime_logs, left, right)
    radius_mid = 0.5 * (antipode.lower + antipode.upper_guard)
    full_radius_mid = 0.5 * (full_antipode.lower + full_antipode.upper_guard)
    thresholds: dict[str, dict] = {}
    threshold_counts = sorted(
        set(
            [
                1,
                long_minimum,
                max(1, len(primes) // 4),
                max(1, len(primes) // 2),
                len(primes),
            ]
        )
    )
    for minimum in threshold_counts:
        if minimum == 1:
            value = any_interval
        elif minimum == long_minimum:
            value = long_interval
        elif minimum == len(primes):
            value = shell
        else:
            value = directional_interval_scan(
                primes,
                prime_logs,
                float(N),
                left,
                right,
                minimum_count=minimum,
                phase_step=directional_phase_step,
            )
        available = value.available
        thresholds[str(minimum)] = {
            "fraction_of_shell_primes": minimum / max(len(primes), 1),
            "direction": asdict(value),
            "effective_lambda_at_radius_mid": (
                effective_lambda(value.lower, radius_mid) if available else None
            ),
            "effective_lambda_at_full_radius_mid": (
                effective_lambda(value.lower, full_radius_mid) if available else None
            ),
            "E_over_R": (
                ratio_to_power(value.lower, radius_mid, 1.0) if available else None
            ),
            "E_over_R_full": (
                ratio_to_power(value.lower, full_radius_mid, 1.0) if available else None
            ),
            "E_over_sqrt_R": (
                ratio_to_power(value.lower, radius_mid, 0.5) if available else None
            ),
        }

    return {
        "N": N,
        "Y": Y,
        "width": width,
        "aperture": aperture,
        "full_lower_exponent": full_lower_exponent,
        "full_aperture": full_aperture,
        "band": [left, right],
        "high_band": [left, right],
        "full_band": [full_left, full_right],
        "prime_power_nodes": len(nodes),
        "prime_nodes": len(primes),
        "prime_mass_M_over_N": len(primes) / N,
        "prime_power_values": [int(value) for value in powers],
        "antipode": asdict(antipode),
        "antipode_high_band": asdict(antipode),
        "antipode_full_band": asdict(full_antipode),
        "radius_midpoint_diagnostic": radius_mid,
        "full_radius_midpoint_diagnostic": full_radius_mid,
        "direction_any_interval": asdict(any_interval),
        "singleton_exact_floor": 1.0 / N if singleton_count else None,
        "singleton_resonant_nodes": singleton_count,
        "long_d": long_d,
        "long_minimum_prime_count": long_minimum,
        "direction_long_interval": asdict(long_interval),
        "direction_full_shell": asdict(shell),
        "direction_fixed_log_cells_optional": asdict(fixed_cells),
        "full_shell_pairing_scale_R_times_M_over_N": radius_mid * len(primes) / N,
        "thresholds": thresholds,
        "diagnostic_only": True,
    }


def summarize_instances(instances: Iterable[dict]) -> dict:
    """Fit log-log slopes and tabulate candidate MRAD powers."""

    rows = list(instances)
    radii = np.array([row["radius_midpoint_diagnostic"] for row in rows])

    def slope(key: str) -> float | None:
        values = np.array([row[key]["lower"] for row in rows])
        mask = (radii > 0.0) & (radii < 1.0) & (values > 0.0) & (values < 1.0)
        if int(np.sum(mask)) < 2:
            return None
        return float(np.polyfit(np.log(radii[mask]), np.log(values[mask]), 1)[0])

    powers = [0.25, 0.5, 0.75, 1.0, 1.25]
    ratios: dict[str, dict[str, list[float | None]]] = {}
    for key in ("direction_any_interval", "direction_long_interval", "direction_full_shell"):
        ratios[key] = {
            str(power): [
                ratio_to_power(row[key]["lower"], row["radius_midpoint_diagnostic"], power)
                if row[key]["available"]
                else None
                for row in rows
            ]
            for power in powers
        }
    return {
        "instances": rows,
        "log_E_on_log_R_slopes": {
            "any_interval": slope("direction_any_interval"),
            "long_interval": slope("direction_long_interval"),
            "full_shell": slope("direction_full_shell"),
        },
        "candidate_power_ratios": ratios,
        "warning": (
            "Finite floating-point diagnostics cannot establish or refute an asymptotic "
            "MRAD inequality. Upper guards use exact derivative constants but LP rounding "
            "is not interval-certified."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", nargs="+", type=int, default=[40, 70, 120, 200])
    parser.add_argument("--width", type=float, default=0.2)
    parser.add_argument("--aperture", type=float, default=1.5)
    parser.add_argument("--full-lower-exponent", type=float, default=0.01)
    parser.add_argument("--full-aperture", type=float, default=50.0 / 33.0)
    parser.add_argument("--long-d", type=float, default=0.019)
    parser.add_argument("--antipode-phase-step", type=float, default=0.08)
    parser.add_argument("--directional-phase-step", type=float, default=0.06)
    parser.add_argument("--max-exchange-iterations", type=int, default=8)
    parser.add_argument("--output", type=str)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    instances = [
        run_instance(
            N,
            width=args.width,
            aperture=args.aperture,
            full_lower_exponent=args.full_lower_exponent,
            full_aperture=args.full_aperture,
            long_d=args.long_d,
            antipode_phase_step=args.antipode_phase_step,
            directional_phase_step=args.directional_phase_step,
            max_exchange_iterations=args.max_exchange_iterations,
        )
        for N in args.N
    ]
    payload = summarize_instances(instances)
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        # CLI output paths are an explicit user/operator choice; ordinary repo
        # edits are still made with apply_patch by the agent.
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(encoded + "\n")
    print(encoded)


if __name__ == "__main__":
    main()
