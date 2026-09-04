# QP parabolic curvature: the anchored first moment removes the endpoint

**Date:** 2026-08-23  
**Verdict:** the previously surviving endpoint

```text
(e,t,g,r,s)=(1,0,0,3/16,3/16)
```

does not saturate the parabolic curvature estimate.  Summing either one
of the two original pair-matching Cauchy estimates directly, instead of
geometrically averaging them, gives relation mass

```text
min(R*T/G, S*E/G) q^o(1).                          (0.1)
```

At the endpoint this is only `D^(3/16+o(1))`.  The full occupied-line
curvature multiplier is `D^(15/32+o(1))`, so the weighted endpoint is

```text
D^(21/32+o(1)) ||z||_2^4,                          (0.2)
```

far below four-cycle strength.  The apparent `37/32` saturation of the
four-energy geometric-mean form is a relaxed principal mode which cannot
come from the common color-chart mass at this imbalanced endpoint.

This result removes this endpoint, not every feasible parabolic block.

There is a second conclusion.  After (0.1), the curvature LP still has a
symmetric equality point

```text
(e,t,g,r,s)=(1/2,1/2,0,7/16,7/16).                (0.3)
```

At this point the positive geometric-mean estimate still genuinely
balances.  Nevertheless its curvature contribution is at four-cycle
strength uniformly on every factor-two coefficient bin.  The two extra
facts are that a line contributing a second point must have `n*H<<D`, and
that the common affine color parameter gives a `1/M` chart bound on a flat
bin of support `M`.  Sections 4--5 give the proof.

## 1. The two estimates should be minimized

Normalize `||z||_2=1`.  On a dyadic block write

```text
|eta|~E, |theta|~T, gcd(eta,theta)~G,
||r||~R, ||s||~S.
```

For fixed `(r,s,eta,theta)`, the exact color chart has one common affine
parameter `X` and total weight `W_gamma`.  Its top--bottom pair projections
are matchings, so the already proved estimate is

```text
W_gamma <=sqrt(P_(s,r2*eta) Q_(s,r1*eta)).          (1.1)
```

For fixed `(s,eta)`, sum first in `r1,r2`.  Enlarging the primitive box to
the full product box and applying Cauchy twice gives

```text
sum_(r1,r2) sqrt(P_(s,r2*eta) Q_(s,r1*eta))
 <=R sqrt(
      (sum_r2 P_(s,r2*eta))
      (sum_r1 Q_(s,r1*eta))).                      (1.2)
```

Another Cauchy inequality over `(s,eta)`, followed by the proved bounded
gap-token overlap, bounds (1.2) by `R q^o(1)`.  For fixed `eta`, the number
of `theta~T` with `gcd(eta,theta)~G` is
`(T/G)q^o(1)`: the possible gcds are divisors of `eta`, and after one is
fixed there are `O(T/G)` multiples.  Therefore

```text
sum_gamma W_gamma <<R*T/G q^o(1).                  (1.3)
```

Using instead the left--right matching estimate

```text
W_gamma <=sqrt(R_(r,-s2*theta) S_(r,-s1*theta))
```

and reversing the roles gives

```text
sum_gamma W_gamma <<S*E/G q^o(1).                  (1.4)
```

Taking the smaller of (1.3) and (1.4) proves (0.1).  The earlier
`sqrt(E*T*R*S)/G` estimate is their geometric mean; that is useful near a
balanced factorization, but it is unnecessarily large when one
determinant factor is much longer than the other.

The common chart parameter `X` causes no additional issue: (1.1) is the
matching Cauchy estimate for that exact same `X`-sum.  Thus (0.1) already
retains a single coefficient vector `z` on all four affine color maps.

## 2. Endpoint arithmetic

At the endpoint,

```text
E=D, T=G=1, R=S=D^(3/16), H=R*S=D^(3/8),
K=D^(5/16).
```

Equation (0.1) gives relation mass `R=D^(3/16)`.  The occupied-line theorem
is pointwise in the color matrix:

```text
m_par(C) <<K+sqrt(D*K/H) q^o(1).
```

Its two exponents are `5/16` and `15/32`.  Multiplication by the relation
mass gives respectively

```text
3/16+5/16=1/2,
3/16+15/32=21/32.                                 (2.1)
```

This proves (0.2), without an `A x B` merger and without the conditional
refined-token estimate.

## 3. Why the four-linear constant box was spurious

On the endpoint, the refined four-energy form has the exact projections

```text
P: (s1,s2,r2,eta,B),   Q: (s1,s2,r1,eta,B),
R: (r1,r2,s2,A),       S: (r1,r2,s1,A).
```

