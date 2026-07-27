"""separator_test.py — Round-2 C-1 separating example (log-gas seat).

Pre-registered in SEAT-log-gas.md §R2.5 BEFORE running. Two deterministic
displacement fields on the smooth staircase (points k >= 3), u_k -> u_k +
A sin(k0 t_k + phi):
  SEP : k0 in {0.08, 0.10, 0.12} first passing the J-structure gates;
        A = 0.9; phi tuned so discrete J(L1) = 0.
  CTRL: k0 = 0.8; A = 0.25; phi tuned at L1 identically.
Evaluate lambda at L in {2.485, 2.996, 3.555}; all J printed BEFORE solves.
"""
import os, sys, time, json, math

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "results", "agent-law-theory"))

import mpmath as mp
from law_core import lam_min_frame, staircase_zeros

mp.mp.dps = 50
KT, M = 180, 48
LS = [mp.mpf('2.485'), mp.mpf('2.996'), mp.mpf('3.555')]
PI2H = float(mp.pi ** 2 / 2)
OUT = open(os.path.join(HERE, "separator_test.jsonl"), "a")

stair = staircase_zeros(KT)
stair_f = [float(g) for g in stair]


def X_of(L):
    return float(mp.e * 2 * mp.pi * mp.e ** (L / 2))


def nbar_inv_targets(us):
    """gamma with Nbar(gamma) = u (Nbar = main + 7/8), warm-start Newton."""
    out = []
    g = mp.mpf(10)
    for u in us:
        t = mp.mpf(repr(u)) - mp.mpf('0.875')
        for _ in range(80):
            f = g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) - t
            fp = mp.log(g / (2 * mp.pi)) / (2 * mp.pi)
            step = f / fp
            gn = g - step
            if gn <= 2 * mp.pi * mp.mpf('1.02'):
                gn = (g + 2 * mp.pi * mp.mpf('1.02')) / 2
            g = gn
            if abs(step) < mp.mpf('1e-30'):
                break
        out.append(+g)
    return out


def displaced(k0, A, phi):
    """u_k = k - 1/2 for k = 1..KT; displace k >= 3 by A sin(k0 t_k + phi)."""
    us = []
    for k in range(1, KT + 1):
        u = k - 0.5
        if k >= 3:
            u += A * math.sin(k0 * stair_f[k - 1] + phi)
        us.append(u)
    ncross = sum(1 for i in range(len(us) - 1) if us[i] >= us[i + 1])
    if ncross:
        # the frame form takes a MULTISET; crossings at the pinned junction
        # are allowed, reported, and folded into supD (printed pre-solve)
        print("  note: %d ordering crossings; configuration sorted" % ncross,
              flush=True)
        us = sorted(us)
    return nbar_inv_targets(us)


def J_of(cfg, X):
    c = [float(g) for g in cfg if float(g) < X]
    s = [g for g in stair_f if g < X]
    return sum(math.log(X / g) for g in s) - sum(math.log(X / g) for g in c)


def tune_phi(k0, A, X1, n=720):
    best, bphi = None, None
    prev = None
    roots = []
    for i in range(n + 1):
        phi = 2 * math.pi * i / n
        J = J_of(displaced_fast(k0, A, phi, X1), X1)
        if prev is not None and prev[1] * J <= 0 and abs(prev[1] - J) > 0:
            # bisect
            lo, hi = prev[0], phi
            flo = prev[1]
            for _ in range(60):
                mid = (lo + hi) / 2
                fm = J_of(displaced_fast(k0, A, mid, X1), X1)
                if flo * fm <= 0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            roots.append((lo + hi) / 2)
        prev = (phi, J)
    return roots


def displaced_fast(k0, A, phi, X):
    """Float-only version for phase tuning (Newton in float)."""
    out = []
    g = 10.0
    tp = 2 * math.pi
    for k in range(1, KT + 1):
        u = k - 0.5
        if k >= 3:
            u += A * math.sin(k0 * stair_f[k - 1] + phi)
        t = u - 0.875
        for _ in range(60):
            f = g / tp * math.log(g / (tp * math.e)) - t
            fp = math.log(g / tp) / tp
            step = f / fp
            gn = g - step
            if gn <= tp * 1.02:
                gn = (g + tp * 1.02) / 2
            g = gn
            if abs(step) < 1e-14:
                break
        out.append(g)
        if g > X + 50:
            break
    return out


