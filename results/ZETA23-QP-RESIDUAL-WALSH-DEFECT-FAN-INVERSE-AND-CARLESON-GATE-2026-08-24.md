# QP residual blocks: exact Walsh inverse, defect fans, and the Carleson gate

**Date:** 2026-08-24  
**Verdict:** the deterministic-versus-random residual-block gap has an exact
physical inverse formulation.  A polynomial gap forces polynomially many
distinct integer defects in common-neighbor fibres carrying a fixed fraction
of the fourth trace.  On a comparable support of size `M`, the randomized
budget improves to `D*min(1,D/M)`, making the Carleson estimate automatic up
to multiplicity `M/D`.  Beyond that threshold, every large actual-shell fan
forces a highly occupied affine rank-two color plane.  It does **not** yet
force one affine/Hankel tangent packet or recurrent color matrix in that same
plane.  The missing global assertion is a sharp weighted Carleson packing
bound across these planes.

No new global exponent and no sharp four-cycle theorem are proved here.

## 1. Absolute values are legal

Let the accepted all-distinct triples be partitioned into residual intervals
of width `q`, and write

```text
A_I(x,y)=z_a                 if {x,y,a} lies in block I.       (1.1)
```

The triple system is linear, so each matrix cell has at most one completion.
Put `A=sum_I A_I` and `u=|z|`.  Entry by entry in the Gram matrix,

```text
|(A_z^* A_z)(x,y)|
 <=sum_v |A_z(v,x) A_z(v,y)|
 =(A_u^* A_u)(x,y).                                      (1.2)
```

Consequently

```text
||A_z||S4^4<=||A_u||S4^4.                               (1.3)
```

Thus an upper bound and any inverse analysis of a violation may be carried
out with nonnegative coefficients.  This is important: all cross terms below
are then positive, rather than merely bounded after a phase loss.

## 2. Exact Walsh expansion of the Rademacher average

Fix endpoints `(x,y)`.  A two-step walk through `v` uses the two matrix
entries `(v,x)` and `(v,y)`.  Let their residual-block labels be `I` and `J`,
and their completion coefficient product be

```text
c_v(x,y)=conj(z_(a(v,x))) z_(a(v,y)).                    (2.1)
```

The product of the two block signs is the Walsh character indexed by

```text
sigma(v;x,y)=emptyset                 if I=J,
             {I,J}                    if I!=J.           (2.2)
```

Define

```text
C_(x,y;sigma)=sum_(v: sigma(v;x,y)=sigma)c_v(x,y).       (2.3)
```

Orthogonality of distinct Rademacher characters gives the two exact finite
identities

```text
F(z):=||sum_I A_I(z)||S4^4
     =sum_(x,y)|sum_sigma C_(x,y;sigma)|^2,              (2.4)

R(z):=E_epsilon||sum_I epsilon_I A_I(z)||S4^4
     =sum_(x,y)sum_sigma|C_(x,y;sigma)|^2.               (2.5)
```

This also classifies the block-label patterns in the fourth-trace expansion.
For a nondegenerate rectangle, adjacent block labels cannot agree unless the
two adjacent entries come from the same triangle.  The Rademacher average
retains exactly those pairs of two-step walks whose unordered block-label
pairs agree; every other rectangle is deterministic excess.

For `u=|z|`, all `C` are nonnegative.  Put

```text
F_xy=(sum_sigma C_(x,y;sigma))^2,
R_xy=sum_sigma C_(x,y;sigma)^2,
m_xy=F_xy/R_xy.                                         (2.6)
```

The number `m_xy` is the effective number of active block-pair characters in
that physical common-neighbor fibre.  Cauchy gives

```text
1<=m_xy<=#{sigma:C_(x,y;sigma)>0}.                      (2.7)
```

### Exact first-stage inverse theorem

If `F=sum F_xy`, `R=sum R_xy`, and `K=F/R`, then fibres satisfying

```text
m_xy>=K/2                                                (2.8)
```

carry at least `F/2` of the all-plus fourth trace.  Indeed, the complementary
fibres contribute at most

```text
(K/2) sum R_xy<=F/2.                                    (2.9)
```

Hence a polynomial all-plus/randomized gap cannot be hidden in many
one-character fibres: a fixed fraction of it lies on fibres with a
polynomial number of genuinely different residual-block pairs.

