# QP sparse/TV classification and cosine-dilation general-position theorem

**Date:** 2026-08-14

**Verdict:** a significant finite-dimensional classification theorem is
proved.  For any fixed finite harmonic dictionary and any pairwise distinct
positive cosine nodes, all harmonic minors, carrier-augmented minors, and
affine minors are nonzero outside a locally finite set of dilation steps.
Consequently:

```text
every exact carrier representation needs at least M atoms;       (0.1)
every extreme TV minimizer has exactly M atoms;                   (0.2)
TV minimization is an exact finite minimum over Cramer bases;     (0.3)
every feasible positive depth maximizer is unique and M-atomic;   (0.4)
strict dual slack gives an explicit near-optimal stability bound. (0.5)
```

The exceptional all-remote AP chambers constructed in the preceding audit
are therefore not merely positive: on their square dictionary they are the
unique TV representations, the unique depth maximizers, and genuinely use
all `M` harmonics.  One coefficient may carry order-one weight while each of
the remaining `M-1` coefficients has weight `Theta(1/M)`; none can be deleted.

This definitively explains why the earlier sparse negative-peak core does not
compress to an exact promoter at a regular step.  It does **not** exclude a
deterministically selected step in the locally finite exceptional set, and it
does not bound the first entry of the actual prime-log flow into an open
positive chamber.  Hence it proves neither QP-PROMOTE nor a zeta strip.

---

## 1. The two optimization problems

Let

```text
u_1,...,u_M > 0                                      (1.1)
```

be pairwise distinct and let `H` be a finite set of `N>=M` distinct positive
integers.  Put

```text
a_k(tau)=(cos(k tau u_j))_(j<=M),
A_H(tau)=[a_k(tau)]_(k in H),
q_0=(1,...,1)^T.                                      (1.2)
```

The signed total-variation problem is

```text
C_TV(tau)=min{||c||_1:A_H(tau)c=q_0}.                 (1.3)
```

The positive antipode problem is

```text
r_+(tau)=max{r>0:-r q_0 in conv{a_k(tau):k in H}}.    (1.4)
```

It is useful to remove the probability normalization.  If

```text
A_H z=-q_0,       z>=0,       C=1^Tz,                 (1.5)
```

then

```text
w=z/C,                 r=1/C.                         (1.6)
```

Thus maximizing positive depth is the one-sided LP

```text
C_+(tau)=min{1^Tz:A_Hz=-q_0,z>=0},
r_+(tau)=1/C_+(tau).                                  (1.7)
```

The direction and signs in (1.4)--(1.7) matter.  The positive problem is not
the symmetric Elfving body used for (1.3).

---

## 2. Exact cosine-Vandermonde transversality

The genericity assertion needed here is one-dimensional in `tau`; it is not
an appeal to unspecified generic phases.

### Theorem 2.1 (cosine determinant leading term)

Let `v_1,...,v_m` be distinct nonnegative real numbers and let
`k_1,...,k_m` be distinct nonnegative integers.  Then

```text
D(tau)=det(cos(k_l tau v_i))_(i,l<=m)                 (2.1)
```

has the expansion

```text
D(tau)
=(-1)^[m(m-1)/2]
 * tau^[m(m-1)]
 * product_(i<j)(v_j^2-v_i^2)
 * product_(l<r)(k_r^2-k_l^2)
 / product_(n=0)^(m-1)(2n)!
 +O(tau^[m(m-1)+2]).                                  (2.2)
```

In particular, `D` is not identically zero and its real zero set is locally
finite.  When `m=1`, (2.2) says simply
`cos(k_1 tau v_1)=1+O(tau^2)`; it need not be constant, but the nonzero
leading term is all that is required.

#### Proof

Write

```text
cos(k tau v)=sum_(n>=0)
 (-1)^n (k^2)^n (v^2)^n tau^(2n)/(2n)!.               (2.3)
```

