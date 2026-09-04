# QP four-cycle: Pluecker ruling inverse and the scattered-secant gate

**Date:** 2026-08-25
**Verdict:** the sharp four-cycle bound is **not proved**.  The exact
algebraic meaning of a tangent secant is now clean, and it corrects one
tempting but false determinant-sensitive route.

For the signed color form

```text
K=(c11,-c12;-c21,c22),       k=det K,
F_K(x,y)=x^T K y,
```

the bilinear Pluecker identity is

```text
F_K(a,b)F_K(A,B)-F_K(a,B)F_K(A,b)
  =k det(a,A)det(b,B).                              (0.1)
```

If `M=ab^T`, `M'=AB^T`, `E=M-M'`, and both completions have level `L`,
then

```text
det E=-det(a,A)det(b,B),
F_K(a,B)F_K(A,b)=L^2+k det E.                      (0.2)
```

The last quantity is **not** the tangent degeneracy.  At the active scale
it is nonzero.  Tangency instead means that a fixed-level, fixed-determinant
secant quadric contains an affine ruling.  If

```text
E, E+V, E+2V
```

have one `K`-level and one determinant, then exactly

```text
<K,V>=0,             det V=0,             B_det(E,V)=0,  (0.3)
```

where

```text
B_det(E,V)=E11 V22+V11 E22-E12 V21-V12 E21.        (0.4)
```

Thus a nonzero direction is rank one, `V=lambda p q^T`, and its tangent
equation is

```text
p^T K q=0.                                           (0.5)
```

This is the precise algebraic object that a tangent-packet merger removes.
It does not control the scattered full-rank secants left afterwards.

---

## 1. Bilinear Pluecker identity

Put

```text
U=(a,A),                 V=(b,B).
```

The matrix of the four bilinear pairings is

```text
U^T K V
 = (F_K(a,b)  F_K(a,B);
    F_K(A,b)  F_K(A,B)).                            (1.1)
```

Taking determinants proves (0.1).  Independently, direct expansion gives

```text
det(ab^T-AB^T)=-det(a,A)det(b,B).                  (1.2)
```

Equations (0.2) follow immediately when the two diagonal pairings in
(1.1) both equal `L`.

There are two different geometric invariants here.

1. `L^2+k det E` is the full-projective nondegeneracy parameter of the
   conic obtained after **fixing** `E`.
2. `(0.3)` is the ruling condition when `E` is allowed to **move** in one
   fixed determinant layer.

Conflating them would incorrectly label the physical tangent family as a
degenerate fixed-`E` conic.  It is not: its nonzero `E` values are all
nonparabolic fixed-secant conics, while those `E` values themselves move
along a ruling.

At the QP scale the distinction is forced numerically.  The proved bounds

```text
1<=|k|<<D,       |det E|<<D^2,       |L| asymp |k|q
```

give

```text
|k det E|<<D^3=o(q^2)<=o(L^2).                     (1.3)
```

Hence `L^2+k det E` cannot vanish for sufficiently large `q`.

---

## 2. Three-point ruling inverse

For arbitrary two-by-two matrices,

```text
det(E+tV)=det E+t B_det(E,V)+t^2 det V.             (2.1)
```

If the determinant at `t=0,1,2` is the same, subtracting the value at zero
gives

```text
B_det(E,V)+det V=0,
2 B_det(E,V)+4 det V=0.                            (2.2)
```

Therefore both coefficients vanish.  Equality of the linear levels at
`t=0,1` separately gives `<K,V>=0`.  This proves (0.3).

Conversely, the three equations in (0.3) inserted in (2.1) show that the
whole line `E+tV` remains in the same common-level/determinant layer.  Thus
(0.3) is an if and only if criterion for an affine ruling.

When `V` is nonzero, `det V=0` factors it over the rationals as a rank-one
matrix.  After clearing content, write `V=lambda p q^T`; then

```text
<K,V>=lambda p^T K q.                              (2.3)
```

This proves the exact tangent equation (0.5), without stationary-phase or
asymptotic notation.

---

## 3. The known tangent witness lands on the ruling exactly

Take

```text
C=(m,m-2h;m-h,m-3h),        D=h^2,
a(t)=(m+h+t,m+2h+t),
b(t)=(m-h-t,m+h-t).                                  (3.1)
```

Then direct calculation gives

```text
det K=-2h^2=-2D,
F_K(a(t),b(t))=-2h^2(m+3h),                         (3.2)
```

independently of `t`.  The carrier directions are

```text
p=(1,1),                q=(-1,-1),
p^T K q=0.                                             (3.3)
```

For the fixed-gap secant

```text
E_t=a(t)b(t)^T-a(t+d)b(t+d)^T,
```

one has

```text
det E_t=2h^2d^2,
E_(t+1)-E_t=2d J,          J=(1,1;1,1).             (3.4)
```

The direction `J` has rank one, `<K,J>=0`, and is tangent to the determinant
level.  Thus the witness is literally a ruling, not merely approximately
tangent.

This also refutes the proposed bound

```text
m(C)<<sqrt(D/|det C|)q^o(1).                        (3.5)
```

Indeed this family has

