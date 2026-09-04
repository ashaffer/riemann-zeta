# Christoffel profile-design concentration barrier

**Date:** 2026-08-13

**Verdict:** broad continuous high-band designs cannot give subpower
directional leverage.  This includes normalized Lebesgue measure, the
arcsine equilibrium measure, fixed-profile Toeplitz/prolate surrogates with
the stated uniform Fourier decay,
mixtures of translated broad packets, and every randomized or leverage-score
discretization which spectrally approximates one of those covariances.

The obstruction is theorem-grade and applies to the **actual prime-power
nodes** (in fact, to every subset of the integer nodes in the same fixed
multiplicative window).  For the principal carrier `q=a(0)`, a profile of
frequency width `ell=Y^a` whose Fourier transform decays with exponent
`gamma` has directional Christoffel cost at least

```text
sqrt(q^T G_rho^dagger q) >= Y^(a*gamma/2-o(1)).           (0.1)
```

Thus an arcsine/equilibrium packet (`gamma=1/2`) wider than
`Y^(.0721212936+epsilon)` and a bounded-variation packet (`gamma=1`) wider
than `Y^(.0360606468+epsilon)` already exceed the required
`Y^.0180303234` obstruction.  On the full band, the arcsine Christoffel cost
is at least `Y^(25/66-o(1))`, while the normalized-Lebesgue cost is at least
`Y^(1/2-o(1))`.

This does **not** prove the global actual-node obstruction.  An optimal
`c`-design can be atomic and need not have Fourier decay.  The theorem says
precisely what any surviving subpower design must do: concentrate on packets
narrower than the displayed threshold or amplify some covariance direction
by almost a factor `Y` relative to Lebesgue.  That singular atomic branch is
the remaining arithmetic Christoffel problem.

No zeta bound or zero-free strip is claimed.

---

## 1. Exact design problem and carrier normalization

Fix `0<w<1` and let

```text
N_Y={p^k : Y*exp(-w) <= p^k <= Y*exp(w)},
u_n=log(n/Y),
a(t)=(cos(t*u_n))_(n in N_Y),
M=#N_Y.                                                    (1.1)
```

For a legal high-band probability measure `rho`, put

```text
G_rho=integral a(t)a(t)^T d rho(t).                       (1.2)
```

If `q` is not in `range(G_rho)`, set its leverage to `+infinity`.
Otherwise the exact directional Christoffel identity is

```text
R_H(q)^2=inf_(rho in Prob(H)) q^T G_rho^dagger q,         (1.3)
```

where `R_H(q)` is the least total variation of a signed high-band measure
representing `q`.

The principal carrier is

```text
q_0=a(0)=(1,...,1),       ||q_0||^2=M.                    (1.4)
```

For the target used in the prime-log extremal,

```text
b(t)=integral_(-w)^w (1-|u|/w)*exp(alpha*u)*cos(t*u)du,
b_0=b(0)=2*(cosh(alpha*w)-1)/(w*alpha^2)>0,               (1.5)
```

with the continuous value `b_0=w` when `alpha=0`.  The exactly normalized
low carrier is `nu=b_0^(-1) delta_0`; it has target value one and feature
vector `q_0/b_0`.  Write

```text
L_rho(q_0)=q_0^T G_rho^dagger q_0.                       (1.6)
```

The least `L^2(rho)` density representing `q_0` has norm
`sqrt(L_rho(q_0))`.  Its carrier-normalized low-plus-high certificate has
the corresponding upper cost

```text
C_(2,rho)=(1+sqrt(L_rho(q_0)))/b_0.                      (1.7)
```

This is an `L^2` Christoffel quantity, not the exact `L^1` cost for one fixed
base measure.  Globally, (1.3) says

```text
C_principal=(1+R_H(q_0))/b_0,
R_H(q_0)^2=inf_rho L_rho(q_0).                            (1.8)
```

Thus excluding a class of `rho` excludes that class from attaining the
atomic optimum.  A small-`L^1` density against a broad base measure induces
the new probability design `|f|rho/||f||_1`, which may be singular and must
be audited separately.  There is no hidden carrier-normalization loss in
the exponents below.

---

## 2. Actual-node packing lemma

Put `v_n=|u_n|`.  Only the fact that the `n` are distinct integers is used.

### Lemma 2.1 (two-branch logarithmic packing)

For every interval `I` in `[0,w]` of length `r`,

```text
#{n in N_Y : v_n in I} <= C_w*(1+Y*r).                   (2.1)
```

#### Proof

