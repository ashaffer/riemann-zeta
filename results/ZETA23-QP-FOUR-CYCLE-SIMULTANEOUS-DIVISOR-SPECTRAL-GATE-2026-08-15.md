# QP four-cycle: simultaneous-divisor spectral gate

**Date:** 2026-08-15  
**Verdict:** the four-cycle estimate is reduced exactly to the norm of one
explicit row-pair/color-pair incidence matrix.  This gives an unconditional
weighted theorem

```text
|Q_nd(z)|<<D+D^3 sum_c |z_c|^4,             ||z||_2=1.
```

Hence `(FC)` is proved for participation ratio at least `D^2`, and any larger
four-cycle obstruction is classified as effectively sparse.  For arbitrary
coefficients, either square-root local degrees or `q^o(1)` hereditary
degeneracy would prove `(FC)`.  The elementary arithmetic gives local degree
`O(D)` and matching residual-shift layers, but neither uniform improvement is
proved.  Thus full `(FC)` remains open.

---

## 1. Truncated incidence tensor

Let `S` be the prime-power shell and let `T` be the truncated set of triples
`(a,b,c)` in `S^3`.  Write

```text
kappa(a,b,c)=K(a,b,c) 1_T(a,b,c),       |kappa|<=1,       (1.1)
A_z(a,b)=sum_c z_c kappa(a,b,c).                         (1.2)
```

The truncation is narrow enough that every two coordinates determine at most
one third coordinate.  In particular, the sum in (1.2) contains at most one
term for every `(a,b)`.

Put

```text
L={(a,a'):a,a' in S, a!=a'},
R={(c,c'):c,c' in S}.                                  (1.3)
```

Define the weighted bipartite incidence matrix

```text
H_((a,a'),(c,c'))
 =sum_b conjugate(kappa(a,b,c))*kappa(a',b,c').          (1.4)
```

For fixed `(a,a',c,c')`, pair uniqueness makes the sum in (1.4) contain at
most one `b`.  Hence every entry of `H` has magnitude at most one.

---

## 2. Exact row-pair Gram identity

For an ordered distinct row pair define

```text
G_(a,a')=sum_b conjugate(A_z(a,b))*A_z(a',b).             (2.1)
```

If

```text
xi_(c,c')=conjugate(z_c)*z_(c'),                         (2.2)
```

then direct expansion gives the exact identity

```text
G=H xi,                    ||xi||_2=||z||_2^2.            (2.3)
```

The diagonal in the common column must still be removed.  With the same
orientation as the fourth-trace expansion,

```text
Q_nd(z)
 =sum_(a!=a') [ |G_(a,a')|^2
                -sum_b |A_z(a,b)|^2 |A_z(a',b)|^2 ].     (2.4)
```

The second term has total mass at most `D` for `||z||_2=1`.  Indeed, for a
fixed column `b`, pair uniqueness in `(b,c)` gives

```text
S_b:=sum_a |A_z(a,b)|^2 <=sum_c |z_c|^2=1.               (2.5)
```

Consequently

```text
sum_b sum_(a!=a') |A_z(a,b)|^2 |A_z(a',b)|^2
 <=sum_b S_b^2
 <=sum_b S_b=||A_z||_F^2<=D.                             (2.6)
```

Equations (2.3)--(2.6) prove

```text
|Q_nd(z)| <= ||H xi||_2^2+D
           <= ||H||_(2->2)^2 ||z||_2^4+D.                (2.7)
```

---

## 3. The square-root degree criterion

Let the absolute weighted degrees be

```text
Delta_L=max_(a!=a') sum_(c,c') |H_((a,a'),(c,c'))|,
Delta_R=max_(c,c') sum_(a!=a') |H_((a,a'),(c,c'))|.       (3.1)
```

Schur's test gives

```text
||H||_(2->2) <=sqrt(Delta_L Delta_R).                     (3.2)
```

It follows from (2.7) that

```text
Delta_L,Delta_R << D^(1/2) q^o(1)
       ==> |Q_nd(z)| << D q^o(1)                         (3.3)
```

