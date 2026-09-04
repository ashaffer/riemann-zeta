# QP balanced broad sector: algebraic incidence fibration barrier

**Date:** 2026-08-24  
**Verdict:** polynomial partitioning, an Elekes--Szabo theorem, or a
coefficient-uniform determinant method does not by itself recover the missing
`D^(1/8)` in the balanced rank-two chart.  There is an exact reason stronger
than an unfavorable numerical exponent: after the four physical residuals
are retained, the completion surfaces are essentially **disjoint fibres** of
one additive--multiplicative rational map.  A selected physical endpoint has
only boundedly many colour fibres through it (in fact its product matrix
determines the colour uniquely for large `q`).  Thus the linear point term in
any point--variety incidence theorem is the unresolved occupied-slice count
itself.

Each of the two ambient hypersurface relations is group-related (one
additively and one multiplicatively).  Their simultaneous complete
intersection can be a non-group-like ternary quadric after elimination, but
the Elekes--Szabo Cartesian estimate is then larger than the already known
`K`-point matching and supplies no aggregation across fibres.  Removing
ruling lines and the already controlled parabolic affine-plane packets does
not change this global fibration.  An exact twisted-cubic construction below has
arbitrarily many integral points on one nonzero-level fibre, every same-fibre
secant invertible, and at most three points in every affine two-plane.

This is an algebraic-method obstruction, not an actual prime-power
counterexample.  The actual shell excludes the old fixed-level Farey model,
and it may also exclude simultaneous saturation of many fibres.  Proving
that exclusion with a power saving would be a genuinely new arithmetic
distribution theorem for the product-window mask; it is not supplied by
ordinary polynomial partitioning or the determinant method.  Consequently
the sharp four-cycle estimate remains open.

---

## 1. The balanced target

At the surviving balanced face,

```text
q=D^(33/16),       M=D^(15/8),       K=D^(5/16),
N_col=M^3*D/q=D^(73/16).                         (1.1)
```

Here `K` is the cap for occupied third-coordinate slices and `N_col` is the
principal determinant-band colour count.  The desired estimate and the
pointwise slice estimate are

```text
sum_C J(C) <= D*M^2 = D^(76/16),
sum_C J(C) <= K*N_col = D^(78/16).                (1.2)
```

Thus a global method must save

```text
D^(2/16)=D^(1/8).                                 (1.3)
```

The fixed-plane prime chart from the preceding report is sharp enough once
the rational plane `W(C)` is fixed.  Its unresolved operation is the union
over varying fibres/planes.

## 2. Exact additive--multiplicative fibration

Put `Q=q^3`.  For a completion with row carrier `a=(a1,a2)`, column carrier
`b=(b1,b2)`, colour matrix `C=(c_ij)`, and rank-one product matrix

```text
P=(a_i*b_j)_ij,
```

define its four exact residuals by

```text
r_ij=8*a_i*b_j*c_ij-Q.                            (2.1)
```

On the positive residual box introduce

```text
S(r)=r11+r22-r12-r21,
R(r)=((Q+r11)*(Q+r22))/((Q+r12)*(Q+r21)).          (2.2)
```

### Proposition 2.1 (exact residual fibre identity)

Every completion satisfies

```text
S(r)=8*(c11*p11+c22*p22-c12*p12-c21*p21)=8L,
R(r)=(c11*c22)/(c12*c21)=rho(C).                  (2.3)
```

**Proof.**  The four copies of `Q` cancel from the alternating sum, giving
the first identity.  For the second,

```text
(Q+r11)*(Q+r22)
 =64*a1*a2*b1*b2*c11*c22,
(Q+r12)*(Q+r21)
 =64*a1*a2*b1*b2*c12*c21.                         (2.4)
```

Cancel the common carrier product.  QED

Consequently all completions on one pinned colour level lie on the affine
surface

```text
F_(ell,rho)={r:S(r)=ell,
                (Q+r11)*(Q+r22)=rho*(Q+r12)*(Q+r21)}. (2.5)
```

Different parameter pairs give disjoint fibres.  Equivalently, in product
coordinates the diagonal affine map

```text
r_ij=8*c_ij*p_ij-Q                               (2.6)
```

identifies (2.5) with

```text
Sigma_(C,L)={P:det P=0, <C,P>=L}.                 (2.7)
```

