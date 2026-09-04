# QP slope blocks: K_(3,2), higher trace, and the reciprocal-height barrier

**Date:** 2026-08-22  
**Verdict:** the new three-row elimination is correct, but it does **not**
produce an exponent below `D^(21/16)` from the presently proved inputs.
The sixth trace counts weighted six-cycles, not common neighbours of a row
triple.  The strongest clean conversion through the `K_(3,2)` excess is

```text
||B||^2 <= Delta_R+2*n_R+(12*n_R*K_32)^(1/3),       (0.1)
K_32=sum_(row triples X) binom(t_3(X),2).            (0.2)
```

The arithmetic lemma turns (0.2) into an anchored reciprocal-height sum.
To improve `D^(21/16)`, it would be enough to prove either

```text
sum_y sum_(X subset N(y), |X|=3) 1/H(X)
       <<D^(31/16-epsilon),                          (RH-global)
```

or the stronger local version

```text
max_y sum_(X subset N(y), |X|=3) 1/H(X)
       <<D^(15/16-epsilon).                          (RH-local)
```

after coherent affine/tangent components have been split off.  Neither
estimate is currently proved.  Direct determinant dyadics give only the
much weaker operator estimate `D^(5/3+o(1))`.  Thus this route gives no new
uniform exponent as it stands.

This is a failure of aggregation, not of the elimination lemma.  A single
merged `K_(sqrt(D),sqrt(D))` tangent chart has norm squared `D` and is
harmless.  Many scattered charts, or a finite-geometric incidence design,
make the raw `K_(3,2)` moment polynomially too large even when the actual
operator is at the target scale.

---

## 1. Exact three-row elimination

Let the three left vertices be

```text
x_i=(a_i,A_i),                 i=1,2,3,
```

and suppose that the two right vertices

```text
y_1=(c_1,d_1),                y_2=(c_2,d_2)
```

are common neighbours.  Let `b_ij` be the carrier on `(x_i,y_j)` and write

```text
8*b_ij*a_i*c_j=q^3+r_ij,
8*b_ij*A_i*d_j=q^3+R_ij,
e_ij=a_i*c_j-A_i*d_j=(r_ij-R_ij)/(8*b_ij).          (1.1)
```

Thus `|e_ij|<<D`.  Subtracting the two residual-difference equations gives

```text
b_i1*e_i1-b_i2*e_i2=L(p,q),                         (1.2)
```

where the right side is independent of `i`.  Put

```text
p=(c_1,c_2),       q=(d_1,d_2),
K=c_1*d_2-c_2*d_1.
```

Direct elimination gives, for every `i`,

```text
d_2*e_i1-d_1*e_i2=K*a_i,
c_2*e_i1-c_1*e_i2=K*A_i.                           (1.3)
```

The narrow shell and primitivity imply that fixed `p` and `K` determine
`q`: two solutions differ by an integral multiple of the primitive vector
`p`, too large to remain in the shell.

Now set

```text
a=(a_1,a_2,a_3),       A=(A_1,A_2,A_3),
h=a cross A.                                             (1.4)
```

Slope localization gives `||h||_infinity<<D`, and exactly

```text
h dot a=h dot A=0.                                    (1.5)
```

If two nonparallel vectors `h,h'` of this size arose for a fixed primitive
positive `a`, then

```text
h cross h'=s*a,       s in Z\{0}.                     (1.6)
```

The left side has norm `O(D^2)`, whereas a nonzero right side has a
coordinate comparable with `q`.  Since `D^2=o(q)`, this is impossible.
Hence all realized short orthogonals lie on one primitive line.  Write

```text
h=t*h_0,       gcd(h_0)=1,       H=||h_0||_infinity. (1.7)
```

There are `O(1+D/H)` possible multipliers.  For a fixed multiplier, two
possible `A` vectors differ by an integral multiple of primitive `a`, again
too large for the shell; then (1.3) fixes the second column.  Consequently

```text
t_3(x_1,x_2,x_3)<<1+D/H(x_1,x_2,x_3).               (1.8)
```

The zero-cross-product case is absent in the all-distinct actual support.
Indeed `A=lambda*a` and pairwise coprimality force `lambda=1`; this repeats
the row coordinates.

The identities (1.3)--(1.7) are replayed in
`src/qp_k23_higher_trace_gate.py`.

---

## 2. What the sixth trace actually counts

Put

```text
M=B*B^*,       m(x,x')=#(N(x) intersect N(x')).
```

Then

```text
trace(M^3)=sum_(x_1,x_2,x_3)
               m(x_1,x_2)m(x_2,x_3)m(x_3,x_1).      (2.1)
```

