"""fits.py — harvest data/*.jsonl into the report tables and fits."""
import json, os, math
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def load(name):
    out = []
    with open(os.path.join(DATA, name)) as f:
        for line in f:
            if line.strip():
                out.append(json.loads(line))
    return out


def key(r, *ks):
    return tuple(r.get(k) for k in ks)


# ---------------- RUN 1: smooth-law grid ----------------
def smoothlaw_table():
    rs = load("smoothlaw.jsonl")
    Ls = sorted({r["L"] for r in rs})
    print("\n### RUN 1 — smooth staircase lambda_min(L) (lower bds in Gcut, "
          "Galerkin m)")
    print("| L | m=48 Gc=840 | m=64 Gc=840 | m=48 Gc=1680 | m=64 Gc=1680 | "
          "m=64 Gc=3360 |")
    print("|---|---|---|---|---|---|")
    grid = {}
    for L in Ls:
        row = [f"{L:g}"]
        for (m, gc) in ((48, 840), (64, 840), (48, 1680), (64, 1680),
                        (64, 3360)):
            v = [r for r in rs if r["L"] == L and r["m"] == m
                 and r["Gcut"] == gc]
            row.append(v[0]["lam"] if v else "--")
            if v:
                grid[(L, m, gc)] = v[0]["lnlam"]
        print("| " + " | ".join(row) + " |")
    return grid


def refit(grid, mm=64, gcs=(3360,), label=""):
    Ls = sorted({L for (L, m, gc) in grid if m == mm and gc in gcs})
    y = [grid[(L, mm, gcs[0])] for L in Ls]
    best = None
    for c0 in np.arange(-2.0, 10.0, 0.005):
        X = np.vstack([np.ones(len(Ls)),
                       [-math.exp(L / 2) * (L / 2 + c0) for L in Ls]]).T
        coef, *_ = np.linalg.lstsq(X, np.array(y), rcond=None)
        pred = X @ coef
        rms = float(np.sqrt(np.mean((pred - np.array(y)) ** 2)))
        if best is None or rms < best[3]:
            best = (float(coef[0]), float(coef[1]), float(c0), rms)
    A, b, c0, rms = best
    kappa = math.exp(c0 + 1)
    print(f"\nrefit[{label}] ln lam = {A:.3f} - {b:.4f} e^(L/2)(L/2 + {c0:.3f})"
          f"   rms={rms:.4f}"
          f"\n  count-toll reading: cutoff kappa*T* with kappa=e^(c0+1)="
          f"{kappa:.2f}, per-zero toll b/kappa = {b / kappa:.4f}"
          f" ... toll*kappa/e = b/e^{{c0}} = {b / math.exp(c0):.4f}")
    return best


def gcut_extrap(grid):
    print("\nGcut drift at m=64 (lnlam at 840 / 1680 / 3360; "
          "geometric extrapolation of the tail):")
    print("| L | E(840) | E(1680) | E(3360) | E_extrap(inf) | drift status |")
    print("|---|---|---|---|---|---|")
    out = {}
    for L in sorted({L for (L, m, gc) in grid if m == 64}):
        try:
            e1, e2, e3 = (-grid[(L, 64, 840)], -grid[(L, 64, 1680)],
                          -grid[(L, 64, 3360)])
        except KeyError:
            continue
        d1, d2 = e1 - e2, e2 - e3          # positive, shrinking
        if d1 > 0 and 0 < d2 < d1:
            q = d2 / d1
            einf = e3 - d2 * q / (1 - q)
            st = "geom q=%.2f" % q
        else:
            einf, st = e3, "non-geometric"
        out[L] = einf
        print(f"| {L:g} | {e1:.3f} | {e2:.3f} | {e3:.3f} | {einf:.3f} | {st} |")
    return out


def refit_einf(einf):
    Ls = sorted(einf)
    y = [-einf[L] for L in Ls]
    best = None
    for c0 in np.arange(-2.0, 10.0, 0.005):
        X = np.vstack([np.ones(len(Ls)),
                       [-math.exp(L / 2) * (L / 2 + c0) for L in Ls]]).T
        coef, *_ = np.linalg.lstsq(X, np.array(y), rcond=None)
        rms = float(np.sqrt(np.mean((X @ coef - np.array(y)) ** 2)))
        if best is None or rms < best[3]:
            best = (float(coef[0]), float(coef[1]), float(c0), rms)
    A, b, c0, rms = best
    print(f"\nrefit[Gcut-extrapolated] ln lam = {A:.3f} - {b:.4f} "
          f"e^(L/2)(L/2 + {c0:.3f})  rms={rms:.4f}"
          f"  (kappa={math.exp(c0 + 1):.2f}, toll={b / math.exp(c0 + 1):.4f})")
    return best


