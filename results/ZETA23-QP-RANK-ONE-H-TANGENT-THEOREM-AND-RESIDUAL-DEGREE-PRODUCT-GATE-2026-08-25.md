# QP rank-one `H`: sharp tangent theorem and the residual degree-product gate

**Date:** 2026-08-25
**Verdict:** preserving the original row-pair coordinate reveals a useful
split which is invisible after convolutional `S=a+a'` grouping.  The exact
multiplicative tangent sector of

```text
||H(conj(z) tensor z)||_2^2                         (0.1)
```

obeys the sharp bound

```text
E_tan(z) << D q^o(1) ||z||_2^4.                    (0.2)
```

This is proved below for arbitrary complex coefficients and even on the
full integer shell.  It keeps the rank-one color tensor throughout.

The complementary nonzero-determinant sector has an exact, substantially
narrower sufficient theorem.  If `l(p),r(gamma)` are its two incidence
degrees, it is enough to prove

```text
max_(p~gamma) l(p) r(gamma) << D q^o(1).            (RDP)
```

Indeed a general edge-degree spectral lemma then gives the full residual
operator norm squared `<<Dq^o(1)`, stronger than the rank-one target.
Exact hard-window searches at the critical scale satisfy `(RDP)` with
constant one in every tested all-integer instance; the worst cases are two
intersecting affine packets of lengths `asymp sqrt(D)`.  Removing exact
affine packet neighborhoods reduces the observed certificate to a small
fraction of `D`.  This is evidence and a precise new target, not a proof of
`(RDP)`.

Thus the four-cycle bound is **not proved**.  What is new here is a complete
tangent theorem, a rigorous one-line spectral closure conditional only on
`(RDP)`, and an exact computational audit of the original ungrouped `H`.
The lossless local Fejer/Airy theorem does not by itself prove `(RDP)`.

## 1. Keep the exact fourth-trace coordinate

Write

```text
kappa(a,b,c)=1_(|8abc-q^3|<=qD),
A_z(a,b)=sum_c z_c kappa(a,b,c).                    (1.1)
```

Cyclically permuting the roles of the three physical factors, define

```text
T_((b,b'),(c,c'))
 =sum_a kappa(a,b,c) kappa(a,b',c').                (1.2)
```

The physical window has width `D/q<1` in a missing coordinate, so `T` is a
`0/1` incidence.  For

```text
xi_(c,c')=conj(z_c) z_c',       ||xi||_2^2=||z||_2^4,
```

direct expansion gives the exact identity

```text
||T xi||_2^2
 =sum_(b,b') |sum_a conj(A_z(a,b)) A_z(a,b')|^2
 =||A_z||_(S_4)^4.                                  (1.3)
```

This is the original row-pair/frame-potential target in cyclic coordinates.
No row pairs are grouped by their sum, no positive convolutional relaxation
is inserted, and no coefficient copy is made.

Split the support of `T` by

```text
delta=b*c-b'*c'.                                    (1.4)
```

The tangent part has `delta=0`; the residual part has `delta!=0`.  From the
two hard-window inequalities on one edge,

```text
8a*delta
 =(8abc-q^3)-(8ab'c'-q^3),
```

and hence

```text
0<|delta|<<D                                         (1.5)
```

on every residual edge.

## 2. Sharp theorem for the complete tangent sector

### Theorem 2.1

Let all coordinates lie in fixed proportional `q`-shells and let `D=o(q)`.
For the tangent restriction `T_0` of (1.2), uniformly for every complex
coefficient vector,

```text
||T_0(conj(z) tensor z)||_2^2
 <<D q^o(1)||z||_2^4.                               (2.1)
```

### Proof

On a tangent edge put

```text
g=gcd(b,b'),       b=g*u,       b'=g*v,       (u,v)=1.
```

The equality `bc=b'c'` then forces, exactly,

```text
c=v*d,             c'=u*d.                          (2.2)
```

All four coordinates are in comparable shells, so `u` and `v` are
comparable.  Put `M=max(u,v)`; then

```text
g,d asymp q/M.                                      (2.3)
```

For fixed `(u,v)` let `R_(u,v)(g,d)` be the remaining physical incidence.
Its condition is simply

```text
|8*g*u*v*d*a-q^3|<=qD                               (2.4)
```

for some shell integer `a`.  Fix `d` and put `n=ga`.  Equation (2.4)
places `n` in an interval of length

