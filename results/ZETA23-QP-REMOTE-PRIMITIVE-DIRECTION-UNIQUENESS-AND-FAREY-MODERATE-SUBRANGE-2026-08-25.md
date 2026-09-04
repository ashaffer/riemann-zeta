# QP remote primitive gate: direction uniqueness and the Farey-moderate subrange

**Date:** 2026-08-25  
**Verdict:** the stronger energy core makes every occupied remote primitive
direction `(p,d)` simple: for all sufficiently large `Q`, it supports at most
one physical point.  Farey spacing proves `Q^o(1)` in the complete
moderate-height region

```text
g*p^5 <= Q.                                           (0.1)
```

More strongly, it proves the full target bound throughout

```text
g*p^5<=Q*(1+A*B/Q)^2.
```

Only the region beyond this larger threshold remains open.  There Farey
spacing alone permits collections larger than the target.  The exact missing
input is a joint residue/content-rounding estimate, displayed in Section 6.
Hostile scans find no repeated direction, but all their remote points lie in
the genuinely unresolved region, so they do not prove the missing estimate.

No sharp four-cycle theorem is proved here.

## 1. Setup and the stronger energy ledger

Use the centered coordinates

```text
e=r*(Q+y)-y^2,             f=s*(Q-y)-y^2,
rho=r+s,                   kappa=s-r,
rho=g*p,                   kappa=g*d,
gcd(p,d)=1,                tau=e-f=g*n.               (1.1)
```

Then

```text
p*y-Q*d=n,                                             (1.2)
|g*n|<=A+B<=2B.                                       (1.3)
```

We work in a fixed compact collar `|y|<=eta*Q`, `eta<1`, after deleting
`n=0`, `L=0`, `kappa=0`, small `rho`, and small `r`.  The preceding cusp
reduction gives

```text
|y| >> Q^(2/3),             p >> (Q/B)^(1/3).         (1.4)
```

The energy core is stronger than the pointwise core:

```text
Q=D^(33/16),       A=D*m,       B=D*M,
1<=m<=M,           m^2*M^3<sqrt(D).                   (1.5)
```

Since `M>=m>=1`, (1.5) implies

```text
M<D^(1/6),         m<D^(1/10),
B<D^(7/6),         A<D^(11/10).                       (1.6)
```

Consequently the remote denominator and the two errors needed below have
the power margins

```text
p >> D^(43/144),
B^(4/3)/Q <= D^(-73/144),
A/Q^(2/3) <= D^(-11/40).                              (1.7)
```

One also has, after optimizing with the coupled constraint in (1.5),

```text
p^2/sqrt(A) >> D^(11/120),
p^4/H       >> D^(19/144),        H=D^(17/16).        (1.8)
```

Thus a remote primitive direction is longer than both the physical
square-root packet and the exact cyclic Fejer scale.  The direct argument
below uses the first two margins in (1.7).

## 2. Exact continuous coordinates

Solving the two centered identities for `rho` gives

```text
rho = [2Q*y^2+Q*sigma-y*tau]/(Q^2-y^2),
sigma=e+f.                                             (2.1)
```

Put

```text
rho_0(y)=2Q*y^2/(Q^2-y^2).                            (2.2)
```

Uniformly in the compact collar,

```text
rho=rho_0(y)+O(B/Q),             rho asymp y^2/Q,     (2.3)
rho_0'(y)=4Q^3*y/(Q^2-y^2)^2 << |y|/Q.               (2.4)
```

The second comparison in (2.3) uses the remote lower bound in (1.4), so
the `O(B/Q)` term is negligible.

Equation (1.2) gives the exact rational-slope approximation

```text
|y-Q*d/p|=|n|/p <= 2B/(g*p)=2B/rho.                  (2.5)
```

These two elementary formulas are enough to control multiplicity.

## 3. A remote primitive direction occurs at most once

Suppose two remote points have the same reduced pair `(p,d)`.  Index their
remaining data by `i=1,2`.  By (2.3)--(2.5), both `y_i` have the same sign,
are comparable to a common size `Y`, and