uniformly for `||z||_2=1`.  Thus (3.3) is an exact sufficient arithmetic
lemma for `(FC)`.

More generally, bounds

```text
Delta_L<<D^theta_L q^o(1),
Delta_R<<D^theta_R q^o(1)                                (3.4)
```

give

```text
|Q_nd(z)| << D^(theta_L+theta_R) q^o(1)+D.               (3.5)
```

Any `theta_L+theta_R<2` would already improve the old square-root operator
scale; `(FC)` is obtained at `theta_L+theta_R<=1`.

### A high-star-safe hereditary criterion

There is a useful weakening of the two maximum-degree hypotheses.  Let
`G_H` be the undirected bipartite support graph of `H`, let `Delta` be its
maximum degree, and suppose `G_H` is `kappa`-degenerate.  Its degeneracy
ordering supplies an orientation with maximum out-degree at most
`kappa`.  In fact, the existence of any such orientation is the weaker
hypothesis actually used below.

Form the full Hermitian adjacency

```text
mathcal_H = [ 0   H  ] .                              (3.6)
            [ H*  0  ]
```

Put each weighted edge into a matrix `T` according to such an orientation,
so `mathcal_H=T+T*`.  The maximum absolute row sum of `T` is at most
`kappa`, while its maximum absolute column sum is at most `Delta`.  Schur's
test therefore gives

```text
||H||=||mathcal_H||<=2 sqrt(kappa Delta).              (3.7)
```

The elementary local estimate below gives `Delta<<D`.  Consequently

```text
kappa=q^o(1)  ==>  |Q_nd(z)|<<D q^o(1).                (3.8)
```

In particular, a forest support (`kappa=1`) proves `(FC)` even if it contains
degree-`D` stars.  This is why bounding both maximum degrees by `sqrt(D)` is
sufficient but not necessary.

One exact piece of hereditary structure is already available.  Label an
incidence edge by

```text
v=ac-a'c'.                                             (3.9)
```

For a fixed left endpoint and `v`, the shell lift `(c,c')` is unique; for a
fixed right endpoint and `v`, the shell lift `(a,a')` is unique.  The same
short-diameter argument used in Section 4 proves both assertions.  Thus
every fixed-`v` layer is a matching and `G_H` is a union of `O(D)` partial
matchings.  This edge coloring alone gives only degeneracy `O(D)`: proving
`q^o(1)` hereditary degeneracy, or finding a counterexample, remains a
separate arithmetic problem.

Indeed, no combination of this matching statement and the global edge count
can prove hereditary sparsity formally.  For odd `m<=D`, put a `K_(m,m)`
component inside an otherwise isolated graph and label its edge `(i,j)` by

```text
carrier=i+j (mod m),             shift=i+2j (mod m).     (3.10)
```

Every carrier layer and every shift layer is a matching, and the total edge
count `m^2` is compatible with (5.3), but the component has degeneracy and
operator norm `m`.  Actual-shell arithmetic must exclude this dense core;
the two edge colorings and global sparsity do not.

---

## 4. Exact simultaneous-short-divisor problem

Use the integral product window

```text
Q=q^3,                         H_0=qD,
|8abc-Q|<=H_0.                                      (4.1)
```

Up to harmless fixed cutoff constants, a left degree is the number of
triples `(b,c,c')` satisfying, for fixed distinct `a,a'`,

```text
|8abc-Q|<=H_0,
|8a'bc'-Q|<=H_0.                                    (4.2)
```

Equivalently, if `X=Q/8`, the same carrier `b` must give a shell divisor in
each of the two intervals

```text
bc  in X/a  +[-O(D),O(D)],
bc' in X/a' +[-O(D),O(D)].                           (4.3)
```

Subtracting the two residuals in (4.2) gives

```text
v=ac-a'c',                         |v|<<D.           (4.4)
```

Distinct shell prime powers are coprime.  All integer solutions of
`ac-a'c'=v` differ by `(a',a)`, while the shell diameter is smaller than its
minimum because `exp(2w)<2`.  Hence each fixed `v` has at most one shell lift
`(c,c')`.  Once `c` is fixed, the first interval in (4.2) has length less
than one as an interval for `b`.  Therefore

