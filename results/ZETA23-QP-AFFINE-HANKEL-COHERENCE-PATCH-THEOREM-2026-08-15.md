# QP four-cycle: affine/Hankel coherence-patch theorem

**Date:** 2026-08-15  
**Parallel-line addendum:** 2026-08-17  
**Verdict:** a whole family of overlapping rational tangent clusters can be
merged into one affine/Hankel patch.  If that merged patch uses `M` colors
and each color occurs on at most `L` carrier pairs, then for arbitrary
complex color coefficients

```text
tr((A_z A_z*)^2)
 <=L min(L,M) ||z||_2^4.                           (0.1)
```

Thus `LM<<D` closes the patch directly, without any bounded-reuse estimate
for its constituent fixed-color completion clusters.  In particular the
multilevel translation obstruction, despite having `Theta(D)` cluster reuse
and a false `D`-scale off-diagonal pair energy, has direct fourth trace
`O(D)`.

This is a local narrow/coherent theorem.  A global decomposition controlling
cross terms between genuinely different affine planes is not proved here.

The addendum proves one broader merger.  Fixing the primitive four-carrier
direction, all affine carrier lines with at least three occupied points
merge at fourth-trace strength even when their intercepts and common levels
vary and they do not lie in one three-variable affine plane.  Distinct
primitive directions and one- or two-point lines remain open.

---

## 1. Partial-matching lemma

Let `E` be a pair-unique set of triples `(a,b,c)`, let `E_c` be a patch of
its colors, and put

```text
A_z(a,b)=sum_c z_c kappa(a,b,c),       |kappa|<=1. (1.1)
```

Pair uniqueness makes the sum in each cell contain at most one term.  It
also makes every fixed-color matrix

```text
P_c(a,b)=kappa(a,b,c)                                  (1.2)
```

a weighted partial permutation, so `||P_c||_op<=1`.

Suppose the patch uses at most `M` colors and every color occurs in at most
`L` triples.  Then

```text
||A_z||_F^2
 =sum_c |z_c|^2 sum_((a,b,c) in E)|kappa(a,b,c)|^2
 <=L ||z||_2^2,                                     (1.3)
```

while

```text
||A_z||_op
 <=sum_c |z_c| ||P_c||_op
 <=sqrt(M) ||z||_2.                                 (1.4)
```

For the singular values `sigma_j` of `A_z`, first

```text
tr((A_z A_z*)^2)=sum_j sigma_j^4
 <=(max_j sigma_j^2) sum_j sigma_j^2
 <=L M ||z||_2^4.                                  (1.5)
```

But also `||A_z||_op^2<=||A_z||_F^2`, so (1.3) gives the independent bound

```text
tr((A_z A_z*)^2)<=||A_z||_F^4<=L^2||z||_2^4.      (1.6)
```

Taking the better of (1.5) and (1.6) proves (0.1).  It also bounds the absolute nondegenerate rectangle mass
after replacing `z` and `kappa` by their absolute values.

---

## 2. Why affine planes identify coherence blocks

Suppose all triples in a patch satisfy

```text
alpha*a+beta*b+gamma*c=N.                           (2.1)
```

For fixed `c`, equation (2.1) cuts out one arithmetic anti-diagonal in the
row--column plane.  Its retained entries form the partial matching `P_c`.
Consequently an arbitrary number of local parameterizations or fixed-color
tangent orbits lying in the same plane must be counted only after taking
their union: duplicate edges disappear, and (1.5) depends on the total
anti-diagonal length and total color support, not on how many charts listed
the edges.

For example, if the row and column intervals have lengths `W_a,W_b`, then
with `g=gcd(alpha,beta)` a fixed color has at most

```text
1+min(g W_a/|beta|, g W_b/|alpha|)                 (2.2)
```

integer entries.  Combining (2.2) with the number of colors gives an
explicit geometric version of `LM`.

---

## 3. The multilevel translation family closes directly

In the exact full-integer family

```text
a_i=m+i h+t,
b_j=m+j l-t,
c_ij=m-i h-j l,                                    (3.1)
```

all triples, for every `h,l,t`, obey

```text
a_i+b_j+c_ij=3m.                                   (3.2)
```

