"""Weighted Clark-measure checkpoint for finite Suzuki diagnostics.

There are two superficially similar weights in the existing finite Galerkin
experiments, and this module keeps them separate.

For a real root ``lambda`` of a boundary phase, analytic differentiation of
the sampled characteristic gives the *candidate* normalized Clark atom

    p_phase(lambda) = 2 / ((1 + lambda**2) Phi'(lambda)).

It is a genuine spectral probability only after proving that the sampled
phasor is the meromorphic-inner characteristic of the relevant simple
symmetric operator.  That theorem is not available for the completed-Weil
Galerkin compression.

Independently, the compression gives exact finite-dimensional defect vectors

    v_z = T^{-1} P e_z,

and hence the exact squared overlap

    p_defect(lambda)
      = |<v_-i,v_lambda>_T|^2
          / (||v_-i||_T^2 ||v_lambda||_T^2).

This is a legitimate vector-overlap calculation.  It becomes a spectral
measure atom only when the root vectors at a fixed extension phase form an
orthogonal eigenfamily.  The diagnostic tests that necessary condition and
the corresponding Bessel bound ``sum p_defect <= 1``.  A finite compression
can have arbitrarily many characteristic roots but only finitely many vector
directions, so this audit prevents a root proxy from being mislabeled as a
finite self-adjoint spectral measure.

All Fourier and Gram calculations are chunked or root-local.  Completed-Weil
rows remain numerical diagnostics, not continuum claims.
"""

from __future__ import annotations

import argparse
import gc
from dataclasses import dataclass
from typing import Sequence

import numpy as np

from shift_phase_covariance_falsifier import ShiftedCharacteristic
from spectral_margins import spectral_form


DEFAULT_SUPPORTS = (1.0, 1.75, 2.485, 2.996)
DEFAULT_DIMENSIONS = (10, 12)
DEFAULT_PHASES = (0.0, float(np.pi))
DEFAULT_PROBES = (1j, 2j, 10j)


@dataclass(frozen=True)
class WeightedClarkRow:
    model: str
    measure_status: str
    support: float
    dimension: int
    shift: float
    phase: float
    height: float
    root_count: int
    nonpositive_phase_derivative_count: int
    phase_candidate_mass: float
    phase_candidate_effective_atom_count: float
    phase_candidate_largest_atom: float
    defect_overlap_mass: float
    defect_bessel_excess: float
    maximum_distinct_root_coherence: float
    median_phase_to_defect_weight_ratio: float
    maximum_phase_to_defect_weight_ratio: float
    cauchy_at_i: complex
    cauchy_at_2i: complex
    cauchy_at_10i: complex


def analytic_boundary_phase_derivative(
    characteristic: ShiftedCharacteristic,
    real_points: Sequence[float] | np.ndarray,
    chunk_size: int = 512,
) -> np.ndarray:
    """Differentiate ``arg E(x)`` without a finite-difference grid.

    With ``E=-(x-i)I_+(x)/((x+i)I_-(x))``, logarithmic
    differentiation gives

    ``Phi'=Im(1/(x-i)-1/(x+i)+I_+'/I_+-I_-'/I_-)``.
    """

    points = np.asarray(real_points, dtype=float)
    shape = points.shape
    flat = points.reshape(-1)
    plus, minus = characteristic.fourier_integrals(points)
    plus_derivative = np.empty(flat.size, dtype=complex)
    minus_derivative = np.empty(flat.size, dtype=complex)
    for start in range(0, flat.size, chunk_size):
        stop = min(start + chunk_size, flat.size)
        exponentials = np.exp(
            1j * np.outer(flat[start:stop], characteristic.nodes)
        )
        plus_derivative[start:stop] = exponentials @ (
            1j
            * characteristic.nodes
            * characteristic.weighted_v_plus
        )
        minus_derivative[start:stop] = exponentials @ (
            1j
            * characteristic.nodes
            * characteristic.weighted_v_minus
        )
    plus = plus.reshape(-1)
    minus = minus.reshape(-1)
    if np.any(np.abs(plus) < 1e-14) or np.any(np.abs(minus) < 1e-14):
        raise FloatingPointError("phase derivative denominator is too small")
    derivative = np.imag(
        1.0 / (flat - 1j)
        - 1.0 / (flat + 1j)
        + plus_derivative / plus
        - minus_derivative / minus
    )
    return derivative.reshape(shape)


