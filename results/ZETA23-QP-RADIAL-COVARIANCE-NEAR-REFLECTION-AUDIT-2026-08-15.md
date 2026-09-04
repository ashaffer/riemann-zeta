# QP radial covariance: near-reflection arithmetic audit

**Date:** 2026-08-15  
**Verdict:** the cross-side `Y^-2` spacing possibility does not contaminate
the canonical Turan event at positive density.  At the full-band Fourier
resolution `B^-1`, all near-reflection pairs occupy at most

```text
Y^(2-A+o(1))                                         (0.1)
```

coordinates.  For `A=50/33` this is `Y^(16/33+o(1))`.  A mass-normalized
event of depth `Y^-d` uses at least `Y^(1-d)` primes, so for every

```text
d<A-1                                                (0.2)
```

the event survives deletion of every near-reflection endpoint.  At the
project value `d=.019`, the power gap is

```text
A-1-d=.4961515... .                                  (0.3)
```

This proves that unresolved cross-side collisions are not carried by a
macroscopic part of the selected prime interval.  It does **not** prove
`LTRAD_full`: an adaptive signed dual may be supported on those exceptional
coordinates, on primes outside the selected interval, or on proper powers.

An independent hostile audit also confirms Proposition 5.3 of the mass
radialization report.  Its one-sided signed frequency family is genuinely
`c_w/Y`-separated, and its Montgomery--Vaughan and first-moment estimates
have the stated normalizations.

The same audit gives a **PASS** verdict to the companion clustered-frame
theorem in
`ZETA23-QP-TRANSVERSE-RETURN-CLUSTER-FRAME-GATE-2026-08-15.md`.  In
particular, its conclusion `s_v,r_+ >> 1/M_Y` is rigorous; its exponent is
far too small for `LTRAD_full` and is not a QP or strip theorem.

---

## 1. Exact product reduction

Let `Y` be a half-integer, let `n<Y<m` be integer shell nodes, and put

```text
u_n=log(Y/n),                 u_m=log(m/Y).           (1.1)
```

Then exactly

```text
|u_n-u_m|=|log(nm/Y^2)|.                             (1.2)
```

If `|u_n-u_m|<=kappa/B`, with fixed `kappa` and `B=Y^A`, then

```text
Y^2 exp(-kappa/B)<=nm<=Y^2 exp(kappa/B),             (1.3)
|nm-Y^2|<<_kappa Y^2/B.                              (1.4)
```

The number `k=nm` is an integer.  There are

```text
O(1+Y^2/B)=O(Y^(2-A))                               (1.5)
```

possible products in (1.3), and each has at most

```text
d(k)=Y^o(1)                                         (1.6)
```

factorizations.  Therefore the number of ordered cross-side pairs, even
before imposing the prime-power restriction, is

```text
O(Y^(2-A+o(1))).                                    (1.7)
```

The number of endpoints is at most twice this.  This proves (0.1).
The half-integer condition gives the additional exact fact that the two
absolute nodes never coincide: `nm` is integral whereas `Y^2` has
fractional part `1/4`.

## 2. Cleaning a Turan-long event

Suppose a selected prime set has

```text
-sum_(p in I) cos(t_0 log(p/Y)) >=Y^(1-d+o(1)).      (2.1)
```

Delete every selected prime which is an endpoint of a pair counted in
(1.7).  Deleting one unit cosine changes the left side by at most one, so
the remaining set has negative sum at least

```text
Y^(1-d+o(1))-Y^(2-A+o(1)).                           (2.2)
```

Under (0.2), this is

```text
(1-o(1))Y^(1-d+o(1)).                               (2.3)
```

Thus the canonical probability may be recalibrated on a set whose nodes
have no opposite-side partner within `kappa/B`, without losing the event's
fixed exponent.  Contiguity is lost after deletion, but transverse mixing
only uses the resulting probability and its scalar calibration; it does
not require contiguity at that later step.

This cleaning does not simplify the complete convex body.  All shell nodes
remain coordinates of `a(t)`, and the signed support-function test still
ranges over vectors concentrated wholly outside the cleaned carrier.  A
claim that (2.3) alone yields the full residual inequality would therefore
drop a quantifier.

## 3. Hostile check of the one-sided positive-return proposition

For primes on one side of `Y`, the mean-value theorem gives

```text
u_p>>_w1/Y,
|u_p-u_q|>>_w1/Y                  (p!=q).             (3.1)
```

Consequently `{+u_p,-u_p}` is also `c_w/Y`-separated.  If

```text
P(t)=M^-1 sum_p cos(tu_p),       L=|H_Y|,             (3.2)
```

Montgomery--Vaughan gives

```text
L^-1 int_(H_Y)P(t)^2dt
 =1/(2M)+O_w(Y/(LM))
 =(1+o(1))/(2M).                                    (3.3)
```

Direct integration and the distinct half-integer distances `|p-Y|` give

```text
|L^-1 int_(H_Y)P(t)dt|
 <<Y log Y/(LM)=o(1/M).                             (3.4)
```

Finally `P^2<=2P_+-P` proves `sup P>>1/M`.  The original proposition is
therefore sound; it does not silently use cross-side separation.

## 4. Hostile check of the clustered-frame return theorem

The positive frequencies are the union of two `c_w/Y`-separated families,
so every unresolved component has at most two nodes.  On a close pair the
normalized sum/difference coordinates are

```text
p=c_1+c_2,       q=min(1,B|u_1-u_2|)(c_1-c_2).
```

After scaling `t=Bx`, the pair is

```text
p cos(zx/2)+i(c_1-c_2)sin(zx/2),   z=B|u_1-u_2|.
```

Positive variance of the smooth averaging density makes its Gram form
uniformly equivalent to `|p|^2+|q|^2`, including as `z` tends to zero.
Separated block centers and Schwartz decay control all normalized first and
second divided differences by an absolutely summable row bound.  This
verifies the delicate `Y^-2` collision step rather than replacing a close
pair by one coordinate.

The remaining implications were checked independently: the smooth mean is
small enough that `U |mean(F)| <= Q/2`; the elementary range inequality
then gives `sup F >= Q/(2U)`.  Point evaluation at `0` and `t_0` costs a
second factor `sqrt(M_Y)`, and support-function separation places
`-(c/M_Y)v` in the convex hull.  The Fejer model has dual ceiling exactly
`1/[2(M-1)]`, so the stated dimension-only sharpness has the correct sign
and normalization.

## 5. Disposition

```text
one-sided Proposition 5.3 normalization:             VERIFIED;
B^-1 cross-side pair count Y^(2-A+o(1)):             PROVED;
Turan-long event survives deleting all endpoints:    PROVED for d<A-1;
cross-side collisions form macroscopic event mass:   FALSE;
arbitrary signed dual controlled by this cleaning:   NOT PROVED;
clustered-frame transverse floor s_v >>1/M_Y:         VERIFIED;
unconditional radial floor r_+ >>1/M_Y:               VERIFIED;
LTRAD_full, QP-to-strip, or a strip:                  NOT PROVED.
```

Executable replay:

- `src/qp_radial_covariance_gate.py`;
- `src/test_qp_radial_covariance_gate.py`;
- `results/verify_zeta23_qp_radial_covariance_gate.py`.