## 3. The physical integer defect is injective

Take a nontrivial two-step walk with triples

```text
{v,x,a},             {v,y,b},                           (3.1)
```

and exact residuals

```text
r=8*v*x*a-q^3,       s=8*v*y*b-q^3.                    (3.2)
```

Then

```text
h=x*a-y*b=(r-s)/(8*v),             |h|<<D.              (3.3)
```

The last estimate uses `|r|,|s|<=qD` and `v asymp q`.

On the actual prime-power shell, distinct nodes are coprime and the shell
diameter is smaller than its minimum.  Fix distinct endpoints `x,y`.  If two
completion pairs have the same defect,

```text
x*a-y*b=x*c-y*d,                                        (3.4)
```

then coprimality gives

```text
(a-c,b-d)=t*(y,x).                                      (3.5)
```

The shell diameter makes `t!=0` impossible.  Thus `(a,b)=(c,d)`.  The
carrier is unique as well: two legal carriers would satisfy

```text
8*x*a*|v-v'|<=2qD,
```

and `qD<4(min S)^2` makes the right-hand interval shorter than one.

If `h=0`, multiplicative Sidonicity gives `{x,a}={y,b}`.  For `x!=y` this is
the single-triangle walk `a=y,b=x`, whose Walsh signature is empty.  Hence
every nonempty signature in a fixed endpoint fibre supplies a distinct
nonzero integer

```text
0<|h|<<D.                                               (3.6)
```

Combining Sections 2 and 3 proves the promised physical inverse statement:

> If the all-plus fourth trace exceeds its residual-block Rademacher average
> by a factor `K`, then fibres with at least `K/2-O(1)` distinct nonzero
> defects carry at least half of the fourth trace.

At the project scale, the already proved randomized theorem gives

```text
R(u)<<D q^o(1)||u||2^4.                                 (3.7)
```

There is now a stronger support-sensitive version.  If `u` lies in one
factor-two coefficient-height bin with support `M`, then

```text
R(u)<<D min(1,D/M)q^o(1)||u||2^4.                       (3.8)
```

The proof is elementary.  With `B=||u||infinity^2`, linearity gives

```text
S_p:=sum_(e contains p)d_e(p)
 <=min(||u||2^2,2D*B),
sum_p S_p<=2D||u||2^2.                                  (3.9)
```

Thus the cross-edge diagonal in either square function is bounded by
`max S_p sum S_p`.  The self terms are smaller.  Since a factor-two bin has
`B<=4||u||2^2/M`, (3.8) follows.  The executable theorem uses the safe
constant `48` before the suppressed comparability factors.

Consequently a hypothetical binwise violation

```text
F(z)>=D^(1+eta)||z||2^4                                (3.10)
```

forces effective multiplicity

```text
K=F/R >=D^eta max(1,M/D)q^(-o(1))                      (3.11)
```

on fibres carrying at least half its mass.  This is much stronger than the
support-blind `D^eta` conclusion.

## 4. The exact Carleson theorem that would close FC

For dyadic `H`, let

```text
R_H=sum_(H<=m_xy<2H) R_xy.                              (4.1)
```

The sharp remaining packing statement is

```text
R_H<<D q^o(1) H^(-1)||z||2^4       for every H>=1.      (CF)
```

This is equivalent to the sharp positive-weight four-cycle estimate up to a
logarithm.  Indeed, `(CF)` gives

```text
F=sum_H sum_(m_xy~H) m_xy R_xy
 <<sum_H 2H*(D/H)q^o(1)
 <<D q^o(1).                                            (4.2)
```

Conversely, `F<<Dq^o(1)` implies `H R_H<=F`, hence `(CF)`.

This is the precise Carleson extraction/packing target.  It says that fibres
with `H` coherent residual-block characters may use only a `1/H` portion of
the sharp randomized square-function budget.  The randomized theorem alone
gave only `R_H<<D`; the coefficient-sensitive theorem sharply narrows the
open range.

### 4.1 The support-dependent tail reduction

Put

```text
delta_M=min(1,D/M),             H_0=delta_M^(-1)
                                      =max(1,M/D).       (4.3)
```

Equation (3.8) gives `R_H<<D delta_M`.  Therefore `(CF)` is already automatic
whenever

```text
H<=H_0.                                                 (4.4)
```