def normalized_clark_candidate_weights(
    real_points: Sequence[float] | np.ndarray,
    phase_derivatives: Sequence[float] | np.ndarray,
) -> np.ndarray:
    """Return ``mu({lambda})/[pi*(1+lambda^2)]``.

    The standard Clark mass is ``mu({lambda})=2*pi/Phi'(lambda)``.
    Nonpositive derivatives are returned as ``nan`` rather than interpreted
    as signed spectral mass.
    """

    points = np.asarray(real_points, dtype=float)
    derivatives = np.asarray(phase_derivatives, dtype=float)
    if points.shape != derivatives.shape:
        raise ValueError("points and derivatives must have the same shape")
    weights = np.full(points.shape, np.nan, dtype=float)
    positive = derivatives > 0.0
    weights[positive] = 2.0 / (
        (1.0 + points[positive] ** 2) * derivatives[positive]
    )
    return weights


def defect_coefficients(
    characteristic: ShiftedCharacteristic,
    spectral_points: Sequence[float] | np.ndarray,
    chunk_size: int = 512,
) -> np.ndarray:
    """Return columns of ``T^{-1} P exp(-i lambda x)`` at real points."""

    points = np.asarray(spectral_points, dtype=float).reshape(-1)
    right_sides = np.empty(
        (characteristic.dimension, points.size), dtype=complex
    )
    for start in range(0, points.size, chunk_size):
        stop = min(start + chunk_size, points.size)
        exponentials = np.exp(
            -1j * np.outer(characteristic.nodes, points[start:stop])
        )
        right_sides[:, start:stop] = characteristic.basis.conj().T @ (
            characteristic.weights[:, None] * exponentials
        )
    shifted_metric = (
        characteristic.metric
        - characteristic.shift * np.eye(characteristic.dimension)
    )
    return np.linalg.solve(shifted_metric, right_sides)


