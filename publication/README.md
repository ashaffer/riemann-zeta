# Guide to the mathematical artifact

This directory is the human-facing entrance to the repository.  It is meant
to let a mathematician understand the ideas, theorem boundaries, and formal
trust structure before reading generated data or tactic proofs.

The repository does **not** prove or disprove the Riemann Hypothesis.  Its
strongest zeta-facing result is a strict local lower bound for an explicitly
defined arithmetic Weil form at one compact-support endpoint.  The equality
with the corresponding sum over zeta zeros remains an explicit literature
assumption, and no uniform all-support positivity theorem is claimed.

## Recommended reading routes

### For a mathematician

1. [`MATHEMATICAL-OVERVIEW.md`](MATHEMATICAL-OVERVIEW.md) gives the main
   definitions, result, proof architecture, and missing global bridge.
2. [`IMPORTED-ANALYTIC-BASELINE.md`](IMPORTED-ANALYTIC-BASELINE.md) is the
   primary-source theorem baseline for the active analytic program.  Read it
   before treating a zero-free, PNT, Mertens, mean-value, density,
   short-interval, decomposition, or Euler-transfer estimate as a research
   target.
3. [`FIXED-WINDOW-WIDTH-AND-TYPE-II-REDUCTION.md`](FIXED-WINDOW-WIDTH-AND-TYPE-II-REDUCTION.md)
   is the canonical short account of the fixed-window detector, the balanced
   Vaughan reduction, and the exact scope of its global-cancellation barriers.
   Its current complete-center dispersion candidate and fixed-step spectral
   cooling fork are recorded in
   [`../results/COBOUNDARY-DISPERSION-CANCELLATION-CANDIDATE.md`](../results/COBOUNDARY-DISPERSION-CANCELLATION-CANDIDATE.md).
   The subsequent fluctuation--dissipation/connected-cluster audit is
   [`../results/WARD-INNOVATION-SCREENING-CANDIDATE.md`](../results/WARD-INNOVATION-SCREENING-CANDIDATE.md);
   its final nonlocal lift is closed in
   [`../results/NONLOCAL-WARD-COVARIANCE-NOGO.md`](../results/NONLOCAL-WARD-COVARIANCE-NOGO.md).
   The resulting direct full-energy target and its fail-fast audit are
   [`../results/DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md`](../results/DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md).
   Its final Mobius-specific cutoff/Riccati attack is
   [`../results/MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md`](../results/MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md).
   The sharp exceptional-set width gate is
   [`../results/MINIMUM-WIDTH-LARGE-VALUE-GATE.md`](../results/MINIMUM-WIDTH-LARGE-VALUE-GATE.md),
   followed by the exact fourth-moment-to-fixed-strip calibration and its
   fail-fast audits in
   [`../results/FIXED-UNIFORM-ZERO-FREE-STRIP-SPRINT.md`](../results/FIXED-UNIFORM-ZERO-FREE-STRIP-SPRINT.md).
   The subsequent direct proof attempt, sharp `p Delta` moment theorem,
   pair-cell reduction, and high-order-filter no-go are in
   [`../results/FIXED-STRIP-FOURTH-MOMENT-PROOF-ATTEMPT.md`](../results/FIXED-STRIP-FOURTH-MOMENT-PROOF-ATTEMPT.md).
   The follow-up recurrence audit proves positive lower Banach density when
   the spectral edge is attained and isolates non-attainment as the exact
   escape in
   [`../results/EDGE-ATTAINMENT-RECURRENCE-GATE.md`](../results/EDGE-ATTAINMENT-RECURRENCE-GATE.md).
   The formerly formal fixed-step Vinogradov--Korobov calibration is proved
   for both the cutoff-independent exact-head field and the frozen evaluated
   center in
   [`../results/FULL-FIELD-VK-SUBPOWER-BOUND.md`](../results/FULL-FIELD-VK-SUBPOWER-BOUND.md).
   The proportional-order follow-up removes the nonattained-edge loophole,
   transfers the bank to a retreated evaluated center, and audits the current
   Type-II and Kloosterman interfaces in
   [`../results/PROPORTIONAL-ORDER-DETECTOR-BANK-GATE.md`](../results/PROPORTIONAL-ORDER-DETECTOR-BANK-GATE.md).
   The completion-preserving additive-mode audit then corrects the proposed
   literature lift: the center can be allocated exactly cofactor by cofactor,
   the completed field has only nonzero direct lattice modes, and an
   individual zero carrier persists on a universal shell-normalized band for
   the actual proportional windows.  The off-axis lattice has Wright's exact
   reciprocal phase, but its coupled amplitude, zero sectors, and completed
   Mertens mode are not covered; a finite Ramanujan basis isolates the latter
   without estimating it.  Fixed rational major arcs retain prime and
   zeta/Dirichlet-zero carriers.  Limiting-coefficient truncation fails in
   `L2`, while absolute cofactor damping buys less than the horizontal shift
   it pays.  See
   [`../results/COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md`](../results/COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md).
   The joint-Schur follow-up proves that the finite Mertens zero coefficient
   is gauge-dependent: a scale-adapted Ramanujan null cloud moves it exactly
   into nonzero modes with the same polylogarithmic ledger.  The augmented
   center Schur complement is therefore zero.  Generic frame estimates fail
   on the resulting coherent Farey direction.  Exact theta completion returns
   the original physical correlation; with its diagonal, the separate native
   upper-half packet is centered prime covariance.  See
   [`../results/FINITE-RAMANUJAN-NULL-GAUGE-GATE.md`](../results/FINITE-RAMANUJAN-NULL-GAUGE-GATE.md).
   The quotient follow-up proves that null-orbit optimization only transfers
   natural-size energy into an exact contact term.  It clears the
   determinant-zero singular-series fluctuation and isolates the completed
   one-point prime axis that must cancel jointly with the off-axis block.  It
   also proves the Ramanujan-matrix determinant `Y!` and an exact
   square-root-modulus Farey-beat frame; the latter preserves the low-beat
   prime carrier and lies outside current separable Wright estimates.  See
   [`../results/GAUGE-QUOTIENT-SECTOR-RECOMPLETION-GATE.md`](../results/GAUGE-QUOTIENT-SECTOR-RECOMPLETION-GATE.md).
   The coefficient-specific follow-up corrects the last sentence's generic
   tensor diagnosis: a global common dual has coefficients
   `W(theta/(pr))`, so log-Mellin separation avoids the apparent
   `Y^(1/4)` rank loss.  In the original nonprimitive cofactor expansion,
   grouping `k=j theta` also makes the actual R81 amplitude scalar-Wright
   admissible before the remaining kernel ledger; the finite primitive basis
   retains an open common-`g` mask.
   The route still stops because the canonical coefficient multiplies the
   slow additive beat while the native product coefficient multiplies the
   reciprocal phase.  Prescribing native low coefficients forces an
   ill-conditioned prolate high-beat repair.  See
   [`../results/COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md`](../results/COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md).
   The arithmetic-centering follow-up then identifies the exact fixed-power
   boundary.  The inverse phase must be centered at its Ramanujan mean
   `c_r(k)/(r-1)`, not at one.  Current Kloosterman-fraction estimates can
   power-save the resulting nonresonant mean-zero component, nominally by
   `H^(-1/40)` after the outstanding kernel ledger, but the complementary
   projection is still the full canonical `gamma` contact.  Integration by
   parts can move the nonconstant mismatch onto a reciprocal derivative term
   without changing that projection.  An exact affine null gauge exists at
   top-prime scale but costs `Y/T` on the low determinant band; at
   square-root scale its defect is the original near-square Type-II tensor.
   See
   [`../results/NATURAL-MEAN-AFFINE-FIXED-POWER-GATE.md`](../results/NATURAL-MEAN-AFFINE-FIXED-POWER-GATE.md).
   The signed follow-up then keeps the Type-II tensor and `-gamma` together.
   Its exact shifted-Ramanujan operator has no reciprocal zero character;
   the zero orbit of the joint difference is the complete canonical carrier.
   Whitening produces dissipative and Schur-leakage squares but no small
   parameter, and positive native prime weights give a uniform full-scale
   residual at prime target points.  Thus natural square-root-frame
   contraction is closed.  A specially weighted cancellation in the full
   R71 kernel, with every cofactor, axis, seam, and Type-I correction retained,
   remains open.  See
   [`../results/SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md`](../results/SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md).
   The full-kernel audit now proves that exact sector recompletion reconstructs
   the original prime-minus-continuum energy; neither common-factor masks,
   axes, B-spline seams, nor Type I cancel the carrier for free.  The later
   orthogonal gates reduce the cleanest scalar alternative to one fixed power
   beyond `k^(-1/2)` for the Newton coefficients.  Exact Muntz quadrature,
   q-free counting, differentiated positivity, bounded-arity Mobius flow,
   harmonic cascades, and tempered prime-support interpolation all fail for
   explicit reasons.  See
   [`../results/FULL-R71-RECIPROCAL-RESPONSE-GATE.md`](../results/FULL-R71-RECIPROCAL-RESPONSE-GATE.md)
   and
   [`../results/R90-NEWTON-COEFFICIENT-CANCELLATION-GATE.md`](../results/R90-NEWTON-COEFFICIENT-CANCELLATION-GATE.md).
   The subsequent positivity audit first shows that every normally
   convergent discrete pole-cancelling multiplier vertically recurs, so
   eta/modulus scalarization necessarily creates fake zeros near one.  A
   genuinely continuous Pareto dilation law escapes that obstruction and
   gives the bounded nonnegative harmonic-sawtooth carrier
   `A(x)=floor(x)(floor(x)+1-x)/x`, whose Mellin transform is exactly
   `(s-1)zeta(s)/[s(s+1)]`.  It has no artificial zeros.  See
   [`../results/R91-ETA-POSITIVE-INTERVAL-NONVANISHING-GATE.md`](../results/R91-ETA-POSITIVE-INTERVAL-NONVANISHING-GATE.md)
   and
   [`../results/R92-NONLATTICE-POLE-CANCELLING-CARRIER-GATE.md`](../results/R92-NONLATTICE-POLE-CANCELLING-CARRIER-GATE.md).
   Higher Pareto divided differences make this carrier positive and
   arbitrarily finitely smooth, but the first unsmoothed derivative retains
   a unit jump at every `log n`; its weighted variation is still
   `sum n^(-sigma)` and therefore stops exactly at `sigma=1`.  Functional-
   equation complementary tilts, finite multigap filters, mod-6 matrices,
   infinite-divisibility, and ordinary Luroth transfer moments all fail
   exact checks.  The surviving theorem must sign the actual integer-cell or
   prime-atom cancellation before total variation.  See
   [`../results/R93-HIGHER-ORDER-PARETO-DIVIDED-DIFFERENCE-GATE.md`](../results/R93-HIGHER-ORDER-PARETO-DIVIDED-DIFFERENCE-GATE.md)
   and
   [`../results/R93-LUROTH-INFINITE-DIVISIBILITY-GATE.md`](../results/R93-LUROTH-INFINITE-DIVISIBILITY-GATE.md).
   The next audit makes the remaining cancellation quantitative.  Luroth
   mixing contracts every later lag but cannot be inverted to the zeta-bearing
   first lag; its coherent tail leaves a finite signed head of the first
   `O(t^2)` digits.  Finite Mobius heads recur vertically, but every such
   return forces an order-one conditional tail and makes the translated
   reciprocal-zeta family nonnormal near the pole.  Finally, even optimal
   phase-aware positive transport between the prime powers and the pole
   continuum has convergence threshold exactly `sup Re(rho)`, because the
   radial coordinate of the Mellin spiral still sees the full cumulative PNT
   discrepancy.  See
   [`../results/R94-LUROTH-FORWARD-CORRELATION-GATE.md`](../results/R94-LUROTH-FORWARD-CORRELATION-GATE.md),
   [`../results/R94-RECIPROCAL-ZETA-VERTICAL-RECURRENCE-GATE.md`](../results/R94-RECIPROCAL-ZETA-VERTICAL-RECURRENCE-GATE.md),
   and
   [`../results/R94-PRIME-POLE-PHASE-TRANSPORT-GATE.md`](../results/R94-PRIME-POLE-PHASE-TRANSPORT-GATE.md).
   The R95--R96 continuation sharpens all three survivors.  The Luroth head
   is linear in height and its complete Poisson sum is exactly the
   complementary value `zeta(1-s)`, with no leftover sign sector.  Mobius
   recurrence is valid in global `B^2`, but prime conditioning selects Euler
   order rather than the natural order controlled by a hypothetical strip;
   the discrepancy is an order-one tail and produces explicit local spikes.
   A continuous scale filter yields one bounded signed von Mangoldt ramp for
   which either one-sided fixed-power envelope would prove a fixed strip, but
   positivity, lcm, complementary-pairing, scale, and Selberg identities do
   not prove that envelope.  See
   [`../results/R96-LUROTH-GLOBAL-ALIAS-POISSON-GATE.md`](../results/R96-LUROTH-GLOBAL-ALIAS-POISSON-GATE.md),
   [`../results/R96-MOBIUS-BESICOVITCH-RECURRENCE-GATE.md`](../results/R96-MOBIUS-BESICOVITCH-RECURRENCE-GATE.md),
   and
   [`../results/R96-ONE-SIDED-VON-MANGOLDT-RAMP-GATE.md`](../results/R96-ONE-SIDED-VON-MANGOLDT-RAMP-GATE.md).
   The R97 topology audit then tests whether operator or nonlinear Euler
   completion can cross the same boundary.  Hilbert--Schmidt Fredholm
   regularization removes exactly the first prime trace carrying the
   reciprocal divisor, and that trace is nonclosable in the Hilbert--Schmidt
   topology.  Scalar prime cancellation can lower coefficient thresholds,
   but only by deleting the zero at one; zero-preserving scalar germs retain
   squarefree almost-prime layers, while any lower-threshold normally
   convergent carrier acquires recurrent artificial zeros near one.
   Exceptional unimodular multiplicative twists reduce to normal nonzero
   Euler multipliers.  See
   [`../results/R97-FERMIONIC-FREDHOLM-TRACE-ANOMALY-GATE.md`](../results/R97-FERMIONIC-FREDHOLM-TRACE-ANOMALY-GATE.md),
   [`../results/R97-NONLINEAR-EULER-PRIME-ZETA-RIGIDITY-GATE.md`](../results/R97-NONLINEAR-EULER-PRIME-ZETA-RIGIDITY-GATE.md),
   and
   [`../results/R97-EXCEPTIONAL-MULTIPLICATIVE-TWIST-GATE.md`](../results/R97-EXCEPTIONAL-MULTIPLICATIVE-TWIST-GATE.md).
   Finally, R98 assumes a fixed strip and audits every standard feedback
   route.  PNT/Mertens converses, Turan, density, mollifiers, repulsion, and
   functional symmetry all return the same rightmost-zero exponent or only
   make exceptions sparse; none yields a strict bootstrap.  See
   [`../results/R98-QUASI-RH-BOOTSTRAP-GATE.md`](../results/R98-QUASI-RH-BOOTSTRAP-GATE.md).
