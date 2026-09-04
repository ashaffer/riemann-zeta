# Codex handoff — 2026-08-10

> **Current handoff (2026-09-03):** run
> `python3 src/zeta23_correction_context.py resume`, then read
> [`results/ZETA23-SPLIT-CARLEMAN-FORM-DOMAIN-CLOSEOUT-2026-09-03.md`](results/ZETA23-SPLIT-CARLEMAN-FORM-DOMAIN-CLOSEOUT-2026-09-03.md).
> The 2026-09-02 post-synthesis route remains an internally verified pre-R181
> snapshot.  R186 closes the split serialization and weak/L2 adapter, retires
> generic endpoint jets, and leaves completed-zeta KNC itself open.

## Distilled frontier — 2026-08-13

The then-current 2026-08-13 compact research state superseded the earlier
detailed route-by-route history below:

- `results/ZETA23-DISTILLED-RESEARCH-KERNEL-AND-FRONTIER-2026-08-13.md`;
- `results/ZETA23-TEN-ORTHOGONAL-LONG-TAIL-HYPOTHESES-2026-08-13.md`;
- `results/ZETA23-OFF-WALL-IDEA-SYNTHESIS-AND-EXPERIMENT-QUEUE-2026-08-13.md`.

For self-contained current routing, use:

```bash
python3 src/zeta23_correction_context.py resume
```

`zeta23_proof_tree.py resume` now labels its route/adapter/closure triple as a
verified 2026-09-02 snapshot and points to the live command above.  The v3
proof bytecode is an audited August 15 snapshot; explicit node and frontier
queries remain useful historically, but its embedded `FQPP` resume node is
not current.

No uniform strip or improved zero bound has been proved.  The core invariant
is the **completed adverse debt divided by retained carrier on the same
state**.  New routes must change this quotient, not merely its representation.

### QP update — 2026-08-14

The positive prime-log problem is now exactly the one-sided actual-node
Delsarte value `A_H`; its promoted antipode depth is `1/(A_H-1)`.  It remains
open at fixed-power precision.  The latest direct attack proves three useful
boundaries:

- KMT covers the entire polynomial aperture and repairs one bad packet of the
  natural smooth von Mangoldt rule exactly with a negligible positive tilt;
- packet count cannot imply a uniform projected-Gram bound—consecutive packet
  columns have an exponentially small binomial direction, and even perfect
  unprojected orthogonality can saturate the critical minimax value in an
  abstract bounded-entry model;
- the minimum packet-zeroing dual is exactly the normalized carrier residual,
  and controlling its full-band sign is equivalent to the original Delsarte
  certificate, not a condition-number corollary.
- scalar KMT control pays the exact source-rank tax `R*delta_KMT^2`; a natural
  modulus saving of fixed power on the half-power-to-top subband would already
  imply the strip `Re(s)>1-(33c/50)^2` by Turán, so the adaptive residual
  cannot be replaced by a routine scalar upgrade.
- local covariance repairs fixed-radius packet clusters, but stable positive
  square repair of `R` critical packets forces an `Omega(R)` block; termwise
  KMT then pays `eta*R`.  Only signed actual-prime adaptive cross-Gram
  cancellation remains.

At this 2026-08-14 snapshot, the sole arithmetic successor was simultaneous,
adaptive actual-prime covariance/residual control, and the proof cache
resumed at `FQPP`.  This routing is historical; see the September pointer at
the top of this file.

### QP/strip bridge update — 2026-08-15

At this 2026-08-15 snapshot, the proof cache had 92 nodes (SHA-256
`7e2573d24982643351c7029bf80efa2f11c5cc2806ee0b46ff1cf929d4032e6f`)
and resumed at `FQPP`.  Neither QP nor a uniform strip was proved.

- A strip of width `delta` gives a canonical positive actual-prime-power
  Delsarte certificate at every fixed power `c<delta`.
- The reverse is not a support-only theorem: a positive-coefficient finite
  Euler modification preserves every QP node set while inserting high zeros.
  The exact centered von Mangoldt discrepancy is equivalent to a strip, but
  it is not QP.  The missing coefficient comparison is open.
- Unconditionally, the tent explicit formula plus Vinogradov--Korobov gives
  only a subpower QP floor throughout the aperture.
