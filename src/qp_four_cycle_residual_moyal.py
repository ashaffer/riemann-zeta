"""Exact residual-modulation identities for the QP carry graph.

The direct multiplicative-Hankel fourth trace can be written as the squared
norm of a row-pair/color-pair incidence operator ``H``.  Its edges have the
integer residual label

``h = a*c - a_prime*c_prime``.

On a strict multiplicative shell of ratio below two, distinct prime-power
coordinates are pairwise coprime.  A fixed ``h`` layer is then a partial
matching on both pair spaces.  Fourier orthogonality in ``h`` therefore gives
an exact averaged Bessel identity.  It does *not* control the required zero
modulation.  The routines below replay the related affine finite-field
Moyal identity and a cyclic zero-mode countermodel.

The countermodel is an obstruction to a structure-free transform argument;
it is not asserted to be an actual-prime-power carry core.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np


def affine_permutation(prime: int, slope: int, shift: int) -> np.ndarray:
    """Return the matrix of ``x -> slope*x+shift`` on ``F_prime``.

    ``slope`` must be nonzero modulo ``prime``.  Rows are source points and
    columns are image points.
    """

    if prime <= 2:
        raise ValueError("prime must be greater than two")
    slope %= prime
    shift %= prime
    if slope == 0:
        raise ValueError("slope must be nonzero modulo prime")
    answer = np.zeros((prime, prime), dtype=complex)
    sources = np.arange(prime, dtype=np.int64)
    targets = (slope * sources + shift) % prime
    answer[sources, targets] = 1.0
    return answer


def centered_affine_permutation(prime: int, slope: int, shift: int) -> np.ndarray:
    """Return ``P_(slope,shift)-J/prime``."""

    return affine_permutation(prime, slope, shift) - np.full(
        (prime, prime), 1.0 / prime, dtype=complex
    )


def affine_fourier_matrix_unit(prime: int, slope: int, frequency: int) -> np.ndarray:
    r"""Fourier transform the affine shifts into one matrix unit.

    For nonzero ``frequency`` this returns

    ``prime^-1 sum_t e(-frequency*t/prime) P_(slope,t)``.

    If ``u_eta(x)=prime^-1/2 e(eta*x/prime)``, the result is exactly
    ``|u_(frequency*slope)><u_frequency|``.
    """

    slope %= prime
    frequency %= prime
    if slope == 0 or frequency == 0:
        raise ValueError("slope and frequency must be nonzero modulo prime")
    sources = np.arange(prime, dtype=float)[:, None]
    targets = np.arange(prime, dtype=float)[None, :]
    phase = frequency * (slope * sources - targets)
    return np.exp(2j * np.pi * phase / prime) / prime


def residual_shift(
    row_pair: tuple[int, int], color_pair: tuple[int, int]
) -> int:
    """Return ``a*c-a_prime*c_prime``."""

    a, a_prime = row_pair
    c, c_prime = color_pair
    return a * c - a_prime * c_prime


def strict_shell_collision_forces_equality(
    fixed_pair: tuple[int, int],
    first_pair: tuple[int, int],
    second_pair: tuple[int, int],
    *,
    shell_minimum: int,
    shell_maximum: int,
) -> bool:
    """Certify the elementary fixed-shift injectivity implication.

    The function checks the assumptions used in the proof.  If

    ``x*u-y*v = x*u_prime-y*v_prime``

    and ``gcd(x,y)=1`` while the shell diameter is below every coordinate,
    then the two varying pairs are equal.
    """

    x, y = fixed_pair
    u, v = first_pair
    u_prime, v_prime = second_pair
    coordinates = (x, y, u, v, u_prime, v_prime)
    if shell_minimum <= 0 or shell_maximum < shell_minimum:
        raise ValueError("invalid shell bounds")
    if shell_maximum - shell_minimum >= shell_minimum:
        raise ValueError("the shell ratio is not strictly below two")
    if any(value < shell_minimum or value > shell_maximum for value in coordinates):
        raise ValueError("a coordinate lies outside the supplied shell")
    if math.gcd(x, y) != 1:
        raise ValueError("the fixed pair must be coprime")
    if x * u - y * v != x * u_prime - y * v_prime:
        raise ValueError("the two shifts are not equal")
    return first_pair == second_pair


@dataclass(frozen=True)
class ZeroModeLedger:
    """Exact cyclic matching countermodel to pointwise residual Bessel."""

    underlying_colors: int
    ordered_distinct_color_pairs: int
    matching_layers: int
    maximum_degree: int
    tensor_pair_norm_squared: float
    averaged_modulated_energy: float
    zero_modulation_energy: float
    zero_to_average_ratio: float
    desired_degree_scale: float
    desired_bound_violation_ratio: float


def cyclic_zero_mode_ledger(underlying_colors: int) -> ZeroModeLedger:
    r"""Return a sharp zero-frequency obstruction with tensor-square input.

    Let ``m=n(n-1)`` index all ordered distinct pairs from ``n`` colors.
    The ``m`` cyclic permutation matrices decompose ``K_(m,m)`` into
    matchings.  For the normalized flat color vector, its restricted tensor
    square has value ``1/n`` at each of the ``m`` right vertices.

    Fourier averaging over the matching label has energy ``(n-1)^2``, while
    zero modulation has energy ``n(n-1)^3``.  Their ratio is exactly ``m``.
    """

    n = int(underlying_colors)
    if n < 2:
        raise ValueError("at least two underlying colors are required")
    m = n * (n - 1)
    tensor_norm_squared = m / (n * n)
    average = float(m * tensor_norm_squared)
    zero = float(m * (m / n) ** 2)
    target = float(m)
    return ZeroModeLedger(
        underlying_colors=n,
        ordered_distinct_color_pairs=m,
        matching_layers=m,
        maximum_degree=m,
        tensor_pair_norm_squared=float(tensor_norm_squared),
        averaged_modulated_energy=average,
        zero_modulation_energy=zero,
        zero_to_average_ratio=zero / average,
        desired_degree_scale=target,
        desired_bound_violation_ratio=zero / target,
    )