When `det C!=0` and `L!=0`, (2.7) is a smooth split affine quadric surface.
Its two ordinary rulings are obtained by fixing one of the two projective
carrier factors.

### Lemma 2.2 (the fibre parameter has bounded colour multiplicity)

For an all-distinct actual-shell colour, `rho(C)` determines `C` up to the
two permutations of its diagonal pair and the two permutations of its
off-diagonal pair.

**Proof.**  Distinct actual shell nodes have distinct prime bases: two
different powers of one prime have ratio at least two, while the project
shell ratio is less than two.  Hence

```text
(c11*c22)/(c12*c21)                               (2.8)
```

is already in lowest terms.  Equality of two such fractions and unique
factorisation identify separately the unordered numerator and denominator
pairs.  There are at most four orientations.  QED

There is an even stronger endpoint statement.  If a rank-one product entry
`p_ij` is fixed in the physical shell, the product window confines `c_ij`
to an interval of length

```text
O(q*D/p_ij)=O(D/q)=D^(-17/16)<1.                  (2.9)
```

Thus the full product matrix `P` determines the oriented colour matrix, if
one exists.  This uses the actual mask and not merely (2.5).

## 3. Why point--surface partitioning has no incidence gain

Choose one completion endpoint in each occupied third slice.  Regard its
residual vector as a point and its colour-level surface (2.5) as a variety.
By Lemma 2.2 each selected point is incident to only `O(1)` relevant
surfaces; by (2.9), using product matrices instead makes the point degree at
most one.  The already proved multiplicative-Sidon statement makes the
product-matrix map injective in the all-distinct generic sector.  Therefore

```text
# selected points  asymp  # occupied (C,slice) incidences. (3.1)
```

At (1.1), the a priori size of both sides is `D^(78/16)`.  Every standard
point--variety incidence estimate contains a linear point term, and here
that term is already

```text
D^(78/16),                                        (3.2)
```

whereas the required answer is `D^(76/16)`.  Cellular partitioning cannot
turn (3.1) into a saving: the surfaces are fibres, so the points do not make
the transversal multiple incidences on which a superlinear incidence term
acts.

The four-endpoint reconstruction from the rank-two chart does not repair
this.  Four generic endpoints recover `W(C)` and the primitive normal
`w_C`, but one physical endpoint already recovers `C` through (2.9).  The
reconstruction is valuable for identifying structure inside a rich colour;
it does not create overlap between different colour fibres.

There is a parallel failure in the Grassmannian formulation.  A rational
two-plane `W` is a point of `Gr(2,4)`, and the condition

```text
W subset w_C^perp                                  (3.3)
```

is a Schubert-plane incidence.  However the reduction convention assigns
only one `W(C)` to each colour, while `J(C)` is a weight attached to that
single edge.  Replicating the colour `J(C)` times only creates coincident
copies.  A point--Schubert-plane theorem can count distinct edges, not
improve these unconstrained fibre weights.  The fixed-`W` prime chart is
precisely the available arithmetic input; the missing statement is a bound
on simultaneous fibre saturation.

## 4. Elekes--Szabo audit: exceptional ambient equations, useless sparse closure

On the physical box all `Q+r_ij` are positive.  The two fibre equations can
be written

```text
r11+r22-r12-r21=ell,                              (4.1)

log(Q+r11)+log(Q+r22)
 -log(Q+r12)-log(Q+r21)=log rho.                  (4.2)
```

Thus (2.5) is the common level of one additive rectangular invariant and
one multiplicative invariant which becomes additive under four locally
invertible logarithms.  Each ambient hypersurface separately is exactly in
the group-related exceptional class.  The same is true of the original
four-variable product equation

```text
8*a*b*c-Q-r=0,                                    (4.3)
```

which becomes `log a+log b+log c-log((Q+r)/8)=0`.

It would be too strong, however, to declare the **simultaneous** complete
intersection automatically group-related.  Write

```text
x=Q+r11, y=Q+r12, z=Q+r21,
w=Q+r22=ell-x+y+z.                                (4.4)
```

The remaining ternary equation is

```text
F_(ell,rho)(x,y,z)
 =x*(ell-x+y+z)-rho*y*z=0.                        (4.5)
```

