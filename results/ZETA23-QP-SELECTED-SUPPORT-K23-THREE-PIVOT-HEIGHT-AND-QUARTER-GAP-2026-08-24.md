# QP selected-support graph: K_(3,2), three-pivot height, and the exact quarter-power gap

**Date:** 2026-08-24  
**Verdict:** the scalar-QP three-pivot lemma is valid.  Three fixed pivots
with `t` common endpoints determine one primitive completion-relation normal
of height `H`, and

```text
t << 1+D/H.                                             (0.1)
```

Together with the exact `K_(3,2)` identity, this reduces the selected-support
codegree tail to an anchored reciprocal-height mass.  At the critical flat
bin

```text
M=D^(15/8),                 T=M/D=D^(7/8),              (0.2)
```

the trivial reciprocal-height mass gives a pair-count bound `D^(13/4)`,
where the elementary codegree first moment already gives `D^3`.  Thus the
new route is worse by exactly `D^(1/4)`.  A reciprocal-height theorem saving
`D^(1/4)` only matches the elementary estimate; a strict saving beyond
`D^(1/4)` is required for a genuinely sub-`D^(7/8)` codegree consequence.

The exact unproved statement is

```text
R_rel:=sum_u sum_(X subset N(u), t_3(X)>=2) 1/H_u(X)
       <<M*D^(11/4+o(1)).                               (RH_1/4)
```

The proved bound is only `R_rel<<M*D^3`.  The missing factor is therefore
`D^(1/4)`, not a hidden logarithm.  There are `asymp D^3` possible primitive
three-dimensional relation labels and their raw reciprocal-height union
budget is `asymp D^2`; the height lemma supplies no multiplicity packing
across those labels.  This is the exact algebraic label count preventing the
factorial argument from closing.

No new four-cycle exponent follows.

## 1. The selected-support graph

Let `Z=supp(z)`, `|Z|=M`, inside one factor-two coefficient bin.  Form the
simple graph `B_Z` on the actual shell by putting an edge `x--y` when the
unique accepted triple containing the pair is

```text
{x,y,c},                    c in Z.                    (1.1)
```

Linearity makes this well-defined.  If the accepted triple system has
maximum vertex degree `Delta<<D`, then

```text
e(B_Z)<=M*Delta,              max_v deg_B(v)<=2*Delta. (1.2)
```

The factor two in the degree bound is real: one triple incident to `v` can
give the two graph edges from `v` when both opposite completions lie in
`Z`.

For endpoints `u,v`, put

```text
mu_uv=|N(u) intersect N(v)|.                           (1.3)
```

Every selected two-step walk contributing to the Walsh fibre `(u,v)` is a
common neighbor in (1.3).  Hence

```text
effective Walsh multiplicity m_uv<=mu_uv.              (1.4)
```

In particular the only open Walsh range `m_uv>T=M/D` lies inside the same
raw-codegree range `mu_uv>T`.

The elementary first moment is

```text
sum_(u<v) mu_uv
 =sum_p binom(deg_B(p),2)
 <=e(B_Z)*(max deg_B-1)
 <<M*D^2.                                               (1.5)
```

Thus a dyadic codegree layer `K<=mu<2K` contains at most

```text
P_K<<M*D^2/K                                             (1.6)
```

pairs.

## 2. Exact K_(3,2) exchange

For a pivot triple `X={p_1,p_2,p_3}`, let

```text
t_3(X)=|N(p_1) intersect N(p_2) intersect N(p_3)|.      (2.1)
```

Counting a pair of endpoints and a triple of their common pivots in the two
orders gives

```text
sum_(u<v) binom(mu_uv,3)
 =sum_(|X|=3) binom(t_3(X),2).                          (2.2)
```

This is the correct factorial identity.  The ordinary sixth trace is not:
it includes triangular six-walks with no common pivot triple.

## 3. Scalar-QP three-pivot common-endpoint height lemma

Fix distinct pivots `p_1,p_2,p_3` and common endpoints

```text
x_0,x_1,...,x_(t-1).                                    (3.1)
```

Write `a_i(x)` for the completion of the selected edge `p_i--x`, and

```text
8*p_i*x*a_i(x)=q^3+r_i(x),       |r_i(x)|<=qD.          (3.2)
```

Put

```text
a(x)=(a_1(x),a_2(x),a_3(x)).                            (3.3)
```

For two common endpoints `x,y`, subtraction in (3.2) gives

```text
e_i=x*a_i(x)-y*a_i(y)
    =(r_i(x)-r_i(y))/(8*p_i),       |e_i|<<D.            (3.4)
```

