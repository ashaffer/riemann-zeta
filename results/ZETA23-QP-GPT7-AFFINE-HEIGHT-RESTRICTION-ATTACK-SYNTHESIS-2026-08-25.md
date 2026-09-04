# QP sharp four-cycle attack: affine height and completion-sum restriction

**Date:** 2026-08-25  
**Status:** the sharp `D^(1+o(1))` fourth-trace bound is **not proved**.  The
best unconditional project bound remains `D^(9/8+o(1))`.

This attack does make several strict advances.  It replaces an unnecessarily
strong fixed-completion-sum target by the exact norm used by the fourth trace,
shrinks the unresolved Fejer core, and completely classifies the exact dual
major-arc geometry.  In the symmetric chart it closes the whole exact remote
rational-stationary sector with a power saving, closes every singular axis in
the arbitrary-content reflected normal form, and raises the denominator floor
of the surviving transverse arithmetic sector.  It also identifies and
falsifies several tempting but incorrect shortcuts.

## 1. The right target is an `S`-restriction norm

At the critical scale

```text
q=D^(33/16),             H=q/D.
```

For a dyadic reciprocal width `U`, put

```text
A_U={a in I_q: ||C/a||<=c*U/H}.
```

The one-product divisor argument gives

```text
|A_U|<<D*U*q^o(1).                                      (1.1)
```

If `z` and `y` are supported on `A_U` and `A_V`, the actual completion
energy is exactly

```text
sum_S |sum_(a+b=S) z_a*y_b|^2
 =||z*y||_2^2
 =integral_0^1 |zhat(alpha)|^2|yhat(alpha)|^2 dalpha.  (1.2)
```

Thus the sharp new theorem is the hereditary reciprocal-strip restriction
estimate

```text
||z*y||_2^2
 <<sqrt(D*min(U,V))*q^o(1)*||z||_2^2*||y||_2^2.        (RSR)
```

It is equivalent, up to logarithms from dyadic amplitudes, to the flat
statement

```text
||1_B*1_E||_2^2
 <<sqrt(D*min(U,V))*|B|*|E|*q^o(1)                    (1.3)
```

for **every** `B subset A_U` and `E subset A_V`.  The hereditary quantifier
is essential because the original coefficients can select a hostile subset.

`(RSR)` is weaker than the formerly targeted pointwise estimate for every
fixed `S`, but it is exactly what the fourth trace needs.  It is also sharp:
at `C=Q^2`, an interval of `L asymp sqrt(D*min(U,V))` tangent points has
normalized self-convolution energy

```text
(2*L^3+L)/(3*L^2)=2*L/3+1/(3*L).                     (1.4)
```

### 1.1 A new unconditional core contraction

Let `m=min(U,V)` and `M=max(U,V)`.  Young's inequality and (1.1) give

```text
||1_(A_m)*1_(A_M)||_2^2<<D^3*m^2*M*q^o(1).           (1.5)
```

After the squared Fejer weight `m^(-4)M^(-4)`, every mask with

```text
m^2*M^3>=sqrt(D)                                      (1.6)
```

is already at the desired `D^(5/2+o(1))` energy scale.  Therefore the true
unresolved energy core is

```text
m^2*M^3<sqrt(D).                                      (1.7)
```

Its balanced endpoint is `U=V<D^(1/10)`, improved from the `D^(1/6)`
endpoint of the fixed-`S` argument.  At `m=1`, it gives `M<D^(1/6)` instead
of `D^(1/4)`.

Assuming `(RSR)`, one dyadic Fejer term in the convolution norm is

```text
<<D^(5/4)/(m^(5/4)*M^(3/2))*q^o(1).                  (1.8)
```

The double dyadic sum converges, proving the required `D^(5/2+o(1))`
completion energy.

### 1.2 Why the old fixed-`S` vector `TT*` cannot work

For every point in the central two-inverse mask, the Fejer rank-one vector
has a constant-size inner product with its sampling vector.  Hence, for any
residual set `E`, even after deleting a chosen tangent packet,

```text
<b,G_E*b>>=c*|E|,          ||G_E||>=c*H^2*|E|.        (1.9)
```

So an `H^2*sqrt(D)` operator estimate in that coefficient space is merely the
desired pointwise cardinality estimate rewritten.  Spatially remote points
do not become orthogonal there.  Orthogonality has to be sought in the
Fourier variable dual to the completion sum `S`.

## 2. Exact dual major arcs are now classified

Normalize the fixed-sum reciprocal curve as

