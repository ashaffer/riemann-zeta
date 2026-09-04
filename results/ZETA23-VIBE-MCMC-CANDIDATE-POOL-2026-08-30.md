# Vibe-MCMC candidate pool for a uniform zero-free strip

**Date:** 2026-08-30  
**Status:** stochastic proof-design audit; no zero-free strip and no proof of
RH is claimed

## 0. Frozen target and acceptance test

The immediate target is a fixed zeta zero-free strip, not RH.  The currently
audited QP implication is

```text
DPA_P(.019) + LTRAD_P(.0189,.001)
       -> no directional event of depth Y^-.001
       -> a zero-free width 10^-6.
```

Write

```text
A=50/33,                    B=Y^A,
d=.001,                     c_rad=.0189,
tau=c_rad-d=.0179,
epsilon=Y^(-tau+o(1)),      Delta=Y^(2-A)=Y^(16/33).
```

The transverse LTRAD target is `s_v>=epsilon`.  A hypothetical separator has

```text
y dot v=-1,                 h_Y(y)<=epsilon,
||y_corr||_E <=epsilon Delta^(1/2)
              =Y^(.22452424...+o(1)).
```

The finite tensor terminator is now available: an actual-prime all-cut
product tensor with

```text
r >> log Y/log log log Y
```

cannot exist, since tensor-labelled SR2PF gives
`r<<log Y/log log Y`.  Therefore every route below is accepted only if it
does one of the following:

1. constructs `DPA_P(.019)` and proves `LTRAD_P(.0189,.001)`;
2. proves an event-conditioned substitute which excludes every depth
   `Y^-.001` event without the universal split; or
3. proves a different pointwise theorem excluding every zero in
   `Re(s)>1-10^-6`.

Average-density conclusions, generic fourth moments, and synthetic real-node
models do not pass this acceptance test.

## 1. MCMC grammar

A proof state is a directed chain

```text
proved inputs -> one explicit conjectural lemma -> proved terminator -> strip.
```

The proposal kernels used in this run were:

```text
Q  change universal quantifiers to event-conditioned ones;
T  tensorize a scalar obstruction;
S  replace a bound by stability of its equality case;
M  add a second physical center or logarithmic scale;
D  dualize a separator into a positive sampling measure;
A  retain the actual-prime labels through an arithmetic invariant;
L  localize, while demanding hereditary source and floor data;
X  splice two independently incomplete chains.
```

States were penalized for circularity, loss of the prime mask, an exponent
deficit, average-only control, or invoking a theorem already refuted by a
local countermodel.  The numerical scores below are heuristic energies, not
probabilities or theorem claims:

```text
2 points each: exact exponent fit, actual-prime retention, pointwise
quantifiers, use of a proved terminator, and a scalable falsifier.
```

## 2. Round-zero pool: 37 candidate chains

### Cluster A -- extract the tensor already known to be impossible

| ID | Candidate chain and exact missing lemma | Exponent requirement | Score / first objection |
|---|---|---|---|
| A1 | **Critical-frame saturation.** Separator cap + the pair-cluster frame imply either an uncancelled carrier return or near-equality in the corrector Bessel bound; classify every near-equality case as a weighted digit autocorrelation; clean it and invoke tensor SR2PF. | Produce an alphabet `q asyp log log Y` and `r>=kappa log Y/log log log Y`, with weighted log error `<=kappa_0/(mB)`, `m=Y^(tau+o(1))`. | **9/10, survives.** The stability/classification theorem is wholly open. |
| A2 | **Multiscale Toeplitz-PSD entropy.** From `epsilon-F_y>=0` on the high band, form windowed PSD moment matrices at geometrically nested resolutions; prove that dispersed source mass forces entropy increments which tensorize. | Total entropy at least `(tau-o(1))log Y`; loss per mode `O(log log log Y)`; final frequency error `O(B^-1)`. | **8/10, survives.** Local positivity is not global Fejer--Riesz positivity. |
| A3 | **Clustered local Fejer--Riesz.** Factor the capped nonharmonic polynomial modulo singleton/pair jets, then iterate the factor support until it has product depth `r`; prime frequencies in the autocorrelation become an all-cut tensor. | Factorization error in coefficient-weighted `L1` at most `o(1/(mB))`; depth as in A1. | **7/10, mutate.** A single spectral factor need not have product structure. |
| A4 | **One-sided separator sparsification.** Every separator at level `epsilon` has a source-preserving sparsification with `P_eff<=epsilon^(-1)Y^o(1)` and the same cap up to `1+o(1)`; the proved lower bound then makes it a near-extremizer, to which A1 applies. | Sparsifier size/effective participation `Y^(tau+o(1))`, not the generic `epsilon^-2`; uniform error `o(epsilon)`. | **8/10, survives.** Ordinary Maurey sampling loses a square. |
| A5 | **Labelled dependent random choice.** Construct the phase-incidence hypergraph of large negative source contributions.  A source- and sign-preserving DRC lemma extracts a `q`-ary cube of actual primes. | Retain `Y^{-o(1)}` source mass and `B^-1` phase accuracy through `r>>log Y/log log Y`. | **5/10, low.** Generic DRC loses coefficients and the carrier floor. |
| A6 | **All-order cumulant collapse.** The one-sided cap bounds every positive-part moment; vanishing mixed cumulants force rank at most two under every partition, hence the secant/tangent fork already closed by SR2PF. | Moment order growing to `r`; total conductor loss `Y^o(1)` rather than `Y^{Theta(r)}`. | **6/10, mutate.** Standard Dirichlet-polynomial moments hit the conductor barrier. |
| A7 | **Approximate-relation hypergraph removal.** Many coherent three-by-three log grids give integer determinants `O(Y^3/B^2)=O(Y^-1/33)`, hence exact rank two; a labelled removal lemma assembles compatible grids across all cuts. | At least `q^r=Y^(tau-o(1))` good vertices; deletion loss `Y^o(1)`; every three-way error `O(B^-1)`. | **8/10, survives.** Density of compatible grids is not yet forced by the separator. |
| A8 | **Prime autocorrelation graph rigidity.** A local spectral factor gives a dense graph with edges labelled by primes near ratios `x_i/x_j`; prove a polylogarithmic bound for such PSD/symmetric prime quotient graphs, stronger than broad one-flattening SR2PF. | Must contradict a graph of order at least `Y^(tau/2-o(1))`; tolerance `Y/B` after exponentiation. | **7/10, survives.** This needs a new rigidity theorem, but uses more labels than broad SR2PF. |
| A9 | **Arithmetic modular-entropy dichotomy.** Reduce significant prime frequencies modulo many small primes.  Either projective collisions create a product cube, or residue expansion forces a positive phase return. | Accumulated saving `Y^tau`; exceptional-prime product only `Y^o(1)`; collisions retain all-cut compatibility. | **7/10, survives.** No established bridge from modular slopes to real-time sign. |