```text
qD/(4*u*v*d) << D/M.                                (2.5)
```

Every integer `n` has `q^o(1)` factorizations `n=ga`, so the column degree
of `R_(u,v)` is

```text
r_(u,v) <<(1+D/M)q^o(1).                            (2.6)
```

Put

```text
w_d=conj(z_(v*d))*z_(u*d).
```

For `s_g=sum_d R(g,d)|w_d|`, positivity gives

```text
s_g<=||w||_1,              sum_g s_g<=r_(u,v)||w||_1.
```

Therefore

```text
sum_g |sum_d R(g,d)w_d|^2
 <=sum_g s_g^2
 <=r_(u,v)||w||_1^2.                                (2.7)
```

On a dyadic block `u,v asymp M`, define

```text
X_u=sum_(d: u*d in shell)|z_(u*d)|^2.
```

Cauchy gives `||w||_1^2<=X_u X_v`.  Moreover

```text
sum_(u asymp M) X_u
 <=max_c tau(c)*||z||_2^2
 <=q^o(1)||z||_2^2,                                 (2.8)
```

because each occurrence `c=ud` makes `u` a divisor of `c`.  Summing (2.7)
over coprime comparable `(u,v)` and then over dyadic `M` gives

```text
sum_M (1+D/M)q^o(1)||z||_2^4
 <<Dq^o(1)||z||_2^4.                                (2.9)
```

Different reduced ratios have disjoint output center pairs, so (2.9) is
exactly (2.1).  QED.

Here the dyadic sum starts with `M=1`; its two parts are explicitly
`O(log q)` and `D sum_(j>=0)2^(-j)=O(D)`.  The case `M=1` is precisely
`u=v=1`, so the proof includes `b=b',c=c'` and hence the full fourth-trace
diagonal.  On the actual narrow prime-power shell, unique factorization
makes the nontrivial tangent even smaller, but that extra fact is not used.

## 3. The residual theorem is an edgewise degree product

Let `T_*` be (1.2) restricted to `delta!=0`.  Put

```text
l(p)=#{gamma:T_*(p,gamma)=1},
r(gamma)=#{p:T_*(p,gamma)=1}.                       (3.1)
```

### Lemma 3.1 (edge-degree spectral bound)

For the biadjacency matrix `B` of any finite bipartite graph,

```text
||B||_(2->2)^2
 <=max_(x~y) deg(x)deg(y).                          (3.2)
```

To prove it, take a nonnegative Perron vector of the full symmetric
adjacency matrix and choose a vertex maximizing `x_v/sqrt(deg(v))`.
Every neighboring degree is at most the edgewise maximum divided by the
chosen degree, and the eigenvalue equation gives (3.2) immediately.

Consequently `(RDP)` implies

```text
||T_* xi||_2^2
 <=||T_*||^2 ||xi||_2^2
 <<Dq^o(1)||z||_2^4.                                (3.3)
```

Together with Theorem 2.1 and `||x+y||^2<=2||x||^2+2||y||^2`, this would
prove the complete unmasked rank-one `H` target.

This reduction is strictly more faithful than center-coherent convolution:
it preserves both ordered physical pairs and makes no additive completion
sum.  It is also more local than a uniform maximum-codegree conjecture.
One endpoint may have large degree provided the opposite endpoint degree on
each of its edges is proportionally small.

## 4. Why affine packets sit exactly at the endpoint

Suppose a left residual neighborhood lies on one integral affine packet

```text
a_t=a_0+r*t,       c_t=c_0-p*t,       c'_t=c'_0-P*t.
```

The first product has the exact expansion

```text
(a_0+r*t)(c_0-p*t)
 =a_0*c_0+(r*c_0-a_0*p)t-r*p*t^2.                  (4.1)
```

Since multiplying by the fixed center changes the allowed product range
only by `O(qD)`, a packet of length `L` satisfies

```text
L<<1+sqrt(D/(r*p))<<sqrt(D)                         (4.2)
```

whenever that leg moves; the other leg gives the symmetric statement.
The same argument applies to an affine right neighborhood.  Thus an edge
whose two endpoint neighborhoods are affine automatically has

```text
l(p)r(gamma)<<D.                                    (4.3)
```