Putting constant arrays on every slice, with

```text
P=Q=(E*R*S^2)^(-1),     Renergy=Senergy=(R^2*S)^(-1),
```

does saturate the *relaxed* geometric-mean expression and exposes its
positive `A x B` constant mode.  For `R=S`, however,

```text
sqrt(P*Q)=P,          sqrt(Renergy*Senergy)=E*P.
```

An actual common chart weight obeys both matching inequalities and is at
most the first quantity.  Replacing that minimum by their geometric mean
inserts an artificial factor `sqrt(E)`.  Consequently these constant
marginals cannot be realized by one `z` with chart mass equal to the
relaxed four-linear value.  They are a counterexample to a marginal-only
Brascamp--Lieb improvement, not a counterexample to the weighted color
sum.

```text
direct top--bottom first moment R*T/G:              PROVED;
direct left--right first moment S*E/G:              PROVED;
minimum relation mass (0.1):                        PROVED;
former endpoint contribution D^(21/32+o(1)):        PROVED;
four-energy constant-box actual-z saturation:       FALSE;
all-block sharp parabolic theorem:                   NOT CLAIMED.
```

## 4. A repeated line has `n*H<<D`

The occupied-line proof gives, for a line of primitive multiplier `n`, an
allowed parameter interval of length

```text
O(sqrt(D/(n*H))).                                  (4.1)
```

The singleton term has already paid for the first occupied integral
parameter on every line.  If a line contributes anything to the curvature
remainder, it contains two distinct integers.  Its interval length is
therefore at least one, and (4.1) forces

```text
n <<D/H.                                           (4.2)
```

There are only `q^o(1)` maximal lines with any fixed `n`.  Consequently

```text
m_curv(C)
 <<sqrt(D/H) sum_(n<<D/H) n^(-1/2) q^o(1)
 <<D/H q^o(1).                                     (4.3)
```

Together with the earlier ordering by the number `K` of occupied lines,
the general pointwise refinement is

```text
m_curv(C)
 <<min(sqrt(D*K/H), D/H) q^o(1).                   (4.4)
```

At (0.3), `H=D^(7/8)` and `K=D^(5/16)`.  The old multiplier in (4.4) is
`D^(7/32)`; the repeated-line multiplier is only `D^(1/8)`.

## 5. Uniform flat-bin closure at the symmetric equality point

Let a factor-two coefficient bin have support `M=D^mu` and normalize its
`ell^2` mass to one.  For fixed `(r,s,eta,theta)`, put `X=x`.  The exact
color equations are

```text
y=(s1*X-r2*eta)/s2,
zeta=(r1*X+s2*theta)/r2,
w=(r1*y+s1*theta)/r2.                             (5.1)
```

All components of `r,s` are nonzero in the active chart, so all four maps
from the integral `X` progression to `x,y,zeta,w` are injective.  Holder's
inequality on this single common progression gives

```text
W_gamma
 <=prod_(c in {x,y,zeta,w})
      (sum_X |z_(c(X))|^4)^(1/4)
 <=||z||_4^4
 <<1/M.                                            (5.2)
```

At (0.3), the number of relation charts is at most

```text
R^2*S^2*E*T=D^(11/4+o(1)).                         (5.3)
```

Equations (4.3), (5.2), and (5.3) therefore prove FC whenever

```text
11/4-mu+1/8 <=1,
mu>=15/8.                                          (5.4)
```

For the complementary range use the flat determinant theorem.  Its
principal mass has exponent `mu-17/16`; after (4.3) this is

```text
mu-17/16+1/8=mu-15/16 <=1
```

through `mu<=31/16`.  The two support ranges overlap by `1/16`.

The nonprincipal determinant mass causes no gap.  The iterated `B*H^2`
product large sieve and the fourth-moment estimate give respectively

```text
65/64-mu/4,       1/2+mu/4.
```

Their minimum is uniformly at most `97/128`.  Adding the repeated-line
exponent `1/8` gives only `113/128<1`.  Hence the symmetric curvature face
(0.3) contributes

```text
O(D^(1+o(1))) ||z||_2^4                            (5.5)
```

on every flat bin.

```text
repeated-line cutoff n*H<<D:                        PROVED;
pointwise curvature min(sqrt(DK/H),D/H):            PROVED;
one-chart flat mass 1/M:                            PROVED;
symmetric-face chart range mu>=15/8:                PROVED;
symmetric-face determinant range mu<=31/16:         PROVED;
symmetric-face curvature D^(1+o(1)):                PROVED;
uniform closure of every other curvature face:      NOT CLAIMED.
```