Taking the union over `h,l in [L,2L]`, `h!=l`, and
`t in [20L,21L]` yields only `3L+1` colors.  For a fixed color, (3.2) makes
the occupied cells an anti-diagonal, and the row support lies in an interval
of length `3L`; hence its matching has at most `3L+1` entries.  Theorem
(1.5) gives

```text
tr((A_z A_z*)^2)<=(3L+1)^2 ||z||_2^4.              (3.3)
```

The literal product-window normalization in the companion construction is
`D=2048L^2`, so (3.3) is `O(D)`.  This remains true for the spiked vector
that makes the completion-pair second moment `Theta(D^(5/4))`.  The gap
between those two quantities is precisely why the second-moment route is
too strong.

The same argument applies to the rational translation grid

```text
a_i=A+R i+t,       b_j=A+R j-t,
c_ij=C-S(i+j),       RC=SA,                        (3.4)
```

because all its triples lie on

```text
S*a+S*b+R*c=2SA+RC.                                (3.5)
```

Whenever its merged anti-diagonal length times its color-support size is
`O(D)`, its entire fourth trace is at target strength.

---

## 4. Shared-progressions pin the slope product

There is one rigorous piece of cross-plane control for exact linearized
charts.  Suppose two blocks use the same color anchor `C` and color step
`U`.  Write their positive row/column steps as `(R,S)` and `(R',S')`.
Exact first-order cancellation at the anchor says

```text
U A=R C,       U B=S C,
U A'=R' C,     U B'=S' C.                           (4.1)
```

If both anchors lie in the common product window

```text
|8ABC-Q|<=H,       |8A'B'C-Q|<=H,                  (4.2)
```

then multiplication by `U^2` and subtraction give

```text
8 C^3 |RS-R'S'| <=2H U^2.                          (4.3)
```

At the QP scale `C asymp q`, `H asymp qD`.  Hence whenever

```text
U^2 <<q^2/D,                                       (4.4)
```

the right side of (4.3) is smaller than the quantum `8C^3`, and

```text
RS=R'S'.                                           (4.5)
```

A nontrivial coherent block has `U<=sqrt(D)` after the ordinary curvature
bound, and `D<q`; therefore (4.4) holds throughout the power-sized tangent
range.  For fixed `U`, (4.5) leaves only

```text
tau(RS)=q^o(1)                                     (4.6)
```

ordered slope pairs.

There is also a simple overlap consequence.  If two exact color arithmetic
progressions contain the same two distinct colors, each primitive step
divides their difference.  That difference has only `q^o(1)` divisors.
Combining this with (4.6), only `q^o(1)` exact pinned slope types can pass
through a fixed color pair.  This rules out the abstract repeated-Latin
mechanism inside the exact shared-progression model.

It does not yet control approximate charts whose colors are not on one exact
arithmetic progression, nor the translation thickness surrounding a pinned
linear chart.

---

## 5. Window-thickened shared-progressions also close

The translation thickness can in fact be included for a complete linear
grid.  Fix shell constants, `H<<qD`, and integers `C,U,n` with `n>=2`.
Consider **all** tuples `(A,B,R,S)` for which

```text
a_i=A+Ri,       b_j=B+Sj,       c_ij=C-U(i+j),
0<=i,j<=n,                                         (5.1)
```

lie in the fixed shell and satisfy

```text
|8 a_i b_j c_ij-Q|<=H                              (5.2)
```

at every cell.  No exact first-order cancellation is assumed.

Put `C_n=C-Un` and

```text
delta_A=UA-R C_n,       delta_B=UB-S C_n.           (5.3)
```

Subtracting the products at `(n,0)` and `(0,0)` gives exactly

```text
(A+Rn)B(C-Un)-ABC=-Bn delta_A.                     (5.4)
```

The two products in (5.4) both lie in an interval of length `H/4`, so

```text
|delta_A|<<D/n,        |delta_B|<<D/n.              (5.5)
```

Since `UA=R C_n+delta_A` and all nodes are comparable with `q`, (5.5) and
`D=o(q)` imply

```text
R asymp U,             S asymp U.                  (5.6)
```

There is also an exact curvature bound.  For `k=floor(n/2)` and