The largest finite residual products are exactly of this type.  For
example at `q=10000,D=87` the extremal two full affine neighborhoods both
have degree `9`; each contains one edge belonging to the exact tangent
sector.  After the tangent sector is removed, their residual degrees are
`8` and `8`, giving the table's certificate `rho=64<D`.  Their coordinates
are consecutive opposite translations and remain at the `sqrt(D)` scale.

What remains unproved is a packet-or-dispersion statement strong enough to
establish `(RDP)` when one or both endpoint neighborhoods are scattered.
This is the honest residual inverse theorem.  The local affine theorem does
not justify simply deleting the scattered case.

## 5. Exact hard-window audit

The following table uses every integer in
`[(q/2)e^(-.2),(q/2)e^(.2)]`, with `D=round(q^(16/33))`.  `rho` is the
maximum edge-degree product of `T_*`.  `rho_peel` is the same quantity after
deleting every edge incident to an exactly affine neighborhood of degree at
least three.  `lambda^2` is the numerically computed squared spectral norm
of `T_*`; it is included only as a diagnostic.

| `q` | `D` | residual edges | `rho` | `rho_peel` | `lambda^2/D` |
|---:|---:|---:|---:|---:|---:|
| 400 | 18 | 684 | 9 | 4 | .500 |
| 900 | 27 | 3,084 | 9 | 8 | .333 |
| 1,400 | 34 | 6,120 | 16 | 6 | .373 |
| 2,200 | 42 | 16,208 | 25 | 15 | .455 |
| 3,500 | 52 | 40,336 | 36 | 12 | .494 |
| 6,000 | 68 | 112,188 | 49 | 12 | -- |
| 10,000 | 87 | 335,744 | 64 | 12 | -- |

Fifteen additional deterministic random scales between `180` and `9000`
also obeyed `rho<=D`; the worst ratio was `49/65=.754`.  After the affine
peel the worst ratio was `16/66=.242`.  These are finite observations, not
an interpolation argument or an asymptotic proof.

On the actual prime-power shell the literal window is much sparser:

| `q` | `D` | prime-power nodes | residual edges | `rho` |
|---:|---:|---:|---:|---:|
| 12,853 | 98 | 298 | 8 | 1 |
| 25,013 | 136 | 535 | 8 | 1 |
| 50,021 | 190 | 996 | 56 | 1 |
| 100,003 | 266 | 1,875 | 392 | 1 |

Every residual vertex in these four scans has degree one.  Again, this is
not a proof for all scales.

### Zero mode versus phase average

For the all-integer scans, the next table normalizes `||z||_2=1` and divides
energy by the target `D`.  “zero” is the flat coefficient
`z_c=|S|^(-1/2)`; “phase avg” averages 128 fixed-seed independent unit
phases.  The three entries are full, residual, and affine-peeled residual.

| `q` | zero ratios | phase-average ratios |
|---:|---:|---:|
| 400 | `.02219 / .00691 / .00630` | `.01989 / .00581 / .00560` |
| 900 | `.01147 / .00390 / .00382` | `.01057 / .00341 / .00338` |
| 1,400 | `.00699 / .00253 / .00240` | `.00648 / .00225 / .00221` |
| 2,200 | `.00587 / .00222 / .00215` | `.00540 / .00196 / .00194` |

The flat/zero mode is not anomalously large in these instances.  This rules
out a simple finite principal-mode obstruction but says nothing about a
specially optimized coefficient vector at untested scales.

## 6. Fejer/Airy assembly audit

The exact Fejer Stinespring lift and fixed-normal-lattice Airy vector
Plancherel theorem remain valid.  They do not imply `(RDP)`:

* the Fejer phase loses its integer center `b` modulo one;
* center Fourier is unitary and preserves the complete frame potential;
* estimating center frequencies separately repeats a physical color packet;
* fixed-lattice Airy Plancherel controls one retained normal lattice, whereas
  `l(p)r(gamma)` measures simultaneous reuse across two physical pair
  coordinates.

Keeping the exact row pair avoids the false convolutional relaxation, but it
does not manufacture cross-pair orthogonality.  A valid assembly can close
the problem in either of two ways:

1. prove `(RDP)` arithmetically by a tangent/affine/scattered inverse theorem;
2. prove an equally strong two-sided vector large sieve directly for `T_*`.

The first route is now the more concrete one: exact tangent packets are
already closed, exact affine packets saturate rather than violate the
target, and the remaining statement is explicitly edgewise.

## 7. Shared-edge transference: the exact remaining inverse theorem

