# QP four-cycle: discrete Hankel packets and the subunit shift gate

**Date:** 2026-08-22  
**Verdict:** the `W=sqrt(D)` packet scale gives an exact merger rule, but
not a global four-cycle proof.  After gcd reduction, every nonzero shifted
color column has a common-product interval of length

```text
D/R <= D^2/q = q^(-1/33)<1.                         (0.1)
```

Thus a fixed shifted column contains at most one product integer and only
`q^o(1)` carrier factorizations.  This is a genuine arithmetic gain.
However, the two shifted columns in the squared correlation vary
independently, and a ratio block still contains a `D`-by-`D` candidate
array.  Curvature has not supplied the missing aggregation across that
array.

A literal tangent Hankel packet shows why ordinary Cotlar orthogonality is
the wrong aggregation.  Its individual color layers have cross-product
operator norm one at every overlapping displacement.  Merging the whole
packet first closes sharply by Hilbert--Schmidt:

```text
||A_packet||_S4^4 <= D ||z||_2^4.                  (0.2)
```

Consequently a successful packet proof needs a uniform theorem which
covers the selected reciprocal-rounding array by `q^o(1)` **merged**
affine/polynomial charts and controls the noncoherent remainder.  This is
the previously isolated slope-block / polynomial-arc covering gate, not a
consequence of block orthogonality alone.  No full FC bound is claimed.

---

## 1. The exact shifted reciprocal packet

Use the hard product-window notation

```text
X=q^3/8,                 H asymp qD,
|a*b*c-X|<=H.                                      (1.1)
```

For two rows write

```text
a=s*g,       a'=r*g,       gcd(r,s)=1,       r,s asymp R. (1.2)
```

If one carrier `b` gives colors `c,d`, subtraction of the two product
relations introduces the integral cross-shift

```text
e=r*d-s*c,                 |e| << D*R/q.            (1.3)
```

Choose Bezout coefficients with

```text
r*beta-s*alpha=1.
```

Then every color pair with shift `e` has the unique parametrization

```text
c=alpha*e+r*h,             d=beta*e+s*h.            (1.4)
```

The map `(e,h)->(c,d)` is unimodular: its determinant is `-1`.  Moreover,

```text
T=s*c=s*alpha*e+r*s*h,
r*d=T+e.                                             (1.5)
```

Thus the two product tests for `n=g*b` are exactly

```text
|n*T-X|<=H,                  |n*(T+e)-X|<=H.         (1.6)
```

Color-shell membership gives `h` an interval of length `O(q/R)`.  Equations
(1.3)--(1.4) therefore place all candidate color pairs for one reduced row
direction in a unimodular rectangle of area

```text
(D*R/q)*(q/R) << D.                                 (1.7)
```

This is the natural discrete packet; no Fourier approximation has been
used.

### Subunit-column lemma

Fix `(r,s,e,h)`.  Since `T asymp qR`, (1.6) puts the integer `n=g*b` in an
interval of length

```text
O(H/T)=O(D/R).                                      (1.8)
```

If `e!=0`, (1.3) forces `R >> q/D`.  At the project scale

```text
D=q^(16/33),       D/R << D^2/q=q^(-1/33).          (1.9)
```

For all sufficiently large `q`, the interval contains at most one integer.
That integer has only `tau(n)=q^o(1)` decompositions `n=g*b`.  Hence a fixed
nonzero shifted color column has `q^o(1)` row/carrier realizations.

This lemma is stronger than a continuous Mellin pulse estimate: it acts
after integer sampling and so has no aliasing error.

---

## 2. Why the lemma does not yet sum the packet

For a fixed reduced direction define schematically

```text
G_g(r,s)=sum_(e,h) z_(alpha*e+r*h)
                      conjugate(z_(beta*e+s*h)) W_g(e,h),   (2.1)
```

where `W_g(e,h)` is the selected reciprocal carrier mask.  The direct
fourth trace contains

