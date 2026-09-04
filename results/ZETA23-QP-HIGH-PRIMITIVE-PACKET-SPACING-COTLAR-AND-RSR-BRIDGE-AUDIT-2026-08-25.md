# QP high primitive packets: exact spacing, Cotlar obstruction, and the RSR bridge

**Date:** 2026-08-25  
**Verdict:** the stronger completion-energy core makes every exact remote
rational tangent packet a singleton.  It does **not** give bounded overlap or
Cotlar decay between different packet pairs.  The cusp fraction `d/p` is only
an approximate physical tangent, and reflected high-height singleton packets
can have exactly the same completion sum.

There is nevertheless one exact positive bridge.  A hereditary mixed
completion-energy theorem (RSR) controls the local post-peeling broad kernel
whenever its ordered-pair weights factor as `z_a*y_b`: every selected broad
mask is entrywise dominated by the full completion-equality kernel.  This
bridge is a closing norm for that local kernel, not a proof of RSR or of the
global fourth-trace assembly.

The proposed thickened-CRT ledger also has a precise status.  In the range
`P^2<=H`, an **outer-L2** square-root over `W` residue layers would leave only
`D^(7/96)` after the worst Airy amplitude.  The algebra is correct, but the
square-root is false pointwise for positive layers.  Beyond `P=sqrt(H)`, the
generic CRT layer scale is `H^(-2)`, not `P^(-4)`, so the proposed
`P>P_f` tail cannot use the same normalization.

No reciprocal-strip restriction theorem or sharp four-cycle theorem is
proved here.

## 1. The energy core raises the primitive floor

Write

```text
Q=D^(33/16),       A=D*m,       B=D*M,
1<=m<=M,           m^2*M^3<sqrt(D).                  (1.1)
```

The last inequality gives

```text
m<D^(1/10),        M<D^(1/6),
A<D^(11/10),       B<D^(7/6).                        (1.2)
```

The corrected remote cusp reduction supplies

```text
p>>(Q/B)^(1/3).                                      (1.3)
```

Consequently, in the energy core,

```text
p>>D^(43/144).                                       (1.4)
```

This improves the pointwise-core floor `D^(13/48)`.  The distinction matters:
all height estimates below should use (1.4) when the target is completion
energy rather than `max_S`.

## 2. Exact parity formula and the singleton tangent sector

For a reduced remote direction `(p,d)`, `|d|<p`, the candidate symmetric
tangent is

```text
t_0=(p+d)/(2p).                                      (2.1)
```

Put

```text
chi=4  if p,d are both odd,
chi=1  otherwise.                                    (2.2)
```

Reducing `(p+d)/(p-d)` and applying the exact `lambda=1/4` tangent formula
gives the primitive direction

```text
(R,-P_-,P_+),
R   =(p^2-d^2)^2/chi,
P_- =p^2*(p-d)^2/chi,
P_+ =p^2*(p+d)^2/chi.                                (2.3)
```

There is no other gcd loss.  In a fixed compact collar all three positive
steps are comparable to `p^4`.  Thus (1.4) gives

```text
R>>D^(43/36),       min(R*P_-,R*P_+)>>D^(43/18).     (2.4)
```

At `C=Q^2,S=2Q`, the exact tangent point has

```text
a_0=Q*(1+d/p),       b_0=Q*(1-d/p).                  (2.5)
```

Along the exact tangent line, direct multiplication gives

```text
a*v-C       =-(a-a_0)^2/(1+d/p)^2,
(S-a)*w-C   =-(a-a_0)^2/(1-d/p)^2.                  (2.6)
```

Hence the allowed first coordinates lie in an interval of radius

```text
X=min((1+d/p)*sqrt(A),(1-d/p)*sqrt(B)).              (2.7)
```

Integral points on a genuine lattice tangent have first coordinates spaced
by `R`.  If `R>2X`, the packet contains at most one point.  In the energy
core,

```text
R/sqrt(A)>>D^(43/36-11/20)=D^(29/45),               (2.8)
```

so the criterion holds with a large power margin.

> **Exact high-tangent sector theorem.** For all sufficiently large `D`,
> every exact rational lattice tangent associated with a surviving remote
> primitive height contains at most one point in the two product bands.

