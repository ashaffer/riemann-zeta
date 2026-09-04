# The target-subtracted carrier slice contains an unavoidable aligned baseline

Status: exact finite-dimensional no-gain theorem, exact full-carrier
collapse, and a matched prime-polynomial audit, 2026-08-12.  This prunes the
target-subtracted support functional as an independent route.  It proves no
uniform zero-free strip and makes no assertion about an unconstructed
different quotient or carrier.

## 1. Verdict

The high-height carrier-slice reduction has an exact obstruction which is
stronger than a failed numerical fixture.

On the target positive-null quotient, the selected reflected pair is
`-N_T`.  Therefore the target-subtracted full remainder is identically

```text
R_full,T = N_T + K_ar,T|S_T.                         (1.1)
```

Likewise, on the exact mirror quotient, the target-subtracted cross
remainder is

```text
R_cross,T = c_T*N_T + B_ar,T|S_T.                    (1.2)
```

The terms `N_T` and `c_T*N_T` are not collateral reservoirs.  They are the
aligned target baselines introduced by subtracting the selected negative
block.  They have to be restored before the arithmetic form is evaluated.

This gives three exact consequences.

1. Every carrier fraction `theta<1` admits the top carrier state.  If the
   completed arithmetic operator is `o(kappa_T)`, then

   ```text
   h_(theta*kappa_T)(R_full,T)=kappa_T+o(kappa_T),
   ```

   not `o(kappa_T)`.  Thus the target-subtracted support gate automatically
   admits a reservoir at every fixed fraction below one.
2. At full carrier the support problem collapses to one arithmetic scalar:

   ```text
   h_kappa(R_full)<kappa
     iff <a_hat,K_ar,T*a_hat><0.                     (1.3)
   ```

   There is no remaining SDP or complement estimate.  The cross version
   similarly collapses to the sign of `<a_hat,B_ar,T*a_hat>`.
3. The exact constrained arithmetic functional

   ```text
   q_eta=max_(Gamma in F_eta) Tr(K_ar,T Gamma)
   ```

   and the target-subtracted support obey

   ```text
   q_eta+eta <= h_eta(R_full,T) <= q_eta+kappa_T.     (1.4)
   ```

   The support functional therefore loses as much as
   `(1-theta)*kappa_T` relative to the direct arithmetic optimization.  At
   full carrier the two sides of (1.4) coincide.

There is also an exact dual explanation.  Put

```text
Phi_eta(nu)=lambda_max(K_ar,T|S_T+nu*N_T)-nu*eta.
```

Then, for `eta<kappa_T`,

```text
q_eta(K_ar,T)=inf_(nu>=0) Phi_eta(nu),
h_eta(R_full,T)=eta+inf_(nu>=1) Phi_eta(nu).          (1.5)
```

Target subtraction does not create a new pencil.  It deletes the dual range
`0<=nu<1` and adds `eta`.  This is the exact source of the support loss.

Consequently separate estimates for the carrier diagonal, complement edge,
and transverse coupling do not open a new route.  After the aligned baseline
is removed, they are exactly the corresponding three blocks of the original
completed arithmetic operator.  The mathematically faithful next object is
`q_eta(K_ar,T)` (or its cross analogue), not
`h_eta(K_ar,T-K_0,T)`.

For the localized two-packet realization, the surviving top-carrier scalar
contains the same smooth centered von Mangoldt polynomial already isolated
in the endpoint-packet theorem card.  The available KMT **upper bound** has
size `Y^(1/2)/(log Y)^(3/10)`, whereas a fixed-depth carrier has size
`Y^alpha`.  The ratio `Y^(1/2-alpha)/(log Y)^(3/10)` diverges for every
fixed `alpha<1/2`.  A fixed-power improvement sufficient at every selected
ordinate is therefore the already identified strip-strength arithmetic
input, not a consequence of rank-one carrier slicing.

## 2. Exact aligned-baseline theorem

Let `S` be a finite-dimensional Hilbert space, let `a` be a unit vector,
and put

```text
N=kappa*a*a^*,                 kappa>0.              (2.1)
```

For `0<=eta<=kappa`, let

```text
F_eta={Gamma>=0: Tr Gamma=1, Tr(N Gamma)>=eta}.      (2.2)
```

For a Hermitian operator `K`, define