```text
gamma(t)=(t,lambda/t,lambda/(1-t)),
Phi(t)=(-m,h,k) dot gamma(t),          lambda=C/S^2.  (2.1)
```

The cleared stationary polynomial is a quartic whose discriminant factors
as

```text
Disc=-16*lambda^2*h*k*m*Delta,
Delta=(m+lambda*(h-k))^3+27*lambda^2*h*k*m.          (2.2)
```

All repeated interior saddles are exactly cubic.  If
`lambda=P/Q` and `t=r/(r+s)` are reduced, the primitive cubic frequency is

```text
(P*(r+s)^3/c, (Q/c)*r^3, -(Q/c)*s^3),
c=gcd(Q,(r+s)^3).                                    (2.3)
```

There is no hidden exact Pell or CRT component of the caustic surface.

More importantly, the cubic ray is only one line in the full rank-two
stationary lattice.  If `n=r+s`,

```text
g=gcd(P*n^2,Q*r^2*s^2),
A=P*n^2/g,             B=Q*r^2*s^2/g,
u*r^2-v*s^2=1,

xi_0=(0,r^2,s^2),      xi_1=(-A,B*v,B*u).            (2.4)
```

Then every integer stationary frequency is uniquely in

```text
Lambda_(r,s)=Z*xi_0+Z*xi_1=V^perp intersect Z^3,     (2.5)
```

where the primitive tangent direction is

```text
V=(Q*r^2*s^2,-P*n^2*s^2,P*n^2*r^2)/g.               (2.6)
```

Let `z_0=S*gamma(r/n)`.  The affine tangent line meets `Z^3` if and only if

```text
xi_0 dot z_0 in Z,           xi_1 dot z_0 in Z.      (2.7)
```

This full affine-height character, not the cubic phase alone, is the exact
packet criterion.

### 2.1 A cubic-only major-arc rule is false

For

```text
lambda=1/2,       S=5,       t=1/3,
```

the primitive tangent is `V=(8,-36,9)`.  Its two stationary heights are

```text
45/2,       15,                                      (2.8)
```

so the affine line misses `Z^3`.  Nevertheless the primitive cubic
frequency `(27,2,-16)` has phase zero.  Thus

```text
integral cubic saddle  =>  physical tangent packet
```

is false.  A proof which subtracts only cubic rays misses nontrivial affine
character cosets.

### 2.2 Exact cyclic Fejer regrouping

Write `V=(R,-P_0,K_0)` and the tangent line as

```text
(a,alpha-P_0*a/R,beta+K_0*a/R).
```

Integer stationary modes obey

```text
k*K_0-h*P_0==0 (mod R).                              (2.9)
```

For any finitely supported coefficients `c_h`, the congruence detector gives
the exact identity

```text
sum_((h,k) satisfying (2.9)) c_h*c_k*e(h*alpha+k*beta)
 =1/R sum_(j mod R)
   P_c(alpha-j*P_0/R)*P_c(beta+j*K_0/R).             (2.10)
```

For the normalized height-one Fejer polynomial `P_N`, define

```text
eta=min_(j mod R) max(
 ||alpha-j*P_0/R||, ||beta+j*K_0/R||).               (2.11)
```

Positivity and the sine bound prove

```text
1/R sum_j P_N(alpha-j*P_0/R)P_N(beta+j*K_0/R)
 <=min(1,1/(4*N^2*eta^2)).                           (2.12)
```

With `N asymp H`, `eta<<1/H` is exactly a tangent-orbit point within product
tolerance `D`; otherwise (2.12) supplies genuine suppression.  The remaining
analytic problem is to retain this orbit decay after inserting the
frequency-dependent stationary-phase amplitude.

Every genuine lattice tangent itself has the sharp capacity

```text
O(1+sqrt(D*min(U,V))/R).                             (2.13)
```

Thus a single major packet never exceeds `(RSR)`.

### 2.3 The symmetric CRT orbit and the exact remote sector

At the symmetric centre `lambda=1/4`, the stationary congruence has no hidden
short aliases.  For coprime `r,s` and `n=r+s`, the primitive direction is

```text
V=(4*r^2*s^2,-n^2*s^2,n^2*r^2)/gcd(n^2,4).          (2.14)
```

If `n` is even, stationarity is exactly `r^2|h` and `s^2|k`.  If `n` is odd,
it is exactly

```text
h=r^2*a,       k=s^2*b,       b-a==0 (mod 4).        (2.15)
```

