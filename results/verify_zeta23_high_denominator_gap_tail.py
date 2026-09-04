#!/usr/bin/env python3
"""Exact exponent audit for the Gafni--Tao prime-gap tail reduction.

This checks the rational inequalities used to deduce

    mu(797/5000) <= 63827/65000

from Gafni--Tao, Theorem 1.2, and the unconditional zero-density
upper bounds in their Table 1.  It then checks that the resulting
Voronoi-mass saving 1173/65000 clears the strip-route threshold.  The
chosen gap and rational-cutoff exponents are a simple rational pair just
inside the continuously optimized admissible boundary.

The imported analytic theorems are not reproved here.
"""

from fractions import Fraction as F


THETA = F(797, 5000)
REQUIRED_A = 1 / (1 - THETA)  # 5000/4203
TAIL_SAVING = (45 * THETA - 6) / 65
MU_BOUND = 1 - TAIL_SAVING
STRIP_THRESHOLD = F(180303234, 10_000_000_000)
APERTURE_EXPONENT = F(50, 33)
RATIONAL_CUTOFF_EXPONENT = F(1537, 10000)
LENGTH_SAVING = 1 - APERTURE_EXPONENT / 2 - RATIONAL_CUTOFF_EXPONENT
SMALL_BOUNDARY_SAVING = (
    2
    - APERTURE_EXPONENT
    - 2 * RATIONAL_CUTOFF_EXPONENT
    - THETA
)
CONTINUOUS_THETA_FLOOR = (65 * STRIP_THRESHOLD + 6) / 45
CONTINUOUS_BETA_CEILING = (
    2 - APERTURE_EXPONENT - CONTINUOUS_THETA_FLOOR - STRIP_THRESHOLD
) / 2
CONTINUOUS_CORRIDOR_INFIMUM = (
    CONTINUOUS_THETA_FLOOR - CONTINUOUS_BETA_CEILING
)
LOCAL_ENVELOPE_LEFT = F(2, 15)
LOCAL_ENVELOPE_RIGHT = F(353, 1445)


# Each entry is (name, sigma_left, sigma_right, numerator, slope, intercept)
# for the Table-1 upper bound U(sigma)=numerator/(slope*sigma+intercept).
# Only the entries that can meet U >= 5000/4203 are needed for the
# minimization.
ACTIVE_PIECES = [
    ("Ingham", F(1, 2), F(7, 10), F(3), F(-1), F(2)),
    ("Guth--Maynard", F(7, 10), F(19, 25), F(15), F(5), F(3)),
    ("Ivic-1", F(19, 25), F(127, 167), F(9), F(8), F(-2)),
    ("Ivic-2", F(127, 167), F(13, 17), F(15), F(13), F(-3)),
    ("Ivic-3", F(13, 17), F(17, 22), F(6), F(5), F(-1)),
    ("TTY-1", F(17, 22), F(41, 53), F(2), F(9), F(-6)),
    ("Ivic-4", F(41, 53), F(7, 9), F(9), F(7), F(-1)),
    ("TTY-2", F(7, 9), F(1867, 2347), F(9), F(16), F(-8)),
    ("Bourgain", F(1867, 2347), F(4, 5), F(3), F(2), F(0)),
    ("Ivic-5", F(4, 5), F(7, 8), F(3), F(2), F(0)),
    ("Heath--Brown", F(7, 8), F(279, 314), F(3), F(10), F(-7)),
    ("CDV", F(279, 314), F(155, 174), F(24), F(30), F(-11)),
    ("Ivic-6", F(155, 174), F(9, 10), F(24), F(30), F(-11)),
    ("TTY-3", F(9, 10), F(31, 34), F(3), F(10), F(-7)),
    ("TTY-4", F(31, 34), F(14, 15), F(11), F(48), F(-36)),
    ("TTY-5", F(14, 15), F(2841, 3016), F(391), F(2493), F(-2014)),
]


# Later Table-1 pieces start below the required A-thresholds audited here
# and decrease on their intervals.
INACTIVE_PIECES = [
    ("TTY-6", F(2841, 3016), F(859, 908), F(22232), F(163248), F(-134765)),
    ("TTY-7", F(859, 908), F(23, 24), F(356), F(2742), F(-2279)),
    ("Pintz-1", F(23, 24), F(2211487, 2274732), F(3), F(24), F(-20)),
    ("TTY-8", F(2211487, 2274732), F(39, 40), F(86152), F(1447460), F(-1311509)),
    ("Pintz-2", F(39, 40), F(41, 42), F(2), F(15), F(-12)),
    ("Pintz-3", F(41, 42), F(59, 60), F(3), F(40), F(-35)),
]


def upper(piece: tuple, sigma: F) -> F:
    _, _, _, numerator, slope, intercept = piece
    denominator = slope * sigma + intercept
    assert denominator > 0
    return numerator / denominator


def saving_from_upper(piece: tuple, sigma: F, theta: F) -> F:
    """1-mu_2 after replacing A(sigma) by its upper bound U(sigma)."""
    return (1 - sigma) * (2 - (1 - theta) * upper(piece, sigma))


def active_right_endpoint(piece: tuple, required_a: F) -> F | None:
    """Clip a Table interval to the condition U(sigma) >= REQUIRED_A."""
    _, left, right, numerator, slope, intercept = piece
    if slope < 0:
        # U is increasing.  This is the first (Ingham) piece, on which the
        # condition already holds at the left endpoint.
        return right if upper(piece, left) >= required_a else None
    cutoff = (numerator / required_a - intercept) / slope
    right = min(right, cutoff)
    if right < left:
        return None
    return right


