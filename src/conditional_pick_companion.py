"""Prime-independent companions from an anchored conditional-Pick law.

The exact theorem is documented in
``results/ZETA23-PRIME-INDEPENDENT-CONDITIONAL-PICK-COMPANION-2026-08-12.md``.
This module contains only its finite-dimensional linear algebra.  It makes
no assertion that the completed zeta matrix satisfies conditional
positivity.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from numpy.typing import NDArray


ComplexVector = NDArray[np.complex128]


def _unit(vector: NDArray[np.complexfloating], tolerance: float = 1.0e-12) -> ComplexVector:
    answer = np.asarray(vector, dtype=np.complex128).reshape(-1)
    norm = float(np.linalg.norm(answer))
    if norm <= tolerance:
        raise ValueError("vector has negligible norm")
    return answer / norm


@dataclass(frozen=True)
class AnchoredCompanion:
    """A boundary carrier state lying in a prescribed anchor hyperplane."""

    companion: ComplexVector
    phase: complex
    boundary_state: ComplexVector
    theta_star: float
    anchor_residual: float


def theta_star(carrier: NDArray[np.complexfloating], anchor: NDArray[np.complexfloating]) -> float:
    """Largest carrier fraction reachable while nulling one known anchor."""

    a = _unit(carrier)
    g = _unit(anchor)
    if a.shape != g.shape:
        raise ValueError("carrier and anchor dimensions differ")
    value = 1.0 - abs(np.vdot(a, g)) ** 2
    return min(1.0, max(0.0, float(value.real)))


def _orthogonal_unit(
    dimension: int,
    columns: list[ComplexVector],
    tolerance: float,
) -> ComplexVector:
    """Choose a deterministic coordinate direction orthogonal to columns."""

    for index in range(dimension):
        candidate = np.zeros(dimension, dtype=np.complex128)
        candidate[index] = 1.0
        for column in columns:
            candidate -= column * np.vdot(column, candidate)
        norm = float(np.linalg.norm(candidate))
        if norm > tolerance:
            return candidate / norm
    raise ValueError("no orthogonal direction is available")


def anchored_companion(
    carrier: NDArray[np.complexfloating],
    anchor: NDArray[np.complexfloating],
    theta: float,
    *,
    tie_breaker: NDArray[np.complexfloating] | None = None,
    tolerance: float = 1.0e-12,
) -> AnchoredCompanion:
    """Construct ``w`` and a phase with ``sqrt(theta)a+phase*...*w ⟂ g``.

    In dimension at least three this works for every ``theta<=theta_star``.
    At ``theta=1`` it works exactly when the carrier already nulls the
    anchor.  A supplied ``tie_breaker`` (normally the confluent target-depth
    row) makes the remaining choice coordinate-free.  The construction
    depends on geometry only, not on an arithmetic operator.
    """

    if not 0.0 < theta <= 1.0:
        raise ValueError("theta must lie in (0,1]")
    a = _unit(carrier, tolerance)
    g = _unit(anchor, tolerance)
    if a.shape != g.shape:
        raise ValueError("carrier and anchor dimensions differ")

    overlap = np.vdot(a, g)
    perpendicular = g - a * overlap
    beta = float(np.linalg.norm(perpendicular))
    maximum = min(1.0, max(0.0, beta * beta))
    if theta > maximum + 20.0 * tolerance:
        raise ValueError("theta exceeds the one-anchor geometric threshold")

    if theta == 1.0:
        if abs(np.vdot(g, a)) > 20.0 * tolerance:
            raise ValueError("full carrier does not null the anchor")
        w = _orthogonal_unit(a.size, [a, g], tolerance)
        state = a.copy()
        return AnchoredCompanion(
            companion=w,
            phase=1.0 + 0.0j,
            boundary_state=state,
            theta_star=maximum,
            anchor_residual=float(abs(np.vdot(g, state))),
        )

    if beta <= tolerance:
        raise ValueError("anchor is parallel to the carrier")
    u = perpendicular / beta
    required = math.sqrt(theta / (1.0 - theta)) * abs(np.vdot(g, a))
    coefficient = min(1.0, max(0.0, required / beta))

    if coefficient < 1.0 - 20.0 * tolerance:
        if tie_breaker is None:
            v = _orthogonal_unit(a.size, [a, u], tolerance)
        else:
            v = np.asarray(tie_breaker, dtype=np.complex128).reshape(-1)
            if v.shape != a.shape:
                raise ValueError("tie-breaker dimension differs")
            v = v - a * np.vdot(a, v) - u * np.vdot(u, v)
            v = _unit(v, tolerance)
        w = coefficient * u + math.sqrt(1.0 - coefficient**2) * v
    else:
        w = u.copy()
    w = _unit(w, tolerance)

    anchor_a = np.vdot(g, a)
    anchor_w = np.vdot(g, w)
    if abs(anchor_a) <= tolerance:
        phase = 1.0 + 0.0j
    else:
        phase = (
            -math.sqrt(theta) * anchor_a
            / (math.sqrt(1.0 - theta) * anchor_w)
        )
        phase /= abs(phase)

    state = math.sqrt(theta) * a + phase * math.sqrt(1.0 - theta) * w
    return AnchoredCompanion(
        companion=w,
        phase=complex(phase),
        boundary_state=state,
        theta_star=maximum,
        anchor_residual=float(abs(np.vdot(g, state))),
    )


def phase_optimized_boundary(
    matrix: NDArray[np.complexfloating],
    carrier: NDArray[np.complexfloating],
    companion: NDArray[np.complexfloating],
    theta: float,
) -> float:
    """Return the joint orientation expression for one carrier plane."""

    operator = np.asarray(matrix, dtype=np.complex128)
    a = _unit(carrier)
    w = _unit(companion)
    if operator.shape != (a.size, a.size) or w.shape != a.shape:
        raise ValueError("incompatible dimensions")
    if np.linalg.norm(operator - operator.conj().T, ord=2) > 1.0e-10:
        raise ValueError("matrix must be Hermitian")
    r = float(np.vdot(a, operator @ a).real)
    d = float(np.vdot(w, operator @ w).real)
    c = float(abs(np.vdot(w, operator @ a)))
    return float(
        theta * r
        + (1.0 - theta) * d
        + 2.0 * math.sqrt(theta * (1.0 - theta)) * c
    )
