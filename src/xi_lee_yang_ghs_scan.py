#!/usr/bin/env python3
"""Lightweight falsification scan for a ferromagnetic Lee--Yang model of xi.

For the normalized moment generating function

    M(h) = xi(1/2 + h) / xi(1/2),

the GHS inequality for a standard ferromagnetic total magnetization would
require

    d^3/dh^3 log M(h) <= 0  for h >= 0.

This script only scans that necessary condition.  A negative scan is not a
proof of the inequality, and satisfying GHS is far weaker than the Lee--Yang
zero-location property.
"""

from __future__ import annotations

import argparse

import mpmath as mp


def pole_removed_zeta(s: mp.mpf) -> mp.mpf:
    """Return (s - 1) zeta(s), using its removable value at s = 1."""

    if s == 1:
        return mp.mpf(1)
    return (s - 1) * mp.zeta(s)


def riemann_xi(s: mp.mpf) -> mp.mpf:
    """Riemann's completed xi on the positive real axis."""

    return (
        mp.mpf("0.5")
        * s
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * pole_removed_zeta(s)
    )


def ghs_density(h: mp.mpf) -> mp.mpf:
    """Third h derivative of log xi(1/2+h)."""

    return mp.diff(lambda x: mp.log(riemann_xi(mp.mpf("0.5") + x)), h, 3)


def linear_grid(start: mp.mpf, stop: mp.mpf, count: int) -> list[mp.mpf]:
    if count <= 1:
        return [start]
    return [start + (stop - start) * k / (count - 1) for k in range(count)]


def geometric_grid(start: mp.mpf, stop: mp.mpf, count: int) -> list[mp.mpf]:
    if start <= 0:
        raise ValueError("geometric grid requires a positive lower endpoint")
    if count <= 1:
        return [start]
    ratio = mp.power(stop / start, mp.mpf(1) / (count - 1))
    return [start * mp.power(ratio, k) for k in range(count)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--h-min", type=str, default="0.01")
    parser.add_argument("--h-max", type=str, default="100")
    parser.add_argument("--linear-samples", type=int, default=101)
    parser.add_argument("--log-samples", type=int, default=101)
    parser.add_argument("--dps", type=int, default=60)
    args = parser.parse_args()

    mp.mp.dps = args.dps
    h_min = mp.mpf(args.h_min)
    h_max = mp.mpf(args.h_max)
    if not (0 < h_min <= h_max):
        raise ValueError("require 0 < h-min <= h-max")

    points = set(linear_grid(h_min, h_max, args.linear_samples))
    points.update(geometric_grid(h_min, h_max, args.log_samples))
    # Include the removable zeta-pole location as a stability check.
    if h_min <= mp.mpf("0.5") <= h_max:
        points.add(mp.mpf("0.5"))

    values = sorted((ghs_density(h), h) for h in points)
    minimum, h_at_minimum = values[0]
    maximum, h_at_maximum = values[-1]

    print(f"samples: {len(values)}")
    print(f"minimum: {mp.nstr(minimum, 24)} at h={mp.nstr(h_at_minimum, 16)}")
    print(f"maximum: {mp.nstr(maximum, 24)} at h={mp.nstr(h_at_maximum, 16)}")
    print("GHS sign violation found:", maximum > 0)


if __name__ == "__main__":
    main()
