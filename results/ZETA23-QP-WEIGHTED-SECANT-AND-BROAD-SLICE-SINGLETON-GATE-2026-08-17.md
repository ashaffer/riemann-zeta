# QP four-cycle: weighted secant and broad-slice singleton gate

**Date:** 2026-08-17  
**Verdict:** the full weighted off-diagonal estimate

```text
P(z)=sum_C m(C)(m(C)-1) w_z(C)
    <<D q^o(1) ||z||_2^4                              (0.1)
```

remains open.  It has an exact factorial-codegree matrix formulation and
three rigorous pair-flattening upper bounds.  Two restricted-type endpoints
are now exact: fixing a nonzero secant and the color determinant gives a
partial matching of color pairs, while fixing two independent color
relations gives an `O(1)` weighted color mass.  A third exact endpoint says
that fixing the two carrier secant determinants gives weighted mass `O(D)`,
but summing those determinant layers gives no exponent saving.  Actual-prime-power scans find
no counterexample; in the generic all-eight-distinct sector the finite
off-diagonal form is zero through `q=50021` at cutoff `U=12`, and is tiny in
the next two scans.  The exact restricted ternary polar discriminant is
`2 det C`, while the projective completion quadric has discriminant `L^2`
and is split.  A Farey matching saturates the raw slice count without any
rank-one secant, so these discriminants alone give no broad-sector saving.
Actual-node coprimality and product-window rigidity exclude that Farey
matching and the exact translation-grid, multilevel tangent, and
critical-covolume lower models; genuinely perturbed actual models remain
open.

For the direct completed form, the exact remaining weighted route is now a
restricted-type estimate for the binary common-carrier incidence between
row pairs and color pairs.  Its `sqrt(D)` cut bound implies FC by finite
Lorentz interpolation, permits degree-`D` stars, and avoids the false
unweighted maximum-anchor-load surrogate.  An exact slope-bin reduction now
shows that it is enough to prove `O(D q^o(1))` edges in each angular block of
width `D/q^2`; the estimate is already proved for cuts whose local block
occupancies have product at most `D`, and for projectively sparse supports.
A primitive full-integer tangent block has `asymp D` edges in one block, so
the proposed local cap is sharp.  A nonempty relevant strip may legally be
enlarged to all integer points and still has `O(D)` vertices, but coherent
low tangent modes force a `sqrt(D)` loss in every generic second-moment
closure.  The remaining analytic statement is an `L^1` cancellation across
scattered Farey fans.  Exact actual-prime factorization now closes every
slope-block sector for which either corner residual projection has
`O(Dq^o(1))` levels: one residual has at most six incident block edges, and
an ordered residual pair recovers the carrier by a gcd.  A legal ten-edge
prime block at `q=25013` shows that the resulting unit anchor resultant can
still be projectively dense and that short-carrier tangent extraction is not
exhaustive.  Thus the cap itself, cross-direction merger, and the sector with
two large residual projections remain open.

There is now a sharp pointwise inverse theorem for two fixed row vertices.
Their actual common-neighbor count is `O(sqrt(D)q^o(1))`.  In the generic
short-lattice branch its factorial energy is already `O(Dq^o(1))`; in the
exceptional branch every power-sized common-neighbor family has a
`q^(-o(1))` portion in one parabolic rational tangent/Hankel chart.  This is
an energy-or-tangent dichotomy, not a proof that every near-sharp generic
codegree is tangent.  It does not aggregate over row pairs and therefore
does not prove `(SB)`, `(RT)`, the weighted secant theorem, or FC.

There is now also a proved stability theorem for one opposite-fan
polynomial arc.  A genuinely quadratic carrier has a fourth-degree
sublevel cap, while a linear carrier has the sharp strict-log-concavity
tangent cap.  Exact quartic resonance cannot embed two actual prime-power
fans in the project shell.  These estimates would prove `(SB)` if a new
uniform approximate-determinant theorem covered each reduced fan pair by
`q^o(1)` such polynomial packets; that covering theorem is not proved.
The direct four-point determinant cell decomposition falls short of its
random-volume remainder by exactly `q^(1/66)`.  In the explicit high-step
quartic model the central arc has no legal positive parallel copy, but this
model-specific uniqueness does not provide the missing covering theorem.
An overlap-free separable-weight version closes the entire isolated-cell
class when `R*S<=q/D^2`; for bounded steps it is `D^(31/32+o(1))`.  Above
that cutoff it supplies three-point cell nonconcentration but no `O(D)`
count, and coplanar rich cells are not automatically polynomial arcs.
Enlarging the high-step cells and sorting by their nonzero integral plane
index does not repair the gap: square-root summation is scale-invariant at
`D^2*R/sqrt(q)`, and the plane projector reintroduces the coupled carrier.

The proposed broad estimate

```text
sum_(completed broad C) K_C w_z(C)<<D q^o(1),
K_C=1+D/lambda3(C),                                  (0.2)
```

is strictly stronger than the secant problem for a structural reason:
`K_C` counts every geometrically available slice even when only one slice
is occupied.  In the first three actual generic scans, every broad completed
color is a singleton.  Thus (0.2) is dominated there by colors making zero
contribution to (0.1).  This does not refute (0.2), but it rules out deriving
it from a nonzero-secant theorem without a separate singleton argument.

The minimal singleton-safe `K` substitute is

```text
sum_(completed broad C) K_C (m(C)-1) w_z(C)
    <<D q^o(1)||z||_2^4.                            (0.3)
```

Since the proved broad slice theorem gives `m(C)<<K_C q^o(1)`, (0.3)
implies the broad part of (0.1).  Neither (0.1), (0.2), nor (0.3) is proved
here.  No full four-cycle, QP, or strip claim is made.

---

## 1. Exact positive quartic

After the proved repeated-coordinate deletion, let `C` run over oriented
color matrices with four distinct colors and all eight displayed rectangle
nodes distinct.  Put

```text
w_z(C)=|z_c11 z_c12 z_c21 z_c22|,
a(C)=m(C)(m(C)-1).                                  (1.1)
```

The missing estimate is the positive quartic

```text
P(z)=sum_C a(C) w_z(C).                             (1.2)
```

This is the ordered off-diagonal energy: the diagonal pair is absent, and
a singleton color matrix contributes exactly zero.  The already proved
fixed-`(C,E)` conic theorem rewrites

```text
a(C)=sum_(E!=0) nu(C,E),             nu(C,E)<<q^o(1), (1.3)
```

so (1.2) is, up to `q^o(1)`, precisely the weighted mass of distinct
realized secants.  The remaining issue is aggregation over `E`, not
multiplicity at a fixed secant.

---

## 2. Three exact pair flattenings

For any partition of the four color positions into ordered pairs

```text
(i,j) | (k,l),                                      (2.1)
```

define the nonnegative matrix

```text
A^pi_((c_i,c_j),(c_k,c_l))
 =sum_(C in that cell) a(C).                        (2.2)
```

Put

```text
u_(x,y)=|z_x z_y|.                                  (2.3)
```

Then, exactly,

```text
P(z)=<u,A^pi u>,                  ||u||_2=||z||_2^2. (2.4)
```

The two copies of `u` may be restricted to different ordered-pair supports;
their norms only decrease.  Consequently

```text
P(z)<=||A^pi||_(2->2)||z||_2^4
    <=sqrt(R_pi*C_pi)||z||_2^4,                    (2.5)
```

where `R_pi` and `C_pi` are the maximum row and column sums of (2.2).
Taking the minimum over the row, column, and diagonal pairings gives a
rigorous finite certificate and an exact sufficient arithmetic theorem.

For the column pairing

```text
gamma=(c11,c21),              gamma'=(c12,c22),    (2.6)
```

let `B` be the unweighted row-pair/color-pair incidence matrix from the
simultaneous-divisor spectral reduction.  Pair uniqueness gives

```text
m(C)=(B^*B)_(gamma,gamma')                         (2.7)
```

with the fixed rectangle orientation understood.  Hence (2.2) is the
factorial-codegree kernel

```text
A_col(gamma,gamma')
 =(B^*B)_(gamma,gamma')*((B^*B)_(gamma,gamma')-1). (2.8)
```

Thus (0.1) is a rank-one-input estimate for an explicit common-neighbor
kernel.  A uniform `O(Dq^o(1))` operator bound for any one flattening would
prove it, but that stronger operator theorem is not established.

---

## 2A. Two restricted-type partial-matching endpoints

Write

```text
L_E(C)=e11*c11+e22*c22-e12*c12-e21*c21.            (2A.1)
```

### Fixed secant and fixed color determinant

Fix an invertible integral secant `E` with
`||E||_infinity<min(S)` and a nonzero integer `k`.  Let `G_(E,k)` be the
incidence matrix from the top color pair `(c11,c12)` to the bottom pair
`(c21,c22)` cut out by

```text
L_E(C)=0,                    det C=k.               (2A.2)
```

After the top pair is fixed, (2A.2) is a two-by-two linear system in the
bottom pair.  Its determinant is

```text
e22*c12-e21*c11.                                  (2A.3)
```

This cannot vanish on an all-distinct actual-shell tuple.  Indeed, adjacent
colors are coprime, so (2A.3) equal to zero and
`|e21|,|e22|<min(S)` force `e21=e22=0`, contrary to `det E!=0`.
Thus every row of `G_(E,k)` has degree at most one.  Fixing the bottom pair
instead gives determinant

```text
e12*c22-e11*c21,                                  (2A.4)
```

and the same argument gives column degree at most one.  Consequently, for
`u_(x,y)=|z_xz_y|`,

```text
sum_(det C=k, L_E(C)=0) w_z(C)
 =<u,G_(E,k)u>
 <=||z||_2^4.                                     (2A.5)
```

This includes zero-entry secants and uses no pivot division.  Summing the
`O(D)` possible nonzero `k` gives the useful fixed-secant cap

```text
sum_(0<|det C|<<D, L_E(C)=0) w_z(C)
 <<D q^o(1)||z||_2^4.                              (2A.6)
```

It improves the earlier fixed-relation estimate when the normalized
determinant of `E` is large, but summing (2A.6) over all realized `E` is
still unaffordable.

The pivot identity

```text
(e22*c12-e21*c11)(e22*c21-e12*c11)
 =-det(E)*c11^2-e22^2*k                            (2A.7)
```

is consistent with (2A.3), but (2A.5), rather than a chosen nonzero pivot,
is the zero-safe formulation.

### Two fixed independent relations

Fix independent integral relations `E,F` and put

```text
V={C in Q^4:L_E(C)=L_F(C)=0}.                      (2A.8)
```

If some partition of the four coordinate positions into pairs `I|J` has
both projections `V->Q^I` and `V->Q^J` injective, the color tuples form a
partial matching between the two ordered-pair spaces.  Cauchy--Schwarz then
gives, for every subset `A` of actual-shell tuples in `V`,

```text
sum_(C in A) w_z(C)<=||z||_2^4.                   (2A.9)
```

If no such partition exists, the rank-two coordinate matroid has a parallel
class of size three.  Those three color coordinates have fixed rational
ratios on `V`.  Pairwise coprimality fixes their common integral scale, and
the fourth coordinate changes `det C` in steps of at least `min(S)`.
Therefore an active determinant interval of width below `min(S)` contains
at most one such tuple, so (2A.9) still holds up to an absolute constant.

Thus two fixed independent color relations have `O(1)` weighted mass.  This
is the exact restricted-type endpoint suggested by a high-`K_C` color,
which has a second short relation beyond a realized transverse secant.  It
does not yet solve the gate: the canonical second relation varies with `C`,
and a raw union over all short relation planes loses polynomially.

## 2B. Fixed row and column secant determinants cost `D`

For two ordered completions write

```text
A=det((a1,a2),(a1',a2')),
B=det((b1,b2),(b1',b2')).                           (2B.1)
```

Both are nonzero and `|A|+|B|<<D` in the generic sector.  Fix their signed
values.  For top and bottom ordered color pairs `p,q`, let
`N_(A,B)(p,q)` count the ordered completion pairs with common color matrix
`(p;q)` and secant determinants `(A,B)`.

Every row sum of this matrix is `O(Dq^o(1))`.  Indeed, fix
`p=(c11,c12)` and use the endpoint-pair set `W_p` from the direct
top/bottom projection.  It has

```text
|W_p|<<Dq^o(1).                                     (2B.2)
```

Choose the first ordered column pair `v=(b1,b2)` in `W_p`.  Distinct actual
prime powers in the narrow shell are coprime, and the shell diameter is
smaller than its minimum.  Therefore

```text
det(v,v')=B                                         (2B.3)
```

has at most one second shell pair `v'`: two solutions differ by an integral
multiple of the primitive vector `v`, too large to remain in the shell.
Pair uniqueness then fixes the two top centers `a1,a1'`.  The same argument
applied to

```text
a1*a2'-a2*a1'=A                                    (2B.4)
```

fixes at most one bottom pair `(a2,a2')`.  The bottom colors are now forced,
if they exist.  Thus (2B.2) bounds the row sum.  Fixing `q` and reversing
top and bottom proves the same column-sum bound.  Schur's test, with
`u_(x,y)=|z_xz_y|`, proves the exact fixed-layer theorem

```text
sum_C nu_(A,B)(C) w_z(C)
 =<u,N_(A,B)u>
 <<Dq^o(1)||z||_2^4.                               (2B.5)
```

The factor cannot be replaced by `O(1)` using product-window geometry and
matching alone.  In the all-distinct full-integer translation grid, compare
the parameters `t` and `t+h`.  With row and column steps
`R*ell_r,R*ell_c`, respectively,

```text
A=-R*ell_r*h,             B=R*ell_c*h,             (2B.6)
```

independently of `t`.  Taking `h=1` gives `Theta(sqrt(D))` ordered pairs of
one fixed four-distinct color matrix in a single `(A,B)` layer.  Flat weight
`1/2` on its four colors makes (2B.5)'s left side
`Theta(sqrt(D))`.  This is not an actual-prime-power counterexample, but it
is a legal all-distinct integer product-window obstruction to an `O(1)`
matching argument.

There is no exponent gain from summing (2B.5).  The proved shortness is

```text
|A|<<D,        |B|<<D,        det(E)=-A*B,          (2B.7)
```

not `|A*B|<<D`.  Hence there are `O(D^2)` signed pairs; grouping by
`n=A*B` merely replaces them by
`sum_(|n|<<D^2) tau(|n|)=D^(2+o(1))` layers.  Even an `O(1)` theorem for
each layer would therefore be weaker than `D^(21/16)`.  The actual broad
fixture (4.1) already has

```text
(A,B)=(1440,5320),       |A*B|=7,660,800>>D=15,509.94, (2B.8)
```

so the stronger product cutoff is not a legal actual-node premise.  A gain
must be an orthogonal or square-function sum across `(A,B)`, not a union of
the fixed-layer estimates (2B.5).

---

## 2C. Exact ternary discriminant gives no broad-slice saving

Let `H` be the integral polar matrix of the determinant in row-major
coordinates:

```text
det X=(1/2) X^T H X,
H=(0 0 0 1; 0 0 -1 0; 0 -1 0 0; 1 0 0 0).       (2C.1)
```

Thus `H^2=I` and `det H=1`.  Put

```text
w=(c11,-c12,-c21,c22),       k=det C,
Lambda_C={E in Z^4:w dot E=0}.                    (2C.2)
```

In the all-distinct actual sector `w` is primitive.  If the columns of
`U` are any saturated integral basis of `Lambda_C`, then

```text
det(U^T H U)=2k.                                  (2C.3)
```

Indeed choose `v in Z^4` with `w dot v=1`.  The matrix `[U v]` is
unimodular.  The lower-right entry of the inverse of
`[U v]^T H[U v]` is both the corresponding cofactor
`det(U^T H U)` and

```text
w^T H^(-1)w=2(c11*c22-c12*c21)=2k.                (2C.4)
```

This is the exact integral discriminant, with no hidden covolume factor.
In an orthonormal basis of `w^perp` the determinant is instead

```text
2k/||w||^2.                                       (2C.5)
```

Multiplication by
`covol(Lambda_C)^2=||w||^2` gives (2C.3): the apparent `q` curvature
cancels.  Since `0<|k|<<D`, the restricted ternary discriminant can be only
`O(D)`, despite `covol(Lambda_C)asymp q`.

There is an equally rigid affine identity.  Let `P0` be one rank-one
completion product matrix and put `L=w dot P0`; active residual pinning has
`L!=0`.  The homogenized completion quadric is

```text
det(U*n+t*P0)=0.                                  (2C.6)
```

Because `det[U P0]=+-L`, its polar determinant is exactly

```text
det([U P0]^T H[U P0])=L^2.                        (2C.7)
```

Over `Q`, (2C.6) is therefore the split determinant surface under the
invertible map `(n,t)->U*n+t*P0`.  Its two rational rulings are intrinsic;
excluding `det(P-P')=0` says only that the selected points form a partial
matching between the rulings.

That matching condition does not give a sublinear integral-point theorem.
Take alternate consecutive positive fractions in the Farey sequence of
order `R`:

```text
a/c < b/d,                   b*c-a*d=1,
P=(a,c)^T(b,d).                                    (2C.8)
```

There are `asymp R^2` retained matrices, all in an `O(R^2)` box, with

```text
det P=0,                    P12-P21=a*d-c*b=-1.     (2C.9)
```

No two retained matrices share either projective factor, so

```text
det(P-P')=-det((a,c),(a',c'))*det((b,d),(b',d'))
            !=0.                                  (2C.10)
```

Thus a split integral quadric can contain `asymp B` ruling-free points in a
`B`-box, exactly saturating a `1+B` slice count.  This blocks a uniform
theorem using only ternary discriminant and rank-one-secant exclusion.  It
is **not** an actual-prime-power or active product-window counterexample,
so an arithmetic occupied-slice theorem remains possible.

The direct-FC refinement does not alter this verdict.  Colors with
`m(C)<=2` cost at most twice the determinant-layer mass and are already
`O(Dq^o(1))`.  If `m(C)>=3`, three completion products are automatically
noncollinear: otherwise a determinant polynomial on their line has three
zeros and vanishes identically, forcing a rank-one secant.  Their plane
section is nondegenerate for the same reason, but need not be parabolic.
For example on `det P=0, tr P=1`,

```text
P1=(1 0;0 0),  P2=(0 0;0 1),  P3=(2 -1;2 -1)     (2C.11)
```

have three invertible pairwise secants.  Their plane is `z+2y=0`, and its
conic is

```text
x-x^2+2y^2=0,                                     (2C.12)
```

whose quadratic discriminant is `8`, not zero.  The two independent
secants give two fixed color relations, so the proved two-relation `O(1)`
theorem applies after that plane is fixed.  The plane varies with the
triple, however, and no bounded-overlap count of these second-relation
planes follows from (2C.3)--(2C.10).

Consequently elementary divisor/Pell counting remains `q^o(1)` only on a
fixed nonparabolic binary slice.  Pila's plane-conic estimate is weaker on
that slice, and summing either estimate over the
`1+D/lambda3(C)` possible slices restores the existing factor.  The exact
ternary discriminants provide no pointwise or weighted improvement of the
broad sector.

## 2D. Actual-node admission rejects the four audited lower-bound models

This subsection concerns actual arithmetic, not a geometry-only surrogate.
Let `S_q` be the prime powers in the project shell.  Since its endpoint
ratio is `e^(2w)<2`, distinct elements of `S_q` have distinct prime bases
and are pairwise coprime.  The shell contains at most one even node.

The logarithmic product window also has the following exact rigidity.  If
two shell nodes `x,z` are fixed, the allowed interval for the third node is

```text
q^3/(8*x*z)*[exp(-U/B),exp(U/B)],
```

whose length is

```text
<<U*q/B=D/q=o(1).                                 (2D.1)
```

Thus two nodes determine the third for all sufficiently large `q`.  In
particular, a composite color in an exact integer model cannot be replaced
by a neighboring prime power while its two carriers are retained.

### Farey/split-quadric matching

Fix an actual color matrix `C`.  An all-distinct completion with

```text
a1*b2-a2*b1 odd                                   (2D.2)
```

must contain the shell's unique even node in exactly one of its four
carrier positions.  Once that position and `C` are fixed, three corners
successively determine the other three carriers by (2D.1).  Hence

```text
#{completions of C satisfying (2D.2)}<=4.          (2D.3)
```

If the shell has no power of two, the count is zero.  The Farey replay in
Section 2C has determinant `+-1`, so its `asymp R^2` fixed-level matching
cannot embed on actual nodes.  This is stronger than merely losing a power:
the actual fixed-color multiplicity of that model is bounded absolutely.

### Exact rational-slope translation grids

The asymmetric exact grid has colors

```text
c00=S*n,       c01=S*(n-ell_c),
c10=S*(n-ell_r), c11=S*(n-ell_r-ell_c).            (2D.4)
```

Actual-shell coprimality forces `S=1`.  Its row and column base is `R*n`:
the two displayed nodes `R*n+t,R*n-t` and the color `n` lie in the same
shell.  Therefore

```text
R=((R*n+t)+(R*n-t))/(2*n)<=exp(2w)<2.              (2D.5)
```

Thus `R=1`, contradicting the construction's `R>S=1`.  The symmetric and
four-distinct exact translation grids are both excluded.  Equation (2D.1)
also rules out repairing their composite colors by unit perturbations while
keeping the grid carriers.

### Equal-base multilevel tangent orbit

The multilevel `D^(5/4)` obstruction is centered at an integer `m`; its
top-left cell has

```text
(a,b,c)=(m+t,m-t,m),            t^2=O(D).          (2D.6)
```

All its internal residuals from `(2m)^3` are `O(qD)`.  But the project
modulus is an odd prime and `2*m asymp q`, so

```text
|q^3-(2m)^3|
 =|q-2m|*(q^2+2*m*q+4*m^2)
 >>q^2.                                             (2D.7)
```

Since `D=o(q)`, (2D.7) is larger than both the internal error and the legal
`O(qD)` window.  No member of the exact multilevel orbit survives at the
active scale.

### Critical-covolume witness

For that exact integer family put

```text
A=N^2+1,
X=A*(2*N^29)-1-N^13,             c11=A*X.          (2D.8)
```

