"""oracle.py — the two-sided Guinand-Weil identities.  RUN THIS FIRST.

Left side: a sum over zeros only.  Right side: primes + pole + digamma integral only.
The two sides use independent computational paths.  Agreement is a high-precision
regression check of the normalizations used by the other scripts; it is not an
interval or formal certificate.  Disagreement means a convention or implementation
bug somewhere.

EXPECTED (as measured July 26, 2026):
  zeta, Gaussian window on gamma_3, dps 30, 16 zeros, primes to 130000:
      both sides 2.0007024351181021364,  diff ~ -1.5e-29
  zeta, window off-resonance (t0 = 18.5):  both sides 0.08328847...,  diff ~ -9e-30
  chi mod 3 (D = -3): first zero 8.0397372,  identity diff ~ -6e-22
  chi mod 4 (D = -4): first zero 6.0209489,  identity diff ~ -2e-22
The quick demo below uses lighter settings; expect diffs ~1e-12 to 1e-16.
"""
import numpy as np
import mpmath as mp
from weil_core import kron


def sieve_prime_powers(N):
    sv = np.ones(N + 1, bool); sv[:2] = False
    for p in range(2, int(N**0.5) + 1):
        if sv[p]:
            sv[p*p::p] = False
    primes = np.nonzero(sv)[0]
    out = []
    for p in primes:
        pk = int(p)
        while pk <= N:
            out.append((pk, int(p)))
            pk *= p
    out.sort()
    return out


def zeta_identity(t0, a=0.5, n_zeros=16, prime_cut=130000, dps=30):
    """Two-sided identity for zeta with h(r) = e^{-a(r-t0)^2} + e^{-a(r+t0)^2}."""
    mp.mp.dps = dps
    aG, t0 = mp.mpf(a), mp.mpf(t0)
    h = lambda r: mp.e**(-aG*(r-t0)**2) + mp.e**(-aG*(r+t0)**2)
    g = lambda u: 2*mp.sqrt(mp.pi/aG)*mp.e**(-u*u/(4*aG))*mp.cos(t0*u)
    zeros = [mp.zetazero(k).imag for k in range(1, n_zeros + 1)]
    zero_side = 2*mp.fsum(h(z) for z in zeros)
    pole = h(mp.mpc(0, '0.5')) + h(mp.mpc(0, '-0.5'))
    arch = mp.quad(lambda r: h(r)*(mp.re(mp.digamma(mp.mpf('0.25')+mp.mpc(0,'0.5')*r))
                                   - mp.log(mp.pi)),
                   [0, t0-10, t0, t0+10, mp.inf]) / mp.pi
    prime = mp.fsum(mp.log(p)*mp.power(n, mp.mpf('-0.5'))*g(mp.log(n))
                    for n, p in sieve_prime_powers(prime_cut)) / mp.pi
    rhs = mp.re(pole) + arch - prime
    return zero_side, rhs


def family_identity(D, q, a=0.5, t_scan=40.0, prime_cut=50000, dps=22):
    """Two-sided identity for a real odd primitive character chi = (D|.), q = |D|.
    Zeros found by scanning the (real) Hardy function Z_chi built from Hurwitz zetas."""
    mp.mp.dps = dps
    def Lchi(s):
        tot = mp.mpc(0)
        for aa in range(1, q):
            c = kron(D, aa)
            if c:
                tot += c*mp.zeta(s, mp.mpf(aa)/q)
        return q**(-s)*tot
    def Z(t):
        th = (t/2)*mp.log(mp.mpf(q)/mp.pi) + mp.im(mp.loggamma(mp.mpf('0.75') + mp.mpc(0,1)*t/2))
        return mp.re(mp.e**(mp.mpc(0,1)*th)*Lchi(mp.mpf('0.5')+mp.mpc(0,1)*t))
    ts = np.arange(2.0, t_scan, 0.05)
    vals = [float(Z(mp.mpf(t))) for t in ts]
    zeros = [mp.findroot(Z, mp.mpf((ts[i]+ts[i+1])/2))
             for i in range(len(ts)-1) if vals[i]*vals[i+1] < 0]
    aG, t0 = mp.mpf(a), zeros[1]
    h = lambda r: mp.e**(-aG*(r-t0)**2) + mp.e**(-aG*(r+t0)**2)
    g = lambda u: 2*mp.sqrt(mp.pi/aG)*mp.e**(-u*u/(4*aG))*mp.cos(t0*u)
    zero_side = 2*mp.fsum(h(z) for z in zeros)
    arch = mp.quad(lambda r: h(r)*(mp.re(mp.digamma(mp.mpf('0.75')+mp.mpc(0,'0.5')*r))
                                   + mp.log(mp.mpf(q)/mp.pi)),
                   [0, t0-8, t0, t0+8, mp.inf]) / mp.pi
    prime = mp.mpf(0)
    for n, p in sieve_prime_powers(prime_cut):
        c = kron(D, p)
        if c == 0:
            continue
        e = 0
        nn = n
        while nn % p == 0:
            nn //= p; e += 1
        prime += (c**e)*mp.log(p)*mp.power(n, mp.mpf('-0.5'))*g(mp.log(n))
    rhs = arch - prime/mp.pi
    return zeros[0], zero_side, rhs


if __name__ == "__main__":
    mp.mp.dps = 18
    zs, rhs = zeta_identity(mp.zetazero(3).imag, n_zeros=12, prime_cut=30000, dps=18)
    print("zeta on gamma_3 : LHS=%s RHS=%s diff=%s" % (mp.nstr(zs, 14), mp.nstr(rhs, 14), mp.nstr(zs-rhs, 2)))
    g1, zs, rhs = family_identity(-3, 3, t_scan=38.0, prime_cut=30000, dps=16)
    print("chi mod 3      : first zero %s  diff=%s" % (mp.nstr(g1, 8), mp.nstr(zs-rhs, 2)))
    g1, zs, rhs = family_identity(-4, 4, t_scan=38.0, prime_cut=30000, dps=16)
    print("chi mod 4      : first zero %s  diff=%s" % (mp.nstr(g1, 8), mp.nstr(zs-rhs, 2)))
    # EXPECTED first zeros: 8.0397372 (mod 3), 6.0209489 (mod 4); diffs ~1e-11..1e-13
