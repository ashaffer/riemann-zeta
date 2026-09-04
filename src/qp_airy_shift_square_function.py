"""Finite vector Plancherel for shifted Airy/fold orbit sums.

The exact theorem is elementary but important.  If ``Ahat`` is the
normalized DFT of a curvature-layer amplitude and ``O(u,v)`` is the shifted
Fourier field of arbitrary (possibly Hilbert-valued) selected normal-lattice
coefficients, then

    sum Ahat(u,v) O(u,v) = sum A(h,k) b(h,k)

and Cauchy--Schwarz plus the two Parseval identities gives

    ||sum Ahat O|| <= ||A||_2 ||b||_2.

For a genuine layer with ``O(d H)`` frequency sites, amplitude
``sqrt(q/d)``, and normalized triangular Fejer products, this is exactly
``sqrt(q/H)``.  The gain is false if either layer localization or the Fejer
``l2`` control is removed; this module includes exact hostile fixtures.
"""

from __future__ import annotations

import cmath
from dataclasses import dataclass
from fractions import Fraction
from math import cos, gcd, pi, sqrt
from typing import Sequence

import numpy as np

from qp_coupled_cusp_fejer_inverse import reduced_symmetric_cusp_data
from qp_dual_tangent_major_arc import rational_tangent_data
from qp_high_primitive_packet_pair_audit import scaled_cusp_normal_form


def normalized_dft2(values: Sequence[Sequence[complex]]) -> np.ndarray:
    """Return the normalized negative-sign DFT on a square finite torus."""

    array = np.asarray(values, dtype=np.complex128)
    if array.ndim != 2 or array.shape[0] == 0 or array.shape[0] != array.shape[1]:
        raise ValueError("values must be a nonempty square matrix")
    size = array.shape[0]
    return np.fft.fft2(array) / (size * size)


def positive_shifted_field(values: Sequence[Sequence[complex]]) -> np.ndarray:
    """Return ``O(u,v)=sum_(x,y) values[x,y] e_M(ux+vy)``."""

    array = np.asarray(values, dtype=np.complex128)
    if array.ndim != 2 or array.shape[0] == 0 or array.shape[0] != array.shape[1]:
        raise ValueError("values must be a nonempty square matrix")
    size = array.shape[0]
    return np.fft.ifft2(array) * (size * size)


@dataclass(frozen=True)
class ShiftSquareAudit:
    size: int
    direct_sum: complex
    shifted_sum: complex
    amplitude_fourier_energy: float
    amplitude_physical_energy_scaled: float
    shifted_field_energy: float
    coefficient_physical_energy_scaled: float
    cauchy_bound: float


def shift_square_audit(
    amplitude: Sequence[Sequence[complex]],
    coefficient_field: Sequence[Sequence[complex]],
) -> ShiftSquareAudit:
    """Replay the exact DFT identity, both Parsevals, and Cauchy bound."""

    amplitude_array = np.asarray(amplitude, dtype=np.complex128)
    coefficient_array = np.asarray(coefficient_field, dtype=np.complex128)
    if (
        amplitude_array.ndim != 2
        or amplitude_array.shape[0] == 0
        or amplitude_array.shape[0] != amplitude_array.shape[1]
        or coefficient_array.shape != amplitude_array.shape
    ):
        raise ValueError("amplitude and coefficient field must be equal square matrices")
    size = amplitude_array.shape[0]
    fourier = normalized_dft2(amplitude_array)
    shifted = positive_shifted_field(coefficient_array)
    direct_sum = complex(np.sum(amplitude_array * coefficient_array))
    shifted_sum = complex(np.sum(fourier * shifted))
    amplitude_fourier_energy = float(np.sum(np.abs(fourier) ** 2))
    amplitude_physical_energy_scaled = float(
        np.sum(np.abs(amplitude_array) ** 2) / (size * size)
    )
    shifted_field_energy = float(np.sum(np.abs(shifted) ** 2))
    coefficient_physical_energy_scaled = float(
        size * size * np.sum(np.abs(coefficient_array) ** 2)
    )
    cauchy_bound = float(
        np.linalg.norm(amplitude_array.ravel())
        * np.linalg.norm(coefficient_array.ravel())
    )
    return ShiftSquareAudit(
        size=size,
        direct_sum=direct_sum,
        shifted_sum=shifted_sum,
        amplitude_fourier_energy=amplitude_fourier_energy,
        amplitude_physical_energy_scaled=amplitude_physical_energy_scaled,
        shifted_field_energy=shifted_field_energy,
        coefficient_physical_energy_scaled=coefficient_physical_energy_scaled,
        cauchy_bound=cauchy_bound,
    )


