# QP two-star gate: short-interval tangent peeling does not close the residual

**Date:** 2026-08-23  
**Verdict:** partitioning the common carrier into intervals of length
`L<=c*sqrt(D)` exactly identifies every locally rich row-pair fibre as a
simultaneous affine/tangent packet.  Those pair incidences can be assigned
to tangent packets without a positive cross-term ambiguity.  Even granting
their complete merger, however, the only local conclusion for the remainder
is

```text
at most two common carriers per (ordered row pair, b-interval). (0.1)
```

There are `q/L>>D` intervals, while one row pair already has the elementary
degree allowance `D`.  Thus all `D` residual carriers can occupy different
intervals, and the global two-star estimate remains

```text
E2(A)<=M*D^2*q^o(1),                              (0.2)
```

not the required `M^2`.  At `M=D^(15/8)`, the gap is exactly

```text
D^2/M=D^(1/8).                                    (0.3)
```

This is not merely a loose ledger.  An explicit cyclic Latin-block
incidence system satisfies every pair-uniqueness and degree condition,
has no locally rich row-pair interval at all, and gives

```text
E2(A)~M*D^2,
||B||_(2->2)=D,
flat factorial trace ~D^3/M=D^(9/8).              (0.4)
```

The construction is an abstract incidence obstruction matching all three
product-window pair-uniqueness properties, not an actual-prime-power QP
configuration: it does not impose the linked
reciprocal equations `8abc=q^3+O(qD)`.  Its role is exact.  The local
three-carrier classification, tangent peeling, pair uniqueness, degree
bounds, and intervalwise Schur estimates alone cannot prove the two-star
bound.  A successful proof must use a genuinely cross-interval arithmetic
correlation of the reciprocal lifts; equivalently, it must control the
off-diagonal character correlation left by the exact multiplicative
expansion.

There is also a literal full-integer tangent packet with
`E2(A)>>M^2`.  It is removed by the tangent peel and therefore does not
contradict a **residual** two-star theorem, but it proves that an unpeeled
global `E2<=M^2` statement is false even before the prime-power mask.

---

## 1. Exact two-star formulation

Let `S=S_q` be the actual prime-power project shell and let `A` be a flat
coefficient support of size `M`.  Define

```text
T_(b,c)=1
```

when there is an `a in S` such that

```text
|8*a*b*c-q^3|<=C*q*D.                             (1.1)
```

For fixed `(b,c)`, the allowed `a` interval has length `O(D/q)<1`, so `a`
is unique.  Put

```text
d_b=sum_(c in A) T_(b,c).                          (1.2)
```

The product interval and divisor/Sidon bounds give

```text
d_b<<D*q^o(1),
sum_b d_b<<M*D*q^o(1).                             (1.3)
```

The ordered two-star count is

```text
E2(A)=sum_b d_b*(d_b-1).                           (1.4)
```

To retain the row information, let

```text
alpha=(a_1,a_2),          gamma=(c_1,c_2),
B_(alpha,gamma)=1
```

if one common carrier `b` supports the two triples

```text
(a_1,b,c_1),              (a_2,b,c_2).             (1.5)
```

The common carrier is unique after `(alpha,gamma)` is fixed.  Therefore

```text
#supp(B)=E2(A).                                     (1.6)
```

If `r_alpha` is the row sum of `B`, the raw occupied-rectangle count is

```text
I_occ=sum_alpha r_alpha*(r_alpha-1).                (1.7)
```

The fixed-row interval bound gives `r_alpha<<D*q^o(1)`, hence

```text
I_occ<<D*E2(A)*q^o(1).                             (1.8)
```

For flat support, `E2(A)<<M^2*q^o(1)` is therefore a sufficient route to
the sharp trace.  It is stronger than necessary: (1.7) depends on how the
support of `B` is dispersed among its rows, while (1.6) forgets that
dispersion.

## 2. What the local three-carrier theorem actually gives

