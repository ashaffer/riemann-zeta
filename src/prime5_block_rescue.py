#!/usr/bin/env python3
"""Diagnose the prime-5 block-rescue mechanism in a constrained Ritz space.

For ``2 log 5 < L < 2 log 7``, the difference between the full arithmetic
form and the form restricted to the prime places ``{2, 3}`` is exactly the
prime-5 event.  This script diagonalizes the old form, splits off its negative
spectral subspace, and tests the sharp block criterion for the full form

    [ A  B  ] > 0  iff  A > 0, D > 0, ||A^-1/2 B D^-1/2|| < 1.
    [ B* D  ]

The default is the full zeta form, including its pole term.  ``--relative``
instead imposes the two pole-zero moment constraints.  All calculations are
ordinary floating-point Ritz diagnostics.  In
particular, a positive result is not an operator theorem or an interval
certificate.
"""

from __future__ import annotations

import argparse
import math

import mpmath as mp
import numpy as np
from scipy.linalg import null_space

from relative_incidence_gap import moment_vectors
from spectral_margins import spectral_form


def inverse_square_root(matrix: np.ndarray) -> np.ndarray:
    """Return the symmetric inverse square root of a positive matrix."""
    values, vectors = np.linalg.eigh(matrix)
    if values[0] <= 0:
        raise ValueError("inverse square root requires a positive matrix")
    return (vectors / np.sqrt(values)) @ vectors.T


def ritz_form(
    support: float,
    dimension: int,
    dps: int,
    prime_set: set[int] | None,
    relative: bool,
) -> tuple[np.ndarray, np.ndarray]:
    """Return the Ritz form and its ambient (possibly constrained) basis."""
    form = np.array(
        spectral_form(
            support,
            dimension,
            dps=dps,
            include_primes=True,
            zeta_pole=not relative,
            prime_set=prime_set,
        ).tolist(),
        dtype=float,
    )
    if not relative:
        return form, np.eye(dimension)
    plus, minus = moment_vectors(support, dimension)
    relative_basis = null_space(np.vstack([plus, minus]))
    return relative_basis.T @ form @ relative_basis, relative_basis


def block_diagnostic(
    support: float,
    dimension: int,
    dps: int,
    negative_tolerance: float,
    relative: bool,
) -> dict[str, float | int]:
    old, relative_basis = ritz_form(
        support, dimension, dps, {2, 3}, relative
    )
    full, full_relative_basis = ritz_form(
        support, dimension, dps, None, relative
    )
    if not np.allclose(relative_basis, full_relative_basis):
        raise RuntimeError("constraint bases unexpectedly differ")

    old_values, old_vectors = np.linalg.eigh(old)
    negative_count = int(np.count_nonzero(old_values < -negative_tolerance))
    if negative_count == 0:
        return {
            "support": support,
            "dimension": dimension,
            "old_min": float(old_values[0]),
            "full_min": float(np.linalg.eigvalsh(full)[0]),
            "negative_count": 0,
            "A_min": math.nan,
            "D_min": math.nan,
            "coupling": math.nan,
            "schur_min": math.nan,
            "event_on_negative_min": math.nan,
        }

    negative_vectors = old_vectors[:, :negative_count]
    positive_vectors = old_vectors[:, negative_count:]
    transformed = old_vectors.T @ full @ old_vectors
    A = transformed[:negative_count, :negative_count]
    B = transformed[:negative_count, negative_count:]
    D = transformed[negative_count:, negative_count:]

    A_min = float(np.linalg.eigvalsh(A)[0])
    D_min = float(np.linalg.eigvalsh(D)[0])
    if A_min > 0 and D_min > 0:
        normalized_cross = inverse_square_root(A) @ B @ inverse_square_root(D)
        coupling = float(np.linalg.svd(normalized_cross, compute_uv=False)[0])
        schur_min = float(np.linalg.eigvalsh(A - B @ np.linalg.solve(D, B.T))[0])
    else:
        coupling = math.nan
        schur_min = math.nan

    event = full - old
    event_on_negative = negative_vectors.T @ event @ negative_vectors
    return {
        "support": support,
        "dimension": dimension,
        "old_min": float(old_values[0]),
        "full_min": float(np.linalg.eigvalsh(full)[0]),
        "negative_count": negative_count,
        "A_min": A_min,
        "D_min": D_min,
        "coupling": coupling,
        "schur_min": schur_min,
        "event_on_negative_min": float(np.linalg.eigvalsh(event_on_negative)[0]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--supports", nargs="+", type=float, default=[3.27, 3.30, 3.40]
    )
    parser.add_argument("--dimension", type=int, default=12)
    parser.add_argument("--dps", type=int, default=24)
    parser.add_argument("--negative-tolerance", type=float, default=1e-10)
    parser.add_argument(
        "--relative",
        action="store_true",
        help="impose the two pole-zero moment constraints instead of using the full zeta form",
    )
    args = parser.parse_args()

    lower = 2 * math.log(5)
    upper = 2 * math.log(7)
    if any(not lower < support < upper for support in args.supports):
        raise ValueError(
            "every support must lie strictly between 2 log 5 and 2 log 7"
        )

    mp.mp.dps = args.dps
    fields = [
        "support",
        "dimension",
        "old_min",
        "full_min",
        "negative_count",
        "A_min",
        "D_min",
        "coupling",
        "schur_min",
        "event_on_negative_min",
    ]
    print(",".join(fields))
    for support in args.supports:
        result = block_diagnostic(
            support,
            args.dimension,
            args.dps,
            args.negative_tolerance,
            args.relative,
        )
        print(
            ",".join(
                str(result[field]) if field in {"dimension", "negative_count"}
                else f"{float(result[field]):.12e}"
                for field in fields
            )
        )


if __name__ == "__main__":
    main()
