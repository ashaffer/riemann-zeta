"""precision_law_test.py — minimal interval precision for a certified rung
(PLAN-numerical-analysis.md, Lemma 3 stress test).

Question: the repo certifies the zeta L = 711/200, m = 40 rung (lam_min ~
1.7997e-20) at iv.prec = 220 bits.  Lemma 3's two-term precision law says the
minimal working precision is

    p_min ~ log2(1/lam) + log2(kappa_asm(m)) + O(log m),

with log2(1/lam) = 65.7 bits and kappa_asm the conditioning of the exact-
rational assembly (Horner evaluation of the universal F_kj polynomials, whose
coefficients grow like 4^deg in the unnormalized Legendre basis, deg <= 79 at
m = 40).  A naive model (kappa_asm ~ 1) predicts p_min ~ 80; the coefficient-
growth model predicts a large overhead, p_min well above 100.

MEASURED (2026-07-26, this machine; certify_spectral(711/200, 40, 17997e-24),
lower-bound interval Cholesky only, N = 400):
    prec 220 bits: True   (31 s)
    prec 190 bits: True   (34 s)
    prec 160 bits: False  (9 s)
    prec 145 bits: False
    prec 130 bits: False
    prec 100 bits: False
    prec  88 bits: False
    prec  76 bits: False
    prec  64 bits: False
  => p_min in (160, 190] bits: assembly-conditioning overhead of 95-125 bits
     above the 66-bit eigenvalue scale, i.e. log2 kappa_asm ~ (2.4-3.1) * m.
  The naive model is refuted; the coefficient-growth model is confirmed.
  Consequence: a compensated / orthonormal-scaled certified assembly would
  reduce p_min toward ~ 80 bits at this rung — a 2.5x precision saving.
"""
import sys
import os
import time
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'src'))
import certified_spectral as cs          # noqa: E402
from mpmath import iv                    # noqa: E402

if __name__ == '__main__':
    L, m, beta = Fraction(711, 200), 40, Fraction(17997, 10 ** 24)
    for prec in (220, 190, 160, 145, 130, 100, 88, 76, 64):
        iv.prec = prec
        t0 = time.time()
        ok, _ = cs.certify_spectral(L, m, beta)
        print('prec %3d bits: certified lower bound %s  (%.0f s)'
              % (prec, ok, time.time() - t0))