```text
Delta_L<<D.                                             (4.5)
```

Interchanging rows and colors proves identically

```text
Delta_R<<D.                                             (4.6)
```

A companion determinant calculation gives a genuine but nonuniform local
improvement.  If `h=|a-a'|`, then at the active scale

```text
degree(a,a') <<(h+1) D^(1/2)+D^(13/16).                (4.6a)
```

Thus row gaps `h<=D^(1/2-eta)` have a fixed power saving, although not the
uniform square-root bound needed in (3.3).  See
`ZETA23-QP-FOUR-CYCLE-COMMON-NEIGHBOR-GCD-AND-SHORT-DIVISOR-GATE-2026-08-15.md`
for the integer second-determinant proof and its precise hypotheses.

This recovers only the old scale.  To reach (3.3), one must show that at most
`D^(1/2)q^o(1)` of the `O(D)` shifts in (4.4) pass the remaining carrier
test.

Writing the unique shell lift explicitly gives

```text
c(v) == inverse(a)*v (mod a'),
distance(Q/(8*a*c(v)), S) << D/q.                       (4.7)
```

At the active aperture

```text
D=q^(16/33+o(1))=q^(1/2-1/66+o(1)).                    (4.8)
```

Thus (4.7) is a joint short affine-permutation/reciprocal problem just below
the square-root length of its modulus.

---

## 5. A proved averaged sparsity bound

Let `N=|S|`, and for a fixed carrier put

```text
d_b=#{(a,c):(a,b,c) in T}.                            (5.1)
```

As above, `ac` is confined to an integer interval of length `O(D)`.  The
narrow prime-power shell has at most two ordered factorizations of any
integer into shell nodes, so

```text
d_b<<D.                                                (5.2)
```

Every incidence in `H` is an ordered pair of distinct triples sharing `b`.
Conversely, such a pair has distinct row and color coordinates by pair
uniqueness.  The carrier belonging to an incidence is unique.  Consequently

```text
#supp(H) <=sum_b d_b(d_b-1)<<N D^2.                    (5.3)
```

Both sides of `H` have `asymp N^2` vertices, and therefore

```text
mean left degree, mean right degree <<D^2/N,
#{vertices with degree>=T}<<N D^2/T.                   (5.4)
```

The fixed proportional shell contains `N=q^(1+o(1))` nodes (the primes alone
suffice), so at the active scale

```text
D^2/N=q^(-1/33+o(1))=o(1).                            (5.5)
```

Thus almost every row pair and almost every color pair is isolated.  This is
a genuine averaged power gain.  It does not imply a spectral gain: a sparse
graph can still contain stars of degree `O(D)`, and an arbitrary coefficient
vector may concentrate on their color endpoints.  A local estimate or a
weighted theorem excluding that concentration is still required.

There is nonetheless an unconditional theorem for coefficients with large
participation ratio.  Put

```text
p_c=|z_c|^2,                 M_4=(sum_c p_c^2)^(-1).     (5.6)
```

For a left vertex `alpha`, its incident color pairs form a matching and its
degree is `O(D)`.  Cauchy--Schwarz gives

```text
|G_alpha|^2<<D sum_(gamma=(c,c') adjacent alpha) p_c p_c'. (5.7)
```

Sum (5.7) over `alpha` and group the edges by their unique carrier `b`.
Let `C_b` be the colors occurring in triples with that carrier and put
`P_b=sum_(c in C_b)p_c`.  The ordered distinct pairs at `b` have total
`p_c p_c'` mass at most `P_b^2`.  Since `|C_b|<<D`,

```text
P_b^2<<D sum_(c in C_b) p_c^2.                          (5.8)
```

Each fixed color occurs in only `O(D)` triples, again by the short product
interval.  Therefore

```text
sum_b P_b^2<<D^2 sum_c p_c^2,
||H(conjugate(z) tensor z)||_2^2<<D^3 sum_c |z_c|^4.    (5.9)
```

