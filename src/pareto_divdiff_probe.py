"""Numerical checks for the higher-order Pareto carrier.

The checks in this module are diagnostics, not a zero-free theorem.  They
verify the exact positivity/smoothing identities used in the accompanying
R93 report and expose the first derivative jump which a finite divided
difference cannot remove.
"""
from __future__ import annotations

import argparse
import cmath
import math
from collections.abc import Sequence


def _check_nodes(nodes: Sequence[float]) -> tuple[float, ...]:
    checked = tuple(float(r) for r in nodes)
    if not checked:
        raise ValueError("at least one Pareto parameter is required")
    if any(not 1.0 < r <= 2.0 for r in checked):
        raise ValueError("the positive Pareto range is 1 < r <= 2")
    if any(a >= b for a, b in zip(checked, checked[1:])):
        raise ValueError("probe nodes must be strictly increasing")
    return checked


def divided_difference(nodes: Sequence[float], values: Sequence[complex]) -> complex:
    """Return the Newton divided difference on distinct ordered nodes."""

    if len(nodes) != len(values) or not nodes:
        raise ValueError("nodes and values must have the same positive length")
    row = [complex(value) for value in values]
    for order in range(1, len(nodes)):
        row = [
            (row[j + 1] - row[j]) / (nodes[j + order] - nodes[j])
            for j in range(len(row) - 1)
        ]
    return row[0]


def pareto_carrier(r: float, x: float) -> float:
    """Evaluate A_r(x) from its finite power-sum formula."""

    if not 1.0 < r <= 2.0:
        raise ValueError("the positive Pareto range is 1 < r <= 2")
    if x < 1.0:
        raise ValueError("x must be at least 1")
    nmax = math.floor(x)
    p = r - 1.0
    power_sum = math.fsum(n**p for n in range(1, nmax + 1))
    return (r * x ** (-p) * power_sum - nmax) / p


def pareto_divided_carrier(nodes: Sequence[float], x: float) -> float:
    """Evaluate (-1)^k [r_0,...,r_k] A_r(x)."""

    checked = _check_nodes(nodes)
    order = len(checked) - 1
    value = divided_difference(checked, [pareto_carrier(r, x) for r in checked])
    return float(((-1) ** order * value).real)


def sector_u_derivative(r: float, nmax: int, u: float, order: int) -> float:
    """One-sided u derivative in the sector floor(exp(u)) = nmax.

    Passing ``nmax=N-1`` or ``nmax=N`` at ``u=log(N)`` gives the two
    traces needed to check the integer-knot jump.
    """

    if order < 0 or nmax < 0:
        raise ValueError("order and nmax must be nonnegative")
    p = r - 1.0
    power_sum = math.fsum(n**p for n in range(1, nmax + 1))
    if order == 0:
        return (r * math.exp(-p * u) * power_sum - nmax) / p
    return ((-1) ** order) * r * p ** (order - 1) * math.exp(-p * u) * power_sum


def divided_sector_u_derivative(
    nodes: Sequence[float], nmax: int, u: float, order: int
) -> float:
    """The corresponding one-sided derivative of the divided carrier."""

    checked = _check_nodes(nodes)
    k = len(checked) - 1
    values = [sector_u_derivative(r, nmax, u, order) for r in checked]
    return float((((-1) ** k) * divided_difference(checked, values)).real)


def knot_jump(nodes: Sequence[float], integer: int, derivative_order: int) -> float:
    """Return the right-minus-left derivative jump at u=log(integer)."""

    if integer < 2:
        raise ValueError("an interior integer knot must be at least 2")
    u = math.log(integer)
    right = divided_sector_u_derivative(nodes, integer, u, derivative_order)
    left = divided_sector_u_derivative(nodes, integer - 1, u, derivative_order)
    return right - left


def closed_laplace(nodes: Sequence[float], s: complex) -> complex:
    """Closed transform (s-1) zeta(s) / (s product(s+r_j-1))."""

    import mpmath as mp

    checked = _check_nodes(nodes)
    z = mp.mpc(s)
    denominator = z
    for r in checked:
        denominator *= z + (r - 1.0)
    return complex((z - 1) * mp.zeta(z) / denominator)


def truncated_piecewise_laplace(
    nodes: Sequence[float], s: complex, intervals: int = 4000
) -> complex:
    """Integrate exactly on the first integer intervals in the x variable."""

    checked = _check_nodes(nodes)
    z = complex(s)
    if z.real <= 1.0:
        raise ValueError("the simple truncation check is intended for Re(s) > 1")
    base_values: list[complex] = []
    for r in checked:
        p = r - 1.0
        power_sum = 0.0
        total = 0.0j
        for n in range(1, intervals + 1):
            power_sum += n**p
            upper = n + 1.0
            power_piece = (
                r
                * power_sum
                * (n ** (-(z + p)) - upper ** (-(z + p)))
                / (z + p)
            )
            floor_piece = n * (n ** (-z) - upper ** (-z)) / z
            total += (power_piece - floor_piece) / p
        base_values.append(total)
    order = len(checked) - 1
    return ((-1) ** order) * divided_difference(checked, base_values)


def weighted_jump_mass(sigma: float, cutoff: int) -> float:
    """Sum of the unavoidable jumps n^{-sigma} through ``cutoff``."""

    if cutoff < 2:
        return 0.0
    return math.fsum(n ** (-sigma) for n in range(2, cutoff + 1))


def run_probe(nodes: Sequence[float], xmax: int, samples: int, sigma: float) -> None:
    checked = _check_nodes(nodes)
    values: list[float] = []
    for n in range(1, xmax + 1):
        for j in range(samples):
            x = n + (j + 0.5) / samples
            values.append(pareto_divided_carrier(checked, x))
    order = len(checked) - 1
    print(f"nodes={checked}, order={order}")
    print(f"sampled carrier range: [{min(values):.12g}, {max(values):.12g}]")
    if order:
        print("knot jumps at u=log(17):")
        for derivative in range(order + 1):
            print(f"  derivative {derivative}: {knot_jump(checked, 17, derivative):+.12g}")
    for cutoff in (100, 1000, 10000):
        mass = weighted_jump_mass(sigma, cutoff)
        print(f"sum_(n<={cutoff}) n^(-{sigma:g}) = {mass:.12g}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodes", nargs="+", type=float, default=[1.2, 1.5, 2.0])
    parser.add_argument("--xmax", type=int, default=100)
    parser.add_argument("--samples", type=int, default=20)
    parser.add_argument("--sigma", type=float, default=0.9)
    args = parser.parse_args()
    run_probe(args.nodes, args.xmax, args.samples, args.sigma)


if __name__ == "__main__":
    main()
