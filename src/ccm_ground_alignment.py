"""Direct CCM-prolate versus Weil-ground-state checkpoint.

The source vector is the same-Fourier-sign combination of the first and third
even prolate modes (degrees 0 and 4) that vanishes at the origin.  We apply
the CCM arithmetic map E, project to the orthonormal Legendre basis used by
spectral_margins.py, and report:

* L2 alignment with the lowest Weil eigenvector;
* scalar defect d = <k,Qk>;
* complement floor of Q on k-perp;
* the Schur/Feshbach ratio <b,C^{-1}b>/d.

The ratio is a diagnostic, not a positivity proof: for C>0 it is <1 exactly
when the finite matrix Q is positive.  Its useful content is whether it stays
well separated from one and whether k itself captures the ground direction.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import numpy as np
import scipy.linalg
import scipy.special
import mpmath as mp
from numpy.polynomial.legendre import legval, legvander

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from spectral_margins import spectral_form


def prolate_source(lam: float, nodes: int) -> tuple[np.ndarray, np.ndarray]:
    """Return GL nodes and the normalized degree-(0,4) CCM source values."""
    t, w = np.polynomial.legendre.leggauss(nodes)
    c = 2 * np.pi * lam * lam
    # The differential equation labels fixed modes even when the integral
    # eigenvalues are indistinguishable from one in machine precision.
    psi0 = scipy.special.pro_ang1(0, 0, c, t)[0]
    psi4 = scipy.special.pro_ang1(0, 4, c, t)[0]
    if not (np.all(np.isfinite(psi0)) and np.all(np.isfinite(psi4))):
        raise RuntimeError("scipy spheroidal evaluation failed at this scale")
    V = legvander(t, nodes - 1)
    degrees = np.arange(nodes)
    c0 = (2 * degrees + 1) / 2 * (V.T @ (w * psi0))
    c4 = (2 * degrees + 1) / 2 * (V.T @ (w * psi4))
    v0 = float(legval(0.0, c0))
    v4 = float(legval(0.0, c4))
    phi = psi4 * v0 - psi0 * v4
    norm = np.sqrt(lam * np.dot(w, phi * phi))
    return t, phi / norm


def source_evaluator(t: np.ndarray, values: np.ndarray):
    w = np.polynomial.legendre.leggauss(len(t))[1]
    V = legvander(t, len(t) - 1)
    degrees = np.arange(len(t))
    coeff = (2 * degrees + 1) / 2 * (V.T @ (w * values))
    return lambda z: legval(z, coeff)


def ccm_coefficients(L: float, m: int, prolate_nodes: int,
                     x_nodes: int) -> np.ndarray:
    a = L / 4
    lam = np.exp(a)
    t, phi = prolate_source(lam, prolate_nodes)
    phi_at = source_evaluator(t, phi)
    tx, wx = np.polynomial.legendre.leggauss(x_nodes)
    x = a * tx
    u = np.exp(x)
    kval = np.zeros_like(x)
    for i, ui in enumerate(u):
        nmax = int(np.floor(lam / ui + 1e-13))
        if nmax:
            args = np.arange(1, nmax + 1) * ui / lam
            kval[i] = np.sqrt(ui) * np.sum(phi_at(args))
    V = legvander(tx, m - 1)
    scale = np.sqrt((2 * np.arange(m) + 1) / (2 * a))
    coeff = a * scale * (V.T @ (wx * kval))
    coeff /= np.linalg.norm(coeff)
    return coeff


def checkpoint(L: float, m: int, dps: int, pn: int, xn: int):
    k = ccm_coefficients(L, m, pn, xn)
    with mp.workdps(dps):
        Q = spectral_form(L, m, dps=dps)
        evals, evecs = mp.eigsy(Q)
        km = mp.matrix([mp.mpf(float(v)) for v in k])
        alignment = abs(mp.fdot(km, evecs[:, 0]))
        qk = Q * km
        defect = mp.fdot(km, qk)
        # Block Schur complement in the decomposition span(k) + k-perp:
        # d - b'C^-1b = 1 / <k,Q^-1 k>.
        invquad = mp.fsum(
            (mp.fdot(km, evecs[:, j]) ** 2) / evals[j]
            for j in range(m)
        )
        ratio = 1 - 1 / (defect * invquad)
        # Cauchy interlacing puts the compressed complement floor between
        # lambda_0 and lambda_1; report lambda_1 as its useful scale proxy.
        return tuple(float(v) for v in
                     (evals[0], evals[1], alignment, defect, evals[1], ratio))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--supports", nargs="+", type=float,
                   default=[1.75, 2.485, 2.996, 3.555, 4.0])
    p.add_argument("--dimension", type=int, default=32)
    p.add_argument("--dps", type=int, default=40)
    p.add_argument("--prolate-nodes", type=int, default=180)
    p.add_argument("--x-nodes", type=int, default=300)
    a = p.parse_args()
    print("L,m,lambda0,lambda1,alignment,scalar_defect,complement_floor,feshbach_ratio")
    for L in a.supports:
        vals = checkpoint(L, a.dimension, a.dps,
                          a.prolate_nodes, a.x_nodes)
        print(f"{L:.9g},{a.dimension}," + ",".join(f"{v:.12e}" for v in vals),
              flush=True)


if __name__ == "__main__":
    main()
