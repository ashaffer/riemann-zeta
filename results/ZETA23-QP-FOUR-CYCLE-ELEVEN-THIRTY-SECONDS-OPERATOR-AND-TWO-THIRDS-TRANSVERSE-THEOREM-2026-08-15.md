# QP four-cycle: `11/32` operator and `2/3` transverse theorem

**Date:** 2026-08-15  
**Verdict:** a second split inside the large two-minimum-product range
removes the remaining `D^(1/16)` slice loss.  For the truncated actual
prime-power carry matrix and every complex vector `z`, the all-distinct
four-cycle form satisfies

```text
|Q_nd(z)| << D^(11/8) q^o(1) ||z||_2^4.           (0.1)
```

After adjoining the already closed repeated-node and permutation sectors,

```text
||A_z||_op << D^(11/32) q^o(1) ||z||_2.           (0.2)
```

The established smooth band-pass and Schwartz-tail transfer therefore gives
the full-shell transverse exponent

```text
1/2 + (11/32)(16/33) = 2/3.                       (0.3)
```

This improves the preceding `D^(23/16)` fourth trace, `D^(23/64)`
operator, and `89/132` transverse exponent.  It does **not** prove the
literal four-cycle target `D^(1+o(1))`, the quarter-power operator bound,
QP, or a uniform strip.

---

## 1. Inputs and notation

Normalize `||z||_2=1`.  For an all-distinct color matrix `C`, let

```text
Lambda_C = {E in Z^4 : w_C dot E = 0},
lambda1 <= lambda2 <= lambda3,
P = lambda1 lambda2.                               (1.1)
```

The reduced-basis and determinant-layer estimates already proved are

```text
lambda1 lambda2 lambda3 asymp q,                  (1.2)
sum_C w_z(C) << D q^o(1).                         (1.3)
```

There are two useful ways to slice the ternary fixed-color quadric.

First, the universal constant-shear slice theorem gives

```text
m(C) << (1 + D/lambda2) q^o(1).                  (1.4)
```

Second, slicing in the third reduced coordinate gives

```text
K_C := 1 + D/lambda3
     << 1 + DP/q                                  (1.5)
```

parallel slices.  If the determinant form on the first two reduced
directions has nonzero discriminant, or vanishes identically, then

```text
m(C) << K_C q^o(1).                               (1.6)
```

In the remaining degenerate case, all slices have one common primitive
rank-one direction `e`.  Put `h=||e||_infinity`.  The pointwise
multi-slice estimate is

```text
m_e(C) << K_C (1 + sqrt(D/h)) q^o(1).             (1.7)
```

The direction kills the signed color matrix, so `e in Lambda_C`.  Since
the first minimum is Euclidean and `e` has four entries,

```text
lambda1 <= ||e||_2 <= 2h,
h >= lambda1/2.                                   (1.8)
```

This elementary lower bound on `h` is the extra geometric input used in
the large-`P` parabolic subrange.

For later use, when `K_C=O(1)` the already proved common-direction height
sum is

```text
Q_deg << D^(11/8) q^o(1).                         (1.9)
```

Indeed, splitting total chart multiplicity at `M` gives

```text
Q_low  << MD,
Q_high << D^(5/2) M^(-3),                         (1.10)
```

and `M=D^(3/8)` balances the two terms.  This is a global weighted sum over
all primitive rank-one directions, not a fixed-color estimate.

---

## 2. Small two-minimum product

Split first at

```text
P_0 = q/D = D^(17/16+o(1)),                       (2.1)
```

using `q=D^(33/16+o(1))`.  If `P<=P_0`, then (1.5) gives

```text
K_C << 1.                                         (2.2)
```

The nondegenerate and identically-zero restrictions contribute only
`Dq^o(1)` by (1.3) and (1.6).  The degenerate restriction is exactly the
`K_C=O(1)` height sum (1.9).  Hence