On the branch `n>=Y`, the inverse map is `n=Y exp(v)`.  The integer interval
corresponding to `I=[x,x+r]` has length at most
`Y exp(w)(exp(r)-1)<=C_w Y r`.  Hence it contains at most
`1+C_w Y r` distinct integers.  The branch `n<=Y`, with inverse
`n=Y exp(-v)`, obeys the same estimate.  Adding the two branches proves
(2.1).  Prime powers are a subset of these integer nodes, so no prime-gap or
equidistribution input is needed.  QED.

As a consequence, after ordering distances from any fixed `v_i`, the
`k`-th point is at distance at least `c_w k/Y`, up to a fixed multiplicity.
For `0<gamma<1`, this gives

```text
sup_i sum_j (1+ell*|v_i-v_j|)^(-gamma)
 <=C_(w,gamma)*[1+Y/ell
       +(Y/ell)^gamma*M^(1-gamma)].                       (2.2)
```

Indeed, split off `O(Y/ell+1)` points within distance `1/ell` and compare
the remaining rank sum with the integral of `x^(-gamma)`.  At the endpoint
`gamma=1`, the same proof gives

```text
sup_i sum_j (1+ell*|v_i-v_j|)^(-1)
 <=C_w*[1+(Y/ell)*(1+log(2+M*ell/Y))].                   (2.3)
```

These estimates automatically handle almost-reflected nodes.  The two
logarithmic branches may put two nodes very close in `v`, but (2.1) bounds
that local multiplicity uniformly; no false minimum-separation assumption
is being made.

---

## 3. Fourier-profile leverage theorem

The Fourier transform convention in this section is

```text
rho_hat(omega)=integral exp(i*omega*t)d rho(t).           (3.1)
```

### Theorem 3.1 (broad-profile directional obstruction)

Suppose a legal high-band probability design obeys

```text
|rho_hat(omega)| <= A*(1+ell*|omega|)^(-gamma)            (3.2)
```

for some `A>=1`, `ell>=1`, and `0<gamma<1`.  Then, with the usual infinite
value when the range condition fails,

```text
q_0^T G_rho^dagger q_0
 >= c_(w,gamma)*M /
    {A*[1+Y/ell+(Y/ell)^gamma*M^(1-gamma)]}.              (3.3)
```

For `gamma=1`, the denominator in braces is replaced by

```text
A*[1+(Y/ell)*(1+log(2+M*ell/Y))].                         (3.4)
```

The same conclusions hold, up to a fixed constant, for every phase carrier
`q_s=a(s)` satisfying `||q_s||^2>=kappa M`.  In particular this is uniform
for `s` in any fixed compact set: the prime number theorem gives

```text
M^(-1)||a(s)||^2
 -> [integral_(-w)^w exp(u)cos^2(su)du]
       /[integral_(-w)^w exp(u)du],                       (3.5)
```

and the positive continuous limit has a positive minimum on a compact
`s`-set.  Thus the obstruction includes the numerically dominant carrier
near `s=6--8`, not only the convenient principal vector at zero.

#### Proof

The product-to-sum identity gives

```text
(G_rho)_(ij)
 =1/2 Re[rho_hat(u_i-u_j)+rho_hat(u_i+u_j)].              (3.6)
```

The two absolute frequencies occurring on the right are
`|v_i-v_j|` and `v_i+v_j`.  Since the majorant in (3.2) decreases,

```text
|(G_rho)_(ij)| <=A*(1+ell*|v_i-v_j|)^(-gamma).            (3.7)
```

The Schur row-sum test and (2.2) therefore give the corresponding upper
bound for `||G_rho||_op`.  If `q_0` lies in the range, Cauchy--Schwarz in
the `G_rho^(1/2)` and `G_rho^(-1/2)` metrics gives

```text
(q_0^T G_rho^dagger q_0)*(q_0^T G_rho q_0)
 >=||q_0||^4=M^2.                                        (3.8)
```

But `q_0^T G_rho q_0<=M*||G_rho||_op`.  Combining these facts proves (3.3).
If the range condition fails, the left side is infinite and the result is
automatic.  Formula (2.3) proves the endpoint case.  Replacing `q_0` by any
`q_s` and using

```text
q_s^T G_rho^dagger q_s>=||q_s||^2/||G_rho||_op           (3.9)
```

proves the extension.  The fixed-compact prime-number-theorem limit is
standard partial summation, and its numerator cannot vanish because
`cos(su)` is not identically zero on an interval.  QED.

### Corollary 3.2 (fixed-power threshold)

The prime number theorem gives `M=Y^(1-o(1))`.  If
`ell>=Y^a`, `A=Y^o(1)`, and `0<gamma<1`, Theorem 3.1 implies

