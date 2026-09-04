# QP iterated Euclidean rebranch audit

**Date:** 2026-08-24  
**Verdict:** every primitive vector in the defect lattice gives an exact
rebranch, and the second derivative, third derivative, and local-`beta`
bounds extend uniformly to it.  Later continued-fraction vectors therefore
close genuine sectors missed by the first Euclidean remainder.  Iteration
does **not** close the whole two-inverse sector: bounded-partial-quotient
steps give a precise trajectory missed by all of the resulting derivative
polytopes and by the full current ANTEDB `beta` table.

This is an enlargement and a no-go theorem for the present route, not a
proof of the sharp four-cycle bound.

Throughout,

```text
Q asymp q,                 q=D^(33/16),
target=D^(7/8),            delta asymp D/q.              (0.1)
```

The companion transverse audit treated the original inverse direction and
the first nearest Euclidean remainder.  The point here is to remove the
word "first" completely.

---

## 1. Every primitive lattice direction is an exact rebranch

In one signed completion chart the lattice is

```text
Lambda(Q,w)={(k,a) in Z^2: a=w*k-Q*n for some n in Z},  (1.1)
```

where `gcd(Q,w)=1`.  The map

```text
(k,n) -> (k,w*k-Q*n)                                      (1.2)
```

is a bijection from `Z^2` to `Lambda` and has determinant `Q`.

Choose integers `p,m` with

```text
gcd(p,m)=1,              r=w*p-Q*m.                     (1.3)
```

Then

```text
v=(p,r) in Lambda                                           (1.4)
```

is primitive **in `Lambda`**.  This is the correct saturation condition.
It is neither necessary nor generally true that `gcd(p,r)=1`.  For example,
the first nearest-remainder vector has lattice coordinates `(L,1)` and is
primitive even when `gcd(L,Q-Lw)>1`.

The vertical cases `p=0,|m|=1` are primitive too.  They move by `(0,+/-Q)`,
so a fixed-width completion shell contains only `O(1)` points on each such
fibre; they yield no new exponent sector.  All power coordinates below refer
to the nonvertical case `p!=0`.  The horizontal case `r=0` is necessarily
`(p,m)=+/-(Q,w)`; since `|p|=Q>D`, it likewise has at most one shell point per
fibre.  The derivative and local-`beta` estimates below concern `r!=0`.

Conversely, if `d=gcd(p,m)>1`, then `(p,r)=d(p/d,r/d)` in `Lambda`; stepping
by `(p,r)` skips `d-1` interlaced lattice progressions.  Thus an
unsaturated vector must be divided before applying a one-dimensional sum.

For `(k,a) in Lambda`, define

```text
ell=m*k-p*n=(-r*k+p*a)/Q.                                (1.5)
```

This is an integer, is unchanged by `(k,a)->(k,a)+j(p,r)`, and, by Bezout,
labels all cosets of `Lambda/Zv`.  A fixed fibre is therefore exactly

```text
(k,a)=(k_ell,a_ell)+j(p,r),       j in I_ell.            (1.6)
```

There is no missing congruence class.

### 1.1 Uniform line-count bound, including saturation

The shell rectangle has `k`-width `O(D)` and `a`-width `O(q)`.  Formula
`(1.5)` shows that the number of fibre labels meeting it is

```text
B << 1+(|r|D+|p|q)/Q
  << 1+|p|+|r|D/q.                                      (1.7)
```

For each of the `O(D)` possible defects there are only `O(1)` shell lifts,
so there are `O(D)` lattice points in total.  In particular the saturated
form is

```text
B << min(D,1+|p|+|r|D/q),
sum_ell |I_ell| << D.                                   (1.8)
```

Intersecting with the second-completion shell condition adds one more
linear interval in `j`; the fixed project shell is already a union of
`O(1)` rectangles.  Hence every fibre has only `O(1)` interval pieces.
This absorbs all boundary fragments without a power loss.

On a fibre the reciprocal phase is

