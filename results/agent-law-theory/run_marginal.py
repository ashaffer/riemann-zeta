"""run_marginal.py — RUN 4: the marginal worth of a single zero.

Delete ONE zero gamma_j from the smooth staircase (everything else fixed:
same L, m, Gcut) and measure Delta E(gamma_j) = ln lam(without) - ln lam(with)
... sign convention: deleting a positive rank-one can only DECREASE lam, so
Delta E := ln lam(full) - ln lam(minus j) >= 0 is the exponent-worth of that
single zero.  Sweeping j maps the per-zero cost profile f(t) directly --
the sharpest discriminator between candidate functionals E[N]:
  - constant toll per zero below a cutoff  -> f flat then 0;
  - edge-dominated (cost near T*)          -> f peaked at T* = 2 pi e^{L/2};
  - cost decaying with height              -> f decreasing.
Insertion of one extra zero at a gap midpoint measures the same derivative
with opposite sign (and tests additivity).
"""
import mpmath as mp
from law_core import staircase_zeros
from runs import record

mp.mp.dps = 50
OUT = "marginal.jsonl"

ZS = staircase_zeros(1400, gmax=1700)

REM = [1, 2, 3, 5, 8, 12, 20, 35, 60, 100, 170, 300, 450]   # 1-based indices
INS = [1, 5, 20, 100]

for L in (2.485, 2.996):
    for (m, gcut) in ((48, 840), (64, 840), (48, 1680)):
        gs = [g for g in ZS if g <= gcut]
        record(OUT, "base", gs, L, m, dps=52, extra={"Gcut": gcut})
        for j in REM:
            if j > len(gs):
                continue
            g2 = gs[:j - 1] + gs[j:]
            record(OUT, "rm", g2, L, m, dps=52,
                   extra={"Gcut": gcut, "j": j, "gj": float(gs[j - 1])})
        if (m, gcut) == (48, 840):
            for j in INS:
                mid = (gs[j - 1] + gs[j]) / 2
                g2 = gs[:j] + [mid] + gs[j:]
                record(OUT, "ins", g2, L, m, dps=52,
                       extra={"Gcut": gcut, "j": j, "gmid": float(mid)})
print("RUN 4 done", flush=True)
