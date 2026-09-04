# ZETA23 pole-killing correction revalidation and route audit

Date: 2026-09-01  
Status: corrected theorem/decision ledger; uniform strip and RH remain open  
Primary theorem suite:
[`ZETA23-GENERAL-POLE-KILLING-BOUNDARY-CALCULUS-2026-09-01.md`](ZETA23-GENERAL-POLE-KILLING-BOUNDARY-CALCULUS-2026-09-01.md)

Execution follow-up:
[`ZETA23-ENDPOINT-FLAT-JORDAN-MASS-AND-RIESZ-VARIATION-GATE-2026-09-01.md`](ZETA23-ENDPOINT-FLAT-JORDAN-MASS-AND-RIESZ-VARIATION-GATE-2026-09-01.md)

## 0. Revalidated verdict

The corrections were structural.  They invalidate the broad statement

```text
all fixed pole-killing filters are spectrally powerless,
```

and replace it with a three-regime theorem:

1. endpoint-normalized uniform-symbol rational filters preserve a fixed
   singularity at leading order;
2. endpoint-flat rational/fractional filters attenuate it algebraically; and
3. compact filters can demodulate it at a far support edge in the certified
   negative-real sectors.

Consequently, endpoint-flat and compact filters must not be labelled closed
by the old rational `1/omega` obstruction.  They are legitimate direct
Landau spectrometers.

The revalidation does **not** yet prove that either family is a reduced route
to a strip.  The weakest scalar direct-Landau premise is control of the
Laplace abscissa of one globally selected Jordan part, equivalently a
subcritical unit-block bad-mass exponent.  A pointwise one-sided
`O(exp(eta*t))` envelope is sufficient but is not necessary.  For the
consecutive-rate endpoint-flat family, the follow-up proves that both
Jordan-part exponents equal the rightmost-zero abscissa `Theta`; the weaker
premise is therefore an exact strip reformulation, not a proved arithmetic
simplification.  For the proposed compact
far-edge derivation, vertical/Stokes uniformity and multiplier coverage are
earlier open adapters.  Thus the corrected filters change more than notation,
but no completed reduction has yet been established.

The revised global status is therefore:

```text
endpoint-normalized rational no-gain theorem:       PROVED, scoped
endpoint-flat rational Landau criterion:            VALID, premise OPEN
compact direct Landau criterion:                    VALID with noncancellation;
                                                    premise OPEN
compact edge-to-envelope derivation:                needs vertical/Stokes and
                                                    quantifier adapters
one-center germ -> unbounded vertical strip:        NOT A VALID ADAPTER
uniform zero-free strip:                            OPEN
RH:                                                 OPEN
```

The QP/Turan locks and the Weil adjacent-support edge are unaffected.  This
calculus is a third, logically separate fixed-strip architecture.  A small
fixed strip still does not imply RH without an amplifier.

## 1. Correction dependency ledger

| Correction | Invalid broad inference | Revalidated statement | Decision effect |
|---|---|---|---|
| all moments do not control a moving hard endpoint | moments alone give every boundary jet | the `N`-jet needs a sampled endpoint rate, averaging, or `k(0)=0` | demotes unqualified all-order expansions; zeta fixed-`N` applications survive its stretched-exponential PNT error |
| fixed-singularity `1/omega` law is not universal | every fixed-order filter leaves a zero mode unchanged | the law holds for endpoint-normalized uniform-symbol filters | reopens endpoint-flat and compact filters as algebraic possibilities |
| endpoint flatness gives `epsilon^r/omega^(r+1)` | the inverse tax closes the filtered Landau route | the `epsilon^(-r)` tax is paid only when reconstructing the original observable; direct Landau exclusion does not invert | direct endpoint-flat eventual-envelope route is logically open |
| compact support has a second symbol edge | rational high-frequency obstruction applies to compact kernels | negative-ray continuation is governed by the far edge in a fixed sector | creates a real edge-demodulation mechanism |
| compact edge needs both tail and endpoint hypotheses | weighted moments suffice for the ordinary Stieltjes edge limit | require the weighted tail plus `t^r E(t)->0`, or use the integrated formula as a renormalized/distributional definition | blocks spike-based false edge limits |
| fractional compact tapers have a singular current edge | `k(0)=0` alone removes all moving-current-edge problems | impose `t^(alpha_T) E(t)->0`, where `alpha_T` is the far-edge scaling order (or use an equivalent uniform concentration condition), and split both kernel edges | narrows the fractional edge theorem |
| Volterra diagonal nonvanishing was only local | `p(0)k(0)!=0` gives stable inversion on every finite interval | it gives stable inversion near zero; global `[0,C]` inversion needs a uniform nonzero diagonal or resolvent condition | retains local identifiability, removes global stability language |
| finite jets are not the complete germ | zeros are absent from all local boundary data | finite jets miss them; the complete germ determines them abstractly | reopens only a global/translated-germ program, not finite-jet iteration |
| a single complete germ controls only its convergence disk quantitatively | one-center coefficient growth gives an unbounded half-plane | height-uniform translated germs or a global continuation theorem are required | removes one-center Laurent bounds as a strip adapter |
| a notch does not replace higher-pole centering | order-`p` pole killing alone gives a bounded higher-pole boundary layer | subtract the full principal polynomial; otherwise hard-cutoff terms of order `epsilon^(-j)` remain | closes the uncentered `zeta(s)^p` shortcut |
| positive kernels may have complex Laplace zeros | real-anchor positivity no-go extends to complex anchors | positivity forbids positive-real notches, not complex ones | corrects the sign theorem but supplies no zero-exclusion mechanism |
| fixed-`omega` asymptotics are not uniform strip estimates | response to one fixed zero describes a sequence approaching `Re(s)=1` at high height | a strip needs joint `(omega,epsilon)` and height-uniform bounds | prevents pointwise diagnostics from becoming a global theorem |
| finite-precision compact solves were ill-conditioned | numerical roots certify the exact Chebyshev theorem | exact ECT mathematics is analytic; replay is guarded high precision with residual checks | trust remains numerical replay, not interval/root certification |

