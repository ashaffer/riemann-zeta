"""fit3.py — the joint global fit of the identified functional

  E(a, alpha, beta) = -A + b * beta * e^{2a/alpha} * (2a + c0 * alpha)
                    = -A + b * [ N(T*) + (c0+1) * D(T*) ] + b*7/8-abs.,

on (i) RUN 1 L-grid (Gcut-extrapolated, m=64), (ii) RUN 3 alpha-grid
(deepest Gcut), (iii) RUN 3 beta-grid, and — separately — (iv) the repo's
TRUE-form five-window ladder (results/RESULTS.md).  Plus the Fuchs
concentration-model exponents for the failure exhibit.
"""
import json, os, math
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def load(name):
    with open(os.path.join(DATA, name)) as f:
        return [json.loads(l) for l in f if l.strip()]


# ---------- assemble data points (E, a, alpha, beta) ----------
pts = []
rs = load("smoothlaw.jsonl")
grid = {(r["L"], r["m"], r["Gcut"]): r["lnlam"] for r in rs}
for L in sorted({r["L"] for r in rs}):
    e1, e2, e3 = (-grid[(L, 64, 840)], -grid[(L, 64, 1680)],
                  -grid[(L, 64, 3360)])
    q = (e2 - e3) / (e1 - e2)
    pts.append((e3 - (e2 - e3) * q / (1 - q), L / 4, 1.0, 1.0, "Lgrid"))

ab = load("alphabeta.jsonl")
seen = {}
for r in ab:
    k = (r["L"], r["alpha"], r["beta"])
    # keep deepest (largest Gcut, then largest m)
    if k not in seen or (r["Gcut"], r["m"]) > (seen[k]["Gcut"], seen[k]["m"]):
        seen[k] = r
for (L, al, be), r in sorted(seen.items()):
    if (al, be) == (1.0, 1.0):
        continue
    # Gcut-drift correction: baseline drift 840->inf is ~ -0.03 in E;
    # apply none (report raw); deepest available Gcut used.
    pts.append((-r["lnlam"], L / 4, al, be, "ab(Gc%d)" % r["Gcut"]))

print("=== joint fit over %d points: E = -A + b beta e^{2a/alpha} "
      "(2a + c0 alpha) ===" % len(pts))
best = None
for c0 in np.arange(3.0, 7.0, 0.005):
    X = np.vstack([-np.ones(len(pts)),
                   [be * math.exp(2 * a / al) * (2 * a + c0 * al)
                    for (E, a, al, be, tag) in pts]]).T
    y = np.array([p[0] for p in pts])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    rms = float(np.sqrt(np.mean((X @ coef - y) ** 2)))
    if best is None or rms < best[3]:
        best = (float(coef[0]), float(coef[1]), float(c0), rms)
A, b, c0, rms = best
print("  A = %.3f   b = %.4f   c0 = %.3f   rms = %.3f  (E range %.1f..%.1f)"
      % (A, b, c0, rms, min(p[0] for p in pts), max(p[0] for p in pts)))
print("  equivalently E = -A + b[N(T*) + mu D(T*)], mu = c0+1 = %.3f" % (c0 + 1))
print("  residual table:")
for (E, a, al, be, tag) in pts:
    pred = -A + b * be * math.exp(2 * a / al) * (2 * a + c0 * al)
    print("    L=%.3f al=%.3g be=%.3g  E=%7.3f pred=%7.3f res=%+.3f  [%s]"
          % (4 * a, al, be, E, pred, pred - E, tag))

# leave-one-block-out sensitivity: fit on Lgrid only vs ab only
for name, sub in (("Lgrid-only", [p for p in pts if p[4] == "Lgrid"]),
                  ("ab-only", [p for p in pts if p[4] != "Lgrid"])):
    bb = None
    for c0s in np.arange(3.0, 7.0, 0.01):
        X = np.vstack([-np.ones(len(sub)),
                       [be * math.exp(2 * a / al) * (2 * a + c0s * al)
                        for (E, a, al, be, tag) in sub]]).T
        y = np.array([p[0] for p in sub])
        coef, *_ = np.linalg.lstsq(X, y, rcond=None)
        r = float(np.sqrt(np.mean((X @ coef - y) ** 2)))
        if bb is None or r < bb[3]:
            bb = (float(coef[0]), float(coef[1]), float(c0s), r)
    print("  [%s] A=%.3f b=%.4f c0=%.3f rms=%.3f" % ((name,) + bb[:3] + (bb[3],)))

# ---------- the TRUE-form five-window ladder (repo RESULTS.md) ----------
print("\n=== TRUE zeta form, five windows (repo operator estimates) ===")
true_pts = [(1.75, 3.13e-5), (2.485, 3.50e-10), (2.996, 4.2e-15),
            (3.555, 2.1e-22), (4.025, 1.5e-30)]
for c0f, tag in ((c0, "c0 from joint fit"), (4.0, "c0=4.0 (repo)"),):
    X = np.vstack([-np.ones(len(true_pts)),
                   [math.exp(L / 2) * (L / 2 + c0f) for (L, lam) in true_pts]]).T
    y = np.array([-math.log(lam) for (L, lam) in true_pts])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = float(np.sqrt(np.mean((X @ coef - y) ** 2)))
    print("  [%s] A=%.3f b=%.4f rms=%.3f" % (tag, coef[0], coef[1], r))
    for (L, lam), pr in zip(true_pts, X @ coef):
        print("     L=%.3f E=%.3f pred=%.3f res=%+.3f"
              % (L, -math.log(lam), pr, pr + math.log(lam)))

# ---------- Fuchs concentration model (failure exhibit) ----------
print("\n=== Fuchs/concentration model E (no free constants) ===")
import mpmath as mp
import sys
sys.path.insert(0, HERE)
from theory import E_fuchs
mp.mp.dps = 30
for L in (2.2, 2.485, 2.996, 3.4):
    a = mp.mpf(L) / 4
    E, T, k = E_fuchs(a)
    print("  L=%.3f: E_Fuchs = %.2f at T=%.1f (k=%d zeros vanished)  "
          "vs measured %.2f"
          % (L, float(E), float(T), k,
             dict((round(4 * p[1], 3), p[0]) for p in pts
                  if p[4] == "Lgrid").get(round(L, 3), float('nan'))))