Thus the cyclic orbit is either a full CRT product grid or an index-four
average of such grids.  For normalized Fejer `P_N`, put

```text
B_N(M)=max_theta 1/M sum_(u mod M) P_N(theta+u/M).
```

If `N=q_0*M+z`, `0<=z<M`, residue orthogonality gives exactly

```text
B_N(M)=[z*(q_0+1)^2+(M-z)*q_0^2]/N^2,               (2.16)
```

and hence the intercept-uniform orbit bound

```text
cyclic mass <=B_N(r^2)*B_N(s^2)
             <<(r^(-2)+N^(-1))*(s^(-2)+N^(-1)).     (2.17)
```

For the remote primitive slope in (3.15), `r,s asymp p`.  The larger
pointwise core gives `p>>D^(13/48)`, while the actual energy core (1.7)
improves this to

```text
p>>D^(43/144).                                       (2.18)
```

With `N asymp H`, (2.17) supplies one full `H` saving plus `D^(1/48)` in
the pointwise core, and plus `D^(19/144)` in the energy core.

This spacing is strong enough to absorb the varying stationary amplitude on
the **exact rational-stationary locus**.  Summing primitive directions
`p asymp P`, their aliases, and dyadic frequencies gives the worst block

```text
D^(49/48)*P^(-2).                                    (2.19)
```

Therefore the exact rational stationary locus contributes `D^(23/48)` in
the larger pointwise core, and in the energy core improves to

```text
D^(49/48)*D^(-43/72)=D^(61/144)
                         =D^(1/2-11/144).            (2.20)
```

Both are below the square-root target.  Exact nonzero aliases occur only
while `P^2<<H`; beyond that scale the Fejer support contains no nonzero exact
alias.  Approximate residue layers instead plateau at `H^(-2)`, so the
`P^(-4)` weight in (2.17) cannot be extrapolated to arbitrary high-
denominator near-saddles.  The unresolved part is the quantitative passage
from approximate primal slopes to exact rational classes, including this
high-`P` plateau and irrational saddles—not the exact rational locus itself.

## 3. The primal cusp and its exact arithmetic

At the worst symmetric centre `C=Q^2,S=2Q`, put

```text
a=Q+y,       v=Q-y+r,
b=Q-y,       w=Q+y+s,
e=r*(Q+y)-y^2,       f=s*(Q-y)-y^2.                 (3.1)
```

Define

```text
rho=r+s,       kappa=s-r,
sigma=e+f,     tau=e-f.                              (3.2)
```

Then exactly

```text
y*rho=Q*kappa+tau,

Q*(rho^3-kappa^2*(rho+2Q))
 =sigma*rho^2+tau*kappa*(rho+4Q)+2*tau^2.            (3.3)
```

The first identity is an indispensable divisibility condition; the cubic
alone does not count points.

On the zero-error curve, `rho^3=kappa^2(rho+2Q)`.  Its nonzero integral
points have the unique factorization

```text
rho=h*d^2*p,       kappa=h*d^3,
(p,d)=1,           h*p*(p^2-d^2)=2Q.                (3.4)
```

Indeed, write `g=gcd(rho,kappa)`, `rho=g*p`, `kappa=g*d`; then `d^2|g`.
Equation (3.4) follows on writing `g=h*d^2`, and the converse is immediate.
Because

```text
h*p*(p-d)*(p+d)=2Q,                                 (3.5)
```

there are only divisor-many exact nonzero cusp labels.  For each fixed label,
the narrower inequality in (3.1) is a monic-quadratic sublevel set and has
`O(1+sqrt(D*min(U,V)))` integer values of `y`.  Consequently the whole exact
algebraic cusp locus is within the necessary packet budget, up to `q^o(1)`.

For a noncentral error-labelled point, put

```text
g=gcd(rho,kappa),       rho=g*p,       kappa=g*d,
tau=g*n.
```

Then a second exact normal form is

```text
p*y-Q*d=n,

rho^3-kappa^2*(rho+2Q)=g^2*Delta,
Delta=g*p*(p^2-d^2)-2Q*d^2,

Q*Delta=sigma*p^2+n*d*(g*p+4Q)+2*n^2.              (3.6)
```

These identities retain the primitive direction, its scale, and both error
coordinates.  They are the primal counterpart of the dual affine-height
lattice.

### 3.1 Exact-cubic versus minor-volume is also a false dichotomy

Removing `n=0` and `Delta=0` does **not** leave a pure volume term.  Let
`Y>=3` and take