The sole binwise theorem still needed is

```text
R_H<<D H^(-1)q^o(1)||z||2^4,
                    H>max(1,M/D).              (CF_M)   (4.5)
```

There are only `O(D)` possible defects in one fibre.  Hence the open tail is
empty when `M>=D^2` (up to fixed bin constants).  At the critical support

```text
M=D^(15/8),
R<<D^(1/8),
H_0=D^(7/8).                                           (4.6)
```

Thus the old description “control `D^(1/8)`-sized fans” was too weak.  A
putative `D^(9/8)` critical-bin saturator would have

```text
F/R asymp D,                                           (4.7)
```

the maximum possible defect multiplicity.  In fact the elementary bound
`m_xy<<D`, combined with (3.8), gives

```text
F<<D^3/M.                                              (4.8)
```

At `M=D^(15/8)`, (4.8) is exactly `D^(9/8)`.  This identifies the current
global exponent as “diffuse randomized budget times maximal defect fan,”
and `(CF_M)` is precisely the missing improvement.

### 4.2 Dyadic coefficient bins

For a finite disjoint height decomposition `z=sum_(j<=J)z_j`, Schatten
triangle inequality and scalar Holder give the exact recombination

```text
F(z)^(1/4)<=sum_j F(z_j)^(1/4),
F(z)<=J^3 sum_j F(z_j).                                (4.9)
```

The truncation is elementary here.  If `n` is the shell cardinality and
`||z||2=1`, delete coefficients below `q^(-B)/sqrt(n)`.  Their `l2` norm is
at most `q^(-B)`, while the linear triple system gives

```text
||A_w||HS^2<=2D||w||2^2.                               (4.10)
```

Taking fixed large `B` makes their Schatten-four contribution negligible
even after the crude `O(D^2)` fourth-power bound.  The retained coefficient
range has only `J=O_B(log q)=q^o(1)` factor-two bins.  Hence it is enough to
prove `(CF_M)` separately on every bin; mixed-height rectangles cost only
the displayed subpower recombination factor.  No cross-bin orthogonality is
being assumed.

## 5. Hostile test: the affine tangent packet saturates `(CF)`

Let `L>=2`, choose `m` much larger than `L`, put `q=2m`, and use the exact
full-integer triples

```text
a_i=m+i,
b_j=m+2L+j,
c_ij=m-2L-i-j,                  0<=i,j<L.              (5.1)
```

Every one of the `L^2` triples lies in the product window for

```text
D_0=100L^2,                                              (5.2)
```

One may take `m asymp D_0^(33/16)`, so this fixture has the project scaling
`D_0 asymp q^(16/33)` and its gap in `(5.4)` is a genuine fixed power rather
than something absorbable by `q^o(1)`.

Partitioning its exact residuals into width-`q` intervals gives vertex
matchings.  Put flat normalized coefficients on the `2L-1` color values
`c_ij` and zero on every `a_i,b_j`.  The all-plus matrix is the symmetric
bipartization of the constant `L` by `L` Hankel matrix, so exactly

```text
F=2L^4/(2L-1)^2 asymp L^2 asymp D_0.                    (5.3)
```

The hyperedge degree is `Delta=L`; the randomized theorem gives `R<=42L`.
Conversely fixed entry magnitudes and the rank bound give `R>>L`.  Hence

```text
F/R asymp L=sqrt(D_0).                                  (5.4)
```

Raw unsigned unconditionality is therefore false by a polynomial factor in
this exact cubic full-integer model.  This is not a counterexample to FC:
the merged packet already has the sharp size `(5.3)`.  In Carleson language,
it sits at `H~L` with

```text
R_H~L~D_0/H,                                            (5.5)
```

so it saturates `(CF)` rather than violating it.

The fixture is not an actual odd-prime/prime-power shell.  Its consecutive
directions are strongly restricted in the actual shell, as recorded in the
earlier tangent audit.  Its role is methodological and exact: one must merge
coherent packets or prove `(CF)`; one cannot prove blanket
`F<<q^o(1)R` before that merger.

## 6. What the remaining high tail now forces

A fibre with many defects gives many solutions of

```text
x*a-y*b=h,                    0<|h|<<D.                (6.1)
```

For two solutions `(a,b,h)` and `(c,d,h')`, their completion determinant has
the exact secant formula

