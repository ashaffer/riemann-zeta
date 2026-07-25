"""family_experiments.py — Dirichlet-family instruments (audit #5 executed).

EXPECTED (July 26, 2026):
  cartography |D| <= 2000: min L(1,chi) at D = -163 (0.2461 = pi/sqrt(163), the
    Heegner near-miss, found blind); Chowla proximity min |L(1/2)| at D = -1411
    (0.0239), then D = 1592 (0.0323), D = -1012 (0.0487); no negative central
    values (a transient negative at D = 908 was the unfixed-Kronecker bug).
  twisted margins (m = 41): arch-only coasts to L* ~ 1.66 (q=3), 2.44 (q=4),
    1.84 (q=5), 2.69 (q=8); q = 7 and q = 11 coast beyond L = 6.
  sign ledger at q = 7, L = 4.04: arch-only +0.238; +2 (chi=+1) -> -0.584;
    +2,3 -> -0.092; full (2,3,5,7) -> +0.00158.  chi = -1 primes stabilize,
    chi = +1 primes drain; zeta is the degenerate all-plus case whose pole
    reverses the roles (see margin_experiments.mechanism_test).
"""
import numpy as np
from weil_core import kron, cdig, build_form, lam_min_of, arch_weights, hat_overlap


def is_fundamental(D):
    def squarefree(n):
        for p in range(2, int(n**0.5) + 1):
            if n % (p*p) == 0:
                return False
        return True
    if D % 4 == 1:
        return squarefree(abs(D))
    if D % 4 == 0 and (D//4) % 4 in (2, 3):
        return squarefree(abs(D)//4)
    return False


def hurwitz_em(s, x, K=25):
    """Euler-Maclaurin Hurwitz zeta, vectorized over x, for 0 < s < 1 and s = 1/2."""
    x = np.asarray(x, float)
    S = sum((x + k)**(-s) for k in range(K))
    xK = x + K
    return (S + xK**(1-s)/(s-1) + 0.5*xK**(-s) + s/12.0*xK**(-s-1)
            - s*(s+1)*(s+2)/720.0*xK**(-s-3))


def cartography(Dmax=2000):
    """L(1, chi) via the digamma formula and L(1/2, chi) via Euler-Maclaurin,
    over all fundamental |D| <= Dmax.  Returns sorted extremes."""
    neg, pos, chow = [], [], []
    for d in range(3, Dmax + 1):
        for D in (-d, d):
            if not is_fundamental(D):
                continue
            q = abs(D)
            a = np.arange(1, q)
            ch = np.array([kron(D, int(x)) for x in a], float)
            L1 = -(ch * cdig(a/q).real).sum()/q
            Lh = (ch * hurwitz_em(0.5, a/q)).sum()/np.sqrt(q)
            (neg if D < 0 else pos).append((L1, D))
            chow.append((abs(Lh), D, Lh))
    return sorted(neg), sorted(pos), sorted(chow)


def twisted_margin(L, m, D, parity, prime_set):
    """lam_min of the chi-twisted form with only the listed primes included."""
    q = abs(D)
    rg, WW = arch_weights(parity)
    Q0, G, ex = build_form(L, m, D=D, q=q, parity=parity, include_primes=False,
                           rg=rg, WW=WW)
    from weil_core import PRIME_POWERS
    P = np.zeros_like(Q0)
    for nn, p in PRIME_POWERS:
        if p in prime_set and 2*np.log(nn) < L:
            c = kron(D, nn)
            if c:
                Ps = hat_overlap(ex['Dm'] + np.log(nn), ex['d'])
                P += 2*np.log(p)*c/np.sqrt(nn)*(Ps + Ps.T)/2
    return lam_min_of(Q0 - P, G)


if __name__ == "__main__":
    neg, pos, chow = cartography(500)     # quick demo range
    print("min L(1), D<0 (|D|<=500):", [("D=%d %.4f" % (D, L)) for L, D in neg[:2]])
    # EXPECTED leader at full range 2000: D = -163, 0.2461
    print("q=7 sign ledger at L=4.04:")
    for tag, V in (("arch", set()), ("+2", {2}), ("+2,3", {2, 3}), ("full", {2, 3, 5, 7})):
        print("  %-5s %+.3e" % (tag, twisted_margin(4.04, 41, -7, 'odd', V)))
    # EXPECTED: +2.38e-01, -5.84e-01, -9.21e-02, +1.58e-03