Modulo `A`, `N^13=N*(N^2)^6` is congruent to `N`, and hence

```text
gcd(A,X)=gcd(N^2+1,N^13+1)
        =gcd(N^2+1,N+1)=gcd(N+1,2).                (2D.9)
```

If `N` is even, the two factors in (2D.8) are coprime and greater than one,
so their product is not a prime power.  If `N` is odd and the product were
a prime power, (2D.9) would force that prime to be `2` and `A` to be a
power of two.  But `A=N^2+1` is `2 mod 8` and greater than `2`.  Thus this
witness also contains a color that is never a prime power.

The binary admission verdict is therefore:

```text
legal actual family with Q_nd>=D^(1+eta):          NOT OBTAINED;
Farey fixed-level matching on actual nodes:        IMPOSSIBLE;
exact rational-slope translation grid:             IMPOSSIBLE;
equal-base multilevel D^(5/4) orbit:                IMPOSSIBLE;
critical-covolume integer witness:                  IMPOSSIBLE;
all perturbed/recentered actual configurations:     OPEN.        (2D.10)
```

This is a proved non-embedding theorem for the four explicit power-scale
parametrizations audited above.  It is not a proof of the full
actual four-cycle upper bound: a new near-tangent prime configuration that
does not preserve these exact parametrizations is not excluded.

---

## 2E. Weighted restricted-type common-carrier gate

There is a direct sufficient theorem which retains color dispersion.  Put

```text
S(z)=sum_C m(C) w_z(C).                              (2E.1)
```

The tempting one-color reduction is exact but too strong.  If

```text
L(c)=sum_C m(C)*#{positions of c in C},             (2E.2)
```

then AM--GM gives

```text
S(z)<=1/4*sum_c L(c)|z_c|^4
    <=1/4*max_c L(c)*||z||_2^4.                     (2E.3)
```

Thus `max_c L(c)<<Dq^o(1)` would prove the direct FC bound.  It is not the
right arithmetic target.  The full-integer multilevel tangent patch has

```text
L(m)=L*(L+1)^2 asymp D^(3/2),                       (2E.4)
```

although its merged affine/Hankel fourth trace is `O(D)`.  Even deleting
rich patches does not make (2E.3) a combinatorial consequence.  Take `D`
anchor edges `(r_i,b_i,c)`; for each `j<D` add fresh `s_ij,t_ij` and the
other three edges of the rectangle, using fresh nonanchor colors.  This is
pair-unique, has maximum degree `D` and common-row degree two, but

```text
L(c)=D*(D-1).                                       (2E.5)
```

The common-carrier incidence operator of this example is a disjoint union
of two-edge stars and has norm `sqrt(2)`.  Equation (2E.3) loses precisely
this dispersion among the fresh colors.

The operator formulation preserves it.  Let `alpha=(a1,a2)` be an ordered
row pair and `gamma=(c1,c2)` an ordered color pair.  Define the binary
matrix

```text
B_(alpha,gamma)=1
```

when there is a common carrier `b` with active triples
`(a1,b,c1),(a2,b,c2)`.  Pair uniqueness makes `b` unique.  For the two
vertical color pairs

```text
gamma_1=(c11,c21),       gamma_2=(c12,c22),
```

one has the exact Gram identity

```text
m(C)=(B^*B)_(gamma_1,gamma_2).                     (2E.6)
```

Put `u_(x,y)=|z_x z_y|`, so `||u||_2=||z||_2^2`.  Positivity and (2E.6)
give

```text
S(z)<=<u,B^*B u><=||B||_(2->2)^2 ||z||_2^4.        (2E.7)
```

This also gives an exact fixed-color-pair endpoint.  With `M=B^*B`, either

```text
max_gamma sum_(gamma') M_(gamma,gamma')<<Dq^o(1)   (2E.7a)
```

or the weaker restricted color-pair theorem

```text
sum_(gamma in P,gamma' in Q) M_(gamma,gamma')
 <<D*sqrt(|P|*|Q|)q^o(1)                           (2E.7b)
```

for all `P,Q` proves the direct bound, by Schur in the first case and finite
Lorentz interpolation in the second.  These statements count completed
rectangles through a fixed vertical color pair or through two coefficient
level sets; they are materially different from the single-color load
(2E.2).

Consequently the following restricted-type incidence theorem is sufficient
for FC:

```text
I(X,Y):=sum_(alpha in X,gamma in Y) B_(alpha,gamma)
 <<sqrt(D)*sqrt(|X|*|Y|) q^o(1)                    (RT)
```

for every set `X` of ordered row pairs and every set `Y` of ordered color
pairs.  Indeed dyadic layer cake, equivalently finite
`ell^(2,1) x ell^(2,1)` interpolation, turns `(RT)` into

```text
||B||_(2->2)<<sqrt(D)*log(q)q^o(1)=sqrt(D)q^o(1).  (2E.8)
```

This formulation permits a degree-`D` star sharply: take its center on one
side and its `D` leaves on the other in `(RT)`.  The already proved singleton
row/column degree estimates therefore do not suffice.  One needs either the
uniform Gram-row theorem (2E.7a) or a joint restricted estimate such as
(2E.7b) or `(RT)` for arbitrary coefficient level sets.

Some ranges of `(RT)` are already elementary.  If `N` is the number of
shell nodes, the proved degree and total-edge bounds give

```text
I(X,Y)<<min(D|X|,D|Y|,N D^2)q^o(1).                (2E.9)
```

Hence `(RT)` is automatic when `|X|/|Y|` lies outside `[1/D,D]`, or when
`|X||Y|>>N^2 D^3`.  Its genuine content is the balanced intermediate-size
core.

Every edge in that core obeys the exact actual-node system

```text
|8*a1*b*c1-q^3|, |8*a2*b*c2-q^3| <<qD,
v=a2*c2-a1*c1,                    0<|v|<<D.         (2E.10)
```

For one fixed row pair with odd second row, put
`n=b*c1`, `rho=8*a1*n-q^3 (mod a2)`.  Then

```text
b*v ==-(q^3+rho)/8 ==-a1*n (mod a2).               (2E.11)
```

Because `D<a2` and `8a1` is a unit modulo `a2`, the map from the
`O(D)`-long product interval for `n` to `rho`, and hence to the inversion
multiplier in (2E.11), is injective.  A `sqrt(D)` product block already has
`sqrt(D)` distinct modular-hyperbola right sides.  Fixed-multiplier
small-box counting therefore does not prove `(RT)`; it merely gives `O(1)`
actual occupancy on each of `O(D)` varying layers.

There is also an exact local classification.  If three common carriers lie
in an interval of length `L<<sqrt(D)`, write
`b1=b2-u<b2<b3=b2+v` and `c_i=N_1/b_i+e_i`, with
`|e_i|<<D/q`.  The integer second determinant satisfies

```text
|u*c3+v*c1-(u+v)*c2|
 <<L^3/q+D*L/q<<D^(3/2)/q=o(1).                    (2E.12)
```

It vanishes, and the same holds for the second colors: every rich short
block is an exact simultaneous affine/tangent patch.  This is only a
classification.  The existing merger closes one certified affine plane or
one fixed primitive direction; it does not sum cross terms over all varying
directions.  Lines with only one or two occupied points also evade the
tangent invariant.

### Exact slope-bin reduction and a proved partial range

There is a more local formulation of the residual cut.  For a left pair
and a right pair put

```text
r(alpha)=a1/a2,                 s(gamma)=c2/c1.
```

On an incidence edge, (2E.10) gives exactly

```text
|r(alpha)-s(gamma)|
 =|a1*c1-a2*c2|/(a2*c1)<<D/q^2.                    (2E.13)
```

Partition the fixed ratio range into intervals of length `delta=C D/q^2`,
with `C` larger than the shell constant.  The block matrix of `B` is then
banded with an absolute number of neighboring blocks.  Write `E_ij` for the
number of all support edges in one such neighboring block pair.  The local
statement

```text
E_ij<<D q^o(1)                                      (SB)
```

implies `(RT)` immediately.  Indeed, for coefficient level sets with local
sizes `x_i,y_j`, simplicity and `(SB)` give

```text
e_ij<=min(x_i*y_j,D q^o(1))
    <=sqrt(D*x_i*y_j) q^o(1).                       (2E.14)
```

For each fixed block offset, Cauchy--Schwarz sums the last expression to
`sqrt(D)*sqrt(|X||Y|)q^o(1)`, and there are only `O(1)` offsets.

This proves a nonempty unconditional range of `(RT)`: the contribution of
all neighboring block pairs satisfying

```text
x_i*y_j<=D                                           (2E.15)
```

obeys the target.  Thus a counterexample to the slope-bin route must put
more than `D` pairs of coefficient vertices into at least one local block
product; the global balanced-intermediate condition (2E.9) alone does not
force this.

The blocks themselves have only `O(D)` vertices on either side.  Distinct
actual row pairs are primitive, and two reduced fractions with coordinates
`asymp q` differ by at least `cq^(-2)`.  An interval of length `D/q^2`
therefore contains `O(D)` of them.  This vertex count does **not** prove
`(SB)`: a simple bipartite graph on two `D`-element blocks may still have
`D^2` edges.

The Farey count can be sharpened to an exact short modular-lift
parametrization.  Fix a primitive reference row `r_0=(p,r)` in a nonempty
row block.  Every other primitive row `a=(a1,a2)` in that block has

```text
h=det(r_0,a)=p*a2-r*a1,                   |h|<<D,
a1==-inverse(r)*h (mod p),
a2=(r*a1+h)/p.                                      (2E.15a)
```

The shell interval has length less than its least node, hence less than
`p`.  It therefore contains at most one representative of the residue
class in (2E.15a): `h` determines the row completely, if it exists.  For a
primitive reference reciprocal-color vector `s_0=(u,v)` and
`s=(c2,c1)`, the same argument gives

```text
g=det(s_0,s)=u*c1-v*c2,                   |g|<<D,
c2==-inverse(v)*g (mod u),
c1=(v*c2+g)/u.                                      (2E.15b)
```

Finally `(a1,c1)` leave an interval of length `O(D/q)<1` for their common
carrier.  Thus `(SB)` is exactly the assertion that only `Dq^o(1)` of the
`O(D^2)` pairs `(h,g)` have an integer `b` passing both tests

```text
|8*b*a1(h)*c1(g)-q^3|,
|8*b*a2(h)*c2(g)-q^3| <<qD.                         (2E.15c)
```

This is an exact reduction, not an estimate: it is a two-short-modular-lift
reciprocal-rounding problem.  The random-scale ledger is favorable but not
a proof.  At `D=q^(16/33)`, there are `D^2` candidate lift pairs and the
unique carrier interval has relative hit density `D/q`, predicting

```text
D^2*(D/q)=D^3/q=D^(15/16),                          (2E.15d)
```

a factor `D^(1/16)` below the desired cap.  The tangent packet below shows
that arithmetic concentration can raise this to order `D`, so the random
ledger cannot replace a uniform theorem.

### Exact residual-factorization sector and a legal resultant obstruction

There is an actual-prime-power sector theorem that is invisible after the
Selberg majorization.  For an all-five-distinct block edge write

```text
rho_i=8*b*a_i*c_i-q^3,
M_i=(q^3+rho_i)/8=b*a_i*c_i,                 i=1,2. (2E.R1)
```

The five nodes have distinct prime bases.  Consequently

```text
gcd(a1*c1,a2*c2)=1,
b=gcd(M_1,M_2),
v=a2*c2-a1*c1=(rho_2-rho_1)/(8*b).                  (2E.R2)
```

These identities give a sharp bounded-fibre projection.  Fix `rho_1`.
Unique factorization determines the unordered triple of maximal prime-power
factors

```text
{a1,b,c1}.
```

There are at most `3!=6` assignments of those factors to the three roles.
For each assignment, injectivity of the two first-coordinate slope-block
projections fixes `a2` and `c2`.  Hence a fixed `rho_1` supports at most six
block edges.  The symmetric second-coordinate argument gives the same result
for `rho_2`.  If the ordered pair `(rho_1,rho_2)` is fixed, (2E.R2) first
recovers `b`; only the two assignments of the remaining factors to `a1,c1`
remain.  Thus, for every block-edge subset `F`,

```text
|F|<=6*min(|rho_1(F)|,|rho_2(F)|),
mult_(rho_1,rho_2)<=2.                              (2E.R3)
```

In particular `(SB)` is proved for every sector satisfying either

```text
|rho_1(F)|<<D*q^o(1)       or       |rho_2(F)|<<D*q^o(1). (2E.R4)
```

This permits arbitrary collisions and permutations inside the retained
residual levels.  The remaining gate is explicitly the sector in which
**both** residual projections are large; neither residual can then be used
as an `O(Dq^o(1))` index set.

The natural congruence resultant does not close that sector.  Choose one
actual anchor edge and put

```text
R=(p,r),       S=(u,v)=(c2,c1),       kappa=r*u-p*v. (2E.R5)
```

The four anchor coordinates are distinct prime powers, so

```text
0<|kappa|<<D,              gcd(kappa,p*r*u*v)=1.     (2E.R6)
```

For another row `A=(x,y)` and reciprocal color `Z=(z,w)=(c2,c1)`, define

```text
h=det(R,A),        alpha=det(S,A),
g=det(S,Z),        beta=det(R,Z).                    (2E.R7)
```

All four determinants are `O(D)`.  Direct elimination gives

```text
alpha=(kappa*x+u*h)/p,       beta=(p*g-kappa*z)/u,
A=(alpha*R-h*S)/kappa,       Z=(g*R-beta*S)/kappa,
kappa*(y*z-x*w)=h*g-alpha*beta.                     (2E.R8)
```

Thus actual coprimality makes `kappa` a unit at every anchor coordinate, but
the resulting determinant-coordinate incidence is still a short bilinear
strip.  It need not be sparse.  The following finite actual-shell fixture
is an exact obstruction to promoting (2E.R8) to a matching or to an
exhaustive short-carrier tangent classification.

At `q=25013`, cutoff `U=24`, take left vertices

```text
(10559,11443), (11443,12401),
(11897,12893), (13259,14369),                        (2E.R9)
```

and right pairs

```text
(11443,10559), (12401,11443),
(12893,11897), (14369,13259).                       (2E.R10)
```

Every displayed value and every carrier is prime and belongs to the project
shell.  All twelve off-diagonal incidences occur, with carrier array

```text
(*,14939,14369,12893)
(14939,*,13259,11897)
(14369,13259,*,11443)
(12893,11897,11443,*).                              (2E.R11)
```

Deleting the two incidences `(0,1)` and `(1,0)`, which repeat `11443` within
their five nodes, leaves ten all-five-distinct edges.  With

```text
B=(q/2)^(50/33),             D_0=q^2/B=387.748...,
```

their maximum normalized product error is `15.029<24`, every carrier
interval has length below `.428<1`, and the combined ratio span is

```text
4.573...*D_0/q^2.                                  (2E.R12)
```

Thus they lie in one legitimate `O(D/q^2)` neighboring block pair.  Their
five surviving carrier values have diameter `2926`, far beyond the short
tangent scale.

Anchor (2E.R8) at the edge from the first left vertex to the third right
vertex.  Then

```text
R=(10559,11443),       S=(11897,12893),       kappa=184,
(h,alpha)=
 (0,184), (-90,98), (-184,0), (-466,-294),
(g,beta)=
 (184,0), (98,-90), (0,-184), (-294,-466).         (2E.R13)
```

The color coordinate is exactly the swapped row coordinate.  All ten edges
satisfy

```text
184*v_ij=h_i*alpha_j-alpha_i*h_j.                   (2E.R14)
```

The corner residual projections nevertheless have only the same four
levels

```text
-145757173, -124606005, -97692069, -87297013,       (2E.R15)
```

with maximum fibre three, in agreement with (2E.R3).  Thus this fixture is
closed by the residual theorem and is not a counterexample to `(SB)`.  Its
role is exact and narrower: prime-power coprimality, unit anchor resultants,
and short determinant coordinates do not by themselves aggregate the sector
with two large residual projections.

### Fixed-row-pair square-root codegree and parabolic inverse

There is nevertheless a sharp theorem after **two row vertices are fixed**.
Let

```text
R=(a,m),             R'=(A,M),
Delta=a*M-m*A !=0.                                  (2E.R16)
```

The determinant is nonzero because the actual row pairs are primitive and
distinct.  A common neighbor consists of one color pair `(c,d)` and the two
carriers `b,B`.  Encode it by

```text
X=(b*c,b*d;B*c,B*d)=(b,B)^T*(c,d).                 (2E.R17)
```

The two factors in (2E.R17) are primitive.  Primitivity of `(c,d)` is
immediate from the all-five-distinct actual shell.  If `b=B`, the fixed pair
`(b,c)` and the sub-unit third-node interval force `a=A`, while `(b,d)`
forces `m=M`; this contradicts (2E.R16).  Thus `b,B` are distinct shell
prime powers, hence coprime because the shell endpoint ratio is below two.

Put

```text
v=m*d-a*c,             V=M*d-A*c,
J=b*v-B*V.                                          (2E.R18)
```

Every entry of `X` lies in a fixed interval of length `O(D)`.  Moreover,
if `r=8abc-q^3` and `s=8ABc-q^3`, direct substitution gives

```text
J=-q^3*d*Delta/(8*a*A*c)
    +r*v/(8*a*c)-s*V/(8*A*c).                     (2E.R19)
```

Here `|r|+|s|<<qD`, `|v|+|V|<<D`, and the ratio `d/c` varies by
`O(D/q^2)` in one color block.  Hence (2E.R19) varies by only
`O(D^2/q)=o(1)` after the two row vertices and the neighboring slope blocks
are fixed.  Since it is integral, one exact `J` serves every common
neighbor, and

```text
|J| asymp q*|Delta|.                               (2E.R20)
```

Equivalently, with the signs displayed explicitly,

```text
K=(-a,m;A,-M),       det K=Delta,       <K,X>=J.   (2E.R21)
```

The earlier fixed-secant norm theorem transposes to (2E.R21) without a
normalization change.  For two distinct neighbors let

```text
E=X-X',              delta=det E.                  (2E.R22)
```

Then `delta!=0`.  Indeed,

```text
det(X-X')
 =-det((b,B),(b',B'))*det((c,d),(c',d')),          (2E.R23)
```

and a zero factor makes one primitive pair equal; the sub-unit product
interval then makes the whole neighbor equal.  Also `<K,E>=0`.  Define

```text
A_0=E*K^T,
T=2*X*adj(E)-delta*I,
U=A_0*T-J*delta*I.                                 (2E.R24)
```

Exactly as in the fixed-color proof,

```text
tr A_0=tr T=tr U=0,
A_0^2=-Delta*delta*I,       T^2=delta^2*I,
A_0*U+U*A_0=0,
U^2=delta^2*(J^2+Delta*delta)*I.                   (2E.R25)
```

Writing `A_0=(alpha,beta;gamma,-alpha)` and
`U=(x,y;z,-x)`, the case `beta!=0` gives the binary equation

```text
beta*x^2-2*alpha*x*y-gamma*y^2
 =beta*delta^2*(J^2+Delta*delta),                  (2E.R26)
```

whose discriminant is `-4*Delta*delta!=0`.  The case `gamma!=0` is
symmetric; if both off-diagonal entries vanish, (2E.R26) becomes a divisor
equation.  The map is injective because

```text
T=A_0^(-1)*(U+J*delta*I),
X=(T+delta*I)*E/(2*delta).                         (2E.R27)
```

Finally, `|Delta*delta|<<D^3=o(q^2)` whereas (2E.R20) gives
`J^2>>q^2*Delta^2`.  Thus the represented integer in (2E.R26) is nonzero.
The uniform divisor/quadratic-order bound proves

```text
#{ordered neighbor pairs with one fixed E}<<q^o(1). (2E.R28)
```

Now let `lambda1<=lambda2<=lambda3` be the successive minima of

```text
Lambda_(R,R')={E in Z^4:<K,E>=0}.
```

The normal in (2E.R21) is primitive, so `det Lambda_(R,R') asymp q`.
There are two branches.

* If `lambda1*lambda2>>D`, the standard lattice count gives only

  ```text
  O(D+D^3/q)=O(D)                                  (2E.R29)
  ```

  possible short `E`.  Summing (2E.R28), a fixed row pair with `M_0`
  common neighbors satisfies

  ```text
  M_0*(M_0-1)<<D*q^o(1).                           (2E.R30)
  ```

* If `lambda1*lambda2<<D`, Minkowski gives
  `lambda3>>q/D`, which exceeds the `O(D)` secant box by the factor
  `q/D^2=q^(1/33-o(1))`.  All neighbor differences therefore lie in one
  rational rank-two plane.  Its rank-one points form a plane conic.  Pila's
  uniform bound gives `M_0<<sqrt(D)q^o(1)`.  More precisely, a nonparabolic
  irreducible section is a nonzero binary norm equation and has only
  `q^o(1)` points; reducible sections have `O(1)` actual points by (2E.R23).
  A power-sized exceptional family must consequently be parabolic.  The
  parabolic factorization theorem writes its product matrices, in
  `q^o(1)` primitive gcd/congruence classes, as

  ```text
  X(t)=(u_0+t*u_1)*(w_0+t*w_1)^T.                  (2E.R31)
  ```

  These are exactly the rational affine/Hankel tangent charts already
  covered by the fixed-chart theorem.  One chart contains a `q^(-o(1))`
  fraction of any power-sized exceptional family.

Combining the branches proves the sharp pointwise theorem

```text
codeg(R,R')<<sqrt(D)*q^o(1).                       (2E.R32)
```

The fixed-`(row,lambda)` multiplicity cap of two means that this also bounds
the corresponding short-CRT overlap up to an absolute factor: after choosing
an odd row coordinate, `lambda` and the congruence modulo `8a` fix the first
residual modulo a `q^2`-scale CRT modulus, larger than its `O(qD)` window;
unique factorization then leaves at most the factor swap.

The logical boundary is important.  The theorem is an
**energy-or-tangent** dichotomy: the generic branch is already bounded by
(2E.R30), while the exceptional power branch yields (2E.R31).  A generic
Sidon transversal of `sqrt(D)` neighbors could still use `D` different
secants once each, so near-sharp codegree alone does not force a tangent
chart.  Most importantly, (2E.R32) is pointwise in one row pair.  It does
not sum the generic secants or the exceptional charts over varying row
pairs, and proves neither `(SB)` nor FC.

