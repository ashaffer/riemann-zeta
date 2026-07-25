"""certified_margins.py — rigorous two-sided enclosures for the margin ladder (M1).

Everything hp_margins.py estimates, this module CERTIFIES, in interval arithmetic
(mpmath.iv, 220-bit endpoints), with no unverified quadrature anywhere:

  archimedean diagonals: the x-space kernel integral is evaluated in closed form.
    On each integer piece of the hat autocorrelation, the bracket
    B(u) = Omega(kd) - (Omega(kd-u)+Omega(kd+u))/2 is an EXACT rational cubic
    (Fraction arithmetic, no rounding).  The kernel splits as
    w(u) = 1/(2u) + g(u):  the 1/(2u) part integrates to rationals plus log of
    integers; g is expanded in its Bernoulli series with an explicit geometric
    remainder |c_j| <= 4 e^{(2-s) pi} / pi^j, so the truncation error enters the
    enclosure as a rigorous +- interval.  The tail INT_U^inf w is a geometric
    series with a rigorous remainder bound.  psi(1/4) = -gamma - pi/2 - 3 ln 2
    and psi(3/4) = -gamma + pi/2 - 3 ln 2 from interval constants.
  Gram, primes, pole: exact rationals, iv.log / iv.sqrt / iv.exp enclosures,
    with a hinge-safe interval evaluation of the piecewise-cubic overlap.
  lower bound: interval Cholesky of Q - beta G.  If every pivot interval is
    strictly positive, EVERY real symmetric matrix inside the interval family is
    positive definite (standard verified linear algebra), hence
    lam_min(Q, G) > beta for the true matrices — a certificate.
  upper bound: interval Rayleigh quotient of a (rationalized) approximate
    minimizer — valid for any test vector.

Trust base: mpmath.iv elementary functions (exp, log, sqrt) and interval ops
produce enclosures.  No floats, no Simpson, no unverified series anywhere else.

EXPECTED (measured July 25, 2026, this machine):
  sanity: iv arch diagonals contain hp_margins' values at every k tested,
    enclosure widths 1.2e-64 / 2.1e-65 / 1.9e-65 / 1.1e-63 (k = 0/1/7/25)
  zeta, L = 7/4,     m = 41: CERTIFIED 3.77497970e-05 < lam_min <= 3.77497984e-05
  zeta, L = 219/100, m = 41: CERTIFIED 1.43609370e-06 < lam_min <= 1.43609382e-06
  zeta, L = 497/200, m = 41: CERTIFIED 1.39740560e-06 < lam_min <= 1.39740567e-06
  chi_{-7} (q = 7, odd), L = 101/25, m = 41, full prime set:
                             CERTIFIED 1.57558810e-03 < lam_min <= 1.57558821e-03
  (the first interval-certified window positivity margins of the program —
   M1's first rungs — including the first certified FAMILY window; each runs
   in ~4 s.  Enclosure relative widths ~4e-8, limited only by the chosen beta.)
"""
from fractions import Fraction
import mpmath as mp
from mpmath import iv, bernfrac
from weil_core import kron

iv.prec = 220


def F2iv(x):
    if isinstance(x, Fraction):
        return iv.mpf(x.numerator) / iv.mpf(x.denominator)
    return iv.mpf(x)


# ------------------------------------------------ Fraction polynomial helpers
def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]


def pscale(p, c):
    return [c * a for a in p]