```text
sum_(r,s) sum_g |G_g(r,s)|^2.                       (2.2)
```

After expanding the square, `(e,h)` and `(e',h')` are independent.  The
subunit-column lemma controls each fixed column but supplies no
orthogonality between two columns at the zero Fourier mode.  One ratio
block can have `O(D)` row directions and `O(D)` reciprocal-color
directions.  Columnwise divisor bounds alone therefore leave the same
`D^2` candidate array as the exact slope-block reduction.

The low-denominator `e=0` proportional sector has separate divisor
structure.  Removing it does not address (2.2), whose first live range is
precisely `R>q/D` and `e,e'!=0`.

---

## 3. A sharp affine Hankel packet

The following full-integer fixture explains the correct merger.  Let
`L>=2`, `m` be much larger than `L`, put `q=2m`, and take

```text
a_i=m+i,                    0<=i<L,
b_j=m+2L+j,                 0<=j<L,
c_ij=m-2L-i-j.                                      (3.1)
```

All three label ranges are disjoint.  With `x=i` and `y=2L+j`, direct
expansion gives

```text
(m+x)(m+y)(m-x-y)-m^3
 =-m*(x^2+x*y+y^2)-x*y*(x+y).                       (3.2)
```

Consequently every one of the `L^2` triples lies in
`|8abc-q^3|<qD_0` for, say,

```text
D_0=100L^2.                                         (3.3)
```

The packet matrix is the finite Hankel matrix

```text
A_ij=z_(i+j).                                       (3.4)
```

Let `P_k(i,j)=1_(i+j=k)` be its color layers.  Whenever two central
anti-diagonals overlap,

```text
||P_k P_l^*||_(2->2)=1.                             (3.5)
```

There is no decay as `|k-l|` varies through the packet.  A Cotlar sum over
the individual colors therefore pays the full factor `L=sqrt(D_0)`.

But the merged packet closes immediately.  Each color occurs at most `L`
times, so for arbitrary complex `z`,

```text
||A||_HS^2=sum_k #(i+j=k)|z_k|^2 <=L||z||_2^2,
||A||_S4^4<=||A||_HS^4<=L^2||z||_2^4.              (3.6)
```

For flat weights on the `2L-1` colors, `A` is the all-ones matrix divided
by `sqrt(2L-1)` and

```text
||A||_S4^4=L^4/(2L-1)^2 asymp L^2.                 (3.7)
```

Thus (3.6) has the correct order.  The packet is neither a counterexample
to the desired bound nor an actual odd-prime shell: it is an exact
counterexample to **unmerged color-layer almost orthogonality**.

---

## 4. Relation to the multilevel tangent fixture

The earlier multilevel full-integer construction has `asymp L^2` fixed
color clusters and `asymp L` completions per cluster.  With its spiked
weights, the pair-of-completions energy

```text
sum_C m(C)*(m(C)-1) w(C)
```

is `asymp L^(5/2)=D^(5/4)`.  The **direct** fourth-trace contribution uses
only

```text
sum_C m(C) w(C) asymp L^(3/2)=D^(3/4).              (4.1)
```

It therefore does not disprove the full-integer direct Hankel conjecture.
Conflating these two energies creates a false counterexample.  The merged
chart calculation (3.6) is the relevant direct model.

### Exact stationary charts cannot repeat across bases

There is also a proof-grade cross-base merger for exact affine packets.
Fix the same color data `(C,S,T)` and consider packets

```text
a_i=A+P*i,       b_j=B+Q*j,       c_ij=C-S*i-T*j,  (4.2)
```

whose first derivatives vanish at the base:

```text
P*C=A*S,                    Q*C=B*T.                (4.3)
```

Write the two color ratios in lowest terms as

```text
C/S=C_0/S_0,               C/T=C_1/T_0.            (4.4)
```

Equation (4.3) gives integers `t,u` with

