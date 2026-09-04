#!/usr/bin/env python3
"""Finite checks for the symmetrized consecutive-gap dispersion gate."""

from __future__ import annotations

import cmath
import math
from fractions import Fraction


KAPPA = Fraction(90_151_617, 5_000_000_000)


def check_prefix_identity() -> None:
    # Any strictly increasing fixture works; primality is irrelevant to the
    # telescoping identity itself.
    nodes = [101, 103, 109, 127, 131, 149, 151]
    gaps = [nodes[j + 1] - nodes[j] for j in range(len(nodes) - 1)]
    weights = [(gaps[j - 1] + gaps[j]) / 2 for j in range(1, len(nodes) - 1)]
    for left in range(1, len(nodes) - 1):
        for right in range(left, len(nodes) - 1):
            lhs = sum(weights[left - 1 : right])
            rhs = (nodes[right] + nodes[right + 1]) / 2 - (
                nodes[left - 1] + nodes[left]
            ) / 2
            assert lhs == rhs


def check_transition_identity() -> None:
    nodes = [101, 103, 109, 127, 131, 149, 151]
    q, a = 17, 5
    z = lambda n: cmath.exp(2j * math.pi * a * n / q)

    edge_form = 0j
    matrix = [[0 for _ in range(q)] for _ in range(q)]
    for p, pp in zip(nodes, nodes[1:]):
        gap = pp - p
        edge_form += gap * (z(p) + z(pp)) / 2
        matrix[p % q][pp % q] += gap

    matrix_form = 0j
    marginal_form = 0j
    for r in range(q):
        row = sum(matrix[r])
        col = sum(matrix[s][r] for s in range(q))
        marginal_form += (row + col) * z(r) / 2
        for s in range(q):
            matrix_form += matrix[r][s] * (z(r) + z(s)) / 2

    assert abs(edge_form - matrix_form) < 1e-10
    assert abs(edge_form - marginal_form) < 1e-10

    # A purely antisymmetric transition perturbation is invisible.
    anti = [[0 for _ in range(q)] for _ in range(q)]
    anti[3][8] = 7
    anti[8][3] = -7
    invisible = sum(
        anti[r][s] * (z(r) + z(s)) / 2 for r in range(q) for s in range(q)
    )
    assert abs(invisible) < 1e-10


def check_bonferroni_identity() -> None:
    for n in range(0, 30):
        for order in range(0, 30):
            truncated = sum(
                (-1) ** k * math.comb(n, k) for k in range(order + 1) if k <= n
            )
            remainder = 0
            if n >= 1 and order <= n - 1:
                remainder = (-1) ** (order + 1) * math.comb(n - 1, order)
            assert truncated + remainder == int(n == 0)


def check_order_scale() -> None:
    # Stirling-scale numerical sanity check: K log K/log Y tends to c for
    # K=c log Y/loglog Y.  This is not used as a proof of the asymptotic.
    c = float(KAPPA)
    for log_y in (10_000.0, 100_000.0, 1_000_000.0):
        order = max(2, int(c * log_y / math.log(log_y)))
        ratio = math.lgamma(order + 2) / log_y
        assert ratio < c
        # Convergence to the leading Stirling coefficient is slow because of
        # the lower-order logloglog term; a fixed factor four safely crosses
        # the requested exponent on these finite sanity fixtures.
        enlarged = max(order + 1, int(4 * c * log_y / math.log(log_y)))
        enlarged_ratio = math.lgamma(enlarged + 2) / log_y
        assert enlarged_ratio > c


def main() -> None:
    check_prefix_identity()
    check_transition_identity()
    check_bonferroni_identity()
    check_order_scale()
    print("PASS")
    print(f"kappa={float(KAPPA):.12f}")
    print("prefix_telescoping=exact")
    print("symmetric_transition_identity=exact")
    print("bonferroni_remainder=exact")
    print("poisson_absolute_order_scale=kappa*logY/loglogY")


if __name__ == "__main__":
    main()