For a line merely parallel to this tangent, the affine intercept can move
the vertex of the product quadratic.  One no longer gets a singleton, but
each connected product-band component has

```text
O(1+sqrt(A/(R*P_-)))=O(1)                            (2.9)
```

points.  Thus high height proves bounded occupancy of one fixed affine line.
It says nothing yet about the number or mutual position of parallel
intercepts.

## 3. The approximate-primal transfer is not automatic

For a physical symmetric-cusp point, the first coordinate corresponds to

```text
t_phys=(Q+y)/(2Q).                                   (3.1)
```

The exact primitive equation is

```text
p*y-Q*d=n.                                           (3.2)
```

Therefore

```text
t_phys-t_0=n/(2Qp).                                  (3.3)
```

The remote sector has `n!=0`.  Equation (3.3) does not say that the physical
point can never lie on the extended rational tangent; it says that membership
and the affine intercept are additional facts which do not follow from the
primitive slope.  The exact tangent may not meet the integer lattice at all,
and a physical point can instead lie on a different parallel intercept.

This is the precise gap in the tempting argument

```text
large p => large R => all remote physical points are separated.          (3.4)
```

Only the first implication is formal.  Even after assigning every point to
an `O(1)` affine packet, global packet-pair overlap remains uncontrolled.

## 4. Exact reflected obstruction to height-based Cotlar decay

There is an infinite genuine product-window family showing that the missing
global step is not cosmetic.  Let `p>d>=1` be coprime and put

```text
L_0=p^2-d^2,          Q=p*L_0+1,       y=d*L_0,
r=d^2*(p-d),          s=d^2*(p+d).                   (4.1)
```

Then the two product errors are exactly

```text
e=r,                  f=s.                           (4.2)
```

The primitive cusp data are

```text
rho=2*p*d^2,          kappa=2*d^3,
g=2*d^2,              n=-d,
T=-2*d^2,             L=-8*d^6.                     (4.3)
```

Thus `n*L*kappa!=0`: this is genuinely in the remote nonmajor sector.  Its
reflection is

```text
(y,r,s) -> (-y,s,r),                                 (4.4)
```

and has primitive direction `(p,-d)`.  Both points fit the symmetric width
`max(r,s)`.  Their first coordinates satisfy

```text
(Q+y)+(Q-y)=2Q.                                      (4.5)
```

For fixed `d` and `p->infinity`,

```text
Q=p^(3+o(1)),       D=Q^(16/33)=p^(16/11+o(1)),
max(|e|,|f|)=p^(1+o(1))<D,
p=D^(11/16+o(1)),   R=D^(11/4+o(1)).                (4.6)
```

So these are arbitrarily high primitive points in the central energy mask
`m=M=1`.  Nevertheless the two ordered singleton packet pairs

```text
delta_(Q+y)*delta_(Q-y),
delta_(Q-y)*delta_(Q+y)                              (4.7)
```

are identical: both equal `delta_(2Q)`.  Their normalized cross Gram is one,
independently of `R`.

This does not disprove a `q^o(1)` overlap theorem; it supplies only a
two-fold collision.  It does prove that no off-diagonal Cotlar coefficient
can decay merely as a function of primitive height or direction separation.
Any global theorem must count/classify conjugate completion collisions or
use an outer norm in which they are harmless.

There is also a small full-integer diagnostic.  At

```text
Q=1009,       A=B=29,       |y|<=200,                (4.8)
```

the remote points have

```text
y:     -144  -126  -100   100   126   144
p:        7     8    10    10     8     7
d:       -1    -1    -1     1     1     1.           (4.9)
```

All six ordered reflection pairs land at displacement sum zero.  The maximum
ordered representation number is six and the additive energy of these six
displacements is exactly `90`.  Every associated exact tangent step is much
larger than `sqrt(29)`.

### 4.1 The integer-`c` branch is divisor-major

The family (4.1) has an exact integer generalization.  Put

```text
L_0=p^2-d^2,          Q=p*L_0+c,       y=d*L_0,
r=d^2*(p-d),          s=d^2*(p+d).                   (4.10)
```

Then