```text
|det C|=2D,               m(C)=h-1 asymp sqrt(D),  (3.6)
```

whereas the right side of (3.5), before the subpower, is `1/sqrt(2)`.
The color determinant measures a different transverse quantity; it does
not pay for tangent completion length.

---

## 4. A hostile residual model after every ruling is removed

The ruling inverse does not imply that a fixed determinant layer has only
subpolynomially many residual points.  There is an exact integer model.
Start with

```text
E_t=(t,1;-t^2-1,-t),
det E_t=1,                 tr E_t=0.                (4.1)
```

For distinct `s,t`,

```text
det(E_t-E_s)=-(t-s)^2 !=0.                          (4.2)
```

Consequently no rank-one ruling contains even two members of this family.
Nevertheless `0<=t<T` gives `T` points in a matrix box of radius `O(T^2)`:
the residual population is of square-root size after all tangent rulings
are deleted.

The model can be given four distinct positive color magnitudes.  For
`r>=3`, put `n=r^2-1` and

```text
K=(n,-(n+r);-(n-r),n-1),
Q=K^(-1)=(n-1,n+r;n-r,n).                           (4.3)
```

Both determinants equal one.  Replacing `E_t` by `E_t Q^T` preserves
determinant one and gives

```text
<K,E_t Q^T>=tr E_t=0.                              (4.4)
```

The four unsigned color entries `n,n+r,n-r,n-1` are positive and distinct.
Moreover each secant is individually a difference of rank-one integer
matrices on one fixed level `L`:

```text
M_t=(t,1;t(L-t),L-t),
N_t=(0,0;tL+1,L),
det M_t=det N_t=0,
tr M_t=tr N_t=L,
M_t-N_t=E_t.                                        (4.5)
```

Right multiplication by `Q^T` transfers (4.5) to the signed color form in
(4.3).

This is deliberately an **algebraic**, not actual-prime-shell, model.  The
pairs `(M_t,N_t)` do not form one common physical completion family.  Its
logical conclusion is exact: common level, fixed determinant, rank-one
endpoint equations, and deletion of every tangent ruling do not by
themselves produce a `q^o(1)` residual secant count.  A proof must retain
the common-family cocycle and the four simultaneous physical product masks.

---

## 5. Direct interface with the residual degree-product theorem

The ruling algebra has a sharper application to the new transition
incidence

```text
T_((b,B),(c,C))
 =sum_a kappa(a,b,c)kappa(a,B,C).                  (5.1)
```

Fix a residual edge, witnessed by

```text
(a,b,c), (a,B,C).                                  (5.2)
```

A left neighbor and a right neighbor are witnessed respectively by

```text
(x,b,d), (x,B,D),
(y,e,c), (y,E,C).                                  (5.3)
```

The missing cross transition `(e,E)--(d,D)` need not exist.  Nevertheless
the six physical product windows force its determinant to be small.

Put `Q=q^3` and write the six residuals as

```text
8abc=Q+r_bc,             8aBC=Q+r_BC,
8xbd=Q+r_bd,             8xBD=Q+r_BD,
8yec=Q+r_ec,             8yEC=Q+r_EC.              (5.4)
```

Direct multiplication gives the exact identity

```text
(Q+r_bd)(Q+r_ec)(Q+r_BC)
 -(Q+r_BD)(Q+r_EC)(Q+r_bc)
 =512 axy bB cC (de-DE).                           (5.5)
```

Every residual in (5.4) has size at most `qD`.  Three-factor telescoping
bounds the left side by

```text
6qD(Q+qD)^2.                                       (5.6)
```

All seven denominator coordinates on the right of (5.5) are comparable
with `q`.  Since `D=o(q^2)`, (5.5)--(5.6) prove

```text
|de-DE|<<D                                          (5.7)
```

for **every Cartesian pair** of neighbors around the shared edge.  This is
stronger than a four-cycle statement: it survives a missing cross corner.

Consequently, if

```text
U={(d,D): left neighbors},
V={(e,E): right neighbors},
F(u,v)=u1*v1-u2*v2,                                 (5.8)
```

then

```text
|F(u,v)|<<D                  for all (u,v) in U x V. (5.9)
```

The residual degree-product target is precisely

```text
|U||V|<<Dq^o(1).                                   (5.10)
```

Thus `(RDP)` has been reduced locally to a **physical Cartesian determinant
strip theorem**.  This reduction uses all six hard-window products and no
center convolution.

### 5.1 Pluecker classification of high determinant layers

For two vectors from each arm, bilinear Pluecker with
`K=diag(1,-1)` gives

```text
F(u1,v1)F(u2,v2)-F(u1,v2)F(u2,v1)
 =-det(u1,u2)det(v1,v2).                            (5.11)
```

It has two rigorous inverse consequences.

* If a Cartesian subblock `U0 x V0` lies in one fixed determinant layer
  `F=kappa`, then the left side of (5.11) vanishes.  Unless one side has
  only one point, one entire side must lie on a rational ray.  Such a
  monochromatic Cartesian block is a rank-one/tangent packet.
* More generally, a rank-one cross-determinant table has the same
  conclusion.  This is the two-dimensional shadow of the matrix ruling
  condition `<K,V>=det V=B_det(E,V)=0` in Section 2.

