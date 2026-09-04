# Coherent microcluster phase transport and the broad-aperture conditioning wall

Status: exact fixed-width Paley--Wiener theorem, fixed-degree endpoint/Gabor
transfer, and an exact Hardy--Blaschke conditioning bound, 2026-08-12.  The
reciprocal-separation phase-flip cluster is defeated by one coherent state,
with every mixed term retained.  The theorem is uniform for a bounded
`L`-rescaled ordinate/depth cluster, even if that cluster contains `O(L)`
pairs.  It does not isolate an arbitrary unit-width collateral list and does
not prove a zero-free strip.

## 1. Verdict

Positive averaging over packet separations is not the only response to the
phase-flip counterconfiguration.  A coherent packet can implement a
finite-band **virtual translation**.

Let the selected packet separation be

```text
D=d*L,                 0<d<1,                       (1.1)
```

and let the selected depth `alpha` stay in a fixed compact subset of
`(0,1/2)`.  For arbitrary fixed `Lambda,C<infinity`, consider any finite
collateral list

```text
beta_j=alpha-lambda_j/L,      0<=lambda_j<=Lambda,
delta_j=c_j/L,                |c_j|<=C.              (1.2)
```

The cardinality of the list is unrestricted in the analytic theorem.  In
particular it may be the full `O(L)` allowance of the present microscopic
zero count.

There is a real normalized fixed-width packet `q_L` such that

```text
F_q(alpha)+F_q(-alpha)=0,                            (1.3)

Q_(alpha,0)(q_L)
 <=-c_0*exp(alpha*D)/L^(2r+2),                       (1.4)

Q_(beta_j,delta_j)(q_L)
 <=-c_1*exp(beta_j*D)/L^(2r+2)       for every j,    (1.5)
```

where `r,c_0,c_1>0` depend only on the fixed compact parameters, not on `L`
or on the number and spacing of the collateral pairs.  Thus the target
retains

```text
exp(alpha*d*L-O(log L))=X^(alpha*d-o(1))             (1.6)
```

negative carrier, while every pair in the whole microscopic rectangle has
the favorable sign.

This includes both members of the normalized phase-flip screen

```text
delta=+/-pi/D,
beta=alpha-L^(-2),                                  (1.7)
```

and it includes an `O(L)` chain of distinct simple pairs in any bounded
`(lambda,c)` rectangle.  The positive-separation counterconfiguration
therefore obstructs positive mixtures, but it is **not** a no-go theorem for
coherent superpositions.

The escape has a sharp scope boundary.  Exact annihilation of a broad list
has a Blaschke-product loss.  With the current Bellotti--Wong endpoint-error
budget and both ordinate signs available, even the exceptional-only
root-per-pair ledger
slightly exceeds the entire selected exponent.  A proposed repair using a
widening smooth packet and the same differential phase filter has no
near/far aperture overlap.  These facts leave arbitrary unit-width
collateral isolation open.

## 2. The exact mixed-term identity

For a packet `q` supported in the physical interval, put

```text
F_q(z)=integral q(t)*exp(z*t)dt.                     (2.1)
```

After demodulation by the selected ordinate, the complete reflected-pair
kernel at depth `beta` and relative ordinate `delta` is

```text
K_(beta,delta)(t,s)
 =(2/L^2)*exp(-i*delta*(t-s))*cosh(beta*(t-s)).       (2.2)
```

Expanding the hyperbolic cosine, without deleting same-packet or reverse
terms, gives the exact rank-two identity

```text
Q_(beta,delta)(q)
 :=integral integral q(t)*conj(q(s))*K(t,s)dt ds

 =(2/L^2)*Re(
       F_q(beta-i*delta)
       *conj(F_q(-beta-i*delta))).                  (2.3)
```

In particular

```text
Q_(alpha,0)(q)
 =(1/(2*L^2))*(|F_q(alpha)+F_q(-alpha)|^2
              -|F_q(alpha)-F_q(-alpha)|^2).         (2.4)
```