```text
e=c*r,                f=c*s,
n=-c*d,               T=-2*c*d^2,
L=-8*c*d^6.                                           (4.11)
```

Thus `c=0` is major and every `c!=0` remains a reflected remote collision.
For fixed `Q,c`, however,

```text
Q-c=p*(p-d)*(p+d).                                   (4.12)
```

Once a divisor `p|Q-c` is chosen, `d` must satisfy

```text
d^2=p^2-(Q-c)/p.                                     (4.13)
```

Hence a fixed `c` has only `Q^o(1)` representations.  In a dyadic
`P=D^pi` block, the remote bound `|y|>>Q^(2/3)` gives

```text
d>>Q^(2/3)/P^2.                                      (4.14)
```

For a reflected pair the narrower band is seen after swapping, so
`|c|d^2P<<A`.  The number of possible integer `c` is therefore

```text
Z_pair<<1+A*P^3/Q^(4/3).                             (4.15)
```

Divisor enumeration proves

```text
# {integer-c reflected branch at P}
 <<(1+A*P^3/Q^(4/3))*Q^o(1).                         (4.16)
```

Writing `A=D^(1+u)`, (4.16) fits the `sqrt(A)` packet budget whenever

```text
pi<=3/4-u/6.                                         (4.17)
```

In particular the natural family `p=Q^(1/3+o(1))=D^(11/16+o(1))` costs

```text
D^(u+5/16+o(1))<D^((1+u)/2)                         (4.18)
```

throughout the energy core.  The displayed reflected counterexample is
therefore a genuine obstruction to height-based Cotlar decay, but this
specific algebraic branch is affordable by divisor enumeration.

This does **not** classify all reflected points.  The ansatz (4.10) imposes
the special relations `g=2d^2` and `y=d(p^2-d^2)`.  The `Q=1009` fixture
already contains a reflected point `(p,d,y,g)=(10,1,100,2)` with
`y!=d(p^2-d^2)`.  Allowing an additional displacement `t` gives the wider
exact family.  To avoid confusing its content multiplier with the balanced
height below, call that multiplier `j`:

```text
Q=j*p*(p^2-d^2)+c,       y=j*d*(p^2-d^2)+t,
g=2*j*d^2,                                               (4.19)

e=j*d^2*(p-d)*(c+t)-2*j*d*(p^2-d^2)*t-t^2,
f=j*d^2*(p+d)*(c-t)-2*j*d*(p^2-d^2)*t-t^2,
n=p*t-c*d,              T=-2*c*d^2.                    (4.20)
```

The cases `(j,c,t)=(1,19,1),(2,1,0),(3,1,0)` recover the positive
`y=100,126,144` fixture points.  Thus “all high-direction collisions are
small-`c` branches” is false as an algebraic classification; further
control of `j,t` is needed.

### 4.2 Balanced-height and one-band divisor peels

There is a more useful normal form on the central-content branch
`g=2d^2`.  Put

```text
ell=p^2-d^2,      c=Q-p*ell,      u=y-d*ell,
H_0=d*c-2*p*u.                                      (4.21)
```

Direct expansion, with no approximation, gives

```text
e+u^2=d*(p-d)*(H_0-d*u),
f+u^2=d*(p+d)*(H_0+d*u),                            (4.22)

n=p*u-c*d,             T=-2*c*d^2,
(e+u^2)*(f+u^2)=d^2*ell*k,
k=(H_0-d*u)*(H_0+d*u).                              (4.23)
```

First take `H_0=0`.  Since `(p,d)=1`, the identity `d*c=2p*u`
implies `p|c`, hence `p|Q`.  Writing `c=p*lambda` also gives
`2u=d*lambda`.  Moreover

```text
e=-d^2*(p-d)*u-u^2,       f=d^2*(p+d)*u-u^2.        (4.24)
```

If both errors are at most `B`, subtraction gives
`p*d^2*|u|<=B`.  A remote point has `u!=0`, so `p*d^2<=B`; also
`|c|<=2B` and therefore `p>=(Q-2B)^(1/3)`.  At fixed `Q`, divisor
enumeration now proves

```text
# {H_0=0 central reflected points}
 <=2*tau(Q)*(1+sqrt(B/(Q-2B)^(1/3))).                (4.25)
```

