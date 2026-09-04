#!/usr/bin/env python3
"""Finite sparse/TV classification for cosine-dilation dictionaries.

For pairwise distinct positive nodes ``u_j`` and distinct nonnegative
frequencies ``k_l``, the determinant

    det(cos(k_l * tau * u_j))

has a nonzero generalized-Vandermonde leading coefficient at ``tau=0``.
This makes every relevant harmonic and augmented minor a nonzero analytic
function of ``tau``.  Away from their discrete zero sets, exact
representations of the all-ones carrier need at least ``M`` atoms.

The remaining statements are finite linear-programming identities.  TV
minimizers and positive-antipode depth maximizers are classified by the
``M``-column bases, with exact dual certificates for optimality, uniqueness,
and near-optimal stability.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from dataclasses import asdict, dataclass
from typing import Iterable, Sequence

import mpmath as mp
import numpy as np
from scipy.linalg import qr
from scipy.optimize import brentq, linprog


def cosine_matrix(
    nodes: Iterable[float], harmonics: Iterable[int], tau: float = 1.0
) -> np.ndarray:
    """Return ``A[j,k] = cos(tau * nodes[j] * harmonics[k])``."""

    u = np.asarray(list(nodes), dtype=float)
    k = np.asarray(list(harmonics), dtype=int)
    if u.ndim != 1 or k.ndim != 1 or len(u) == 0 or len(k) == 0:
        raise ValueError("nodes and harmonics must be nonempty vectors")
    if np.any(u <= 0.0) or len(np.unique(u)) != len(u):
        raise ValueError("nodes must be pairwise distinct and positive")
    if np.any(k <= 0) or len(np.unique(k)) != len(k):
        raise ValueError("harmonics must be pairwise distinct and positive")
    if not math.isfinite(tau):
        raise ValueError("tau must be finite")
    return np.cos(tau * np.outer(u, k))


def cosine_vandermonde_leading_constant(
    nodes: Sequence[float], frequencies: Sequence[int]
) -> float:
    """Leading constant of a square cosine determinant at zero.

    If ``m=len(nodes)=len(frequencies)``, then

    ``det(cos(tau*u_i*k_j)) = C*tau^(m*(m-1)) + O(tau^(m*(m-1)+2))``.

    Frequency zero is allowed here, so this routine also covers augmented
    minors whose first column is the all-ones carrier.
    """

    u = np.asarray(nodes, dtype=float)
    k = np.asarray(frequencies, dtype=int)
    if u.ndim != 1 or k.ndim != 1 or len(u) != len(k) or len(u) == 0:
        raise ValueError("nodes and frequencies must have the same positive size")
    if np.any(u < 0.0) or len(np.unique(u)) != len(u):
        raise ValueError("nodes must be pairwise distinct and nonnegative")
    if np.any(k < 0) or len(np.unique(k)) != len(k):
        raise ValueError("frequencies must be pairwise distinct and nonnegative")

    node_vandermonde = 1.0
    frequency_vandermonde = 1.0
    for left in range(len(u)):
        for right in range(left + 1, len(u)):
            node_vandermonde *= u[right] ** 2 - u[left] ** 2
            frequency_vandermonde *= k[right] ** 2 - k[left] ** 2
    denominator = math.prod(math.factorial(2 * degree) for degree in range(len(u)))
    parity = -1.0 if (len(u) * (len(u) - 1) // 2) % 2 else 1.0
    return parity * node_vandermonde * frequency_vandermonde / denominator


def normalized_cosine_determinant(
    nodes: Sequence[float], frequencies: Sequence[int], tau: float, dps: int = 80
) -> float:
    """High-precision determinant divided by its predicted power of ``tau``."""

    if tau == 0.0:
        raise ValueError("tau must be nonzero")
    if len(nodes) != len(frequencies):
        raise ValueError("a square determinant is required")
    with mp.workdps(dps):
        matrix = mp.matrix(
            [
                [mp.cos(mp.mpf(tau) * mp.mpf(node) * int(freq)) for freq in frequencies]
                for node in nodes
            ]
        )
        exponent = len(nodes) * (len(nodes) - 1)
        return float(mp.det(matrix) / mp.power(mp.mpf(tau), exponent))


@dataclass(frozen=True)
class BasisCandidate:
    support_positions: tuple[int, ...]
    support_harmonics: tuple[int, ...]
    coefficients: tuple[float, ...]
    tv_cost: float
    signed_dual_slack: float
    signed_optimal: bool
    signed_unique: bool
    positive_feasible: bool
    positive_cost: float | None
    positive_depth: float | None
    positive_dual_slack: float | None
    positive_optimal: bool
    positive_unique: bool


@dataclass(frozen=True)
class SparseClassification:
    row_count: int
    dictionary_size: int
    full_spark: bool
    minimum_signed_cost: float
    signed_minimizing_supports: tuple[tuple[int, ...], ...]
    signed_unique: bool
    positive_feasible: bool
    minimum_positive_cost: float | None
    maximum_positive_depth: float | None
    positive_minimizing_supports: tuple[tuple[int, ...], ...]
    positive_unique: bool
    candidates: tuple[BasisCandidate, ...]


def classify_matrix(
    matrix: np.ndarray,
    harmonics: Sequence[int],
    *,
    rank_tolerance: float = 1.0e-11,
    comparison_tolerance: float = 2.0e-9,
) -> SparseClassification:
    """Classify signed-TV and positive-antipode optima by square bases.

    The routine is intended for the full-spark locus certified by the report.
    It nevertheless skips numerically singular bases and records whether all
    bases were nonsingular.
    """

    A = np.asarray(matrix, dtype=float)
    labels = tuple(int(value) for value in harmonics)
    if A.ndim != 2 or A.shape[1] != len(labels) or A.shape[0] == 0:
        raise ValueError("matrix shape and harmonic labels do not match")
    rows, columns = A.shape
    if columns < rows:
        raise ValueError("the dictionary must contain at least as many atoms as rows")
    if len(set(labels)) != len(labels):
        raise ValueError("harmonic labels must be distinct")

    q = np.ones(rows)
    raw: list[dict[str, object]] = []
    total_bases = math.comb(columns, rows)
    for support in itertools.combinations(range(columns), rows):
        basis = A[:, support]
        if abs(float(np.linalg.det(basis))) <= rank_tolerance:
            continue
        coefficients = np.linalg.solve(basis, q)
        complement = tuple(index for index in range(columns) if index not in support)

        signed_dual = np.linalg.solve(basis.T, np.sign(coefficients))
        if complement:
            signed_slack = 1.0 - float(
                np.max(np.abs(A[:, complement].T @ signed_dual))
            )
        else:
            signed_slack = math.inf

        positive = bool(np.all(coefficients < -rank_tolerance))
        positive_cost: float | None = None
        positive_depth: float | None = None
        positive_slack: float | None = None
        if positive:
            positive_cost = float(-np.sum(coefficients))
            positive_depth = 1.0 / positive_cost
            positive_dual = np.linalg.solve(basis.T, -np.ones(rows))
            if complement:
                positive_slack = float(
                    np.min(1.0 + A[:, complement].T @ positive_dual)
                )
            else:
                positive_slack = math.inf

        raw.append(
            {
                "support": support,
                "coefficients": coefficients,
                "tv": float(np.sum(np.abs(coefficients))),
                "signed_slack": signed_slack,
                "positive": positive,
                "positive_cost": positive_cost,
                "positive_depth": positive_depth,
                "positive_slack": positive_slack,
            }
        )

    if not raw:
        raise ValueError("no nonsingular square basis was found")
    signed_cost = min(float(item["tv"]) for item in raw)
    signed_winners = tuple(
        tuple(labels[index] for index in item["support"])  # type: ignore[index]
        for item in raw
        if abs(float(item["tv"]) - signed_cost)
        <= comparison_tolerance * max(1.0, signed_cost)
    )
    positive_raw = [item for item in raw if bool(item["positive"])]
    positive_cost = (
        min(float(item["positive_cost"]) for item in positive_raw)
        if positive_raw
        else None
    )
    positive_winners: tuple[tuple[int, ...], ...] = ()
    if positive_cost is not None:
        positive_winners = tuple(
            tuple(labels[index] for index in item["support"])  # type: ignore[index]
            for item in positive_raw
            if abs(float(item["positive_cost"]) - positive_cost)
            <= comparison_tolerance * max(1.0, positive_cost)
        )

    candidates: list[BasisCandidate] = []
    for item in raw:
        support = tuple(int(value) for value in item["support"])  # type: ignore[arg-type]
        is_signed_winner = (
            abs(float(item["tv"]) - signed_cost)
            <= comparison_tolerance * max(1.0, signed_cost)
        )
        is_positive_winner = bool(item["positive"]) and positive_cost is not None and (
            abs(float(item["positive_cost"]) - positive_cost)
            <= comparison_tolerance * max(1.0, positive_cost)
        )
        signed_slack = float(item["signed_slack"])
        positive_slack = (
            float(item["positive_slack"])
            if item["positive_slack"] is not None
            else None
        )
        candidates.append(
            BasisCandidate(
                support_positions=support,
                support_harmonics=tuple(labels[index] for index in support),
                coefficients=tuple(
                    float(value) for value in item["coefficients"]  # type: ignore[union-attr]
                ),
                tv_cost=float(item["tv"]),
                signed_dual_slack=signed_slack,
                signed_optimal=is_signed_winner,
                signed_unique=is_signed_winner
                and len(signed_winners) == 1
                and signed_slack > rank_tolerance,
                positive_feasible=bool(item["positive"]),
                positive_cost=(
                    float(item["positive_cost"])
                    if item["positive_cost"] is not None
                    else None
                ),
                positive_depth=(
                    float(item["positive_depth"])
                    if item["positive_depth"] is not None
                    else None
                ),
                positive_dual_slack=positive_slack,
                positive_optimal=is_positive_winner,
                positive_unique=is_positive_winner
                and len(positive_winners) == 1
                and positive_slack is not None
                and positive_slack > rank_tolerance,
            )
        )

    return SparseClassification(
        row_count=rows,
        dictionary_size=columns,
        full_spark=len(raw) == total_bases,
        minimum_signed_cost=signed_cost,
        signed_minimizing_supports=signed_winners,
        signed_unique=len(signed_winners) == 1,
        positive_feasible=positive_cost is not None,
        minimum_positive_cost=positive_cost,
        maximum_positive_depth=(1.0 / positive_cost if positive_cost else None),
        positive_minimizing_supports=positive_winners,
        positive_unique=len(positive_winners) == 1,
        candidates=tuple(candidates),
    )


def classify_cosine_dictionary(
    nodes: Iterable[float], harmonics: Iterable[int], tau: float
) -> SparseClassification:
    """Convenience wrapper for a cosine-dilation dictionary."""

    u = tuple(float(value) for value in nodes)
    k = tuple(int(value) for value in harmonics)
    return classify_matrix(cosine_matrix(u, k, tau), k)


def positive_depth_minimax(matrix: np.ndarray) -> float:
    """Replay ``min_{y.q=-1} max_k y.a_k`` by linear programming.

    When the positive antipode is feasible, this value equals its maximum
    depth.  The signs in this formulation are deliberately exposed because a
    reversed normalization computes the wrong radial side of the polytope.
    """

    A = np.asarray(matrix, dtype=float)
    if A.ndim != 2 or A.shape[0] == 0 or A.shape[1] == 0:
        raise ValueError("matrix must be nonempty")
    rows, columns = A.shape
    objective = np.zeros(rows + 1)
    objective[-1] = 1.0
    inequalities = np.column_stack([A.T, -np.ones(columns)])
    equality = np.zeros((1, rows + 1))
    equality[0, :rows] = 1.0
    result = linprog(
        objective,
        A_ub=inequalities,
        b_ub=np.zeros(columns),
        A_eq=equality,
        b_eq=np.asarray([-1.0]),
        bounds=[(None, None)] * (rows + 1),
        method="highs",
    )
    if not result.success:
        raise ValueError(f"positive-depth minimax was not finite: {result.message}")
    return float(result.fun)


@dataclass(frozen=True)
class NearOptimalStability:
    objective_excess: float
    dual_slack: float
    inverse_infinity_norm: float
    off_support_l1_upper: float
    total_l1_distance_upper: float


def near_optimal_stability_bound(
    objective_excess: float,
    dual_slack: float,
    inverse_infinity_norm: float,
    support_size: int,
) -> NearOptimalStability:
    """Sharp dual-slack concentration plus a basis-inverse error bound."""

    if objective_excess < 0.0 or dual_slack <= 0.0:
        raise ValueError("excess must be nonnegative and dual slack positive")
    if inverse_infinity_norm <= 0.0 or support_size <= 0:
        raise ValueError("inverse norm and support size must be positive")
    off = objective_excess / dual_slack
    return NearOptimalStability(
        objective_excess=objective_excess,
        dual_slack=dual_slack,
        inverse_infinity_norm=inverse_infinity_norm,
        off_support_l1_upper=off,
        total_l1_distance_upper=(1.0 + support_size * inverse_infinity_norm) * off,
    )


@dataclass(frozen=True)
class BasisPerturbationLedger:
    phase_radius: float
    entrywise_matrix_perturbation: float
    basis_infinity_perturbation: float
    neumann_product: float
    coefficient_infinity_shift_upper: float
    candidate_cost_shift_upper: float


def basis_perturbation_ledger(
    phase_radius: float,
    top_harmonic: int,
    support_size: int,
    maximum_inverse_infinity_norm: float,
    maximum_coefficient_infinity_norm: float,
) -> BasisPerturbationLedger:
    """Uniform Cramer-candidate perturbation bound for a phase box.

    The returned coefficient and cost bounds are certified when the displayed
    ``neumann_product`` is at most ``1/2``.
    """

    if phase_radius < 0.0 or top_harmonic <= 0 or support_size <= 0:
        raise ValueError("phase radius must be nonnegative and sizes positive")
    if maximum_inverse_infinity_norm <= 0.0:
        raise ValueError("the inverse norm must be positive")
    if maximum_coefficient_infinity_norm < 0.0:
        raise ValueError("the coefficient norm must be nonnegative")
    entrywise = top_harmonic * phase_radius
    basis_perturbation = support_size * entrywise
    neumann = maximum_inverse_infinity_norm * basis_perturbation
    coefficient_shift = (
        2.0
        * maximum_inverse_infinity_norm
        * basis_perturbation
        * maximum_coefficient_infinity_norm
    )
    return BasisPerturbationLedger(
        phase_radius=phase_radius,
        entrywise_matrix_perturbation=entrywise,
        basis_infinity_perturbation=basis_perturbation,
        neumann_product=neumann,
        coefficient_infinity_shift_upper=coefficient_shift,
        candidate_cost_shift_upper=support_size * coefficient_shift,
    )


@dataclass(frozen=True)
class ExtremalChamberCertificate:
    node_count: int
    harmonics: tuple[int, ...]
    phases: tuple[float, ...]
    epsilon: float
    expected_coefficients: tuple[float, ...]
    solved_coefficients: tuple[float, ...]
    cost: float
    depth: float
    minimum_weight: float
    determinant: float
    residual: float


def all_remote_extremal_chamber(
    node_count: int, constant: float = 0.05
) -> ExtremalChamberCertificate:
    """Construct the uniform full-support chamber on ``{M,...,2M-1}``.

    This numerically replays the exact construction proved in the report:

    ``1/2 + (constant/M) sum_{k=M}^{2M-2} cos(k theta)
           + cos((2M-1) theta)``.
    """

    if node_count < 2:
        raise ValueError("node_count must be at least two")
    threshold = (math.sqrt(2.0) - 1.0) / 2.0
    if not 0.0 < constant < threshold:
        raise ValueError("constant is outside the certified bracket margin")
    top = 2 * node_count - 1
    harmonics = np.arange(node_count, top + 1, dtype=int)
    epsilon = constant / node_count
    alpha = math.acos(-0.5)
    base_roots: list[float] = []
    for turn in range(-top - 2, top + 3):
        for numerator in (alpha + 2.0 * math.pi * turn, -alpha + 2.0 * math.pi * turn):
            if 0.0 < numerator < top * math.pi:
                base_roots.append(numerator / top)
    centers = np.asarray(sorted(base_roots), dtype=float)
    if len(centers) != top:
        raise ArithmeticError("base-root enumeration failed")

    def polynomial(theta: float) -> float:
        return 0.5 + epsilon * sum(
            math.cos(int(index) * theta) for index in harmonics[:-1]
        ) + math.cos(top * theta)

    radius = math.pi / (12.0 * top)
    roots: list[float] = []
    for center in centers:
        left, right = center - radius, center + radius
        if polynomial(left) * polynomial(right) >= 0.0:
            raise ArithmeticError("a uniform root bracket was lost")
        roots.append(brentq(polynomial, left, right, xtol=1.0e-14))
    root_matrix = np.cos(np.outer(np.asarray(roots), harmonics))
    if np.linalg.matrix_rank(root_matrix) != node_count:
        raise ArithmeticError("the root-by-harmonic matrix lost full column rank")
    _, _, pivots = qr(root_matrix.T, pivoting=True, mode="economic")
    selected = np.sort(np.asarray(pivots[:node_count], dtype=int))
    phases = np.asarray(roots)[selected]
    matrix = np.cos(np.outer(phases, harmonics))
    coefficients = np.linalg.solve(matrix, np.ones(node_count))
    expected = np.full(node_count, -2.0 * epsilon)
    expected[-1] = -2.0
    if not np.allclose(coefficients, expected, rtol=2.0e-9, atol=2.0e-11):
        raise ArithmeticError("the exact extremal coefficients did not replay")
    cost = float(np.sum(-coefficients))
    weights = -coefficients / cost
    return ExtremalChamberCertificate(
        node_count=node_count,
        harmonics=tuple(int(value) for value in harmonics),
        phases=tuple(float(value) for value in phases),
        epsilon=epsilon,
        expected_coefficients=tuple(float(value) for value in expected),
        solved_coefficients=tuple(float(value) for value in coefficients),
        cost=cost,
        depth=1.0 / cost,
        minimum_weight=float(np.min(weights)),
        determinant=float(np.linalg.det(matrix)),
        residual=float(np.max(np.abs(matrix @ coefficients - np.ones(node_count)))),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", type=int, default=4)
    args = parser.parse_args()
    chamber = all_remote_extremal_chamber(args.nodes)
    phase_classification = classify_matrix(
        np.cos(np.outer(chamber.phases, chamber.harmonics)), chamber.harmonics
    )
    print(
        json.dumps(
            {
                "schema": "qp-sparse-tv-classification-v1",
                "verdict": (
                    "outside a discrete dilation set, exact optima are classified "
                    "by full M-atom bases"
                ),
                "chamber": asdict(chamber),
                "classification": asdict(phase_classification),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
