"""Nonrigorous crossing scout for the actual-theta second tail S_2(P,T).

It uses the gamma-rescaled completed-xi grid from
``probe_theta_s3_fast_grid.py`` and the exact cosine-transform formula

  S_2(P,T) = (2/pi) int_0^inf
      [Z(T)^2-Z(T+x)Z(T-x)] cos(Px)/x^2 dx.

A DCT-I evaluates all P=k*pi/W.  Values below the requested relative floor
are discarded before crossing counts are formed.  This is a conjecture
finder, not an interval proof.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.fft import dct
from scipy.special import sici

from probe_theta_s3_fast_grid import (
    critical_transform_grid,
    extrapolate_laguerre,
)


def constant_cosine_quadratic_tail(p: np.ndarray, cutoff: float) -> np.ndarray:
    """Integral from cutoff to infinity of cos(p*x)/x^2, p>=0."""
    ans = np.empty_like(p)
    zero = p == 0.0
    ans[zero] = 1.0 / cutoff
    if np.any(~zero):
        pp = p[~zero]
        si, _ = sici(pp * cutoff)
        ans[~zero] = (
            np.cos(pp * cutoff) / cutoff
            - pp * (math.pi / 2.0 - si)
        )
    return ans


def scan(args: argparse.Namespace) -> None:
    dx = args.dx
    grid = np.arange(0.0, 2.0 * args.t_max + args.margin + dx / 2.0, dx)
    z = critical_transform_grid(grid, args.dps, args.backend)
    stride = max(1, int(round(args.t_step / dx)))
    first = max(1, int(math.ceil(args.t_min / dx)))
    last = int(math.floor(args.t_max / dx))
    summaries: list[tuple[int, float, float, float, float, float, float, str]] = []

    for i in range(first, last + 1, stride):
        t = i * dx
        n = min(i + int(round(args.margin / dx)), len(z) - 1 - i)
        j = np.arange(n + 1)
        factor = np.ones(n + 1)
        beyond = j > i
        factor[beyond] = np.exp(-math.pi * (j[beyond] - i) * dx / 4.0)
        gap = z[i] * z[i] - factor * z[i + j] * z[np.abs(i - j)]
        laguerre = extrapolate_laguerre(gap, dx)

        divided = np.empty(n + 1)
        divided[0] = laguerre
        divided[1:] = gap[1:] / ((j[1:] * dx) ** 2)
        # DCT-I / 2 is exactly the trapezoid cosine sum on this grid.
        integral = 0.5 * dx * dct(divided, type=1)
        p = math.pi * np.arange(n + 1) / (n * dx)
        keep = p <= min(args.p_max, math.log1p(t) + args.wedge_pad)
        p = p[keep]
        integral = integral[keep]
        integral += z[i] * z[i] * constant_cosine_quadratic_tail(p, n * dx)
        s2 = (2.0 / math.pi) * integral

        scale = max(abs(laguerre), z[i] * z[i], np.finfo(float).tiny)
        tol = args.relative_floor * scale
        reliable = np.flatnonzero(np.abs(s2) > tol)
        if len(reliable):
            signs = np.sign(s2[reliable])
            changed = np.flatnonzero(signs[1:] != signs[:-1]) + 1
            changes = int(len(changed))
            crossing_text = ",".join(f"{p[reliable[k]]:.6g}" for k in changed)
            first_sign = float(signs[0])
            last_sign = float(signs[-1])
        else:
            changes = 0
            crossing_text = ""
            first_sign = last_sign = 0.0
        minimum_index = int(np.argmin(s2))
        summaries.append(
            (
                changes,
                t,
                float(s2[0] / scale),
                float(np.min(s2) / scale),
                first_sign,
                last_sign,
                float(p[minimum_index]),
                crossing_text,
            )
        )

    max_changes = max(row[0] for row in summaries)
    negative_endpoints = sum(row[2] < -args.relative_floor for row in summaries)
    print(
        "heights", len(summaries),
        "max robust crossings", max_changes,
        "negative endpoints", negative_endpoints,
        "relative floor", args.relative_floor,
    )
    interesting = [row for row in summaries if row[0] or row[2] < -args.relative_floor]
    interesting.sort(key=lambda row: (-row[0], row[3]))
    for changes, t, endpoint, minimum, first_sign, last_sign, p_min, crossing_text in interesting[: args.show]:
        print(
            f"T={t:.9g} crossings={changes} endpoint/scale={endpoint:+.9e} "
            f"min/scale={minimum:+.9e} at P={p_min:.6g} "
            f"reliable signs={first_sign:+.0f}->{last_sign:+.0f} "
            f"crossings near [{crossing_text}]"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--t-min", type=float, default=0.025)
    parser.add_argument("--t-max", type=float, default=200.0)
    parser.add_argument("--t-step", type=float, default=0.25)
    parser.add_argument("--p-max", type=float, default=10.0)
    parser.add_argument("--wedge-pad", type=float, default=3.0)
    parser.add_argument("--margin", type=float, default=45.0)
    parser.add_argument("--dx", type=float, default=0.025)
    parser.add_argument("--dps", type=int, default=30)
    parser.add_argument("--backend", choices=("arb", "mpmath"), default="arb")
    parser.add_argument("--relative-floor", type=float, default=1e-8)
    parser.add_argument("--show", type=int, default=80)
    scan(parser.parse_args())
