"""Collision-stable packet Grams and the two-lobe mirror invariant.

This module is a small numerical companion to the exact formulas in
``results/ZETA23-NEAR-TIE-GRAM-AND-MIRROR-ALIGNMENT-2026-08-12.md``.
It deliberately contains no zeta zeros and makes no zero-free claim.

The packet row convention is

    e_(alpha,gamma)(t) = exp((alpha - i gamma)t) / sqrt(M(2 alpha)),

on the centered interval ``[-width/2,width/2]``, where
``M(s)=integral exp(s t) dt``.  The exact normalized Gram determinant is
implemented by :func:`gram_determinant`.
"""

from __future__ import annotations

from dataclasses import dataclass
import cmath
import math

import numpy as np
from numpy.typing import NDArray


def _sinhc(z: complex) -> complex:
    """Return sinh(z)/z with a stable removable value at zero."""

    if abs(z) < 1.0e-5:
        z2 = z * z
        return 1.0 + z2 / 6.0 + z2 * z2 / 120.0 + z2 * z2 * z2 / 5040.0
    return cmath.sinh(z) / z


def interval_moment(s: complex, width: float) -> complex:
    """Return ``integral_(-w/2)^(w/2) exp(s t) dt``."""

    if width <= 0.0:
        raise ValueError("width must be positive")
    return width * _sinhc(0.5 * width * complex(s))


def tilted_mean(alpha: float, width: float) -> float:
    """Mean of t under density proportional to exp(2 alpha t)."""

    q = 2.0 * alpha
    a = 0.5 * width
    if abs(q * a) < 1.0e-5:
        # a*coth(aq)-1/q = a^2 q/3-a^4 q^3/45+...
        return a * a * q / 3.0 - a**4 * q**3 / 45.0
    return a / math.tanh(a * q) - 1.0 / q


def tilted_variance(alpha: float, width: float) -> float:
    """Variance of t under density proportional to exp(2 alpha t)."""

    q = 2.0 * alpha
    a = 0.5 * width
    if abs(q * a) < 1.0e-4:
        # 1/q^2-a^2*csch(aq)^2 = a^2/3-a^4 q^2/15+...
        return a * a / 3.0 - a**4 * q * q / 15.0
    return 1.0 / (q * q) - a * a / (math.sinh(a * q) ** 2)


def normalized_correlation(
    alpha0: float,
    gamma0: float,
    alpha1: float,
    gamma1: float,
    width: float,
) -> complex:
    """Exact correlation of two normalized Fourier--Laplace packet rows."""

    numerator = interval_moment(
        alpha0 + alpha1 + 1j * (gamma1 - gamma0), width
    )
    denominator = math.sqrt(
        interval_moment(2.0 * alpha0, width).real
        * interval_moment(2.0 * alpha1, width).real
    )
    return numerator / denominator


def gram_determinant(
    alpha0: float,
    gamma0: float,
    alpha1: float,
    gamma1: float,
    width: float,
) -> float:
    """Return the exact determinant of the normalized 2 by 2 Gram matrix."""

    correlation = normalized_correlation(
        alpha0, gamma0, alpha1, gamma1, width
    )
    value = 1.0 - abs(correlation) ** 2
    # Roundoff can make an exact collision very slightly negative.
    return max(0.0, float(value))


def collision_quadratic(
    mean_alpha: float, delta_alpha: float, delta_gamma: float, width: float
) -> float:
    """The quadratic collision prediction for the Gram determinant."""

    return tilted_variance(mean_alpha, width) * (
        delta_alpha * delta_alpha + delta_gamma * delta_gamma
    )