Apply Cauchy--Binet to the product of the infinite evaluation matrix
`((v_i^2)^n)` and coefficient matrix
`((-1)^n(k_l^2)^n tau^(2n)/(2n)!)`.  A nonzero determinant must use distinct
Taylor orders.  The unique least total order is

```text
{0,1,...,m-1},       sum n=m(m-1)/2.                  (2.4)
```

Its two determinants are the Vandermonde products in (2.2).  Every other
choice raises the power of `tau` by at least two.  This proves (2.2).  QED

The formula includes both special augmentations used below:

```text
k=0       gives the carrier column q_0;
v=0       gives the affine row (1,...,1).              (2.5)
```

### Theorem 2.2 (full spark, carrier transversality, affine general position)

For fixed `u` and finite `H`, there is a locally finite set

```text
E(u,H) subset (0,infinity)                            (2.6)
```

such that for every `tau` outside `E(u,H)`:

1. every `M` columns of `A_H(tau)` are a basis of `R^M`;
2. `q_0` together with every set of fewer than `M` dictionary columns is
   linearly independent;
3. every `M+1` dictionary atoms are affinely independent.

#### Proof

For item 1 and each `M`-set `K subset H`, apply Theorem 2.1 with nodes
`u_1,...,u_M` and frequencies `K`.  The determinant is a nonzero analytic
function of `tau`.

For item 2, let `K` have size `s<M`, restrict to any fixed `s+1` of the
distinct nodes, and use frequencies

```text
{0} union K.                                           (2.7)
```

The resulting determinant is precisely a minor of `[q_0,A_K]`, and Theorem
2.1 again says that it is not identically zero.

For item 3, append the affine row `(1,...,1)` to any `M+1` atoms.  By (2.5)
its determinant is (2.1) with nodes

```text
0,u_1,...,u_M                                          (2.8)
```

and the selected `M+1` positive frequencies.  Its leading coefficient is
nonzero.

There are only finitely many selected column sets.  A finite union of zero
sets of nonzero real-analytic functions is locally finite on
`(0,infinity)`.  Remove that union.  QED

### Corollary 2.3 (sharp generic support lower bound)

For `tau` outside `E(u,H)`, every solution of

```text
A_H(tau)c=q_0                                          (2.9)
```

has at least `M` nonzero coefficients.  Likewise every positive solution of
`A_Hz=-q_0` has support at least `M`.

This is immediate from item 2 of Theorem 2.2.  The lower bound is sharp by
the classifications below.

---

## 3. Complete signed-TV classification

Fix a regular `tau`, suppress it from the notation, and for every
`M`-element subset `K` of `H` put

```text
c^K=A_K^(-1)q_0,
C_K=||c^K||_1.                                        (3.1)
```

Every entry of every `c^K` is nonzero: otherwise `q_0` would lie in the span
of `M-1` columns.

### Theorem 3.1 (minimum-Cramer classification)

At every regular step,

```text
C_TV=min_(K subset H, |K|=M) C_K.                     (3.2)
```

Embed each `c^K` in `R^H` by setting its off-support entries to zero.  The
whole set of TV minimizers is the convex hull of the basis vectors attaining
the minimum in (3.2).  In particular, every extreme minimizer has exactly
`M` atoms.

#### Proof

Split `c=c^+-c^-` and minimize `1^T(c^++c^-)` subject to

```text
[A_H,-A_H](c^+,c^-)^T=q_0,       c^+,c^->=0.          (3.3)
```

An optimal extreme point exists because the objective level sets are
bounded.  A basic feasible solution of (3.3) has at most `M` positive
variables.  It never uses both signs of one column, since cancelling their
common positive part lowers the objective.  Corollary 2.3 forces at least
`M` distinct dictionary atoms.  Hence every optimal extreme point has
exactly `M` atoms and equals `c^K` for a square basis `K`.  This proves (3.2).
The optimal face is compact and is the convex hull of its extreme points.
QED