## 6. Floor/cutoff reoptimization and the final face

There is a second elementary refinement of the line kernel.  Since

```text
|eta*alpha|~D^(1+s),       |theta*beta|~D^(1+r),
```

and the transverse gcd cannot exceed the smaller integer, every primitive
line multiplier satisfies

```text
n=|A*B| >=D^|r-s|.                                 (6.1)
```

If `J<=D^kappa` lines are occupied, the two positive estimates are

```text
sum_lines n^(-1/2)
 <<D^(kappa/2) q^o(1),
sum_lines n^(-1/2)
 <<D^(kappa-|r-s|/2) q^o(1).                       (6.2)
```

The first orders the integer multipliers and uses divisor-many lines per
multiplier; the second uses (6.1) on every line.  Combine (6.2), the
repeated-line cutoff (4.3), and the anchored relation mass (0.1).  The
remaining equality face of this positive LP is

```text
(e,t,r,s,g)=(21/32,11/32,23/64,3/64,0),
kappa=5/16.                                        (6.3)
```

Its exact ledger is

```text
relation mass min(r+t,s+e)        =45/64,
direction height r+s              =13/32,
multiplier floor |r-s|            =5/16,
inverse-sqrt line sum             =5/32,
sqrt(D/H) prefactor               =19/64,
pointwise curvature               =29/64,
weighted curvature                =74/64=37/32.    (6.4)
```

Thus the refinements relocate, but do not lower, the final uniform
`37/32` positive bound.

At (6.3) the extremal line geometry is one-sided:

```text
A~1,              B~K=D^(5/16).
```

The raw carrier steps nevertheless balance, because

```text
||A*r||~D^(23/64),       ||B*s||~D^(23/64).        (6.5)
```

Each such line has an allowed longitudinal parameter interval of length
`D^(9/64)`.

## 7. Common `X` and one coefficient vector do not remove the face

The four token-family cardinalities at (6.3) are exactly balanced:

```text
e+r+2s=2r+s+t=71/64.                               (7.1)
```

The total chart count has exponent

```text
2r+2s+e+t=116/64,
```

so every token has the equality-scale lift degree `D^(45/64)`.

There is an explicit finite common-parameter model saturating both
one-sided matching inequalities.  Work in a cyclic group `G` of order
`N`.  Choose `L<=N`, and for every `p in G` and `a` in an `L`-set put

```text
r=p+2a+1,       q=p+a,       s=r+a,
(x,y,zeta,w)=(X, X+p, X+r, X+p+r+a).               (7.2)
```

As `X` varies, all four coordinate maps are permutations.  The four pair
differences are exactly `p,q,r,s`, and every token family is `L`-regular.
With the single flat vector `z_x=N^(-1/2)`, every token matching has energy
`1/N` and every chart has mass `1/N`.  Hence both matching Cauchy bounds
are equalities and the total chart mass is

```text
(N*L)/N=L.                                         (7.3)
```

Taking the formal scales `N=D^(71/64)` and `L=D^(45/64)` reproduces the
relation exponent in (6.4).  This is an abstract permutation model, not an
integer prime-power construction, but it proves that common-`X`
Brascamp--Lieb/Finner/Schatten rank and single-`z` consistency alone cannot
save a power on (6.3).

## 8. Exact `A=1`, variable-`B` star and the prime mask

The whole positive slope star is also algebraically compatible with the
transverse and level identities.  Let `c~S` and set

```text
alpha=theta*c,             beta=eta*c*B.            (8.1)
```

Then exactly

```text
g0=gcd(eta*alpha,theta*beta)=|eta*theta*c|,
A=1,                       B=B.                     (8.2)
```

Moreover the common-level equation divides by its signed transverse scale
to give

```text
B*u+v+gamma*c*B=C,
B*(u+gamma*c)+v=C.                                 (8.3)
```

Thus it has an integral solution for every `B~K`; there is no hidden rank
collapse in the exact affine level.  Equations (7.2)--(8.3) show that the
color principal mode and the full positive `B` star are mutually
compatible at the algebraic/projection level.

What they do not realize is the actual arithmetic mask.  Along one star
line the four carrier coordinates are affine forms

```text
a_i+t*r_i,             b_j+t*B*s_j,
|t|<<D^(9/64),                                      (8.4)
```

with all raw steps of size `D^(23/64)`.  The project requires these forms
to land simultaneously on the prime-power shell and to obey the four
product windows, for a weighted family of `B~D^(5/16)`.  Controlling that
positive family is the final mask-sensitive affine-prime-progression gate.

