"""Exact exponent ledger for the retuned prime-hat transition and CA4 gate.

This module proves no prime-cancellation estimate.  It records the exact
arithmetic in the deterministic adapters surrounding the open centered
fourth-moment statement CA4(163/1000, 1/10).
"""

from __future__ import annotations

from fractions import Fraction


GT_MIN = Fraction(2, 15)
GT_MAX = Fraction(353, 1445)
APERTURE = Fraction(50, 33)
TARGET = Fraction(19, 1000)

TRANSITION_THETA = Fraction(201, 1250)
TRANSITION_TIME = 1 - TRANSITION_THETA

CA4_THETA = Fraction(163, 1000)
CA4_LOSS = Fraction(1, 10)


def gt_tail_saving(theta: Fraction) -> Fraction:
    """Power saving in the Gafni--Tao local linear envelope."""

    if not GT_MIN <= theta <= GT_MAX:
        raise ValueError("theta lies outside the audited Gafni--Tao branch")
    return (45 * theta - 6) / 65


def truncated_third_moment_saving(theta: Fraction) -> Fraction:
    """Saving in sum Delta^3 before the two t derivatives."""

    return 2 - 2 * theta + gt_tail_saving(theta)


def peano_saving(theta: Fraction, time_exponent: Fraction) -> Fraction:
    """Saving after paying t^2 in the trapezoid Peano remainder."""

    return truncated_third_moment_saving(theta) - 2 * time_exponent


def retained_l2_saving(theta: Fraction) -> Fraction:
    """q for sum(lambda_p^2) << Y^(-q+o(1)) after edge truncation."""

    # Dyadic Gafni--Tao tails give
    # sum_{g<=Y^theta} g^2 << Y^[1+(20 theta+6)/65+o(1)].
    return (59 - 20 * theta) / 65


def ca4_pointwise_saving(
    theta: Fraction,
    loss: Fraction,
    aperture: Fraction = APERTURE,
) -> Fraction:
    """Uniform exponent obtained from a translated-window fourth moment.

    The input is

        int_T^(2T) |R(t)|^4 dt
            << T Y^(-2q + loss + o(1)).

    Lipschitz persistence of a bad value contributes its fifth power.
    """

    return (2 * retained_l2_saving(theta) - aperture - loss) / 5


TRANSITION_SAVING = gt_tail_saving(TRANSITION_THETA)
CA4_TAIL_SAVING = gt_tail_saving(CA4_THETA)
CA4_L2_SAVING = retained_l2_saving(CA4_THETA)
CA4_OUTPUT_SAVING = ca4_pointwise_saving(CA4_THETA, CA4_LOSS)


def ledger_closes_target() -> bool:
    """Whether every power-sensitive adapter has strict target slack."""

    return (
        TRANSITION_SAVING > TARGET
        and peano_saving(TRANSITION_THETA, TRANSITION_TIME) > TARGET
        and CA4_TAIL_SAVING > TARGET
        and CA4_OUTPUT_SAVING > TARGET
    )


def summary() -> dict[str, str | bool]:
    """Machine-readable exact ledger."""

    return {
        "transition_theta": str(TRANSITION_THETA),
        "transition_time": str(TRANSITION_TIME),
        "transition_saving": str(TRANSITION_SAVING),
        "ca4_theta": str(CA4_THETA),
        "ca4_loss": str(CA4_LOSS),
        "ca4_tail_saving": str(CA4_TAIL_SAVING),
        "ca4_l2_saving": str(CA4_L2_SAVING),
        "ca4_output_saving": str(CA4_OUTPUT_SAVING),
        "target": str(TARGET),
        "closes_target_conditionally": ledger_closes_target(),
        "ca4_status": "OPEN",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(summary(), indent=2, sort_keys=True))
