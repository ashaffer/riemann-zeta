"""Exact algebra for the calibrated signed-cubic carrier no-go."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import sqrt


@dataclass(frozen=True)
class CalibratedCubicModel:
    """Finite-dimensional parameters for the direct-sum obstruction."""

    dimension: int
    packet_factor: float

    def __post_init__(self) -> None:
        if self.dimension <= 0 or self.dimension % 4:
            raise ValueError("dimension must be a positive multiple of four")
        if not 1.0 <= self.packet_factor < self.dimension:
            raise ValueError("require 1 <= packet_factor < dimension")

    @property
    def carrier_norm(self) -> float:
        return sqrt(3.0 * self.dimension / 4.0)

    @property
    def negative_skew_scale(self) -> float:
        return sqrt(self.packet_factor)

    @property
    def witness_leverage(self) -> float:
        return self.carrier_norm / 2.0

    @property
    def witness_negative_skew(self) -> float:
        return 3.0 * sqrt(3.0) * self.negative_skew_scale / 8.0

    @property
    def witness_joint_value(self) -> float:
        return self.witness_leverage * (1.0 + self.witness_negative_skew)

    @property
    def asymptotic_joint_floor(self) -> float:
        return 9.0 * sqrt(self.dimension * self.packet_factor) / 32.0


def phase_vector_counts(dimension: int) -> tuple[int, int]:
    """Return counts of phases ``+1`` and ``-1`` in the calibrated model."""

    if dimension <= 0 or dimension % 4:
        raise ValueError("dimension must be a positive multiple of four")
    return dimension // 4, 3 * dimension // 4


def calibration_average(dimension: int, depth: float = 0.5) -> tuple[float, float]:
    """Return uniform averages of ``a_*`` and ``v=a_*+depth``."""

    positive, negative = phase_vector_counts(dimension)
    average_phase = (positive - negative) / dimension
    return average_phase, average_phase + depth


def standardized_two_point_atoms(negative_skew: float) -> tuple[float, float, float]:
    """Return ``(p, positive_atom, negative_atom)`` with skew ``-S``.

    The negative atom is returned as a negative number.
    """

    if negative_skew < 0.0:
        raise ValueError("negative_skew must be nonnegative")
    scale = negative_skew
    probability = (1.0 + scale / sqrt(scale * scale + 4.0)) / 2.0
    positive_atom = sqrt((1.0 - probability) / probability)
    negative_atom = -sqrt(probability / (1.0 - probability))
    return probability, positive_atom, negative_atom


def two_point_moments(negative_skew: float) -> tuple[float, float, float]:
    """Compute mean, variance, and third moment of the exact two-point law."""

    probability, positive, negative = standardized_two_point_atoms(negative_skew)
    mean = probability * positive + (1.0 - probability) * negative
    second = probability * positive**2 + (1.0 - probability) * negative**2
    third = probability * positive**3 + (1.0 - probability) * negative**3
    return mean, second, third


def active_exponent(aperture: Fraction = Fraction(50, 33)) -> Fraction:
    """Exponent of ``sqrt(M Delta)`` for ``M=Y`` and ``Delta=Y^(2-A)``."""

    if not Fraction(1) < aperture < Fraction(2):
        raise ValueError("require 1 < aperture < 2")
    return Fraction(1, 2) + (Fraction(2) - aperture) / 2
