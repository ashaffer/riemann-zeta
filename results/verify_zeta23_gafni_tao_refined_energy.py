#!/usr/bin/env python3
"""Exact audit of the refined Gafni--Tao exceptional-set envelope.

The published refined theorem replaces the second-moment expression by

    min(mu_2(theta, sigma), mu_4(theta, sigma)).

This script certifies that this does not improve the Table-1 general envelope
on the branch relevant to the high-denominator gap truncation.  The reason is
an exact witness at sigma=7/10: the published A* bound makes mu_4 strictly
larger than mu_2 there, while the all-piece Table-1 audit shows that mu_2 at
this point is the general-envelope maximum.

The imported zero-density and additive-energy theorems are not reproved.
"""

from fractions import Fraction as F

import verify_zeta23_high_denominator_gap_tail as general


SIGMA = F(7, 10)
A_BOUND = F(30, 13)
ASTAR_BOUND = F(235, 39)

THETA_LEFT = F(3, 20)
THETA_RIGHT = F(353, 1445)
THETA_TARGET = F(797, 5000)

KAPPA = F(180303234, 10_000_000_000)
APERTURE = F(50, 33)
BETA = F(1537, 10000)


def tail_saving(theta: F) -> F:
    return (45 * theta - 6) / 65


def mu2_witness(theta: F) -> F:
    return (1 - theta) * (1 - SIGMA) * A_BOUND + 2 * SIGMA - 1


def mu4_witness(theta: F) -> F:
    return (1 - theta) * (1 - SIGMA) * ASTAR_BOUND + 4 * SIGMA - 3


def audit_theta(theta: F) -> None:
    saving = tail_saving(theta)

    # This independently invokes the exact rational scan of every active
    # published Table-1 branch.  It identifies sigma=7/10 as the maximizer of
    # mu_2, equivalently the minimizer of 1-mu_2.
    minimum = general.audit_theta(theta, saving)
    assert minimum[0] == saving
    assert minimum[2] == SIGMA

    # The witness is in the upper-envelope active set.
    assert A_BOUND >= 1 / (1 - theta)

    # Exact published-envelope identities at sigma=7/10.
    assert mu2_witness(theta) == 1 - saving
    assert mu4_witness(theta) >= mu2_witness(theta)

    # Hence the refined computed envelope is at least this witness, while
    # min(mu_2,mu_4)<=mu_2 makes it at most the general computed envelope.
    # Together these two inequalities prove equality of the envelopes.


def audit_general_branch_continuum() -> None:
    """Certify the general-envelope formula on the full theta interval.

    For fixed sigma the saving minus ``tail_saving(theta)`` is affine in
    theta.  A Table-1 point is active for theta up to

        theta_max(sigma) = 1 - 1/U(sigma).

    Endpoint audits therefore suffice for pieces active throughout.  If a
    point leaves the active set inside the theta interval, also check the
    moving boundary theta=theta_max.  On that boundary the difference is the
    affine function checked below.
    """

    audit_theta(THETA_LEFT)
    audit_theta(THETA_RIGHT)

    for piece in general.ACTIVE_PIECES:
        _, left, right, numerator, slope, intercept = piece
        if slope <= 0:
            # The Ingham piece is active throughout this theta interval.
            continue

        active_at_left = (numerator * (1 - THETA_LEFT) - intercept) / slope
        active_at_right = (numerator * (1 - THETA_RIGHT) - intercept) / slope
        moving_left = max(left, active_at_right)
        moving_right = min(right, active_at_left)
        if moving_left > moving_right:
            continue

        def boundary_difference(sigma: F) -> F:
            # At U(sigma)=1/(1-theta), the mu_2 saving is 1-sigma.
            # Subtract s(theta_max), with
            # theta_max=1-(slope*sigma+intercept)/numerator.
            return (
                F(2, 5)
                - sigma
                + F(9, 13) * (slope * sigma + intercept) / numerator
            )

        # This is affine in sigma.
        assert boundary_difference(moving_left) >= 0
        assert boundary_difference(moving_right) >= 0


def main() -> None:
    # The difference is decreasing in theta, so positivity at the right end
    # certifies the whole interval used here.
    assert mu4_witness(THETA_RIGHT) - mu2_witness(THETA_RIGHT) > 0
    assert (
        mu4_witness(THETA_TARGET) - mu2_witness(THETA_TARGET)
        == F(43887, 130000)
    )

    audit_general_branch_continuum()

    for theta in (
        THETA_TARGET,
        F(4, 25),
        F(17, 100),
    ):
        audit_theta(theta)

    # A* would have to cross this value at the binding point before the
    # fourth-moment term could beat the second-moment term there.
    astar_critical = A_BOUND + 2 / (1 - THETA_TARGET)
    assert astar_critical == F(256090, 54639)
    assert ASTAR_BOUND - astar_critical == F(73145, 54639)

    # Propagation to the optimized half-cell constraints is therefore
    # unchanged from the general-envelope calculation.
    theta_floor = (65 * KAPPA + 6) / 45
    beta_ceiling = (2 - APERTURE - theta_floor - KAPPA) / 2
    assert theta_floor == F(796885669, 5_000_000_000)
    assert beta_ceiling == F(25363884781, 165_000_000_000)

    target_tail = tail_saving(THETA_TARGET)
    main_saving = 1 - APERTURE / 2 - BETA
    collar_saving = 2 - APERTURE - 2 * BETA - THETA_TARGET
    assert target_tail == F(1173, 65000)
    assert main_saving == F(29279, 330000)
    assert collar_saving == F(1489, 82500)
    assert min(target_tail, main_saving, collar_saving) > KAPPA

    print("PASS")
    print(
        "refined_envelope_equals_general_on_certified_branch: "
        f"{THETA_LEFT} <= theta <= {THETA_RIGHT}"
    )
    print(
        f"target_theta={THETA_TARGET}; mu2={mu2_witness(THETA_TARGET)}; "
        f"mu4={mu4_witness(THETA_TARGET)}; "
        f"mu4_minus_mu2={mu4_witness(THETA_TARGET)-mu2_witness(THETA_TARGET)}"
    )
    print(
        f"published_Astar={ASTAR_BOUND}; Astar_needed_below={astar_critical}; "
        f"gap={ASTAR_BOUND-astar_critical}"
    )
    print(
        f"theta_floor={theta_floor}={float(theta_floor):.12f}; "
        f"beta_ceiling={beta_ceiling}={float(beta_ceiling):.12f}"
    )


if __name__ == "__main__":
    main()
