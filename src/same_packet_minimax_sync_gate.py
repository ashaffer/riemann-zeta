#!/usr/bin/env python3
"""Finite algebra for the QP/GP/GA same-packet synchronization gate.

The analytic state space is most naturally lifted to compact
autocorrelations.  On that convex space all completed-form evaluations are
affine.  This module records the resulting minimax criterion, the exact
two-witness interpolation test, and two small counterfixtures showing why
separate existential witnesses do not synchronize.

Nothing in this module asserts QP-PROMOTE or an arithmetic zeta estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence

import numpy as np


# Candidate-strip ledger, in exact conservative rational normalization.
ALPHA_0 = Fraction(49, 100)
D = Fraction(33, 50)
RAW_CARRIER_X_EXPONENT = ALPHA_0 * D
GREEN_BASE_X_EXPONENT = Fraction(298_008_745, 1_000_000_000)
GP_SURCHARGE = RAW_CARRIER_X_EXPONENT - GREEN_BASE_X_EXPONENT
KAPPA_PROMOTE = Fraction(180_303_234, 10_000_000_000)
QP_PROMOTE_X_BILL = D * KAPPA_PROMOTE
GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER = GP_SURCHARGE - QP_PROMOTE_X_BILL
ZF_DELTA = Fraction(1, 100)


def joint_budget_margin(
    gp_correction_x_exponent: Fraction,
    qp_loss_y_exponent: Fraction,
    *,
    surcharge: Fraction = GP_SURCHARGE,
    d: Fraction = D,
) -> Fraction:
    """Final X-exponent after jointly charging GP correction and QP loss."""

    return surcharge - gp_correction_x_exponent - d * qp_loss_y_exponent


def joint_budget_closes(
    gp_correction_x_exponent: Fraction,
    qp_loss_y_exponent: Fraction,
    *,
    fixed_margin: Fraction = Fraction(0),
) -> bool:
    """Whether the carrier retains a strict requested fixed X-margin."""

    if fixed_margin < 0:
        raise ValueError("fixed_margin must be nonnegative")
    return joint_budget_margin(
        gp_correction_x_exponent, qp_loss_y_exponent
    ) > fixed_margin


@dataclass(frozen=True)
class TwoWitnessSlacks:
    """Cross-evaluation of a GP witness and a GA witness.

    The GP witness has slack vector ``(gp_own, -ga_deficit_at_gp)``.
    The GA witness has slack vector ``(-gp_deficit_at_ga, ga_own)``.
    All four entries are nonnegative.
    """

    gp_own: Fraction
    ga_deficit_at_gp: Fraction
    gp_deficit_at_ga: Fraction
    ga_own: Fraction

    def __post_init__(self) -> None:
        if min(
            self.gp_own,
            self.ga_deficit_at_gp,
            self.gp_deficit_at_ga,
            self.ga_own,
        ) < 0:
            raise ValueError("slacks and deficits must be nonnegative")

    @property
    def determinant_margin(self) -> Fraction:
        """Own-slack product minus cross-deficit product."""

        return (
            self.gp_own * self.ga_own
            - self.ga_deficit_at_gp * self.gp_deficit_at_ga
        )

    @property
    def synchronizable(self) -> bool:
        """Exact condition for a convex mixture to satisfy both gates."""

        return self.determinant_margin >= 0

    def feasible_lambda_interval(self) -> tuple[Fraction, Fraction] | None:
        """Weights of the GA witness in a successful two-state mixture.

        The mixed state is ``(1-lambda) R_GP + lambda R_GA``.
        """

        a = self.gp_own
        b = self.ga_deficit_at_gp
        c = self.gp_deficit_at_ga
        d = self.ga_own
        lower = Fraction(0) if b + d == 0 else b / (b + d)
        upper = Fraction(1) if a + c == 0 else a / (a + c)
        return (lower, upper) if lower <= upper else None


def same_observable_cross_margin(
    gp_own: Fraction, ga_own: Fraction, reserve_gap: Fraction
) -> Fraction:
    """Two-witness determinant when GP and GA bound one observable.

    If the GP witness is below the upper threshold by ``gp_own`` and the GA
    witness is above the lower threshold by ``ga_own``, while the lower
    threshold exceeds the upper by ``reserve_gap``, then the unreported
    cross-deficits are ``gp_own+reserve_gap`` and
    ``ga_own+reserve_gap``.  The determinant is strictly negative for every
    positive gap.
    """

    if min(gp_own, ga_own, reserve_gap) < 0:
        raise ValueError("slacks and reserve_gap must be nonnegative")
    return -reserve_gap * (gp_own + ga_own + reserve_gap)


def common_observable_minimax(
    upper: Fraction,
    lower: Fraction,
    observable_min: Fraction = Fraction(0),
    observable_max: Fraction = Fraction(1),
) -> tuple[Fraction, Fraction]:
    """Maximize ``min(upper-f, f-lower)`` over an observable interval.

    Returns the exact game value and one maximizing observable value.
    This is the actual-candidate polarity fixture: GP asks for ``f<=upper``
    and GA asks for the *same* completed observable ``f>=lower``.
    """

    if observable_min > observable_max:
        raise ValueError("empty observable interval")
    crossing = (upper + lower) / 2
    optimizer = min(max(crossing, observable_min), observable_max)
    value = min(upper - optimizer, optimizer - lower)
    return value, optimizer


def scalarized_common_observable_value(
    theta: Fraction,
    upper: Fraction,
    lower: Fraction,
    observable_min: Fraction = Fraction(0),
    observable_max: Fraction = Fraction(1),
) -> Fraction:
    """Inner maximum in the two-gate Sion scalarization.

    ``theta`` weights the GP slack and ``1-theta`` the GA slack.
    """

    if not Fraction(0) <= theta <= Fraction(1):
        raise ValueError("theta must lie in [0,1]")
    coefficient = Fraction(1) - 2 * theta
    observable = observable_max if coefficient >= 0 else observable_min
    return (
        theta * upper
        - (Fraction(1) - theta) * lower
        + coefficient * observable
    )


def minimum_slack(slacks: Sequence[Fraction]) -> Fraction:
    if not slacks:
        raise ValueError("at least one gate is required")
    return min(slacks)


def finite_state_primal_value(
    slack_vectors: Iterable[Sequence[Fraction]],
) -> Fraction:
    """Best common slack when the listed vectors are the available states.

    This intentionally does not optimize over their convex hull; it is a
    lightweight exact checker used for fixtures.  The theorem card gives the
    full convex minimax identity.
    """

    values = [minimum_slack(tuple(row)) for row in slack_vectors]
    if not values:
        raise ValueError("at least one state is required")
    return max(values)


# Exact three-coordinate scalar packet used for the phase obstruction.
def lag_one_matrix() -> np.ndarray:
    """Hermitian matrix whose quadratic form is Re of the lag-one row."""

    return np.array(
        [[0, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0]], dtype=complex
    )


def lag_two_real_matrix() -> np.ndarray:
    """Hermitian matrix extracting Re(c*conj(a)) from q=(a,b,c)."""

    return np.array(
        [[0, 0, 0.5], [0, 0, 0], [0.5, 0, 0]], dtype=complex
    )


def lag_two_imag_matrix() -> np.ndarray:
    """Hermitian matrix extracting Im(c*conj(a)) from q=(a,b,c)."""

    return np.array(
        [[0, 0, -0.5j], [0, 0, 0], [0.5j, 0, 0]], dtype=complex
    )


def quadratic_value(vector: np.ndarray, matrix: np.ndarray) -> float:
    vector = np.asarray(vector, dtype=complex)
    return float(np.vdot(vector, matrix @ vector).real)


def lag_autocorrelation(vector: np.ndarray, lag: int) -> complex:
    """Finite scalar autocorrelation ``sum q[j+lag] conj(q[j])``."""

    vector = np.asarray(vector, dtype=complex)
    if lag < 0:
        return lag_autocorrelation(vector, -lag).conjugate()
    if lag >= len(vector):
        return 0j
    return complex(np.vdot(vector[: len(vector) - lag], vector[lag:]))


def phase_joint_feasible(
    gp_real_threshold: Fraction,
    ga_imag_threshold: Fraction,
    *,
    lag_radius: Fraction = Fraction(1, 2),
) -> bool:
    """Schur/AM-GM test for one phase meeting two orthogonal lower bounds."""

    if gp_real_threshold < 0 or ga_imag_threshold < 0 or lag_radius < 0:
        raise ValueError("phase thresholds and radius must be nonnegative")
    return (
        gp_real_threshold * gp_real_threshold
        + ga_imag_threshold * ga_imag_threshold
        <= lag_radius * lag_radius
    )


PHASE_THRESHOLD = Fraction(2, 5)
PHASE_RADIUS = Fraction(1, 2)
PHASE_REQUIRED_SQUARED_RADIUS = 2 * PHASE_THRESHOLD * PHASE_THRESHOLD
PHASE_AVAILABLE_SQUARED_RADIUS = PHASE_RADIUS * PHASE_RADIUS


def phase_counterfixture_vectors() -> tuple[np.ndarray, np.ndarray]:
    """Separate normalized QP-null witnesses for real and imaginary phase."""

    scale = 1.0 / np.sqrt(2.0)
    q_gp = np.array([scale, 0.0, scale], dtype=complex)
    q_ga = np.array([scale, 0.0, 1j * scale], dtype=complex)
    return q_gp, q_ga


def coherent_null_break_vectors() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Two self-null channels whose coherent sum is not null at lag one."""

    e = np.array([1.0, 0.0, 0.0], dtype=complex)
    v = np.array([0.0, 1.0, 0.0], dtype=complex)
    q = (e + v) / np.sqrt(2.0)
    return e, v, q


