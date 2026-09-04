# QP Gibbs reweighting: the halfspace cluster gate

**Date:** 2026-08-15  
**Verdict:** exponential reweighting does not close fixed-power QP from the
available scalar KMT/Heath--Brown estimates.  There is an exact compact-group
countermodel in which

```text
every nontrivial scalar Fourier character is O(R^(-1/2));
every fixed degree-D character is O_D(R^(-D/2));
the shifted R-by-R square ledger is O(1);
each single packet is repairable by an O(R^(-1/2)) Gibbs tilt;
the simultaneous Gibbs partition function is stably normalized;
```

but **no positive reweighting whatsoever** can lift all `R` packet moments
above `-1/(2 sqrt(R))`.

At the QP scale

```text
epsilon=Y^(-c),             R asyp (4 epsilon^2)^(-1),              (0.1)
```

this countermodel has scalar Fourier error `O(Y^(-c))`, much smaller than
the logarithmic KMT floor, while its packet count is within the
Guth--Maynard allowance `R<=epsilon^(-2)`.  It therefore proves that a
cumulant/cluster expansion which uses only termwise scalar KMT bounds and
the existing Heath--Brown square ledger cannot certify the simultaneous
Gibbs repair.

This is a theorem about that **black-box proof package**.  The model lives on
an `R`-dimensional torus, not on the one-dimensional actual prime-log orbit.
It does not disprove the actual-prime directional theorem, QP, or a uniform
zero-free strip.  Rather, it identifies the genuinely missing input: a
scalar-orbit/actual-prime theorem excluding a collective cosine halfspace.

---

## 1. Gibbs reweighting is an exact convex-hull parametrization

Let `u_1,...,u_M` be the actual shell nodes, let `t_1,...,t_R` be selected
bad-packet centres, and put

```text
x_j=(cos(t_1 u_j),...,cos(t_R u_j)) in [-1,1]^R.       (1.1)
```

Start with any strictly positive probability vector `mu_j`.  Its Gibbs
family is

```text
p_j(theta)=mu_j exp(theta dot x_j)/Z(theta),
psi(theta)=log Z(theta),
grad psi(theta)=sum_j p_j(theta)x_j.                   (1.2)
```

The standard finite log-sum-exp argument gives

```text
closure {grad psi(theta):theta in R^R}
   =conv{x_1,...,x_M}.                                (1.3)
```

Indeed, every Gibbs mean is a convex combination.  Conversely, exposing a
face by sending `theta` to infinity and then varying tangent parameters
recovers the relative interior of that face; induction over faces proves
(1.3).  Thus allowing arbitrary Gibbs parameters already gives, in closure,
the original finite node simplex.  Restricting to nonnegative parameters
can only shrink it.

For the target orthant

```text
O_epsilon={y:y_i>=-epsilon for every i},              (1.4)
```

finite separation says

```text
conv{x_j} intersects O_epsilon
```

if and only if, for every `a_i>=0`,

```text
max_j sum_i a_i cos(t_i u_j)>=-epsilon sum_i a_i.     (1.5)
```

If the sets are disjoint, the separating functional must have nonnegative
coordinates because `O_epsilon` is unbounded in every positive coordinate,
and its infimum on `O_epsilon` is `-epsilon sum a_i`; this gives the reverse
direction.  Formula (1.5) is the selected-packet actual-prime convex-hull
gate.  Gibbs dynamics organizes that gate but does not weaken it.

---

## 2. A Fourier-uniform collective halfspace

Let `Theta_1,...,Theta_R` be independent Haar angles on the circle and set

```text
X_i=cos Theta_i,               S_R=sum_i X_i.         (2.1)
```

Let `mu_R` be Haar probability conditioned on

```text
A_R={S_R<=-sqrt(R)}.                                  (2.2)
```

The central limit theorem gives

```text
P(A_R) -> Phi(-sqrt(2))>0,                            (2.3)
```

because `E X_i=0` and `Var X_i=1/2`.

### Theorem 2.1 (uniform character bound)

For all sufficiently large `R`, uniformly over every nonzero
`k in Z^R`,

```text
|hat mu_R(k)|<=C R^(-1/2).                            (2.4)
```

#### Proof

Choose `i` with `k_i!=0`, condition on all other angles, and write

```text
Z=sum_(j!=i) cos Theta_j,             b=-sqrt(R).     (2.5)
```

The inner integral

```text
int exp(i k_i theta)
    1_(Z+cos theta<=b) dtheta/(2 pi)                  (2.6)
```

vanishes unless `|Z-b|<1`: outside that boundary layer the indicator is
identically zero or one, and a nonconstant circle character integrates to
zero.  Its modulus is at most one inside the layer.  Hence the unnormalized
Fourier coefficient is at most

```text
P(|Z-b|<1)<=2 ||f_(R-1)||_infinity,                   (2.7)
```