Equation (1.3) is exactly the selected positive-row quotient, and on that
quotient

```text
Q_(alpha,0)(q)=-(2/L^2)*|F_q(alpha)|^2.              (2.5)
```

All coherent cross terms among all packet components are already contained
in the products in (2.3).  No diagonal ensemble or random-phase deletion is
used below.

## 3. A finite-degree virtual translation

Choose a nonzero real nonnegative even

```text
phi in C_c^infinity((-w/2,w/2))                     (3.1)
```

with fixed `w`, and write

```text
Phi(z)=integral phi(u)*exp(z*u)du.                   (3.2)
```

After shrinking the fixed packet supports if necessary, the translates by
`+/-D/2` lie strictly inside the physical interval.

Let

```text
S={-lambda-i*c: 0<=lambda<=Lambda, |c|<=C}.          (3.3)
```

Polynomial approximation on this fixed compact set supplies a real
polynomial `p` of some fixed degree `r`, with `p(0)=1`, such that

```text
sup_(s in S) |p(s)-exp(-d*s)|<1/8.                  (3.4)
```

Nothing deep is needed: a sufficiently long Taylor polynomial for
`exp(-d*s)` works.  Define the right filtered packet and the unfiltered left
packet by

```text
R_L(t)=p(L*(-partial_t-alpha))*phi(t-D/2),
ell_L(t)=phi(t+D/2).                                 (3.5)
```

Integration by parts is exact because `phi` is compactly supported:

```text
F_(R_L)(z)
 =exp(z*D/2)*Phi(z)*p(L*(z-alpha)),

F_(ell_L)(z)=exp(-z*D/2)*Phi(z).                    (3.6)
```

Choose the real scalar

```text
a_L=[F_(R_L)(alpha)+F_(R_L)(-alpha)]
    /[F_(ell_L)(alpha)+F_(ell_L)(-alpha)]           (3.7)
```

and put

```text
q_L^0=R_L-a_L*ell_L,
q_L=q_L^0/||q_L^0||_2.                              (3.8)
```

Then (1.3) holds exactly.  Since `p(0)=1`, while
`p(-2*alpha*L)=O(L^r)`, one has

```text
a_L=1+O(L^r*exp(-alpha*D)),
||q_L^0||_2=Theta(L^r),                             (3.9)

F_(q_L)(alpha)
 =(1+o(1))*exp(alpha*D/2)*Phi(alpha)/Theta(L^r).     (3.10)
```

Equations (2.5) and (3.10) prove (1.4).

Now take one collateral parameter from (1.2), and set

```text
z_+=beta-i*delta,
z_-=-beta-i*delta,
s=L*(z_+-alpha)=-lambda-i*c.                        (3.11)
```

The right packet dominates `F(z_+)`, and the left packet dominates
`F(z_-)`.  The two discarded endpoint contributions have relative size

```text
O(L^r*exp(-beta*D)).                                (3.12)
```

Because `phi` is real and even,

```text
conj(Phi(-beta-i*delta))=Phi(beta-i*delta).          (3.13)
```

Therefore (2.3), before the common positive normalization, has leading
factor

```text
-exp(beta*D)*Re[
   exp(-i*c*d)*p(-lambda-i*c)*Phi(beta-i*delta)^2]. (3.14)
```

By (3.4),

```text
Re[exp(-i*c*d)*p(-lambda-i*c)]
 >=exp(d*lambda)-1/8>=7/8.                          (3.15)
```

Uniformly on the fixed rectangle,

```text
Phi(beta-i*delta)^2=Phi(alpha)^2*(1+O(1/L)).         (3.16)
```

Equations (3.12)--(3.16) prove (1.5).  Notice that the
`exp(-i*c*d)` phase which created the target-only screen has been canceled
coherently by `p(-lambda-i*c)`.  The factor `exp(d*lambda)` also compensates
the microscopic depth drop.

