"""Finite center-Fourier identities for the QP fourth-cycle operator.

The center DFT is an exact unitary change of basis on the carrier index.  It
does not turn the two-dimensional row-pair Schatten norm into the stronger
one-dimensional completion-sum convolution norm.  This module keeps those
two quantities separate and supplies finite countermodels for conflating
them.
"""

from __future__ import annotations

from collections import defaultdict
from cmath import exp
from math import ceil, e, floor, pi, sqrt
from typing import Mapping, Sequence


Cell = tuple[int, int]


def unitary_center_dft(
    matrix: Mapping[Cell, complex],
    rows: Sequence[int],
    modulus: int,
) -> dict[Cell, complex]:
    """Right multiply a zero-padded row-by-center matrix by a unitary DFT.

    Center labels are interpreted modulo ``modulus``.  The represented
    labels must therefore be distinct modulo the modulus.
    """

    if modulus <= 0:
        raise ValueError("modulus must be positive")
    centers = {center % modulus for _, center in matrix}
    if len(centers) != len({center for _, center in matrix}):
        raise ValueError("represented centers must be distinct modulo modulus")
    scale = 1.0 / sqrt(modulus)
    return {
        (row, frequency): scale
        * sum(
            matrix.get((row, center), 0j)
            * exp(2j * pi * frequency * center / modulus)
            for center in centers
        )
        for row in rows
        for frequency in range(modulus)
    }


def unnormalized_center_dft(
    matrix: Mapping[Cell, complex],
    rows: Sequence[int],
    modulus: int,
) -> dict[Cell, complex]:
    """The same center DFT without the factor ``modulus**(-1/2)``."""

    unitary = unitary_center_dft(matrix, rows, modulus)
    scale = sqrt(modulus)
    return {index: scale * value for index, value in unitary.items()}


def row_pair_energy(
    matrix: Mapping[Cell, complex],
    rows: Sequence[int],
    centers: Sequence[int],
    *,
    distinct_rows: bool = False,
) -> float:
    r"""Return ``sum_(a,a') |sum_b F(a,b) conjugate(F(a',b))|^2``."""

    return float(
        sum(
            abs(
                sum(
                    matrix.get((row, center), 0j)
                    * matrix.get((other, center), 0j).conjugate()
                    for center in centers
                )
            )
            ** 2
            for row in rows
            for other in rows
            if not distinct_rows or row != other
        )
    )


def center_frequency_frame_energy(
    transformed: Mapping[Cell, complex],
    rows: Sequence[int],
    modulus: int,
) -> float:
    r"""Return the center-frequency frame potential.

    For a unitary center transform this is

    ``sum_(t,u) |sum_a conjugate(Fhat(a,t))*Fhat(a,u)|^2``

    and equals ``row_pair_energy`` exactly up to floating-point evaluation.
    """

    return float(
        sum(
            abs(
                sum(
                    transformed.get((row, first), 0j).conjugate()
                    * transformed.get((row, second), 0j)
                    for row in rows
                )
            )
            ** 2
            for first in range(modulus)
            for second in range(modulus)
        )
    )


def same_center_convolution(
    matrix: Mapping[Cell, complex],
    rows: Sequence[int],
    centers: Sequence[int],
    *,
    distinct_rows: bool = False,
) -> dict[int, complex]:
    r"""Return ``G(S)=sum_b sum_(a+a'=S) F(a,b)F(a',b)``."""

    answer: defaultdict[int, complex] = defaultdict(complex)
    for center in centers:
        for row in rows:
            first = matrix.get((row, center), 0j)
            if first == 0:
                continue
            for other in rows:
                if distinct_rows and row == other:
                    continue
                second = matrix.get((other, center), 0j)
                if second != 0:
                    answer[row + other] += first * second
    return dict(answer)


def convolution_energy(values: Mapping[int, complex]) -> float:
    """Squared ell-two norm of a finite scalar sequence."""

    return float(sum(abs(value) ** 2 for value in values.values()))


def center_fourier_convolution(
    transformed: Mapping[Cell, complex],
    rows: Sequence[int],
    modulus: int,
) -> dict[int, complex]:
    r"""Reconstruct the same-center convolution from a *unitary* center DFT.

    The exact identity is

    ``G = sum_t Fhat_t * Fhat_(-t)``.
    """

    answer: defaultdict[int, complex] = defaultdict(complex)
    for frequency in range(modulus):
        opposite = (-frequency) % modulus
        for row in rows:
            first = transformed.get((row, frequency), 0j)
            if first == 0:
                continue
            for other in rows:
                second = transformed.get((other, opposite), 0j)
                if second != 0:
                    answer[row + other] += first * second
    return dict(answer)


