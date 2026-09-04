#!/usr/bin/env python3
"""Nodal-product obstruction for shallow QP-PROMOTE measures.

For a signed measure ``h`` of total variation at most one supported in
``[0, D]``, its cosine transform

    F(u) = integral cos(t u) dh(t)

satisfies ``|F^(M)| <= D^M``.  If it vanishes at the M actual prime-power
log nodes, the Lagrange remainder formula gives

    |F(u)| <= D^M / M! * product_n |u-u_n|.

This module evaluates the resulting (slightly relaxed) carrier bound using
the maximum nodal product.  Floating calculations are diagnostics; the
inequality itself is exact.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar


KAPPA_MIN = 0.0180303234
FULL_APERTURE_EXPONENT = 50.0 / 33.0
LOW_CUTOFF_EXPONENT = 0.01


def prime_powers(limit: int) -> list[int]:
    """Return all positive prime powers at most ``limit``."""
    if limit < 2:
        return []
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    values: set[int] = set()
    for p_value in np.flatnonzero(sieve):
        p = int(p_value)
        q = p
        while q <= limit:
            values.add(q)
            if q > limit // p:
                break
            q *= p
    return sorted(values)


def actual_nodes(y: float, width: float) -> np.ndarray:
    """Prime-power nodes ``log(n/y)`` in the audited multiplicative shell."""
    lower = y * math.exp(-width)
    upper = y * math.exp(width)
    nodes = [
        math.log(n / y)
        for n in prime_powers(math.ceil(upper))
        if lower <= n <= upper
    ]
    return np.asarray(nodes, dtype=float)


def carrier_mass(width: float, alpha: float) -> float:
    """Integral of the positive triangular carrier weight."""
    if abs(alpha) < 1e-14:
        return width
    return 2.0 * (math.cosh(alpha * width) - 1.0) / (
        width * alpha * alpha
    )


def cluster_collapse_feature_error(
    *, total_variation: float, width: float, node_count: int, diameter: float
) -> float:
    """L2 error after replacing a time cluster by its aggregate center atom."""
    return total_variation * width * diameter * math.sqrt(node_count)


def cluster_collapse_carrier_error(
    *, total_variation: float, width: float, alpha: float, diameter: float
) -> float:
    """Carrier error after the same cluster collapse."""
    return total_variation * width * carrier_mass(width, alpha) * diameter


def log_nodal_product(u: float, nodes: np.ndarray) -> float:
    distances = np.abs(nodes - u)
    if np.any(distances == 0.0):
        return -math.inf
    return float(np.sum(np.log(distances)))


def max_log_nodal_product(nodes: np.ndarray, width: float) -> tuple[float, float]:
    """Find the maximum nodal product on ``[-width,width]``.

    There is exactly one critical point of the product in every gap between
    consecutive real roots.  Bisection on the logarithmic derivative finds
    all of them.  The returned result is floating, not interval-certified.
    """
    if len(nodes) == 0:
        return 0.0, 0.0
    roots = np.sort(nodes)
    candidates = [-width, width]

    def logarithmic_derivative(u: float) -> float:
        return float(np.sum(1.0 / (u - roots)))

    for left, right in zip(roots[:-1], roots[1:]):
        lo = float(np.nextafter(left, right))
        hi = float(np.nextafter(right, left))
        # The logarithmic derivative is strictly decreasing from +inf to -inf.
        for _ in range(80):
            mid = (lo + hi) / 2.0
            if logarithmic_derivative(mid) > 0.0:
                lo = mid
            else:
                hi = mid
        candidates.append((lo + hi) / 2.0)

    values = [log_nodal_product(u, roots) for u in candidates]
    index = int(np.argmax(values))
    return float(values[index]), float(candidates[index])


def continuum_log_potential(u: float, width: float) -> float:
    """PNT-limit log potential for prime(-power) nodes."""
    normalization = 2.0 * math.sinh(width)

    def integrand(x: float) -> float:
        return math.exp(x) * math.log(abs(u - x)) / normalization

    if -width < u < width:
        left = quad(integrand, -width, u, points=[u], limit=300)[0]
        right = quad(integrand, u, width, points=[u], limit=300)[0]
        return float(left + right)
    return float(quad(integrand, -width, width, points=[u], limit=300)[0])


def continuum_potential_max(width: float) -> tuple[float, float, float]:
    """Return ``(max U, argmax U, 1/(e exp(max U)))``."""
    interior = minimize_scalar(
        lambda u: -continuum_log_potential(float(u), width),
        bounds=(-width, width),
        method="bounded",
        options={"xatol": 1e-13},
    )
    candidates = [
        (-width, continuum_log_potential(-width, width)),
        (width, continuum_log_potential(width, width)),
        (float(interior.x), -float(interior.fun)),
    ]
    argmax, value = max(candidates, key=lambda item: item[1])
    ratio = math.exp(-1.0 - value)
    return value, argmax, ratio


def log_relaxed_carrier_bound(
    *,
    max_log_product: float,
    node_count: int,
    cutoff: float,
    weight_mass: float,
) -> float:
    """Log of ``mass * cutoff^M/M! * max product``."""
    if cutoff <= 0.0:
        return -math.inf
    return (
        math.log(weight_mass)
        + node_count * math.log(cutoff)
        - math.lgamma(node_count + 1.0)
        + max_log_product
    )


def cutoff_frontier(
    *,
    y: float,
    kappa: float,
    max_log_product: float,
    node_count: int,
    weight_mass: float,
) -> float:
    """Cutoff where the relaxed upper bound equals ``y^(-kappa)``."""
    log_cutoff = (
        -kappa * math.log(y)
        - math.log(weight_mass)
        + math.lgamma(node_count + 1.0)
        - max_log_product
    ) / node_count
    return math.exp(log_cutoff)


@dataclass(frozen=True)
class Diagnostic:
    y: float
    node_count: int
    max_product_location: float
    max_log_product_per_node: float
    cutoff_frontier: float
    cutoff_frontier_over_nodes: float
    cutoff_frontier_exponent: float
    low_cutoff: float
    low_cutoff_log_bound: float
    target_log: float
    full_aperture: float


def diagnose(y: float, width: float, alpha: float, kappa: float) -> Diagnostic:
    nodes = actual_nodes(y, width)
    if len(nodes) == 0:
        raise ValueError("the shell has no prime-power nodes")
    max_log_product, location = max_log_nodal_product(nodes, width)
    mass = carrier_mass(width, alpha)
    frontier = cutoff_frontier(
        y=y,
        kappa=kappa,
        max_log_product=max_log_product,
        node_count=len(nodes),
        weight_mass=mass,
    )
    low = y**LOW_CUTOFF_EXPONENT
    low_log_bound = log_relaxed_carrier_bound(
        max_log_product=max_log_product,
        node_count=len(nodes),
        cutoff=low,
        weight_mass=mass,
    )
    return Diagnostic(
        y=y,
        node_count=len(nodes),
        max_product_location=location,
        max_log_product_per_node=max_log_product / len(nodes),
        cutoff_frontier=frontier,
        cutoff_frontier_over_nodes=frontier / len(nodes),
        cutoff_frontier_exponent=math.log(frontier) / math.log(y),
        low_cutoff=low,
        low_cutoff_log_bound=low_log_bound,
        target_log=-kappa * math.log(y),
        full_aperture=y**FULL_APERTURE_EXPONENT,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--Y", nargs="+", type=float, default=[300, 1000, 3000])
    parser.add_argument("--width", type=float, default=0.2)
    parser.add_argument("--alpha", type=float, default=0.49)
    parser.add_argument("--kappa", type=float, default=KAPPA_MIN)
    args = parser.parse_args()

    potential, location, ratio = continuum_potential_max(args.width)
    payload = {
        "schema": "qp-nodal-product-gate-v1",
        "polarity": "upper bound on shallow-support E; obstruction to PROMOTE only",
        "width": args.width,
        "alpha": args.alpha,
        "kappa": args.kappa,
        "continuum_max_log_potential": potential,
        "continuum_max_location": location,
        "continuum_cutoff_over_M": ratio,
        "rows": [asdict(diagnose(y, args.width, args.alpha, args.kappa)) for y in args.Y],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
