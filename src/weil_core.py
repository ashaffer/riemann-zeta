"""weil_core.py — shared primitives for the truncated Weil quadratic form.

Conventions were certified against the two-sided Guinand-Weil identity (oracle.py):
  sum_rho h(gamma) = h(i/2) + h(-i/2)                                [zeta pole; absent for chi]
                   + (1/2pi) INT h(r) [Re psi(1/4 + a/2 + ir/2) + log(q/pi)] dr
                   - (1/pi) SUM Lambda(n) chi(n) n^{-1/2} g(log n),
with g(u) = INT h(r) e^{-iur} dr, a = 0 (even chi / zeta) or 1 (odd chi), q = 1 for zeta.
Quadratic form: h = |phihat|^2, prime term = 2 SUM Lambda(n) chi(n) n^{-1/2} psi_phi(log n),
pole term = 2 (INT phi e^{x/2})(INT phi e^{-x/2}).

Certified: zeta identity to 1.5e-29; chi mod 3 and mod 4 to ~1e-22 (see oracle.py).
"""
import numpy as np


def cdig(z):
    """Complex digamma, vectorized: 14-step recurrence + asymptotic series.
    Accuracy ~1e-13 for Re z >= 0.25 arguments used here."""
    z = np.asarray(z, complex)
    s = np.zeros_like(z)
    for k in range(14):
        s += 1.0 / (z + k)
    w = z + 14
    ps = np.log(w) - 0.5 / w
    B = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6]
    zi = 1.0 / (w * w)
    t = zi.copy()
    for n, b in enumerate(B, 1):
        ps -= b / (2 * n) * t
        t *= zi
    return ps - s


def hatFT(r, xc, d):
    """Fourier transforms of unit hat functions of half-width d at centers xc.
    FT convention: phihat(r) = INT phi(x) e^{-irx} dx = d sinc^2(rd/2) e^{-ir xc}."""
    r = np.asarray(r, float)
    rr = r[:, None] * d / 2
    s2 = np.where(np.abs(rr) < 1e-12, 1.0,
                  (np.sin(rr) / np.where(np.abs(rr) < 1e-12, 1, rr)) ** 2)
    return d * s2 * np.exp(-1j * r[:, None] * xc[None, :])


def hat_overlap(dv, d):
    """INT hat(x - a) hat(x - b) dx as a function of center distance |a-b| = t*d.
    Exact piecewise cubic; equals 2d/3 at t = 0, d/6 at t = 1, 0 for t >= 2."""
    t = np.abs(dv) / d
    return d * np.where(t <= 1, 2/3 - t*t + t**3/2,
                        np.where(t <= 2, (2 - t)**3 / 6, 0.0))


def kron(D, n):
    """Kronecker symbol (D|n) for n >= 0.  FIXED version: the (even D, even n) -> 0
    check precedes stripping factors of 2 from n.  The unfixed order manufactured a
    fake negative central value (fake GRH disproof) -- see PROGRAM.md 2.9."""
    if n == 0:
        return 1 if abs(D) == 1 else 0
    if D % 2 == 0 and n % 2 == 0:
        return 0
    r = 1
    while n % 4 == 0:
        n //= 4
    if n % 2 == 0:
        n //= 2
        if D % 8 in (3, 5):
            r = -r
    a = D % n
    while a != 0:
        while a % 4 == 0:
            a //= 4
        if a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a, n = n % a, a
    return r if n == 1 else 0


def arch_weights(parity='even', R=3000.0, K=240000):
    """Simpson-weighted archimedean integrand samples W(r_i) * w_i on [0, R].
    parity 'even': Re psi(1/4 + ir/2) (zeta, even chi); 'odd': Re psi(3/4 + ir/2).
    The log(q/pi) constant is added separately (it multiplies the Gram matrix).
    NOTE: trapezoid at K=60000 produced a 1.5% error that faked a disproof of RH;
    Simpson at these parameters passed the zero-side oracle. See PROGRAM.md 2.6."""
    rg = np.linspace(1e-9, R, K + 1)
    h = rg[1] - rg[0]
    wS = np.ones(K + 1)
    wS[1:-1:2] = 4
    wS[2:-1:2] = 2
    wS *= h / 3
    shift = 0.25 if parity == 'even' else 0.75
    return rg, (cdig(shift + 0.5j * rg).real) * wS


# prime powers used in the truncated forms (n, underlying prime); n <= 64 covers
# supports L < 2 log 64 = 8.3 (every use is gated by 2 log n < L, so extending
# the table never changes a result at smaller support)
PRIME_POWERS = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3), (11, 11),
                (13, 13), (16, 2), (17, 17), (19, 19), (23, 23), (25, 5), (27, 3),
                (29, 29), (31, 31), (32, 2), (37, 37), (41, 41), (43, 43), (47, 47),
                (49, 7), (53, 53), (59, 59), (61, 61), (64, 2)]


def build_form(L, m, D=1, q=1, parity='even', include_primes=True,
               rg=None, WW=None, R=3000.0, K=240000):
    """Assemble the truncated Weil form on m interior hat functions of support
    [-L/4, L/4] (so the autocorrelation, hence prime sensitivity, reaches |u| < L/2:
    prime power n enters when L > 2 log n).

    D, q: Kronecker discriminant and conductor (D=q=1 with parity 'even' = zeta,
    which also switches on the pole term).  Returns (Q, G, extras) in the hat basis;
    generalized eigenproblem Q v = lam G v.  lam_min via lam_min_of()."""
    if rg is None or WW is None:
        rg, WW = arch_weights(parity, R, K)
    ell = L / 2
    d = ell / (m + 1)
    xc = np.linspace(-ell/2 + d, ell/2 - d, m)
    Dm = xc[None, :] - xc[:, None]
    G = hat_overlap(Dm, d)
    A = np.zeros((m, m))
    step = 40000
    for i in range(0, len(rg), step):
        E = hatFT(rg[i:i+step], xc, d)
        A += ((E * WW[i:i+step][:, None]).conj().T @ E).real
    Q = A / np.pi + np.log(q / np.pi) * G
    if q == 1:  # zeta: pole term, exact hat transforms INT hat e^{+-x/2}
        s = 0.5
        hp = np.exp(s * xc) * (2 * np.cosh(s * d) - 2) / (s * s * d)
        hm = np.exp(-s * xc) * (2 * np.cosh(s * d) - 2) / (s * s * d)
        Q += np.outer(hp, hm) + np.outer(hm, hp)
    P = np.zeros((m, m))
    for nn, p in PRIME_POWERS:
        if 2 * np.log(nn) < L:
            c = 1 if q == 1 else kron(D, nn)
            if c:
                Ps = hat_overlap(Dm + np.log(nn), d)
                P += 2 * np.log(p) * c / np.sqrt(nn) * (Ps + Ps.T) / 2
    if include_primes:
        Q = Q - P
    return Q, G, {'P': P, 'xc': xc, 'd': d, 'Dm': Dm}


def lam_min_of(Q, G, k=1):
    """Smallest k generalized eigenvalues of (Q, G) via Cholesky reduction.
    Rayleigh-Ritz: these are UPPER bounds on the true operator minima."""
    Lc = np.linalg.cholesky(G)
    Li = np.linalg.inv(Lc)
    w = np.linalg.eigvalsh(Li @ Q @ Li.T)
    return w[:k] if k > 1 else w[0]