- Heath--Brown clears every cross-Gram exponent except a weighted
  repeated-difference term.  Fejer concentration excludes the stable uniform
  critical AP, not approximate weighted mixtures.
- All-line Fourier-positive signed-kernel amplification is blocked by a
  sharp Turán capacity inequality; band-only or zero-to-zero cancellation
  remains outside that no-go.

See the four `ZETA23-QP-*2026-08-15.md` reports and cache nodes
`FQPB`, `FQPT`, `FQPY`, and `FQPS`.

### QP transverse-scale update — 2026-08-15

The transverse return is now proved to exist at a fixed-power actual-node
scale.  A clustered frame handles reflected shell pairs, and the integer-log
fourth moment plus bounded prime-power product multiplicity gives, at
`A=50/33`,

```text
s_v, r_+(H_Y;S_Y) >> sqrt(log Y) Y^(-49/66).
```

This improves the dimension-only exponent by `17/66`.  The standard fixed
`2k`-moment family is optimized at `k=2`; mixed cubic incidence reaches the
same exponent, and unsigned short-product energy is saturated at power
`2-A`.  A further power gain therefore needs signed packet cancellation or
joint calibrated leverage--skew control.  A legal singleton residual
has a VK subpower upper certificate.  Worst-case Lipschitz transfer of a
harmonic Fejer core is arithmetically limited to `L<<Y^(16/33)` terms, but
this is only a method ceiling: no matching fixed-power upper and no long-event
strip-scale return are proved.  Thus `LTRAD_full`, QP, the reverse
QP-to-strip implication, and a uniform strip remain open.  Resume from
`results/ZETA23-QP-TRANSVERSE-FOURTH-MOMENT-AND-ACTUAL-UPPER-GATE-2026-08-15.md`.

Two restricted sectors now improve the exponent rigorously:

- central packets `0<|n-Y|<=H<=Y^(1/2-epsilon)` satisfy
  `s_v,r_+>>M_H^(-1/2)` by odd half-integer cubic nonresonance, including
  reflected divided-difference modes;
- at `Y=q/2`, `q` odd prime, the one-sided actual prime-power projection
  satisfies `s_v^+,r_+^+>>q^(-755/1056-o(1))` for every prime center and
  `>>q^(-361/528-o(1))` for density-one prime centers.

Both have independent hostile audits and executable replays.  They do not
cover balanced two-sided vectors or composite centers.  Resume the restricted
theorems from
`results/ZETA23-QP-CENTRAL-PACKET-SQRT-DIMENSION-TRANSVERSE-THEOREM-2026-08-15.md`
and
`results/ZETA23-QP-PRIME-CENTER-ONE-SIDED-BURGESS-CUBIC-SAVING-2026-08-15.md`;
the balanced full-shell frontier remains `49/66`.

The exact residual is the balanced far-side tensor
`|8abc-q^3|<<q^3/B`.  The current Schur norm is `sqrt(R)`.  A modulo-`q^3`
character decomposition is exact but its nonprincipal Parseval floor is
`sqrt(qR)`, so separate Burgess/character closure is provably the wrong tool.
Every fixed-power central- or side-dominant sector does improve `49/66`; the
balanced sector is nonempty.  Continue from
`results/ZETA23-QP-SECTOR-COMBINATION-BALANCED-CROSS-GATE-2026-08-15.md`
and
`results/ZETA23-QP-BALANCED-ALL-PLUS-CHARACTER-METHOD-BARRIER-2026-08-15.md`.

The only live frontiers are:

1. positive definiteness of every full-theta diagonal-excised density `B_P`;
2. the prime-log atomic cancellation dichotomy
   `C_(T,B)=Y^o` versus `C_(T,B)>=Y^delta`;
3. the coefficient-specific Husimi reverse-localization inequality at a
   hypothetical outer-line zero;
4. a candidate-conditioned arithmetic certificate carrying an exact
   nonlocal completion/approximate-functional-equation remainder.

Do not restart generic matrix/quantum lifts, tensor moments beyond the
aperture, finite-head PSD learning, local FFT partitions, separate determinant
estimates, or density arguments which tolerate one zero.  Their exact
conservation laws and kill conditions are in the distilled kernel.

