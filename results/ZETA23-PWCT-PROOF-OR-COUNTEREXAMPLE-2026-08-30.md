# Positive-weight carrier theorem: proof-or-counterexample audit

**Date:** 2026-08-30  
**Status:** hostile audit completed.  The actual-prime theorem is neither
proved nor refuted.  Its source-time and low-participation branches are
closed, while a prime-density diffuse real-node model refutes every soft
relaxation tested.  No zero-free strip and no proof of RH.

## 0. Frozen statement

At scale `N`, let `Y` be an allowed half-integer center with
`N<=Y<=2exp(w)N`, and let

```text
P_Y={p prime:Y exp(-w)<p<Y exp(w)},
u_p=|log(p/Y)|,
H_Y=[Y^.01,Y^(50/33)].
```

For a legal contiguous prime event `I` at
`t_0 in [N^(1/2),N]`, put

```text
M=#I,
D=-M^(-1)sum_(p in I)cos(t_0u_p),
e=(M/N)D>=N^(-.001+o(1)),
v=a_P(t_0)+Dq_P.                                      (0.1)
```

Join each opposite-side pair with `B|u_p-u_q|<=1`, where
`B=Y^(50/33)`, and let `C_Y` be the subspace having equal coefficients on
each such pair.  This graph is a matching for large `Y`: two distinct primes
on the same side have absolute-log separation `>>Y^-1`, whereas two neighbors
of one opposite-side vertex would be within `2B^-1=o(Y^-1)`.  Define

```text
rho_+(v)=inf {-inf_(t in H_Y) W_w(t):
              w>=0, w in C_Y, w.v=1},
W_w(t)=sum_p w_p cos(tu_p),                           (0.2)
```

with infimum `+infinity` when the feasible set is empty.

The positive-weight carrier theorem, `PWCT(.0179,.001)`, asserts that for
every fixed `eta>0` and every sufficiently large legal event,

```text
rho_+(v)>=Y^(-(.0179+eta)).                           (0.3)
```

If `(0.3)` fails with a fixed exponent margin, `y=-w` is a carrier-supported
COSE separator.  Conversely, proving `(0.3)` excludes only nonpositive
separators; it does not prove full COSE.

## 1. The source negative mass survives deletion of every reflected pair

Let `R_Y` be the set of prime coordinates incident to a close reflected
pair, and put `U_Y=P_Y\R_Y`.  The integer-product count gives

```text
#R_Y<=2Y^(16/33+o(1)).                                (1.1)
```

### Proposition 1.1 (unpaired-event inheritance)

Every event in `(0.1)` obeys

```text
-N^(-1)sum_(p in I intersect U_Y)cos(t_0u_p)
 >=N^(-.001+o(1)).                                   (1.2)
```

More precisely, the left side is at least
`e-2Y^(-17/33+o(1))`.

#### Proof

Deleting one summand changes the unnormalized cosine sum by at most one.
Thus deletion of `I intersect R_Y` changes its mass-normalized negative value
by at most `#R_Y/N`.  Since `N asymp Y`, `(1.1)` makes this
`O(Y^(-17/33+o(1)))=o(N^-.001)`.  This proves `(1.2)`.  QED

In particular the source event cannot place a macroscopic share of its
negative mass in the reflected-pair sector.  Every vector supported on
`U_Y` automatically belongs to `C_Y`.

**Scope warning.**  The set `I intersect U_Y` need not be contiguous.
Therefore `(1.2)` is only inheritance of mass-normalized negative mass; it
cannot be reused as a legal LTRAD source event.  The estimate also does not
show that pair coordinates are irrelevant to high-band cancellation.

## 2. Exact probability normalization

For a feasible `w`, let

```text
S=sum_p w_p,
alpha=w/S,
Phi_alpha(t)=sum_p alpha_p cos(tu_p),
A(alpha)=D+Phi_alpha(t_0).                            (2.1)
```

Then `alpha` is a carrier probability vector and `S A(alpha)=1`.  Conversely
every carrier probability vector with `A(alpha)>0` gives the feasible vector
`w=alpha/A(alpha)`.  Therefore

```text
rho_+(v)=inf_(alpha>=0, sum alpha=1, alpha in C_Y,
              A(alpha)>0)
             a(alpha)/A(alpha),
a(alpha)=-inf_(t in H_Y)Phi_alpha(t).                 (2.2)
```