```text
|y_1-y_2| << B*Q/Y^2.                                 (3.1)
```

Using (2.3)--(2.4),

```text
p*|g_1-g_2|=|rho_1-rho_2|
 << (Y/Q)*|y_1-y_2|+B/Q
 << B/Y+B/Q.                                          (3.2)
```

The lower bounds in (1.4) now give

```text
|g_1-g_2| << B/(pY)+B/(pQ)
          << B^(4/3)/Q=o(1).                          (3.3)
```

Hence `g_1=g_2`.  Therefore

```text
r_1=r_2=g*(p-d)/2.                                    (3.4)
```

Subtracting the two first-band equations gives

```text
|(y_1-y_2)*(r-y_1-y_2)|<=2A.                         (3.5)
```

Compactness, (2.3), and the common sign imply

```text
|r-y_1-y_2| >> Y.                                     (3.6)
```

For positive `y`, this also follows directly from
`r=y^2/(Q+y)+O(A/Q)`; for negative `y`, `r>=0` makes (3.6) immediate.
Thus

```text
|y_1-y_2| << A/Y << A/Q^(2/3)=o(1).                  (3.7)
```

The two shifts are integral, so they are equal.  This proves:

> **Remote direction-uniqueness lemma.** In the energy core, for all
> sufficiently large `Q`, every reduced primitive direction `(p,d)` in the
> remote sector supports at most one point, even when the content `g` is not
> fixed in advance.

This is stronger than the elementary fixed-`(p,d,g)` quadratic count.  It
also explains the direction multiplicity one seen in every hostile scan.

## 4. Dyadic Farey spacing

Fix dyadic ranges

```text
G<=g<2G,                 P<=p<2P.                    (4.1)
```

By Section 3, two distinct points in this cell have distinct reduced
fractions `d/p`.  Farey spacing and (2.5) give

```text
1/(4P^2)
 <= |d_1/p_1-d_2/p_2|
 <= |y_1-y_2|/Q+4B/(G*P*Q).                          (4.2)
```

If

```text
B*P=o(Q*G),                                             (4.3)
```

then every two points in the same sign component satisfy

```text
|y_1-y_2| >> Q/P^2.                                   (4.4)
```

On the other hand (2.3) and (4.1) confine that component to an interval of
length

```text
Y << sqrt(Q*G*P).                                     (4.5)
```

It follows rigorously that the cell count obeys

```text
N(G,P) << 1+Y*P^2/Q
       << 1+sqrt(G*P^5/Q).                            (4.6)
```

This is the precise amount obtainable from Farey spacing alone.

## 5. A complete moderate-height theorem

Suppose now that

```text
G*P^5 <= Q.                                           (5.1)
```

Then (4.6) is `O(1)`.  Moreover (5.1) makes the error in (4.2) negligible
automatically:

```text
B*P/(Q*G)
 <= B*Q^(-4/5)*G^(-6/5)
 <= B*Q^(-4/5)=o(1),                                  (5.2)
```

where (1.6) gives `B<=Q^(56/99)<Q^(4/5)`.

There are only `O(log^2 Q)` dyadic `(G,P)` cells.  We have therefore proved

> **Farey-moderate theorem.** The total number of remote points satisfying
>
> ```text
> g*p^5<=Q
> ```
>
> is `O(log^2 Q)`, hence `O(Q^epsilon)` for every fixed `epsilon>0`.

This is stronger than the required
`(1+AB/Q)Q^epsilon` bound on that subrange.

In fact the same proof reaches exactly the target-sized transition.  Put

```text
Z=1+A*B/Q.                                             (5.3)
```

If

```text
G*P^5<=Q*Z^2,                                         (5.4)
```

then (4.6) is `O(Z)`.  The Farey error is still negligible.  When `Z=O(1)`
this follows from (5.2).  When `Z` is larger, use `Z<<AB/Q` to get

```text
B*Q^(-4/5)*Z^(2/5)
 <<A^(2/5)*B^(7/5)*Q^(-6/5)
 <=D^(-53/120),                                       (5.5)
```