```text
f(i)=B(A+Ri)(C-Ui),
```

one has

```text
f(0)-2f(k)+f(2k)=-2BRU k^2.                        (5.7)
```

Equations (5.2) and (5.7), and their column analogues, give

```text
RU n^2<<D,       SU n^2<<D,
U^2 n^2<<D.                                         (5.8)
```

The slope product still pins despite the thickness.  From (5.3),

```text
U^2ABC
 =C(R C_n+delta_A)(S C_n+delta_B).                 (5.9)
```

Using (5.2), (5.5), and (5.6) in (5.9), two members of the family satisfy

```text
|RS-R'S'|
 << D U^2/q^2 + U D/(nq) + D^2/(n^2q^2).          (5.10)
```

By (5.8), at `D=q^(16/33+o(1))` the right side is

```text
<<D^2/(n^2q^2)+D^(3/2)/(n^2q)
 =q^(-9/33+o(1))/n^2=o(1).                         (5.11)
```

Thus all the integral products `RS` are equal, and there are only `q^o(1)`
slope pairs in the entire thickened family.

For one fixed slope `R`, (5.3)--(5.5) put every possible row base `A` in an
interval of length `O(D/(Un))`.  Its rows therefore belong to an interval
of length

```text
O(Rn+D/(Un)).                                      (5.12)
```

After summing the `q^o(1)` pinned slopes, pair uniqueness bounds the maximum
degree of one color by

```text
L<<q^o(1)(Rn+D/(Un)).                              (5.13)
```

The common color support has `M=2n+1`.  Hence (5.8), (5.13), and the
coherence-patch theorem give

```text
LM<<q^o(1)(R n^2+D/U)<<D q^o(1),                  (5.14)

tr((A_z A_z*)^2)<<D q^o(1)||z||_2^4.              (5.15)
```

### Theorem 5.1 (thickened exact-AP narrow theorem)

For fixed `(C,U,n)`, the union of every complete active grid (5.1), with
arbitrary integral row/column bases and steps, satisfies the direct
fourth-trace target (5.15).  In particular, parallel intercepts and nearby
approximate tangents do not recreate the repeated-Latin obstruction.

The restriction `n>=2` is material: three points in each carrier direction
are what expose the quadratic curvature in (5.7).  Isolated `2 by 2`
rectangles belong to the broad remainder.

---

## 6. Parallel rational lines in a product band

The common-affine-plane hypothesis is not needed for lines having one fixed
four-carrier direction.  The extra input is the actual product band.

Fix a color `c`.  Its row--column support lies in

```text
E_c={(a,b) in Z^2: a,b~q, |ab-N_c|<=Delta},
N_c=q^3/(8c),                 Delta<<D.             (6.1)
```

At the project scale `q=D^(33/16+o(1))`, so

```text
q>>D^2.                                             (6.2)
```

Consider an integral affine line containing at least `T>=3` occupied
points of `E_c`.  An axis-parallel or same-sign line contains at most one
point, since one primitive step changes `ab` by `>>q>D`.  The remaining
case has primitive direction `(p,-s)`, with `p,s>0`, and invariant

```text
W=s*a+p*b.                                         (6.3)
```

Along the line,

```text
4*p*s*a*b=W^2-(s*a-p*b)^2,
max(ab)=W^2/(4*p*s).                               (6.4)
```

The inverse image of the interval in (6.1) has at most two real
components.  One component contains at least `ceil(T/2)` occupied integer
parameters.  Missing intermediate points cause no problem: its first and
last occupied parameters still have separation at least
`ceil(T/2)-1`.  Comparing that span with the quadratic in (6.4) gives

```text
p*s*T^2<<D.                                        (6.5)
```

If the vertex in (6.4) lies above the product interval, the length of one
branch is

```text
{sqrt(A+O(D))-sqrt(A)}/sqrt(p*s),                  (6.6)
```

where `A` is the excess of the vertex.  Equations (6.5)--(6.6) imply

```text
W^2=4*p*s*N_c+O(D^2/T^2).                          (6.7)
```

