# Leading-frequency defect dichotomy for the balanced tower

**Date:** 2026-08-27
**Verdict:** the simultaneous leading-frequency core has an exact
zero/nonzero determinant dichotomy.  The zero branch collapses to one scalar
frequency and contains the primitive shifted-cube transition.  The nonzero
branch has bounded lane gcd and an explicit modular-inverse offset, but the
remaining incomplete inverse-discrepancy estimate is not supplied by divisor
or period bounds.  Thus this reduction does not prove the nonprincipal sector
of DRPLS.

## 1. Frozen core

Fix positive shell constants `c0,c1,C`.  Let

```text
c0*F <= a,b <= c1*F
```

and suppose that, for integers `h,r,s`,

```text
X=h*F^3/(a^2*b),       Y=h*F^3/(a*b^2),
|X-r|<=C/F,            |Y-s|<=C/F.                 (1.1)
```

At the critical balanced top one has `h~K`, where

```text
K=F^(17/8),
```

up to fixed factors.  Nothing in the algebraic dichotomy below uses that
particular value until the counting ledger in Section 5.

Define the integral rounding defect

```text
d=a*r-b*s.                                           (1.2)
```

The two unrounded frequencies obey the exact rank-one identity

```text
a*X=b*Y=h*F^3/(a*b).                                 (1.3)
```

Consequently

```text
|d|=|a*(r-X)-b*(s-Y)|
   <=C*(a+b)/F<=2*c1*C,                              (1.4)
gcd(a,b) | d.                                        (1.5)
```

Thus there are only `O_(c1,C)(1)` defect values.  If `d!=0`, then
`gcd(a,b)=O_(c1,C)(1)`.  These statements are exact; no genericity or
equidistribution has been used.

The cross cancellation in (1.3) is also machine-checked as
`leading_frequency_cross_cancellation` in
`lean/weilcert/QPSelfOrbitTowerCubicSurvival.lean`.

## 2. The zero-defect branch

Put

```text
g=gcd(a,b),       a=g*A,       b=g*B,       gcd(A,B)=1.
```

If `d=0`, then `A*r=B*s`.  Euclid's lemma gives a unique integer `t`
such that

```text
r=B*t,                 s=A*t.                       (2.1)
```

Define the common scalar frequency

```text
Theta=h*F^3/(g^3*A^2*B^2).                          (2.2)
```

Then, identically,

```text
X=B*Theta,             Y=A*Theta.                   (2.3)
```

Hence (1.1) on the zero branch is equivalent to

```text
|Theta-t| <= C/(F*max(A,B)).                         (2.4)
```

In particular, this is genuinely one scalar near-integrality condition;
there is no second independent character left.  Identity (2.3) is
machine-checked as `zero_defect_common_frequency` in the Lean file cited
above.

## 3. Exact diagonal gcd slicing

On the diagonal `a=b=u`, one has `g=u` and `A=B=1`.  Equation (2.4) becomes

```text
|h*F^3/u^3-t|<=C/F,
|h*F^3-t*u^3|<=C*u^3/F << F^2                     (3.1)
```

for `u~F`.  Let

```text
c=gcd(h,t),       h=c*B0,       t=c*A0,
gcd(A0,B0)=1.                                          (3.2)
```

Dividing (3.1) by `c` gives the primitive equation

```text
|A0*u^3-B0*F^3| << F^2/c,       gcd(A0,B0)=1.       (3.3)
```

On the previously isolated critical gcd slice

```text
c~F^(25/16),
```

the top-band sizes `h,t~K=F^(34/16)` give

```text
A0,B0~F^(9/16),
0<|A0*u^3-B0*F^3|<<F^(7/16).                        (3.4)
```

Thus the coprimality in the hostile shifted-cube gate is forced by the
exact gcd reduction; it is not an optional strengthening.  The zero
residual in (3.3) belongs to the exact principal sector.  The unresolved
transition is the nonzero residual in (3.4).

## 4. Exact normal form when `d!=0`

Continue to write `a=g*A`, `b=g*B`, and now put

```text
d=g*delta,       delta!=0,       gcd(A,B)=1.         (4.1)
```

The defect equation is

```text
A*r-B*s=delta.                                      (4.2)
```

Let `rho` be the unique residue in `[0,B)` satisfying

```text
A*rho == delta (mod B),                             (4.3)
```

and set

```text
sigma=(A*rho-delta)/B.
```

Every solution of (4.2), and no other pair, is

```text
r=rho+B*l,             s=sigma+A*l,                 (4.4)
```

for an integer `l`.  Thus the nonzero branch contains the explicit inverse
offset

```text
rho == inverse(A)*delta (mod B).                     (4.5)
```

With `Theta` as in (2.2), put

