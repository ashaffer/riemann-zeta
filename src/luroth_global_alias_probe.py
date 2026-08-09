"""Numerical checks for the R96 all-alias Poisson finite part.

These routines test the forced dual counterterm, its convergent Euler-defect
carrier, and the phase match between stationary phase and the exact gamma
multiplier.  They do not establish a zero-free region.
"""
from __future__ import annotations

import argparse
import cmath
import math


def dual_finite_part(cutoff: int, s: complex) -> complex:
    """Return sum_{k<=K} k^(s-1) - K^s/s."""

    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    z = complex(s)
    if z == 0:
        raise ValueError("s must be nonzero")
    raw = sum((k ** (z - 1) for k in range(1, cutoff + 1)), 0.0j)
    return raw - cutoff**z / z


def dual_defect(index: int, s: complex) -> complex:
    """Return the exact increment D_{K+1}(s)-D_K(s)."""

    if index < 1:
        raise ValueError("index must be positive")
    z = complex(s)
    if z == 0:
        raise ValueError("s must be nonzero")
    return (index + 1) ** (z - 1) - ((index + 1) ** z - index**z) / z


def defect_carrier_partial(cutoff: int, s: complex) -> complex:
    """Return (s-1)/s plus dual defects through index cutoff-1."""

    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    z = complex(s)
    return (z - 1) / z + sum(
        (dual_defect(index, z) for index in range(1, cutoff)), 0.0j
    )


def exact_chi(s: complex) -> complex:
    """Return the standard zeta functional-equation multiplier chi(s)."""

    import mpmath as mp

    z = mp.mpc(s)
    value = 2**z * mp.pi ** (z - 1) * mp.sin(mp.pi * z / 2) * mp.gamma(1 - z)
    return complex(value)


def exact_alias_prefactor(s: complex) -> complex:
    """Return P(s) chi(s) for the Luroth carrier."""

    z = complex(s)
    return (z - 1) / (z * (z + 1)) * exact_chi(z)


def stationary_prefactor(s: complex) -> complex:
    """Return the leading full-Gaussian stationary-phase prefactor."""

    z = complex(s)
    if z.imag <= 0:
        raise ValueError("the displayed stationary phase uses positive height")
    t = z.imag
    return (
        (2 * math.pi) ** (z.real - 0.5)
        * t ** (-z.real - 0.5)
        * cmath.exp(1j * (t - t * math.log(t / (2 * math.pi)) - math.pi / 4))
    )


def scaled_dual_alias(index: int, sigma: float, height: float) -> complex:
    """Sample K^(1-s)d_K(s) at the m-th dual alias."""

    if index < 1 or height <= 0:
        raise ValueError("index and height must be positive")
    k = max(1, round(height / (2 * math.pi * index)))
    s = complex(sigma, height)
    return k ** (1 - s) * dual_defect(k, s)


def exact_dual_value(s: complex) -> complex:
    """Return zeta(1-s)."""

    import mpmath as mp

    return complex(mp.zeta(1 - mp.mpc(s)))


def run_probe(sigma: float, height: float, cutoff: int, aliases: int) -> None:
    s = complex(sigma, height)
    finite = dual_finite_part(cutoff, s)
    corrected = finite - 0.5 * cutoff ** (s - 1)
    exact = exact_dual_value(s)
    print(f"s={s}, cutoff={cutoff}")
    print(f"dual finite part:              {finite}")
    print(f"after half-endpoint correction:{corrected}")
    print(f"zeta(1-s):                    {exact}")
    print(f"corrected error:              {abs(corrected-exact):.6g}")
    exact_prefactor = exact_alias_prefactor(s)
    predicted_prefactor = stationary_prefactor(s)
    print(
        "gamma/stationary relative error: "
        f"{abs(exact_prefactor-predicted_prefactor)/abs(exact_prefactor):.6g}"
    )
    for index in range(1, aliases + 1):
        response = scaled_dual_alias(index, sigma, height)
        print(f"alias {index}: response={response}, error={abs(response-1):.6g}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sigma", type=float, default=0.9)
    parser.add_argument("--height", type=float, default=1000.0)
    parser.add_argument("--cutoff", type=int, default=200_000)
    parser.add_argument("--aliases", type=int, default=3)
    args = parser.parse_args()
    run_probe(args.sigma, args.height, args.cutoff, args.aliases)


if __name__ == "__main__":
    main()