In the energy core the right side is

```text
D^(23/96+o(1)),                                      (4.26)
```

well below the `sqrt(A)` packet budget.  This peel catches an important
counterexample to the small-`c` criterion: for `d=1`, fixed nonzero `u`,

```text
c=2*p*u,       Q=p*(p^2-1)+2*p*u,       y=p^2-1+u,  (4.27)
e=-u*(p+u-1),             f=u*(p+1-u).
```

Here the physical band costs only `O(p*|u|+u^2)`, whereas the small-`c`
quantity `|c|p` is `2p^2|u|`.  Thus small `c` is not the correct invariant,
but the family is still divisor-major because `H_0=0` forces `p|Q`.

There is a second completely removable branch.  If `k=0`, then
`H_0=epsilon*d*u` for `epsilon=+1` or `-1`.  Equation (4.22) says that one
error is exactly `-u^2`; after reflecting, that error occurs in the narrow
`A` band.  Thus a reflected pair admitted by both product bands has
`|u|<=sqrt(A)`.  Also

```text
d*(c-epsilon*u)=2*p*u,       p|(Q-epsilon*u).        (4.28)
```

For fixed `(epsilon,u)` and divisor `p|(Q-epsilon*u)`, the possible `d`
are roots of the cubic

```text
d^3+d*((Q-epsilon*u)/p-p^2)-2u=0,                   (4.29)
```

so there are at most three.  Consequently

```text
# {central reflected pairs with k=0}
 <=3*sum_{epsilon=+-1} sum_{0<|u|<=sqrt(A)}
       tau(|Q-epsilon*u|)
 <<sqrt(A)*Q^o(1).                                  (4.30)
```

This is a closing sector theorem for `k=0`.  What remains unclassified on
the exact central-content reflected locus is `k!=0`; (4.23) is an exact
factorization for that residual problem, not yet a bound for it.

The companion report
`ZETA23-QP-REFLECTED-C-MAJOR-ARC-COUNT-AND-BALANCED-OFFSET-COUNTEREXAMPLE-2026-08-25.md`
proves the stronger asymmetric one-point version of (4.30), without assuming
that the reflected partner obeys the same mask, by a fixed-`d` divisor
factorization of `8Q-3*epsilon*d^3`.

## 5. What elementary Farey spacing proves

The exact cusp equations imply

```text
rho=g*p
   =2Q*y^2/(Q^2-y^2)
    +(Q*sigma-g*y*n)/(Q^2-y^2).                     (5.1)
```

In a fixed collar, the last term is `O(B/Q)=o(1)`.  Thus, for fixed `(y,p)`,
there is at most one possible content `g` once `Q` is large.  Also

```text
|y-Q*d/p|<=2B/(g*p).                                 (5.2)
```

In a dyadic cell `p~P,g~G`, a direct global Farey count gives the elementary
majorant

```text
#cell <<P^2+B*P/G.                                   (5.3)
```

To put the first term inside the square-root packet budget using only (5.3)
would require

```text
P<=A^(1/4)<=D^(11/40).                               (5.4)
```

But the remote energy core starts at

```text
P>>D^(43/144),
43/144-11/40=17/720.                                (5.5)
```

This is an exact `17/720` near miss for the naive global Farey route.

A stronger use of the continuous coordinate proves direction uniqueness and
the complete moderate theorem

```text
g*p^5<=Q  =>  O(Q^epsilon) remote points.            (5.6)
```

Indeed, two points in a dyadic cell have Farey spacing `Q/P^2`, while
`rho~GP` confines one sign component to length `O(sqrt(QGP))`, giving

```text
N(G,P)<<1+sqrt(G*P^5/Q).                             (5.7)
```

The proof and its two `o(1)` margins are recorded in
`ZETA23-QP-REMOTE-PRIMITIVE-DIRECTION-UNIQUENESS-AND-FAREY-MODERATE-SUBRANGE-2026-08-25.md`.
The high hard region `GP^5>Q` remains.

## 6. Audit of the thickened-CRT square-root proposal

In the hard Farey-valid range, an approximate slope thickens the exact normal
congruence to roughly