### Cluster B -- prevent a reflected corrector from hiding the carrier

| ID | Candidate chain and exact missing lemma | Exponent requirement | Score / first objection |
|---|---|---|---|
| B1 | **Universal multicluster dual measure.** For every actual-prime singleton/pair cloud and legal source vector `v`, construct a probability measure `nu` on `H_Y` with `int a(t)dnu=-r v` and `r>=Y^(-tau+o(1))`.  Duality directly proves LTRAD. | Uniform `r>=epsilon`; constants independent of the number and the tiny internal gaps of pairs. | **8/10, survives.** Known only for one cluster and one fixed six-node fixture. |
| B2 | **Many-peak/Bessel escape.** Produce `Delta=Y^(16/33-o(1))` carrier-positive, effectively orthogonal tests.  The corrector's norm bound gives RMS `epsilon`; unless it nearly saturates at all tests, one peak escapes.  Send saturation to A1. | Strict saving `Y^o(1)` is enough away from equality; equality branch must be classified, not discarded. | **10/10, top survivor.** Existence of labelled positive tests is the missing theorem. |
| B3 | **Slow-envelope interpolation.** Each close-pair difference is a fast carrier oscillation times an envelope of bandwidth `<=B^-1`.  Cancellation at a geometric ladder of high-band times forces an interpolation norm larger than `epsilon Delta^(1/2)`. | Required gain exactly `Delta^(1/2)=Y^(8/33)` between source scale and high band. | **7/10, survives.** Several pair envelopes can cooperate; a scalar Bernstein bound is insufficient. |
| B4 | **Mask-sensitive vector-valued large sieve.** On the subset where `F_car` is positive, prove a two-component large-sieve inequality for pair jets with a fixed deficit unless their phase matrix has low tensor rank. | Any fixed deficit closes the nonstructured branch; low-rank branch must have `r>>log Y/log log Y`. | **9/10, survives.** This is a precise strengthened version of the previously sought theorem. |
| B5 | **Source-null singular-value bound.** The long contiguous source interval couples all reflected-pair gaps.  Prove the evaluation map from the exact source-null corrector space to carrier-positive queries has smallest singular value `>>Delta^-1/2Y^-o(1)`. | Must hold for `t_0/B<=Y^-17/33` and arbitrarily many pairs; target return `epsilon`. | **7/10, survives.** Abstract pair clouds have null directions; actual contiguity must do all the work. |
| B6 | **Few-template reduction.** Show an extremal separator is a convex combination of bounded-size cluster templates, then certify each by a positive dual measure as in the six-node fixture. | Template size independent of `Y`; approximation error `o(epsilon)`. | **4/10, reject unless amended.** Tensor-Fejer examples have genuinely growing rank. |
| B7 | **Semiprime-gap dispersion.** For the half-integer center `Y=N+1/2`, encode a reflected pair by the nonzero integer `G=4pq-(2N+1)^2`, of size `O(Y^2/B)=O(Delta)`.  Prove these gap labels have enough additive/multiplicative expansion to prevent coherent corrector cancellation. | A square-function saving of `Delta^(1/2)` on source-labelled coefficients; exceptional set `Y^o(1)`. | **8/10, survives.** It is an actual-prime invariant absent from synthetic countermodels. |

### Cluster C -- remove or construct the independent DPA gate