def normalized_fejer_square_mass(order: int) -> Fraction:
    """Return the exact ``l2^2`` mass of height-one Fejer coefficients.

    For ``c_h=(order-|h|)/order^2``, ``|h|<order``, the answer is

        (2*order^2+1)/(3*order^3).
    """

    if order <= 0:
        raise ValueError("order must be positive")
    return Fraction(2 * order * order + 1, 3 * order**3)


def localized_fejer_vector_bound(
    order: int,
    layer_cardinality: int,
    amplitude_ceiling: float,
) -> dict[str, float]:
    """Bounds for an arbitrary complex amplitude on one finite layer.

    The square-function bound uses only Fejer ``l2`` mass.  The pointwise
    bound additionally uses ``|c_h c_k|<=order^-2`` and is stronger when
    the selected coefficient vectors are contractions.
    """

    if order <= 0 or layer_cardinality < 0 or amplitude_ceiling < 0:
        raise ValueError("invalid localized-layer parameters")
    square = (
        amplitude_ceiling
        * sqrt(layer_cardinality)
        * float(normalized_fejer_square_mass(order))
    )
    pointwise = amplitude_ceiling * layer_cardinality / (order * order)
    return {
        "square_function": square,
        "pointwise_fejer": pointwise,
        "best": min(square, pointwise),
    }


@dataclass(frozen=True)
class AiryVectorLedger:
    q: Fraction
    height: Fraction
    airy_width: Fraction
    airy_amplitude: Fraction
    fourier_spread: Fraction
    l2_layer_gain: Fraction
    l2_total: Fraction
    l1_layer_gain: Fraction
    l1_total: Fraction
    target: Fraction


def airy_vector_exponent_ledger() -> AiryVectorLedger:
    """Return the exact Airy layer exponents after vector localization."""

    q = Fraction(33, 16)
    height = Fraction(17, 16)
    width = Fraction(1, 48)
    amplitude = Fraction(49, 48)
    l2_gain = (width - height) / 2
    l1_gain = width - height
    return AiryVectorLedger(
        q=q,
        height=height,
        airy_width=width,
        airy_amplitude=amplitude,
        fourier_spread=height - width,
        l2_layer_gain=l2_gain,
        l2_total=amplitude + l2_gain,
        l1_layer_gain=l1_gain,
        l1_total=amplitude + l1_gain,
        target=Fraction(1, 2),
    )


def constant_amplitude_no_localization_fixture(size: int, amplitude: float = 1.0):
    """Positive counterexample to a gain inferred from smoothness alone.

    A constant amplitude has every derivative equal to zero but its DFT is
    concentrated at the zero shift.  A singleton positive coefficient field
    then gives direct value ``amplitude``, with no ``size^-1/2`` gain.
    """

    if size <= 1 or amplitude <= 0:
        raise ValueError("require size>1 and positive amplitude")
    values = np.full((size, size), amplitude, dtype=np.complex128)
    coefficients = np.zeros((size, size), dtype=np.complex128)
    coefficients[0, 0] = 1.0
    return values, coefficients


@dataclass(frozen=True)
class CompletionRepetitionAudit:
    completion_count: int
    one_fiber_norm: float
    repeated_operator_norm: float
    repetition_loss: float


def completion_repetition_audit(
    row: Sequence[complex], completion_count: int
) -> CompletionRepetitionAudit:
    """Exact obstruction to automatic orthogonality in completion ``S``.

    Repeat the same synthesis row at every completion.  As a map from the
    coefficient ``l2`` space to unnormalized ``l2(S)``, its norm is
    ``sqrt(completion_count)`` times the one-fiber norm.  Thus a fixed-chart
    shift-square theorem does not tensor into completion orthogonality unless
    a genuine varying character (or another Bessel input) is supplied.
    """

    if completion_count <= 0 or not row:
        raise ValueError("require a nonempty row and positive completion count")
    one = float(np.linalg.norm(np.asarray(row, dtype=np.complex128)))
    repeated = sqrt(completion_count) * one
    return CompletionRepetitionAudit(
        completion_count=completion_count,
        one_fiber_norm=one,
        repeated_operator_norm=repeated,
        repetition_loss=sqrt(completion_count),
    )