Fix an ordered row pair `alpha=(a_1,a_2)`.  Its common carriers have unique
color pairs `(c_i,d_i)`.  Suppose three lie in a numeric interval of length
`L`, and write

```text
b_1=b_2-u<b_2<b_3=b_2+v,
c_i=N_1/b_i+e_i,                 |e_i|<<D/q.        (2.1)
```

The exact second determinant satisfies

```text
|u*c_3+v*c_1-(u+v)*c_2|
 <<L^3/q+D*L/q.                                    (2.2)
```

For `L<=c*sqrt(D)` with a sufficiently small fixed `c`, the right side is
`o(1)` because

```text
D^(3/2)/q=D^(-9/16)=o(1).                          (2.3)
```

Thus (2.2) vanishes as an integer.  The same identity holds for the second
colors `d_i`.  Every triple in a fixed rich cell is collinear in both
`(b,c)` and `(b,d)`, so all its points lie on one exact simultaneous affine
packet.  The fixed-row primitive-direction theorem also merges all short
chords into one tangent direction.

Partition the `b` shell into half-open intervals `I` of length `L`.  Assign
each edge of `B` to its unique pair `(alpha,I)`.  Declare the cell rich if
it contains at least three edges.  This is a partition of the **pair
incidences themselves**, not a partition of the original `T` edges, so
there is no omitted term of the form `2*d_rich*d_sparse`: every ordered
pair at `b` belongs to exactly one cell.

After the rich cells are assigned to the tangent treatment, the residual
obeys

```text
r_(alpha,I)<=2.                                    (2.4)
```

That is the complete positive conclusion of the local classification.

## 3. Exact residual ledger

The number of intervals is

```text
Q_b~q/L>=q/sqrt(D)=D^(25/16).                     (3.1)
```

Since `D^(25/16)>>D`, the elementary allowance of `D` common carriers for
one row pair can be placed one per interval while satisfying (2.4).  Hence

```text
E2_res
 =sum_(alpha,I) r_(alpha,I)
 <=sum_b d_b*(d_b-1)
 <=D*sum_b d_b*q^o(1)
 <=M*D^2*q^o(1).                                  (3.2)
```

No power improves in (3.2).  At the critical flat support,

```text
M=D^(15/8),
M*D^2/M^2=D^(1/8).                                (3.3)
```

Even peeling cells rich on the color-pair side does not create
orthogonality.  Write

```text
B_res=sum_I B_I.                                   (3.4)
```

After two-sided peeling, each `B_I` may have row and column degree at most
two and therefore bounded operator norm.  Their supports are disjoint, but
the positive cross products `B_I^* B_J` need not vanish.  A union of `D`
permutation matrices has norm `D`, despite every summand having norm one.
Thus intervalwise Schur followed by square-function summation assumes the
very cross-interval decorrelation which remains to be proved.

There is an even more basic mismatch between (2.4) and the support target
`E2<=M^2`.  One carrier of degree `D` contributes `D*(D-1)` distinct
ordered row pairs, each with cell load one.  If the row-pair blocks of
different carriers are disjoint, then

```text
E2~M*D^2,                 but r_alpha<=1 and I_occ=0. (3.5)
```

Such a linear block packing is cardinality-feasible at the critical scales:

```text
M*D^2=D^(62/16)<N^2=D^(66/16),                    (3.6)
```

where `N=q^(1+o(1))` is the row-shell size.  Pair labels can be assigned so
that all three two-coordinate projections remain injective.  This abstract
star-dispersion model shows why `E2` is stronger than the factorial/Schur
quantity: it counts many harmless fresh-row stars.  The cyclic fixture in
the next section additionally shows that the same local hypotheses also
permit coherent cross-interval aggregation which is genuinely harmful.

## 4. A residual Latin-block saturator

The preceding warning has an exact finite realization.  Let `delta` be an
integer on the scale `D`, let `G` be an integer on the scale `M/D`, and use
the cyclic group `Z/delta Z`.  For every group `g=1,...,G`, introduce