```text
f_ell(j)=T/[x(a_ell+r*j)],
|f_ell''(j)| asymp |r|^2/q,
|f_ell'''(j)| asymp |r|^3/q^2.                          (1.9)
```

Thus Euclidean depth never enters the analytic estimate.  Only the ambient
direction `(p,r)` and the line count `B` do.

---

## 2. The arbitrary-vector derivative theorems

Apply the same degree-`K` Selberg majorant as in the transverse audit.  The
constant term contributes

```text
D^2/q+D/K.                                               (2.1)
```

The estimates below remain valid for fibres of length zero or one because
the derivative ceilings make the endpoint term at least one.

### 2.1 Second derivative

The second-derivative theorem, summed using `(1.8)`, gives

```text
N(x,y)
 <<D^2/q+D/K+D*|r|*sqrt(K/q)
   +B*sqrt(q)/(|r|*sqrt(K)),                             (2.2)

1<=K<=min(q/D,q/|r|^2).                                 (2.3)
```

This specializes to the first-remainder bound after `|p| asymp q/w` and
`B asymp q/w`.

Write the uniform fibre-budget exponent as

```text
|p|=D^(u+o(1)),       |r|=D^(v+o(1)),
B<<D^(b+o(1)),
b=min(1,max(0,u,v+1-33/16)).                            (2.4)
```

If `K=D^k`, all terms in the resulting uniform bound `(2.2)` are at most the
target precisely when

```text
max(1/8, 2b+33/16-2v-7/4)
 <= k <=
min(17/16,33/16-2v-1/4).                               (2.5)
```

Eliminating `k` gives the exact sufficient polytope for this fibre budget,

```text
C_2:
v<=27/32,             b<=3/4,             b-v<=3/8.    (2.6)
```

These three conditions are algebraically equivalent to the nonemptiness of
`(2.5)`.  They are not claimed to be necessary if extra mask information
reduces the actual number of occupied fibres below `(2.4)`.

### 2.2 Third derivative

For the third derivative, Cauchy--Schwarz and `(1.8)` give

```text
N(x,y)
 <<D^2/q+D/K+D*|r|^(1/2)*q^(-1/3)*K^(1/6)
   +sqrt(D*B)*q^(1/3)*|r|^(-1/2)*K^(-1/6),              (2.7)

1<=K<=min(q/D,q^2/|r|^3).                              (2.8)
```

The target degree interval is

```text
max(1/8,3b+2*(33/16)-3v-9/4)
 <= k <=
min(17/16,2*(33/16)-3v-3/4).                           (2.9)
```

It is nonempty exactly on

```text
C_3:
v<=13/12,             b<=1/2,             v-b>=13/48.  (2.10)
```

The condition `v-b>=13/48` is the cost of having many short fibres; an
exceptionally tiny remainder is not automatically good.

### 2.3 Recovery of the first-remainder theorems

For nearest division `Q=Lw+r`, the vector is `(p,r)=(-L,r)` up to signs,
so if `w=D^s` then

```text
u=33/16-s.                                               (2.11)
```

For the second-derivative range, `b=u`.  Substituting `(2.11)` into `(2.6)`
gives

```text
s>=21/16,       v<=27/32,       s+v>=27/16,             (2.12)
```

For the third-derivative range one may have
`b=max(u,v-17/16)` rather than `b=u`, but the extra term changes none of the
three resulting inequalities: `v<=13/12` puts it below `1/2`, and
`v-(v-17/16)=17/16>13/48`.  Substitution into `(2.10)` therefore gives

```text
s>=25/16,       v<=13/12,       s+v>=7/3.               (2.13)
```

Thus the earlier two Euclidean sectors are exactly the first point of the
primitive-vector polytopes, with no discrepancy in a boundary exponent.

---

## 3. Arbitrary-vector local-`beta` theorem

For a primitive vector in the nontrivial range `1<=|r|<<q`, put
`M=q/|r|`.  After dividing the denominator by `|r|`, the phase has the
standard normalization