Mere high multiplicity of one layer does **not** force a Cartesian block.
It may be a matching, as in the affine example below.  Therefore (5.11)
does not prove (5.10) by itself.

### 5.2 A proved one-sided RDP sector

There is a useful exact packet-or-ruling theorem.  Suppose one whole arm is
the affine progression

```text
U={u0+t*p:0<=t<L},             L>=2,               (5.12)
```

and let `K0=max_(u,v)|F(u,v)|`.  For every `v in V`, subtracting the two
endpoint values gives

```text
(L-1)|F(p,v)|<=2K0.                                (5.13)
```

The integer token `F(p,v)` therefore has only

```text
1+2 floor(2K0/(L-1))=O(1+K0/L)                    (5.14)
```

possible values.  For a fixed token, the solutions `v` lie on one affine
line; differences `w` in that fiber obey

```text
F(p,w)=0.                                          (5.15)
```

This is exactly the parallel rank-one ruling induced by the packet
direction `p`.

If every such opposite-arm ruling fiber contains at most `R` retained
neighbors, then (5.14) gives

```text
|U||V|<<R(K0+L).                                   (5.16)
```

For a physical nontrivial packet, `L<<sqrt(D)` by the already proved
quadratic curvature bound, while (5.9) gives `K0<<D`.  Hence

```text
|U||V|<<RD.                                        (5.17)
```

In particular `(RDP)` is proved in this sector after the parallel fibers
have been merged down to `R=q^o(1)`.  The statement is symmetric in the two
arms.  A dominant packet occupying a `1/J` fraction loses only the explicit
factor `J`.

This is the strongest direct RDP consequence of the ruling algebra found
here.  It closes one-affine/one-ruling-sparse neighborhoods; it does not
close two scattered neighborhoods.

### 5.3 Literal hard-window sharpness and a method countermodel

There is a complete all-integer physical grid showing that (5.17) is sharp.
Let `L>=2`, set

```text
D=512L^2,                 q=2m,
p_i=(m+2i,m+2i+1),                    0<=i<L,
gamma_j=(m+2j+2,m+2j+1),              2L<=j<3L,
a_ij=m-2i-2j-2.                                  (5.18)
```

For `m>>L`, both triples on every transition have sum `3m`, and exact
expansion verifies

```text
|8 a_ij (p_i)_1 (gamma_j)_1-q^3|<=qD,
|8 a_ij (p_i)_2 (gamma_j)_2-q^3|<=qD.              (5.19)
```

The transition determinant is

```text
F(gamma_j,p_i)=2(i-j)-1!=0.                        (5.20)
```

Thus these are `L^2` literal residual hard-window edges forming a complete
affine biclique, and the central degree product is

```text
L^2=D/512.                                         (5.21)
```

For fixed `i-j`, (5.20) is a high-multiplicity determinant layer along an
affine diagonal.  It is a packet/ruling, exactly as (5.11)--(5.15) predict.
The physical quadratic window truncates its length at `sqrt(D)` and makes
the product saturate, rather than violate, `(RDP)`.

There is also a rigorous limitation on using only completed four-cycles.
Delete every edge of (5.18) except one central row-star and column-star.
All retained edges still have the literal physical coordinates (5.18), the
central endpoint degrees remain `L,L`, and their product remains `D/512`.
But the retained graph is a double star and contains no completed
noncentral arm pair, hence no four-cycle on which the pair-completion
Pluecker identity can act.  The six-product identity (5.5) still sees all
`(L-1)^2` open arm pairs.

This is not a counterexample to `(RDP)`; it attains `(RDP)` at the correct
constant scale.  It proves that **four-cycle Pluecker alone** cannot be the
RDP proof, especially under physical deletions.  The missing-corner-stable
determinant strip (5.5) is essential.

The surviving open case is now precise:

```text
U and V both scattered,
|F(u,v)|<<D for every U x V pair,
each point additionally carries its actual hard-window row witness,
prove |U||V|<<Dq^o(1).                              (5.22)
```

Dropping the row witnesses makes (5.22) false: the primitive affine vectors
`(m+t,m+t+1)`, `0<=t<D`, have all pair determinants at most `D` but give
product `D^2`.  The hard-window curvature is therefore not optional.

---

## 6. Fixed-determinant midpoint normal form

There is a complementary exact statement for the matrix secants of
Sections 1--4.  Suppose

```text
<K,E>=<K,V>=0,       det(E+V)=det E=Delta,
Y=2E+V.                                               (6.1)
```

Then direct polarization gives

```text
<K,Y>=0,
B_det(Y,V)=0,
det Y=4Delta-det V.                                  (6.2)
```

When `det K`, `det V`, and `4Delta-det V` are nonzero, the first two
equations cut out a rank-two lattice on which determinant is a nondegenerate
binary quadratic form with nonzero right side.  The same elementary
divisor/Pell lemma used in the fixed-`(C,E)` theorem gives only `q^o(1)`
integral points of polynomial height.

The two exceptional cases are geometric.

