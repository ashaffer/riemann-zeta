"""sep_test.py — Round-2 C-1 separating-example test (SEP), magic-functions seat.

Pre-registered in results/ias/SEAT-magic-functions.md SR2.2.1a BEFORE this run.
Modulated staircases N_config(T) = Nhat(T) + A sin(k0 u + phi), u = ln(T/2pi):
MOD-N (window-neutral phase, in-gap wavenumber k0 = 0.35 < ln 2) vs MOD-C
(charged control, phi + pi/2). L = 2.485, m = 24, K = 180, dps 40.
"""
import sys, time, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
import mpmath as mp
from model_zeros import frame_form
from spectral_margins import spectral_lam_min

mp.mp.dps = 40
pi = mp.pi
K = 180
L = mp.mpf('2.485')
M = 24
ell = L / 2
Tstar = 2 * pi * mp.e**ell
X = mp.e * Tstar                      # capacity height eT*
A = mp.mpf('0.35')
k0 = mp.mpf('0.35')
u0 = mp.log(mp.mpf('14.5213') / (2 * pi))
uX = ell + 1
phi0 = -k0 * (u0 + uX) / 2

def stair_mod(K, A, k0, phi):
    """t_k solving Nhat(t) + A sin(k0 ln(t/2pi) + phi) = k - 1/2."""
    out = []
    g = mp.mpf(14)
    for k in range(1, K + 1):
        rhs = k - mp.mpf('0.5')
        for _ in range(80):
            u = mp.log(g / (2 * pi))
            f = g / (2 * pi) * (u - 1) + mp.mpf('0.875') + A * mp.sin(k0 * u + phi) - rhs
            fp = u / (2 * pi) + A * k0 * mp.cos(k0 * u + phi) / g
            step = f / fp
            g = g - step
            if abs(step) < mp.mpf('1e-28'):
                break
        out.append(+g)
        g = g + 2 * pi / mp.log(g / (2 * pi))
    return out

def Iw_disc(nodes_mod, nodes_base):
    """(pi^2/2) * [ sum_{mod<=X} ln(X/t) - sum_{base<=X} ln(X/t) ] (Fubini)."""
    s1 = sum(mp.log(X / t) for t in nodes_mod if t <= X)
    s0 = sum(mp.log(X / t) for t in nodes_base if t <= X)
    return (pi**2 / 2) * (s1 - s0)

def run(tag, gs):
    t0 = time.time()
    Q = frame_form(gs, float(L), M, dps=40)
    lam = spectral_lam_min(Q, nev=1, dps=35)[0]
    print("%-8s t1=%-11s lam=%s  (%.0fs)" % (tag, mp.nstr(gs[0], 7), mp.nstr(lam, 8), time.time() - t0), flush=True)
    return lam

base = stair_mod(K, mp.mpf(0), k0, phi0)          # A=0 -> plain beta=1/2 staircase
modN = stair_mod(K, A, k0, phi0)
modC = stair_mod(K, A, k0, phi0 + pi / 2)
print("# SEP config: A=%s k0=%s phi0=%s  X=eT*=%s" % (A, k0, mp.nstr(phi0, 6), mp.nstr(X, 6)), flush=True)
print("# discrete I_w(MOD-N) = %s nats (locked |.| <= 0.3)" % mp.nstr(Iw_disc(modN, base), 5), flush=True)
print("# discrete I_w(MOD-C) = %s nats (smoothed prediction +2.402)" % mp.nstr(Iw_disc(modC, base), 5), flush=True)
lam_base = run("base", base)
lam_N = run("MOD-N", modN)
lam_C = run("MOD-C", modC)
dN = mp.log(lam_N / lam_base)
dC = mp.log(lam_C / lam_base)
print("\n# dlnlam(MOD-N) = %+.4f nats   [SEP-P1: |.|<=0.4 and <=0.2*|MOD-C|]" % dN, flush=True)
print("# dlnlam(MOD-C) = %+.4f nats   [SEP-P2: +2.40*(1+-0.35) = [1.56, 3.24]]" % dC, flush=True)
print("# ratio |N|/|C| = %.3f" % abs(dN / dC), flush=True)
