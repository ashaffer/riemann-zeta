"""One-sided carrier-slice support for the finite Zeta23 fixtures.

For Hermitian matrices ``R`` and ``N >= 0`` on an already compressed
positive-null space, this module evaluates

    h_eta(R) = max Tr(R Gamma)
               Gamma >= 0, Tr(Gamma) = 1, Tr(N Gamma) >= eta.

The scalar dual

    h_eta(R) = inf_{mu >= 0} lambda_max(R + mu N) - mu eta

reduces the SDP to Hermitian eigenvalues and one convex scalar minimization.
No external SDP package is used.  The two built-in fixtures are the exact
normalized one-pair mirror compression and the abstract two-pair collateral
cross-row model documented in the 2026-08-12 Zeta23 audits.

This is a finite diagnostic.  In particular, the collateral fixture is not
asserted to be a joint normalized Paley--Wiener realization or actual zeta
coefficient matrix.
"""
from __future__ import annotations

from dataclasses import dataclass
import argparse
import json
import math
from typing import Any, Dict

import numpy as np


@dataclass(frozen=True)
class SupportResult:
    value: float
    dual_mu: float
    boundary_slice: bool


def _as_hermitian(matrix: np.ndarray, name: str) -> np.ndarray:
    answer = np.asarray(matrix, dtype=complex)
    if answer.ndim != 2 or answer.shape[0] != answer.shape[1]:
        raise ValueError(f"{name} must be square")
    scale = max(1.0, float(np.linalg.norm(answer, ord=2)))
    if np.linalg.norm(answer - answer.conj().T, ord=2) > 1e-10 * scale:
        raise ValueError(f"{name} must be Hermitian")
    return (answer + answer.conj().T) / 2


def carrier_slice_support(
    remainder: np.ndarray,
    carrier: np.ndarray,
    eta: float,
    *,
    iterations: int = 160,
) -> SupportResult:
    """Evaluate the carrier-slice support by its one-variable dual.

    The matrices must already act on the positive-null space.  For
    ``eta < lambda_max(carrier)`` the primal has a strict carrier point and
    the scalar dual is minimized numerically.  At the boundary
    ``eta = lambda_max(carrier)``, feasible states are supported on the top
    eigenspace of ``carrier``; that restriction is evaluated directly.
    Inputs within the explicit floating tolerances below are snapped to that
    boundary.  This routine is therefore a double-precision evaluator of the
    exact analytic dual, not an interval or exact-arithmetic certificate.
    """
    if eta < 0:
        raise ValueError("eta must be nonnegative")
    r_matrix = _as_hermitian(remainder, "remainder")
    n_matrix = _as_hermitian(carrier, "carrier")
    if r_matrix.shape != n_matrix.shape:
        raise ValueError("remainder and carrier shapes differ")

    n_values, n_vectors = np.linalg.eigh(n_matrix)
    n_min = float(n_values[0])
    n_max = float(n_values[-1])
    scale = max(1.0, abs(n_min), abs(n_max))
    if n_min < -1e-10 * scale:
        raise ValueError("carrier must be positive semidefinite")
    if eta > n_max + 1e-10 * scale:
        raise ValueError("carrier slice is empty")

    # At the exposed boundary, Tr(N Gamma) >= lambda_max(N) forces Gamma to
    # live on the top eigenspace.  This also covers a one-dimensional mirror.
    if eta >= n_max - 1e-10 * scale:
        keep = n_values >= n_max - 1e-9 * scale
        top = n_vectors[:, keep]
        restricted = top.conj().T @ r_matrix @ top
        value = float(np.linalg.eigvalsh(restricted)[-1])
        return SupportResult(value=value, dual_mu=math.inf,
                             boundary_slice=True)

    def objective(mu: float) -> float:
        top = float(np.linalg.eigvalsh(r_matrix + mu * n_matrix)[-1])
        return top - mu * eta

    # The objective is convex and tends to +infinity because
    # eta < lambda_max(N).  Exponential bracketing therefore finds an interval
    # containing a minimizer, including the endpoint mu=0.
    r_norm = float(np.linalg.norm(r_matrix, ord=2))
    gap = max(n_max - eta, 1e-15)
    right = max(1.0, 2.0 * r_norm / gap)
    f_zero = objective(0.0)
    f_right = objective(right)
    if f_right < f_zero:
        for _ in range(80):
            doubled = 2.0 * right
            f_doubled = objective(doubled)
            if f_doubled >= f_right:
                right = doubled
                break
            right, f_right = doubled, f_doubled
        else:
            raise RuntimeError("failed to bracket the scalar dual minimum")

    # Golden-section minimization is sufficient here: each evaluation is only
    # one Hermitian eigenvalue computation, and the objective is convex.
    left = 0.0
    golden = (math.sqrt(5.0) - 1.0) / 2.0
    x_left = right - golden * (right - left)
    x_right = left + golden * (right - left)
    f_left = objective(x_left)
    f_right_inner = objective(x_right)
    for _ in range(iterations):
        if f_left <= f_right_inner:
            right = x_right
            x_right, f_right_inner = x_left, f_left
            x_left = right - golden * (right - left)
            f_left = objective(x_left)
        else:
            left = x_left
            x_left, f_left = x_right, f_right_inner
            x_right = left + golden * (right - left)
            f_right_inner = objective(x_right)

    candidates = [
        (0.0, f_zero),
        (x_left, f_left),
        (x_right, f_right_inner),
        (right, objective(right)),
    ]
    dual_mu, value = min(candidates, key=lambda pair: pair[1])
    return SupportResult(value=float(value), dual_mu=float(dual_mu),
                         boundary_slice=False)