For `||z||_2=1`, the exact diagonal correction (2.7) now yields

```text
|Q_nd(z)|<<D+D^3/M_4.                                  (5.10)
```

This proves `(FC)` whenever

```text
M_4>=D^2 q^(-o(1)).                                    (5.11)
```

Conversely, (5.10) is an inverse theorem.  If, for a factor `Lambda` larger
than the harmless absolute constants,

```text
|Q_nd(z)|>=Lambda D,
```

then necessarily

```text
sum_c |z_c|^4 >> Lambda/D^2,
M_4 << D^2/Lambda.                                     (5.11a)
```

Thus any old-scale obstruction `|Q_nd|` of order `D^2` must concentrate on
effective color support `O(D)`.  This classification is unconditional even
though that sparse regime remains open arithmetically.

Combining (5.10) with the fourth-trace inequality also gives the explicit
operator interpolation

```text
||A_z||_op <<D^(1/4)*(1+D^2/M_4)^(1/4).                (5.11b)
```

It recovers the old square-root scale at `M_4` of order `D` and reaches the
quarter-power scale at `M_4>=D^2`.

No literal support or max-norm hypothesis is needed.  For a uniform vector
on `M` colors, `M_4=M`, so `M>=D^2` suffices.  At the active aperture the
threshold is `D^2=q^(32/33+o(1))`, strictly below the full-shell size
`N=q^(1+o(1))`.  The perfectly flat full-shell vector has Gram contribution

```text
D^3/N=D*(D^2/N)=D q^(-1/33+o(1)).                       (5.12)
```

There is also a complementary literal-support bound.  If `M=|supp(z)|`,
then restricting the carrier count gives

```text
#edges on supp(z)^2<<M D min(M,D),
sum_alpha degree_supp(alpha)^2<<M D min(M,D)^2.         (5.13)
```

For a uniform vector this is

```text
||H(conjugate(z) tensor z)||_2^2
 <<D M                              (M<=D),
 <<D^3/M                            (M>=D).             (5.14)
```

Abstract repeated Latin blocks show that the first bound can be sharp, so
support interpolation alone cannot close the remaining range.

The same obstruction is visible in a dyadic decomposition.  For a dyadic
piece of `ell^2` mass `s` and support `M`, ordinary row/column Schur gives

```text
||A_piece||<=||z_piece||_1<=s sqrt(M),                 (5.15)
```

which reaches the quarter-power **operator** target when `M<=sqrt(D)`.
This does not prove `(FC)` in that range; repeated Latin blocks show that
`(FC)` can fail while the operator target holds.  At the other end, (5.9)
proves `(FC)`, and hence the operator target, when `M>=D^2`.  For a roughly
uniform piece in between, the available fourth-trace bounds interpolate only
as

```text
s*(D M)^(1/4)                  (sqrt(D)<M<=D),
s*D^(3/4) M^(-1/4)            (D<=M<D^2).              (5.16)
```

Both are larger than `s D^(1/4)` in the open range
`sqrt(D)<M<D^2`.  Summing dyadic pieces therefore does not close arbitrary
`z`; it isolates the same intermediate-support arithmetic core.

### 5.1 A sharp weighted fixed-color second-moment gate

Let `m(C)` be the number of actual row/carrier completions of the ordered
color matrix

```text
C=(c11,c12;c21,c22),
w_z(C)=|z_c11 z_c12 z_c21 z_c22|.                  (5.17)
```

The proved fixed-determinant energy estimate gives, after summing the
`O(D)` possible nonzero determinants,

```text
sum_C w_z(C)<<D q^o(1)||z||_2^4.                   (5.18)
```

Consequently weighted Cauchy--Schwarz gives the exact sufficient gate

```text
[sum_C m(C)w_z(C)]^2
 <=[sum_C m(C)^2w_z(C)] [sum_C w_z(C)].             (5.19)
```

Thus the single global estimate

```text
sum_C m(C)^2w_z(C)<<D q^o(1)||z||_2^4              (5.20)
```

would prove `(FC)` directly.  This is strictly weaker than a uniform
`m(C)<<q^o(1)` theorem and is the precise way a second moment could turn the
already proved determinant energy into `D`.