def defect_overlap_data(
    characteristic: ShiftedCharacteristic,
    spectral_points: Sequence[float] | np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Return exact Galerkin overlap weights and normalized root Gram matrix."""

    vectors = defect_coefficients(characteristic, spectral_points)
    shifted_metric = (
        characteristic.metric
        - characteristic.shift * np.eye(characteristic.dimension)
    )
    gram = vectors.conj().T @ shifted_metric @ vectors
    diagonal = np.real(np.diag(gram))
    if np.any(diagonal <= 0.0):
        raise FloatingPointError("defect Gram diagonal is not positive")
    norms = np.sqrt(diagonal)
    normalized_gram = gram / (norms[:, None] * norms[None, :])

    reference = characteristic.v_minus_coefficients
    reference_norm_sq = float(
        np.real(np.vdot(reference, shifted_metric @ reference))
    )
    if reference_norm_sq <= 0.0:
        raise FloatingPointError("reference defect norm is not positive")
    cross = reference.conj() @ (shifted_metric @ vectors)
    weights = np.abs(cross) ** 2 / (reference_norm_sq * diagonal)
    return np.asarray(weights, dtype=float), normalized_gram


def weighted_cauchy_transform(
    points: Sequence[float] | np.ndarray,
    weights: Sequence[float] | np.ndarray,
    probe: complex,
) -> complex:
    """Cauchy transform of a finite positive atomic measure."""

    locations = np.asarray(points, dtype=float)
    masses = np.asarray(weights, dtype=float)
    if locations.shape != masses.shape:
        raise ValueError("points and weights must have the same shape")
    if np.imag(probe) <= 0.0:
        raise ValueError("probe must lie in the upper half-plane")
    if np.any(~np.isfinite(masses)) or np.any(masses < 0.0):
        raise ValueError("weights must be finite and nonnegative")
    return complex(np.sum(masses / (locations - probe)))


def analyze_weighted_clark_candidates(
    characteristic: ShiftedCharacteristic,
    model: str,
    support: float,
    phase: float,
    height: float,
    samples: int = 24001,
) -> WeightedClarkRow:
    """Audit one compact phase level and its two candidate weight systems."""

    if support <= 0.0 or height <= 0.0:
        raise ValueError("support and height must be positive")
    roots = characteristic.real_zeros(
        phase, -height, height, samples=samples
    )
    derivatives = analytic_boundary_phase_derivative(characteristic, roots)
    phase_weights = normalized_clark_candidate_weights(roots, derivatives)
    positive = np.isfinite(phase_weights)
    positive_phase_weights = phase_weights[positive]

    defect_weights, normalized_gram = defect_overlap_data(
        characteristic, roots
    )
    if roots.size > 1:
        off_diagonal = np.abs(
            normalized_gram - np.eye(roots.size, dtype=complex)
        )
        maximum_coherence = float(np.max(off_diagonal))
    else:
        maximum_coherence = 0.0

    comparable = positive & (defect_weights > 0.0)
    ratios = phase_weights[comparable] / defect_weights[comparable]
    phase_mass = float(np.sum(positive_phase_weights))
    square_mass = float(np.sum(positive_phase_weights**2))
    effective_count = phase_mass**2 / square_mass if square_mass > 0.0 else 0.0
    transforms = tuple(
        weighted_cauchy_transform(roots[positive], positive_phase_weights, probe)
        for probe in DEFAULT_PROBES
    )

    return WeightedClarkRow(
        model=model,
        measure_status=(
            "phase weights are Clark candidates pending a meromorphic-inner "
            "identification; defect weights are exact overlaps but fail to be "
            "a spectral measure unless root vectors are orthogonal"
        ),
        support=float(support),
        dimension=characteristic.dimension,
        shift=characteristic.shift,
        phase=float(phase),
        height=float(height),
        root_count=int(roots.size),
        nonpositive_phase_derivative_count=int(np.sum(~positive)),
        phase_candidate_mass=phase_mass,
        phase_candidate_effective_atom_count=effective_count,
        phase_candidate_largest_atom=(
            float(np.max(positive_phase_weights))
            if positive_phase_weights.size
            else float("nan")
        ),
        defect_overlap_mass=float(np.sum(defect_weights)),
        defect_bessel_excess=max(0.0, float(np.sum(defect_weights)) - 1.0),
        maximum_distinct_root_coherence=maximum_coherence,
        median_phase_to_defect_weight_ratio=(
            float(np.median(ratios)) if ratios.size else float("nan")
        ),
        maximum_phase_to_defect_weight_ratio=(
            float(np.max(ratios)) if ratios.size else float("nan")
        ),
        cauchy_at_i=transforms[0],
        cauchy_at_2i=transforms[1],
        cauchy_at_10i=transforms[2],
    )


def _format_complex(value: complex) -> str:
    return f"{value.real:.9e}{value.imag:+.9e}j"


def _print_row(row: WeightedClarkRow) -> None:
    print(
        f"{row.model},{row.support:.3f},{row.dimension},{row.shift:.9g},"
        f"{row.phase:.9g},{row.height:.3f},{row.root_count},"
        f"{row.nonpositive_phase_derivative_count},"
        f"{row.phase_candidate_mass:.12g},"
        f"{row.phase_candidate_largest_atom:.12g},"
        f"{row.phase_candidate_effective_atom_count:.9g},"
        f"{row.defect_overlap_mass:.12g},"
        f"{row.defect_bessel_excess:.9g},"
        f"{row.maximum_distinct_root_coherence:.9g},"
        f"{row.median_phase_to_defect_weight_ratio:.9g},"
        f"{row.maximum_phase_to_defect_weight_ratio:.9g},"
        f"{_format_complex(row.cauchy_at_i)},"
        f"{_format_complex(row.cauchy_at_2i)},"
        f"{_format_complex(row.cauchy_at_10i)}",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--supports", type=float, nargs="+", default=list(DEFAULT_SUPPORTS)
    )
    parser.add_argument(
        "--dimensions", type=int, nargs="+", default=list(DEFAULT_DIMENSIONS)
    )
    parser.add_argument(
        "--phases", type=float, nargs="+", default=list(DEFAULT_PHASES)
    )
    parser.add_argument("--shift", type=float, default=-0.25)
    parser.add_argument("--height", type=float, default=96.0)
    parser.add_argument("--samples", type=int, default=24001)
    parser.add_argument("--form-dps", type=int, default=35)
    args = parser.parse_args()

    print(
        "model,L,m,shift,phase,T,roots,nonpositive_phase_derivatives,"
        "phase_mass,largest_phase_atom,effective_atoms,defect_mass,"
        "defect_bessel_excess,max_root_coherence,median_phase_defect_ratio,"
        "max_phase_defect_ratio,Cauchy_i,Cauchy_2i,Cauchy_10i",
        flush=True,
    )
    for support in args.supports:
        for dimension in args.dimensions:
            high_precision = spectral_form(
                support, dimension, dps=args.form_dps
            )
            metric = np.asarray(high_precision.tolist(), dtype=float)
            del high_precision
            characteristic = ShiftedCharacteristic(
                metric, support / 4.0, args.shift
            )
            for phase in args.phases:
                row = analyze_weighted_clark_candidates(
                    characteristic=characteristic,
                    model="completed-Weil-finite-Galerkin",
                    support=support,
                    phase=phase,
                    height=args.height,
                    samples=args.samples,
                )
                _print_row(row)
            del characteristic, metric
            gc.collect()


if __name__ == "__main__":
    main()
