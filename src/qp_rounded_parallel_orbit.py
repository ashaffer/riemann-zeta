"""One-orbit and rounded-row identities for parallel Bezout token charts.

The identities here are lossless.  They do not assert the open occupied-cell
bound.  Their purpose is to replace an arbitrary pair of token strips by the
single modular orbit forced by a fixed primitive anchor, and to state exactly
what a finite-difference argument can recover from unique integer completion
rows.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from qp_four_completion_bezout_token import BezoutTokenChart


Pair = tuple[int, int]


@dataclass(frozen=True)
class OrbitReflectionLedger:
    center: Pair
    center_token: Pair
    reflected_endpoint: Pair
    endpoint_token: Pair
    center_transverse_numerator: int
    endpoint_transverse_numerator: int


def orbit_reflection_ledger(
    chart: BezoutTokenChart, center: Pair
) -> OrbitReflectionLedger:
    """Reflect one centre orbit point into the endpoint orbit.

    If ``P=(t,n)`` corresponds to ``(b,B)``, then the endpoint ``(B,b)``
    has token ``-P=(-t,-n)``.  Moreover

        C*n-u*t=-b,       C*(-n)-u*(-t)=b.

    Thus both token populations occupy rational strips of the same slope
    ``u/C``; the physical shell supplies their opposite transverse offsets.
    """

    token = chart.center_to_token(center)
    reflected = (center[1], center[0])
    endpoint_token = chart.endpoint_to_token(reflected)
    expected = (-token[0], -token[1])
    if endpoint_token != expected:
        raise AssertionError("orbit reflection did not negate the token")
    centre_transverse = chart.C * token[1] - chart.u * token[0]
    endpoint_transverse = (
        chart.C * endpoint_token[1] - chart.u * endpoint_token[0]
    )
    if centre_transverse != -center[0]:
        raise AssertionError("centre strip numerator is not -b")
    if endpoint_transverse != reflected[1]:
        raise AssertionError("endpoint strip numerator is not E")
    return OrbitReflectionLedger(
        center=center,
        center_token=token,
        reflected_endpoint=reflected,
        endpoint_token=endpoint_token,
        center_transverse_numerator=centre_transverse,
        endpoint_transverse_numerator=endpoint_transverse,
    )


@dataclass(frozen=True)
class ParallelOrbitDirectionLedger:
    token_direction: Pair
    physical_direction: Pair
    token_label_step: int
    first_line_invariant: int
    second_line_invariant: int
    middle_determinant_constant: int
    middle_determinant_r_step: int
    middle_determinant_s_step: int
    nonnull: bool


def parallel_orbit_direction_ledger(
    chart: BezoutTokenChart,
    token_direction: Pair,
    first_base: Pair,
    second_base: Pair,
) -> ParallelOrbitDirectionLedger:
    """Return the exact physical normal form of two parallel orbit lines.

    A token direction ``V=(v,w)`` lifts on the centre side to

        U=(p,P)=(u*v-C*w, v_bezout*v-c*w).

    Reflection swaps this into the endpoint direction.  If

        (b_r,B_r)=(b0+p*r,B0+P*r),
        (b'_s,B'_s)=(b1+p*s,B1+P*s),

    then the two middle products are ``b_r*B'_s`` and ``B_r*b'_s`` and
    their difference is

        A + J1*r - J0*s,

    where ``Ji=p*Bi-P*bi`` is the invariant of the corresponding line.
    """

    v0, v1 = token_direction
    if token_direction == (0, 0):
        raise ValueError("the token direction must be nonzero")
    p = chart.u * v0 - chart.C * v1
    other_p = chart.v * v0 - chart.c * v1
    b0, B0 = first_base
    b1, B1 = second_base
    first_invariant = p * B0 - other_p * b0
    second_invariant = p * B1 - other_p * b1
    constant = b0 * B1 - B0 * b1
    # Check the polynomial at a few signed parameters, rather than merely
    # recording a symbolic formula.
    for r, s in ((0, 0), (1, 0), (0, 1), (2, -3)):
        direct = (b0 + p * r) * (B1 + other_p * s) - (
            B0 + other_p * r
        ) * (b1 + p * s)
        closed = constant + second_invariant * r - first_invariant * s
        if direct != closed:
            raise AssertionError("parallel orbit determinant did not linearise")
    if chart.c * p - chart.C * other_p != v0:
        raise AssertionError("the physical direction lost its token-label step")
    return ParallelOrbitDirectionLedger(
        token_direction=token_direction,
        physical_direction=(p, other_p),
        token_label_step=v0,
        first_line_invariant=first_invariant,
        second_line_invariant=second_invariant,
        middle_determinant_constant=constant,
        middle_determinant_r_step=second_invariant,
        middle_determinant_s_step=-first_invariant,
        nonnull=p * other_p != 0,
    )


def completion_row_error(q: int, row: int, left: int, right: int) -> Fraction:
    """Return ``row-q^3/(8*left*right)`` exactly."""

    if min(q, row, left, right) <= 0:
        raise ValueError("completion variables must be positive")
    return Fraction(row) - Fraction(q**3, 8 * left * right)


@dataclass(frozen=True)
class RoundedRectangleLedger:
    integer_mixed_difference: int
    ideal_mixed_difference: Fraction
    error_mixed_difference: Fraction
    absolute_error_budget: Fraction
    forced_additivity: bool


def rounded_rectangle_ledger(
    q: int,
    D: int,
    rows: tuple[int, int, int, int],
    left_values: Pair,
    right_values: Pair,
) -> RoundedRectangleLedger:
    """Certify the exact four-corner reciprocal-curvature identity.

    The row order is ``(x00,x01,x10,x11)``.  Every corner is required to
    satisfy the literal hard window.  If ``f(b,d)=q^3/(8bd)``, then

        Delta_b Delta_d f
          =(q^3/8)(1/b0-1/b1)(1/d0-1/d1).

    Since each accepted integer row differs from ``f`` by its exact hard
    residual divided by ``8bd``, the same mixed-difference identity holds
    with an explicit error.  In particular, if curvature plus the sum of
    the four row-error magnitudes is less than one, the integral mixed row
    difference is forced to vanish.
    """

    if D < 0:
        raise ValueError("D must be nonnegative")
    b0, b1 = left_values
    d0, d1 = right_values
    x00, x01, x10, x11 = rows
    cells = (
        (x00, b0, d0),
        (x01, b0, d1),
        (x10, b1, d0),
        (x11, b1, d1),
    )
    for row, left, right in cells:
        if abs(8 * row * left * right - q**3) > q * D:
            raise ValueError("a rectangle corner is outside the hard window")
    errors = tuple(completion_row_error(q, *cell) for cell in cells)
    integer_mixed = x00 - x01 - x10 + x11
    ideal_mixed = Fraction(q**3, 8) * (
        Fraction(1, b0) - Fraction(1, b1)
    ) * (Fraction(1, d0) - Fraction(1, d1))
    error_mixed = errors[0] - errors[1] - errors[2] + errors[3]
    if Fraction(integer_mixed) != ideal_mixed + error_mixed:
        raise AssertionError("rounded rectangle identity failed")
    budget = sum(map(abs, errors), Fraction())
    forced = abs(ideal_mixed) + budget < 1
    if forced and integer_mixed != 0:
        raise AssertionError("subunit rounded curvature did not force additivity")
    return RoundedRectangleLedger(
        integer_mixed_difference=integer_mixed,
        ideal_mixed_difference=ideal_mixed,
        error_mixed_difference=error_mixed,
        absolute_error_budget=budget,
        forced_additivity=forced,
    )


def hard_residual(q: int, row: int, first: int, second: int) -> int:
    """Return the literal residual ``8*row*first*second-q^3``."""

    return 8 * row * first * second - q**3


@dataclass(frozen=True)
class NonreturnTwoInverseLedger:
    first_error: int
    second_error: int
    endpoint_determinant: int
    first_error_numerator: int
    second_error_numerator: int
    determinant_identity: int


def nonreturn_two_inverse_ledger(
    q: int,
    D: int,
    anchor: Pair,
    base_row: int,
    center: Pair,
    next_row: int,
    endpoint: Pair,
) -> NonreturnTwoInverseLedger:
    """Extract the short exact error pair from an arbitrary rooted path.

    This statement does *not* assume that the reflected endpoint is another
    root neighbour.  From the four hard windows one gets exactly

        r=x*d-a*c=(F_1-E_1)/(8*b),
        s=x*E-a*C=(F_2-E_2)/(8*B),
        C*r-c*s=x*(C*d-c*E).

    In particular ``|r|<=qD/(4b)`` and ``|s|<=qD/(4B)``.  The last map is
    injective on a sufficiently short error box because ``(c,C)`` is
    primitive, but this ledger deliberately makes no occupied-cell claim.
    """

    c, C = anchor
    a, x = base_row, next_row
    b, B = center
    d, E = endpoint
    triples = ((a, b, c), (a, B, C), (x, b, d), (x, B, E))
    residuals = tuple(hard_residual(q, *triple) for triple in triples)
    if any(abs(value) > q * D for value in residuals):
        raise ValueError("a proposed path triple is outside the hard window")
    first_numerator = residuals[2] - residuals[0]
    second_numerator = residuals[3] - residuals[1]
    if first_numerator % (8 * b) or second_numerator % (8 * B):
        raise AssertionError("hard-residual subtraction lost integrality")
    first_error = first_numerator // (8 * b)
    second_error = second_numerator // (8 * B)
    if first_error != x * d - a * c:
        raise AssertionError("the first two-inverse error is wrong")
    if second_error != x * E - a * C:
        raise AssertionError("the second two-inverse error is wrong")
    if 4 * b * abs(first_error) > q * D:
        raise AssertionError("the first hard-error bound failed")
    if 4 * B * abs(second_error) > q * D:
        raise AssertionError("the second hard-error bound failed")
    endpoint_determinant = C * d - c * E
    determinant_identity = C * first_error - c * second_error
    if determinant_identity != x * endpoint_determinant:
        raise AssertionError("the endpoint determinant identity failed")
    return NonreturnTwoInverseLedger(
        first_error=first_error,
        second_error=second_error,
        endpoint_determinant=endpoint_determinant,
        first_error_numerator=first_numerator,
        second_error_numerator=second_numerator,
        determinant_identity=determinant_identity,
    )


@dataclass(frozen=True)
class ReturnBilinearTransferLedger:
    transfer_residual: int
    first_transfer_numerator: int
    second_transfer_numerator: int
    first_absolute_ceiling: Fraction
    second_absolute_ceiling: Fraction
    row_error: Fraction


def return_bilinear_transfer_ledger(
    q: int,
    D: int,
    anchor: Pair,
    first_base_row: int,
    first_center: Pair,
    second_base_row: int,
    second_center: Pair,
    middle_row: int,
) -> ReturnBilinearTransferLedger:
    """Transfer a genuine return edge to a near-integral bilinear kernel.

    If both ``(b,B)`` and ``(b',B')`` are root neighbours with rows ``a``
    and ``a'``, and the middle endpoint is the reflection ``(B',b')``, then

        Z=8*c*C*a*a' - q^3*x

    has two exact residual expansions.  Each gives ``|Z|=O(q^2 D)`` and

        |x-(8*c*C/q^3)*a*a'|=O(D/q).

    This transfer is intentionally *not* asserted for a nonreturn endpoint.
    """

    c, C = anchor
    a, other_a, x = first_base_row, second_base_row, middle_row
    b, B = first_center
    other_b, other_B = second_center
    base_residuals = (
        hard_residual(q, a, b, c),
        hard_residual(q, a, B, C),
        hard_residual(q, other_a, other_b, c),
        hard_residual(q, other_a, other_B, C),
    )
    middle_residuals = (
        hard_residual(q, x, b, other_B),
        hard_residual(q, x, B, other_b),
    )
    if any(
        abs(value) > q * D for value in (*base_residuals, *middle_residuals)
    ):
        raise ValueError("a return-transfer triple is outside the hard window")
    transfer = 8 * c * C * a * other_a - q**3 * x

    def expansion(first: int, second: int, middle: int) -> int:
        # q^3*(q^3*x-8*c*C*a*a')
        opposite = (
            8 * a * other_a * c * C * middle
            - x * q**3 * (first + second)
            - x * first * second
        )
        return -opposite

    first_numerator = expansion(
        base_residuals[0], base_residuals[3], middle_residuals[0]
    )
    second_numerator = expansion(
        base_residuals[1], base_residuals[2], middle_residuals[1]
    )
    if first_numerator != q**3 * transfer:
        raise AssertionError("the first return-transfer expansion failed")
    if second_numerator != q**3 * transfer:
        raise AssertionError("the second return-transfer expansion failed")

    def ceiling(first: int, second: int, middle: int) -> Fraction:
        return (
            Fraction(x * (abs(first) + abs(second)))
            + Fraction(x * abs(first * second), q**3)
            + Fraction(8 * a * other_a * c * C * abs(middle), q**3)
        )

    first_ceiling = ceiling(
        base_residuals[0], base_residuals[3], middle_residuals[0]
    )
    second_ceiling = ceiling(
        base_residuals[1], base_residuals[2], middle_residuals[1]
    )
    if abs(transfer) > min(first_ceiling, second_ceiling):
        raise AssertionError("the return-transfer ceiling failed")
    return ReturnBilinearTransferLedger(
        transfer_residual=transfer,
        first_transfer_numerator=first_numerator,
        second_transfer_numerator=second_numerator,
        first_absolute_ceiling=first_ceiling,
        second_absolute_ceiling=second_ceiling,
        row_error=Fraction(transfer, q**3),
    )


@dataclass(frozen=True)
class VirtualEndpointBilinearLedger:
    endpoint_height_from_E: Fraction
    endpoint_height_from_d: Fraction
    height_discrepancy: Fraction
    bilinear_scale: Fraction
    predicted_row_from_E: Fraction
    predicted_row_from_d: Fraction
    first_row_error: Fraction
    second_row_error: Fraction


def virtual_endpoint_bilinear_ledger(
    q: int,
    D: int,
    anchor: Pair,
    base_row: int,
    center: Pair,
    next_row: int,
    endpoint: Pair,
) -> VirtualEndpointBilinearLedger:
    """Attach a canonical real right-row to a possibly nonreturn endpoint.

    Put ``Q=q^3/8`` and

        Y_E=Q/(cE),       Y_d=Q/(Cd),       lambda=cC/Q.

    The general two-inverse errors give the exact rank-one formulae

        x-lambda*a*Y_E=(xE-aC)/E,
        x-lambda*a*Y_d=(xd-ac)/d.

    Thus every rooted edge, including a nonreturn edge, lies within
    ``O(D/q)`` of a bilinear kernel between its actual left row ``a`` and a
    real virtual right row.  Also

        Y_E-Y_d=Q*(Cd-cE)/(c*C*d*E).

    Integrality or membership of either virtual height is *not* asserted.
    """

    c, C = anchor
    d, E = endpoint
    if min(c, C, d, E) <= 0:
        raise ValueError("anchor and endpoint coordinates must be positive")
    general = nonreturn_two_inverse_ledger(
        q, D, anchor, base_row, center, next_row, endpoint
    )
    Q = Fraction(q**3, 8)
    height_E = Q / (c * E)
    height_d = Q / (C * d)
    discrepancy = height_E - height_d
    expected_discrepancy = Q * general.endpoint_determinant / (c * C * d * E)
    if discrepancy != expected_discrepancy:
        raise AssertionError("the two virtual endpoint heights disagree incorrectly")
    scale = Fraction(c * C, 1) / Q
    predicted_E = scale * base_row * height_E
    predicted_d = scale * base_row * height_d
    error_E = Fraction(next_row) - predicted_E
    error_d = Fraction(next_row) - predicted_d
    if error_E != Fraction(general.second_error, E):
        raise AssertionError("the E-side virtual bilinear error is wrong")
    if error_d != Fraction(general.first_error, d):
        raise AssertionError("the d-side virtual bilinear error is wrong")
    return VirtualEndpointBilinearLedger(
        endpoint_height_from_E=height_E,
        endpoint_height_from_d=height_d,
        height_discrepancy=discrepancy,
        bilinear_scale=scale,
        predicted_row_from_E=predicted_E,
        predicted_row_from_d=predicted_d,
        first_row_error=error_d,
        second_row_error=error_E,
    )


@dataclass(frozen=True)
class VirtualBilinearCycleLedger:
    integer_alternating_sum: int
    ideal_alternating_sum: Fraction
    error_alternating_sum: Fraction
    absolute_error_budget: Fraction
    forced_additivity: bool


def virtual_bilinear_cycle_ledger(
    scale: Fraction,
    left_rows: tuple[int, ...],
    right_heights: tuple[Fraction, ...],
    diagonal_rows: tuple[int, ...],
    shifted_rows: tuple[int, ...],
) -> VirtualBilinearCycleLedger:
    """Audit one alternating cycle in a rounded rank-one kernel.

    At right vertex ``j`` the two cycle edges are ``(a_j,Y_j)`` and
    ``(a_{j+1},Y_j)`` (cyclic indices).  Their integer labels are supplied
    by ``diagonal_rows`` and ``shifted_rows``.  Then exactly

        sum_j (x_j-x'_j)
          =lambda*sum_j (a_j-a_{j+1})Y_j + sum_j(error_j-error'_j).

    If the ideal alternating area plus all individual rounding errors is
    subunit, the integral cycle holonomy is zero.  This is a local coherent
    cycle test, not a theorem that all cycles pass the test.
    """

    length = len(left_rows)
    if length < 2 or not (
        len(right_heights)
        == len(diagonal_rows)
        == len(shifted_rows)
        == length
    ):
        raise ValueError("all cycle arrays must have one common length at least two")
    diagonal_errors = tuple(
        Fraction(diagonal_rows[index])
        - scale * left_rows[index] * right_heights[index]
        for index in range(length)
    )
    shifted_errors = tuple(
        Fraction(shifted_rows[index])
        - scale * left_rows[(index + 1) % length] * right_heights[index]
        for index in range(length)
    )
    integer_sum = sum(
        diagonal_rows[index] - shifted_rows[index] for index in range(length)
    )
    ideal_sum = scale * sum(
        (left_rows[index] - left_rows[(index + 1) % length])
        * right_heights[index]
        for index in range(length)
    )
    error_sum = sum(diagonal_errors, Fraction()) - sum(
        shifted_errors, Fraction()
    )
    if Fraction(integer_sum) != ideal_sum + error_sum:
        raise AssertionError("the virtual bilinear cycle identity failed")
    budget = sum(map(abs, diagonal_errors), Fraction()) + sum(
        map(abs, shifted_errors), Fraction()
    )
    forced = abs(ideal_sum) + budget < 1
    if forced and integer_sum != 0:
        raise AssertionError("subunit cycle area did not force additive holonomy")
    return VirtualBilinearCycleLedger(
        integer_alternating_sum=integer_sum,
        ideal_alternating_sum=ideal_sum,
        error_alternating_sum=error_sum,
        absolute_error_budget=budget,
        forced_additivity=forced,
    )