The scale in (5.20) is sharp.  The full-integer tangent family has one
four-distinct color matrix with `m(C)=sqrt(D)-1`.  Taking `z` flat on its
four colors makes that single matrix contribute `asymp D` to the left side
of (5.20).  Hence neither an `o(D)` second moment nor a coefficient-uniform
replacement of `m(C)` by its unweighted average is available from geometry.
For arbitrary `z`, a high-multiplicity matrix can always be selected by
putting mass on its four colors.  The actual prime-power version of (5.20)
remains a new simultaneous short-divisor correlation theorem; it is not
proved here.

---

## 6. Unordered-hypergraph quotient and what it removes

Regard the symmetric retained support as an unordered triple system.  A
carrier wedge consists of

```text
{a,b,c},                    {a',b,c'},              (6.1)
```

and gives the `H` edge `(a,a')->(c,c')`.  Pair uniqueness makes the simple
part of this triple system linear.  If both triples in (6.1) have three
distinct nodes but the five displayed labels are not all distinct, then
linearity forces

```text
(c,c')=(a',a).                                      (6.2)
```

Thus the two oriented triples are the same unordered hyperedge.  These
permutation edges form a partial matching and have operator norm at most
one.

Triples with a repeated node are also spectrally cheap.  Let `m` be the
shell minimum and suppose `2H_0<8m(2m+1)`, as holds at the active scale.
For a fixed node in any specified coordinate there are at most three
repeated-node triples: one for each of the two equalities involving that
coordinate, by pair uniqueness, and at most one triple `(x,y,y)`, by

```text
8*x*|y^2-y'^2|>2H_0.                                (6.3)
```

Split the wedge incidence according to which of its two triples is
repeated.  On either split, fixing a left vertex leaves at most three
choices for the repeated first triple and then pair uniqueness fixes the
second; the same argument with colors fixes a right vertex.  Schur therefore
gives norm at most three for each orientation.  Combining both orientations
with (6.2), the whole non-five-distinct incidence `X` satisfies

```text
||X||<=7.                                            (6.4)
```

Writing `H=G+X`, where `G` retains only wedges with
`a,a',b,c,c'` pairwise distinct, and using the crude `||G||<<D`, gives for
every unit vector `xi`

```text
| ||H xi||_2^2-||G xi||_2^2 |<<D.                   (6.5)
```

Consequently the all-five-distinct estimate
`||G(conjugate(z) tensor z)||_2^2<<Dq^o(1)` would imply `(FC)`; repeated
nodes inside either carrier wedge are not the obstruction.

At the rectangle level there is now a stronger complete theorem.  Pair
uniqueness classifies every equality among

```text
a1,a2,b1,b2,c11,c12,c21,c22
```

into one of three types: adjacent unordered hyperedges are identical, one
corner is a square triple `{x,x,y}`, or opposite colors agree
`c11=c22`/`c12=c21`.  Let `Delta<<Dq^o(1)` be the maximum ordered triple
degree and let `sigma<=1` count square roots `{u,u,x}`.  Each of the three
types admits two color-pair projections whose fiber bounds have geometric
mean at most `Delta*sqrt(max(1,sigma))`.  Weighted Cauchy--Schwarz therefore
gives the explicit arbitrary-coefficient bound

```text
sum_repeated |z_c11 z_c12 z_c21 z_c22|
 <=18*Delta*sqrt(max(1,sigma))*||z||_2^4
 <<Dq^o(1)||z||_2^4.                                (6.6)
```

Thus **every** repeated-coordinate rectangle is closed, including the
opposite-corner modes not supplied by the tangent calculation alone.  The
remaining four-cycle sector has eight distinct displayed nodes and four
distinct unordered hyperedges.

The fully generic core nevertheless survives.  Actual-prime finite
data contain an all-five-distinct 3-core at `q=100003,U=24` and an
all-five-distinct 4-core at `q=25013,U=40`.  At the rectangle level, 86,878
of the 100,529 rectangles at `q=100003,U=24` use eight distinct coordinate
values.  Hence a permutation or repeated-node classification cannot prove
the remaining estimate.

