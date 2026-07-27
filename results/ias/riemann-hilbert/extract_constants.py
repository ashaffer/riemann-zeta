#!/usr/bin/env python3
"""
RH seat cheap test: pinned-action constant extraction on the recorded deep-window
Rayleigh-Ritz ladders (results/agent-deep-windows/runs.csv + agent-deep-windows.md).

NO eigensolves. Pure arithmetic on recorded numbers (< 1 CPU-second).

Model under test (deep / Fuchs-form):  ln lam = A' - 4*pi*e^{l} + p*l,  l = L/2.
Pinned action b' = 4*pi throughout (measured by deep-windows to 0.4-1.3%).

Outputs:
  1. Aitken limits per window from the deepest triples (incl. the rungs that
     landed after the deep-windows report froze: 4.60/160, 5.00/160, 5.50 triple).
  2. A'(p) = ln lam + 4 pi e^l - p*l  per window, for p in {9/2, pi^2/2, 11/2, 6.5}.
     Flatness of A'(p) across L discriminates p; value of A' is the constant.
  3. Free (p, A') least squares with 4pi pinned; sensitivity variants.
  4. Comparator constants: Fuchs n=4 (Connes 2602.04022 par.6.4): 1-chi2 and 1-lam4.
  5. Forecasts at L = 5.50 and 6.00 for each surviving (p, A').
"""
import math

PI = math.pi
LN = math.log

# ---- recorded ladders (lam, RR upper bounds), deepest triples ----------------
# provenance: results/agent-deep-windows/runs.csv (authoritative), 2026-07-26.
ladders = {
    # L : [(m, lam), ...] deepest three rungs
    4.25: [(128, 5.4302903216e-35), (144, 5.25889827219e-35), (160, 5.23316053313e-35)],
    4.50: [(128, 8.97318032944e-41), (144, 8.13421925362e-41), (160, 7.92448858514e-41)],
    4.60: [(128, 3.07691562325e-43), (144, 2.36393439918e-43), (160, 2.17139835976e-43)],
    4.75: [(128, 1.48804095715e-46), (144, 2.04044762883e-47), (160, 1.86366090828e-47)],
    5.00: [(144, 2.94132035712e-53), (160, 1.77657079904e-54), (176, 7.00751342349e-55)],
    5.50: [(152, 1.98537547115e-64), (168, 1.4413990224e-67), (184, 4.29586487391e-69)],
}

def aitken(x0, x1, x2):
    d1, d2 = x1 - x0, x2 - x1
    if d2 - d1 == 0:
        return x2
    return x2 - d2 * d2 / (d2 - d1)

print("=== 1. Aitken limits (geometric model; ratio r = d2/d1 as convergence flag) ===")
limits = {}
for L, tr in sorted(ladders.items()):
    (m0, x0), (m1, x1), (m2, x2) = tr
    r = (x2 - x1) / (x1 - x0)
    lim = aitken(x0, x1, x2)
    conv = "OK" if 0 < r < 0.5 else ("SOFT" if r < 0.8 else "PLUNGE")
    limits[L] = (lim, conv, r)
    print(f"  L={L:4.2f}: rungs {x0:.4e} {x1:.4e} {x2:.4e}  r={r:.3f}  Aitken={lim:.4e}  [{conv}]")

# convergence policy (pre-registered): use L in {4.25,4.50,4.60,4.75} as the fit
# set; 5.00 indicative only (soft); 5.50 excluded (mid-plunge, bound only).
fitL = [4.25, 4.50, 4.60, 4.75]

print("\n=== 2. A'(p) per window, action pinned at 4*pi ===")
p_menu = [4.5, PI * PI / 2, 5.5, 6.5]
names = ["9/2", "pi^2/2", "11/2", "6.5(free-fit ref)"]
rows = {}
for L in fitL + [5.00]:
    l = L / 2
    lam = limits[L][0]
    y = LN(lam) + 4 * PI * math.exp(l)          # = A' + p*l
    rows[L] = y
    vals = [y - p * l for p in p_menu]
    tag = "(fit)" if L in fitL else "(soft, indicative)"
    print(f"  L={L:4.2f} l={l:.3f}  y=lnlam+4pi e^l={y:9.4f}   " +
          "  ".join(f"A'({n})={v:7.3f}" for n, v in zip(names, vals)) + f"  {tag}")

print("\n  flatness (max-min of A' over the four fit windows):")
for p, n in zip(p_menu, names):
    vs = [rows[L] - p * L / 2 for L in fitL]
    print(f"    p={n:18s}: spread {max(vs)-min(vs):6.3f}   mean A' = {sum(vs)/4:7.3f}")