```text
line multiplier floor n>=D^|r-s|:                  PROVED;
final positive LP face (6.3)--(6.4):                PROVED;
regular common-X/single-z saturation model:         EXPLICIT ABSTRACT MODEL;
exact A=1, B-variable level star:                   PROVED;
actual-prime realization of the saturator:          NOT CLAIMED;
power saving over the final affine-prime star:      OPEN;
sharp uniform parabolic curvature D^(1+o(1)):       OPEN.
```

## 9. The `B`-star is a pencil of Hankel planes, not one proved patch

The exact carrier chart makes the remaining operator issue transparent.
Choose unimodular matrices

```text
U=(r,r_tilde),             V=(s,s_tilde),
```

and orient signs so that

```text
U^T K(gamma) V=(0,theta;eta,gamma),
alpha=theta*c,             beta=-eta*c*B.          (9.1)
```

After division by the transverse common factor, the level is

```text
v-B*(u+gamma*c)=C.
```

Put `p=u+gamma*c`.  Every point of the corresponding carrier line has

```text
a=r*p+c*(theta*r_tilde-gamma*r),
b=s*C+B*(s*p-eta*c*s_tilde).                       (9.2)
```

Changing the harmless global sign convention changes the two minus signs
in (9.1)--(9.2), but none of the conclusions below.

Assume for display that `det(U)=det(V)=1`.  Differentiating the color chart
in `gamma` gives

```text
d/dgamma (c11,c12,c21,c22)
 =(r2*s2,r2*s1,r1*s2,r1*s1).                      (9.3)
```

Consequently the four scaled colors

```text
x_ij=r_i*s_j*c_ij
```

all translate with the same velocity

```text
Delta=r1*r2*s1*s2.                                (9.4)
```

This recovers the exact additive color normal form.  It does not put the
varying-`B` carrier family into one affine plane.  Eliminating `p` and
`gamma` from (9.2)--(9.4), separately in cell `(i,j)`, gives

```text
B*s_j*a_i-r_i*b_j
 +(B*c/(r_(3-i)*s_(3-j)))*x_ij=N_(ij,B),          (9.5)
```

where `N_(ij,B)` is independent of the two chart parameters.  Thus fixed
`B` is an ordinary rational affine/Hankel chart.  For `B!=B'`, however, the
plane normals

```text
(B*s_j,-r_i,B*c/(r_(3-i)*s_(3-j)))                (9.6)
```

are not proportional: the middle coordinate is fixed while the other two
scale with `B`.  The union over `B~D^(5/16)` is therefore a pencil of
different rational planes.  The common-plane patch theorem and the
fixed-direction parallel-line merger apply one `B` at a time, not to this
pencil.

One can formally divide the column coordinate in (9.5) by `B`.  In the
longitudinal coordinates this is exactly the incidence

```text
B*p+v=C.                                           (9.7)
```

With kernel `B^(-1/2)`, its row `ell^1` degree is `sqrt(K)` and its column
`ell^1` degree is `K^(-1/2)q^o(1)`, so Schur gives norm `q^o(1)`.  This
would remove the missing `sqrt(K)=D^(5/32)` and give

```text
D^(45/64)*sqrt(D/H)=D.                             (9.8)
```

But `b -> b/B` is not a reindexing of the original carry matrix.  It
replaces one column space by the lifted space of pairs `(B,b/B)`.  A base
color-pair coefficient which occurs in all `K` members of the star is then
copied into `K` lifted entries.  Its lifted squared norm is `K` times its
base gap-token energy.  The resulting `sqrt(K)` norm inflation cancels the
Schur gain in (9.7).  Pair uniqueness makes the lifted *edges* distinct; it
does not divide their repeated color coefficient.

This is exactly the hypothesis mismatch in the conditional refined-token
estimate (7.6) of the gap-token report.  The fixed-row packet merger does
not repair it either: it fixes a literal actual row pair, while distinct
members of the star may use disjoint row pairs.  If two members share the
same row pair and the same colors, ordinary pair uniqueness already forces
their column pair, hence `B`, to agree.

```text
scaled-color common translation (9.3)--(9.4):       EXACT;
fixed-B rational Hankel plane (9.5):                 EXACT;
varying-B common affine plane:                       FALSE;
weighted level-incidence Schur norm q^o(1):          PROVED;
norm-preserving pullback to base color tokens:       FALSE IN GENERAL;
existing affine/fixed-direction merger gives (9.8):  NO;
missing theorem: weighted rational-dilation merger / (7.6).
```