## 2. The local theorem suite after correction

The following statements survive as project-proved analytic theorems in
their corrected scope.

### 2.1 Universal Stieltjes boundary identity

For `A=-C+E`, the exact integration-by-parts identity

\[
 R_\epsilon(c)=
 -C\Phi_c(0)+\Phi_c(c)E(c/\epsilon)
 -\epsilon\int_0^{c/\epsilon}\Phi_c'(\epsilon u)E(u)\,du
\]

and its leading compact-positive-`c` limit require only `E(t)->0` and the
recorded bounded-test hypotheses.  This theorem is unaffected.

### 2.2 Jets and germ calculus

Every fixed `N` moment expansion is valid with its explicit `N`th weighted
moment, test regularity, and hard-endpoint hypothesis.  Endpoint-flat kernels
remove the literal hard endpoint.  The fixed-dimensional identity

\[
 \mathcal S_\epsilon=
 H(-\epsilon(\sigma-\partial_c))k
\]

is valid on the stated invariant kernel space.  An `O_N(epsilon^N)` theorem
for each fixed `N` is not a uniform analytic statement as `N->infinity`.

### 2.3 Rational and fractional bidegree classification

For prescribed distinct real stable rates, notch order `m` and integer
endpoint order `r`, the minimal transfer remains

\[
 \widehat k(s)=
 \frac{(s-\sigma)^m}{\prod_{j=0}^{m+r}(s+a_j)},
 \qquad
 k^{(\ell)}(0)=0\ (\ell<r),\quad k^{(r)}(0)=1.
\]

It has exactly `m` positive crossings and fixed-singularity multiplier

\[
 \epsilon^{-1}\widehat k(\sigma+\omega/\epsilon)
 \sim \frac{\epsilon^r}{\omega^{r+1}}.
\]

The associated-Laguerre formula and its fractional `alpha>=0` continuation
also survive.  These formulas are pointwise for fixed nonzero `omega`.

### 2.4 Compact Chebyshev synthesis

The fractional two-edge, multiple-real-anchor construction survives.  The
mixed moment matrix is nonsingular by the extended-Chebyshev sign theorem;
the degree-`M` polynomial has exactly `M` simple interior roots; and every
requested anchor multiplicity is exact.

The positive- and negative-ray Watson laws hold in closed sectors with fixed
branch choices.  The edge limit is valid pointwise in fixed `x` under both
the weighted tail and moving-endpoint hypotheses.  Local uniformity requires
uniform versions of those hypotheses.

### 2.5 Landau adapter

Let the real fixed-`epsilon` response have a finite initial Laplace abscissa.
It is enough that one globally selected Jordan part have unit-block exponent
at most `eta`:

\[
 \limsup_{N\to\infty}\frac1N
 \log\int_N^{N+1}B_\pm(t)\,dt\le\eta.
\]

A pointwise bound `B(t)<=C exp(eta*t)` or
`B(t)>=-C exp(eta*t)` is a stronger sufficient hypothesis.  If the continued
filtered Laplace transform has no real-axis singularity at any `q>eta`,
Landau forces the other Jordan part's convergence abscissa to be at most
`eta` as well.  At every target where the filter multiplier is nonzero, the
transform factorization then excludes singularities in