| ID | Candidate chain and exact missing lemma | Exponent requirement | Score / first objection |
|---|---|---|---|
| C1 | **Event-conditioned antenna.** Given a depth `Y^-d` source event, construct the DPA upper certificate only at that center, using the event weights in its design; combine with LTRAD. | Floor `>=-Y^(-.019)` while preserving carrier one; `.019>.0189` supplies strict contradiction. | **9/10, top survivor.** It avoids an unnecessary universal theorem but no construction is known. |
| C2 | **Joint minimax certificate.** Dualize the simultaneous existence of a bad source event and a deep radial antipode.  Prove the joint feasible cone is empty by one prime-labelled PSD certificate, rather than separate DPA and LTRAD estimates. | Separation margin at least `Y^(-.019+o(1))`; no product of margins worse than `.019`. | **8/10, survives.** Must not merely rename direct event exclusion. |
| C3 | **Multiblock signed antenna.** Combine many short exact-prime blocks, each with a locally optimized growing-alphabet profile, and randomize/correct cross-block phases. | Uniform floor `Y^(-.019)` on `[Y^.01,Y^(50/33)]`; transfer/correction loss `o(Y^-.019)`. | **7/10, survives.** Pointwise finite-band control, not mean control, is required. |
| C4 | **Prime-log Christoffel/SDP bound.** Prove the exact finite prime-log semi-infinite LP has value at most `Y^(-.019)` by bounding a source-normalized Christoffel function and rigorously controlling the continuum between grid points. | Grid and derivative loss together `o(Y^-.019)`; certificates supported only on ordinary primes. | **7/10, survives as a computational theorem-discovery route.** A finite computation alone cannot reach asymptotic scales. |
| C5 | **Approximate prime Riesz product.** Build a nonnegative polynomial on an auxiliary short-block support, project its difference spectrum to prime logs, and repair projection errors with a signed tail. | Every active frequency error `O(B^-1)` or aggregate error `o(Y^-.019/B)`; tail keeps carrier one. | **4/10, low.** PHR2 and tensor rigidity obstruct long pointwise transfers. |
| C6 | **Bad-center averaging.** A hypothetical zero generates bad events at many nearby centers; average center-dependent upper certificates so each only needs a weak floor, while their mean reaches `.019`. | At least `Y^eta` coherent centers with total phase drift `o(1)` and averaged loss below `Y^-.019`. | **7/10, mutate.** The existing bridge guarantees one center, not a coherent family. |
| C7 | **Natural smooth prime weights.** Normalize `Lambda`-type positive weights and seek absolute transform `O(Y^-.019)` on the whole aperture. | Fixed power `.019`. | **2/10, reject as low information.** For natural weights this is already essentially a fixed-strip prime-error estimate. |

### Cluster D -- bypass QP with a direct zero-to-prime contradiction

| ID | Candidate chain and exact missing lemma | Exponent requirement | Score / first objection |
|---|---|---|---|
| D1 | **Direct sign-sensitive Turan sum.** Prove `-N^-1 sum_(p in I)cos(t log(p/Y))<N^-.001` for every legal interval and `N^.5<=t<=N`. | Any fixed saving `.001`; interval uniformity and sign retained. | **5/10, low.** This directly implies the strip and is close to restating the hard scalar theorem. |
| D2 | **Vaughan negative-part theorem.** Use the actual Vaughan coefficients to bound only the negative real tail, avoiding an absolute-value estimate that is known to be strip-strength. | Rule out negative mass `N^(1-.001)`; Type-II loss below `N^.999`. | **6/10, survives weakly.** Coefficient-uniform factorization destroys curvature, so signs must be used specifically. |
| D3 | **Growing-degree Stechkin positivity.** If `rho=beta+i gamma` with `beta>1-10^-6`, combine logarithmic derivatives at `sigma+ik gamma` using an optimized nonnegative trigonometric polynomial whose conductor term cancels. | A gamma-independent positive reserve `>=10^-6`; degree and coefficient sum may grow only subpolynomially. | **4/10, low.** Classical constant-term/conductor bookkeeping is the likely obstruction. |
| D4 | **Compressed zero replication.** Compress the Euler phases relevant to one off-edge zero to `O(log T/log log T)` dimensions, find polynomial-height almost-periods, and create too many right-edge zeros for zero density. | At least `T^eta` replicas in height `T^C` for some fixed `eta>0`; approximation strong enough for Rouche winding. | **6/10, mutate.** Uncompressed simultaneous recurrence is exponentially late. |
| D5 | **Zero-to-digital-prime tensor.** Use the explicit formula at a geometrically nested family of scales.  A single off-edge zero supplies a common phase and coherent signed prime events; an entropy increment extracts the all-cut tensor forbidden by SR2PF. | `r>>log Y/log log Y`, log accuracy `B^-1`, and a positive-entropy set of nested scales from one zero. | **8/10, survives.** This is the most promising direct splice with SR2PF, but the zero-to-many-scales lemma is open. |
| D6 | **Critical-growth R176 contour.** Allow exactly the polynomial boundary growth forced by harmonic access and prove a strict arithmetic deficit in the joint nonlinear Euler head. | Save `c q log H` with fixed `c>0`. | **2/10, reject.** After the access law this is the original zero-exclusion estimate, not a reduced lemma. |

### Cluster E -- multiplicative scale history

| ID | Candidate chain and exact missing lemma | Exponent requirement | Score / first objection |
|---|---|---|---|
| E1 | **Nested-scale resonance entropy.** One zero with `beta>1-delta` forces the same Archimedean character to correlate with Mobius or von Mangoldt on a positive-entropy tree of intervals; an entropy inverse theorem makes the function pretentious, contradicting Euler-factor divergence. | Here `delta=10^-6`; branch density may lose `x^(-o(1))` but not `x^-c`; coherence must persist for `c log log x` levels. | **7/10, survives as an orthogonal program.** A single zero may force only sparse scales. |
| E2 | **Renormalization contraction for Mertens.** Turn a subpower Vinogradov--Korobov saving into `M(x)=O(x^(1-delta))` via an exact prime-factor recursion with a uniform spectral gap. | Any `delta>=10^-6`. | **4/10, low.** The uniform gap is essentially the new theorem and parity is hostile. |
| E3 | **Buchstab martingale rigidity.** Reveal prime factors sequentially; persistent `x^(1-delta)` Mobius growth would give a low-entropy martingale path, then use sign independence across newly revealed primes. | Entropy production bounded below by a fixed constant per logarithmic scale for `delta=10^-6`. | **6/10, mutate.** No unconditional pointwise sign-independence theorem exists. |
| E4 | **Prime-error multiscale convexity.** Prove that `psi(x)-x` cannot have upper power order `1-o(1)` because its smoothed errors obey a strict log-scale convexity/energy decay law. | Derive `psi(x)-x=O(x^(1-10^-6+o(1)))`. | **3/10, low.** Such a power bound is itself equivalent to a strip unless the decay law is independently arithmetic. |

