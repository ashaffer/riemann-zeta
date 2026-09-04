"""Exact rigidity in the small-step/small-remainder self-orbit sector.

The dyadic reciprocal scale ``K`` has physical radius ``R=sqrt(q/K)``.
If one realized primitive direction ``U=(p,P)`` satisfies

    ||U||_infinity * R <= D,
    |c*p-C*P| * R**2 <= 2*D**2,

then every other realized radius-``R`` direction is parallel to ``U``.
This module records that integral argument and the exact macroscopic
separation of the resulting parallel tower.  It does not prove the open
signed translate-Bessel/MSPD estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Mapping


Pair = tuple[int, int]


def det(left: Pair, right: Pair) -> int:
    return left[0] * right[1] - left[1] * right[0]


def primitive_content(vector: Pair) -> int:
    return gcd(abs(vector[0]), abs(vector[1]))


def anchor_remainder(anchor: Pair, direction: Pair) -> int:
    """Return ``c*p-C*P`` for ``anchor=(c,C)`` and ``U=(p,P)``."""

    c, C = anchor
    p, P = direction
    return c * p - C * P


def orbit_label(anchor: Pair, point: Pair) -> int:
    c, C = anchor
    b, B = point
    return c * b - C * B


def line_index(direction: Pair, point: Pair) -> int:
    """The affine ``U``-line index ``det(U,z)``."""

    return det(direction, point)


def two_direction_identity(
    anchor: Pair, first: Pair, second: Pair
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return both exact small-remainder determinant identities.

    If ``rho_U=c*p-C*P`` and ``rho_V=c*s-C*S``, then

    ``C det(U,V)=rho_U*s-rho_V*p`` and
    ``c det(U,V)=rho_U*S-rho_V*P``.
    """

    c, C = anchor
    p, P = first
    s, S = second
    rho_first = anchor_remainder(anchor, first)
    rho_second = anchor_remainder(anchor, second)
    determinant = det(first, second)
    return (
        (C * determinant, rho_first * s - rho_second * p),
        (c * determinant, rho_first * S - rho_second * P),
    )


@dataclass(frozen=True)
class HardDirectionCollapseCertificate:
    anchor: Pair
    D: int
    radius: int
    hard_direction: Pair
    hard_remainder: int
    determinant_numerator_bound: int
    anchor_minimum: int
    realized_directions: tuple[Pair, ...]
    all_parallel: bool


def certify_hard_direction_collapse(
    anchor: Pair,
    D: int,
    radius: int,
    hard_direction: Pair,
    realized_directions: Iterable[Pair],
) -> HardDirectionCollapseCertificate:
    """Certify that one hard direction absorbs every radius-``R`` direction.

    A realized primitive direction ``V`` is required to satisfy
    ``||V||_infinity<=R`` and ``|c*s-C*S|<=2D``.  The hard direction obeys
    the scale-sensitive bounds displayed in the module docstring.  Under
    ``R**2>=D`` and ``8*D*R<min(c,C)``, the determinant identity puts
    ``C*det(U,V)`` strictly between ``-C`` and ``C``.
    """

    c, C = map(int, anchor)
    D, radius = int(D), int(radius)
    p, P = map(int, hard_direction)
    if min(c, C, D, radius) <= 0 or gcd(c, C) != 1:
        raise ValueError("require a positive primitive anchor and positive scales")
    if primitive_content((p, P)) != 1:
        raise ValueError("the hard direction must be primitive")
    if radius * radius < D or 8 * D * radius >= min(c, C):
        raise ValueError("require R^2>=D and 8*D*R<min(anchor)")
    hard_remainder = anchor_remainder(anchor, (p, P))
    if max(abs(p), abs(P)) * radius > D:
        raise ValueError("the hard direction is not small-step")
    if abs(hard_remainder) * radius * radius > 2 * D * D:
        raise ValueError("the hard direction is not small-remainder")
    if not hard_remainder:
        raise ValueError("a short direction cannot be parallel to the anchor")

    selected = tuple((int(s), int(S)) for s, S in realized_directions)
    all_parallel = True
    for direction in selected:
        if primitive_content(direction) != 1:
            raise ValueError("every realized direction must be primitive")
        if max(map(abs, direction)) > radius:
            raise ValueError("a realized direction exceeds the radius")
        if abs(anchor_remainder(anchor, direction)) > 2 * D:
            raise ValueError("a realized direction exceeds the label window")
        first_identity, second_identity = two_direction_identity(
            anchor, (p, P), direction
        )
        if (
            first_identity[0] != first_identity[1]
            or second_identity[0] != second_identity[1]
        ):
            raise AssertionError("the two-direction identity failed")
        numerator = abs(first_identity[1])
        direct_bound = abs(hard_remainder) * abs(direction[0]) + abs(
            anchor_remainder(anchor, direction)
        ) * abs(p)
        if numerator > direct_bound:
            raise AssertionError("the triangle-inequality bound failed")
        if direct_bound * radius > 4 * D * D:
            raise AssertionError("the scale-sensitive determinant bound failed")
        # R^2>=D turns 4D^2/R into at most 4DR, which is < C.
        if direct_bound >= C:
            raise AssertionError("the integral determinant is not forced to vanish")
        all_parallel &= det((p, P), direction) == 0
    if not all_parallel:
        raise AssertionError("a realized direction escaped the unique hard tower")
    return HardDirectionCollapseCertificate(
        anchor=(c, C),
        D=D,
        radius=radius,
        hard_direction=(p, P),
        hard_remainder=hard_remainder,
        determinant_numerator_bound=4 * D * D // radius,
        anchor_minimum=min(c, C),
        realized_directions=selected,
        all_parallel=True,
    )