* `det V=0` is the rank-one ruling of Section 2.
* `det V=4Delta` makes the midpoint norm zero.  Its rational solution locus
  is at most two null lines, again tangent rulings.  For example, with
  `K=diag(1,-1)`, `Delta=1`, and `V=2I`,

  ```text
  E_t=(-1,t;0,-1),          E_t+V=(1,t;0,1)         (6.3)
  ```

  is one such line.

Thus high fixed-displacement multiplicity on one fixed-determinant secant
quadric is forced into the same ruling geometry.  This is a valid additive-
energy input, but it does not bound the cardinality of a scattered Sidon
set such as (4.1), and therefore does not close (5.22).

---

## 7. Strongest valid consequence and remaining theorem

The new algebra validates the following decomposition principle.

* Any affine three-term family inside a fixed common-level/determinant
  secant layer has a rank-one `K`-tangent direction and belongs on a ruling.
* Such rich rulings are the correct objects to send to the existing
  affine/Hankel packet merger.
* What remains is a scattered family of full-rank secant chords.  The model
  in Section 4 proves that its size cannot be controlled from the local
  quadric equations alone.

The previously proved unconditional statements therefore remain the
strongest safe global ledger:

```text
fixed nonzero (C,E) multiplicity:          q^o(1),
fixed-C completion multiplicity:           D^(1/2)q^o(1),
dominant tangent/plane-coherent packets:    sharp D/K tail,
one-affine/one-ruling-sparse RDP sector:     PROVED,
scattered one-/two-point secant aggregation: OPEN.  (7.1)
```

In the corrected physical-incidence language, the last item is exactly the
rank-one zero-mode restriction

```text
||H(conj(z) tensor z)||_2^2
  <<D q^o(1)||z||_2^4,                              (7.2)
```

after the tangent rulings have been merged, with

```text
H_((a,a'),(c,c'))
 =sum_b kappa(a,b,c)kappa(a',b,c').                 (7.3)
```

No center convolution or grouped completion surrogate is used here.  A
successful next theorem has to show that a large zero mode in the scattered
sector forces many secants into one of the rulings classified by (0.3), or
derive cancellation directly from the common physical cocycle.  The
Pluecker identity identifies the inverse object; it does not yet prove that
inverse theorem.

---

## 8. Audit of the fixed-row-pair square-root theorem

The theorem labelled `(2E.R32)` in the weighted-secant report is a valid
local theorem in its stated transverse, all-distinct sector, but it is not
an endpoint-degree theorem for `T`.  The distinction is easiest to see by
writing the underlying three-partite relation as

```text
h(a,b,c)=1_(|8abc-q^3|<=qD).
```

The matrix used in `(2E.R32)` is

```text
B_((a,m),(c,d))=sum_b h(a,b,c)h(m,b,d).             (8.1)
```

For two distinct ordered row-pair vertices

```text
R=(a,m),       R'=(A,M),       aM-mA!=0,
```

its codegree counts quadruples `(b,B,c,d)` satisfying **four** incidences:

```text
h(a,b,c)h(m,b,d)h(A,B,c)h(M,B,d)=1.                (8.2)
```

By contrast, the residual transition matrix is

```text
T_((b,B),(c,C))=sum_a h(a,b,c)h(a,B,C),             (8.3)
```

and `deg_T(b,B)` counts objects satisfying only the **two** incidences in
(8.3).  Cyclic relabelling sends `(8.2)` to a codegree of two distinct
vertices of `T`; it cannot turn four incidences into the degree in `(8.3)`.
Formally,

```text
codeg_T(p,p')=sum_gamma T_(p,gamma)T_(p',gamma),
deg_T(p)=codeg_T(p,p).                              (8.4)
```

The proof of `(2E.R32)` assumes the transverse determinant of `p,p'` is
nonzero.  The diagonal specialization `p'=p` needed in (8.4) has determinant
zero and makes both the fixed-secant norm and the inverse conic degenerate.
The residual edge determinant `bc-BC!=0` is a determinant between one
center pair and one oppositely oriented color pair; it is not the missing
determinant between `p` and a second copy of `p`.

Here is the detailed hypothesis audit of the local theorem.

1. For one common neighbor, put

   ```text
   v=md-ac,       V=Md-Ac,       Delta=aM-mA.
   ```

   Directly subtracting the four product errors gives

   ```text
   |v|+|V|<<D,       d*Delta=a*V-A*v,       |Delta|<<D. (8.5)
   ```

   Hence every possible `d/c` for the fixed pair lies in one interval of
   length `O(D/q^2)`.  In the exact identity

   ```text
   J=-q^3*d*Delta/(8*a*A*c)
       +r*v/(8*a*c)-s*V/(8*A*c),                    (8.6)
   ```

   the variation between any two common neighbors is `O(D^2/q)=o(1)`.
   Since `J` is integral, it is one exact value for the whole fixed pair.
   Thus the reference to fixed neighboring slope blocks causes no omitted
   summation; indeed the block localization is unnecessary here.

2. Each coordinate of

   ```text
   X=(bc,bd;Bc,Bd)
   ```

   lies in an interval of length `O(D)`: for example
   `8a*bc-q^3=O(qD)`, and `a asymp q`.  Therefore every secant
   `E=X-X'` lies in an honest `O(D)` box.