```text
Q_(P<=P_0) << D^(11/8) q^o(1).                   (2.3)
```

No uniform replacement of a variable slice count is made in this range:
the threshold (2.1) makes the actual slice count bounded.

---

## 3. Large product and a large second minimum

Suppose `P>P_0`.  First take

```text
lambda2 >= D^(5/8).                               (3.1)
```

The universal slice bound (1.4) immediately gives

```text
m(C) << D/lambda2 q^o(1)
     << D^(3/8) q^o(1).                           (3.2)
```

Here the harmless `1` in (1.4) is absorbed because `D/lambda2>=D^(3/8)`
throughout the active range.

---

## 4. Large product and a small second minimum

It remains to take

```text
P>P_0,                 lambda2<D^(5/8).           (4.1)
```

Because `DP/q>1` and `lambda1<=lambda2`, (1.5) sharpens to

```text
K_C << DP/q
    <= D lambda2^2/q
    << D^(1+10/8-33/16+o(1))
     = D^(3/16+o(1)).                              (4.2)
```

Thus (1.6) already gives `m(C)<<D^(3/16+o(1))` in the
nondegenerate and identically-zero cases.

In the degenerate case, combine (1.7), (1.8), and (4.2).  The additive
part is `K_C<<D^(3/16+o(1))`.  The square-root part obeys

```text
K_C sqrt(D/h)
 << (DP/q) sqrt(D/lambda1)
  = D^(3/2) sqrt(lambda1) lambda2/q
 <= D^(3/2) lambda2^(3/2)/q
 << D^(3/2+15/16-33/16+o(1))
  = D^(3/8+o(1)).                                  (4.3)
```

Consequently every color in (4.1), including the parabolic colors, has the
pointwise cap

```text
m(C) << D^(3/8) q^o(1).                           (4.4)
```

Together, (3.2) and (4.4) show that (4.4) holds throughout `P>P_0`.
Multiplying by (1.3),

```text
Q_(P>P_0) << D^(11/8) q^o(1).                    (4.5)
```

Equations (2.3) and (4.5) prove (0.1).

---

## 5. Why the exponent `5/8` is exact for this split

Write `lambda2=D^beta` in the small-second-minimum part.  The
nondegenerate slice count has exponent

```text
1 + 2beta - 33/16,                                (5.1)
```

while the parabolic square-root term in (4.3) has exponent

```text
3/2 + 3beta/2 - 33/16.                            (5.2)
```

The universal slice cap in the complementary range has exponent `1-beta`.
Balancing (5.2) with `1-beta` gives

```text
beta=5/8,                 common exponent=3/8.     (5.3)
```

At this value (5.1) is only `3/16`, so the nondegenerate term is strictly
smaller.  Thus the split is controlled by the parabolic square-root term
and the universal slice cap.

---

## 6. Operator and transverse consequences

The exact fourth-trace expansion and the closed repeated/permutation
sectors give

```text
||A_z||_op^4
 <= tr((A_z^* A_z)^2)
 << D + |Q_nd(z)|.                                 (6.1)
```

Taking fourth roots of (0.1) proves (0.2).  The established smooth
band-pass theorem includes every cubic orientation, and its Schwartz-tail
transfer changes an operator exponent `theta` into

```text
1/2 + theta(16/33).                               (6.2)
```

For `theta=11/32`,

```text
1/2 + (11/32)(16/33)
= 1/2 + 11/66
= 2/3.                                            (6.3)
```

```text
bounded-slice low-P sector:                        PROVED;
large-lambda2 universal cap D^(3/8+o):             PROVED;
small-lambda2 parabolic cap D^(3/8+o):             PROVED;
absolute fourth trace D^(11/8+o):                  PROVED;
carry operator D^(11/32+o):                        PROVED;
transverse exponent 2/3 via smooth transfer:       PROVED;
full four-cycle D^(1+o):                           OPEN;
quarter-power operator / QP / uniform strip:       NOT CLAIMED.
```