```text
W_+=1+H*B*P^3/(Q*G)                                 (6.1)
```

residue layers.  The factor `P^3` is consistent with multiplying the slope
uncertainty `B/(QGP)` by the primitive congruence scale `H*P^4`.
Furthermore,

```text
W/R << H*B/(Q*G*P)<<1                               (6.2)
```

throughout the remote collar, so the thickening does not wrap around the
whole modulus.

Assume first that `P^2<=H`, where one shifted CRT layer has normalized Fejer
scale `P^(-4)`.  Suppose an actual outer square function gave

```text
|| sum_(|ell|<=W) T_(p,d,ell) ||_X
 <<q^epsilon*P^(-4)*sqrt(W)*input_norm.              (6.3)
```

Here `X` must be a genuine `L2` norm in a variable dual to `ell`; (6.3) is
not asserted pointwise.  Summing occupied directions absolutely and using
(5.7), the hard condition makes the square-root term dominate, and

```text
N(G,P)*P^(-4)*sqrt(W)
 <<sqrt(G*P^5/Q)*P^(-4)
   *sqrt(H*B*P^3/(Q*G))
 =sqrt(H*B)/Q.                                       (6.4)
```

The cancellation of `G,P` is exact.  At the worst energy endpoint,

```text
sqrt(H*B)/Q=D^(-91/96).                              (6.5)
```

Multiplying by the worst Airy amplitude `D^(49/48)` leaves

```text
D^(49/48-91/96)=D^(7/96).                           (6.6)
```

The `1` in `W_+` is covered by the exact weighted hard calculation
`D^(73/240)`.  Thus (6.3), with the correct physical outer norm and amplitude
stability, would have ample room.

### 6.1 Exact auxiliary residue-character L2 theorem

The square root itself can be proved exactly in an auxiliary character.  Let
`c_h=(H-|h|)/H^2` be the normalized triangular coefficients and, for one
primitive direction `(R,-P_0,K_0)`, define

```text
O_ell(alpha,beta)
 =sum_(k*K_0-h*P_0==ell mod R)
   c_h*c_k*e(h*alpha+k*beta).                        (6.7)
```

The shifted congruence detector gives

```text
O_ell
 =1/R sum_(j mod R) e_R(-j*ell)
   P_H(alpha-j*P_0/R)*P_H(beta+j*K_0/R).             (6.8)
```

Since the normalized Fejer polynomial `P_H` is nonnegative, the absolute
value of (6.8) is bounded by the unmodulated orbit.  In the symmetric chart,

```text
|O_ell|<=M_H(p,d)
 :=B_H(r^2)*B_H(s^2)                                (6.9)
```

for every residue `ell` and every intercept pair.  Here `r/s` is the reduced
tangent parameter and `B_H` is the exact grid maximum from the symmetric CRT
theorem.

For a set `I` of residue layers introduce a genuinely new cyclic character
`x` and put

```text
F_I(x)=sum_(ell in I) O_ell*e_R(x*ell).              (6.10)
```

Discrete Parseval proves the exact identity

```text
1/R sum_(x mod R)|F_I(x)|^2
 =sum_(ell in I)|O_ell|^2
 <=|I|*M_H(p,d)^2.                                  (6.11)
```

Therefore

```text
||F_I||_(L2_x)<=sqrt(|I|)*M_H(p,d).                 (6.12)
```

This is a rigorous finite theorem.  In a fixed compact collar its two sharp
regimes are

```text
P^2<=H:       M_H(p,d)<<P^(-4),
P^2> H:       M_H(p,d)<<H^(-2).                     (6.13)
```

No `P^(-4)` continuation exists past the second line.

What is **not** proved is that the auxiliary `x` in (6.10) is the physical
completion-sum Fourier variable.  The minimal missing statement is a Bessel
intertwining: after the physical stationary decomposition, the residue-layer
characters `psi_ell(S)` must satisfy

```text
||sum_ell a_ell*psi_ell(S)||_(ell2_S)
 <<q^o(1)*(sum_ell|a_ell|^2)^(1/2),                 (6.14)
```