This is a weighted count of closed six-walks.  Its three column vertices
may be distinct, and none need be common to all three row vertices.  A
literal six-cycle already has positive (2.1) and no `K_(3,2)` at all.
Therefore (1.8) does not bound `trace(M^3)` term by term.

The same issue appears in the anchored factorial quantity

```text
F(x)=sum_(x'!=x)m(x,x')*(m(x,x')-1).                (2.2)
```

Take `K_(2,s)`.  It has no three distinct left vertices and hence zero
`K_(3,2)` excess, while each of its two left vertices has

```text
F(x)=s*(s-1).                                      (2.3)
```

Nevertheless its norm squared is only `2s`, at the desired `O(D)` scale
when `s<=D`.  Thus an attempt to deduce `(AFP)` directly from (1.8) is
logically impossible; pair-only twins have to be retained as a safe
low-rank component.

---

## 3. The sharp graph-theoretic bridge

It is more efficient to transpose and put

```text
G=B^*B,
m(y,y')=#(N(y) intersect N(y')).                   (3.1)
```

The exact double count is

```text
K_32
 =sum_(three distinct rows X) binom(t_3(X),2)
 =sum_(y<y') binom(m(y,y'),3).                      (3.2)
```

For `m>=3`,

```text
(m-2)^3<=6*binom(m,3).                              (3.3)
```

Split every off-diagonal entry of `G` as

```text
m=min(m,2)+(m-2)_+.
```

The first matrix has norm at most `2(n_R-1)`.  Frobenius followed by
Holder in the second matrix gives

```text
||(m-2)_+||_op
 <=||(m-2)_+||_F
 <=(12*n_R*K_32)^(1/3).                            (3.4)
```

Including the diagonal proves (0.1).  A rowwise version is

```text
||B||^2
 <=Delta_R+2*n_R
   +n_R^(2/3)*(6*max_y K_y)^(1/3),                 (3.5)

K_y=sum_(y'!=y)binom(m(y,y'),3)
   =sum_(X subset N(y), |X|=3)(t_3(X)-1).          (3.6)
```

These inequalities correctly preserve the harmless `m<=2` base.  They are
strictly stronger here than using `trace((BB^*)^3)` without subtracting the
base.

---

## 4. The exact reciprocal-height gate

From (1.8),

```text
binom(t_3(X),2)
 <=(D/(2H(X)))*t_3(X).                             (4.1)
```

Summing and anchoring one of the common columns gives

```text
K_32 <=(D/2)*R_global,                              (4.2)

R_global=sum_y sum_(X subset N(y), |X|=3)1/H(X).  (4.3)
```

Similarly, (3.6) gives

```text
K_y<=D*R_y,
R_y=sum_(X subset N(y), |X|=3)1/H(X).             (4.4)
```

Since both vertex classes have size at most `D`, equations (3.4)--(4.4)
become

```text
||B||^2
 <<D+D^(2/3)*R_global^(1/3),                       (4.5)

||B||^2
 <<D+D*max_y(R_y)^(1/3).                           (4.6)
```

Therefore `(RH-global)` or `(RH-local)` with the displayed exponents gives
a strict improvement over `D^(21/16)`.  In particular, a global bound
`R_global<<D^(2+o(1))` would already give `D^(4/3+o(1))`, which is **not**
enough; the required exponent is strictly below `31/16`.

The local criterion is more demanding but naturally chart-aware.  A
column whose reciprocal-height mass is at the tangent scale `D` must be
merged rather than paid through (4.6).

---

## 5. What determinant dyadics prove, and why it is insufficient

Let `X` be a localized left-vertex set of at most `D` primitive shell
vectors.  For distinct `x,y`, write

```text
delta=|det(x,y)|,       1<=delta<<D.                (5.1)
```

For a third vertex `z`, put

```text
g=gcd(det(x,y),det(y,z),det(z,x)).                  (5.2)
```

If its primitive triple height is at most `R`, then `g>=delta/R` and
`g|delta`.  For fixed `x` and a fixed determinant `det(x,z)`, there is at
most one shell vector `z`: two solutions differ by an integral multiple of
primitive `x`, larger than the shell diameter.  Hence, for fixed `(x,y)`,

```text
#{z:H(x,y,z)<=R}
 <<sum_(g|delta, g>=delta/R) D/g
 <<(D*R/delta) q^o(1).                              (5.3)
```

For fixed `x`, the nonzero determinants `det(x,y)` are themselves distinct.
Summing (5.3), with the trivial bound `D` when `delta<=R`, gives

```text
#{ordered triples X:H(X)<=R}<<D^2*R*q^o(1).        (5.4)
```

Consequently

```text
sum_X 1/H(X)<<D^2 q^o(1),
sum_X 1/H(X)^2<<D^2 q^o(1).                        (5.5)
```

But substituting the pointwise codegree cap once more gives only