\[
 \Re s>\sigma_0-\sigma\epsilon+\eta.
\]

The strip width is `sigma*epsilon-eta`, so a nontrivial result requires
`eta<sigma*epsilon`.  This conditional implication remains valid.  Its
subcritical Jordan-mass premise is completely open.

## 3. Hostile countermodels that now govern the route

### 3.1 Moments and all algebraic orders do not imply an eventual envelope

Let `t_n=n^4`, and place isolated alternating plateaus in `E` near `t_n` with
height `(-1)^n exp(-n^2)` and bounded width.  Then

\[
 E(t)\to0,
 \qquad
 \int_0^\infty t^N|E(t)|\,dt<\infty
 \quad\text{for every fixed }N,
\]

and the diagonal endpoint is smaller than every algebraic power.  Thus all
fixed-order boundary/germ expansions pass.  For a fixed `delta>0`, however,
an isolated recent jump in a compact filter contributes on the scale

\[
 \exp(\sigma\delta t_n-n^2)k(v_*),
\]

which grows and alternates.  The same construction can be separated enough
to defeat a stable rational endpoint-flat filter.  Therefore

```text
all algebraic boundary data  !=>  a fixed-delta one-sided O(exp(eta*t))
                                  envelope for any eta < sigma*delta.
```

This is the cleanest proof that the missing theorem must use arithmetic not
present in a generic discrepancy model.

### 3.2 Diagonal positivity does not survive the Landau quantifiers

The model

\[
 B_\epsilon(t)=1+\epsilon^r e^{-1/\epsilon}
 e^{\lambda_\epsilon t}\cos(\tau t),
 \qquad \lambda_\epsilon=\theta\epsilon,\quad\theta>\sigma>0,
\]

has the same positive diagonal expansion to every algebraic order on every
fixed compact `c`-window with `t=c/epsilon`: its perturbation is bounded by
`epsilon^r exp(-1/epsilon+theta*c)`.  For every fixed `epsilon`, however, the
oscillatory mode eventually dominates.  Algebraic attenuation changes only
the crossover time; it does not imply any Landau-useful one-sided envelope
with exponent `eta<sigma*epsilon`.

### 3.3 Compact multipliers can hide singularities

For an ordinary compactly supported `h` with `widehat h(sigma)!=0`, define

\[
 k(v)=h(v)-e^{\sigma T}h(v-T)1_{v\ge T}.
\]

Then

\[
 \widehat k(s)=\widehat h(s)
 \left(1-e^{(\sigma-s)T}\right),
\]

so the intended notch at `sigma` is accompanied by the exact lattice

\[
 s=\sigma+2\pi i n/T.
\]

This lattice lies on the notch line, so by itself it does not exhibit a
blind point strictly inside the desired region.  Indeed, in (9.4) a kernel
zero `s_k` maps to the Dirichlet offset
`w=epsilon*(s_k-sigma)`, so this lattice maps to `Re(w)=0`.  Interior blind
points are equally explicit, however.  Take

\[
 h(v)=e^{av}1_{[0,L]}(v),\qquad 0<a<\sigma.
\]

Then `widehat h` vanishes at
`s_k=a+2*pi*i*n/L` for every nonzero integer `n`, while
`widehat h(sigma)>0`; these zeros are inherited by `widehat k` and map to
`Re(w)=epsilon*(a-sigma)<0`.  Thus compact support does not by itself protect
the target region from accidental zeros.  A compact-filter strip proof needs
a zero-free multiplier there or a jointly coprime family whose one-sided
estimates hold simultaneously.

### 3.4 A positive primitive need not control its derivative

Set

\[
 F(x)=e^{-x}(2+\sin 2x)>0,
 \qquad
 E(x)=-F'(x)=e^{-x}(2+\sin2x-2\cos2x).
\]

Then `F(x)=int_x^infinity E(u)du`, but `E` changes sign.  Positivity or an
envelope for one compact-edge primitive does not transfer through Volterra
inversion without a Tauberian/modulus hypothesis.  The failure of envelope
transfer can be made strict: for `0<eta<2`, let

\[
 F(x)=e^{-2x}\left(2+\tfrac12\sin(e^{(2-\eta)x})\right)>0,
 \qquad E(x)=-F'(x).
\]

Here `F=O(e^{-2x})`, whereas the leading oscillatory term in `E` has size
`e^{-eta*x}` along subsequences.  Hence differentiation can genuinely lose
the exponential rate.