There is a stronger two-sided relation than estimating the two endpoint
degrees separately.  Fix one residual base edge with row witness `a`,

```text
(a,b,c), (a,B,C),            delta=b*c-B*C!=0.       (7.1)
```

Let a full left neighbor and a full right neighbor be

```text
(x,b,d), (x,B,D),            (y,e,c), (y,E,C).       (7.2)
```

Every choice of a left neighbor and a right neighbor is allowed in (7.2),
whether or not the missing corner is an edge of `T_*`.  Put

```text
L1=x*d-a*c,   L2=x*D-a*C,
R1=y*e-a*b,   R2=y*E-a*B.                            (7.3)
```

Direct multiplication gives the exact ledger

```text
x*y*(d*e-D*E)
 =a^2*delta+a*c*R1+a*b*L1+L1*R1
             -a*C*R2-a*B*L2-L2*R2.                 (7.4)
```

Suppose all physical coordinates lie in `[alpha*q,beta*q]`.  Subtracting
two hard-window inequalities which share a coordinate gives

```text
|delta|, |L1|, |L2|, |R1|, |R2| <=D/(4*alpha).     (7.5)
```

Consequently every one of the `l(p)r(gamma)` Cartesian cross pairs obeys

```text
|d*e-D*E|
 <=[5*beta^2/(4*alpha^3)]D
   +[1/(8*alpha^4)]D^2/q^2
 <<_(alpha,beta) D.                                 (7.6)
```

This proves the proposed complete-bipartite near-determinant transference,
including its constants.  It does **not** assert that `(e,E)` and `(d,D)`
have a common physical row.

### 7.1 Cramer tokens and Pluecker identity

Orient the four endpoint vectors as

```text
p=(b,B),       q_0=(C,c),       u=(D,d),       v=(e,E).
```

Then `det(p,q_0)=delta`.  Define

```text
k=det(p,u),       r=det(u,q_0),
ell=det(v,q_0),   t=det(p,v).                        (7.7)
```

Cramer's rule and the two-dimensional Pluecker identity give, exactly,

```text
delta*u=r*p+k*q_0,       delta*v=ell*p+t*q_0,
delta*det(u,v)=r*t-k*ell.                            (7.8)
```

The same product-error comparison that proves (7.6) shows that all six
minors in (7.8) are `O(D)`.  The map from `u` to `(k,r)`, and symmetrically
from `v` to `(ell,t)`, is injective because `delta!=0`.  Thus `(RDP)` is
equivalent to the following more explicit physical inverse problem:

> Two sets of Cramer tokens in an `O(D)` box come from the two reciprocal
> hard-window arms of one base edge, and every cross token determinant is
> `O(|delta|D)`.  Prove that the product of their cardinalities is
> `O(Dq^o(1))`.

This normal form contracts the displayed coordinates from scale `q` to
scale `D`, but it is not by itself a complexity contraction.  The linear
token map has determinant `delta`, the cross tolerance becomes
`|delta|D`, and (7.8) reconstructs every original endpoint.  Without using
the reciprocal row witnesses it is an invertible repackaging of the same
two-inverse problem.

Indeed, for any `N` and `Q>>N`, the two `N`-point vector families

```text
u_i=(Q+i+1,Q+i),        v_j=(Q+j+1,Q+j)
```

satisfy `det(u_i,v_j)=j-i`.  Hence all `N^2` cross determinants have size
less than `N`.  Taking `N=D` disproves any attempt to deduce `(RDP)` from
the near-determinant Cartesian table alone.  These vectors are not claimed
to have physical row witnesses; that missing curvature is precisely the
essential input.

There is nevertheless a rigorous two-anchor token inequality.  Suppose two
left tokens `(k_1,r_1),(k_2,r_2)` are linearly independent, put

```text
g_1=gcd(k_1,r_1),
Delta_12=|k_1*r_2-r_1*k_2|,
E=max_(left x right)|r*t-k*ell|.                    (7.8a)
```

Then the opposite endpoint degree satisfies

```text
r(gamma)
 <=(2 floor(E/g_1)+1)
   (floor(2E*g_1/Delta_12)+1).                      (7.8b)
```

Indeed the cross token against the first anchor is a multiple of `g_1`, so
it has at most the first displayed number of values.  In one fixed fiber,
the integral right tokens differ by multiples of `(r_1/g_1,k_1/g_1)`;
their cross token against the second anchor changes by exactly
`Delta_12/g_1`.  This proves the second factor.  The symmetric statement
bounds the left degree from two independent right tokens.

