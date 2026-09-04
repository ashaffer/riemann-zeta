# QP four completions: a lossless Bezout-token and diamond normal form

**Date:** 2026-08-25  
**Verdict:** the sharp occupied-cell theorem is not proved.  There is,
however, a new exact coordinate reduction which retains every physical row
and actual prime-power mask.  For one fixed primitive endpoint, both
determinant labels are lifted by the **same** Bezout inverse to primitive
two-dimensional tokens.  The middle transition determinant becomes their
ordinary area, while the two middle hard windows become one exact radial
diamond for an integral symmetric form of determinant `-1`.

Thus the remaining theorem is now a selected, rooted token-incidence bound,
not an informal “two inverses” analogy.  No fibre multiplicity or Fourier
kernel has yet been paid.  The reduction also gives a fail-fast result:
deleting the radial/product diamond permits `asymp D^2` primitive token
incidences even though all three physical determinant labels are `O(D)`.
In the principal adjacent affine chart, restoring just one physical product
window cuts this `D^2` block to `O(D)` by an exact positive-definite quadratic
law.  The unclosed case is the aggregation of many scattered token directions.

## 1. The two unimodular lifts

Fix the actual primitive ordered endpoint

```text
gamma=(c,C),                    gcd(c,C)=1,
```

and choose integers `u,v` with

```text
c*u-C*v=1.                                           (1.1)
```

For a centre pair `p=(b,B)`, put

```text
delta=c*b-C*B.
```

There is a unique integer `n` such that

```text
b=u*delta-C*n,             B=v*delta-c*n.            (1.2)
```

For a later colour pair `eta=(d,E)`, put

```text
h=C*d-c*E.
```

There is a unique integer `m` such that

```text
d=-v*h+c*m,                E=-u*h+C*m.                (1.3)
```

The two matrices in (1.2)--(1.3) have determinants `-1` and `1`.
Consequently

```text
p <-> P=(delta,n),         eta <-> R=(h,m)            (1.4)
```

are bijections of `Z^2`, not projections.  In particular

```text
gcd(P)=gcd(b,B),            gcd(R)=gcd(d,E).           (1.5)
```

On the all-distinct actual prime-power sector both tokens are primitive.
The fixed root itself is especially simple:

```text
gamma <-> R_0=(0,1).                                  (1.6)
```

The hard windows give `|delta|,|h|<<D`; (1.2)--(1.3) and the physical shell
then give `|n|,|m|<<D`.  Hence every four-completion chain lies in one honest
`O(D)` token box.  Actual masks remain attached to the inverse images in
(1.2)--(1.3).

## 2. Area and the determinant-minus-one radial form

Direct expansion of (1.2)--(1.3) gives the central identity

```text
b*d-B*E=delta*m-n*h=det(P,R).                         (2.1)
```

Define

```text
K = (-2uv       cu+Cv
     cu+Cv      -2cC).                                (2.2)
```

Then

```text
det K=4uvcC-(cu+Cv)^2=-(cu-Cv)^2=-1                  (2.3)
```

and the other physical product coordinate is

```text
b*d+B*E=P^T K R.                                     (2.4)
```

Thus the difference and sum of the two coordinate products are precisely
the symplectic and Lorentz pairings of the same two tokens.  In particular,
with `R_0=(0,1)`,

```text
P^T K R_0=b*c+B*C,
det(P,R_0)=delta.                                    (2.5)
```

No completion or asymptotic approximation occurs in (2.1)--(2.5).

## 3. Two physical windows are exactly one diamond

For a row `y`, write

```text
X=8ybd-q^3,             Y=8yBE-q^3.
```

The elementary real identity

```text
max(|A+B|,|A-B|)=|A|+|B|                             (3.1)
```

and (2.1)--(2.4) give the equivalence

```text
|X|,|Y|<=qD
  iff
|4y P^T K R-q^3|+4y |det(P,R)|<=qD.                 (3.2)
```

The base two windows use the same formula with `R=R_0` and row `a`; the
middle two use `R` and row `x`.  Since a missing-coordinate interval has
length `O(D/q)<1`, the row attached to an accepted token edge is unique.
Therefore the neighbourhood-degree sum is **exactly**

```text
W(gamma)
 =#{ selected primitive token paths R_0 -- P -- R
     in the O(D) box, satisfying both diamonds (3.2) }. (3.3)
```

“Selected” in (3.3) means that the inverse images (1.2)--(1.3) and both
rows belong to the original actual prime-power carrier.  There is no copied
coefficient, completed token box, or forgotten row multiplicity.

This is a concrete formulation of the desired mask-sensitive vector-valued
two-inverse theorem:

> uniformly in the root chart, the selected rooted token graph in (3.3) has
> at most `D q^o(1)` length-two paths.

## 4. The Gram identity has no unused divisor reserve

Because `det K=-1`, every two tokens obey

```text
(P^T K R)^2-(P^T K P)(R^T K R)=det(P,R)^2.           (4.1)
```

The self-pairings are exactly

```text
P^T K P=-2bB,                 R^T K R=-2dE.          (4.2)
```