### Cluster F -- long-range orthogonal mechanisms

| ID | Candidate chain and exact missing lemma | Exponent requirement | Score / first objection |
|---|---|---|---|
| F1 | **Passive-scattering index.** Realize completed zeta as a causal transfer function whose negative-square index counts zeros right of `1-delta`; prove local Euler/gamma interconnection has index zero there. | Uniform index zero for `delta=10^-6`; analytic continuation must not assume the strip. | **5/10, long horizon.** Risk of circular continuation. |
| F2 | **Finite-prime Lorentzian Hodge.** Construct a functorial finite-prime correspondence volume polynomial, prove Lorentzianity, and pass its Hodge inequality to the Weil form. | Limit must control test functions resolving horizontal distance `10^-6`; no collapsing coercivity requirement. | **5/10, long horizon.** Defining the product may insert positivity by hand. |
| F3 | **Stable multivariate xi lift.** Represent the relevant two-parameter Jensen array as diagonal specializations of stable multiaffine polynomials; stability excludes zeros outside the target strip. | Uniformity when degree and shift grow together; enough quantitative stability for `delta=10^-6`. | **4/10, long horizon.** Fixed-degree eventual hyperbolicity is insufficient. |
| F4 | **Quantitative Nyman--Beurling collar.** Construct approximants whose Mellin error has a power-decaying weighted collar near `Re(s)=1`; use the exact Hardy-space zero evaluation bound. | Power decay corresponding to `delta=10^-6`, uniformly in height. | **4/10, long horizon.** Ordinary `L2` approximation does not control an exceptional zero. |

## 3. First Metropolis collapse

The following proposals receive effectively zero continuation weight unless a
new interface is added:

```text
B6  bounded-template reduction: refuted by growing-rank tensor-Fejer states;
C7  natural smooth prime transform: already fixed-strip strength;
D6  R176 contour optimization: reduced back to the original strict deficit;
generic BSG versions of A5: lose source, signs, floor, and actual labels;
generic high-moment versions of A6: conductor loss is fatal;
any use of broad one-flattening SR2PF alone: Y^(4/33) is too weak;
any direct use of the sharp four-cycle moment bound: returns exponent 41/66,
  whereas the transverse target is .0179;
average zero density or almost-all cancellation: cannot exclude one zero.
```

The main new observation from the collapse is a candidate critical matching.
The norm estimate in the first line is proved; producing the test family in
the second line is part of the proposed lemma:

```text
||y_corr||_E <= epsilon Delta^(1/2),                 [proved]
# desired carrier-positive orthogonal tests = Delta, [conjectural]
RMS corrector size <=epsilon.                         [then follows] (3.1)
```

Thus a proof should not expect a generic power saving over the corrector.
It should prove a dichotomy:

```text
strict Bessel deficit -> an uncancelled return of size epsilon;
near Bessel equality  -> rigid product/autocorrelation structure -> SR2PF.
```

This changes the target from “improve the large sieve” to “classify its
source-labelled near-extremizers.”

## 4. Second-generation splices

### S1 -- critical inverse large sieve (`B2+B4+A1`)

Prove the following theorem card.

> **CILS.**  Let an actual-prime singleton/pair cloud carry a legal source
> vector and let `y` satisfy `y dot v=-1` and `h_Y(y)<=epsilon`.  Then either
> there is a high-band query with total return at least
> `epsilon Y^(-o(1))`, or the carrier/corrector evaluation matrix is within
> weighted error `o(1/(mB))` of a `q`-ary product autocorrelation with
> `m=Y^(tau+o(1))` and product depth
> `r>=kappa log Y/log log log Y`.

The first outcome proves LTRAD.  The second is impossible by cleaning and the
proved tensor SR2PF theorem.  CILS is not yet proved; it is the highest-weight
state because every exponent in it is already matched and both outputs have
proved terminators.

Fast falsifier: solve scalable semi-infinite LPs on pair clouds with
`tau_0=t_0/B->0`; measure the singular spectrum of every near-separator.  A
family with no spectral gap and no growing tensor entropy refutes this theorem
card.

### S2 -- local spectral factor to determinant cube (`A2+A3+A7`)

Use `epsilon-F_y>=0` to produce nested windowed PSD Toeplitz forms.  An entropy
increment either concentrates a hereditary carrier, already excluded below
physical width `Y^(8/33)`, or supplies compatible approximate three-grids.
For each grid the integer determinant is

```text
O(Y^3/B^2)=O(Y^(-1/33)),
```

so it vanishes exactly.  A labelled hypergraph assembly must then turn the
overlapping exact ranks into an all-cut tensor.

Exact missing lemma: the entropy-to-compatible-grid theorem with only
`Y^o(1)` deletion and coefficient-weighted `B^-1` error.  This is more
elementary than a full nonharmonic Fejer--Riesz theorem and gives a clear
finite combinatorial falsifier.