```text
sqrt(L_rho(q_0))
 >=Y^(min(1,a*gamma)/2-o(1)).                             (3.12)
```

In the range relevant here, `a*gamma<1`, this is (0.1).  Consequently every
such design with

```text
a*gamma>2*delta_*,       delta_*=.0180303234,             (3.10)
```

has directional Christoffel cost strictly beyond the required threshold.

Translations of the profile only multiply its Fourier transform by a phase
and do not affect the proof.  More generally, if

```text
rho=sum_r theta_r rho_r,    theta_r>=0, sum_r theta_r=1,  (3.11)
```

and every `rho_r` satisfies (3.2) with the same `A,gamma` and a scale at
least `ell`, then `rho` also satisfies (3.2).  Thus (3.12) covers arbitrary
multiscale mixtures provided their narrowest packet has the stated width.

---

## 4. Explicit equilibrium and Lebesgue consequences

Let a fixed probability profile `sigma` be rescaled to an interval of width
`ell`.  If

```text
|sigma_hat(x)|<=A*(1+|x|)^(-gamma),                       (4.1)
```

then its rescaling satisfies (3.2).

### 4.1 Arcsine/equilibrium design

The arcsine probability density on an interval of width `ell` has transform

```text
exp(i*c*omega)*J_0(ell*omega/2).                          (4.2)
```

The standard Bessel bound is `|J_0(x)|<=C(1+|x|)^(-1/2)`.
Thus `gamma=1/2`.  At the full legal width

```text
ell=Y^(50/33+o(1)),                                      (4.3)
```

(3.12) gives

```text
sqrt(L_rho(q_0))>=Y^(25/66-o(1))
                  =Y^(.378787...-o(1)).                  (4.4)
```

Even a mixture of translated arcsine packets is killed once every packet
has width

```text
ell>=Y^(4*delta_*+epsilon)
    =Y^(.0721212936+epsilon).                             (4.5)
```

### 4.2 Uniform and bounded-variation profiles

Normalized Lebesgue measure on an interval of width `ell` has a sinc
transform and satisfies (3.2) with `gamma=1`.  The endpoint estimate gives

```text
sqrt(L_rho(q_0))>=Y^(min(1,a)/2-o(1)) when ell=Y^a.       (4.6)
```

In particular the full high interval gives
`sqrt(L_rho(q_0))>=Y^(1/2-o(1))`.
Any mixture of bounded-variation fixed profiles with packet widths

```text
ell>=Y^(2*delta_*+epsilon)
    =Y^(.0360606468+epsilon)                              (4.7)
```

already exceeds the target.

The same conclusion applies to broad Toeplitz/prolate surrogate densities
whenever their rescaled Fourier transforms obey a uniform fixed-profile
decay estimate.  A name such as "equilibrium" or "prolate" supplies no
escape from the carrier leverage; only loss of the broad-profile estimate
can do so.

---

## 5. Density, leverage-score sampling, and Loewner domination

Let `m_H` be normalized Lebesgue measure on a high interval of length
`asymp Y^(50/33)`.  The preceding sinc calculation gives

```text
q_0^T G_(m_H)^dagger q_0 >=c_w M.                         (5.1)
```

Suppose another legal design satisfies the covariance domination

```text
G_rho <=D*G_(m_H)                                        (5.2)
```

in Loewner order.  This includes every density with
`d rho/dm_H<=D`, and it is exactly the kind of guarantee produced by a
spectral sparsification or a successful leverage-score sampling theorem.
Then

```text
q_0^T G_rho^dagger q_0 >=c_w*M/D.                        (5.3)
```

To see this without any invertibility assumption, use (3.8) and
`q_0^T G_rho q_0<=D q_0^T G_(m_H)q_0<=C_w D M`.

Since `M=Y^(1-o(1))`, for every fixed `epsilon>0`,

```text
D<=Y^(1-2*delta_*-epsilon)
  =Y^(.9639393532-epsilon)                               (5.4)
```

forces

```text
sqrt(L_rho(q_0))>=Y^(delta_*+epsilon/3)                   (5.5)
```

for all sufficiently large `Y`.  In particular, every `D=Y^o(1)`
Lebesgue perturbation, randomized phase design, or covariance-preserving
leverage sampler has essentially square-root cost.  Leverage-score sampling
can compress the number of atoms while preserving a covariance; it cannot
turn an order-`M` directional leverage into a subpower one.

Conversely, any successful subpower design must violate (5.2) for every
`D<=Y^(1-o(1))`.  Equivalently, it must amplify at least one feature-space
direction by almost a full factor `Y` relative to the broad high-band
covariance.  This is a useful, falsifiable concentration certificate.

