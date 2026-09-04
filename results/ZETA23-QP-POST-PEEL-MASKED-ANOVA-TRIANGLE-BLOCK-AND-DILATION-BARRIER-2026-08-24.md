# QP post-peeling masks: exact ANOVA, triangle blocks, and the dilation barrier

**Date:** 2026-08-24  
**Binary verdict:** the full post-peeling compatibility bridge is **not
proved**, and it is not a formal consequence of the proposed scalar or
unmasked `q^2` vector theorem.

There are two exact positive statements.

1. Every Hermitian pair-incidence mask has a constant/degree/broad ANOVA,
   whether or not it is a Gram mask.
2. If a residual interval has diameter less than `8*min(S)`, its
   all-distinct physical incidence matrix is a disjoint union of triangles.
   A masked ordered pair of such residual blocks has operator norm `O(1)`.

Neither statement aggregates the blocks.  There is an exact affine
countermodel over `F_3`: all residual blocks are edge-disjoint triangle
factors and their **full** centered sum has norm `1`, but selecting the
directions in a proper subspace gives a centered norm equal to twice the
number of selected blocks.  The corresponding ordered-block Gram has the
square of that norm.  Thus a full unmasked estimate can be perfect while a
legitimate block submask has an arbitrarily small fixed power excess above
the square-root scale.

There is a separate dilation obstruction.  A pair mask has a Hilbert-space
Gram lift exactly when it is positive semidefinite.  A diagonal-one `0/1`
mask is positive semidefinite only when its selected-pair relation is a
disjoint union of cliques.  General post-peeling masks need not have this
form.  Bilateral lifts of `0/1` masks can require factorization norm
`Omega(sqrt(r))` on an `r`-edge fibre.  Even positive-semidefinite masks do
not follow from the scalar theorem: two identical scalar carrier rows can
be killed exactly by centering while two different correlation lifts of
those rows have centered norm `asymp sqrt(r)`.

Consequently neither the `D^(71/64)` curvature sector nor the
`D^(137/128)` parabolic singleton sector is automatically absorbed.  A
successful bridge must be a completely bounded, mask-sensitive theorem for
the second physical tensor (or an equivalent unconditional ordered-block
square function), with its mask-dependent polar pullback controlled.  That
is an additional theorem, not a dilation of the presently stated `q^2`
estimate.

---

## 1. Residual blocks really are triangle matchings

Let `S` be the actual narrow prime-power shell and put

```text
s_0=min(S),                 R(a,b,c)=8*a*b*c-q^3.       (1.1)
```

The shell has endpoint ratio less than two, so it contains at most one
power of each prime base.  Consequently it is multiplicatively Sidon in
degree two:

```text
x*y=x'*y', x,y,x',y' in S
  => {x,y}={x',y'} as multisets.                       (1.2)
```

Fix an interval `I` of diameter strictly less than `8*s_0`.  If two triples
in its residual block share their first coordinate, then

```text
|8*a*(b*c-b'*c')|<8*s_0<=8*a.                         (1.3)
```

The expression in parentheses is integral, so it vanishes.  Equation
(1.2) says that `(b',c')` is either `(b,c)` or `(c,b)`.  The same argument
holds after fixing the second or third coordinate.

### Proposition 1.1 (exact triangle-block theorem)

In the all-distinct sector, the projected carrier--colour matrix

```text
T_I(b,c)=sum_a 1_(R(a,b,c) in I)                         (1.4)
```

is the adjacency matrix of vertex-disjoint triangles.

**Proof.**  One triple `(x,y,z)` brings all six permutations with it,
because their integer products and hence their residuals agree.  By
(1.3), any triple sharing one coordinate in the same role belongs to this
same permutation orbit.  Every value in the orbit occurs in every role, so
two different orbits cannot share an underlying shell value.  Projecting
the six permutations to `(b,c)` gives the six directed edges of the
triangle on `{x,y,z}`. `square`

Repeated-node degeneracies have already been assigned to the elementary
sectors.  Deleting or weighting individual incidences inside (1.4) leaves
a subgraph of each triangle, so its absolute row and column sums are at
most two.  Therefore

```text
||T_I,masked||_(2->2)<=2.                               (1.5)
```

If `I,J` are two ordered residual blocks, then