3. On all-distinct actual-prime-power support, `(b,B)` and `(c,d)` are
   primitive.  The sub-unit missing-node interval excludes `b=B`; and the
   Pluecker factorization

   ```text
   det(X-X')=-det((b,B),(b',B'))det((c,d),(c',d'))
   ```

   makes every distinct-neighbor secant invertible.  These conclusions do
   not automatically extend to the repeated-coordinate sectors; those
   sectors require the separate deletion already assumed by the old
   report.

4. With `J` and a nonzero `E` fixed, the binary norm has discriminant
   `-4*Delta*det(E)` and nonzero right side.  Its divisor/quadratic-order
   bound is `q^o(1)`.  The normal lattice is primitive with determinant
   `asymp q`.  Its generic branch has `O(D)` short secants.  In the other
   branch the third minimum exceeds the `O(D)` box, so all differences lie
   in a rational plane; the rank-one quadric cuts a conic, giving
   `O(sqrt(D)q^o(1))`.  A reducible section contains at most one actual
   neighbor on each line because two points on a ruling would have
   determinant-zero difference.

Consequently the audited implication is exactly

```text
transverse all-distinct codeg_B(R,R')<<sqrt(D)q^o(1),  (8.7)
```

and, by cyclic symmetry, the corresponding **off-diagonal codegree** bounds
for `T`.  It supplies neither `deg_T(p)<<sqrt(D)` nor `(RDP)`.  Even at the
pure graph level a double star has every distinct-vertex codegree equal to
one while its central edge has arbitrarily large endpoint-degree product.

---

## 9. A weaker sufficient theorem for the rank-one residual target

The residual degree-product condition is sufficient but not necessary.
There is a strictly weaker mask-preserving closure which follows from only
one rowwise Cauchy--Schwarz.  Write

```text
d(p)=#N(p),
W(gamma)=sum_(p~gamma) d(p).                         (9.1)
```

Then for every vector `xi`, not merely a rank-one vector,

```text
||T_res xi||_2^2
 <=sum_gamma W(gamma)|xi_gamma|^2.                  (9.2)
```

Indeed

```text
|sum_(gamma~p)xi_gamma|^2
 <=d(p)sum_(gamma~p)|xi_gamma|^2,
```

and summing over `p` proves (9.2).  Therefore the neighbor-degree-sum
theorem

```text
max_gamma sum_(p~gamma)d(p)<<Dq^o(1)                (NDS)
```

already implies the desired residual estimate.  `(RDP)` implies `(NDS)`,
because on a fixed `gamma`,

```text
d(p)<=Dq^o(1)/deg(gamma)
```

for each of its `deg(gamma)` neighbors.  The converse is false.

On rank-one inputs, `(9.2)` can be written as the weighted copositive
inequality

```text
sum_(c,C) W(c,C) x_c*x_C
 <<Dq^o(1)(sum_c x_c)^2             for every x_c>=0. (WNDS)
```

Taking `x_c=|z_c|^2` proves

```text
||T_res(conj(z) tensor z)||_2^2<<Dq^o(1)||z||_2^4. (9.3)
```

This retains every ungrouped row-pair and every actual edge mask.  It is a
weighted energy condition, not the false center-convolution/CCSR
replacement.  However, positivity makes `(WNDS)` equivalent to `(NDS)` up
to a factor four, so it is a reformulation rather than a softer theorem.
Indeed `(NDS)` immediately implies `(WNDS)`.  Conversely, if an off-diagonal
ordered pair `(c,C)` maximizes `W`, choose `x_c=x_C=1/2` and all other
weights zero; nonnegativity gives the left side at least `W(c,C)/4`.
For a diagonal pair put all mass on its one coordinate.  Thus `(WNDS)`
forces `max W<=4Dq^o(1)`.

The strictness is witnessed by a completely explicit masked graph.  Take a
double star with central edge `(p_0,gamma_0)`, with

```text
deg(p_0)=L,       deg(gamma_0)=R,
```

and make the `L` color pairs `gamma_j` a directed matching on `2L`
different color coordinates.  Every row neighborhood is then a partial
matching and all off-diagonal codegrees on both sides are at most one.  Yet
the central degree product is `LR`.  Its rank-one energy is exactly

```text
|sum_(j<L) conj(z_j)z_(L+j)|^2
 +(R-1)|z_0|^2|z_L|^2
 <=R/4*||z||_2^4.                                  (9.4)
```

Choosing `L=R=floor(D/3)` makes `LR asymp D^2`, so `(RDP)` fails by a
power, while `(NDS)` holds since `max W=L+R-1<=D`, and (9.3) holds with
room to spare.  This is a rigorous combinatorial no-go to necessity of
`(RDP)`, not a claimed actual-prime hard-window counterexample.  Whether
the physical graph can violate `(RDP)` while still satisfying `(WNDS)` is
open.

The fixed-row-pair theorem controls individual off-diagonal entries of the
codegree Gram matrix.  It does not control the row sums `W(gamma)` in
(9.1), and a double star shows that no such implication is graph-theoretic.
The clean local degree-sum completion theorem isolated here is therefore
the equivalent pair `(NDS)`/`(WNDS)`.