### Theorem 3.2 (exact dual, uniqueness, and strict certificate)

For a basis candidate `c^K`, set

```text
s_K=sign(c^K),
y_K=A_K^(-T)s_K.                                      (3.4)
```

Then `c^K` is TV-optimal if and only if

```text
|a_l^T y_K|<=1             for every l outside K.     (3.5)
```

It is the unique TV minimizer if and only if all inequalities in (3.5) are
strict.  Equivalently,

```text
C_TV=max{q_0^Ty:||A_H^Ty||_infinity<=1}.              (3.6)
```

#### Proof

Equations (3.5)--(3.6) are primal-dual equality for basis pursuit.  For
completeness, `q_0^Ty_K=(c^K)^Ts_K=C_K`; hence (3.5) proves optimality by
Holder's inequality.

If the off-support slack is strict and `c` is another feasible vector, the
standard subgradient inequality is strict unless `c` is supported on `K`;
invertibility of `A_K` then gives `c=c^K`.

Conversely, suppose `|a_l^Ty_K|=1` off support.  Put

```text
sigma=sign(a_l^Ty_K),
h_l=sigma,
h_K=-A_K^(-1)a_l sigma.                               (3.7)
```

Then `Ah=0`, and while the signs on `K` persist,

```text
d/dt|_(0+) ||c^K+t h||_1
=s_K^Th_K+|h_l|
=-sigma y_K^Ta_l+1=0.                                (3.8)
```

For all sufficiently small positive `t`, the objective is exactly affine
with zero slope, producing a distinct optimum.  QED

This necessary-and-sufficient strict-certificate statement is classical; its
specialization here is included to keep the determinant signs auditable.

---

## 4. Unique positive depth and its hostile sign check

For a basis `K`, retain it only when

```text
c^K=A_K^(-1)q_0<0             coordinatewise.         (4.1)
```

Define

```text
C_K^+=-1^Tc^K,
r_K=1/C_K^+.                                           (4.2)
```

### Theorem 4.1 (positive Cramer/facet classification)

At a regular step, a positive antipode exists if and only if at least one
basis satisfies (4.1).  When it exists,

```text
C_+=min_(K:c^K<0)(-1^Tc^K),
r_+=max_(K:c^K<0) 1/(-1^Tc^K).                        (4.3)
```

The maximizing basis is unique.  Its weights and depth are

```text
w_K=-c^K/(-1^Tc^K),
r_+=1/(-1^Tc^K).                                      (4.4)
```

Every weight is strictly positive, and the support has exactly `M` atoms.
If `N>=M+1`, geometrically `-r_+q_0` lies in the relative interior of a
simplicial supporting facet with exactly `M` vertices.  If `N=M`, it instead
lies in the relative interior of the whole `(M-1)`-simplex dictionary, and
uniqueness is the square-system statement proved separately below.

#### Proof

Every negative Cramer vector gives (4.4) directly, so the right side of
(4.3) is feasible.  Conversely, an extreme solution of the one-sided LP
(1.7) uses at most `M` atoms, while Corollary 2.3 forces at least `M`; hence it
is one of the candidates (4.1).

For uniqueness, first suppose `N=M`.  Full spark makes `A_H` invertible, so
`A_Hz=-q_0` has at most one solution.  If it is positive, (4.4) is therefore
the unique optimizer and Corollary 2.3 gives its full support.

Now suppose `N>=M+1`, and let

```text
P=conv{a_k:k in H},        x_*=-r_+q_0.               (4.5)
```

Maximality of `r_+` puts `x_*` on the boundary of `P`.  Every convex
representation of `x_*` is supported on its minimal face `F`.  If `F`
contained `M+1` dictionary atoms, those atoms would lie in one supporting
hyperplane and be affinely dependent, contrary to Theorem 2.2(3).  Thus
`F` has at most `M` vertices.  If it had fewer than `M`, then `q_0` would lie
in their linear span, contrary to Theorem 2.2(2).  Hence `F` has exactly `M`
vertices.  They are affinely independent, so `F` is a simplex and its
barycentric representation is unique.  Theorem 2.2(3) makes the dictionary
polytope full-dimensional, so `F` is a facet.  Minimality of `F` makes every
weight strictly positive.  QED