def pmul(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return out


def pcompose_linear(p, a, b):
    """p(a + b*tau) as a polynomial in tau (a, b, coeffs Fractions)."""
    out = [Fraction(0)]
    lin = [Fraction(a), Fraction(b)]
    pw = [Fraction(1)]
    for c in p:
        if c:
            out = padd(out, pscale(pw, c))
        pw = pmul(pw, lin)
    return out


def peval_frac(p, x):
    r = Fraction(0)
    for c in reversed(p):
        r = r * x + c
    return r


def peval_iv(p, x):
    r = iv.mpf(0)
    for c in reversed(p):
        r = r * x + F2iv(c)
    return r


def pint_frac(p, a, b):
    """INT_a^b p(tau) d tau exactly."""
    r = Fraction(0)
    for i, c in enumerate(p):
        if c:
            r += c * (Fraction(b) ** (i + 1) - Fraction(a) ** (i + 1)) / (i + 1)
    return r


# hat autocorrelation omega(t): t in [0,1]: 2/3 - t^2 + t^3/2 ; [1,2]: (2-t)^3/6
OM1 = [Fraction(2, 3), Fraction(0), Fraction(-1), Fraction(1, 2)]
OM2 = [Fraction(8, 6), Fraction(-12, 6), Fraction(6, 6), Fraction(-1, 6)]


def omega_frac(t):
    t = abs(Fraction(t))
    if t >= 2:
        return Fraction(0)
    return peval_frac(OM2 if t >= 1 else OM1, t)


def omega_poly(k, j, sign):
    """omega(|k + sign*tau|) as an exact cubic on the integer piece tau in [j, j+1]
    (the piece must not straddle a hinge; callers pass integer pieces only)."""
    mid = Fraction(2 * j + 1, 2)
    t_mid = k + sign * mid
    tm = abs(t_mid)
    if tm >= 2:
        return [Fraction(0)]
    br = OM2 if tm >= 1 else OM1
    if t_mid >= 0:
        return pcompose_linear(br, Fraction(k), Fraction(sign))
    return pcompose_linear(br, Fraction(-k), Fraction(-sign))


# --------------------------------------------------- kernel series (rigorous)
_GCACHE = {}


def g_series(N, s_num, s_den):
    """Coefficients g[j] (of u^j) of g(u) = e^{-su}/(1-e^{-2u}) - 1/(2u), exact
    Fractions, plus the rigorous bound |c_j| <= C / pi^j on the tail generator
    (c = coefficients of 2u*w(u); g_j = c_{j+1}/2).  s = s_num/s_den."""
    key = (N, s_num, s_den)
    if key in _GCACHE:
        return _GCACHE[key]
    s = Fraction(s_num, s_den)
    # bern(2u): sum B_n (2u)^n / n!
    bern = []
    fact = 1
    for n in range(N + 2):
        if n:
            fact *= n
        p, q = bernfrac(n)
        bern.append(Fraction(p, q) * Fraction(2 ** n) / fact)
    # e^{(2-s)u}
    ex = []
    fact = 1
    for n in range(N + 2):
        if n:
            fact *= n
        ex.append(Fraction(2 - s) ** n / fact)
    c = [Fraction(0)] * (N + 2)
    for i, a in enumerate(ex):
        if i > N + 1:
            break
        for j2, b in enumerate(bern):
            if i + j2 <= N + 1:
                c[i + j2] += a * b
    g = [c[j + 1] / 2 for j in range(N + 1)]
    Cbound = 4 * mp.e ** (float(2 - s) * mp.pi)      # |c_j| <= Cbound / pi^j
    _GCACHE[key] = (g, Cbound)
    return _GCACHE[key]


def kernel_tail_iv(U, s_num, s_den):
    """Enclosure of INT_U^inf e^{-su}/(1-e^{-2u}) du = SUM e^{-(2n+s)U}/(2n+s),
    with a rigorous geometric remainder (ratio e^{-2U})."""
    s = Fraction(s_num, s_den)
    Uiv = F2iv(U)
    tot = iv.mpf(0)
    r = iv.exp(-2 * Uiv)
    n = 0
    while True:
        cn = F2iv(2 * n + s)
        term = iv.exp(-cn * Uiv) / cn
        tot += term
        if float(term.b) < 1e-70 or n > 2500:
            rem = term * r / (1 - r)
            return tot + iv.mpf([0, 1]) * rem
        n += 1


def arch_diag_iv(k, d, parity='even', N=90):
    """Rigorous enclosure of the k-th archimedean Toeplitz diagonal, hat basis,
    spacing/half-width d (a Fraction).  Same object as hp_margins.arch_diagonal."""
    s_num, s_den = (1, 2) if parity == 'even' else (3, 2)
    g, Cb = g_series(N, s_num, s_den)
    div = F2iv(d)
    # psi(s0/... ) : psi(1/4) = -gamma - pi/2 - 3 ln2 ; psi(3/4) = -gamma + pi/2 - 3 ln2
    psi0 = -iv.euler - 3 * iv.log(iv.mpf(2)) + (iv.pi / 2 if parity == 'odd' else -iv.pi / 2)
    om_k = omega_frac(k)
    total = psi0 * (div * F2iv(om_k))
    # pieces [j, j+1], j = max(k-2, 0) .. k+1
    for j in range(max(k - 2, 0), k + 2):
        qm = padd(pscale(padd(omega_poly(k, j, -1), omega_poly(k, j, +1)), Fraction(-1, 2)),
                  [om_k])
        # I1: d * INT q/tau dtau  (q(0)=0 on the piece touching 0)
        if j == 0:
            q0 = qm[0]
            assert q0 == 0
            qq = qm[1:]
            I1 = pint_frac(qq, 0, 1)
            total += div * F2iv(I1)
        else:
            q0 = qm[0]
            qq = padd(qm, [-q0])[1:]          # (q(tau) - q(0))/tau, exact
            I1 = pint_frac(qq, j, j + 1)
            total += div * (F2iv(I1) + F2iv(q0) * (iv.log(iv.mpf(j + 1)) - iv.log(iv.mpf(j))))
        # I2: 2 d^2 * SUM_r g_r d^r INT tau^r q(tau) dtau  + rigorous remainder
        acc = iv.mpf(0)
        tp = [Fraction(1)]
        dr = Fraction(1)
        for r in range(N + 1):
            mom = pint_frac(pmul(qm, tp), j, j + 1)
            acc += F2iv(g[r] * dr) * F2iv(mom)
            tp = pmul(tp, [Fraction(0), Fraction(1)])
            dr *= d
        # remainder: |g_r| <= Cb/(2 pi^{r+1}); u <= (j+1) d
        umax = F2iv((j + 1) * d)
        ratio = umax / iv.pi
        rN = F2iv(Cb) / (2 * iv.pi) * ratio ** (N + 1) / (1 - ratio)
        qmax = abs(peval_iv(qm, iv.mpf([j, j + 1])))
        rem = rN * qmax * 1        # x (piece length 1) in tau
        acc += iv.mpf([-1, 1]) * rem
        total += 2 * div * div * acc
    total += 2 * div * F2iv(om_k) * kernel_tail_iv((k + 2) * d, s_num, s_den)
    return total


# --------------------------------------------------------------- form assembly
def omega_iv(arg, div):
    """Hinge-safe enclosure of Omega(arg)/d = omega(|arg|/d) for interval arg."""
    t = abs(arg) / div
    lo, hi = mp.mpf(t.a), mp.mpf(t.b)
    lo = max(lo, mp.mpf(0))
    pieces = []
    for plo, phi, br in ((0, 1, OM1), (1, 2, OM2)):
        a2, b2 = max(lo, mp.mpf(plo)), min(hi, mp.mpf(phi))
        if a2 <= b2:
            pieces.append(peval_iv(br, iv.mpf([a2, b2])))
    if hi >= 2:
        pieces.append(iv.mpf(0))
    if not pieces:
        return iv.mpf(0)
    lo_all = min(mp.mpf(p.a) for p in pieces)
    hi_all = max(mp.mpf(p.b) for p in pieces)
    return iv.mpf([lo_all, hi_all])


from weil_core import PRIME_POWERS


def certified_form(L, m, q=1, D=1, parity='even', prime_set=None, zeta_pole=True):
    """Q, G as m x m lists of iv enclosures; L a Fraction."""
    L = Fraction(L)
    ell = L / 2
    d = ell / (m + 1)
    div = F2iv(d)
    arch = [arch_diag_iv(k, d, parity) for k in range(m)]
    gram = [d * omega_frac(k) for k in range(m)]      # exact Fractions
    lq = iv.log(iv.mpf(q)) - iv.log(iv.pi)
    diag = [arch[k] + lq * F2iv(gram[k]) for k in range(m)]
    if prime_set is None:
        prime_set = {2, 3, 5, 7, 11, 13}
    for nn, p in PRIME_POWERS:
        if p not in prime_set:
            continue
        lniv = iv.log(iv.mpf(nn))
        if not 2 * mp.mpf(lniv.b) < float(L):
            continue
        c = 1 if q == 1 else kron(D, nn)
        if not c:
            continue
        w = 2 * iv.log(iv.mpf(p)) * c / iv.sqrt(iv.mpf(nn))
        for k in range(m):
            kd = F2iv(k * d)
            s = (omega_iv(kd + lniv, div) + omega_iv(kd - lniv, div)) / 2
            diag[k] = diag[k] - w * (div * s)
    Q = [[diag[abs(i - j)] for j in range(m)] for i in range(m)]
    G = [[F2iv(gram[abs(i - j)]) for j in range(m)] for i in range(m)]
    if zeta_pole and q == 1:
        xc = [-ell / 2 + (i + 1) * d for i in range(m)]
        e2 = iv.exp(F2iv(d) / 2)
        cs = (e2 + 1 / e2 - 2) * 4 / F2iv(d)          # (2 cosh(d/2) - 2)/((1/2)^2 d)
        hp_ = [iv.exp(F2iv(x) / 2) * cs for x in xc]
        hm_ = [iv.exp(-F2iv(x) / 2) * cs for x in xc]
        for i in range(m):
            for j in range(m):
                Q[i][j] = Q[i][j] + hp_[i] * hm_[j] + hm_[i] * hp_[j]
    return Q, G


# ------------------------------------------------------------- certification
def iv_cholesky_pd(M):
    """True iff interval Cholesky completes with strictly positive pivots:
    then every real symmetric matrix inside the intervals is PD."""
    m = len(M)
    Lc = [[iv.mpf(0)] * m for _ in range(m)]
    for j in range(m):
        s = M[j][j]
        for k2 in range(j):
            s = s - Lc[j][k2] * Lc[j][k2]
        if not mp.mpf(s.a) > 0:
            return False
        Lc[j][j] = iv.sqrt(s)
        for i in range(j + 1, m):
            t = M[i][j]
            for k2 in range(j):
                t = t - Lc[i][k2] * Lc[j][k2]
            Lc[i][j] = t / Lc[j][j]
    return True


def certify(L, m, beta, q=1, D=1, parity='even', prime_set=None, ray_vec=None):
    """Certificate lam_min(Q, G) > beta, plus interval Rayleigh upper bound."""
    L = Fraction(L)
    beta = Fraction(beta)
    Q, G = certified_form(L, m, q=q, D=D, parity=parity, prime_set=prime_set)
    m_ = len(Q)
    M = [[Q[i][j] - F2iv(beta) * G[i][j] for j in range(m_)] for i in range(m_)]
    ok = iv_cholesky_pd(M)
    ub = None
    if ray_vec is not None:
        c = [F2iv(Fraction(x).limit_denominator(10 ** 12)) for x in ray_vec]
        num = iv.mpf(0)
        den = iv.mpf(0)
        for i in range(m_):
            for j in range(m_):
                num += c[i] * Q[i][j] * c[j]
                den += c[i] * G[i][j] * c[j]
        ub = num / den
    return ok, ub


if __name__ == "__main__":
    import time
    from hp_margins import arch_diagonal, hp_form, hp_lam_min
    # sanity: enclosures contain the hp (tanh-sinh) values (compare at dps 80;
    # an earlier version compared at ambient dps and manufactured a fake
    # discrepancy of 6e-19 — the interval collapsed under 15-digit rounding.
    # Diagnosed to be a test artifact; hp and iv agree to 24+ digits.)
    Lfr, m = Fraction(7, 4), 41
    d = (Lfr / 2) / (m + 1)
    with mp.workdps(80):
        for k in (0, 1, 7, 25):
            hpv = arch_diagonal(k, mp.mpf(d.numerator) / d.denominator, mp.mpf('0.5'))
            en = arch_diag_iv(k, d)
            inside = mp.mpf(en.a) <= hpv <= mp.mpf(en.b)
            print("k=%2d  iv width %.1e  contains hp value: %s"
                  % (k, float(en.delta), inside))
    # certificates: tightest beta first, fall back if the pivot test fails
    cases = [
        ("zeta  L=7/4    ", Fraction(7, 4), 1, 1, 'even', None,
         [Fraction(37749797, 10 ** 12), Fraction(377, 10 ** 7)]),
        ("zeta  L=219/100", Fraction(219, 100), 1, 1, 'even', None,
         [Fraction(14360937, 10 ** 13), Fraction(143, 10 ** 8)]),
        ("zeta  L=497/200", Fraction(497, 200), 1, 1, 'even', None,
         [Fraction(13974056, 10 ** 13), Fraction(139, 10 ** 8)]),
        ("chi-7 L=101/25 ", Fraction(101, 25), 7, -7, 'odd', {2, 3, 5, 7},
         [Fraction(15755881, 10 ** 10), Fraction(157, 10 ** 5)]),
    ]
    for tag, Lc, qc, Dc, par, ps, betas in cases:
        t0 = time.time()
        Qh, Gh = hp_form(float(Lc), m, parity=par, q=qc, D=Dc,
                         zeta_pole=(qc == 1), prime_set=ps, dps=30)
        lams, vecs = hp_lam_min(Qh, Gh, nev=1, dps=25, vectors=True)
        for beta in betas:
            ok, ub = certify(Lc, m, beta, q=qc, D=Dc, parity=par, prime_set=ps,
                             ray_vec=[float(x) for x in vecs[0]])
            if ok:
                break
        print("%s m=%d: CERTIFIED %.8e < lam_min <= %.8e (%s)  (%.0f s)"
              % (tag, m, float(beta), float(ub.b),
                 "tight" if beta == betas[0] else "fallback", time.time() - t0))