where the last exponent is the worst value under `2u+3v<=1/2`,
`0<=u<=v`, with `m=D^u`, `M=D^v`.

Thus we have the stronger target-matched statement

> **Target-sized Farey theorem.** All remote points satisfying
>
> ```text
> g*p^5<=Q*(1+A*B/Q)^2
> ```
>
> contribute `O((1+AB/Q)Q^epsilon)`.

Since `rho=g*p asymp y^2/Q`, the boundary `g*p^5=Q` is equivalently

```text
rho*p^4 asymp Q,       or       |y|*p^2 asymp Q.      (5.6)
```

It is exactly where the Farey spacing `Q/p^2` ceases to dominate the full
physical `y`-scale.  The target allowance `Z` extends the controlled boundary
from this baseline to `g*p^5=Q*Z^2`.

## 6. Exact surviving gate in the hard region

It remains to count only the farther region

```text
g*p^5>Q*(1+A*B/Q)^2.                                  (6.1)
```

For fixed `(p,d,y)`, the first product band is

```text
|g*(p-d)*(Q+y)/2-y^2|<=A.                             (6.2)
```

Since `|d|<=eta'*p` for some fixed `eta'<1` in the compact collar, (6.2)
places `g` in an interval of length

```text
O(A/(Q*p))=o(1).                                      (6.3)
```

Thus `(p,d,y)` determines at most one content `g`.  The other exact
condition is

```text
n=p*y-Q*d,                 |g*n|<=2B.                (6.4)
```

Consequently the remaining theorem is precisely a joint count of the two
near-integrality events

```text
|p*y-Q*d|<=2B/g,
|g-2y^2/((p-d)*(Q+y))|<=C_eta*A/(Q*p),                (6.5)
```

with `(p,d)=1`, the parity condition making `g*(p+-d)/2` integral, the
remote cutoffs, and (6.1).

There is a useful exact renormalization of the second condition.  Define

```text
Gamma_Q(p,d)=2Q*d^2/[p*(p^2-d^2)].                    (6.6)
```

Then

```text
Gamma_Q(p,d)
 =Q/(p-d)+Q/(p+d)-2Q/p.                               (6.7)
```

Using `y=(Qd+n)/p`, the exact centre selected by the narrow `e`-band is

```text
Gamma_(Q,n)(p,d)
 =2*(Qd+n)^2/[p*(p-d)*(Q*(p+d)+n)],                   (6.8)
```

and direct subtraction gives

```text
Gamma_(Q,n)-Gamma_Q
 =2n*[Qd*(2p+d)+n*(p+d)]
   /[p*(p^2-d^2)*(Q*(p+d)+n)].                        (6.9)
```

Thus the hard core is exactly a **shifted three-reciprocal discrepancy**:
`g` must lie within `O(A/(Qp))` of (6.8), while `n` is the short residue
`py-Qd` with `|gn|<=2B`.  In a compact collar the shift in (6.9) is

```text
O(|n|*|d|/p^3+n^2/(Q*p^3)).
```

It need not fit inside the much narrower `A/(Qp)` window.  Hence the
`n`-dependence cannot be discarded by replacing (6.8) with the unshifted
three-reciprocal value (6.7).

A sufficient missing lemma is

```text
sum_(hard dyadic G,P)
 # {(g,p,d,y) satisfying (6.5)}
 << (1+A*B/Q)*Q^epsilon.                              (6.10)
```

The first condition in (6.5) is a short modular/Farey residue window; the
second is the much thinner shifted three-reciprocal content-rounding window.
Their heuristic
densities multiply to the desired volume.  Farey spacing controls the first
window but gives only (4.6); it supplies no deterministic decorrelation from
the second window beyond (6.1).  Proving (6.10) requires an anisotropic
large sieve, a Kloosterman-type dispersion estimate, or an additional exact
factorization.  No such estimate is proved here.

## 7. What the exact CRT `p^(-4)` gain does in the hard region

The symmetric exact-stationary CRT theorem gives, for one compact primitive
direction `p asymp P` with `P^2<=H`, normalized two-mask mass