uniformly under the selected weights and stationary symbol.  Equivalently,
the physical completion norm must factor through (6.10) with bounded
multiplicity.  The standard identity
`||z*y||_2^2=int |zhat|^2|yhat|^2` does not supply (6.14) after rational
stationary partitioning: `lambda=C/S^2`, the intercepts, and even the tangent
chart vary with `S`.  Thus (6.11) is proved, while the completion-sum
intertwining (6.14) is the exact remaining identity.

### 6.2 Why the square root is not pointwise

For a primitive cyclic linear form on `(Z/RZ)^2`, place flat mass `1/R^2`
on every pair and group by its residue `ell`.  Every residue layer then has
mass exactly `1/R`.  At the zero outer character, `W` selected positive
layers sum to

```text
W/R,                                                 (6.15)
```

not `sqrt(W)/R`.  This is the exact finite-group obstruction to obtaining
(6.3) by Cauchy or the congruence detector alone.

If an independent character `x` is present, Parseval does give

```text
||sum_ell O_ell*e(ell*x)||_(L2_x)
  =(sum_ell |O_ell|^2)^(1/2)
  <<sqrt(W)*P^(-4).                                  (6.16)
```

The missing bridge is therefore precise: identify the residue-dual character
with an outer variable that the fourth trace genuinely averages in `L2`, and
show that arbitrary selected weights and the stationary symbol do not collapse
that average to `x=0`.  Without this identification, (6.3) is a new theorem,
not a consequence of cyclic CRT.

### 6.3 Exact dyadic exponent polytope

Write

```text
A=D^(1+u),       B=D^(1+v),
G=D^gamma,       P=D^pi,                             (6.17)
0<=u<=v,         2u+3v<1/2.
```

The thickening exponent and the Farey-valid occupied-direction exponent are

```text
omega=(v+3*pi-gamma)_+,
nu=(gamma+5*pi-33/16)_+/2.                          (6.18)
```

Farey validity is

```text
pi<=17/16+gamma-v.                                  (6.19)
```

The region `gamma+5*pi<=33/16` is already closed by the scalar moderate
theorem.  In the hard region, the exact auxiliary-L2 exponent after the worst
Airy amplitude is

```text
E_2=49/48+nu+layer+omega/2,                          (6.20)

layer=-4*pi       if pi<=17/32,
layer=-17/8       if pi> 17/32.                     (6.21)
```

The corresponding proved pointwise exponent replaces `omega/2` by `omega`.
The target is `E<=1/2`.

For nontrivially thickened, Farey-valid cells (`omega>0`), (6.20) simplifies
exactly as follows.

```text
pi<=17/32:
    E_2=v/2-1/96.                                   (6.22)

pi>17/32:
    E_2=4*pi+v/2-205/96.                            (6.23)
```

Consequently, if the completion intertwining (6.14) is available, every
low-CRT hard cell closes, and the true `H^(-2)` plateau closes by this ledger
precisely through

```text
17/32<pi<=253/384-v/8.                              (6.24)
```

Within the present pointwise theory the high plateau closes only in the
following two polytopes:

```text
omega<=0:     gamma+5*pi<=253/48,                   (6.25)

omega>0:      11*pi-gamma+2v<=253/48.               (6.26)
```

Equations (6.24)--(6.26) are sharp for the stated ingredients: the scalar
direction count, the exact CRT layer envelope, and respectively square-root
or triangle summation over layers.  They do not assert that the approximate
stationary reduction itself has already been transferred to the physical
fourth trace.

### 6.4 The `P>P_f` normalization changes

Put

```text
P_f=Q*G/B.                                           (6.27)
```

The energy core gives

```text
P_f>=Q/B=D^(43/48),
sqrt(H)=D^(17/32),
P_f/sqrt(H)>=D^(35/96).                              (6.28)
```

Thus the whole exact-CRT range `P^2<=H` lies below `P_f`.  There is no
`P>P_f` tail for nonzero **exact** stationary aliases.

For approximate layers beyond `sqrt(H)`, the uniform shifted-layer envelope
is

```text
(P^(-2)+H^(-1))^2 asymp H^(-2),                     (6.29)
```

not `P^(-4)`.  Formally retaining `P^(-4)` and using the trivial occupied
count `N<=sqrt(QGP)` gives