```text
x*(a*d-b*c)=h*d-h'*b.                                  (6.2)
```

The support-blind theorem left open fans below `sqrt(D)`, where all secants
could be distinct.  The flat-bin refinement removes that particular
obstruction at the critical support: its only open range is
`H>D^(7/8)>>sqrt(D)`.  In this range there is an exact stronger conclusion.

Write `P_h=(a_h,b_h)`.  The actual project shell satisfies the strengthened
width inequality

```text
2*diam(S)<min(S).                                        (6.3)
```

If four defects obey `h_i-h_j=h_k-h_l`, then

```text
x*((a_i-a_j)-(a_k-a_l))
 =y*((b_i-b_j)-(b_k-b_l)).                             (6.4)
```

Because `(x,y)=1`, the first parenthesis is a multiple of `y`; by (6.3) its
modulus is strictly below `y`.  It vanishes, and so does the second
parenthesis.  The converse is immediate.  Thus

```text
h_i-h_j=h_k-h_l
 iff P_(h_i)-P_(h_j)=P_(h_k)-P_(h_l).                  (6.5)
```

The defect-to-completion map is an exact Freiman two-isomorphism on every
fixed endpoint fan.

Now take `N>=H` active signatures and choose one wedge from each.  Their
distinct defects occupy an interval of length `O(D)`.  The first completion
coordinates are separately distinct, as are the second ones, by pair
uniqueness; the middle vertices are distinct as well.  Cross-coordinate
coincidences delete only `O(N)` ordered chords.  More explicitly, the two
color-crossings and four middle/color crossings cost at most `6N`, so at
least `N(N-7)` chords retain all eight displayed nodes.  Pigeonholing these
differences gives a nonzero `t` represented at least

```text
Omega(N^2/D)>=Omega(H^2/D)                              (6.6)
```

times.  By (6.5), all those pairs have one common vector translation

```text
P_h-P_(h-t)=(alpha,beta).                               (6.7)
```

Their all-four-distinct row-major color matrices lie in the fixed affine
two-plane

```text
Pi_(alpha,beta):
c11-c21=alpha,                 c12-c22=beta.            (6.8)
```

At the critical open threshold `H>D^(7/8)`, this plane contains at least
`D^(3/4-o(1))` extracted color matrices.  At a putative `D^(9/8)` saturator,
`H~D` and the plane occupancy is `Omega(D)`.

One fixed plane is harmless for arbitrary weights:

```text
sum_(C in Pi_(alpha,beta)) w_z(C)
 <=(sum_c |z_(c+alpha)z_c|)
   (sum_d |z_(d+beta)z_d|)
 <=||z||2^4.                                            (6.9)
```

So the surviving theorem is no longer a local tangent-recognition lemma.
It is a **square-function/Carleson packing theorem across the many affine
rank-two planes and endpoint fibres** produced by (6.8).

### 6.1 Recurrence is global, not fibrewise

The extraction above does not force `m(C)>=3`.  Inside one endpoint fibre,
different ordered wedge pairs give different color matrices.  A fixed
translation may consist entirely of disjoint two-point chords, with no
three points on one translation chain.  This is not a minor quantitative
loophole: classical Behrend sets give three-term-progression-free subsets of
an interval of size `D^(1-o(1))`, larger than the critical `D^(7/8)` scale.
Thus defect density and (6.5) alone cannot manufacture a rich affine line.

The already proved determinant-layer theorem does say globally that

```text
sum_(C:m(C)<=2) m(C)w_z(C)<<Dq^o(1)||z||2^4.            (6.10)
```

Consequently any genuine polynomial violation of FC has a positive fraction
of its mass on recurrent color matrices `m(C)>=3`.  What is not proved is
that this recurrent mass lies in the popular planes extracted from the same
high-Walsh fibres.  Establishing that bridge, or directly proving `(CF_M)`,
is the minimal remaining packing statement.

This is exactly where the proposed GPT-7 inverse theorem stops.  To finish,
one needs a **global weighted aggregation theorem** saying that the
rank-two planes in (6.8) jointly obey the `1/H` packing in `(CF_M)`, while
the recurrent exceptional planes are charged to the already merged tangent
and fixed-relation charts.  The individual `O(1)` plane bound (6.9) is not
summable by itself because both the plane translation and the endpoint pair
vary.