```text
O(P^(-4)).                                             (7.1)
```

For `P^2>>_eta H`, there is no nonzero exact alias: the relations
`h=(p-d)^2*a` and `k=(p+d)^2*b` force `a=b=0` inside the Fejer support.
Thus only `P<<_eta sqrt(H)` matters for the nonzero exact sector.

There are `O(P^2)` reduced pairs `(p,d)` in a dyadic denominator block.
Consequently the unconditional exact-class mass is `O(P^(-2))`.  With the
energy-core floor `P>=D^(43/144)`, the worst opposite-sign stationary
amplitude from the companion CRT audit improves to

```text
D^(49/48)*D^(-43/72)=D^(61/144)
                     =D^(1/2-11/144).                (7.2)
```

This sharpens the earlier pointwise-core exponent `D^(23/48)`.  It proves
that the exact rational-stationary sector remains safely below square root.

The baseline split at

```text
P_c=(Q/G)^(1/5)                                       (7.3)
```

gives an even stronger *occupied-direction weighted* calculation.  Put

```text
P_Z=Z^(2/5)*P_c.                                      (7.4)
```

The unweighted obstruction (6.1) starts only at `P>P_Z`.  For comparison,
the weighted ledger can already be summed from `P_c`.  Put

```text
P_f=Q*G/B.                                            (7.5)
```

Energy gives `P_Z<<P_f`.  For
`P_c<P<=min(P_f,C_eta*sqrt(H))`, the Farey error is smaller than the main
spacing, so (4.6) and (7.1) give

```text
sum_(P_c<P<=min(P_f,C_eta*sqrt(H))) N(G,P)*P^(-4)
 <<sqrt(G/Q)*P_c^(-3/2)
 =(G/Q)^(4/5).                                        (7.6)
```

For the ultra-large exact-alias range
`P_f<P<=C_eta*sqrt(H)`, discard Farey spacing and use only the `O(P^2)`
possible reduced directions.  Then

```text
sum_(P_f<P<=C_eta*sqrt(H)) N(G,P)*P^(-4)
 <<P_f^(-2)=(B/(Q*G))^2.                              (7.7)
```

Summing dyadic `1<=G<=2B`, (7.6)--(7.7) give

```text
weighted hard mass
 <<Q^epsilon*((B/Q)^(4/5)+(B/Q)^2)
 <<Q^epsilon*(B/Q)^(4/5).                             (7.8)
```

At the worst energy endpoint this is `D^(-43/60)`.  Formally multiplying by
the worst exact opposite-sign amplitude `D^(49/48)` leaves

```text
D^(49/48-43/60)=D^(73/240)
                 =D^(1/2-47/240).                    (7.9)
```

If `P_f>C_eta*sqrt(H)`, the sum in (7.7) is empty.  Beyond the exact-alias
cutoff the pointwise CRT average plateaus at `H^(-2)`; one may not continue
the `P^(-4)` estimate into an approximate high-denominator sector.

Equations (7.2) and (7.8) are genuine gains for exact CRT classes.  They do
**not** prove the unweighted cardinality estimate (6.10): the physical slope
is only approximately the exact rational direction, and transferring the
frequency-dependent stationary amplitude to the occupied direction without
losing (7.1) is a separate theorem.  Neither `g<=2B` nor `rho=g*p` forces a
cardinality saving in the ultra-large range; they become useful only after
the `P^(-4)` weight is present.

## 8. Exact reflected hard family: height does not imply orthogonality

There is an infinite exact family showing why high primitive height cannot
by itself yield Cotlar decay between packet pairs.  Let `p>d>=1` be coprime
and put

```text
ell=p^2-d^2,                 Q=p*ell+1,
y=d*ell,                     r=d^2*(p-d),
s=d^2*(p+d).                                           (8.1)
```

A direct substitution gives

```text
e=r,                         f=s,
g=2d^2,                      n=-d,
T=-2d^2,                     L=-8d^6.                 (8.2)
```

Thus `n*L*kappa!=0`.  Reflection

