# QP carry grids: exact 3-by-3 determinant rigidity

**Date:** 2026-08-15  
**Verdict:** every completed `3 x 3` carry grid in the active shell has a
singular color matrix.  If its three row labels and three column labels are
distinct, the already proved `2 x 2` result upgrades this to **rank exactly
two with all nine `2 x 2` minors nonzero and `O(D)`**.  This is a new exact
rigidity theorem, but it does not yet prove that a large weighted four-cycle
sum contains a completed `3 x 3` grid.

Moreover, singularity, distinct prime entries, a narrow shell, and small
nonzero minors do not by themselves classify the color matrix: an explicit
rank-two prime matrix below has all of those properties.  Any closure must
retain the simultaneous row/column carrier equations.

---

## 1. Exact determinant quantum

Let

```text
Q=q^3,                       H=qD,
N_ij=8*a_i*b_j*c_ij=Q+r_ij, |r_ij|<=H               (1.1)
```

for `1<=i,j<=3`, with all row and column labels positive integers in the
shell.  Put `C=(c_ij)`, `R=(r_ij)`, and let `J` be the all-ones matrix.  The
two exact matrix factorizations are

```text
N=8*diag(a_1,a_2,a_3)*C*diag(b_1,b_2,b_3)=QJ+R.     (1.2)
```

Taking determinants on the first side gives

```text
det N=8^3*(prod_i a_i)*(prod_j b_j)*det C.           (1.3)
```

Hence, if `det C` is nonzero, then

```text
|det N| >= 8^3*(prod_i a_i)*(prod_j b_j).            (1.4)
```

This lower bound is the determinant quantum; it is `asymp q^6` in the
shell.

---

## 2. Rank-one background forces two residual columns

Expand `det(QJ+R)` multilinearly in its three columns.  Every term using two
or three columns of `QJ` vanishes because those columns are equal.  There are
three terms using exactly one `QJ` column.  The Leibniz formula bounds each
by `6QH^2`; the all-residual term is at most `6H^3`.  Therefore

```text
|det(QJ+R)| <= 18*Q*H^2+6*H^3.                      (2.1)
```

This estimate is deliberately elementary and has ample constant slack.

### Theorem 2.1 (completed-grid singularity)

If

```text
18*Q*H^2+6*H^3
 <8^3*(prod_i a_i)*(prod_j b_j),                    (2.2)
```

then `det C=0`.

**Proof.**  If `det C!=0`, (1.3)--(1.4) put `|det N|` at or above the
right side of (2.2), whereas (2.1) puts the same integer strictly below it.
QED

At the active scale, with `m=min S asymp q`,

```text
18*Q*H^2+6*H^3 = 18*q^5*D^2+6*q^3*D^3,
8^3*(prod a_i)*(prod b_j) >= 8^3*m^6 asymp q^6.     (2.3)
```

For `D=q^(16/33+o(1))`, the leading ratio is

```text
q^5*D^2/q^6=q^(-1/33+o(1)),                         (2.4)
```

and the `H^3` term is smaller.  Thus (2.2) holds for all sufficiently large
`q` after the same harmless truncation slack used in the `2 x 2` theorem.

### Corollary 2.2 (rank exactly two in a nondegenerate grid)

Assume additionally that the three `a_i` are distinct and the three `b_j`
are distinct.  Every `2 x 2` subgrid is then nondegenerate.  The previously
proved zero-minor exclusion and determinant bound give

```text
1 <= |c_ij*c_kl-c_il*c_kj| << D                     (2.5)
```

for every choice `i!=k`, `j!=l`.  In particular `C` cannot have rank one.
Theorem 2.1 therefore forces

```text
rank C=2, and all nine 2 x 2 minors are nonzero O(D). (2.6)
```

Equivalently, the adjugate is a nonzero rank-one integer matrix whose nine
entries are all `O(D)`.  This supplies short integral left and right null
relations, but it does not make them multiplicative identities.

