# QP narrow tokens: content rigidity and the anchored codegree-Carleson gate

**Date:** 2026-08-25  
**Binary verdict:** this audit does **not** prove the sharp four-cycle bound.
It corrects the quantitative role of the Cramer two-anchor estimate and
replaces the unnecessarily strong residual degree-product conjecture by a
strictly weaker, exact row-sum problem.

The main conclusions are:

1. primitive physical vectors impose `gcd(k,r)|delta` on their Cramer
   tokens, and token areas equal the base minor times physical areas;
2. after inserting these facts, the existing two-anchor lattice count is
   always at least a constant times `D`, so it cannot by itself close even
   a nontrivial broad arm;
3. the weighted rank-one neighbor-degree condition `(WNDS)` is equivalent,
   up to a factor four, to the unweighted maximum row sum `(NDS)`;
4. that row sum is the `ell^1` mass of one anchored codegree distribution;
5. the exact remaining inverse theorem is a weak-`ell^1`/Carleson tail
   bound for rich anchored codegrees.  The physical affine grid saturates
   this bound with constant size, rather than refuting it.

## 1. Primitive Cramer tokens retain the physical area scale

Fix primitive integer vectors and orient

```text
delta=det(p,q),       k=det(p,u),       r=det(u,q).
```

Cramer's rule gives

```text
delta*u=r*p+k*q.                                      (1.1)
```

If `g=gcd(k,r)`, then `g` divides both coordinates of `delta*u`.
Primitivity `gcd(u_1,u_2)=1` and Bezout therefore imply

```text
gcd(k,r)|delta.                                      (1.2)
```

For two physical vectors `u_1,u_2`, direct determinant expansion gives

```text
det((k_1,r_1),(k_2,r_2))
 =-delta*det(u_1,u_2).                               (1.3)
```

Thus token coordinates do not create a new transverse saving: their
content is controlled by `delta`, while their area is exactly the physical
area multiplied by `|delta|`.

## 2. The two-anchor estimate does not close a broad sector

The proved integral two-anchor ceiling is

```text
|V| <=(2 floor(E/g)+1)
      (floor(2E*g/Delta_12)+1),                     (2.1)
```

where `g=gcd(k_1,r_1)` and `Delta_12` is the token area.  In the physical
range,

```text
E=|delta|D,
Delta_12=|delta|h,       1<=h<=D,
g|delta.                                                    (2.2)
```

Consequently the first factor in `(2.1)` is at least `2D+1`, and the
second is at least `3`.  Hence, exactly,

```text
right side of (2.1) >=3(2D+1).                      (2.3)
```

Even at maximal internal determinant this is only an `O(D)` degree bound.
The residual product target needs `|V|<<D/|U|`; `(2.1)` supplies no gain
when `|U|` is nontrivial.  The two-anchor lemma remains correct, but the
claim that it closes a broad token sector at the target scale was too
strong.

## 3. `(WNDS)` and `(NDS)` differ only by constants

Let

```text
W(c,C)=sum_(p~(c,C)) deg(p)>=0.                     (3.1)
```

The proposed weighted condition is

```text
sum_(c,C) W(c,C)x_c*x_C
 <=K (sum_c x_c)^2                    for x_c>=0.   (3.2)
```

Positivity immediately gives `(3.2)` with

```text
K=max_(c,C)W(c,C).                                  (3.3)
```

Conversely, for an off-diagonal ordered pair choose a vector supported
equally on `c,C`.  Its single directed contribution is `W(c,C)/4`, so any
valid constant in `(3.2)` satisfies

```text
max_(c,C)W(c,C)<=4K.                                (3.4)
```

A diagonal pair is detected with no factor four.  Therefore

```text
(1/4) max W <= best WNDS constant <=max W.          (3.5)
```

In particular, rank-one color weights do not hide a power-sized heavy
ordered pair.  The exact remaining sufficient theorem is simply

```text
max_(c,C) W(c,C)<<Dq^o(1).                          (NDS)
```

This is still strictly weaker than the edgewise degree-product theorem.

## 4. The row sum is an anchored codegree `ell^1` norm

For a fixed right vertex `gamma`, define