Consequently

```text
a(x) cross a(y)=-(a(x) cross e)/y,                     (3.5)
```

so every coordinate of this integral normal is `O(D)`.  More explicitly,
if the shell is `[L,U]`, then

```text
||a(x) cross a(y)||_infinity
 <=W:=floor(U*q*D/(2*L^2)).                             (3.6)
```

On the actual prime-power shell the three entries of `a(x)` are distinct
and coprime, hence `a(x)` is primitive.  Fix `x=x_0`.  Two normals

```text
n_y=a(x_0) cross a(y),       n_z=a(x_0) cross a(z)     (3.7)
```

are both orthogonal to `a(x_0)`.  Their cross product is therefore an
integral multiple of that primitive positive vector.  But

```text
||n_y cross n_z||_infinity<=2W^2=o(q),                 (3.8)
```

while every nonzero integral multiple of `a(x_0)` has a coordinate at
least `L asymp q`.  Hence the cross product vanishes.  All normals in
(3.7) lie on one primitive line

```text
n_y=k_y*h_0,              H=||h_0||_infinity.           (3.9)
```

The multipliers `k_y` are nonzero and distinct.  Indeed, equality of two
normals says

```text
a(x_0) cross (a(y)-a(z))=0.                            (3.10)
```

Primitivity makes the difference an integral multiple of `a(x_0)`; the
shell diameter is smaller than its minimum, so that multiple is zero.
Coordinatewise pair uniqueness then gives `y=z`.  Finally

```text
|k_y|*H<=W,                                             (3.11)
```

and there are at most `2 floor(W/H)` nonzero integral multipliers.  This
proves the exact finite form

```text
t_3(X)<=1+2*floor(W/H(X)).                              (3.12)
```

The executable certificate checks (3.2), primitivity, coordinatewise pair
uniqueness, (3.6), the separation `2W^2<L`, collinearity, and all primitive
multipliers.

### Tangent hostile test

For the full-integer packet

```text
p_j=m+2L+j,       x_i=m+i,       a_j(x_i)=m-2L-i-j,    (3.13)
```

take three even-spaced pivots.  The common primitive normal is, for the
parameters `j=(0,2,4)`,

```text
h_0=(1,-2,1),                  H=2.                    (3.14)
```

Thus the lemma recognizes the affine tangent packet rather than excluding
it.  This is the expected behavior: that packet is already handled by the
merger.

## 4. The exact reciprocal-height reduction

For every pivot triple with at least two common endpoints, let `H(X)` be
the primitive height in (3.9).  It is independent of the chosen base
endpoint because all completion vectors lie in the same rational plane.
Define the anchored mass

```text
R_rel=sum_u sum_(X subset N(u), t_3(X)>=2) 1/H(X).
                                                               (4.1)
```

From (3.12),

```text
binom(t_3(X),2)<=W*t_3(X)/H(X).                       (4.2)
```

Summing (4.2) and using (2.2) gives the exact gate

```text
sum_(u<v) binom(mu_uv,3)<=W*R_rel.                    (4.3)
```

This is genuine progress over a purely abstract support graph: actual QP
has attached a primitive arithmetic height to every `K_(3,2)`.

The aggregation currently stops at the trivial estimate

```text
R_rel
 <=sum_u binom(deg_B(u),3)
 <=e(B_Z)*(delta-1)*(delta-2)/3
 <<M*D^3,                                               (4.4)
```

where `delta=max deg_B<<D`.  Since `W<<D`, equations (4.3)--(4.4) give

```text
sum_(u<v) binom(mu_uv,3)<<M*D^4.                       (4.5)
```

Therefore a dyadic layer `K<=mu<2K` has only

```text
P_K<<M*D^4/K^3.                                        (4.6)
```

At no `K<=D` is (4.6) stronger than (1.6): their ratio is

```text
(D/K)^2>=1.                                             (4.7)
```

Thus the valid three-pivot lemma alone gives no sub-`D^(7/8)` codegree
consequence.

## 5. Why the critical threshold still misses by exactly D^(1/4)

At (0.2), the elementary and factorial pair-count exponents are

```text
(1.6):  M*D^2/T   =D^3,
(4.6):  M*D^4/T^3 =D^(13/4).                          (5.1)
```

So the factorial route is worse by `D^(1/4)`.

For completeness, this is also exactly the gap in the flat-bin weighted
reduction.  On a factor-two bin with `||z||_2=1`, every selected wedge has
weight `O(1/M)`.  If the effective Walsh multiplicity lies in `[H,2H)`,
then

