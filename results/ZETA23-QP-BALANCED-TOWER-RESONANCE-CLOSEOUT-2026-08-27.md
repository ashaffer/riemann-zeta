# Balanced-tower resonance closeout

**Date:** 2026-08-27

## Verdict

The sharp four-cycle bound is **not proved**.  This attack does, however,
close the exact-alias and exact-principal sectors at the sharp dyadic scale
and reduce every remaining large simultaneous linear resonance to two
explicit nonprincipal arithmetic problems.

For

```text
F=N^8, R=N^25, q=2FR, K=R/F,
```

the packet moment budget is

```text
q^2/K asymp K F^4.                                    (0.1)
```

## 1. Sectors now closed

### Exact reciprocal aliases

The reduced key

```text
kappa_T(w)=(w/gcd(w,T), (T/gcd(w,T)) mod (w/gcd(w,T)))
```

classifies `e(T/w)` exactly.  Each key has `q^o(1)` cells, so its Gram
matrix is a disjoint union of all-one blocks of subpolynomial size.  This
gives the mask-sensitive sharp estimate for arbitrary cell coefficients.

### Exact principal linear resonances

For a lane pair `(a,b)`, put

```text
d_F(a,b)=lcm(a^2*b/gcd(a^2*b,F^3),
             a*b^2/gcd(a*b^2,F^3)).                   (1.1)
```

At any height `h`, only `q^o(1)` packets satisfy `d_F(a,b)|h`.  Pointwise
Cauchy--Schwarz therefore proves the vector-valued principal estimate at
the budget (0.1).  The carrier imposes no additional congruence.

The stronger principal-hinge Schur row is also closed uniformly:

```text
sum_(c asymp F)
 gcd(d1,d_F(b,c))/sqrt(d1*d_F(b,c))
 <= C*3^omega(F*b*d1)*tau(F*b*d1)=F^o(1)             (1.2)
```

for `b asymp F` and `d1<=F^O(1)`.

## 2. Exact nonprincipal dichotomy

Choose nearest integers `r,s` to

```text
h*F^3/(a^2*b),             h*F^3/(a*b^2)
```

within `C/F`, and set

```text
d=a*r-b*s.                                             (2.1)
```

Then

```text
|d|=O(1),                  gcd(a,b)|d.                 (2.2)
```

This leaves two branches.

### Zero defect

Write `a=g*A`, `b=g*B`, `(A,B)=1`.  If `d=0`, then

```text
r=B*t, s=A*t,
||h*F^3/(g^3*A^2*B^2)|| <= C/(F*max(A,B)).             (2.3)
```

On the diagonal and on the critical gcd slice, (2.3) becomes exactly

```text
A0*u^3-B0*F^3=Delta,
gcd(A0,B0)=1,
A0,B0 asymp F^(9/16), 0<|Delta|<<F^(7/16).             (2.4)
```

Thus coprimality is mandatory.  The previously used raw nonprimitive count
was the wrong quantifier.

### Nonzero defect

Now `g=gcd(a,b)=O(1)`.  With `delta=d/g`, every solution has

```text
r=rho+B*l,
rho == inverse(A)*delta (mod B).                       (2.5)
```

The remaining positive core is an averaged incomplete rational rotation:

```text
||(g^3*A^2*B^2*l+g^3*A^2*B*rho)/F^3|| <= C/F.          (2.6)
```

Its volume is exactly `K`; complete-period bounds give `K*F`, and residual
enumeration gives `K*F^2`.  The inverse offset in (2.5), not divisor
multiplicity, is the unused structure.

## 3. Shifted-cube audit

For the primitive transition (2.4):

- all solutions over one fixed `u` lie on one scalar ray, so the primitive
  slice has at most one coefficient pair per `u`;
- for distinct inputs, the coefficient determinant is
  `asymp F^(1/8)*|u2-u1|`, so it is not uniformly bounded;
- eliminating a shared coefficient produces another shifted-cube equation
  with the same coefficient, input, and residual scales, so determinant
  iteration does not descend;
- for prime base, the first nontrivial lift is a constrained
  Fermat-quotient incidence modulo `p^2`, not a bounded-degree finite-field
  phase.

The fully checked Huxley-II input gives primitive exponent `17/24`, versus
the required `9/16`.  The often-quoted primitive `5/8` exponent depends on
an as-yet-unverified application of Huxley IV to the integral cubic.  For
the literal raw nonprimitive count, a correct content decomposition gives
the unconditional exponent `25/32`; that raw count is not the critical
top-slice statement.

## 4. Credible closing theorem

The best remaining route is a **signed, two-index nonprincipal large
sieve**, not a coefficient-blind positive count.  It must use both pieces of
the dichotomy simultaneously:

1. modular-inverse cancellation in (2.5)--(2.6) when `d!=0`;
2. scalar reciprocal-cube/Fermat-quotient cancellation when `d=0`.

A positive proof may instead establish the primitive estimate (2.4) and
the inverse-discrepancy estimate (2.6) separately, but neither estimate is
currently proved.  Exact aliases, rational hinges, gcd rigidity, and
determinant iteration no longer conceal an elementary shortcut.

## 5. Status ledger

```text
exact reciprocal aliases:                    PROVED AT SHARP SCALE;
exact principal vector theorem:              PROVED AT SHARP SCALE;
uniform principal-hinge weighted degree:     PROVED;
zero/nonzero defect dichotomy:                PROVED;
primitive shifted-cube aggregation:          OPEN;
nonzero-defect inverse discrepancy:          OPEN;
full nonprincipal DRPLS:                      OPEN;
sharp four-cycle bound:                      NOT PROVED.
```

The algebraic identities are certified in
`lean/weilcert/QPSelfOrbitTowerCubicSurvival.lean`.  The detailed proofs are
in the companion exact-alias, weighted-degree, defect-dichotomy, and
shifted-cube audit reports dated 2026-08-27.