### Theorem 4.2 (two exact dual formulations)

Let `K_*` be the unique positive optimizer and put

```text
y_+=-A_(K_*)^(-T)q_0.                                 (4.6)
```

Then

```text
A_(K_*)^T y_+=-q_0,
A_H^T y_+>=-q_0,
C_+=q_0^Ty_+.                                         (4.7)
```

All off-support inequalities are strict.  Equivalently,

```text
C_+=max{q_0^Ty:A_H^Ty>=-q_0}.                         (4.8)
```

The depth itself has the support-function minimax formula

```text
r_+=min_(y:q_0^Ty=-1) max_(k in H) y^Ta_k.             (4.9)
```

The signs in (4.7)--(4.9) have been checked both algebraically and against a
linear program.  In particular, (4.9) normalizes `q_0^Ty=-1`, not `+1`.

#### Proof

Equation (4.8) is the dual of (1.7), since `A_Hz=-q_0` and `z>=0` give the
dual constraint `A_H^Ty>=-q_0`.  Equations (4.6)--(4.7) are complementary
slackness.  An off-support equality would put an additional atom in the
supporting facet, contradicting Theorem 2.2(3).

For (4.9), any feasible `-r q_0=sum w_k a_k` and any `y` with
`q_0^Ty=-1` satisfy

```text
r=sum_k w_k y^Ta_k<=max_k y^Ta_k.                    (4.10)
```

Thus the right side of (4.9) is at least `r_+`.  Set

```text
y=-y_+/C_+.                                           (4.11)
```

Then `q_0^Ty=-1`, active atoms have `y^Ta_k=1/C_+=r_+`, and (4.7) gives
`y^Ta_l<=r_+` for every other atom.  Equality follows.  QED

---

## 5. Quantitative uniqueness and stability

### Theorem 5.1 (dual-slack stability)

Suppose `c^*` is the unique signed optimum on support `K`, and define

```text
eta=1-max_(l outside K)|a_l^Ty_K|>0,
beta=||A_K^(-1)||_infinity.                           (5.1)
```

Every feasible `c` with

```text
||c||_1<=C_TV+epsilon                                 (5.2)
```

satisfies

```text
||c_(K^c)||_1<=epsilon/eta,
||c-c^*||_1<=(1+M beta)epsilon/eta.                   (5.3)
```

For the positive problem, define its strict one-sided slack

```text
eta_+=min_(l outside K_*)(1+a_l^Ty_+)>0.              (5.4)
```

When the dictionary is square, the off-support sets are empty.  In that case
the feasible representation is already unique; throughout this theorem use
the convention `eta=eta_+=+infinity`, so the off-support bounds read zero.

Every feasible `z>=0`, `Az=-q_0`, with `1^Tz<=C_++epsilon` satisfies

```text
||z_(K_*^c)||_1<=epsilon/eta_+,
||z-z^*||_1<=(1+M||A_(K_*)^(-1)||_infinity)
              epsilon/eta_+.                         (5.5)
```

#### Proof

For the signed problem, subgradient duality gives

```text
||c||_1-C_TV
>=sum_(l outside K)(1-|a_l^Ty_K|)|c_l|
>=eta ||c_(K^c)||_1.                                 (5.6)
```

Feasibility gives

```text
A_K(c_K-c_K^*)=-A_(K^c)c_(K^c).                      (5.7)
```

Every cosine entry has magnitude at most one, so the infinity norm of the
right side is at most `||c_(K^c)||_1`.  Multiplication by `A_K^-1` and
conversion from infinity to `l1` prove (5.3).

For the positive problem, (4.7) gives the exact identity