```text
K_32
 <<sum_X [D/H(X)+D^2/H(X)^2]
 <<D^4 q^o(1).                                     (5.6)
```

Equation (0.1) now yields

```text
||B||^2<<D^(5/3+o(1)),                              (5.7)
```

worse than `D^(21/16)`.  The local calculation gives the same exponent:
`R_y` can be as large as `D^(1+o(1))`, so (4.6) gives `D^(4/3+o(1))` even
for a single tangent-size neighbourhood, and the structure-free dyadic
bound can be still larger.  No choice of the height splitting point repairs
this: the `D^2/H^2` term is concentrated at the low-height end.

Thus the missing fact is not another divisor estimate for an individual
height.  It is a theorem saying that the low-height triples with many
common columns merge into a controlled number of affine packets, with the
remaining anchored mass satisfying `(RH-global)` or `(RH-local)`.

---

## 6. Sharpness audits

### 6.1 Projective plane: the `O(D)` base is sharp

For points versus lines in `PG(2,Q)`,

```text
n=Q^2+Q+1 asyp D,
degree=Q+1 asyp sqrt(D),
every two columns have codegree one.                (6.1)
```

Hence `K_32=0`, but the constant vector has

```text
||B||^2=(Q+1)^2 asyp D.                             (6.2)
```

This proves that the `min(m,2)` base in (3.4) cannot be discarded.  The
many projective triangles also show directly why a sixth-trace proof must
allow `Theta(D^3)` target-scale six-walk mass.

### 6.2 `PG(3,Q)`: the excess inequality is exponent-sharp

For points versus hyperplanes in `PG(3,Q)`,

```text
D asyp Q^3,
degree asyp Q^2=D^(2/3),
pair-column codegree asyp Q=D^(1/3).                (6.3)
```

Therefore

```text
K_32 asyp D^2*(D^(1/3))^3=D^3,
||B||^2 asyp D^(4/3).                               (6.4)
```

The excess term in (0.1) is exactly `D^(4/3)`.  In triple language, the
exceptional triples are the collinear triples: there are `D^(7/3+o(1))`
of them and each has `D^(1/3+o(1))` common hyperplanes.  The arithmetic
height lemma would force their heights below `D^(2/3+o(1))`.  The raw
capacity (5.4) is `D^(8/3+o(1))` at that height and therefore does not rule
out this design.

This is not a QP realization.  It identifies the exact arithmetic debt:
one must exclude a finite-geometric arrangement of many overlapping
low-height packets, not merely improve the graph inequality.

### 6.3 Tangent charts: moment size is not operator size

Let `D=L^2` and take one affine tangent chart with

```text
x_t=(m+t,m+h+t),             1<=t<=L.
```

For `t_1<t_2<t_3`, its primitive cross-product height is

```text
H=(t_3-t_1)/gcd(t_2-t_1,t_3-t_2)<=L.               (6.5)
```

The `K_(L,L)` incidence has triple codegree `L`, so (1.8) is sharp in
scale, while

```text
||B||^2=L^2=D,
K_32=binom(L,3)binom(L,2)=D^(5/2+o(1)).             (6.6)
```

Applied on this component with its actual `L` vertices, (0.1) recovers the
correct `O(D)` scale.  A structure-free union of `L` disjoint such blocks
has `D` vertices per side and

```text
K_32=D^(3+o(1)),
||B||^2=D,                                         (6.7)
```

whereas (0.1) pays `D^(4/3)`.  Componentwise merging restores `D`.
The existing full-integer multilevel tangent construction supplies exactly
this kind of warning, although its different directions need not occupy
one genuine QP slope block and its nodes are not actual prime powers.

Actual primality does not currently give a power saving for one affine
chart: simultaneous primality of two linear forms is at best removed by
logarithmic sieve factors.  The safe theorem is instead the already proved
`O(D)` product-window cap after a chart has been identified.

---

## 7. Exact status

```text
three-row determinant recovery identities:          PROVED;
D^2<q unique short-orthogonal line:                  PROVED;
triple codegree 1+D/H:                               PROVED;
K_(3,2) double count:                                PROVED;
global/local excess operator inequalities:           PROVED;
sixth trace directly controlled by triple codegree:  FALSE;
AFP F(x) directly controlled by triple codegree:     FALSE (K_(2,s));
dyadic low-height triple count D^2*R:                PROVED;
best direct dyadic operator exponent:                D^(5/3+o(1));
improvement below D^(21/16) from current inputs:      NO;
post-merger reciprocal-height bound RH-global/local: OPEN;
uniform slope-block / four-cycle theorem:            OPEN.
```

Finite replay:

```bash
PYTHONPATH=src pytest -q src/test_qp_k23_higher_trace_gate.py
```

