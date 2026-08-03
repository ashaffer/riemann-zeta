"""Fail-fast sign scan for the de Bruijn--Newman theta heat flow.

For H_t(x)=int_0^infty exp(t u^2) Phi(u) cos(xu) du, test the
Laguerre expression

    L_t(x) = H_t'(x)^2 - H_t(x) H_t''(x).

Strict positivity would exclude real double zeros and is necessary for a
Laguerre--Polya function.  This numerical scan is only a falsifier for proposed
global sign mechanisms; it is not a proof of positivity or RH.
"""
from __future__ import annotations

import argparse

import numpy as np
from scipy.integrate import quad


def theta_kernel(u: float) -> float:
    """Rodgers--Tao normalization of the positive xi theta kernel Phi."""
    e4 = np.exp(4.0 * u)
    e5 = np.exp(5.0 * u)
    e9 = np.exp(9.0 * u)
    total = 0.0
    for n in range(1, 40):
        n2 = n * n
        decay = np.exp(-np.pi * n2 * e4)
        term = (2.0 * np.pi**2 * n2**2 * e9
                - 3.0 * np.pi * n2 * e5) * decay
        total += term
        if n > 4 and abs(term) < 1e-18 * max(1.0, abs(total)):
            break
    return total


def oscillatory_integral(t: float, x: float, power: int,
                         trig: str, cutoff: float) -> float:
    def amplitude(u: float) -> float:
        return u**power * np.exp(t * u * u) * theta_kernel(u)

    value, _ = quad(amplitude, 0.0, cutoff, weight=trig, wvar=x,
                    epsabs=2e-12, epsrel=2e-12, limit=300)
    return value


def laguerre_value(t: float, x: float, cutoff: float):
    h = oscillatory_integral(t, x, 0, "cos", cutoff)
    hp = -oscillatory_integral(t, x, 1, "sin", cutoff)
    hpp = -oscillatory_integral(t, x, 2, "cos", cutoff)
    laguerre = hp * hp - h * hpp
    scale = hp * hp + abs(h * hpp) + 1e-300
    return h, hp, hpp, laguerre, laguerre / scale


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--times", nargs="+", type=float,
                        default=[0.0, 0.01, 0.05, 0.1, 0.25, 0.5])
    parser.add_argument("--x-max", type=float, default=80.0)
    parser.add_argument("--x-step", type=float, default=0.25)
    parser.add_argument("--cutoff", type=float, default=4.0)
    args = parser.parse_args()

    print("t,min_L,min_relative_L,x_at_min,negative_count")
    xs = np.arange(0.0, args.x_max + args.x_step / 2, args.x_step)
    for t in args.times:
        rows = [(x,) + laguerre_value(t, x, args.cutoff) for x in xs]
        worst = min(rows, key=lambda row: row[4])
        relative_worst = min(row[5] for row in rows)
        negative = sum(row[4] < -1e-18 for row in rows)
        print(f"{t:.9g},{worst[4]:.12e},{relative_worst:.12e},"
              f"{worst[0]:.9g},{negative}")


if __name__ == "__main__":
    main()