```text
1^Tz-C_+
=sum_k (1+a_k^Ty_+)z_k
>=eta_+||z_(K_*^c)||_1.                              (5.8)
```

The same basis-inverse argument proves (5.5).  QED

### Lemma 5.2 (finite-dictionary phase stability)

At a regular phase point, define over all `M`-bases

```text
beta=max_K ||A_K^-1||_infinity,
L=max_K ||A_K^-1q_0||_infinity,
nu=min_(K,j)|(A_K^-1q_0)_j|.                          (5.9)
```

For signed TV, let `gamma` be the positive gap between the unique winning
candidate cost and the next Cramer cost.  For the positive problem, take the
next cost only among negative Cramer vectors; condition (5.15) keeps that
feasible set unchanged.  With only one candidate, use `gamma=+infinity`.
If each phase changes by at most `rho` and
`K_max=max H`, put

```text
e=M K_max rho.                                        (5.10)
```

If

```text
beta e<=1/2,                                          (5.11)
```

then every Cramer vector changes in infinity norm by at most

```text
2 beta e L,                                           (5.12)
```

and every candidate cost changes by at most

```text
2M beta e L.                                          (5.13)
```

Thus the winning support persists if

```text
4M beta e L<gamma.                                    (5.14)
```

All Cramer sign patterns, hence the set of positive bases, persist if also

```text
2 beta e L<nu.                                        (5.15)
```

#### Proof

The cosine Lipschitz bound makes each matrix entry change by at most
`K_max rho`, and hence each basis changes by at most `e` in row-sum norm.
The Neumann series under (5.11) gives perturbed inverse norm at most
`2 beta`.  The resolvent identity gives (5.12); summing coordinates gives
(5.13).  Comparing the possible upward motion of the winner with the
possible downward motion of a competitor proves (5.14), and (5.15) prevents
a coefficient from crossing zero.  QED

This is a genuine stability theorem, not only an openness assertion.  It is
finite-dimensional; no uniform polynomial lower bound for `rho` is claimed
when `M` grows.

---

## 6. Explicit all-remote extremal chambers

The following strengthens the interpretation, but not the construction, of
the universal chamber from the preceding hostile audit.

### Theorem 6.1 (unique full-support all-remote chamber)

Let `M>=2`, put `D=2M-1`, and choose

```text
0<c<(sqrt(2)-1)/2,
epsilon=c/M,
H_M={M,M+1,...,D}.                                    (6.1)
```

There are `M` distinct phases `theta_1,...,theta_M` in `(0,pi)` for which
the square matrix

```text
A_(j,k)=cos(k theta_j),        k in H_M               (6.2)
```

is invertible and its unique carrier representation is

```text
c_M=...=c_(D-1)=-2c/M,
c_D=-2.                                                (6.3)
```

It is the unique signed-TV representation and the unique positive antipode
on this dictionary.  Explicitly,

```text
C=2[1+c(M-1)/M],
r=1/{2[1+c(M-1)/M]},                                  (6.4)

w_D=1/[1+c(M-1)/M],
w_k=(c/M)/[1+c(M-1)/M]       (M<=k<D).                (6.5)
```

Invertibility, uniqueness, full support, and strict positivity persist on an
open phase neighborhood.  The exact coefficients, weights, and depth in
(6.3)--(6.5) hold at the constructed phase point and vary continuously under
perturbation; they are not asserted constant on that neighborhood.

#### Proof

Consider

```text
F(theta)=1/2+(c/M)sum_(k=M)^(D-1)cos(k theta)
                   +cos(D theta).                     (6.6)
```

Around every root of `1/2+cos(D theta)`, use radius `pi/(12D)`.  At each
endpoint the unperturbed magnitude is at least `(sqrt(2)-1)/2`, while the
entire perturbation is less than `c`; hence all `D` sign changes persist.