### Exact Selberg reciprocal-sum gate and the relevant-strip integer lift

There is a precise analytic form of the same missing estimate.  Let `A_i`
and `C_j` be the first-coordinate projections of one neighboring row/color
block pair.  These projections are injective because the transverse width
of a ratio strip over one fixed first coordinate is `O(D/q)<1`; in
particular

```text
|A_i|,|C_j|<<D.                                    (2E.F1)
```

If `(a,c)` supports an edge, discarding the requirement that its carrier be
an actual prime power gives

```text
||q^3/(8*a*c)||_(R/Z)<<Delta,       Delta=D/q.      (2E.F2)
```

Take `H` comparable to `Delta^(-1)=q/D` and majorize the interval in
(2E.F2) by a degree-`H` Selberg polynomial.  With

```text
S_ell(A_i,C_j)
  =sum_(a in A_i,c in C_j) exp(2*pi*i*ell*q^3/(8*a*c)),
```

one obtains rigorously

```text
E_ij << Delta*|A_i|*|C_j|
       +Delta*sum_(1<=|ell|<=H)|S_ell(A_i,C_j)|.    (2E.F3)
```

The zero mode is already below the conjectured cap:

```text
Delta*D^2=D^3/q=D^(15/16).                         (2E.F4)
```

Consequently `(SB)` would follow from the sharp averaged reciprocal-sum
theorem

```text
sum_(1<=|ell|<=q/D)|S_ell(A_i,C_j)|
 <<q*q^o(1),                                       (2E.F5)
```

equivalently average size `Dq^o(1)`.  This is a theorem-sized reformulation,
not a proof.  Cauchy--Schwarz in `ell` would require the weighted second
moment to be

```text
sum_(|ell|<H)(1-|ell|/H)|S_ell|^2
 <<H*D^2*q^o(1)=q*D*q^o(1).                        (2E.F6)
```

The diagonal already reaches this size for maximal blocks.  More strongly,
a primitive full-integer consecutive-strip model proves that a
geometry-only second-moment route is off by a factor `D`.  Put `q=2m` and,
for a sufficiently small
absolute `c`, take

```text
A=C={m+i:0<=i<cD}.
```

These are the first-coordinate projections of primitive consecutive-vector
strips.  Uniformly for `0<=i,j<cD`,

```text
m^3/((m+i)(m+j))
 =m-(i+j)+(i^2+i*j+j^2)/m+O(D^3/m^2).             (2E.F6a)
```

Consequently all `D^2` summands lie in one fixed short arc whenever
`1<=ell<=c q/D^2`, and hence

```text
|S_ell|>>D^2,
sum_(ell<=c*q/D^2)|S_ell|>>q,
sum_(ell<=c*q/D^2)|S_ell|^2>>q*D^2.               (2E.F6b)
```

The first line has exactly the desired `L^1` mass, so this is not a
counterexample to (2E.F5).  The last line is a factor `D` above (2E.F6),
however: Cauchy--Schwarz or an unclassified large sieve necessarily loses
`sqrt(D)`.  At the active scale the coherent range contains
`q/D^2=q^(1/33)=D^(1/16)` modes.

The display `q=2m` is not an actual-prime fixture, but the obstruction is
not merely parity.  Let `kappa=288^(1/3)` and choose continued-fraction
convergents `Q/T` with odd numerator `Q` (infinitely many exist, since two
successive convergent numerators cannot both be even).  The integer centre

```text
(a_0,b_0,c_0)=(3T,3T,4T)
```

satisfies `|Q^3-8a_0b_0c_0|<<T`, while its two linear reciprocal gradients
are `1+O(T^(-2))` and `3/4+O(T^(-2))`.  On modes divisible by four the same
Taylor argument gives (2E.F6b) for consecutive strips about `a_0,c_0`.
This odd-composite family still is not an actual prime-centre counterexample;
it shows that any successful second-moment theorem must use more than
parity-blind convex-strip geometry.

The consecutive geometry is also compatible with a fully actual reference
at finite scale.  Namely

```text
p=2^31=2147483648,  r=p-1=2147483647,
q=4294967311=2p+15, D=46830
```

has `r,q` prime, `p,r` in the `q` shell, and
`-inverse(r)==1 (mod p)`.  Its legal all-integer determinant enlargement is
therefore consecutive.  Taking `L=floor(D/10)` consecutive lifts, the
`ell=1` Taylor phases lie in a fixed short arc and

```text
|S_1|>>L^2,                  L^4/(qD)>2.39.        (2E.F6c)
```

Thus actual-reference arithmetic does not formally forbid the obstruction.
This is only a finite certificate: an asymptotic actual family would require
infinitely many suitable Mersenne/Fermat-type neighbours, which is not
known.  Accordingly (2E.F6b) is a rigorous no-go for geometry-only `L^2`,
not a disproof of a future prime-sensitive second-moment theorem.

Additive reciprocity does not place (2E.F5) directly inside a current
fixed-modulus Kloosterman theorem.  For coprime odd `a,c`, CRT gives

```text
exp(2*pi*i*ell*q^3/(8*a*c))
 =omega_8(a,c,ell)
  *e_a(ell*q^3*inverse(8*c))
  *e_c(ell*q^3*inverse(8*a)),                       (2E.F7)
```

where `omega_8` is an eighth root of unity.  Both moduli and both reciprocal
arguments vary jointly with `(a,c)`.  The separated fixed-modulus kernel
needed by the available bilinear Kloosterman estimates is not present.

The earlier rational-ray objection to an all-integer enlargement does **not**
apply to a relevant nonempty block.  Such a block contains a primitive
shell-scale reference `r_0=(p,r)`.  For every integer shell vector
`x=(x1,x2)` in the same ratio strip,

```text
h=det(r_0,x)=p*x2-r*x1,                 |h|<<D.     (2E.F7a)
```

If two vectors have the same `h`, their difference is an integer multiple
of `(p,r)`.  The project shell is shorter than `p` and `r`, so that multiple
must be zero.  Thus fixed `h` has at most one shell lift and the entire
all-integer strip has `O(D)` points, with no primitivity condition on `x`.
Equivalently, a distinct reduced slope `P/R` in the bin obeys Farey spacing
`1/(pR)<<D/q^2`, whence `R>>q/D`; its ray contributes at most `q/R<<D`
shell multiples.  The generic long ray with fixed small denominator cannot
occur in a block already containing `r_0`.

It is therefore legal, for an upper bound, to drop the prime-power and
visibility masks and count all integer points in the two relevant strips.
This correction removes the Mobius obstruction, but it does not prove
(2E.F5).  The natural pointwise estimate that would close the gate is

```text
|S_ell|<<q^o(1)*(q/ell+ell*D^2/q),                 (2E.F7b)
```

because both terms sum to `O(q log q)` for `ell<=q/D`.

The estimate is routine on one contiguous tangent-band pair.  On a box of
side at most `L<=D`, the phase `f(a,c)=ell*q^3/(8ac)` has

```text
||Hess f||asymp ell/q,   det(Hess f)asymp (ell/q)^2,
(ell/q)*L<=1,            (ell/q)^(-1)>=D.          (2E.F7b')
```

The two-dimensional `B` process has only `O(1)` dual stationary points,
each of size `O(q/ell)`; the edge, image-area, and nonstationary terms are
`O((L+ell*L^2/q)*q^o(1))`.  They are absorbed by `q/ell` because
`ell<=q/D` and `L<=D`.  A dyadic smooth partition of the sharp box costs
only `q^o(1)` and gives

```text
|S_ell(one band pair)|<<q^(o(1))*q/ell.            (2E.F7b'')
```

For `ell<=q/L^2` the same display follows trivially from `L^2<=q/ell`, so
the `B` process is needed only in its nondegenerate range.

Thus one fan has the required summed bound.  There is, however, an exact
obstruction to obtaining (2E.F7b) by splitting a whole modular strip into
such fans and summing them absolutely.  Take the primitive
reference `(p,p-k)`, with `k|(p+1)`.  Since

```text
-(p-k)^(-1)==(p+1)/k=:t (mod p),
h=k*n+s  =>  a1(h)==n+t*s (mod p),                 (2E.F7c)
```

the determinant lifts split into as many as `k` separated bands, each of
length `O(D/k)`.  Two strips can therefore produce `k^2` tangent-band
pairs.  Even granting the optimal local Hessian estimate on every pair,
absolute summation gives

```text
k^2*q/ell + ell*D^2/q,                             (2E.F7d)
```

and loses `k^2` in the stationary term.  The phases of the band centres are
again reciprocal, so removing this loss is precisely an outer Farey-fan
`L^1` cancellation theorem, not routine two-dimensional stationary phase.
The scattered phenomenon is compatible with actual reference nodes at
finite scale.  For example

```text
q=1161203,  p=580607,  r=579583,  k=1024,  t=567
```

has `q,p,r` prime, `p-r=k`, `p+1=k*t`, and `p,r` in the standard project
shell; the active rounded scale is `D=872`.  Thus `|h|<=D` occupies `1024`
bands of length at most two before shell cuts, and exactly `519` lifts
in `411` bands survive the two shell-coordinate cuts.  This is not an asymptotic
counterexample or a proof that large `k` occurs infinitely often, but it
shows that actual-reference primality does not formally eliminate the fan
geometry.  Any use of that extra arithmetic would require a quantitative
theorem, not a convex-strip Poisson argument.

The `k`-band description is exact, but it is not an invariant or reduced
fan decomposition.  There is a uniform geometry-of-numbers correction.
Write

```text
Lambda_(p,t)={(h,a) in Z^2:a==t*h (mod p)},
||(u,v)||_* =max(|u|/D,|v|/p).                    (2E.F7e)
```

This lattice has determinant `p`; after the displayed anisotropic scaling
its determinant is `1/D`.  Minkowski therefore supplies a primitive
shortest vector `v_0=(u,v)` with

```text
lambda=||v_0||_*<<D^(-1/2).                       (2E.F7f)
```

Extend `v_0` to a lattice basis `(v_0,w)`, with
`|det(v_0,w)|=p`.  On the determinant-lift rectangle, whose side lengths
are `O(D)` and `O(p)`, the integer quotient coordinate

```text
nu(x)=det(v_0,x)/p
```

varies through only

```text
O(1+|u|+D*|v|/p)=O(1+D*lambda)=O(sqrt(D))         (2E.F7g)
```

values.  Each value is one affine arithmetic fan parallel to `v_0`, and
the rectangle contains `O(1/lambda)` points on it.  This proves, without
any primality or visibility input, that a whole relevant modular strip is
a union of at most `O(sqrt(D))` reduced parallel fans.  The proof also
shows that their number times their maximal length is `O(D)`.

For the special basis in (2E.F7c), both

```text
(k,1), (1,t) in Lambda_(p,t),       det((k,1),(1,t))=p. (2E.F7h)
```

Thus `(k,1)` is the useful direction for `k<=sqrt(D)`, while `(1,t)` is
the useful direction for `k>=sqrt(D)`.  In the finite prime fixture above,
`(1,t)=(1,567)` corresponds in the original row coordinates to the single
direction `(567,566)`; the full determinant interval has only `O(1)`
wraps in this direction.  Grouping those same points by `h mod 1024`
creates the hundreds of singleton bands artificially.

This correction removes an arbitrarily large *coordinate-dependent*
`k^2` loss: two optimally reduced strips have at most `O(D)` fan pairs.
It does not prove (2E.F7b), because absolute use of (2E.F7b'') on those
`O(D)` pairs still loses a factor `D`.  What remains is cancellation or a
positive-curvature merger across the reduced quotient coordinates, not
the raw number of residue-class bands.

There is an exact invariant form of the remaining fan obstruction.  Enlarge
two compatible strips by an absolute factor and choose one common primitive
direction

```text
d=(R,S),  e=(U,V),                 R*V-S*U=1.       (2E.F7i)
```

Here `(d,e)` is a unimodular basis of the physical integer lattice.  On a
fixed row fan and a fixed reciprocal-color fan write

```text
x=m*d+r*e=(a1,a2),       y=n*d+s*e=(c2,c1).        (2E.F7j)
```

The two carrier products then have the exact expansions

```text
a1*c1=R*S*m*n+R*V*m*s+U*S*r*n+U*V*r*s,
a2*c2=R*S*m*n+S*U*m*s+V*R*r*n+V*U*r*s,
a1*c1-a2*c2=m*s-r*n.                              (2E.F7k)
```

Thus the two physical progression steps in a fan pair are not unrelated:
they are the complementary coordinates `R,S` of one primitive direction,
and the compatibility determinant becomes affine in the two long
coordinates.  This is the useful content of the common `SL_2(Z)` reduction.

It does not, by itself, give the proposed local curvature count.  Put
`T=q^3/8`, `a=R*m+U*r`, `c=S*n+V*s`, and apply the two-dimensional `B`
process to

```text
f_ell(m,n)=ell*T/(a*c).
```

At a stationary dual pair `(j,k)` one has, up to the harmless choice of
Poisson signs,

```text
j=ell*R*b/a,      k=ell*S*b/c,      b=T/(a*c),
b=(T*j*k/(ell^2*R*S))^(1/3).                         (2E.F7l)
```

Moreover the Legendre phase, including the fixed-fan translations, is
exactly

```text
3*(T*ell*j*k/(R*S))^(1/3)
       -j*U*r/R-k*V*s/S.                            (2E.F7m)
```

Indeed `f-a*f_a-c*f_c=3f`, and substitution of (2E.F7l) proves the
display.  The index Hessian has

```text
sqrt(det Hess(f_ell))asymp ell*R*S/q,               (2E.F7n)
```

so one stationary term has size `asymp q/(ell*R*S)`.  The area of the
dual gradient image of an `L_a`-by-`L_c` fan pair is
`asymp ell^2*R^2*S^2*L_a*L_c/q^2`.  Consequently absolute stationary-term
summation contains the term

```text
ell*R*S*L_a*L_c/q.                                  (2E.F7o)
```

After the Selberg sum through `ell<=q/D`, (2E.F7o) becomes
`R*S*L_a*L_c/D`, rather than the desired random-volume term
`(D/q)*L_a*L_c`.  Exact tangent resonances are represented correctly by
the complementary `D/(R*S)` scale.  There is a small rigorous refinement
for the exactly coherent interior stationary terms.  Choose the common
primitive direction `d=(R,S)` to have slope in an absolute enlargement of
the two neighboring slope strips; the shell-scale primitive reference is
always an admissible, though not necessarily reduced, choice.  If `P,Q`
are the numbers of row and color fans in one dyadic fan-length class, then

```text
P<<R,                 Q<<S.                         (2E.F7o1)
```

Indeed the quotient fan coordinate is exactly
`det(d,x)`: from `x=m*d+r*e` and `det(d,e)=1` it equals `r`.  Since
`x asymp q`, two slopes in a `D/q^2` enlargement have determinant
`O(R*D/q)` (and `R asymp S`), so the number of integer quotient values is
`O(1+R*D/q)<<R`.  This argument is not valid for an arbitrary shortest
Minkowski direction whose slope may lie outside the strip; the
slope-adapted choice is part of (2E.F7o1).

Let the fan lengths be at most `L_a,L_c`, with
`P*L_a,Q*L_c<<D`.  In the normalized dual coordinates `(j/R,k/S)`, the
gradient image has boundary length and area

```text
O(1+ell*R*L_a/q+ell*S*L_c/q),
O(ell^2*R*S*L_a*L_c/q^2),                           (2E.F7o2)
```

respectively.  The planar convex lattice-point bound therefore gives

```text
#(gradient image intersect (R*Z)x(S*Z))
 <<1+ell*R*L_a/q+ell*S*L_c/q
      +ell^2*R*S*L_a*L_c/q^2.                      (2E.F7o3)
```

On this sublattice the two translation terms in (2E.F7m) are integers.
Even summing these coherent **interior stationary terms** absolutely over
all `P*Q` fan pairs, (2E.F7n), (2E.F7o1), and (2E.F7o3) give

```text
q/(ell*R*S)*P*Q*
 (1+ell*R*L_a/q+ell*S*L_c/q
      +ell^2*R*S*L_a*L_c/q^2)
 <<q/ell+D+D+ell*D^2/q
 <<q/ell+ell*D^2/q.                                (2E.F7o4)
```

Here `D<<q/ell` for `ell<=q/D`.  Hence the exact coherent interior
stationary sublattice has total Selberg mass `O(q log q)`; it is not the
missing loss.  Formula (2E.F7o4) does not estimate boundary/nonstationary
terms of singleton fans, and it does not allow the slope-adapted direction
to be replaced silently by the shortest reduced direction.

There is an exact fail-fast ledger for the omitted terms, even if one grants
a diagonal-strength estimate for the full interior HSM kernel.  Put

```text
H=q/D,             H_0=q/D^2.                      (2E.F7o4a)
```

The low Selberg modes close trivially: the whole neighboring block product
has at most `D^2` pairs, so

```text
(D/q)*sum_(ell<=H_0)|S_ell|
 <=(D/q)*(q/D^2)*D^2=D.                            (2E.F7o4b)
```

The coherent interior terms also close.  Summing (2E.F7o4) through `H`
gives

```text
sum_(ell<=H)(q/ell+ell*D^2/q)<<q*q^o,              (2E.F7o4c)
```

and the Selberg coefficient `D/q` turns this into `D*q^o`.

Sharp fan endpoints are different.  A sequential one-dimensional
`B`-process has an `O(q^o(1))` endpoint/transition/nonstationary error for
each value of the coordinate not yet transformed.  In a dyadic class with
`P,Q` fans and lengths `L_a,L_c`, the two possible orders therefore give

```text
P*Q*L_a  or  P*Q*L_c.
```

Using `P*L_a,Q*L_c<<D` and the proved fan-count product `P*Q<<D`, the best
available bound is

```text
min(P*Q*L_a,P*Q*L_c)
 <<D*min(P,Q)<=D^(3/2)                             (2E.F7o4d)
```

per frequency.  The exponent is attained by the balanced ledger
(2E.F7o6), where `P=Q=L_a=L_c=sqrt(D)`.  Corner errors alone are harmless:
they cost `P*Q<<D` per frequency and hence `q` before the Selberg factor.
The one-dimensional edge errors in (2E.F7o4d), however, give

```text
H*D^(3/2)=(q/D)*D^(3/2)=q*sqrt(D)=q^(41/33),       (2E.F7o4e)
```

before the Selberg coefficient, and

```text
(D/q)*q*sqrt(D)=D^(3/2)=q^(8/11)                  (2E.F7o4f)
```

after it.  The target is `D=q^(16/33)`, so the current boundary treatment
loses `sqrt(D)=q^(8/33)`.  A smooth global partition could replace the
sequential endpoint error only if its Fresnel transition charts were shown
to enter the same HSM estimate with uniform fan-translation weights.  That
lemma is not proved: the interior HSM hypothesis does not include these
codimension-one charts.  Thus low modes and coherent interior resonances
pass, but the complete high-step `B`-process proof **fails** at the
boundary/transition term.  This is a proof gap, not a lower bound for the
actual boundary contribution.

There is, however, a rigorous way to bypass this particular endpoint term
in the positive Selberg count.  It is different from smoothing the boundary
of the original skew convex strip.  Use the slope-adapted basis in
(2E.F7i)--(2E.F7j), fill the integer quotient coordinates `r,s` to intervals,
and complete every retained fan through one fixed constant enlargement of
the physical shell.  Relevance and Farey spacing give

```text
R,S>>q/D,
P<<1+R*D/q,                 Q<<1+S*D/q.             (2E.F7o4g)
```

The completed physical lengths are `O(1+q/R)` and `O(1+q/S)`.  Hence

```text
P*(1+q/R)
 <<(1+R*D/q)*(1+q/R)<<D,
Q*(1+q/S)<<D.                                      (2E.F7o4h)
```

The completion is legal **before** Fourier expansion: the Selberg upper
polynomial majorizing the reciprocal window is nonnegative everywhere.
Thus missing quotient classes and shell points may be added, and the sharp
physical shell indicator may be replaced by fixed nonnegative smooth
functions `w_a(a/q),w_c(c/q)` which equal one on the original shell and are
supported in an absolute enlargement.  The zero mode is still
`O(D^3/q)` by (2E.F7o4h).

For the completed row support, Poisson summation is now made only in the
long coordinate `m`:

```text
sum_m w_a((R*m+U*r)/q)*e(f(R*m+U*r,c))
 =1/R*sum_j e(j*U*r/R)
      *integral w_a(a/q)*e(f(a,c)-j*a/R) da.        (2E.F7o4i)
```

After the analogous color transform and the `r,s` sums, the exact formula is

```text
S_tilde_ell
 =1/(R*S)*sum_(j,k) W_P(j)*W_Q(k)*I_ell(j,k),       (2E.F7o4j)

I_ell(j,k)=double_integral w_a(a/q)*w_c(c/q)
 e(ell*T/(a*c)-j*a/R-k*c/S) da dc.
```

There are no fanwise endpoints in (2E.F7o4j): the sharp quotient intervals
remain the external Dirichlet weights `W_P,W_Q`, while the variables to
which the `B` process is applied have slow `C_c^infinity` cutoffs on scale
`q`.  Nonstationary dual ranges are rapidly summable by integration by
parts.  On the stationary range, inserting (2E.F7o9) into
`w_a(a/q)w_c(c/q)` is Mellin-separable with bounded (hence `q^o(1)`) Mellin
cost, exactly as in (2E.F7o10).  Thus this completion produces the same
smooth interior HSM kernel and no Fresnel-transition addendum.  In the
balanced class, (2E.F7o4h) reads

```text
R=S=q/sqrt(D),       P=Q=sqrt(D),
completed fan lengths=sqrt(D),       completed masses=D. (2E.F7o4k)
```

Consequently, **conditional on** the diagonal-strength smooth HSM estimate,
the complete raw sum is `O(q*q^o(1))` and the Selberg-weighted contribution
is `O(D*q^o(1))`; the old `D^(3/2)` endpoint ledger does not occur.  This is
a proved boundary reduction, not a proof of the HSM estimate.  It also does
not assert cancellation for the sharp fanwise endpoint pieces in
(2E.F7o4d): it avoids creating those pieces by using positivity first.