def averaged_frequency_convolution_energy(
    transformed: Mapping[Cell, complex],
    rows: Sequence[int],
    modulus: int,
) -> float:
    r"""Average per-frequency convolution energy for an unnormalized DFT.

    Since ``G=M^(-1) sum_t F_t*F_(-t)``, convexity gives

    ``||G||_2^2 <= M^(-1) sum_t ||F_t*F_(-t)||_2^2``.

    The right side can lose a full physical participation degree.
    """

    total = 0.0
    for frequency in range(modulus):
        opposite = (-frequency) % modulus
        convolution: defaultdict[int, complex] = defaultdict(complex)
        for row in rows:
            first = transformed.get((row, frequency), 0j)
            if first == 0:
                continue
            for other in rows:
                second = transformed.get((other, opposite), 0j)
                if second != 0:
                    convolution[row + other] += first * second
        total += convolution_energy(convolution)
    return total / modulus


def interval_additive_energy(length: int) -> int:
    """Exact additive energy of ``{0,...,length-1}``."""

    if length <= 0:
        raise ValueError("length must be positive")
    return (2 * length**3 + length) // 3


def repeated_row_fixture(row_count: int, center_count: int) -> dict[Cell, complex]:
    """An abstract pair-unique incidence with identical occupied rows.

    Give every occupied cell its own color of coefficient one.  Then the
    coefficient norm squared is ``row_count*center_count`` even though the
    resulting scalar matrix is the all-ones rectangle.
    """

    if min(row_count, center_count) <= 0:
        raise ValueError("fixture sizes must be positive")
    return {
        (row, center): 1.0
        for row in range(row_count)
        for center in range(center_count)
    }


def partial_matching_fixture(size: int) -> dict[Cell, complex]:
    """One-color abstract partial matching with distinct binary rows."""

    if size <= 0:
        raise ValueError("size must be positive")
    return {(2**index, index): 1.0 for index in range(size)}


def density_lower_bound(
    matrix: Mapping[Cell, complex],
    rows: Sequence[int],
    centers: Sequence[int],
) -> tuple[float, float, float]:
    r"""Return the exact mass and two Cauchy lower bounds for nonnegative F.

    If ``d_b=sum_a F(a,b)``, then

    ``||G||_1=sum_b d_b^2`` and
    ``||G||_2^2 >= ||G||_1^2 / |supp(G)|``.

    Also ``sum_b d_b^2 >= E^2/B``, where ``E=sum_b d_b`` and ``B`` is the
    number of represented centers.  The third returned value is the lower
    bound obtained by combining both Cauchy inequalities.
    """

    if any(value.real < 0 or abs(value.imag) > 1.0e-12 for value in matrix.values()):
        raise ValueError("density lower bound requires nonnegative real entries")
    degrees = [sum(matrix.get((row, center), 0j).real for row in rows) for center in centers]
    mass = sum(degree * degree for degree in degrees)
    convolution = same_center_convolution(matrix, rows, centers)
    support = len([value for value in convolution.values() if value != 0])
    first = mass * mass / support if support else 0.0
    total_edges = sum(degrees)
    second = (
        total_edges**4 / (len(centers) ** 2 * support)
        if centers and support
        else 0.0
    )
    return float(mass), float(first), float(second)


def integer_log_shell(q: int) -> list[int]:
    r"""All integers in ``[(q/2)e^(-.2),(q/2)e^(.2)]``."""

    if q <= 0:
        raise ValueError("q must be positive")
    return list(range(ceil((q / 2) * e ** (-0.2)), floor((q / 2) * e**0.2) + 1))


def hard_window_matrix(
    q: int,
    degree: int,
    nodes: Sequence[int],
    coefficients: Mapping[int, complex],
) -> dict[Cell, complex]:
    r"""Build ``F(a,b)=sum_c z_c 1_(|8abc-q^3|<=qD)`` exactly."""

    if min(q, degree) <= 0 or any(node <= 0 for node in nodes):
        raise ValueError("physical parameters must be positive")
    return {
        (row, center): sum(
            coefficients.get(color, 0j)
            for color in nodes
            if abs(8 * row * center * color - q**3) <= q * degree
        )
        for row in nodes
        for center in nodes
    }


def maximum_cell_multiplicity(
    q: int, degree: int, nodes: Sequence[int]
) -> int:
    """Maximum number of selected colors in one row-center cell."""

    return max(
        (
            sum(
                abs(8 * row * center * color - q**3) <= q * degree
                for color in nodes
            )
            for row in nodes
            for center in nodes
        ),
        default=0,
    )
