"""two_scale_test.py -- pre-registered two-curve quasicrystal test (quasicrystal seat).

Union of the zero-ordinate sets of two elliptic curves over F_5 and F_7
(incommensurate periods 2pi/ln5, 2pi/ln7). Frame form
Q_L(phi) = sum_{gamma in Gamma} |phihat(gamma)|^2 on unit phi in L^2[-L/4,L/4],
orthonormal Legendre Galerkin. Predictions logged in prereg.md BEFORE this ran.

Run from repo root:  python3 results/ias/quasicrystal/two_scale_test.py
Cost: ~1-2 CPU-min.
"""
import math
import numpy as np
from scipy.special import spherical_jn

def curve_count(q, c1, c0):
    """#points of y^2 = x^3 + c1 x + c0 over F_q (brute force, incl. infinity)."""
    N = 1
    sq = {}
    for y in range(q):
        sq.setdefault((y * y) % q, 0)
        sq[(y * y) % q] += 1
    for x in range(q):
        rhs = (x * x * x + c1 * x + c0) % q
        N += sq.get(rhs, 0)
    return N

def ordinates(q, theta, H):
    """All gamma = (+-theta + 2 pi k)/ln q with |gamma| <= H."""
    lq = math.log(q)
    p = 2 * math.pi / lq
    out = []
    for th in (theta, -theta):
        g0 = th / lq
        k0 = math.ceil((-H - g0) / p)
        k1 = math.floor((H - g0) / p)
        out.extend(g0 + p * k for k in range(k0, k1 + 1))
    return np.array(out)

def lam_min(gammas, L, m):
    """Smallest eigenvalue of the Legendre-Galerkin frame form."""
    a = L / 4.0
    z = gammas * a
    az = np.abs(z)
    sgn = np.where(z < 0, -1.0, 1.0)  # j_k(-z) = (-1)^k j_k(z); scipy needs z >= 0
    V = np.zeros((m, len(z)), dtype=complex)
    for k in range(m):
        V[k] = ((-1j) ** k) * (sgn ** k) * math.sqrt(2 * a * (2 * k + 1)) \
            * spherical_jn(k, az)
    Q = np.real(V @ V.conj().T)
    Q = 0.5 * (Q + Q.T)
    return float(np.linalg.eigvalsh(Q)[0])

def main():
    N5 = curve_count(5, 1, 1)
    N7 = curve_count(7, 1, 1)
    a5, a7 = 5 + 1 - N5, 7 + 1 - N7
    th5 = math.acos(a5 / (2 * math.sqrt(5)))
    th7 = math.acos(a7 / (2 * math.sqrt(7)))
    print(f"E1/F5: N={N5} a={a5} theta={th5:.6f}  wall 4ln5={4*math.log(5):.4f}")
    print(f"E2/F7: N={N7} a={a7} theta={th7:.6f}  wall 4ln7={4*math.log(7):.4f}")
    print(f"union Landau wall 4ln35 = {4*math.log(35):.4f}\n")

    # P-D control: single curve, rung interior flatness + value.
    rung = (2 - abs(a5) / math.sqrt(5)) * math.log(5)
    print(f"P-D control (E1 alone). expected rung value {rung:.7f}")
    for L in (5.0, 6.0):
        for m in (48, 64):
            g = ordinates(5, th5, 2000.0)
            lam = lam_min(g, L, m)
            print(f"  L={L:5.2f} m={m} H=2000  lam={lam:.7f}  ratio-to-rung={lam/rung:.5f}")
    print()

    # Union scan.
    print("Union scan (m=48/64, H=2000; H=4000 where marked)")
    print("L      m    H     lam_min")
    grid = [7.0, 8.0, 8.5, 9.0, 9.25, 9.5, 10.5, 11.5, 12.5, 13.5, 15.0]
    results = {}
    for L in grid:
        for m in (48, 64):
            for H in ((2000.0, 4000.0) if L in (9.0, 12.5, 13.5, 15.0) else (2000.0,)):
                g = np.concatenate([ordinates(5, th5, H), ordinates(7, th7, H)])
                lam = lam_min(g, L, m)
                results[(L, m, H)] = lam
                print(f"{L:5.2f}  {m}  {int(H):4d}  {lam:.6e}")
    print()

    # Verdicts against prereg.md
    print("== pre-registered verdicts ==")
    lam9_48, lam9_64 = results[(9.0, 48, 2000.0)], results[(9.0, 64, 2000.0)]
    lam9_H = results[(9.0, 64, 4000.0)]
    mdrift = abs(lam9_48 - lam9_64) / max(lam9_64, 1e-300)
    hdrift = abs(results[(9.0, 64, 2000.0)] - lam9_H) / max(lam9_H, 1e-300)
    print(f"P-A: lam(9.0)={lam9_64:.3e} m-drift={100*mdrift:.2f}% H-drift={100*hdrift:.2f}%")
    seq = [results[(L, 64, 2000.0)] for L in (8.0, 8.5, 9.0, 9.25, 9.5)]
    drop = 1 - seq[-1] / seq[0]
    mono = all(seq[i + 1] < seq[i] for i in range(len(seq) - 1))
    print(f"P-B: [8.0..9.5] strictly decreasing={mono} total drop={100*drop:.1f}%")
    span = results[(9.0, 64, 2000.0)] / max(results[(13.5, 64, 2000.0)], 1e-300)
    h135 = abs(results[(13.5, 64, 2000.0)] - results[(13.5, 64, 4000.0)]) / max(
        results[(13.5, 64, 4000.0)], 1e-300)
    print(f"P-C: lam(9)/lam(13.5)={span:.2e}  H-drift at 13.5={100*h135:.1f}%")
    print(f"P-E: lam(15.0)={results[(15.0, 64, 2000.0)]:.3e} "
          f"vs lam(12.5)={results[(12.5, 64, 2000.0)]:.3e}")

if __name__ == "__main__":
    main()
