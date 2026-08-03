"""Falsify a classical sufficient mechanism for theta-flow positivity.

For the even heat kernel a_t and its Fourier transform F_t,

  F_t'^2 - F_t F_t'' = Fourier[b_t],
  b_t(w) = 1/2 int (2u-w)^2 a_t(u) a_t(w-u) du >= 0.

Polya's criterion would give Fourier[b_t] >= 0 if b_t were decreasing and
convex on the positive half-line.  Violations reject this mechanism, not the
Laguerre inequality itself.
"""
from __future__ import annotations

import argparse

import numpy as np
from scipy.integrate import quad

from xi_heat_laguerre_scan import theta_kernel


def even_heat_kernel(t: float, u: float) -> float:
    v = abs(u)
    return np.exp(t * v * v) * theta_kernel(v)


def polya_kernel(t: float, w: float, cutoff: float) -> float:
    def integrand(u: float) -> float:
        return ((2.0 * u - w) ** 2 * even_heat_kernel(t, u)
                * even_heat_kernel(t, w - u) / 2.0)

    value, _ = quad(integrand, -cutoff, cutoff + abs(w),
                    epsabs=2e-11, epsrel=2e-11, limit=400)
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--times", nargs="+", type=float,
                        default=[0.0, 0.05, 0.25, 0.5])
    parser.add_argument("--w-max", type=float, default=3.0)
    parser.add_argument("--w-step", type=float, default=0.025)
    parser.add_argument("--cutoff", type=float, default=4.0)
    args = parser.parse_args()

    ws = np.arange(0.0, args.w_max + args.w_step / 2, args.w_step)
    print("t,max_first_difference,min_second_difference,"
          "monotonicity_violations,convexity_violations")
    for t in args.times:
        bs = np.array([polya_kernel(t, w, args.cutoff) for w in ws])
        first = np.diff(bs) / args.w_step
        second = np.diff(bs, 2) / args.w_step**2
        tolerance = 1e-9 * max(1.0, float(np.max(np.abs(bs))))
        print(f"{t:.9g},{np.max(first):.12e},{np.min(second):.12e},"
              f"{np.count_nonzero(first > tolerance)},"
              f"{np.count_nonzero(second < -tolerance)}")


if __name__ == "__main__":
    main()