---

## 7. Completed-grid determinant rigidity, and its exact limit

There is a genuine higher-rank identity.  Suppose a completed `3 x 3` grid
satisfies

```text
N_ij=Q+r_ij=8*a_i*b_j*c_ij,             |r_ij|<=H_0. (7.1)
```

Put `J` for the all-ones matrix and `R=(r_ij)`.  Column multilinearity of
`det(QJ+R)` leaves only terms with zero or one column from `QJ`; the terms
with two equal all-ones columns vanish.  Leibniz expansion gives the explicit
bound

```text
|det N|<=18*Q*H_0^2+6*H_0^3.                       (7.2)
```

On the other hand, diagonal factorization gives exactly

```text
det N=8^3*(product_i a_i)*(product_j b_j)*det(c_ij). (7.3)
```

Since the color determinant is integral, if `a_i,b_j>=m` and

```text
18*Q*H_0^2+6*H_0^3 < 8^3*m^6,                      (7.4)
```

then

```text
det(c_ij)=0.                                        (7.5)
```

At the active scale `Q=q^3`, `H_0<<qD`, `m>>q`, the leading ratio in
(7.4) is

```text
Q*H_0^2/q^6 << D^2/q=q^(-1/33+o(1)).               (7.6)
```

Thus (7.5) holds for every completed actual `3 x 3` grid for sufficiently
large `q`.  The same multilinear argument proves that every completed
`m x m` color matrix is singular for fixed `m>=3`: its upper bound is
`O_m(QH_0^(m-1)+H_0^m)`, whereas a nonzero color determinant costs
`>>_m q^(2m)`.  The exponent margin is

```text
2-m+(m-1)*(16/33)<0.                                (7.7)
```

This rigidity does **not** by itself give the needed spectral inverse
theorem.  A previously tempting abstract countermodel must, however, be
discarded after enforcing the full resource ledger.  One-factorize
`K_(2D)` and reuse the same `2D` colors in `R` matching components, with
`T` row-pair clones per component.  The resulting `H` is a union of
`K_(T,D)` blocks and is linear and grid-free if every incidence receives a
fresh carrier.  For the flat vector, every left output is `1/2`, whence

```text
||H(conjugate(z) tensor z)||_2^2=R*T/4.             (7.8)
```

But every color occurs in exactly `R*T` triples.  The actual color-degree
cap `R*T<=D` therefore makes (7.8) at most `D/4`, already at the desired
scale.  Taking `R=2D-1,T=D` creates the formerly advertised `~D^2`
output only by giving every color degree `D(2D-1)` and using
`D^2(2D-1)` fresh carriers.  It is not a countermodel under the full
hypotheses.

Consequently completed-grid forcing remains open rather than abstractly
refuted at super-target scale.  What is rigorously false is the weaker
claim that **target-size** mass forces a grid: disjoint properly colored
`K_(2,D)` blocks attain `asymp D` while containing no `K_(3,3)`.  The
determinant lemma and the corrected resource ledger are replayed in the
finite modules.

---

## 8. High moments: exact transport and the near-product obstruction

There is a second precise spectral formulation.  Identify the left and
right ordered-pair vertex sets.  For a carrier `b`, let

```text
phi_b(x)=c  iff  (x,b,c) is a retained triple.       (8.1)
```

Pair uniqueness and symmetry make `phi_b` a partial involution.  Up to its
unit-modulus edge weights, the carrier slice `H_b` is the coordinatewise
partial permutation

```text
(x1,x2) -> (phi_b(x1),phi_b(x2)),       H=sum_b H_b. (8.2)
```

This makes a trace-moment proof tempting.  The exact arithmetic along two
successive edges is as follows.  If

```text
Q+r=8*x*b*c,                 Q+s=8*c*d*y,
```

then cancellation of the middle node gives

```text
d*y*(Q+r)=b*x*(Q+s),
(d*y-b*x)*(Q+r)=b*x*(s-r).                    (8.3)
```

