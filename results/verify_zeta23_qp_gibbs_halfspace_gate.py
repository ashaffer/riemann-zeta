#!/usr/bin/env python3
"""Replay the finite exponent ledger for the Gibbs halfspace report."""

from qp_gibbs_halfspace_gate import (
    forced_bad_moment,
    limiting_common_tilt_mean,
    qp_scaling,
    shifted_square_ledger,
    target_epsilon,
)


def main() -> None:
    packet_count = 10_000
    epsilon = target_epsilon(packet_count)
    square = shifted_square_ledger(packet_count)
    scaling = qp_scaling(2_000.0)
    tilted = limiting_common_tilt_mean(2.0)
    assert forced_bad_moment(packet_count) == -2.0 * epsilon
    assert square.total_bound < 2.001
    assert tilted < -1.0
    print(
        "PASS "
        f"R={packet_count} epsilon={epsilon:.9g} "
        f"forced_bad={forced_bad_moment(packet_count):.9g} "
        f"shifted_square={square.total_bound:.9g} "
        f"tilted_limit_mean={tilted:.9g} "
        f"critical_R={scaling['packet_count']:.9g}"
    )


if __name__ == "__main__":
    main()
