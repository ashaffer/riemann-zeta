# QP rounded parallel charts: one orbit and the rectangle gate

**Date:** 2026-08-25  
**Verdict:** the arbitrary-two-strip model was unnecessarily loose.  For a
fixed primitive anchor, centre and endpoint tokens are reflections of one
modular orbit.  This gives an exact physical normal form for every parallel
chart and an exact finite-difference rigidity test for its unique integer
completion rows.  It does **not** prove the desired `O(D q^o(1))` cell count:
the rigidity test requires occupied rectangles, while a scattered support can
avoid them at densities still polynomially above `D`.

## 1. One modular orbit, not two arbitrary token clouds

Fix `gamma=(c,C)` and `cu-Cv=1`.  If the centre token `P_t=(t,n_t)` has
physical point

```text
(b_t,B_t)=(u*t-C*n_t, v*t-c*n_t),
```

then the endpoint with label `h=-t` is exactly

```text
(d_{-t},E_{-t})=(B_t,b_t),       R_{-t}=(-t,-n_t)=-P_t.   (1.1)
```

Moreover

```text
n_t-(u/C)t=-b_t/C.                                    (1.2)
```

The physical shell has multiplicative width `e^0.4<2`; hence its image in
the transverse coordinate in (1.2) has width `<1`.  For every integer `t`
there is therefore at most one possible `n_t`.  Centres and endpoints are
oppositely translated pieces of the same rational digital line.

## 2. Exact normal form for a parallel direction

Let the common token direction be `V=(v0,v1)` and put

```text
(p,P)=(u*v0-C*v1, v*v0-c*v1),       c*p-C*P=v0.       (2.1)
```

Two orbit lines have the form

```text
(b_r,B_r)=(b0+p*r,B0+P*r),
(b'_s,B'_s)=(b1+p*s,B1+P*s).                           (2.2)
```

By (1.1), the middle hard legs are

```text
x*b_r*B'_s,                 x*B_r*b'_s.               (2.3)
```

Writing `Ji=p*Bi-P*bi`, their determinant is exactly

```text
b_r B'_s-B_r b'_s
 =(b0 B1-B0 b1)+J1*r-J0*s.                            (2.4)
```

The mixed term cancels.  The chart is non-null precisely when `pP!=0`.
This recovers the earlier parallel Hessian branch without an arbitrary
choice of two token populations.

## 3. What row uniqueness really gives

For one physical leg define

```text
f(b,d)=q^3/(8bd).
```

At an accepted cell, the unique integer row `x` obeys

```text
x-f(b,d)=(8xbd-q^3)/(8bd)=O(D/q).                     (3.1)
```

For four accepted corners `(b_i,d_j)`, therefore,

```text
Delta_b Delta_d x
 = (q^3/8)(1/b0-1/b1)(1/d0-1/d1)
   + Delta_b Delta_d(error).                          (3.2)
```

This is exact, not a Taylor expansion.  In particular, if

```text
|(q^3/8)(1/b0-1/b1)(1/d0-1/d1)|
  + sum_corners |error| <1,                           (3.3)
```

then the integral mixed difference in (3.2) is zero.  For affine steps this
is the rounded-row analogue of the stationary Hessian calculation.  The
second physical leg supplies the same integer mixed difference with the
swapped orbit coordinates.

## 4. Literal all-prime rounded chart

The existing seven-prime fixture at

```text
q=5,868,182,        D=1,912
```

already lies in this branch.  Relative to its anchor, all 15 chains have

```text
5*delta-6*n=6,             5*h-6*m=-6,               (4.1)
```

so the two token populations are parallel lines of primitive direction
`(6,5)`.  Their physical direction is `(1,1)`, hence non-null.  Every unique
prime completion row satisfies the exact integral law

```text
x=3*(q/2)-b-d.                                      (4.2)
```

But the formal stationary slopes `-x/b` and `-x/d` at a base cell are
nonintegral.  Thus requiring equality with the formal stationary affine row
is too restrictive; a correct proof must allow a rounded integral plane
such as (4.2).