```text
(y,r,s) -> (-y,s,r)                                    (8.3)
```

gives a second remote point with primitive direction `(p,-d)`.  Their first
coordinates are `Q+y` and `Q-y`, whose sum is exactly `2Q`; hence the two
ordered singleton packets have an exact completion-sum collision.

For fixed `d` and `p` tending to infinity,

```text
Q asymp p^3,       |e|+|f| asymp_d p,
Q^(16/33) asymp p^(16/11),
g*p^5/Q asymp_d p^2.                                  (8.4)
```

So this family lies in the energy core and far beyond the unresolved
threshold (6.1).  It does not contradict direction uniqueness—the two
directions are `(p,d)` and `(p,-d)`—and a two-point reflection costs only
`Q^o(1)`.  It does disprove any proposed argument that converts large `p`,
exact-tangent singleton capacity, or the CRT step alone into decay between
distinct reflected packet pairs.

The exact fixture and parity ledger are in
`src/qp_high_primitive_packet_pair_audit.py`; the full spacing/Cotlar audit
is `results/ZETA23-QP-HIGH-PRIMITIVE-PACKET-SPACING-COTLAR-AND-RSR-BRIDGE-AUDIT-2026-08-25.md`.

## 9. Direction-cluster hostile scans

The strict diagnostic deletes `n=0`, `L=0`, and `kappa=0`, and also imposes
`rho^3>Q` and `r^2>A`.  It then groups by `(p,d)`, by `p`, and by `g`.

| `Q` | `A` | `B` | remote | distinct `(p,d)` | max direction mult. | distinct `p` | max `p` mult. | distinct `g` | `<=Q / (Q,QZ^2] / >QZ^2` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5000 | 63 | 100 | 10 | 10 | 1 | 6 | 3 | 4 | `0 / 0 / 10` |
| 20011 | 122 | 488 | 12 | 12 | 1 | 11 | 2 | 5 | `0 / 0 / 12` |
| 39800 | 170 | 170 | 10 | 10 | 1 | 5 | 2 | 3 | `0 / 0 / 10` |
| 100003 | 266 | 1064 | 9 | 9 | 1 | 8 | 2 | 4 | `0 / 0 / 9` |
| 100003 | 266 | 2128 | 12 | 12 | 1 | 11 | 2 | 6 | `0 / 0 / 12` |
| 1000003 | 812 | 2478 | 11 | 11 | 1 | 7 | 2 | 5 | `0 / 0 / 11` |

Every direction is simple, as the theorem predicts.  Denominator
clustering does not reduce merely to a sign pair: in the first fixture,
`p=55` supports the three distinct directions `d=-9,-7,9`, with contents
`5,3,5`.  Thus grouping only by `p` is not a valid replacement for the
direction theorem.  Most importantly, every observed point is in the hard
region (6.1).  The scans
therefore expose, rather than resolve, the remaining gate.  They find no
counterexample or growing repeated-direction packet.

The exact cluster scanner and energy ledger are in
`src/qp_coupled_cusp_fejer_inverse.py`; focused tests are in
`src/test_qp_coupled_cusp_fejer_inverse.py`.

## 10. Binary status

```text
energy bounds (1.6)--(1.8):                           PROVED;
one point per remote primitive direction:             PROVED;
dyadic Farey bound (4.6):                              PROVED;
remote region g*p^5<=Q has O(Q^epsilon) points:        PROVED;
region g*p^5<=Q*(1+AB/Q)^2 meets target:              PROVED;
fixed (p,d,y) determines at most one g:                PROVED;
exact CRT sector with energy floor is D^(61/144):      PROVED;
weighted exact-alias hard split (7.8):                PROVED AS A WEIGHT LEDGER;
approximate-primal to exact-CRT attachment:           OPEN;
infinite reflected hard collision family:             PROVED;
hard-region joint residue/content estimate (6.10):     OPEN;
remote bound (1+AB/Q)Q^epsilon in full:                OPEN;
counterexample to the corrected remote gate:           NOT FOUND;
sharp four-cycle bound:                                NOT PROVED.
```