```text
N*P^(-4)*sqrt(W)=sqrt(HB)*P^(-2),                   (6.30)
```

and, at `P=P_f`, the advertised final exponent `D^(11/32)`.  The algebra in
(6.12) is correct; its `P^(-4)` premise is not supplied by the CRT theorem in
this range.  Approximate high-denominator stationary points require a separate
near-alias sparsity theorem or a reorganization by frequency pairs.  They
cannot be closed by extrapolating (6.3).

Using the correct plateau and the scalar failure-range count

```text
N<=min(P^2,sqrt(QGP))                                (6.31)
```

in (6.20) leaves every `P>P_f` cell above the square-root target.  This can
be seen without optimization software.  The failure condition is
`pi>17/16+gamma-v`; it forces `omega>0` and the high plateau.  It also gives

```text
3*pi-(33/16+gamma)>2*pi-1-v>9/8-3v>0.              (6.31a)
```

Thus `sqrt(QGP)` is always the smaller term in (6.31); the `P^2` count must
not be used on this face.  The resulting exponent is

```text
E_fail=-7/96+2*pi+v/2
      >197/96-(3/2)*v>173/96.                      (6.31b)
```

This is far above `1/2`.  Thus the Farey-failure range is a genuine residual
face of this method, not merely a slightly weaker exponent.

### 6.5 Coarse frequency resolution does not form one physical packet

One might try to merge every `P>sqrt(H)` direction into a Dirichlet chart of
denominator at most `sqrt(H)`.  Frequencies of size `H` resolve normalized
slope only to `1/H`.  A physical tangent packet of product width `A` has
normalized slope radius

```text
delta_phys~sqrt(A)/Q.                                (6.32)
```

Therefore one frequency chart contains potentially

```text
(1/H)/delta_phys
 =Q/(H*sqrt(A))
 =D^((1-u)/2)                                       (6.33)
```

distinct physical packet locations.  Resolving them by Farey denominators
would require

```text
P_phys~sqrt(Q/sqrt(A))
      =D^(25/32-u/4),                               (6.34)
```

whereas the exact-frequency cutoff is only

```text
sqrt(H)=D^(17/32).                                   (6.35)
```

The denominator gap is `D^((1-u)/4)`.  Hence resolution renormalization
merely repackages a power-sized stack of tangent packets; proving that this
stack has a square function is again the missing RSR/completion-intertwining
theorem.  The integer-`c`, balanced-height, and `k=0` divisor peels from
Sections 4.1--4.2 remove explicit conjugate branches, but they do not
control the residual `k!=0` charts in the stack.

## 7. Conditional packet-pair theorem and the exact missing factor

Let

```text
z=sum_i z_i,       y=sum_j y_j                      (7.1)
```

be disjoint packet decompositions.  Suppose every packet has at most `C`
points on the smaller side and every output sum belongs to at most `L`
packet-pair sumsets.  Pointwise Cauchy and Young give

```text
||sum_(i,j) z_i*y_j||_2^2
 <=L*sum_(i,j)||z_i*y_j||_2^2
 <=C*L*||z||_2^2*||y||_2^2.                         (7.2)
```

High primitive spacing proves `C=O(1)` for an exact/parallel high-direction
packet.  It does not prove `L=q^o(1)`.  The reflection family has `L>=2` with
cross Gram one at arbitrarily large height; a large collection of reflected
pairs would make `L` exactly the unresolved remote completion multiplicity.

Thus the hoped-for Cotlar argument has not reduced the theorem below RSR.
It has isolated the remaining factor correctly: an arithmetic bound on
packet-pair output multiplicity, or an outer square function which controls
the same collisions.

## 8. Exact bridge from RSR to the local post-peeling broad norm

Let `a_i,b_j` be two reciprocal-strip projections and let `z_i,y_j` be
arbitrary complex weights.  On ordered-pair space put

```text
w_(i,j)=z_i*y_j.                                     (8.1)
```

Let `M_(ij,kell)` be any selected mask with

```text
|M_(ij,kell)|<=1,
M_(ij,kell)!=0 => a_i+b_j=a_k+b_ell.                (8.2)
```

Then entrywise absolute values give the exact domination