```text
||T_I^* T_J||<=4.                                       (1.6)
```

Any entrywise pair mask dominated in absolute value by the nonnegative
kernel `T_I^*T_J` also has absolute row and column sums at most four, hence
the same Schur bound.  This is the strongest automatic local consequence
of the short residual partition.

The whole active residual window has length `O(qD)`, while
`8*s_0 asymp q`.  It therefore has `O(D)` such blocks and `O(D^2)` ordered
block pairs.  Bounds (1.5)--(1.6) are at exactly the right local scale, but
they provide no orthogonality among those blocks.

## 2. Exact triangle-factor obstruction to the square function

Let

```text
V=F_3^m.
```

For every projective direction `[v]`, the affine lines

```text
{x,x+v,x+2v},                  x in V,                (2.1)
```

partition `V` into triples.  Let `A_[v]` be the union of the complete
triangle graphs on these lines.  Then

```text
A_[v] is symmetric and 2-regular,
||A_[v]||=2,                                            (2.2)
```

and different directions have disjoint edge sets.  Every two distinct
points determine a unique direction, so, writing `J` for the all-ones
matrix,

```text
sum_[v] A_[v]=J-I.                                     (2.3)
```

Thus the full doubly centered operator has norm exactly one:

```text
||P (sum_[v]A_[v]) P||=1.                              (2.4)
```

Now fix a proper `k`-dimensional linear subspace `W` of `V` and retain only
the directions contained in `W`.  Their number is

```text
d=(3^k-1)/2.                                           (2.5)
```

The selected sum is the disjoint union, over cosets of `W`, of complete
graphs on `3^k` vertices:

```text
sum_([v] subset W) A_[v]
   = direct-sum_(V/W) (J_(3^k)-I_(3^k)).               (2.6)
```

A vector constant on each coset, of total mean zero, is therefore an
eigenvector with eigenvalue

```text
3^k-1=2d.                                              (2.7)
```

Hence a subfamily of perfectly legal, edge-disjoint triangle blocks has

```text
||P sum_([v] subset W) A_[v] P||=2d,                  (2.8)
```

although the full sum in (2.4) has norm one.

The ordinary square function fails on the same vector `z`.  Every selected
factor obeys `A_[v]z=2z`, so

```text
||sum_([v] subset W) A_[v]z||^2
   =d * sum_([v] subset W)||A_[v]z||^2.                (2.9)
```

The required square-function constant is at least `d`, not `q^o(1)`.
For the ordered Gram blocks, every selected pair satisfies

```text
A_[v]^* A_[w] z=4z,                                   (2.10)
```

so the `d^2` ordered blocks align and their sum has eigenvalue `4d^2`.

This model also has the exact abstract three-coordinate uniqueness behind
Proposition 1.1: attach to each affine line all six permutations of its
three points and label its direction by one residual block.  Every ordered
pair of coordinate values occurs in at most one triple.  It is not an
actual prime-power/product-window construction, because the direction
labels have not been realized as numerical residual intervals.  Its role
is exact: residual-block divisibility, pair uniqueness, disjoint triangles,
and even the excellent full centered norm (2.4) do not imply stability
under a block mask.

Let `L=(3^m-1)/2` be the number of all blocks.  Choosing `k/m` arbitrarily
close to any fixed `theta in (1/2,1)` gives

```text
d=L^(theta+o(1))>sqrt(L)*L^(theta-1/2-o(1)).           (2.11)
```

Thus the obstruction exists for arbitrarily small fixed power violations,
including violations smaller than the powers left in the `71/64` and
`137/128` ledgers.  It is not merely a large constant or an endpoint
artifact.

## 3. Exact ANOVA for an arbitrary Hermitian pair mask

Let `E_b` be the physical edges on carrier `b`.  For a colour vector `z`,
write

```text
(R_b z)_e=kappa_e*z_(c(e)),             e in E_b.       (3.1)
```

Let `M_b=M_b^*` be any weighted pair-incidence mask on `E_b`, and define
the induced colour kernel

```text
K_M=sum_b R_b^* M_b R_b.                               (3.2)
```

This includes masks which cut through the rank-one all-pairs block on one
carrier.  No positivity or factorization is assumed.

Put