In particular, `|r|,|s|<=H_0` with `H_0<<qD` implies
`|d*y-b*x|<<D`.  Thus a two-step walk is an exact near-dilation, but not an
exact dilation.

More generally, let one coordinate of a closed walk be

```text
x_0 --b_1--> x_1 --b_2--> ... --b_(2k)--> x_(2k)=x_0
```

and put `Q+r_j=8*x_(j-1)*b_j*x_j`.  Multiplication over alternating edges
cancels every `x_j` exactly and proves

```text
 prod_(j odd) b_j       prod_(j odd) (Q+r_j)
 ---------------- =    ----------------------- .           (8.4)
 prod_(j even) b_j      prod_(j even) (Q+r_j)
```

The second coordinate of the ordered-pair walk gives a second
residual-product representation of the same carrier ratio.

If closure forced the odd and even carrier **multisets** to agree, the
moment bound would follow quickly.  From a starting ordered pair there are
`O(D)` choices per odd step; the even labels would then be a permutation of
the odd labels.  Consequently one would have, schematically,

```text
tr((H H*)^k) << N^2 D^k k! q^o(k),                         (8.5)
```

and a slowly growing `k` would give `||H||<<sqrt(D)q^o(1)`.

That pairing statement is false even on the actual prime shell.  At
`q=25013`, cutoff `U=12`, the support graph contains the four-cycle

```text
L1=(10429,11393),       L2=(11423,12479),
R1=(12479,11423),       R2=(15031,13759),
```

whose cyclic carrier sequence is

```text
15031, 13723, 11393, 12479.
```

Its alternating products are

```text
15031*11393 = 171248183,
13723*12479 = 171249317,                    difference=-1134. (8.6)
```

Thus both exact product equality and multiset pairing already fail at the
fourth moment.

Equation (8.4) explains the size of the failure but does not count it.  Since
`Q=q^3` and `H_0<<qD`, it gives only

```text
log(P_odd/P_even)<<kD/q^2,
|P_odd-P_even|<<kD q^(k-2),                             (8.7)
```

where each carrier product has size `q^k`.  A generic divisor estimate must
inspect every integer in the last interval and therefore pays essentially
its length.  The two-factor short-interval Sidon lemma applies when the two
near-`Q` products are already equal; it does not turn (6.7) into equality.
For three and more near-`Q` factors, its coefficient-by-coefficient proof
also loses the inequality `H_0^k<Q`.

The viable high-moment replacement is therefore a new theorem: for a fixed
starting ordered pair and fixed odd carrier labels, only `q^o(k)` compatible
even-label sequences should close **both** coordinate walks.  Neither
(8.3), (8.4), the divisor bound, nor residual Sidonicity proves that joint
near-product statement.  This is the exact obstruction to the trace route.

The identities and the unequal-product witness are replayed in
`qp_four_cycle_spectral_gate.py`.

---

## 9. Character expansion: principal differences survive the quotient

The hard residual cutoff has an exact multiplicative-character expansion
modulo `Q=q^3`.  Let `Phi=phi(Q)`, let

```text
D(chi)=sum_(r in I) chi(r),
Z(chi)=sum_(c in S) z_c chi(c),
t_chi=Phi^-1 chi(8) conjugate(D(chi)) Z(chi).        (9.1)
```

Then

```text
A_z(a,b)=sum_chi t_chi chi(a)chi(b).                 (9.2)
```

Put `K(eta)=sum_(x in S)eta(x)`.  Expanding the two nondegenerate row and
column sums exactly gives

```text
Q_nd=sum_(chi1,...,chi4) t1 conjugate(t2) t3 conjugate(t4)
 [K(chi1 conjugate(chi4))*K(chi3 conjugate(chi2))-K(Omega)]
 [K(chi1 conjugate(chi2))*K(chi3 conjugate(chi4))-K(Omega)], (9.3)

Omega=chi1*chi3*conjugate(chi2*chi4).
```

This formula answers the principal-mode question negatively.  Character
differences becoming principal do not correspond exactly to repeated
coordinates or tangent rectangles.  For example, when
`chi1=chi2, chi3=chi4`, the second bracket in (9.3) is

