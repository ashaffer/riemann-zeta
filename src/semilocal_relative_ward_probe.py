#!/usr/bin/env python3
"""Moment-null Ward diagnostic for the semilocal Weil source.

The Connes--Consani phase reproduces the pole-free Weil multiplier, whereas
the completed zeta form also contains the rank-two form

    ell_+ tensor ell_- + ell_- tensor ell_+.

This probe imposes ``ell_+=ell_-=0`` *before* forming the old/collar split.
It then constructs a G-orthonormal old relative space and its G-orthogonal
complement in the full relative space.  On these coordinates the pole is
annihilated algebraically, and the usual reference-harmonic Ward response is
computed for the pole-free source.

The result is an ordinary floating-point generalized eigensolve applied to
cutoff-free, high-precision mpmath form assembly.  It is a finite Galerkin
diagnostic, not an interval certificate or a continuum Ward theorem.
"""

from __future__ import annotations

import argparse
import json
from typing import Sequence

import mpmath as mp
import numpy as np
from scipy.linalg import eigvalsh, null_space

from harmonic_schur_collar_probe import mixed_extension_forms
from ward_source_extremizer_probe import literal_collar_geometry, pole_matrix


def exponential_hat_moment(
    center: float | mp.mpf, width: float | mp.mpf, sign: int
) -> mp.mpf:
    """Return ``integral hat(center,width)(x) exp(sign*x/2) dx``."""

    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    c, d = mp.mpf(center), mp.mpf(width)
    s = mp.mpf(sign) / 2
    return mp.exp(s * c) * (2 * mp.cosh(s * d) - 2) / (s * s * d)


def moment_matrix(
    centers: Sequence[float | mp.mpf], widths: Sequence[float | mp.mpf]
) -> np.ndarray:
    """Two rows representing ``ell_+`` and ``ell_-`` on a hat basis."""

    if len(centers) != len(widths):
        raise ValueError("centers and widths must have the same length")
    plus = [float(exponential_hat_moment(c, d, +1)) for c, d in zip(centers, widths)]
    minus = [float(exponential_hat_moment(c, d, -1)) for c, d in zip(centers, widths)]
    return np.asarray([plus, minus], dtype=float)


def _g_orthonormalize(basis: np.ndarray, gram: np.ndarray) -> np.ndarray:
    metric = (basis.T @ gram @ basis + basis.T @ gram.T @ basis) / 2
    chol = np.linalg.cholesky(metric)
    return np.linalg.solve(chol, basis.T).T


def relative_old_collar_coordinates(
    gram: np.ndarray,
    moments: np.ndarray,
    old_degree: int,
    rcond: float = 1.0e-12,
) -> tuple[np.ndarray, int, dict[str, float]]:
    """Build ``[old relative | full-relative G-complement]`` coordinates.

    The first ``old_degree-2`` columns are supported on the old coordinates.
    The remaining columns span their G-orthogonal complement inside the full
    two-moment nullspace.  The returned matrix is G-orthonormal.
    """

    g = np.asarray(gram, dtype=float)
    c = np.asarray(moments, dtype=float)
    n = g.shape[0]
    if g.shape != (n, n) or c.shape != (2, n):
        raise ValueError("expected an n by n Gram matrix and a 2 by n moment matrix")
    if not 3 <= old_degree < n:
        raise ValueError("require 3 <= old_degree < total dimension")

    old_local = null_space(c[:, :old_degree], rcond=rcond)
    if old_local.shape[1] != old_degree - 2:
        raise ValueError("old moment matrix does not have rank two")
    old_embedded = np.zeros((n, old_degree - 2))
    old_embedded[:old_degree, :] = old_local
    old = _g_orthonormalize(old_embedded, g)

    full_null = null_space(c, rcond=rcond)
    if full_null.shape[1] != n - 2:
        raise ValueError("full moment matrix does not have rank two")
    full = _g_orthonormalize(full_null, g)

    old_in_full = full.T @ g @ old
    complement_coordinates = null_space(old_in_full.T, rcond=rcond)
    collar = full @ complement_coordinates
    coordinates = np.column_stack([old, collar])

    diagnostics = {
        "g_orthogonality_error": float(
            np.linalg.norm(coordinates.T @ g @ coordinates - np.eye(n - 2), ord=2)
        ),
        "moment_annihilation_error": float(np.linalg.norm(c @ coordinates, ord=2)),
        "old_support_leakage": float(
            np.linalg.norm(coordinates[old_degree:, : old_degree - 2], ord=2)
        ),
    }
    return coordinates, old_degree - 2, diagnostics


def _symmetrize(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.T) / 2


