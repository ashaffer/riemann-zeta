"""chowla_hunt.py — Track D hunter #5: central values of real characters at scale.

A single certified NEGATIVE L(1/2, chi_D) for a real character would disprove GRH
(positivity near s = 1 plus a negative central value forces a real zero in (1/2, 1)).
Program law: any negative value is a bug until three independent methods agree.
This module's own history enforces that: an unfixed Kronecker symbol and then a
mangled Lentz continued fraction each manufactured a fake negative — both caught.

EXPECTED (July 26, 2026, |D| <= 100000, 60,786 fundamental discriminants):
  uinc unit test vs mpmath: max rel err ~ 6e-15
  global minimum L(1/2) = +0.00180 at D = 14693  (adjudicated three ways to 6 digits:
    corrected numpy / Euler-Maclaurin / mpmath exact = 0.001798 / 0.001798 / 0.00179796)
  records < 0.02: 14693, 13340 (0.00361), 60357, 90461, -37427, 37901, -28963, -17923
  small-value CDF exponent on certified data: 1.50  (symplectic prediction 3/2)
  D = 14693 lowest zero gamma_1 = 0.0232 = 5.7% of mean spacing 0.405
    (ordinary comparator D = 14696: L(1/2) = 1.73, gamma_1 = 0.683 = 169%)
"""
import numpy as np
import mpmath as mp
from math import gamma as GAMMA
from weil_core import kron
from family_experiments import is_fundamental


def uinc(a, x):
    """Upper incomplete gamma Gamma(a, x), vectorized: series for x <= 1.2,
    modified-Lentz continued fraction otherwise.  Unit-tested against mpmath."""
    x = np.asarray(x, float)
    out = np.empty_like(x)
    ga = GAMMA(a)
    lo = x <= 1.2
    if lo.any():
        xs = x[lo]
        term = np.ones_like(xs)/a
        s = term.copy()
        for k in range(1, 45):
            term = term*xs/(a + k)
            s += term
        out[lo] = ga - (xs**a)*np.exp(-xs)*s
    hi = ~lo
    if hi.any():
        xh = x[hi]
        b = xh + 1.0 - a
        c = np.full_like(xh, 1e30)      # correct Lentz seed: c0 "infinite"
        d = 1.0/b
        h = d.copy()
        for i in range(1, 140):
            an = -i*(i - a)
            b = b + 2.0
            d = an*d + b
            d = np.where(np.abs(d) < 1e-300, 1e-300, d)
            c = b + an/c
            c = np.where(np.abs(c) < 1e-300, 1e-300, c)
            d = 1.0/d
            h = h*(d*c)
        out[hi] = np.exp(-xh)*(xh**a)*h
    return out


def unit_test_uinc():
    errs = []
    for a in (0.25, 0.75):
        for xv in (0.03, 0.5, 1.1, 1.3, 2.7, 8.0, 25.0):
            ref = float(mp.gammainc(a, xv, mp.inf))
            errs.append(abs(float(uinc(a, np.array([xv]))[0]) - ref)/ref)
    return max(errs)


G14, G34 = GAMMA(0.25), GAMMA(0.75)


def L_half(D):
    """Exact central value via the theta-integral incomplete-gamma series.
    even chi (D > 0):  L = 2 SUM chi(n) x^{-1/4} G(1/4, x) / ((q/pi)^{1/4} G(1/4))
    odd  chi (D < 0):  L = 2 SUM n chi(n) x^{-3/4} G(3/4, x) / ((q/pi)^{3/4} G(3/4))
    with x = pi n^2 / q; truncation n <= 3.2 sqrt(q) gives tail < e^{-32}."""
    q = abs(D)
    N = int(3.2*np.sqrt(q)) + 1
    n = np.arange(1, N, dtype=float)
    ch = np.array([kron(D, int(k)) for k in range(1, N)], float)
    nz = ch != 0
    n, c = n[nz], ch[nz]
    x = np.pi*n*n/q
    if D > 0:
        return 2.0*(c*(x**-0.25)*uinc(0.25, x)).sum()/((q/np.pi)**0.25 * G14)
    return 2.0*(c*n*(x**-0.75)*uinc(0.75, x)).sum()/((q/np.pi)**0.75 * G34)


def hunt(Dmax, record_below=0.02, progress=None):
    """Scan all fundamental |D| <= Dmax.  Returns (global_min, D_min, records)."""
    recs, best = [], (1e9, 0)
    for d in range(3, Dmax + 1):
        for D in (-d, d):
            if not is_fundamental(D):
                continue
            L = L_half(D)
            if L < best[0]:
                best = (L, D)
            if L < record_below:
                recs.append((L, D))
    return best, sorted(recs)


def lowest_zero(D, t_max=1.6, step=0.03, N=280, dps=15):
    """gamma_1 for chi_D (even D) via the completed-Lambda incomplete-gamma series,
    real on the critical line for real chi with root number +1."""
    mp.mp.dps = dps
    q = mp.mpf(abs(D))
    ch = {}
    def chi(n):
        if n not in ch:
            ch[n] = kron(D, n)
        return ch[n]
    def Lam_re(t):
        sv = mp.mpf('0.5') + mp.mpc(0, 1)*mp.mpf(t)
        tot = mp.mpc(0)
        for n in range(1, N):
            c = chi(n)
            if c == 0:
                continue
            x = mp.pi*n*n/q
            tot += c*(x**(-sv/2)*mp.gammainc(sv/2, x, mp.inf)
                      + x**(-(1-sv)/2)*mp.gammainc((1-sv)/2, x, mp.inf))
        return float(mp.re(tot))
    tprev, vprev = 0.02, Lam_re(0.02)
    t = tprev + step
    while t < t_max:
        v = Lam_re(t)
        if vprev*v < 0:
            lo, hi = tprev, t
            for _ in range(8):
                mid = (lo + hi)/2
                lo, hi = ((lo, mid) if Lam_re(mid)*Lam_re(lo) < 0 else (mid, hi))
            return (lo + hi)/2
        tprev, vprev = t, v
        t += step
    return None


if __name__ == "__main__":
    print("uinc unit test: max rel err = %.1e (EXPECTED ~6e-15)" % unit_test_uinc())
    print("L(1/2) anchors: D=-163: %.4f (exp 0.0685)  D=-1411: %.4f (exp 0.0239)"
          % (L_half(-163), L_half(-1411)))
    print("D=14693: L(1/2) = %.6f (EXPECTED 0.001798)" % L_half(14693))
    g1 = lowest_zero(14693)
    print("D=14693 gamma_1 = %.4f (EXPECTED 0.0232; mean spacing 0.405)" % g1)
