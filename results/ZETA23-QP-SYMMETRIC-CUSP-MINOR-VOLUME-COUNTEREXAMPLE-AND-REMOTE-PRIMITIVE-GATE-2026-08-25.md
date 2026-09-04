# QP symmetric cusp: false pure volume, translated tangents, and the remote primitive gate

**Date:** 2026-08-25  
**Verdict:** deleting only the common-product locus `n=0` and the exact cubic
`L=0` does **not** leave a pure `AB/Q` minor arc.  There is an infinite exact
family with `nL!=0` in the Fejer compact core while `AB/Q` tends to zero by a
fixed power.

The family is not a counterexample to the desired special-curve theorem.  It
lies on the secondary translated tangent `r=s`.  The whole `r=s` sector, and
in fact the whole sufficiently small-`rho` sector, fits inside the existing
`sqrt(A)` packet budget.  After removing it, every surviving point has
power-sized displacement and power-sized primitive denominator.  Bounding
those remote points by `(1+AB/Q)Q^o(1)` remains open.

No sharp four-cycle theorem is proved here.

## 1. Exact primitive coordinates

At `C=Q^2` and `S=2Q`, write

```text
a=Q+y,            v=Q-y+r,
b=Q-y,            w=Q+y+s,                            (1.1)
e=r(Q+y)-y^2,     f=s(Q-y)-y^2,
|e|<=A<=B,        |f|<=B.
```

Put

```text
rho=r+s,          kappa=s-r,
sigma=e+f,        tau=e-f.                             (1.2)
```

Direct elimination gives

```text
y*rho=Q*kappa+tau,
Q*rho-y*kappa=2y^2+sigma,                              (1.3)

Q*L=sigma*rho^2+tau*kappa*(rho+4Q)+2tau^2,
L=rho^3-kappa^2*(rho+2Q).                              (1.4)
```

For a nonsingular point put

```text
g=gcd(rho,kappa),       rho=g*p,       kappa=g*d,
gcd(p,d)=1.                                                (1.5)
```

Equation (1.3) shows that `g|tau`; writing `tau=g*n` gives

```text
p*y-Q*d=n.                                             (1.6)
```

The cubic has an exact square-content factor:

```text
L=g^2*T,
T=g*p*(p^2-d^2)-2Q*d^2,                               (1.7)

Q*T=sigma*p^2+n*d*(g*p+4Q)+2n^2.                      (1.8)
```

Thus `n` and `T` are the correct divided minor labels.  Neither may be
discarded, but their being nonzero is not by itself a minor-arc condition.

## 2. Exact counterexample to the proposed pure volume term

Let `Y>=4` and take

```text
Q=Y(Y-1),          y=Y,          r=s=1.                (2.1)
```

Then

```text
e=Q+Y-Y^2=0,       f=Q-Y-Y^2=-2Y.                     (2.2)
```

The primitive data are

```text
rho=2,   kappa=0,   g=2,   p=1,   d=0,
tau=2Y,  n=Y,       L=8,   T=2.                       (2.3)
```

In particular `nL!=0`.  Now choose the project-scale widths

```text
A=ceil(Q^(16/33)),          B=2Y.                      (2.4)
```

Since `Y=Q^(1/2+o(1))`,

```text
A*B/Q=Q^(-1/66+o(1)).                                 (2.5)
```

For every fixed `epsilon<1/66`, the alleged upper bound

```text
#minor <<(A*B/Q)*Q^epsilon                             (2.6)
```

tends to zero, although (2.1) supplies one point.  Hence (2.6) is false.

This example lies genuinely inside the unresolved Fejer core.  With
`D=Q^(16/33)`, it has

```text
A=D,       B=D^(33/32+o(1)),
U=1,       V=D^(1/32+o(1)),
U*V^2=D^(1/16+o(1))<sqrt(D).                           (2.7)
```

The missing additive `1` is therefore not a boundary convention outside the
application.

## 3. Why the family is a secondary translated tangent

More generally, `kappa=0` means `r=s=j`.  The four physical coordinates are

```text
(a,b,v,w)
 =(Q+y,Q-y,Q-y+j,Q+y+j).                              (3.1)
```

For fixed `(Q,j)` this is the affine rank-one line of direction

```text
(1,-1,-1,1).                                           (3.2)
```

It is the usual swapped tangent with both carrier coordinates translated by
the same integer `j`.  Its errors are

```text
e=j(Q+y)-y^2,          f=j(Q-y)-y^2.                  (3.3)
```

Thus

```text
2j|y|=|e-f|<=A+B<=2B,                                 (3.4)
```

and the first, narrower band gives