### S3 -- event-conditioned primal/dual saddle (`C1+C2+A4`)

Do not prove universal DPA.  For each bad event, optimize the upper antenna and
the transverse separator jointly.  A one-sided sparsification at size
`epsilon^-1Y^o(1)` makes an extremal failed saddle near-critical; apply CILS.

Exact missing lemma: every event-conditioned failed saddle either has a DPA
certificate with floor `Y^-.019` or a source separator satisfying the
near-extremal participation hypotheses of CILS.  This would remove one of the
two universal open gates rather than merely solve them in parallel.

### S4 -- semiprime-gap vector sieve (`B4+B7+A9`)

Index each close reflected pair by the nonzero integer

```text
G=4pq-(2N+1)^2,              Y=N+1/2,
|G|<<Y^2/B=Delta.
```

Use the `g` labels as the second inverse variable in a vector-valued large
sieve.  Expansion modulo many small primes either yields a fixed deficit in
the corrector square function or a multiplicative collision network.  The
network is then fed to determinant-cube extraction and SR2PF.

Exact missing lemma: a source-weighted two-inverse large sieve with total
exceptional modulus `Y^o(1)` and equality classification.  This is the most
arithmetic version of CILS and specifically distinguishes actual primes from
the synthetic null-corrector models.

### S5 -- zero-to-many-centers tensorization (`C6+D5+E1`)

Instead of extracting tensor structure from one separator, derive many
coherent source events from one hypothetical zero across nested `Y`-scales.
Shared ordinate supplies one phase coordinate; scale history supplies the
remaining product coordinates.  A positive-entropy branch gives the tensor
for SR2PF.

Exact missing lemma: one zero with `beta>1-10^-6` forces a source event of
depth `Y^-.001` on `>>log Y/log log log Y` independently branching scales,
with total phase error `O(B^-1)`.  This is presently much stronger than the
audited one-center Turan bridge, but it imports multiplicative scale history
that the one-center countermodels do not possess.

### S6 -- independent DPA construction (`C3+C4`)

Run a multiblock semi-infinite SDP on exact prime logs, but demand a symbolic
certificate template whose inequalities can be proved asymptotically.  Short
blocks avoid PHR2; a global Christoffel or discrepancy estimate controls the
union.

Exact missing lemma: a family of ordinary-prime coefficients of carrier one
with

```text
inf_(Y^.01<=t<=Y^(50/33)) F_y(t)>=-Y^(-.019+o(1)).
```

This remains necessary for the uncoupled QP route even if CILS proves LTRAD.

## 5. Posterior ordering

The subjective posterior ordering after two collapse rounds is:

| Rank | State | Why it remains live | Primary failure mode |
|---:|---|---|---|
| 1 | S1 critical inverse large sieve | exact exponent match; both branches have proved terminators | near-saturators may be diffuse without tensor structure |
| 2 | S4 semiprime-gap vector sieve | injects a genuinely actual-prime invariant into S1 | available sieve may lose source signs or a square root |
| 3 | S3 event-conditioned saddle | removes the likely over-strong universal split | one-sided sparsification may intrinsically cost `epsilon^-2` |
| 4 | S2 PSD entropy to determinant cube | integer determinant has a strict `Y^-1/33` collapse | local positivity may not create enough compatible grids |
| 5 | B1 universal positive dual measure | directly proves LTRAD and is finitely falsifiable | dimension-free positivity may fail in growing rank |
| 6 | S6 multiblock DPA | still needed by the uncoupled route | continuum pointwise floor and prime transfer |
| 7 | S5 multi-center tensorization | attacks a single zero rather than all separators | no present positive-entropy zero-to-scale theorem |
| 8 | E1 nested-scale pretentious route | genuinely orthogonal arithmetic information | exceptional scales may have zero entropy |

The recommended first attack is not to attempt all of CILS at once.  Isolate
its critical linear-algebra core:

> **Near-saturation test lemma.**  For the legal singleton/pair frame, assume
> `h_Y(y)<=epsilon` and that the corrector cancels every carrier-positive
> query in a maximal `Delta`-sized separated family.  Prove either a fixed
> Bessel deficit or that the normalized query-by-cluster matrix has
> `Y^o(1)` stable rank after peeling tensor factors.

This statement has a direct adversarial numerical falsifier, preserves the
lost separator premise, and tests the precise equality regime exposed by
`(3.1)`.  If stable rank remains polynomial with no peelable factors, S1
should be killed.  If repeated factors appear, the next theorem is the
source-labelled stability upgrade needed to reach SR2PF.

## 6. What this run learned

The highest-value new direction is not another global moment estimate.  The
current exponents put corrector cancellation exactly at square-function
capacity.  Consequently the only plausible gain is rigidity of saturation,
and the newly proved tensor SR2PF theorem supplies an unusually strong
terminator for precisely such rigid states.

There are therefore two serious programs rather than one:

```text
LTRAD side: classify critical carrier/corrector saturation and collapse its
            structured branch by tensor SR2PF;

upper side: construct DPA only where a bad event occurs, or independently
            solve the multiblock exact-prime antenna problem.
```

Every assertion labelled “missing lemma” above remains conjectural.  The pool
is a map of falsifiable proof states, not evidence that the strip or RH has
been proved.

## 7. Third-generation resampling: diffuse/Sidon conditioning

**Later pass on 2026-08-30.**  This section supersedes the posterior preference
for S1 and the “near-saturation test lemma” above.

Two hostile states must now be included in the proposal distribution.