def collateral_support_closed_form(k0: float, k1: float, eta: float) -> float:
    """Closed form for the two-pair collateral cross-row fixture."""
    if k0 <= 0 or k1 <= 0:
        raise ValueError("k0 and k1 must be positive")
    fraction = eta / (2.0 * k0)
    if fraction < 0 or fraction > 1 + 1e-12:
        raise ValueError("carrier slice is empty")
    fraction = min(1.0, max(0.0, fraction))
    optimum = (1.0 - 1.0 / math.sqrt(3.0)) / 2.0
    if fraction <= optimum:
        return k1 * (math.sqrt(3.0) - 1.0) / 2.0
    return k1 * (-fraction + math.sqrt(2.0 * fraction * (1.0 - fraction)))


def mirror_demo(
    alpha: float = 2.0 / 5.0,
    separation_fraction: float = 3.0 / 5.0,
    support_length: float = 10.0,
    m: float = 1.0,
) -> Dict[str, Any]:
    """Exact scale-normalized one-pair PW/Gabor mirror calculation."""
    distance = separation_fraction * support_length
    c_hyp = math.cosh(alpha * distance)
    # On e_- after the positive spectral row is nulled:
    # B = -m C, N_spectral = m(C-1), and the exact same-lobe remainder is m.
    n_spectral = np.array([[m * (c_hyp - 1.0)]])
    diagonal_remainder = np.array([[m]])
    eta = m * (c_hyp - 1.0)
    support = carrier_slice_support(diagonal_remainder, n_spectral, eta)
    cancellation_bill = m * c_hyp
    carrier_scale = m * c_hyp / 2.0
    return {
        "alpha": alpha,
        "separation_fraction": separation_fraction,
        "support_length": support_length,
        "distance": distance,
        "m": m,
        "C_cosh_alpha_D": c_hyp,
        "spectral_carrier_mass": eta,
        "cross_cancellation_bill": cancellation_bill,
        "K_equals_mC_over_2": carrier_scale,
        "h_eta_diagonal_remainder": support.value,
        "h_over_cross_bill": support.value / cancellation_bill,
        "h_over_K": support.value / carrier_scale,
    }


def collateral_demo(k0: float = 1.0, k1: float = 1.0) -> Dict[str, Any]:
    """Two-pair abstract collateral cross-row calculation.

    The compressed basis is ``q=(u-v)/sqrt(2), w``.  The selected aligned row
    is ``B0=-N`` and the collateral aggregate cross remainder is ``R``.
    """
    n_matrix = np.array([[2.0 * k0, 0.0], [0.0, 0.0]])
    r_matrix = k1 * np.array(
        [[-1.0, -1.0 / math.sqrt(2.0)],
         [-1.0 / math.sqrt(2.0), 0.0]]
    )

    # The largest-carrier aggregate-null pure state has q-mass x_cancel.
    denominator = (2.0 * k0 + k1) ** 2 + 2.0 * k1 ** 2
    x_cancel = 2.0 * k1 ** 2 / denominator
    eta_cancel = 2.0 * k0 * x_cancel
    compressed_state = np.array([-math.sqrt(x_cancel),
                                 math.sqrt(1.0 - x_cancel)])
    aligned = -n_matrix
    selected_value = float(compressed_state @ aligned @ compressed_state)
    remainder_value = float(compressed_state @ r_matrix @ compressed_state)

    support = carrier_slice_support(r_matrix, n_matrix, eta_cancel)
    analytic = collateral_support_closed_form(k0, k1, eta_cancel)
    positive_part_norm = max(0.0, float(np.linalg.eigvalsh(r_matrix)[-1]))

    # Recover the full (u,w,v) vector and complete pair forms from the report.
    q_value, w_value = compressed_state
    full_state = np.array([q_value / math.sqrt(2.0), w_value,
                           -q_value / math.sqrt(2.0)])
    u = np.array([1.0, 0.0, 0.0])
    w = np.array([0.0, 1.0, 0.0])
    v = np.array([0.0, 0.0, 1.0])
    a0 = math.sqrt(k0 / 2.0)
    a1 = math.sqrt(k1 / 2.0)
    x0, y0 = a0 * (u + v), a0 * (u - v)
    x1, y1 = a1 * (u + v), a1 * (w - v)
    complete0 = 2.0 * (np.outer(x0, x0) - np.outer(y0, y0))
    complete1 = 2.0 * (np.outer(x1, x1) - np.outer(y1, y1))

    high_fraction = 3.0 / 4.0
    high_eta = 2.0 * k0 * high_fraction
    high_support = carrier_slice_support(r_matrix, n_matrix, high_eta)
    return {
        "k0": k0,
        "k1": k1,
        "compressed_N": n_matrix.tolist(),
        "compressed_R_cross": r_matrix.tolist(),
        "positive_part_norm_R": positive_part_norm,
        "x_cancel_q_mass": x_cancel,
        "eta_cancel": eta_cancel,
        "h_eta_cancel_dual": support.value,
        "h_eta_cancel_closed_form": analytic,
        "dual_mu": support.dual_mu,
        "aggregate_null_state": compressed_state.tolist(),
        "aligned_expectation": selected_value,
        "remainder_expectation": remainder_value,
        "aggregate_expectation": selected_value + remainder_value,
        "complete_selected_pair_expectation": float(
            full_state @ complete0 @ full_state
        ),
        "complete_collateral_pair_expectation": float(
            full_state @ complete1 @ full_state
        ),
        "three_quarter_carrier_eta": high_eta,
        "h_at_three_quarter_carrier": high_support.value,
    }


