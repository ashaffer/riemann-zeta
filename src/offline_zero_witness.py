"""Synthetic quantitative converse-Weil experiment (explicitly assumes ¬RH data).

This is NOT an unconditional zeta computation.  It takes a *truncated* on-line
zero background and injects a functional-equation quartet
  1/2 +/- delta +/- i gamma.
For a real compact-support test vector with bilateral transform F, that
quartet contributes 4 Re(F(delta+i gamma) F(-delta-i gamma)), an indefinite
rank-two real quadratic form.  We measure when it defeats the positive
on-line frame background as support grows.

The hybrid zero set is only a calibration model: actual zeta zeros below the
cutoff cannot be held fixed while an extra quartet is inserted without also
respecting zero counting and the explicit formula.  Moreover, deleting the
on-line tail deletes positive frame terms and can make negativity easier.
Consequently a negative result here demonstrates a witness mechanism, not a
theorem about zeta and not a rigorous support bound under negation of RH.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import mpmath as mp
import numpy as np
import scipy.linalg

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from model_zeros import frame_form, true_zeros_to_cutoff
from spectral_margins import gl_nodes, legvals, spectral_lam_min


def carrier_matrices(L: float, modes: int, gamma0: float,
                     online_zeros: list, delta: float, dps: int):
    """Gram, on-line frame, and quartet matrices in a carrier-adapted basis."""
    with mp.workdps(dps + 10):
        a = mp.mpf(L) / 4
        dim = 2 * modes
        nodes = gl_nodes(max(256, 6 * modes + int(float(a * gamma0) / 2) + 64))
        values = []
        weights = []
        for x0, w0 in nodes:
            x = a * x0
            P = legvals(modes, x0)
            c, s = mp.cos(gamma0 * x), mp.sin(gamma0 * x)
            values.append([P[k] * c for k in range(modes)] +
                          [P[k] * s for k in range(modes)])
            weights.append(w0 * a)

        def eval_vector(z):
            return [mp.fsum(weights[t] * values[t][j] * mp.exp(z * a * nodes[t][0])
                            for t in range(len(nodes))) for j in range(dim)]

        G = mp.matrix(dim); B = mp.matrix(dim)
        for i in range(dim):
            for j in range(dim):
                G[i, j] = mp.fsum(weights[t] * values[t][i] * values[t][j]
                                  for t in range(len(nodes)))
        for g in online_zeros:
            v = eval_vector(mp.j * g)
            for i in range(dim):
                for j in range(dim):
                    B[i, j] += 2 * mp.re(v[i] * mp.conj(v[j]))
        z = mp.mpc(delta, gamma0)
        vp, vm = eval_vector(z), eval_vector(-z)
        A = mp.matrix(dim)
        for i in range(dim):
            for j in range(dim):
                A[i, j] = 2 * mp.re(vp[i] * vm[j] + vm[i] * vp[j])
        return G, B, A


def generalized_min(A: mp.matrix, G: mp.matrix) -> float:
    Af = np.array(A.tolist(), dtype=float)
    Gf = np.array(G.tolist(), dtype=float)
    return scipy.linalg.eigh((Af + Af.T) / 2, (Gf + Gf.T) / 2,
                             subset_by_index=[0, 0], check_finite=False)[0][0]


def laplace_vector(L: float, m: int, z: complex, dps: int) -> list[mp.mpc]:
    """Coordinates of f -> integral f(x) exp(z x) dx in the orthonormal basis."""
    with mp.workdps(dps + 10):
        a = mp.mpf(L) / 4
        z = mp.mpc(z)
        norm = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in range(m)]
        nodes = gl_nodes(max(m + 12, 128, int(float(a * abs(z.imag)) / 1.5) + 48))
        out = [mp.mpc(0)] * m
        for x0, w0 in nodes:
            x = a * x0
            P = legvals(m, x0)
            factor = w0 * a * mp.exp(z * x)
            for k in range(m):
                out[k] += factor * norm[k] * P[k]
        return out


def quartet_matrix(L: float, m: int, delta: float, gamma: float,
                   dps: int) -> mp.matrix:
    z = mp.mpc(delta, gamma)
    vp = laplace_vector(L, m, z, dps)
    vm = laplace_vector(L, m, -z, dps)
    A = mp.matrix(m)
    # c^T A c = 4 Re[(c.vp)(c.vm)].
    for i in range(m):
        for j in range(m):
            A[i, j] = 2 * mp.re(vp[i] * vm[j] + vm[i] * vp[j])
    return A


def first_negative_carrier(supports, modes, gamma, zeros, delta, dps):
    """Return the first sampled support with a negative hybrid eigenvalue."""
    for L in supports:
        G, background, quartet = carrier_matrices(
            L, modes, gamma, zeros, delta, dps)
        value = generalized_min(background + quartet, G)
        if value < 0:
            return L, value
    return None, value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delta", type=float, default=0.308517182457)
    parser.add_argument("--gamma", type=float, default=85.6993484854)
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[2, 3, 4, 5, 6, 8, 10, 12])
    parser.add_argument("--size", type=int, default=48)
    parser.add_argument("--carrier-modes", type=int, default=0,
                        help="use this many envelope modes for cos/sin carriers")
    parser.add_argument("--zero-cutoff", type=float, default=300)
    parser.add_argument("--dps", type=int, default=40)
    parser.add_argument("--robustness", action="store_true",
                        help="compare sampled sign thresholds by cutoff and carrier size")
    parser.add_argument("--robust-cutoffs", nargs="+", type=float,
                        default=[180, 300])
    parser.add_argument("--robust-modes", nargs="+", type=int,
                        default=[6, 8])
    parser.add_argument("--threshold-supports", nargs="+", type=float,
                        default=[8, 8.5, 9, 9.5, 10, 10.5, 11])
    args = parser.parse_args()

    mp.mp.dps = args.dps
    max_cutoff = max(args.robust_cutoffs) if args.robustness else args.zero_cutoff
    all_zeros = true_zeros_to_cutoff(max_cutoff)
    zeros = [g for g in all_zeros if g <= args.zero_cutoff]
    print("ASSUMPTION: synthetic truncated hybrid zero set; this is not zeta evidence.")
    print("NORMALIZATION: quartet sum = 4 Re(F(delta+i*gamma) F(-delta-i*gamma)).")
    print("LIMITATION: omitted on-line tail is positive; thresholds are lower-bound calibration only.")
    if args.robustness:
        print("cutoff  online  envelope  sampled first negative       value")
        for cutoff in args.robust_cutoffs:
            cutoff_zeros = [g for g in all_zeros if g <= cutoff]
            for modes in args.robust_modes:
                threshold, value = first_negative_carrier(
                    args.threshold_supports, modes, args.gamma, cutoff_zeros,
                    args.delta, args.dps)
                shown = ">" + str(max(args.threshold_supports)) if threshold is None else f"{threshold:g}"
                print(f"{cutoff:6.0f} {len(cutoff_zeros):7d} {modes:9d} "
                      f"{shown:>22} {value:12.5g}")
        return
    print("L      m  online       min(background)    min(+quartet)")
    for L in args.supports:
        if args.carrier_modes:
            G, background, quartet = carrier_matrices(
                L, args.carrier_modes, args.gamma, zeros, args.delta, args.dps)
            base_min = generalized_min(background, G)
            injected_min = generalized_min(background + quartet, G)
            shown_size = 2 * args.carrier_modes
        else:
            background = frame_form(zeros, L, args.size, dps=args.dps)
            quartet = quartet_matrix(L, args.size, args.delta, args.gamma, args.dps)
            base_min = spectral_lam_min(background, nev=1, dps=args.dps)[0]
            injected_min = spectral_lam_min(background + quartet, nev=1,
                                            dps=args.dps)[0]
            shown_size = args.size
        print(f"{L:5.2f} {shown_size:3d} {len(zeros):7d}  "
              f"{mp.nstr(base_min, 9):>16}  {mp.nstr(injected_min, 9):>16}")


if __name__ == "__main__":
    main()