```text
rows:       a_(g,i),       i in Z/delta Z,
colors:     c_(g,j),       j in Z/delta Z,
carriers:   b_(g,s),       s in Z/delta Z.         (4.1)
```

Put a triple in `T` exactly when

```text
(a_(g,i), b_(g,s), c_(g,i+s))                     (4.2)
```

for some `(g,i,s)`.  All indices in (4.2) are modulo `delta`.

Every pair of displayed coordinates determines the third:

```text
(a_(g,i),b_(g,s)) determines c_(g,i+s),
(b_(g,s),c_(g,j)) determines a_(g,j-s),
(a_(g,i),c_(g,j)) determines b_(g,j-i).            (4.3)
```

Thus the system has the exact three pair-uniqueness properties of the
product window.  Every row, color, and carrier has degree `delta`.

There are

```text
M_0=G*delta                                        (4.4)
```

colors and carriers.  Assign, for each fixed `g`, its `delta` carrier
labels to `delta` distinct intervals of the partition in Section 2.  This
is compatible with the project cardinalities: `Q_b>>delta`, and the total
number of carrier slots is `q>>M_0`.  A balanced assignment has only

```text
M_0/Q_b=D^(5/16+o(1))<L                            (4.5)
```

labels per interval.  Therefore actual integer positions can be assigned
without collision at the level of this abstract model.

Fix an ordered row pair

```text
alpha=(a_(g,i),a_(g,i')),        i!=i'.            (4.6)
```

It has all `delta` carriers `b_(g,s)` as common carriers, but by construction
at most one lies in any short interval.  Hence there are no rich cells at
all.  For each `s`, its color-pair neighbor is

```text
gamma_s=(c_(g,i+s),c_(g,i'+s)).                    (4.7)
```

The `gamma_s` are distinct, so every row of `B` has degree `delta`.  The
same calculation backwards gives every column degree `delta`.  Each group
component is a `delta`-regular bipartite graph and consequently

```text
||B||_(2->2)=delta.                                (4.8)
```

The exact counts are

```text
E2=M_0*delta*(delta-1),                            (4.9)

I_occ=M_0*delta*(delta-1)^2.                       (4.10)
```

Indeed there are `M_0` carriers of degree `delta`; alternatively there are
`G*delta*(delta-1)` ordered row pairs, each of `B`-degree `delta`.

Give every one of the `M_0` colors the flat coefficient
`M_0^(-1/2)`.  The normalized factorial contribution is

```text
I_occ/M_0^2
 =delta*(delta-1)^2/M_0
 ~D^3/M.                                           (4.11)
```

At `M=D^(15/8)`, this is `D^(9/8)`.  Likewise

```text
E2/M^2~D^2/M=D^(1/8).                              (4.12)
```

The model therefore reproduces both exact losses in the residual, while
every short-interval tangent test is vacuous.

For the all-distinct subform, discard pairs of shifts for which two of the
four displayed colors coincide.  For each ordered row pair there are only
`O(delta)` such bad ordered shift pairs out of `delta*(delta-1)`, so (4.10)
and (4.11) retain their orders of magnitude.

The qualification is essential.  Arbitrary labels in (4.1) need not obey

```text
8*a_(g,i)*b_(g,s)*c_(g,i+s)=q^3+O(qD).            (4.13)
```

Indeed, ruling out a power-sized Latin block by the linked equations
(4.13) is one possible formulation of the missing global arithmetic
theorem.  The model proves that (4.13), or an equivalent reciprocal
large-sieve input, must be used across different intervals.

### 4.1 The exact reciprocal equations reject the complete cyclic block

There is a useful positive check: the literal cyclic fixture (4.2) cannot
itself be embedded in the project product windows when `delta~D`.  Suppose
for contradiction that all its labels are shell integers satisfying
(4.13), and put

```text
X_s=q^3/(8*b_(g,s)).                               (4.14)
```

After division by `b_(g,s)~q`, every edge gives

```text
|a_i*c_(i+s)-X_s|<<D.                              (4.15)
```