```text
r_gamma(eta)=#{p:p~gamma and p~eta}.
```

Double counting length-two paths gives the exact identity

```text
W(gamma)
 =sum_(p~gamma)deg(p)
 =sum_eta r_gamma(eta).                             (4.1)
```

For physical color pairs `gamma=(c,C)`, `eta=(d,D)`, four hard windows
give

```text
|cD-Cd|<<D.                                         (4.2)
```

On the actual narrow prime-power shell, `gcd(c,C)=1` in the all-distinct
sector.  For a fixed determinant label `h=cD-Cd`, two solutions differ by
an integral multiple of `(c,C)`.  The shell diameter is smaller than its
minimum coordinate, so there is at most one solution for each `h` (up to
the separately handled repeated-coordinate orientations).  Hence

```text
# supp(r_gamma)<<D.                                 (4.3)
```

Combining `(4.3)` with the known pointwise bound
`r_gamma(eta)<<sqrt(D)q^o(1)` gives only

```text
W(gamma)<<D^(3/2)q^o(1),                            (4.4)
```

missing the target by exactly `sqrt(D)`.

## 5. The sharp missing theorem

For dyadic `R>=1`, put

```text
N_gamma(R)=#{eta:r_gamma(eta)>=R}.
```

The exact new target is the anchored codegree-Carleson tail

```text
N_gamma(R)<<D*R^(-1)q^o(1)              for all R. (ACCT)
```

Dyadic summation of `(ACCT)` in `(4.1)` proves `(NDS)`, with only a
logarithm absorbed by `q^o(1)`.  Conversely `(NDS)` implies `(ACCT)` by
Markov, so these statements are equivalent up to that harmless dyadic
loss.  This is not another conjecturally stronger surrogate; it is the
distributional form of the exact row-sum theorem.

The literal affine hard-window biclique with side length `L` and
`D=Theta(L^2)` has, for every anchored color,

```text
r_gamma(eta)=L on L choices of eta.
```

Thus

```text
N_gamma(L)*L=L^2=Theta(D).                          (5.1)
```

It saturates `(ACCT)`.  This explains the geometry a proof must retain:
one rich ruling may carry `R` common neighbors, but only `D/R` opposite
vertices can participate at that richness.  Pointwise conic bounds ignore
this packing tradeoff.

After the already classified tangent/ruling charts are allocated, the
remaining analytic statement is a mask-sensitive incidence theorem:

> For one fixed actual color pair, reciprocal hard-window secants of
> multiplicity at least `R` occupy at most `D/R` determinant layers, up to
> a subpower factor.

Equivalently, prove a Carleson packing estimate for the fixed-level conics
indexed by `h=cD-Cd`.  Current local theorems bound each conic separately
by `sqrt(D)`; they do not square-sum or weak-`ell^1` sum across `h`.

## 6. Four-completion coordinates and a closed low-degree sector

Fix

```text
gamma=(c,C),       eta=(d,D),
```

and one common-center completion with row witnesses `a,x`.  Define

```text
r=x*d-a*c,       s=x*D-a*C,       h=C*d-c*D.       (6.1)
```

The four hard windows give `|r|+|s|<<D`, and direct expansion gives the
exact compatibility identity

```text
x*h=C*r-c*s.                                         (6.2)
```

For fixed `x,h`, the short error pair `(r,s)` is unique in the narrow box:
two solutions differ by a multiple of `(c,C)`, whose coordinates exceed
the box diameter.  Thus a rich codegree is a genuinely rich collection of
physical rows, not multiplicity hidden in one error label.

There is also a useful unconditional rich-level estimate.  Put

```text
H=deg(gamma),
B=max_(p!=p' in N(gamma)) codeg(p,p').              (6.3)
```

Every partner with `r_gamma(eta)>=R>=2` contributes at least `R(R-1)`
ordered distinct pairs from `N(gamma)`.  Double counting those pairs proves

```text
N_gamma(R) R(R-1)<=H(H-1)B.                         (6.4)
```

In the all-distinct transverse physical sector, the proved fixed-row-pair
theorem gives

```text
B<<sqrt(D)q^o(1).                                    (6.5)
```

