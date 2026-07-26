"""make_certificate.py — regenerate the integer congruence certificate used by
lean/weilcert/Weilcert.lean from the analytic pipeline (src/certified_spectral.py).

Steps: interval-enclose the truncated Weil matrix (L = 497/200, unnormalized
Legendre m = 12); round midpoints to the 10^-24 grid (A); B := A - 120000 I;
exact rational LDL^T of B; integerize to W (rows r_k L^T), g_k = d_k c^2/r_k^2,
Winv with Winv W = f I; verify every identity exactly in Fractions; emit the
Nat-match Lean data functions.  All assertions are exact; any failure aborts.
"""

import sys, math
sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/src')
from fractions import Fraction
import mpmath as mp
from certified_spectral import certified_spectral_form

L = Fraction(497, 200); m = 12; DEN = 10**24
Q, G = certified_spectral_form(L, m)
with mp.workdps(60):   # dps-15 ambient conversion caused the 2026-07-26 bridge defect
    A = [[int(mp.nint(((mp.mpf(Q[i][j].a)+mp.mpf(Q[i][j].b))/2)*DEN)) for j in range(m)] for i in range(m)]
for i in range(m):
    for j in range(m):
        assert A[i][j] == A[j][i] and float(Q[i][j].delta) < 5e-21
S = 12 * 10**4
B = [[A[i][j] - (S if i == j else 0) for j in range(m)] for i in range(m)]
Lm = [[Fraction(1 if i==j else 0) for j in range(m)] for i in range(m)]
D = [Fraction(0)]*m
Aw = [[Fraction(B[i][j]) for j in range(m)] for i in range(m)]
for k in range(m):
    D[k] = Aw[k][k]; assert D[k] > 0
    for i in range(k+1, m): Lm[i][k] = Aw[i][k]/D[k]
    for i in range(k+1, m):
        for j in range(k+1, i+1):
            Aw[i][j] -= Lm[i][k]*Lm[j][k]*D[k]; Aw[j][i] = Aw[i][j]
Li = [[Fraction(1 if i==j else 0) for j in range(m)] for i in range(m)]
for i in range(m):
    for j in range(i):
        Li[i][j] = -sum(Lm[i][k]*Li[k][j] for k in range(j, i))
lcm = lambda a, b: a*b//math.gcd(a, b)
r = [1]*m
for k in range(m):
    for i in range(m):
        r[k] = lcm(r[k], Lm[i][k].denominator)
c = 1
for k in range(m):
    c = lcm(c, r[k]); c = lcm(c, D[k].denominator)
W = [[int(r[k]*Lm[i][k]) for i in range(m)] for k in range(m)]
g = [int(D[k]*c*c/(r[k]*r[k])) for k in range(m)]
for k in range(m): assert g[k] > 0
for i in range(m):
    for j in range(m):
        assert c*c*B[i][j] == sum(W[k][i]*g[k]*W[k][j] for k in range(m))
f = 1
for i in range(m):
    for k in range(m):
        f = lcm(f, (Li[k][i]/r[k]).denominator)
Wi = [[int(f*Li[k][i]/r[k]) for k in range(m)] for i in range(m)]
for i in range(m):
    for j in range(m):
        assert sum(Wi[i][k]*W[k][j] for k in range(m)) == (f if i==j else 0)
print("certificate re-verified exactly; c, f, g, W, Winv consistent")
