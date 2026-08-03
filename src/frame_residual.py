"""Test a non-circular finite-zero factorization of the arithmetic Weil form.

For verified critical-line ordinates gamma <= T, form the positive matrix

    F_T = 2 sum_gamma (v_re v_re^T + v_im v_im^T)

and inspect R_{L,T} = Q_L - F_T, where Q_L is assembled independently from
the pole, digamma, and prime-power terms.  No zero-side identity is assumed:
this is simply subtraction of an explicit positive finite-rank matrix.  A
robust positive residual would suggest the proof strategy
Q_L = F_T + R_{L,T}; a negative residual kills that choice of cutoff/basis.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import mpmath as mp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from model_zeros import frame_form, true_zeros_to_cutoff
from spectral_margins import spectral_form, spectral_lam_min


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[2.485, 2.996, 3.555])
    parser.add_argument("--size", type=int, default=32)
    parser.add_argument("--cutoffs", nargs="+", type=float,
                        default=[40, 80, 120, 180, 300])
    parser.add_argument("--dps", type=int, default=40)
    args = parser.parse_args()

    mp.mp.dps = args.dps
    all_zeros = true_zeros_to_cutoff(max(args.cutoffs))
    print("L      m  cutoff  zeros      min(Q)       min(Q-F_T)    max(F_T)")
    for L in args.supports:
        Q = spectral_form(L, args.size, dps=args.dps)
        qmin = spectral_lam_min(Q, nev=1, dps=args.dps)[0]
        for cutoff in args.cutoffs:
            zeros = [g for g in all_zeros if g <= cutoff]
            F = frame_form(zeros, L, args.size, dps=args.dps)
            R = Q - F
            rmin = spectral_lam_min(R, nev=1, dps=args.dps)[0]
            fmax = max(mp.eigsy(F, eigvals_only=True))
            print(f"{L:5.3f} {args.size:3d} {cutoff:7.1f} {len(zeros):5d}  "
                  f"{mp.nstr(qmin, 7):>12}  {mp.nstr(rmin, 7):>12}  "
                  f"{mp.nstr(fmax, 7):>11}")


if __name__ == "__main__":
    main()
