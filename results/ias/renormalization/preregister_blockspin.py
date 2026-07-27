"""PRE-REGISTRATION script — block-spin linear-response test (renormalization seat).

Run BEFORE any measurement. Computes and logs the predicted Delta-E for the
block-spin (block-averaged density) perturbation of the smooth staircase at
L = 2.485, using ONLY the measured marginal law of results/agent-law-theory.md
RUN 4:  f(t) = (pi^2/2) * ln(e*T*/t)  for t below ~0.6 eT*.

The perturbation: inside the block [T1, T2] = [18, 36] replace the graded
(RvM) staircase zeros by equal-count constant-density (chord / block-averaged)
positions:  t_k = T1 + (k - 1/2 - N(T1)) / rho_bar,
rho_bar = (N(T2) - N(T1)) / (T2 - T1).  Count in block is preserved; zeros
outside the block are untouched.  This is one decimation step of the
"spliced ladder" block-spin construction (seed (b) of the seat brief).

Linear-response prediction (independent of eT*, telescopes to pure RG time):

  dE_pred(avg) = (pi^2/2) * SUM_k ln(gamma_k_base / t_k_mod)   > 0
  dE_pred(rev) = (pi^2/2) * SUM_k ln(gamma_k_base / t_k_rev)   < 0
      with the reflected block t_k_rev = 2*gamma_k_base - t_k_mod
      (same displacement magnitudes, opposite direction).

Pre-registered acceptance band (logged before measurement):
  ratio r = dE_measured / dE_pred in [0.65, 1.35] -> linear response holds,
      the marginal potential acts as an RG kernel for redistributions;
  r in [0.5, 2.0] -> qualified pass (interaction-dressed);
  r outside [0.5, 2.0] (or wrong sign) -> KILL: the marginal law does NOT
      integrate as a linear-response kernel; the deficit-dipole/block-spin
      reading of the marginal law is dead.
Secondary (concavity, from law-theory RUN 4(iv): insertions ~20% smaller):
  expect |dE_measured(rev)| / dE_pred-magnitude ratio BELOW the avg-direction
  ratio (mild concavity).
"""
import mpmath as mp

mp.mp.dps = 30

L = mp.mpf('2.485')
a = L / 4
ell = L / 2
Tstar = 2 * mp.pi * mp.e**ell
eTstar = mp.e * Tstar
T1, T2 = mp.mpf(18), mp.mpf(36)

def N(T):
    return (T / (2 * mp.pi)) * (mp.log(T / (2 * mp.pi)) - 1) + mp.mpf('0.875')

def solveN(level, lo, hi):
    return mp.findroot(lambda t: N(t) - level, (lo + hi) / 2)

N1, N2 = N(T1), N(T2)
rho_bar = (N2 - N1) / (T2 - T1)
print("L = %s, T* = %s, eT* = %s" % (L, mp.nstr(Tstar, 8), mp.nstr(eTstar, 8)))
print("N(18) = %s, N(36) = %s, rho_bar = %s" % (mp.nstr(N1, 8), mp.nstr(N2, 8), mp.nstr(rho_bar, 8)))

ks = [k for k in range(1, 40) if N1 < k - mp.mpf('0.5') < N2]
print("block indices k:", ks)

rows = []
S_avg = mp.mpf(0)
S_rev = mp.mpf(0)
for k in ks:
    lev = k - mp.mpf('0.5')
    gb = solveN(lev, T1, T2)          # base (graded) position
    tm = T1 + (lev - N1) / rho_bar    # block-averaged position
    tr = 2 * gb - tm                  # reflected position
    S_avg += mp.log(gb / tm)
    S_rev += mp.log(gb / tr)
    rows.append((k, gb, tm, tr))
    print("k=%d  base %s  avg %s  (disp %s)  rev %s" %
          (k, mp.nstr(gb, 8), mp.nstr(tm, 8), mp.nstr(tm - gb, 6), mp.nstr(tr, 8)))

c = mp.pi**2 / 2
dE_avg = c * S_avg
dE_rev = c * S_rev
print()
print("PRE-REGISTERED PREDICTIONS (marginal-law linear response):")
print("  dE_pred(block-avg, zeros move DOWN)  = +%s" % mp.nstr(dE_avg, 6))
print("  dE_pred(reflected, zeros move UP)    = %s" % mp.nstr(dE_rev, 6))
print("  (E = -ln lambda; positive dE means lambda DECREASES)")
print("Acceptance: ratio in [0.65, 1.35] pass; [0.5, 2.0] qualified; else KILL.")