---

## 6. Every subpower design must live on extreme prime-phase peaks

The preceding concentration conclusion can be made intrinsic, without
assuming a density or profile.  Put

```text
S_Y(t)=<q_0,a(t)>=sum_(n in N_Y) cos(t*log(n/Y)),
E_eta={t in H: |S_Y(t)|>=M*Y^(-eta)}.                    (6.1)
```

Take `H` to be an interval of length `asymp Y^(50/33)`.  The sinc case of
Theorem 3.1, or equivalently the Montgomery--Vaughan mean-value inequality
applied separately to the two logarithmic branches, gives

```text
(1/|H|)*integral_H |S_Y(t)|^2 dt <=C_w M.                (6.2)
```

Consequently

```text
|E_eta|/|H| <=C_w*Y^(2*eta)/M
             =Y^(-1+2*eta+o(1)).                        (6.3)
```

Now let `rho` be **any** legal design, including an atomic one, and write
`L=L_rho(q_0)`.  Equation (3.8) says

```text
integral |S_Y(t)|^2 d rho(t) >=M^2/L.                    (6.4)
```

Since `|S_Y(t)|<=M`, splitting this integral over `E_eta` yields the exact
mass bound

```text
rho(E_eta)
 >=[L^(-1)-Y^(-2*eta)]/[1-Y^(-2*eta)]                   (6.5)
```

whenever the numerator is positive.

### Corollary 6.1 (exceptional-set necessity)

If `L_rho(q_0)=Y^o(1)`, then for every fixed `eta>0`,

```text
rho(E_eta)>=Y^(-o(1)),
|E_eta|/|H|<=Y^(-1+2*eta+o(1)).                          (6.6)
```

Thus a subpower design must place subpower mass on frequencies where the
unweighted actual prime-power cosine sum loses **every fixed power** of
cancellation, even though those frequencies occupy only a
`Y^(-1+o(1))` fraction of the band as `eta` tends to zero.  This is stronger
than saying that the optimizer may be atomic: it identifies the exact
arithmetic exceptional set on which its atoms must live.

At the finite target `sqrt(L)<=Y^delta_*`, choose any
`eta=delta_*+epsilon`.  Equations (6.3)--(6.5) force mass of order at least
`Y^(-2*delta_*+o(1))` on a set of relative Lebesgue measure at most
`Y^(-1+2*delta_*+2*epsilon+o(1))`.  Any successful threshold design must
therefore amplify this explicit prime-phase peak set by a fixed power.

What remains missing is a theorem that these rare extreme atoms fail to
span `q_0` with the required directional covariance.  A measure estimate
alone cannot supply that span theorem, which is why (6.3) is not promoted to
a global leverage lower bound.

---

## 7. Hostile scope audit and remaining branch

The theorem closes the following proposed shortcuts:

```text
normalized Lebesgue design                         POWER-OBSTRUCTED;
continuous arcsine/equilibrium design              POWER-OBSTRUCTED;
fixed-profile broad Toeplitz/prolate surrogate     POWER-OBSTRUCTED;
mixtures with no sufficiently narrow packet        POWER-OBSTRUCTED;
spectral/leverage-score sparsification of these    POWER-OBSTRUCTED;
random samples which preserve the base covariance  POWER-OBSTRUCTED. (7.1)
```

It deliberately does not claim any of the following:

```text
all atomic legal designs are obstructed             NOT PROVED;
the actual optimum obeys Loewner domination         FALSE IN GENERAL;
prime-phase exceptional atoms have small span       NOT PROVED;
full carrier-aware C_(L,H)>=Y^delta                 NOT PROVED;
uniform zero-free strip                             NOT PROVED.       (7.2)
```

The optimal-design identity permits an optimizer supported on finitely many
frequencies, so absolute continuity cannot be assumed.  The surviving
binary problem is therefore narrower than before:

> Either construct an atomic/narrow-packet design which violates broad
> covariance domination by `Y^(1-o(1))` **in the principal carrier
> direction**, or prove that the actual prime-log phase curve has no such
> exceptional spanning set.

Lebesgue large values, determinant volume, ordinary equilibrium measures,
and randomized covariance preservation do not address that last statement.

---

## 8. Reproduction

The floating diagnostic

```bash
python3 results/verify_christoffel_profile_barrier.py
```

builds the actual prime-power nodes, evaluates the exact uniform-interval
and arcsine-profile Gramians (sinc and `J_0` formulas), and reports the
directional leverages for the principal carrier and for `a(7)`.  It is a
reproducibility check on the formulas, not part of the asymptotic proof
above.