```text
u=n^(-1/2)1,               P=I-u*u^*,
d=K_M*1,                   dbar=n^(-1)1^*d,
delta=d-dbar*1,            w=delta/sqrt(n),
mu=dbar/n.                                             (3.3)
```

### Theorem 3.1 (masked Hermitian ANOVA)

For every Hermitian mask family,

```text
K_M-mu*J=P*K_M*P+u*w^*+w*u^*,                         (3.4)

||u*w^*+w*u^*||=||w||
  =[n^(-1)sum_i|d_i-dbar|^2]^(1/2),                   (3.5)

(P*K_M*P)^2=P*K_M^2*P-delta*delta^*/n.                (3.6)
```

Consequently

```text
max(||w||,||P*K_M*P||)
 <=||K_M-mu*J||
 <=||w||+||P*K_M*P||.                                 (3.7)
```

The proof is the same two-by-two block expansion as for the full carrier
matrix and uses only `K_M=K_M^*`.  This is the strongest unconditional
masked ANOVA: it remains true even when `M_b` is indefinite.

Its limitation is equally exact.  The covariance in (3.6) contains

```text
K_M^2
 =sum_(b,b') R_b^* M_b R_b R_(b')^* M_(b') R_(b'),    (3.8)
```

with all mask cross-products.  It is not the unmasked physical
common-neighbour covariance, and the `q^2` decomposition of the full edge
operator supplies no estimate for (3.8).

For completeness, an arbitrary rectangular weighted incidence operator
`A:C^n->C^m` also has an exact two-sided ANOVA.  With constant unit vectors
`u,v`, projections `P,Q`, and

```text
alpha=u^*A v,       s=P A v,       r=Q A^*u,       B=P A Q,
```

one has

```text
A-alpha*u*v^*=B+s*v^*+u*r^*,                         (3.9)
B^*B=Q*A^*P*A*Q,             B*B^*=P*A*Q*A^*P.       (3.10)
```

Equivalently,

```text
B^*B=Q*A^*A*Q-r*r^*,
B*B^*=P*A*A^*P-s*s^*.                                (3.11)
```

Thus nonsymmetry does not break ANOVA; it breaks the identification with
one physical scalar covariance.

## 4. Which pair masks admit a no-loss Hilbert dilation?

A Hilbert feature lift of one fibre has the form

```text
m_(e,e')=<xi_e,xi_(e')>_H.                            (4.1)
```

It turns the masked form into

```text
sum_(e,e')m_(e,e')x_e*conjugate(x_(e'))
 =||sum_e x_e xi_e||_H^2.                             (4.2)
```

Such a lift exists exactly when `M=(m_(e,e'))` is positive semidefinite.
If `m_(e,e)<=1`, the features may be chosen with norm at most one.

### Proposition 4.1 (`0/1` Gram masks)

A symmetric diagonal-one `0/1` matrix is positive semidefinite if and only
if its `1` relation is a disjoint union of cliques.

**Proof.**  In a Gram realization the diagonal-one vectors are unit.  If
their inner product is one, they are equal; if it is zero, they are
orthogonal.  Equality is transitive, so the indices split into orthogonal
classes, each class producing an all-ones block.  The converse is
immediate. `square`

The smallest warning is

```text
M_path=[1 1 0]
       [1 1 1],                                        (4.3)
       [0 1 1]
```

whose eigenvalues are

```text
1-sqrt(2), 1, 1+sqrt(2).                              (4.4)
```

It is a perfectly valid symmetric selection of pair incidences but has no
positive Hilbert dilation.  An original-edge deletion gives a clique
block; a pair-by-pair tangent assignment need not.

For a general bilateral lift, the relevant cost is the factorization norm

```text
gamma_2(M)=inf max_i||xi_i|| * max_j||eta_j||,
M_ij=<xi_i,eta_j>.                                     (4.5)
```

This cost can be polynomial even for `0/1` masks.  Let `H` be an `r by r`
Hadamard matrix and `M=(J+H)/2`.  Then `M` is `0/1`.  The nuclear-norm
lower bound and the elementary coordinate factorization give

```text
gamma_2(H)=sqrt(r),             gamma_2(J)=1.           (4.6)
```

Since `H=2M-J`,

```text
gamma_2(M)>=(sqrt(r)-1)/2.                             (4.7)
```