This identity exposes the support-avoidance issue: the source interval enters
the objective only through the admissible pair `(t_0,D)`.  The adaptive
probability `alpha` may give the source interval no mass.

### Corollary 2.1 (source-time branch)

Since `Phi_alpha(t_0)=A-D`,

```text
a(alpha)>=D-A(alpha)                    when A(alpha)<D. (2.3)
```

Writing `epsilon=Y^(-(.0179+eta))`, every counterexample to `(0.3)` must
satisfy

```text
A(alpha)>D/(1+epsilon).                               (2.4)
```

Thus a putative shallow positive antenna cannot itself be substantially
negative at the source time.

Let `lambda_I` be the uniform probability on the source interval, extended
by zero to the rest of the shell.  Since
`Phi_(lambda_I)(t_0)=-D`, there is also the exact identity

```text
A(alpha)=(alpha-lambda_I).a_P(t_0),
A(alpha)<=||alpha-lambda_I||_1.                      (2.5)
```

Thus a counterexample is at least `D/(1+epsilon)` away from the uniform
source in `ell^1` distance.  At `D=Y^(-.001+o(1))` this separation tends to
zero and does not imply that `alpha` avoids most of `I`.

### Proposition 2.2 (exact feasibility and vacuity)

For a carrier group `g`, put

```text
V_g=sum_(p in g)[cos(t_0u_p)+D].                     (2.6)
```

The feasible set in `(0.2)` is nonempty if and only if `V_g>0` for at least
one singleton or paired group.  The unpaired-only feasible set is nonempty
if and only if some unpaired coordinate has
`cos(t_0u_p)+D>0`.

Indeed a nonnegative carrier vector is parameterized by group weights
`x_g>=0`, and its normalization is `sum_g x_gV_g=1`.  This equation has a
solution exactly under the displayed positivity condition.  Notice that

```text
M^(-1)sum_(p in I)[cos(t_0u_p)+D]=0.                 (2.7)
```

The canonical source probability is therefore null, not feasible.  The
event identity by itself does not guarantee group positivity.  If no group
is positive, PWCT holds vacuously with `rho_+=+infinity`; this cannot exclude
the source event.

For a proposed radius `r>0`, define the nonvacuous threshold functional

```text
Gamma_r=max_(alpha>=0, sum alpha=1, alpha in C_Y)
          min_(t in H_Y){Phi_alpha(t)
                         +r[Phi_alpha(t_0)+D]}.       (2.8)
```

Then `Gamma_r>0` if and only if `rho_+(v)<r`; `Gamma_r<=0` if and only if the
PWCT inequality at radius `r` holds, possibly vacuously.  This is the exact
semi-infinite LP used in the finite diagnostic below.

## 3. Exact semi-infinite dual

Parameterize `C_Y` by its singleton and pair groups `g`, and put

```text
A_g(t)=sum_(p in g)cos(tu_p),
V_g=A_g(t_0)+D|g|.                                   (3.1)
```

Whenever `(0.2)` is feasible, standard finite-variable semi-infinite LP
duality gives

```text
rho_+(v)=sup {s: there is a probability measure mu on H_Y with
              integral A_g(t)dmu(t)<=-sV_g for every g}. (3.2)
```

Indeed, attach a nonnegative measure to
`r+sum_g x_gA_g(t)>=0`, and a free multiplier to
`sum_g x_gV_g=1`.  Minimization in `r` forces the measure to have mass one;
minimization over `x_g>=0` gives the coordinatewise inequalities in `(3.2)`.

Equation `(3.2)` is a coordinatewise dominated radial measure.  It is a
useful exact dual, but it is not yet a simpler construction theorem.

### Proposition 3.1 (positive-carrier DPA incompatibility)

Define the positive-carrier antenna depth

```text
delta_+^C(Y)=inf_(alpha>=0, sum alpha=1, alpha in C_Y) a(alpha). (3.3)
```

The mean-absorbed estimate in Section 4 gives `a(alpha)>0` for every
admissible probability vector (all half-integer-centered frequencies are
nonzero), and hence `delta_+^C(Y)>=0`.

For every legal event with `D>delta_+^C(Y)`, equation `(2.2)` gives

```text
rho_+(v)<=delta_+^C(Y)/[D-delta_+^C(Y)].             (3.4)
```

Indeed a minimizing sequence for `(3.3)` obeys
`Phi_alpha(t_0)>=-a(alpha)`, and hence
`A(alpha)>=D-a(alpha)`.  Since `a(alpha)>=0`, division preserves the upper
bound `a(alpha)/A(alpha)<=a(alpha)/[D-a(alpha)]`; now take the limit.

