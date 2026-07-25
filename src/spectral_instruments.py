"""spectral_instruments.py — the zero-side and prime-side instruments.

EXPECTED (July 26, 2026):
  census [100, 30000]: 35,644 zeros found vs 35,643.63 predicted (deficit 0)
  record Lehmer-type pair: t = 17143.7865, gap 0.0353, max|Z| between = 0.00215
    (classic pair t = 7005.0629/7005.1006: gap 0.0377, bump 0.00397)
  GUE small-gap counts run at 65-73% of asymptotic prediction at these heights
  equal-loudness (pole-subtracted): line heights ~ log X, all lines equal;
    at X = 1e6: 13.79/13.26/13.08/12.90/13.13 vs log X = 13.82; off-res floor ~0.8
  rogue scan t in [10,300], X = 1e5 -> 1e6: 138 lines vs ~139 zeros,
    growth ratios 1.209 +/- 0.133 vs RH prediction 1.200, max 1.526 (beta < 0.604)
  Davenport-Heilbronn off-line zero: rho = 0.808517182457 + 85.6993484854i
"""
import numpy as np
import mpmath as mp


# ---------------- Riemann-Siegel Z (screening accuracy: main sum + C0 term) --------
def theta(t):
    return t/2*np.log(t/(2*np.pi)) - t/2 - np.pi/8 + 1/(48*t)


def Z_screen(t):
    N = np.floor(np.sqrt(t/(2*np.pi))).astype(np.int64)
    th = theta(t)
    s = np.zeros_like(t)
    for n in range(1, int(N.max()) + 1):
        m = N >= n
        s[m] += np.cos(th[m] - t[m]*np.log(n))/np.sqrt(n)
    a = np.sqrt(t/(2*np.pi)); p = a - N
    Psi = np.cos(2*np.pi*(p*p - p - 1.0/16))/np.cos(2*np.pi*p)
    return 2*s + (-1.0)**(N-1) * (t/(2*np.pi))**(-0.25) * Psi


def scan_zeros(t0=100.0, t1=30000.0, step=0.004, block=300000):
    zs = []
    for lo in np.arange(t0, t1, block*step):
        t = np.arange(lo, min(lo + block*step, t1) + step, step)
        Z = Z_screen(t)
        sc = np.nonzero(Z[:-1]*Z[1:] < 0)[0]
        zs.append(t[sc] - Z[sc]*step/(Z[sc+1]-Z[sc]))
    return np.unique(np.concatenate(zs))


def lehmer_hunt(zeros, top=6, refine=True, dps=25):
    """Smallest normalized gaps; refine with mpmath and measure the interior bump."""
    g = np.diff(zeros); gam = zeros[:-1]
    delta = g*np.log(gam/(2*np.pi))/(2*np.pi)
    idx = np.argsort(delta)[:top]
    out = []
    if refine:
        mp.mp.dps = dps
        for i in sorted(idx, key=lambda j: delta[j]):
            z1, z2 = zeros[i], zeros[i+1]; mid = (z1+z2)/2
            r1 = mp.findroot(mp.siegelz, (mp.mpf(z1)-mp.mpf('0.012'), mp.mpf(mid)), solver='anderson')
            r2 = mp.findroot(mp.siegelz, (mp.mpf(mid), mp.mpf(z2)+mp.mpf('0.012')), solver='anderson')
            gap = r2 - r1
            bump = max(abs(mp.siegelz(r1 + gap*k/240)) for k in range(1, 240))
            out.append((float(r1), float(gap), float(gap*mp.log(r1/(2*mp.pi))/(2*mp.pi)), float(bump)))
    return out