def analyze_relative_ward(
    old_degree: int,
    collar_degree: int,
    delta: float | mp.mpf,
    dps: int = 50,
    event_prime: int = 5,
) -> dict:
    """Run one pole-null relative Ward diagnostic."""

    delta_mp = mp.mpf(delta)
    q_mp, g_mp, h_mp, lold, lnew = mixed_extension_forms(
        old_degree=old_degree,
        collar_degree=collar_degree,
        delta=delta_mp,
        event_prime=event_prime,
        dps=dps,
    )
    centers, widths, _, _ = literal_collar_geometry(
        old_degree, collar_degree, delta_mp, event_prime
    )
    pole_mp = pole_matrix(centers, widths)

    q = np.asarray(q_mp.tolist(), dtype=float)
    g = np.asarray(g_mp.tolist(), dtype=float)
    h = np.asarray(h_mp.tolist(), dtype=float)
    pole = np.asarray(pole_mp.tolist(), dtype=float)
    moments = moment_matrix(centers, widths)
    coordinates, old_relative_dimension, diagnostics = (
        relative_old_collar_coordinates(g, moments, old_degree)
    )

    compressed_g = _symmetrize(coordinates.T @ g @ coordinates)
    compressed_h = _symmetrize(coordinates.T @ h @ coordinates)
    compressed_q = _symmetrize(coordinates.T @ q @ coordinates)
    compressed_pole = _symmetrize(coordinates.T @ pole @ coordinates)
    compressed_nonpole = _symmetrize(compressed_q - compressed_pole)

    split = old_relative_dimension
    h_old = compressed_h[:split, :split]
    h_cross = compressed_h[:split, split:]
    harmonic_correction = np.linalg.solve(h_old, h_cross)
    lift = np.vstack(
        [-harmonic_correction, np.eye(compressed_h.shape[0] - split)]
    )
    denominator = _symmetrize(lift.T @ compressed_g @ lift)

    def ward_data(form: np.ndarray) -> tuple[float, np.ndarray, float]:
        old = _symmetrize(form[:split, :split])
        cross = form[:split, split:]
        residual_cross = cross - old @ harmonic_correction
        response = _symmetrize(residual_cross.T @ np.linalg.solve(old, residual_cross))
        spectrum = eigvalsh(response, denominator)
        floor = float(eigvalsh(old, compressed_g[:split, :split])[0])
        return float(spectrum[-1]), spectrum, floor

    theta_nonpole, spectrum, old_floor = ward_data(compressed_nonpole)
    theta_completed, _, _ = ward_data(compressed_q)
    diagnostics.update(
        {
            "compressed_pole_operator_norm": float(
                np.linalg.norm(compressed_pole, ord=2)
            ),
            "completed_nonpole_theta_difference": abs(
                theta_completed - theta_nonpole
            ),
            "reference_harmonicity_error": float(
                np.linalg.norm(
                    compressed_h[:split, :] @ lift,
                    ord=2,
                )
            ),
        }
    )

    return {
        "old_degree": old_degree,
        "collar_degree_per_side": collar_degree,
        "delta": float(delta_mp),
        "event_prime": event_prime,
        "old_support": float(lold),
        "new_support": float(lnew),
        "old_relative_dimension": split,
        "collar_relative_dimension": compressed_h.shape[0] - split,
        "old_ritz_floor": old_floor,
        "ward_ratio_pole_free": theta_nonpole,
        "ward_ratio_completed": theta_completed,
        "generalized_response_spectrum": [float(x) for x in spectrum],
        "diagnostics": diagnostics,
    }


def _parse_case(text: str) -> tuple[int, int, float]:
    fields = text.split(":")
    if len(fields) != 3:
        raise argparse.ArgumentTypeError("case must have form OLD:COLLAR:DELTA")
    return int(fields[0]), int(fields[1]), float(fields[2])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--case",
        action="append",
        type=_parse_case,
        dest="cases",
        help="OLD:COLLAR:DELTA; repeat for multiple cases",
    )
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--event-prime", type=int, default=5)
    args = parser.parse_args()
    cases = args.cases or [
        (40, 1, 0.32),
        (48, 2, 0.40),
        (80, 1, 0.16),
        (96, 2, 0.20),
        (128, 1, 0.10),
    ]
    rows = [
        analyze_relative_ward(m, q, delta, args.dps, args.event_prime)
        for m, q, delta in cases
    ]
    print(
        json.dumps(
            {
                "schema": "zeta23.semilocal-relative-ward-probe.v1",
                "status": "FINITE_GALERKIN_DIAGNOSTIC_NOT_A_THEOREM",
                "moment_conditions": ["ell_plus=0", "ell_minus=0"],
                "rows": rows,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
