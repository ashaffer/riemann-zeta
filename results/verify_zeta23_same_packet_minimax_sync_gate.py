#!/usr/bin/env python3
"""Replay the exact same-packet minimax and phase counterfixtures."""

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from same_packet_minimax_sync_gate import (  # noqa: E402
    GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER,
    PHASE_AVAILABLE_SQUARED_RADIUS,
    PHASE_REQUIRED_SQUARED_RADIUS,
    PHASE_THRESHOLD,
    TwoWitnessSlacks,
    audit,
    common_observable_minimax,
    coherent_null_break_vectors,
    lag_autocorrelation,
    lag_one_matrix,
    lag_two_imag_matrix,
    lag_two_real_matrix,
    phase_counterfixture_vectors,
    phase_joint_feasible,
    quadratic_value,
    scalarized_common_observable_value,
    same_observable_cross_margin,
)


def main() -> None:
    assert GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER == Fraction(
        3_372_810_389, 250_000_000_000
    )

    value, optimizer = common_observable_minimax(
        Fraction(1, 4), Fraction(3, 4)
    )
    assert value == Fraction(-1, 4)
    assert optimizer == Fraction(1, 2)
    assert scalarized_common_observable_value(
        Fraction(1, 2), Fraction(1, 4), Fraction(3, 4)
    ) == Fraction(-1, 4)

    fixture = TwoWitnessSlacks(
        gp_own=Fraction(1, 4),
        ga_deficit_at_gp=Fraction(3, 4),
        gp_deficit_at_ga=Fraction(3, 4),
        ga_own=Fraction(1, 4),
    )
    assert fixture.determinant_margin == Fraction(-1, 2)
    assert same_observable_cross_margin(
        Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)
    ) == Fraction(-1, 2)
    assert not fixture.synchronizable
    assert fixture.feasible_lambda_interval() is None

    assert PHASE_REQUIRED_SQUARED_RADIUS == Fraction(8, 25)
    assert PHASE_AVAILABLE_SQUARED_RADIUS == Fraction(1, 4)
    assert not phase_joint_feasible(PHASE_THRESHOLD, PHASE_THRESHOLD)

    e, v, coherent = coherent_null_break_vectors()
    assert np.isclose(lag_autocorrelation(e, 1), 0.0)
    assert np.isclose(lag_autocorrelation(v, 1), 0.0)
    assert np.isclose(lag_autocorrelation(coherent, 1), 0.5)

    q_gp, q_ga = phase_counterfixture_vectors()
    h_null = lag_one_matrix()
    h_real = lag_two_real_matrix()
    h_imag = lag_two_imag_matrix()
    assert np.isclose(np.vdot(q_gp, q_gp).real, 1.0)
    assert np.isclose(np.vdot(q_ga, q_ga).real, 1.0)
    assert np.isclose(quadratic_value(q_gp, h_null), 0.0)
    assert np.isclose(quadratic_value(q_ga, h_null), 0.0)
    assert np.isclose(abs(lag_autocorrelation(q_gp, 1)), 0.0)
    assert np.isclose(abs(lag_autocorrelation(q_ga, 1)), 0.0)
    assert np.isclose(quadratic_value(q_gp, h_real), 0.5)
    assert np.isclose(quadratic_value(q_gp, h_imag), 0.0)
    assert np.isclose(quadratic_value(q_ga, h_real), 0.0)
    assert np.isclose(quadratic_value(q_ga, h_imag), 0.5)
    assert np.isclose(lag_autocorrelation(q_gp, 2), 0.5)
    assert np.isclose(lag_autocorrelation(q_ga, 2), 0.5j)

    print("same-packet minimax synchronization gate: PASS")
    for key, item in audit().items():
        print(f"{key}={item}")


if __name__ == "__main__":
    main()