---

## 3. Why singular-prime classification alone is false

Take the prime `q=1,688,917` and

```text
C = [844427  844433  844439]
    [844457  844463  844469]
    [844511  844517  844523].                        (3.1)
```

All nine entries are distinct primes and lie within `0.1%` of `q/2`.  The
matrix has the additive form

```text
c_ij=x_i+y_j,
x=(844427,844457,844511), y=(0,6,12),                (3.2)
```

so its rank is two.  Its `2 x 2` minors are

```text
(x_i-x_k)*(y_l-y_j),                                 (3.3)
```

and hence all nine are nonzero, with maximum modulus `84*12=1008`.  Exact
integer arithmetic gives

```text
1008^33 < q^16,
```

so even the numerical condition `|minor|<D=q^(16/33)` holds.

This is **not** asserted to be a completed carry grid: no row and column
carriers satisfying all nine equations (1.1) have been supplied.  It is a
counterexample only to the tempting claim that narrow-shell prime powers,
singularity, and small nonzero minors force repetitions or a permutation
matrix pattern.  The carrier completion is essential information.

---

## 4. Inverse-theorem audit: a grid is not forced yet

Let `A_z` be the weighted row-column carry matrix from the four-cycle
reduction.  The known color-degree bound gives

```text
||A_z||_F^2 <= D*||z||_2^2=D.                        (4.1)
```

If a positive nondegenerate fourth-trace contribution satisfies
`Q_nd(z)>=Lambda*D`, then

```text
||A_z||_S4^4 >= Lambda*D,
||A_z||_op^2 >= ||A_z||_S4^4/||A_z||_F^2 >= Lambda. (4.2)
```

The existing sparse theorem also yields, for `Lambda` larger than an
absolute constant,

```text
(sum_c |z_c|^4)^(-1) << D^2/Lambda.                 (4.3)
```

These are genuine concentration statements.  Neither one, at the present
exponents, invokes a standard dependent-random-choice theorem.  The
unweighted carry support has `n=q^(1+o(1))` vertices on each side and average
degree at most

```text
D=q^(16/33+o(1)) << n^(2/3),                         (4.4)
```

whereas the usual balanced `K_(3,3)` forcing threshold is average degree of
order `n^(2/3)`.  Restricting to `M` colors gives at most `MD` edges but does
not confine their row and column endpoints to `O(M)` vertices, so (4.3) does
not repair this exponent gap by itself.

There is also a sharp scope warning at the target scale.  Abstractly take
`B` disjoint copies of `K_(2,L)`, properly color every copy with the same
`L` colors by

```text
color(row i,column j)=i+j mod L,
```

and put `z_c=L^(-1/2)`.  Each color is a matching of size `2B`; choosing
`B=floor(D/2)` respects color multiplicity `D`.  The nondegenerate weighted
four-cycle mass is `asymp B=asymp D`, but the graph has no `K_(3,3)` because
every connected component has only two left vertices.  Thus target-size
four-cycle mass alone cannot imply a completed `3 x 3` grid in the abstract
properly colored model.

This example does not violate the desired `O(D)` bound and is not an
actual-shell counterexample.  It shows exactly what an inverse theorem would
have to improve: a **super-target** obstruction, together with the arithmetic
carrier constraints, must force either a completed grid or some other
rank-two structured object.  No such inverse theorem is proved here.

---

## 5. Status

```text
completed 3 x 3 grid => det C=0:                    PROVED;
distinct rows/columns => rank C=2 and minors 1..D: PROVED;
singular narrow prime matrix => repetitions:        FALSE;
FC obstruction => completed 3 x 3 grid:             OPEN;
classification with all carrier equations:          OPEN;
full four-cycle bound (FC):                          OPEN.
```

Exact finite replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_three_by_three_grid.py \
  src/test_qp_four_cycle_permutation_sector.py
```