Embedding `M` and `M^T` as the two off-diagonal blocks of a symmetric
diagonal-one `0/1` mask retains this lower bound by restriction.  Thus an
arbitrary fibre of polynomial size cannot be lifted at `q^o(1)` cost.

### Even positive masks do not follow from the scalar theorem

Take two carriers and `r` colours.  The unmasked scalar incidence matrix is

```text
T=[1 ... 1]
  [1 ... 1].                                          (4.8)
```

Its output-centered norm is zero.  On the first carrier use the positive
correlation mask `J_r`, represented by sending every colour to the same
unit feature.  On the second use `I_r`, represented by orthogonal unit
features.  For the flat unit vector `z`, the two lifted outputs are

```text
y_1=sqrt(r)e_1,               y_2=r^(-1/2)(1,...,1).
```

Carrier centering gives exact energy

```text
||(P_2 tensor I)(y_1,y_2)||^2
   =(1/2)||y_1-y_2||^2=(r-1)/2.                       (4.9)
```

Thus even correlation masks with unit diagonal require a genuinely
coefficient-valued, coherently aligned theorem.  They do not tensorize from
the scalar centered estimate.

There is a further geometric ambiguity: if each carrier is dilated into a
different feature space, there is no canonical constant-carrier subspace
to remove.  Embedding all fibres into one common Hilbert space is extra
data, and (4.9) shows that its choice affects the centered norm.

## 5. Why this does not bridge the two remaining sectors

The high-completion formulation uses the second physical incidence
operator

```text
B_(alpha,gamma)=1
```

when the ordered row pair `alpha` and ordered colour pair `gamma` share a
physical carrier.  Completion multiplicities are entries of `B^*B`.
Tangent peeling assigns entries of this row-pair/colour-pair operator, not
necessarily original triples.  The curvature and parabolic singleton
restrictions are consequently pair masks on `B` or `B^*B`.

There is a useful scope distinction.  If the peel merely deletes entries
of `B`, the residual matrix `B_res` certainly exists and
`B_res^*B_res` is positive semidefinite.  This does **not** give a
first-level dilation of `T`.  One retained entry of `B` is already a wedge
of two original triples, and its row feature `alpha=(a_1,a_2)` depends
jointly on both edges.  Representing wedge deletion by individual edge
features would require its within-carrier pair relation to be a Gram mask;
Proposition 4.1 shows that this fails unless the retained relation is a
union of cliques.  Passing instead to `B_res` is a genuine second-tensor
theorem, not the Hilbert amplification of the linear operator `T`.

Moreover, the later restrictions used in the high tail are entrywise
threshold masks on `B_res^*B_res`, for example

```text
1_(K<=m(gamma,gamma')<2K),
m=(B_res^*B_res)_(gamma,gamma').                       (5.0)
```

Schur thresholding does not preserve positive semidefiniteness.  Thus even
the second-level Gram factorization does not automatically survive the
dyadic curvature/singleton mask whose weighted norm is actually being
estimated.

This failure occurs in dimension three.  The positive-definite matrix

```text
G=[1    3/5  1/10]
  [3/5  1    3/5 ]                                    (5.0a)
  [1/10 3/5  1   ]
```

has determinant `171/500>0`, while thresholding its entries at `1/2`
produces `M_path` from (4.3), which has eigenvalue `1-sqrt(2)<0`.

The `q^2` theorem proposed in the companion report concerns one fixed
unmasked carrier--colour synthesis

```text
sum_h alpha_h C_h                                      (5.1)
```

whose coefficients reconstruct the original fine window.  It does not
assert complete boundedness under:

```text
* arbitrary edge features depending on (a,b,c);
* arbitrary Schur masks on the second tensor B;
* arbitrary multipliers on residual blocks; or
* the mask-dependent operator-valued principal terms created by a lift. (5.2)
```

The affine example in Section 2 already refutes the third implication with
positive, edge-factorable masks.  Sections 4.1--4.9 refute the first two as
formal dilation principles.

A canonical pair-by-pair polarization also loses the required power.  For
a symmetric selected-pair graph,

```text
2 Re(x_i conjugate(x_j))
 =1/2*(|x_i+x_j|^2-|x_i-x_j|^2).                      (5.3)
```