```text
q_eta(K)=max_(Gamma in F_eta) Tr(K Gamma),
h_eta(R)=max_(Gamma in F_eta) Tr(R Gamma).           (2.3)
```

### Theorem 2.1 (baseline sandwich and full-carrier collapse)

If `R=K+N`, then

```text
q_eta(K)+eta <= h_eta(R) <= q_eta(K)+kappa.          (2.4)
```

At the boundary,

```text
q_kappa(K)=<a,K*a>,
h_kappa(R)=kappa+<a,K*a>.                           (2.5)
```

In particular, for `eta=theta*kappa`,

```text
h_eta(R)<eta  implies  q_eta(K)<0,                  (2.6)

q_eta(K)<-(1-theta)*kappa
              implies  h_eta(R)<eta.                (2.7)
```

At `theta=1`, (2.6)--(2.7) are equivalent and reduce to

```text
h_kappa(R)<kappa iff <a,K*a><0.                     (2.8)
```

For `eta<kappa`, define

```text
Phi_eta(nu)=lambda_max(K+nu*N)-nu*eta.              (2.9)
```

Then exactly

```text
q_eta(K)=inf_(nu>=0) Phi_eta(nu),
h_eta(K+N)=eta+inf_(nu>=1) Phi_eta(nu).             (2.10)
```

Thus the target-subtracted support is the same scalar dual with its
multiplier interval truncated at one.

#### Proof

For every `Gamma in F_eta`,

```text
eta<=Tr(N Gamma)<=kappa.                             (2.11)
```

Evaluate `R=K+N` first at a maximizer of `q_eta(K)` and then at a maximizer
of `h_eta(R)`.  The lower and upper inequalities in (2.4) follow
respectively.  When `eta=kappa`, equality in
`Tr(N Gamma)<=kappa Tr Gamma` forces `Gamma=a*a^*`, proving (2.5).  Equations
(2.6)--(2.8) are immediate.  Finite-dimensional SDP duality gives

```text
q_eta(K)=inf_(mu>=0)
  [lambda_max(K+mu*N)-mu*eta].                      (2.12)
```

Applying the same formula to `K+N` and substituting `nu=mu+1` proves
(2.10).  QED

### Corollary 2.2 (small arithmetic norm makes the support gate pass)

If

```text
||K||<=epsilon*kappa,                               (2.13)
```

then, for every `0<=theta<=1`,

```text
(1-epsilon)*kappa
 <=h_(theta*kappa)(K+N)
 <=(1+epsilon)*kappa.                               (2.14)
```

Hence if `theta<1-epsilon`, then

```text
h_(theta*kappa)(K+N)>theta*kappa.                   (2.15)
```

In particular, any successful proof that the completed arithmetic operator
is `o(kappa)` makes the target-subtracted support functional asymptotic to
one full carrier and causes every fixed sub-full threshold to pass.

#### Proof

The top carrier state `a*a^*` belongs to every `F_(theta*kappa)` and has
expectation at least `kappa-||K||`.  Every state has `N`-expectation at most
`kappa` and `K`-expectation at most `||K||`.  QED

### Corollary 2.3 (the three proposed estimates are the old arithmetic
blocks)

Write `S=C*a direct_sum a^perp` and decompose

```text
K=[[q_0,g^*],[g,E]].                                (2.16)
```

Then

```text
K+N=[[kappa+q_0,g^*],[g,E]].                        (2.17)
```

Thus for the target-subtracted remainder

```text
r_0=kappa+q_0,
b=g,
D=E.                                                (2.18)
```

The carrier diagonal contains a deterministic full-carrier baseline.  The
transverse coupling and complement edge are precisely the transverse and
complement blocks of `K`; target subtraction does not regularize either of
them.

## 3. Application to the completed full form

Use the notation of
[`ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md`](ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md).
On `S_T=ker(x_0^*)`, the selected pair satisfies

```text
K_0,T|S_T=-N_T.                                     (3.1)
```

By definition,

```text
R_full,T=(K_ar,T-K_0,T)|S_T.                        (3.2)
```

Combining (3.1)--(3.2) proves the exact identity (1.1):

```text
R_full,T=N_T+K_ar,T|S_T.                            (3.3)
```

Theorem 2.1 now gives (1.4), and (2.18) becomes

