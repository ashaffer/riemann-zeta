"""analysis2.py — final identification: fit the DISCRETE functional
E_total(L) = -A + c * SUM_j ln(kappa T* / gamma_j)_+  (T* = 2 pi e^{L/2})
to the RUN 1 grid; test the marginal profile against (pi^2/2) ln(eT*/t);
compute alpha/beta slopes and the candidate table on discrete sums.
"""
import json, os, math
import numpy as np
import mpmath as mp
from law_core import staircase_zeros

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
mp.mp.dps = 30


def load(name):
    with open(os.path.join(DATA, name)) as f:
        return [json.loads(l) for l in f if l.strip()]


ZS11 = [float(g) for g in staircase_zeros(600, gmax=3500)]


def Ssum(L, kappa, zs=None, alpha=1.0):
    """SUM_j ln(kappa * T*_alpha / gamma_j)_+ over staircase zeros."""
    zs = zs if zs is not None else ZS11
    Tk = kappa * 2 * math.pi * math.exp(2 * (L / 4) / alpha)
    return sum(math.log(Tk / g) for g in zs if g < Tk)


# ---------- 1. discrete refit of RUN 1 ----------
rs = load("smoothlaw.jsonl")
grid = {(r["L"], r["m"], r["Gcut"]): r["lnlam"] for r in rs}
Ls = sorted({r["L"] for r in rs})
# Gcut-extrapolated E (m=64):
Einf = {}
for L in Ls:
    e1, e2, e3 = (-grid[(L, 64, 840)], -grid[(L, 64, 1680)],
                  -grid[(L, 64, 3360)])
    q = (e2 - e3) / (e1 - e2)
    Einf[L] = e3 - (e2 - e3) * q / (1 - q)

print("=== 1. RUN 1 discrete-functional refit: "
      "E = -A + c * SUM_j ln(kappa T*/gamma_j)_+ ===")
best = None
for kap in np.arange(1.0, 8.0, 0.01):
    X = np.vstack([np.ones(len(Ls)), [Ssum(L, kap) for L in Ls]]).T
    y = np.array([Einf[L] for L in Ls])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    rms = float(np.sqrt(np.mean((X @ coef - y) ** 2)))
    if best is None or rms < best[3]:
        best = (float(coef[0]), float(coef[1]), float(kap), rms)
negA, c, kap, rms = best
print("  best: E = %.3f + %.4f * S(L, kappa=%.2f)   rms=%.4f"
      % (negA, c, kap, rms))
print("  [compare: c vs pi^2/2 = %.4f ; kappa vs e = %.4f]"
      % (math.pi ** 2 / 2, math.e))
print("  per-L residuals:")
for L in Ls:
    pred = negA + c * Ssum(L, kap)
    print("    L=%.3g  E=%.3f  pred=%.3f  resid=%+.3f"
          % (L, Einf[L], pred, pred - Einf[L]))

# fixed-constant variant: c = pi^2/2, kappa = e: fit only A
X1 = np.array([Ssum(L, math.e) for L in Ls])
y = np.array([Einf[L] for L in Ls])
c0 = math.pi ** 2 / 2
A1 = float(np.mean(y - c0 * X1))
rms1 = float(np.sqrt(np.mean((A1 + c0 * X1 - y) ** 2)))
print("  pinned (c=pi^2/2, kappa=e): E = %.3f + 4.9348*S(L,e)  rms=%.3f"
      % (A1, rms1))

# ---------- 2. marginal profile vs (pi^2/2) ln(eT*/t) ----------
print("\n=== 2. marginal profile f(gamma_j) vs (pi^2/2) ln(e T*/gamma_j) ===")
rm = load("marginal.jsonl")
for L in (2.485, 2.996):
    Ts = 2 * math.pi * math.exp(L / 2)
    base = {(r["m"], r["Gcut"]): r["lnlam"] for r in rm
            if r["tag"] == "base" and r["L"] == L}
    print("L = %.3f  (e*T* = %.1f)" % (L, math.e * Ts))
    print("| gamma_j | u=gamma/T* | dE meas (m64) | (pi^2/2)ln(eT*/g) | ratio |")
    print("|---|---|---|---|---|")
    for r in sorted([r for r in rm if r["tag"] == "rm" and r["L"] == L
                     and r["m"] == 64], key=lambda r: r["j"]):
        dE = base[(64, r["Gcut"])] - r["lnlam"]
        pred = (math.pi ** 2 / 2) * math.log(math.e * Ts / r["gj"])
        if pred > 0:
            print("| %.1f | %.3f | %.3f | %.3f | %.3f |"
                  % (r["gj"], r["gj"] / Ts, dE, pred,
                     dE / pred if abs(pred) > 1e-9 else float('nan')))
        else:
            print("| %.1f | %.3f | %.3f | (past eT*) | -- |" %
                  (r["gj"], r["gj"] / Ts, dE))
    # additivity
    tot = sum(base[(64, 840)] - r["lnlam"] for r in rm
              if r["tag"] == "rm" and r["L"] == L and r["m"] == 64
              and r["Gcut"] == 840)
    print("  sum of measured marginals (13 zeros) = %.2f vs "
          "E_total(Gc840,m64) = %.2f" % (tot, -base[(64, 840)]))