### 3.5 Fixed finite one-center coefficient data miss a high vertical pole

For fixed real `a` and `Y->infinity`, let

\[
 H_Y(w)=\frac1{w-a-iY}.
\]

It has a pole at fixed real offset and height `Y`, while every fixed Taylor
coefficient at `w=0` is `O(Y^(-j-1))`.  Thus every fixed finite coefficient
set, and coefficientwise-in-`j` limiting data, can miss a high pole.  The
complete coefficient sequence does detect its convergence radius, but the
resulting one-center disk still does not cover an unbounded vertical strip.

## 4. Revalidated route passports

### Route A: endpoint-normalized rational response

```text
multiplier zeros:       intended notch only for the minimal Q=1 filter
fixed-zero response:    order one in the fixed-omega limit
forward sign:           necessarily signed
terminal scalar coordinate: subcritical fixed-sign unit-block Jordan mass
Landau socket:          complete if eta < sigma*epsilon
status:                 valid criterion; no easier premise found
```

The original Suzuki-to-positive-forward-kernel route remains closed: a
nonzero nonnegative causal kernel cannot have a positive-real Laplace notch.

### Route B: endpoint-flat rational/fractional response

```text
multiplier zeros:       intended notch only for the minimal associated-Laguerre filter
fixed-zero response:    attenuated by epsilon^alpha
hard endpoint:          removed for alpha > 0
inverse tax:            epsilon^(-alpha), irrelevant if no inversion is used
terminal scalar coordinate: subcritical fixed-sign unit-block Jordan mass
status:                 valid exact strip spectrometer; exponent saving open
```

This is the cleanest correction to the old route map.  Direct Landau
exclusion does not reconstruct the triangular response, so inverse
instability cannot be cited as a refutation.  The alternating-plateau model
shows why endpoint flatness and all moments alone still cannot prove the
premise.

There is also an exact one-way relation.  If `G_(m,0)` uses the first `m+1`
stable rates, then adding `r` endpoint orders gives

\[
 G_{m,r}(q)=G_{m,0}(q)
 \prod_{\ell=1}^r\frac{\epsilon}{q+a_{m+\ell}\epsilon}.
\]

Each added factor has nonnegative impulse
`epsilon*exp(-a_(m+ell)*epsilon*t)`.  Thus endpoint flatness is a positive
causal smoothing hierarchy, BIBO-stable when every added rate is positive.
A same-exponent one-sided bound
`O(exp(eta*t))` transfers through a factor with rate `a` when
`eta+a*epsilon>0`; equality introduces `t*exp(eta*t)`, while
`eta+a*epsilon<0` leaves the slower kernel tail.  It does not transfer
backward without the differentiating `epsilon^(-r)` inverse.  This is a real
one-way comparison for generic response classes.  It does not lower the
spectral exponent: for the exact consecutive-rate beta/Riesz realization,
both fixed-sign unit-block Jordan exponents are `Theta`.  Thus no strict
arithmetic simplification for the actual prime measure has been established.

It is not a finite-scale high-zero amplifier.  Along a strip-failure sequence
`omega_n=-d_n+i*gamma_n`, `epsilon_n` comparable to `d_n`, and
`|gamma_n|->infinity`, the exact rational formula gives

\[
 |G_{\epsilon_n,m,r}(q_{\rho_n})|
 \asymp \frac{d_n^r}{|\gamma_n|^{r+1}}.
\]

The forbidden mode remains qualitatively detectable at eventual times, but
endpoint flatness attenuates it on the boundary scale.

### Route C: compact far-edge response

```text
gain:                   fixed-edge demodulation
limit quantifiers:      epsilon -> 0 for each fixed x
Landau quantifiers:     fix epsilon, then t/x -> infinity
additional socket:      multiplier noncancellation / coprime family
stability socket:       weighted tail + endpoint rate + Tauberian inversion
direct terminal coordinate: subcritical fixed-sign unit-block Jordan mass
edge-method first edge: uniform vertical/two-parameter arithmetic control
status:                 valid direct criterion; far-edge derivation has extra gates
```

The stability socket in this passport belongs only to an attempt to derive
the fixed-`epsilon` envelope premise from the `epsilon->0` edge asymptotic.
It is not an assumption of direct Landau applied to a compact filtered response.
The direct criterion has the same Jordan-mass edge as Route B, plus the
possible multiplier blind spots.  A pointwise envelope remains a sufficient
but unnecessarily strong version of that edge.