def audit_theta(theta: F, target_saving: F) -> tuple:
    """Audit the full Table-1 envelope at one exact rational theta."""
    required_a = 1 / (1 - theta)
    # For sigma<=1/2 one has A(sigma)=1/(1-sigma) exactly.  On the active
    # portion sigma>=theta, the corresponding saving is
    # 1-(2*sigma-theta), whose minimum is theta at sigma=1/2.
    assert theta >= target_saving
    # For U=A/(B*sigma+C), the inequality
    # (1-sigma)(2-(1-theta)U) >= target_saving becomes a quadratic
    # N(sigma)>=0 after multiplication by the positive denominator.  Check
    # its endpoints and, in the convex case, its exact rational vertex.
    certificates = []
    for piece in ACTIVE_PIECES:
        name, left, _, numerator, slope, intercept = piece
        right = active_right_endpoint(piece, required_a)
        if right is None:
            continue
        assert upper(piece, left) >= required_a or left == F(1, 2)
        k = 1 - theta
        # N(s)=a*s^2+b*s+c.
        a = -2 * slope
        b = 2 * slope - 2 * intercept + k * numerator - target_saving * slope
        c = 2 * intercept - k * numerator - target_saving * intercept
        points = [left, right]
        if a > 0:
            vertex = -b / (2 * a)
            if left <= vertex <= right:
                points.append(vertex)
        for point in points:
            denominator = slope * point + intercept
            assert denominator > 0
            polynomial = a * point * point + b * point + c
            assert polynomial >= 0, (name, point, polynomial)
            saving = saving_from_upper(piece, point, theta)
            assert saving >= target_saving, (name, point, saving)
            certificates.append((saving, name, point))

    minimum = min(certificates)
    assert minimum == (target_saving, "Guth--Maynard", F(7, 10)) or (
        minimum[0] == target_saving and minimum[2] == F(7, 10)
    )

    # Once the TTY-5 bound crosses REQUIRED_A, every later displayed piece is
    # already below REQUIRED_A at its left endpoint and decreases thereafter.
    for piece in INACTIVE_PIECES:
        name, left, _, _, slope, _ = piece
        assert slope > 0
        assert upper(piece, left) < required_a, (name, upper(piece, left))

    # Pintz's n>=6 final family starts at 3/(n-1), hence is also inactive.
    for n in range(6, 100):
        assert F(3, n - 1) < required_a
    return minimum


def main() -> None:
    audit_theta(THETA, TAIL_SAVING)
    # Endpoint checks for the denominator window discussed in the literature
    # audit.  Between them each fixed Table-1 branch is affine in theta; the
    # only moving boundary is Abar(sigma)=1/(1-theta), whose rational crossing
    # is included in the branch comparison yielding LOCAL_ENVELOPE_RIGHT.
    audit_theta(F(3, 20), F(3, 260))
    audit_theta(F(4, 25), F(6, 325))
    # Certify that the same local envelope remains binding all the way down
    # to the continuous strip-threshold boundary used in the optimization.
    audit_theta(CONTINUOUS_THETA_FLOOR, STRIP_THRESHOLD)

    assert MU_BOUND == F(63827, 65000)
    assert TAIL_SAVING == F(1173, 65000)
    assert LENGTH_SAVING == F(29279, 330000)
    assert SMALL_BOUNDARY_SAVING == F(1489, 82500)
    assert CONTINUOUS_THETA_FLOOR == F(796885669, 5_000_000_000)
    assert CONTINUOUS_BETA_CEILING == F(25363884781, 165_000_000_000)
    assert CONTINUOUS_CORRIDOR_INFIMUM == F(116667787, 20_625_000_000)
    assert LOCAL_ENVELOPE_LEFT < CONTINUOUS_THETA_FLOOR < THETA
    assert THETA < LOCAL_ENVELOPE_RIGHT
    assert THETA > CONTINUOUS_THETA_FLOOR
    assert RATIONAL_CUTOFF_EXPONENT < CONTINUOUS_BETA_CEILING
    assert TAIL_SAVING > STRIP_THRESHOLD
    assert LENGTH_SAVING > STRIP_THRESHOLD
    assert SMALL_BOUNDARY_SAVING > STRIP_THRESHOLD

    print("PASS")
    print(f"theta={THETA} required_A={REQUIRED_A}")
    print(f"mu_bound={MU_BOUND}={float(MU_BOUND):.12f}")
    print(f"tail_saving={TAIL_SAVING}={float(TAIL_SAVING):.12f}")
    print(
        f"continuous_boundary: theta>{CONTINUOUS_THETA_FLOOR}="
        f"{float(CONTINUOUS_THETA_FLOOR):.12f}; beta<"
        f"{CONTINUOUS_BETA_CEILING}="
        f"{float(CONTINUOUS_BETA_CEILING):.12f}; corridor_infimum="
        f"{CONTINUOUS_CORRIDOR_INFIMUM}="
        f"{float(CONTINUOUS_CORRIDOR_INFIMUM):.12f}"
    )
    print(
        f"rational_cutoff={RATIONAL_CUTOFF_EXPONENT}; "
        f"length_saving={LENGTH_SAVING}={float(LENGTH_SAVING):.12f}; "
        f"small_boundary_saving={SMALL_BOUNDARY_SAVING}="
        f"{float(SMALL_BOUNDARY_SAVING):.12f}"
    )
    print(
        "margin_over_strip_threshold="
        f"{TAIL_SAVING - STRIP_THRESHOLD}="
        f"{float(TAIL_SAVING - STRIP_THRESHOLD):.12f}"
    )


if __name__ == "__main__":
    main()
