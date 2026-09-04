#!/usr/bin/env python3
"""Exact finite algebra for the QP first-return dual audit.

The accompanying report separates three facts which are easy to conflate.

* Promotion is calibrated by the shallow carrier exponent ``kappa_min``;
  an architecture-wide dual kill must beat the deeper ``kappa_max``.
* A finite set of exceptional packets can be corrected exactly by a
  projected Gram solve, but propagation away from those packets costs an
  independent Schur/leverage bound.
* Rational independence, excellent mesh, and incommensurate remote atoms do
  not imply a dual kill.  A strict positive chamber survives independent
  perturbations of both its nodes and its atom frequencies.

The numerical routines replay finite identities.  The asymptotic and Baire
arguments are proved in the report; floating output is not used in place of
them.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import json
import math
from typing import Iterable

import numpy as np

from sparse_cosine_antipode_classification import build_antipode_certificate


ALPHA_MIN = 0.49
D_SCALE = 0.66
BELLOTTI_WONG_A = 0.10076
FULL_APERTURE_EXPONENT = Fraction(50, 33)
LOW_FREQUENCY_EXPONENT = Fraction(1, 100)
UNIFORM_KILL_EXPONENT = Fraction(19, 1000)
RECALIBRATED_BETA = Fraction(19, 125)
RECALIBRATED_THETA = Fraction(161, 1000)


def carrier_loss_exponent(
    alpha: float, d_scale: float = D_SCALE, discrepancy: float = BELLOTTI_WONG_A
) -> float:
    """Return the audited carrier loss ``kappa(alpha,d)`` in Y-units."""

    if not 0.0 < alpha <= 0.5:
        raise ValueError("alpha must lie in (0,1/2]")
    if not 0.5 < d_scale <= 2.0 / 3.0:
        raise ValueError("d_scale must lie in (1/2,2/3]; the endpoint is the supremal limit")
    y = math.pi * discrepancy / (alpha * (2.0 * d_scale - 1.0))
    response = (y * math.log1p(y ** -2) + 2.0 * math.atan(y)) / math.pi
    return alpha * (d_scale - 0.5) * (1.0 - response) / d_scale


@dataclass(frozen=True)
class ExponentLedger:
    alpha_min: float
    d_scale: float
    kappa_min: float
    kappa_max: float
    proposed_kill: float
    proposed_margin_over_kappa_max: float
    beta: str
    theta: str
    long_gap_saving: str
    short_collar_saving: str
    inverse_image_saving: str
    long_gap_margin: str
    short_collar_margin: str
    inverse_image_margin: str
    ap_step_exponent: str
    ap_shadow_relative_exponent_at_kappa_min: float


def exponent_ledger() -> ExponentLedger:
    """Replay the min/max polarity and a rational full-kill calibration."""

    kappa_min = carrier_loss_exponent(ALPHA_MIN)
    kappa_max = carrier_loss_exponent(0.5)
    beta = RECALIBRATED_BETA
    theta = RECALIBRATED_THETA
    target = UNIFORM_KILL_EXPONENT
    long_gap = (45 * theta - 6) / 65
    short_collar = 2 - FULL_APERTURE_EXPONENT - 2 * beta - theta
    inverse_image = 1 - FULL_APERTURE_EXPONENT / 2 - beta
    step = FULL_APERTURE_EXPONENT - 1
    return ExponentLedger(
        alpha_min=ALPHA_MIN,
        d_scale=D_SCALE,
        kappa_min=kappa_min,
        kappa_max=kappa_max,
        proposed_kill=float(target),
        proposed_margin_over_kappa_max=float(target) - kappa_max,
        beta=str(beta),
        theta=str(theta),
        long_gap_saving=str(long_gap),
        short_collar_saving=str(short_collar),
        inverse_image_saving=str(inverse_image),
        long_gap_margin=str(long_gap - target),
        short_collar_margin=str(short_collar - target),
        inverse_image_margin=str(inverse_image - target),
        ap_step_exponent=str(step),
        ap_shadow_relative_exponent_at_kappa_min=2.0 * kappa_min - float(step),
    )


def cosine_atoms(nodes: Iterable[float], frequencies: Iterable[float]) -> np.ndarray:
    """Return the node-by-frequency real cosine dictionary."""

    u = np.asarray(tuple(nodes), dtype=float)
    t = np.asarray(tuple(frequencies), dtype=float)
    if u.ndim != 1 or t.ndim != 1 or len(u) == 0 or len(t) == 0:
        raise ValueError("nodes and frequencies must be nonempty vectors")
    return np.cos(np.outer(u, t))


def solve_positive_antipode(
    nodes: Iterable[float], frequencies: Iterable[float]
) -> tuple[np.ndarray, float, float, float]:
    """Solve ``A w + r*1=0, 1^T w=1`` on a square support."""

    matrix = cosine_atoms(nodes, frequencies)
    rows, columns = matrix.shape
    if rows != columns:
        raise ValueError("the replay solver expects a square support")
    augmented = np.zeros((rows + 1, rows + 1), dtype=float)
    augmented[:rows, :columns] = matrix
    augmented[:rows, columns] = 1.0
    augmented[rows, :columns] = 1.0
    target = np.zeros(rows + 1)
    target[-1] = 1.0
    solution = np.linalg.solve(augmented, target)
    residual = float(np.max(np.abs(augmented @ solution - target)))
    return (
        solution[:-1],
        float(solution[-1]),
        residual,
        float(np.linalg.det(augmented)),
    )


def carrier_projection(carrier: Iterable[float]) -> np.ndarray:
    """Orthogonal projection onto the complement of a carrier direction."""

    q = np.asarray(tuple(carrier), dtype=float)
    norm_square = float(q @ q)
    if q.ndim != 1 or norm_square == 0.0:
        raise ValueError("carrier must be a nonzero vector")
    return np.eye(len(q)) - np.outer(q, q) / norm_square


@dataclass(frozen=True)
class GramCorrection:
    corrected_dual: tuple[float, ...]
    correction: tuple[float, ...]
    center_values_before: tuple[float, ...]
    center_values_after: tuple[float, ...]
    target_values: tuple[float, ...]
    carrier_change: float
    gram_smallest_eigenvalue: float
    correction_energy: float
    maximum_center_residual: float


def projected_gram_correction(
    base_dual: Iterable[float],
    center_atoms: np.ndarray,
    target_values: Iterable[float],
    carrier: Iterable[float] | None = None,
) -> GramCorrection:
    """Correct finitely many packet centers without changing carrier mass.

    If ``v_i=P a(t_i)`` and ``G=(v_i.v_j)``, the minimum-norm correction is

    ``delta = V G^{-1} (target - A^T y_0)``.

    What this does away from the centers is *not* controlled here; that is
    the independent leverage/Schur gate exposed by ``projection_leverage``.
    """

    y0 = np.asarray(tuple(base_dual), dtype=float)
    atoms = np.asarray(center_atoms, dtype=float)
    targets = np.asarray(tuple(target_values), dtype=float)
    if atoms.ndim != 2 or atoms.shape[0] != len(y0):
        raise ValueError("center_atoms must have one row per dual coordinate")
    if atoms.shape[1] != len(targets):
        raise ValueError("one target is required per packet center")
    q = np.ones(len(y0)) if carrier is None else np.asarray(tuple(carrier), dtype=float)
    projection = carrier_projection(q)
    projected = projection @ atoms
    gram = projected.T @ projected
    eigenvalues = np.linalg.eigvalsh(gram)
    if float(eigenvalues[0]) <= 1e-12:
        raise ValueError("projected packet Gramian is singular")
    before = atoms.T @ y0
    demand = targets - before
    coefficients = np.linalg.solve(gram, demand)
    correction = projected @ coefficients
    corrected = y0 + correction
    after = atoms.T @ corrected
    return GramCorrection(
        corrected_dual=tuple(float(value) for value in corrected),
        correction=tuple(float(value) for value in correction),
        center_values_before=tuple(float(value) for value in before),
        center_values_after=tuple(float(value) for value in after),
        target_values=tuple(float(value) for value in targets),
        carrier_change=float(q @ correction),
        gram_smallest_eigenvalue=float(eigenvalues[0]),
        correction_energy=float(correction @ correction),
        maximum_center_residual=float(np.max(np.abs(after - targets))),
    )


def projection_leverage(
    center_atoms: np.ndarray,
    query_atoms: np.ndarray,
    carrier: Iterable[float] | None = None,
) -> np.ndarray:
    """Return normalized packet-span projection leverage at query atoms.

    The numerator is ``k(t)^T G^{-1} k(t)`` and the denominator is the
    squared norm of the carrier-projected query atom.  Values near one mean
    that a query atom lies almost in the corrected packet span.  Packet
    counting alone places no useful off-packet upper bound on this array.
    """

    centers = np.asarray(center_atoms, dtype=float)
    queries = np.asarray(query_atoms, dtype=float)
    if centers.ndim != 2 or queries.ndim != 2 or centers.shape[0] != queries.shape[0]:
        raise ValueError("center and query atoms must share their row dimension")
    q = np.ones(centers.shape[0]) if carrier is None else np.asarray(tuple(carrier), dtype=float)
    projection = carrier_projection(q)
    projected_centers = projection @ centers
    projected_queries = projection @ queries
    gram = projected_centers.T @ projected_centers
    cross = projected_centers.T @ projected_queries
    solved = np.linalg.solve(gram, cross)
    numerator = np.sum(cross * solved, axis=0)
    denominator = np.sum(projected_queries * projected_queries, axis=0)
    return np.divide(
        numerator,
        denominator,
        out=np.zeros_like(numerator),
        where=denominator > 0.0,
    )


@dataclass(frozen=True)
class RemoteIncommensurateFixture:
    node_count: int
    harmonic_offset: int
    tau0: float
    base_depth: float
    perturbed_depth: float
    minimum_weight: float
    first_frequency: float
    last_frequency: float
    maximum_node_gap: float
    q_independent_node_form: str
    q_independent_frequency_form: str
    interpolation_residual: float
    augmented_determinant: float


def _first_primes(count: int, start: int = 2) -> list[int]:
    values: list[int] = []
    candidate = max(2, start)
    while len(values) < count:
        prime = True
        for divisor in range(2, int(math.sqrt(candidate)) + 1):
            if candidate % divisor == 0:
                prime = False
                break
        if prime:
            values.append(candidate)
        candidate += 1
    return values


def remote_incommensurate_fixture(
    node_count: int = 5,
    harmonic_offset: int = 7,
    tau0: float = math.pi / 0.2,
    depth: float = 0.5,
) -> RemoteIncommensurateFixture:
    """Replay an all-remote strict chamber after independent perturbations.

    Numerically we approximate each base node by a rational and add
    ``delta*sqrt(p_j)``; mathematically, choosing the rational approximation
    and rational ``delta`` inside the chamber makes the nodes Q-independent.
    At the actual rational width ``w=1/5``, ``tau0=pi/w=5*pi``.
    Frequencies have the form ``tau0*k+eta*sqrt(q_k)`` with rational nonzero
    ``eta`` and distinct squarefree primes.  Transcendence of pi followed by
    multiquadratic independence makes them Q-independent.
    """

    if node_count < 2 or harmonic_offset < 1:
        raise ValueError("node_count must be >=2 and harmonic_offset positive")
    harmonics = tuple(range(harmonic_offset + 1, harmonic_offset + node_count + 1))
    certificate = build_antipode_certificate(harmonics, depth)
    base_nodes = np.asarray(certificate.phases) / tau0
    sorted_base = np.sort(base_nodes)
    base_gap = float(np.min(np.diff(sorted_base)))

    node_primes = _first_primes(node_count, start=2)
    rational_nodes = np.round(base_nodes * 10**10) / 10**10
    node_delta = min(1e-11, base_gap / (1000.0 * math.sqrt(node_primes[-1])))
    nodes = rational_nodes + node_delta * np.sqrt(np.asarray(node_primes, dtype=float))

    atom_primes = _first_primes(node_count, start=101)
    frequency_eta = 1e-8
    frequencies = tau0 * np.asarray(harmonics, dtype=float) + frequency_eta * np.sqrt(
        np.asarray(atom_primes, dtype=float)
    )
    weights, solved_depth, residual, determinant = solve_positive_antipode(
        nodes, frequencies
    )
    if np.min(weights) <= 0.0 or solved_depth <= 0.0:
        raise ArithmeticError("the strict positive chamber was lost")

    ordered = np.sort(nodes)
    gaps = np.diff(np.concatenate(([0.0], ordered, [math.pi / tau0])))
    return RemoteIncommensurateFixture(
        node_count=node_count,
        harmonic_offset=harmonic_offset,
        tau0=tau0,
        base_depth=depth,
        perturbed_depth=float(solved_depth),
        minimum_weight=float(np.min(weights)),
        first_frequency=float(np.min(frequencies)),
        last_frequency=float(np.max(frequencies)),
        maximum_node_gap=float(np.max(gaps)),
        q_independent_node_form="rational_j + rational_delta*sqrt(distinct_prime_j)",
        q_independent_frequency_form="5*pi*k + rational_eta*sqrt(distinct_prime_k)",
        interpolation_residual=residual,
        augmented_determinant=determinant,
    )


def finite_bohr_average(coefficients: Iterable[float], nodes: Iterable[float], horizon: float) -> float:
    """Exact Cesaro average of a finite cosine dual on ``[0,horizon]``."""

    y = np.asarray(tuple(coefficients), dtype=float)
    u = np.asarray(tuple(nodes), dtype=float)
    if y.shape != u.shape or horizon <= 0.0 or np.any(u == 0.0):
        raise ValueError("matching nonzero nodes and a positive horizon are required")
    return float(np.sum(y * np.sin(horizon * u) / (horizon * u)))


def main() -> None:
    nodes = np.asarray([0.11, 0.17, 0.23, 0.31])
    centers = cosine_atoms(nodes, [17.0, 31.0])
    base = -np.ones(len(nodes)) / len(nodes)
    correction = projected_gram_correction(base, centers, [0.0, 0.0])
    payload = {
        "schema": "qp-first-return-dual-v1",
        "status": "PASS",
        "exponents": asdict(exponent_ledger()),
        "gram_correction": asdict(correction),
        "remote_incommensurate_fixture": asdict(remote_incommensurate_fixture()),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