Consequently a positive-carrier version of `DPA_P(.019)`, together with
`D>=Y^(-.001+o(1))`, would give

```text
rho_+(v)<=Y^(-.018+o(1)).                            (3.5)
```

This contradicts PWCT at any fixed margin below `.0001`.  Thus PWCT plus
that separately open positive-carrier upper antenna excludes every legal
event.  The ordinary `DPA_P` currently on record permits signed coefficients
and cannot silently be substituted into this proposition.

### Proposition 3.2 (carrierization is free for a diffuse positive antenna)

Suppose `alpha` is a positive prime probability vector with

```text
||alpha||_infinity<=Y^(-1+o(1)).                     (3.6)
```

On every canonical reflected pair replace its two coefficients by their
average, and call the result `alpha^C`.  If there are `K` pairs, then

```text
sup_(0<=t<=B)|Phi_(alpha^C)(t)-Phi_alpha(t)|
 <=K||alpha||_infinity<=Y^(-17/33+o(1)),             (3.7)

|Phi_(alpha^C)(t_0)-Phi_alpha(t_0)|
 <=K||alpha||_infinity Y/B
 <=Y^(-34/33+o(1)).                                  (3.8)
```

For one pair this is the mean-value bound

```text
|(alpha_p-alpha_q)[cos(tu_p)-cos(tu_q)]/2|
 <=||alpha||_infinity t/B;
```

summing and using `K<=Y^(16/33+o(1))` proves the claim.  Positivity and total
mass are unchanged.

Consequently an event-free **diffuse positive** `PDPA_+(.019)` would
automatically supply the positive-carrier upper antenna required in
Proposition 3.1; the carrierization errors are much smaller than
`Y^-.019`.  This identifies a genuine companion theorem.  PWCT alone still
does not connect to the signed `DPA_P(.019)` in the recorded strip chain.

### Proposition 3.3 (event-free carrier minimax)

For each carrier group put

```text
c_g(t)=|g|^(-1)sum_(p in g)cos(tu_p),
beta_g=|g|alpha_p.                                   (3.9)
```

Then `beta` ranges over the group simplex and finite-dimensional minimax
duality gives

```text
-delta_+^C(Y)
 =max_(beta in simplex) min_(t in H_Y)sum_g beta_g c_g(t)
 =min_(nu in Prob(H_Y)) max_g integral c_g(t)dnu(t). (3.10)
```

A coordinate cap `alpha_p<=L_Y/Y` is exactly the group constraint
`beta_g<=|g|L_Y/Y`.  This source-free primal/dual comparison tests whether
the diffuse sufficient adapter is active without first finding a finite
surrogate for a legal source event.

## 4. What positivity and second moments prove

Apply the proved mean-absorbed participation theorem in
`ZETA23-QP-LTRAD-B3-SPARSE-SEPARATOR-AND-TWO-CLUSTER-CLOSURE-2026-08-30.md`
to the source-normalized separator `y=-alpha/A(alpha)`.  On carrier pairs the
difference coordinate vanishes, so its block participation is, up to an
absolute factor,

```text
P_eff(alpha)=(sum alpha_p)^2/sum alpha_p^2.           (4.1)
```

That theorem gives directly

```text
a(alpha)/A(alpha)>>1/P_eff(alpha).                   (4.2)
```

Consequently a counterexample must be diffuse:

```text
P_eff(alpha)>>epsilon^(-1)=Y^(.0179+o(1)).           (4.3)
```

Before source normalization, the same mean-absorbed calculation reads

```text
a(alpha)>>1/P_eff(alpha).                            (4.4)
```

Thus failure at radius `epsilon` in fact requires

```text
P_eff(alpha)>>(epsilon A(alpha))^(-1).               (4.5)
```

At `A asymp 1` this is `(4.3)`; at the smallest possible scale
`A asymp D asymp Y^-.001` it is `Y^(.0189+o(1))`.  There is no
source-derived upper bound of this size on `P_eff`; the unpaired shell has
`Y^(1+o(1))` available coordinates.  Positivity plus second moments
therefore does not prove PWCT.

## 5. Two pseudo-prime falsifiers

For both constructions in this section take the allowed center
`Y=N+1/2`.  Hence `Y/N=1+o(1)` in the frozen event normalization.

### 5.1 Exact Fejer lattice