1. If `A` is a sparse Sidon-like generator with
   `m=Y^(.0179+o(1))`, its exact Fejer autocorrelation has the desired floor
   but can have

   ```text
   P_eff asyp m^2=Y^(.0358+o(1)),
   ```

   no long progression, no localization, and no Cartesian digit tensor.
2. A coisometric evaluation map of stable rank `Delta` admits a completely
   diffuse Bessel saturator of norm `epsilon sqrt(Delta)`.  Equality in the
   square-function estimate therefore does not imply low rank or peelable
   product factors.

There is also a superresolution constraint.  The source height satisfies
`t_0<=Y`, so source phases alone resolve a log frequency only to `Y^-1`.
The arithmetic determinant gate requires

```text
B^-1=Y^(-50/33),
```

which is finer by the factor `B/Y=Y^(17/33)`.  Any legal extraction must get
that precision from contacts extending to height `asyp B`, not from the
source event or from rounding synthetic nodes.

Accordingly, every third-generation state whose edge is

```text
near-Bessel saturation -> digit tensor
```

is assigned infinite energy.  The permitted structured outputs are instead:

```text
a general weighted prime-labelled difference/quotient graph;
the complete KKT contact saddle of the semi-infinite problem; or
an event-conditioned certificate which directly closes one or both radial
directions.
```

### 7.1 Graph-output mutations

In the graph cards below, `m=Y^(tau+o(1))`, `tau=.0179`.  A general Sidon
autocorrelation has `asymp m^2=Y^(.0358+o(1))` separately labelled edges, so
no repeated-difference hypothesis is allowed.

#### G1 -- complete prime quotient-graph rigidity

**Exact missing lemma.**  Let `alpha_i,beta_j` be arbitrary real vertex
potentials and let a dense bipartite graph have distinct prime labels
`p_ij asyp Y` satisfying

```text
|log(p_ij/Y)-alpha_i-beta_j|<=C/B                   (7.1)
```

on edges of total KKT weight `1-o(1)`.  Add the row/column balance identities
inherited from complementary slackness.  Prove that such a graph has fewer
than `Y^(tau-o(1))` vertices on one side, unless it directly yields an
event-conditioned radial certificate of size `epsilon`.

**Ledger.**  Exponentiation gives physical error `Y/B=Y^-17/33`; a complete
`3 x 3` subgraph has integer determinant `O(Y^3/B^2)=O(Y^-1/33)` and hence
rank at most two.  Unlike old SR2PF, the desired theorem must use graph
balance to improve the broad `Y^(4/33)` side bound below `Y^.0179`.

**Fastest falsifier.**  Search rank-two prime matrices with prescribed KKT
row/column stresses and side length growing faster than a logarithm.  The
existing additive prime grids falsify any version that omits the stresses.

#### G2 -- dense partial quotient-graph completion

**Exact missing lemma.**  If `(7.1)` holds only on a weighted graph with
`m` vertices and edge weight `1-o(1)`, prove either a source-preserving
completion to a complete quotient graph after deleting `Y^o(1)` weighted
mass, or a positive high-band query of size `epsilon`.

**Ledger.**  Deletion may cost `Y^o(1)` but no fixed power of `m`; the
completed graph must retain at least `Y^(2tau-o(1))` edge incidences and
`B^-1` accuracy.

**Fastest falsifier.**  Generate random regular Sidon difference graphs with
adversarial KKT weights.  If they retain unit weight while every complete
bipartite minor has size `O(log m)`, this card is false without an additional
arithmetic hypothesis.

#### G3 -- KKT-weighted cycle-holonomy divisor theorem

**Exact missing lemma.**  For a weighted prime quotient graph satisfying
`(7.1)`, use overlapping four-cycles and the KKT balance to prove either a
fixed square-function deficit or at most `Y^(tau-eta)` vertices for some
fixed `eta>0`.  The conclusion may use bounded nonzero two-by-two minors and
their gcd/resultant graph; it must not posit a product tensor.

**Ledger.**  Each two-by-two minor is a nonzero integer of size
`H=Y^(16/33)`.  A saving of only `Y^eta` beyond the critical vertex count
closes the branch.  Products over exceptional gcd classes must cost `Y^o(1)`.

**Fastest falsifier.**  Extend the explicit rank-two prime fixture by a SAT
or MILP search while maximizing graph girth and minimizing common minor gcd.
A family of size `Y^.0179` with diffuse KKT weights kills the card.

#### G4 -- projective larger sieve with stress rather than cardinality

**Exact missing lemma.**  Strengthen the proved two-sided projective sieve by
weighting row and polar-column collisions with the KKT stress.  Show that a
diffuse weight cannot hide entirely in the large residue classes; either

```text
effective vertex mass <=Y^(tau-eta)
```

or one residue fiber gives a direct positive contact certificate.

**Ledger.**  The unweighted result is only `Y^(4/33)`.  The stress-weighted
gain required is `4/33-.0179=.103312...` in the side exponent.  It is large,
so a mere logarithmic sieve refinement is rejected.

**Fastest falsifier.**  Optimize weights on the known Schur normal form
modulo all primes up to a growing cutoff.  A diffuse distribution saturating
the weighted collision inequalities with support `Y^.0179` rejects the
proposal.

#### G5 -- reflected-semiprime label graph

**Exact missing lemma.**  Label every close lower/upper prime pair at
`Y=N+1/2` by

```text
G(p,q)=4pq-(2N+1)^2,
0<|G(p,q)|<<Y^2/B=Delta.                              (7.2)
```