@dataclass(frozen=True)
class TowerCoordinateLedger:
    anchor: Pair
    direction: Pair
    point: Pair
    remainder: int
    label: int
    line_index: int
    first_identity: tuple[int, int]
    second_identity: tuple[int, int]


def tower_coordinate_ledger(
    anchor: Pair, direction: Pair, point: Pair
) -> TowerCoordinateLedger:
    """Verify ``r*b=p*t+C*s`` and ``r*B=P*t+c*s`` exactly."""

    c, C = anchor
    p, P = direction
    b, B = point
    remainder = anchor_remainder(anchor, direction)
    label = orbit_label(anchor, point)
    index = line_index(direction, point)
    first = (remainder * b, p * label + C * index)
    second = (remainder * B, P * label + c * index)
    if first[0] != first[1] or second[0] != second[1]:
        raise AssertionError("the exact tower coordinate identity failed")
    return TowerCoordinateLedger(
        anchor=anchor,
        direction=direction,
        point=point,
        remainder=remainder,
        label=label,
        line_index=index,
        first_identity=first,
        second_identity=second,
    )


@dataclass(frozen=True)
class InterlineSeparationCertificate:
    remainder: int
    label_difference: int
    line_index_difference: int
    first_distance: int
    second_distance: int
    first_numerator_lower_bound: int
    second_numerator_lower_bound: int


def certify_interline_separation(
    anchor: Pair,
    D: int,
    direction: Pair,
    first: Pair,
    second: Pair,
) -> InterlineSeparationCertificate:
    """Certify the exact coordinate gap between two distinct ``U``-lines.

    With ``r=c*p-C*P`` and ``s=det(U,z)``, subtraction of the tower
    identities gives

    ``|r|*|Delta b| >= C-2D|p|`` and
    ``|r|*|Delta B| >= c-2D|P|``

    whenever both labels lie in ``[-D,D]`` and the line indices differ.
    """

    c, C = anchor
    p, P = direction
    r = anchor_remainder(anchor, direction)
    if not r:
        raise ValueError("the direction remainder must be nonzero")
    t_first, t_second = orbit_label(anchor, first), orbit_label(anchor, second)
    if max(abs(t_first), abs(t_second)) > D:
        raise ValueError("both points must lie in the short orbit")
    s_first = line_index(direction, first)
    s_second = line_index(direction, second)
    if s_first == s_second:
        raise ValueError("the points lie on the same affine U-line")
    delta_t = t_second - t_first
    delta_s = s_second - s_first
    delta_b = second[0] - first[0]
    delta_B = second[1] - first[1]
    if r * delta_b != p * delta_t + C * delta_s:
        raise AssertionError("the first subtracted tower identity failed")
    if r * delta_B != P * delta_t + c * delta_s:
        raise AssertionError("the second subtracted tower identity failed")
    first_lower = C - 2 * D * abs(p)
    second_lower = c - 2 * D * abs(P)
    if abs(r) * abs(delta_b) < first_lower:
        raise AssertionError("the first-coordinate interline gap failed")
    if abs(r) * abs(delta_B) < second_lower:
        raise AssertionError("the second-coordinate interline gap failed")
    return InterlineSeparationCertificate(
        remainder=r,
        label_difference=delta_t,
        line_index_difference=delta_s,
        first_distance=abs(delta_b),
        second_distance=abs(delta_B),
        first_numerator_lower_bound=first_lower,
        second_numerator_lower_bound=second_lower,
    )


@dataclass(frozen=True)
class TowerLineCountCertificate:
    remainder: int
    line_indices: tuple[int, ...]
    line_count: int
    residue_count: int
    coordinate_diameter: int
    same_residue_exclusion_margin: int


