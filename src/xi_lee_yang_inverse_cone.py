#!/usr/bin/env python3
"""Certified finite inverse-cone tests for the centered Riemann xi function.

Put

    M(h) = xi(1/2 + h) / xi(1/2).

There are two deliberately separate tests.

1. Newman--Lee--Yang cone.  If all zeros of ``M`` are purely imaginary, its
   Hadamard product gives

       log M(h) = sum_{n >= 1} (-1)^(n-1) a_n h^(2n) / n,
       a_n = sum_j alpha_j^(-2n) >= 0.

   Consequently ``(a_n)`` has the two Stieltjes Hankel localizers

       H0[i,j] = a_(i+j+1),   H1[i,j] = a_(i+j+2)

   positive semidefinite.  Failure would refute the purely-imaginary-zero
   property (and hence RH).  A finite pass proves only truncated consistency.

2. Independent weighted-spin cone.  A much narrower representation

       M(h) = exp(b h^2) product_j cosh(w_j h),   b >= 0,

   would make

       p_n = [h^(2n)] log M(h) / [h^(2n)] log cosh(h)

   a Stieltjes power-moment sequence (with Gaussian slack in ``p_1``).
   A negative Hankel determinant rules out this product-spin representation,
   but not interacting ferromagnetic Ising models, general Lee--Yang measures,
   or RH.

All Taylor coefficients and determinants are rigorous Arb balls supplied by
python-flint.  A comparison ``ball > 0`` or ``ball < 0`` succeeds only when
the entire enclosure has that sign.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from flint import acb, acb_series, arb, arb_mat, ctx


@dataclass(frozen=True)
class DeterminantResult:
    family: str
    dimension: int
    determinant: arb
    sign: str


def interval_sign(value: arb) -> str:
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "unresolved"


def centered_log_xi(moment_count: int, bits: int) -> tuple[acb_series, acb_series]:
    """Return rigorous series for ``log M(h)`` and ``log cosh(h)``."""

    ctx.threads = 1
    ctx.prec = bits
    ctx.cap = 2 * moment_count + 2

    h = acb_series([0, 1])
    s = h + acb(arb(1) / 2)
    pi = acb.pi()
    xi = (
        s
        * (s - 1)
        / 2
        * (-s * pi.log() / 2).exp()
        * (s / 2).gamma()
        * s.zeta()
    )
    log_m = (xi / xi[0]).log()
    log_cosh = ((h.exp() + (-h).exp()) / 2).log()
    return log_m, log_cosh


def hankel_determinants(
    moments: dict[int, arb], maximum_dimension: int, prefix: str
) -> list[DeterminantResult]:
    results: list[DeterminantResult] = []
    for shift, suffix in ((1, "H0"), (2, "H1")):
        for dimension in range(1, maximum_dimension + 1):
            matrix = arb_mat(
                [
                    [moments[i + j + shift] for j in range(dimension)]
                    for i in range(dimension)
                ]
            )
            determinant = matrix.det()
            results.append(
                DeterminantResult(
                    f"{prefix}-{suffix}",
                    dimension,
                    determinant,
                    interval_sign(determinant),
                )
            )
    return results


def summarize_family(
    name: str,
    coefficient_moments: dict[int, arb],
    determinants: list[DeterminantResult],
    digits: int,
) -> str:
    coefficient_failure = next(
        (
            (index, value)
            for index, value in coefficient_moments.items()
            if value < 0
        ),
        None,
    )
    coefficient_unresolved = next(
        (
            (index, value)
            for index, value in coefficient_moments.items()
            if not (value > 0 or value < 0)
        ),
        None,
    )
    determinant_failures = [
        result for result in determinants if result.sign == "negative"
    ]
    determinant_unresolved = next(
        (result for result in determinants if result.sign == "unresolved"), None
    )

    if coefficient_failure is not None:
        index, value = coefficient_failure
        print(f"{name}: KILLED by moment {index}: {value.str(digits)}")
        return "KILLED"
    if determinant_failures:
        print(f"{name}: KILLED by negative Hankel determinant(s)")
        for family in sorted({result.family for result in determinant_failures}):
            first_failure = next(
                result
                for result in determinant_failures
                if result.family == family
            )
            print(
                f"  {family} first failure at dimension "
                f"{first_failure.dimension}: "
                f"{first_failure.determinant.str(digits)}"
            )
            if first_failure.dimension > 1:
                previous = next(
                    result
                    for result in determinants
                    if result.family == family
                    and result.dimension == first_failure.dimension - 1
                )
                pivot = first_failure.determinant / previous.determinant
                print(f"    corresponding LDL pivot: {pivot.str(digits)}")
        return "KILLED"
    if coefficient_unresolved is not None:
        index, value = coefficient_unresolved
        print(f"{name}: UNRESOLVED at moment {index}: {value.str(digits)}")
        return "UNRESOLVED"
    if determinant_unresolved is not None:
        print(
            f"{name}: UNRESOLVED at {determinant_unresolved.family} "
            f"dimension {determinant_unresolved.dimension}: "
            f"{determinant_unresolved.determinant.str(digits)}"
        )
        return "UNRESOLVED"

    final_results = [
        result
        for result in determinants
        if result.dimension == max(item.dimension for item in determinants)
    ]
    print(
        f"{name}: SURVIVES; all coefficient moments and leading Hankel "
        "determinants are rigorously positive"
    )
    for result in final_results:
        print(
            f"  {result.family} dimension {result.dimension}: "
            f"{result.determinant.str(digits)}"
        )
    return "SURVIVES"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, default=8000)
    parser.add_argument("--moments", type=int, default=40)
    parser.add_argument("--hankel-dimension", type=int, default=20)
    parser.add_argument("--digits", type=int, default=20)
    args = parser.parse_args()

    if args.bits < 128:
        raise ValueError("require at least 128 bits")
    if args.hankel_dimension < 1:
        raise ValueError("hankel dimension must be positive")
    if args.moments < 2 * args.hankel_dimension:
        raise ValueError("moments must be at least twice the Hankel dimension")

    log_m, log_cosh = centered_log_xi(args.moments, args.bits)

    lee_yang_moments = {
        n: log_m[2 * n].real * ((-1) ** (n - 1) * n)
        for n in range(1, args.moments + 1)
    }
    product_spin_moments = {
        n: (log_m[2 * n] / log_cosh[2 * n]).real
        for n in range(1, args.moments + 1)
    }

    lee_yang_determinants = hankel_determinants(
        lee_yang_moments, args.hankel_dimension, "LY"
    )
    product_spin_determinants = hankel_determinants(
        product_spin_moments, args.hankel_dimension, "SPIN"
    )

    print(
        f"Arb bits={args.bits} moments={args.moments} "
        f"Hankel dimension={args.hankel_dimension}"
    )
    lee_yang_status = summarize_family(
        "Newman--Lee--Yang cone",
        lee_yang_moments,
        lee_yang_determinants,
        args.digits,
    )
    product_spin_status = summarize_family(
        "Independent weighted-spin cone",
        product_spin_moments,
        product_spin_determinants,
        args.digits,
    )

    print(f"FINAL: Lee--Yang={lee_yang_status}; product-spin={product_spin_status}")


if __name__ == "__main__":
    main()
