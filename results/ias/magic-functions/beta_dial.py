"""beta_dial.py — SEAT-magic-functions §5 pre-registered test.

Phase family of the smooth staircase: t_k(beta) solves N_hat(t_k) = k - beta.
beta = 1/2 is the program's staircase. Frame form of the first K = 180 nodes
(matching the cached true-zero list length and the model_zeros convention),
L = 2.485, Legendre m = 24, dps 40. Predictions P1-P4 pre-registered in
results/ias/SEAT-magic-functions.md BEFORE this run.
"""
import sys, time, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
import mpmath as mp
from model_zeros import frame_form
from spectral_margins import spectral_lam_min

mp.mp.dps = 40
K = 180
L = 2.485
M = 24

def staircase_beta(K, beta):
    out = []
    g = mp.mpf(14)
    for k in range(1, K + 1):
        target = k - mp.mpf(beta) - mp.mpf('0.875')
        for _ in range(60):
            f = g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) - target
            fp = mp.log(g / (2 * mp.pi)) / (2 * mp.pi)
            step = f / fp
            g = g - step
            if abs(step) < mp.mpf('1e-30'):
                break
        out.append(+g)
        g = g + 2 * mp.pi / mp.log(g / (2 * mp.pi))
    return out

true_zeros = []
zf = os.path.join(os.path.dirname(__file__), "..", "..", "agent-law-theory", "data", "zeta_zeros.txt")
with open(zf) as fh:
    for line in fh:
        line = line.strip()
        if line:
            true_zeros.append(mp.mpf(line))
assert len(true_zeros) == K
print("# L=%.3f m=%d K=%d (t_K ranges ~364; no Gcut filter needed)" % (L, M, K), flush=True)

def run(tag, gs):
    t0 = time.time()
    Q = frame_form(gs, L, M, dps=40)
    lam = spectral_lam_min(Q, nev=1, dps=35)[0]
    print("%-10s t1=%-12s lam=%s   (%.0fs)" % (tag, mp.nstr(gs[0], 8), mp.nstr(lam, 8), time.time() - t0), flush=True)
    return lam

results = {}
for beta in ('0.10', '0.25', '0.40', '0.50', '0.60', '0.75', '0.90'):
    gs = staircase_beta(K, mp.mpf(beta))
    results[beta] = run("beta=" + beta, gs)
results['true'] = run("true", true_zeros)

lams = {b: results[b] for b in results if b != 'true'}
mx = max(lams, key=lambda b: lams[b]); mn = min(lams, key=lambda b: lams[b])
print("\n# max at beta=%s (%s); min at beta=%s (%s); ratio %.2f" % (
    mx, mp.nstr(lams[mx], 6), mn, mp.nstr(lams[mn], 6), float(lams[mx] / lams[mn])), flush=True)
print("# lam(beta*)/lam(0.5) = %.3f" % float(lams[mx] / lams['0.50']), flush=True)
print("# true inside family range: %s (true=%s)" % (
    lams[mn] <= results['true'] <= lams[mx], mp.nstr(results['true'], 6)), flush=True)