def certify_tower_line_count(
    anchor: Pair,
    D: int,
    direction: Pair,
    labelled_points: Mapping[int, Pair],
) -> TowerLineCountCertificate:
    """Certify that a narrow short orbit occupies at most ``|r|`` U-lines.

    The proof uses a unimodular companion to ``U``.  If two line indices
    are congruent modulo ``r``, their labels are also congruent modulo
    ``r`` and their point difference is ``k*U+l*(C,c)``.  The displayed
    shell-diameter condition forces ``l=0``.
    """

    c, C = anchor
    p, P = direction
    r = anchor_remainder(anchor, direction)
    modulus = abs(r)
    if gcd(c, C) != 1:
        raise ValueError("the anchor must be primitive")
    if primitive_content(direction) != 1 or not modulus:
        raise ValueError("require a primitive direction of nonzero remainder")
    points = {int(t): (int(z[0]), int(z[1])) for t, z in labelled_points.items()}
    for t, point in points.items():
        if abs(t) > D or orbit_label(anchor, point) != t:
            raise ValueError("the mapping is not contained in the short orbit")
    if points:
        firsts = [point[0] for point in points.values()]
        seconds = [point[1] for point in points.values()]
        diameter = max(max(firsts) - min(firsts), max(seconds) - min(seconds))
    else:
        diameter = 0
    step = max(abs(p), abs(P))
    # Multiplying by |r| avoids a rounding issue in 2D*step/|r|.
    margin = modulus * min(c, C) - modulus * diameter - 2 * D * step
    if margin <= 0:
        raise ValueError("the shell is not narrow enough to identify line residues")

    indices = tuple(sorted({line_index(direction, point) for point in points.values()}))
    residues = {index % modulus for index in indices}
    if len(residues) != len(indices):
        raise AssertionError("two distinct lines have the same residue modulo r")
    if len(indices) > modulus:
        raise AssertionError("the tower has more than |r| parallel lines")
    return TowerLineCountCertificate(
        remainder=r,
        line_indices=indices,
        line_count=len(indices),
        residue_count=len(residues),
        coordinate_diameter=diameter,
        same_residue_exclusion_margin=margin,
    )


@dataclass(frozen=True)
class CenteredReciprocalHessianBounds:
    q: int
    lower_shell_ratio: Fraction
    upper_shell_ratio: Fraction
    lower_eigenvalue_coefficient: Fraction
    upper_eigenvalue_coefficient: Fraction


def centered_reciprocal_hessian_bounds(
    q: int, lower: int, upper: int
) -> CenteredReciprocalHessianBounds:
    """Give explicit ``constant/q`` Hessian bounds on a positive shell.

    For ``Phi(x,y)=q^3/(8xy)+x+y``, the Hessian determinant is
    ``3(q^3/8)^2/(x^4*y^4)``.  If ``alpha*q<=x,y<=beta*q``, then every
    eigenvalue lies between

    ``3*alpha^4/(32*beta^8*q)`` and ``1/(2*alpha^4*q)``.

    The lower bound is ``det(H)/trace(H)`` and the upper bound is the trace.
    """

    q, lower, upper = int(q), int(lower), int(upper)
    if q <= 0 or not (0 < lower <= upper):
        raise ValueError("require a positive shell")
    alpha = Fraction(lower, q)
    beta = Fraction(upper, q)
    return CenteredReciprocalHessianBounds(
        q=q,
        lower_shell_ratio=alpha,
        upper_shell_ratio=beta,
        lower_eigenvalue_coefficient=Fraction(3, 32) * alpha**4 / beta**8,
        upper_eigenvalue_coefficient=Fraction(1, 2) / alpha**4,
    )


def exact_stationary_gradient_gap_lower_bound(
    q: int,
    h: int,
    lower: int,
    upper: int,
    anchor: Pair,
    D: int,
    direction: Pair,
) -> Fraction:
    """Lower-bound scaled gradient separation for distinct tower cells.

    Strong convexity of the centered reciprocal phase converts the exact
    interline distance into separation of the B-process stationary-frequency
    images.  This is a geometric statement only; it does not imply
    orthogonality of the resulting scalar Legendre actions.
    """

    if h <= 0:
        raise ValueError("the Fourier frequency must be positive")
    bounds = centered_reciprocal_hessian_bounds(q, lower, upper)
    r = abs(anchor_remainder(anchor, direction))
    if not r:
        raise ValueError("the direction remainder must be nonzero")
    step = max(map(abs, direction))
    coordinate_gap_numerator = min(anchor) - 2 * D * step
    if coordinate_gap_numerator <= 0:
        raise ValueError("the interline coordinate gap is not positive")
    minimum_lane_step = min(abs(direction[0]), abs(direction[1]))
    if minimum_lane_step <= 0:
        raise ValueError("the hard direction must be noncoordinate")
    # Hess(Phi) >= lambda_0/q.  Scaling the two lane variables multiplies
    # Euclidean gradient separation by at least min(|p|,|P|).
    return (
        Fraction(h * minimum_lane_step * coordinate_gap_numerator, q * r)
        * bounds.lower_eigenvalue_coefficient
    )
