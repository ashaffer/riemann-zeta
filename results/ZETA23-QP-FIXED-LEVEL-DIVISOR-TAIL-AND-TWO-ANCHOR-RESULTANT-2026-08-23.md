# QP high-completion tail: fixed-level divisor theorem and the two-anchor resultant

**Date:** 2026-08-23  
**Verdict:** aggressive elimination produces a sharp high-tail theorem on
every fixed integral bilinear level.  If `L` is fixed, then

```text
#{gamma': m(gamma,gamma')~K and L(gamma,gamma')=L}
 <<(D/K)q^o(1).                                      (0.1)
```

The proof retains the actual prime-power carrier: for one anchor completion
the partner carrier is a large divisor of the explicit integer `b*e-L`.

For two completions there is also an exact resultant

```text
X_ij*X_ji=L_i*L_j-k*delta_ij*t_ij.                  (0.2)
```

At the asymptotic QP scale the two levels pin, so the right side becomes
`L^2-k*delta*t`.  This is nonzero and is divisor-controlled after `t` is
fixed.  It does not prove the uniform tail: the integral level varies with
the partner through a sub-square-root reciprocal rounding map, and the
carrier determinant `t` has `O(D)` possible values.

Actual-prime finite scans exhibit nonzero carrier minors as small as `58`.
Zero minors are impossible in a genuine rectangle by multiplicative
Sidonicity, but primality does not force a useful positive lower bound.
Moreover, a two-anchor/rectangle-energy proof cannot see a linear
hypergraph of high partners whose pairwise intersections have size at most
one.  The remaining theorem must aggregate the varying levels or act on
individual high partners, not merely on their `2 x 2` overlaps.

In fact the varying levels do not collide on the generic all-distinct
sector: two distinct primitive partner colors have color-only centers, and
hence asymptotic integral levels, separated by `>>q`.  Thus every generic
fixed-level partner fibre is a singleton.  At one fixed anchor completion
the corresponding shifted large-prime divisors are also pairwise disjoint.
These facts make positive fixed-level summation powerless; any successful
aggregation must occur before absolute values.

---

## 1. Setup

Fix an actual anchor color pair

```text
gamma=(c,d)
```

and a partner

```text
gamma'=(c',d'),              k=c*d'-c'*d!=0.
```

A common completion consists of a row pair `(a_i,A_i)`, anchor carrier
`b_i`, and partner carrier `B_i`.  Put

```text
e_i=a_i*c-A_i*d,
f_i=a_i*c'-A_i*d',
ell_i=c'*B_i-c*b_i,
L_i=b_i*e_i-B_i*f_i.                               (1.1)
```

Every defect in (1.1) is `O(D)`, while every row, color, and carrier is
`asymp q`.  Direct elimination gives

```text
c*L_i=A_i*B_i*k-e_i*ell_i.                         (1.2)
```

Indeed `c*f_i=e_i*c'-A_i*k`, so

```text
c(b_i e_i-B_i f_i)
 =e_i(c b_i-c'B_i)+A_iB_i k.
```

There are three symmetric companions, but (1.2) is enough below.

## 2. Integral-level pinning

The active bottom-right product window gives

```text
A_i*B_i=q^3/(8*d')+O(D).                           (2.1)
```

Consequently, for two completions of the same color matrix,

```text
c*(L_i-L_j)
 =k*(A_iB_i-A_jB_j)-(e_i ell_i-e_j ell_j)
 =O(D^2).                                         (2.2)
```

Since

```text
D^2/q=q^(-1/33+o(1))=o(1),                        (2.3)
```

and `L_i-L_j` is integral, (2.2) proves that, for all sufficiently large
`q`, one exact integer `L=L(gamma,gamma')` serves every completion.

The determinant identity for the four product residuals gives the
color-only description

```text
L=nearest(q^3*k/(8*c*d'))
  =nearest(q^3*k/(8*c'*d)).                        (2.4)
```

The two displayed centers differ by `O(k^2/q)=O(D^2/q)`.  Thus they pin
the same integer.  Formula (1.2) also shows

```text
|L|asymp q*|k|.                                    (2.5)
```

At moderate diagnostic values the fixed hard-cutoff constants can make
`D^2/q` much larger than one, so finite fibres need not yet have a constant
`L_i`.  This does not contradict the asymptotic theorem.

## 3. Sharp tail on one fixed level

Fix an anchor completion `(a,A,b)` with defect `e`, and fix an integer
`L`.  Every partner completion on this level satisfies

```text
B*f=b*e-L.                                         (3.1)
```

If the right side is nonzero, the actual shell carrier `B` is a divisor of
one explicit `O(qD)` integer.  Hence the divisor bound leaves only
`q^o(1)` possible `B`, and then `f` is fixed.  For fixed `f`, the equation