def gauss_packet(width: float, order: int = 160) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Gauss--Legendre nodes and weights on the centered packet."""

    if order < 2:
        raise ValueError("order must be at least two")
    nodes, weights = np.polynomial.legendre.leggauss(order)
    return 0.5 * width * nodes, 0.5 * width * weights


def sampled_normalized_row(
    alpha: float,
    gamma: float,
    width: float,
    order: int = 160,
) -> NDArray[np.complex128]:
    """Quadrature representation of one normalized packet row."""

    nodes, weights = gauss_packet(width, order)
    norm = math.sqrt(interval_moment(2.0 * alpha, width).real)
    return np.sqrt(weights) * np.exp((alpha - 1j * gamma) * nodes) / norm


def hermite_row(
    alpha: float,
    gamma: float,
    direction_alpha: float,
    direction_gamma: float,
    width: float,
    order: int = 160,
) -> NDArray[np.complex128]:
    """Unit centered Hermite tangent for a nonzero parameter direction."""

    radius = math.hypot(direction_alpha, direction_gamma)
    if radius == 0.0:
        raise ValueError("the collision direction must be nonzero")
    nodes, _ = gauss_packet(width, order)
    base = sampled_normalized_row(alpha, gamma, width, order)
    phase = (direction_alpha - 1j * direction_gamma) / radius
    row = phase * (nodes - tilted_mean(alpha, width)) * base
    return row / math.sqrt(tilted_variance(alpha, width))


def branch_gram(
    mean_alpha: float,
    mean_gamma: float,
    delta_alpha: float,
    delta_gamma: float,
    width: float,
    order: int = 160,
) -> NDArray[np.complex128]:
    """Gram of the four normalized ``+/-`` branches of two nearby pairs."""

    parameters = (
        (mean_alpha - 0.5 * delta_alpha, mean_gamma - 0.5 * delta_gamma),
        (mean_alpha + 0.5 * delta_alpha, mean_gamma + 0.5 * delta_gamma),
    )
    rows: list[NDArray[np.complex128]] = []
    for sign in (1.0, -1.0):
        for alpha, gamma in parameters:
            rows.append(sampled_normalized_row(sign * alpha, gamma, width, order))
    matrix = np.asarray(rows)
    return matrix @ matrix.conj().T


@dataclass(frozen=True)
class MirrorIdentity:
    residual: float
    cross_real: float
    negative_seed_mass: float


def mirror_cross_identity(
    free_rows: NDArray[np.complex128],
    seed_rows: NDArray[np.complex128],
    seed: NDArray[np.complex128],
) -> MirrorIdentity:
    """Solve all leading positive rows and evaluate the pure-cross identity.

    If ``U ell + V r = 0``, then

        Re <U ell, V r> = -||V r||^2.

    The row orientations and their mutual Gram matrix do not enter.
    """

    free_rows = np.asarray(free_rows, dtype=np.complex128)
    seed_rows = np.asarray(seed_rows, dtype=np.complex128)
    seed = np.asarray(seed, dtype=np.complex128)
    values = seed_rows @ seed
    free, *_ = np.linalg.lstsq(free_rows, -values, rcond=None)
    residual = float(np.linalg.norm(free_rows @ free + values))
    cross = float(np.vdot(free_rows @ free, values).real)
    mass = float(np.vdot(values, values).real)
    return MirrorIdentity(residual=residual, cross_real=cross, negative_seed_mass=mass)


@dataclass(frozen=True)
class PacketBlockRatios:
    same_lobe_norm: float
    cross_lobe_norm: float
    reverse_cross_norm: float

    @property
    def same_to_cross(self) -> float:
        return self.same_lobe_norm / self.cross_lobe_norm

    @property
    def reverse_to_cross(self) -> float:
        return self.reverse_cross_norm / self.cross_lobe_norm


def packet_block_ratios(
    alpha: float, separation: float, width: float, order: int = 100
) -> PacketBlockRatios:
    """Compute exact quadrature block ratios for one separated packet pair.

    The free packet is centered at ``-separation/2`` and the seed packet at
    ``+separation/2``.  The pair operator is ``a b^* + b a^*``, with
    ``a=exp(alpha t)`` and ``b=exp(-alpha t)``.
    """

    if alpha <= 0.0 or separation <= width:
        raise ValueError("require alpha>0 and disjoint separated packets")
    centered_nodes, weights = gauss_packet(width, order)
    left = centered_nodes - 0.5 * separation
    right = centered_nodes + 0.5 * separation
    root_weights = np.sqrt(weights)
    a_left = root_weights * np.exp(alpha * left)
    b_left = root_weights * np.exp(-alpha * left)
    a_right = root_weights * np.exp(alpha * right)
    b_right = root_weights * np.exp(-alpha * right)

    same = np.outer(a_left, np.conj(b_left)) + np.outer(
        b_left, np.conj(a_left)
    )
    dominant = np.outer(b_left, np.conj(a_right))
    reverse = np.outer(a_left, np.conj(b_right))
    cross = dominant + reverse

    return PacketBlockRatios(
        same_lobe_norm=float(np.linalg.norm(same, 2)),
        cross_lobe_norm=float(np.linalg.norm(cross, 2)),
        reverse_cross_norm=float(np.linalg.norm(reverse, 2)),
    )


if __name__ == "__main__":
    alpha = 0.30
    width = 1.0
    print("collision determinant / quadratic prediction")
    for epsilon in (1.0e-1, 5.0e-2, 2.5e-2, 1.25e-2):
        determinant = gram_determinant(
            alpha - epsilon / 2,
            -epsilon / 4,
            alpha + epsilon / 2,
            epsilon / 4,
            width,
        )
        prediction = collision_quadratic(alpha, epsilon, epsilon / 2, width)
        print(f"  eps={epsilon:.5g} ratio={determinant / prediction:.12f}")

    print("separated-packet block ratios")
    for separation in (8.0, 12.0, 16.0, 20.0):
        ratios = packet_block_ratios(alpha, separation, width)
        print(
            f"  D={separation:4.1f} same/cross={ratios.same_to_cross:.6e} "
            f"reverse/cross={ratios.reverse_to_cross:.6e}"
        )