## 5. Why this still does not close the chart

Equation (3.2) constrains occupied `2 by 2` rectangles.  A support with no
such rectangle can still have `Theta(D^(3/2))` cells by the elementary
Zarankiewicz scale.  Consequently, finite differences plus row uniqueness,
without an additional incidence/packing input, cannot yield the required
`D q^o(1)` bound.  The one-orbit reduction removes the fictitious `D^2`
direction cover, but it leaves a genuinely sparse rounded-reciprocal
incidence problem.

## 6. Return edges transfer to a bilinear row kernel

There is a useful stronger identity, with an important scope restriction.
Suppose the reflected endpoint is itself another root neighbour.  Write the
two root neighbours as `(b,B)` and `(b',B')`, with root rows `a,a'`; the
middle endpoint is `(B',b')`, with middle row `x`.  Put

```text
e1=8abc-q^3,       e4=8a'B'C-q^3,
f1=8xbB'-q^3.
```

Then exact cancellation of `bB'` gives

```text
q^3(q^3*x-8cCaa')
 =8aa'cC*f1-x*q^3(e1+e4)-x*e1*e4.                 (6.1)
```

The other coordinate gives the analogous identity with the other three
residuals.  Consequently

```text
|8cCaa'-q^3*x| <<q^2 D,
|x-(8cC/q^3)aa'| <<D/q.                            (6.2)
```

Thus the genuine return-return subgraph is a symmetric near-integral
bilinear kernel on the root rows.  This explains the exact additive row
plane in the seven-prime fixture.

Equation (6.2) must **not** be applied to every endpoint.  In the large
rich-anchor experiment most paths do not return to the root neighbourhood.
For such an endpoint there is no actual second base row `a'` to insert in
(6.1).

## 7. Exact substitute for a nonreturn edge

For an arbitrary rooted path

```text
(c,C) --a--> (b,B) --x--> (d,E),
```

subtract the first middle hard residual from the first base residual, and
likewise in the other coordinate.  One gets the exact short errors

```text
r=x*d-a*c=(F1-E1)/(8b),
s=x*E-a*C=(F2-E2)/(8B),                              (7.1)
```

and hence

```text
|r|<=qD/(4b)<<D,       |s|<=qD/(4B)<<D,
C*r-c*s=x*(C*d-c*E).                                 (7.2)
```

This is the correct nonreturn invariant.  Equivalently, every edge puts the
reduced fraction `x/a` within `O(D/q^2)` of both `c/d` and `C/E`.  The map
in (7.2) is injective on the short error box, but it still has `O(D^2)`
possible cells.  A sharp proof needs a packing theorem for these simultaneous
two-inverse rays; the return transfer alone cannot count the dominant
nonreturn sector.

There is a lossless real-valued replacement for the missing return row.  Put

```text
Q=q^3/8,       Y_E=Q/(cE),       Y_d=Q/(Cd),
lambda=cC/Q.
```

Then (7.1) is exactly

```text
x-lambda*a*Y_E=s/E=O(D/q),
x-lambda*a*Y_d=r/d=O(D/q),                              (7.3)
```

while

```text
Y_E-Y_d=Q*(Cd-cE)/(cCdE)=O(D/q).                       (7.4)
```

Thus the entire rooted kernel is a near-integral rank-one bilinear graph
between the actual left rows and separated **real virtual endpoint rows**.
A return occurs only when the virtual row also lands in the actual root-row
mask.  On a four-cycle, (7.3) gives the exact rounded mixed term

```text
lambda*(a_1-a_2)*(Y_1-Y_2).                            (7.5)
```

Hence the same forbidden annulus reappears: a nonadditive cycle must be
broad, with side product comparable to `q`; an additive cycle is the
coherent packet branch.  This does not prove large girth after peeling.
It reduces that proposal to the already unresolved broad-cycle incidence
problem rather than bypassing it.