For generic `(ell,rho)` this ternary quadric may satisfy the non-group
hypothesis of a three-variable Elekes--Szabo theorem.  That still gives no
useful estimate here.  Replacing the three coordinate sets by the coordinate
projections of `J` selected points gives sets of size at most `J<=K`, while
the balanced Cartesian bound is of order

```text
K^(11/6)>K.                                       (4.6)
```

The physical points form a sparse matched subset of that Cartesian product,
and their known cardinality `K` is already stronger.  If instead one uses
the full residual intervals, their length is `qD=D^(49/16)` and the bound is
vastly larger.  Applying (4.6) fibre by fibre still sums over `N_col` fibres
and cannot produce (1.3).

Hence the generic alternative is either formally unavailable at the
ambient product level or numerically weaker after the two invariants are
combined.  A theorem exploiting the simultaneous additive--multiplicative
structure **and** the common-carrier mask could be relevant, but it would be
a new result rather than an ordinary Elekes--Szabo application.  Eliminating
one residual makes (4.2) fractional-linear in another; the family remains a
rational foliation rather than a transverse family of unrelated surfaces.

## 5. Ruling removal and parabolic peeling do not fix the algebraic class

Pair uniqueness removes repeated points on either ruling of (2.7), but a
split quadric admits large partial matchings between its two ruling
families.  The Farey construction already recorded in the weighted-secant
report gives `asymp B` rank-one integral matrices in a `B`-box on the exact
nonzero level

```text
p12-p21=-1,                                       (5.1)
```

with every pairwise secant invertible.  Its anchored version distributes
`B^(1-o(1))` points over `B^(1-o(1))` different four-point volume planes,
each fixed volume plane containing only divisor-many points.  Hence the
varying-plane union problem is sharp in the integer/algebraic category.

For completeness, there is also an elementary obstruction which avoids
every affine two-plane packet, not just the ruling lines.

### Lemma 5.1 (a ruling-free broad twisted cubic on one fibre)

Let

```text
K_C=((c11,-c12),(-c21,c22)),       k=det K_C!=0,
A>T^2.                                             (5.2)
```

For `1<=t<=T`, put

```text
u_t=(1,t),
y_t=(A-t^2,t),
v_t=adj(K_C)*y_t,
P_t=u_t*v_t^T.                                    (5.3)
```

Then

```text
det P_t=0,                 <C,P_t>=k*A,            (5.4)

det(P_s-P_t)=-k*(t-s)^2*(A+s*t) !=0               (5.5)
```

for `s!=t`.  If the colours are positive, `u_t,v_t` are positive because

```text
adj(K_C)=((c22,c12),(c21,c11)).                    (5.6)
```

Moreover any four distinct `P_t` are affinely independent.  Thus every
affine two-plane contains at most three members of the family.

**Proof.**  Since `K_C*adj(K_C)=kI`,

```text
u_t^T*K_C*v_t
 =k*u_t dot y_t=k*(A-t^2+t^2)=kA.                 (5.7)
```

For rank-one two-by-two matrices,

```text
det(uv^T-u'v'^T)=-det(u,u')*det(v,v').            (5.8)
```

Here

```text
det(u_s,u_t)=t-s,
det(y_s,y_t)=(t-s)*(A+s*t),
det(adj K_C)=k,                                   (5.9)
```

which proves (5.5).  Expanding `P_t` in `1,t,t^2,t^3`, the three nonconstant
coefficient vectors are independent: the determinant of the two top
coefficient pairs is `k`.  Vandermonde then gives affine rank three for any
four distinct parameters.  A two-plane meets this nondegenerate twisted
cubic in at most three points.  QED

For example,

```text
C=(64,71;73,81),                 det C=1,          (5.10)
```

has four distinct pairwise-coprime prime powers in a ratio-`<2` interval,
and Lemma 5.1 is completely integral and positive.  It is not an actual QP
family: its carrier sizes and residuals have not been placed in the project
shell/window.  Its exact conclusion is that bounded degree, smoothness,
invertible secants, and removal of all rich affine two-planes still permit
arbitrarily long fibres.  The Farey construction supplies the complementary
box-scale saturation.  Any successful theorem must use the actual mask
beyond those algebraic hypotheses.

### Corollary 5.2 (degree-only incidence no-go)

For arbitrary positive integers `N,T`, there are `N` pairwise disjoint
smooth integral surfaces of the form (2.7), with `T` positive integral
points selected on each, such that within each surface every selected
secant is invertible and every affine two-plane contains at most three
selected points.  The point--surface incidence count is exactly `N*T`.

