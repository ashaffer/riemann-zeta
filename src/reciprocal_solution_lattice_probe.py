#!/usr/bin/env python3
"""Exact arithmetic checks for the R81 reciprocal solution lattice.

For coprime positive integers ``m,n``, the mode pairs on

    a*n - b*m = theta

form one affine integer lattice.  Poisson summation along that lattice
extracts ``exp(2*pi*i*k*theta*inverse(n)/m)``.  This module checks only that
exact modular algebra and identifies the punctured-axis corrections; it does
not estimate the resulting analytic sums.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class LatticeSolution:
    """A particular solution to ``a*n-b*m=theta``."""

    a: int
    b: int


def particular_solution(theta: int, m: int, n: int) -> LatticeSolution:
    """Return the representative with ``0 <= a < m``."""

    if m <= 0 or n <= 0:
        raise ValueError("m and n must be positive")
    if math.gcd(m, n) != 1:
        raise ValueError("m and n must be coprime")
    inverse_n = pow(n, -1, m) if m > 1 else 0
    a = (theta * inverse_n) % m if m > 1 else 0
    b = (a * n - theta) // m
    return LatticeSolution(a=a, b=b)


def lattice_solution(
    theta: int,
    m: int,
    n: int,
    ell: int,
) -> LatticeSolution:
    """Return the solution indexed by ``ell``."""

    base = particular_solution(theta, m, n)
    return LatticeSolution(a=base.a + m * ell, b=base.b + n * ell)


def reciprocal_residue(theta: int, m: int, n: int, k: int) -> int:
    """Return ``k*theta*inverse(n) mod m``, the Poisson phase residue."""

    particular_solution(theta, m, n)  # validates the inputs
    if m == 1:
        return 0
    return (k * theta * pow(n, -1, m)) % m


def axis_indices(theta: int, m: int, n: int) -> tuple[int | None, int | None]:
    """Return lattice indices at which ``a=0`` and ``b=0``, if present."""

    base = particular_solution(theta, m, n)
    ell_a = -base.a // m if base.a % m == 0 else None
    ell_b = -base.b // n if base.b % n == 0 else None
    return ell_a, ell_b


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theta", type=int, default=5)
    parser.add_argument("--m", type=int, default=7)
    parser.add_argument("--n", type=int, default=11)
    parser.add_argument("--k", type=int, default=3)
    args = parser.parse_args()
    base = particular_solution(args.theta, args.m, args.n)
    residue = reciprocal_residue(
        args.theta,
        args.m,
        args.n,
        args.k,
    )
    print(f"particular_solution={base}")
    print(f"poisson_phase_residue_mod_m={residue}")
    print(f"axis_indices={axis_indices(args.theta, args.m, args.n)}")


if __name__ == "__main__":
    main()