The resulting root-by-`H_M` matrix has column rank `M`.  Otherwise a
supported cosine polynomial of degree at most `D` would vanish at all `D`
roots and be proportional to `F`; its missing constant term makes this
impossible.  The `D` disjoint sign changes already exhaust the degree-`D`
polynomial in `cos(theta)`, so there is exactly one root per bracket and every
root is simple.  Select an invertible `M`-row minor.  At every selected root,
(6.6) gives exactly (6.3).  The square dictionary makes this the only
representation, and (6.4)--(6.5) follow by normalization.  Strict signs and
invertibility persist by continuity or Lemma 5.2.  QED

The support lower bound `M` is therefore attained.  The example also shows
that no coefficient lower bound stronger than order `1/M` is possible at
fixed positive depth: `M-1` atoms are individually small but jointly
essential.

### Corollary 6.2 (Kronecker transfer)

If `u_1,...,u_M` are linearly independent over `Q`, the flow

```text
tau -> (tau u_1,...,tau u_M) mod 2pi                  (6.7)
```

enters an open chamber from Theorem 6.1 with positive lower asymptotic time
density.  Thus there are arbitrarily large `tau` for which the all-remote
square AP dictionary has a unique, strictly `M`-supported positive antipode
of fixed depth.

Indeed, the open chamber contains a phase box whose boundary has Haar measure
zero.  Unique ergodicity gives that box its positive Haar visit frequency,
which lower-bounds visits to the whole chamber.  As in the preceding audit,
this provides no first-entry bound uniform in growing `M`.

---

## 7. Consequence for the sparse-core route

The earlier theorem forced at least

```text
r/(2-r)                                                (7.1)
```

of the barycentric mass onto at most

```text
O(r^-2 Y^o(1))                                         (7.2)
```

negative-peak harmonics.  The present theorem identifies the exact limit of
that compression:

```text
at every regular step, the core alone cannot represent q_0
whenever its cardinality is below M.                  (7.3)
```

The complementary harmonics can have very small total or individual weight
and still carry indispensable transverse coordinates.  Theorem 6.1 is an
explicit fixed-depth model of precisely this behavior.

This is a no-go theorem for **exact support deletion at regular steps**.  It
is not a no-go theorem for:

```text
approximate sparse promotion;
a deterministic tau in E(u,H);
an arithmetic argument that rules out all positive chambers;
or an early actual-prime entry into a full-support chamber.       (7.4)
```

---

## 8. Literature boundary and novelty scope

The convex and optimization components are classical.

