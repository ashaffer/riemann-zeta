"""worth_weighted_check.py — first-order worth-weighted discrepancy vs the
RECORDED true/smooth/poisson frame offsets. No eigensolves.

PREDICTION (logged before running, derived from the 12-seed GUE mechanism
result sign(Delta) = sign(band dN) in 11/12 and the marginal law):

  Delta(L) := ln lam[model] - ln lam[smooth]  should be approximated at first
  order by the worth-weighted net discrepancy

    I_w(L) = (pi^2/2) * INT_{t0}^{e T*} DN(t) dt/t,
    DN(t) = #{model levels <= t} - #{smooth levels <= t},  T* = 2 pi e^{L/2},

  (integration by parts of the marginal law w(t) = (pi^2/2) ln(eT*/t);
  deleting a level LOWERS the frame form, so a surplus raises it).

Recorded offsets (RESULTS.md, Gcut = 420, m = 48):
  L = 2.485: true - smooth = ln(2.68972/2.75124) = -0.023
  L = 2.996: true - smooth = ln(2.71352/3.17610) = -0.157
  L = 3.555: true - smooth = ln(9.90930/1.57685e) = +1.838   (the Q3 anomaly)
  poisson (seed 7): -4.554 / -4.672 / -0.566 at the three L.

Pre-registered success criterion for THIS script: sign match for the two
non-negligible true-vs-smooth offsets (L = 2.996, 3.555) and |I_w| within a
factor of 3 of the measured offset at L = 3.555; for the Poisson seed, I_w
strongly negative at the two shallower L. If I_w at L = 3.555 is positive and
O(1-2) nats, Q3's factor 6.3 is explained as a REAL worth-weighted
S(T)-fluctuation, not Gcut truncation.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "src"))
import numpy as np
import mpmath as mp
from model_zeros import smooth_zeros, poisson_zeros

mp.mp.dps = 30
K = 180


def iw(levels, sm, L, npts=4000):
    Tstar = float(2 * mp.pi) * np.exp(L / 2)
    hi = np.e * Tstar
    lo = min(levels[0], sm[0]) * 0.999
    ts = np.exp(np.linspace(np.log(lo), np.log(hi), npts))
    lv = np.asarray(levels)
    s = np.asarray(sm)
    dn = np.searchsorted(lv, ts, side='right') - \
         np.searchsorted(s, ts, side='right')
    # integrate DN(t) dt/t = DN d(ln t), trapezoid in ln t
    return (np.pi ** 2 / 2) * np.trapz(dn, np.log(ts))


if __name__ == "__main__":
    sm = [float(g) for g in smooth_zeros(K)]
    true = []
    k = 1
    while len(true) < K:
        true.append(float(mp.zetazero(k).imag))
        k += 1
    po = [float(g) for g in poisson_zeros(K, seed=7)]
    rec = {2.485: (-0.023, -4.554), 2.996: (-0.157, -4.672),
           3.555: (+1.838, -0.566)}
    for L in (2.485, 2.996, 3.555):
        it = iw(true, sm, L)
        ip = iw(po, sm, L)
        print("L=%.3f: I_w(true) = %+0.3f vs measured %+0.3f | "
              "I_w(poisson s7) = %+0.3f vs measured %+0.3f"
              % (L, it, rec[L][0], ip, rec[L][1]), flush=True)