# ---------------- RUN 2: AP ----------------
def ap_table():
    rs = load("ap.jsonl")
    print("\n### RUN 2 — arithmetic progressions gamma_k = s0(k+1/2)")
    for L in sorted({r["L"] for r in rs}):
        print(f"\nL = {L}  (Nyquist spacing pi/a = {math.pi / (L / 4):.4f})")
        print("| s0 | s0/(pi/a) | pred lam_inf | m=32 Gc420 | m=48 Gc420 | "
              "m=64 Gc420 | m=48 Gc840 | m=64 Gc840 |")
        print("|---|---|---|---|---|---|---|---|")
        for s0 in sorted({r["s0"] for r in rs if r["L"] == L}):
            sel = [r for r in rs if r["L"] == L and r["s0"] == s0]
            row = [f"{s0:g}", f"{sel[0]['s0_over_nyq']:.3f}",
                   f"{sel[0]['pred_inf']:.4f}" if sel[0]['pred_inf'] else "0"]
            for (m, gc) in ((32, 420), (48, 420), (64, 420), (48, 840),
                            (64, 840)):
                v = [r for r in sel if r["m"] == m and r["Gcut"] == gc]
                row.append(v[0]["lam"] if v else "--")
            print("| " + " | ".join(row) + " |")


# ---------------- RUN 4: marginal ----------------
def marginal_table():
    rs = load("marginal.jsonl")
    print("\n### RUN 4 — marginal worth of one zero: "
          "DeltaE = ln lam(full) - ln lam(minus gamma_j)")
    for L in sorted({r["L"] for r in rs}):
        Tstar = 2 * math.pi * math.exp(L / 2)
        Tcap = math.e * Tstar
        print(f"\nL = {L}:  T* = {Tstar:.1f}, e*T* = {Tcap:.1f}")
        print("| j | gamma_j | dE (m48,Gc840) | dE (m64,Gc840) | "
              "dE (m48,Gc1680) |")
        print("|---|---|---|---|---|")
        base = {}
        for r in rs:
            if r["tag"] == "base" and r["L"] == L:
                base[(r["m"], r["Gcut"])] = r["lnlam"]
        js = sorted({r["j"] for r in rs if r["tag"] == "rm" and r["L"] == L})
        for j in js:
            row = [str(j)]
            gj = None
            for (m, gc) in ((48, 840), (64, 840), (48, 1680)):
                v = [r for r in rs if r["tag"] == "rm" and r["L"] == L
                     and r["j"] == j and r["m"] == m and r["Gcut"] == gc]
                if v:
                    gj = v[0]["gj"]
                    dE = base[(m, gc)] - v[0]["lnlam"]
                    row.append(f"{dE:.3f}")
                else:
                    row.append("--")
            row.insert(1, f"{gj:.1f}")
            print("| " + " | ".join(row) + " |")
        ins = [r for r in rs if r["tag"] == "ins" and r["L"] == L]
        if ins:
            print("insertions (midpoint after gamma_j): "
                  + ", ".join("j=%d g=%.1f dE=%+.3f"
                              % (r["j"], r["gmid"],
                                 base[(r["m"], r["Gcut"])] - r["lnlam"])
                              for r in ins))


# ---------------- RUN 3: alpha/beta ----------------
def alphabeta_table():
    if not os.path.exists(os.path.join(DATA, "alphabeta.jsonl")):
        print("\n(RUN 3 not finished)")
        return
    rs = load("alphabeta.jsonl")
    print("\n### RUN 3 — staircase deformations N_{alpha,beta}")
    for L in sorted({r["L"] for r in rs}):
        print(f"\nL = {L}")
        print("| alpha | beta | m=48 Gc420 | m=64 Gc420 | m=48 Gc840 | "
              "m=64 Gc840 | m=64 Gc1680 |")
        print("|---|---|---|---|---|---|---|")
        combos = sorted({(r["alpha"], r["beta"]) for r in rs
                         if r["L"] == L})
        for (al, be) in combos:
            row = [f"{al:g}", f"{be:g}"]
            for (m, gc) in ((48, 420), (64, 420), (48, 840), (64, 840),
                            (64, 1680)):
                v = [r for r in rs if r["L"] == L and r["alpha"] == al
                     and r["beta"] == be and r["m"] == m and r["Gcut"] == gc]
                row.append(v[0]["lam"] if v else "--")
            print("| " + " | ".join(row) + " |")


if __name__ == "__main__":
    grid = smoothlaw_table()
    refit(grid, 64, (3360,), "m=64,Gcut=3360")
    refit(grid, 64, (840,), "m=64,Gcut=840")
    einf = gcut_extrap(grid)
    refit_einf(einf)
    ap_table()
    marginal_table()
    alphabeta_table()