The operator in (3.5) is a finite coherent divided difference.  Each
derivative can be obtained as a limit of translated copies of the same
packet, and a sufficiently fine finite difference preserves the strict
margin in (3.15).  Thus the construction may be written as an ordinary
finite superposition of nearby packet centers.  Formula (2.3), rather than
a diagonal surrogate, retains every resulting mixed `D,D'` term.

## 4. The phase-flip and near-collision corollaries

For (1.7),

```text
lambda=L*(alpha-beta)=1/L,
c=+/-pi/d.                                          (4.1)
```

Both points lie in one fixed rectangle (3.3).  A single real polynomial
handles both signs because it has real coefficients.  Hence the exact
three-pair form consisting of the selected pair and the two phase-flipped
collaterals is strictly negative on `q_L` at carrier exponent
`alpha*d`; on the old two-packet vector it was strictly positive.

More generally, place `M_L<=C_0*L` distinct simple collateral pairs at
arbitrary points of (1.2), with no lower spacing.  Equations (1.5) hold
pointwise and their sum is nonpositive.  No inverse Gram matrix depends on
`M_L`; the same virtual translation signs the whole rectangle.  Thus an
`O(L)` near-confluent chain of distinct simple pairs in an `O(1/L)`
ordinate window is not, by itself, a coherent obstruction.  This concerns
repeated point-value rows, not Hermite derivative conditions.

This does not contradict the finite adaptive-separation countermodel.  That
countermodel quantifies over positive measures in `D`; the state (3.8) has
signed coherent coefficients and uses all their mixed terms.

## 5. Exact annihilation and the Hardy--Blaschke bill

There is a second, complementary escape for a fixed finite list.  In the
complex-polarized PW space, apply

```text
P(-partial_t),       P(z)=product_j (z-z_j),         (5.1)
```

to a two-endpoint packet and then solve the one selected positive-row
equation.  Its transform is multiplied by `P(z)`, so every chosen
`F(z_j)` vanishes exactly.  A real construction uses the conjugate-symmetric
polynomial and at most doubles the degree.  For fixed list size and
`L^(-O(1))` separation from the selected transform point, the loss is only a
power of `L`, hence the full exponential carrier survives.  With no spacing
hypothesis the exact statement is instead (5.4).

The conditioning cost has an exact universal upper bound.  Let
`q in L^2([-D/2,D/2])`, let `F=F_q`, and suppose

```text
F(z_j)=0,             Re z_j>0.                     (5.2)
```

Put

```text
G(s)=exp(-s*D/2)*F(s)
     =integral_0^D q(D/2-u)*exp(-s*u)du.             (5.3)
```

This is a right-half-plane `H^2` function.  Dividing by its finite Blaschke
product preserves the boundary norm, so evaluation at the positive real
point `alpha` gives exactly

```text
|F(alpha)|
 <=exp(alpha*D/2)/sqrt(2*alpha)
   *product_j |(alpha-z_j)/(alpha+conj(z_j))|
   *||q||_2.                                        (5.4)
```

If the selected positive row is zero, (2.5) squares this product.  Thus a
fixed list whose transform points stay at least `L^(-O(1))` from `alpha`
costs only `X^o(1)`, but fixed cardinality alone is not enough: even one
exponentially close transform zero can spend a fixed carrier exponent.
The spacing-free statement is (5.4), and `Theta(L)` genuinely separated
conditions can also spend a fixed carrier exponent.

### 5.1 The current explicit discrepancy budget misses the square-ledger threshold

Bellotti--Wong give the endpoint discrepancy

```text
abs(N(T)-main(T)) <=(0.10076+o(1))*L.               (5.5)
```

Thus `[t-h,t+h]` contains at most

```text
(h/pi+0.20152+o(1))*L                               (5.5a)
```