Prove that the bipartite graph of these integer labels cannot support the
source-null KKT stress needed to cancel all contacts, unless the desired
radial measure already exists.

**Ledger.**  The needed singular-value gain is exactly `Delta^(1/2)=Y^(8/33)`;
exceptions over all label divisors must be `Y^o(1)`.  No digit or repeated
difference structure is assumed.

**Fastest falsifier.**  Enumerate actual close reflected pairs at feasible
shells, form the exact `G`-incidence matrix, and minimize its source-null
weighted singular value.  Polynomial decay faster than `Delta^-1/2` argues
against the theorem.

### 7.2 Full-KKT-contact mutations

For

```text
r(v)=inf_(y dot v=-1) sup_(t in H_Y) y dot a(t),
```

finite-dimensional semi-infinite LP duality gives an exact KKT pair at an
attained optimum:

```text
int a(t)dnu(t)=-r(v)v,
nu>=0,  nu(H_Y)=1,
supp(nu) subset {t:y dot a(t)=r(v)}.                 (7.3)
```

Interior contacts also satisfy `(d/dt)(y dot a(t))=0`.  These are legitimate
starting identities; the mutations below concern new consequences of them.

#### K1 -- contact-to-graph superresolution

**Exact missing lemma.**  Given a bad actual-prime source event and a KKT
system `(7.3)` with `r(v)<epsilon`, prove either an event-conditioned radial
certificate of size `epsilon`, or extract a weighted prime quotient graph
satisfying `(7.1)` on `Y^(2tau-o(1))` incidences.  The vertex potentials may
be arbitrary; no low entropy, repeated difference, or tensor conclusion is
allowed.

**Ledger.**  Contact times must reach `cB<=t<=B`; only then can their joint
phase equations deliver `B^-1` rather than `Y^-1` resolution.  Lost contact
weight and log-error budget must both be `Y^o(1)` and `O(B^-1)`, respectively.

**Fastest falsifier.**  Solve the continuum LP by exchange on exact prime
clouds, interval-certify the contacts, and test whether their phase matrix
has any quotient-potential fit at `B^-1`.  A scalable diffuse contact saddle
with residual `gg B^-1` kills K1.

#### K2 -- second-order contact stress graph

**Exact missing lemma.**  Combine stationarity `(7.3)`, contact equalities,
`F_y'(t_k)=0`, and `F_y''(t_k)<=0` into a positive semidefinite stress matrix
on prime-frequency columns.  Prove that either its spectral gap gives return
`epsilon`, or its null-stress graph satisfies G3.

**Ledger.**  The gap need only be `Y^{-o(1)}` relative to the critical
corrector budget; the degenerate output must retain edge weight
`Y^{-o(1)}` and `B^-1` phase accuracy.

**Fastest falsifier.**  On the diffuse coisometric stress family, impose the
exact first- and second-order contact equations and inspect stable rank.  A
full-rank PSD stress with no quotient fit refutes this mutation even before
prime arithmetic.

#### K3 -- paired `q`/`v` KKT saddle

**Exact missing lemma.**  Condition on one bad event and solve the two radial
problems in the directions

```text
q,                 v=a(t_0)+Dq,
D>=Y^(-.001+o(1)).                                  (7.4)
```

Prove from their joint contact equations that either

```text
r(q)<=Y^(-.019+o(1)) and r(v)>=Y^(-.0179+o(1)),      (7.5)
```

or their common contact graph satisfies G1/G3.  The first output, combined
with transverse mixing, excludes the event; the second is an arithmetic
graph problem.

**Ledger.**  Mixing `(7.5)` gives radial depth
`D r(v)/(1+r(v))>=Y^(-.0189+o(1))`, strictly larger than the upper
`Y^(-.019+o(1))`.  No exponent may be lost in passing between the two contact
sets.

**Fastest falsifier.**  Jointly solve both LPs on synthetic Sidon and actual
prime clouds.  If their contact sets remain disjoint and diffuse while both
radial inequalities fail by a fixed factor, the proposed common-graph branch
is not exhaustive.

#### K4 -- event-conditioned positive atomic gauge

**Exact missing lemma.**  Define the positive high-band gauge

```text
C_+(v)=inf{C>=1:-v/C lies in conv{a(t):t in H_Y}}.
```

Construct, from the full source event and its KKT contacts, a certificate
`C_+(v)<=Y^(tau+o(1))`; equivalently `r(v)>=epsilon`.  Unlike a signed atomic
norm, positivity of the representing measure is mandatory.

**Ledger.**  The target cost is `Y^.0179`; the generic signed-frame cost
`Y^(1/2+o(1))` is useless.  Contact discretization error must be
`o(epsilon)` in every prime coordinate.

**Fastest falsifier.**  Compare the positive gauge and signed atomic norm on
growing exact-prime clouds.  A persistent polynomial gap above `Y^.0179`
rules out this certificate architecture.

#### K5 -- KKT contact-count/conditioning theorem

**Exact missing lemma.**  Prove that a separator with `r(v)<epsilon` cannot
have a well-conditioned, macroscopically separated KKT support of full
Caratheodory size.  Either the contact Vandermonde has a singular value below
`Y^{-o(1)}` and yields a quotient graph, or the well-conditioned contacts
construct a positive radial measure with `r(v)>=epsilon`.

**Ledger.**  The conclusion must survive as many as `M+1`,
`M asyp Y/log Y`, contacts; a bound for fixed contact number is irrelevant.
The singular branch must resolve frequencies to `B^-1`.