```text
|j(Q+y)-y^2|<=A.                                      (3.5)
```

For `j>0`, (3.4)--(3.5) imply

```text
j<<J:=1+(B^2/Q)^(1/3).                                (3.6)
```

For each fixed `j`, completing the square in (3.5) gives

```text
|(2y-j)^2-(j^2+4jQ)|<=4A,                             (3.7)
```

so square spacing bounds the number of `y` by

```text
O(1+A/sqrt(jQ)).                                       (3.8)
```

For `j=0`, both errors equal `-y^2`, so there are `O(sqrt(A))` points;
this is also the singular common-product packet.  Summing (3.8) for `j>0`
and then restoring `j=0` yields the rigorous secondary-packet bound

```text
# {kappa=0}
 <<sqrt(A)+J+A*sqrt(J/Q).                             (3.9)
```

In the compact core write

```text
Q=D^(33/16),       A=D*m,       B=D*M,
1<=m<=M,           m*M^2<sqrt(D).                     (3.10)
```

Then `M<D^(1/4)`, and the deliberately independent worst-case bounds give

```text
J<<D^(7/48),
A*sqrt(J/Q)<<D^(5/24),
sqrt(A)>=D^(1/2).                                     (3.11)
```

Therefore

```text
# {kappa=0}<<sqrt(A).                                 (3.12)
```

The family in Section 2 is an isolated point on this already affordable
secondary packet.  It refutes the proposed *classification*, not the final
square-root estimate.

## 4. Every sufficiently small `rho` is on that packet

Fix a compact collar

```text
|y|<=eta*Q,             eta<1,                         (4.1)
```

and let `A,B=o(Q)`.  The two error equations force `r,s>=0` for large `Q`,
so

```text
|kappa|<=rho.                                           (4.2)
```

From the second equation in (1.3),

```text
y^2<<Q*rho+B.                                          (4.3)
```

Consequently, for a sufficiently small collar-dependent constant `c>0`
and all sufficiently large `Q`,

```text
rho<=c*Q^(1/3)
 => |y*rho|+|tau|<Q.                                   (4.4)
```

Here the compact core bound `B<=D^(5/4)=Q^(20/33)` is more than enough for
the terms involving `B` in (4.3)--(4.4).  Since

```text
Q*kappa=y*rho-tau                                      (4.5)
```

and `kappa` is integral, (4.4) forces

```text
kappa=0.                                               (4.6)
```

Combining (4.6) with (3.12) proves

> **Small-height theorem.** Uniformly throughout the Fejer compact core,
> all points with `rho<=cQ^(1/3)` contribute `O(sqrt(A))`.

This is the corrected major arc: it contains `nL!=0` points and is strictly
larger than the union of `n=0` and `L=0`.

## 5. A separate narrow-shift square-spacing lemma

There is also a useful one-coordinate statement.  For fixed `r`,

```text
|(2y-r)^2-(r^2+4Qr)|<=4A.                             (5.1)
```

When `1<=r<=R` and `A=o(Q)`, square spacing gives

```text
#y for this r <<1+A/sqrt(Qr).                          (5.2)
```

Including `r=0` and summing,

```text
# {0<=r<=R}
 <<sqrt(A)+R+A*sqrt(R/Q).                              (5.3)
```

Here the count is a count of full points: once `y` is fixed, the second
band determines at most one integer `s`, since its interval has length
`2B/(Q-y)<1` for all sufficiently large `Q` in the fixed compact collar.

Taking `R=sqrt(A)` and using

```text
A<=D^(7/6)=Q^(56/99)<Q^(2/3)                          (5.4)
```

shows that every point with `r<=sqrt(A)` also costs only
`O(sqrt(A))`.  This lemma does not use the cubic and is useful for absorbing
finite endpoint fragments of the small-height decomposition.

## 6. The two original major arcs remain affordable

If `n=0`, then `tau=e-f=0`, so the two products are equal.  The established
common-product parametrization gives

```text
# {n=0}<<sqrt(A)*Q^o(1).                              (6.1)
```

If `L=0` and `rho>0`, (1.7) gives

```text
g*p*(p^2-d^2)=2Q*d^2.                                 (6.2)
```

Since `(p,d)=1`, one has `d^2|g`; writing `g=h*d^2` yields

```text
h*p*(p^2-d^2)=2Q.                                     (6.3)
```

There are only `Q^o(1)` triples `(h,p,d)` by divisor enumeration.  For each
fixed direction the first quadratic band contains at most
`O(1+sqrt(A))` integral `y`.  Therefore

```text
# {L=0}<<sqrt(A)*Q^o(1).                              (6.4)
```