Therefore `(ACCT)` is already proved throughout

```text
R >> H^2/sqrt(D) * q^o(1).                           (6.6)
```

At `R=1`, determinant-label support gives `(ACCT)` directly.  If

```text
H<=D^(1/4)q^o(1),                                    (6.7)
```

then `(6.6)` starts at constant richness.  Dyadic summation proves the
complete anchored row-sum theorem

```text
W(gamma)<<Dq^o(1)                                    (6.8)
```

for every such anchor.  This is a genuine closed sector of `(NDS)`.

For a general anchor, the only unclosed dyadic interval is

```text
q^o(1)<<R<<min(sqrt(D),H^2/sqrt(D)),
H>>D^(1/4).                                          (6.9)
```

Here the lower endpoint means that bounded or subpower richness is absorbed
by the permitted `q^o(1)` in the trivial `O(D)` support bound.

## 7. Rich inverse and the exact packet-overlap obstruction

The fixed-color completion theorem applies to the matrix

```text
(c C; d D).
```

Its completion count is exactly `r_gamma(eta)`.  In the **exceptional
successive-minima branch**, the parabolic inverse refinement says that a
fixed-power-rich matrix is, up to `q^o(1)` classes, carried by rational
parabolic/tangent charts.  Hence an exceptional partner with
`R>=q^epsilon` supplies an affine packet of length `R q^(-o(1))` in the
fixed-anchor reciprocal fan.  This conclusion is not currently proved for
the generic lattice branch, where richness may be spread across `O(D)`
different nonzero short secants.

What remains unproved is the packing implication

```text
number of fixed-anchor tangent charts carrying >=R actual completions
   <<D/R*q^o(1).                                    (APC)
```

The full-integer multilevel construction shows why `(APC)` must be a
Carleson theorem rather than bounded reuse.  For one fixed anchor it has
`sqrt(D)` partner charts, each with `sqrt(D)` common completions.  Their
product is exactly `D`, so the example saturates `(APC)`.

The current inverse theorem pins every genuine packet's completion
projection to one low-height continued-fraction ray, but does not pin the
remaining carrier slope.  Different parabolic charts over that ray can
therefore overlap the same anchor fan.  Proving that their actual
prime-power occupancy has total capacity `D` is the exact packet-overlap
obstruction.  Neither token geometry nor the pointwise conic theorem
supplies this packing.

There is a parallel generic obstruction: prove that fixed-anchor generic
secant families of multiplicity at least `R` occupy only `D/R` partner
determinant layers.  The fixed-nonzero-secant divisor theorem is pointwise
in the color matrix and does not control reuse of distinct short secants
across those matrices.  Thus a complete proof of `(ACCT)` needs two
Carleson packings, exceptional packet overlap and generic secant reuse.

## 8. What is and is not proved

```text
Cramer reconstruction and token area identity:       PROVED;
primitive token content divides delta:                PROVED;
two-anchor ceiling has unavoidable order-D floor:     PROVED;
WNDS equivalent to NDS up to factor four:             PROVED;
row sum equals anchored codegree L1 mass:              PROVED;
anchored determinant support has O(D) labels:          PROVED;
four-completion identity xh=Cr-cs:                     PROVED;
rich-tail dependent-pair inequality (6.4):             PROVED;
transverse NDS for anchor degree <=D^(1/4)q^o:         PROVED;
transverse ACCT for R >=H^2/sqrt(D)q^o:                PROVED;
pointwise sqrt(D) plus support closes NDS:              NO, loses sqrt(D);
affine ruling grid obeys and saturates ACCT:            PROVED;
fixed-power exceptional richness gives tangent charts:  PROVED PREVIOUSLY;
fixed-anchor tangent-chart Carleson packing (APC):       OPEN;
fixed-anchor generic secant Carleson packing:            OPEN;
anchored codegree-Carleson theorem ACCT:                OPEN;
sharp four-cycle bound:                                NOT PROVED.
```

The finite identities and hostile affine ledger are replayed in
`src/qp_narrow_token_row_sum_gate.py` and its focused tests.  The polynomial
Cramer identities are independently checked in
`lean/weilcert/QPNarrowTokenRowSumGate.lean`.
