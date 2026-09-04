"""Numerical check of the polar-subtracted modular reduction for B_P.

This is a consistency probe, not an interval certificate.  It compares

  S_3(P,T) = 1/2 int_P^inf (p-P)^2 h_T(p) dp

computed from Phi with the exact boundary/tail expression obtained from

  R(u) = exp(u) theta(exp(4u)) - 2 cosh(u),
  C_T(d) = int R((w+d)/2) R((w-d)/2) cos(Tw) dw.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from numpy.polynomial.legendre import leggauss


def phi(x: np.ndarray) -> np.ndarray:
    """Full even Rodgers--Tao kernel, using its stable positive-half series."""
    x = np.abs(np.asarray(x, dtype=float))
    e4 = np.exp(4.0 * x)
    ans = np.zeros_like(x)
    for n in range(1, 16):
        ans += (
            2.0 * np.pi**2 * n**4 * np.exp(9.0 * x)
            - 3.0 * np.pi * n**2 * np.exp(5.0 * x)
        ) * np.exp(-np.pi * n * n * e4)
    return ans


def polar_remainder(x: np.ndarray) -> np.ndarray:
    """R=Theta-2cosh, evaluated without subtracting two large exponentials."""
    x = np.abs(np.asarray(x, dtype=float))
    e4 = np.exp(4.0 * x)
    theta_tail = np.zeros_like(x)
    for n in range(1, 16):
        theta_tail += np.exp(-np.pi * n * n * e4)
    return 2.0 * np.exp(x) * theta_tail - np.exp(-x)


def polar_remainder_prime(x: np.ndarray) -> np.ndarray:
    """Derivative of the even smooth function R."""
    x = np.asarray(x, dtype=float)
    ax = np.abs(x)
    e4 = np.exp(4.0 * ax)
    tail0 = np.zeros_like(ax)
    tail2 = np.zeros_like(ax)
    for n in range(1, 16):
        term = np.exp(-np.pi * n * n * e4)
        tail0 += term
        tail2 += n * n * term
    positive_derivative = (
        2.0 * np.exp(ax) * (tail0 - 4.0 * np.pi * e4 * tail2)
        + np.exp(-ax)
    )
    return np.sign(x) * positive_derivative


def gauss_interval(count: int, left: float, right: float) -> tuple[np.ndarray, np.ndarray]:
    nodes, weights = leggauss(count)
    scale = (right - left) / 2.0
    return (left + right) / 2.0 + scale * nodes, scale * weights


def cross_orbit(
    d: np.ndarray,
    t: float,
    w_nodes: np.ndarray,
    w_weights: np.ndarray,
) -> np.ndarray:
    """C_T(d), which is real because its w-integrand is even."""
    d = np.atleast_1d(d)[:, None]
    w = w_nodes[None, :]
    product = polar_remainder((w + d) / 2.0)
    product *= polar_remainder((w - d) / 2.0)
    return product @ (w_weights * np.cos(t * w_nodes))


def cross_orbit_derivative(
    p: float,
    t: float,
    w_nodes: np.ndarray,
    w_weights: np.ndarray,
) -> float:
    """Exact differentiated integrand for d/dP C_T(P)."""
    u = (w_nodes + p) / 2.0
    v = (w_nodes - p) / 2.0
    derivative = 0.5 * (
        polar_remainder_prime(u) * polar_remainder(v)
        - polar_remainder(u) * polar_remainder_prime(v)
    )
    return float(np.dot(w_weights * np.cos(t * w_nodes), derivative))


def direct_s3(p0: float, t: float, count: int) -> float:
    p, pw = gauss_interval(count, p0, 4.0)
    q, qw = gauss_interval(count, -4.0, 4.0)
    base = phi((p[:, None] + q[None, :]) / 2.0)
    base *= phi((p[:, None] - q[None, :]) / 2.0)
    h = base @ (qw * np.cos(t * q))
    return float(0.5 * np.dot(pw * (p - p0) ** 2, h))


def reduced_s3(p0: float, t: float, count: int, d_max: float) -> tuple[float, tuple[float, ...]]:
    d, dw = gauss_interval(count, p0, d_max)
    # R only has exponential tails.  The w interval must extend beyond d_max.
    w, ww = gauss_interval(2 * count, -(d_max + 25.0), d_max + 25.0)
    c = cross_orbit(d, t, w, ww)
    c_prime = cross_orbit_derivative(p0, t, w, ww)
    tail0 = float(np.dot(dw, c))
    tail2 = float(np.dot(dw * (d - p0) ** 2, c))
    terms = (
        -4.0 * c_prime,
        8.0 * (t * t - 1.0) * tail0,
        2.0 * (t * t + 1.0) ** 2 * tail2,
    )
    return sum(terms) / 1024.0, terms


def transform_check(t: float, count: int) -> tuple[float, float]:
    u, uw = gauss_interval(2 * count, -35.0, 35.0)
    z_from_phi = float(np.dot(uw, phi(u) * np.cos(t * u)))
    r_hat = float(np.dot(uw, polar_remainder(u) * np.cos(t * u)))
    z_from_remainder = -(t * t + 1.0) * r_hat / 16.0
    return z_from_phi, z_from_remainder


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=float, default=0.3)
    parser.add_argument("--T", type=float, default=2.0)
    parser.add_argument("--count", type=int, default=500)
    parser.add_argument("--d-max", type=float, default=35.0)
    args = parser.parse_args()

    direct = direct_s3(args.P, args.T, args.count)
    reduced, terms = reduced_s3(args.P, args.T, args.count, args.d_max)
    z_phi, z_remainder = transform_check(args.T, args.count)
    sample = np.linspace(0.0, 12.0, 1201)

    print("P", args.P, "T", args.T)
    print("direct S3", f"{direct:+.17e}")
    print("reduced S3", f"{reduced:+.17e}")
    print("relative discrepancy", f"{abs(direct-reduced)/max(abs(direct),1e-300):.6e}")
    print("1024-scaled reduced terms", *(f"{term:+.17e}" for term in terms))
    print("Z from Phi", f"{z_phi:+.17e}")
    print("Z from R", f"{z_remainder:+.17e}")
    print("max R on [0,12]", f"{np.max(polar_remainder(sample)):+.17e}")