```text
T_H asymp Hq,           alpha_H=log(q/|r|)/log(Hq).      (3.1)
```

The fibre may be shorter than `[M,2M]`; the definition of `beta` is uniform
for arbitrary subintervals.  The fractional translate in `a_ell/|r|` is a
`O(1/M)` perturbation after rescaling and is uniform in the non-asymptotic
phase-function formulation.  Partitioning the fixed shell takes only
`O(1)` intervals.

Consequently a dyadic frequency block `h asymp H` contributes

```text
B*(H/K)*(Hq)^(beta(alpha_H)+o(1)).                       (3.2)
```

This is the local-`beta` theorem for every primitive vector in that range.
If `|r|` exceeds `q` by a fixed power, each fibre has only `O(1)` points and
the `beta` normalization is neither valid nor needed.  With `K=D^(1/8)`, the
exact sufficient condition in the nontrivial range is

```text
max_(1<=H<=D^(1/8))
 [ b+log_D(H)-1/8
   +(33/16+log_D(H))*beta(alpha_H) ] <=7/8.              (3.3)
```

No continued-fraction assumption occurs in `(3.2)` or `(3.3)`.

### 3.1 Explicit Bourgain two-line sector

For

```text
33/32<=v<=221/192,                                      (3.4)
```

all the `alpha_H` lie in `[5/12,1/2]`.  Bourgain's adjacent bounds

```text
beta(alpha)<=13/84+alpha/2,       3/7<=alpha<=1/2,
beta(alpha)<=1/12+2alpha/3,       5/12<=alpha<=3/7       (3.5)
```

have positive intercepts and agree at `3/7`, so the top block is worst.
Writing `(3.3)` in `(b,v)` gives

```text
C_beta:

33/32<=v<=9/8,        b<=v/2-665/1344;
9/8<=v<=221/192,      b<=2v/3-131/192.                 (3.6)
```

The fibre budgets at the lower endpoint, crossing, and upper endpoint are

```text
1/48,                 13/192,                 49/576.   (3.7)
```

This is a real extra sector for a later convergent whose denominator is
small.  For `v>73/64`, however, the drifting-line term forces
`b>=v+1-33/16`; the prior full-table scan for the original vector then
applies unchanged.  Merely choosing a different primitive vector with the
same large remainder cannot lower that unavoidable part of `B`.

### 3.2 Full current ANTEDB table

For `v>=33/32`, every frequency in `(3.3)` has `alpha_H<=1/2`.  If a table
piece is

```text
beta(alpha)<=a+c*alpha,                                  (3.8)
```

then on that piece the block exponent is

```text
b+eta-1/8+(33/16+eta)*a+c*(33/16-v),
eta=log_D(H),                                             (3.9)
```