```text
N^2-N=N(N-1),                                        (9.4)
```

so it survives the deletion `b1!=b2`.  When all four characters agree, the
exact contribution is

```text
|t_chi|^4 N^2(N-1)^2.                                (9.5)
```

It is supported throughout the coordinate-generic sum, not only on a
repeated-node sector.  The base principal character itself is harmless:
using `|D(1)|<<H_0` and `|Z(1)|<=sqrt(N)` bounds its (9.5) term by

```text
H_0^4*N^6/Phi^4=q^(-2/33+o(1)).                      (9.6)
```

But the full repeated-difference families remain.  Standard positive
large-sieve or Burgess estimates do not remove them after the geometric
quotient; closing (9.3) requires a joint signed four-character estimate,
not merely deletion of the principal base character.

---

## 10. Why the standard modular-hyperbola theorem does not close it

Cilleruelo--Garaev's small-box theorem gives a divisor-sized count for a
**fixed** congruence `xy=lambda (mod p)` in a box of side below `p^(1/4)`.
The coherence scale `sqrt(D)=q^(8/33+o(1))` is indeed below `q^(1/4)`.
However, (4.7) does not retain a fixed residue: the allowed product residual
in (4.2) ranges through an interval of length `qD`, longer than the
modulus.  Introducing that residual produces `O(D)` residue layers and loses
the desired saving.  Therefore that theorem is not directly applicable to
(4.7).

Primary source:

J. Cilleruelo and M. Z. Garaev, *Concentration points on two and three
dimensional modular hyperbolas and applications*,
<https://arxiv.org/abs/1007.1526>.

The August 2026 Mohammadi and Milićević--Qin--Wu bilinear Kloosterman
theorems have also been checked at the exact active exponents.  The former's
phase is relevant but its independent-box hypothesis does not match (4.7);
the latter would save only `q^(-1/275+epsilon)` in the most optimistic
length-`D`, modulus-`q` model and has a complete `Kl_2` kernel rather than
the reciprocal graph.  See
`ZETA23-QP-FOUR-CYCLE-NEW-BILINEAR-KLOOSTERMAN-RANGE-AUDIT-2026-08-15.md`.

Finite replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_spectral_gate.py
```

---

## 11. Status

```text
row-pair Gram/incidence identity:                     PROVED;
diagonal correction bounded by D:                    PROVED;
sqrt(D) two-sided degree criterion implies FC:        PROVED;
support degeneracy q^o(1) implies FC:                 PROVED;
non-five-distinct carrier-wedge incidence norm O(1): PROVED;
all repeated-coordinate Q_nd contribution O(Dq^o): PROVED;
reduction to eight-distinct loose rectangles:       PROVED;
completed 3x3 color determinant is zero:             PROVED;
completed fixed m>=3 color determinant is zero:      PROVED;
super-target rank-one output forces completed 3x3:   OPEN;
target-size rank-one output forces completed 3x3:    FALSE ABSTRACTLY;
each fixed residual-shift layer is a matching:         PROVED;
elementary two-sided degree O(D):                     PROVED;
mean two-sided degree D^2/N=q^(-1/33+o(1)):           PROVED;
FC for participation ratio M_4>=D^2 q^(-o(1)):        PROVED;
FC for uniform support M>=D^2:                       PROVED;
large-Q participation-ratio inverse theorem:          PROVED;
weighted multiplicity second moment D => FC:          PROVED CONDITIONALLY;
actual weighted multiplicity second moment D:         OPEN;
two-sided degree D^(1/2) q^o(1):                     OPEN;
support degeneracy q^o(1):                            OPEN;
closed-walk carrier multiset pairing:                 REFUTED FINITELY;
joint near-product closed-walk count q^o(k):           OPEN;
principal character-difference modes equal tangents: REFUTED ALGEBRAICALLY;
new bilinear Kloosterman papers directly imply FC:    NO;
uniform all-pair power-improved degree theorem:       NOT PROVED;
four-cycle estimate (FC):                             NOT PROVED.
```