### 9.1 Anchored determinant layers and the failed square-sum closure

There is one additional exact physical reduction, in the same
all-distinct sector after the already assumed repeated-coordinate deletion.
Fix an actual primitive color pair `gamma=(c,C)`.  If `gamma'=(d,D)` shares
a center-pair neighbor with `gamma`, the four product windows give

```text
|c*D-C*d|<<D.                                       (9.5)
```

For one fixed value `k=cD-Cd`, there is at most one shell pair `(d,D)`.
Indeed two solutions differ by an integral multiple of `(c,C)`; a nonzero
multiple has a coordinate displacement at least the smaller shell
endpoint, while the shell diameter is smaller than that endpoint.  Thus

```text
W(gamma)=sum_(gamma') codeg_T(gamma,gamma')
        =sum_(|k|<<D) m_gamma(k),                   (9.6)
```

with at most one partner on each determinant layer.  For `k!=0`, the
audited theorem only gives `m_gamma(k)<<sqrt(D)q^o(1)`, whose positive sum
is `D^(3/2)q^o(1)` and is insufficient.  The diagonal layer `k=0` is not
covered by that transverse theorem; it equals `deg_T(gamma)`, but the same
residual-determinant-layer uniqueness bounds this one term by `O(D)`.

The tempting repair

```text
sum_k m_gamma(k)^2<<Dq^o(1)                        (9.7)
```

is false before affine-packet removal.  In the exact physical integer
biclique (5.18), fix one color vertex.  Its `L` partners occupy distinct
determinant layers, each codegree is `L`, and `D_window=512L^2`.  Hence

```text
sum_k m_gamma(k)   =L^2=D_window/512,
sum_k m_gamma(k)^2 =L^3 asymp D_window^(3/2).       (9.8)
```

This packet saturates the desired first moment while violating (9.7) by a
power.  It belongs to the affine/ruling-coherent class, so (9.8) does not
rule out a post-peel square-sum theorem.  It does prove that such a theorem
cannot be inserted before the packet split.

After the split, the generic branch of `(2E.R32)` still permits a Sidon
transversal of `sqrt(D)` completions using `D` different secants.  Fixed-`E`
`q^o(1)` multiplicity controls repetitions of one secant, not the number of
different secants as `k` varies.  Abstractly, a finite-projective-plane
incidence with the anchor joined to all points has all off-diagonal
codegrees `O(sqrt(D))`, one partner per labelled determinant layer, and no
large pairwise intersection, but its anchored square sum and first moment
are too large.  This is not a hard-window construction; it shows exactly
which additional physical input is needed.

Equivalently, a proof of `(NDS)` is the anchored high-partner tail

```text
P_gamma(K):=#{gamma':K<=codeg_T(gamma,gamma')<2K}
 <<D*K^(-1)q^o(1).                         (AT_K)  (9.9)
```

uniformly in `gamma` and dyadic `K`.  This is equivalent to `(NDS)` up to a
`q^o(1)` factor.  In one direction, `(NDS)` and positivity give
`K P_gamma(K)<=W(gamma)`.  Conversely, codegrees have polynomial height,
so there are `O(log q)=q^o(1)` dyadic bins, and `(AT_K)` gives

```text
W(gamma)
 <=sum_K 2K*P_gamma(K)
 <<Dq^o(1).                                         (9.10)
```

For `K=q^o(1)`, the `O(D)` determinant layers already prove `(AT_K)` with
the permitted subpower loss.  Thus only power-rich partners matter.

The parabolic inverse theorem does not by itself prove `(AT_K)`.  It has
two exact limitations.

* A `K`-rich partner in the generic successive-minima branch can have
  `K` as large as `sqrt(D)` while using `asymp K^2` distinct secants once
  each.  Such a partner is not assigned any parabolic chart.
* In the exceptional branch, a power-rich partner does place a
  `q^(-o(1))` fraction of its completions in one of `q^o(1)` rational
  affine/Hankel charts.  But the chart and its direction depend on the
  partner.  The theorem supplies no bound on how those charts reuse the
  fixed anchor's completion set as the partner varies.

The exact missing exceptional packing statement can be written as follows.
For every exceptional `K`-rich partner `r`, select a chart subset
`C_r` of anchor completions with `|C_r|>=Kq^(-o(1))`, and merge locally
identical affine/Hankel charts into global packets.  One needs

```text
sum_r |C_r|<<Dq^o(1),                               (CP_K)
```

or a weighted packet inequality implying the same dyadic contribution.
Then `K P_gamma^exc(K)q^(-o(1))<=sum_r|C_r|` proves the exceptional part of
`(AT_K)`.  The affine biclique has `P=K=sqrt(D)` and makes `(CP_K)` sharp:
many local charts cohere into one packet and the total incidence is `D`.
The currently proved fixed-chart theorem controls one already identified
packet; it does not prove the cross-partner merger or `(CP_K)`.