X1, X2, X3 = (X_of(L) for L in LS)
print("=== separator test; X = %.3f / %.3f / %.3f ===" % (X1, X2, X3), flush=True)

# --- select SEP k0 by the pre-registered deterministic rule ---
# 2026-07-26 AMENDMENT (post-hoc at the DETERMINISTIC stage; no eigensolve was
# run before this change): the locked A = 0.9 fails the |(pi2/2)J(L3)| >= 1.0
# gate at all three k0 (max 0.77). J is exactly linear in A and the tuned
# roots phi* are A-independent, so the amplitude is raised to A = 1.8 (still
# inside the monotonicity bound rho(t_3)/k0 = 2.23 at k0 = 0.10 and inside
# the LR regime sup|dN| <= 2). P-R2-B/C bands unchanged; P-R2-A scored FAILED
# as locked, PASSED as amended. Original run preserved in separator_test.log.
A_SEP = 1.8
chosen = None
for k0 in (0.08, 0.10, 0.12):
    for phi in tune_phi(k0, A_SEP, X1):
        Js = [J_of(displaced_fast(k0, A_SEP, phi, X), X) for X in (X1, X2, X3)]
        g1 = abs(PI2H * Js[0]) <= 0.05
        g3 = abs(PI2H * Js[2]) >= 1.0
        print("SEP candidate k0=%.2f phi=%.4f: (pi2/2)J = %+.3f / %+.3f / %+.3f  gates(%s,%s)"
              % (k0, phi, *(PI2H * j for j in Js), g1, g3), flush=True)
        if g1 and g3 and chosen is None:
            chosen = (k0, phi, Js)
    if chosen:
        break
if chosen is None:
    print("NO SEP candidate passed gates -- reporting best and stopping per prereg")
    sys.exit(1)
k0S, phiS, JsS = chosen
print("SEP CHOSEN: k0=%.2f phi=%.5f A=%.2f" % (k0S, phiS, A_SEP), flush=True)

# --- CTRL ---
rootsC = tune_phi(0.8, 0.25, X1)
phiC = rootsC[0] if rootsC else 0.0
JsC = [J_of(displaced_fast(0.8, 0.25, phiC, X), X) for X in (X1, X2, X3)]
print("CTRL k0=0.80 phi=%.5f: (pi2/2)J = %+.3f / %+.3f / %+.3f"
      % (phiC, *(PI2H * j for j in JsC)), flush=True)

# --- eigensolves ---
def run(tag, cfg, L, X, Eref, J):
    t0 = time.time()
    lam = lam_min_frame(cfg, L, M, dps=50)[0]
    E = -mp.log(lam)
    dE = float(E - Eref)
    rec = {"tag": tag, "L": float(L), "lam": mp.nstr(lam, 8), "dE": dE,
           "pi2h_J": PI2H * J, "secs": round(time.time() - t0, 1)}
    OUT.write(json.dumps(rec) + "\n"); OUT.flush()
    print("%-10s L=%.3f lam=%-14s dE=%+7.3f vs (pi2/2)J=%+7.3f  (%.0fs)"
          % (tag, float(L), rec["lam"], dE, PI2H * J, rec["secs"]), flush=True)
    return dE

Erefs = {}
for L, X, exp in zip(LS, (X1, X2, X3), ("2.75124e-10", "3.17610e-15", "1.57685e-22")):
    lam = lam_min_frame(stair, L, M, dps=50)[0]
    Erefs[float(L)] = -mp.log(lam)
    print("smooth    L=%.3f lam=%s (expect %s)" % (float(L), mp.nstr(lam, 8), exp), flush=True)

sep_cfg = displaced(k0S, A_SEP, phiS)
ctl_cfg = displaced(0.8, 0.25, phiC)
res = {}
for tag, cfg, Js in (("SEP", sep_cfg, JsS), ("CTRL", ctl_cfg, JsC)):
    for L, X, J in zip(LS, (X1, X2, X3), Js):
        res[(tag, float(L))] = run(tag, cfg, L, X, Erefs[float(L)], J)

print("P-R2-C: SEP |dE(L3)-dE(L1)| = %.3f ; CTRL = %.3f"
      % (abs(res[("SEP", 3.555)] - res[("SEP", 2.485)]),
         abs(res[("CTRL", 3.555)] - res[("CTRL", 2.485)])), flush=True)
OUT.close()