**Fastest falsifier.**  The known remote atomic designs already look
well-conditioned and diffuse.  Extend them to event-conditioned `v` and test
whether the smallest normalized singular value stays polynomially bounded
away from zero.

### 7.3 Event-conditioned direct-certificate mutations

#### E1 -- direct lower radial quadrature

**Exact missing lemma.**  Given a legal source event, explicitly construct a
positive probability `nu_v` on `H_Y` such that

```text
int a(t)dnu_v(t)=-r_v v,
r_v>=Y^(-.0179+o(1)).                                 (7.6)
```

This is a direct LTRAD certificate; it makes no structural assertion about a
failed separator.

**Ledger.**  Coordinate error must be `o(Y^-.0179)` uniformly over all shell
primes, or be corrected by a positive measure of `o(1)` mass.

**Fastest falsifier.**  Optimize the positive moment problem for adversarial
synthetic Sidon sources and exact prime sources.  A scalable dual separator
below the target refutes any proposed universal construction formula.

#### E2 -- event-conditioned upper antenna

**Exact missing lemma.**  From the same source event construct ordinary-prime
coefficients `z` satisfying

```text
z dot q=1,
inf_(t in H_Y) z dot a(t)>=-Y^(-.019+o(1)).           (7.7)
```

Only event-carrying centers are covered; universal `DPA_P` is not requested.

**Ledger.**  The `.0001` gap between `.019` and `.0189` is the entire strict
reserve.  Every grid, smoothing, and source-adaptation loss must be `Y^o(1)`,
not a fixed power.

**Fastest falsifier.**  Joint exchange optimization over source intervals
and antenna coefficients.  A family of actual-prime events whose conditioned
upper LP value is `ggY^-.0189` kills this route.

#### E3 -- one paired contact certificate

**Exact missing lemma.**  Construct `(nu_v,z)` simultaneously so that
`(7.6)` and `(7.7)` hold and their contact sets share a positive fraction of
mass.  Use the shared KKT equations, rather than separate estimates, to keep
the `.0001` exponent reserve.

**Ledger.**  Shared mass may be `Y^{-o(1)}` but not `Y^-eta`; radial depths
must remain `.0179` and `.019` exactly as in `(7.6)--(7.7)`.

**Fastest falsifier.**  Solve the coupled primal/dual SDP while explicitly
penalizing contact overlap.  Asymptotically disjoint optimal contact sets
with no objective improvement refute the proposed coupling mechanism.

#### E4 -- source-interval positive-kernel certificate

**Exact missing lemma.**  Choose event-dependent nonnegative prime weights
and a positive time kernel so that integration against the source interval
produces `(7.6)`, while the orthogonal complement produces `(7.7)`.  All
prime coordinates must be matched, not just the aggregate source sum.

**Ledger.**  The source has at least `Y^(1-.001)` primes, but its phase
accuracy is only `Y^-1`; the positive time kernel must supply the additional
`Y^-17/33` superresolution without coefficient norm exceeding
`Y^(.0179+o(1))`.

**Fastest falsifier.**  Form the exact event Gram matrix and compare the
required inverse norm with `Y^.0179`.  Random-polytope growth near
`sqrt(Y/log Y)` rejects the kernel unless positivity supplies a new gap.

#### E5 -- contact-assisted sign-sensitive Vaughan certificate

**Exact missing lemma.**  Use KKT contact times as adaptive test frequencies
inside the completed Vaughan identity.  Prove that a depth `Y^-.001` negative
event forces either the direct certificates `(7.6)--(7.7)` or a G3
quotient-cycle graph.  Center, unequal-product, and cross terms remain joined.

**Ledger.**  The completed remainder needs only beat `Y^(1-.001)`, but any
graph extraction must reach `B^-1` accuracy and lose at most `Y^o(1)` source
mass.

**Fastest falsifier.**  Replay the completed Type-II observable on optimized
contact sets.  If the main cancellation remains diffuse and of both signs
with no graph concentration, this mutation adds no information to the direct
strip-strength Type-II target.

### 7.4 Third-generation posterior

The top two mutations are a consecutive pair, not independent proof claims.

1. **K1: contact-to-graph superresolution.**  It attacks the earliest honest
   missing edge.  It uses the full high-band contact set to bridge the exact
   `Y^(17/33)` resolution gap, allows a completely diffuse/Sidon generator,
   and has a direct scalable LP falsifier.  It makes no tensor assertion.
2. **G3: KKT-weighted cycle-holonomy divisor theorem.**  This is the most
   economical possible arithmetic terminator for K1's general graph.  It
   retains the nonzero integer minor scale `Y^(16/33)` and asks only for a
   fixed saving below vertex exponent `.0179`, rather than a polylogarithmic
   tensor classification.

Their proposed chain is

```text
bad event + failed direct radial certificate
  -> full KKT contacts at heights as large as B
  -> general weighted prime quotient graph at B^-1 resolution       [K1]
  -> fixed graph saving or direct positive return                    [G3]
  -> LTRAD_P(.0189,.001).
```

This still leaves the upper direction.  The least redundant completion is
K3/E3: run the `q`- and `v`-direction KKT systems jointly, seeking the
event-conditioned upper certificate rather than universal `DPA_P`.

No mutation in this section is proved.  In particular, K1 may fail because
full KKT contacts can remain superresolved yet graph-free, and G3 may fail
because rank-two prime quotient graphs can be genuinely diffuse.  Those are
the two immediate falsification questions; they replace the now-rejected
question of whether Bessel saturation peels into digit factors.