```text
Q=Y*(Y-1),       y=Y,       r=s=1.                  (3.7)
```

Then

```text
e=0, f=-2Y, rho=2, kappa=0, n=Y, Delta=2.           (3.8)
```

Thus `n*Delta!=0`.  Taking `A=Q^(16/33)` and `B=2Y` gives

```text
A*B/Q=2*Q^(-1/66),                                  (3.9)
```

although there is an actual counted point.  This disproves an estimate of
the form `O(A*B/Q*q^o(1))` for the complement of only the exact cubic and
common-product loci.  The full conjectural bound with `+sqrt(A)` survives:
the example is a small-height secondary packet.  Major arcs must therefore
be defined by affine height/orbit proximity, not merely by the equation
`Delta=0`.

### 3.2 The complete low-height sector is affordable

This repair can be made rigorous.  The translated-tangent condition is
`kappa=0`, hence `r=s=j`.  Its two bands imply

```text
j*|y|<=B,               |j*(Q+y)-y^2|<=A.            (3.10)
```

Put

```text
J=1+(B^2/Q)^(1/3).                                   (3.11)
```

Square spacing in the narrow quadratic gives

```text
# {kappa=0}
 <<sqrt(A)+J+A*sqrt(J/Q).                            (3.12)
```

Throughout even the larger pointwise core `m*M^2<sqrt(D)`, the last two
terms are smaller than `sqrt(A)`.  More generally, the identities in (3.3)
give

```text
y^2<<Q*rho+B.                                        (3.13)
```

For a sufficiently small collar-dependent constant `c`, every point with

```text
rho<=c*Q^(1/3)                                       (3.14)
```

has `|y*rho|+|tau|<Q`; the divisibility in (3.3) then forces `kappa=0`.
Therefore the **entire** small-`rho` sector, including the counterexample
(3.7), costs only `O(sqrt(A))`.

After also paying the already controlled `n=0` and `L=0` slices, every
survivor satisfies

```text
rho>>Q^(1/3),       |y|>>Q^(2/3),
g<=2B,              d!=0,
p>>(Q/B)^(1/3).                                      (3.15)
```

At the worst endpoint of the larger pointwise core this gives

```text
p>>D^(13/48).                                        (3.16)
```

Thus all bounded and subpower rational directions have been rigorously
removed.  The corrected scalar remote gate is

```text
# {remote points with n*L*kappa!=0}
 <<(1+A*B/Q)*Q^o(1).                                 (3.17)
```

It remains open, but it is now a genuinely high-denominator rational-slope
problem rather than a mislabeled cusp packet.

### 3.3 Direction uniqueness and the Farey-moderate theorem

The energy core strengthens (3.16).  Since `m^2*M^3<sqrt(D)` implies
`B<D^(7/6)`, (3.15) gives the energy-scale bound (2.18).  Solving (3.3)
also gives

```text
rho=2Q*y^2/(Q^2-y^2)+O(B/Q).                         (3.18)
```

The margins `B^(4/3)/Q=o(1)` and `A/Q^(2/3)=o(1)` then prove that a fixed
reduced primitive direction `(p,d)` supports at most one remote point, even
when its content `g` varies.

In a dyadic cell `g asymp G`, `p asymp P`, Farey spacing and (3.18) give

```text
N(G,P)<<1+sqrt(G*P^5/Q),                             (3.19)
```

whenever `B*P=o(Q*G)`.  Put

```text
Z=1+A*B/Q.
```

The energy inequalities make the Farey error negligible throughout
`G*P^5<=Q*Z^2`; summing dyadic cells proves the full target there:

```text
# {remote points with g*p^5<=Q*Z^2} <<Z*Q^o(1).      (3.20)
```

Thus the corrected scalar gate remains open only in the sharply defined
region

```text
g*p^5>Q*(1+A*B/Q)^2.                                 (3.21)
```

There the two exact near-integrality conditions are

```text
|p*y-Q*d|<=2B/g,
|g-2y^2/((p-d)*(Q+y))|<<A/(Q*p).                     (3.22)
```

If `n=p*y-Q*d`, the centre in the second line equals

```text
Gamma_(Q,n)(p,d)
 =2*(Q*d+n)^2/[p*(p-d)*(Q*(p+d)+n)].                 (3.23)
```

At `n=0` it has the exact three-reciprocal form

```text
Gamma_Q(p,d)=Q/(p-d)+Q/(p+d)-2Q/p.                  (3.24)
```

