# QP four-cycle: dyadic carrier-gap projection theorem

**Date:** 2026-08-15  
**Verdict:** three complementary color-pair projections give a rigorous
weighted bound for every fixed carrier-gap sector.  This strictly extends
the previously proved anisotropic tangent sector and leaves an explicit
minimal generic-gap remainder.  The carry shell does **not** automatically
put a rectangle in the new `O(D)` region: an exact all-prime active fixture
survives all three tests by a large finite margin.  The full four-cycle bound
remains open.

---

## 1. Setup

Let `T` be the symmetric carry hypergraph on a fixed-width shell `S`, with

```text
|8abc-Q| <= H,          Q=q^3,          H=O(qD),    (1.1)
```

where every node is between fixed positive multiples of `q`, `D<=q`, and
fixing two nodes determines at most one third node.  The last property is the
pair-uniqueness lemma already proved for the active QP window.

An ordered rectangle has edges

```text
(a_i,b_j,c_ij) in T,                 i,j in {1,2}. (1.2)
```

Fix nonnegative upper bounds

```text
A >= |a2-a1|,             B >= |b2-b1|,
R_ij >= |a_i-b_j|.                                  (1.3)
```

The sector cut out by (1.3) may be one ordinary dyadic box, or an exact-gap
subsector.  Put

```text
alpha=1+A,        beta=1+B,        rho_ij=1+R_ij.   (1.4)
```

All constants below may depend on the fixed shell and the constant in
`H=O(qD)`, but not on the dyadic scales.

---

## 2. One-corner localization

For a fixed color `c`, an active corner `(a,b,c)` satisfying `|a-b|<=R`
has only

```text
L(R) << 1+R+(D+R^2)/q << 1+R                    (2.1)
```

possible ordered carrier pairs.  Indeed, with `X=Q/(8c)` and
`u=(a+b)/2`,

```text
|u^2-X| <= H/(8c)+R^2/4,                           (2.2)
```

so `a` lies in an interval of length
`R+O((D+R^2)/q)`; pair uniqueness then fixes `b`.  The final inequality in
(2.1) uses `D<=q` and `R=O(q)` on the fixed shell.

This is the only arithmetic input beyond pair uniqueness.

---

## 3. The six fiber bounds

### 3.1 Horizontal color pairing

Fix `(c11,c12)`.  Starting at the shorter of its two corners gives at most

```text
F_top << alpha * min(rho_11,rho_12)                (3.1)
```

rectangles:

1. the anchor corner has `O(min(rho_11,rho_12))` choices by (2.1);
2. the other top carrier is fixed by pair uniqueness;
3. `a2` has at most `2A+1` choices;
4. the two bottom colors are then fixed.

The bottom pair has the symmetric bound

```text
F_bottom << alpha * min(rho_21,rho_22).            (3.2)
```

### 3.2 Vertical color pairing

The same argument after row-column interchange gives

```text
F_left  << beta * min(rho_11,rho_21),
F_right << beta * min(rho_12,rho_22).              (3.3)
```

### 3.3 Opposite color pairing

Fix `(c11,c22)` and anchor at whichever of these two corners has the shorter
cross-gap.  Once that corner is fixed, one may either choose `a2` in an
interval of length `2A`, after which `(a2,c22)` fixes `b2`, or choose `b2`
in an interval of length `2B`, after which `(b2,c22)` fixes `a2`.  Both are
valid bounds for the same fiber, so one may take their minimum:

```text
F_11,22 << min(alpha,beta) * min(rho_11,rho_22).
                                                               (3.4)
```

Likewise,

```text
F_12,21 << min(alpha,beta) * min(rho_12,rho_21).   (3.5)
```

No assumption about repeated or distinct colors is needed for these fiber
bounds.

---

## 4. Weighted theorem

For arbitrary complex coefficients `z`, discard the smooth edge factors in
absolute value and define