where `f_n` is the density of a sum of `n` independent cosine variables.
Its characteristic function is `J_0(t)^n`, so Fourier inversion gives

```text
||f_n||_infinity
 <=(2 pi)^(-1) int_R |J_0(t)|^n dt
 <<n^(-1/2).                                         (2.8)
```

For completeness, near zero use `|J_0(t)|<=exp(-c t^2)`.  On a fixed
annulus away from zero use `sup |J_0|<1`, and in the tail use the standard
stationary-phase bound `|J_0(t)|<<|t|^(-1/2)`.  These three ranges prove
(2.8).  Divide (2.7) by the fixed positive denominator in (2.3).  QED

Thus this model satisfies a scalar Fourier bound at **every** nontrivial
additive character, not merely at the original packet coordinates.

### Theorem 2.2 (fixed-degree refinement)

Fix a multi-index `k` whose support size is fixed, and put

```text
D=||k||_1.                                             (2.9)
```

Then

```text
hat mu_R(k)=O_k(R^(-D/2)).                            (2.10)
```

#### Proof

Separate the fixed active coordinates and let `F_n` be the distribution
function of the sum of the other `n=R-O_k(1)` cosine variables.  The
unnormalized coefficient is

```text
int exp(i k dot theta) F_n(b-sum cos theta_j)dtheta.  (2.11)
```

Taylor-expand `F_n` through degree `D-1`.  Every resulting polynomial in
the active cosines has Fourier `l1` degree below `D`, so its `k` coefficient
vanishes.  The remainder is bounded by a fixed multiple of

```text
||F_n^(D)||_infinity
 =||f_n^(D-1)||_infinity
 <=(2 pi)^(-1) int |t|^(D-1)|J_0(t)|^n dt
 <<_D n^(-D/2).                                      (2.12)
```

Divide again by (2.3).  QED

In particular, for distinct indices,

```text
E_mu X_i=O(R^(-1/2)),
E_mu X_i X_j=O(R^(-1)),
E_mu X_i X_j X_k=O(R^(-3/2)), ... .                  (2.13)
```

The corresponding connected cumulants of any fixed list of distinct
coordinates have the same `R^(-D/2)` scale.  Every fixed-order cluster
therefore looks perturbative.

---

## 3. Every positive simultaneous repair fails

Put

```text
epsilon_R=1/(2 sqrt(R)).                              (3.1)
```

### Theorem 3.1 (positive-reweighting lock)

For every measurable `h>=0` with `int h dmu_R>0`, write

```text
m_i(h)=int h X_i dmu_R / int h dmu_R.                 (3.2)
```

Then

```text
sum_i m_i(h)<=-sqrt(R),
min_i m_i(h)<=-1/sqrt(R)=-2 epsilon_R.                (3.3)
```

This is immediate by integrating the pointwise support inequality (2.2).
It applies in particular to every Gibbs weight

```text
h_theta=exp(sum_i theta_i X_i),                       (3.4)
```

with arbitrary real parameters, and to every finite product or sequence of
one-packet exponential tilts.  Thus none can achieve

```text
m_i(h)>=-epsilon_R             for every i.           (3.5)
```

Equivalently, if

```text
psi_R(theta)=log int exp(theta dot X)dmu_R,           (3.6)
```

then the exact log-partition identity is

```text
sum_i partial_i psi_R(theta)<=-sqrt(R)                (3.7)
```

for every `theta`.

### Each packet separately is nevertheless repairable

Permutation symmetry and (2.4) give

```text
-C/sqrt(R)<=E_mu X_i<=-1/sqrt(R),                    (3.8)
```

while

```text
Var_mu(X_i)=1/2+O(R^(-1/2)).                          (3.9)
```

For the one-coordinate tilt, the derivative of its tilted mean is its
tilted variance.  Since `X_i in [-1,1]`, that variance changes by at most a
fixed multiple of the parameter.  Equations (3.8)--(3.9) therefore show
that some positive parameter

```text
lambda_i=O(R^(-1/2))                                 (3.10)
```

lifts the individual `i`th mean through zero.  So the failure is genuinely
simultaneous, not a failure of the already-proved one-packet covariance
mechanism.

---

## 4. Stable normalization does not rescue the cluster expansion

The most symmetric simultaneous tilt has

```text
theta_i=lambda/sqrt(R),
h_lambda=exp(lambda S_R/sqrt(R)).                    (4.1)
```

Under `mu_R`, the variable `S_R/sqrt(R)` converges to

```text
Z ~ N(0,1/2) conditioned on Z<=-1.                  (4.2)
```

For every fixed `lambda>=0`, the normalized partition function converges to

```text
E[exp(lambda Z)|Z<=-1]
 =exp(lambda^2/4)
   Phi(-sqrt(2)-lambda/sqrt(2))/Phi(-sqrt(2)),        (4.3)
```