The explicit `n`-shift is generally larger than the narrow window in
(3.22), so it cannot be discarded.  The last scalar problem is therefore a
short-residue, shifted three-reciprocal discrepancy theorem in the hard
region (3.21).

## 4. The remaining new theorem

The local determinant lemma decomposes each `q^(1/3)` block into an affine
reciprocal packet and at most two atoms.  If

```text
z=sum_i z_i,       y=sum_j y_j
```

are the corresponding packet decompositions, the exact sufficient square
function is

```text
||sum_(i,j) z_i*y_j||_2^2
 <<q^o(1)*sum_(i,j)||z_i*y_j||_2^2.                 (4.1)
```

Young on one packet pair gives

```text
||z_i*y_j||_2^2
 <=sqrt(D*min(U,V))*||z_i||_2^2*||y_j||_2^2.        (4.2)
```

Equations (4.1)--(4.2) imply `(RSR)`.  Bounded overlap of packet-pair
sumsets would imply (4.1), but abstract remote singleton packets show that
spatial separation alone is insufficient.

### 4.1 High primitive packets are atomic, but not orthogonal

For a reduced remote direction `(p,d)`, the exact symmetric tangent has
first-coordinate step

```text
R=(p^2-d^2)^2/chi,       chi in {1,4}.               (4.2a)
```

The energy floor (2.18) makes `R>>D^(43/36)`, so every exact tangent is a
singleton and every fixed parallel product-band component has `O(1)`
points.  This local fact does not control how many different singleton
packet pairs have the same completion sum.

Indeed, for any coprime `p>d>=1`, put

```text
ell=p^2-d^2,       Q=p*ell+1,       y=d*ell,
r=d^2*(p-d),       s=d^2*(p+d).                     (4.2b)
```

Then `e=r`, `f=s`, `g=2d^2`, `n=-d`, and `L=-8d^6`; this is genuinely
remote.  Its reflection `(-y,s,r)` has direction `(p,-d)`, yet the two
singleton pairs collide exactly at completion sum `2Q`.  The family lies in
the central energy mask with arbitrarily large `p`.  Hence primitive height,
singleton capacity, and direction separation alone do **not** imply Cotlar
decay or bounded packet-pair overlap.

The reflected obstruction can nevertheless be peeled algebraically.  Put

```text
ell=p^2-d^2,       c=Q-p*ell,       u=y-d*ell,
delta=g-2d^2,      h=d*c-2p*u.                        (4.2c)
```

On the central-content branch `delta=0`, the errors become

```text
e=d*(p-d)*(h-d*u)-u^2,
f=d*(p+d)*(h+d*u)-u^2.                                (4.2d)
```

The literal `u=0` reflected family has only `D^(23/96+o(1))` fixed-centre
points.  The distinct balanced branch `h=0` also has
`D^(23/96+o(1))` points.  After those are removed, set

```text
k=(h-d*u)*(h+d*u).
```

Both one-band cancellation branches `k=0` have
`O(sqrt(A)*Q^o(1))` points by an exact divisor parametrization.  The surviving
central-content chart has the normal-crossing identity

```text
(e+u^2)*(f+u^2)=d^2*(p^2-d^2)*k,       k!=0.         (4.2e)
```

An additional transverse identity gives

```text
u*y=-d*p*n-(e+f)/2.
```

On the already established remote region `|y|>>Q^(2/3)`, it forces
`|u|<<B/Q^(1/3)`.  Cubic spacing then gives the complete central-content
count

```text
# {g=2d^2 remote points} <<B/Q^(1/3)
                              <<D^(23/48)
                              <<D^(-1/48)*sqrt(A).    (4.2e')
```

Thus the entire nonzero-`k` chart is closed, not merely its three axes.

For arbitrary content, the correct blow-up is scaled rather than centred at
`g=2d^2`.  Put

```text
ell=p^2-d^2,
T=g*p*ell-2Q*d^2,       v=2d*y-g*ell,
z=T+2p*v.                                             (4.2e'')
```

Then exactly

```text
4d^2*e+v^2=-g*(p-d)*(z+d*v),
4d^2*f+v^2=-g*(p+d)*(z-d*v),
(4d^2*e+v^2)*(4d^2*f+v^2)
 =g^2*ell*(z+d*v)*(z-d*v).                           (4.2e''')
```

The same transverse mechanism gives `|v|/|d|<<B/Q^(1/3)=o(sqrt(A))`.
All three singular axes