```text
a*c'-A*d'=f                                        (3.2)
```

has at most one partner shell pair.  Indeed two solutions differ by an
integral multiple of `(A,a)`, and a nonzero such multiple cannot fit in the
project shell, whose diameter is smaller than every shell coordinate.

If the right side of (3.1) vanishes, then `f=0`.  Equation (3.2) is then
the proportional/swap case and again has `O(1)` shell lifts.  Therefore

```text
one anchor completion sees q^o(1) partners at fixed L. (3.3)
```

The anchor neighbourhood has `O(Dq^o(1))` members because its defect `e`
is injective and `|e|<<Dq^o(1)`.  Double-counting incidences with partners
having `K<=m<2K` proves (0.1).

This is exactly the desired `D/K` scale, without dropping any carrier or
prime-power mask.  Its limitation is solely that different partners may
have different levels (2.4).

## 4. Exact two-anchor resultant

Take two completions `i,j` of one color matrix and define

```text
delta_ij=a_i*A_j-A_i*a_j,
t_ij    =b_i*B_j-B_i*b_j,
X_ij    =b_i*e_j-B_i*f_j,
X_ji    =b_j*e_i-B_j*f_i.                          (4.1)
```

Let

```text
U=(e_i f_i; e_j f_j),
V=(b_i B_i; b_j B_j),
J=diag(1,-1).
```

Then `V J U^T` has diagonal entries `L_i,L_j` and off-diagonal entries
`X_ij,X_ji`.  Moreover

```text
det U=-k*delta_ij,             det V=t_ij.
```

Taking determinants proves exactly

```text
L_i*L_j-X_ij*X_ji=k*delta_ij*t_ij,                (4.2)
```

which is (0.2).  In the asymptotic pinned range,

```text
X_ij*X_ji=L^2-k*delta_ij*t_ij.                    (4.3)
```

The right side is nonzero: `L^2>>q^2k^2`, whereas
`|k delta t|<<D^3=o(q^2)`.  Thus, after `(k,L,delta,t)` is fixed, the
factor pair `(X_ij,X_ji)` has only `q^o(1)` possibilities.

This is a genuine divisor resultant, but not the missing aggregation.
The carrier determinant `t` ranges through `O(D)` nonzero levels, and
fixing `k` already fixes the partner.  Summing the divisor estimate
positively over `t` returns the original loss.

## 5. Why `2 x 2` energy cannot by itself prove the tail

For a fixed anchor, let `S_gamma'` be the set of its completions shared
with a partner.  A carrier `2 x 2` minor exists only when two distinct
partners satisfy

```text
|S_gamma' intersect S_gamma''|>=2.                 (5.1)
```

Purely combinatorially, `P` subsets of size `K` in an `M`-element universe
may have pairwise intersections at most one.  A projective plane gives
`M` lines on `M` points, each of size `asymp sqrt(M)`, with every pair
meeting once.  Truncating every line gives the same property for every
`K<=sqrt(M)`.  Thus at

```text
M~D,             K=D^(5/16),             P~D,     (5.2)
```

there need be no partner-partner rectangle at all, although the desired
tail would require `P<<D/K`.  This is not an actual-prime construction; it
proves that even a perfect theorem for the multiplicative energy of
carrier minors cannot close the scattered/linear-hypergraph case.

## 6. Actual-prime minor audit

For a genuine anchored rectangle with rows `i,j` and partners `r,s`, put

```text
h=B_(i,r)*B_(j,s)-B_(i,s)*B_(j,r).                 (6.1)
```

The four product windows imply `|h|<<D`.  Also `h!=0`.  If `h=0`,
multiplicative Sidonicity of the narrow prime-power shell forces equality
of the two unordered carrier pairs.  One pairing repeats a carrier along a
fixed row and forces the partners equal; the other repeats it along a fixed
partner and forces the rows equal.

Nonzero small minors nevertheless occur with every label actual and all
sixteen row/color/carrier labels distinct.  One exact fixture is

```text
q=25013,
anchor gamma=(13469,13687),
partners      (12457,12659), (14449,14683),
rows          (11171,10993), (12163,11969),
anchor B      13001,11941,
partner 1 B   14057,12911,
partner 2 B   12119,11131.
```

Its carrier minor is

```text
14057*11131-12119*12911=58.                        (6.2)
```

All twelve product residuals lie in the finite hard core.  Broader scans
gave no zero minor and, within each fixed anchor, no repeated absolute
minor, but this is evidence rather than an asymptotic theorem.

The same scans verified (1.2) and (4.2) with exact integer arithmetic on
thousands of actual partner fibres.