def separate_witnesses_do_not_imply_joint_state() -> bool:
    """Binary verdict of the exact phase counterfixture."""

    return not phase_joint_feasible(PHASE_THRESHOLD, PHASE_THRESHOLD)


def live_same_packet_hypothesis_closes_strip(
    *,
    qp_promote: bool,
    compact_autocorrelation_factorization: bool,
    full_scalarization_nonnegative: bool,
    strict_joint_budget: bool,
    reserve_gap_positive: bool,
    low_height_closed: bool,
) -> bool:
    """Logical audit of the strengthened same-packet theorem card."""

    return all(
        (
            qp_promote,
            compact_autocorrelation_factorization,
            full_scalarization_nonnegative,
            strict_joint_budget,
            reserve_gap_positive,
            low_height_closed,
        )
    )


def audit() -> dict[str, str | bool]:
    upper = Fraction(1, 4)
    lower = Fraction(3, 4)
    game_value, optimizer = common_observable_minimax(upper, lower)
    fixture = TwoWitnessSlacks(
        gp_own=upper,
        ga_deficit_at_gp=lower,
        gp_deficit_at_ga=Fraction(1) - upper,
        ga_own=Fraction(1) - lower,
    )
    return {
        "zf_delta": str(ZF_DELTA),
        "gp_surcharge": str(GP_SURCHARGE),
        "qp_promote_x_bill": str(QP_PROMOTE_X_BILL),
        "gp_correction_room_at_promote_frontier": str(
            GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER
        ),
        "common_observable_game_value": str(game_value),
        "common_observable_optimizer": str(optimizer),
        "two_witness_determinant_margin": str(fixture.determinant_margin),
        "two_witness_synchronizable": fixture.synchronizable,
        "phase_required_squared_radius": str(PHASE_REQUIRED_SQUARED_RADIUS),
        "phase_available_squared_radius": str(PHASE_AVAILABLE_SQUARED_RADIUS),
        "phase_joint_feasible": phase_joint_feasible(
            PHASE_THRESHOLD, PHASE_THRESHOLD
        ),
        "coherent_channels_preserve_qp_null_automatically": False,
        "separate_witnesses_imply_joint_state": not (
            separate_witnesses_do_not_imply_joint_state()
        ),
    }


if __name__ == "__main__":
    print(audit())