```text
z=0,             z=d*v,             z=-d*v
```

have `O(sqrt(A)*Q^o(1))` points, even for asymmetric bands `A<=B`.  The
bad-sign balanced cancellation is covered by the exact factorization

```text
(p-d)*(a*(p-d)+M)=2*(Q+eta),       |eta|<<sqrt(A).
```

There is also a uniform theorem beyond the axes.  Summing all integral and
half-integral scaled-cusp multiplier charts at once gives

```text
# {d^2 divides g} <<B/Q^(1/3)*Q^o(1)
                       <<D^(23/48+o(1)).             (4.2e.4)
```

The order of summation matters: grouping first by the small scaled height
makes the multiplier unique by cubic spacing.  Summing separate multiplier
charts would lose this gain.

After these axes are removed, both factors in (4.2e''') are nonzero.  The
narrow factor forces

```text
p>>sqrt(Q/A)>=D^(77/160),                           (4.2e.5)
```

improving the old universal energy floor `D^(43/144)`.  The sole surviving
arithmetic locus is therefore the genuinely transverse, high-primitive joint
rounding problem `(z+d*v)*(z-d*v)!=0` with `d^2` not forced to divide `g`;
no unclassified singular axis remains.  An explicit compact-remote
family with `g=2d`, `d^2` not dividing `g`, and both factors nonzero proves
that square-content forcing would be false.  The family is sparse and does
not violate the target, but it confirms that the residual locus is genuine.

There is also a precise scale limit on a tempting thickened-CRT argument.
If an actual outer `L^2` variable supplied square-root cancellation across
`W` residue layers, then in the range `P^2<=H` the Farey ledger would leave
only `D^(7/96)` after the worst Airy amplitude.  Such a square root is false
pointwise for positive cyclic layers.  For `P^2>H`, a shifted layer has
generic mass `H^(-2)`, not `P^(-4)`, so even the conditional low-`P` ledger
cannot be extrapolated across the remaining hard range.  The needed theorem
must identify genuine completion-sum orthogonality while classifying the
reflected algebraic collisions.

The residue square root itself is exact in an auxiliary cyclic character:
Parseval gives `sqrt(W)` times the one-layer mass.  What is unproved is the
intertwining of that auxiliary character with the physical completion-sum
`L^2` variable when `lambda=C/S^2`, the affine intercept, and the tangent
chart all vary with `S`.  If this intertwining were proved, every low-CRT
cell would close, and the `H^(-2)` plateau would close through

```text
P<=D^(253/384-v/8),       B=D^(1+v).                 (4.2f)
```

The larger Farey-failure range still lies beyond this polytope.  Thus even
the correct outer square function needs a second, high-denominator input.

There is a second exact finite theorem behind the anisotropic masks.  If an
outer variable is genuinely Fourier-dual to `(e-f)/g`, Parseval and fiberwise
Cauchy improve the isotropic `sqrt(B)` operator loss to `sqrt(A)`, giving the
sharp factor

```text
sqrt(A/B).                                            (4.2g)
```

At the worst endpoint this is `D^(-1/12)`.  On the no-wrap opposite-sign
branch, an exact residue--fold identity forces curvature `>>dH/P` and lowers
the flattened ledger to `D^(55/96)`; (4.2g) would then give `D^(47/96)`, with
`D^(-1/96)` slack.

Neither Fourier variable is automatic.  The wrap label is an integral
Poisson alias, so its carrier character is identically one.  Likewise the
physical completion character is dual to `S=2Q`, not to `(e-f)/g`; explicit
remote points with different reduced error differences share the same
completion output.  Thus the finite anisotropic theorem is proved, but its
physical Bessel intertwining remains a real new theorem rather than a formal
Parseval step.  Combining Farey spacing, cubic-offset counting, and the
fixed-factor divisor count does close a nonempty part of the transverse
polytope, but the worst high-`P` cell remains above the square-root target.

### 4.2 The stationary amplitude can be transferred exactly

The amplitude issue can now be stated without hand-waving.  Put a stationary
symbol `A(h,k)` on a finite frequency torus `(Z/MZ)^2`, with normalized DFT
`Ahat(u,v)`.  The amplitude-weighted version of (2.10) is exactly

```text
S_A(alpha,beta)
 =sum_(u,v) Ahat(u,v) * 1/R sum_(j mod R)
   P_c(alpha+u/M-j*P_0/R)
   P_c(beta +v/M+j*K_0/R).                           (4.3)
```

Consequently, for triangular Fejer coefficients,

```text
|S_A|<=sum_(u,v)|Ahat(u,v)|
 min(1,1/(4*H^2*eta_(u,v)^2)),                       (4.4)
```

where `eta_(u,v)` is the shifted affine-orbit distance.  This is an exact
Fourier transference identity, not an asymptotic stationary-phase claim.

For a uniformly curved top-block stationary symbol, `Ahat` is rapidly
localized to `O(q^epsilon)` modes.  Its shifts are only `O(q^epsilon/H)`, so
the affine-height decay survives.  On one fixed normal lattice this regular,
quantitatively nonmajor sector is closed at amplitude `sqrt(q/H)=sqrt(D)`.

Away from the exact rational-stationary classes closed in Section 2.3, the
analytic obstruction is now confined to the fold.  On a curvature layer
`d`, the stationary amplitude is `sqrt(q/d)` and its DFT spreads through
`H/d` normal modes, shifting affine intercepts by `1/d`.  The exact missing
gain for this unrestricted transference argument is

```text
sqrt(H/d).                                           (4.5)
```

At the Airy transition

```text
J=(H^2/q)^(1/3)=D^(1/48),                            (4.6)
```

the ledger is

```text
Airy amplitude:              D^(49/48),
target:                      D^(24/48),
remaining amplitude loss:   D^(25/48),
Fourier spread H/J:          D^(25/24).              (4.7)
```

Thus an unweighted Wiener-norm bound for `Ahat` is insufficient.  What is
needed is a shifted-character square function showing at least a
`sqrt(d/H)` saving in the Fourier mass which can align with major affine
characters (the stronger one-aligned-shift heuristic would give `d/H`).

The exact dual work now specifies how to prove (4.1):

1. organize packet pairs by the rational tangent normal lattice (2.4);
2. use the full affine character, not only its cubic vector;
3. treat `eta<<1/H` by the packet capacity (2.13);
4. use the cyclic identity (2.10) and decay (2.12) on the other cosets;
5. transfer each approximate or irrational fold saddle to the rational
   affine-height charts without summing the short error characters
   absolutely;
6. below `P=sqrt(H)`, use (4.3)--(4.4) and an actual outer completion-sum
   character to obtain the shifted-character square-function gain;
7. above `P=sqrt(H)`, replace the unavailable `P^(-4)` decay by dispersion
   for the coupled short residue and shifted three-reciprocal condition
   (3.22)--(3.24), classifying reflected algebraic branches as major arcs;
8. square-sum in the completion variable so distinct tangent charts obey
   (4.1).

Steps 5--7 are the closest analytic bottleneck.  The exact rational sector is
closed, and the amplitude-free orbit theorem and its exact amplitude
transference are proved.  What remains is a quantitative stability theorem
for irrational/near-rational saddles, a high-denominator discrepancy theorem
past the Fejer plateau, and recovery of the explicit `D^(25/48)` Airy-layer
loss in (4.7), followed by square summation over tangent charts.

## 5. Binary status

```text
sharp fourth trace D^(1+o(1)):                         NOT PROVED;
best unconditional fourth trace:                       D^(9/8+o(1));
correct completion-sum restriction norm:               IDENTIFIED EXACTLY;
fixed-S phase-only TT* after packet deletion:           REFUTED;
Young energy masks m^2*M^3>=sqrt(D):                   CLOSED;
balanced unresolved Fejer energy core:                  U,V<D^(1/10);
stationary quartic and cubic discriminant:               CLASSIFIED;
all exact interior multiple saddles cubic:               PROVED;
full rational stationary normal lattice:                 CLASSIFIED;
affine character trivial iff physical lattice packet:    PROVED;
integral cubic implies physical packet:                  FALSE;
cyclic Fejer normal-lattice identity:                    PROVED;
amplitude-free orbit decay by eta:                       PROVED;
symmetric CRT product-grid orbit bound:                  PROVED;
remote exact rational sector, pointwise/energy core:      D^(23/48) / D^(61/144), CLOSED;
finite-DFT stationary-amplitude transference:            PROVED;
regular fixed-lattice nonmajor amplitude sector:          CLOSED;
near-rational/irrational Airy shifted-character loss:     D^(25/48);
P^(-4) CRT decay beyond P^2=H:                           FALSE;
one affine tangent capacity <=sqrt(D*min(U,V)):          PROVED;
high remote exact tangent/parallel component:             O(1) POINTS;
height-only packet-pair Cotlar decay:                     FALSE;
reflected u=0 and h=0 algebraic branches:                 D^(23/96), CLOSED;
entire central-content chart:                             D^(23/48), CLOSED;
arbitrary-content balanced/one-band axes:                 <=sqrt(A)Q^o(1), CLOSED;
all square-content charts d^2|g, uniformly in scale:       D^(23/48), CLOSED;
square content d^2|g on the transverse residual:           FALSE;
transverse arbitrary-content denominator floor:           p>>D^(77/160), PROVED;
transverse noncentral joint-rounding chart:                OPEN;
symmetric error-cusp identity and primitive normal form:  PROVED;
exact nonzero cusp label factorization:                   PROVED;
pure volume after deleting n=0 and Delta=0:              FALSE;
whole rho<<Q^(1/3) translated-tangent sector:            CLOSED;
energy-core primitive denominator p>>D^(43/144):         PROVED;
one remote point per primitive direction:                PROVED;
remote region g*p^5<=Q*(1+AB/Q)^2:                       CLOSED;
shifted three-reciprocal hard region beyond that:         OPEN;
factorable local post-peeling mask dominated by RSR:      PROVED;
auxiliary residue-character sqrt(W) Parseval:             PROVED;
anisotropic difference-character sqrt(A/B) theorem:       PROVED;
wrap/difference label equals physical Fourier variable:   FALSE;
physical completion-sum Bessel intertwining:              OPEN;
corrected remote scalar gate globally:                    OPEN;
hereditary reciprocal-strip restriction `(RSR)`:         OPEN;
packet-pair square function:                              OPEN.
```

## Reproducibility

The new identities and exponent ledgers are replayed in

```text
src/qp_coupled_cusp_fejer_inverse.py
src/test_qp_coupled_cusp_fejer_inverse.py
src/qp_dual_tangent_major_arc.py
src/test_qp_dual_tangent_major_arc.py
src/qp_fejer_s_restriction_gate.py
src/test_qp_fejer_s_restriction_gate.py
src/qp_stationary_amplitude_transference.py
src/test_qp_stationary_amplitude_transference.py
src/qp_high_primitive_packet_pair_audit.py
src/test_qp_high_primitive_packet_pair_audit.py
src/qp_approximate_tangent_character_stability.py
src/test_qp_approximate_tangent_character_stability.py
src/qp_anisotropic_outer_l2.py
src/test_qp_anisotropic_outer_l2.py
src/qp_universal_content_blowup.py
src/test_qp_universal_content_blowup.py
```

Detailed companion reports:

```text
results/ZETA23-QP-DUAL-TANGENT-NORMAL-LATTICE-AFFINE-HEIGHT-AND-CAUSTIC-CLASSIFICATION-2026-08-25.md
results/ZETA23-QP-FEJER-S-RESTRICTION-AND-PACKET-PAIR-SQUARE-FUNCTION-2026-08-25.md
results/ZETA23-QP-STATIONARY-AMPLITUDE-FOURIER-TRANSFERENCE-AND-CAUSTIC-DERIVATIVE-LOSS-2026-08-25.md
results/ZETA23-QP-SYMMETRIC-CUSP-MINOR-VOLUME-COUNTEREXAMPLE-AND-REMOTE-PRIMITIVE-GATE-2026-08-25.md
results/ZETA23-QP-REMOTE-PRIMITIVE-DIRECTION-UNIQUENESS-AND-FAREY-MODERATE-SUBRANGE-2026-08-25.md
results/ZETA23-QP-HIGH-PRIMITIVE-PACKET-SPACING-COTLAR-AND-RSR-BRIDGE-AUDIT-2026-08-25.md
results/ZETA23-QP-REFLECTED-C-MAJOR-ARC-COUNT-AND-BALANCED-OFFSET-COUNTEREXAMPLE-2026-08-25.md
results/ZETA23-QP-APPROXIMATE-TANGENT-CHARACTER-STABILITY-AND-WRAP-BARRIER-2026-08-25.md
results/ZETA23-QP-ANISOTROPIC-ERROR-DIFFERENCE-OUTER-L2-GATE-2026-08-25.md
results/ZETA23-QP-UNIVERSAL-CONTENT-BLOWUP-MULTIPLIER-AND-RESIDUAL-FAMILY-2026-08-25.md
results/ZETA23-QP-GPT7-FEJER-CORE-AND-SPECIAL-RECIPROCAL-CURVE-SYNTHESIS-2026-08-25.md
```
