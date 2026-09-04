#!/usr/bin/env python3
"""Finite certificates for the sparse positive-cosine antipode theorem.

The mathematical theorem is proved in the accompanying report.  This module
replays its finite root-cell, rank, barycentric, and consecutive-Chebyshev
identities.  Numerical output is diagnostic; the proof itself uses exact sign
inequalities and polynomial degree.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import math
from typing import Iterable

import numpy as np
from numpy.polynomial import Chebyshev, Polynomial
from scipy.linalg import qr
from scipy.optimize import brentq


@dataclass(frozen=True)
class AntipodeCertificate:
    harmonics: tuple[int, ...]
    phases: tuple[float, ...]
    weights: tuple[float, ...]
    depth: float
    top_weight_margin: float
    maximum_vector_residual: float
    evaluation_determinant: float
    minimum_root_cell_margin: float


def validate_harmonics(harmonics: Iterable[int]) -> tuple[int, ...]:
    """Return a strictly increasing nonempty positive harmonic set."""
    values = tuple(int(value) for value in harmonics)
    if not values or any(value <= 0 for value in values):
        raise ValueError("harmonics must be nonempty and positive")
    if tuple(sorted(set(values))) != values:
        raise ValueError("harmonics must be strictly increasing")
    return values


def dominant_top_weights(
    harmonics: Iterable[int], depth: float, top_weight: float | None = None
) -> np.ndarray:
    """Choose positive weights with ``2*w_D-1 > depth``.

    The default ``w_D=(3+depth)/4`` lies strictly between
    ``(1+depth)/2`` and one.  The remaining mass is spread uniformly.
    """
    values = validate_harmonics(harmonics)
    if not 0.0 < depth < 1.0:
        raise ValueError("depth must lie in (0,1)")
    if len(values) == 1:
        return np.ones(1)
    if top_weight is None:
        top_weight = (3.0 + depth) / 4.0
    if not (1.0 + depth) / 2.0 < top_weight < 1.0:
        raise ValueError("top weight must exceed (1+depth)/2 and be below one")
    weights = np.full(len(values), (1.0 - top_weight) / (len(values) - 1))
    weights[-1] = top_weight
    return weights


def cosine_polynomial(
    theta: float, harmonics: np.ndarray, weights: np.ndarray, depth: float
) -> float:
    return depth + float(np.dot(weights, np.cos(harmonics * theta)))


def palindromic_coefficients(
    harmonics: Iterable[int], weights: np.ndarray, depth: float
) -> np.ndarray:
    """Return coefficients of the normalized polynomial in Corollary 3.3.

    Coefficients are in increasing power order.  On the unit circle,

    ``P(exp(i*theta)) = (2/w_D) exp(i*D*theta) G(theta)``.
    """
    values = validate_harmonics(harmonics)
    masses = np.asarray(weights, dtype=float)
    if masses.shape != (len(values),) or np.any(masses <= 0.0):
        raise ValueError("weights must be positive on the harmonic support")
    if not math.isclose(float(np.sum(masses)), 1.0, abs_tol=1e-12):
        raise ValueError("weights must sum to one")
    if not 0.0 < depth < 2.0 * masses[-1] - 1.0:
        raise ValueError("dominant-top condition failed")
    degree = values[-1]
    coefficients = np.zeros(2 * degree + 1)
    coefficients[0] = coefficients[-1] = 1.0
    coefficients[degree] = 2.0 * depth / masses[-1]
    for harmonic, mass in zip(values[:-1], masses[:-1], strict=True):
        coefficients[degree - harmonic] = mass / masses[-1]
        coefficients[degree + harmonic] = mass / masses[-1]
    return coefficients


def all_root_cells(
    harmonics: Iterable[int], weights: np.ndarray, depth: float
) -> np.ndarray:
    """Isolate the theorem's unique root in every ``j*pi/D`` cell."""
    values = validate_harmonics(harmonics)
    indices = np.asarray(values, dtype=float)
    masses = np.asarray(weights, dtype=float)
    if masses.shape != indices.shape or np.any(masses <= 0.0):
        raise ValueError("weights must be a positive vector on the harmonics")
    if not math.isclose(float(np.sum(masses)), 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("weights must sum to one")
    if not 0.0 < depth < 2.0 * masses[-1] - 1.0:
        raise ValueError("dominant-top condition depth < 2*w_D-1 failed")
    degree = values[-1]
    roots = []
    for cell in range(degree):
        left = cell * math.pi / degree
        right = (cell + 1) * math.pi / degree
        roots.append(
            brentq(
                cosine_polynomial,
                left,
                right,
                args=(indices, masses, depth),
                xtol=1e-14,
                rtol=4.0 * np.finfo(float).eps,
            )
        )
    return np.asarray(roots)


def select_full_rank_phases(roots: np.ndarray, harmonics: Iterable[int]) -> np.ndarray:
    """Select an invertible row minor from the full root-by-harmonic table."""
    values = validate_harmonics(harmonics)
    matrix = np.cos(np.outer(np.asarray(roots), np.asarray(values)))
    _, _, pivots = qr(matrix.T, pivoting=True, mode="economic")
    chosen = np.sort(pivots[: len(values)])
    selected = np.asarray(roots)[chosen]
    determinant = float(np.linalg.det(np.cos(np.outer(selected, values))))
    if abs(determinant) <= 1e-11:
        raise ArithmeticError("rank-selected cosine minor is numerically singular")
    return selected


def build_antipode_certificate(
    harmonics: Iterable[int], depth: float, top_weight: float | None = None
) -> AntipodeCertificate:
    """Build a finite certificate for a prescribed harmonic support."""
    values = validate_harmonics(harmonics)
    weights = dominant_top_weights(values, depth, top_weight)
    roots = all_root_cells(values, weights, depth)
    phases = select_full_rank_phases(roots, values)
    matrix = np.cos(np.outer(phases, values))
    residual = matrix @ weights + depth * np.ones(len(values))
    degree = values[-1]
    cell_distance = min(
        min(theta - math.floor(theta * degree / math.pi) * math.pi / degree,
            (math.floor(theta * degree / math.pi) + 1) * math.pi / degree - theta)
        for theta in roots
    )
    return AntipodeCertificate(
        harmonics=values,
        phases=tuple(float(value) for value in phases),
        weights=tuple(float(value) for value in weights),
        depth=float(depth),
        top_weight_margin=float(2.0 * weights[-1] - 1.0 - depth),
        maximum_vector_residual=float(np.max(np.abs(residual))),
        evaluation_determinant=float(np.linalg.det(matrix)),
        minimum_root_cell_margin=float(cell_distance),
    )


@dataclass(frozen=True)
class ConsecutiveClassification:
    chebyshev_coefficients: tuple[float, ...]
    feasible_positive_antipode: bool
    strict_positive_antipode: bool
    depth: float | None
    weights: tuple[float, ...] | None
    formula_residual: float | None


def consecutive_chebyshev_classification(phases: Iterable[float]) -> ConsecutiveClassification:
    """Replay the exact nodal-polynomial classification for ``K={1,...,M}``."""
    theta = np.asarray(tuple(phases), dtype=float)
    if theta.ndim != 1 or len(theta) == 0 or np.any(theta <= 0.0) or np.any(theta >= math.pi):
        raise ValueError("phases must be a nonempty vector in (0,pi)")
    nodes = np.cos(theta)
    if len(np.unique(np.round(nodes, 14))) != len(nodes):
        raise ValueError("cosine nodes must be distinct")
    nodal = Polynomial.fromroots(nodes)
    coefficients = nodal.convert(kind=Chebyshev).coef
    if len(coefficients) < len(theta) + 1:
        coefficients = np.pad(coefficients, (0, len(theta) + 1 - len(coefficients)))
    r0 = float(coefficients[0])
    tolerance = 2e-11
    feasible = r0 > tolerance and bool(np.all(coefficients[1:] >= -tolerance))
    strict = r0 > tolerance and bool(np.all(coefficients[1:] > tolerance))
    if not feasible:
        return ConsecutiveClassification(
            tuple(float(value) for value in coefficients), False, False, None, None, None
        )
    positive = np.maximum(coefficients[1:], 0.0)
    total = float(np.sum(positive))
    weights = positive / total
    depth = r0 / total
    matrix = np.cos(np.outer(theta, np.arange(1, len(theta) + 1)))
    residual = float(np.max(np.abs(matrix @ weights + depth)))
    return ConsecutiveClassification(
        tuple(float(value) for value in coefficients),
        True,
        strict,
        float(depth),
        tuple(float(value) for value in weights),
        residual,
    )


def main() -> None:
    certificate = build_antipode_certificate((11, 14, 20, 23), depth=0.5)
    classification = consecutive_chebyshev_classification(
        build_antipode_certificate((1, 2, 3, 4), depth=0.5).phases
    )
    print(
        json.dumps(
            {
                "status": "PASS",
                "arbitrary_sparse_support": asdict(certificate),
                "consecutive_classification": asdict(classification),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