4. [`LEAN-ANALYTIC-INFRASTRUCTURE.md`](LEAN-ANALYTIC-INFRASTRUCTURE.md) explains
   the reusable analysis as ordinary mathematics rather than as a file list.
5. [`CERTIFICATE-GUIDE.md`](CERTIFICATE-GUIDE.md) explains what the exact
   certificates prove and how they enter the conceptual argument.
6. [`NO-GO-THEOREM-GUIDE.md`](NO-GO-THEOREM-GUIDE.md) organizes the negative
   results by mathematical mechanism.
7. [`../PUBLICATION.md`](../PUBLICATION.md) ranks possible papers and library
   contributions conservatively.

### For a Lean contributor

1. Read [`LEAN-ANALYTIC-INFRASTRUCTURE.md`](LEAN-ANALYTIC-INFRASTRUCTURE.md).
2. Use [`../lean/UPSTREAMING.md`](../lean/UPSTREAMING.md) for proposed extraction
   boundaries and review-sized packages.
3. Use [`../lean/README-verify.md`](../lean/README-verify.md) for focused builds
   and axiom audits.  The projects are intentionally checked serially on this
   machine because some certificate modules have high peak memory use.
4. Treat RH-specific wrappers and generated numerical witnesses as application
   artifacts, not as part of a general-purpose mathlib contribution.

