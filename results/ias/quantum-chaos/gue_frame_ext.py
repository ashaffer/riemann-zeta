"""gue_frame_ext.py — POST-HOC EXTENSION of the pre-registered GUE test.

Labeled post-hoc (written AFTER seeing seeds 1-3 of gue_frame_test.py):
 (a) seeds 4..12 for a stable median (same protocol, more samples);
 (b) diagnostic: standoff-band level-count discrepancy
     dN(T) = #{gue <= T} - #{smooth <= T}, averaged over
     T in {1.0, 1.5, 2.0, 2.5, 3.0} x T*, T* = 2 pi e^{L/4*2}.
Mechanism prediction (logged before running THIS script): the sign of
Delta = ln lam_GUE - ln lam_smooth is OPPOSITE to the band discrepancy
(level deficit in the standoff band => cheaper dodging => Delta > 0);
expected correlation across all 12 seeds: sign agreement >= 9/12.
Seeds 1-3 lam values are reused from the pre-registered run.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "src"))
import numpy as np
import mpmath as mp
from model_zeros import smooth_zeros, frame_form
from spectral_margins import spectral_lam_min
from gue_frame_test import gue_zeros, L, M, K, DPS

mp.mp.dps = DPS
LN_SM = -22.0138          # smooth anchor, validated in the pre-registered run
LN_PO = float(mp.log(mp.mpf('2.89509e-12')))
TSTAR = float(2 * mp.pi * mp.e ** (L / 2))
BAND = [1.0 * TSTAR, 1.5 * TSTAR, 2.0 * TSTAR, 2.5 * TSTAR, 3.0 * TSTAR]

PRIOR = {1: -18.2079, 2: -23.6539, 3: -19.9902}   # ln lam, seeds 1-3 (recorded)

if __name__ == "__main__":
    sm = [float(g) for g in smooth_zeros(K)]
    rows = []
    for seed in range(1, 13):
        gz = gue_zeros(K, seed)
        gzf = [float(g) for g in gz]
        dn = np.mean([sum(g <= T for g in gzf) - sum(s <= T for s in sm)
                      for T in BAND])
        if seed in PRIOR:
            ln_g = PRIOR[seed]
            note = "(reused)"
        else:
            t0 = time.time()
            Q = frame_form(gz, L, M, dps=DPS)
            ln_g = float(mp.log(spectral_lam_min(Q, nev=1)[0]))
            note = "(%.0f s)" % (time.time() - t0)
        d = ln_g - LN_SM
        rows.append((seed, d, dn))
        print("seed %2d: Delta = %+0.3f  band dN = %+0.2f  %s"
              % (seed, d, dn, note), flush=True)
    ds = sorted(r[1] for r in rows)
    med = 0.5 * (ds[5] + ds[6])
    agree = sum(1 for _, d, dn in rows if d * dn < 0 or (dn == 0))
    print("\nn=12: median Delta = %+0.3f | mean = %+0.3f | spread = %0.3f | "
          "min = %+0.3f max = %+0.3f" % (med, np.mean(ds), ds[-1] - ds[0],
                                         ds[0], ds[-1]), flush=True)
    print("sign(Delta) opposite to sign(band dN): %d / 12" % agree, flush=True)
    print("all seeds vs poisson: min dist = %0.2f nats"
          % min(d - (LN_PO - LN_SM) for d in ds), flush=True)