## Latest breakthrough-sprint update — 2026-08-12

The target-only carrier geometry is now closed exactly.  For a hypothetical
target at `gamma`, center the odd critical grid at `gamma` and choose the
endpoint order even.  The selected positive row and inherited Hahn anchor
are even, while the carrier is odd, so `theta_*=1` at finite dimension and

```text
dim S_m^odd=(d-m-1)/2.
```

The existing symmetric endpoint-flat packet theorem supplies an odd state
with carrier `X^(alpha-o(1))/L` for the chosen even order.  No uniform Hahn
tail is needed.  The resulting arithmetic square is exactly cosine-only,
but its sign and actual-zeta collateral isolation remain open.

The unprojected centered square is now an explicit sinh-tent scalar: its
prime term is a fixed combination of `P_T,P_T'` at
`1/2+/-alpha+i*gamma`.  Pointwise evenized positivity has an Arb
counterexample, local positive averaging has too few zeros, and an exact
matched-quartet construction proves that functional equation, reality,
order, and critical-line phase cannot sign the square without
Euler-coefficient input.

Positive harmonic amplification does not repair this: the extremal
nonnegative trigonometric polynomial keeps the target quartet but the
sinh-tent prime weight changes sign, and its mandatory zero harmonic creates
a larger same-sign pole response.

The former microscopic phase-flip obstruction has been removed.  A coherent
fixed-degree endpoint-flat packet signs every collateral row in an arbitrary
bounded rescaled near-confluent cluster, keeps all mixed terms, and retains
`X^(alpha*d-o(1))`.  Balanced bipartite coloring between endpoint legs now
removes the same-state square loss: the selected positive-row equation pays
one total Blaschke product, with an exact real compact realization for fixed
polynomially-conditioned lists.  Broad unit-width isolation remains open at
the growing compact discrete-Pick/phase-cell theorem.  Under the ideal cell
compression its density ledger retains exponent `0.0133834...`, but that
compression is not proved for actual zeta.
The universal one-zero-per-cell inner lattice is not the missing proof: it
signs the complete continuum exactly but spends the entire carrier, and
finite truncation obeys an exact phase/exponent conservation law.  Only a
tailored discrete-Pick construction on occupied clusters survives.
The alternating critical Pick model is exactly solvable at target amplitude
`1/sqrt(cosh(a))`, the half-product exponent.  A five-point cell can require
double-zero local behavior, so the remaining conjecture is global
half-product control rather than one-root-per-cell compression.
Every fixed local Schur-jet order can in fact be forced by a finite cluster,
but no multiplication of those local losses across growing cells is proved.
After correcting the real-dimension count, small factor-two clusters remain
within the current conditional budget; only very large fixed multiplicity
produces a proved adverse conditional ledger.

The prime-null route also has a new exact boundary.  Any finite-band positive
prime-power moment solution descends to a compact scalar two-lobe packet with
the predicted carrier.  Removing the upper frequency cap solves the full
prime-power moment problem with `r>>1/log Y`; the missing input is return of
the actual scalar prime-log orbit before `T=Y^(1/d)`.  Grouped Riesz products
have exact norms `exp(Theta(rM))` and `exp(Theta(r^2M))`, so the audited
bounded-degree absolute and stable-Gram transfers stop at fixed-power scale.
This does not upper-bound the unrestricted finite-band convex program.
The bipartite divisor filters and prime nulls do coexist exactly for every
fixed list.  At growing scale their joint problem is a twisted prime-hull
inradius (or one aggregate Schur angle), neither of which is presently
bounded uniformly.
The direct ordinary Montgomery-mean-value/derivative conversion also stops
at the exact conductor transition: `max(1/d,q)-q>=0` for every fixed moment
order `q`; its explicit `4^q q!` form remains trivial for growing `q`.

The current hostile-audited synthesis is:

- `results/ZETA23-BREAKTHROUGH-SPRINT-CENTERED-PARITY-AND-PRIME-MOMENT-SYNTHESIS-2026-08-12.md`;
- `results/ZETA23-CENTERED-EVEN-JET-PARITY-COMPANION-2026-08-12.md`;
- `results/ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md`;
- `results/ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md`;
- `results/ZETA23-HARMONIC-CENTER-SINH-TENT-AMPLIFICATION-NOGO-2026-08-12.md`;
- `results/ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md`;
- `results/ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md`;
- `results/ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md`;
- `results/ZETA23-GLOBAL-PHASE-CELL-COMPRESSION-PICK-LATTICE-GATE-2026-08-12.md`;
- `results/ZETA23-HALF-DISK-PICK-EXTREMAL-PROBE-2026-08-12.md`;
- `results/ZETA23-TAILORED-DISCRETE-PICK-JET-OBSTRUCTION-2026-08-12.md`;
- `results/ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md`;
- `results/ZETA23-POSITIVE-SPECTRAL-PRIME-NULL-SQUARE-ROOT-GATE-2026-08-12.md`;
- `results/ZETA23-PRIME-RIESZ-PRODUCT-SCALAR-ORBIT-GATE-2026-08-12.md`;
- `results/ZETA23-PRIME-LOG-EARLY-RETURN-MEAN-VALUE-GATE-2026-08-12.md`.

No bound on a zeta zero has moved.  The smallest live closure package is a
uniform centered one-square arithmetic sign plus an actual-zeta collateral
support-function bound on the same state.

## Superseding research update — 2026-08-12

The 2026-08-11 frontier below is now historical.  In particular, the
formerly described conditional `3/4` target and the later formal `5/6` and
`7/8` ledgers are **not** proved zeta edges.

The then-current exact state was:

- the selected one-pair asymmetric carrier has a normalized
  Paley--Wiener/Gabor realization, including all growing endpoint jets;
- in that mirror block, positive-row nulling aligns the completed aggregate
  arithmetic row with the negative carrier, so even one real aggregate
  cancellation can erase the carrier exactly;
- current counts and moments do not control a carrier-sized transverse
  collateral row.  Normalized sampling proves that all collateral pairs
  below depth `alpha*d-epsilon` are subcarrier, but one
  `alpha-o(1/log T)` near-tie is permitted.  The explicit two-pair reservoir
  is presently an abstract operator/moment construction, not a normalized
  joint Gabor realization or an actual zeta divisor;
- positive multi-witness and multiscale ensembles, unused quadratures,
  block randomization, local positivity gluing, low-order nonlinear
  certificates, deterministic critical pole/main resonance, and coherent
  Mellin-scale filtering have all been audited.  None supplies a free
  escape;
- a category-theoretic consolidation reduces those routes and the older
  trace/polarization branches to four exact lemmas.  In the carrier
  associated grade, the unresolved datum is the target-transverse part of
  the actual prime/collateral remainder; it is a corona class when uniformly
  bounded, while unbounded normalized growth is a separate analytic case.
  Uniformly bounded grade-preserving changes of representation cannot create
  either, while an ill-conditioned change must pay its amplification in the
  transported norm;
- the expanded categorical search grammar leaves only five kinds of genuinely
  new input: relative order reflection, a carrier-grade transverse arithmetic
  term, a signed nonlinear cross-effect, an independently positive
  polarization, or a carrier-conservative limit/index.  The most executable
  finite tests have now been executed.  Fixed finite scalar probes fail on the
  first asymmetric two-packet system; parity recovery and the natural
  covariance only recover the old spectral/Schur tests.  The formerly
  prioritized target-subtracted carrier support has now been executed and
  pruned: on the selected quotient it is exactly `N_T+K_ar,T`, so it inserts
  an aligned baseline and discards dual multipliers in `[0,1)`.  The surviving
  object is the direct constrained arithmetic edge `q_eta(K_ar,T)`.  An
  actual-coefficient fixture through `T=512` validates the assembly in
  floating arithmetic but proves no uniform sign.  A later adversarial scan
  covered 61,896 full-carrier and 11,565 sub-full configurations without a
  negative; the closest point was rigorously proved positive with Arb.  This
  is a finite fail-fast result, not asymptotic evidence.  An exact `2 x 2`
  Ritz theorem reduces admission to one joint completed orientation
  inequality; separate KMT estimates do not prove it.  Approximate
  polarization remains high-risk only after a positive middle degree and a
  zeta-divisor generator are constructed;