```text
(A,P)=(t*C_0,t*S_0),       (B,Q)=(u*C_1,u*T_0).    (4.5)
```

The base product is therefore

```text
A*B*C=t*u*C_0*C_1*C.                                (4.6)
```

If it lies in the legal interval of length `O(qD)`, then the integer `t*u`
lies in an interval of length

```text
O(qD/(C*C_0*C_1))
 <<D*S*T/q^2.                                       (4.7)
```

Here `C_0>>q/S` and `C_1>>q/T`.  A nontrivial tangent packet has
`S,T<<sqrt(D)` by quadratic curvature, so (4.7) is at most

```text
D^2/q^2=q^(-34/33)<1.                               (4.8)
```

Thus `t*u` is unique and has only `q^o(1)` divisor factorizations.  Exact
stationary packets with the same color tangent data cannot form a
polynomially repeated blocked-Latin family across different bases.  The
open case consists of approximate defects and scattered packets, not
repetition of the exact affine model.

---

## 5. Exact remaining packet theorem

A `W=sqrt(D)` decomposition can now be stated without ambiguity:

1. use `(e,h)` as the exact color coordinates in each reduced row
   direction;
2. exploit (0.1) for individual nonzero-shift columns;
3. merge all columns belonging to one primitive affine tangent chart before
   applying any square-function estimate;
4. prove that every dense modular-lift cell is covered by `q^o(1)` such
   merged affine charts or by the already controlled curved polynomial
   arcs;
5. prove `O(1)` average occupancy for the remaining `sqrt(D)`-by-`sqrt(D)`
   cells.

Steps 1--3 are rigorous.  Steps 4--5 are exactly the missing
polynomial-arc covering / slope-block theorem.  Quadratic curvature bounds
the size of one merged chart, but it does not presently prove the global
cover or suppress the zero-mode coherence between scattered charts.

```text
unimodular (shift,height) packet:                  PROVED;
nonzero-shift subunit product column:              PROVED;
candidate area per reduced direction O(D):         PROVED;
ordinary color-layer Cotlar decay:                 FALSE (sharp packet);
merged affine Hankel packet S4 bound O(D):          PROVED;
full-integer direct conjecture:                    OPEN;
actual prime-power slope-block bound / FC:         OPEN.
```

The identities and finite fixture are replayed by
`src/qp_discrete_hankel_packet_audit.py` and
`src/test_qp_discrete_hankel_packet_audit.py`.

---

## 6. A Sidon-regular obstruction to a purely local inverse theorem

There is an exact abstract model showing that the implication

```text
large tensor zero mode => one rich mergeable affine chart              (6.1)
```

is false if it uses only matching layers, fixed-column uniqueness, and
small pairwise codegrees.  The model deliberately omits the QP
`O(D)`-vertex slope-block localization; that qualification is essential.

Let `p` be an odd prime, let both vertex sets be

```text
G=F_p^2,
```

and put

```text
H={(t,t^2):t in F_p},
B_(x,y)=1_(y-x in H).                                (6.2)
```

For each fixed `t`, the edges `y=x+(t,t^2)` form one perfect matching.
Moreover `H` is Sidon.  Indeed, if

```text
(t,t^2)-(s,s^2)=(u,v),       u!=0,
```

then

```text
t-s=u,                t+s=v/u,                      (6.3)
```

which determines `(t,s)` uniquely because `2` is invertible.  Consequently
two distinct rows have at most one common neighbor.  In particular there is
no three-neighbor family from which a local affine chart could be extracted.

Nevertheless take the genuine tensor coefficient

```text
z_c=p^(-1/2),             u_(c,d)=z_c*z_d=1/p.      (6.4)
```

It has `||u||_2=1` on `G`.  Since `B` is `p`-regular,

```text
(Bu)(x)=1,
||Bu||_2^2=p^2.                                      (6.5)
```

If the number of residual layers is identified with `D=p`, the desired
scale is only `D`; (6.5) loses the exact factor `D`.