For the physical arms, (7.8) gives `E<<|delta|D`.  A later primitive-content
audit gives `g_1|delta` and
`Delta_12=|delta|*|det(u_1,u_2)|<=|delta|D`.  Substitution into (7.8b)
shows that its right side is always at least a constant times `D`; it never
supplies the required factor `D/|U|` for a nontrivial opposite arm.  Thus
(7.8b) is a correct lattice count but not a broad-sector closure.  The
remaining inverse theorem needs separate physical input in both the generic
and approximately-collinear regimes.

### 7.2 Reciprocal-step transport

There is also an exact bridge between the two endpoint inverse charts.  Put

```text
g=B-b,        h=c-C.
```

When the indicated gaps are invertible, choose least-absolute signed steps

```text
g*U ==-1 (mod b),          h*V ==-1 (mod C).          (7.9)
```

For integers `R,S`, one then has

```text
delta*U=C+b*R,             delta*V=-b+C*S,           (7.10)
b*(1+R*S)=delta*(S*U-V),
C*(1+R*S)=delta*(U+R*V).                              (7.11)
```

Thus the two inverse steps are not independent.  The extremal affine
packets in the integer scans lie on the exact resonance `1+R*S=0`.  Away
from that resonance, however, (7.11) still permits `R,S=O(D)` and inverse
steps of order `q`; none of the currently proved derivative estimates turns
(7.11) into the product bound.

The exact determinant palettes of one representative maximizing edge at
each audited scale are:

| `q` | `D` | degrees | `delta` | cross `det(u,v)` range | palette size | largest multiplicity |
|---:|---:|---:|---:|---:|---:|---:|
| 400 | 18 | `3 x 3` | -1 | `[-2,3]` | 6 | 2 |
| 900 | 27 | `3 x 3` | -1 | `[-2,3]` | 6 | 2 |
| 1,400 | 34 | `4 x 4` | -1 | `[-3,4]` | 8 | 3 |
| 2,200 | 42 | `5 x 5` | -1 | `[-5,5]` | 11 | 4 |
| 3,500 | 52 | `6 x 6` | -1 | `[-6,6]` | 13 | 5 |
| 6,000 | 68 | `7 x 7` | -1 | `[-7,7]` | 15 | 6 |
| 10,000 | 87 | `8 x 8` | -1 | `[-8,8]` | 17 | 7 |

At `q=10000`, the full oriented palette `det(u,v):multiplicity` is

```text
-8:1, -7:2, -6:2, -5:3, -4:4, -3:4, -2:5, -1:7, 0:7,
 1:6,  2:5,  3:5,  4:4,  5:3,  6:3,  7:2,  8:1.       (7.12)
```

For the representative base

```text
p=(5000,5001),       (c,C)=(5002,5001),       delta=-1,
```

the left Cramer pairs `(k,r)` are

```text
(5,-6),(4,-5),(3,-4),(2,-3),(1,-2),(-1,0),(-2,1),(-3,2),
```

and the right pairs `(ell,t)` are

```text
(-6,5),(-5,4),(-4,3),(-3,2),(-2,1),(-1,0),(1,-2),(2,-3).
```

They are the two affine token packets `r=-k-1`, `t=-ell-1`.  All maximizing
edges in all seven scans have `|delta|<=3`; every one for which the inverse
chart is defined has `|U|=|V|=1`, `(R,S)=(-1,1)`, and coupling factor zero.
This is finite evidence for the affine-resonance classification, not a
proof that every future extremizer has this form.  In the four actual
prime-power scans both endpoint degrees are one, so every cross palette is
a singleton.

### 7.3 Endpoint gcd audit

Let

```text
G=gcd(b,B),       H=gcd(c,C).
```

The exact divisibility

```text
lcm(G,H) | delta                                  (7.13)
```

is true, since both `G` and `H` divide the two terms in `delta`.  It does
not close `(RDP)`.  The tempting one-arm bound

```text
degree(b,B) <<min(G,D/G)q^o(1)                     (7.14)
```

is false.  The literal physical affine biclique

```text
D=512L^2, q=2m,
p_i=(m+2i,m+2i+1),
gamma_j=(m+2j+2,m+2j+1),
a_ij=m-2i-2j-2                                    (7.15)
```

