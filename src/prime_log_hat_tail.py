"""Frozen high-tail diagnostic for the explicit prime-log BHP hat antenna.

The primary object is a fixed positive cosine polynomial

    P_Y(t) = sum_p lambda_p cos(t log(p/Y)),

where the coefficients are integrals of a tilted tent against piecewise-linear
nodal hats on the ordinary primes in a fixed logarithmic shell.  Floating
scouts locate candidate minima and compare matched controls.  Arb ball
arithmetic separately certifies the finite continuum inequality for the
actual-prime vector.

Nothing in this module extrapolates a finite calculation to an asymptotic
theorem.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time
from typing import Sequence

import flint
from flint import arb, ctx
import numpy as np
from scipy.optimize import minimize_scalar

from qp_radialization_lab import primes_up_to


WIDTH = Fraction(1, 5)
TILT = Fraction(49, 100)
LOWER_EXPONENT = Fraction(931, 2000)
UPPER_EXPONENT = Fraction(50, 33)
FLOOR_EXPONENT = Fraction(19, 1000)
PHASE_STEP = Fraction(1, 4)
SUBBAND_EXPONENTS = (
    LOWER_EXPONENT,
    Fraction(4, 5),
    Fraction(23, 20),
    UPPER_EXPONENT,
)


def fraction_arb(value: Fraction | int) -> arb:
    """Convert a rational to an exact Arb ball."""

    if isinstance(value, int):
        return arb(value)
    return arb(value.numerator) / arb(value.denominator)


def float_arb_exact(value: float) -> arb:
    """Convert a finite IEEE double to its exact binary rational in Arb."""

    if not math.isfinite(value):
        raise ValueError("expected a finite float")
    numerator, denominator = value.as_integer_ratio()
    return arb(numerator) / arb(denominator)


def arb_mid_float(value: arb) -> float:
    """Return the floating midpoint of an Arb ball."""

    return float(value.mid())


def arb_text(value: arb, digits: int = 40) -> str:
    """Stable human-readable ball serialization."""

    return value.str(digits)


def _unique_integer(value: arb) -> int:
    integer = value.unique_fmpz()
    if integer is None:
        raise ArithmeticError(f"Arb value is not a unique integer: {value}")
    return int(integer)


@dataclass(frozen=True)
class HatVector:
    """A positive nodal-hat probability vector in Arb arithmetic."""

    nodes: tuple[arb, ...]
    raw_weights: tuple[arb, ...]
    weights: tuple[arb, ...]
    truncated_mass: arb

    @property
    def float_nodes(self) -> np.ndarray:
        return np.array([arb_mid_float(value) for value in self.nodes])

    @property
    def float_weights(self) -> np.ndarray:
        weights = np.array([arb_mid_float(value) for value in self.weights])
        return weights / float(np.sum(weights))


@dataclass(frozen=True)
class PrimeHatVector:
    """An actual-prime shell and its explicit hat vector."""

    center: Fraction
    primes: tuple[int, ...]
    shell_lower: arb
    shell_upper: arb
    vector: HatVector
    full_tent_mass: arb
    precision_bits: int


def exact_prime_shell(
    center: Fraction,
    width: Fraction = WIDTH,
    *,
    precision_bits: int = 192,
) -> tuple[tuple[int, ...], tuple[arb, ...], arb, arb]:
    """Enumerate and certify every ordinary prime in the exact shell."""

    ctx.prec = precision_bits
    center_ball = fraction_arb(center)
    width_ball = fraction_arb(width)
    shell_lower = center_ball * (-width_ball).exp()
    shell_upper = center_ball * width_ball.exp()
    sieve_limit = _unique_integer(shell_upper.ceil())
    primes = primes_up_to(sieve_limit)
    selected: list[int] = []
    nodes: list[arb] = []
    for prime_raw in primes:
        prime = int(prime_raw)
        prime_ball = arb(prime)
        if prime_ball < shell_lower or prime_ball > shell_upper:
            continue
        if not (prime_ball >= shell_lower and prime_ball <= shell_upper):
            raise ArithmeticError(
                f"prime {prime} has ambiguous shell membership at "
                f"{precision_bits} bits"
            )
        selected.append(prime)
        nodes.append((prime_ball / center_ball).log())
    if len(selected) < 2:
        raise ValueError("the shell needs at least two prime nodes")
    for left, right in zip(nodes, nodes[1:]):
        if not left < right:
            raise ArithmeticError("prime log nodes are not strictly ordered")
    if any(node.contains(0) for node in nodes):
        raise ArithmeticError("a prime node contains the shell center")
    return tuple(selected), tuple(nodes), shell_lower, shell_upper


def _exp_poly_antiderivative(
    u: arb,
    c0: arb,
    c1: arb,
    c2: arb,
    alpha: arb,
) -> arb:
    """Antiderivative of exp(alpha*u)*(c0+c1*u+c2*u^2)."""

    p2 = c2 / alpha
    p1 = c1 / alpha - 2 * c2 / (alpha * alpha)
    p0 = (
        c0 / alpha
        - c1 / (alpha * alpha)
        + 2 * c2 / (alpha * alpha * alpha)
    )
    return (alpha * u).exp() * (p0 + p1 * u + p2 * u * u)


def _integrate_hat_side(
    left: arb,
    right: arb,
    h0: arb,
    h1: arb,
    width: arb,
    alpha: arb,
    *,
    positive_side: bool,
) -> arb:
    """Integrate one linear hat segment on one side of the tent cusp."""

    profile_slope = -1 / width if positive_side else 1 / width
    c0 = h0
    c1 = h1 + profile_slope * h0
    c2 = profile_slope * h1
    return _exp_poly_antiderivative(
        right, c0, c1, c2, alpha
    ) - _exp_poly_antiderivative(left, c0, c1, c2, alpha)


def integrate_hat_segment(
    left: arb,
    right: arb,
    h0: arb,
    h1: arb,
    width: arb,
    alpha: arb,
) -> arb:
    """Integrate a linear function (h0+h1*u) times the tilted tent."""

    if not left < right:
        raise ValueError("hat segment endpoints must be strictly ordered")
    zero = arb(0)
    if right <= zero:
        return _integrate_hat_side(
            left,
            right,
            h0,
            h1,
            width,
            alpha,
            positive_side=False,
        )
    if left >= zero:
        return _integrate_hat_side(
            left,
            right,
            h0,
            h1,
            width,
            alpha,
            positive_side=True,
        )
    if not (left < zero and right > zero):
        raise ArithmeticError("a hat segment has ambiguous cusp geometry")
    return _integrate_hat_side(
        left,
        zero,
        h0,
        h1,
        width,
        alpha,
        positive_side=False,
    ) + _integrate_hat_side(
        zero,
        right,
        h0,
        h1,
        width,
        alpha,
        positive_side=True,
    )


def hat_vector_from_arb_nodes(
    nodes: Sequence[arb],
    width: Fraction = WIDTH,
    alpha: Fraction = TILT,
) -> HatVector:
    """Compute exact-form finite-element weights with Arb enclosures."""

    if len(nodes) < 2:
        raise ValueError("at least two nodes are required")
    for left, right in zip(nodes, nodes[1:]):
        if not left < right:
            raise ValueError("nodes must be strictly increasing")
    width_ball = fraction_arb(width)
    alpha_ball = fraction_arb(alpha)
    raw: list[arb] = []
    for index, node in enumerate(nodes):
        weight = arb(0)
        if index:
            left = nodes[index - 1]
            denominator = node - left
            weight += integrate_hat_segment(
                left,
                node,
                -left / denominator,
                1 / denominator,
                width_ball,
                alpha_ball,
            )
        if index + 1 < len(nodes):
            right = nodes[index + 1]
            denominator = right - node
            weight += integrate_hat_segment(
                node,
                right,
                right / denominator,
                -1 / denominator,
                width_ball,
                alpha_ball,
            )
        if not weight.lower() > 0:
            raise ArithmeticError(f"hat weight {index} is not certified positive")
        raw.append(weight)
    mass = sum(raw, arb(0))
    if not mass.lower() > 0:
        raise ArithmeticError("hat mass is not certified positive")
    weights = tuple(value / mass for value in raw)
    normalized_sum = sum(weights, arb(0))
    if not normalized_sum.contains(1):
        raise ArithmeticError("normalized weight balls do not contain unit mass")
    return HatVector(tuple(nodes), tuple(raw), weights, mass)


def full_tent_mass(width: Fraction = WIDTH, alpha: Fraction = TILT) -> arb:
    """Integral of the tilted tent over its complete theoretical support."""

    width_ball = fraction_arb(width)
    alpha_ball = fraction_arb(alpha)
    return 2 * ((alpha_ball * width_ball).cosh() - 1) / (
        width_ball * alpha_ball * alpha_ball
    )


def build_prime_hat_vector(
    center: Fraction,
    *,
    precision_bits: int = 192,
) -> PrimeHatVector:
    """Recompute the actual prime mask, log nodes, and hat weights."""

    ctx.prec = precision_bits
    primes, nodes, lower, upper = exact_prime_shell(
        center, precision_bits=precision_bits
    )
    vector = hat_vector_from_arb_nodes(nodes)
    return PrimeHatVector(
        center=center,
        primes=primes,
        shell_lower=lower,
        shell_upper=upper,
        vector=vector,
        full_tent_mass=full_tent_mass(),
        precision_bits=precision_bits,
    )


def vector_from_float_nodes(
    nodes: np.ndarray,
    *,
    precision_bits: int = 160,
) -> HatVector:
    """Build control weights while freezing every double as an exact rational."""

    ctx.prec = precision_bits
    exact_nodes = tuple(float_arb_exact(float(value)) for value in nodes)
    return hat_vector_from_arb_nodes(exact_nodes)


def odd_half_grid_control(nodes: np.ndarray, band_right: float) -> np.ndarray:
    """Snap interior nodes to same-sign odd multiples of pi/band_right."""

    nodes = np.asarray(nodes, dtype=float)
    if len(nodes) < 3 or not np.all(np.diff(nodes) > 0):
        raise ValueError("ordered nodes with an interior are required")
    result = nodes.copy()
    for index in range(1, len(nodes) - 1):
        quotient = nodes[index] * band_right / math.pi
        anchor = math.floor(quotient)
        candidates = [
            integer
            for integer in range(anchor - 5, anchor + 7)
            if integer % 2 != 0 and integer * nodes[index] > 0
        ]
        if not candidates:
            raise ArithmeticError("no same-sign odd half-grid candidate")
        odd_integer = min(
            candidates,
            key=lambda value: (abs(value - quotient), value),
        )
        result[index] = odd_integer * math.pi / band_right
    if not np.all(np.diff(result) > 0):
        raise ArithmeticError("half-grid snapping did not preserve order")
    if len(np.unique(result)) != len(result):
        raise ArithmeticError("half-grid snapping created a duplicate")
    if not np.all(np.sign(result) == np.sign(nodes)):
        raise ArithmeticError("half-grid snapping changed a node sign")
    return result


def jitter_control(nodes: np.ndarray, eta: float, seed: int) -> np.ndarray:
    """Apply the preregistered local order- and sign-preserving jitter."""

    nodes = np.asarray(nodes, dtype=float)
    if not 0 < eta < 1:
        raise ValueError("eta must lie in (0,1)")
    if len(nodes) < 3 or not np.all(np.diff(nodes) > 0):
        raise ValueError("ordered nodes with an interior are required")
    result = nodes.copy()
    rng = np.random.Generator(np.random.PCG64(seed))
    random_values = rng.uniform(-1.0, 1.0, len(nodes) - 2)
    for offset, index in enumerate(range(1, len(nodes) - 1)):
        radius = 0.25 * min(
            nodes[index] - nodes[index - 1],
            nodes[index + 1] - nodes[index],
            abs(nodes[index]),
        )
        result[index] += eta * radius * random_values[offset]
    if not np.all(np.diff(result) > 0):
        raise ArithmeticError("jitter did not preserve strict order")
    if not np.all(np.sign(result) == np.sign(nodes)):
        raise ArithmeticError("jitter changed a node sign")
    if result[0] != nodes[0] or result[-1] != nodes[-1]:
        raise ArithmeticError("jitter moved an endpoint")
    return result


def polynomial_value(nodes: np.ndarray, weights: np.ndarray, time_value: float) -> float:
    """Evaluate one floating cosine polynomial value."""

    return float(np.dot(weights, np.cos(nodes * time_value)))


def polynomial_values(
    nodes: np.ndarray,
    weights: np.ndarray,
    times: np.ndarray,
    *,
    chunk_size: int = 30_000,
) -> np.ndarray:
    """Evaluate a cosine polynomial without allocating one huge matrix."""

    values = np.empty(len(times))
    for left in range(0, len(times), chunk_size):
        right = min(len(times), left + chunk_size)
        values[left:right] = (
            np.cos(np.outer(times[left:right], nodes)) @ weights
        )
    return values


@dataclass(frozen=True)
class FloatingScout:
    """A nonrigorous, curvature-guarded search summary."""

    grid_minimum: float
    grid_argmin: float
    refined_minimum: float
    refined_argmin: float
    refined_argmin_exponent: float
    curvature: float
    grid_step: float
    curvature_guard: float
    guarded_lower: float
    grid_size: int
    target_floor: float
    negative_depth: float
    target_ratio: float
    subband_minima: tuple[dict[str, float], ...]
    local_minima: tuple[dict[str, float], ...]
    trust: str = "FLOAT-SCOUT"


def floating_scout(
    nodes: np.ndarray,
    weights: np.ndarray,
    center: float,
    *,
    phase_step: float = float(PHASE_STEP),
    local_minimum_count: int = 8,
) -> FloatingScout:
    """Scan the complete frozen band and refine the lowest sampled minima."""

    nodes = np.asarray(nodes, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if len(nodes) != len(weights) or len(nodes) < 2:
        raise ValueError("nodes and weights must have equal nontrivial length")
    left = center ** float(LOWER_EXPONENT)
    right = center ** float(UPPER_EXPONENT)
    max_node = float(np.max(np.abs(nodes)))
    interval_count = max(
        2,
        int(math.ceil((right - left) * max_node / phase_step)),
    )
    grid = np.linspace(left, right, interval_count + 1)
    values = polynomial_values(nodes, weights, grid)
    grid_index = int(np.argmin(values))
    candidate_indices = np.flatnonzero(
        (values[1:-1] <= values[:-2]) & (values[1:-1] <= values[2:])
    ) + 1
    candidate_indices = np.unique(
        np.r_[candidate_indices, 0, len(grid) - 1]
    )
    ordered_candidates = candidate_indices[
        np.argsort(values[candidate_indices])
    ][:local_minimum_count]
    refined: list[tuple[float, float]] = []
    for index in ordered_candidates:
        if index == 0 or index == len(grid) - 1:
            refined.append((float(values[index]), float(grid[index])))
            continue
        result = minimize_scalar(
            lambda time_value: polynomial_value(nodes, weights, time_value),
            bounds=(float(grid[index - 1]), float(grid[index + 1])),
            method="bounded",
            options={"xatol": 1e-11, "maxiter": 120},
        )
        if result.success:
            refined.append((float(result.fun), float(result.x)))
        else:
            refined.append((float(values[index]), float(grid[index])))
    refined.sort()
    refined_minimum, refined_argmin = refined[0]
    grid_step = float(grid[1] - grid[0])
    curvature = float(np.dot(weights, nodes * nodes))
    curvature_guard = curvature * grid_step * grid_step / 8.0
    target = center ** -float(FLOOR_EXPONENT)
    subbands: list[dict[str, float]] = []
    for exponent_left, exponent_right in zip(
        SUBBAND_EXPONENTS, SUBBAND_EXPONENTS[1:]
    ):
        time_left = center ** float(exponent_left)
        time_right = center ** float(exponent_right)
        first = int(np.searchsorted(grid, time_left, side="left"))
        last = int(np.searchsorted(grid, time_right, side="right"))
        last = max(first + 1, min(last, len(grid)))
        local_index = first + int(np.argmin(values[first:last]))
        subbands.append(
            {
                "left_exponent": float(exponent_left),
                "right_exponent": float(exponent_right),
                "minimum": float(values[local_index]),
                "argmin": float(grid[local_index]),
            }
        )
    return FloatingScout(
        grid_minimum=float(values[grid_index]),
        grid_argmin=float(grid[grid_index]),
        refined_minimum=refined_minimum,
        refined_argmin=refined_argmin,
        refined_argmin_exponent=math.log(refined_argmin) / math.log(center),
        curvature=curvature,
        grid_step=grid_step,
        curvature_guard=curvature_guard,
        guarded_lower=float(values[grid_index]) - curvature_guard,
        grid_size=len(grid),
        target_floor=-target,
        negative_depth=max(0.0, -refined_minimum),
        target_ratio=max(0.0, -refined_minimum) / target,
        subband_minima=tuple(subbands),
        local_minima=tuple(
            {"minimum": minimum, "argmin": argmin}
            for minimum, argmin in refined
        ),
    )


def feature_audit(
    nodes: np.ndarray,
    weights: np.ndarray,
    *,
    reference_nodes: np.ndarray | None = None,
    reference_weights: np.ndarray | None = None,
) -> dict[str, float | int]:
    """Record geometry and mass features for actual and control vectors."""

    nodes = np.asarray(nodes, dtype=float)
    weights = np.asarray(weights, dtype=float)
    gaps = np.diff(nodes)
    if len(nodes) != len(weights) or np.any(gaps <= 0):
        raise ValueError("feature audit requires ordered nodes and matching weights")
    result: dict[str, float | int] = {
        "node_count": int(len(nodes)),
        "negative_node_count": int(np.count_nonzero(nodes < 0)),
        "positive_node_count": int(np.count_nonzero(nodes > 0)),
        "left_endpoint": float(nodes[0]),
        "right_endpoint": float(nodes[-1]),
        "minimum_gap": float(np.min(gaps)),
        "maximum_gap": float(np.max(gaps)),
        "sum_squared_gaps": float(np.dot(gaps, gaps)),
        "weight_sum": float(np.sum(weights)),
        "maximum_weight": float(np.max(weights)),
        "minimum_weight": float(np.min(weights)),
        "effective_support": float(1.0 / np.dot(weights, weights)),
        "second_moment": float(np.dot(weights, nodes * nodes)),
    }
    if reference_nodes is not None:
        reference_nodes = np.asarray(reference_nodes, dtype=float)
        if len(reference_nodes) != len(nodes):
            raise ValueError("reference nodes have a different size")
        reference_gaps = np.diff(reference_nodes)
        result.update(
            {
                "maximum_rank_displacement": float(
                    np.max(np.abs(nodes - reference_nodes))
                ),
                "maximum_relative_gap_change": float(
                    np.max(np.abs(gaps - reference_gaps) / reference_gaps)
                ),
            }
        )
    if reference_weights is not None:
        reference_weights = np.asarray(reference_weights, dtype=float)
        if len(reference_weights) != len(weights):
            raise ValueError("reference weights have a different size")
        result["weight_l1_change"] = float(
            np.sum(np.abs(weights - reference_weights))
        )
    return result


def prime_vector_fingerprints(prime_vector: PrimeHatVector) -> dict[str, str]:
    """Hash the exact construction inputs and the current Arb enclosures."""

    exact_payload = {
        "center": [
            prime_vector.center.numerator,
            prime_vector.center.denominator,
        ],
        "width": [WIDTH.numerator, WIDTH.denominator],
        "tilt": [TILT.numerator, TILT.denominator],
        "primes": list(prime_vector.primes),
    }
    exact_bytes = json.dumps(
        exact_payload, sort_keys=True, separators=(",", ":")
    ).encode()
    numeric_payload = {
        "nodes": [arb_text(value, 70) for value in prime_vector.vector.nodes],
        "weights": [
            arb_text(value, 70) for value in prime_vector.vector.weights
        ],
    }
    numeric_bytes = json.dumps(
        numeric_payload, sort_keys=True, separators=(",", ":")
    ).encode()
    return {
        "exact_input_sha256": hashlib.sha256(exact_bytes).hexdigest(),
        "arb_enclosure_sha256": hashlib.sha256(numeric_bytes).hexdigest(),
    }


def arb_polynomial_value(
    nodes: Sequence[arb],
    weights: Sequence[arb],
    time_value: Fraction,
) -> arb:
    """Evaluate a fixed cosine polynomial at one exact rational height."""

    time_ball = fraction_arb(time_value)
    return sum(
        (
            weight * (node * time_ball).cos()
            for node, weight in zip(nodes, weights)
        ),
        arb(0),
    )


def arb_hat_polynomial_value(
    vector: HatVector,
    time_value: Fraction,
) -> arb:
    """Evaluate as one raw-weight numerator divided by the shared mass."""

    time_ball = fraction_arb(time_value)
    numerator = sum(
        (
            raw_weight * (node * time_ball).cos()
            for node, raw_weight in zip(vector.nodes, vector.raw_weights)
        ),
        arb(0),
    )
    return numerator / vector.truncated_mass


def _outer_dyadic_cover(
    band_left: arb,
    band_right: arb,
    dyadic_bits: int,
) -> tuple[Fraction, Fraction]:
    denominator = 1 << dyadic_bits
    scaled_left = band_left * denominator
    scaled_right = band_right * denominator
    left_numerator = _unique_integer(scaled_left.floor()) - 1
    right_numerator = _unique_integer(scaled_right.ceil()) + 1
    left = Fraction(left_numerator, denominator)
    right = Fraction(right_numerator, denominator)
    if not fraction_arb(left) < band_left:
        raise ArithmeticError("left dyadic endpoint is not an outer endpoint")
    if not fraction_arb(right) > band_right:
        raise ArithmeticError("right dyadic endpoint is not an outer endpoint")
    return left, right


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class ContinuumCertificate:
    """Result of the rigorous fixed-vector threshold decision."""

    status: str
    trust: str
    precision_bits: int
    exact_band_left: str
    exact_band_right: str
    threshold: str
    cover_left: str
    cover_right: str
    dyadic_bits: int
    second_moment: str
    leaf_count: int
    point_evaluation_count: int
    maximum_depth_used: int
    minimum_leaf_lower_bound: str | None
    leaf_sha256: str | None
    partition_verified: bool
    kraft_sum: str
    witness_time: str | None
    witness_value: str | None
    unresolved_cell: dict[str, int] | None
    wall_seconds: float
    leaves: tuple[dict[str, int | str], ...] = ()


def interpolation_cell_lower(
    value_left: arb,
    value_right: arb,
    second_moment: arb,
    width: Fraction,
) -> arb:
    """Rigorous endpoint-interpolation lower bound on one cell."""

    endpoint_lower = (
        value_left.lower()
        if value_left.lower() <= value_right.lower()
        else value_right.lower()
    )
    width_ball = fraction_arb(width)
    guard = second_moment.upper() * width_ball * width_ball / 8
    return (endpoint_lower - guard).lower()


def validate_dyadic_leaf_partition(
    paths: Sequence[tuple[int, int]],
) -> tuple[bool, Fraction]:
    """Check that dyadic paths are disjoint and cover the unit root interval."""

    intervals = sorted(
        (
            Fraction(index, 1 << depth),
            Fraction(index + 1, 1 << depth),
        )
        for depth, index in paths
    )
    kraft_sum = sum(
        (Fraction(1, 1 << depth) for depth, _ in paths),
        Fraction(0),
    )
    if not intervals:
        return False, kraft_sum
    cursor = Fraction(0)
    for left, right in intervals:
        if left != cursor or not left < right:
            return False, kraft_sum
        cursor = right
    return cursor == 1 and kraft_sum == 1, kraft_sum


def _is_proved_inside(
    time_value: Fraction,
    band_left: arb,
    band_right: arb,
) -> bool:
    time_ball = fraction_arb(time_value)
    return bool(time_ball > band_left and time_ball < band_right)


def continuum_certificate(
    prime_vector: PrimeHatVector,
    *,
    scout_argmin: float | None = None,
    dyadic_bits: int = 40,
    max_depth: int = 32,
    max_leaves: int = 1_000_000,
    record_leaves: bool = True,
) -> ContinuumCertificate:
    """Certify or refute the finite floor on the full continuum band.

    Every accepted leaf uses the endpoint interpolation remainder with the
    global positive-weight second moment.  A failure is returned only from a
    rigorous point ball at a point proved to be strictly inside the exact
    band.
    """

    started = time.monotonic()
    ctx.prec = prime_vector.precision_bits
    center_ball = fraction_arb(prime_vector.center)
    band_left = center_ball ** fraction_arb(LOWER_EXPONENT)
    band_right = center_ball ** fraction_arb(UPPER_EXPONENT)
    threshold = -(center_ball ** (-fraction_arb(FLOOR_EXPONENT)))
    root_left, root_right = _outer_dyadic_cover(
        band_left, band_right, dyadic_bits
    )
    root_width = root_right - root_left
    vector = prime_vector.vector
    second_moment_numerator = sum(
        (
            raw_weight * node * node
            for node, raw_weight in zip(vector.nodes, vector.raw_weights)
        ),
        arb(0),
    )
    second_moment = second_moment_numerator / vector.truncated_mass
    if not second_moment.lower() > 0:
        raise ArithmeticError("second moment is not certified positive")
    if not second_moment.upper() < fraction_arb(WIDTH) ** 2:
        raise ArithmeticError("second moment exceeds the shell aperture bound")

    cache: dict[Fraction, arb] = {}

    def evaluate(time_value: Fraction) -> arb:
        if time_value not in cache:
            cache[time_value] = arb_hat_polynomial_value(vector, time_value)
        return cache[time_value]

    def point_witness(time_value: Fraction) -> tuple[bool, arb]:
        value = evaluate(time_value)
        fails = (
            _is_proved_inside(time_value, band_left, band_right)
            and bool(value.upper() < threshold.lower())
        )
        return fails, value

    if scout_argmin is not None:
        scout_time = Fraction.from_float(float(scout_argmin))
        fails, scout_value = point_witness(scout_time)
        if fails:
            return ContinuumCertificate(
                status="FAIL",
                trust="ARB-POINT-WITNESS",
                precision_bits=prime_vector.precision_bits,
                exact_band_left=arb_text(band_left),
                exact_band_right=arb_text(band_right),
                threshold=arb_text(threshold),
                cover_left=_fraction_text(root_left),
                cover_right=_fraction_text(root_right),
                dyadic_bits=dyadic_bits,
                second_moment=arb_text(second_moment),
                leaf_count=0,
                point_evaluation_count=len(cache),
                maximum_depth_used=0,
                minimum_leaf_lower_bound=None,
                leaf_sha256=None,
                partition_verified=False,
                kraft_sum="0/1",
                witness_time=_fraction_text(scout_time),
                witness_value=arb_text(scout_value),
                unresolved_cell=None,
                wall_seconds=time.monotonic() - started,
            )

    stack: list[tuple[int, int]] = [(0, 0)]
    passed_leaves: list[dict[str, int | str]] = []
    passed_paths: list[tuple[int, int]] = []
    passed_leaf_count = 0
    leaf_hasher = hashlib.sha256()
    minimum_leaf_ball: arb | None = None
    minimum_leaf_text: str | None = None
    maximum_depth_used = 0
    unresolved: dict[str, int] | None = None
    witness_time: Fraction | None = None
    witness_value: arb | None = None

    while stack:
        depth, index = stack.pop()
        denominator = 1 << depth
        left = root_left + root_width * Fraction(index, denominator)
        right = root_left + root_width * Fraction(index + 1, denominator)
        midpoint = (left + right) / 2
        value_left = evaluate(left)
        value_right = evaluate(right)
        lower_bound = interpolation_cell_lower(
            value_left,
            value_right,
            second_moment,
            right - left,
        )
        maximum_depth_used = max(maximum_depth_used, depth)
        if lower_bound >= threshold.upper():
            passed_leaf_count += 1
            passed_paths.append((depth, index))
            if (
                minimum_leaf_ball is None
                or lower_bound.lower() < minimum_leaf_ball.lower()
            ):
                minimum_leaf_ball = lower_bound
                minimum_leaf_text = arb_text(lower_bound)
            canonical = f"{depth}:{index}:{arb_text(lower_bound, 50)}\n"
            leaf_hasher.update(canonical.encode())
            if record_leaves:
                passed_leaves.append(
                    {
                        "depth": depth,
                        "index": index,
                        "lower_bound": arb_text(lower_bound, 50),
                    }
                )
            continue

        fails, midpoint_value = point_witness(midpoint)
        if fails:
            witness_time = midpoint
            witness_value = midpoint_value
            break
        if depth >= max_depth:
            unresolved = {"depth": depth, "index": index}
            break
        prospective_leaf_count = passed_leaf_count + len(stack) + 2
        if prospective_leaf_count > max_leaves:
            unresolved = {"depth": depth, "index": index}
            break
        stack.append((depth + 1, 2 * index + 1))
        stack.append((depth + 1, 2 * index))

    if witness_time is not None and witness_value is not None:
        status = "FAIL"
        trust = "ARB-POINT-WITNESS"
    elif unresolved is not None:
        status = "INCONCLUSIVE"
        trust = "ARB-INCOMPLETE-COVER"
    elif stack:
        status = "INCONCLUSIVE"
        trust = "ARB-INCOMPLETE-COVER"
    else:
        status = "PASS"
        trust = "ARB-CONTINUUM-CERTIFIED"
    partition_verified, kraft_sum = validate_dyadic_leaf_partition(passed_paths)
    if status == "PASS" and not partition_verified:
        raise ArithmeticError("accepted leaves do not form a complete partition")
    return ContinuumCertificate(
        status=status,
        trust=trust,
        precision_bits=prime_vector.precision_bits,
        exact_band_left=arb_text(band_left),
        exact_band_right=arb_text(band_right),
        threshold=arb_text(threshold),
        cover_left=_fraction_text(root_left),
        cover_right=_fraction_text(root_right),
        dyadic_bits=dyadic_bits,
        second_moment=arb_text(second_moment),
        leaf_count=passed_leaf_count,
        point_evaluation_count=len(cache),
        maximum_depth_used=maximum_depth_used,
        minimum_leaf_lower_bound=minimum_leaf_text,
        leaf_sha256=(
            leaf_hasher.hexdigest() if status == "PASS" else None
        ),
        partition_verified=partition_verified,
        kraft_sum=_fraction_text(kraft_sum),
        witness_time=(
            _fraction_text(witness_time) if witness_time is not None else None
        ),
        witness_value=(
            arb_text(witness_value) if witness_value is not None else None
        ),
        unresolved_cell=unresolved,
        wall_seconds=time.monotonic() - started,
        leaves=tuple(passed_leaves),
    )


def prime_vector_payload(prime_vector: PrimeHatVector) -> dict[str, object]:
    """Serialize enough exact and interval data to replay a certificate."""

    vector = prime_vector.vector
    float_nodes = vector.float_nodes
    float_weights = vector.float_weights
    gaps = np.diff(float_nodes)
    shell_margin = min(
        abs(prime_vector.primes[0] - arb_mid_float(prime_vector.shell_lower)),
        abs(prime_vector.primes[-1] - arb_mid_float(prime_vector.shell_upper)),
    )
    return {
        "center": {
            "numerator": prime_vector.center.numerator,
            "denominator": prime_vector.center.denominator,
            "decimal": float(prime_vector.center),
        },
        "precision_bits": prime_vector.precision_bits,
        "primes": list(prime_vector.primes),
        "prime_count": len(prime_vector.primes),
        "shell_lower": arb_text(prime_vector.shell_lower),
        "shell_upper": arb_text(prime_vector.shell_upper),
        "minimum_boundary_margin_float": shell_margin,
        "nodes_arb": [arb_text(value, 70) for value in vector.nodes],
        "weights_arb": [arb_text(value, 70) for value in vector.weights],
        "nodes_float": float_nodes.tolist(),
        "weights_float": float_weights.tolist(),
        "truncated_mass": arb_text(vector.truncated_mass),
        "full_tent_mass": arb_text(prime_vector.full_tent_mass),
        "truncated_to_full_mass_ratio": (
            arb_mid_float(vector.truncated_mass)
            / arb_mid_float(prime_vector.full_tent_mass)
        ),
        "maximum_log_gap": float(np.max(gaps)),
        "fingerprints": prime_vector_fingerprints(prime_vector),
        "features": feature_audit(float_nodes, float_weights),
    }


def _preregistered_controls() -> tuple[dict[str, object], ...]:
    controls: list[dict[str, object]] = [{"kind": "half_grid"}]
    controls.extend(
        {"kind": "jitter", "eta": 0.3, "seed": seed}
        for seed in (1729, 2718, 31415, 65537, 104729)
    )
    controls.extend(
        {"kind": "jitter", "eta": 0.1, "seed": seed}
        for seed in (1729, 31415)
    )
    controls.extend(
        {"kind": "jitter", "eta": 0.6, "seed": seed}
        for seed in (1729, 31415)
    )
    return tuple(controls)


def run_controls(
    actual_nodes: np.ndarray,
    actual_weights: np.ndarray,
    actual_scout: FloatingScout,
    center: float,
) -> list[dict[str, object]]:
    """Run all frozen controls with freshly recomputed hat weights."""

    band_right = center ** float(UPPER_EXPONENT)
    results: list[dict[str, object]] = []
    for specification in _preregistered_controls():
        if specification["kind"] == "half_grid":
            nodes = odd_half_grid_control(actual_nodes, band_right)
            name = "half_grid"
        else:
            eta = float(specification["eta"])
            seed = int(specification["seed"])
            nodes = jitter_control(actual_nodes, eta, seed)
            name = f"jitter_eta_{eta:g}_seed_{seed}"
        control_vector = vector_from_float_nodes(nodes)
        weights = control_vector.float_weights
        scout = floating_scout(nodes, weights, center)
        payload: dict[str, object] = {
            "name": name,
            "specification": specification,
            "scout": asdict(scout),
            "value_at_actual_argmin": polynomial_value(
                nodes, weights, actual_scout.refined_argmin
            ),
            "features": feature_audit(
                nodes,
                weights,
                reference_nodes=actual_nodes,
                reference_weights=actual_weights,
            ),
            "truncated_mass": arb_text(control_vector.truncated_mass),
        }
        if specification["kind"] == "half_grid":
            interior_cosines = np.cos(nodes[1:-1] * band_right)
            payload.update(
                {
                    "value_at_band_right": polynomial_value(
                        nodes, weights, band_right
                    ),
                    "maximum_interior_antipode_error": float(
                        np.max(np.abs(interior_cosines + 1.0))
                    ),
                    "endpoint_weight": float(weights[0] + weights[-1]),
                }
            )
        results.append(payload)
    return results


def certificate_summary(
    certificate: ContinuumCertificate,
) -> dict[str, object]:
    """Serialize a certificate without duplicating its potentially large leaf list."""

    payload = asdict(certificate)
    payload.pop("leaves")
    return payload


def write_json(path: Path, payload: object) -> str:
    """Write canonical indented JSON and return its SHA-256 digest."""

    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(
        payload,
        indent=2,
        sort_keys=True,
        allow_nan=False,
    ) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(serialized, encoding="utf-8")
    temporary.replace(path)
    return hashlib.sha256(serialized.encode()).hexdigest()


def _validated_centers(preregistration: dict[str, object]) -> tuple[Fraction, ...]:
    if preregistration.get("schema") != "zeta23.ht_hat.prereg.v1":
        raise ValueError("unexpected preregistration schema")
    construction = preregistration["construction"]
    assert isinstance(construction, dict)
    width = construction["width"]
    tilt = construction["tilt"]
    assert isinstance(width, dict) and isinstance(tilt, dict)
    if Fraction(int(width["numerator"]), int(width["denominator"])) != WIDTH:
        raise ValueError("preregistered width does not match the implementation")
    if Fraction(int(tilt["numerator"]), int(tilt["denominator"])) != TILT:
        raise ValueError("preregistered tilt does not match the implementation")
    centers_raw = construction["centers"]
    assert isinstance(centers_raw, list)
    centers = tuple(
        Fraction(int(item["numerator"]), int(item["denominator"]))
        for item in centers_raw
    )
    expected = (
        Fraction(1025, 2),
        Fraction(2049, 2),
        Fraction(4097, 2),
        Fraction(8193, 2),
    )
    if centers != expected:
        raise ValueError("the center ladder differs from the frozen ladder")
    band = preregistration["band_and_floor"]
    assert isinstance(band, dict)
    checks = (
        ("lower_exponent", LOWER_EXPONENT),
        ("upper_exponent", UPPER_EXPONENT),
        ("floor_exponent", FLOOR_EXPONENT),
        ("scout_phase_step", PHASE_STEP),
    )
    for key, expected_value in checks:
        value = band[key]
        assert isinstance(value, dict)
        observed = Fraction(
            int(value["numerator"]), int(value["denominator"])
        )
        if observed != expected_value:
            raise ValueError(f"preregistered {key} differs from the implementation")
    if band.get("subband_exponents") != [
        "931/2000",
        "4/5",
        "23/20",
        "50/33",
    ]:
        raise ValueError("preregistered subbands differ from the implementation")

    controls = preregistration["controls"]
    assert isinstance(controls, dict)
    if controls.get("recompute_hat_weights_for_every_control") is not True:
        raise ValueError("control weights must be recomputed")
    jitter = controls["order_preserving_jitter"]
    assert isinstance(jitter, dict)
    expected_jitters = {
        "primary": {
            "eta": "3/10",
            "seeds": [1729, 2718, 31415, 65537, 104729],
        },
        "sensitivity_low": {"eta": "1/10", "seeds": [1729, 31415]},
        "sensitivity_high": {"eta": "3/5", "seeds": [1729, 31415]},
    }
    for key, expected_jitter in expected_jitters.items():
        if jitter.get(key) != expected_jitter:
            raise ValueError(f"preregistered {key} jitter differs")

    certification = preregistration["certification"]
    assert isinstance(certification, dict)
    expected_certification = {
        "precision_bits": 192,
        "repeat_precision_bits": 256,
        "cover_dyadic_bits": 40,
        "max_depth": 32,
        "max_leaves": 1_000_000,
    }
    for key, expected_value in expected_certification.items():
        if certification.get(key) != expected_value:
            raise ValueError(f"preregistered certification {key} differs")
    expected_stop = (
        "Run exactly the four frozen centers. Do not add scales, alter "
        "parameters, or promote trends after inspecting outcomes."
    )
    if preregistration.get("stopping_rule") != expected_stop:
        raise ValueError("the preregistered stopping rule differs")
    return centers


def _certificate_payload(
    preregistration_sha256: str,
    source_sha256: str,
    prime_vector: PrimeHatVector,
    certificate: ContinuumCertificate,
) -> dict[str, object]:
    return {
        "schema": "zeta23.ht_hat.arb_certificate.v1",
        "experiment_id": "HT-HAT-PREREG-V1",
        "preregistration_sha256": preregistration_sha256,
        "source_sha256": source_sha256,
        "mathematical_scope": (
            "One fixed-vector, fixed-center finite continuum inequality only."
        ),
        "construction": {
            "width": [WIDTH.numerator, WIDTH.denominator],
            "tilt": [TILT.numerator, TILT.denominator],
            "lower_exponent": [
                LOWER_EXPONENT.numerator,
                LOWER_EXPONENT.denominator,
            ],
            "upper_exponent": [
                UPPER_EXPONENT.numerator,
                UPPER_EXPONENT.denominator,
            ],
            "floor_exponent": [
                FLOOR_EXPONENT.numerator,
                FLOOR_EXPONENT.denominator,
            ],
        },
        "prime_vector": prime_vector_payload(prime_vector),
        "certificate": asdict(certificate),
        "replay": {
            "module": "src/prime_log_hat_tail.py",
            "method": (
                "Recompute the exact prime list and Arb hat integrals, then "
                "replay every dyadic leaf using the endpoint interpolation bound."
            ),
        },
        "dependencies": {
            "python": sys.version,
            "python_flint": flint.__version__,
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }


def source_sha256() -> str:
    """Hash the exact implementation file used for a run or replay."""

    return hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()


def _parse_fraction_text(value: str) -> Fraction:
    numerator, denominator = value.split("/", maxsplit=1)
    return Fraction(int(numerator), int(denominator))


def verify_certificate_file(path: Path) -> dict[str, object]:
    """Recompute a serialized PASS cover or rigorous FAIL witness from disk."""

    stored = json.loads(path.read_text(encoding="utf-8"))
    if stored.get("schema") != "zeta23.ht_hat.arb_certificate.v1":
        raise ValueError("unexpected certificate schema")
    stored_vector = stored["prime_vector"]
    center_data = stored_vector["center"]
    center = Fraction(
        int(center_data["numerator"]), int(center_data["denominator"])
    )
    stored_certificate = stored["certificate"]
    precision_bits = int(stored_certificate["precision_bits"])
    prime_vector = build_prime_hat_vector(
        center, precision_bits=precision_bits
    )
    current_source = source_sha256()
    source_matches = current_source == stored.get("source_sha256")
    exact_input_matches = (
        prime_vector_fingerprints(prime_vector)["exact_input_sha256"]
        == stored_vector["fingerprints"]["exact_input_sha256"]
    )
    status = stored_certificate["status"]
    replay_status: str
    leaf_hash_matches = False
    leaf_count_matches = False
    stored_partition_valid = False
    witness_verified = False
    recomputed_status: str | None = None

    if status == "PASS":
        stored_leaves = stored_certificate["leaves"]
        stored_paths = tuple(
            (int(leaf["depth"]), int(leaf["index"]))
            for leaf in stored_leaves
        )
        stored_partition_valid, stored_kraft = validate_dyadic_leaf_partition(
            stored_paths
        )
        stored_partition_valid = (
            stored_partition_valid
            and _fraction_text(stored_kraft)
            == stored_certificate["kraft_sum"]
            and len(stored_paths) == int(stored_certificate["leaf_count"])
        )
        recomputed = continuum_certificate(
            prime_vector,
            dyadic_bits=int(stored_certificate["dyadic_bits"]),
            max_depth=max(32, int(stored_certificate["maximum_depth_used"])),
            max_leaves=max(
                1_000_000, 2 * int(stored_certificate["leaf_count"])
            ),
            record_leaves=True,
        )
        recomputed_status = recomputed.status
        leaf_hash_matches = (
            recomputed.leaf_sha256 == stored_certificate["leaf_sha256"]
        )
        leaf_count_matches = (
            recomputed.leaf_count == int(stored_certificate["leaf_count"])
        )
        verified = (
            source_matches
            and exact_input_matches
            and stored_partition_valid
            and recomputed.status == "PASS"
            and recomputed.partition_verified
            and leaf_hash_matches
            and leaf_count_matches
        )
        replay_status = "PASS-REPLAYED" if verified else "REPLAY-MISMATCH"
    elif status == "FAIL":
        witness_text = stored_certificate.get("witness_time")
        if witness_text is None:
            witness_time = None
        else:
            witness_time = _parse_fraction_text(witness_text)
        if witness_time is not None:
            center_ball = fraction_arb(center)
            band_left = center_ball ** fraction_arb(LOWER_EXPONENT)
            band_right = center_ball ** fraction_arb(UPPER_EXPONENT)
            threshold = -(center_ball ** (-fraction_arb(FLOOR_EXPONENT)))
            witness_value = arb_hat_polynomial_value(
                prime_vector.vector, witness_time
            )
            witness_verified = (
                _is_proved_inside(witness_time, band_left, band_right)
                and bool(witness_value.upper() < threshold.lower())
            )
        verified = source_matches and exact_input_matches and witness_verified
        replay_status = "FAIL-WITNESS-REPLAYED" if verified else "REPLAY-MISMATCH"
    else:
        verified = False
        replay_status = "INCONCLUSIVE-NOT-A-DECISIVE-CERTIFICATE"

    return {
        "verified": verified,
        "replay_status": replay_status,
        "stored_status": status,
        "recomputed_status": recomputed_status,
        "source_sha256_matches": source_matches,
        "exact_input_sha256_matches": exact_input_matches,
        "stored_partition_valid": stored_partition_valid,
        "leaf_hash_matches": leaf_hash_matches,
        "leaf_count_matches": leaf_count_matches,
        "witness_verified": witness_verified,
        "current_source_sha256": current_source,
    }


def run_scale(
    center: Fraction,
    *,
    preregistration_sha256: str,
    source_sha256: str,
    certificate_directory: Path,
    precision_first: int = 192,
    precision_repeat: int = 256,
    dyadic_bits: int = 40,
    max_depth: int = 32,
    max_leaves: int = 1_000_000,
) -> dict[str, object]:
    """Run scouts, two precision certifications, and all frozen controls."""

    center_float = float(center)
    print(
        f"[HT-HAT] Y={center_float:g}: building {precision_first}-bit vector",
        flush=True,
    )
    first_vector = build_prime_hat_vector(
        center, precision_bits=precision_first
    )
    actual_nodes = first_vector.vector.float_nodes
    actual_weights = first_vector.vector.float_weights
    print(
        f"[HT-HAT] Y={center_float:g}: FLOAT-SCOUT with "
        f"{len(actual_nodes)} primes",
        flush=True,
    )
    actual_scout = floating_scout(
        actual_nodes, actual_weights, center_float
    )
    print(
        f"[HT-HAT] Y={center_float:g}: {precision_first}-bit Arb cover",
        flush=True,
    )
    first_certificate = continuum_certificate(
        first_vector,
        scout_argmin=actual_scout.refined_argmin,
        dyadic_bits=dyadic_bits,
        max_depth=max_depth,
        max_leaves=max_leaves,
        record_leaves=False,
    )

    print(
        f"[HT-HAT] Y={center_float:g}: same-code "
        f"{precision_repeat}-bit stability recomputation",
        flush=True,
    )
    repeat_vector = build_prime_hat_vector(
        center, precision_bits=precision_repeat
    )
    if repeat_vector.primes != first_vector.primes:
        raise ArithmeticError("prime mask changed under precision doubling")
    repeat_certificate = continuum_certificate(
        repeat_vector,
        scout_argmin=actual_scout.refined_argmin,
        dyadic_bits=dyadic_bits,
        max_depth=max_depth,
        max_leaves=max_leaves,
        record_leaves=True,
    )
    if (
        first_certificate.status == repeat_certificate.status
        and repeat_certificate.status in {"PASS", "FAIL"}
    ):
        final_status = repeat_certificate.status
        precision_stable = True
    else:
        final_status = "INCONCLUSIVE"
        precision_stable = False

    certificate_name = (
        f"HT-HAT-Y-{center.numerator}-OVER-{center.denominator}-ARB-256.json"
    )
    certificate_path = certificate_directory / certificate_name
    certificate_sha256 = write_json(
        certificate_path,
        _certificate_payload(
            preregistration_sha256,
            source_sha256,
            repeat_vector,
            repeat_certificate,
        ),
    )
    replay_check = verify_certificate_file(certificate_path)
    if (
        repeat_certificate.status in {"PASS", "FAIL"}
        and not replay_check["verified"]
    ):
        raise ArithmeticError("from-disk certificate replay failed")

    print(
        f"[HT-HAT] Y={center_float:g}: running 10 matched FLOAT-SCOUT controls",
        flush=True,
    )
    controls = run_controls(
        actual_nodes, actual_weights, actual_scout, center_float
    )
    half_grid = controls[0]
    half_grid_sanity = (
        float(half_grid["maximum_interior_antipode_error"]) <= 1e-8
    )
    if not half_grid_sanity:
        raise ArithmeticError("the preregistered half-grid control failed sanity")

    first_fingerprints = prime_vector_fingerprints(first_vector)
    repeat_fingerprints = prime_vector_fingerprints(repeat_vector)
    exact_fingerprint_stable = (
        first_fingerprints["exact_input_sha256"]
        == repeat_fingerprints["exact_input_sha256"]
    )
    result = {
        "center": {
            "numerator": center.numerator,
            "denominator": center.denominator,
            "decimal": center_float,
        },
        "actual": {
            "vector": prime_vector_payload(first_vector),
            "scout": asdict(actual_scout),
            "certificate_first": certificate_summary(first_certificate),
            "certificate_repeat": certificate_summary(repeat_certificate),
            "final_finite_status": final_status,
            "precision_stable": precision_stable,
            "exact_fingerprint_stable": exact_fingerprint_stable,
            "certificate_file": str(certificate_path),
            "certificate_file_sha256": certificate_sha256,
            "from_disk_replay": replay_check,
        },
        "controls": controls,
        "control_sanity": {
            "half_grid_antipode_detected": half_grid_sanity,
            "half_grid_float_violates_target": (
                float(half_grid["value_at_band_right"])
                < actual_scout.target_floor
            ),
        },
    }
    print(
        f"[HT-HAT] Y={center_float:g}: {final_status}; "
        f"min={actual_scout.refined_minimum:.9g}, "
        f"ratio={actual_scout.target_ratio:.4g}",
        flush=True,
    )
    return result


def _aggregate_results(scales: list[dict[str, object]]) -> dict[str, object]:
    centers: list[float] = []
    depths: list[float] = []
    statuses: list[str] = []
    scale_summaries: list[dict[str, object]] = []
    for scale in scales:
        center = float(scale["center"]["decimal"])
        actual = scale["actual"]
        scout = actual["scout"]
        controls = scale["controls"]
        jitter_ratios = [
            float(control["scout"]["target_ratio"])
            for control in controls
            if control["specification"]["kind"] == "jitter"
        ]
        centers.append(center)
        depths.append(float(scout["negative_depth"]))
        statuses.append(str(actual["final_finite_status"]))
        scale_summaries.append(
            {
                "center": center,
                "finite_status": actual["final_finite_status"],
                "actual_minimum": scout["refined_minimum"],
                "actual_target_ratio": scout["target_ratio"],
                "half_grid_minimum": controls[0]["scout"]["refined_minimum"],
                "half_grid_target_ratio": controls[0]["scout"]["target_ratio"],
                "jitter_target_ratio_minimum": min(jitter_ratios),
                "jitter_target_ratio_median": float(np.median(jitter_ratios)),
                "jitter_target_ratio_maximum": max(jitter_ratios),
            }
        )
    empirical_exponents = [
        (
            -math.log(depth) / math.log(center)
            if depth > 0
            else math.inf
        )
        for center, depth in zip(centers, depths)
    ]
    consecutive_slopes: list[float | None] = []
    for index in range(1, len(centers)):
        if depths[index] > 0 and depths[index - 1] > 0:
            consecutive_slopes.append(
                -math.log(depths[index] / depths[index - 1])
                / math.log(centers[index] / centers[index - 1])
            )
        else:
            consecutive_slopes.append(None)
    return {
        "all_four_finite_pass": all(status == "PASS" for status in statuses),
        "status_counts": {
            status: statuses.count(status)
            for status in ("PASS", "FAIL", "INCONCLUSIVE")
        },
        "scale_summaries": scale_summaries,
        "pointwise_empirical_exponents": empirical_exponents,
        "consecutive_depth_slopes": consecutive_slopes,
        "logical_ceiling": (
            "Finite fixed-vector evidence only; no asymptotic or strip theorem."
        ),
    }


def run_experiment(
    preregistration_path: Path,
    output_path: Path,
    certificate_directory: Path,
) -> dict[str, object]:
    """Execute exactly the preregistered center ladder."""

    preregistration_bytes = preregistration_path.read_bytes()
    preregistration = json.loads(preregistration_bytes)
    centers = _validated_centers(preregistration)
    preregistration_sha256 = hashlib.sha256(
        preregistration_bytes
    ).hexdigest()
    implementation_sha256 = source_sha256()
    payload: dict[str, object] = {
        "schema": "zeta23.ht_hat.finite_diagnostic.v1",
        "experiment_id": "HT-HAT-PREREG-V1",
        "preregistration_file": str(preregistration_path),
        "preregistration_sha256": preregistration_sha256,
        "source_sha256": implementation_sha256,
        "claim_status_before_run": "OPEN",
        "scales": [],
        "dependencies": {
            "python": sys.version,
            "python_flint": flint.__version__,
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }
    for center in centers:
        scale = run_scale(
            center,
            preregistration_sha256=preregistration_sha256,
            source_sha256=implementation_sha256,
            certificate_directory=certificate_directory,
        )
        payload["scales"].append(scale)
        payload["aggregate"] = _aggregate_results(payload["scales"])
        write_json(output_path, payload)
    payload["aggregate"] = _aggregate_results(payload["scales"])
    payload["claim_status_after_run"] = (
        "OPEN: the run has no eventual-in-Y inference rule"
    )
    write_json(output_path, payload)
    return payload


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--preregistration",
        type=Path,
        default=Path("results/context/zeta23_ht_hat_prereg_v1.json"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/ZETA23-HT-HAT-FINITE-DIAGNOSTIC-2026-08-31.json"
        ),
    )
    parser.add_argument(
        "--certificate-directory",
        type=Path,
        default=Path("results/ht_hat_certificates_2026_08_31"),
    )
    parser.add_argument(
        "--verify-certificate",
        type=Path,
        default=None,
        help="Replay one existing Arb certificate instead of running the ladder.",
    )
    return parser.parse_args()


def main() -> None:
    arguments = _parse_args()
    if arguments.verify_certificate is not None:
        replay = verify_certificate_file(arguments.verify_certificate)
        print(json.dumps(replay, indent=2, sort_keys=True), flush=True)
        if not replay["verified"]:
            raise SystemExit(1)
        return
    payload = run_experiment(
        arguments.preregistration,
        arguments.output,
        arguments.certificate_directory,
    )
    aggregate = payload["aggregate"]
    print(
        "[HT-HAT] complete: "
        + json.dumps(aggregate["status_counts"], sort_keys=True),
        flush=True,
    )


if __name__ == "__main__":
    main()