#### Why HSM excess does not yet transfer back to actual carrier arcs

The positivity step is one-way, which blocks a proposed inverse proof of the
remaining HSM.  Let `A_0,C_0` be the original actual-node projections and
`A_tilde,C_tilde` the filled supports in (2E.F7o4h).  If `K_H^+` is the
nonnegative Selberg upper polynomial, then the exact input is only

```text
sum_(A_0 x C_0) K_H^+(T/(a*c))
 <=sum_(A_tilde x C_tilde)w_a(a/q)w_c(c/q)K_H^+(T/(a*c)). (2E.F7o4l)
```

The Poisson data in (2E.F7o4j) contain `W_P,W_Q` and the smooth completed
shell cutoffs; they no longer contain the prime-power masks of `A_0,C_0`.
Consequently an inverse theorem for a large component of the **completed**
HSM can locate a resonance among added integer points without assigning any
mass to the original edges.  To transfer such a conclusion one would need,
for a recovered packet `P`, a new mass-retention statement of the form

```text
sum_((a,c) in (A_0 x C_0) intersect P) K_H^+(T/(a*c))
 >>q^(-o(1))*(original excess),                    (2E.F7o4m)
```

or a positive packet decomposition whose unstructured total is `O(D)`.
Neither follows from (2E.F7o4l), because its Fourier expansion is signed,
and neither is proved here.  This is particularly material for scattered
one- and two-point packets: the fixed-direction affine/Hankel merger applies
to rich lines with at least three points and one fixed primitive direction;
it does not aggregate cross terms over varying directions or certify
(2E.F7o4m).

Even granting mass retention, the current prime nonembedding theorem is not
a terminal inverse theorem for approximate arcs.  It uses exact vanishing of
the three lower coefficients in (2E.F7w).  At the largest possible packet
size `N=D`, interpolation gives only

```text
|c_3|<<q/D^2=q^(1/33),
N=D=q^(48/99)<(q*D)^(1/3)=q^(49/99).               (2E.F7o4n)
```

Thus integrality misses by `q^(1/99)`.  The exact centered quartic exclusion
does not exclude shifted-center or genuinely approximate quadratic-carrier
arcs, and the proved fixed-direction merger does not merge all their varying
directions.  The conditional `(PAC)` ledger would control such arcs if a
`q^o(1)` covering with mass retention were supplied; an inverse theorem that
merely finds one dense packet is insufficient.