### For a referee or independent reproducer

1. [`PROOF-STANDARD.md`](PROOF-STANDARD.md) defines the evidence classes and
   theorem contract.
2. [`REFEREE-CHECKLIST.md`](REFEREE-CHECKLIST.md) is the release audit.
3. [`NO-GO-REFEREE-RESPONSE.md`](NO-GO-REFEREE-RESPONSE.md) records the first
   adversarial disposition of the obstruction atlas.
4. [`../NO-GO-ATLAS.md`](../NO-GO-ATLAS.md) is the canonical scope and proof-debt
   ledger for negative results.

## The four layers

The project is easiest to assess when its layers are kept separate.

| Layer | What belongs there | What establishes it |
|---|---|---|
| Mathematical statement | Definitions, hypotheses, theorem, proof idea, limitations | Human-readable exposition and theorem cards |
| Reusable formal machinery | General analysis, Hilbert-space, contour, and matrix lemmas | Lean source plus focused axiom audits |
| Exact application | Rational witnesses, interval enclosures, and their composition with the general lemmas | Kernel-checked certificate modules or explicitly stated software trust base |
| Exploration | Numerical scans, failed mechanisms, and conjectural patterns | Reproducible experiments, never promoted to theorem status |

A generated certificate is therefore a leaf of the proof tree.  It supplies
exact arithmetic data after the mathematical reduction has been stated and
proved; it is not intended to carry the explanation.

## Canonical sources of claims

To avoid several documents slowly acquiring incompatible versions of the same
claim, use these sources in this order:

- exact Lean statement and its focused audit for formal dependency questions;
- [`IMPORTED-ANALYTIC-BASELINE.md`](IMPORTED-ANALYTIC-BASELINE.md) for what
  the active analytic program treats as established literature or classical
  synthesis rather than a research target;
- [`../NO-GO-ATLAS.md`](../NO-GO-ATLAS.md) for the scope of obstruction results;
- [`../PUBLICATION.md`](../PUBLICATION.md) for publication status and novelty;
- [`MANUSCRIPT-BRIEFS.md`](MANUSCRIPT-BRIEFS.md) for proposed paper structure;
- historical files in `results/` only for branch provenance and experimental
  detail.

If a historical report conflicts with a current theorem card or audit, the
current theorem card and audit govern.