The two incidence lifts in (5.3) have norm `O(sqrt(Delta_M))`, where
`Delta_M` is the maximum number of selected pairs containing one original
edge.  Their squared-norm estimate therefore pays `Delta_M`.  The current
one- and two-point-line ledgers do not bound this participation by
`q^o(1)`: an edge may participate once on each of polynomially many fresh
line, relation, or residual-block labels.  Giving every pair a fresh
feature merely destroys the cross-label cancellation which the proof needs.

At the `71/64` auxiliary curvature endpoint the longitudinal line length is
`O(1)`, but there are polynomially many different line labels.  At the
`137/128` parabolic singleton endpoint the unresolved term is explicitly
the nonprincipal aggregation over relation/character labels.  Neither fact
makes its mask an edge deletion or a union-of-cliques Gram mask.  A dilation
therefore does not reclassify these contributions as instances of (5.1).

The coarse `q^2` principal term also becomes feature- and mask-dependent.
It is not the scalar constant mode even before lifting.  The proved
`D^(23/24)` principal parabolic chart bound does not estimate the lifted
nonprincipal `D^(137/128)` kernel, and no identity moves the latter into the
principal chart.

Hence the statements

```text
unmasked q^2 vector theorem => D^(71/64) curvature is sharp,
unmasked q^2 vector theorem => D^(137/128) singleton is sharp            (5.4)
```

do not follow from the present decomposition.

## 6. The exact additional bridge that would suffice

One sufficient formulation is a completely bounded physical theorem.
For every actual post-peeling mask, construct a common Hilbert feature
space and a decomposition

```text
m_b(e,e')
 =sum_nu sigma_nu <xi_(nu,b,e),eta_(nu,b,e')>,          (6.1)

sum_nu |sigma_nu| sup_(b,e)||xi_(nu,b,e)||
                    sup_(b,e)||eta_(nu,b,e)||
 <=q^o(1),                                              (6.2)
```

such that the `q^2` square function holds for these coefficient-valued
features and every resulting polar pullback is charged to a proved
tangent/chart packet.  Condition (6.2) is a mask-specific `gamma_2` bound;
it is false for arbitrary masks by (4.7), so it must use new arithmetic of
the actual post-peeling family.

Equivalently, for the residual-block decomposition one needs the
unconditional ordered-block estimate

```text
|| sum_(I,J) epsilon_(I,J)
       P*T_I^*T_J*P - Polar_epsilon ||
   <<D*q^o(1)                                          (6.3)
```

for the precise sector masks `epsilon_(I,J)`.  The local norm in (1.6) is
`O(1)`, but the affine example makes (6.3) false for arbitrary block masks
even when the full unmasked covariance has norm one.

Proving (6.1)--(6.3) for the actual curvature and singleton masks would be
the missing compatibility theorem.  It is comparable in strength to the
mask-sensitive two-inverse/common-neighbour theorem itself; it is not an
automatic corollary of conductor lowering, ANOVA, triangle matching, or
Hilbert-space dilation.

## 7. Binary status

```text
short residual block is a disjoint triangle matching:       PROVED;
masked one-block norm O(1):                                 PROVED;
masked ordered-block norm O(1):                             PROVED;
square function across all ordered blocks from local norms: FALSE ABSTRACTLY;
full centered sum controls every block submask:              FALSE ABSTRACTLY;
Hermitian masked ANOVA (3.4)--(3.6):                        PROVED;
arbitrary pair mask has a positive Hilbert dilation:         FALSE;
0/1 PSD masks are exactly disjoint clique unions:            PROVED;
arbitrary 0/1 bilateral dilation costs q^o(1):               FALSE ABSTRACTLY;
scalar q^2 theorem tensorizes to all PSD masks:               FALSE ABSTRACTLY;
automatic closure of D^(71/64) curvature:                    NO;
automatic closure of D^(137/128) singleton:                  NO;
actual-prime counterexample to either desired bound:         NOT OBTAINED;
mask-completely-bounded bridge (6.1)--(6.3):                 OPEN;
sharp four-cycle theorem:                                   NOT PROVED.
```

Finite exact replays are in

```text
src/qp_post_peel_mask_stability.py
src/test_qp_post_peel_mask_stability.py
```

and verify the two ANOVA identities, the indefinite three-edge mask, the
positive two-carrier dilation gap, the affine triangle-factor obstruction,
and the Hadamard factorization lower bound.
