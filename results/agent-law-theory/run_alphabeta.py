"""run_alphabeta.py — RUN 3: two-parameter staircases
N_{alpha,beta}(T) = alpha (T/2pi) ln(T/(2 pi beta e)) + 7/8.

alpha scales the density, beta the height scale; (1,1) is the smooth model
that reproduces the true-zero envelope.  The partial derivatives
d ln lam / d alpha and d ln lam / d beta at fixed L discriminate candidate
functionals E[N; a] sharply (see theory.py / report).

Also V4: the exact dilation identity lam_{a, beta*Gamma} = (1/beta) *
lam_{beta*a, Gamma} (change of variables), checked on dilated TRUE staircase
zeros — a pipeline consistency test independent of any model.
"""
import mpmath as mp
from law_core import staircase_zeros
from runs import record
from law_core import lam_min_frame

mp.mp.dps = 50
OUT = "alphabeta.jsonl"

ALPHAS = ['0.85', '0.925', '1', '1.075', '1.15']
BETAS = ['0.75', '0.875', '1.125', '1.25']
LS = [2.485, 2.996]

for L in LS:
    for al in ALPHAS:
        ZS = staircase_zeros(2400, alpha=al, beta='1', gmax=1700)
        for (m, gcut) in ((48, 420), (64, 420), (48, 840), (64, 840),
                          (64, 1680)):
            gs = [g for g in ZS if g <= gcut]
            record(OUT, "stair", gs, L, m, dps=52,
                   extra={"Gcut": gcut, "alpha": float(al), "beta": 1.0})
    for be in BETAS:
        ZS = staircase_zeros(2400, alpha='1', beta=be, gmax=900)
        for (m, gcut) in ((48, 420), (64, 420), (48, 840), (64, 840)):
            gs = [g for g in ZS if g <= gcut]
            record(OUT, "stair", gs, L, m, dps=52,
                   extra={"Gcut": gcut, "alpha": 1.0, "beta": float(be)})

# ---- V4: exact dilation identity (no staircase regeneration: dilate by hand)
print("V4 dilation identity check", flush=True)
be = mp.mpf('1.2')
Z0 = staircase_zeros(1400, gmax=1100)
g840 = [g for g in Z0 if g <= 840]
lam_R = lam_min_frame(g840, 1.2 * 2.485, 48, dps=52)[0]          # lam_{beta a, Gamma}
gd = [be * g for g in Z0 if be * g <= be * 840]                   # beta*Gamma, cut beta*840
lam_L = lam_min_frame(gd, 2.485, 48, dps=52)[0]                   # lam_{a, beta Gamma}
print("V4: lam_L = %s ; lam_R/beta = %s ; ratio-1 = %s"
      % (mp.nstr(lam_L, 10), mp.nstr(lam_R / be, 10),
         mp.nstr(lam_L * be / lam_R - 1, 3)), flush=True)
print("RUN 3 done", flush=True)