**Proof.**  Keep the colour (5.10), for which `k=1`, and choose `N` distinct
integers `A_i>T^2`.  The levels `<C,P>=A_i` are disjoint.  Apply Lemma 5.1
with `t=1,...,T` on every level.  QED

Taking formally `N=D^(73/16)` and `T=D^(5/16)` reproduces the exponent
`D^(78/16)` while satisfying all of the stated bounded-degree and broad
secant hypotheses.  The construction does not satisfy the common physical
shell; its purpose is the exact logical one: no theorem whose hypotheses
stop at algebraic degree, smoothness, ruling removal, and plane-packet
removal can imply the needed `D^(76/16)`.

## 6. Determinant-method ledger

For one fixed colour, slicing (2.7) by the third reduced-lattice coordinate
gives a binary conic.  The established norm-equation argument costs
`q^o(1)` per nonparabolic slice, and there are at most

```text
K=D^(5/16)                                         (6.1)
```

slices.  This is already the natural determinant-method scale for a
nonsingular ternary quadric.  Sections 4--5 show why it cannot be improved
uniformly from algebraic degree: the surface is split, the ambient equations
have group form, and ruling-free broad sets can occupy linearly many slices.

Applying this fibrewise to all colours gives exactly

```text
N_col*K=D^(78/16).                                (6.2)
```

A determinant method does not couple the coefficients of different fibres.
Their union is the level-set foliation (2.5), so a common low-degree
auxiliary polynomial either cuts the fibres separately and retains the
linear point term, or contains a parameter subfamily of the foliation and
leaves that subfamily untreated.  The required `D^(1/8)` is therefore not a
missing optimization of the standard fibrewise determinant method.

## 7. The genuinely new incidence statement

The preceding argument does not say that the sharp estimate is false.  It
identifies the additional theorem it would require.  In one equivalent
form, after selecting one endpoint in every occupied broad slice, prove

```text
# {physical masked endpoints in high-J fibres}
   <<D*M^2*q^o(1),                                 (7.1)
```

using simultaneously

```text
r_ij=8*a_i*b_j*c_ij-Q,
a_i,b_j,c_ij actual prime powers,
the common row/column carriers across all four cells,                (7.2)
```

and after subtracting the certified affine/Hankel packets.  Equivalently,
one needs an `L^1`/energy theorem saying that no more than
`M*q^o(1)` fixed-plane labels can be simultaneously saturated at the
fixed-plane mass from the rank-two prime chart.

This is a distribution theorem for multiplication-table residuals among
the additive--multiplicative fibres (2.5).  Ordinary polynomial partitioning
does not see (7.2), the Elekes--Szabo alternatives are either exceptional
or weaker than the sparse matching as in Section 4, and the determinant
method is already sharp fibrewise.  A mask-sensitive arithmetic
partition or inverse theorem might still prove (7.1), but that would be the
new `D^(1/8)` input rather than a consequence of existing incidence
machinery.

```text
exact residual additive--multiplicative fibration:       PROVED;
colour multiplicity per fibre parameter O(1):            PROVED;
physical product endpoint determines colour:             PROVED;
ordinary point--surface partition saves D^(1/8):         NO (linear term);
ordinary Elekes--Szabo alternative saves D^(1/8):        NO (Section 4);
fibrewise determinant method improves the K slice cap:    NO;
ruling-free, no-rich-plane algebraic fibre family:        PROVED;
faithful actual-prime/product-window counterexample:      NOT OBTAINED;
mask-sensitive simultaneous-fibre theorem (7.1):         OPEN;
sharp four-cycle theorem from this route:                 NOT PROVED.
```

Finite replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_balanced_broad_algebraic_incidence.py \
  src/test_qp_balanced_broad_rank_two_chart.py
```

For the theorem-class terminology, see Raz--Sharir--de Zeeuw,
[*The Elekes--Szabo Theorem in four dimensions*](https://arxiv.org/abs/1607.03600)
and
[*Polynomials vanishing on Cartesian products: The Elekes--Szabo theorem
revisited*](https://arxiv.org/abs/1504.05012).  The theorem-class mismatch is
checked directly in Section 4; no black-box incidence theorem is invoked.