def completion_character_gram(labels: Sequence[int], completion_modulus: int) -> np.ndarray:
    """Gram matrix of normalized genuine completion characters.

    Its entries are one exactly for equal labels modulo the completion
    modulus and zero otherwise.  Hence its norm is the maximum label-fiber
    multiplicity, making the required global intertwining explicit.
    """

    if completion_modulus <= 0:
        raise ValueError("completion modulus must be positive")
    labels = tuple(labels)
    if not labels:
        return np.zeros((0, 0), dtype=np.complex128)
    samples = np.arange(completion_modulus)
    matrix = np.asarray(
        [
            np.exp(2j * np.pi * (label % completion_modulus) * samples / completion_modulus)
            / sqrt(completion_modulus)
            for label in labels
        ],
        dtype=np.complex128,
    )
    return matrix @ matrix.conjugate().T


def positive_cosine_amplitude(size: int, first_shift: int, second_shift: int):
    """Return the nonnegative amplitude ``1+cos(2pi(ux+vy)/M)``."""

    if size <= 1:
        raise ValueError("size must exceed one")
    return tuple(
        tuple(
            1.0
            + cos(
                2
                * pi
                * (first_shift * first + second_shift * second)
                / size
            )
            for second in range(size)
        )
        for first in range(size)
    )


@dataclass(frozen=True)
class ActualResidualShiftFixture:
    Q: int
    y: int
    left_shift: int
    right_shift: int
    p: int
    d: int
    n: int
    content: int
    left_error: int
    right_error: int
    tangent_modulus: int
    left_step: int
    right_step: int
    alpha: Fraction
    beta: Fraction
    torus_size: int
    alpha_shift: int
    beta_shift: int


def actual_residual_shift_fixture(
    multiplier: int = 1, family_index: int = 0
) -> ActualResidualShiftFixture:
    """A transverse nonsquare residual shifted exactly to a major character.

    More generally, for ``j=family_index`` use

    ``Q=349+223080j, y=74+47320j, g=1+637j, r=13g, s=20g``.

    Every member has primitive tangent ``(p,d)=(33,7)``, ``n=-1``, and the
    same affine intercepts modulo one.  Since ``g=1 (mod 49)``, the family
    stays off square content; its scaled-cusp factors are also all nonzero.
    It is a broad-mask physical fixture, not an energy-core construction.
    Taking a torus of size 270400 times ``multiplier`` makes both intercept
    denominators divide the torus, so one exact Fourier shift lands at the
    major character.
    """

    if multiplier <= 0 or family_index < 0:
        raise ValueError("require a positive multiplier and nonnegative family index")
    content = 1 + 637 * family_index
    Q = 349 + 223080 * family_index
    y = 74 + 47320 * family_index
    left_shift, right_shift = 13 * content, 20 * content
    point = reduced_symmetric_cusp_data(Q, y, left_shift, right_shift)
    p, d = point.p, point.d
    normal = scaled_cusp_normal_form(point)
    assert point.g % (d * d) != 0
    assert normal["z"] != 0 and normal["quadratic_residual"] != 0
    assert normal["z"] != -p * normal["v"]
    parity = gcd(p + d, p - d)
    left = (p + d) // parity
    right = (p - d) // parity
    tangent = rational_tangent_data(1, 4, left, right)
    R, minus_left_step, right_step = tangent.primitive_direction
    physical_a = Q + y
    physical_v = Q - y + left_shift
    physical_w = Q + y + right_shift
    alpha = Fraction(physical_v) + Fraction(p * p * physical_a, (p + d) ** 2)
    beta = Fraction(physical_w) - Fraction(p * p * physical_a, (p - d) ** 2)
    size = R * multiplier
    assert (alpha * size).denominator == (beta * size).denominator == 1
    alpha_shift = (-int(alpha * size)) % size
    beta_shift = (-int(beta * size)) % size
    assert (alpha + Fraction(alpha_shift, size)).denominator == 1
    assert (beta + Fraction(beta_shift, size)).denominator == 1
    return ActualResidualShiftFixture(
        Q=Q,
        y=y,
        left_shift=left_shift,
        right_shift=right_shift,
        p=p,
        d=d,
        n=point.n,
        content=point.g,
        left_error=point.e,
        right_error=point.f,
        tangent_modulus=R,
        left_step=-minus_left_step,
        right_step=right_step,
        alpha=alpha,
        beta=beta,
        torus_size=size,
        alpha_shift=alpha_shift,
        beta_shift=beta_shift,
    )