## 7. Exact separation of the varying levels

For a partner `r=(c_r,d_r)`, write

```text
k_r=c*d_r-c_r*d,
X_r=q^3*k_r/(8*c*d_r).                              (7.1)
```

For two partners `r,s`, direct subtraction gives the exact rational
identity

```text
X_r-X_s
 =q^3*d*(c_s*d_r-c_r*d_s)/(8*c*d_r*d_s).          (7.2)
```

On the generic all-distinct sector, actual partner pairs are primitive and
cannot have the same slope, so the last parenthesis in (7.2) is a nonzero
integer.  All four coordinates lie in a fixed shell `asymp q`;
consequently

```text
|X_r-X_s|>>q.                                      (7.3)
```

The pinning theorem says `L_r=nearest(X_r)` for sufficiently large `q`.
It follows that distinct partners have distinct, `>>q`-separated integral
levels.  In particular, the fixed-`L` theorem of Section 3 has at most one
partner to count on every level.  Its `D/K` conclusion is true but cannot
be positively summed to prove the uniform tail.

There is a companion divisor-disjointness statement.  Fix one anchor
completion `(a,A,b,e)`.  For a partner `r`, put

```text
N_r=b*e-L_r=B_r*f_r.                               (7.4)
```

If the carrier of a distinct partner `s` divided `N_r`, then
`gcd(B_r,B_s)=1` would force `B_s|f_r`.  Since `|f_r|<<D<B_s`, this forces
`f_r=0`, the proportional/swapped repeated-label sector.  On the generic
all-distinct sector, therefore, no partner carrier divides another
partner's shifted integer.  The varying levels have disjoint large-divisor
supports, not a common divisor packet.

Neither (7.3) nor this disjointness is a Bessel inequality.  A `q`-spaced
set in an interval of length `qD` can still be a dilated arithmetic
progression with maximal additive energy.  The exact separation removes
level collisions but gives no cancellation for the positive high-tail
form.

There is also an exact row-wise generalized-progression chart.  Define the
second carrier defect

```text
ell_2=d'*B-d*b,             |ell_2|<<D.
```

Expanding `L=b*e-B*f` without approximation gives

```text
L=A*ell_2-a*ell.                                    (7.5)
```

For a fixed row `(a,A)`, the map `(ell,ell_2)->L` is injective in the
`D`-box: equality of two values would give
`a*Delta ell=A*Delta ell_2`; coprimality of the actual row coordinates and
`2D<min(a,A)` force both differences to vanish.  Thus every fixed row sees
the varying levels inside an exact injective rank-two GAP, and the actual
partner subset is `q`-separated inside that GAP.  Additive large-sieve
orthogonality for these levels returns the square sum of their
coefficients; at the positive zero frequency it still pays the square root
of the number of levels.  Equation (7.5) is therefore a useful exact
coordinate system, not by itself the missing high-tail estimate.

## 8. Remaining gate

The fixed-level theorem proves that the obstruction is not internal to an
`L` fibre.  The unresolved map is

```text
k -> d'(k) -> L(k)=nearest(q^3*k/(8*c*d'(k))),     (8.1)
```

where `d'(k)` is the actual modular shell lift.  The rounding window in
(2.4) has width

```text
D^2/q=D^(-1/16+o(1)).                              (8.2)
```

A random-volume count over `D` possible `k` therefore leaves
`D^3/q=D^(15/16)` levels, only a `D^(1/16)` saving.  At the critical
`K=D^(5/16)`, the high-tail target is `D/K=D^(11/16)`, a further
`D^(1/4)` gain.  That gain must be a square-function or mask-sensitive
distribution theorem across the separated reciprocal levels in (8.1), or a
first-moment theorem which also handles the rectangle-free scattered
family.

```text
fixed-fibre integral L pinning:                    PROVED;
fixed-L high tail D/K:                             PROVED;
generic distinct-partner levels are q-separated:   PROVED;
off-diagonal shifted shell divisors:                ABSENT GENERICALLY;
fixed-row level GAP L=A*ell_2-a*ell:                PROVED;
two-anchor resultant XY=L^2-k*delta*t:             PROVED;
zero actual carrier minor in genuine rectangle:    IMPOSSIBLE;
nonzero actual carrier minor has power lower bound: FALSE (minor 58);
minor-energy theorem handles rectangle-free family: NO;
varying-L square function / first moment:           OPEN;
uniform high-completion tail:                       OPEN.
```

Exact replay of (1.2), (4.2), and the minor-`58` fixture is in
`src/qp_fixed_level_pair_resultant.py`:

```bash
PYTHONPATH=src pytest -q src/test_qp_fixed_level_pair_resultant.py
```