zeros for fixed `h=O(1)`; only when `h=o(1)` does the main term disappear.
Accordingly `0.20152` is the endpoint-error, or exceptional-cluster,
allowance, not the total fixed-width count.  A horizontally reflected
off-line pair consumes two zeros, so its exceptional pair-center budget is

```text
c_BW=0.10076.                                       (5.6)
```

To test (5.4) against this exceptional budget alone, put one effective
condition in each successive dangerous phase cell.  This is a favorable
abstract allocation for root-per-row nulling and deliberately omits the
nonnegative Riemann--von Mangoldt background.  On one
ordinate side those cells have centers `(2m-1)*pi/D`; both signs are
available, so after ordering by absolute ordinate the worst sequence is

```text
|delta_m|=(pi/d)*(m/L)+o(1),
1<=m<=c_BW*L.                                       (5.7)
```

Take `beta_m=alpha-o(1)`.  Riemann summation in (5.4) gives

```text
(1/L)*log product_m
 |(alpha-z_m)/(alpha+conj(z_m))|

 -> I(alpha,d,c)
  =integral_0^c log[
       ((pi/d)*x)/sqrt(4*alpha^2+((pi/d)*x)^2)] dx. (5.8)
```

Put

```text
y=pi*c/(2*alpha*d),
H(y)=atan(y)-y*log[y/sqrt(1+y^2)].                   (5.9)
```

Direct integration yields

```text
I=-(2*alpha*d/pi)*H(y).                             (5.10)
```

After the square in (2.5), the surviving carrier exponent is at most

```text
alpha*d+2*I
 =alpha*d*[1-(4/pi)*H(y)].                          (5.11)
```

The function `H` is strictly increasing from `0` to `pi/2`, since

```text
H'(y)=-log[y/sqrt(1+y^2)]>0.                        (5.12)
```

The root of `H(y)=pi/4` is

```text
y_0=0.4088594417203485... .                         (5.13)
```

In the present packet range `alpha<=1/2`, `d<=2/3`, one has

```text
y>=3*pi*c_BW/2=0.474820313663561...>y_0.            (5.14)
```

Consequently (5.11) is negative throughout that range.  At the most
favorable endpoint `alpha=1/2,d=2/3`, the numbers are

```text
selected exponent                         0.3333333333...,
Blaschke-square loss                      0.3587246666...,
remaining exponent                      -0.0253913332.... (5.15)
```

At `alpha=0.49,d=2/3`, the remaining exponent is
`-0.0282618871...`.

The exact-null strategy would become favorable at the endpoint only if the
pair-center coefficient satisfied

```text
c<(2*alpha*d/pi)*y_0
 <=0.08676266824... .                                (5.16)
```

Equivalently, this endpoint-error coefficient would need to improve from
`0.20152` to below `0.1735253365...` even before the main-density background
is charged.  Present global fixed-depth
zero-density estimates do not give that uniform local improvement.

If only one ordinate sign were present, the spacing in (5.7) would double
and the ledger would have positive slack.  The actual divisor may occupy
both signs around the selected ordinate; dropping that factor of two is not
legitimate.  This resolves the apparent near-equality obtained from a
one-sided Stirling estimate.

The calculation is a sharp verdict on **root-per-condition exact
annihilation**, not a no-go theorem for every sign-only coherent design.
The microcluster theorem in Sections 3--4 is precisely an example where
many conditions are handled without paying one Blaschke factor per row.

### 5.2 Exact half-line theorem: unequal endpoints pay only once

There is an important distinction between a negative selected-pair value
and the stronger selected-positive-row quotient (1.3).

The one-loss statement is exact in the causal half-line Hardy model.  Put

```text
B(s)=product_j (s-z_j)/(s+conj(z_j)),
G_B(s)=B(s)/(s+alpha).                               (5.17)
```

Multiplication by the inner function `B` preserves the `H^2` norm, so
`G_B` has the same norm as the reproducing kernel `1/(s+alpha)`, vanishes at
every `z_j`, and satisfies