- fixed-width near-tie rows have a collision-stable Hermite limit, and after
  every represented positive row is imposed their leading mirror blocks have
  one sign.  This does **not** extend to the target-only quotient.  A strictly
  deepest target plus two `o(1/L)`-shallower pairs at ordinate gaps
  `+/-pi/D` gives a normalized positive carrier-scale screen.  Existing bulk
  zero inputs permit but do not imply this sparse pattern.  A universal
  positive average over separations cannot remove it without losing a fixed
  carrier power;
- the exact remaining choices are a joint actual coefficient-specific
  completed-orientation theorem, a finite-list/coherent separation theorem
  with all arithmetic cross terms retained, genuinely new zeta-specific
  local spacing/depth input, or a direct fixed-power arithmetic estimate
  already of strip strength; and
- the opposite hypothesis is also open.  If
  `Theta=sup Re(rho)`, RH is `Theta=1/2`, while failure of every fixed strip
  is the strictly stronger assertion `Theta=1`.  No accepted theorem proves
  even one zeta zero with `Re(rho)>1/2`.

Start with:

- `results/ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md`;
- `results/ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`;
- `results/ZETA23-SEPARATION-AVERAGE-POSITIVE-COSINE-NOGO-2026-08-12.md`;
- `results/ZETA23-PHASE-FLIP-AND-SEPARATION-AVERAGE-REFEREE-ADDENDUM-2026-08-12.md`;
- `results/ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md`;
- `results/ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`;
- `results/ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`;
- `results/ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md`;
- `results/ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md`;
- `results/CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md`;
- `results/ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md`;
- `results/UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md`;
- `results/ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`;
- `results/ZETA23-CRITICAL-POLE-MAIN-AND-MELLIN-SCALE-ESCAPE-AUDIT-2026-08-12.md`;
- `results/ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md`;
- `results/ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md`; and
- `results/ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md`.

No uniform zero-free strip, failure of a uniform strip, RH proof, or ZFC
independence result has been obtained.  Do not revive a numerical edge from
an older section without reconciling it with the 2026-08-12 master audit.

## Superseding research update — 2026-08-11

The original frontier below is historical.  The publication-facing Lean
closure has since been rebuilt and content-rehash checked, Anthropic's Zeta23
density theorem has been audited and integrated, and the active strip branch
has moved to a growing-support Gabor/endpoint-packet problem.

The then-current exact state was:

- one core off-line pair against only on-line competitors retains the full
  endpoint-jet edge `K>=X^(alpha-o(1))/L`;
- a hostile-audited sparse tapered `k=3` island preserves the current count,
  simple-line-density, trace, Frobenius, and pair-correlation inputs while
  reducing that edge to `K<=X^(2*alpha/3+o(1))`;
- the explicit endpoint-flat two-lobe packet reduces its only power-sized
  completed arithmetic term to a smooth centered von Mangoldt polynomial;
  the needed estimate is `o(Y^alpha)`, while the best directly applicable
  unconditional result remains `Y^(1/2-o(1))`; and
- exact all-head recompletion retains the ordinary coefficient
  `-mu(n)log(n)`.  Endpoint jets, nonzero reciprocal phases, and raw
  dimension counts do not delete it;
- optimizing the two lobes is exactly a Wiener-`l^1` prime-log extremal;
  KMT gives a logarithmic upper bound but no matching lower bound or fixed
  power loss; and
- the formal `0.597907...` two-lobe edge is contradicted by the sparse
  island on the current inputs.  The first non-refuted numerical target is
  the still-conditional edge `3/4+epsilon`.

The live high-risk target is a target-conditioned prime/zero translate
theorem: either prove subpower joint leverage for every proportional lobe
width `a>1/3`, or use new zeta-specific information to exclude the sparse
`k=3` geometry and work below that threshold.  A nonzero algebraic kernel is
insufficient.  Global simple-line density permits locally dense off-line
clusters, while the prime part lives in a Wiener rather than Hilbert norm, so
both sides require quantitative structure beyond dimension counting.

Start with:

- `results/UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md`;
- `results/ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md`;
- `results/ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md`;
- `results/ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`;
- `results/ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`;
- `results/ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md`;
- `publication/ANTHROPIC-ZETA23-INTEGRATION.md`; and
- `results/RESEARCH-AUDIT-AND-PUBLICATION-ASSESSMENT-2026-08-10.md`.