Consequently (4.1) is the physical identity

```text
(bd+BE)^2-4bBdE=(bd-BE)^2.                            (4.3)
```

Factoring it gives

```text
(P^T K R-det(P,R))(P^T K R+det(P,R))
       =(2BE)(2bd).                                   (4.4)
```

Thus a divisor argument applied to (4.1) merely reconstructs the two
original product legs.  It does not manufacture a common integer shared by
different token cells.  Fixing `P^T K P` fixes `bB`; on all-distinct actual
prime support, unique factorisation then fixes the unordered physical pair
up to `q^o(1)` choices.  There is no large fixed-norm family over which a
new square-root estimate can average.  Allowing the norm to vary restores
the entire original sum.

There is an equivalent lattice warning.  For fixed `P`, the map

```text
R -> (P^T K R, det(P,R))                              (4.5)
```

has determinant `P^T K P=-2bB asymp q^2`.  This proves the familiar
fixed-row/pair uniqueness when the physical shell masks are retained.  A
covolume statement alone is not a large sieve: the image lattice may have a
short tangent vector.  Completing (4.5) to its whole lattice pays exactly
for that vector and loses the selected radial diamond.  Hence neither the
Gram factorisation nor a full-lattice Fourier completion yields a new global
range beyond the already known fixed-cell/fixed-secant divisor bounds.

## 5. Determinants alone permit `D^2` cells

The loss from dropping (3.2) is polynomial and literal.  Put

```text
gamma=(M,M+1),             1<=r,s<=L,
P_r=(r,r-1),               R_s=(s,s+1).              (5.1)
```

The inverse physical vectors are

```text
p_r=(M+1-r,M-r),           eta_s=(M+s,M+1+s).         (5.2)
```

All tokens in (5.1) are primitive, all physical coordinates remain in one
narrow full-integer shell for `M>>L`, and

```text
det(P_r,R_0)=r,
det(R_0,R_s)=-s,
det(P_r,R_s)=r+s.                                    (5.3)
```

Taking `L=floor(D/2)` gives `asymp D^2` pairs satisfying every small
determinant condition.  This is not a hard-window counterexample: it is an
exact counterexample to any proof which projects away the radial/product
part of (3.2).

## 6. Restoring one product mask closes the principal chart sharply

The same model shows how the hard mask removes the false `D` factor.  Write

```text
A=r-1,
b=M-A,                    d=M+s,
x_0=M+A-s.
```

Then exactly

```text
x_0*b*d-M^3
 =-M(A^2-As+s^2)+As(s-A).                            (6.1)
```

Assume `M>=16D^2` and `1<=r,s<=D`.  If any integer row `x` satisfies the
first middle hard window for `q=2M`, then the gap between consecutive values
of `x*b*d` and the bound `D^2<M/16` force `x=x_0`.  Equation (6.1) then gives

```text
A^2-As+s^2<=5D/16.                                   (6.2)
```

Since

```text
A^2-As+s^2 >=(A^2+s^2)/2,                            (6.3)
```

there are only `O(D)` possible pairs `(r,s)`.  The other coordinate window
and every actual mask can only delete pairs.  Therefore the whole principal
adjacent Bezout chart satisfies the desired occupied-cell scale.

This is the exact affine/rank-one major arc predicted by the token geometry.
It also explains why `D^2<q`, though insufficient for the global theorem,
is decisive after a common token direction has been identified: the first
nonlinear displacement is quadratic and cannot wrap to a second row branch.

## 7. Remaining theorem and honest status

The normal form separates the problem without solving the broad aggregate:

```text
two physical-to-token maps are GL_2(Z):                 PROVED;
actual masks and token primitivity are preserved:       PROVED;
middle determinant equals token area:                   PROVED;
product sum is a symmetric det(-1) form:                 PROVED;
two hard windows equal one exact diamond:                PROVED;
W(gamma) equals selected rooted token paths:             PROVED;
Gram identity and physical factorisation:                PROVED;
Gram/divisor identity gives a new aggregate saving:      NO;
determinant-only D^2 primitive block:                     PROVED;
principal adjacent full-integer hard chart is O(D):      PROVED;
many scattered token directions pack into O(D q^o):      OPEN;
sharp four-cycle theorem:                                NOT PROVED.
```

The remaining inverse statement can now be posed precisely: if the rooted
selected token graph has more than `D q^o(1)` paths, prove that a positive
fraction of its edges lie in `q^o(1)` common affine token directions.  Each
such direction is governed by a quadratic law of the type (6.1) and has
capacity `O(D)`.  Current fixed-direction packet theorems handle a direction
after it is found; they do not prove this cross-direction Carleson packing.

Verification artifacts:

```text
src/qp_four_completion_bezout_token.py
src/test_qp_four_completion_bezout_token.py
lean/weilcert/QPFourCompletionBezoutToken.lean
```

The executable tests include the literal all-prime double-star fixture, so
the reduction is replayed on selected actual masks rather than only on the
full-integer principal chart.  Lean independently certifies the two lifts,
the area and form identities, `det K=-1`, the diamond identity, the Gram
identity, and the principal quadratic residual.