```text
G_B(alpha)=B(alpha)/(2*alpha).                       (5.18)
```

Thus (5.4) is attained, up to the harmless phase of `B(alpha)`, in the
unrestricted causal `L^2(0,infinity)` model.

Pair this constrained right-endpoint component with an unconstrained
left-endpoint component of the opposite phase.  After unit normalization
their selected evaluations have sizes

```text
|F_R(alpha)|
 asymp exp(alpha*D/2)*B_alpha,

|F_L(-alpha)|
 asymp exp(alpha*D/2),                               (5.19)

B_alpha=product_j |(alpha-z_j)/(alpha+conj(z_j))|.
```

Their cross product is negative and has size

```text
exp(alpha*D)*B_alpha.                               (5.20)
```

Thus a merely negative selected pair pays the Blaschke product **once**.
Forcing `F(alpha)+F(-alpha)=0` reduces the larger endpoint to the smaller
one and pays `B_alpha^2`, as in (5.11).

For the exceptional phase-cell ledger (5.7), considered by itself, the
one-product exponent is

```text
E_one(alpha,d,c)
 =alpha*d+I
 =alpha*d*[1-(2/pi)*H(y)].                          (5.21)
```

Since `H(y)<pi/2` for every finite `y`, this exceptional-only ledger has the
exact potential ceiling

```text
E_one(alpha,d,c)>0                                  (5.22)
```

for every finite pair-center coefficient `c`.  At the current explicit
endpoint-error constant,

```text
E_one(1/2,2/3,0.10076)=0.1539710001...,
E_one(0.49,2/3,0.10076)=0.1492023898....            (5.23)
```

The separate continuum background has another cost.  One condition at ordinate gap
`delta` has one-product potential

```text
V_alpha(delta)
 =(1/2)*log(1+(2*alpha/delta)^2).                   (5.24)
```

At the Riemann--von Mangoldt off-line pair density `L/(4*pi)`, a perfectly
uniform full-line ledger would cost

```text
(1/(4*pi))*integral_R V_alpha(delta)d delta
 =alpha/2.                                          (5.25)
```

By itself, it would therefore leave the exponent

```text
alpha*(d-1/2)>0                 when d>1/2.          (5.26)
```

These two favorable calculations cannot be substituted for their sum.  A
count-only broad-list argument must allow both the main-density background
and the endpoint-error cluster.  Root-per-row one-loss nulling then has the
combined ledger

```text
E_combined(alpha,d,c)
 =alpha*d+I-alpha/2
 =alpha*(d-1/2)-(2*alpha*d/pi)*H(y).                (5.26a)
```

At the current constant this is negative at the favorable endpoint:

```text
E_combined(1/2,2/3,0.10076)=-0.0960289999...,
E_combined(0.49,2/3,0.10076)=-0.0957976102....      (5.26b)
```

For `alpha=1/2,d=2/3`, positivity of this combined ledger would require the
pair-center endpoint-error coefficient below `0.0272878643...`, equivalently
the zero-count endpoint-error coefficient below `0.0545757286...`.  This is
a sufficiency ledger, not a claim that zeta realizes the extremal allocation.

Equations (5.21)--(5.26b) identify the exact one-loss improvement and also
show that it does not clear the current count-only broad-list bill.  Three
further gaps remain.

1. Arbitrarily many rows can occupy one phase cell.  Exact zeros pay once
   per row, while the microcluster phase transporter pays once per bounded
   rescaled cluster.  A global all-pass/sign-interpolation theorem combining
   those local groupings across `Theta(L)` cells is not proved here.
2. The causal Hardy extremizer for `B_alpha` need not lie in the required
   finite physical support after `Theta(L)` factors.  Its group delay is
   `Theta(L)`; a quantitative endpoint truncation and jet transfer is still
   needed.