The abstract Fejer obstruction can retain substantially more than mere node
count.  Fix `0<eta<10^-4`, and put

```text
t_0=Y^(1/2),
omega=2pi/t_0,
m=ceil(Y^(.0179+2eta)),
u_d=d omega,                         1<=d<m.          (5.1)
```

These active nodes are one-sided and unpaired.  For the event depth `D`, put

```text
w_d=2(m-d)/[(1+D)m(m-1)].                           (5.2)
```

If

```text
K_m(t)=m^(-1)|sum_(j=0)^(m-1)exp(ij omega t)|^2,
```

then exactly

```text
W_w(t)=[K_m(t)-1]/[(1+D)(m-1)],
W_w(0)=W_w(t_0)=1/(1+D),
w.[a(t_0)+Dq]=1,
-inf W_w=1/[(1+D)(m-1)]
          <<Y^(-(.0179+eta)).                        (5.3)
```

The minimum in `(5.3)` occurs at `t=t_0/m in H_Y`.

The source population can simultaneously be contiguous and prime-density
like.  In a fixed log interval disjoint from `(5.1)`, take
`M asymp cY/log Y` quantiles of the positive density

```text
1-kappa_Y cos(t_0u),
kappa_Y=C(log Y)Y^(-.001).                           (5.4)
```

Its source mean is `-kappa_Y/2+o(kappa_Y)`; quantile quadrature contributes
only `O(t_0/M)=O(Y^(-1/2)log Y)=o(kappa_Y)`.  Hence

```text
D=kappa_Y/2+o(kappa_Y),
e=(M/N)D=(1+o(1))(M/Y)D
  =(cC/2+o(1))Y^(-.001).                             (5.5)
```

The constants can make `(5.5)` legal, and the relative source-density
modulation tends to zero.  Insert zero-weight ordinary-density same-side
nodes between the much more widely spaced active Fejer nodes and throughout
the unused shell.  Insert analogous opposite-side filler while avoiding the
active nodes' total `O(m/B)` forbidden neighborhood.  The filler does not
change the antenna.  The complete node set then has prime-scale density and
spacing while retaining a contiguous event, legal mass, positivity, and
unpaired carrier support.

It is not a counterexample to PWCT: its frequencies are not logarithms of
ordinary primes.  It proves that all of the preceding soft or metric data
remain insufficient.  The unreproduced actual-prime mask bundles
integrality, multiplicativity, and consecutive-prime transition data.

Replay the exact Fejer and exponent identities with

```bash
python3 results/verify_zeta23_pwct.py
```

### 5.2 Diffuse ordinary-density falsifier

The lattice is not the essential obstruction.  There is also a smooth,
diffuse probabilistic construction with ordinary-prime-scale density and
maximum gaps.

Choose a fixed antenna interval `[0,L]` and

```text
g(u)=(1-u/L)_+,
G(t)={integral_0^L g(u)cos(tu)du}/{integral_0^L g(u)du}
    =2[1-cos(Lt)]/(L^2t^2)>=0.                       (5.6)
```

Take `M_A asymp Y/log Y` stratified independent nodes with background
density `f_0(u) asymp exp(u)`, and give a sampled node the importance weight
`g(u)/f_0(u)`, followed by probability normalization.  Hoeffding's
inequality on a polynomial-size time grid, the uniform derivative bound
`|Phi'(t)|<=L`, and concentration of the denominator give a deterministic
realization satisfying

```text
sup_(t in H_Y)|Phi_alpha(t)-G(t)|
 <<sqrt(log(Y)/M_A)=Y^(-1/2+o(1)).                   (5.7)
```

In a disjoint source interval take `M_I asymp cY/log Y` quantile nodes of

```text
exp(u)[1-kappa_Y cos(t_0u)],
t_0=Y^(1/2),              kappa_Y=C(log Y)Y^(-.001). (5.8)
```

Integration by parts and quantile error `O(t_0/M_I)` give

```text
D=kappa_Y/2+o(kappa_Y),
e=(M_I/N)D=(1+o(1))(M_I/Y)D>Y^(-.001)                (5.9)
```

after choosing the fixed constants.  The source nodes form one contiguous
block.  Fill the complementary same-side intervals at zero antenna weight,
and add an independently sampled ordinary-density opposite side across its
entire shell.  Stratification then gives prime-scale density and physical
maximum gaps `O(log^2 Y)` with positive probability.

