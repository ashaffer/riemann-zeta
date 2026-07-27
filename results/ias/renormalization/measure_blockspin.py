"""MEASUREMENT script — block-spin linear-response test (renormalization seat).

Run AFTER preregister_blockspin.py (predictions logged in
preregister_blockspin.log). Uses the law-theory agent's exact-Bessel frame
builder (results/agent-law-theory/law_core.py) unmodified.

Three configurations at L = 2.485, Gcut = 840:
  base : smooth staircase (alpha = beta = 1), zeros k = 1..K(840)
  avg  : same, with zeros k = 2..5 replaced by block-averaged (chord)
         positions in [18, 36]
  rev  : same, with those zeros reflected to 2*base - avg (moved UP)

One matrix build at m = 64 per configuration; m = 48 minima extracted from
the nested leading parity sub-blocks (Legendre Galerkin is nested), giving a
basis-drift check of Delta-E for free.  E := -ln lambda_min.
"""
import os, sys, time
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
LT = os.path.join(HERE, "..", "..", "agent-law-theory")
sys.path.insert(0, LT)
import law_core  # noqa: E402

mp.mp.dps = 50

L = mp.mpf('2.485')
GCUT = 840
M = 64
T1, T2 = mp.mpf(18), mp.mpf(36)

def N(T):
    return (T / (2 * mp.pi)) * (mp.log(T / (2 * mp.pi)) - 1) + mp.mpf('0.875')

t0 = time.time()
base = law_core.staircase_zeros(700, dps=50, gmax=GCUT)
base = [g for g in base if g <= GCUT]
print("staircase zeros up to Gcut=%d: %d (%.1fs)" % (GCUT, len(base), time.time() - t0))

N1, N2 = N(T1), N(T2)
rho_bar = (N2 - N1) / (T2 - T1)

avg, rev = [], []
moved = 0
for k, g in enumerate(base, start=1):
    lev = k - mp.mpf('0.5')
    if T1 < g < T2 and N1 < lev < N2:
        tm = T1 + (lev - N1) / rho_bar
        avg.append(tm)
        rev.append(2 * g - tm)
        moved += 1
    else:
        avg.append(g)
        rev.append(g)
print("moved zeros:", moved)

def lam_min_nested(gammas, tag):
    """lam_min at m=64 and at the nested m=48 sub-blocks."""
    t = time.time()
    Qe, Qo = law_core.frame_blocks(gammas, L, M, dps=50)
    out = {}
    with mp.workdps(45):
        for mm in (48, 64):
            ne, no = mm // 2 + mm % 2, mm // 2  # even ks: 0,2,..; count = ceil(mm/2)
            ne = (mm + 1) // 2
            no = mm // 2
            Ee = mp.eigsy(Qe[:ne, :ne], eigvals_only=True)
            Eo = mp.eigsy(Qo[:no, :no], eigvals_only=True)
            lam = min(min(Ee[i] for i in range(ne)), min(Eo[i] for i in range(no)))
            out[mm] = lam
            print("%s  m=%d  lam_min = %s   E = %s   (%.1fs)"
                  % (tag, mm, mp.nstr(lam, 8), mp.nstr(-mp.log(lam), 8),
                     time.time() - t))
    return out

res = {}
for tag, gs in (("base", base), ("avg", avg), ("rev", rev)):
    res[tag] = lam_min_nested(gs, tag)

print()
print("=== RESULTS (E = -ln lambda) ===")
for mm in (48, 64):
    Eb = -mp.log(res["base"][mm])
    Ea = -mp.log(res["avg"][mm])
    Er = -mp.log(res["rev"][mm])
    print("m=%d:  E_base = %s   dE(avg) = %s   dE(rev) = %s"
          % (mm, mp.nstr(Eb, 8), mp.nstr(Ea - Eb, 6), mp.nstr(Er - Eb, 6)))
print()
print("Pre-registered predictions: dE(avg) = +0.573372, dE(rev) = -0.555265")
for mm in (48, 64):
    Eb = -mp.log(res["base"][mm])
    ra = (-mp.log(res["avg"][mm]) - Eb) / mp.mpf('0.573372')
    rr = (-mp.log(res["rev"][mm]) - Eb) / mp.mpf('-0.555265')
    print("m=%d:  ratio(avg) = %s   ratio(rev) = %s"
          % (mm, mp.nstr(ra, 5), mp.nstr(rr, 5)))