and increases with `eta` with slope `1+a>0`.  Thus the complete current
table gives a finite polyhedral complex in `(b,v)`, cut out by affine
halfspaces and checks on both sides of every table breakpoint.  All twenty exact rational
pieces from the current [ANTEDB beta table](https://teorth.github.io/expdb/blueprint/beta-chapter.html)
are reproduced in the ledger; no decimal scan is being used.

---

## 4. What continued fractions add, and what they cannot force

Let `m_j/p_j` and `m_(j+1)/p_(j+1)` be consecutive reduced convergents to
`w/Q`, and put

```text
r_j=w*p_j-Q*m_j.                                        (4.1)
```

Their coordinate determinant is one, so

```text
|p_j*r_(j+1)-p_(j+1)*r_j|=Q.                           (4.2)
```

For the alternating convergent errors this is

```text
p_j*|r_(j+1)|+p_(j+1)*|r_j|=Q.                         (4.3)
```

Equations `(4.2)--(4.3)` are the exact tradeoff: later denominators grow
while remainders shrink, but a large partial quotient can jump over an
entire power window.  Continued fractions do not provide a bounded mesh in
`(u,v)`.

### 4.1 A later vector can close when the first remainder does not

Here is an asymptotically exact construction.  Let `X->infinity`, choose

```text
p asymp X^(3/5),          r asymp X^(4/5),
Q asymp X^(33/16),        n/p ->2/5,                    (4.4)
```

with `gcd(p,n)=gcd(Q,r)=1` and choose `Q` in the residue class

```text
Q*n == -r (mod p).                                      (4.5)
```

There are arbitrarily large such choices: take `p,r` prime in the indicated
ranges, take `n=floor(2p/5)` (adjusting by `O(1)` if needed), and select one
of the many integers in the progression `(4.5)` while avoiding the single
bad residue modulo `r`.  Define

```text
w=(Q*n+r)/p.                                             (4.6)
```

Then `gcd(Q,w)=1`, `w/Q->2/5`, and

```text
w*p-Q*n=r.                                               (4.7)
```

Both the original remainder `w` and the first nearest remainder of `Q`
modulo `w` are `asymp Q`, so neither lies in `(2.6)`, `(2.10)`, or `(3.6)`.
On the other hand

```text
|w/Q-n/p|=r/(pQ)<1/(2p^2)                               (4.8)
```

because `pr=o(Q)`.  Legendre's criterion makes `n/p` a genuine later
continued-fraction convergent.  Since `D=Q^(16/33)=X^(1+o(1))`, its power
coordinates are

```text
(u,v,b)=(3/5,4/5,3/5),                                  (4.9)
```

which lie strictly inside `C_2`.  Thus iteration yields genuinely new
closed pairs, not just a reformulation of the first remainder.

### 4.2 A precise uncovered trajectory

Suppose `w/Q` has uniformly bounded partial quotients.  The standard
best-approximation inequalities give, uniformly for `1<=p<Q`,

```text
|w*p-Q*m| >> Q/p.                                       (4.10)
```

Signs are immaterial here.  Directions with `|p|>=Q` move farther than the
entire defect interval, so every nonempty fibre is a singleton and the fibre
count has saturated exponent `1`; they cannot enter any of the recorded
target regions.  Thus `(4.10)` covers every potentially useful nonvertical
direction.

Put `h=33/16-v`, the natural fibre-length exponent.  Equation `(4.10)` says
`h<=u` for every primitive vector; for convergents this is sharp up to
constants.  The equality curve, which is the lower envelope of all primitive
vectors, is therefore

```text
U_BA:
u+v=33/16,
b>=min(1,max(u,1-u)).                                   (4.11)
```

The fibre exponent in `(4.11)` is not merely an artifact of the upper bound
`(1.8)`.  For a bounded-partial-quotient rotation, the standard
Denjoy--Koksma discrepancy estimate shows that a full fixed-width shell
rectangle contains `asymp D` lattice points (the discrepancy is only
logarithmic), while one such nonempty fibre contains at most

```text
1+min(D/|p|,q/|r|)
 =D^(max(0,min(1-u,h))+o(1))
 <=D^(max(0,min(1-h,h))+o(1)).                         (4.11a)
```

Hence the rectangle meets at least
`D^(min(1,max(h,1-h))+o(1))` fibres.  Equality in this lower envelope is most
favourable when `u=h`, namely on `(4.11)`; a nonconvergent vector with `u>h`
can only shorten its fibres and increase their number.  Any smaller effective
fibre count would have to use the reciprocal mask itself, which is additional
information not present in a bare Euclidean rebranch.

This lower envelope, and therefore every primitive vector above it, is
disjoint from every derivative polytope:

* `C_2` has `v<=27/32`, hence `h>=39/32`; `(4.11a)` forces
  fibre exponent `1>3/4`;
* `C_3` has `v<=13/12`, hence `h>=47/48`; `(4.11a)` forces
  fibre exponent at least `47/48>1/2`.

It also misses the full current local-`beta` table.  For fixed natural-length
exponent `h`, the `beta` cost depends on `h` while `(4.11a)` shows that the
fibre cost is minimized at `u=h`.  Thus nonconvergents cannot improve on the
equality curve.  On that curve, at the top Selberg frequency put

```text
C=33/16+1/8=35/16,        alpha=u/C.                    (4.12)
```

On `u<=1/2`, the top-block cost on every affine beta piece decreases with
`u` apart from the finitely checked table boundaries; on `u>=1/2` it
increases.  Checking the exact rational boundaries in the ledger, together
with the trivial bound `beta(alpha)<=alpha`, shows that the global minimum of
the tabulated top-block ledger occurs at

```text
u=1/2,       v=25/16,       b=1/2,       alpha=8/35.    (4.13)
```

The active current table line there is

```text
beta(alpha)<=13/414+(346/414)alpha,                     (4.14)
```

and the resulting top-block power is

```text
b+C*beta_tab(8/35)
 =6535/6624
 =7/8+739/6624.                                         (4.15)
```

As an upper-bound ledger, `(4.15)` misses the target by
`D^(739/6624)`.  It does not prove that the actual exponential sums are
large; it proves that the full currently tabulated fibrewise `beta` input
does not certify this trajectory.  The rational table scan covers
`u<=35/32`, equivalently `alpha<=1/2`; beyond that point `b=1` and the
universal lower constraint `beta(alpha)>=alpha/2` already puts the formal
top-block scale above the target, so no omitted reflected-table interval
can improve the minimum in `(4.13)`.

### 4.3 The obstruction occurs simultaneously in both endpoint charts

Take consecutive Fibonacci endpoints

```text
x=F_(j-1),                  y=F_j.                       (4.16)
```

Cassini's identity gives the least inverse steps

```text
w_y=F_(j-2),                w_x=F_(j-3).                 (4.17)
```

Both step/host ratios tend to `phi^(-2)` and have bounded partial
quotients.  Also `y-x=F_(j-2) asymp q`, so the close-gap theorem does not
apply, while both original steps are `asymp q` and far beyond
`D^(73/64)`.  Hence both Euclidean descents follow the uncovered trajectory
`(4.11)`.

The Fibonacci endpoints are a coprime defect-lattice fixture, not a claim
about an all-prime subfamily.  If primality of the original endpoints is
retained, ruling out this geometry would require a new primality-sensitive
input.  Euclidean iteration itself uses only coprimality and therefore
cannot supply such an exclusion.

---

## 5. Consequence for the sharp four-cycle attack

An explicit closed subunion furnished by this route is

```text
C_2 union C_3 union C_beta,
```

and it has a finite refinement obtained by substituting the applicable current
ANTEDB pieces into `(3.3)`.  One may test these sufficient regions at **every** primitive
continued-fraction vector in either endpoint chart.  This strictly improves
the first-remainder audit because of `(4.4)--(4.9)`.

There is no theorem forcing a vector into any of these recorded regions for
every coprime `(Q,w)`: `(4.10)--(4.17)` give a precise two-chart obstruction.
Therefore
the remaining proof cannot be completed by repeatedly applying the same
one-dimensional derivative or local-`beta` estimate after Euclidean
coordinate changes.  It must add cancellation between fibres/frequencies,
use a mask-sensitive packet theorem, or exploit arithmetic absent from the
bare defect lattice.

Machine-checkable exact identities and all rational exponent ledgers are in
`src/qp_iterated_euclidean_rebranch_ledger.py`; focused tests are in
`src/test_qp_iterated_euclidean_rebranch_ledger.py`.

Status:

```text
primitive/saturation criterion:                         PROVED;
line count and boundary-piece control:                   PROVED;
arbitrary-vector second/third bounds:                    PROVED;
exact sufficient derivative-budget polytopes C_2,C_3:  PROVED;
arbitrary-vector local-beta formula:                     PROVED;
explicit Bourgain sector C_beta:                         PROVED;
later-convergent strict enlargement:                     PROVED;
bounded-partial-quotient two-chart obstruction:          PROVED;
global transverse D^(7/8+o(1)) bound:                   OPEN;
sharp four-cycle theorem:                                OPEN.
```