```text
r_0=kappa_T+<a_hat,K_ar,T*a_hat>,
b=P_(a_hat^perp)*K_ar,T*a_hat,
D=P_(a_hat^perp)*K_ar,T|a_hat^perp.                 (3.4)
```

This also clarifies the logical roles of the two functionals.

```text
h_eta(R_full,T)       target-subtracted support, with aligned baseline;
q_eta(K_ar,T)         direct completed-arithmetic constrained edge.       (3.5)
```

The inequality `h_eta<eta` is a sufficient way to prove `q_eta<0`, but it
is stronger by up to `(1-theta)*kappa_T`.  Since `q_eta` already has the
same scalar dual and a rank-one optimizer, passing through `h_eta` supplies
no convexity or computational gain.  More precisely, (1.5) shows that it
throws away all candidate dual minimizers in `0<=nu<1`.

At full carrier,

```text
h_kappa(R_full,T)<kappa_T
 iff Q_T(a_hat)<0.                                  (3.6)
```

Thus a full-carrier support certificate is exactly one target-adaptive
negative completed Weil value.  To turn it into a zero exclusion still
requires an independent arithmetic lower bound for the same value.  The
carrier slice does not provide that lower bound.

## 4. Application to the aggregate cross form

On the exact mirror quotient the selected cross block is

```text
B_0,T|S_T=-c_T*N_T.                                 (4.1)
```

Since `R_cross,T=(B_ar,T-B_0,T)|S_T`, one has (1.2):

```text
R_cross,T=c_T*N_T+B_ar,T|S_T.                       (4.2)
```

Applying Theorem 2.1 after replacing `N_T` by `c_T*N_T` **and the threshold
`eta` by `c_T*eta`** (the feasible states themselves are unchanged) gives
the direct top-state lower bound

```text
h_(theta*kappa_T)(R_cross,T)
 >=c_T*kappa_T+<a_hat,B_ar,T*a_hat>.                (4.3)
```

Consequently, if

```text
||B_ar,T|S_T||<=epsilon*kappa_T,                    (4.4)
```

then the necessary aggregate admission condition

```text
h_(theta*kappa_T)(R_cross,T)>=c_T*theta*kappa_T     (4.5)
```

holds automatically whenever

```text
epsilon<=c_T*(1-theta).                             (4.6)
```

At full carrier it reduces exactly to

```text
h_kappa(R_cross,T)>=c_T*kappa_T
 iff <a_hat,B_ar,T*a_hat>>=0.                       (4.7)
```

The scalar in (4.7) is the actual completed aggregate cross correlation.
No complement or transverse estimate survives at the boundary.

For `eta<kappa_T`, the exact cross dual has the parallel truncation

```text
h_eta(R_cross,T)
 =c_T*eta+inf_(nu>=c_T)
   [lambda_max(B_ar,T|S_T+nu*N_T)-nu*eta].           (4.8)
```

The direct completed-cross functional uses the identical bracket with
`nu>=0`.

## 5. What the actual von Mangoldt bounds do

For the normalized endpoint-flat two-packet carrier, let

```text
Y=exp(D_T),
kappa_T=Y^(alpha+o(1))/L.                           (5.1)
```

Up to the already audited same-lobe and completion errors, the top-carrier
cross scalar in (4.7) is the smooth centered polynomial

```text
S_(Y,w)(gamma)
 =integral v^(-1/2)*omega_(T,w)(log(v/Y))
                  *cos(gamma*log v)d(psi(v)-v).     (5.2)
```

All von Mangoldt coefficients and the continuum completion are retained.
The published KMT estimate used in the endpoint-packet report gives, in its
applicable polynomial height/length range,

```text
S_(Y,w)(gamma)
 <<_w Y^(1/2)/(log Y)^(3/10).                       (5.3)
```

For fixed `alpha<1/2`, its ratio to the carrier numerator is

```text
Y^(1/2-alpha)/(log Y)^(3/10) -> infinity.           (5.4)
```

Neither the Loewner displacement identity nor the rank-one slice changes
this exponent: (3.4) shows that they merely place the same completed
arithmetic operator into carrier/complement coordinates.

There is a narrow moving-depth regime in which (5.3) really is subcarrier.
Write

```text
alpha=1/2-delta_Y.                                  (5.5)
```

For every fixed `epsilon>0`, if

