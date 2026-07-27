"""FB-T2: bare defect-potential sum vs measured marginal worth.

Pre-registered in SEAT-free-boundary.md R2.5 (gates G1-G3) BEFORE this run.
G(t0) = sum_{staircase t_k <= H, k != k0} ln|1 - t0^2/t_k^2|
      - sum_{budget (j-1/2)pi/a <= H} ln|1 - t0^2/t'_j^2|
Conjecture FB-1(ii): f_measured(t0) ~ 2 G(t0), profile (pi^2/2) ln(eT*/t0).
Pure sums, no eigensolves. python3 fbt2_defect_potential.py
"""
import math

PI = math.pi
E = math.e

# RUN-4 measured worths (results/agent-law-theory/report.md sec. 3.4)
MEAS = {
    2.485: [(14.5, 6.923), (20.7, 5.277), (25.5, 4.256), (33.6, 2.737),
            (44.0, 0.724), (56.1, 0.049)],
    2.996: [(14.5, 8.062), (20.7, 6.485), (25.5, 5.536), (33.6, 4.214),
            (44.0, 2.727), (56.1, 0.855)],
}


def nhat(T):
    return (T / (2 * PI)) * math.log(T / (2 * PI * E)) + 7.0 / 8.0


def quantile(k):
    """Solve nhat(t) = k - 1/2 by Newton."""
    t = max(10.0, 2 * PI * E * math.exp(k / 3.0))
    for _ in range(80):
        f = nhat(t) - (k - 0.5)
        df = math.log(t / (2 * PI)) / (2 * PI)
        t -= f / df
        t = max(t, 7.0)
    return t


def gsum(t0, pts):
    s = 0.0
    for t in pts:
        if abs(t - t0) < 1e-9:
            continue
        s += math.log(abs(1 - (t0 * t0) / (t * t)))
    return s


for L in (2.485, 2.996):
    a = L / 4.0
    ell = L / 2.0
    Tstar = 2 * PI * math.exp(ell)
    eTs = E * Tstar
    H2 = math.exp(0.62) * Tstar
    # staircase points up to eT*
    stair = []
    k = 1
    while True:
        t = quantile(k)
        if t > eTs:
            break
        stair.append(t)
        k += 1
    # budget lattice
    budget = []
    j = 1
    while (j - 0.5) * PI / a <= eTs:
        budget.append((j - 0.5) * PI / a)
        j += 1
    stair2 = [t for t in stair if t <= H2]
    budget2 = [t for t in budget if t <= H2]
    print(f"\nL={L}: T*={Tstar:.3f} eT*={eTs:.3f} H2={H2:.3f} "
          f"#stair={len(stair)} #budget={len(budget)} "
          f"(H2: {len(stair2)}/{len(budget2)})")
    print(" t0      u      f_meas  purelog  2G(eT*)  R=2G/f  2G(H2)  R2")
    rows = []
    for (gm, fm) in MEAS[L]:
        # match to nearest staircase point
        t0 = min(stair, key=lambda t: abs(t - gm))
        if abs(t0 - gm) > 0.8:
            print(f"  [no staircase match for {gm}]")
            continue
        u = t0 / Tstar
        plog = (PI * PI / 2) * math.log(eTs / t0)
        G1v = gsum(t0, stair) - gsum(t0, budget)
        G2v = gsum(t0, stair2) - gsum(t0, budget2)
        R = 2 * G1v / fm if fm != 0 else float('nan')
        R2 = 2 * G2v / fm if fm != 0 else float('nan')
        rows.append((t0, u, fm, plog, 2 * G1v, R, 2 * G2v, R2))
        print(f" {t0:6.2f} {u:6.3f} {fm:7.3f} {plog:7.3f} {2*G1v:8.3f} "
              f"{R:6.2f} {2*G2v:8.3f} {R2:6.2f}")
    # OLS slope of 2G vs ln(eT*/t0) over bulk points u <= 1.6
    for (tag, col) in (("eT*", 4), ("H2 ", 6)):
        xs = [math.log(eTs / r[0]) for r in rows if r[1] <= 1.6]
        ys = [r[col] for r in rows if r[1] <= 1.6]
        n = len(xs)
        mx, my = sum(xs) / n, sum(ys) / n
        sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / \
             sum((x - mx) ** 2 for x in xs)
        print(f"  bulk OLS slope ({tag}, n={n}): {sl:.3f}  "
              f"vs pi^2/2 = {PI*PI/2:.3f}  ratio {sl/(PI*PI/2):.3f}")
