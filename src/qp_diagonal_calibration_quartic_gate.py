"""Exact algebra for the diagonal calibrated quartic gate.

Only finite-dimensional identities are certified here.  No arithmetic
estimate for the actual prime-power cubic tensor is encoded.
"""

from __future__ import annotations

from itertools import product

import numpy as np


def cubic_value(tensor: np.ndarray, x: np.ndarray) -> float:
    """Evaluate a real cubic tensor on the diagonal."""

    return float(np.einsum("ijk,i,j,k->", tensor, x, x, x))


def trilinear_value(
    tensor: np.ndarray, x: np.ndarray, y: np.ndarray, z: np.ndarray
) -> float:
    return float(np.einsum("ijk,i,j,k->", tensor, x, y, z))


def calibrated_quartic(a: np.ndarray, tensor: np.ndarray, x: np.ndarray) -> float:
    """Return ``(a.x) T(x,x,x)``."""

    return float(a @ x) * cubic_value(tensor, x)


def active_leverage_skew_product(
    a: np.ndarray, tensor: np.ndarray, x: np.ndarray
) -> float:
    """Return ``[-a.x]_+[-T(x,x,x)]_+``."""

    return max(0.0, -float(a @ x)) * max(0.0, -cubic_value(tensor, x))


def symmetrized_rank_one_quartic(a: np.ndarray, tensor: np.ndarray) -> np.ndarray:
    """Build the symmetric four-tensor associated with ``(a.x)T(x^3)``."""

    term0 = np.einsum("i,jkl->ijkl", a, tensor)
    term1 = np.einsum("j,ikl->ijkl", a, tensor)
    term2 = np.einsum("k,ijl->ijkl", a, tensor)
    term3 = np.einsum("l,ijk->ijkl", a, tensor)
    return (term0 + term1 + term2 + term3) / 4.0


def polarization_replay(
    tensor: np.ndarray, x: np.ndarray, y: np.ndarray, z: np.ndarray
) -> float:
    """Recover a symmetric trilinear value from its diagonal cubic."""

    total = 0.0
    vectors = (x, y, z)
    for signs in product((-1.0, 1.0), repeat=3):
        combined = sum(sign * vector for sign, vector in zip(signs, vectors))
        total += float(np.prod(signs)) * cubic_value(tensor, combined)
    return total / 48.0


def singleton_residual(log_nodes: np.ndarray, selected: int, odd: int = 1) -> np.ndarray:
    """Return the exactly calibrated ``D=1`` singleton residual."""

    if odd <= 0 or odd % 2 == 0:
        raise ValueError("odd must be a positive odd integer")
    selected_log = abs(float(log_nodes[selected]))
    if selected_log == 0.0:
        raise ValueError("selected node must differ from the center")
    t0 = odd * np.pi / selected_log
    return 1.0 + np.cos(t0 * log_nodes)


def positive_core_legal_value(
    tensor: np.ndarray, v: np.ndarray, x_nonnegative: np.ndarray
) -> tuple[float, float]:
    """Orient a nonnegative vector into the legal negative half-space."""

    if np.any(tensor < 0) or np.any(v < 0) or np.any(x_nonnegative < 0):
        raise ValueError("tensor, residual, and vector must be nonnegative")
    norm = float(np.linalg.norm(x_nonnegative))
    if norm == 0.0:
        raise ValueError("vector must be nonzero")
    x = x_nonnegative / norm
    y = -x
    return float(y @ v), -cubic_value(tensor, y)

