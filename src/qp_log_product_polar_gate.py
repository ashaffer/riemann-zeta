"""Finite identities for the logarithmic product-polar audit."""

from __future__ import annotations

from dataclasses import dataclass
from math import log
from typing import Iterable, Sequence

import numpy as np


def triangle_adjacency(size: int, triangles: Iterable[Sequence[int]]) -> np.ndarray:
    """Return the simple two-section adjacency of edge-disjoint triangles."""

    matrix = np.zeros((size, size), dtype=float)
    for raw_triangle in triangles:
        triangle = tuple(int(index) for index in raw_triangle)
        if len(triangle) != 3 or len(set(triangle)) != 3:
            raise ValueError("triangles must contain three distinct vertices")
        for i in range(3):
            for j in range(3):
                if i != j:
                    matrix[triangle[i], triangle[j]] += 1.0
    return matrix


@dataclass(frozen=True)
class LogRayleighIdentity:
    matrix_quadratic: float
    triangle_quadratic: float
    negative_mass: float
    residual_square_mass: float


def log_rayleigh_identity(
    log_values: Sequence[float], triangles: Iterable[Sequence[int]]
) -> LogRayleighIdentity:
    """Replay ``x^T T x=sum_tau[(sum_tau x)^2-sum_tau x^2]``."""

    values = np.asarray(log_values, dtype=float)
    triangle_list = [tuple(int(index) for index in triangle) for triangle in triangles]
    matrix = triangle_adjacency(values.size, triangle_list)
    matrix_quadratic = float(values @ matrix @ values)
    negative_mass = 0.0
    residual_square_mass = 0.0
    for triangle in triangle_list:
        local = values[list(triangle)]
        negative_mass += float(local @ local)
        residual_square_mass += float(np.sum(local) ** 2)
    return LogRayleighIdentity(
        matrix_quadratic=matrix_quadratic,
        triangle_quadratic=residual_square_mass - negative_mass,
        negative_mass=negative_mass,
        residual_square_mass=residual_square_mass,
    )


def physical_log_values(nodes: Sequence[int], q: int) -> np.ndarray:
    """The product-linearizing coordinate ``log(2s/q)``."""

    return np.log(2.0 * np.asarray(nodes, dtype=float) / float(q))


def residual_log_error(q: int, degree_parameter: int) -> float:
    """Uniform bound for ``|log(8abc/q^3)|`` in the fine window."""

    eta = float(degree_parameter) / float(q * q)
    if eta >= 0.5:
        raise ValueError("the elementary logarithmic bound needs eta<1/2")
    return eta / (1.0 - eta)


def product_mean_boundary_lower_bound(
    *,
    triangle_count: int,
    log_center_separation: float,
    log_block_radius: float,
    shell_log_diameter: float,
) -> float:
    """Continuous boundary lower bound from two equal-size product covers."""

    if shell_log_diameter <= 0:
        raise ValueError("shell_log_diameter must be positive")
    signal = triangle_count * (
        abs(log_center_separation) - 2.0 * abs(log_block_radius)
    )
    return max(0.0, signal / shell_log_diameter)


@dataclass(frozen=True)
class CoarseWeightedBounds:
    hilbert_schmidt_squared: float
    operator_norm: float
    schatten_four_fourth: float


def coarse_weighted_bounds(
    *,
    q: int,
    degree_parameter: int,
    layer_entry_cap: int,
    cell_overlap_cap: int,
    row_degree_cap: int,
    z_l1: float,
    z_l2: float,
    principal_constant: float = 2.0,
) -> CoarseWeightedBounds:
    """Schur/HS bounds for the weighted mod-q^2 principal coarse operator."""

    scale = principal_constant * degree_parameter / q
    hs_squared = (
        scale**2 * cell_overlap_cap * layer_entry_cap * z_l2**2
    )
    operator = scale * row_degree_cap * z_l1
    return CoarseWeightedBounds(
        hilbert_schmidt_squared=hs_squared,
        operator_norm=operator,
        schatten_four_fourth=operator**2 * hs_squared,
    )


def centered_log_rayleigh_lower_bound(
    *,
    weighted_triangle_log_mass: float,
    triangle_count: int,
    log_error: float,
    log_norm_squared: float,
) -> float:
    """Lower bound for the empirical-centered all-distinct carrier norm."""

    if log_norm_squared <= 0:
        raise ValueError("log_norm_squared must be positive")
    numerator = weighted_triangle_log_mass - triangle_count * log_error**2
    return max(0.0, numerator / log_norm_squared)

