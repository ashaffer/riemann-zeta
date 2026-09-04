# QP four-cycle: factorial-convolution zero layer and the fixed-determinant gate

**Date:** 2026-08-22  
**Verdict:** extending the direct multiplicative-Hankel coefficient to every
integer in its product intervals produces a majorant which is too large.
For the full integer color shell, its factorial off-diagonal energy is
`Omega(D^2)` already in the zero color-determinant layer.  This remains true
when all four colors are distinct and when

```text
H=qD,                    2H^2<q^3                  (0.1)
```

so the sub-square-root residual rigidity does not remove the example.  It
identifies it exactly.

The actual narrow prime-power shell has no such zero-layer factorial
collision: multiplicative Sidonicity fixes the color pair, and the common
residual spacing is of order `q^2>H`.  After that sector is removed, however,
a determinant-by-determinant proof still does not follow.  The exact
full-integer translation family can be specialized to one fixed nonzero
determinant and gives `Omega(sqrt(D))` factorial collisions on one four-color
tuple.  Its exact version is incompatible with prime-power colors, but no
current theorem excludes the corresponding near-tangent prime-power family.

Thus the broad full-integer `f*f` inequality is false, and an actual-shell
nonzero-determinant proof would still require a prime-sensitive merged-packet
or weighted tangent-orbit estimate.  No four-cycle bound is claimed here.

---

## 1. The broad factorial majorant

Put

```text
Q=q^3,
I_c={n in Z_(>0): |8*c*n-Q|<=H},
f_z(n)=z_c  for n in I_c.                           (1.1)
```

At `H=qD` with `D=o(q)`, the intervals `I_c`, for `c` in a fixed
proportional `q`-shell, are disjoint for all sufficiently large `q`.
Indeed, if `n` belonged to two distinct intervals, then

```text
8*n <= 8*n*|c-d| <=2H,
```

whereas `n` is comparable with `q^2` and `H=o(q^2)`.

For a nonnegative coefficient define its factorial off-diagonal energy by

```text
F#(f)=sum_(n1*n2=n3*n4, {n1,n2}!={n3,n4})
       f(n1)f(n2)f(n3)f(n4).                       (1.2)
```

Every direct nondegenerate rectangle gives a term of (1.2): take

```text
(n1,n2,n3,n4)=(a1*b1,a2*b2,a2*b1,a1*b2).          (1.3)
```

The converse need not have a factorization with all four factors in the
shell.  Therefore (1.2) is a legitimate positive majorant, up to divisor
multiplicity, but it is a strictly stronger object than the direct fourth
trace.

## 2. Equal color product: exact residual rigidity

Write

```text
ri=8*ci*ni-Q,                 |ri|<=H.              (2.1)
```

For a multiplicative collision put

```text
p=c1*c2,                     p'=c3*c4.             (2.2)
```

If `p=p'`, cancellation gives

```text
Q*(r1+r2-r3-r4)=r3*r4-r1*r2.                       (2.3)
```

Under `2H^2<Q`, both sides vanish.  Consequently

```text
{r1,r2}={r3,r4}.                                    (2.4)
```

This is the strongest possible conclusion.  It does not identify the
colors which carry the two equal residual numerators.

## 3. A `D`-by-`D` proportional-dilate block

Fix coprime positive integers `u<v` with

```text
log(v/u)<2w.                                        (3.1)
```

For `w=0.2`, one may take `(u,v)=(5,6)`.  There is a proportional interval
of scales `g` for which both `u*g` and `v*g` lie in the shell

```text
(q/2)*exp(-w)<c<(q/2)*exp(w).                       (3.2)
```

Choose two distinct nearby integers `g,h` in this interval.  The four
colors

```text
(c1,c2,c3,c4)=(u*g,v*h,v*g,u*h)                    (3.3)
```

are distinct for large `q`, and

```text
c1*c2=c3*c4=u*v*g*h.                               (3.4)
```

Define the integer intervals

```text
J_g={A: |8*u*v*g*A-Q|<=H},
J_h={B: |8*u*v*h*B-Q|<=H}.                         (3.5)
```

Since `g,h` are comparable with `q`,

```text
|J_g|,|J_h| asymp H/q asymp D.                     (3.6)
```

For every `A in J_g` and `B in J_h`, put

```text
(n1,n2,n3,n4)=(v*A,u*B,u*A,v*B).                  (3.7)
```

Then, exactly,

```text
n1 in I_(u*g),        n3 in I_(v*g),
n2 in I_(v*h),        n4 in I_(u*h),
n1*n2=u*v*A*B=n3*n4.                               (3.8)
```

The two unordered pairs in (3.8) agree only when `A=B`.  Hence (3.7)
supplies

```text
|J_g|*|J_h|-|J_g intersect J_h| asymp D^2         (3.9)
```

