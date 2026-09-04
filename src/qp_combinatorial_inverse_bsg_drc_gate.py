"""Ledgers for the combinatorial inverse branch of the QP fan problem.

The module records the sharp popular-difference exponents and an exact
globally labelled broad-rectangle fixture.  The fixture preserves the
endpoint lattice, shell, broad scale, and mixed second/third-difference
scales, but intentionally does not satisfy a common physical product band.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class LabelDispersingPoint:
    defect: int
    first_completion: int
    second_completion: int
    carrier: int


def label_dispersing_point(step: int, scale: int, defect: int) -> LabelDispersingPoint:
    """Return the exact endpoint-lattice cubic-label fixture point.

    The endpoint pair is

        y=step^2+1,  x=step^2-step+1,

    so ``x*step-y*(step-1)=1``.  The carrier is a tangent polynomial with
    a small cubic term; this gives the right mixed-label and third-difference
    scales while keeping the graph strictly convex when ``scale=o(step)``.
    """

    if step <= 4 or scale <= 0 or not scale <= defect <= 2 * scale:
        raise ValueError("require step>4 and scale<=defect<=2*scale")
    if 4 * scale >= step:
        raise ValueError("strict-convexity regime requires 4*scale<step")
    y = step * step + 1
    x = step * step - step + 1
    first = y + step * defect
    second = x + (step - 1) * defect
    carrier = (
        y
        - step * defect
        + 3 * defect * defect
        - (defect**3 // step)
    )
    if x * first - y * second != defect:
        raise AssertionError("the exact defect identity failed")
    return LabelDispersingPoint(defect, first, second, carrier)


def mixed_carrier_label(
    step: int, scale: int, base: int, first_shift: int, second_shift: int
) -> int:
    """Return the exact mixed carrier difference on one rectangle."""

    values = {
        offset: label_dispersing_point(step, scale, base + offset).carrier
        for offset in (0, first_shift, second_shift, first_shift + second_shift)
    }
    return (
        values[0]
        + values[first_shift + second_shift]
        - values[first_shift]
        - values[second_shift]
    )


def continuous_mixed_label(
    step: int, base: int, first_shift: int, second_shift: int
) -> Fraction:
    """Mixed label before flooring the cubic term."""

    d = first_shift
    e = second_shift
    return 6 * d * e - Fraction(3 * d * e * (2 * base + d + e), step)


def popular_difference_exponent_ledger(epsilon: Fraction = Fraction(0)) -> dict[str, Fraction]:
    """Critical ``H=D^(7/8)``, ``E=D^(5/2+epsilon)`` ledger."""

    epsilon = Fraction(epsilon)
    fan = Fraction(7, 8)
    energy = Fraction(5, 2) + epsilon
    bsg_parameter = 3 * fan - energy
    return {
        "fan": fan,
        "energy": energy,
        "popular_multiplicity_floor": energy - 2 * fan,
        "popular_direction_count_floor": energy - 2 * fan,
        "matching_headroom": 3 * fan - energy,
        "bsg_parameter": bsg_parameter,
        "standard_bsg_subset_floor": fan - bsg_parameter,
        "standard_bsg_doubling_ceiling": 4 * bsg_parameter,
        "behrend_energy": Fraction(21, 8),
        "behrend_excess_over_threshold": Fraction(1, 8) - epsilon,
        "completion_step": Fraction(33, 32),
        "completion_shell_variation": Fraction(61, 32),
        "low_label_product_rectangles": Fraction(61, 32),
        "low_label_margin_below_behrend_energy": Fraction(23, 32),
        "generic_u3_cube_floor": 3 + 2 * epsilon,
        "narrow_face_cube_ceiling": Fraction(3),
        "fixed_direction_triple_base_floor": 2 * epsilon,
        "broad_pair_triple_product_floor": Fraction(99, 32),
        "third_difference_small_product_ceiling": Fraction(49, 16),
        "broad_to_third_difference_margin": Fraction(1, 32),
        "high_volume_threshold": Fraction(33, 8),
        "fixture_u3_cubes": Fraction(7, 2),
        "fixture_low_volume_cubes": Fraction(61, 32),
        "fixture_low_volume_cube_margin": Fraction(51, 32),
    }