For a hypothetical failure of every uniform strip, the relevant zeros have
`rho_n=1-d_n+i*gamma_n`, with `d_n->0` and `|gamma_n|->infinity`.  Taking
`epsilon_n` on the scale `d_n` sends
`s=sigma+(rho_n-1)/epsilon_n` toward the imaginary/Stokes direction, **not**
the negative-real sector in which the far-edge formula was proved.  Both
kernel endpoints then generally enter the Fourier asymptotic and can
interfere.  With sufficient endpoint regularity the schematic form is

\[
 \widehat k(s)\sim
 \frac{\kappa_0\Gamma(\alpha_0+1)}{s^{\alpha_0+1}}
 +\frac{\kappa_T\Gamma(\alpha_T+1)e^{-sT}}
 {(-s)^{\alpha_T+1}},
\]

not the isolated far-edge term.  Fixed support therefore has no certified
high-zero amplification; it may instead attenuate or cancel the signal.
Using this branch for a strip first requires a uniform vertical/Stokes
two-edge theorem, before the eventual-envelope and noncancellation gates are
even reached.  Support or order growing with height would also require a new
uniform kernel/envelope theorem.

### Route D: complete-germ propagation

```text
finite jets:            proved, local, insufficient
complete one-center germ: information-theoretically determining
quantitative reach:     nearest-singularity disk
missing adapter:        translated-germ/global vertical propagation
status:                 open; one-center coefficient bounds are not enough
```

## 5. Corrected decision graph

```text
ultimate goal: RH
  |
  +-- global Weil positivity [RH-equivalent]
  |      `-- zeta-specific adjacent-support propagation OPEN
  |
  `-- intermediate fixed strip near Re(s)=1 [not RH]
         |
         +-- QP/Turan route
         |      +-- DPA_P(.019) OPEN
         |      `-- LTRAD_P(.0189,.001) OPEN
         |
         `-- pole-filter/Landau route
                +-- rational endpoint-flat Jordan mass OPEN [strip-equivalent exponent]
                +-- compact direct criterion
                |      +-- fixed-epsilon Jordan mass OPEN
                |      |      `-- possible far-edge upstream program:
                |      |          vertical/two-parameter + arithmetic/Tauberian adapters
                |      `-- multiplier spectral coverage OPEN
                `-- global translated-germ propagation [upstream program]
```

Nothing in the corrected calculus proves or weakens the QP/Turan locks, and
nothing supplies the Weil adjacent-support estimate.  The pole-filter branch
is genuinely distinct.  The endpoint-flat Jordan-mass exponent is now proved
to be exactly `Theta`, so an exponent saving there is equivalent to a strip.
The one-way smoothing relation remains useful algebraically but no longer
licenses a priority upgrade by itself.

## 6. Research-course correction

The appropriate course change is precise:

1. retire the global phrase “fixed filters cannot help”;
2. retain endpoint-flat rational filters as the cleanest direct Landau test,
   because the minimal multiplier has no accidental target zeros;
3. distinguish direct compact Landau tests from the far-edge program; treat
   the latter as a two-edge microscope until a jointly coprime family and a
   vertical/two-parameter arithmetic estimate are supplied;
4. stop optimizing notch order, stable rates, or finite boundary jets by
   themselves—the hostile models already preserve all of that data; and
5. do not globally reprioritize away from QP/Turan or Weil: no corrected
   filter theorem changes their first open edges.

Within the arithmetic-response side of the pole-filter calculus, the
clearest admissible successor is a zeta-specific inequality that rules out
both the smooth oscillatory model and the positive Euler-product countermodel
while controlling the full adaptive-mask cone.  Exact unit Euler factors, or
equivalently the divisor identity `Lambda*1=log`, expose one discriminator but
do not alone supply a linear coercive estimate.  Zero-side,
functional-equation, or direct complex-analytic mechanisms remain separate
sockets.  Until one of these mechanisms is stated with a complete passport,
“prove the endpoint-flat ramp bound” is an exact rephrasing of the strip
target rather than a reduced route to it.

## 7. Trust and replay

The analytic revalidation was performed independently on the endpoint,
Volterra, germ, fixed-singularity, and Landau dependencies.  Exact rational
identities and selected low-order cases remain kernel-checked in Lean.

Replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_pole_killing_boundary_calculus.py \
  src/test_shifted_psi_ramp_bridge.py

cd lean/rhbridge
lake build RHBridge.HigherPoleKillingFilters
lake env lean RHBridge/HigherPoleKillingFiltersAudit.lean
```

Current result: `52` Python tests pass; the Lean module and axiom audit pass.
These checks certify algebra and numerical replay, not the Stieltjes,
Tauberian, Landau, or zero-free-region theorems.
