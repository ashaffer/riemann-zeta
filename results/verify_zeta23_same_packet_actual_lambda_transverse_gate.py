#!/usr/bin/env python3
"""Replay the exact coefficient and isolation ledgers for the GA2 gate."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from high_height_carrier_slice import (
    archimedean_matrix_sign,
    pole_matrix_sign,
    prime_matrix_sign,
)
from same_packet_actual_lambda_transverse_gate import (
    actual_lambda_cross_coefficient,
    actual_lambda_schur_vector,
    gram_energy,
    isolation_log_ratio,
    transverse_data,
)
from signed_garding_failfast import prime_powers


def main() -> None:
    length = math.log(64.0)
    indices = np.arange(-3, 4)
    tau = 96.0 + 2.0 * math.pi * indices / length
    logs, weights = prime_powers(64)
    active = logs <= length + 1e-13
    logs, weights = logs[active], weights[active]
    rng = np.random.default_rng(230813)
    synthesis = rng.normal(size=(tau.size, tau.size - 2))
    inclusion = np.linalg.qr(synthesis)[0]
    background = (
        archimedean_matrix_sign(tau, length)
        + pole_matrix_sign(tau, indices, length)
    )
    quotient_dimension = inclusion.shape[1]
    e = rng.normal(size=quotient_dimension) + 1j * rng.normal(
        size=quotient_dimension
    )
    e /= np.linalg.norm(e)
    v = rng.normal(size=quotient_dimension) + 1j * rng.normal(
        size=quotient_dimension
    )
    v -= e * np.vdot(e, v)
    v /= np.linalg.norm(v)

    prime = prime_matrix_sign(tau, length, logs, weights)
    reserve = (
        inclusion.conj().T @ (background - prime) @ inclusion
        / (length * length)
    )
    direct = np.vdot(e, reserve @ v)
    expanded = actual_lambda_cross_coefficient(
        tau, length, logs, weights, inclusion, e, v, background
    )
    cross_error = abs(direct - expanded)
    total, bg_vector, columns = actual_lambda_schur_vector(
        tau, length, logs, weights, inclusion, e, background
    )
    gram_error = abs(np.vdot(total, total).real - gram_energy(bg_vector, columns))

    data = transverse_data(reserve, e)
    aligned = transverse_data(reserve + 11.0 * np.outer(e, e.conj()), e)
    aligned_error = max(
        abs(data.schur_residual - aligned.schur_residual),
        abs(data.transverse_lambda_max - aligned.transverse_lambda_max),
    )
    hostile = isolation_log_ratio(40_000.0, 0.3234, 0.3034, 8.0)
    if cross_error > 1e-10 or gram_error > 1e-10 or aligned_error > 1e-10:
        raise SystemExit("FAIL: exact transverse identity residual")
    if hostile >= -100.0:
        raise SystemExit("FAIL: fixed depth gap did not beat logarithmic loss")

    print("PASS same-packet actual-Lambda transverse gate")
    print(f"actual coefficient residual={cross_error:.3e}")
    print(f"two-prime Gram residual={gram_error:.3e}")
    print(f"aligned-carrier invisibility residual={aligned_error:.3e}")
    print(f"hostile isolation log-ratio={hostile:.6f}")
    print(f"active actual prime powers={logs.size}")


if __name__ == "__main__":
    main()