# ---------- 3. alpha/beta slopes + candidates ----------
print("\n=== 3. alpha/beta discrimination ===")
ab = load("alphabeta.jsonl")
for L in (2.485, 2.996):
    a = L / 4
    sel = {(r["alpha"], r["beta"], r["m"], r["Gcut"]): -r["lnlam"]
           for r in ab if r["L"] == L}
    E1 = sel.get((1.0, 1.0, 64, 840))
    print("\nL = %.3f (a=%.5f): E(1,1) = %.3f  [m=64 Gc=840]" % (L, a, E1))
    # measured slopes (central where available)
    for (m, gc) in ((48, 840), (64, 840)):
        try:
            dEda = (sel[(1.075, 1.0, m, gc)] - sel[(0.925, 1.0, m, gc)]) / 0.15
            dEdb = (sel[(1.0, 1.125, m, gc)] - sel[(1.0, 0.875, m, gc)]) / 0.25
            print("  measured dE/dalpha = %.2f   dE/dbeta = %.2f   (m=%d,Gc=%d)"
                  % (dEda, dEdb, m, gc))
        except KeyError:
            pass
    # candidate slopes via discrete sums (marginal functional, and C1/C3/C5)
    # marginal functional S_marg(alpha) = SUM ln(e*T*_alpha / gamma_j^alpha)_+
    dal = 0.075
    vals = {}
    for alp in (0.925, 1.0, 1.075):
        zs = [float(g) for g in staircase_zeros(400, alpha=str(alp),
                                                gmax=400)]
        vals[alp] = Ssum(L, math.e, zs=zs, alpha=alp)
    dSda = (vals[1.075] - vals[0.925]) / 0.15
    print("  marginal-functional: S(e) = %.3f, dS/dalpha = %.3f "
          "-> pred dE/dalpha at c=pi^2/2: %.2f"
          % (vals[1.0], dSda, (math.pi ** 2 / 2) * dSda))
    # C5: N(Tcap): 2a beta e^{2a/alpha+1}+7/8
    NE = lambda alp: 2 * a * math.exp(2 * a / alp + 1) + 0.875
    bC5 = (E1 + 11.13) / NE(1.0)
    print("  C5 (b*N(eT*), b=%.2f): pred dE/dalpha = %.2f"
          % (bC5, bC5 * (NE(1.075) - NE(0.925)) / 0.15))
    # C1: N(T*)
    NT = lambda alp: math.exp(2 * a / alp) * (2 * a - alp) + 0.875
    bC1 = (E1 + 11.13) / NT(1.0)
    print("  C1 (b*N(T*), b=%.2f): pred dE/dalpha = %.2f"
          % (bC1, bC1 * (NT(1.075) - NT(0.925)) / 0.15))
    # C3: area: alpha beta e^{2a/alpha}
    AR = lambda alp: alp * math.exp(2 * a / alp)
    bC3 = (E1 + 11.13) / AR(1.0)
    print("  C3 (b*area, b=%.2f): pred dE/dalpha = %.2f"
          % (bC3, bC3 * (AR(1.075) - AR(0.925)) / 0.15))
    # beta prediction for all linear-in-beta candidates: dE/dbeta = E + A
    print("  all-beta-linear candidates: pred dE/dbeta = E(1,1)+A = %.2f "
          "(A=11.13 from RUN 1 refit)" % (E1 + 11.13))

# ---------- 4. beta-linearity exhibit ----------
print("\n=== 4. E(beta) linearity ===")
for L in (2.485, 2.996):
    sel = {(r["alpha"], r["beta"]): -r["lnlam"] for r in ab
           if r["L"] == L and r["m"] == 64 and r["Gcut"] == 840}
    row = [(be, sel.get((1.0, be))) for be in (0.75, 0.875, 1.0, 1.125, 1.25)]
    print("L=%.3f: " % L + "  ".join("E(beta=%g)=%.3f" % (b, e)
                                      for b, e in row if e))