No uniform zero-free strip or RH proof has been obtained.  Do not revive the
old adjacent-support implementation plan without first reconciling it with
the sparse-island and packet obstructions above.

This file is the compact context seed for a **new** Codex chat. Inherit the
written state below, not any prior transcript. Open the larger recovery and
registry files only at targeted sections when a claim needs verification.

## Repository snapshot

- Working tree: `/home/ubuntu/Projects/Riemann-Zeta`
- Branch: `master`, one commit ahead of `origin/master`
- HEAD: `4ad72dca0c1b63defa2657afd153ddfe4e01ce5e`
  (`checkpoint: recovered RH research state (unreviewed)`)
- Pre-existing untracked `error.log` contains private account data: do not
  quote, stage, commit, or modify it.
- `RECOVERY_STATE.md` is the comprehensive archival recovery record. It is
  intentionally much larger than this handoff and should not be loaded whole
  unless a discrepancy requires it.

## Truth boundary

This repository does **not** prove or disprove the Riemann hypothesis. It
contains rigorous local/formal reductions, conditional implications, open
analytic premises, and explicitly catalogued failed routes. Preserve those
distinctions in every report and commit message.

## Current mathematical frontier

The preferred branch is uniform-in-support propagation for the arithmetic
Weil form.

- Completed abstract Lean scaffolding: old/collar two-block Schur algebra,
  positive finite-product propagation along a cofinal support sequence, and
  the abstract implication from a genuine propagation package to global Weil
  positivity.
- Important simplification: adjacent factors need only be strictly positive
  one step at a time. No common lower bound or positive infinite product is
  required.
- Main open gate: a **zeta-specific adjacent-support relative estimate** with
  the correct logarithmic form domain. Equivalently, one needs noncircular
  old/collar lower bounds and a cross estimate giving a strict determinant
  inequality `c^2 < beta*d` at every cofinal step.
- Known hazards: sharp old/collar projections may leave the logarithmic form
  domain; a two-sliver family defeats naive local margins; the activation
  defect symbol vanishes at zero frequency; assuming target-block positivity
  in order to prove it is circular.

A parallel R176 contour branch has closed the generic Hardy/Carleman escape.
Its surviving premise is a coefficient-specific upper bound for the
complementary harmonic `log^+` mean, uniform over the full hypothetical-zero
and contour geometry. This is open and would at most yield a fixed zero-free
strip under the stated package, not RH by itself.

## Immediate next task

1. Attack the completed arithmetic edge through the exact low-dimensional
   Ritz card.  Choose a prime-independent background/confluent companion and
   prove the joint inequality for `(r,d,<w,b>)`; do not bound its three
   entries separately.  Alternatively use the Lanczos companion only with an
   explicit quadratic/cubic completed-prime correlation theorem.
2. Keep the interval direct-`q` scanner as a falsifier.  Extend it adaptively
   to larger heights and replay every near-zero candidate with Arb.  More
   positive finite samples cannot prove a uniform sign.
3. Do not seek divisor isolation from the all-positive-row mirror theorem:
   the target-only phase-flip report gives a normalized counterconfiguration.
   The remaining zero-side experiment is the finite-list convex separation
   problem with every coherent cross-scale arithmetic term retained.  A
   universal positive separation average is already ruled out.
4. A strip still needs two uniform statements on the same quotient:
   arithmetic admission `q_eta>=0` and actual-target exclusion `q_eta<0`.
   Current results prove neither.  New local zeta spacing/depth information
   would be an alternative to the finite-list construction.
5. Do not reopen scalar-probe refinements, the obvious dephasing covariance,
   ungraded Lyapunov optimization, or universal positive separation
   averaging.

Execution details are in
`results/CATEGORICAL-ADMISSION-TESTS-EXECUTION-SYNTHESIS-2026-08-12.md`;
the independent audit verdict is **PASS AFTER PATCHES** in
`results/CATEGORICAL-ADMISSION-TESTS-REFEREE-AUDIT-2026-08-12.md`.

## Targeted source map

- Executed admission synthesis:
  `results/CATEGORICAL-ADMISSION-TESTS-EXECUTION-SYNTHESIS-2026-08-12.md`
- Independent admission audit:
  `results/CATEGORICAL-ADMISSION-TESTS-REFEREE-AUDIT-2026-08-12.md`
