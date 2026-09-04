"""Weighted ``q^2`` principal-channel ledgers for the QP carry matrix.

The unweighted physical carrier has a genuine logarithmic (coarse Hankel)
polar mode.  For the coefficient-normalized four-cycle matrix this mode is
small for a much simpler reason.  If ``P_c`` is the coarse color layer, then

    A_0 = (D/q) * sum_c z_c P_c.

Every ``P_c`` has bounded row and column degree and ``O(q)`` entries, while
every matrix cell belongs to only boundedly many coarse layers.  Hence

    ||A_0||_op  << D/sqrt(q) ||z||_2,
    ||A_0||_HS^2 << D^2/q ||z||_2^2,
    ||A_0||_S4^4 << D^4/q^2 ||z||_2^4.

At ``q=D^(33/16)`` the last factor is ``D^(-1/8)``.  The routines below
record the exact finite matrix inequality and the exponent conversion.  They
do not assert the primitive-channel square function or the full four-cycle
theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class CoarseLayerBounds:
    """Combinatorial parameters for a family of coarse color layers."""

    shell_size: int
    max_layer_degree: int
    max_layer_entries: int
    max_cell_overlap: int


def weighted_coarse_matrix(
    layers: np.ndarray,
    weights: np.ndarray,
    scale: float,
) -> np.ndarray:
    """Return ``scale * sum_c weights[c] * layers[c]``.

    ``layers`` has shape ``(number_of_colors, rows, columns)``.  This finite
    helper is deliberately agnostic about how the exact smooth coarse mask
    was constructed.
    """

    array = np.asarray(layers)
    z = np.asarray(weights)
    if array.ndim != 3:
        raise ValueError("layers must be a three-dimensional array")
    if z.ndim != 1 or z.size != array.shape[0]:
        raise ValueError("one weight is required for every color layer")
    return float(scale) * np.tensordot(z, array, axes=(0, 0))


def exact_schatten_fourth_power(matrix: np.ndarray) -> float:
    """Return ``tr((A* A)^2)``."""

    a = np.asarray(matrix)
    gram = a.conj().T @ a
    return float(np.trace(gram @ gram).real)


def coarse_principal_upper_bounds(
    q: float,
    D: float,
    z_l2: float,
    bounds: CoarseLayerBounds,
) -> tuple[float, float, float]:
    """Return the elementary ``(op, HS^2, S4^4)`` upper bounds.

    The harmless absolute factor ``2`` in the exact principal coefficient
    can be included by replacing ``D`` with ``2D`` at the call site.
    """

    if q <= 0 or D <= 0 or z_l2 < 0:
        raise ValueError("q,D must be positive and z_l2 nonnegative")
    if min(
        bounds.shell_size,
        bounds.max_layer_degree,
        bounds.max_layer_entries,
        bounds.max_cell_overlap,
    ) < 0:
        raise ValueError("combinatorial bounds must be nonnegative")

    scale = D / q
    # Triangle inequality and Schur on every individual color layer.
    op = (
        scale
        * bounds.max_layer_degree
        * bounds.shell_size**0.5
        * z_l2
    )
    # Cellwise Cauchy, followed by summation over the color layers.
    hs2 = (
        scale**2
        * bounds.max_cell_overlap
        * bounds.max_layer_entries
        * z_l2**2
    )
    s4_fourth = op**2 * hs2
    return op, hs2, s4_fourth


def project_scale_exponents() -> dict[str, float]:
    """Return powers of ``D`` in the ideal project-scale coarse bounds."""

    # q = D^(33/16), |S| = q^(1+o(1)), and all local constants are q^o(1).
    q_power = 33.0 / 16.0
    return {
        "operator": 1.0 - q_power / 2.0,
        "hilbert_schmidt_squared": 2.0 - q_power,
        "schatten_fourth": 4.0 - 2.0 * q_power,
    }

