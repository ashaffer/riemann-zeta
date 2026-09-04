# QP four-cycle: weighted triangle Rademacher square and the exact unconditionality gate

**Date:** 2026-08-24  
**Verdict:** random residual-block signs already give the sharp fourth-trace
budget.  Removing the signs is the single new arithmetic step; it is not
proved here.

## 1. Weighted triangle blocks

For an actual all-distinct triple `e={i,j,k}`, its contribution to the
coefficient-weighted carry matrix is

```text
M_e(i,j)=z_k,       M_e(i,k)=z_j,       M_e(j,k)=z_i,   (1.1)
```

with the symmetric entries filled in.  Partition residuals into intervals
of diameter below `8 min(S)`.  The previously proved short-block lemma says
that every class is a vertex matching.  The full actual triple system is
linear: two distinct triples cannot share two vertices, since changing the
third shell integer changes the residual by `asymp q^2>qD`.

Let

```text
A_I(z)=sum_(e in I) M_e(z).                             (1.2)
```

## 2. A deterministic square-function bound

Put `s_e=sum_(v in e)|z_v|^2`.  Since the edges inside a class are
vertex-disjoint,

```text
sum_I A_I^* A_I=sum_e M_e^*M_e.                        (2.1)
```

The self terms obey

```text
sum_e ||M_e^*M_e||HS^2
 <=4 sum_e s_e^2
 <=12 Delta ||z||2^4,                                  (2.2)
```

where `Delta` is the maximum hyperedge degree.

If distinct edges `e,f` meet in `p`, the supports of `M_e^*M_e` and
`M_f^*M_f` meet only in the diagonal cell `(p,p)`.  Write

```text
d_e(p)=sum_(u in e, u!=p)|z_u|^2.                      (2.3)
```

Linearity makes the vertices occurring in these sums distinct for fixed
`p`, so `sum_(e contains p)d_e(p)<=||z||2^2`.  Moreover

```text
sum_p sum_(e contains p)d_e(p)
 =2 sum_u deg(u)|z_u|^2
 <=2 Delta||z||2^2.                                    (2.4)
```

It follows that

```text
||sum_I A_I^*A_I||HS^2 <=14 Delta||z||2^4.            (2.5)
```

The same proof gives the left square function

```text
||sum_I A_I A_I^*||HS^2 <=14 Delta||z||2^4.            (2.6)
```

## 3. Exact Rademacher consequence

Let `(epsilon_I)` be independent signs.  Expanding the fourth trace and
pairing the signs, or applying the elementary `S_4` noncommutative
Khintchine identity, gives

```text
E_epsilon ||sum_I epsilon_I A_I(z)||S4^4
 <= ||sum_I A_I^*A_I||HS^2
    +2||sum_I A_I A_I^*||HS^2
 <=42 Delta||z||2^4.                                   (3.1)
```

At the QP scale `Delta<<Dq^o(1)`, (3.1) is exactly the conjectured
four-cycle budget.

### 3.1 Coefficient-sensitive refinement

There is a stronger bound on one comparable coefficient bin.  Put

```text
s=||z||2,              B=||z||infinity^2,
theta=B/s^2.                                             (3.2)
```

For a vertex `p`, let

```text
S_p=sum_(e contains p) d_e(p).
```

Linearity makes all non-`p` vertices in this sum distinct.  It also leaves
at most `2 Delta` such vertices, hence

```text
S_p<=min(s^2,2 Delta B),
sum_p S_p<=2 Delta s^2.                                 (3.3)
```

The cross-edge part of either square-function Gram is therefore at most

```text
sum_p S_p^2
 <=2 Delta min(1,2 Delta theta)s^4.                     (3.4)
```

For the self terms, `s_e<=3B` and
`sum_e s_e<=Delta s^2`, so (2.2) sharpens to

```text
sum_e ||M_e^*M_e||HS^2<=12 Delta B s^2.                (3.5)
```

Combining the two estimates safely gives, on both sides,

```text
||sum_I A_I^*A_I||HS^2,
||sum_I A_I A_I^*||HS^2
 <=16 Delta min(1,Delta theta)s^4,                     (3.6)
```

and hence

```text
E_epsilon||sum_I epsilon_I A_I(z)||S4^4
 <=48 Delta min(1,Delta theta)||z||2^4.                (3.7)
```

If `z` lies in a factor-two height bin of support `M`, then
`theta<=4/M`.  At `Delta<<Dq^o(1)`, (3.7) becomes

```text
R_M(z)<<D min(1,D/M)q^o(1)||z||2^4.                   (3.8)
```

At the critical support `M=D^(15/8)`, its scale is only
`D^(1/8+o(1))`, not `D`.  This refinement does not prove the unsigned
estimate, but it moves every possible obstruction into the extreme
high-Walsh-multiplicity tail described in the companion defect-fan report.

Thus there is no remaining square-function loss.  The missing assertion is
the arithmetic unsigned-unconditionality estimate

```text
||sum_I A_I(z)||S4^4
 <=q^o(1) E_epsilon||sum_I epsilon_I A_I(z)||S4^4,      (3.9)
```

or a mask-stable second-tensor variant with the same consequence.

## 4. Why (3.9) is genuinely arithmetic

Resolvable Steiner triple systems partition into exactly the same kind of
matching classes.  For flat normalized `z`, their all-plus adjacency has a
large constant or component mode, while the randomized fourth trace obeys
(3.1).  Therefore (3.9) is false for abstract linear triple systems.

The actual QP family adds the ordered identity

```text
I=the interval containing 8abc-q^3,                    (4.1)
```

and product conservation rules out identical parallel classes.  The
quantitative boundary supplied by conservation is only one vertex, however,
so it does not yet prove (3.9).  Literal actual-prime examples also show
that adjacent block cross-Grams need not vanish.

The full coarse `q^2` principal continuum can be removed first: its weighted
fourth trace is `O(D^4/q^2)||z||2^4=O(D^(-1/8))||z||2^4`.  Hence (3.9) should
be formulated for the primitive ordered family (and, if one follows the
sector proof, for its actual post-peeling masks).

```text
random-sign weighted fourth trace O(D):                PROVED;
flat-bin random trace O(D*min(1,D/M)):                  PROVED;
coarse weighted principal polar:                       CLOSED;
all-plus arithmetic unconditionality:                  OPEN;
post-peeling complete-boundedness:                      OPEN;
new unconditional global exponent:                     NONE;
sharp four-cycle theorem:                              NOT PROVED.
```

Executable replay:

```text
src/qp_weighted_triangle_rademacher_square.py
src/test_qp_weighted_triangle_rademacher_square.py
```