Counting all filler, the expected number of `B^-1`-close opposite-side pair
vertices is `O(Y^(16/33+o(1)))`; concentration supplies a realization with
that bound simultaneously with `(5.7)`.  Delete the incident vertices from
the antenna and renormalize.  Since every antenna atom is `Y^(-1+o(1))`, this
changes its transform by at most

```text
Y^(16/33+o(1))/M_A=Y^(-17/33+o(1)).                 (5.10)
```

The resulting antenna is positive, diffuse, and supported entirely on
unpaired nodes.  Equations `(5.7)--(5.10)` imply

```text
A(alpha)>=D-Y^(-1/2+o(1)),
rho_+(v)<=Y^(-1/2+o(1))/[D-Y^(-1/2+o(1))]
          =Y^(-.499+o(1)).                           (5.11)
```

This beats the proposed lower bound by a huge exponent margin while
retaining source contiguity, legal mass, positivity, diffuseness,
prime-scale density and gaps, and unpaired carrier support.  It is still
not an actual-prime counterexample: concentration selects real nodes, not
integers or prime logarithms.  The remaining actual-prime mask bundles all
deterministic integrality, multiplicative, and consecutive-prime transition
information; the model does not reproduce those properties.

Together with the previously recorded half-period model, these examples
also show that the same coarse density, gap, and low-denominator data permit
opposite positive-antenna behavior.  Exact ordinary-prime arithmetic is
indispensable in either direction.

## 6. Finite actual-prime diagnostic

### 6.1 Source-conditioned PWCT probe

The exchange LP was run on full-shell and half-shell contiguous intervals
attained over a 2,501-point source-time grid.  The table gives floating
continuum brackets for the resulting actual-prime carrier problems and their
unpaired restrictions.

| `Y` | source | `D` | `e` | `rho_+` | `rho_(+,U)` |
|---:|:---|---:|---:|:---|:---|
| 254.5 | full | .4884 | .03269 | [.6720,.6741] | same |
| 254.5 | half | .6198 | .02196 | [.6175,.6194] | same |
| 299.5 | full | .2889 | .01836 | [.6399,.6404] | [.6673,.6676] |
| 299.5 | half | .4305 | .01440 | [.6618,.6645] | [.6632,.6656] |
| 500.5 | full | .3553 | .02203 | [.5338,.5386] | [.5485,.5541] |
| 500.5 | half | .4860 | .01555 | [.4649,.4697] | [.4771,.4822] |
| 800.5 | full | .1883 | .01083 | [.5176,.5210] | [.5267,.5295] |
| 800.5 | half | .3123 | .00898 | [.4160,.4214] | same |
| 1600.5 | full | .1422 | .00737 | [.3876,.3930] | same |
| 1600.5 | half | .2962 | .00777 | [.3214,.3248] | [.3226,.3247] |

The optimizers did not reliably inherit the source or the reflected pairs.
Four of ten used zero paired mass.  On half-shell sources the probability
mass assigned to the source ranged from `.00046` to `.317`, and
`||alpha-lambda_I||_1` ranged from `1.56` to `2.00`.  One phase-lift control
for each of the ten events preserved every source cosine, hence `t_0,M,D,e`,
to floating precision.  These are labelled source-matched controls: they do
not preserve log order, contiguity, spacing, or pair count, so they do not
isolate prime arithmetic alone.  The actual-versus-control difference changed
sign across centers.  At `Y=500.5` the actual value was lower than the gap and
phase-lift controls for both profiles (and lower than the order control for
the half profile); the full-profile order control is identical because it
only permutes the full source.  There is no stable actual-prime surplus in
this limited sample.

These events are not asymptotically legal at their small scales, and the
brackets use floating exchange plus curvature guards rather than interval
arithmetic.  They neither prove nor refute PWCT.  They do falsify the
heuristic that positivity automatically forces source overlap.

The thresholded active weights, active prime labels, controls, and residuals
are in `ZETA23-PWCT-FINITE-DIAGNOSTIC-2026-08-30.json`; replay code is
`src/qp_positive_weight_carrier_probe.py`.

### 6.2 Event-free carrier and diffuseness probe

Proposition 3.3 permits larger source-free tests.  On one shared exchange
pool, compare the unrestricted positive simplex, the carrier-positive
simplex, and the carrier-positive simplex with coordinate cap

```text
alpha_p<=4log(Y)/Y.                                  (6.1)
```

The common pool makes the three sampled lower values exactly ordered.  Each
returned candidate has a separate curvature-guarded continuum upper value.