Notice that `L=0` alone does not force `y=Qd/p`; that equality is the further
condition `n=0`.  The count (6.4) retains the possible nonzero error
determinant `n`.

## 7. Exact remote primitive reduction

After paying (3.12), (5.3), (6.1), and (6.4), a surviving point may be
assumed to satisfy

```text
n!=0,       L!=0,       kappa!=0,
rho>>Q^(1/3),           r>sqrt(A).                    (7.1)
```

Conversely, the two product equations give

```text
rho<<y^2/Q+B/Q.                                       (7.2a)
```

Together with `rho>>Q^(1/3)`, this gives

```text
|y|>>Q^(2/3).                                          (7.2b)
```

There are two further exact height restrictions.  Since `tau=g*n` and
`n!=0`,

```text
g<=|tau|<=A+B<=2B.                                    (7.3)
```

Also `d!=0`.  From (1.6), compactness, and `B=o(Q)`,

```text
|y|>>Q*|d|/p.                                         (7.4)
```

The second equation in (1.3), together with `y^2>>B`, gives

```text
y^2<<g*Q*p<<B*Q*p.                                    (7.5)
```

Combining (7.4)--(7.5),

```text
p^3>>Q*d^2/B,
p>>(Q/B)^(1/3).                                        (7.6)
```

At the worst unbalanced endpoint `B<D^(5/4)`, this is

```text
p>>D^(13/48).                                          (7.7)
```

Thus every bounded or subpower primitive direction has been removed.  The
remaining rational approximation is literally

```text
|d/p-y/Q|=|n|/(Qp)<=2B/(Q*rho),                        (7.8)
```

and the nonzero cubic height is

```text
T=g*p*(p^2-d^2)-2Q*d^2!=0.                            (7.9)
```

The unresolved theorem can now be stated without misclassifying translated
tangents:

```text
# {points satisfying (7.1)}
 <<(1+A*B/Q)*Q^o(1).                                  (7.10)
```

The additive `1` is harmless after (3.12), but it is arithmetically
necessary unless a further exceptional-set theorem is proved.  Establishing
(7.10) is a high-denominator rational-slope recurrence or anisotropic
dispersion theorem.  None of the identities above proves it.

## 8. Hostile finite scan

An exact scan takes, for every integer `y` in `|y|<=2Q/5`, the unique
possible integers `r,s` in the two bands and classifies them in the disjoint
order `n=0`, `L=0`, `kappa=0`, remote minor.  Representative results are:

| `Q` | `A` | `B` | `AB/Q` | `sqrt(A)` | `(n=0,L=0,kappa=0,remote)` | min remote `rho` | min remote `p` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1009 | 29 | 29 | 0.833 | 5.39 | `(11,0,0,8)` | 20 | 7 |
| 5003 | 62 | 248 | 3.073 | 7.87 | `(15,0,2,7)` | 34 | 9 |
| 20011 | 122 | 488 | 2.975 | 11.05 | `(23,0,2,12)` | 71 | 71 |
| 39800 | 170 | 170 | 0.726 | 13.04 | `(27,0,0,10)` | 3210 | 769 |
| 100003 | 266 | 1064 | 2.830 | 16.31 | `(33,0,2,9)` | 1520 | 380 |
| 100003 | 266 | 2128 | 5.660 | 16.31 | `(33,0,4,12)` | 1520 | 145 |

The scans find no family threatening the `sqrt(A)` budget and no growth
contradicting (7.10).  They are much too small to distinguish `Q^o(1)` from
a small power, and they do not prove the remote theorem.

The identities, counterexample, exponent ledger, secondary-packet majorant,
and scanner are in `src/qp_coupled_cusp_fejer_inverse.py`; focused checks are
in `src/test_qp_coupled_cusp_fejer_inverse.py`.

## 9. Binary status

```text
primitive identities (1.6)--(1.8):                    PROVED;
pure nL!=0 minor bound (AB/Q)Q^o(1):                   FALSE;
infinite compact-core counterexample:                 PROVED;
counterexample lies on translated tangent r=s:        PROVED;
whole kappa=0 sector <=sqrt(A):                        PROVED;
whole rho<=cQ^(1/3) sector <=sqrt(A):                  PROVED;
n=0 common-product sector <=sqrt(A)Q^o(1):             PROVED;
L=0 exact-cusp sector <=sqrt(A)Q^o(1):                 PROVED;
surviving p>>(Q/B)^(1/3)>=D^(13/48):                  PROVED;
corrected remote estimate (7.10):                      OPEN;
special reciprocal-curve theorem:                     OPEN;
sharp four-cycle bound:                               NOT PROVED.
```
