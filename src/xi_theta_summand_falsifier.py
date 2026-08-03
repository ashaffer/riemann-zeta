"""Test termwise Laguerre positivity of individual xi theta summands."""
from __future__ import annotations

import argparse

import numpy as np
from scipy.integrate import quad


def theta_summand(u: float, n: int) -> float:
    n2 = n * n
    return ((2.0 * np.pi**2 * n2**2 * np.exp(9.0 * u)
             - 3.0 * np.pi * n2 * np.exp(5.0 * u))
            * np.exp(-np.pi * n2 * np.exp(4.0 * u)))


def laguerre(n: int, x: float, t: float, cutoff: float):
    def integral(power: int, trig: str) -> float:
        def amplitude(u: float) -> float:
            return u**power * np.exp(t * u * u) * theta_summand(u, n)

        return quad(amplitude, 0.0, cutoff, weight=trig, wvar=x,
                    epsabs=2e-12, epsrel=2e-12, limit=300)[0]

    h = integral(0, "cos")
    hp = -integral(1, "sin")
    hpp = -integral(2, "cos")
    value = hp * hp - h * hpp
    relative = value / (hp * hp + abs(h * hpp) + 1e-300)
    return value, relative


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summands", nargs="+", type=int, default=[1, 2, 3])
    parser.add_argument("--time", type=float, default=0.0)
    parser.add_argument("--x-max", type=float, default=100.0)
    parser.add_argument("--x-step", type=float, default=0.25)
    parser.add_argument("--cutoff", type=float, default=4.0)
    args = parser.parse_args()

    print("n,min_relative_L,x_at_min,L_at_min,negative_count")
    xs = np.arange(0.0, args.x_max + args.x_step / 2, args.x_step)
    for n in args.summands:
        rows = [(x,) + laguerre(n, x, args.time, args.cutoff) for x in xs]
        worst = min(rows, key=lambda row: row[2])
        negative = sum(row[1] < -1e-18 for row in rows)
        print(f"{n},{worst[2]:.12e},{worst[0]:.9g},"
              f"{worst[1]:.12e},{negative}")


if __name__ == "__main__":
    main()