print("\n=== 3. free (p, A') least squares, 4pi pinned ===")
def fit(Ls, note):
    xs = [L / 2 for L in Ls]
    ys = [rows[L] if L in rows else LN(limits[L][0]) + 4*PI*math.exp(L/2) for L in Ls]
    n = len(xs)
    mx, my = sum(xs)/n, sum(ys)/n
    cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    var = sum((x-mx)**2 for x in xs)
    p = cov / var
    A = my - p * mx
    res = [y - (A + p*x) for x, y in zip(xs, ys)]
    print(f"  {note}: p = {p:6.3f}, A' = {A:7.3f}, resid = " +
          " ".join(f"{r:+.3f}" for r in res))
    return p, A

pfit, Afit = fit(fitL, "four converged windows (Aitken limits)      ")
fit([4.25, 4.50, 4.75], "drop L=4.60 (staircase-suspect window)      ")
# raw last-rung variant (no Aitken): bias check
rows_raw = {}
for L in fitL:
    lam = ladders[L][-1][1]
    rows_raw[L] = LN(lam) + 4 * PI * math.exp(L / 2)
xs = [L/2 for L in fitL]; ys = [rows_raw[L] for L in fitL]
mx, my = sum(xs)/4, sum(ys)/4
cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); var = sum((x-mx)**2 for x in xs)
print(f"  raw m-deepest rungs, no Aitken (bias check) : p = {cov/var:6.3f}, A' = {my-(cov/var)*mx:7.3f}")
# L=4.25 staircase bracket lower endpoint 5.1e-35 (deep-windows report)
rows_b = dict(rows); rows_b[4.25] = LN(5.1e-35) + 4*PI*math.exp(4.25/2)
xs = [L/2 for L in fitL]; ys = [rows_b[L] for L in fitL]
mx, my = sum(xs)/4, sum(ys)/4
cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); var = sum((x-mx)**2 for x in xs)
print(f"  L=4.25 at bracket floor 5.1e-35             : p = {cov/var:6.3f}, A' = {my-(cov/var)*mx:7.3f}")

print("\n=== 4. comparator constants (Fuchs 1964 Thm 1 at n=4; Connes 2602.04022 par.6.4) ===")
# 1 - lam_4(c) ~ 4 sqrt(pi) 8^4/4! c^{9/2} e^{-2c}; c = T* = 2 pi e^l.
K4 = 4 * math.sqrt(PI) * 8**4 / math.factorial(4)
A_lam4 = LN(K4) + 4.5 * LN(2 * PI)          # constant for 1 - lam_4 in our chart
A_chi2 = A_lam4 - LN(2)                     # 1 - chi_2 = (1 - lam_4)/2
print(f"  A'(1-lam4) = ln(4 sqrt(pi) 8^4/4!) + (9/2) ln 2pi = {A_lam4:8.4f}")
print(f"  A'(1-chi2) = same - ln 2                          = {A_chi2:8.4f}")
print(f"  Connes prefactor check: (2^14/3) sqrt2 pi^5 = {2**14/3*math.sqrt(2)*PI**5:.4e}"
      f"  (ln = {LN(2**14/3*math.sqrt(2)*PI**5):.4f})")
Ame = sum(rows[L] - 4.5 * L/2 for L in fitL) / 4
print(f"  measured A'(p=9/2) mean = {Ame:.3f};  Delta vs 1-chi2 = {Ame - A_chi2:+.3f}"
      f"  (e^Delta = {math.exp(Ame - A_chi2):.2f});  vs 1-lam4 = {Ame - A_lam4:+.3f}")
print(f"  [speculation probe] A'(1-chi2) + 2 = {A_chi2 + 2:.4f}")

print("\n=== 5. forecasts (lam at L = 5.50, 6.00) ===")
for (p, A, tag) in [(4.5, Ame, "p=9/2, measured A'"),
                    (PI*PI/2, sum(rows[L] - PI*PI/2*L/2 for L in fitL)/4, "p=pi^2/2, measured A'"),
                    (pfit, Afit, "free-p fit"),
                    (4.5, A_chi2, "Connes/Fuchs 1-chi2 literal")]:
    out = []
    for L in (5.50, 6.00):
        l = L/2
        lnlam = A - 4*PI*math.exp(l) + p*l
        out.append(f"L={L}: log10 lam = {lnlam/LN(10):8.2f}")
    print(f"  {tag:28s}: " + "   ".join(out))

print("\n  L=5.50 recorded bound (m=184, mid-plunge): lam <= 4.296e-69 "
      f"(log10 = {LN(4.29586487391e-69)/LN(10):.2f}) -- not yet adjudicating")