def prime5_actual_demo(
    support_length: float = 3.27,
    dimension: int = 12,
    dps: int = 24,
    relative: bool = False,
) -> Dict[str, Any]:
    """Floating actual-prime diagnostic from the repository's p=5 fixture.

    The old form contains the actual zeta places ``{2,3}``; the remainder is
    exactly the p=5 event when ``2 log(5) < L < 2 log(7)``.  This old low-
    support Ritz model is zero-independent, but it is not the high-T
    asymmetric Gabor fixture used by the mirror argument.
    """
    if not 2.0 * math.log(5.0) < support_length < 2.0 * math.log(7.0):
        raise ValueError("prime5 support must lie between 2 log(5) and 2 log(7)")
    # Keep the exact-mirror path lightweight.  These established repository
    # routines (mpmath/scipy) are imported only for the optional actual-prime
    # diagnostic.
    import mpmath as mp
    from prime5_block_rescue import inverse_square_root, ritz_form

    mp.mp.dps = dps
    old, old_basis = ritz_form(
        support_length, dimension, dps, {2, 3}, relative
    )
    full, full_basis = ritz_form(
        support_length, dimension, dps, None, relative
    )
    if not np.allclose(old_basis, full_basis):
        raise RuntimeError("prime5 constraint bases unexpectedly differ")

    old_values, old_vectors = np.linalg.eigh(old)
    negative_count = int(np.count_nonzero(old_values < -1e-10))
    if negative_count == 0:
        raise ValueError("old prime5 fixture has no resolved negative carrier")
    negative_vectors = old_vectors[:, :negative_count]
    carrier = np.diag(-old_values[:negative_count])
    event = negative_vectors.T @ (full - old) @ negative_vectors

    # The default L=3.27 fixture has one negative direction.  For a larger
    # negative block, eta=lambda_max(N) deliberately tests its deepest exposed
    # carrier slice rather than claiming a uniform Loewner rescue.
    eta = float(np.linalg.eigvalsh(carrier)[-1])
    event_support = carrier_slice_support(event, carrier, eta)

    transformed = old_vectors.T @ full @ old_vectors
    block_a = transformed[:negative_count, :negative_count]
    block_b = transformed[:negative_count, negative_count:]
    block_d = transformed[negative_count:, negative_count:]
    coupling = math.nan
    if (np.linalg.eigvalsh(block_a)[0] > 0
            and np.linalg.eigvalsh(block_d)[0] > 0):
        normalized = (inverse_square_root(block_a) @ block_b
                      @ inverse_square_root(block_d))
        coupling = float(np.linalg.svd(normalized, compute_uv=False)[0])

    return {
        "scope": "floating low-support actual-prime Ritz diagnostic",
        "support_length": support_length,
        "dimension": dimension,
        "dps": dps,
        "relative": relative,
        "negative_count_old_2_3_form": negative_count,
        "old_min": float(old_values[0]),
        "full_min": float(np.linalg.eigvalsh(full)[0]),
        "eta_deepest_old_carrier": eta,
        "h_eta_prime5_event": event_support.value,
        "h_over_eta": event_support.value / eta,
        "full_A_min_on_old_negative_block": float(
            np.linalg.eigvalsh(block_a)[0]
        ),
        "normalized_cross_coupling": coupling,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture",
                        choices=("mirror", "collateral", "prime5", "all"),
                        default="all")
    parser.add_argument("--k0", type=float, default=1.0)
    parser.add_argument("--k1", type=float, default=1.0)
    parser.add_argument("--support", type=float, default=3.27)
    parser.add_argument("--dimension", type=int, default=12)
    parser.add_argument("--dps", type=int, default=24)
    parser.add_argument("--relative", action="store_true")
    args = parser.parse_args()

    payload: Dict[str, Any] = {}
    if args.fixture in ("mirror", "all"):
        payload["mirror"] = mirror_demo()
    if args.fixture in ("collateral", "all"):
        payload["collateral"] = collateral_demo(args.k0, args.k1)
    if args.fixture == "prime5":
        payload["prime5"] = prime5_actual_demo(
            args.support, args.dimension, args.dps, args.relative
        )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
