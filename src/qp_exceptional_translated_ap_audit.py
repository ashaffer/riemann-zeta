#!/usr/bin/env python3
"""Exact ledgers for the exceptional translated-AP promotion audit.

The module separates three logically different facts.

* A zero of the constant Chebyshev coefficient of the nodal product makes
  the square first-harmonic interpolation system inconsistent.  Approaching
  such a zero makes the directional cost diverge at fixed degree.
* Positive coefficients and a full set of real trigonometric roots are
  perfectly compatible.  ``positive_harmonic_template`` constructs such a
  configuration for *any* prescribed set of positive harmonic indices.
* For rationally independent feature frequencies, Kronecker recurrence
  transfers every open positive template chamber to arbitrarily large AP
  steps.  The two-frequency search below is only a numerical illustration of
  that theorem; it is not used as its proof and gives no finite-aperture bound.

Floating calculations certify the displayed finite examples.  The report
contains the exact algebraic and Kronecker arguments and scopes them away from
the still-open ``tau <= B/M`` first-return problem.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from typing import Iterable

import numpy as np
from numpy.polynomial.chebyshev import chebmul, chebroots
from scipy.linalg import qr
from scipy.optimize import brentq


BASE_TEMPLATE_DEPTH = 0.5
FIRST_HARMONIC_SIGN_MARGIN = (math.sqrt(2.0) - 1.0) / 2.0


def nodal_chebyshev_coefficients(roots: Iterable[float]) -> np.ndarray:
    """Chebyshev coefficients of ``product_x (X-x)``."""

    coefficients = np.asarray([1.0])
    for root in np.asarray(list(roots), dtype=float):
        coefficients = chebmul(coefficients, np.asarray([-root, 1.0]))
    return coefficients


def positive_antipode_from_phases(
    phases: Iterable[float], indices: Iterable[int]
) -> tuple[np.ndarray, float, float, float]:
    """Solve the square positive-antipode equations on a harmonic block.

    The unknowns are weights ``w_k`` and depth ``r``:

    ``sum_k w_k cos(k theta_j) + r = 0`` and ``sum_k w_k = 1``.

    The returned tuple is ``(weights, depth, residual, determinant)``.  No
    positivity is imposed by the solver; callers inspect the signs.
    """

    theta = np.asarray(list(phases), dtype=float)
    harmonics = np.asarray(list(indices), dtype=int)
    if theta.ndim != 1 or harmonics.ndim != 1 or len(theta) != len(harmonics):
        raise ValueError("one phase and one harmonic are required per row")
    if len(theta) == 0 or np.any(harmonics <= 0):
        raise ValueError("harmonics must be nonempty and positive")
    if len(np.unique(harmonics)) != len(harmonics):
        raise ValueError("harmonics must be distinct")

    size = len(theta)
    augmented = np.zeros((size + 1, size + 1), dtype=float)
    augmented[:size, :size] = np.cos(np.outer(theta, harmonics))
    augmented[:size, size] = 1.0
    augmented[size, :size] = 1.0
    target = np.zeros(size + 1, dtype=float)
    target[size] = 1.0
    solution = np.linalg.solve(augmented, target)
    residual = float(np.max(np.abs(augmented @ solution - target)))
    return (
        solution[:-1],
        float(solution[-1]),
        residual,
        float(np.linalg.det(augmented)),
    )


def base_cosine_roots(degree: int, depth: float) -> np.ndarray:
    """The ``degree`` roots of ``depth + cos(degree*theta)`` in ``(0,pi)``."""

    if degree < 1:
        raise ValueError("degree must be positive")
    if not 0.0 < depth < 1.0:
        raise ValueError("depth must lie strictly between zero and one")
    alpha = math.acos(-depth)
    phase_roots: list[float] = []
    for turn in range(-degree - 2, degree + 3):
        for numerator in (alpha + 2.0 * math.pi * turn, -alpha + 2.0 * math.pi * turn):
            if 0.0 < numerator < degree * math.pi:
                phase_roots.append(numerator / degree)
    result = np.asarray(sorted(phase_roots), dtype=float)
    if len(result) != degree:
        raise ArithmeticError("base cosine root enumeration failed")
    return result


def _independent_base_rows(
    roots: np.ndarray, lower_harmonics: np.ndarray, row_count: int
) -> np.ndarray:
    """Select a nonsingular evaluation minor by rank-revealing QR."""

    evaluation = np.column_stack(
        [np.ones(len(roots)), np.cos(np.outer(roots, lower_harmonics))]
    )
    if np.linalg.matrix_rank(evaluation) != row_count:
        raise ArithmeticError("the expected lower-harmonic evaluation rank failed")
    _, _, pivots = qr(evaluation.T, pivoting=True, mode="economic")
    return np.sort(np.asarray(pivots[:row_count], dtype=int))


@dataclass(frozen=True)
class HarmonicTemplateCertificate:
    harmonic_indices: list[int]
    top_degree: int
    selected_base_root_indices: list[int]
    epsilon: float
    coefficient_sum: float
    expected_depth: float
    solved_depth: float
    minimum_weight: float
    maximum_weight: float
    interpolation_residual: float
    augmented_determinant: float
    minimum_root: float
    maximum_root: float
    minimum_bracket_margin: float


def positive_harmonic_template(
    indices: Iterable[int], depth: float = BASE_TEMPLATE_DEPTH
) -> HarmonicTemplateCertificate:
    """Construct an interior positive antipode for any harmonic index set.

    Let ``D=max(indices)``.  The base polynomial ``depth+cos(D*theta)`` has
    ``D`` simple roots in ``(0,pi)``.  Evaluation of

    ``1, cos(k*theta), k in indices without D``

    on all those roots has full column rank: a nonzero cosine polynomial of
    degree below ``D`` cannot have ``D`` distinct roots there.  We select a
    nonsingular minor, add a sufficiently small positive coefficient at every
    lower chosen harmonic, and continue the selected roots by bracketing.
    Normalizing the nonconstant coefficients gives the desired probability.
    """

    harmonics = np.asarray(sorted(set(int(value) for value in indices)), dtype=int)
    if len(harmonics) == 0 or np.any(harmonics <= 0):
        raise ValueError("indices must be distinct positive integers")
    row_count = len(harmonics)
    top = int(harmonics[-1])
    lower = harmonics[:-1]
    base_roots = base_cosine_roots(top, depth)
    selected = _independent_base_rows(base_roots, lower, row_count)
    centers = base_roots[selected]

    radii: list[float] = []
    endpoint_margins: list[float] = []
    for root_index, center in zip(selected, centers):
        left_gap = center if root_index == 0 else center - base_roots[root_index - 1]
        right_gap = (
            math.pi - center
            if root_index == top - 1
            else base_roots[root_index + 1] - center
        )
        radius = 0.2 * min(left_gap, right_gap)
        radii.append(radius)
        endpoint_margins.extend(
            [
                abs(depth + math.cos(top * (center - radius))),
                abs(depth + math.cos(top * (center + radius))),
            ]
        )

    minimum_margin = min(endpoint_margins)
    if len(lower):
        epsilon = min(1.0e-4, minimum_margin / (4.0 * len(lower)))
    else:
        epsilon = 0.0

    def polynomial(theta: float) -> float:
        return depth + math.cos(top * theta) + epsilon * sum(
            math.cos(int(index) * theta) for index in lower
        )

    continued_roots: list[float] = []
    for center, radius in zip(centers, radii):
        left = center - radius
        right = center + radius
        if polynomial(left) * polynomial(right) >= 0.0:
            raise ArithmeticError("positive template root lost its sign bracket")
        continued_roots.append(brentq(polynomial, left, right, xtol=1e-14))

    weights, solved_depth, residual, determinant = positive_antipode_from_phases(
        continued_roots, harmonics
    )
    coefficient_sum = 1.0 + len(lower) * epsilon
    expected_weights = np.full(row_count, epsilon / coefficient_sum)
    expected_weights[-1] = 1.0 / coefficient_sum
    expected_depth = depth / coefficient_sum
    if not np.allclose(weights, expected_weights, rtol=2e-9, atol=2e-11):
        raise ArithmeticError("template coefficients did not replay")
    if not math.isclose(solved_depth, expected_depth, rel_tol=2e-9, abs_tol=2e-11):
        raise ArithmeticError("template depth did not replay")

    return HarmonicTemplateCertificate(
        harmonic_indices=[int(value) for value in harmonics],
        top_degree=top,
        selected_base_root_indices=[int(value) for value in selected],
        epsilon=epsilon,
        coefficient_sum=coefficient_sum,
        expected_depth=expected_depth,
        solved_depth=solved_depth,
        minimum_weight=float(np.min(weights)),
        maximum_weight=float(np.max(weights)),
        interpolation_residual=residual,
        augmented_determinant=determinant,
        minimum_root=float(np.min(continued_roots)),
        maximum_root=float(np.max(continued_roots)),
        minimum_bracket_margin=minimum_margin,
    )


def all_remote_uniform_template(
    node_count: int, constant: float = 0.05
) -> HarmonicTemplateCertificate:
    """Uniform ``epsilon=constant/M`` certificate on ``K={M,...,2M-1}``.

    Around every root of ``1/2+cos((2M-1)theta)`` use a bracket of phase
    radius ``pi/(12(2M-1))``.  The base endpoint magnitude is at least
    ``FIRST_HARMONIC_SIGN_MARGIN`` and the whole lower-harmonic perturbation
    is smaller than ``constant``.  Hence all ``2M-1`` simple roots persist
    whenever ``constant`` is below that margin.

    On the full continued root set, the ``K``-evaluation matrix has rank M:
    a supported degree-``2M-1`` cosine polynomial vanishing at every root
    would be proportional to the template, contradicting its missing
    constant coefficient.  A rank-revealing minor therefore yields an open
    positive chamber with fixed depth.
    """

    if node_count < 2:
        raise ValueError("node_count must be at least two")
    if not 0.0 < constant < FIRST_HARMONIC_SIGN_MARGIN:
        raise ValueError("constant must be below the uniform sign margin")
    size = node_count
    harmonics = np.arange(size, 2 * size, dtype=int)
    top = int(harmonics[-1])
    lower = harmonics[:-1]
    epsilon = constant / size
    centers = base_cosine_roots(top, BASE_TEMPLATE_DEPTH)
    radius = math.pi / (12.0 * top)

    def polynomial(theta: float) -> float:
        return BASE_TEMPLATE_DEPTH + math.cos(top * theta) + epsilon * sum(
            math.cos(int(index) * theta) for index in lower
        )

    roots: list[float] = []
    margins: list[float] = []
    for center in centers:
        left = center - radius
        right = center + radius
        base_left = abs(BASE_TEMPLATE_DEPTH + math.cos(top * left))
        base_right = abs(BASE_TEMPLATE_DEPTH + math.cos(top * right))
        margins.extend([base_left, base_right])
        if polynomial(left) * polynomial(right) >= 0.0:
            raise ArithmeticError("uniform all-remote template lost a root bracket")
        roots.append(brentq(polynomial, left, right, xtol=1e-14))

    all_roots = np.asarray(roots)
    evaluation = np.cos(np.outer(all_roots, harmonics))
    if np.linalg.matrix_rank(evaluation) != size:
        raise ArithmeticError("uniform all-remote root evaluation lost rank")
    _, _, pivots = qr(evaluation.T, pivoting=True, mode="economic")
    selected = np.sort(np.asarray(pivots[:size], dtype=int))
    selected_roots = all_roots[selected]
    weights, solved_depth, residual, determinant = positive_antipode_from_phases(
        selected_roots, harmonics
    )

    coefficient_sum = 1.0 + (size - 1) * epsilon
    expected_weights = np.full(size, epsilon / coefficient_sum)
    expected_weights[-1] = 1.0 / coefficient_sum
    expected_depth = BASE_TEMPLATE_DEPTH / coefficient_sum
    if not np.allclose(weights, expected_weights, rtol=2e-9, atol=2e-11):
        raise ArithmeticError("uniform all-remote coefficients did not replay")
    if not math.isclose(solved_depth, expected_depth, rel_tol=2e-9, abs_tol=2e-11):
        raise ArithmeticError("uniform all-remote depth did not replay")

    return HarmonicTemplateCertificate(
        harmonic_indices=[int(value) for value in harmonics],
        top_degree=top,
        selected_base_root_indices=[int(value) for value in selected],
        epsilon=epsilon,
        coefficient_sum=coefficient_sum,
        expected_depth=expected_depth,
        solved_depth=solved_depth,
        minimum_weight=float(np.min(weights)),
        maximum_weight=float(np.max(weights)),
        interpolation_residual=residual,
        augmented_determinant=determinant,
        minimum_root=float(np.min(selected_roots)),
        maximum_root=float(np.max(selected_roots)),
        minimum_bracket_margin=min(margins),
    )


@dataclass(frozen=True)
class FirstHarmonicTemplateCertificate:
    degree: int
    epsilon: float
    perturbation_l1: float
    sign_margin: float
    root_count: int
    maximum_root_imaginary_part: float
    minimum_root: float
    maximum_root: float
    minimum_chebyshev_coefficient: float
    normalized_depth: float
    minimum_probability_weight: float
    nodal_ratio_error: float
    interpolation_residual: float
    augmented_determinant: float


def first_harmonic_template(degree: int) -> FirstHarmonicTemplateCertificate:
    """Explicit all-positive Chebyshev template for ``{1,...,degree}``.

    We use

    ``F(theta)=1/2 + eps*sum_{k<degree} cos(k theta)+cos(degree theta)``,

    with ``eps=(sqrt(2)-1)/(8*degree)``.  Around every root of
    ``1/2+cos(degree theta)`` take a phase bracket of radius
    ``pi/(12*degree)``.  The unperturbed endpoint magnitude is at least
    ``(sqrt(2)-1)/2``, while the perturbation is less than one quarter of
    that amount.  Hence all ``degree`` simple roots persist in ``(0,pi)``.
    """

    if degree < 2:
        raise ValueError("degree must be at least two")
    epsilon = FIRST_HARMONIC_SIGN_MARGIN / (4.0 * degree)
    coefficients = np.full(degree + 1, epsilon, dtype=float)
    coefficients[0] = BASE_TEMPLATE_DEPTH
    coefficients[-1] = 1.0
    roots = chebroots(coefficients)
    max_imaginary = float(np.max(np.abs(roots.imag)))
    real_roots = np.sort(roots.real)
    if max_imaginary > 1e-10 or np.min(real_roots) <= -1.0 or np.max(real_roots) >= 1.0:
        raise ArithmeticError("explicit positive template lost real interior roots")

    phases = np.arccos(real_roots[::-1])
    weights, solved_depth, residual, determinant = positive_antipode_from_phases(
        phases, range(1, degree + 1)
    )
    coefficient_sum = float(np.sum(coefficients[1:]))
    normalized_depth = BASE_TEMPLATE_DEPTH / coefficient_sum

    nodal = nodal_chebyshev_coefficients(real_roots)
    # The monic nodal product is 2^(1-degree) times the template.
    replay = coefficients * (2.0 ** (1 - degree))
    ratio_error = float(np.max(np.abs(nodal - replay)))
    if not math.isclose(solved_depth, normalized_depth, rel_tol=2e-9, abs_tol=2e-11):
        raise ArithmeticError("explicit template depth did not replay")

    return FirstHarmonicTemplateCertificate(
        degree=degree,
        epsilon=epsilon,
        perturbation_l1=(degree - 1) * epsilon,
        sign_margin=FIRST_HARMONIC_SIGN_MARGIN,
        root_count=len(real_roots),
        maximum_root_imaginary_part=max_imaginary,
        minimum_root=float(np.min(real_roots)),
        maximum_root=float(np.max(real_roots)),
        minimum_chebyshev_coefficient=float(np.min(coefficients)),
        normalized_depth=normalized_depth,
        minimum_probability_weight=float(np.min(weights)),
        nodal_ratio_error=ratio_error,
        interpolation_residual=residual,
        augmented_determinant=determinant,
    )


@dataclass(frozen=True)
class SingularR0Certificate:
    delta: float
    roots: list[float]
    r0: float
    r1: float
    r2: float
    directional_cost: float
    positive_depth: float
    singular_matrix_rank: int
    singular_augmented_rank: int
    singular_least_squares_residual: float


def singular_r0_certificate(delta: float) -> SingularR0Certificate:
    """Approach the exact ``r0=0`` obstruction through positive coefficients.

    Put ``a=1/sqrt(2)`` and take roots ``a-delta,-a``.  Then

    ``R(x)=r0*T0+r1*T1+r2*T2`` with
    ``r0=a*delta, r1=delta, r2=1/2``.

    All coefficients are positive for ``delta>0``; nevertheless the AP cost
    diverges and the positive depth tends to zero.  At ``delta=0`` the
    no-constant evaluation matrix cannot represent the all-ones vector.
    """

    if not 0.0 < delta < 0.1:
        raise ValueError("delta must lie in (0,0.1)")
    a = 1.0 / math.sqrt(2.0)
    roots = np.asarray([a - delta, -a])
    coefficients = nodal_chebyshev_coefficients(roots)
    r0, r1, r2 = (float(value) for value in coefficients)
    cost = (abs(r1) + abs(r2)) / abs(r0)
    depth = r0 / (r1 + r2)

    singular_roots = np.asarray([a, -a])
    singular_matrix = np.column_stack(
        [singular_roots, 2.0 * singular_roots**2 - 1.0]
    )
    target = np.ones(2)
    least_squares = np.linalg.lstsq(singular_matrix, target, rcond=None)[0]
    least_residual = float(np.linalg.norm(singular_matrix @ least_squares - target))
    augmented = np.column_stack([singular_matrix, target])

    return SingularR0Certificate(
        delta=delta,
        roots=[float(value) for value in roots],
        r0=r0,
        r1=r1,
        r2=r2,
        directional_cost=cost,
        positive_depth=depth,
        singular_matrix_rank=int(np.linalg.matrix_rank(singular_matrix)),
        singular_augmented_rank=int(np.linalg.matrix_rank(augmented)),
        singular_least_squares_residual=least_residual,
    )


def negative_packet_mass_lower(depth: float) -> float:
    """Mass forced where ``S/M <= -depth/2`` by an antipode of depth ``depth``."""

    if not 0.0 < depth <= 1.0:
        raise ValueError("depth must lie in (0,1]")
    return depth / (2.0 - depth)


def generic_r0_exponential_term_lower(degree: int) -> int:
    """Generic term-count lower bound for ``tau -> r0(tau)``.

    The full product ``prod_j cos(tau*u_j)`` occurs in ``r0``.  If the
    ``u_j`` are rationally independent, its signed subset frequencies are
    distinct, giving at least ``2**degree`` exponential terms before the
    lower elementary-symmetric contributions are added.
    """

    if degree < 1:
        raise ValueError("degree must be positive")
    return 2**degree


@dataclass(frozen=True)
class TwoFrequencyReturnCertificate:
    maximum_turn: int
    best_turn: int
    tau: float
    circular_phase_error: float
    solved_depth: float
    minimum_weight: float
    interpolation_residual: float


def two_frequency_kronecker_return(maximum_turn: int = 20000) -> TwoFrequencyReturnCertificate:
    """Toy recurrence for frequencies ``1,sqrt(2)`` into the M=2 chamber."""

    if maximum_turn < 1:
        raise ValueError("maximum_turn must be positive")
    template = first_harmonic_template(2)
    coefficients = np.asarray(
        [BASE_TEMPLATE_DEPTH, template.epsilon, 1.0], dtype=float
    )
    roots = np.sort(chebroots(coefficients).real)[::-1]
    target = np.arccos(roots)

    best_error = math.inf
    best_turn = 0
    best_tau = float(target[0])
    for turn in range(maximum_turn + 1):
        tau = float(target[0] + 2.0 * math.pi * turn)
        difference = (
            math.sqrt(2.0) * tau - float(target[1]) + math.pi
        ) % (2.0 * math.pi) - math.pi
        error = abs(difference)
        if error < best_error:
            best_error = error
            best_turn = turn
            best_tau = tau

    phases = np.asarray(
        [best_tau % (2.0 * math.pi), (math.sqrt(2.0) * best_tau) % (2.0 * math.pi)]
    )
    weights, depth, residual, _ = positive_antipode_from_phases(phases, [1, 2])
    return TwoFrequencyReturnCertificate(
        maximum_turn=maximum_turn,
        best_turn=best_turn,
        tau=best_tau,
        circular_phase_error=best_error,
        solved_depth=depth,
        minimum_weight=float(np.min(weights)),
        interpolation_residual=residual,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--degrees", nargs="+", type=int, default=[2, 3, 5, 8])
    parser.add_argument("--return-turns", type=int, default=20000)
    args = parser.parse_args()
    payload = {
        "schema": "qp-exceptional-translated-ap-hostile-audit-v1",
        "first_harmonic_templates": [
            asdict(first_harmonic_template(degree)) for degree in args.degrees
        ],
        "translated_harmonic_templates": [
            asdict(all_remote_uniform_template(degree))
            for degree in args.degrees
        ],
        "singular_r0": [
            asdict(singular_r0_certificate(delta)) for delta in (1e-2, 1e-4, 1e-6)
        ],
        "two_frequency_recurrence": asdict(
            two_frequency_kronecker_return(args.return_turns)
        ),
        "scope": (
            "positive determinant chambers recur at unbounded steps, but this "
            "does not put a return below the QP polynomial aperture"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
