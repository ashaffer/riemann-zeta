"""Quadratic curvature in affine four-completion token charts.

The principal Bezout chart has a row and two product factors which vary
affinely.  This module records the general one-product calculation and its
precise scope.  It proves a sharp local ``O(D)`` ellipse bound when the
physical row is locked to the stationary affine law.  It does not claim that
an arbitrary actual-prime token chart has such a row law; obtaining that lock
is part of the remaining inverse theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, log, sqrt


Pair = tuple[int, int]


def affine_determinant_value(
    constant: int,
    r_coefficient: int,
    s_coefficient: int,
    mixed_coefficient: int,
    r: int,
    s: int,
) -> int:
    """Evaluate ``constant+B*r+C*s+E*r*s``."""

    return (
        constant
        + r_coefficient * r
        + s_coefficient * s
        + mixed_coefficient * r * s
    )


def transverse_affine_strip_ceiling(r_count: int, s_count: int, D: int) -> int:
    """A uniform ceiling for a transverse integral bilinear strip.

    If the mixed coefficient ``E`` is nonzero, fixing ``r`` leaves slope
    ``C+E*r`` in ``s``.  The nonzero slopes are distinct integers and at most
    one slope vanishes.  Summing their reciprocal widths gives

        R + S + 4*D*(1+log R).

    This is ``O(D log D)`` whenever both token intervals have ``O(D)``
    points.  Actual masks only delete cells.
    """

    if r_count < 0 or s_count < 0 or D < 0:
        raise ValueError("counts and strip width must be nonnegative")
    if r_count == 0 or s_count == 0:
        return 0
    return int(r_count + s_count + 4 * D * (1 + log(max(r_count, 1))))


def count_affine_determinant_strip(
    constant: int,
    r_coefficient: int,
    s_coefficient: int,
    mixed_coefficient: int,
    r_values: range,
    s_values: range,
    D: int,
) -> int:
    """Count a finite affine determinant strip exactly for diagnostics."""

    return sum(
        abs(
            affine_determinant_value(
                constant,
                r_coefficient,
                s_coefficient,
                mixed_coefficient,
                r,
                s,
            )
        )
        <= D
        for r in r_values
        for s in s_values
    )


def verify_transverse_affine_strip_bound(
    constant: int,
    r_coefficient: int,
    s_coefficient: int,
    mixed_coefficient: int,
    r_values: range,
    s_values: range,
    D: int,
) -> tuple[int, int]:
    """Verify the harmonic-slope bound on one finite transverse chart."""

    if mixed_coefficient == 0:
        raise ValueError("the harmonic-slope theorem requires a transverse chart")
    count = count_affine_determinant_strip(
        constant,
        r_coefficient,
        s_coefficient,
        mixed_coefficient,
        r_values,
        s_values,
        D,
    )
    ceiling = transverse_affine_strip_ceiling(len(r_values), len(s_values), D)
    if count > ceiling:
        raise AssertionError("the transverse harmonic-slope ceiling failed")
    return count, ceiling


def parallel_affine_strip_elementary_ceiling(
    r_count: int,
    s_count: int,
    D: int,
    r_coefficient: int,
    s_coefficient: int,
) -> int:
    """Best elementary line-strip ceiling when the mixed coefficient is zero.

    This displays the exact escaping regime.  Unless ``|C|`` is at least the
    ``r``-length or ``|B|`` is at least the ``s``-length, the determinant
    strip alone may retain a quadratic-size block.
    """

    candidates = [r_count * s_count]
    if s_coefficient:
        candidates.append(r_count * (1 + (2 * D) // abs(s_coefficient)))
    if r_coefficient:
        candidates.append(s_count * (1 + (2 * D) // abs(r_coefficient)))
    return min(candidates)


@dataclass(frozen=True)
class StationaryAffineProduct:
    """One product leg ``x(r,s)b(r)d(s)`` in stationary affine coordinates."""

    base_row: int
    base_left: int
    base_right: int
    left_step: int
    right_step: int

    @property
    def row_r_step(self) -> Fraction:
        return Fraction(-self.base_row * self.left_step, self.base_left)

    @property
    def row_s_step(self) -> Fraction:
        return Fraction(-self.base_row * self.right_step, self.base_right)

    @property
    def integral_row_law(self) -> bool:
        return self.row_r_step.denominator == self.row_s_step.denominator == 1

    @property
    def hessian_determinant(self) -> Fraction:
        """Determinant of the Hessian of the quadratic residual term."""

        # The Hessian is -2*x0 times
        # [[d0*p^2/b0, p*z/2], [p*z/2, b0*z^2/d0]].
        x0 = self.base_row
        p = self.left_step
        z = self.right_step
        return Fraction(3 * x0 * x0 * p * p * z * z, 1)

    @property
    def nondegenerate(self) -> bool:
        return self.left_step != 0 and self.right_step != 0

    def row(self, r: int, s: int) -> Fraction:
        return self.base_row + self.row_r_step * r + self.row_s_step * s

    def normalized_displacements(self, r: int, s: int) -> tuple[Fraction, Fraction]:
        return (
            Fraction(self.left_step * r, self.base_left),
            Fraction(self.right_step * s, self.base_right),
        )

    def exact_residual_from_base(self, r: int, s: int) -> Fraction:
        """Return the product change and verify the stationary cubic law."""

        row = self.row(r, s)
        left = self.base_left + self.left_step * r
        right = self.base_right + self.right_step * s
        base = self.base_row * self.base_left * self.base_right
        direct = row * left * right - base
        A, B = self.normalized_displacements(r, s)
        closed = -base * (A * A + A * B + B * B + A * B * (A + B))
        if direct != closed:
            raise AssertionError("the stationary affine cubic identity failed")
        return direct

    def necessary_displacement_bound(
        self,
        r: int,
        s: int,
        *,
        base_residual_bound: int,
        cell_residual_bound: int,
        target: int,
    ) -> Fraction:
        """Prove the positive-ellipse bound for one accepted chart cell.

        The method requires ``|A|+|B|<=1/4``.  If the base and cell products
        are respectively within the supplied bounds of ``target``, then

            A^2+B^2 <= 4*(base_bound+cell_bound)/(3*base_product).

        The returned value is the right side; an assertion checks the cell.
        """

        if not self.integral_row_law:
            raise ValueError("the stationary row law is not integral")
        A, B = self.normalized_displacements(r, s)
        if abs(A) + abs(B) > Fraction(1, 4):
            raise ValueError("the chart is outside the short stationary range")
        base = self.base_row * self.base_left * self.base_right
        cell = self.row(r, s) * (
            self.base_left + self.left_step * r
        ) * (
            self.base_right + self.right_step * s
        )
        if abs(base - target) > base_residual_bound:
            raise ValueError("the base point is outside its product window")
        if abs(cell - target) > cell_residual_bound:
            raise ValueError("the chart cell is outside its product window")
        bound = Fraction(
            4 * (base_residual_bound + cell_residual_bound), 3 * base
        )
        if A * A + B * B > bound:
            raise AssertionError("the stationary ellipse consequence failed")
        return bound


def stationary_lattice_point_ceiling(
    q: int,
    D: int,
    chart: StationaryAffineProduct,
    *,
    lower_shell_ratio: Fraction = Fraction(1, 3),
    upper_shell_ratio: Fraction = Fraction(2, 3),
) -> int:
    """Return an explicit ``O(D)`` ceiling from the stationary ellipse.

    Assume ``x0,b0,d0`` lie between ``lower*q`` and ``upper*q`` and both the
    base and cell use the unscaled QP tolerance ``q*D/8``.  Every short
    accepted cell then has ``|p*r|,|z*s| <=sqrt(C*D)`` with the explicit
    shell constant below.
    """

    if q <= 0 or D <= 0 or not chart.nondegenerate:
        raise ValueError("the ceiling requires a positive nondegenerate chart")
    low = lower_shell_ratio * q
    high = upper_shell_ratio * q
    if not all(low <= value <= high for value in (
        chart.base_row,
        chart.base_left,
        chart.base_right,
    )):
        raise ValueError("the base point is outside the declared shell")
    # From A^2+B^2 <= 2*q*D/(3*x0*b0*d0).
    # Multiplication by b0^2 (or d0^2) and shell comparability gives C*D.
    shell_constant = Fraction(2, 3) * upper_shell_ratio / (
        lower_shell_ratio * lower_shell_ratio
    )
    radius = sqrt(float(shell_constant * D))
    r_count = 2 * int(radius // abs(chart.left_step)) + 1
    s_count = 2 * int(radius // abs(chart.right_step)) + 1
    return r_count * s_count


@dataclass(frozen=True)
class TwoLegDirectionClassification:
    center_direction: Pair
    endpoint_direction: Pair
    first_hessian_degenerate: bool
    second_hessian_degenerate: bool
    simultaneous_degeneracy: bool
    coordinate_tangent_ruling: bool
    signed_tangent: bool


def classify_two_leg_directions(
    center_direction: Pair, endpoint_direction: Pair
) -> TwoLegDirectionClassification:
    """Classify degeneracy of the two coordinate-product Hessians.

    For nonzero directions ``U=(p,P)`` and ``Z=(z,Z)``, the first restored
    product is degenerate exactly when ``p*z=0`` and the second exactly when
    ``P*Z=0``.  Simultaneous degeneracy forces the directions onto opposite
    coordinate axes.  This is a signed tangent ruling, but the converse is
    false: the full tangent equation ``p*z-P*Z=0`` is strictly weaker.
    """

    p, other_p = center_direction
    z, other_z = endpoint_direction
    if center_direction == (0, 0) or endpoint_direction == (0, 0):
        raise ValueError("both affine directions must be nonzero")
    first = p * z == 0
    second = other_p * other_z == 0
    simultaneous = first and second
    coordinate = (
        (p == 0 and other_z == 0 and other_p != 0 and z != 0)
        or (other_p == 0 and z == 0 and p != 0 and other_z != 0)
    )
    if simultaneous != coordinate:
        raise AssertionError("simultaneous degeneracy classification failed")
    signed_tangent = p * z - other_p * other_z == 0
    if coordinate and not signed_tangent:
        raise AssertionError("a coordinate ruling was not tangent")
    return TwoLegDirectionClassification(
        center_direction=center_direction,
        endpoint_direction=endpoint_direction,
        first_hessian_degenerate=first,
        second_hessian_degenerate=second,
        simultaneous_degeneracy=simultaneous,
        coordinate_tangent_ruling=coordinate,
        signed_tangent=signed_tangent,
    )


@dataclass(frozen=True)
class ParallelTokenDirectionLedger:
    center_token_direction: Pair
    endpoint_token_direction: Pair
    center_physical_direction: Pair
    endpoint_physical_direction: Pair
    token_area: int
    first_product_cross: int
    second_product_cross: int
    token_norm: int
    coordinate_null_ruling: bool


def parallel_token_direction_ledger(
    c: int,
    C: int,
    u: int,
    v: int,
    center_token_direction: Pair,
    endpoint_token_direction: Pair,
) -> ParallelTokenDirectionLedger:
    """Lift a parallel token-direction pair and classify its radial curvature.

    The two physical direction maps are the linear parts of the Bezout chart.
    If the token area vanishes, their signed cross products agree.  They both
    vanish exactly on the coordinate-null ruling; otherwise either physical
    product leg has nonzero stationary Hessian.
    """

    if c * u - C * v != 1:
        raise ValueError("the supplied coefficients are not Bezout coefficients")
    V0, V1 = center_token_direction
    W0, W1 = endpoint_token_direction
    if center_token_direction == (0, 0) or endpoint_token_direction == (0, 0):
        raise ValueError("token directions must be nonzero")
    token_area = V0 * W1 - V1 * W0
    if token_area != 0:
        raise ValueError("the ledger is only for the parallel token branch")
    p = u * V0 - C * V1
    other_p = v * V0 - c * V1
    z = -v * W0 + c * W1
    other_z = -u * W0 + C * W1
    first_cross = p * z
    second_cross = other_p * other_z
    if first_cross != second_cross:
        raise AssertionError("parallel tokens did not lift to a signed tangent pair")
    mixed = c * u + C * v
    token_norm = (
        -2 * u * v * V0 * V0
        + 2 * mixed * V0 * V1
        - 2 * c * C * V1 * V1
    )
    if token_norm != -2 * p * other_p:
        raise AssertionError("the token norm did not match the physical direction")
    null = first_cross == 0
    classification = classify_two_leg_directions((p, other_p), (z, other_z))
    if null != classification.coordinate_tangent_ruling:
        raise AssertionError("the parallel null-direction classification failed")
    return ParallelTokenDirectionLedger(
        center_token_direction=center_token_direction,
        endpoint_token_direction=endpoint_token_direction,
        center_physical_direction=(p, other_p),
        endpoint_physical_direction=(z, other_z),
        token_area=token_area,
        first_product_cross=first_cross,
        second_product_cross=second_cross,
        token_norm=token_norm,
        coordinate_null_ruling=null,
    )


def actual_prime_stationary_integrality_obstruction(
    base_row: int, base_factor: int, factor_step: int
) -> bool:
    """Return whether a nonzero short stationary row step is impossible.

    If ``gcd(base_row,base_factor)=1`` and ``0<|factor_step|<base_factor``,
    integrality of ``-base_row*factor_step/base_factor`` is impossible.  This
    is the generic all-distinct actual-prime situation and explains why the
    principal full-integer proof does not automatically globalize.
    """

    return (
        gcd(base_row, base_factor) == 1
        and 0 < abs(factor_step) < base_factor
        and (base_row * factor_step) % base_factor != 0
    )