3. The one-product state deliberately has unequal selected endpoint
   evaluations.  It is a valid negative selected-pair witness, but it does
   not lie in the selected positive-row kernel used by the current
   target-only arithmetic feasible set.  The uniform support-function bound
   on that same feasible set continues to pay the square ledger unless a new
   same-state reduction removes this constraint.

The compact-realization issue can be measured exactly at the boundary.  A
single factor has group delay

```text
tau_j(omega)
 =-d/domega arg[(i*omega-z_j)/(i*omega+conj(z_j))]
 =2*Re(z_j)/[(omega-Im(z_j))^2+Re(z_j)^2],          (5.27)

integral_R tau_j(omega)domega=2*pi.                 (5.28)
```

For a cascade, the delays add.  Hence `K=Theta(L)` factors carry total phase
winding `2*pi*K` and `Theta(L)` aggregate delay on a fixed ordinate band
containing the factor centers.
The inverse Laplace transform is causal but has infinite support.  Equations
(5.27)--(5.28) explain why truncating it into the available endpoint layer
is a genuine quantitative step rather than a formal density argument; they
do not themselves give the needed tail bound.

There is, however, a useful exact sufficient tail estimate.  Write
`a_0=min_j Re z_j`, let `g_B` be the inverse Laplace transform of `G_B`, and
take `0<eta<min(a_0,alpha)`.  Plancherel on the shifted boundary gives

```text
||exp(eta*t)*g_B||_2^2
 =(1/(2*pi))*integral_R |G_B(-eta+i*omega)|^2 d omega

 <=1/[2*(alpha-eta)]
   *product_j [(Re z_j+eta)/(Re z_j-eta)]^2

 <=exp(2*M*log[(a_0+eta)/(a_0-eta)])
   /[2*(alpha-eta)].                                (5.29)
```

Consequently

```text
||1_[W,infinity)*g_B||_2^2
 <=exp(-2*eta*W
       +2*M*log[(a_0+eta)/(a_0-eta)])
   /[2*(alpha-eta)].                                (5.30)
```

For `M=cL` and `W=w_0L`, this estimate has a positive exponential tail
margin whenever

```text
w_0>2*c/a_0.                                        (5.31)
```

Indeed `eta^(-1)log[(a_0+eta)/(a_0-eta)]` increases from `2/a_0`.
If the relevant roots obey the present deep threshold
`a_0>=alpha*d-o(1)` and one may use an inward layer of length `W=D=dL`,
(5.31) becomes

```text
alpha*d^2>2*c.                                      (5.32)
```

At `c=0.10076,d=2/3`, this asks for
`alpha>0.45342...`.  Truncating under (5.30) perturbs evaluation at a root
`z_j` by at most the displayed tail norm times
`exp(-Re(z_j)*W)/sqrt(2*Re(z_j))`, so the lost exact zero is still
exponentially small.

This partially resolves compact realization for a separated
root-per-condition cascade in the very-deep range.  It does not control the
Blaschke attenuation of an arbitrarily confluent `M=Theta(L)` cluster, does
not prove one effective factor per phase cell, and does not restore the
selected positive-row equality.  Accordingly it is not promoted to an
actual divisor-isolation theorem.

Fixed-depth global density estimates make a uniform background of very deep
pairs sparse, but they do not presently improve the `0.20152*L`
shrinking-window/endpoint-error allowance uniformly at the selected height.
Hence they do not by themselves fill gaps 1--3.

## 6. Why widening the packet does not complete the argument

A tempting extension is to let `w->infinity`, `w=o(L)`, use the polynomial
phase transport on

```text
|delta|<=C/L,                                       (6.1)
```

and invoke Fourier decay of the width-`w` packet outside that aperture.
For the differential construction above, these two estimates do not
overlap.

Indeed, suppose a polynomial `p` satisfies

```text
|p(-i*c)-exp(i*d*c)|<1/2       for |c|<=C.           (6.2)
```

At the points `c=k*pi/d`, the real part of `p(-i*c)` must alternate sign.
Hence the degree obeys the elementary lower bound