The exponent `17/33` in Fouvry--Radziwill does not supply the missing
statement.  [Corollary 1.1 of their paper](https://arxiv.org/abs/1811.08672)
is an averaged-modulus dispersion theorem for a multiplicative convolution
`alpha*beta`, with one divisor-bounded factor supported on a tiny interval
and satisfying a uniform Siegel--Walfisz condition.  Corollary 1.2 gives, for
the divisor function, only the weak average

```text
sum_(Q<r<=2Q)|AP discrepancy modulo r|
 <<x/(log x)^(1-epsilon),       Q<=x^(17/33-epsilon). (2E.F7o4o)
```

Our HSM is instead the balanced four-variable shifted product
`j*k-j'*k'=h`, with cubic-root weights and one fixed `q`-dependent pair
`R,S` (or fixed cross-cusp level `R*S`).  On its natural scale

```text
X=J*K=q^(84/33),       R*S=q^(50/33)=X^(25/42),
25/42-17/33=37/462.                                 (2E.F7o4p)
```

Hence an attempted fixed-level application is outside the quoted level of
distribution.  Identifying the theorem's `x` with the original `q` merely
makes its modulus exponent look like the Selberg frequency exponent: a
Selberg frequency is not an arithmetic-progression modulus, and the theorem
stops at `17/33-epsilon`, not the endpoint `H=q^(17/33)`.  The DFI
`c`-average has `c`-dependent CRT and Kloosterman weights and is not the AP
discrepancy in (2E.F7o4o).  Finally (2E.F7o4o) supplies logarithmic saving,
where the optimistic shifted-divisor ledger (2E.F7o20) misses by the fixed
power `q^(2/11)`.  Smooth positive completion changes none of these
hypotheses.

Therefore the proposed inverse route does not presently prove `(SB)` or
full FC.  The sharp missing inputs are a mask-sensitive HSM inverse/packet
decomposition proving (2E.F7o4m), a global cross-direction merger, and an
approximate-prime arc theorem that bridges (2E.F7o4n).  This is a rigorous
non-implication audit, not an actual-prime counterexample.

The complementary minor residues do not acquire a free mean-zero saving.
For consecutive fan indices and `(U,R)=1`, put

```text
W_P(j)=sum_(r<P)e(-j*U*r/R).
```

When `P<=R`, exact finite Fourier orthogonality gives

```text
sum_(j mod R)|W_P(j)|^2=R*P,
sum_(j mod R, j!=0)|W_P(j)|^2=R*P-P^2.             (2E.F7o5)
```

Thus in the active sparse ratio `P/R<<D/q`, deleting the coherent residue
retains a proportion `1-O(D/q)` of the transverse `L^2` mass.  The same
holds on the color side.  In the balanced ledger

```text
P=Q=sqrt(D), R=S=q/sqrt(D),
L_a=L_c=sqrt(D), ell asymp q/D,                    (2E.F7o6)
```

one fan-pair gradient image has `N asymp q^4/D^3` dual points, while the
coherent sublattice has only `N/(R*S)=q^2/D^2=o(N)`.  There are
`M asymp ell*P*Q=q` sampled triples and a stationary amplitude
`A_0 asymp D^2/q^2`.  Even an ideal weighted surface-energy sampling bound
with its compulsory sample factor gives

```text
A_0*M*sqrt(N)=q*sqrt(D)=q^(41/33).                 (2E.F7o7)
```

The sample factor cannot be removed: a one-point extension is identically
one at every sample.  Summing the fan translations before applying energy
makes the diagonal ledger `O(q)`, but collapses all evaluations to the
two-coordinate trace `(y_1,y_2)=(0,0)` of the surface extension.  Exact
three-dimensional additive energy does not control that trace; the
automatic two-dimensional Nikolskii step loses `(J*K)^(1/4)`, which in
(2E.F7o6), where `J asymp K asymp q^2/D^(3/2)`, is
`q/D^(3/4)=q^(7/11)`.  Thus transverse Dirichlet-kernel cancellation does
not invalidate the minor-sampling obstruction.

There is nevertheless more structure than an arbitrary weighted surface
extension sees.  Freeze a smooth dyadic block `ell asymp L`.  The exact
stationary amplitude in (2E.F7l) is

```text
1/sqrt(det Hess(f_ell))
 =a^2*c^2/(sqrt(3)*ell*T*R*S)
 =T^(1/3)*ell^(1/3)*(R*S)^(-1/3)*(j*k)^(-2/3)/sqrt(3). (2E.F7o8)
```

Thus its `j,k` dependence is separable.  The inverse stationary map is

```text
a=T^(1/3)*ell^(1/3)*R^(2/3)*S^(-1/3)*j^(-2/3)*k^(1/3),
c=T^(1/3)*ell^(1/3)*S^(2/3)*R^(-1/3)*k^(-2/3)*j^(1/3). (2E.F7o9)
```

Consequently Mellin inversion separates every smooth translated `a`-cutoff
and `c`-cutoff in the stationary main term.  The translation phases then
sum independently in `r` and `s`; for consecutive fans they give precisely
`W_P(j)` and `W_Q(k)`, with smooth Mellin-dependent coefficients in the
nonuniform case.  The total `L^1` norm of the Mellin parameters is
`q^o(1)`.  Deleting the joint coherent set
`j==0 (mod R), k==0 (mod S)` is a rank-two separable operation.  Hence,
after the standard smooth dyadic partition, the **interior stationary minor
main term** is a `q^o(1)`-cost superposition of sums

```text
F_ell=sum_(j,k) u(j)*v(k)
       *e(3*(T*ell*j*k/(R*S))^(1/3)).              (2E.F7o10)
```

This statement does not absorb the boundary/nonstationary terms excluded
in (2E.F7o4).  It does show that an arbitrary-coefficient surface theorem
is unnecessarily strong for the interior minor sum.

For one separated term put

```text
d(x)=sum_(j*k=x)u(j)*v(k),
K_L(x,y)=sum_(ell asymp L)
 e(3*(T/(R*S))^(1/3)*ell^(1/3)*(x^(1/3)-y^(1/3))). (2E.F7o11)
```

Smooth weights in `ell` may be inserted without changing the ledger.  The
four-point spacing identity is exact:

```text
sum_(ell asymp L)|F_ell|^2
 =sum_(x,y)d(x)*conj(d(y))*K_L(x,y).               (2E.F7o12)
```

The product diagonal is already sharp, since Cauchy on the divisor fibre
gives

```text
sum_x|d(x)|^2
 <=max_(x in supp d) tau(x)*sum_(j,k)|u(j)*v(k)|^2
 <<q^o(1)*||u||_2^2*||v||_2^2.                    (2E.F7o13)
```

In the balanced block (2E.F7o6), write `J,K` for the two dual interval
lengths and `X=J*K`.  Then

```text
L=q/D, R=S=q/sqrt(D), J=K=q^2/D^(3/2),
X=q^4/D^3, ||u*v||_(pair,2)^2:=||u||_2^2*||v||_2^2
 asymp P*Q*X=D*X=q^4/D^2,
A_0=q/(L*R*S)=D^2/q^2.                            (2E.F7o14)
```

Therefore the diagonal contribution to the original minor moment is

```text
A_0^2*L*D*X
 =(D^4/q^4)*(q/D)*(q^4/D^2)=q*D.                 (2E.F7o15)
```

There is no polynomial slack.  The exact remaining theorem is the weighted
shifted multiplication-table estimate

```text
(*)  sum_(x!=y)d(x)*conj(d(y))*K_L(x,y)
     <<L*||u||_2^2*||v||_2^2*q^o(1).              (2E.F7o16)
```

Equivalently, on writing `h=x-y`, its correlations are

```text
C_h[Psi]=sum_(j*k-j'*k'=h)
 u(j)*v(k)*conj(u(j'))*conj(v(k'))*Psi(j*k,j'*k'). (2E.F7o17)
```

Thus separability converts the arbitrary surface problem into a restricted
Dirichlet-convolution/additive-divisor problem; it does not prove `(*)`.
Indeed, with

```text
B_0=L*R*S/q,              W=L^2*R*S/q=L*B_0,       (2E.F7o18)
```

the phase changes by `O(1)` throughout `0<|h|<<B_0`.  A sufficient
short-shift part of `(*)` already requires, for the smooth phases inherited
from `K_L`,

```text
sum_(0<|h|<<B_0) C_h[Psi_h]
 <<||u||_2^2*||v||_2^2*q^o(1).                    (2E.F7o19)
```

At `D=q^(16/33)`, the exact powers are

```text
X=q^(84/33), B_0=q^(34/33), ||u||_2^2*||v||_2^2=q^(100/33).
```

Even granting that every shifted-divisor main term vanishes and granting
the optimistic classical level-one spectral error `X^(2/3+o(1))` per
shift, with only the natural coefficient-density factor `D`, absolute
summation over the short shifts gives

```text
D*B_0*X^(2/3)=q^(106/33),
D*X=q^(100/33),
(D*B_0*X^(2/3))/(D*X)=q^(6/33)=q^(2/11).          (2E.F7o20)
```

Equivalently the required average error per short shift is
`D*X/B_0=q^(66/33)`, whereas that benchmark is
`D*X^(2/3)=q^(72/33)`.  This comparison is deliberately optimistic:
classical shifted-divisor theorems concern standard divisor/automorphic
coefficients and require subtraction of explicit zero-frequency main terms.
They are not uniform for the present Dirichlet kernels of growing moduli
`R=S=q^(25/33)`.  Formula (2E.F7o5) supplies neither the needed main-term
vanishing nor the extra `q^(2/11)` averaged saving.

#### A rigorous `P^3` spacing fallback and its sharp fixtures

There is a short unconditional fallback for the spacing subproblem.  Put

```text
A_mn=q^3/(8R^2*S*m^2*n),       B_mn=q^3/(8R*S^2*m*n^2),
N(delta)=sum_(m,n~P) #{0<|h|,|k|<=P:
                       ||h*A_mn+k*B_mn||<=delta}.
```

Uniformly for `1/L<=delta<=1/2`, one has

```text
N(delta) << (delta*P^4+P^3)q^o(1).                 (2E.F7N1)
```

Here is the proof.  A fixed `(m,n)` fiber of size `Y>>P` has `O(P)`
nearest-integer levels `t`, hence one level contains `U>>Y/P` points.
Ordering that level by `h` and subtracting adjacent points produces a
nonzero homogeneous relation

```text
|r*A_mn+s*B_mn|<=2*delta,       |r|,|s|<<P/U<<P^2/Y.
```

For small fixed `delta`, its signs are opposite.  On writing
`x=m|s|, y=n|r|`, it implies

```text
|x-(S/R)y|<<delta*P.
```

For relations of height at most `H`, there are `O(PH)` possible `y`, at
most `O(1+delta*P)` integers `x` for each `y`, and only divisor-many
representations of `x,y`.  Thus

```text
R_0(H,delta)<<P*H*(1+delta*P)q^o(1),
#{(m,n): fiber size >=Y}
 <<P^3*(1+delta*P)*Y^(-1)q^o(1).                  (2E.F7N2)
```

Dyadic summation, with the fibers of size `O(P)` treated trivially, proves
(2E.F7N1).  For larger fixed `delta`, the trivial `P^4` count is already
absorbed by `delta*P^4`.

This does not improve the high-step ledger.  Indeed, for

```text
K=sum_(m,n,h,k) min(L,||h*A_mn+k*B_mn||^(-1)),
```

dyadic integration of (2E.F7N1) gives

```text
K<<(P^4*log L+L*P^3)q^o(1),
P^(-2)K<<L*P*q^o(1).                              (2E.F7N3)
```

The desired normalized bound is `Lq^o(1)`.  Thus the fallback retains the
full factor `P=q^(8/33)=sqrt(D)` and merely reproduces the existing local
`D*P=D^(3/2)` loss.  It proves no new HSM, `(SB)`, `(RT)`, or FC estimate.

Both endpoint terms in the desired sharper bound are genuinely present for
the actual Dirichlet autocorrelations.  For a large prime `q`, take an even
`P_0~q^(8/33)`, let `R` be the nearest integer to `q/P_0`, and put `S=R+1`.
Then `(R,S)=1`.  At `m=n=P_0/2`,

```text
A_mn=(q/(R*P_0))^3*(R/S)=1+O(1/R),
B_mn=(q/(R*P_0))^3*(R/S)^2=1+O(1/R).
```

Consequently `gg P_0^2` positive pairs `h,k<<P_0` obey
`||hA_mn+kB_mn||<=P_0^2/q~1/L`, with nonzero nearest integer `t=h+k`.
This is the aligned-center `P^2` fixture.  There is also a homogeneous
`t=0` fixture.  For `P_0/2<=m,n<=3P_0/4`, put `d=(m,n)` and

```text
h=z*m/d,       k=-z*n/d,       1<=z<=d.
```

Then

```text
h*A_mn+k*B_mn
 =z*q^3*(S-R)/(8*d*R^2*S^2*m*n)=O(1/L),
sum_(m,n in this interval) (m,n) asymp P_0^2*log P_0. (2E.F7N4)
```

All these shifts lie inside `3P_0/4`, so each triangular autocorrelation
factor `P_0-|h|`, `P_0-|k|` is a fixed fraction of its maximum.  These are
sharp fixtures for the spacing/Dirichlet-correlation subproblem, not by
themselves normalized HSM lower bounds.  The exact finite checks in
`qp_four_cycle_weighted_secant_lab.py` use rational arithmetic.

#### The cubic endpoint and a genuine arithmetic hard wall

The sharper weighted problem cannot be bypassed merely by retaining Fejer
positivity.  On the diagonal `m=n`, with `S=R+1`, one cubic resonance implies
the second one after a fixed enlargement because `L/R~1/P`.  Thus the smooth
HSM already requires the positive incidence estimate

```text
#{ell~L,m~P,a~L:
  |ell*q^3-8*a*R^2*S*m^3|<<R^2*S*m^3/P}
 <<L*q^o(1).                                             (2E.F7N5)
```

This positive diagonal peak is weaker than the four-variable spacing theorem,
but it is unavoidable: on `||ell*A_mm||,||ell*B_mm||<<1/P`, both Fejer
kernels are `gg P^2`, so a diagonal-strength weighted HSM bound forces
(2E.F7N5).  Put

```text
K=8*R^2*S,             beta_m=K*m^3/q^3~1.
```

After exchanging the nearest integer `a` with `ell`, at bounded multiplicity,
(2E.F7N5) is equivalent up to fixed enlargements to

```text
E_diag=sum_(a~L,m~P) 1_(||a*beta_m||<<1/P) <<L*q^o(1).  (2E.F7N5a)
```

There is a proof-grade intermediate bound

```text
E_diag <<L*P^(3/7+o(1)).                               (2E.F7N5b)
```

Indeed, a degree-`P` Selberg majorant and the geometric sum over `a` give

```text
E_diag <<L+P^(-1)*sum_(m~P) sum_(1<=r<=P)
                    min(L,||r*beta_m||^(-1)).            (2E.F7N5c)
```

For each `m`, choose a reduced Dirichlet approximant `b/d` with
`1<=d<=P` and

```text
|beta_m-b/d|<=1/(d*P).
```

The standard reciprocal-sum lemma then gives

```text
sum_(r<=P) min(L,||r*beta_m||^(-1))
 <<P*L/d+(P+d)*log P.                                  (2E.F7N5d)
```

Let `N(Q)` count the chosen denominators `d~Q`.  Monotonicity
`beta'_m~1/P` and Farey spacing give the elementary bound `N(Q)<<Q^2`:
there are `O(Q^2)` reduced fractions in the fixed value range, and each
`1/(QP)` tube contains `O(1)` integers `m`.  A second, independent bound
comes from Theorem 2 of
[Huxley, *The rational points close to a curve II*](https://matwbn.icm.edu.pl/ksiazki/aa/aa93/aa9331.pdf).
Its parameters are `M=P`, curve scale `lambda~1`, denominator `Q`, and
`delta_H=Q/P`; the cubic `beta_m` satisfies all three derivative and
nondegeneracy hypotheses.  It gives

```text
N(Q) <<(P^(3/4)*Q^(1/4)+P^(1/3)*Q)*P^o(1).             (2E.F7N5e)
```

For `Q<=P^(3/7)` use `N(Q)<<Q^2`; for larger `Q` use (2E.F7N5e).  Therefore

```text
sum_(m~P) 1/d_m
 <<sum_(Q dyadic) min(Q,
       P^(3/4)*Q^(-3/4)+P^(1/3))*P^o(1)
 <<P^(3/7+o(1)).                                       (2E.F7N5f)
```

Equations (2E.F7N5c)--(2E.F7N5f), and `P^2<<P*L`, prove
(2E.F7N5b).  Thus Fejer positivity improves the trivial diagonal loss from
`P` to `P^(3/7)=q^(8/77)`, but it does not remove it.  It also controls only
the diagonal peak, not the other dyadic Fejer scales or the off-diagonal
`(m,n)` terms.

The exactly coherent stratum is already sharp and harmless.  In the aligned
integer model write `P_0/m=s/t` in lowest terms.  Exact `ell` resonances have
period `t^3`.  Since `s|P_0` and `t~s` on a dyadic `m~P_0` interval,

```text
sum_(m~P_0) L/t^3
 <=L*sum_(s|P_0) sum_(t~s) t^(-3) <<L.                (2E.F7N5g)
```

Changing `1<=ell<=L` to a dyadic interval adds only `O(P)<<L`.  The
denominator-one tangent ray attains order `L`; Fejer positivity does not
cancel it, but it is exactly target-sized.  The unresolved part of
(2E.F7N5a) is the noncoherent near-cube remainder, not an exact rational ray.

The dual endpoint has an especially precise one-dimensional obstruction.
At the hostile dyadic scale

```text
Q=P^(11/32),       G=P^(21/32),       H=P^(7/32),
```

one must average primitive solutions of

```text
r*a^3-p*c^3=e,       r,p~Q, a,c~P,       0<|e|<<H.       (2E.F7N6)
```

The needed raw count is `O(Q*P^o(1))`; restoring the multiplicity `G` then
costs only `P^(1+o(1))`.  Two elementary bounds are
`O(P)` (two primitive solutions cannot share `c`) and
`O(Q*H*P^o(1))` (fix `r,e` and use `c^3 | r*a^3-e`).  The best audited
off-the-shelf improvement is Konyagin's rational-approximation theorem:

```text
raw count <<P^(43/80+o(1)),
restored count <<P^(21/32+43/80+o(1))
               =P^(191/160+o(1)).                        (2E.F7N7)
```

This saves `P^(1/40)` over the relevant `P^(9/16)` term in Huxley's bound,
but it still misses the target by `P^(31/160)`.  See
[Konyagin, *Mathematika* 46 (1999), DOI 10.1112/S0025579300007555](https://doi.org/10.1112/S0025579300007555),
whose formula is also stated as Theorem 6 in
[Trifonov](https://www.math.bas.bg/serdica/1998/1998-319-338.pdf).
The global exceptional-`abc` estimate of
[Bernert--Browning--Duker Lichtman--Teravainen](https://arxiv.org/abs/2410.12234)
is much weaker in this fixed-`a`, mixed-height box.

There is a proof-grade reason not to expect a pointwise repair.  For one
solution of (2E.F7N6), put

```text
A=r*a^3,       B=p*c^3,       g=gcd(A,B).
```

Since `g | e`, the three integers `A/g,B/g,|e|/g` form a primitive `abc`
triple.  The common gcd is not a loss in the quality ledger: writing
`g=P^gamma`, with `0<=gamma<=7/32`, one has

```text
max(A/g,B/g)>>P^(107/32-gamma),
rad((A/g)*(B/g)*(e/g))
  <<r*p*a*c*(|e|/g)<<P^(93/32-gamma).              (2E.F7N8)
```

The quotient `(107-32*gamma)/(93-32*gamma)` is increasing in `gamma`.
Its uniform quality is therefore at least `107/93-o(1)`.  The `abc` conjecture
would eventually exclude every nonzero solution, and an infinite sequence
of even single solutions would contradict `abc` for every
`epsilon<14/93`.  The function-field analogue has the same invariant gap:
assigning
degrees `32,32,11,11,7` to `a,c,r,p,e`, the common gcd has degree at most
`7`; after division, the term and radical degrees are at most shifted from
`107` and `93` by the same gcd degree.  Mason--Stothers therefore rules out
every scale-correct nonzero polynomial family.

The exact `e=0` rays are different and elementary.  Their cube
parameterization has `r=v^3`, `p=u^3`, with the remaining common scale in
`a,c`; divisor accounting gives only

```text
#{e=0 rays}<<Q^(1/3)*P^o(1)=P^(11/96+o(1)),        (2E.F7N8a)
```

well below the required raw `Q*P^o(1)` count.  Thus `abc` is invoked only
as a diagnostic for the nonzero residual bins, not for the exact rays.

This does **not** show that the desired average is equivalent to `abc`.
It shows that pointwise exclusion is an `abc`-level strategy.  No
counterfamily was found, but no unconditional averaged estimate improving
(2E.F7N7) to `Q*P^o(1)` is known here.  More importantly, this
one-dimensional bin is only a necessary obstruction: no implication from
its removal to sharp spacing, weighted HSM, `(SB)`, or FC has been proved.
Those theorems therefore remain open even after granting `abc`.  Ordinary
Mellin separation does not remove the shifted-cube obstruction:
the Mellin bandwidth is `N=R*S=q*L`, whereas the sampled output has length
`L`; Bessel/positive mean values lose the exact factor `N/L=q` and expand
back to the same shifted-product kernel.

#### Exact boundary of the conditional `abc` audit

The positive diagonal Fejer peak is not itself an `abc`-quality equation.
Huxley's fourth rational-points-near-a-curve theorem applies to the cubic
with determinant parameter `d=2`.  Its four primitive terms have `P`
exponents

```text
5/8, 5/8, 3/5, 25/72.
```

Thus the pure minor term leaves the floor `P^(5/8+o(1))`; standard `abc`
removes a lower-height range but does not lower this term.  Relative to the
transition target `P^(9/16)`, the remaining loss is exactly
`5/8-9/16=1/16`.  The audited Farey/Huxley decomposition therefore gives
only the conditional bound

```text
E_diag <<L*P^(1/16+o(1))=q^(35/66+o(1)),           (2E.F7N8b)
```

not `L*P^o(1)`.  The source is Huxley, *The rational points close to a
curve IV*, Bonner Math. Schriften 360 (2003), Theorem 1; see also
[Blomer--Schobel, Proposition 1](https://doi.org/10.7169/facm/2013.49.2.12)
for the stated form of the four terms.  The surviving transition has input denominator of
order `P`, approximation height `T=P^(9/16)`, and residual width
`H=P^(7/16)`.  Its primitive equation is

```text
A*u^3-B*P^3=D,       A,B~T, u~P, 0<|D|<=H.         (2E.F7N8c)
```

Both the term height and the permitted generic radical have exponent

```text
T*P^3=P^(57/16),
rad(A*B*u*P*D)<=T^2*P^2*H=P^(57/16).               (2E.F7N8d)
```

Thus this is exactly quality one.  If `P!=3` is prime, fixing `(A,D)`
leaves at most three Hensel lifts of
`u^3==D*inverse(A) (mod P^3)`.  Consequently

```text
R_transition<<T*H*P^o(1)=P^(1+o(1)),               (2E.F7N8e)
```

whereas the target is `T*P^o(1)=P^(9/16+o(1))`.  Standard `abc` applied to
(2E.F7N8c) forces only `|D|>=P^(7/16-o(1))`: it moves all surviving
solutions to the top residual shell and does not save the missing factor
`H`.

#### Fixed-denominator cubic energy: exact gains and exact remaining gap

There is a sharper formulation which respects the tangent packet
`u=P`, `A=B`.  For each `A~T`, let `r_A` count the transition solutions and
put

```text
R=sum_A r_A,                 E_2=sum_A r_A*(r_A-1).
```

Then Cauchy--Schwarz gives the exact sufficient reduction

```text
R^2 <=T*sum_A r_A^2=T*(R+E_2).                     (2E.F7N8e1)
```

Consequently `E_2<<T*P^o(1)` would prove `R<<T*P^o(1)`.  Unlike a raw
`H`-block square function, this fixed-denominator factorial energy is not
falsified by `u=P`, `A=B`: that packet has one point for each fixed `A`.
The factorial-energy estimate is sufficient, but it is not proved below.

Two solutions with the same `A` satisfy two exact identities.  With

```text
k=u_2-u_1,   c=B_2-B_1,   e=D_2-D_1,
Q=3*u_1^2+3*u_1*k+k^2,
```

subtraction and elimination of `A` give respectively

```text
A*k*Q-c*P^3=e,                                      (2E.F7N8e2)
P^3*(B_1*u_2^3-B_2*u_1^3)
       =D_2*u_1^3-D_1*u_2^3.                       (2E.F7N8e3)
```

For distinct ordered inputs, monotonicity makes `c>=1`, and (2E.F7N8e2)
forces

```text
k>>P/T=H=P^(7/16).                                  (2E.F7N8e4)
```

On `k~K` one has `c<<1+K/H`.  For fixed `(c,e)`, choosing the divisor pair
`(A,k)` of `c*P^3+e` fixes `Q`, and

```text
12*Q-3*k^2=(6*u_1+3*k)^2.
```

The divisor bound therefore proves

```text
#{same-A pairs with k~K}<<(H+K)*P^o(1).             (2E.F7N8e5)
```

After dyadic summation it closes all `K<=T` bins, as well as the
equal-residual stratum `e=0`, but summing the nonzero long-gap bins
`T<K<=P` gives only `P^(1+o(1))`.  The differenced equation
has discarded the absolute endpoint condition
`|A*u_1^3-B_1*P^3|<=H`.

The coherent zero-residual rays are target-controlled even in this energy.
Write `u/P=x/y` in lowest terms.  Then `D=0` is equivalent to

```text
y|P,                 y^3|A,                 B=(A/y^3)*x^3.
```

Since `x~y`, their square energy is at most

```text
T*sum_(y_1,y_2|P) y_1*y_2/lcm(y_1,y_2)^3
 <<T*P^o(1).                                           (2E.F7N8e6)
```

Writing `y_1=g*a`, `y_2=g*b`, `(a,b)=1`, changes the summand to
`1/(g*a^2*b^2)`; the logarithmic `g`-sum is absorbed in `P^o(1)`.

Exact cubic alternants give two further local spacings.  For three same-`A`
solutions in an interval of span `X`, the integer determinant with rows
`(1,u_i,B_i)` obeys

```text
P^3*det(1,u,B)=A*det(1,u,u^3)-det(1,u,D).
```

The main term is `asymp A*P*V_3(u)` and the error is `O(H*X)`.  Integrality
applies because the determinant cannot vanish: equality of the two secant
slopes would make the change of the cubic secant slope, which is
`>>P*X`, at most `O(H/A)`, whereas `A*P>>H`.  Therefore

```text
X>>(P^2/A)^(1/3)=P^(23/48).                         (2E.F7N8e7)
```

For six same-`A` solutions use the integer determinant with rows
`(1,u,u^2,B,uB,u^2B)`.  On its nonzero-alternant (minor) branch,
multiplication of the last three columns by `P^3` gives the main term
`A^3*V_6(u)` and error

```text
O(A^2*H*P^2*X^10+A*H^2*P^2*X^7+H^3*X^6).
```

The `P^2` in the one-error term is the degree-two Schur factor of the
five-column generalized Vandermonde.  In the two-error term, the wedge of
`u^j*D` and `u^k*D` supplies one gap, leaving the same `P^2`.  Thus the
display is uniform for `u~P`.  For `X<P^(39/80)` every displayed term is
`o(P^9)`, contradicting the integrality of a nonzero determinant.  Hence
the exact alternative is

```text
det=0 (a rational-quadratic packet),
or X>>(P^9/A^3)^(1/15)=P^(39/80).                   (2E.F7N8e8)
```

These facts still do not imply the factorial-energy estimate.  There is an
exact abstract configuration at the entire Huxley floor.  Let

```text
L=P^(3/8),        T=P^(9/16),        r=P^(1/16),
T*r=P^(5/8)=P/L.
```

Index the `P/L` critical `u`-cells by `0<=j<T*r`.  For each of the `T`
denominator labels `a`, put points in the `r` cells

```text
j=a+k*T,                  0<=k<r.                  (2E.F7N8e9)
```

Every critical cell contains one point.  Equal labels are separated by
`T*L=P^(15/16)`, farther than both determinant spacings.  At a dyadic
physical gap `K~J*T*L`, their pair count is `O(T*r*J)<<K`, so (2E.F7N8e5)
also holds with room.  Nevertheless the total incidence is
`T*r=P^(5/8)`, larger than the target by exactly `P^(1/16)`.  This is not an
arithmetic counterexample; it proves that the current gap and determinant
constraints cannot be combined combinatorially to obtain the missing
energy estimate.  A new estimate retaining both endpoint congruences, or
an equally strong arithmetic packet theorem, is still required.

The full spacing problem has a separate quality-one stratum.  Multiplying
the nearest-integer relation gives

```text
q^3*w-2*t*z^2=e,       z~q^2, w~t*q.               (2E.F7N8f)
```

The `t=0` product strip contributes `O(P^2*q^o(1))`, and exact `e=0` with
`t!=0` is impossible because `q^3` is coprime to the second coefficient.
For generic `t=1`, squarefree `w,z`, and unit residual, however, both height
and radical may have exponent four in `q`.  Hence `abc` does not improve the
remaining nonzero spacing levels to the sharp `P^2` endpoint.

Finally, for two fixed row vertices and two common neighbors, put

```text
Phi=u^T*K*v',       Psi=u'^T*K*v.
```

Taking determinants of `U^T*K*V`, where `U=[u,u']` and `V=[v,v']`, gives
the exact identity

```text
J^2+Delta*det(E)=Phi*Psi.                           (2E.F7N8g)
```

Here `J^2` has size at least `q^2`, while the correction is at most
`D^3=q^(48/33)=o(q^2)`.  A generic squarefree `Phi*Psi` already has radical
of full height, so (2E.F7N8g) is again quality one.  Standard `abc` neither
rules out a one-point-per-secant Sidon transversal nor forces tangent-chart
reuse across row pairs.  Sharp spacing, the positive diagonal target,
weighted HSM, `(SB)`, and FC consequently all remain open under this
conditional audit.

#### Hostile audit of the cross-cusp Kuznetsov proposal

There is a numerically favorable but presently conditional cross-cusp
reformulation.  In the balanced ledger put

```text
N=R*S=q^(50/33),       J=K=q^(42/33),
X=J*K=q^(84/33),       B_0=X/N=q^(34/33),
Q_delta=sqrt(N)=q^(25/33).                         (2E.F7o20a)
```

The Bezout identity `R*V-S*U=1` makes `R,S` coprime.  The cusps represented
by `U/R` and `V/S` are opposite exact-divisor cusps of `Gamma_0(N)`, with
widths `S` and `R`.  Canonical Atkin--Lehner scaling absorbs those widths.
Indeed, [Kiral--Young, Theorem 2.7](https://arxiv.org/abs/1710.00914),
specialized with `p=q=1,u=R,v=S`, has allowed geometric moduli
`c*sqrt(N)` with `(c,N)=1` and reduces the cross-cusp Kloosterman sum to an
ordinary Kloosterman sum of modulus `c`, up to the displayed fixed scaling
phases.  Thus there is no power loss caused merely by the unequal cusp
widths.  For one fixed cusp and one fixed scalar sequence, the regular
spectral large sieve has the usual cusp-normalized constant
`T_spec^2+M/N`; see, for example, Lemma H in
[Pascadi](https://arxiv.org/abs/2404.04239).

This does **not** prove the needed data-side estimate.  The exact expanded
correlation before a delta method is

```text
C_h=sum_(r,r',s,s') alpha_r*conj(alpha_r')
                    *beta_s*conj(beta_s')
    *sum_(j*k-j'*k'=h) U(j)*conj(U(j'))*V(k)*conj(V(k'))
    *e(-U0*(r*j-r'*j')/R-V0*(s*k-s'*k')/S)*Psi.   (2E.F7o20b)
```

Here `r,r'` range over `P=sqrt(D)` physical row-fan translations and
`s,s'` over `Q=sqrt(D)` color-fan translations.  A scalar large-sieve
operator `T:ell^2(I)->L^2(Pi,dmu)` does formally tensor with a Hilbert
space `H`:

```text
int_Pi ||sum_i rho_pi(i)*a_i||_H^2 dmu(pi)
 <=||T||^2*sum_i||a_i||_H^2.                       (2E.F7o20c)
```

Thus the fan indices would be free if they survived every transformation
as external orthogonal coordinates, or entered only through a fixed unitary
diagonal modulation.  Formula (2E.F7o20b) has not been put in that form.

The raw Poisson congruence shows both the positive CRT fact and the exact
aliasing obstruction.  On the row side it has the shape

```text
n==U*r*c-a*k*R (mod c*R).                          (2E.F7o20d)
```

For `(a,c)=(c,R)=(U,R)=1`, reduction modulo `R` recovers `r`, and reduction
modulo `c` recovers `k mod c`.  Hence

```text
(r mod R,k mod c) -> n mod cR
```

is a bijection: there is no hidden collision between the two fundamental
residue coordinates.  But the actual dual interval has length

```text
K/c=q^(42/33-25/33)=q^(17/33),                     (2E.F7o20e)
```

and `k` and `k+c` give the same residue in (2E.F7o20d).  The color side has
the identical folding.  The joint alias multiplicity is therefore

```text
(J/c)*(K/c)=q^(34/33)=B_0.                         (2E.F7o20f)
```

For each fixed `c`, full CRT/Fourier coordinates can record the quotient as
an additional index.  They do not make it disappear.  Moreover the CRT
permutation depends on the delta modulus `c`, which is precisely the
variable later consumed by Kuznetsov.  A single external Hilbert coordinate
valid through the `c`-sum requires an explicit intertwining identity.  The
cross-cusp Kloosterman formula identifies the scalar kernel after this
reorganization; it does not itself prove that the quotient indices remain
orthogonal.  Bounding the residue-folding map directly costs
`sqrt(K/c)` on each side, hence `B_0` in the squared data estimate.

There is a second functional-analytic gap.  If a hoped-for spectral formula
factorizes `A_pi` into row- and color-cusp transforms at the same `pi`,
ordinary Hilbert tensorization controls the product spectral space
`Pi x Pi`, not restriction to its diagonal.  With harmonic weights `w_pi`,
the product of two scalar large-sieve estimates controls
`sum_pi w_pi^2|U_pi*V_pi|^2`, whereas the desired Kuznetsov norm contains
one `w_pi`.  Recovering it by a minimum-weight bound can cost the inverse
harmonic weight, of level size `N`; it is not a formal Bessel step.  For the
continuous Eisenstein measure the same issue is the elementary failure of
`||U*V||_2<=||U||_2||V||_2`.  An exact representation of `A_pi` as one
linear spectral coefficient could avoid this diagonal loss, but no such
formula has been proved here.

The exponent threshold has zero room for either loss.  A schematic
expansion

```text
C_h^circ=sum_pi^harm lambda_(pi,a)(h)*A_pi(alpha,beta)+Eis
```

followed by the shift-side large sieve would close if one proved the strong
data estimate

```text
sum_pi^harm|A_pi|^2+Eis
 <<q^o*||alpha||_2^4*||beta||_2^4*X^(4/3).         (2E.F7o20g)
```

Since `||alpha||_2^2=P`, `||beta||_2^2=Q`, its final exponent would be

```text
P*Q*X^(2/3)*sqrt(B_0)=q^(89/33),                  (2E.F7o20h)
```

below the target `P*Q*X=q^(100/33)`.  The weakest usable local lift is

```text
sum_pi^harm|A_pi|^2+Eis
 <<q^o*||alpha||_2^4*||beta||_2^4*X^2/B_0.         (2E.F7o20i)
```

Its right side has exponent `q^(166/33)`; taking its square root and then
the shift large sieve gives

```text
q^(83/33)*q^(17/33)=q^(100/33),                   (2E.F7o20j)
```

exactly the target, with no polynomial slack.  Paying the raw joint alias
factor `B_0` raises the final exponent to `q^(117/33)`.  Paying an inverse
harmonic weight of size `N` raises it to `q^(125/33)`.  Consequently
(2E.F7o20i) is a new vector-valued, cross-cusp local-lift theorem, not a
formal consequence of scalar Kuznetsov, Hilbert tensorization, or finite
Fourier orthogonality.  The favorable exponent ledger is correct; the
cross-cusp closure is **conditional** on proving that theorem (including its
Eisenstein part).

There is a useful conditional Hecke fold, but the current conductor-lowered
kernel has not reached its hypotheses.  Suppose one had the exact identity

```text
A_pi=(sum_(m<=Y) a_m*lambda_pi(m))
     *(sum_(n<=Y) b_n*lambda_pi(n)),
Y=N/J=N/K=sqrt(D).                                 (2E.F7o20k)
```

For a newform, away from the level,

```text
lambda_pi(m)*lambda_pi(n)
 =sum_(d|(m,n),(d,N)=1)lambda_pi(m*n/d^2).         (2E.F7o20l)
```

The ramified local relation is even sparser.  Therefore (2E.F7o20k) folds
to one Hecke polynomial

```text
A_pi=sum_(ell<=Y^2=D)c_ell*lambda_pi(ell),
sum_ell|c_ell|^2<<q^o*||a||_2^2*||b||_2^2.         (2E.F7o20m)
```

The norm bound is just Cauchy on each multiplication fibre and the
`q^o(1)` divisor bound.  The ordinary level-`N` spectral large sieve then
costs `N+D=asymp N`.  Since

```text
X^2/B_0=X*N,                                       (2E.F7o20n)
```

this is exactly the arithmetic scale required by the weak lift
(2E.F7o20i), after restoring its archimedean normalization.  At the two
exact-divisor cusps, level-`N` newform coefficients differ from the
infinity coefficients only by Atkin--Lehner signs, so cusp width does not
invalidate this conditional fold.

The word **conditional** is essential.  The present delta/Poisson output
has not been shown to equal (2E.F7o20k) with two fixed, `c`-independent
coefficient sequences.  For oldforms, Kiral--Young Lemma 2.5 permutes the
oldclass coefficient lists between Atkin--Lehner cusps rather than
identifying every chosen oldvector with one scalar Hecke list.  This may be
resolvable with a `q^o(1)` local matrix calculation, but that calculation is
not supplied.  Eisenstein coefficients carry cusp/scattering indices; an
analogous continuous Hecke fold and its Plancherel normalization also have
to be proved.  Neither follows merely by quoting the newform Hecke identity.

The inter-modulus CRT operator has an exact coherent subspace that explains
why (2E.F7o20k) is not automatic.  In normalized phase coordinates the raw
row transform sends `(r,k)` to

```text
theta_(c,a)(r,k)=U*r/R-a*k/c (mod 1).              (2E.F7o20o)
```

On fundamental residues its normalized finite-Fourier pullback is

```text
(U_(c,a)x)(y)=(cR)^(-1/2)
 *sum_(r mod R,k mod c)x_(r,k)*e(y*theta_(c,a)(r,k)),
y mod cR.                                          (2E.F7o20o')
```

CRT makes this unitary for each fixed `(c,a)`.  On the actual long interval
`K=cL`, the quotient `t=floor(k/c)` must be appended as an archimedean
coordinate; it is not part of the finite CRT isometry.

Thus its ideal cross-Gram kernel has support on

```text
theta_(c,a)(r,k)=theta_(c',a')(r',k') (mod 1).     (2E.F7o20p)
```

In particular, fix `a=a'`, `r=r'` and put

```text
k=t*c,                  k'=t*c'.                   (2E.F7o20q)
```

Then (2E.F7o20p) holds exactly for every pair `c,c'`.  In the unnormalized
residue (2E.F7o20d),

```text
n=U*r*c-a*k*R=c*(U*r-a*t*R),
n/c=U*r-a*t*R,                                    (2E.F7o20r)
```

so conductor lowering preserves, rather than removes, this coherent ray.
For `c` in a dyadic block of size

```text
C=Q_delta=q^(25/33)
```

and `t asymp K/C=q^(17/33)`, the indices `k=t*c` remain in the active
length-`K` dual block.  Taking, for example, pairwise distinct primes `c`
in the dyadic interval makes the rays distinct on the data side while their
conductor-lowered output is identical.  After identifying
`e_(r,tc)` with `e_(r,tc')`, the kernel `U_c^*U_c'` contains the identity on
this `(r,t)` subspace.  Consequently the Gram operator of a family of
`C*q^o(1)` such moduli has eigenvalue

```text
C*q^o(1)=q^(25/33+o(1)).                           (2E.F7o20s)
```

The proposed inter-modulus large sieve needs a squared saving `q^(1/11)`,
namely Gram constant

```text
C/q^(1/11)=q^(22/33).                              (2E.F7o20t)
```

It is therefore false as a coefficient-blind operator inequality on the raw
CRT transforms.  A complete delta-numerator sum or a separately subtracted
main/coherent channel could conceivably cancel (2E.F7o20q), but such a
cancellation is additional arithmetic input.  Finite Fourier orthogonality
and the individual isometry of every CRT permutation do not provide it.
Thus the Hecke fold (2E.F7o20m) is a valid repair **if** the exact product
formula (2E.F7o20k) is first proved after removing this coherent subspace;
the raw inter-modulus transform does not prove that formula.

There is a further normalization gate before a Farey or Burgess repair can
be applied to this operator.  Put

```text
n=j*k-j'*k'-h,       C=sqrt(N)=q^(25/33).
```

In a standard DFI normalization the exact delta symbol is

```text
1_(n=0)=c_C/C^2 *sum_(c>=1) sum_(a mod c)^*
 e(a*n/c)*H_DFI(c/C,n/C^2),       c_C=1+O_A(C^(-A)). (2E.F7o20u)
```

On `c asymp C`, its coefficient can be written exactly as

```text
C^(-2)*H_DFI(c/C,n/C^2)
 =(c*C)^(-1)*[(c/C)*H_DFI(c/C,n/C^2)].             (2E.F7o20v)
```

Thus the numerator completion has a reciprocal `1/c` weight and an outer
`1/C` average.  Moreover `K_L(x,x-h)=L*K(x/X,h/B_0)` up to rapidly decaying
tails.  Inserting the harmless mismatch cutoff `|n|<<B_0` makes
`n/C^2<<B_0/N=D^(-1)`, but the exact DFI sum still contains every lower
dyadic modulus block allowed by `H_DFI`; it is not an identity using only
`c asymp C`.  Replacing it by a top Farey family is a Jutila approximation,
whose circle-approximation error has to be paired with the fourth moment of
the product polynomial.  No such error estimate has been supplied.

The exact one-row Poisson formula also retains its archimedean scale.  For
a smooth length-`J` cutoff `W`,

```text
sum_j W(j/J)e(j*(a*k/c-U*r/R))
 =J*sum_(nu==U*r*c-a*R*k mod c*R)
       W_hat(J*nu/(c*R)).                            (2E.F7o20w)
```

If Poisson is performed after splitting into residues, the lattice
prefactor is `J/(cR)` and the complete residue sum restores `cR`.  Relative
to the normalized transform (2E.F7o20o'), the multiplier is therefore
`J/sqrt(cR)`, not one.  At the balanced point the complete list is

```text
L=q^(17/33), C=R=q^(25/33), c*R=q^(50/33),
J=K=q^(42/33), B_0=q^(34/33),
C^(-2)=q^(-50/33), J/(cR)=q^(-8/33),
J/sqrt(cR)=q^(17/33), K/c=q^(17/33).               (2E.F7o20x)
```

Stopping here would be misleading, however.  For a fully separable smooth
term the second Poisson transform cancels the first-step quotient exactly.
If `(c,R*S)=1`, `(a,c)=1`, and

```text
T_(c,a)(r,s)=sum_(j,k) W_1(j/J)W_2(k/K)
 e_c(a*j*k)e_R(-U_0*r*j)e_S(-V_0*s*k),
```

then two-dimensional Poisson and the complete bilinear sum give

```text
T_(c,a)(r,s)=J*K/c
 *sum_(nu==U_0*r*c mod R) sum_(mu==V_0*s*c mod S)
 W_1hat(J*nu/(cR))*W_2hat(K*mu/(cS))
 *e_c(-a_bar*(R*S)^(-1)*nu*mu).                   (2E.F7o20y)
```

Indeed the raw Poisson prefactor is `J*K/[(cR)(cS)]`.  The complete sum
vanishes unless the two displayed congruences hold, and on their support it
is `c*R*S` times the displayed phase.  Its exponent is `75/33`, while the
raw prefactor has exponent `-16/33`; their product `J*K/c` has exponent
`59/33`.  Thus `floor(k/c)` and the apparent `K/c` alias in a one-row
transform are not final obstructions for the fully transformed top-`c`
interior term.  The finite test in `qp_four_cycle_weighted_secant_lab.py`
checks this complete sum directly.

Formula (2E.F7o20y) also corrects the zero-mode diagnosis.  Combining two
copies with the delta numerator gives, with
`Delta=nu*mu-nu'*mu'`,

```text
1/c*sum_(a mod c)^*
 e_c(-a*h-a_bar*(R*S)^(-1)*Delta)
 =S(-h,-(R*S)^(-1)*Delta;c)/c.                    (2E.F7o20z)
```

A zero product on only one transformed side is therefore a nondegenerate
Kloosterman sum whenever the other product and `h` are nonzero modulo `c`;
it is not the one-sided Ramanujan term obtained by stopping after the first
Poisson step.  When `Delta==0 (mod c)`, (2E.F7o20z) is `c_c(h)/c`.  The
case `h==Delta==0 (mod c)` is the major term `phi(c)/c` and must be
extracted with the product diagonal.  These degenerate axes, including
their gcd factors, have not yet been summed uniformly.

Combining (2E.F7o20v), two copies of (2E.F7o20y), and the numerator sum
gives the exact top-block scalar normalization

```text
1/C * (J*K/c)^2
 *[S(-h,-(R*S)^(-1)*Delta;c)/c]                   (2E.F7o20z1)
```

times the four Fourier weights and the smooth DFI bracket.  The prefactor
outside the normalized Kloosterman sum has exponent `93/33=31/11`; a
nondegenerate Weil estimate for `S/c` contributes `q^(-25/66+o(1))`, before
the transformed frequency sums and their gcds.  This is an identity-level
normalization, not a bound for HSM.

Even a favorable first support lemma does not by itself finish this top
block.  Let `n_c,m_c` be the row and color support sizes in (2E.F7o20y).
Grant the elimination bounds

```text
sum_c n_c^2<<P^2*q^o,       sum_c m_c^2<<Q^2*q^o,
sum_c n_c*m_c<<P*Q*q^o,                             (2E.F7o20z2)
```

and also grant fixed-`c` numerator Parseval plus divisor multiplicity for
the short product transform `B_(c,a)`:

```text
sum_(a mod c)^*|B_(c,a)|^2<<c*n_c*m_c*q^o.
```

Since `T_(c,a)=(J*K/c)B_(c,a)`, the exact delta normalization gives only

```text
1/C*sum_c (J*K/c)^2*(1/c)sum_a|B_(c,a)|^2
 <<P*Q*(J*K)^2/C^3*q^o=q^(109/33+o(1)).            (2E.F7o20z3)
```

The correlation target is `P*Q*J*K=q^(100/33)`.  Thus support Cauchy and
fixed-`c` Parseval still miss by

```text
J*K/C^3=q^(9/33)=q^(3/11).                         (2E.F7o20z4)
```

Closure at this level requires

```text
sum_c n_c*m_c<<P*Q*C^3/(J*K)*q^o=q^(7/33+o(1)),   (2E.F7o20z5)
```

which is exactly the random joint row/color intersection scale, rather
than the Cauchy scale `P*Q=q^(16/33)`.  Nondegenerate Weil cancellation may
handle part of the difference; the `Delta==0` Ramanujan axes require their
own joint inter-modulus estimate.  Neither estimate is presently proved.

In fact the support-only target in (2E.F7o20z5) is uniformly false.  Choose
an odd `R`, and put

```text
S=R+1, c=S+1=R+2, U=R-1, V=R;       R*V-S*U=1.
```

Then `c==2 (mod R)` and `c==1 (mod S)`, while `U==-1 (mod R)` and
`V==-1 (mod S)`.  Hence the two frequency congruences in (2E.F7o20y) are

```text
nu==-2r (mod R),                 mu==-s (mod S).   (2E.F7o20z6)
```

For windows `|nu|<=P`, `|mu|<=Q`, with `2P<R` and `Q<S`, this single
admissible modulus has

```text
n_c>=floor(P/2),       m_c=Q,       n_c*m_c>>P*Q. (2E.F7o20z7)
```

Its exponent is `16/33`, exceeding the requested aggregate exponent
`7/33` by exactly `3/11`.  Thus averaging support sizes cannot close the
top block.  Cancellation in the completed numerator/shift Kloosterman sum,
including its Ramanujan degeneracies, is essential.  The finite aligned
fixture is checked in `qp_four_cycle_weighted_secant_lab.py`.

For significant frequencies `|nu|,|mu|<<c`, the literal condition `nu=0`
forces `r=0`, and similarly `mu=0` forces `s=0`.  Flat fan coefficients
would then gain one fan out of `P=q^(8/33)`.  The weighted data estimate
(2E.F7o20g) is uniform in `alpha,beta`, which may concentrate on those
fans, so that density is not by itself an operator-norm saving.  It remains
a plausible separate simplification for the unweighted slope-block count.

The `1/c` in (2E.F7o20v) also changes a gcd/Farey multiplicity.  If

```text
c=d*q_0, k=d*kappa, (kappa,q_0)=1,
```

then reduction of primitive numerators from modulus `d*q_0` to `q_0` has
`phi(d*q_0)/phi(q_0)` lifts, but

```text
1/(d*q_0) * phi(d*q_0)/phi(q_0)
 =1/q_0 * phi(d*q_0)/(d*phi(q_0)) <=1/q_0.         (2E.F7o20aa)
```

Consequently a raw `d`-fold representation count and a completed
numerator estimate are not interchangeable.  After (2E.F7o20y), the native
gcd is instead the gcd of `h`, `Delta`, and `c` in the Kloosterman sum.
Any Farey decomposition must therefore be rederived in the transformed
`nu*mu` variables with (2E.F7o20v) and all archimedean weights present.

The resulting audit is therefore

```text
exact DFI-to-top-Farey replacement:              NOT PROVED;
DFI/Jutila approximation error:                  NOT ESTIMATED;
full top-c two-dimensional Poisson identity:      VERIFIED EXACT ALGEBRA;
raw first-step quotient/alias obstruction:        REMOVED FOR THAT TERM;
Kloosterman/Ramanujan zero-axis sum:               NOT ESTIMATED;
Farey/a-sum and c-Burgess intertwining:           NOT PROVED;
stationary boundary/nonstationary B-process:      STILL OPEN;
oldform and Eisenstein/scattering completion:     STILL OPEN;
high-step HSM or slope-block theorem from route:  NOT PROVED.          (2E.F7o20ab)
```

A single smooth slope-strip cutoff can supply the separable archimedean
functions required by (2E.F7o20y), so it is a genuine possible repair of
the raw quotient problem.  It does not by itself separate the DFI weight
`H_DFI(c/C,n/C^2)`, cover the lower modulus blocks, or control the original
stationary boundary and minor-mask terms.  The transformed congruences and
weights in (2E.F7o20y) also still vary with `c`; an explicit common
multiplication representation is required before the `c`-sum is a Burgess
character sum.  Using a positive majorant without that identity would
restore the old triangle-inequality fan loss.

For completeness, arbitrary weights really can defeat (2E.F7o16), but this
is only a **method counterexample**.  Put `H=q/D=L` and, inside the balanced
dual box, support unit weights on

```text
(j_t,k_t)=(J_0+t,J_0-t),             |t|<=c*H.     (2E.F7o21)
```

Shift `J_0` and delete `O(1)` points so all retained pairs are minor.  Since
`H<R,S`, this deletion does not change the scale.  The products
`j_t*k_t=J_0^2-t^2` lie in an interval of length

```text
H^2=q^2/D^2=B_0,                                  (2E.F7o22)
```

so, for sufficiently small fixed `c`, their phases remain in one fixed arc
for every `ell asymp L`.  Hence the left side of (2E.F7o12) is
`asymp L*H^2`, while its diagonal is `asymp L*H`, a loss `H=q/D`.
The support (2E.F7o21) is correlated and is not of the separable form
`u(j)v(k)` (nor is it asserted to come from a primal determinant strip).
It therefore rejects a hereditary arbitrary-weight proof of `(*)`, not the
actual separable minor theorem.

Controlling the remaining *near* resonances is therefore a weighted,
trace-sensitive shifted cubic-root-product cancellation problem in
(2E.F7m).  Thus
the common-basis reduction proves that the old raw-band loss was artificial,
while also proving that absolute Poisson/stationary phase does not establish
the local fan bound or `(SB)`.  No cancellation estimate for (2E.F7m) is
claimed here.

Nor can the missing estimate be replaced by a geometry-only four-point
determinant bound for each pair of arithmetic fans.  The superficially
natural local claim

```text
E_fan <<q^o(1+D/(R*S)+(D/q)*L_a*L_c)               (2E.F7p)
```

is false without the actual prime-centre arithmetic.  Let `n>=2` and put

```text
R=n^33,       m=R^2=n^66,       q=2m,
T=n^8,        D=4T^4=4n^32.                       (2E.F7q)
```

Thus `D=asymp q^(16/33)` and `T=asymp q^(4/33)`.  On two oppositely
ordered step-`R` fans, pair only equal indices and take

```text
a_i=m+R*i,       c_i=m-R*i,       b_i=m+i^2,
1<=i<=T.                                             (2E.F7r)
```

The carrier absorbs the entire quadratic curvature, since

```text
(m+R*i)(m-R*i)(m+i^2)=m^3-m*i^4.                   (2E.F7s)
```

Consequently all `T` pairs satisfy

```text
|8*a_i*b_i*c_i-q^3|=8m*i^4<=qD,                    (2E.F7t)
```

whereas the right side of (2E.F7p), before its `q^o(1)` factor, is

```text
1+D/R^2+(D/q)*T^2=1+4*n^(-34)+2*n^(-18)<2.         (2E.F7u)
```

The support in (2E.F7r) is a matching, so it contains no four-edge
rectangle.  A four-point determinant or dependent-random-choice argument
therefore sees nothing, while the local count grows like `q^(4/33)`.
This is a rigorous method barrier, not a disproof of `(SB)`: its centre
`q=2R^2` is even and composite, its nodes are unrestricted integers, and
the two projection fans are not asserted to be actual prime-power slope
vertices in one relevant block.  In particular, the odd-prime centre is
not a cosmetic hypothesis in any valid replacement for (2E.F7p).

### Stable opposite-fan polynomial arcs and the exact missing covering

There is a sharp positive statement for each polynomial major arc.  Put

```text
a(t)=A+R*t,       c(t)=C-S*t,
b(t)=B+L*t+K*t^2.                                  (2E.F7v)
```

with all three factors positive and comparable to `q` on the occupied
indices.  Write `X=R*C-A*S`.  Direct multiplication gives

```text
a(t)b(t)c(t)=c_0+c_1*t+c_2*t^2+c_3*t^3+c_4*t^4,
c_0=A*B*C,
c_1=A*C*L+B*X,
c_2=A*C*K+L*X-B*R*S,
c_3=K*X-L*R*S,
c_4=-K*R*S.                                        (2E.F7w)
```

For a real polynomial of fixed degree `d`, leading coefficient `lambda`,
and `N` distinct integer arguments on which `|P|<=M`, divided differences
at `d+1` ordinally well-separated arguments give

```text
N<<_d 1+(M/|lambda|)^(1/d).                         (2E.F7x)
```

Consequently, if `K!=0`, the legal residual window proves

```text
N_arc<<1+(q*D/(R*S*|K|))^(1/4).                     (2E.F7y)
```

For indices in an arithmetic progression of spacing `h`, the second term
is divided by `h`.  This is sharp in power on (2E.F7r): there
`R*S=asymp q`, `K=1`, and (2E.F7y) is `D^(1/4)=q^(4/33)`.

If `K=0`, the stronger tangent bound follows without a determinant method.
For

```text
phi(t)=log(a(t)b(t)c(t))
```

one has exactly

```text
phi''(t)=-R^2/a(t)^2-S^2/c(t)^2-L^2/b(t)^2
        <<-(R^2+S^2+L^2)/q^2.                      (2E.F7z)
```

The product window gives `|phi(t)-3log(q/2)|<<D/q^2`.  If three occupied
arguments `x<y<z` are chosen, strong concavity bounds
`(y-x)(z-y)<<D/(R^2+S^2+L^2)`.  Choosing the middle occupied argument
therefore gives the uniform count

```text
N_arc<<1+sqrt(D/(R^2+S^2+L^2))
      <<1+sqrt(D/(R*S)).                             (2E.F7aa)
```

Thus every linear-carrier arc is already a tangent/Knapp contribution.
The estimate does not require its occupied indices to be consecutive.

The exact quartic resonance in (2E.F7r) also has a prime-power
non-embedding theorem.  If the three lower coefficients in (2E.F7w)
vanish, then

```text
R*C=A*S,             L=0,             K*A*C=B*R*S.  (2E.F7ab)
```

Indeed, if `X!=0`, the equations `c_1=c_3=0` give
`L=-B*X/(A*C)` and `K=-B*R*S/(A*C)`; substitution in `c_2=0` gives the
impossible equality

```text
B*(2*R*S+X^2/(A*C))=0.
```

Suppose both affine fans in (2E.F7v) contain two distinct actual shell
prime powers.  Distinct project-shell prime powers are coprime, so

```text
gcd(A,R)=gcd(C,S)=1.                                (2E.F7ac)
```

The first equation in (2E.F7ab) then gives both `A|C` and `C|A`, hence
`A=C` and `R=S`.  The last equation gives

```text
A^2|B.                                              (2E.F7ad)
```

If the resonance centers `A,B,C` themselves lie in the project shell, its
endpoint ratio is strictly below two, whereas `B/A>=A>=2`.  Therefore a
centered exact quartic opposite-fan resonance cannot contain two actual
nodes on both sides.  This excludes the exact model (2E.F7r); it does not
exclude a shifted-center or genuinely approximate quadratic-carrier arc.

There is a precise stability limit to the last argument.  Interpolation of
`N` well-spread occupied points only gives

```text
|c_j|<<q*D/N^j.                                     (2E.F7ae)
```

At `N=D`, the cubic coefficient is bounded by

```text
q*D/D^3=q/D^2=q^(1/33),
```

not by a number below one.  Forcing it to vanish by integrality needs

```text
N>(q*D)^(1/3)=q^(49/99),
D=q^(48/99),                                        (2E.F7af)
```

a power miss of `q^(1/99)`.  Finite differences alone therefore do not
upgrade an approximate major arc to (2E.F7ab) at the active scale.

For clarity, the exact new sufficient input can be stated as follows.

```text
(PAC) In every reduced row-fan/color-fan pair, after the random-volume
      part is removed, all occupied points are covered by q^o(1)
      affine tangent packets or opposite-fan polynomial arcs (2E.F7v).
      Affine packets with the same rational tangent data are merged
      before they are counted.                                  (2E.F7ag)
```

Assuming `(PAC)`, the exponent ledger closes.  If `R,S` are the two
physical fan steps, the fan counts obey

```text
F_R<<1+D*R/q,       F_S<<1+D*S/q,       F_R*F_S<<D. (2E.F7ah)
```

The random-volume terms sum by the fan length budgets to

```text
(D/q)*(sum L_a)*(sum L_c)<<D^3/q=D^(15/16).         (2E.F7ai)
```

For the nonlinear arcs put `x=D*R/q`, `y=D*S/q`.  The reduced range is
`D/q<<x,y<<sqrt(D)`.  Equations (2E.F7y) and (2E.F7ah) give

```text
F_R*F_S*(q*D/(R*S))^(1/4)
 <<(D^3/q)^(1/4)*(1+x)*(1+y)*(x*y)^(-1/4)
 <<D^(63/64).                                       (2E.F7aj)
```

The last maximum occurs at `x=y=sqrt(D)`; in `q`-powers it is
`D^(3/2)q^(-1/4)=q^(21/44)`.  The one-per-packet term in (2E.F7y) sums to
`O(D)`, and (2E.F7aa), together with the affine-packet merger in `(PAC)`,
also sums to `O(D)`.  Hence

```text
(PAC) => E_ij<<D*q^o(1),                            (2E.F7ak)
```

which is exactly `(SB)`.

The implication (2E.F7ak), the arc sublevel estimates (2E.F7y) and
(2E.F7aa), and the exact-prime exclusion (2E.F7ab)--(2E.F7ad) are proved.
`(PAC)` itself is **not proved**.  Current approximate determinant results
do not supply it.  For example, applying Adiceam--Marmon Theorem 2.1 after
fixing one compatibility line has `n=3`, `k=3`, residual exponent
`gamma=49/33`, and covering exponent

```text
theta=(3/2)^2/(3-49/33)=297/200.                    (2E.F7al)
```

This is not `o(1)`.  Moreover the homogenized product form is `q`-dependent
and singular at infinity, outside that theorem's fixed nonsingular
hypotheses.  Exact rational-point covering theorems do not count the `qD`
neighborhood.  Thus `(PAC)` is the remaining theorem, not a consequence
silently available from the determinant-method literature.

### Exact four-point cell barrier and uniqueness in the quartic model

The most direct multiscale determinant covering can be audited exactly.
In one reduced fan pair write

```text
a=A+R*m,          c=C+S*n,          b=q^3/(8*a*c)+epsilon,
|epsilon|<<D/q,                                      (2E.F7am)
```

where signs may be absorbed into `R,S` and all factors are comparable to
`q`.  For four occupied points in an index rectangle of side lengths
`H,K`, the determinant with rows `(1,m,n,b)` is an integer.  The cofactors
of its last column are `O(H*K)`.  After subtracting the affine Taylor
polynomial of `q^3/(8ac)`, its second derivatives have respective sizes
`O(R^2/q)`, `O(R*S/q)`, and `O(S^2/q)`.  Hence

```text
|det(1,m,n,b)|
 <<(H*K/q)*(D+R^2*H^2+R*S*H*K+S^2*K^2).            (2E.F7an)
```

In particular, for a sufficiently small absolute constant `c`,

```text
H*K*(D+R^2*H^2+R*S*H*K+S^2*K^2)<c*q               (2E.F7ao)
```

forces exact coplanarity of every four occupied points in the cell.  Thus
four is the exact rich-cell threshold for this argument; cells below that
threshold still have to be paid for individually.

Put `u=R*H`, `v=S*K`.  Condition (2E.F7ao) becomes, up to constants,

```text
u*v*(D+u^2+u*v+v^2)<q*R*S.                          (2E.F7ap)
```

Since `R*S>=1` and `D=q^(16/33)`, one has `q*R*S>D^2`.  The continuous
optimization in `u,v` therefore gives the upper bound

```text
H*K<<sqrt(q/(R*S)),                                 (2E.F7aq)
```

attained up to constants in the balanced worst case `R=S=1`.  This is only
`q^(1/2)`, whereas a random-volume cell has index area
`q/D=q^(17/33)`.  Consequently even the best possible charge for cells
containing at most three points is

```text
M*N*sqrt(R*S/q),                                    (2E.F7ar)
```

instead of the random-volume target `(D/q)M*N`.  Already at `R*S=1` their
ratio is

```text
(sqrt(q)/D)=q^(1/66).                               (2E.F7as)
```

For the maximal box `M=N=D`, the two exact powers are

```text
D^2/sqrt(q)=q^(31/66)=D^(31/32),
D^3/q       =q^(5/11) =D^(15/16).                  (2E.F7at)
```

Thus the local coplanarity criterion is positive, but a cell-by-cell
rich/sparse argument misses the random remainder by `q^(1/66)`.  This is a
barrier to that proof method, not an obstruction to `(SB)`: points in
different sparse cells can share global affine data.  Indeed the quartic
matching (2E.F7r) lies on the single index line `m=n`, so all of its graph
points lie in one global plane even though its optimal local cells can be
sparse.  A successful multiscale proof would have to recover precisely
this cross-cell alignment.

There is a complementary exact uniqueness statement inside that explicit
model.  Retain

```text
R=N^33,       m=R^2=N^66,       q=2m,
T=N^8,        D=4T^4,
```

and move from the central index line to the positive parallel line
`y=x+k`, where `1<=x,k<=T`.  The natural integral carrier is

```text
b=m+R*k+x^2+x*k+k^2.
```

Direct multiplication gives

```text
a*b*c-m^3=-R^2*Q(x,k),
Q=R*k^3+2R*k^2*x+2R*k*x^2
  +k^3*x+2k^2*x^2+2k*x^3+x^4.                      (2E.F7au)
```

The original product window is exactly `Q<=D/4=T^4`.  Positivity gives

```text
Q(x,k)>=Q(1,1)=5R+6>T^4,
```

because `R=N^33` and `T^4=N^32`.  Moreover, throughout this box,

```text
2m*Q(T,T)<(m+R*T)*(m-2R*T)<=a*c.
```

Therefore this displayed `b` is the unique nearest integer to `m^3/(ac)`;
since even it misses the window, no other integral carrier can restore a
legal point.  The central line `k=0` remains legal through `x=T`, with
`Q(x,0)=x^4`.  Hence the high-step family has no nontrivial positive
parallel quartic copy in the audited quadrant.  This is a uniqueness
result for (2E.F7r), not a general arc-covering theorem and not a proof of
`(PAC)` or `(SB)`.

### Weighted cell decomposition and the exact low/high-step cutoff

The cell argument has an overlap-free weighted form, but it is important
not to identify its rich part with the polynomial arcs above.  Fix one
reduced fan pair and let `E` be its occupied triples `(m,n,b)`.  Start with
any **already certified** list of coherent/tangent packets and polynomial
arcs.  Order the list once and assign an edge to the first packet containing
it.  This makes their assigned edge sets disjoint without increasing any
per-packet count.  Remove their union and call the residual set `E_0`.

Tile the index plane by half-open `H`-by-`K` cells satisfying (2E.F7ao).
There are no boundary overlaps.  Declare a residual cell rich if it
contains at least four points, put all points of those cells in `E_copl`,
and put the other residual points in `E_iso`.  Then, exactly,

```text
E=E_cert disjoint_union E_copl disjoint_union E_iso,
#(E_iso intersect Q)<=3 for every grid cell Q.       (2E.F7av)
```

Every cell contributing to `E_copl` is coplanar by (2E.F7ao).  This is the
full proved conclusion: coplanarity can arise merely because the `(m,n)`
projections are collinear, in which case it imposes no polynomial condition
on `b`.  Thus a coplanar rich cell is **not** silently a polynomial arc of
the form (2E.F7v).  Extracting or merging such cells into a controlled
number of certified arcs remains an additional input.

The isolated part is compatible with the actual separable weights.  Let
`u_m,v_n` be arbitrary complex weights and let `zeta_mn` include any
Selberg phase or smooth cutoff, with `|zeta_mn|<=1`.  Cellwise Cauchy and
(2E.F7av) give

```text
sum_((m,n) in E_iso)|u_m*v_n*zeta_mn|
 <=3*N_cell*||u||_infinity*||v||_infinity,          (2E.F7aw)

sum_Q |sum_((m,n) in E_iso intersect Q)
             u_m*v_n*zeta_mn|^2
 <=3*sum_((m,n) in E_iso)|u_m|^2*|v_n|^2
 <=3*||u||_2^2*||v||_2^2.                          (2E.F7ax)
```

No positivity is used.  A `q^o(1)`-cost Mellin or smooth dyadic
superposition may therefore be treated term by term.  More locally, an
arbitrary index rectangle of side lengths `X,Y` meets at most

```text
(2+X/H)*(2+Y/K)                                    (2E.F7ay)
```

grid cells, up to harmless integer roundings.  Equations (2E.F7av),
(2E.F7ax), and (2E.F7ay) are the precise weighted nonconcentration data
available to an analytic treatment of the residual set.

The boundary ledger is also exact.  A fan box of index lengths `M,N` meets
at most

```text
ceil(M/H)*ceil(N/K)
 <=(1+M/H)*(1+N/K)                                 (2E.F7az)
```

half-open cells.  In a dyadic class let there be `F_a,F_c` row and color
fans, with the proved length budgets

```text
F_a*M<<D,       F_c*N<<D.                          (2E.F7ba)
```

Choose the balanced determinant scales

```text
H asymp (q*S/R^3)^(1/4),
K asymp (q*R/S^3)^(1/4),
H*K asymp sqrt(q/(R*S)),                            (2E.F7bb)
```

with a sufficiently small common constant.  If a displayed scale is below
one, a unit-width index cell is used; its fixed index coordinate already
makes every four points coplanar.  From (2E.F7az), the isolated charge over
the entire dyadic fan class is at most

```text
3*F_a*F_c*(1+M/H)*(1+N/K).                         (2E.F7bc)
```

Its two-dimensional main term satisfies

```text
F_a*F_c*M*N/(H*K)
 <<D^2*sqrt(R*S/q).                                (2E.F7bd)
```

The exact low/high-step cutoff is therefore

```text
R*S<=q/D^2=q^(1/33)=D^(1/16).                      (2E.F7be)
```

At and below (2E.F7be), (2E.F7bd) is `O(D)`.  The already proved fan-count
bounds `F_a<<1+D*R/q`, `F_c<<1+D*S/q` make both fan counts `O(1)` in this
range.  Also `R,S<=q/D^2`, so the shorter side in (2E.F7bb) is at least
`q^(5/22)`; hence all one-dimensional boundary terms in (2E.F7bc) are
`O(q^(17/66))=o(D)`.  Thus the complete isolated contribution, including
boundary cells, is `O(D)` throughout the low-step class.

If `R*S=q^o(1)`, the sharper powers are

```text
D^2/sqrt(q)=q^(31/66)=D^(31/32),
D/q^(1/4)=q^(31/132)=D^(31/64),                    (2E.F7bf)
```

so the weighted `L^1` remainder in (2E.F7aw), for normalized actual
separable weights, is `D^(31/32+o(1))`.  This proves the proposed exponent
only in the bounded-step class.  When `R*S>q/D^2`, the main expression in
(2E.F7bd) is larger than `D`; neither the length budgets nor separability
removes it.  The high-step analytic class inherits (2E.F7av), (2E.F7ax),
and (2E.F7ay), but no `O(D)` unweighted or weighted count.  In particular,
this decomposition supplies no implicit polynomial-arc covering claim.

### Nonzero determinant levels do not repair the balanced high-step class

One possible repair is to enlarge the determinant cells beyond the
coplanarity scale and retain the nonzero integral determinant instead of
forcing it to vanish.  This has an exact plane-index formulation.  In a
cell `Q`, choose three affinely independent occupied anchors
`P_1,P_2,P_3`, if they exist, and put

```text
delta_Q(P)=det(P_1,P_2,P_3,P),       P=(1,m,n,b).  (2E.F7bg)
```

If no such triple exists, the cell is already coplanar.  Otherwise each
level of `delta_Q` is a parallel affine plane.  The same Taylor/cofactor
calculation as (2E.F7an) gives the number of arithmetically available
integer levels

```text
L(H,K)=1+(H*K/q)*(D+R^2*H^2+R*S*H*K+S^2*K^2).     (2E.F7bh)
```

Because the carrier interval has length below one, each index pair has at
most one `b`.  Thus the number `J_Q` of nonempty levels obeys only

```text
J_Q<=min(H*K,L(H,K)).                              (2E.F7bi)
```

There is no bounded-multiplicity theorem inside a level: an entire
coplanar rich patch may have one plane index.  Enlarging a cell can also
put many previously isolated small cells onto the same plane.  This is
useful only after a separate plane/arc estimate; the determinant label
itself supplies none.

The square-root ledger already fails before this multiplicity issue.  In a
balanced class put `R=S` and take square cells `H=K=h`.  In the
curvature-dominated range,

```text
L(h) asymp R^2*h^4/q.                              (2E.F7bj)
```

If the row and color classes both saturate `F*M=D`, the number of cells in
all `F^2` fan pairs has main term

```text
C(h) asymp F^2*(M/h)^2=D^2/h^2.                   (2E.F7bk)
```

Consequently even granting square-root summation over every available
determinant level gives

```text
C(h)*sqrt(L(h)) asymp D^2*R/sqrt(q),               (2E.F7bl)
```

independently of the enlarged scale `h`.  This is at most `D` exactly when

```text
R<=sqrt(q)/D,       equivalently R*S<=q/D^2,       (2E.F7bm)
```

which is the low-step cutoff (2E.F7be), not a repair above it.

One can optimistically replace the full range by the nonempty-level cap
`J_Q<=h^2`.  The resulting bound supplied by this information is

```text
C(h)*sqrt(J_Q)<=D^2/h.                             (2E.F7bn)
```

It can reach `D` only if the fan length permits `h>=D`.  In the genuinely
balanced high-step class from (2E.F7o6),

```text
R=S=q/sqrt(D),       F=M=sqrt(D).                  (2E.F7bo)
```

At the largest possible cell `h=M`, there are `C=D` cells, the determinant
range is `L=qD`, and as many as `J=D` levels are not excluded by (2E.F7bi).
Thus full-range square-root summation costs

```text
D*sqrt(qD)=q^(27/22),                              (2E.F7bp)
```

while even the nonempty-level ledger (2E.F7bn) is

```text
D*sqrt(D)=D^(3/2).                                 (2E.F7bq)
```

Neither meets the `D` target.

Global `L^2` orthogonality does not create a hidden saving.  Even if the
locally defined labels `(Q,delta_Q)` are treated as mutually orthogonal,
there are up to `C*J=D^2` occupied bins in (2E.F7bo).  Unit separable
weights on `D` row and `D` color vertices have coefficient norm
`||u||_2||v||_2=D`; Cauchy over the bins returns `D*D=D^2`.  This is just
the original trivial count in another partition.

Finally, the plane levels do not preserve the separability needed by the
analytic half.  Expanding (2E.F7bg) gives

```text
delta_Q(m,n)=A_Q+B_Q*m+C_Q*n+G_Q*b(m,n).           (2E.F7br)
```

If `G_Q=0`, the anchor projections are collinear and the level condition
does not constrain the carrier at all.  If `G_Q!=0`, a Fourier projector
onto one determinant level contains

```text
e(theta*G_Q*b(m,n)),
```

where `b(m,n)` is the coupled reciprocal rounding function.  The other two
factors separate in `m,n`, but this one does not; it reinstates the original
two-variable carrier phase.  Therefore plane-index stratification provides
neither bounded multiplicity nor a separability-preserving orthogonality
statement.  Its strongest scale ledger closes exactly the already closed
low-step range and is a no-go for the balanced high-step repair.

The [Bettin--Chandee trilinear Kloosterman-fraction theorem and smooth
extension](https://arxiv.org/abs/1502.00769) contain one varying inverse;
(2E.F7) contains two coupled varying inverses.  Its smooth
`1/(mn)` extension does not absorb the second modular inverse, and in the
present `q^3`-numerator, `m,n asymp q` range its high-numerator factor is
already `asymp q^(1/2)`.  It therefore does not supply (2E.F7b).

For calibration only, an intermediate local theorem

```text
E_ij<<q^(1/2+o(1))=D^(33/32+o(1))                 (2E.F8)
```

would already improve the global result.  Replacing `D` by
`K=q^(1/2)` in (2E.14) gives restricted-type constant `sqrt(K)=q^(1/4)`,
and hence

```text
Q_nd<<D^(33/32+o(1)),
||A_z||_op<<D^(33/128+o(1)),
transverse exponent=1/2+(33/128)*(16/33)=5/8.      (2E.F9)
```

No estimate (2E.F8) is proved here.  Standard convex-surface completion
does not automatically supply it: absolute stationary-phase summation over
the transverse/Farey dual modes is exactly the loss in (2E.F7d).

There is a second rigorous sparse range inside a block.  Write

```text
v(alpha,gamma)=a2*c2-a1*c1.
```

If `alpha=(a1,a2)` and `alpha'=(a1',a2')` share `gamma`, direct elimination
gives the two exact identities

```text
c2*det(alpha,alpha')=a1*v(alpha',gamma)-a1'*v(alpha,gamma),
c1*det(alpha,alpha')=a2*v(alpha',gamma)-a2'*v(alpha,gamma). (2E.16)
```

Hence every right neighborhood is a clique in the graph on left pairs
joining two vertices when their determinant is `O(D)`.  The transpose
identity says the same on the right.  If the largest such projective clique
inside `X` has size `K`, then the degrees into `X` on the right are at most
`K`; combining this with the proved degree `O(D)` on the left gives

```text
I(X,Y)<<sqrt(D*K)*sqrt(|X|*|Y|).                    (2E.17)
```

Thus `(RT)` is proved whenever either coefficient support has projective
clique number `q^o(1)`.  In particular it holds if one side is
determinant-`CD` separated.  This is stronger than merely requiring small
cardinality and it permits arbitrary degree-`D` stars.  The unresolved
sector has polynomial near-parallel clusters on both sides.

### The `D` scale in `(SB)` is sharp

There is an exact primitive full-integer packet saturating the proposed
block cap.  Let `L>=2`, `m>6000L^4`, and put

```text
q=2m,                     D_0=100L^2.
```

For `0<=i<L` and `2L<=j<3L`, take

```text
alpha_i=(m+i,m+i+1),
gamma_j=(m+j+1,m+j),
b_ij=m-i-j-1.                                      (2E.18)
```

The two displayed triples on this incidence have products obtained from

```text
(m+x)(m-x-z)(m+z)-m^3
 =-m*(x^2+x*z+z^2)-x*z*(x+z).                      (2E.19)
```

Use `(x,z)=(i,j+1)` and `(i+1,j)`.  Since `x<=L` and `z<=3L`, (2E.19) gives

```text
|8*a1*b_ij*c1-q^3|, |8*a2*b_ij*c2-q^3|<=q*D_0.    (2E.20)
```

All five nodes on every displayed edge are distinct, the row and color
pairs are consecutive and hence primitive, and the deduplicated unordered
triple system is pair-unique.  Moreover

```text
|r(alpha_i)-s(gamma_j)|<=3L/m^2
                         <D_0/q^2,                 (2E.21)
```

so all `L^2=D_0/100` incidences lie in one slope interval.  They form a
`K_(L,L)` and have norm `L=asymp sqrt(D_0)`, exactly the RT scale.  This is
not a counterexample to `(SB)` or `(RT)`, and `q=2m` with full-integer nodes
is not the actual odd-prime/prime-power model.  It proves that neither the
local edge target nor the square-root norm can be improved using only
primitivity, pair uniqueness, product-window curvature, and ratio
localization.

### The sharp tangent packet cannot be multiplied inside its chart

Moving and packing disjoint copies of (2E.18) does not produce a
counterexample to `(SB)`.  The whole symmetric tangent normal form is

```text
alpha_x=(m+x,m+x+1),       gamma_z=(m+z,m+z-1),
b_xz=m-x-z.                                         (2E.22)
```

It simultaneously contains every translated rectangle made with these
directions.  Put `Q(x,z)=x^2+x*z+z^2`.  The first residual in (2E.22) is
exactly

```text
F(x,z)=-m*Q(x,z)-x*z*(x+z),                         (2E.23)
```

and the second is `F(x+1,z-1)`.  If
`|x|,|z|<=D_0` and `m>4D_0`, then

```text
|x*z*(x+z)|<=2D_0*Q(x,z),
|F(x,z)|>=(m/2)*Q(x,z).                             (2E.24)
```

The legal window `|8F|<=qD_0=2mD_0` therefore forces

```text
Q(x,z)<=D_0/2,              x^2+z^2<=D_0.          (2E.25)
```

Hence the **total** number of legal pairs in the chart is `O(D_0)`, before
requiring the second residual.  This bounds any packing of its subrectangles,
not just one `K_(L,L)`.  The surviving ratios occupy
`O(sqrt(D_0)/m^2)` width, so the argument stays inside a constant number of
the canonical `D_0/q^2` blocks.

There are two independent actual-model obstructions to this particular
chart.  Its centre is `q=2m`, not an odd prime.  Moreover every row and
color pair is consecutive.  In a project shell the ratio of the largest to
smallest node is `exp(0.4)<2`, so it contains at most one even prime power,
which must be a power of two.  Every consecutive prime-power pair contains
that even node and is one of its two neighbors.  Thus the chart has at most
two actual row vertices, at most two actual color vertices, and at most four
actual incidences even after recentering.  This does not exclude transformed
primitive directions or the scattered modular lifts (2E.15a--b); those are
precisely the unresolved sector of `(SB)`.

The remaining slope-block lemma `(SB)` is a genuine arithmetic aggregation
problem.  After selecting the unique numerator in a ratio interval, an edge
still asks whether a reciprocal product has an actual carrier in an interval
of length `D/q<1`.  The arbitrary coefficient masks retain all those
rounding layers; fixed-multiplier small-box counting and the existing
fixed-direction merger do not sum them.  No proof of `(SB)` is claimed.

Thus the sharp remaining direct gate is `(RT)` on the residual
actual-prime chord incidence after removing only already-certified merged
patches, together with a global merger/orthogonality theorem for the rich
directions.  Maximum common-neighbor degree, fixed inversion layers, and
the unweighted anchor load are all strictly stronger or structurally
misaligned substitutes.

---

## 3. Why pure `K_C` is not the secant theorem

On a broad fixed-color conic, the proved slice estimate is

```text
m(C)<<K_C q^o(1),              K_C=1+D/lambda3(C). (3.1)
```

Equation (3.1) counts possible slices.  Actual occupancy can be much
smaller.  Decompose

```text
m(C)=1+(m(C)-1).                                    (3.2)
```

The determinant-layer theorem already controls the first term:

```text
sum_C w_z(C)<<Dq^o(1)||z||_2^4.                    (3.3)
```

Only the second term requires arithmetic.  Moreover,

```text
m(C)(m(C)-1)
 <<K_C(m(C)-1)q^o(1),                              (3.4)
```

which proves the implication (0.3) => broad (0.1).  Unlike pure (0.2),
every term in (0.3) has two actual completions and therefore a nonzero
realized secant to which the fixed-`(C,E)` theorem applies.

This is a logical scope distinction, not a counterexample to (0.2).
Existence of one completion may still correlate arithmetically with
`lambda3(C)` strongly enough to prove (0.2), but no such correlation theorem
is currently available.

### 3.1 Isolated chords are already harmless

The remaining chord language should not be read as saying that a single
two-point color fibre is expensive.  Split the direct fourth-trace form as

```text
sum_C m(C)w_z(C)
 <=2*sum_C w_z(C)+sum_(m(C)>=3)(m(C)-2)w_z(C).     (3.5)
```

The first term is `O(Dq^o(1))` by the determinant-layer theorem.  Hence an
actual obstruction must contain at least three completions of one color
matrix.  If their product matrices are `M_0,M_1,M_2`, the three nonzero
secants satisfy the exact cocycle identity

```text
E_01+E_12+E_20=0.                                  (3.6)
```

Pairwise actual-shell Sidonicity makes every `det(E_ij)` nonzero.  Thus the
unresolved two-chord sector is more precisely a weighted aggregation of
coherent secant triangles (and larger matching configurations), not a sum
of isolated doubletons.  Fixing two sides of one triangle invokes the
proved two-independent-relations endpoint, but the resulting plane varies
with the color and with the triangle; summing those planes is still the
open step.

### 3.2 The secant-triangle normal and an actual varying-direction fixture

An isolated triangle is harmless too.  On the subfamily `m(C)=3`, the
off-diagonal coefficient is exactly six, so (3.3) gives

```text
sum_(m(C)=3) m(C)(m(C)-1) w_z(C)
 <=6Dq^o(1)||z||_2^4.                              (3.7)
```

More generally every `m(C)<=q^o(1)` subfamily has the desired bound.  The
remaining issue is therefore a coherent family of increasingly many
overlapping triangles, not one three-point fibre.

There is nevertheless a canonical exact invariant of one triangle.  Write

```text
M_i=a_i b_i^T,
u_ij=det(a_i,a_j),       v_ij=det(b_i,b_j),
Delta_ij=det(E_ij)=-u_ij*v_ij.                     (3.8)
```

Let `N_T` be the row-major cofactor normal of the three-by-four matrix with
rows `M_0,M_1,M_2`: its coordinate `ell` is `(-1)^ell` times the minor
obtained by deleting coordinate `ell`, with zero-based indexing.  Then

```text
<N_T,M_i>=0,
det(N_T)
 =(u_01*u_12*u_20)*(v_01*v_12*v_20)
 =-Delta_01*Delta_12*Delta_20.                     (3.9)
```

The first assertion is the cofactor identity.  The determinant formula is
a direct Cauchy--Binet expansion; equivalently normalize `(a_0,a_1)` and
`(b_0,b_1)` to the two coordinate bases and then undo the two changes of
basis.  Pairwise actual-shell Sidonicity makes all six factors in (3.9)
nonzero, so the three product matrices are linearly independent and `N_T`
is well defined.  If `h_T` is the content of `N_T`, its primitive version
satisfies only

```text
det(N_T/h_T)
 =-Delta_01*Delta_12*Delta_20/h_T^2.               (3.10)
```

The actual prime-power factorization appears in the two Pluecker relations

```text
u_12*a_0+u_20*a_1+u_01*a_2=0,
v_12*b_0+v_20*b_1+v_01*b_2=0.                      (3.11)
```

These hold coordinatewise.  They are not fixed norm/divisor equations:
after the rich fixed-direction cases are removed, their six coefficients
vary with the triangle, and (3.11) asks for two simultaneous variable-
coefficient ternary linear patterns in prime powers.  A divisor bound applies
after all Pluecker data are fixed, but summing those data is the original
varying-direction problem.

This failure can also be read in the conic geometry.  Put

```text
K_C=(c11,-c12;-c21,c22),
W_T=span(E_01,E_12).                                (3.12)
```

The two normals of `W_T` are `K_C` and `N_T`.  With `H` as in (2C.1), the
direction-conic discriminant is, up to the fixed polar convention,

```text
Disc_T=(N_T^T H K_C)^2-4 det(N_T) det(K_C).         (3.13)
```

The parabolic/fixed-direction merger applies when this vanishes and the
corresponding affine carrier line is occupied richly.  When it is nonzero,
binary norm counting is `q^o(1)` only after `W_T` is fixed.  Formula (3.9)
does not pin `N_T` or `W_T`; even fixing its determinant leaves many
integral normals.  Thus it supplies no summable family of two-relation
planes.

The genuinely varying sector occurs on actual prime support.  At the prime
`q=11801` and cutoff `U=35`, take

```text
C=(6337,5717;5479,4943),       det C=348,

X0=(5171,5981,6269,6949),
X1=(5821,6733,5569,6173),
X2=(5861,6779,5531,6131).                           (3.14)
```

All sixteen displayed nodes are distinct primes in the project shell, all
twelve cell frequencies have absolute value below `34.590<35`, and

```text
L_C(X0)=L_C(X1)=L_C(X2)=2282556.                    (3.15)
```

The cyclic secants and their determinants are

```text
E01=(-150,246,-1188,-840),       Delta01=418248,
E12=(-42,-758,1428,760),         Delta12=1050504,
E20=(192,512,-240,80),           Delta20=138240.    (3.16)
```

They sum to zero.  The cofactor normal has

```text
N_T=(4696450792896,-4237065848256,
     -4060735442112,3663533199552),
content(N_T)=192,
det(N_T)=-60738674272174080
        =-Delta01*Delta12*Delta20.                  (3.17)
```

The three carrier points are not affine-collinear.  More strongly, the
quadratic coefficients of the three pair carrier lines are

```text
<K_C,delta_a delta_b^T>=(-32136,-264,-35856),       (3.18)
```

so none is a constant-level rich line, and

```text
Disc_T=66571014489955460775936 !=0.                 (3.19)
```

This is an exact actual-prime-power/product-window witness that the cocycle,
rank-one factorization, common residual level, and prime support do not
force a triangle into the proved fixed-direction merger.  It has only three
completions and therefore satisfies (3.7) with enormous room; it is not an
asymptotic counterexample to the `D` theorem.  Its role is to identify the
remaining arithmetic gate precisely: control the weighted aggregation of
the varying primitive normals `N_T/h_T` (or equivalently the variable
Pluecker systems (3.11)).

### 3.3 Four points: exact volume quantization and local planes

Four completions give a stronger exact integer invariant.  For
`i=0,1,2,3`, retain the notation `M_i=a_i b_i^T`, `u_ij`, and `v_ij`, and
put

```text
Vol(M_0,M_1,M_2,M_3)=det(rows M_0,M_1,M_2,M_3).    (3.20)
```

The four-by-four Khatri--Rao determinant is

```text
Vol
 =u_02*u_13*v_01*v_23-u_01*u_23*v_02*v_13.         (3.21)
```

This follows by a two-by-two Cauchy--Binet expansion.  It is the difference
of the row and column cross-ratio monomials.  In the common nonzero-level
setting below, `Vol=0` is precisely the affine-coplanar case after one point
is chosen as origin.

Now put `F_i=M_i-M_0` for `i=1,2,3`, and let `n(F_1,F_2,F_3)` be their
integral cofactor normal.  The common-level equations give

```text
K_C dot F_i=0.                                     (3.22)
```

The signed color normal `K_C` is primitive on all-distinct actual support.
Consequently there is an integer `t` such that

```text
n(F_1,F_2,F_3)=t*K_C,
content(n)=|t|,
Vol=t*L.                                           (3.23)
```

The last identity is Laplace expansion after subtracting the first product
row from the other three.  Thus an affine-rank-three quadruple recovers both
the color normal and the level from its three secants:

```text
K_C=n/content(n),             L=Vol/t,              (3.24)
```

up to the fixed orientation sign.  Actual prime-power coprimality is used
exactly in the primitivity/content assertion; it does not make the small
determinants `u_ij,v_ij` pairwise coprime.

Every coordinate of `F_i` is `O(D)`, whereas every coordinate of `K_C` is
`asymp q`.  The three-by-three cofactors in (3.23) therefore give

```text
|t|<<D^3/q.                                        (3.25)
```

This yields an exact local-plane decomposition.  Fix any anchor triangle
`M_0,M_1,M_2` and its homogeneous normal `N_T` from (3.9).  Every further
completion of affine rank three lies on one of

```text
K_C dot M=L,
N_T dot M=-t*L,
det M=0,                    |t|<<D^3/q,             (3.26)
```

with the sign corresponding to the cofactor convention.  Each fixed `t`
is a plane conic.  If no rank-three fourth point exists, the whole fibre is
already in the anchor plane.  Hence the number of exact volume planes is

```text
J_4<<1+D^3/q<<D.                                   (3.27)
```

At the project aperture `50/33` and a subpower cutoff, this is the genuine
power refinement

```text
J_4<<D^(15/16) q^o(1).                             (3.28)
```

Fixed-plane binary-norm counting and the proved parabolic rich-line merger
can be applied inside each plane.  Equations (3.27)--(3.28), however, do
not control pairs lying in different volume planes.  Paying `J_4` for each
actual secant recreates the open singleton-safe `K_C*(m(C)-1)` form.

Equating (3.21) and (3.23) isolates the new arithmetic gate:

```text
u_02*u_13*v_01*v_23-u_01*u_23*v_02*v_13=t*L.       (3.29)
```

For fixed Pluecker data this is exact and finite, but after the data vary it
is a shifted product/additive-divisor equation, not a norm or divisor
equation.  The two monomials can have large common factors because
determinants of distinct prime pairs need not be coprime.  No summable
bound over `(t,N_T)` follows from prime-power unique factorization alone.

Affine rank three is not excluded by rank-one/common-level geometry.  On
`det M=0, tr M=1`, the four matrices

```text
(1 0;0 0), (0 0;0 1), (2 -1;2 -1), (3 2;-3 -2)    (3.30)
```

have all six pairwise secants invertible and `Vol=-1`.  This is only an
integer algebraic obstruction, not an active product-window fixture.  The
finite actual-prime scans used here found the varying triangle (3.14), but
no affine-rank-three four-completion fibre.  Thus a prime-specific theorem
forcing large fibres into few local planes remains possible; (3.29) is the
precise unproved input needed to obtain it.

### 3.4 High multiplicity does not amplify fixed-plane bounds

The exact multiplicity identities are

```text
(m-2)*binom(m,2)=3*binom(m,3),
binom(m-2,2)*binom(m,2)=6*binom(m,4),
sum_(T in binom(V_C,3)) (m-3)=4*binom(m,4).        (3.31)
```

Thus a global `O(D)` weighted triangle or quadruple incidence theorem
would control the `m>=4` tail (for example
`m(m-1)<=3*binom(m,3)` and
`m(m-1)<=12*binom(m,4)`).  The two-fixed-relation theorem is not such a
global incidence theorem: it gives `O(1)` color mass after one triangle
relation plane is fixed.  Summing it over all triangles introduces exactly
the `binom(m,3)` labels that (3.31) was meant to divide by.

The same cancellation is visible with one canonical triangle `T(C)`.  If
`r_(C,t)` is the number of further completions in its exact volume plane,
then

```text
m(C)-3=sum_t r_(C,t),
binom(m(C)-3,2)
 =sum_t binom(r_(C,t),2)+sum_(t<u) r_(C,t)r_(C,u). (3.32)
```

Fixed-plane conic estimates see only the first term in (3.32).  The second
term can contain essentially every pair, even when every individual plane
has divisor-many points.  This is sharp on an exact integral matching.

On `det M=0, tr M=1`, take the anchor triangle

```text
A_x=(2 x;-2/x -1),                     x=1,2,-1.  (3.33)
```

Its homogeneous cofactor normal is `-6*(1,0,0,2)`.  For alternate
disjoint Farey neighbors

```text
a/c<b/d,                         b*c-a*d=1,
M=(a,c)^T*(-d,b)=(-ad,ab;-cd,cb),                 (3.34)
```

all matrices have trace one and lie in an `O(R^2)` box.  There are
`asymp R^2` of them.  Disjoint left and right Farey endpoints make every
pairwise secant invertible; deleting the `O(1)` edges meeting an anchor
ruling makes all anchor secants invertible too.  The exact volume index of
`(A_1,A_2,A_-1,M)` is, up to orientation,

```text
|t|=6*(1+b*c).                                      (3.35)
```

For fixed `t`, first factor `bc`, then `ad=bc-1`; consequently

```text
r_t<=tau(bc)*tau(bc-1)=R^o(1).                     (3.36)
```

Hence this fibre has `m=R^(2+o(1))` points spread over
`R^(2-o(1))` occupied volume planes, while
`sum_t binom(r_t,2)=R^(2+o(1))` and the cross-plane term in (3.32) is
`R^(4+o(1))`.

This is not caused by zero or repeated color coordinates.  Put

```text
K=(64 -71;-73 81),                 det K=1,         (3.37)
```

and apply the integral determinant-quadric automorphism
`M -> M*K^(-T)`.  The new signed color normal is `K`, so the color tuple is
`(64,71,73,81)`: four distinct pairwise-coprime prime powers in a narrow
ratio.  Common level, secant invertibility, volume indices, and the
`O(R^2)` box are preserved.  The transformed carriers are not shell prime
powers and are not in the active product window, so (3.33)--(3.37) are an
integer/algebraic barrier, not an actual-node counterexample.

The exact verdict is therefore negative for combinatorial amplification:
local two-relation and fixed-volume-plane estimates cannot by themselves
improve the high-multiplicity tail.  A proof still requires a genuinely
global weighted aggregation theorem over the varying `(T,t)` labels (or
new actual-prime rigidity that rules out the cross-plane term).

---

## 4. Actual-prime-power scans

The following table uses the project shell, all-eight-distinct rectangles,
and exact oriented color matrices.  `K max`, `Schur K`, and `best K` use a
finite broad proxy: the third LLL-basis length in place of `lambda3`, and
the determinant type of that reduced first plane.  In fixed dimension this
changes `K` only by a constant factor, but these columns are diagnostics,
not theorem certificates.

| `q` | `U` | `D` | completed `C` | proxy broad `C` | broad singletons | `K max` | `Schur K` | `best K` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 12,853 | 12 | 3,369.24 | 728 | 692 | 692 | 135.66 | 329.98 | 19.383 |
| 25,013 | 12 | 4,652.98 | 902 | 876 | 876 | 153.58 | 244.11 | 22.656 |
| 50,021 | 12 | 6,511.25 | 2,680 | 2,624 | 2,624 | 174.90 | 365.25 | 26.491 |

The pure broad form is nonzero in every row, while the exact off-diagonal
form is identically zero.  This is the promised finite separation between
potential slices and occupied secants.

The exact off-diagonal diagnostics are:

| `q` | `U` | `D` | repeated generic `C` terms | sum of coefficients | best flattening Schur bound | searched value |
|---:|---:|---:|---:|---:|---:|---:|
| 25,013 | 12 | 4,652.98 | 0 | 0 | 0 | 0 |
| 50,021 | 12 | 6,511.25 | 0 | 0 | 0 | 0 |
| 100,003 | 12 | 9,110.37 | 6 | 12 | 2 | 0.25 |
| 200,003 | 12 | 12,749.31 | 2 | 4 | 2 | 0.25 |
| 25,013 | 40 | 15,509.94 | 2,712 | 5,604 | 12.962 | 1.50 |

The Schur entries are rigorous upper bounds for the corresponding finite
positive forms, up to ordinary floating representation of their integer
coefficients.  The searched values are deterministic lower bounds, not
certified maxima.  All values are far below `D`; no legal actual-node
counterexample was found.

The wide-cutoff row is useful hostile evidence: repeated generic colors are
no longer rare, yet the factorial-codegree flattening remains tiny at this
finite scale.  It has no asymptotic force.

It also contains a sharper actual-prime-power warning against a singleton
shortcut after exact level pinning.  At `q=25013,U=40` there are 26 oriented
all-eight-distinct `(C,L)` fibers with two completions on the same integral
level and with nonzero reduced-plane discriminant.  One is

```text
C=(14723,14207;12211,11783),       det C=-568,
L=-6404680,
X =(10267,12379,12941,13411),
X'=(10733,12941,12379,12829),
E=M(X)-M(X')=(1440,-2920;0,-5320), det E=-7660800. (4.1)
```

Here `L_E(C)=0` exactly.  Thus actual prime-power support, exact common-level
pinning, and a broad binary plane do not force singleton occupancy.  This is
a finite obstruction only; it neither violates the desired `D` bound nor
asserts an asymptotic family.

---

## 5. Exact status

```text
fixed-(C,E) multiplicity q^o(1):                    PROVED EARLIER;
factorial-codegree / three-flattening identities:   PROVED;
fixed-(E,k) color-pair partial matching:             PROVED;
two-fixed-relation weighted color mass O(1):         PROVED;
fixed-(A,B) weighted color mass O(D):                 PROVED;
O(1) fixed-(A,B) from matching/product window:        FALSE IN INTEGER MODEL;
summed fixed-(A,B) layers improve D^(21/16):          NO;
restricted ternary polar discriminant = 2 det C:     PROVED;
projective completion discriminant = L^2 / split:    PROVED;
geometry-only improvement over broad slice count:    FALSE;
exact m(C)=3 weighted sector O(D):                    PROVED;
secant-triangle normal determinant factorization:    PROVED;
actual varying-direction common-level prime triangle: FOUND FINITELY;
weighted aggregation over varying triangle normals:  OPEN;
four-point Khatri--Rao / volume identities:           PROVED;
anchor local-plane count 1+D^3/q:                     PROVED;
cross-volume-plane weighted aggregation:              OPEN;
triangle/quadruple multiplicity amplification alone:  SHARP BARRIER;
Farey many-volume-plane matching:                      EXACT INTEGER MODEL;
AM--GM maximum anchor-load gate:                       SUFFICIENT / OVERSTRONG;
common-carrier Gram identity for direct completion:    PROVED;
fixed-color-pair Gram row bound `D` implies FC:         PROVED / INPUT OPEN;
restricted-type incidence theorem `(RT)` implies FC:   PROVED;
rich short common-neighbor block is affine:            PROVED;
full cross-direction rich-patch merger:                 OPEN;
actual-prime sparse restricted-type chord bound:        OPEN;
slope-block edge cap `(SB)` implies `(RT)`:              PROVED;
short modular-lift parametrization (2E.15a--c):          PROVED;
fixed-row-pair common-neighbor cap `sqrt(D)q^o`:         PROVED;
generic fixed-row factorial codegree `Dq^o`:             PROVED;
exceptional power codegree => parabolic tangent charts:  PROVED;
near-sharp generic codegree => one tangent chart:         NOT PROVED;
cross-row-pair secant/chart aggregation:                  OPEN;
Selberg reciprocal-sum reduction (2E.F3--F6):            PROVED;
relevant all-integer strip has `O(D)` determinant lifts:  PROVED;
single contiguous fan-pair reciprocal `L^1` bound:        PROVED;
anisotropic shortest-vector fan decomposition (2E.F7e--h): PROVED;
geometry-only per-fan curvature cap (2E.F7p):           FALSE (QUARTIC MATCHING);
quadratic-carrier arc fourth-degree sublevel cap:         PROVED;
linear-carrier strict-log-concavity tangent cap:          PROVED;
centered exact quartic resonance on two actual fans:      IMPOSSIBLE;
conditional polynomial-arc covering `(PAC)` implies SB:  PROVED;
uniform `q^o(1)` packet covering `(PAC)`:                 OPEN;
four-point coplanarity cell criterion (2E.F7ao):          PROVED;
isolated-cell random-volume closure by that criterion:    FALSE (`q^(1/66)` GAP);
bounded-step weighted isolated-cell cap `D^(31/32+o(1))`: PROVED;
low-step weighted isolated-cell cap through `R*S<=q/D^2`: PROVED (`O(D)`);
high-step three-point weighted cell nonconcentration:      PROVED / COUNT OPEN;
coplanar rich cell implies controlled polynomial arc:      NOT PROVED;
nonzero plane-index square-root repair in high step:        FAILS (SCALE-INVARIANT GAP);
plane-index Fourier projection preserves separability:      FALSE (`b(m,n)` COUPLES);
positive parallel copies of high-step quartic model:      IMPOSSIBLE IN AUDITED BOX;
geometry-only Selberg/large-sieve second-moment closure:  FALSE (`sqrt(D)` LOSS);
interior stationary minor weights Mellin-separable:        PROVED;
low Selberg modes and coherent interior B-process terms:    PROVED (`O(q q^o)` RAW);
sharp fanwise endpoint B-process summation:                  OPEN (`sqrt(D)` LOSS);
positive rectangular smooth completion of endpoints:        PROVED / HSM-CONDITIONAL;
completed-HSM excess => actual packet mass retention:         NOT PROVED / MASK ERASED;
Fouvry--Radziwill `17/33` theorem supplies HSM:                NO (HYPOTHESES MISMATCH);
minor product-kernel diagonal equals `qD`:                 PROVED;
arbitrary-weight minor `L2` theorem:                       FALSE (DIAGONAL PATH);
separable weighted shifted multiplication-table `(*)`:    OPEN (`q^(2/11)` GAP);
spacing fallback `N(delta)<<delta*P^4+P^3`:                PROVED (`P` LOSS ONLY);
sharp spacing endpoint `delta*P^4+P^2`:                    OPEN (SHARP FIXTURES);
aligned exact cubic rays and homogeneous gcd ruling:        PROVED (`P^2 q^o`, SHARP);
positive diagonal Fejer peak `E_diag`:                     PROVED (`L*P^(3/7+o)`, GAP);
sharp diagonal Fejer peak `E_diag<<L*q^o`:                 OPEN (`P^(3/7)=q^(8/77)` GAP);
conditional `abc` + Huxley-IV diagonal peak:               PROVED CONDITIONALLY (`L*P^(1/16+o)`, GAP);
Huxley-IV primitive minor floor (`d=2`):                   PROVED (`P^(5/8+o)`, TARGET `P^(9/16)`);
Konyagin bound for hostile shifted-cube bin:                 PROVED (`P^(43/80+o)` RAW);
required averaged shifted-cube count `P^(11/32+o)`:          OPEN (`P^(31/160)` GAP);
nonzero shifted-cube pointwise exclusion:                    `abc`-CONDITIONAL (`107/93`, EPS `14/93`);
exact zero-residual cubic rays:                              PROVED (`P^(11/96+o)`, TARGET-CONTROLLED);
fixed-`A` factorial energy `E_2<<P^(9/16+o)`:                OPEN (SUFFICIENT FOR TRANSITION);
same-`A` pair gap / dyadic cap:                              PROVED (`k>>P^(7/16)`, `#_K<<(H+K)P^o`);
same-`A` three-point / six-point-minor spans:                PROVED (`P^(23/48)`, `P^(39/80)`);
zero-residual fixed-`A` energy:                              PROVED (`P^(9/16+o)`);
abstract critical-cell saturator:                           PROVED (`P^(5/8)`, CURRENT INPUTS DO NOT CLOSE);
transition cubic count `R<<P^(9/16+o)`:                     OPEN (`R<<P^(1+o)`, QUALITY ONE);
sharp spacing / HSM / `(SB)` / FC under standard `abc`:     OPEN (QUALITY-ONE GATES);
ordinary Mellin/positive mean-value closure of HSM:          NO (`N/L=q` LOSS);
cross-cusp Kuznetsov exponent ledger:                       FAVORABLE / CONDITIONAL;
vector-valued cross-cusp local lift (2E.F7o20i):            OPEN / NOT FORMAL TENSORIZATION;
exact-divisor cusp-width power loss:                        NONE FOR FIXED SCALAR DATA;
Hecke fold after exact product formula (2E.F7o20k):         PROVED CONDITIONALLY;
actual conductor-lowered product formula (2E.F7o20k):      OPEN;
coefficient-blind inter-modulus CRT power saving:           FALSE (COHERENT `k=t*c` RAYS);
smooth top-`c` full two-dimensional Poisson transform:       EXACT (RAW QUOTIENT CANCELS);
top-`c` support-Cauchy plus numerator Parseval closure:       FALSE (`q^(3/11)` GAP);
joint transformed row/color inter-modulus estimate:           OPEN;
scattered Farey-fan `L^1` cancellation (2E.F7b--d):      OPEN;
local slope-block cap `q^(1/2+o(1))`:                    OPEN;
random slope-block scale `D^(15/16)`:                    EXACT HEURISTIC;
`(RT)` for local occupancy products at most `D`:         PROVED;
projectively sparse-support `(RT)` range:                PROVED;
primitive full-integer `Omega(D)` one-block model:       PROVED;
symmetric tangent multi-packet cap `O(D)`:               PROVED;
consecutive-chart actual embedding (at most four edges): PROVED;
slope-block edge cap `(SB)` itself:                      OPEN;
finite actual off-diagonal diagnostics:             IMPLEMENTED;
actual counterexample to weighted pair theorem:     NOT FOUND;
pure broad K theorem:                               OPEN;
singleton-safe K*(m-1) theorem:                     OPEN;
weighted off-diagonal D theorem:                    OPEN;
full four-cycle bound:                              OPEN.
```

Executable replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_weighted_secant_lab.py
```

The exact saturated kernel basis, exact small-instance successive-minimum
enumerator, anchor-load/common-carrier incidence ledgers, sparse positive
quartic, three Schur flattenings, deterministic search, and broad proxy are in
`src/qp_four_cycle_weighted_secant_lab.py`.
