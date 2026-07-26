"""run_smoothlaw.py — RUN 1: the smooth-staircase law on a fine L-grid.

Purpose: the envelope law was fit on 5 prime windows of the TRUE form; the
model-zeros experiment showed the smooth staircase reproduces it.  Here we
map lambda_min(L) for the smooth staircase itself over a fine L-grid with
m- and Gcut-escalation, to (i) refit (b, c0) in
ln lam = A - b e^{L/2}(L/2 + c0) for the pure-density model, and (ii) give
the derivation a clean target with stated convergence bars.

Gcut semantics: lam rises with Gcut toward the infinite-frame value (lower
bounds).  m semantics: lam falls with m (Rayleigh-Ritz upper bounds at fixed
Gcut).  The pair of escalations brackets the drift.
"""
import mpmath as mp
from law_core import staircase_zeros
from runs import record

mp.mp.dps = 50

OUT = "smoothlaw.jsonl"
ZS = staircase_zeros(2900, gmax=3400)
print("zeros ready: K=%d up to %.1f" % (len(ZS), float(ZS[-1])), flush=True)

LGRID = [2.2, 2.35, 2.5, 2.65, 2.8, 2.95, 3.1, 3.25, 3.4]

for L in LGRID:
    for (m, gcut, dps) in ((48, 840, 50), (64, 840, 50), (64, 1680, 55),
                           (48, 1680, 50), (64, 3360, 55)):
        gs = [g for g in ZS if g <= gcut]
        record(OUT, "smooth", gs, L, m, dps=dps,
               extra={"Gcut": gcut, "alpha": 1.0, "beta": 1.0})
print("RUN 1 done", flush=True)