a finite positive constant.  Thus there is no exploding or vanishing
normalization tax at the critical parameter scale.

The tilted limiting mean is

```text
lambda/2
 -(1/sqrt(2)) phi(-sqrt(2)-lambda/sqrt(2))
                 /Phi(-sqrt(2)-lambda/sqrt(2))
 <-1.                                                 (4.4)
```

It approaches `-1` only as `lambda` tends to infinity.  The desired target
is `-1/2` after multiplication by `1/sqrt(R)`, so even the full normalized
Gibbs response stops on the wrong side of the support wall.

This also explains the cumulant failure.  Every fixed distinct-coordinate
cumulant is small, but the normalized collective variable

```text
S_R/sqrt(R)                                           (4.5)
```

has a non-Gaussian truncated limit.  At the critical parameters in (4.1),
every order of its log-partition expansion contributes at constant scale.
A finite cluster truncation cannot encode the halfspace boundary.

---

## 5. The Heath--Brown square ledger can be better than required

Let `e_i` denote the `i`th torus character and put

```text
Phi(k)=hat mu_R(k).                                   (5.1)
```

Fix a query packet `e_k`.  Among the `R^2` translated characters

```text
e_k+e_i-e_j,                                         (5.2)
```

there are exactly

```text
2R-1       characters of l1 degree 1,
(R-1)^2    characters of l1 degree 3.                (5.3)
```

Theorem 2.2 therefore gives

```text
sum_(i,j)|Phi(e_k+e_i-e_j)|^2
 <<(2R-1)R^(-1)+(R-1)^2 R^(-3)
 <<1.                                                 (5.4)
```

This is stronger than the normalized `O(R)` repeated-difference term left by
the currently imported Heath--Brown estimate.  Nevertheless Theorem 3.1
still forbids every simultaneous positive repair.  Even an excellent
fixed-degree cross-Gram theorem does not, by itself, control the all-order
exponential tilt.

The distinction is exact:

```text
fixed-degree Fourier/covariance control:       local information;
exclusion of (2.2) on the sampled scalar orbit: collective support theorem.
```

---

## 6. Fixed-power ledger

Take the desired fixed QP floor

```text
epsilon=Y^(-c),              c>.0187463697147...,    (6.1)
```

and choose

```text
R=floor((4 epsilon^2)^(-1)).                         (6.2)
```

Then

```text
R=Y^(2c+o(1))/4<=epsilon^(-2),
R^(-1/2)=2 epsilon(1+o(1)).                          (6.3)
```

The torus model has all-character scalar error `O(epsilon)`, its
fixed-degree cross-Gram square is `O(1)`, and yet some reweighted packet
stays below `-2 epsilon(1+o(1))`.  For `c=.019`, its packet exponent is
`.038`, exactly the critical exponent already present in the QP ledger.

Again, (6.3) is an abstract compact-group saturation, not a construction
using the actual prime-power logarithms.

---

## 7. What an actual Gibbs theorem would have to prove

The surviving statement can be written without any algorithm.  For every
selected actual bad-packet list and every nonzero `a_i>=0`, prove

```text
max_(p^m in the shell)
  sum_i a_i cos(t_i log(p^m/Y))
 >=-Y^(-c) sum_i a_i.                                (7.1)
```

By Section 1 this is exactly the finite packet feasibility condition.  To
make the final antenna valid on the continuum band, one must additionally
control the off-packet moments after the reweighting or run a compact
exchange argument with a uniform margin.

Possible analytic forms of genuinely new input are:

1. a critical-scale all-order Laplace-transform comparison for the actual
   prime-log curve, uniform for adaptive `theta` with `||theta||_2=O(1)`;
2. an actual-prime anti-halfspace/sampling theorem proving (7.1);
3. a candidate-specific nonlinear covariance estimate which retains the
   complete Gibbs normalization and rules out collective support walls.

Scalar KMT values, the present Heath--Brown square estimate, and a
fixed-order cumulant expansion do not imply any of these, by Theorems
2.1--3.1.

---

## 8. Binary disposition

```text
one-packet Gibbs repair at critical depth:              PROVED in model;
all nontrivial torus characters O(R^-1/2):              PROVED;
fixed degree-D characters O_D(R^-D/2):                 PROVED;
shifted cross-Gram square O(1):                         PROVED;
stable critical Gibbs normalization:                    PROVED;
simultaneous positive/Gibbs repair from those data:     FALSE ABSTRACTLY;
actual-prime scalar-orbit anti-halfspace theorem:        OPEN;
fixed-power positive QP-KILL:                           NOT PROVED;
uniform zero-free strip or QP equivalence:              NOT PROVED.
```

Executable replay:

- `src/qp_gibbs_halfspace_gate.py`;
- `src/test_qp_gibbs_halfspace_gate.py`;
- `results/verify_zeta23_qp_gibbs_halfspace_gate.py`.