for `0<=i<L`, `2L<=j<3L`, and `m>>L`, has all `L^2`
transitions in the hard window, all transition determinants nonzero, and
both endpoint degrees equal to `L`.  Yet every endpoint gcd is one.  Taking
`m` polynomial in `L` makes `L` a fixed power of `q`, so the discrepancy in
(7.14) cannot be hidden in `q^o(1)`.  This family saturates `(RDP)` at
`L^2=D/512`; it does not refute `(RDP)`.

The elementary fixed-defect count explains the failed tradeoff.  A defect
`k=b*d-B*D` is a multiple of `G`, so there are `O(D/G)` possible layers.
Within one layer, solutions differ by `(B/G,b/G)`, allowing `O(G)` shell
positions before the reciprocal witness is used.  These are two
alternative costs, not two simultaneous bounds whose minimum may be taken.
The affine family (7.15) is the concrete hostile case for the missing
`O(G)` bound.

On the actual narrow prime-power shell the divisibility is even less useful.
A residual endpoint pair consists of two distinct prime powers.  Two powers
of the same prime differ by a ratio at least two, larger than the shell
ratio, so the two endpoints are coprime.  Therefore every actual residual
edge has `G=H=1`, and (7.13) is vacuous.

### 7.4 Existing common-neighbor and determinant theorems

The endpoint degrees are exactly the two common-neighbor counts

```text
l(p)=N(b,B),             r(gamma)=N(c,C).            (7.16)
```

The base edge relates their signed gaps by

```text
delta=b*(c-C)-C*(B-b),                               (7.17)
```

so the two gap sizes are comparable.  The strongest currently proved
uniform elementary estimate

```text
N(x,y)<<(|x-y|+1)sqrt(D)+D^(13/16)                  (7.18)
```

and the newer closed transverse sectors at the `D^(7/8)` scale estimate
each endpoint separately.  Even inserting `D^(7/8)` twice gives
`D^(7/4)`, not `D`.  No checked short-reciprocal, Kloosterman, determinant,
or fixed-determinant theorem couples the two selected endpoints strongly
enough to improve this to `(RDP)`.  In particular, unweighted
fixed-determinant matrix counts do not retain the two reciprocal row
witnesses, and summing their determinant layers gives only a much larger
ambient count.

The rigorous outcome is therefore a sharp reduction, not a closure:

```text
shared-edge Cartesian cross determinant O(D):          PROVED;
Cramer/Pluecker token identities:                       PROVED;
two endpoint reciprocal-step transport:                 PROVED;
lcm(endpoint gcds) divides delta:                        PROVED;
degree <=min(G,D/G)q^o:                                 FALSE;
Cramer tokens alone contract the arithmetic problem:    NO;
existing common-neighbor theorem implies RDP:            NO;
physical scattered-arm Cartesian determinant theorem:   OPEN.
```

## 8. Mechanical verification and status

The exact transition/Schatten identity, tangent split and parametrization,
rank-one application, degree-product certificate, affine detector, and
literal hard-window scans are implemented in

```text
src/qp_rank_one_h_tangent_residual.py
src/test_qp_rank_one_h_tangent_residual.py
```

Eight focused tests pass.  Lean certifies the tangent product identity, the
quadratic affine drift, the determinant mixed difference, the exact
two-sided affine-gap error ledger, both Cramer reconstructions, the
shared-edge Pluecker and product-error ledgers, and the reciprocal-step
transport identities in

```text
lean/weilcert/QPRankOneHTangentResidual.lean
```

Binary status:

```text
original ungrouped H / Schatten-4 identity:             EXACT;
exact tangent/residual determinant split:               EXACT;
tangent sector D q^o rank-one bound:                    PROVED;
edge-degree spectral lemma:                              PROVED;
RDP implies the complete residual bound:                 PROVED;
two-sided exact affine packet contribution:              <=D, PROVED;
shared-edge cross-neighborhood determinant band:          PROVED;
Cramer and inverse-step transference:                      PROVED;
all tested critical integer hard windows satisfy RDP:    VERIFIED FINITELY;
all tested actual prime-power residual degrees:           1;
uniform residual degree-product theorem RDP:              OPEN;
lossless Fejer/Airy automatically implies RDP:            NO;
complete rank-one H theorem:                              NOT PROVED;
sharp four-cycle bound:                                   NOT PROVED.
```