* Elfving's theorem gives the directional boundary characterization in the
  symmetric convex hull used by `c`-optimal design:
  G. Elfving,
  [*Optimum Allocation in Linear Regression Theory*](https://doi.org/10.1214/aoms/1177729442).
  H. Dette and V. Melas,
  [*Optimal Designs for Estimating Individual Coefficients in Fourier
  Regression Models*](https://doi.org/10.1214/aos/1065705122), solve related
  fixed-order Fourier `c`-optimal design problems; their design variable and
  target differ from the fixed-node harmonic-atom transpose in (1.2).
* The strict dual certificate in Theorem 3.2 is the exact finite basis-pursuit
  uniqueness criterion:
  H. Zhang, W. Yin, and L. Cheng,
  [*Necessary and Sufficient Conditions of Solution Uniqueness in
  1-Norm Minimization*](https://arxiv.org/abs/1209.0652).
* Chebyshev moment-space theory proves uniqueness of boundary and principal
  representations in its continuous design-variable setting; a modern
  design account is H. Dette and K. Schorning,
  [*Complete Classes of Designs for Nonlinear Regression Models and
  Principal Representations of Moment Spaces*](https://arxiv.org/abs/1306.4872).
  Consecutive `1,T_1,...,T_m` form a Chebyshev system, but an arbitrary
  gapped harmonic selection need not have a determinant of one fixed sign on
  the whole phase interval.  Theorem 2.2 instead proves nonidentity and a
  locally finite zero set along the specified dilation path.
* Finite trigonometric moment determinacy and positive-polynomial
  certificates are treated by J.-P. Gabardo,
  [*Truncated Trigonometric Moment Problems and Determinate
  Measures*](https://doi.org/10.1006/jmaa.1999.6567).
* Trigonometric convex hulls and their faces belong to the orbitope
  literature; see R. Sanyal, F. Sottile, and B. Sturmfels,
  [*Orbitopes*](https://arxiv.org/abs/0911.5436), and A. Barvinok,
  S. Lee, and I. Novik,
  [*Neighborliness of the Symmetric Moment Curve*](https://arxiv.org/abs/1104.5168).
* The relation between total positivity and cyclic-polytope geometry is
  classical; see B. Sturmfels,
  [*Totally Positive Matrices and Cyclic
  Polytopes*](https://doi.org/10.1016/0024-3795(88)90250-9).
* The closest coefficient-dominance theorem behind the explicit root
  chambers is P. Lakatos and L. Losonczi,
  [*Self-Inversive Polynomials Whose Zeros Are on the Unit
  Circle*](https://doi.org/10.5486/PMD.2004.3250).  It gives sufficient
  conditions, simplicity, and root-location intervals for unimodular zeros;
  it does not classify the fixed-node cosine carrier LP or its dilation
  exceptional set.
* The closest general full-spark reference is B. Alexeev, J. Cahill, and
  D. G. Mixon,
  [*Full Spark Frames*](https://doi.org/10.1007/s00041-012-9235-4), which
  constructs full-spark frames using Vandermonde and discrete Fourier
  matrices and proves abundance results.  It does not give the simultaneous
  carrier transversality and affine general position along the present
  one-parameter cosine-dilation path.

None of these sources is claimed to miss a theorem in its own setting.  The
generalized-Vandermonde expansion (2.2), LP basis classification, dual
certificates, and simplicial-facet argument are individually standard
mechanisms.

The contribution established here is their exact project-specific synthesis:

```text
one common locally finite exceptional set for the cosine-dilation path;
simultaneous full spark, q_0-transversality, and affine general position;
minimum-Cramer classification for the signed QP carrier;
automatic uniqueness of the positive AP depth maximizer;
and the sharp interpretation of the all-remote chamber as full-support.
                                                               (8.1)
```

No broad historical priority claim is made without a dedicated publication
search beyond the primary literature above.

---

## 9. Exact disposition

```text
cosine generalized-Vandermonde leading term:          PROVED;
locally finite dilation exceptional set:              PROVED;
all M harmonic columns full spark off that set:       PROVED;
q_0 plus every <M columns independent:                PROVED;
every M+1 atoms affinely independent:                 PROVED;
generic exact support lower bound M:                  PROVED / SHARP;
minimum-Cramer signed-TV formula:                     PROVED;
signed uniqueness iff strict dual certificate:        PROVED;
positive depth Cramer formula:                        PROVED;
positive optimizer unique, strict, M-atomic:          PROVED;
hostile-sign radial minimax formula:                  PROVED;
dual-slack near-optimal stability:                    PROVED;
finite-dictionary phase stability:                    PROVED;
explicit all-remote unique fixed-depth chambers:      PROVED;
generic Kronecker recurrence to those chambers:       PROVED;
uniform first hit before B/M:                         OPEN;
deterministic avoidance of E(u,H):                    OPEN;
QP-PROMOTE / zeta strip:                              NOT PROVED.
```

The next live AP question remains arithmetic and finite-aperture: either
certify one legal full-support chamber entry, or prove the actual prime-log
flow avoids all such chambers up to `B/M`.  Further Caratheodory compression
or generic determinant arguments cannot decide it.

## 10. Replay

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_sparse_tv_classification.py
python3 results/verify_zeta23_qp_sparse_tv_classification.py
PYTHONPATH=src python3 src/qp_sparse_tv_classification.py --nodes 5
```