This cardinal statement must be distinguished from the rank-one weighted
problem.  The previously proved high-completion theorem already aggregates
the weights of merged rich affine/Hankel packets at the sharp `D/K` scale.
Indeed the parabolic inverse gives `q^o(1)` charts for one exceptional
partner, so one chart contains `Kq^(-o(1))` completions; the
height-versus-length estimate and gap-token aggregation absorb the
subpower chart split.  Therefore the exceptional/coherent contribution to
the **rank-one weighted tail** is already closed.  What remains unproved is
the stronger unweighted `(CP_K)`, and it is not necessary if one continues
on the weighted route.

For the generic partners one separately needs

```text
P_gamma^gen(K)<<D*K^(-1)q^o(1),                    (GP_K)
```

a scattered-secant packing theorem.  Fixed-`E` multiplicity does not imply
`(GP_K)`, since each rich generic partner may use different secants.

Without `(CP_K)` and `(GP_K)`, the best positive bound furnished by the
audited inputs is only

```text
P_gamma(K)<<D                                      (all K),
P_gamma(K)<=1                              if K>>sqrt(D)q^o(1),
W(gamma)<<D^(3/2)q^o(1).                            (9.11)
```

The existing fixed-integral-level divisor theorem proves `(AT_K)` inside
one pinned level, but distinct partners have distinct, `q`-separated
levels.  Consequently its positive sum gives no saving.  The generic
varying-level aggregation `(GP_K)` and the cross-partner chart packing
`(CP_K)` are the two precise residual inverse theorems, isolated without
any false center convolution.  For the original rank-one target, the
weighted packet theorem replaces `(CP_K)` in the coherent sector, leaving
only the generic/scattered weighted analogue of `(GP_K)` (the existing
factorial-secant/triangle or reciprocal-height square-function gate).

### 9.2 Hu's hereditary Young theorem does not supply `(GP_K)`