```text
delta_Y*log Y
 <=(3/10-epsilon)*loglog Y,                         (5.6)
```

then

```text
S_(Y,w)(gamma)=o(Y^alpha).                          (5.7)
```

Indeed the quotient in (5.4) is at most
`(log Y)^(-epsilon)`.  This is a genuine arithmetic subcarrier estimate,
but it illustrates the no-gain theorem rather than defeating it: when the
other packet and completion terms are also `o(kappa_T)`, (2.5) gives

```text
h_kappa(R_full,T)=kappa_T+o(kappa_T),               (5.8)
```

and (2.14)--(2.15) make every fixed sub-full carrier fraction pass.  Moreover the
region (5.6) lies much closer to `Re(s)=1` than the classical zeta zero-free
region and therefore supplies no new zeta theorem.

For a fixed depth, replacing (5.3) by the matched estimate

```text
S_(Y,w)(gamma)=o(Y^alpha)                            (5.9)
```

uniformly at every candidate selected ordinate is exactly the
fixed-power prime-polynomial input isolated in the endpoint-packet and
confluent-Loewner reports.  Coupled with a signed carrier-isolation theorem,
it excludes a depth-`alpha` pair.  In that precise sense the missing bound
is strip-strength; carrier slicing does not make it weaker.

## 6. Checks of the proposed escape routes

### Positivity of the von Mangoldt coefficients

The prime quadratic form contains translated correlations multiplied by
`cos(gamma*log n)` and is centered by `d(psi-v)`.  It is not a positive
measure pairing.  Replacing it by its absolute positive majorant costs
`Y^(1/2+o(1))`, which is larger than `Y^alpha` for every fixed
`alpha<1/2`.

### Large sieve or local mean square

The target ordinate is selected pointwise.  The opposite-lobe packet has
fixed modulation bandwidth, so a phase average long enough for a standard
mean-square gain is unavailable without reducing the selected evaluation
by the same factor.  This is the endpoint-packet phase-averaging obstruction.

### Displacement rank two

Confluent Loewner structure reconstructs the arithmetic matrix from two
scalar prime polynomials, but its diagonal remains free at the structural
level.  Equation (3.4) shows that displacement does not remove the aligned
`kappa_T` baseline and does not sign the remaining arithmetic blocks.

### Completion

Exact pole completion replaces `d psi` by the centered measure
`d(psi-v)` plus the audited rational/gamma remainder.  It produces (5.2),
not zero.  Dropping the ordinary recompleted component would change the
arithmetic problem.

### Near-tie collateral zeros

Depth stratification remains useful for interpreting the zero side, but it
does not alter (3.3).  A shallow/deep decomposition of `R_full,T` must carry
the aligned `N_T` baseline somewhere, because the exact arithmetic identity
forces it.  Calling every nonselected summand `o(kappa_T)` while also proving
`K_ar,T=o(kappa_T)` is consistent only because their sum restores `N_T`.

## 7. Revised theorem card

The rank-one carrier program should use the following order.

```text
DO NOT TARGET
  h_eta(K_ar,T-K_0,T) as though K_ar,T-K_0,T were a small independent
  collateral remainder.  It contains the aligned baseline N_T.

TARGET DIRECTLY
  q_eta(K_ar,T)
    =max_(Gamma>=0, Tr Gamma=1, Tr(N_T Gamma)>=eta)
       Tr(K_ar,T Gamma),
  or the corresponding completed cross functional.

FULL CARRIER
  Evaluate the single scalar Q_T(a_hat), with every von Mangoldt,
  pole, and gamma term retained.

SUB-FULL CARRIER
  Any proof through target-subtracted support pays an artificial loss up
  to (1-theta)*kappa_T.  Use the direct scalar dual for q_eta instead.

ARITHMETIC GATE
  A fixed-depth conclusion still requires a matched fixed-power estimate
  for the centered smooth von Mangoldt polynomial, or a direct constrained
  Pick/Loewner sign theorem of the same carrier scale.
```

This does not prove that every conceivable carrier construction fails.  It
proves that the presently defined **target-subtracted rank-one support
functional** is not an independent screening theorem: after exact
bookkeeping, its only nontrivial content is the original constrained
completed-arithmetic sign problem.

Principal inputs:

- [`ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md`](ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md),
- [`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`](ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md),
- [`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md), and
- [`ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md`](ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md).
