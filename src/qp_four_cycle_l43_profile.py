"""Exact exponent ledger for the coefficient-sensitive L^(4/3) FC profile.

The arithmetic input is that the active determinant band is a
three-coordinate matching: any three color coordinates determine the
fourth.  Multilinear interpolation therefore bounds its weighted mass by
the product of four L^(4/3) norms.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence, Tuple


POINTWISE_COMPLETION_EXPONENT = Fraction(1, 2)
PARABOLIC_TRACE_EXPONENT = Fraction(5, 4)
MAX_SLICE_EXPONENT = Fraction(5, 16)
UNIFORM_TRACE_EXPONENT = Fraction(21, 16)
TRANSFER_SCALE = Fraction(16, 33)


ColorTuple = Tuple[int, int, int, int]


@dataclass(frozen=True)
class ChapmanMudgalHsmLedger:
    """Balanced exponents for the fixed-determinant literature no-match.

    Chapman--Mudgal prove an unweighted, centered box discrepancy of size
    ``N+h``.  The two ``formal`` fields record what that error would give if
    it were stable under the four HSM Dirichlet kernels; the twist fields
    record the cost of expanding those kernels and summing the resulting
    characters absolutely.  Neither weighted stability nor weighted-main-
    term cancellation is asserted by the ledger.
    """

    box_side_exponent_in_q: Fraction
    short_shift_exponent_in_q: Fraction
    product_scale_exponent_in_q: Fraction
    kernel_length_exponent_in_q: Fraction
    coefficient_density_exponent_in_q: Fraction
    hsm_target_exponent_in_q: Fraction
    formal_weighted_error_exponent_in_q: Fraction
    formal_margin_exponent_in_q: Fraction
    four_kernel_twist_count_exponent_in_q: Fraction
    absolute_twist_error_exponent_in_q: Fraction
    absolute_twist_loss_exponent_in_q: Fraction
    unweighted_theorem_only: bool
    weighted_stability_is_proved: bool
    weighted_main_term_cancellation_is_proved: bool
    closes_hsm: bool


def determinant(color: ColorTuple) -> int:
    """Return ``c11*c22-c12*c21`` in row-major coordinates."""

    c11, c12, c21, c22 = color
    return c11 * c22 - c12 * c21


def three_coordinate_projections_are_injective(
    colors: Iterable[ColorTuple],
) -> bool:
    """Check injectivity after deleting each of the four coordinates."""

    colors = tuple(colors)
    for omitted in range(4):
        seen = set()
        for color in colors:
            projection = color[:omitted] + color[omitted + 1 :]
            if projection in seen:
                return False
            seen.add(projection)
    return True


def l43_effective_support(weights: Sequence[float]) -> float:
    """Return ``||z||_(4/3)^4 / ||z||_2^4`` for real magnitudes."""

    l2_squared = sum(abs(value) ** 2 for value in weights)
    if l2_squared == 0:
        return 0.0
    l43_sum = sum(abs(value) ** (4.0 / 3.0) for value in weights)
    return l43_sum**3 / l2_squared**2


def trace_profile_exponent(mu: Fraction) -> Fraction:
    """Best proved trace exponent when ``R_(4/3)=D^mu``.

    This is the minimum of three unconditional estimates:

    * the uniform ``21/16`` theorem;
    * pointwise completion ``D^(1/2)`` times the L^(4/3) color mass;
    * the parabolic ``D^(5/4)`` theorem plus the broad slice bound
      ``D^(5/16)`` times the same color mass.

    The repeated-coordinate contribution supplies the floor ``D``.
    """

    if mu < 0:
        raise ValueError("the L^(4/3) effective-support exponent is nonnegative")

    pointwise = max(Fraction(1), POINTWISE_COMPLETION_EXPONENT + mu)
    sector_split = max(PARABOLIC_TRACE_EXPONENT, MAX_SLICE_EXPONENT + mu)
    return min(UNIFORM_TRACE_EXPONENT, pointwise, sector_split)


def operator_profile_exponent(mu: Fraction) -> Fraction:
    """Return the fourth-root operator exponent for the profile."""

    return trace_profile_exponent(mu) / 4


def transverse_profile_exponent(mu: Fraction) -> Fraction:
    """Return the inherited smooth-transfer exponent for a uniform profile."""

    return Fraction(1, 2) + TRANSFER_SCALE * operator_profile_exponent(mu)


def chapman_mudgal_hsm_ledger() -> ChapmanMudgalHsmLedger:
    """Return the exact balanced ``q``-power comparison.

    At the balanced HSM point, ``N=J=K=q^(42/33)``, the short shifts have
    length ``B_0=q^(34/33)``, and each of the two translation kernels has
    length ``P=Q=q^(8/33)``.  Thus the natural coefficient density is
    ``P*Q=D=q^(16/33)`` and the target is ``D*N^2=q^(100/33)``.

    A hypothetical error ``D*(N+h)`` summed over the short shifts would cost
    ``q^(92/33)``, leaving ``q^(8/33)``.  Expanding all four kernels instead
    creates ``P^2*Q^2=D^2`` twists; even a hypothetical uniform ``O(N)``
    centered bound for each twist costs ``q^(108/33)``, losing the same
    ``q^(8/33)=sqrt(D)``.  Chapman--Mudgal prove neither hypothetical
    weighted statement.
    """

    box_side = Fraction(42, 33)
    short_shift = Fraction(34, 33)
    product_scale = 2 * box_side
    kernel_length = Fraction(8, 33)
    density = 2 * kernel_length
    target = density + product_scale
    formal_weighted_error = short_shift + density + box_side
    twist_count = 4 * kernel_length
    absolute_twist_error = short_shift + twist_count + box_side

    return ChapmanMudgalHsmLedger(
        box_side_exponent_in_q=box_side,
        short_shift_exponent_in_q=short_shift,
        product_scale_exponent_in_q=product_scale,
        kernel_length_exponent_in_q=kernel_length,
        coefficient_density_exponent_in_q=density,
        hsm_target_exponent_in_q=target,
        formal_weighted_error_exponent_in_q=formal_weighted_error,
        formal_margin_exponent_in_q=target - formal_weighted_error,
        four_kernel_twist_count_exponent_in_q=twist_count,
        absolute_twist_error_exponent_in_q=absolute_twist_error,
        absolute_twist_loss_exponent_in_q=absolute_twist_error - target,
        unweighted_theorem_only=True,
        weighted_stability_is_proved=False,
        weighted_main_term_cancellation_is_proved=False,
        closes_hsm=False,
    )