Theorem 1.3 of X. Hu, *Complexity-sensitive additive energy and
off-diagonal Young inequalities on bounded-degree algebraic varieties*,
[arXiv:2608.18956](https://arxiv.org/abs/2608.18956), is a genuine new
hereditary convolution theorem.  In its near-diagonal case, hereditary
energy bounds

```text
E(A)<<K_X |A|^(2+eta),       E(B)<<K_Y |B|^(2+eta)
```

imply an `ell^p*ell^q -> ell^2` estimate for `1<=p,q<=2` and
`1/p+1/q>=1`.  It does not, however, control the projection/fibre trace
which defines `(AF_2)`.

There is an exact full-vector convolution model.  Fix the anchor `gamma`,
let `r` run over its dyadic `K`-rich partners, and let `S_r` be the set of
their common completion product matrices.  In the cyclic fixed-pair chart
one may take

```text
X=(b,B)^T*(a,x),       det X=0.
```

Retain an injective partner tag `tau(r)`, either the full pair `(d,D)` or
the determinant layer `k=cD-Cd`, and put

```text
S={(tau(r),X):X in S_r},       F=1_S.
```

On the full additive group of tag and matrix coordinates,

```text
R=F*tilde(F),
sum_(E!=0) R(0,E)
 =sum_r |S_r|(|S_r|-1)=F_(2,K)(gamma).              (9.12)
```

Thus `(AF_2)` is an `ell^1` norm on the **zero-tag slice** of a
full-vector convolution.  Hu's theorem controls the full `ell^2` norm of
`R`; it neither takes the trace `tau=0` nor converts its `ell^2` norm to
the required `ell^1_E` norm without paying the number of distinct secants.
A generic Sidon fibre has `K^2` distinct secants and exactly saturates that
loss.

There is also an intrinsic-exponent obstruction before one even invokes
Theorem 1.3.  The safe bounded-degree variety retaining the full tag is

```text
V_0=A^2_tau x {X in A^4:det X=0} subset A^6.
```

It has dimension `m=5`, full difference dimension `d=6`, hence

```text
sigma=2m-d=4,       alpha(V_0)=1+2sigma/m=13/5.     (9.13)
```

Hu's general theorem therefore starts at exponent `13/5`, not at the
hereditary exponent `2` assumed by Theorem 1.3.  Using only the injective
scalar determinant tag improves this merely to
`A^1 x {det X=0}` with `(m,n,alpha)=(4,5,5/2)`.  The actual partner lift
`k -> (d(k),D(k))` is modular/prime and is not a bounded-degree algebraic
map, so its two coordinates cannot be recovered polynomially from `k`.
Adding the pinned level as a coordinate and imposing its bilinear equation
gives a five-dimensional variety in `A^7`; even with maximal difference
dimension its intrinsic exponent is at least `11/5`.  Fixing one partner instead leaves a
two-dimensional quadric section in `A^4`, where the post-line-peel
near-diagonal theorem can apply, but applying it separately to each
partner supplies no cross-partner aggregation.

Dropping the tag is not a legal repair.  If `pi(tau,X)=X`, then

```text
(pi_*F*widetilde(pi_*F))(E)=sum_t R(t,E),           (9.14)
```

whereas `(9.12)` needs only `R(0,E)`.  Formula (9.14) inserts every
cross-partner pair, precisely the false projected/center-convolution
surrogate.

An exact counterexample shows that even granting Hu's strongest
near-diagonal hypothesis cannot recover the zero-tag tail.  Put

```text
S_(P,K)={(r,r^2,t,t^2):0<=r<P, 0<=t<K}
        subset V={(r,r^2,t,t^2)} subset A^4.        (9.15)
```

The product-of-parabolas variety is irreducible, bounded-degree, has no
affine lines and has the near-diagonal hereditary exponent: for every
subset, one ordered input pair permits at most four ordered output pairs.
Since a sum and a sum of squares determine an unordered pair,

```text
E(S_(P,K))=(2P^2-P)(2K^2-K)<<|S_(P,K)|^2.          (9.16)
```

Nevertheless its zero-tag off-diagonal mass is

```text
sum_(E!=0)R(0,E)=P*K*(K-1).                        (9.17)
```

Taking `P=D`, `K=sqrt(D)` violates the desired `D*K` bound by
`sqrt(D)`, despite (9.16) and the absence of affine lines.  Projection
turns the indicator into the multiplicity-`P` function on the second
parabola and changes (9.17) to `P^2*K*(K-1)`, an additional exact factor
`P`.

The theorem actually needed is therefore a **tagged trace/Carleson Young
inequality** for the physical family of post-peel quadric sections.  With

```text
Tr_0(F,G)(E)
 :=sum_tau sum_(X-Y=E) F(tau,X) conjugate(G(tau,Y)),
```

its indicator endpoint must say

```text
||Tr_0(F,F)||_(ell^1(E!=0))<<D*K*q^o(1)             (9.18)
```

on the dyadic `K`-rich mask.  A weighted route may replace (9.18) by a
vector-valued `ell^2_E` Bessel inequality across the distinct pinned
normals/levels, together with the already isolated reciprocal-height
Carleson packing.  Hu proves neither this zero-tag mixed norm nor the
required outer-tag orthogonality.  His theorem is applicable inside a
fixed generic section after the line peel, but it cannot prove `(GP_K)` or
`(AF_2)` across the varying physical partner tags.

---

## 10. Mechanical verification

Exact finite replay and hostile tests are in

```text
src/qp_tangent_plucker_inverse.py
src/test_qp_tangent_plucker_inverse.py
```

They verify (0.1)--(0.5), the full tangent family, the failure of (3.5),
the transformed residual model (4.1)--(4.5), the six-product identity
(5.5), the one-sided affine-fiber theorem, the physical grid (5.18)--(5.21),
the cycle-free double-star deletion, the directed-matching rank-one
double-star, its neighbor-degree sum, the anchored first/second codegree
moments, the tagged product-of-parabolas projection obstruction, and the
midpoint form (6.2).

The polynomial identities are independently certified in Lean:

```text
lean/weilcert/QPTangentPluckerInverse.lean
```

Final focused verification on 2026-08-25:

```text
python3 -m pytest -q src/test_qp_tangent_plucker_inverse.py   14 passed
python3 -m py_compile src/qp_tangent_plucker_inverse.py \
  src/test_qp_tangent_plucker_inverse.py                      passed
(cd lean/weilcert && lake env lean QPTangentPluckerInverse.lean) passed
```

The certificate proves the bilinear Pluecker identity, the rank-one
difference determinant, the equal-level cross factor, the three-point
ruling inverse, the tangent witness identities, the six-product shared-edge
identity, the cross-determinant Pluecker identity, the midpoint normal form,
the fixed-row determinant/defect and pinned-level identities used in the
`(2E.R32)` audit, and the residual models.

```text
bilinear Pluecker identity:                         PROVED;
fixed-E full conic parameter nonzero at QP scale:   PROVED PREVIOUSLY;
three-term secant ruling inverse:                   PROVED;
exact tangent equation p^T K q=0:                  PROVED;
determinant-sensitive cap sqrt(D/|k|):              FALSE;
sqrt-box ruling-free fixed-det residual model:      CONSTRUCTED;
six hard-window products force |de-DE|<<D:          PROVED;
monochromatic Cartesian layer forces a ruling:      PROVED;
one-affine/one-ruling-sparse RDP sector:             PROVED;
physical affine RDP saturation at constant*D:        CONSTRUCTED;
four-cycle Pluecker alone proves RDP:                FALSE AS A METHOD;
fixed-row-pair sqrt(D) theorem is locally valid:    PROVED/AUDITED;
cyclic R32 implies an endpoint degree cap:          FALSE (ARITY ERROR);
AT_K iff NDS up to q^o:                             PROVED;
anchored codegree square sum <=D:                   FALSE PRE-PEEL;
weighted coherent/parabolic high tail:              PROVED PREVIOUSLY;
generic scattered partner packing GP_K:             OPEN;
Hu Theorem 1.3 proves GP_K/AF_2 after line peel:     NO (TAGGED TRACE MISMATCH);
naive projection away from the partner tag:         FALSE (EXACT COUNTERMODEL);
tagged trace/Carleson Young inequality:              OPEN;
unweighted cross-partner chart packing CP_K:         OPEN/NOT NEEDED WEIGHTED;
RDP is necessary for the rank-one target:            FALSE ABSTRACTLY;
two-scattered physical Cartesian determinant strip: OPEN;
tangent-ruling merger alone closes zero mode:       NO;
scattered physical secant inverse theorem:          OPEN;
sharp four-cycle bound:                             NOT PROVED.
```