Since `W~q*(p+s)>>q*sqrt(p*s)`, consecutive positive values of `W` have
squares separated by `>>q*sqrt(p*s)`.  Equations (6.2) and (6.7) therefore
leave `O(1)` possible invariants `W` for fixed `(c,p,s)`.  This is the
cross-level pinning: arbitrary intercepts do not create polynomially many
parallel rich lines.

The complete intersection of one such geometric line with `E_c` has

```text
<<1+sqrt(D/(p*s))                                  (6.8)
```

integer points.  Now fix a primitive four-carrier direction

```text
delta=(d1,d2,e1,e2).                               (6.9)
```

For cell `(i,j)`, put

```text
g_ij=gcd(|d_i|,|e_j|),
mu_ij=|d_i*e_j|/g_ij^2.                            (6.10)
```

The cell projection has primitive direction product `mu_ij`.  Every color
can occur in each of the four positions, so (6.7)--(6.8) bound its degree
in the union of **all** rich carrier lines with direction `delta` by

```text
L_delta
 <<sum_(i,j) (1+sqrt(D/mu_ij)).                    (6.11)
```

Pair uniqueness makes each fixed-color support a partial permutation.
Applying the trace lemma of Section 1 to the merged union gives

```text
tr((A_delta A_delta*)^2)
 <<L_delta^2 ||z||_2^4
 <<D ||z||_2^4.                                    (6.12)
```

### Theorem 6.1 (fixed-direction parallel-line merger)

At the active scale, the union of every maximal rational affine/Hankel
carrier line with at least three occupied points and one fixed primitive
four-carrier direction satisfies the direct FC bound (6.12), uniformly in
the number of intercepts and common levels.  The lines need not lie in one
common affine plane.

If `delta=(A*r,B*s)` with primitive `r,s`, `gcd(A,B)=1`, and `n=|AB|`,
then

```text
mu_ij=n*|r_i*s_j|/g_ij^2.                          (6.13)
```

Thus the refined coefficient before the final `O(D)` simplification is

```text
D*(sum_(i,j) g_ij/sqrt(n*|r_i*s_j|))^2.           (6.14)
```

The residue factors `g_ij` are material.  They can remove the apparent
`1/n` gain, so (6.14) is not summable over all primitive directions by a
raw divisor argument.  Nor may the fourth traces in (6.12) simply be added:
rectangles can use edges assigned to different directions.  The cases
`T=1,2` also evade (6.7); two points can occupy opposite branches of the
same parabola without pinning its tangent invariant.

This threshold is not cosmetic.  At `T=2`, product-band geometry alone
leaves the a priori `D q^o(1)` product/divisor count for chords of one fixed
projected direction: the two endpoints may sit on opposite branches while
the vertex ranges far above the band.  Fixing the complete secant restores
the earlier fixed-`(C,E)` theorem, but summing those varying secants is
precisely the remaining two-point gate.

---

## 7. Exact remaining broad gate

The theorem removes polynomial reuse inside one affine plane, and Theorem
6.1 also removes it across arbitrary parallel levels of one fixed carrier
direction.  It does not justify summing the separate direction estimates,
because Schatten-fourth norms have cross terms.  The remaining direct route
needs one of the following genuinely global statements:

1. heavy overlap between two tangent charts forces their affine planes to
   coincide, so they merge under (1.5);
2. distinct planes have enough row, column, or color orthogonality for their
   cross terms to be summable;
3. a broad incidence estimate handles rectangles whose four edges do not
   concentrate in any one `LM<<D` plane patch.

```text
partial-matching trace lemma (1.5):                 PROVED;
affine-plane merger principle:                     PROVED LOCALLY;
multilevel translation family direct FC bound:     PROVED;
shared-progression slope-product pinning:           PROVED;
window-thickened fixed-progression theorem (5.15):  PROVED;
fixed-color-pair exact slope multiplicity q^o:      PROVED;
fixed-direction parallel-line merger:               PROVED;
one-/two-point parallel-line pinning:                OPEN;
cross-direction affine/Hankel orthogonality:         OPEN;
approximate-chart cross-plane orthogonality:        OPEN;
broad generic incidence theorem:                   OPEN;
global four-cycle bound:                            OPEN.
```

The exact finite ledger and complex-weight replay are in
`src/qp_four_cycle_affine_patch.py` and
`src/test_qp_four_cycle_affine_patch.py`.