```text
|sum_(ij,kell) conjugate(w_ij)*M_(ij,kell)*w_kell|
 <=sum_S (sum_(a_i+b_j=S) |z_i|*|y_j|)^2
 =|| |z|*|y| ||_2^2.                                (8.3)
```

Consequently the hereditary mixed RSR estimate

```text
||z*y||_2^2
 <<sqrt(D*min(U,V))*q^o(1)*||z||_2^2*||y||_2^2      (8.4)
```

applied to the nonnegative sequences `|z|,|y|` proves every factorable
post-peeling submask satisfying (8.2).  For the local broad kernel in the
error-labelled reduction, take `z=y`; its broad and peel indicators only
delete completion-equality entries.  Equation (8.3) then gives exactly the
desired local post-peeling quadratic-form target.

This is stronger than proving the unmasked complex convolution alone: the
absolute-value version automatically survives arbitrary pair-of-pair
deletions.  It still relies on the point-pair coefficient factoring as
`z_i*y_j`.

## 9. Remaining assembly gaps

The local domination (8.3) does not by itself identify the whole original
fourth trace with one RSR form.  The remaining checks are:

1. prove RSR, or the equivalent hereditary flat mixed-energy theorem, in the
   hard remote sector;
2. identify a genuine outer `L2` residue character before using the
   thickened-CRT square root;
3. transfer the original colour/carrier coefficients to point weights with
   the required `l2` normalization in every dyadic amplitude and phase bin;
4. verify that the second physical tensor introduces no nonfactorable pair
   weights.  A general pair mask or vector lift need not be controlled by a
   scalar RSR theorem;
5. sum over physical endpoints/centres `C=T/x` without a polynomial
   participation loss or cross-centre coherence;
6. recombine broad/narrow, tangent, curvature, singleton, and peeled sectors
   without double counting, and retain the established smooth scalar-kernel
   bounds;
7. handle approximate high-denominator stationary layers and the near-fold
   amplitude without extending the exact `P^(-4)` CRT weight past its support.

These are assembly requirements, not claims that the local RSR bridge is
false.  For the literal factorable broad kernel at one fixed centre, (8.3)
is complete.

## 10. Binary status

```text
energy-core primitive floor p>>D^(43/144):           PROVED;
exact tangent parity and R~p^4 formula:               PROVED;
one exact high rational tangent is singleton:         PROVED;
one fixed parallel packet has O(1) occupancy:         PROVED;
approximate cusp slope automatically lies on it:      NOT PROVED;
height alone gives packet-pair Cotlar decay:           FALSE;
infinite genuine reflected high-height collision:     PROVED;
integer-c reflected branch formulas/divisor bound:    PROVED;
integer-c branch exhausts reflected collisions:       FALSE;
balanced-height H_0=0 reflected branch:               CLOSED;
central reflected one-band branch k=0:                CLOSED;
central reflected residual branch k!=0:               OPEN;
finite Q=1009 sixfold collision / energy 90:           VERIFIED;
naive global Farey closure misses by 17/720:           PROVED;
moderate remote region g*p^5<=Q:                      CLOSED (companion);
auxiliary residue-character Parseval/sqrt(W):          PROVED;
auxiliary character equals completion-sum Fourier:     OPEN;
thickened CRT physical ledger in P^2<=H:               CONDITIONAL;
pointwise sqrt(W) character bound:                    FALSE IN GENERAL;
high plateau conditional boundary (6.24):              DERIVED;
high plateau pointwise polytopes (6.25)--(6.26):       DERIVED;
P>Pf estimate with continued P^(-4) weight:           UNJUSTIFIED;
coarse sqrt(H)-denominator chart is one packet:        FALSE;
factorable local post-peeling mask <= absolute RSR:   PROVED;
RSR / packet-pair square function:                    OPEN;
global fourth-trace assembly:                         OPEN;
sharp four-cycle bound:                               NOT PROVED.
```

The parity formulas, exponent ledgers, reflected family, finite fixture,
pointwise cyclic obstruction, and factorable-mask domination are replayed in

```text
src/qp_high_primitive_packet_pair_audit.py
src/test_qp_high_primitive_packet_pair_audit.py
```