```text
v=Theta-l-rho/B.
```

Equations (1.1) are exactly

```text
|B*v|<=C/F,
|A*v+delta/B|<=C/F.                                 (4.6)
```

The displacement `delta/(A*B)` between the two rational centres has size
`asymp F^(-2)`, exactly the same scale as the two windows.  Therefore
`d!=0` does not give a power saving in either geometric sum; it only gives
the bounded gcd and inverse offset.

For an integral residual form, define

```text
Q=g^3*A^2*B^2=(a*b)^2/g,
P=Q/B=g^3*A^2*B,
E=h*F^3-Q*l-P*rho.                                  (4.7)
```

Then (4.6) is exactly

```text
|E|<=C*Q/(B*F),
|E+g^3*A*B*delta|<=C*Q/(A*F).                       (4.8)
```

Both right sides are `asymp F^2`.  Notice also that

```text
g^3*A*B*delta=a*b*d.
```

This recovers directly the difference of the two cleared residuals.

## 5. The remaining counting theorem

For `h~K`, equation (2.2) makes `l` range over an interval of length

```text
L~K/F=F^(9/8).                                      (5.1)
```

Since (4.8) has width `O(F^2)`, a necessary condition for a core point is

```text
|| (Q*l+P*rho)/F^3 || <= C1/F                       (5.2)
```

with a shell-dependent constant `C1`.  The integer `h`, if it exists, is
unique once `l` is fixed.  The natural sufficient core-counting statement
for each fixed nonzero `d` is therefore

```text
sum_(g|d) sum_(A,B~F/g, gcd(A,B)=1)
  #{l in I_(A,B):
      ||(g^3*A^2*B^2*l+g^3*A^2*B*rho)/F^3||<=C1/F,
      rho==inverse(A)*(d/g) (mod B)}
 << K*F^o(1).                                        (ID)
```

The second inequality in (4.8) may be retained in `(ID)`; dropping it only
makes the displayed statement stronger and cleaner.  There are `asymp F^2`
lane pairs, `L~K/F` candidate progression points per pair, and a window of
relative width `1/F`.  Thus the volume term in `(ID)` is exactly

```text
F^2*(K/F)*(1/F)=K.                                  (5.3)
```

Proving `(ID)` would put the large-amplitude diagonal core of the
`d!=0` sector at the DRPLS budget.  It would not, by itself, prove every
off-diagonal signed Gram term of full DRPLS.

## 6. Why period and divisor bounds do not prove `(ID)`

For one pair let

```text
w=gcd(Q,F^3),             q0=F^3/w.
```

After reduction, the progression in (5.2) has period `q0`.  Splitting an
`l` interval into complete periods plus one remainder gives only

```text
#(5.2) << L/F + L/q0 + q0/F + 1,                    (6.1)
```

or the same estimate with the endpoint term truncated by `L`.  The desired
`L/F` is the first term.  For the generic case `q0~F^3`, however, the
incomplete-block term is as large as `L`; summing it over `asymp F^2` lane
pairs is `K*F`, one full factor `F` above (5.3).  Knowing the exact period,
or bounding the number of pairs with any fixed period by divisors, does not
control where this short incomplete block lands.

Clearing the first inequality gives the equivalent divisor description

```text
h*F^3-E=a^2*b*r,
a*r-b*s=d,
|E|<<F^2.                                           (6.2)
```

If `M=a*r`, then

```text
M==0 (mod a),       M==d (mod b),
h*F^3-E=a*b*M.                                      (6.3)
```

For fixed `(h,E)`, divisor bounds give only `F^o(1)` choices for
`(a,b,M)`, but `E` has `O(F^2)` admissible values.  This yields
`K*F^(2+o(1))`, not `K*F^o(1)`.  Conversely, fixing `(a,b)` returns exactly
the incomplete rotation (5.2).  The two elementary organizations therefore
lose on opposite sides of the same discrepancy problem.

The inverse residue (4.5) is genuine additional structure and is the most
credible route to `(ID)`, possibly through a bilinear/Kloosterman-type
estimate averaged over `A` and `B`.  But merely observing that the residue
is a modular inverse supplies no cancellation in the positive count.

## 7. Binary status

```text
bounded defect d:                                  PROVED;
d!=0 implies gcd(a,b)=O(1):                        PROVED;
d=0 scalar-frequency collapse:                    PROVED;
diagonal primitive shifted-cube gcd slice:         PROVED;
d!=0 modular-inverse progression normal form:      PROVED;
period/divisor proof of the d!=0 target:            DOES NOT CLOSE;
averaged inverse-discrepancy estimate (ID):         OPEN;
nonprincipal balanced-tower DRPLS:                 OPEN;
sharp four-cycle bound:                            NOT PROVED.
```
