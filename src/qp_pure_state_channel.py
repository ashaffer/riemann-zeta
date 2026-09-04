"""Exact completely-positive-channel form of the QP four-cycle target.

For a finite carry tensor ``kappa[a,b,c]`` put ``P_b[a,c]=kappa[a,b,c]``
and

    Phi(X) = sum_b P_b X P_b^*.

If ``A_z[a,b]=sum_c kappa[a,b,c] z[c]``, then

    A_z A_z^* = Phi(z z^*)

and the fourth Schatten mass is ``||Phi(z z^*)||_HS^2``.  The routines in
this module replay that identity, its row-pair/color-pair ``H`` form, and
the residual-modulation decomposition.  They make no asymptotic claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np


def _carry_tensor(kappa: np.ndarray | Sequence[complex]) -> np.ndarray:
    tensor = np.asarray(kappa, dtype=complex)
    if tensor.ndim != 3:
        raise ValueError("kappa must have axes (row, carrier, color)")
    return tensor


def weighted_carry_matrix(
    kappa: np.ndarray | Sequence[complex], z: np.ndarray | Sequence[complex]
) -> np.ndarray:
    """Return ``A_z[a,b]=sum_c kappa[a,b,c] z[c]``."""

    tensor = _carry_tensor(kappa)
    vector = np.asarray(z, dtype=complex)
    if vector.ndim != 1 or vector.size != tensor.shape[2]:
        raise ValueError("z has the wrong color dimension")
    return np.einsum("abc,c->ab", tensor, vector)


def pure_state_channel(
    kappa: np.ndarray | Sequence[complex], z: np.ndarray | Sequence[complex]
) -> np.ndarray:
    """Return ``Phi(z z^*)=sum_b P_b z z^* P_b^*``."""

    tensor = _carry_tensor(kappa)
    vector = np.asarray(z, dtype=complex)
    if vector.ndim != 1 or vector.size != tensor.shape[2]:
        raise ValueError("z has the wrong color dimension")
    state = np.outer(vector, vector.conj())
    return np.einsum("abc,cd,ebd->ae", tensor, state, tensor.conj())


def cross_state_channel(
    kappa: np.ndarray | Sequence[complex],
    x: np.ndarray | Sequence[complex],
    y: np.ndarray | Sequence[complex],
) -> np.ndarray:
    """Return ``Phi(x y^*)``.

    The Kraus Gram identity gives

    ``||Phi(x y^*)||_HS^2 <= ||Phi(x x^*)||_HS ||Phi(y y^*)||_HS``.

    Consequently a uniform pure-state bound for this completely positive
    map automatically extends, with no constant loss, from positive rank-one
    matrices to all trace-class inputs by singular-value decomposition.
    """

    left = np.asarray(x, dtype=complex)
    right = np.asarray(y, dtype=complex)
    if left.ndim != 1 or right.ndim != 1 or left.shape != right.shape:
        raise ValueError("x and y must have the same one-dimensional shape")
    return channel_apply(kappa, np.outer(left, right.conj()))


def kraus_cross_cauchy_ledger(
    kappa: np.ndarray | Sequence[complex],
    x: np.ndarray | Sequence[complex],
    y: np.ndarray | Sequence[complex],
) -> tuple[float, float]:
    """Return the two sides of the exact Kraus Gram Cauchy inequality."""

    cross = cross_state_channel(kappa, x, y)
    pure_x = pure_state_channel(kappa, x)
    pure_y = pure_state_channel(kappa, y)
    left = float(np.vdot(cross, cross).real)
    right = float(
        np.sqrt(np.vdot(pure_x, pure_x).real * np.vdot(pure_y, pure_y).real)
    )
    return left, right


def channel_apply(
    kappa: np.ndarray | Sequence[complex], matrix: np.ndarray
) -> np.ndarray:
    """Apply ``Phi(X)=sum_b P_b X P_b^*`` to an arbitrary color matrix."""

    tensor = _carry_tensor(kappa)
    value = np.asarray(matrix, dtype=complex)
    colors = tensor.shape[2]
    if value.shape != (colors, colors):
        raise ValueError("matrix has the wrong color dimensions")
    return np.einsum("abc,cd,ebd->ae", tensor, value, tensor.conj())


def channel_adjoint_apply(
    kappa: np.ndarray | Sequence[complex], matrix: np.ndarray
) -> np.ndarray:
    """Apply ``Phi^*(Y)=sum_b P_b^* Y P_b`` to a row matrix."""

    tensor = _carry_tensor(kappa)
    value = np.asarray(matrix, dtype=complex)
    rows = tensor.shape[0]
    if value.shape != (rows, rows):
        raise ValueError("matrix has the wrong row dimensions")
    return np.einsum("abc,ae,ebd->cd", tensor.conj(), value, tensor)


def pair_incidence_operator(kappa: np.ndarray | Sequence[complex]) -> np.ndarray:
    r"""Return the flattened row-pair/color-pair incidence ``H``.

    With row-pair index ``(a,e)`` and color-pair index ``(c,d)``,

    ``H[(a,e),(c,d)] = sum_b kappa[a,b,c] conj(kappa[e,b,d])``.
    """

    tensor = _carry_tensor(kappa)
    rows, _, colors = tensor.shape
    four_tensor = np.einsum("abc,ebd->aecd", tensor, tensor.conj())
    return four_tensor.reshape(rows * rows, colors * colors)


def pure_pair_vector(z: np.ndarray | Sequence[complex]) -> np.ndarray:
    """Vectorize ``z z^*`` in the convention used by ``H``."""

    vector = np.asarray(z, dtype=complex)
    if vector.ndim != 1:
        raise ValueError("z must be one-dimensional")
    return np.outer(vector, vector.conj()).reshape(-1)


def fourth_schatten_mass(matrix: np.ndarray) -> float:
    """Return ``tr((A A^*)^2)=||A A^*||_HS^2``."""

    value = np.asarray(matrix, dtype=complex)
    if value.ndim != 2:
        raise ValueError("matrix must be two-dimensional")
    gram = value @ value.conj().T
    return float(np.vdot(gram, gram).real)


def channel_fourth_mass(
    kappa: np.ndarray | Sequence[complex], z: np.ndarray | Sequence[complex]
) -> float:
    """Return the same fourth mass through the pure-state channel."""

    image = pure_state_channel(kappa, z)
    return float(np.vdot(image, image).real)


def residual_layers(
    kappa: np.ndarray | Sequence[complex],
    row_values: Sequence[int],
    color_values: Sequence[int],
) -> dict[int, np.ndarray]:
    r"""Split ``H`` by ``h=a*c-a'*c'``.

    The returned matrices have the same flattened shape as ``H``.  Their
    sum is exactly ``H``.  For a strict coprime shell the nonzero support of
    each layer is a partial matching, but this routine does not assume that
    arithmetic hypothesis.
    """

    tensor = _carry_tensor(kappa)
    rows, _, colors = tensor.shape
    if len(row_values) != rows or len(color_values) != colors:
        raise ValueError("coordinate values have the wrong dimensions")
    base = np.einsum("abc,ebd->aecd", tensor, tensor.conj())
    layers: dict[int, np.ndarray] = {}
    for a in range(rows):
        for e in range(rows):
            for c in range(colors):
                for d in range(colors):
                    coefficient = base[a, e, c, d]
                    if coefficient == 0:
                        continue
                    shift = row_values[a] * color_values[c] - row_values[e] * color_values[d]
                    layer = layers.setdefault(
                        int(shift), np.zeros((rows * rows, colors * colors), dtype=complex)
                    )
                    layer[a * rows + e, c * colors + d] = coefficient
    return layers


@dataclass(frozen=True)
class PureStateChannelLedger:
    """Numerical replay of all exact channel representations."""

    fourth_mass: float
    channel_mass: float
    pair_operator_mass: float
    residual_zero_mass: float
    residual_average_mass: float
    pure_trace_norm: float


def channel_ledger(
    kappa: np.ndarray | Sequence[complex],
    z: np.ndarray | Sequence[complex],
    *,
    row_values: Sequence[int] | None = None,
    color_values: Sequence[int] | None = None,
) -> PureStateChannelLedger:
    """Compute the fourth trace, channel, ``H``, and residual ledgers."""

    tensor = _carry_tensor(kappa)
    vector = np.asarray(z, dtype=complex)
    matrix = weighted_carry_matrix(tensor, vector)
    image = pure_state_channel(tensor, vector)
    h_operator = pair_incidence_operator(tensor)
    pair = pure_pair_vector(vector)
    h_image = h_operator @ pair
    if row_values is None:
        row_values = tuple(range(tensor.shape[0]))
    if color_values is None:
        color_values = tuple(range(tensor.shape[2]))
    layers = residual_layers(tensor, row_values, color_values)
    layer_images = [layer @ pair for layer in layers.values()]
    residual_zero = sum(layer_images, np.zeros_like(h_image))
    residual_average = sum(float(np.vdot(value, value).real) for value in layer_images)
    return PureStateChannelLedger(
        fourth_mass=fourth_schatten_mass(matrix),
        channel_mass=float(np.vdot(image, image).real),
        pair_operator_mass=float(np.vdot(h_image, h_image).real),
        residual_zero_mass=float(np.vdot(residual_zero, residual_zero).real),
        residual_average_mass=residual_average,
        pure_trace_norm=float(np.vdot(vector, vector).real),
    )
