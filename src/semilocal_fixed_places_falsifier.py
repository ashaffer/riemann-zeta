#!/usr/bin/env python3
"""Falsify fixed-place semilocal positivity after an omitted prime activates.

The calculation uses the repository's cutoff-free Legendre assembly for the
pole-free Weil form and then imposes both exponential moment conditions.  It
compares a fixed set of prime places with the full set of prime powers active
at the same support.

These are Rayleigh--Ritz upper bounds, not certified operator eigenvalues.  A
negative value is nevertheless a valid finite-section falsifier up to the
stated numerical assembly; the accompanying analytic broad-bump argument in
``results/TWO-PRIME-INFINITY-FAIL-FAST.md`` proves fixed-S indefiniteness
without numerics.
"""

from __future__ import annotations

import argparse
import math

import mpmath as mp
import numpy as np
from scipy.linalg import null_space

from relative_incidence_gap import moment_vectors
from spectral_margins import spectral_form


def relative_minimum(
    support: float,
    dimension: int,
    dps: int,
    prime_set: set[int] | None,
) -> float:
    form = np.array(
        spectral_form(
            support,
            dimension,
            dps=dps,
            include_primes=True,
            zeta_pole=False,
            prime_set=prime_set,
        ).tolist(),
        dtype=float,
    )
    plus, minus = moment_vectors(support, dimension)
    relative_basis = null_space(np.vstack([plus, minus]))
    compressed = relative_basis.T @ form @ relative_basis
    return float(np.linalg.eigvalsh(compressed)[0])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", nargs="+", type=int, default=[2, 3])
    parser.add_argument(
        "--supports",
        nargs="+",
        type=float,
        default=[3.0, 3.22, 3.27, 3.4, 4.0],
    )
    parser.add_argument("--dimension", type=int, default=8)
    parser.add_argument("--dps", type=int, default=22)
    args = parser.parse_args()

    if max(args.supports) >= 2 * math.log(64):
        raise ValueError(
            "the shared prime-power table is complete only for supports below 2 log 64"
        )

    mp.mp.dps = args.dps
    fixed_primes = set(args.primes)
    print("support,dimension,fixed_places_min,full_active_min")
    for support in args.supports:
        fixed = relative_minimum(
            support, args.dimension, args.dps, fixed_primes
        )
        full = relative_minimum(support, args.dimension, args.dps, None)
        print(
            f"{support:.9g},{args.dimension},"
            f"{fixed:.12e},{full:.12e}"
        )


if __name__ == "__main__":
    main()