factorial off-diagonal terms.  Give each of the four colors weight `1/2`.
Then `||z||_2=1`, while

```text
F#(f_|z|) >=(D^2+O(D))/16 >>D.                    (3.10)
```

The residuals in (3.7) are paired literally:

```text
r1=r3=8*u*v*g*A-Q,
r2=r4=8*u*v*h*B-Q.                                (3.11)
```

Thus (2.4) certifies this family instead of contradicting it.  At the
project exponent `D=q^(16/33+o(1))`, condition (0.1) holds asymptotically.

Most integers in (3.7) need not factor into two nodes of the original
shell.  This is why (3.10) disproves the broad factorial majorant but not
the direct four-cycle estimate.

## 4. Why the actual zero layer disappears

In the narrow actual prime-power shell, distinct colors are coprime and
the shell is multiplicatively Sidon.  Thus (3.4) forces equality of the
two unordered color pairs.

There is one apparent cross-pairing left.  For distinct colors `c,d`, two
different residual numerators would both have to be divisible by `c` and
`d`.  Their separation is therefore a nonzero multiple of

```text
lcm(c,d)=c*d asymp q^2.                            (4.1)
```

The whole numerator window has length `2H=O(qD)=o(q^2)`.  It contains at
most one such common multiple.  Hence the cross-pairing has equal residuals
and is factorial-diagonal.  Repeated-color cases are immediate from (2.4).
Therefore

```text
actual prime-power factorial zero layer: EMPTY.     (4.2)
```

This uses both multiplicative Sidonicity and the residual spacing.  Either
input alone is insufficient for the full integer shell.

## 5. The nonzero determinant is pinned but not pointwise sparse

Let

```text
k=p'-p,       S12=r1+r2,       S34=r3+r4.          (5.1)
```

The collision identity is

```text
(p+k)*(Q^2+Q*S12+r1*r2)
 =p*(Q^2+Q*S34+r3*r4).                             (5.2)
```

It first gives `|k|<<D`.  Rearranging then gives

```text
|(S34-S12)-k*Q/p| <<D^2/q.                         (5.3)
```

Thus, for large `q`, the residual-sum gap is the unique nearest integer to
`kQ/p`.  This is the same sub-square-root rigidity which closes the color
ledger:

```text
sum_(c1*c2-c3*c4=k)|z_c1 z_c2 z_c3 z_c4|
 <<q^o(1)||z||_2^4.                                (5.4)
```

What (5.4) does not include is the number of interval-product collisions
carried by one color quadruple.

That multiplicity is not `q^o(1)` for full-integer colors, even with `k`
fixed and nonzero.  In the exact translation construction of
`ZETA23-QP-FOUR-CYCLE-FIXED-COLOR-TRANSLATION-GRID-OBSTRUCTION-2026-08-15.md`,
take fixed unequal steps

```text
ell_r=1,                  ell_c=2.                  (5.5)
```

The four colors are distinct and their determinant is the fixed integer

```text
k=-2*S^2.                                           (5.6)
```

The opposite translation parameter still ranges over

```text
|t|<=epsilon*sqrt(D).                               (5.7)
```

Every `t` gives a distinct direct rectangle and hence a distinct factorial
collision in the same four intervals.  With weight `1/2` on the four
colors, one fixed determinant layer therefore contributes

```text
Omega(sqrt(D)).                                     (5.8)
```

So a proposed uniform estimate `F#_k<<q^o(1)||z||_2^4` is false.  This
specialization is a consequence of the already recorded translation
identity, not a new packet construction.

Exact cancellation in that construction forces the colors to share a
fixed factor `S>1`, and hence excludes an actual all-distinct prime-power
realization.  Near cancellation, however, only asks for a short
first-order slope error and is not excluded by multiplicative Sidonicity.
No actual-shell theorem currently bounds all such near-tangent orbits.

## 6. Consequence for the proposed route

```text
equal-product residual multiset rigidity:          PROVED;
full-integer k=0 factorial bound O(D):              FALSE, Omega(D^2);
same obstruction with four distinct colors:        PROVED;
actual prime-power k=0 factorial off-diagonal:      EMPTY / PROVED;
nonzero determinant range |k|<<D:                  PROVED;
nonzero residual-sum nearest-integer pinning:       PROVED;
full-integer fixed-k factorial bound q^o(1):        FALSE, Omega(sqrt(D));
actual prime-power nonzero-k factorial bound:       OPEN;
broad full-integer factorial route to FC:           CLOSED / INVALID;
direct four-cycle bound:                            OPEN.
```

The exact zero-layer identities and finite replay are implemented in

```text
src/qp_factorial_convolution_zero_layer.py
src/test_qp_factorial_convolution_zero_layer.py
```

Run

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_factorial_convolution_zero_layer.py
```