```text
M = sum_sector |z_c11 z_c12 z_c21 z_c22|.          (4.1)
```

Cauchy--Schwarz using the top and bottom color pairs gives

```text
M <= sqrt(F_top F_bottom) ||z||_2^4.               (4.2)
```

The two other complementary pairings give analogous estimates.  Therefore:

### Theorem 4.1 (dyadic carrier-gap projection theorem)

Under (1.1)--(1.3),

```text
M << min(Phi_h,Phi_v,Phi_o) ||z||_2^4,             (4.3)
```

where

```text
Phi_h = alpha * sqrt(
           min(rho_11,rho_12) min(rho_21,rho_22)),

Phi_v = beta * sqrt(
           min(rho_11,rho_21) min(rho_12,rho_22)),

Phi_o = min(alpha,beta) * sqrt(
           min(rho_11,rho_22) min(rho_12,rho_21)). (4.4)
```

In particular, every dyadic sector for which at least one of the three
quantities in (4.4) is `O(D)` already satisfies the target four-cycle bound.
The statement is an absolute arbitrary-complex weighted theorem, rather than
a count for one fixed color matrix.

### Recovery of the anisotropic tangent theorem

If, in one orientation,

```text
|a1-b1|<=R,       |a2-a1|<=T<=R,       R*T<=D,     (4.5)
```

then `|a2-b1|<=R+T<=2R`.  Hence the horizontal expression obeys

```text
Phi_h << T sqrt(R(R+T)) << RT << D.                (4.6)
```

Thus Theorem 4.1 contains all previously proved anisotropic tangent sectors,
and may additionally close sectors through the vertical or opposite-color
pairings even when the first orientation fails.

---

## 5. Exact generic-gap remainder

After applying Theorem 4.1, the unresolved dyadic sectors may be required to
satisfy all three strict inequalities

```text
alpha^2 min(rho_11,rho_12) min(rho_21,rho_22) >> D^2,

beta^2 min(rho_11,rho_21) min(rho_12,rho_22) >> D^2,

min(alpha,beta)^2
  min(rho_11,rho_22) min(rho_12,rho_21) >> D^2.    (5.1)
```

Together with the repeated-node deletion, (5.1) is a precise minimal
generic-gap gate.  It is stronger and less orientation-dependent than merely
requiring `RT>D` for each adjacent tangent orientation.

The gap inequalities do not, by themselves, contradict the carry shell.  In
the exact all-prime active fixture

```text
q=50021,
(a1,a2)=(21277,22741),       A=1464,
(b1,b2)=(28277,28793),       B=516,

(R_ij) = [7000 7516]
         [5536 6052],                                  (5.2)
```

all four edges have normalized Fourier residual below `.7`, and the four
colors are prime.  At the project cutoff `U=12`,

```text
D_project = ceil(12 q^2/(q/2)^(50/33)) = 6512.      (5.3)
```

The three scales are approximately

```text
Phi_h = 9.12e6,
Phi_v = 2.99e6,
Phi_o = 2.99e6,                                    (5.4)
```

so even the best exceeds `64 D_project`.  This is a rigorous finite warning,
not an asymptotic lower bound: shell membership and individual residual
smallness do not make Theorem 4.1 automatically exhaustive.  A further
arithmetic aggregation or spacing input is needed for (5.1).

---

## 6. Scope ledger

```text
six color-pair projection fiber bounds:             PROVED;
weighted dyadic gap theorem (4.3):                  PROVED;
anisotropic tangent theorem recovered:              PROVED;
automatic closure from shell geometry:              FALSE FINITELY;
minimal generic-gap sector (5.1):                   ISOLATED;
summation of all generic dyadic sectors at O(D):     OPEN;
full four-cycle bound (FC):                          OPEN.
```

The exact finite envelopes, the squared scale predicate, and the all-prime
fixture replay are in
`src/qp_four_cycle_gap_projection.py` and
`src/test_qp_four_cycle_gap_projection.py`.