### 6.2 The selected-support `K_(3,2)` route stops at the same packing bill

There is a second exact inverse formulation.  On one flat bin, put an edge
`u--v` when the completion of `{u,v}` belongs to `supp(z)`, and let
`mu_uv` be graph codegree.  Then `m_uv<=mu_uv`, the graph has

```text
e<<M*D,                     maximum degree <<D,        (6.11)
```

and

```text
sum_(u<v) binom(mu_uv,3)
 =sum_(pivot triples X) binom(t_3(X),2).               (6.12)
```

For three fixed pivots, product-residual subtraction makes the cross
products of their completion vectors `O(D)`.  Since `D^2=o(q)`, all such
short normals are collinear.  If the common primitive normal has height
`J(X)`, then the number of common endpoints satisfies the proved scalar-QP
height lemma

```text
t_3(X)<=1+O(D/J(X)).                                   (6.13)
```

Thus (6.12) is bounded by `D*R_rel`, where

```text
R_rel=sum_u sum_(X subset N(u), t_3(X)>=2)1/J(X).       (6.14)
```

The current bound `R_rel<<M*D^3` gives only

```text
#{(u,v):mu_uv~T}<<M*D^4/T^3.                           (6.15)
```

At `M=D^(15/8), T=D^(7/8)`, this is `D^(13/4)`, whereas
the elementary codegree first moment already gives `D^3`.  The factorial
route is therefore worse by exactly `D^(1/4)`.  It reaches the flat-bin
Carleson second-moment target precisely if

```text
R_rel<<M*D^(11/4+o(1));                                (6.16)
```

equality merely matches the `D^(7/8)` threshold, and a strict saving beyond
`D^(1/4)` is needed to push below it.  There are `asymp D^3` available
primitive normal labels and raw reciprocal label budget `asymp D^2`; the
unproved step is again multiplicity packing across labels, not the local
three-pivot algebra.  The full proof and exact exponent ledger are in the
selected-support `K_(3,2)` report listed in the replay files below.

The abstract affine-plane/Steiner systems show why arithmetic is essential.
For `V=F_3^k`, its `d=(|V|-1)/2` affine-line triangle factors form matching
classes.  With flat weights their all-plus adjacency is `(J-I)/sqrt(|V|)`,
whose fourth trace is `asymp d^2`, whereas the randomized theorem is
`O(d)`.  Their coherent fibres have effective multiplicity `asymp d` and
violate `(CF)` by a polynomial factor, with no numerical defect coordinate
or product curvature available to force a tangent merger.

## 7. Binary status

```text
complex-to-absolute-weight domination:                 PROVED;
exact residual-block Walsh formula (2.4)--(2.5):       PROVED;
flat-bin randomized budget D*min(1,D/M):               PROVED;
Carleson range H<=max(1,M/D):                          AUTOMATIC;
critical open tail starts at H=D^(7/8):                PROVED;
current D^(9/8)=maximal fan times randomized budget:   EXACT LEDGER;
half-mass effective-multiplicity extraction:           PROVED;
fixed-endpoint defect/completion/carrier injection:    PROVED;
polynomial gap => polynomial physical defect fans:     PROVED;
defect map is a Freiman two-isomorphism:                PROVED;
H-fan => one rank-two plane with Omega(H^2/D) colors:   PROVED;
one fixed translation plane has weighted mass O(1):    PROVED;
high fibre forces m(C)>=3 locally:                      NO;
global polynomial violation has m(C)>=3 mass:           PROVED;
raw unsigned unconditionality before merger:           FALSE in cubic
                                                       full-integer model;
tangent packet obeys the sharp D budget:                PROVED;
defect fan => one tangent/Hankel chart:                  NOT PROVED;
rank-two-plane Carleson packing `(CF_M)`:                OPEN;
new global four-cycle exponent:                         NONE;
sharp four-cycle theorem:                               NOT PROVED.
```

Executable replay:

```text
src/qp_residual_walsh_defect_inverse.py
src/test_qp_residual_walsh_defect_inverse.py
src/qp_weighted_triangle_rademacher_square.py
src/test_qp_weighted_triangle_rademacher_square.py
src/qp_support_graph_k23_gate.py
src/test_qp_support_graph_k23_gate.py
```