def gue_gap_counts(zeros, thresholds=(0.10, 0.15, 0.20, 0.30)):
    g = np.diff(zeros); gam = zeros[:-1]
    delta = g*np.log(gam/(2*np.pi))/(2*np.pi)
    s = np.linspace(0, max(thresholds), 3000)
    p = 32/np.pi**2 * s**2 * np.exp(-4*s**2/np.pi)     # GUE Wigner surmise, beta = 2
    trap = getattr(np, 'trapezoid', np.trapz)          # numpy < 2.0 compatibility
    return [(s0, int((delta < s0).sum()),
             len(delta)*trap(p[s <= s0], s[s <= s0])) for s0 in thresholds]


# ---------------- prime-side spectrum (never evaluates zeta) -----------------------
def von_mangoldt(N):
    sv = np.ones(N+1, bool); sv[:2] = False
    for p in range(2, int(N**0.5)+1):
        if sv[p]:
            sv[p*p::p] = False
    primes = np.nonzero(sv)[0]
    lam = np.zeros(N+1); lam[primes] = np.log(primes)
    for p in primes[primes <= int(N**0.5)+1]:
        pk = p*p
        while pk <= N:
            lam[pk] = np.log(p); pk *= p
    nz = np.nonzero(lam)[0]
    return nz, np.log(nz), lam[nz]/np.sqrt(nz)


def prime_spectrum(tgrid, X, nz, ln, w):
    """|F_X(t) - pole|: pole-subtracted prime spectrum.  Under RH every line at a zero
    ordinate grows like log X (equal loudness); a zero at beta + i gamma off the line
    grows like X^{beta - 1/2}."""
    m = nz <= X
    lnX, wX = ln[m], w[m]
    F = np.zeros(len(tgrid), complex)
    for i in range(0, len(tgrid), 100):
        ph = tgrid[i:i+100][:, None]*lnX[None, :]
        F[i:i+100] = (wX*np.cos(ph)).sum(1) - 1j*(wX*np.sin(ph)).sum(1)
    s = 0.5 + 1j*tgrid
    return np.abs(F - X**(1-s)/(1-s))


# ---------------- Davenport-Heilbronn: functional equation without Euler product ---
def dh_zero(start=(0.81, 85.70), dps=25):
    """Finds the off-critical-line zero of the Davenport-Heilbronn function.
    EXPECTED: 0.808517182457 + 85.6993484854i, |f| ~ 1e-26, FE partner ~ 1e-24."""
    mp.mp.dps = dps
    kappa = (mp.sqrt(10-2*mp.sqrt(5))-2)/(mp.sqrt(5)-1)
    chi = {1: mp.mpc(1), 2: mp.mpc(0, 1), 3: mp.mpc(0, -1), 4: mp.mpc(-1)}
    def L(s, conj=False):
        tot = mp.mpc(0)
        for a in (1, 2, 3, 4):
            c = chi[a].conjugate() if conj else chi[a]
            tot += c*mp.zeta(s, mp.mpf(a)/5)
        return 5**(-s)*tot
    i = mp.mpc(0, 1)
    f = lambda s: (1-i*kappa)/2*L(s) + (1+i*kappa)/2*L(s, conj=True)
    rho = mp.findroot(f, mp.mpc(*[str(x) for x in start]))
    return rho, abs(f(rho)), abs(f(1-rho))


if __name__ == "__main__":
    zeros = scan_zeros(t1=8000.0)
    import mpmath as _mp
    smooth = float((_mp.siegeltheta(8000)-_mp.siegeltheta(100))/_mp.pi)
    print("census [100,8000]: %d zeros vs %.2f predicted" % (len(zeros), smooth))
    for t, gap, nd, bump in lehmer_hunt(zeros, top=2):
        print("close pair t=%.4f gap=%.4f norm=%.4f bump=%.5f" % (t, gap, nd, bump))
    # EXPECTED: pair near t = 7005.063 with gap 0.0377, bump 0.00397; pair near 5229.199
    rho, res, fe = dh_zero()
    print("DH zero:", _mp.nstr(rho, 12), " |f|=%.1e  |f(1-rho)|=%.1e" % (float(res), float(fe)))
