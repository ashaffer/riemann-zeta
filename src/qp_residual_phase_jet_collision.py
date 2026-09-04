"""Exact phase-jet fingerprints for the transverse symmetric-cusp residual.

The functions in this module are an arithmetic audit, not a physical large
sieve.  They attach two canonical stationary phases to a primitive tangent
``(p,d)`` and evaluate their lifted action defects at the physical parameter
``t=(Q+y)/(2Q)``.  Together with the regular tangent curvature, these defects
form an exactly invertible fingerprint, up to the unavoidable reflection

    (y,r,s,d,n) -> (-y,s,r,-d,-n).

The cubic phase generally lies outside the actual Fejer frequency support at
large primitive height.  Consequently the fingerprint is a useful inverse
theorem target, but its realization as a physical Bessel variable remains a
separate analytic problem.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt
from typing import Iterable

from qp_coupled_cusp_fejer_inverse import (
    ReducedSymmetricCuspData,
    reduced_symmetric_cusp_data,
)
from qp_dual_tangent_major_arc import normalized_phase_derivatives
from qp_high_primitive_packet_pair_audit import scaled_cusp_normal_form


Frequency = tuple[int, int, int]  # coordinates (-m,h,k)


def _phase_value(frequency: Frequency, t: Fraction) -> Fraction:
    """Evaluate ``Phi(t)=h/(4t)+k/(4(1-t))-m*t`` exactly."""

    minus_m, h, k = frequency
    return minus_m * t + Fraction(h, 4) / t + Fraction(k, 4) / (1 - t)


def _fractional_part(value: Fraction) -> Fraction:
    return value - value.numerator // value.denominator


def _distance_to_integer(value: Fraction) -> Fraction:
    residue = _fractional_part(value)
    return min(residue, 1 - residue)


@dataclass(frozen=True)
class ResidualPhaseJet:
    """Canonical regular/cubic phase data for one physical cusp point."""

    point: ReducedSymmetricCuspData
    parity_divisor: int
    left_direction: int
    right_direction: int
    direction_sum: int
    caustic_divisor: int
    physical_parameter: Fraction
    tangent_parameter: Fraction
    regular_frequency: Frequency
    caustic_frequency: Frequency
    regular_action: Fraction
    regular_tangent_action: Fraction
    regular_action_defect: Fraction
    caustic_action: Fraction
    caustic_tangent_action: Fraction
    caustic_action_defect: Fraction
    regular_tangent_curvature: Fraction
    regular_physical_slope: Fraction
    regular_physical_curvature: Fraction
    caustic_physical_slope: Fraction
    caustic_physical_curvature: Fraction
    caustic_physical_third: Fraction
    scaled_z: int
    scaled_v: int
    scaled_residual: int

    @property
    def oriented_fingerprint(self) -> tuple[object, ...]:
        """A lifted exact fingerprint which distinguishes reflection."""

        return (
            self.parity_divisor,
            self.regular_tangent_curvature,
            self.regular_action_defect,
            self.caustic_action_defect,
        )

    @property
    def unoriented_fingerprint(self) -> tuple[object, ...]:
        """The exact fingerprint after quotienting by reflection."""

        return (
            self.parity_divisor,
            self.regular_tangent_curvature,
            self.regular_action_defect,
            abs(self.caustic_action_defect),
        )

    @property
    def caustic_character_distance(self) -> Fraction:
        """Distance of the cubic action defect to the character lattice."""

        return _distance_to_integer(self.caustic_action_defect)


def residual_phase_jet(point: ReducedSymmetricCuspData) -> ResidualPhaseJet:
    """Return and verify the canonical phase-jet fingerprint.

    Put ``c=gcd(p+d,p-d)``, ``a=(p+d)/c``, ``b=(p-d)/c`` and
    ``N=a+b``.  The two phases are

    ``Phi_2=(a^2/t+b^2/(1-t))/4``

    and

    ``Phi_3=(a^3/t-b^3/(1-t)+N^3*t)/c_0``,

    where ``c_0=gcd(4,N^3)``.  The first has a regular stationary point
    and the second a cubic stationary point at ``t_0=a/N``.  If
    ``n=p*y-Q*d``, their exact lifted action defects are

    ``J_2=2Q*n^2/(c^2*(Q^2-y^2))`` and
    ``J_3=-8*n^3/(c_0*c^3*(Q^2-y^2))``.

    In particular ``J_3/(c*J_2)=-n/Q`` whenever ``n!=0``.
    """

    if point.Q <= abs(point.y):
        raise ValueError("require an interior physical point |y|<Q")
    if point.d == 0 or point.p <= abs(point.d):
        raise ValueError("require a nonsingular primitive tangent p>|d|>0")

    Q, y, p, d = point.Q, point.y, point.p, point.d
    parity = gcd(p + d, p - d)
    if parity not in (1, 2):
        raise AssertionError("a primitive tangent has parity divisor one or two")
    left = (p + d) // parity
    right = (p - d) // parity
    direction_sum = left + right
    caustic_divisor = gcd(4, direction_sum**3)
    assert caustic_divisor * parity**2 == 4

    regular_frequency = (0, left * left, right * right)
    caustic_frequency = (
        direction_sum**3 // caustic_divisor,
        4 * left**3 // caustic_divisor,
        -4 * right**3 // caustic_divisor,
    )
    physical_t = Fraction(Q + y, 2 * Q)
    tangent_t = Fraction(left, direction_sum)
    assert physical_t - tangent_t == Fraction(point.n, 2 * Q * p)

    scale = 2 * Q
    regular_action = scale * _phase_value(regular_frequency, physical_t)
    regular_tangent_action = scale * _phase_value(regular_frequency, tangent_t)
    regular_defect = regular_action - regular_tangent_action
    caustic_action = scale * _phase_value(caustic_frequency, physical_t)
    caustic_tangent_action = scale * _phase_value(caustic_frequency, tangent_t)
    caustic_defect = caustic_action - caustic_tangent_action

    denominator = Q * Q - y * y
    assert regular_defect == Fraction(
        2 * Q * point.n * point.n,
        parity * parity * denominator,
    )
    assert caustic_defect == Fraction(
        -8 * point.n**3,
        caustic_divisor * parity**3 * denominator,
    )
    if point.n:
        assert caustic_defect / (parity * regular_defect) == Fraction(
            -point.n, Q
        )

    regular_derivatives = normalized_phase_derivatives(
        Fraction(1, 4),
        regular_frequency[1],
        regular_frequency[2],
        -regular_frequency[0],
        physical_t,
    )
    regular_tangent_derivatives = normalized_phase_derivatives(
        Fraction(1, 4),
        regular_frequency[1],
        regular_frequency[2],
        -regular_frequency[0],
        tangent_t,
    )
    caustic_derivatives = normalized_phase_derivatives(
        Fraction(1, 4),
        caustic_frequency[1],
        caustic_frequency[2],
        -caustic_frequency[0],
        physical_t,
    )
    assert regular_tangent_derivatives["first"] == 0
    tangent_curvature = Fraction(
        direction_sum**4, 2 * left * right
    )
    assert regular_tangent_derivatives["second"] == tangent_curvature
    assert tangent_curvature == Fraction(
        8 * p**4, parity**2 * (p * p - d * d)
    )

    # The phase on the reciprocal curve differs from its value at the
    # corresponding integral physical point by the weighted product errors.
    first_coordinate = Q + y
    second_coordinate = Q - y + point.r
    third_coordinate = Q + y + point.s
    for frequency, action in (
        (regular_frequency, regular_action),
        (caustic_frequency, caustic_action),
    ):
        lattice_action = (
            frequency[0] * first_coordinate
            + frequency[1] * second_coordinate
            + frequency[2] * third_coordinate
        )
        error_correction = (
            Fraction(frequency[1] * point.e, Q + y)
            + Fraction(frequency[2] * point.f, Q - y)
        )
        assert action + error_correction == lattice_action

    normal = scaled_cusp_normal_form(point)
    return ResidualPhaseJet(
        point=point,
        parity_divisor=parity,
        left_direction=left,
        right_direction=right,
        direction_sum=direction_sum,
        caustic_divisor=caustic_divisor,
        physical_parameter=physical_t,
        tangent_parameter=tangent_t,
        regular_frequency=regular_frequency,
        caustic_frequency=caustic_frequency,
        regular_action=regular_action,
        regular_tangent_action=regular_tangent_action,
        regular_action_defect=regular_defect,
        caustic_action=caustic_action,
        caustic_tangent_action=caustic_tangent_action,
        caustic_action_defect=caustic_defect,
        regular_tangent_curvature=tangent_curvature,
        regular_physical_slope=regular_derivatives["first"],
        regular_physical_curvature=regular_derivatives["second"],
        caustic_physical_slope=caustic_derivatives["first"],
        caustic_physical_curvature=caustic_derivatives["second"],
        caustic_physical_third=caustic_derivatives["third"],
        scaled_z=int(normal["z"]),
        scaled_v=int(normal["v"]),
        scaled_residual=int(normal["quadratic_residual"]),
    )


def reconstruct_reduced_data_from_fingerprint(
    Q: int,
    parity_divisor: int,
    tangent_curvature: Fraction,
    regular_action_defect: Fraction,
    caustic_action_defect: Fraction,
) -> dict[str, int]:
    """Invert an oriented lifted fingerprint to ``(p,d,y,n)``.

    The result includes signed ``d`` and ``y``.  It does not recover the
    content ``g`` without the product bands; the narrow-band uniqueness
    lemma below supplies that last step in the QP application.
    """

    if Q <= 0 or parity_divisor not in (1, 2):
        raise ValueError("require Q>0 and parity divisor one or two")
    curvature = Fraction(tangent_curvature)
    J2, J3 = Fraction(regular_action_defect), Fraction(caustic_action_defect)
    if curvature <= 0 or J2 <= 0 or J3 == 0:
        raise ValueError("the oriented residual fingerprint is nondegenerate")

    reduced_curvature = curvature * parity_divisor**2 / 8
    # p^4/(p^2-d^2) is already in lowest terms because gcd(p,d)=1.
    p_fourth = reduced_curvature.numerator
    p = isqrt(isqrt(p_fourth))
    if p <= 0 or p**4 != p_fourth:
        raise ValueError("curvature numerator is not a primitive fourth power")
    ell = reduced_curvature.denominator
    d_square = p * p - ell
    if d_square <= 0:
        raise ValueError("curvature denominator does not give an interior slope")
    d_abs = isqrt(d_square)
    if d_abs**2 != d_square or gcd(p, d_abs) != 1:
        raise ValueError("curvature does not encode a primitive direction")

    n_value = Fraction(-Q) * J3 / (parity_divisor * J2)
    if n_value.denominator != 1 or n_value == 0:
        raise ValueError("action ratio does not encode a nonzero integral n")
    n = n_value.numerator
    denominator_value = Fraction(
        2 * Q * n * n,
        parity_divisor**2,
    ) / J2
    if denominator_value.denominator != 1:
        raise ValueError("regular action does not encode integral Q^2-y^2")
    y_square = Q * Q - denominator_value.numerator
    if y_square <= 0:
        raise ValueError("action defect does not encode an interior y")
    y_abs = isqrt(y_square)
    if y_abs**2 != y_square:
        raise ValueError("action denominator does not encode integral y")

    candidates: list[tuple[int, int]] = []
    for y in (y_abs, -y_abs):
        numerator = p * y - n
        if numerator % Q:
            continue
        d = numerator // Q
        if abs(d) == d_abs:
            candidates.append((y, d))
    if len(candidates) != 1:
        raise ValueError("the oriented fingerprint has no unique sign lift")
    y, d = candidates[0]
    if gcd(p + d, p - d) != parity_divisor:
        raise ValueError("recovered signs have the wrong parity divisor")
    return {"p": p, "d": d, "y": y, "n": n, "ell": ell}


def content_is_unique_in_narrow_left_band(
    Q: int, y: int, p: int, d: int, left_half_width: int
) -> bool:
    """Sufficient exact condition for at most one admissible content ``g``.

    Changing ``g`` by one changes the left product error by
    ``(p-d)(Q+y)/2``.  Two values inside ``[-A,A]`` are therefore impossible
    when this step is larger than ``2A``.  The test uses absolute orientation
    so it remains valid after reflection.
    """

    if Q <= abs(y) or p <= abs(d) or left_half_width < 0:
        raise ValueError("invalid compact-band parameters")
    minimum_step_twice = (p - abs(d)) * (Q - abs(y))
    return minimum_step_twice > 4 * left_half_width


def reflected_point(point: ReducedSymmetricCuspData) -> ReducedSymmetricCuspData:
    """Return the exact physical reflection ``(y,r,s)->(-y,s,r)``."""

    return reduced_symmetric_cusp_data(point.Q, -point.y, point.s, point.r)


def reflection_jet_identity(point: ReducedSymmetricCuspData) -> dict[str, bool]:
    """Verify the exact action/derivative identities under reflection."""

    left = residual_phase_jet(point)
    right = residual_phase_jet(reflected_point(point))
    return {
        "same_unoriented_fingerprint": (
            left.unoriented_fingerprint == right.unoriented_fingerprint
        ),
        "opposite_cubic_defect": (
            left.caustic_action_defect == -right.caustic_action_defect
        ),
        "same_regular_defect": (
            left.regular_action_defect == right.regular_action_defect
        ),
        "same_caustic_slope": (
            left.caustic_physical_slope == right.caustic_physical_slope
        ),
        "opposite_caustic_curvature": (
            left.caustic_physical_curvature == -right.caustic_physical_curvature
        ),
        "same_caustic_third": (
            left.caustic_physical_third == right.caustic_physical_third
        ),
    }


def non_square_n_one_residual_family(
    multiplier: int, d: int
) -> ReducedSymmetricCuspData:
    """Return an infinite non-square-content, nonaxis residual family.

    Put ``p=multiplier*d+1``, ``ell=p^2-d^2``, ``g=2d``, ``y=ell`` and
    ``Q=(p*ell-1)/d``.  Then ``n=1``, ``v=0``, ``z=2d`` and
    ``K=4d^2``.  For ``d>2``, ``d^2`` does not divide ``g``.
    """

    if multiplier < 2 or d <= 2:
        raise ValueError("require multiplier>=2 and d>2")
    p = multiplier * d + 1
    ell = p * p - d * d
    numerator = p * ell - 1
    assert numerator % d == 0
    Q = numerator // d
    y = ell
    g = 2 * d
    r = g * (p - d) // 2
    s = g * (p + d) // 2
    point = reduced_symmetric_cusp_data(Q, y, r, s)
    normal = scaled_cusp_normal_form(point)
    assert point.n == 1
    assert point.e == -(p - d) and point.f == -(p + d)
    assert point.g == g and g % (d * d) != 0
    assert (normal["v"], normal["z"], normal["quadratic_residual"]) == (
        0,
        2 * d,
        4 * d * d,
    )
    return point


def enumerate_transverse_non_square_residuals(
    Q: int,
    A: int,
    B: int,
    y_limit: int | None = None,
    *,
    strict_remote: bool = False,
) -> tuple[ReducedSymmetricCuspData, ...]:
    """Exhaust a finite residual window after every proved algebraic peel.

    The scan deletes ``n=0``, ``L=0``, the translated tangent, the scaled
    balanced axis ``z=0``, the two one-band axes ``K=0``, and the full
    square-content locus ``d^2|g``.  ``strict_remote`` additionally imposes
    the older finite proxies ``rho^3>Q`` and ``r^2>A``.
    """

    if min(Q, A, B) <= 0 or A > B or 2 * B >= Q:
        raise ValueError("require 0<A<=B<Q/2")
    if y_limit is None:
        y_limit = Q // 3
    if y_limit < 0 or 2 * y_limit >= Q:
        raise ValueError("require 0<=y_limit<Q/2")

    def candidates(numerator: int, denominator: int, width: int) -> Iterable[int]:
        lower = numerator // denominator
        for value in (lower, lower + 1):
            if abs(value * denominator - numerator) <= width:
                yield value

    answer: list[ReducedSymmetricCuspData] = []
    for y in range(-y_limit, y_limit + 1):
        square = y * y
        for r in candidates(square, Q + y, A):
            for s in candidates(square, Q - y, B):
                point = reduced_symmetric_cusp_data(Q, y, r, s)
                if (
                    point.d == 0
                    or point.p <= abs(point.d)
                    or point.n == 0
                    or point.L == 0
                    or point.kappa == 0
                ):
                    continue
                if strict_remote and (point.rho**3 <= Q or point.r * point.r <= A):
                    continue
                normal = scaled_cusp_normal_form(point)
                if normal["z"] == 0 or normal["quadratic_residual"] == 0:
                    continue
                if point.g % (point.d * point.d) == 0:
                    continue
                answer.append(point)
    return tuple(answer)


@dataclass(frozen=True)
class ResidualJetCollisionAudit:
    point_count: int
    reflection_orbit_count: int
    cubic_character_class_count: int
    maximum_cubic_character_multiplicity: int
    nonreflection_cubic_character_collisions: int
    unoriented_fingerprint_class_count: int
    maximum_unoriented_fingerprint_multiplicity: int
    nonreflection_full_jet_collisions: int


def _reflection_shape(point: ReducedSymmetricCuspData) -> tuple[int, ...]:
    return (
        abs(point.y),
        min(point.r, point.s),
        max(point.r, point.s),
        point.g,
        point.p,
        abs(point.d),
        abs(point.n),
        min(point.e, point.f),
        max(point.e, point.f),
    )


def residual_jet_collision_audit(
    points: Iterable[ReducedSymmetricCuspData],
) -> ResidualJetCollisionAudit:
    """Cluster exact lifted/character phase labels and classify collisions."""

    materialized = tuple(points)
    character_classes: dict[tuple[object, ...], list[ResidualPhaseJet]] = defaultdict(list)
    full_classes: dict[tuple[object, ...], list[ResidualPhaseJet]] = defaultdict(list)
    shapes = set()
    for point in materialized:
        jet = residual_phase_jet(point)
        shapes.add(_reflection_shape(point))
        character_classes[
            (
                jet.parity_divisor,
                jet.caustic_character_distance,
            )
        ].append(jet)
        full_classes[jet.unoriented_fingerprint].append(jet)

    def nonreflection_collisions(
        classes: dict[tuple[object, ...], list[ResidualPhaseJet]],
    ) -> int:
        total = 0
        for members in classes.values():
            orbit_shapes = {_reflection_shape(member.point) for member in members}
            total += max(0, len(orbit_shapes) - 1)
        return total

    return ResidualJetCollisionAudit(
        point_count=len(materialized),
        reflection_orbit_count=len(shapes),
        cubic_character_class_count=len(character_classes),
        maximum_cubic_character_multiplicity=max(
            map(len, character_classes.values()), default=0
        ),
        nonreflection_cubic_character_collisions=nonreflection_collisions(
            character_classes
        ),
        unoriented_fingerprint_class_count=len(full_classes),
        maximum_unoriented_fingerprint_multiplicity=max(
            map(len, full_classes.values()), default=0
        ),
        nonreflection_full_jet_collisions=nonreflection_collisions(full_classes),
    )


def phase_lift_exponent_ledger() -> dict[str, Fraction]:
    """Return action-wrap exponents at the worst energy endpoint.

    With ``B=D^(7/6)`` and ``Q=D^(33/16)``, the quadratic action can have
    ``O(1+B^2/Q)=D^(13/48)`` integer lifts.  The cubic defect is
    ``O(B^3/Q^2)=D^(-5/8)``, hence is unwrapped.  The lift count is below
    the smallest ``sqrt(A)=D^(1/2)`` budget by ``D^(11/48)``.
    """

    B = Fraction(7, 6)
    Q = Fraction(33, 16)
    quadratic_wrap = 2 * B - Q
    cubic_size = 3 * B - 2 * Q
    square_root_budget = Fraction(1, 2)
    assert quadratic_wrap == Fraction(13, 48)
    assert cubic_size == Fraction(-5, 8)
    return {
        "B": B,
        "Q": Q,
        "quadratic_wrap_count": quadratic_wrap,
        "cubic_action_size": cubic_size,
        "sqrt_A_floor": square_root_budget,
        "wrap_count_margin": square_root_budget - quadratic_wrap,
    }


def residual_frequency_support_ledger() -> dict[str, Fraction]:
    """Compare the virtual fingerprint with the actual Fejer support.

    After the three scaled-axis peels, the residual primitive height is
    ``p>=D^(77/160)`` and the Fejer frequency cutoff is ``H=D^(17/16)``.
    The regular canonical frequency has size ``p^2`` and is available only
    up to ``p=D^(17/32)``.  The primitive cubic frequency has size ``p^3``
    and is already above ``H`` at the residual floor.
    """

    p_floor = Fraction(77, 160)
    H = Fraction(17, 16)
    regular_at_floor = 2 * p_floor
    cubic_at_floor = 3 * p_floor
    regular_ceiling = H / 2
    return {
        "residual_p_floor": p_floor,
        "H": H,
        "regular_frequency_at_floor": regular_at_floor,
        "regular_support_margin_at_floor": H - regular_at_floor,
        "regular_p_ceiling": regular_ceiling,
        "regular_residual_strip_width": regular_ceiling - p_floor,
        "cubic_frequency_at_floor": cubic_at_floor,
        "cubic_support_deficit_at_floor": cubic_at_floor - H,
    }