```text
R_uv=F_uv/m_uv<<mu_uv^2/(M^2*H).                       (5.2)
```

After a second dyadic split `K<=mu_uv<2K`, it is sufficient to prove

```text
sum_(mu~K) mu_uv^2<<D*M^2.                             (5.3)
```

The factorial estimate (4.6) supplies instead

```text
sum_(mu~K) mu_uv^2<<M*D^4/K.                           (5.4)
```

At `K=T=D^(7/8)`, the exponents in (5.3)--(5.4) are respectively

```text
1+2*(15/8)=19/4,              15/8+4-7/8=5.           (5.5)
```

again an exact gap of `1/4`.

More generally, suppose a new arithmetic theorem improved (4.4) to

```text
R_rel<<M*D^(3-alpha).                                  (5.6)
```

Then

```text
P_K<<M*D^(4-alpha)/K^3,                                (5.7)
sum_(mu~K)mu_uv^2<<M*D^(4-alpha)/K.                    (5.8)
```

For `M=D^m`, `K=D^tau`, (5.8) reaches (5.3) exactly when

```text
alpha>=3-m-tau.                                        (5.9)
```

At `(m,tau)=(15/8,7/8)`, this is `alpha>=1/4`.  Equality
only matches the existing threshold; `alpha>1/4` is required to push the
codegree consequence below `D^(7/8)`.

## 6. The precise algebraic-label obstruction

The relation normal is a primitive unoriented vector

```text
h in Z^3,                 1<=||h||_infinity<<D.         (6.1)
```

Before imposing primitivity and quotienting by sign, the exact number of
nonzero raw labels in the radius-`R` cube is

```text
(2R+1)^3-1.                                               (6.2)
```

The shell of height exactly `r` contains

```text
(2r+1)^3-(2r-1)^3=24r^2+2                            (6.3)
```

vectors.  Hence its exact raw reciprocal-height budget is

```text
sum_(0<||h||infinity<=R)1/||h||infinity
 =sum_(r<=R)(24r^2+2)/r
 =12R(R+1)+2H_R
 asymp R^2.                                             (6.4)
```

For a fixed anchor `u` and label `h`, the triples being counted solve the
scalar equation

```text
h_1*a_1+h_2*a_2+h_3*a_3=0,          a_i in Z.          (6.5)
```

Fixing two completion values determines the third, so the structure-free
fixed-label count is at best quadratic in `deg_B(u)`.  Summing that bound
with (6.4) is worse than (4.4).  Conversely, summing only over triples and
discarding the labels gives exactly (4.4).  What is missing is a theorem
coupling the multiplicities

```text
E_u(h)=#{pivot triples X subset N(u): h(X)=h}           (6.6)
```

across `u` and `h` strongly enough to save `D^(1/4)`:

```text
sum_(u,h) E_u(h)/||h||infinity
 <<M*D^(11/4+o(1)).                                    (6.7)
```

Neither the product-window subtraction nor the `K_(3,2)` identity proves
(6.7).  The full-integer tangent fixture has highly recurrent labels and is
mergeable.  Abstract Steiner/Latin designs show that a codegree identity
alone can spread the triples across unrelated labels, although no claim is
made that those designs realize the actual prime/product mask.  Thus (6.7),
or an equivalent recurrent-label/packet packing theorem, is the minimal
remaining statement in this route.

## 7. Binary status

```text
selected-support graph edge/degree ledger:              PROVED;
high Walsh multiplicity implies high graph codegree:    PROVED;
K_(3,2) factorial identity (2.2):                       PROVED;
scalar-QP three-pivot common-endpoint height lemma:      PROVED;
three-pivot normal is one primitive relation label:      PROVED;
factorial-to-reciprocal reduction (4.3):                 PROVED;
trivial reciprocal mass R_rel<<M*D^3:                   PROVED;
critical factorial pair bound D^(13/4):                 PROVED;
critical elementary pair bound D^3:                     PROVED;
exact stopping gap D^(1/4):                             PROVED;
raw relation-label count and reciprocal budget:          EXACT;
reciprocal packing saving alpha>=1/4:                   OPEN;
sub-D^(7/8) codegree consequence from this route:        NONE;
new global four-cycle exponent:                          NONE;
sharp four-cycle theorem:                               NOT PROVED.
```

Executable replay:

```text
src/qp_support_graph_k23_gate.py
src/test_qp_support_graph_k23_gate.py
```