```text
one-orbit endpoint reflection:                         PROVED;
common digital-strip slope and width <1:               PROVED;
parallel physical swap normal form (2.2)--(2.4):       PROVED;
exact rounded rectangle identity (3.2):                PROVED;
literal all-prime non-null rounded chart (4.1)--(4.2): VERIFIED;
return-return bilinear transfer (6.1)--(6.2):          PROVED;
transfer applies automatically to nonreturn endpoints: FALSE;
nonreturn short two-inverse errors (7.1)--(7.2):       PROVED;
virtual endpoint bilinearization (7.3)--(7.4):         PROVED;
post-peel large girth from bilinearization alone:      NOT PROVED;
O(D q^o(1)) cells in an arbitrary fixed rounded chart: OPEN;
global cross-chart Carleson summability:                OPEN.
```

## 8. Hostile test: a nonreturn bridge creates an induced nonplanar `C6`

The tempting stronger assertion that every short cycle in the unmasked
hard-window graph is one coherent affine packet is false.  There is an exact
full-integer example with

```text
q=100000,       D=265,       gamma=(50000,50007),
q>D^2.
```

Its three left and three right token vertices are

```text
r0=(-7,-7), r1=(7,5), r2=(35,29),
s0=(-35,-29), s1=(7,7), s2=(-36,-30),
```

and the exact scanner finds the six cyclic edges

```text
(r0,s0), (r1,s0), (r1,s1), (r2,s1), (r2,s2), (r0,s2),
```

while all three chords `(r0,s1),(r1,s2),(r2,s0)` are absent.  The associated
physical triples `(b,d,x)` are

```text
(50008,49995,49997), (50006,49995,49999),
(50006,50001,49993), (50002,50001,49997),
(50002,42852,58338), (50008,42852,58331).
```

Every one of their 24 hard legs has residual at most `qD`, and every
determinant is non-null.  But

```text
49997-49999+49993-49997+58338-58331=1,               (8.1)
```

and the augmented affine `4 by 4` minor on physical points numbered
`0,1,2,4` is exactly `14304`.  Thus the six edges are neither additive nor
contained in a single affine row plane.

The scope of this obstruction is precise.  The first four edges use endpoint
vertices whose reflections are actual root neighbours.  The last two share
the endpoint `(42852,42858)`, whose reflection is not a root neighbour.  It is
therefore exactly a **nonreturn bridge**.  The anchor and several vertices are
composite, so this does not refute an actual-prime cycle theorem.  Nor does it
refute the desired count: the entire rooted graph has only `98<D` edges.
It refutes a mask-free inference from the hard windows alone that an induced
short cycle must itself be a coherent plane.

Constants also prevent a false contradiction with the proved subunit-area
lemma.  For this cycle the exact virtual ideal alternating area is

```text
744747133337 / 744211317262 = 1.0007199784...,
```

the signed rounding correction is `-0.0007199784...`, and their sum is the
integer `1` in (8.1).  Although `D^2<q`, estimates carrying the cycle-length
factor (`9D^2` or `36D^2`) are not subunit here.  Consequently the exact
local lemma correctly makes no additivity assertion.

This leaves two viable variants rather than the naive high-girth shortcut:

1. exploit the actual-prime mask to forbid or sparsify such nonreturn bridges;
2. define a surgical packet peel that charges a mixed cycle to its coherent
   return segment, rather than claiming that the whole cycle is one plane.

The fixture is replayed losslessly by
`test_full_integer_nonreturn_bridge_has_induced_noncoherent_six_cycle`.

Verification:

```text
src/qp_rounded_parallel_orbit.py
src/test_qp_rounded_parallel_orbit.py
lean/weilcert/QPRoundedParallelOrbit.lean
```

Lean certifies the parallel determinant cancellation, the exact reciprocal
four-corner identity, and the token-direction reconstruction.  It does not
certify the open sparse rectangle-packing estimate.