Thus all of the following can hold simultaneously:

```text
every residual layer is a matching;
every fixed shifted column has one lift;
every distinct pair of bases has codegree at most one;
there is no rich local affine packet;
the tensor zero mode is D times too large.           (6.6)
```

This is not a QP product-window construction.  In fact it has `D^2`
vertices per side.  If its vertices are partitioned into `D` blocks of size
`D`, the parabolic shifts cross `D` different block offsets, whereas the QP
ratio decomposition is banded across only `O(1)` neighboring offsets.  On
one group of order `D`, a Sidon generating set has size at most
`O(sqrt(D))` and merely saturates the desired norm scale; a larger generator
must repeat differences.

Thus (6.2) is a sharp warning, not a counterexample to the localized
slope-block inverse lemma.  It proves that slope banding and its `O(D)`
vertex cap must be retained in any valid inverse argument.  Matching
layers, fixed-lift uniqueness, and optimal codegrees alone cannot exclude a
globally regular scattered-shift zero mode.

---

## 7. The strongest localized graph lemma and its sharp obstruction

Now retain the genuine slope-block input.  Let `B` be one neighboring block,
with at most `C*D` vertices on either side, and put

```text
m(x,x')=#(N(x) intersect N(x')),
F(x)=sum_(x'!=x) m(x,x')*(m(x,x')-1).               (7.1)
```

For every nonnegative integer `m`,

```text
m<=1+sqrt(m*(m-1)).                                 (7.2)
```

Hence Cauchy--Schwarz gives

```text
sum_(x'!=x)m(x,x')
 <<D+sqrt(D*F(x)).                                  (7.3)
```

The left side is the off-diagonal row sum of `B*B^*`.  Schur therefore
proves the exact localized inequality

```text
||B||_(2->2)^2 <<D+sqrt(D*max_x F(x)).              (7.4)
```

Consequently the anchored factorial parallel-chain estimate

```text
max_x F(x)<<D*q^o(1)                                (AFP)
```

would prove the desired `||B||<<sqrt(D)q^o(1)` and hence close the
slope-block gate.  The already proved pointwise codegree estimate
`m(x,x')<<sqrt(D)q^o(1)` gives only

```text
F(x)<<D^2*q^o(1),       ||B||<<D^(3/4)q^o(1).       (7.5)
```

This is the strongest possible consequence of the vertex and pointwise
codegree bounds alone.  It is sharp by a classical finite incidence design.
Take points versus hyperplanes in `PG(4,Q)`.  Then

```text
v=Q^4+Q^3+Q^2+Q+1 asymp D,
k=Q^3+Q^2+Q+1 asymp D^(3/4),
lambda=Q^2+Q+1 asymp sqrt(D),                       (7.6)
```

where both sides have `v` vertices, every degree is `k`, and every two
distinct point rows have codegree `lambda`.  The constant vector is a top
singular vector with singular value `k`.  Since the graph is regular and
bipartite, its edges decompose into `k` perfect matching layers.

The tensor restriction does not remove the obstruction abstractly.  Put the
`v` right vertices inside a Cartesian set `C x C` with
`|C|=ceil(sqrt(v))`, set `z_c=|C|^(-1/2)`, and pad unused pairs by zero
columns.  The restriction of `z tensor z` is constant, has norm bounded
away from zero, and sees energy comparable with

```text
k^2 asymp D^(3/2).                                  (7.7)
```

This finite-geometric graph is not a QP realization.  Its role is to locate
the exact arithmetic debt.  Fixed-base direction uniqueness can merge the
coherent part of `F(x)`, but it does not control `F(x)` when its
`asymp D^2` parallel chains use many distinct directions across varying
bases.  The remaining localized inverse theorem is therefore `(AFP)` for
the **generic/scattered** chains after all certified affine charts have
been merged.  A maximum-codegree theorem, Freiman extraction from one rich
fiber, or matching-layer orthogonality is strictly weaker.