```text
deg p >=(2*d/pi)*C-O(1)=Omega(C).                   (6.3)
```

Applying this degree-`r` differential filter multiplies the local Fourier
transform by a degree-`r` polynomial in `L*delta`.  The direct
integration-by-parts estimate with derivative order comparable to `r` can
dominate that multiplier only once

```text
|delta|*w >> r.                                     (6.4)
```

At the proposed interface `|delta|=C/L`, however,

```text
|delta|*w=C*w/L=o(C)=O(r),                          (6.5)
```

for every `w=o(L)`.  Thus that standard differential-filter tail estimate
begins only after a gap in which the phase polynomial can be large.  The
example `w=L^(2/3), C=L^(1/2)` has exactly this defect:
`delta*w=L^(1/6)` at the interface, while `r` is of order `L^(1/2)`.

Equations (6.3)--(6.5) rule out this proposed proof by differential
filtering plus the stated integration-by-parts tail estimate.  They are not
a universal lower bound for every smooth/Gevrey construction and do not
exclude a new bounded-outside superoscillatory filter whose full real-axis
norm is controlled by a different mechanism.

## 7. Endpoint jets and finite Gabor transfer

Every packet in (3.5) is supported strictly inside the physical endpoints;
differentiation and finite differences preserve that support.  Therefore
all physical endpoint jets vanish exactly already in the continuous PW
model.

For fixed `Lambda,C`, the degree `r` is fixed.  The common binomial
endpoint-flat cutoff and Fourier truncation in
`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`,
Section 5, apply after paying only the polynomial factor `L^r`.  Their
`O_A(T^-A)` error may be made smaller than
`exp(alpha*D)/L^(2r+2)`, uniformly on the compact parameter rectangle.
Exact target-row projection and Gram--Schmidt preserve the strict margin in
(3.15).  If `O(L)` collateral rows are present, increase the fixed
truncation power once more to absorb their total count.

Hence (1.3)--(1.5) transfer to the growing-endpoint-jet finite Gabor space
for every fixed rescaled microcluster.  This realizes an admissible
coefficient-space state for an abstract allowed divisor list.  It does not
assert that zeta contains that list, and it does not control collateral
pairs outside the rectangle (1.2).

## 8. Truth boundary and next gate

What is proved:

| statement | verdict |
|---|---|
| positive separation averaging always defeats the phase flip | false, by the earlier counterconfiguration |
| coherent fixed-width superposition defeats `+/-pi/D` | **yes** |
| the same state signs an arbitrary-cardinality bounded rescaled microcluster | **yes** |
| all mixed coherent terms are included | **yes**, by (2.3) |
| fixed clusters retain `X^(alpha*d-o(1))` after endpoint transfer | **yes** |
| exact nulling of `Theta(L)` broad conditions is free | **no**, by (5.4) |
| current explicit local count clears the broad Blaschke bill on the selected-positive quotient | **no**, by (5.11)--(5.15) |
| the unrestricted causal unequal-endpoint exceptional-only ledger retains a positive exponent | **yes**, by (5.21), but adding the count-only Riemann--von Mangoldt background makes the current combined ledger negative by (5.26a)--(5.26b) |
| widening plus the stated integration-by-parts tail closes the remaining aperture | **no**, for that construction |
| arbitrary actual-zeta collateral isolation | open |

The next coherent question is now narrow:

> Construct a compactly supported phase transporter which is
> superoscillatory on the required low band but has a controlled exterior
> response, or prove a Bode/Beurling-type lower bound for that exterior
> response.  The exceptional-only selected-positive quotient misses by
> `0.02539...`; a count-only one-loss ledger that also charges the
> Riemann--von Mangoldt background misses by `0.09603...` at the favorable
> endpoint.

That is a genuine mixed-term problem.  Positive measures, row-by-row roots,
and ordinary smooth tails have each reached an explicit wall.