All indices below are cyclic modulo `delta`.  Set `j=i+s`.  Take the
determinant of the four instances of (4.15) at
`(i,s),(i+1,s+1),(i,s+1),(i+1,s)`.  The two center products
`X_s*X_(s+1)` cancel exactly, giving

```text
|a_i*a_(i+1)*(c_j*c_(j+2)-c_(j+1)^2)|<<q^2*D.
```

Since `a_i*a_(i+1)~q^2`,

```text
|c_j*c_(j+2)-c_(j+1)^2|<<D                       (4.16)
```

for every `j`.  Put `rho_j=c_(j+1)/c_j`.  Then

```text
|rho_(j+1)-rho_j|<<D/q^2.                          (4.17)
```

The cyclic product of the `rho_j` is one, so one lies on each side of one
unless they are all one.  Equations (4.17) and `delta<<D` therefore imply

```text
|rho_j-1|<<D^2/q^2,
|c_(j+1)-c_j|<<D^2/q=o(1),                         (4.18)
```

because `q/D^2=D^(1/16+o(1))` tends to infinity.  The integral colors must
all be equal, contradicting the distinct cyclic vertices.

Thus the canonical graph saturator is arithmetically forbidden, but its
rejection uses a chain of product equations from many **different** carrier
intervals.  It cannot be recovered from (2.2) or intervalwise Schur.  A
general proof would need an inverse theorem turning large residual
two-star/operator mass into enough linked multiplicative cycles for the
rigidity (4.16)--(4.18) to apply.  That inverse theorem is not currently
proved.

## 5. An unpeeled full-integer tangent obstruction

The global two-star inequality is false for unrestricted full-integer
product-window nodes even before one considers the sparse Latin model.
Let

```text
q=2*m,                 D=100*L^2,
0<=i,u<L,              j=2*L+u,
b=m-i-j-1.                                           (5.1)
```

For every `(i,u)`, retain the two triples

```text
(m+i,   b, m+j+1),
(m+i+1, b, m+j).                                    (5.2)
```

Direct expansion places both products in the window
`|8abc-q^3|<<qD` when `m` is sufficiently large compared with `L`; all
five displayed nodes are distinct.  The color support is

```text
A={m+2L,...,m+3L},            |A|=M=L+1.            (5.3)
```

For `k=i+u`, let

```text
r_k=#{(i,u) in [0,L)^2 : i+u=k}.                   (5.4)
```

The carrier depends only on `k`, and its color degree is `r_k+1`.
Therefore

```text
E2(A)=sum_k (r_k^2+r_k)
     =L*(L+1)*(2L+1)/3
     ~2*L^3/3>>M^2.                                (5.5)
```

This fixture is one coherent tangent packet, so the rich-cell merger is
the correct treatment.  It is not an obstruction to a tangent-peeled
residual theorem, and its nodes are not required to be prime powers.

## 6. The surviving theorem

After tangent packets are removed, the desired positive statement is

```text
E2_sparse(A)
 :=sum_(alpha,I sparse) r_(alpha,I)
 <<M^2*q^o(1).                                     (6.1)
```

The more faithful operator version is

```text
||B_sparse||_(2->2)^2<<D*q^o(1).                  (6.2)
```

Neither follows from (2.4).  In the exact multiplicative-character
expansion of `sum_b d_b^2`, the principal term and the equal-character
nonprincipal diagonal are already below `M^2`; the remaining term couples
two distinct characters through the shell transform of `b`.  Equations
(6.1)--(6.2) are therefore a cross-interval joint restriction theorem, not
a local tangent-classification corollary.

```text
three carriers in a sqrt(D) interval are tangent:   PROVED;
rich pair-incidences can be assigned without cross terms: PROVED;
residual consequence r_(alpha,I)<=2:               PROVED;
residual E2<=M^2 from local/degree data:             FALSE;
abstract residual Latin saturation MD^2:            EXPLICIT;
literal unpeeled integer tangent E2>M^2:             EXPLICIT;
actual-prime sparse reciprocal E2 or operator bound: OPEN.
```
