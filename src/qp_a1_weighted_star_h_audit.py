"""Finite ledgers for the final ``A=1`` parabolic star in the original H graph.

The row-pair/color-pair incidence is denoted by ``H``.  A fixed color
rectangle whose completions occupy ``A=1`` lines gives two fixed columns of
``H`` and one row for every actual completion.  This module records two
elementary facts used in the hostile audit:

* the inverse-square-root ``B`` star has bounded operator norm before its
  endpoint coefficient is copied to every leaf;
* after that copy, the compressed coefficient is the old positive
  ``sum_B B^{-1/2}``, and the corresponding two-column Gram block retains
  every common neighbour after diagonal subtraction.

These are abstract incidence ledgers.  They do not construct an actual-prime
QP packet.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Iterable, Sequence


@dataclass(frozen=True)
class WeightedStarLedger:
    """Norm data for ``T(e_B)=B^{-1/2}e_0`` and a constant endpoint lift."""

    branches: int
    operator_norm: float
    copied_endpoint_norm: float
    compressed_coefficient: float

    @property
    def cauchy_ratio(self) -> float:
        """Ratio to ``||T|| * ||J e||``; it is close to one on a dyadic star."""

        denominator = self.operator_norm * self.copied_endpoint_norm
        return self.compressed_coefficient / denominator if denominator else 0.0


def weighted_a1_star(branches: Iterable[int]) -> WeightedStarLedger:
    """Return the exact scalar norm ledger for positive integer ``B`` values.

    The one-row operator has entries ``B^{-1/2}``.  Its norm is the Euclidean
    norm of that row.  Pulling one base endpoint coefficient to all leaves has
    norm ``sqrt(#B)``, while compressing back to the base endpoints sums the
    entries positively.
    """

    values = tuple(int(value) for value in branches)
    if not values or any(value <= 0 for value in values):
        raise ValueError("branches must be a nonempty family of positive integers")
    weights = tuple(value ** -0.5 for value in values)
    return WeightedStarLedger(
        branches=len(values),
        operator_norm=math.sqrt(math.fsum(weight * weight for weight in weights)),
        copied_endpoint_norm=math.sqrt(len(values)),
        compressed_coefficient=math.fsum(weights),
    )


@dataclass(frozen=True)
class TwoColumnHGramLedger:
    """Exact Gram data for an all-one ``N``-by-two incidence submatrix."""

    common_neighbours: int
    incidence_operator_norm: float
    gram_off_diagonal: int
    diagonal_subtracted_operator_norm: int
    equal_unit_pair_quadratic: int
    four_distinct_equal_z_quadratic: Fraction


def two_column_h_packet(line_lengths: Sequence[int]) -> TwoColumnHGramLedger:
    """Return the original-``H`` ledger for line lengths ``ell_B``.

    The packet has two fixed color-pair columns and ``sum ell_B`` distinct
    row-pair vertices.  Both columns contain one on every row.  Thus

    ``H^* H = N [[1,1],[1,1]]``

    and subtracting the common-column diagonal leaves
    ``N [[0,1],[1,0]]``.
    """

    lengths = tuple(int(value) for value in line_lengths)
    if not lengths or any(value < 0 for value in lengths):
        raise ValueError("line lengths must be a nonempty nonnegative sequence")
    neighbours = sum(lengths)
    return TwoColumnHGramLedger(
        common_neighbours=neighbours,
        incidence_operator_norm=math.sqrt(2 * neighbours),
        gram_off_diagonal=neighbours,
        diagonal_subtracted_operator_norm=neighbours,
        equal_unit_pair_quadratic=neighbours,
        # Four distinct colors with z_c=1/2 give two pair coefficients 1/4.
        # The two ordered off-diagonal terms therefore contribute N/8.
        four_distinct_equal_z_quadratic=Fraction(neighbours, 8),
    )


@dataclass(frozen=True)
class FinalFaceExponentLedger:
    """Power-of-``D`` exponents at the final positive parabolic face."""

    relation_mass: Fraction
    direction_height: Fraction
    line_count: Fraction
    inverse_sqrt_line_sum: Fraction
    bare_curvature_prefactor: Fraction
    one_line_length: Fraction
    common_neighbour_count: Fraction
    positive_trace: Fraction
    desired_trace: Fraction
    missing_saving: Fraction


def final_face_exponents() -> FinalFaceExponentLedger:
    """Return the exact ``(21/32,11/32,23/64,3/64)`` ledger."""

    relation = Fraction(45, 64)
    height = Fraction(26, 64)
    line_count = Fraction(20, 64)
    line_sum = line_count / 2
    prefactor = (Fraction(1) - height) / 2
    line_length = prefactor - line_count / 2
    neighbours = line_count + line_length
    positive = relation + neighbours
    desired = Fraction(1)
    return FinalFaceExponentLedger(
        relation_mass=relation,
        direction_height=height,
        line_count=line_count,
        inverse_sqrt_line_sum=line_sum,
        bare_curvature_prefactor=prefactor,
        one_line_length=line_length,
        common_neighbour_count=neighbours,
        positive_trace=positive,
        desired_trace=desired,
        missing_saving=positive - desired,
    )