| `Y` | primes / pairs | unrestricted | carrier | capped carrier |
|---:|:---:|:---|:---|:---|
| 500.5 | 31 / 2 | [.31044,.31315] | [.31329,.31602] | [.32423,.32716] |
| 1000.5 | 58 / 0 | [.22464,.22691] | same | [.22735,.22988] |
| 2000.5 | 103 / 1 | [.18572,.18816] | [.18575,.18819] | [.18731,.18971] |
| 4000.5 | 191 / 0 | [.14593,.14837] | same | [.14738,.14963] |
| 8000.5 | 360 / 0 | [.11612,.11855] | same | [.11739,.11977] |

The carrier itself contributed almost nothing in this range: three shells
had no close pair, and its largest sampled penalty was `.00285`.  The cap was
active at every center, but its sampled penalty fell from `.01095` to
`.00127` (from `3.5%` to `1.1%` of the uncapped carrier level).  Capped
effective support grew from `26.3/31` to `289.2/360`; sampled dual contact
count grew from `20` to `282`.  Thus the diffuse adapter is not visibly aimed
at the wrong finite optimizer class, but neither a bounded-contact template
nor a stable prime-pair effect appears.

The capped level fell from `.324` to `.117`.  This is compatible with a
fixed-power positive antenna and gives no evidence for a uniform positive
floor, but five small floating instances cannot determine an asymptotic
exponent.  All dual contact masses were `1+O(10^-9)` and all cap/pair
residual checks passed.

The serialized contacts and weights are in
`ZETA23-DELTA-PLUS-C-FINITE-DIAGNOSTIC-2026-08-30.json`; replay code and tests
are `src/qp_positive_antenna_probe.py` and
`src/test_qp_positive_antenna_probe.py`.

## 7. Final decision

The exact remaining positive branch is:

```text
alpha may avoid I or adaptively reweight it;
||alpha-lambda_I||_1>D/(1+epsilon);
A(alpha)>D/(1+epsilon);
P_eff(alpha)>>Y^(.0179);
a(alpha)<epsilon A(alpha).                           (7.1)
```

Resolving `(7.1)` requires either

1. a source-conditioned, positive, one-sided prime Turan theorem for diffuse
   adaptive weights; or
2. a scalable actual-prime construction of such a diffuse antenna.

Neither follows from source mass, carrier projection, or second/fourth
moments alone.  The smooth construction shows that any proof must use a
deterministic arithmetic property of actual prime logarithms strong enough
to defeat every diffuse adaptive positive weight.  Naming that property a
"source-conditioned positive prime Turan theorem" does not reduce PWCT.

The proof-or-counterexample ledger is therefore

```text
unpaired-event inheritance:                           PROVED
probability normalization and semi-infinite dual:     PROVED
small-A/source-time branch:                           CLOSED
low-participation branch:                             CLOSED
tested density/gap/source/positivity relaxations:     REFUTED
finite actual-prime arithmetic surplus:               NOT OBSERVED
PWCT on actual primes:                                OPEN
PWCT => full COSE:                                    FALSE (only y<=0)
PWCT + recorded signed DPA_P(.019):                   NO VALID ADAPTER
PWCT + diffuse positive PDPA_+(.019):                 VALID CONDITIONAL CLOSURE
uniform zero-free strip:                              NOT PROVED
RH:                                                   NOT PROVED
```

PWCT should therefore be demoted from the highest-value standalone target.
Proposition 3.2 supplies one useful sufficient adapter, but diffuse positive
`PDPA_+(.019)` is not a new program: it strictly strengthens the extensively
audited actual-prime positive-antenna problem.  Refuting the diffuse cap would
not close non-diffuse carrier antennas, whose participation need only be
`Y^(.019+o(1))`; no valid diffusification lemma is known.

The event-free comparison has now been run.  It did not falsify diffuseness:
the cap remained active but its relative penalty shrank, while both primal
support and dual contact count grew with the prime dimension.  It also
produced no low-complexity coefficient template and no meaningful carrier
effect.  Therefore the only live analytic continuation **within this PWCT
branch** is the already-known actual-prime adaptive convex-hull/covariance
problem, now with the capped
primal and its contact measure frozen exactly.  If no arithmetic structure
can be extracted from those contacts, this branch should return to the
signed KKT/quotient-graph program rather than rerun positive DPA under a new
name.  More PWCT moment work has negligible value because the diffuse
pseudo-prime model already saturates that proof class.
