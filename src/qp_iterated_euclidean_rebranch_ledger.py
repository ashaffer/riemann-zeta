"""Exact ledgers for primitive-vector Euclidean rebranching.

The defect lattice in one completion chart is

    Lambda(Q, w) = {(k, a): a = w*k - Q*n for some integer n}.

A primitive lattice direction is encoded by coprime lattice coordinates
``(p, m)`` and has ambient displacement ``(p, r)``, where
``r = w*p - Q*m``.  The analytic bounds themselves are proved in the
companion report; this module records the exact coordinate identities and
the resulting power polytopes at ``q = D**(33/16)``.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


Q_POWER_IN_D = Fraction(33, 16)
TARGET_POWER_IN_D = Fraction(7, 8)
SELBERG_FLOOR_IN_D = Fraction(1, 8)


@dataclass(frozen=True)
class BetaAffinePiece:
    """One current ANTEDB bound ``beta(alpha) <= intercept+slope*alpha``."""

    intercept: Fraction
    slope: Fraction
    alpha_lower: Fraction
    alpha_upper: Fraction


# Table 4.3 in the current ANTEDB beta chapter.  The piece domains meet at
# the listed rational endpoints; their displayed upper bounds can jump.
# Keeping the full table here makes the
# bounded-partial-quotient obstruction independently reproducible.
ANTEDB_BETA_PIECES = (
    BetaAffinePiece(Fraction(13, 414), Fraction(346, 414), Fraction(0), Fraction(2848, 12173)),
    BetaAffinePiece(Fraction(13, 318), Fraction(253, 318), Fraction(2848, 12173), Fraction(161, 646)),
    BetaAffinePiece(Fraction(11, 492), Fraction(107, 123), Fraction(161, 646), Fraction(19, 74)),
    BetaAffinePiece(Fraction(89, 2706), Fraction(2243, 2706), Fraction(19, 74), Fraction(199, 716)),
    BetaAffinePiece(Fraction(29, 600), Fraction(58, 75), Fraction(199, 716), Fraction(967, 3428)),
    BetaAffinePiece(Fraction(49, 1614), Fraction(1351, 1614), Fraction(967, 3428), Fraction(120, 419)),
    BetaAffinePiece(Fraction(1, 66), Fraction(235, 264), Fraction(120, 419), Fraction(1328, 4447)),
    BetaAffinePiece(Fraction(13, 194), Fraction(139, 194), Fraction(1328, 4447), Fraction(104, 343)),
    BetaAffinePiece(Fraction(13, 146), Fraction(47, 73), Fraction(104, 343), Fraction(87, 275)),
    BetaAffinePiece(Fraction(11, 244), Fraction(191, 244), Fraction(87, 275), Fraction(423, 1295)),
    BetaAffinePiece(Fraction(89, 1282), Fraction(454, 641), Fraction(423, 1295), Fraction(227, 601)),
    BetaAffinePiece(Fraction(29, 280), Fraction(173, 280), Fraction(227, 601), Fraction(12, 31)),
    BetaAffinePiece(Fraction(1, 32), Fraction(103, 128), Fraction(12, 31), Fraction(1508, 3825)),
    BetaAffinePiece(Fraction(18, 199), Fraction(521, 796), Fraction(1508, 3825), Fraction(62831, 155153)),
    BetaAffinePiece(Fraction(569, 2800), Fraction(1053, 2800), Fraction(62831, 155153), Fraction(143, 349)),
    BetaAffinePiece(Fraction(491, 5530), Fraction(1812, 2765), Fraction(143, 349), Fraction(263, 638)),
    BetaAffinePiece(Fraction(113, 1345), Fraction(897, 1345), Fraction(263, 638), Fraction(1673, 4038)),
    BetaAffinePiece(Fraction(2, 9), Fraction(1, 3), Fraction(1673, 4038), Fraction(5, 12)),
    BetaAffinePiece(Fraction(1, 12), Fraction(2, 3), Fraction(5, 12), Fraction(3, 7)),
    BetaAffinePiece(Fraction(13, 84), Fraction(1, 2), Fraction(3, 7), Fraction(1, 2)),
)


def antedb_beta_affine_piece(alpha: Fraction) -> BetaAffinePiece:
    """Return a right-continuous combined-table piece containing ``alpha``.

    Use :func:`antedb_beta_bound` when the best value at a shared endpoint is
    required.
    """

    alpha = Fraction(alpha)
    if not 0 <= alpha <= Fraction(1, 2):
        raise ValueError("the recorded table covers 0 <= alpha <= 1/2")
    for index, piece in enumerate(ANTEDB_BETA_PIECES):
        right_closed = index == len(ANTEDB_BETA_PIECES) - 1
        if piece.alpha_lower <= alpha and (
            alpha < piece.alpha_upper
            or (right_closed and alpha == piece.alpha_upper)
        ):
            return piece
    raise AssertionError("the ANTEDB beta pieces have a gap")


def antedb_beta_bound(alpha: Fraction) -> Fraction:
    """Evaluate the best recorded piecewise-affine bound for ``beta(alpha)``.

    Adjacent table intervals are both closed in the source theorem.  At their
    first common endpoint the displayed bounds have a small jump, so taking
    the minimum of all incident pieces is necessary.
    """

    alpha = Fraction(alpha)
    if not 0 <= alpha <= Fraction(1, 2):
        raise ValueError("the recorded table covers 0 <= alpha <= 1/2")
    candidates = [alpha]  # The universal trivial bound beta(alpha) <= alpha.
    candidates.extend(
        piece.intercept + piece.slope * alpha
        for piece in ANTEDB_BETA_PIECES
        if piece.alpha_lower <= alpha <= piece.alpha_upper
    )
    return min(candidates)


def antedb_local_beta_top_power(
    fibre_power: Fraction, remainder_power: Fraction
) -> Fraction:
    """Top Selberg-block power from the full current beta table.

    This uses ``K=D^(1/8)``, so ``T=Kq=D^(35/16)`` and
    ``alpha=(33/16-v)/(35/16)``.  It applies when that alpha lies in
    ``[0,1/2]``.  Lower blocks must also be checked at the finitely many
    table breakpoints because adjacent displayed upper bounds can jump.
    """

    b = Fraction(fibre_power)
    v = Fraction(remainder_power)
    phase_power = Q_POWER_IN_D + SELBERG_FLOOR_IN_D
    alpha = (Q_POWER_IN_D - v) / phase_power
    return b + phase_power * antedb_beta_bound(alpha)


@dataclass(frozen=True)
class PrimitiveRebranchVector:
    """A primitive direction in ``Lambda(Q,w)``.

    Primitivity is in lattice coordinates: it is ``gcd(p,m)=1``.  It need
    not be the same as ``gcd(p,r)=1``.
    """

    host: int
    step: int
    p: int
    m: int
    remainder: int


def primitive_rebranch_vector(
    host: int, step: int, p: int, m: int
) -> PrimitiveRebranchVector:
    """Construct the direction ``(p, step*p-host*m)``.

    The map ``(k,n) -> (k,step*k-host*n)`` is an isomorphism from
    ``Z^2`` onto the defect lattice, so ``gcd(p,m)=1`` is exactly the
    saturation condition for this direction.
    """

    if not 1 <= step < host or gcd(host, step) != 1:
        raise ValueError("host and step must be coprime positive integers")
    if gcd(abs(p), abs(m)) != 1:
        raise ValueError("(p,m) must be a primitive direction")
    remainder = step * p - host * m
    return PrimitiveRebranchVector(host, step, p, m, remainder)


def rebranch_fibre_label(
    vector: PrimitiveRebranchVector, defect: int, completion: int
) -> int:
    """Return the exact coset label, constant along the primitive vector.

    For a lattice point ``completion = step*defect-host*n``, the label is

        ell = m*defect-p*n = (-r*defect+p*completion)/host.
    """

    numerator = (
        -vector.remainder * defect + vector.p * completion
    )
    if numerator % vector.host:
        raise ValueError("the supplied point is not in the defect lattice")
    return numerator // vector.host


def advance_on_rebranch_fibre(
    vector: PrimitiveRebranchVector,
    defect: int,
    completion: int,
    amount: int,
) -> tuple[int, int]:
    """Move by an integral number of primitive steps on one fibre."""

    new_defect = defect + amount * vector.p
    new_completion = completion + amount * vector.remainder
    if rebranch_fibre_label(vector, new_defect, new_completion) != (
        rebranch_fibre_label(vector, defect, completion)
    ):
        raise AssertionError("the primitive move changed its fibre label")
    return new_defect, new_completion


def saturated_fibre_power(
    p_power: Fraction, remainder_power: Fraction
) -> Fraction:
    """Power of ``B <= min(D,1+p+|r|D/q)``.

    Here ``p=D^u``, ``|r|=D^v``, and ``q=D^(33/16)``.  Saturation at
    ``D`` is essential for very long primitive directions, although it is
    inactive inside each of the closed polytopes below.
    """

    p_power = Fraction(p_power)
    remainder_power = Fraction(remainder_power)
    return min(
        Fraction(1),
        max(
            Fraction(0),
            p_power,
            remainder_power + 1 - Q_POWER_IN_D,
        ),
    )


def full_rectangle_fibre_capacity_power(
    p_power: Fraction, remainder_power: Fraction
) -> Fraction:
    """Largest power of the number of points on one nonempty fibre.

    A fibre has

    ``O(1 + min(D/|p|, q/|r|))``

    points in a full shell rectangle.  The outer ``max(0,...)`` records the
    indispensable singleton term when either quotient is below one.
    """

    u = Fraction(p_power)
    v = Fraction(remainder_power)
    return max(
        Fraction(0),
        min(Fraction(1), Fraction(1) - u, Q_POWER_IN_D - v),
    )


def full_rectangle_fibre_lower_count_power(
    p_power: Fraction, remainder_power: Fraction
) -> Fraction:
    """Power forced for the number of fibres containing ``D^(1+o(1))`` points."""

    return Fraction(1) - full_rectangle_fibre_capacity_power(
        p_power, remainder_power
    )


def bounded_type_envelope_fibre_power(
    natural_length_power: Fraction,
) -> Fraction:
    """Least fibre-count power on a bounded-type approximation envelope.

    If ``h=log_D(q/|r|)`` and bad approximability gives ``h<=u``, the full
    rectangle fibre count is minimized at ``u=h`` and has this power.
    """

    h = Fraction(natural_length_power)
    if h < 0:
        raise ValueError("the natural fibre length must not be a negative power")
    return min(Fraction(1), max(h, Fraction(1) - h))


def primitive_second_degree_interval(
    fibre_power: Fraction, remainder_power: Fraction
) -> tuple[Fraction, Fraction]:
    """Admissible ``K=D^k`` interval for the second derivative bound."""

    b = Fraction(fibre_power)
    v = Fraction(remainder_power)
    lower = max(
        SELBERG_FLOOR_IN_D,
        2 * b + Q_POWER_IN_D - 2 * v - Fraction(7, 4),
    )
    upper = min(
        Q_POWER_IN_D - 1,
        Q_POWER_IN_D - 2 * v - Fraction(1, 4),
    )
    return lower, upper


def primitive_third_degree_interval(
    fibre_power: Fraction, remainder_power: Fraction
) -> tuple[Fraction, Fraction]:
    """Admissible ``K=D^k`` interval for the third derivative bound."""

    b = Fraction(fibre_power)
    v = Fraction(remainder_power)
    lower = max(
        SELBERG_FLOOR_IN_D,
        3 * b + 2 * Q_POWER_IN_D - 3 * v - Fraction(9, 4),
    )
    upper = min(
        Q_POWER_IN_D - 1,
        2 * Q_POWER_IN_D - 3 * v - Fraction(3, 4),
    )
    return lower, upper


def in_primitive_second_polytope(
    p_power: Fraction, remainder_power: Fraction
) -> bool:
    """Whether the exact second-derivative sufficient conditions hold."""

    v = Fraction(remainder_power)
    b = saturated_fibre_power(p_power, v)
    return (
        v <= Fraction(27, 32)
        and b <= Fraction(3, 4)
        and b - v <= Fraction(3, 8)
    )


def in_primitive_third_polytope(
    p_power: Fraction, remainder_power: Fraction
) -> bool:
    """Whether the exact third-derivative sufficient conditions hold."""

    v = Fraction(remainder_power)
    b = saturated_fibre_power(p_power, v)
    return (
        v <= Fraction(13, 12)
        and b <= Fraction(1, 2)
        and v - b >= Fraction(13, 48)
    )


def bourgain_two_line_beta_budget(remainder_power: Fraction) -> Fraction:
    """Largest fibre power allowed by the two adjacent Bourgain lines.

    The formula applies for ``33/32 <= v <= 221/192``.  It comes from
    ``K=D^(1/8)`` and, respectively,

        beta(alpha) <= 13/84 + alpha/2,
        beta(alpha) <= 1/12 + 2*alpha/3.
    """

    v = Fraction(remainder_power)
    if not Fraction(33, 32) <= v <= Fraction(221, 192):
        raise ValueError("remainder power is outside the two-line range")
    if v <= Fraction(9, 8):
        return v / 2 - Fraction(665, 1344)
    return 2 * v / 3 - Fraction(131, 192)


def in_bourgain_two_line_beta_polytope(
    p_power: Fraction, remainder_power: Fraction
) -> bool:
    """Whether the verified two-line local-beta sector closes."""

    v = Fraction(remainder_power)
    if not Fraction(33, 32) <= v <= Fraction(221, 192):
        return False
    b = saturated_fibre_power(p_power, v)
    return b <= bourgain_two_line_beta_budget(v)


def primitive_rebranch_polytope_ledger() -> dict[str, Fraction]:
    """Return all exact vertices and margins used in the audit."""

    return {
        "q_power": Q_POWER_IN_D,
        "target": TARGET_POWER_IN_D,
        "selberg_floor": SELBERG_FLOOR_IN_D,
        "second_remainder_ceiling": Fraction(27, 32),
        "second_fibre_ceiling": Fraction(3, 4),
        "second_fibre_minus_remainder_ceiling": Fraction(3, 8),
        "third_remainder_ceiling": Fraction(13, 12),
        "third_fibre_ceiling": Fraction(1, 2),
        "third_remainder_minus_fibre_floor": Fraction(13, 48),
        "beta_remainder_floor": Fraction(33, 32),
        "beta_line_crossing": Fraction(9, 8),
        "beta_remainder_ceiling": Fraction(221, 192),
        "beta_budget_at_floor": Fraction(1, 48),
        "beta_budget_at_crossing": Fraction(13, 192),
        "beta_budget_at_ceiling": Fraction(49, 576),
        "badly_approximable_second_p_floor": Fraction(39, 32),
        "badly_approximable_third_p_floor": Fraction(47, 48),
        "badly_approximable_beta_p_floor": Fraction(175, 192),
        "badly_approximable_current_beta_best": Fraction(6535, 6624),
        "badly_approximable_current_beta_loss": Fraction(739, 6624),
    }