- Corrected direct carrier frontier:
  `results/ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md`
- Three-step direct carrier iteration:
  `results/ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md`
- Interval direct-`q` fail-fast:
  `results/ZETA23-SUBFULL-DIRECT-Q-FAILFAST-AND-ARB-CERTIFICATE-2026-08-12.md`,
  `src/subfull_direct_q_failfast.py`
- Exact low-dimensional Ritz gate:
  `results/ZETA23-SUBFULL-RITZ-LOEWNER-ADMISSION-GATE-2026-08-12.md`,
  `src/carrier_ritz_loewner_gate.py`
- Near-tie and target-only geometry:
  `results/ZETA23-NEAR-TIE-GRAM-AND-MIRROR-ALIGNMENT-2026-08-12.md`,
  `results/ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`,
  `results/ZETA23-SEPARATION-AVERAGE-POSITIVE-COSINE-NOGO-2026-08-12.md`
- Three-step and follow-on audits:
  `results/ZETA23-THREE-STEP-DIRECT-CARRIER-PROGRAM-REFEREE-AUDIT-2026-08-12.md`,
  `results/ZETA23-PHASE-FLIP-AND-SEPARATION-AVERAGE-REFEREE-ADDENDUM-2026-08-12.md`
- Exact aligned-baseline no-go:
  `results/ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md`
- Actual-coefficient high-height fixture:
  `results/ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md`,
  `src/high_height_carrier_slice.py`
- High-height hostile audit:
  `results/HIGH-HEIGHT-CARRIER-SLICE-REFEREE-AUDIT-2026-08-12.md`
- Analytic target-only quotient reduction:
  `results/ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md`
- Carrier-slice theorem and fixtures:
  `results/ZETA23-CARRIER-SLICE-SUPPORT-FINITE-FIXTURE-2026-08-12.md`,
  `src/carrier_slice_support.py`
- Operator-system gate:
  `results/ZETA23-FINITE-OPERATOR-SYSTEM-ADMISSION-GATE-2026-08-12.md`,
  `src/categorical_operator_system_gate.py`
- Approximate-polarization fail-fast:
  `results/ZETA23-APPROXIMATE-POLARIZATION-SEMILOCAL-FAIL-FAST-2026-08-12.md`,
  `src/approximate_polarization_gate.py`
- Categorical construction grammar:
  `results/ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`
- Completed Gabor carrier reduction:
  `results/ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`
- Canonical claim statuses: `results/RH-PROXY-LEDGER.md`
- Reduction status, especially R3 and R176: `results/REDUCTION-REGISTRY.md`
- Failed-route registry: `NO-GO-ATLAS.md`
- R176 details: `results/R176-HARDY-MODE-CARLEMAN-AND-ONE-SIDED-CONTOUR-GATE.md`
- Full recovery/audit record: `RECOVERY_STATE.md`

Toolchain recorded by the recovery checkpoint: Lean `4.32.1`, mathlib revision
`520045ab14e26149ee970e2e617ca04b09bde5d6`. Some literature bridges remain
explicit axioms; inspect the relevant `#print axioms` audit before promoting
any formal implication to an unconditional theorem about zeta.

## Operating guardrails

- Fix the provenance and normalization of `S_T,N_T,R_T` before evaluating
  signs or tuning parameters.
- Treat direct carrier-edge numerics only as admission diagnostics until their
  matrices and error bounds are certified; do not infer a strip from a finite
  positive value or revive the baseline-contaminated target-subtracted
  support.
- Do not start additional scalar-probe or support-window campaigns until the
  actual high-height remainder is assembled or reduced to a minimal theorem.
- Keep analytic error bounds explicit and, where this project requires it,
  verified in Lean.
- Do not contact external people or services on the user's behalf.
- Do not resume, import, or summarize old Codex sessions. They are preserved
  separately only as a recovery fallback.

## Bootstrap prompt for the fresh chat

> Treat `CODEX_HANDOFF.md` as the sole inherited conversational context. Do
> not resume old Codex threads or load `RECOVERY_STATE.md` wholesale. Verify
> the lightweight Git snapshot, then execute the “Immediate next task,”
> consulting only the targeted files and sections needed. Preserve the truth
> boundary and report the first candidate theorem card or decisive obstruction.
