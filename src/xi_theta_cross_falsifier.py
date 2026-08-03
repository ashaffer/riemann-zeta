"""Sign scan for bilinear Laguerre cross terms of theta summands."""
from __future__ import annotations

import argparse

import numpy as np
from scipy.integrate import quad

from xi_theta_summand_falsifier import theta_summand


def jet(n: int, x: float, cutoff: float):
    def integral(power: int, trig: str) -> float:
        return quad(lambda u: u**power * theta_summand(u, n),
                    0.0, cutoff, weight=trig, wvar=x,
                    epsabs=2e-12, epsrel=2e-12, limit=300)[0]

    return integral(0, "cos"), -integral(1, "sin"), -integral(2, "cos")


def cross(left, right) -> float:
    h, hp, hpp = left
    g, gp, gpp = right
    return hp * gp - 0.5 * (h * gpp + g * hpp)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", nargs="+", default=["1,2", "1,3", "2,3"])
    parser.add_argument("--x-max", type=float, default=120.0)
    parser.add_argument("--x-step", type=float, default=0.25)
    parser.add_argument("--cutoff", type=float, default=4.0)
    args = parser.parse_args()

    xs = np.arange(0.0, args.x_max + args.x_step / 2, args.x_step)
    print("left,right,min_cross,x_at_min,max_cross,x_at_max")
    for encoded in args.pairs:
        left_n, right_n = map(int, encoded.split(","))
        rows = []
        for x in xs:
            rows.append((cross(jet(left_n, x, args.cutoff),
                               jet(right_n, x, args.cutoff)), x))
        minimum = min(rows)
        maximum = max(rows)
        print(f"{left_n},{right_n},{minimum[0]:.12e},{minimum[1]:.9g},"
              f"{maximum[0]:.12e},{maximum[1]:.9g}")


if __name__ == "__main__":
    main()
