"""Diagnostic scan of a log-elliptic Birman--Schwinger preconditioner.

The unshifted archimedean matrix is used as the log-elliptic part.  A scalar
L2 shift makes it positive, P = A_arch + mu G, and the remainder is R = Q-P.
The full zero-mode equation is equivalent to Kc=c for K=-P^{-1}R.

This is a discovery diagnostic, not a positivity proof: for P>0, kappa_max<1
is algebraically equivalent to Q>0 in the same Galerkin space.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import numpy as np
import scipy.linalg

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from hp_margins import hp_form


def matrix(form) -> np.ndarray:
    out = np.array(form.tolist(), dtype=float)
    return (out + out.T) / 2


def scan_one(L: float, m: int, dps: int, shift_factor: float) -> tuple[float, ...]:
    Qmp, Gmp = hp_form(L, m, dps=dps)
    Amp, _ = hp_form(L, m, dps=dps, include_primes=False, zeta_pole=False)
    Q, G, A = matrix(Qmp), matrix(Gmp), matrix(Amp)

    arch_floor = float(scipy.linalg.eigh(A, G, subset_by_index=[0, 0])[0][0])
    # The +1 scale is fixed in the L2 metric and prevents a nearly singular P.
    mu = max(0.0, -arch_floor) + shift_factor
    P = A + mu * G
    R = Q - P
    qeval, qvec = scipy.linalg.eigh(Q, G, subset_by_index=[0, 0])
    keval, kvec = scipy.linalg.eigh(-R, P, subset_by_index=[m - 1, m - 1])
    qv, kv = qvec[:, 0], kvec[:, 0]
    qv /= np.sqrt(qv @ G @ qv)
    kv /= np.sqrt(kv @ G @ kv)
    alignment = abs(float(qv @ G @ kv))
    return arch_floor, mu, float(qeval[0]), float(keval[0]), 1-float(keval[0]), alignment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.38629436, 1.75, 2.19722458, 2.485,
                                 2.77258872, 2.996, 3.21887582, 3.58351894])
    parser.add_argument("--sizes", nargs="+", type=int, default=[31, 51])
    parser.add_argument("--shifts", nargs="+", type=float, default=[0.25, 1.0, 4.0])
    parser.add_argument("--dps", type=int, default=35)
    args = parser.parse_args()
    print("L,m,shift,arch_floor,mu,lambda_Q,kappa_max,gap,ground_alignment")
    for L in args.supports:
        for m in args.sizes:
            for shift in args.shifts:
                vals = scan_one(L, m, args.dps, shift)
                print(f"{L:.9g},{m},{shift:.6g}," + ",".join(f"{v:.10e}" for v in vals))


if __name__ == "__main__":
    main()
