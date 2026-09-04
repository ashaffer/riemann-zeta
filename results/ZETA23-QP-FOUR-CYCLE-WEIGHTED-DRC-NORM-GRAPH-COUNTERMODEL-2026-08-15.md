# QP four-cycle: exact weighted-DRC norm-graph countermodel

**Date:** 2026-08-15  
**Verdict:** carrier count, pair uniqueness, full symmetry, the degree and
color-Frobenius caps, all-eight-distinctness, and absence of completed
`3 x 3` grids do **not** imply the weighted four-cycle bound.  An exact
projective norm-graph construction obeys all those combinatorial resources
and has generic flat rank-one mass larger than the cap `D` by an unbounded
factor.

The construction is not a QP counterexample: its symbolic triples do not
satisfy `8abc=q^3+O(qD)`.  It proves that the reopened route must use the
joint cubic carry labels, not only a carrier-budget/DRC dichotomy.

---

## 1. The linear symmetric triple system

Let `r>3` be an odd prime power, let `F=GF(r)`, `K=GF(r^2)`, and write
`N:K^* -> F^*` for the norm.  Take disjoint row and carrier copies of

```text
V=K x F^*,                         |V|=n=r^2(r-1),  (1.1)
```

and take the nonzero elements of `K` as colors.  Join

```text
u=(A,a), v=(B,b)  iff  N(A+B)=ab,                  (1.2)
```

and color this edge by

```text
C=A+B in K^*.                                       (1.3)
```

For fixed `u` and `C`, equations (1.2)--(1.3) give uniquely

```text
B=C-A,                  b=N(C)/a.                  (1.4)
```

The same is true from the carrier endpoint.  Consequently:

```text
row degree = carrier degree = Delta=r^2-1;
number of colors = Delta;
every color is a perfect matching of degree n.      (1.5)
```

Make every colored edge the unordered hyperedge `{u,v,C}` and include all
six tensor permutations.  Because the role sets are disjoint and the edge
coloring is proper, this is a symmetric linear 3-uniform hypergraph.  With

```text
D_0=n=r^2(r-1),                                     (1.6)
```

every node and every color has degree at most `D_0`.  There are exactly `n`
active carriers.  Padding by isolated labels can impose any larger ambient
budget; in particular it can impose `D_0=N^(16/33+o(1))`.  The symbolic
nodes can also be injectively renamed by distinct shell primes, so
coprimality does not repair the construction.  What cannot be retained
under such a renaming is the cubic carry equation.

---

## 2. There is no completed `3 x 3`

Any three distinct row vertices have at most two common carriers.  If two
of their `K` coordinates agree, a common carrier would force their distinct
`F^*` coordinates to agree, so there is none.  Otherwise divide the three
norm equations by one of them and make the fractional-linear substitution
used for projective norm graphs.  The two remaining equations become

```text
(Y+A_1)(Y^r+A_1^r)=b_1,
(Y+A_2)(Y^r+A_2^r)=b_2.                            (2.1)
```

Subtracting makes one variable linear in the other; substitution leaves a
nonzero quadratic.  Hence there are at most two solutions.  This is the
elementary `t=3` proof of Theorem 1 in Alon--Rónyai--Szabó,
[*Norm-graphs: variations and applications*](https://www.cs.tau.ac.il/~nogaa/PDFS/norm7.pdf),
JCTB 76 (1999), 280--290.

Thus the row-carrier graph is `K_(3,3)`-free.  Completed-grid determinant
rigidity is entirely vacuous on this example.

---

## 3. Exact four-cycle count

For two distinct rows `(A,a),(A',a')`, their codegree is

```text
0,        A=A';
r,        A!=A' and a=a';
r+1,      A!=A' and a!=a'.                         (3.1)
```

Indeed, with a common carrier `(B,b)`, the fractional-linear parameter

```text
T=(A+B)/(A'+B)                                     (3.2)
```

runs through the norm fiber `N(T)=a/a'`.  Every nonzero norm fiber has
`r+1` elements, and only the fiber of one loses the forbidden value `T=1`.

Summing `binom(codegree,2)` over row pairs gives exactly

```text
#C4 = r^3(r-1)(r^2-1)(r^2-3)/4.                   (3.3)
```

Put `z_C=Delta^(-1/2)` on all colors.  Every ordered rectangle has weight
`Delta^(-2)`, so its total nondegenerate flat mass is

```text
4#C4/Delta^2
 =r^3(r-1)(r^2-3)/(r^2-1) asymp r^4.              (3.4)
```

This already exceeds `D_0 asymp r^3`.

---

## 4. The excess survives the all-eight-distinct quotient

On a rectangle the colors are

```text
C_ij=A_i+B_j.                                      (4.1)
```

The two rows have distinct `A_i`, and the two carriers have distinct
`B_j`, so adjacent colors are distinct.  A repetition can occur only on
one of the two opposite pairs.  For `C_11=C_22`, choose ordered
`A_1,A_2,B_1`; then `B_2` is forced.  Choosing `a_1` gives at most `r-1`
scalar lifts, since the other three scalar coordinates are forced by three
corners and the fourth is a check.  Therefore the two opposite-equality
events together contain at most

```text
2r^4(r^2-1)(r-1)                                   (4.2)
```

ordered rectangles.  Subtracting (4.2) from four times (3.3), then dividing
by `Delta^2`, leaves the exact lower bound

```text
generic flat mass >=r^3(r-3),
generic flat mass / D_0 >=r(r-3)/(r-1).             (4.3)
```

Because the three role sets are disjoint, four distinct colors mean all
eight displayed rectangle labels are distinct.  Thus the super-target mass
does not hide in the repeated-coordinate sector.

---

## 5. Consequence for the reopened route

The hoped-for abstract dichotomy

```text
rank-one mass >> D
  => carrier reuse forces a completed 3x3 grid       (5.1)
```

is false.  Here carriers have degree `r^2-1`, colors have the full allowed
degree `D_0`, the generic mass is `~rD_0`, and there is no completed grid.
Nor can Cauchy--Schwarz plus an unweighted average of fixed-color
multiplicity close the arbitrary-`z` problem: `z` can concentrate on the
exceptional color rectangles.  The separate full-integer tangent family
already gives one fixed matrix with multiplicity `sqrt(D)-1`.

The smallest viable positive statement must mention the simultaneous
integer equations

```text
8a_i b_j c_ij=q^3+r_ij,              |r_ij|<<qD,   (5.2)
```

around many rectangles or around a dense core.  Degree budgets, symmetry,
linear-hypergraph structure, carrier reuse, determinant rigidity of grids,
and weighted DRC alone cannot supply FC.

---

## 6. Status

```text
full resource-capped symmetric linear countermodel: PROVED;
no completed 3x3 in that countermodel:              PROVED;
generic flat mass / D tends to infinity:            PROVED;
same construction satisfies cubic carry equations: NO;
carrier-budget/weighted-DRC closure without carry:  FALSE;
fixed-k actual completion average q^o:               OPEN;
four-cycle bound (FC):                               OPEN.
```

Finite replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_norm_graph_countermodel.py
```
