# Guide to the mathematical artifact

> **Research-frontier notice (2026-09-02):** for current priorities and
> nonclaims, read
> [`ZETA23-POST-SYNTHESIS-DECISION-PATH-2026-09-02.md`](../results/ZETA23-POST-SYNTHESIS-DECISION-PATH-2026-09-02.md)
> and its linked correction artifacts.
> This publication guide remains authoritative for its scoped artifacts, not
> for the latest exploratory decision tree.

This directory is the human-facing entrance to the repository.  It is meant
to let a mathematician understand the ideas, theorem boundaries, and formal
trust structure before reading generated data or tactic proofs.

The repository does **not** prove or disprove the Riemann Hypothesis.  Its
strongest zeta-facing result is a strict local lower bound for an explicitly
defined arithmetic Weil form at one compact-support endpoint.  The equality
with the corresponding sum over zeta zeros remains an explicit literature
assumption inside this build, and no uniform all-support positivity theorem is
claimed.  Anthropic's independent Zeta23 development now proves a compatible
smooth explicit formula and a major positive-density theorem; its precise
integration seam and its inability to imply a uniform strip are audited in
[`ANTHROPIC-ZETA23-INTEGRATION.md`](ANTHROPIC-ZETA23-INTEGRATION.md).
The standalone note
[`ROUGH-GAP-SECOND-MOMENT.md`](ROUGH-GAP-SECOND-MOMENT.md) proves a
second-moment bound for gaps between polynomially rough integers uniformly
through the exponent `3/16-epsilon`; it has no zeta-strip consequence.
The standalone finite-dimensional note
[`SPARSE-POSITIVE-COSINE-ANTIPODES.md`](SPARSE-POSITIVE-COSINE-ANTIPODES.md)
proves that `M` is the sharp sparse scale for positive cosine antipodes:
generic deepest finite-pool solutions are unique and exactly `M`-atomic,
while every prescribed `M`-harmonic support and every depth below one has an
exact realization inside an open positive chamber.  A harmonic-progression
first return is therefore one sufficient promotion mechanism, but it is not
the full prime-log problem: the optimizer may use `M` arbitrary,
incommensurable atoms.  The full positive obstruction is now exactly the
one-sided Delsarte value `A_H` for the actual prime-log nodes, with promoted
depth `r_+=1/(A_H-1)`.  A legal Bernoulli construction gives only exponential
depth, bounded/polylogarithmic grouping cannot reach the target, and a
continuum random-node model is overwhelmingly on the KILL side.  No known
actual-prime theorem estimates `A_H` at the required fixed-power scale, so
this remains open and has no strip consequence by itself.  The latest direct
attack proves that KMT covers the full aperture and repairs any one natural
prime packet with negligible positive-weight loss, but simultaneous adaptive
repair is the genuine obstruction.  A packet count cannot be upgraded to a
uniform projected-Gram theorem: consecutive packets have an exponentially
small binomial direction, and even perfect unprojected orthogonality can
saturate the critical minimax value in an abstract bounded-entry model.  The
exact surviving condition is the actual-prime carrier-residual Delsarte
inequality, not a condition number.  Scalar KMT estimates pay a sharp
`R*delta^2` source-rank tax, while a natural prime modulus upgrade of the
desired fixed power on the half-power-to-top subband would already imply a
zero-free strip by Turán.  Fixed-radius packet clusters are repairable, but
stable simultaneous square repair forces a macroscopic block and scalar KMT
then pays `eta*R`; the
adaptive residual must therefore be attacked directly.  See the
[spectral-null/Delsarte gate](../results/ZETA23-QP-SPECTRAL-NULL-DELSARTE-AND-GROUPING-GATE-2026-08-14.md)
and the
[projected-Gram/source classification](../results/ZETA23-QP-PROJECTED-GRAM-CLUSTER-AND-SOURCE-GATE-2026-08-14.md),
[positive-weight barrier](../results/ZETA23-QP-ACTUAL-PRIME-POSITIVE-WEIGHT-BARRIER-2026-08-14.md),
[multiplicative boundary](../results/ZETA23-QP-ACTUAL-PRIME-MULTIPLICATIVE-EXPLICIT-FORMULA-GATE-2026-08-14.md),
[cluster-square rank-tax audit](../results/ZETA23-QP-KMT-CLUSTER-SQUARE-RANK-TAX-2026-08-14.md), and
[hostile literature audit](../results/ZETA23-QP-ACTUAL-NODE-DELSARTE-GRAM-LITERATURE-HOSTILE-AUDIT-2026-08-14.md).
The [exact strip/QP bridge](../results/ZETA23-QP-STRIP-BRIDGE-AND-SUPPORT-NONIMPLICATION-2026-08-15.md)
proves that a strip of width `delta` supplies positive actual-node Delsarte
certificates at every power `c<delta`.  The reverse is not a support theorem,
even with coherent all-scale selection: a positive-coefficient finite factor
preserves all node sets while inserting high zeros, and a Fejer model
separates moving bands from fixed ordinates.

The reverse radialization target is now normalized correctly.  Its old
probability version is false by an actual-prime singleton; the correct
`N`-mass version converts Turan modulus to a negative shell event.  A new
[cluster-frame theorem](../results/ZETA23-QP-TRANSVERSE-RETURN-CLUSTER-FRAME-GATE-2026-08-15.md)
proves that every calibrated actual-node residual returns with depth
`>>1/M_Y`, after resolving the possible `Y^-2` cross-shell pairs.  Actual
integer-log fourth moments sharpen this to
`>>sqrt(log Y)Y^(-49/66)` at aperture `A=50/33`; the exponent gain over the
dimension floor is `17/66`.  Standard higher even moments cannot improve this
power; a mixed-cubic argument reaches the same frontier, and unsigned local
product energy is provably saturated at exponent `2-A`.  See the
[fourth-moment scale theorem](../results/ZETA23-QP-TRANSVERSE-FOURTH-MOMENT-AND-ACTUAL-UPPER-GATE-2026-08-15.md).
[The mixed-cubic audit](../results/ZETA23-QP-TRANSVERSE-MIXED-CUBIC-INCIDENCE-BARRIER-2026-08-15.md)
isolates signed packet cancellation and calibrated leverage--skew control as
the remaining routes to a further power gain.

There are now two rigorous restricted-sector improvements.  Central packets
`|n-Y|<=Y^(1/2-epsilon)` have the square-root-dimension floor
`s_v,r_+>>M_H^(-1/2)`.  At prime half-centers `Y=q/2`, a one-sided actual
prime-power projection has exponent `755/1056` for every odd prime `q`, and
`361/528` for a density-one set of prime centers.  The
[central-packet theorem](../results/ZETA23-QP-CENTRAL-PACKET-SQRT-DIMENSION-TRANSVERSE-THEOREM-2026-08-15.md)
and [Burgess cubic theorem](../results/ZETA23-QP-PRIME-CENTER-ONE-SIDED-BURGESS-CUBIC-SAVING-2026-08-15.md)
are independently audited.  Neither result lowers the exponent for balanced
two-sided full-shell vectors, so neither proves QP or a strip.

The unresolved balanced tensor is now explicit:
`|8abc-q^3|<<q^3/B`.  Every fixed-power dominant component sector improves
`49/66`, but a balanced upper/lower far-tail vector need not enter one.  An
exact modulo-`q^3` character decomposition loses `sqrt(q)` by Parseval and
therefore cannot improve the existing `sqrt(R)` Schur estimate.  This is a
method barrier, not a counterexample on actual prime powers; see the
[sector gate](../results/ZETA23-QP-SECTOR-COMBINATION-BALANCED-CROSS-GATE-2026-08-15.md)
and [character audit](../results/ZETA23-QP-BALANCED-ALL-PLUS-CHARACTER-METHOD-BARRIER-2026-08-15.md).

On the upper-construction side, the
[actual-log Fejer rigidity theorem](../results/ZETA23-QP-ACTUAL-FEJER-TRANSFER-RIGIDITY-GATE-2026-08-15.md)
limits worst-case perturbative harmonic transfer to `L<<Y^(16/33)` terms.
It is a method ceiling and does not supply an actual fixed-power upper bound.
The
[arithmetic audit](../results/ZETA23-QP-RADIAL-COVARIANCE-NEAR-REFLECTION-AUDIT-2026-08-15.md)
shows those pairs occupy only `Y^(16/33+o(1))` endpoints.  This establishes
fixed-power transverse return but not the much larger strip-scale depth.  A
legal singleton has a VK subpower upper certificate; no matching power upper
or long-event upper is proved.  The exact
remaining theorem is thresholded full-band `LTRAD_full`; it, QP, the reverse
QP-to-strip implication, and the strip remain open.  See also the
[mass-normalization gate](../results/ZETA23-QP-RADIALIZATION-MASS-NORMALIZATION-GATE-2026-08-15.md)
and [hereditary hard-core obstruction](../results/ZETA23-QP-LTRAD-HEREDITARY-BOOSTING-GATE-2026-08-15.md).
The latest unconditional support is still subpower: the
[actual-node tent formula](../results/ZETA23-QP-TENT-EXPLICIT-FORMULA-STRIP-AND-AMPLIFICATION-GATE-2026-08-15.md)
uses the Vinogradov--Korobov region across the full aperture.  A
[coefficient-sensitive cross-Gram estimate](../results/ZETA23-QP-COEFFICIENT-SENSITIVE-CROSS-GRAM-MOMENT-GATE-2026-08-15.md)
leaves one weighted repeated-lag term, while the
[signed-kernel capacity theorem](../results/ZETA23-QP-SIGNED-KERNEL-CAPACITY-GATE-2026-08-15.md)
rules out termwise-absolute Fourier-positive amplification.  None of these
three results is a fixed-power QP or strip theorem.
The growing-support follow-up begins with the endpoint-jet Gabor theorem in
[`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md),
which repairs the qualitative dimension/tail gate and exposes an exact
rank-two Loewner compression.  Its companion
[`ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md)
removes zero separation as a qualitative obstruction.  An effective
asymptotic carrier rate and a prime lower-edge estimate remain, but they are
not independently sufficient at unrelated scales.  For a depth-`alpha` pair,
write the actual normalized carrier margin as
`K=(X^alpha/L)r_T`, `X=exp(L)`, and set
`B_X=osc(A_X)+(2/L)max|D_X|`.  Tail closure requires
`E_remote=o(K)`; the scalar prime route additionally requires the matched
bound `B_X=o(X^alpha r_T)`.  Alternatively, a direct constrained
Pick/Loewner theorem must put the normalized prime negative edge at `o(K)`
for that same actual `K`.  Their exact Schur and scalar-Loewner forms are
isolated in
[`ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md`](../results/ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md)
and
[`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](../results/ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md).
Two later counterconfigurations correct the scope of that carrier target.  A
distinguished pair in the padding collar can be suppressed at the same
exponential scale as the endpoint tail, so a strip argument must recenter it
in the modulation core.  Even there, counts alone permit
`K<<X^(2*alpha/3)`; Anthropic's simple-line density rules out that model but
still permits, at the count-and-density level, a periodic `k=7` model with
`K<<X^(6*alpha/7)`.  The `k=7` model is incompatible with Zeta23's full
Frobenius moment, so it is not a candidate for the actual zeros.  A matching
signed-edge theorem proves that its least eigenvalue really is of order
`X^(6*alpha/7)` after endpoint jets and count-bounded on-line filling.  The
exact ledgers are
[`ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md),
[`ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md`](../results/ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md),
[`ZETA23-FIXED-PERIODIC-MASK-SIGNED-EDGE-THEOREM-2026-08-11.md`](../results/ZETA23-FIXED-PERIODIC-MASK-SIGNED-EDGE-THEOREM-2026-08-11.md),
and
[`ZETA23-K7-GABOR-MOMENT-INCOMPATIBILITY-2026-08-11.md`](../results/ZETA23-K7-GABOR-MOMENT-INCOMPATIBILITY-2026-08-11.md).
The opposite sparse endpoint is positive: if there is only one core off-line
pair and every other local atom is simple and on line, an explicit
binomial-tail endpoint-jet packet proves `K>=X^(alpha-o(1))/L`.  The on-line
Gram operator is only polylogarithmic under the unit count, and the first two
Zeta23 moments are compatible with this unscreened edge.  Thus any remaining
carrier screen must use additional off-line positive mates.  See
[`ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md`](../results/ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md).
A hostile-audited tapered `k=3` island now shows that such mates can in fact
screen at sublinear rank without changing any of those bulk ledgers.  In the
standard mesoscopic-padding regime it has one depth-`alpha` core pair, global
off-line density `o(1)`, and

```text
0<K<=X^(2*alpha/3+o(1)),
```

while preserving the Riemann--von Mangoldt counts and the leading
trace/Frobenius/pair-correlation moments.  This is an artificial zero
configuration, not a zeta-zero construction, but it proves that the current
count, density, and two-moment inputs cannot yield a near-isolated carrier
edge.  See
[`ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md`](../results/ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md).
For the explicit endpoint-flat packet, the completed arithmetic form reduces
the only power-sized term to one centered smooth von Mangoldt polynomial at
the carrier-selected length.  Its required bound is `o(Y^alpha)`, whereas the
best directly applicable unconditional estimate is still
`Y^(1/2-o(1))`.  Exact pointwise prime-translate nulling remains a live
finite-dimensional criterion, but a dimension surplus alone gives no lower
bound for its Laplace leverage.  The exact coefficient, autocorrelation,
pole, gamma, and prime ledger is
[`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`](../results/ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md).
Optimizing two independently polarized lobes turns this nulling problem into
an exact Wiener-`l^1` extremal.  Its finite dual is an `l^infinity` distance
from the Laplace-moment Fourier vector to the prime-log evaluation span.
KMT supplies only a logarithmic upper bound for that optimized leverage;
neither a matching subpower lower bound nor a fixed-power upper bound is
known.  Hermitian complexification is not an additional obstruction:
`z^*Az=x^TAx+y^TAy` descends any negative complex total form to a real test.
See
[`ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`](../results/ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md).
A proportional two-lobe ledger makes the numerical frontier precise, but
none of its advertised edges is presently a zeta theorem.  Raw use of the
global simple-line density suggested `0.597907...`; the sparse `k=3` theorem
refutes its target-retention premise.  An inward exact-density `k=2` island
then refutes the symmetric `3/4+epsilon` premise, while the power-length
varying-depth `k=3` island refutes the formal asymmetric `5/6+epsilon`
premise.  The next exponent ledger, `7/8+epsilon`, also does not follow from
the current bulk inputs: in the normalized one-pair mirror block, adjoining
the completed aggregate arithmetic row can erase the selected carrier
exactly.  Its actual-zeta version remains conditional on a coefficient-
specific target-transverse prime/collateral theorem.  A separate local
`k=2` audit shows that the Frobenius moment rules out a macroscopic
equal-depth cluster, while sublinear clusters can remain bulk-compatible and
exponentially ill-conditioned.  See
[`ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md`](../results/ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md),
[`ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md`](../results/ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md),
[`ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md`](../results/ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md),
and the consolidated
[`UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md`](../results/UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md).
The full audit of less-obvious escapes, including multi-witness ensembles,
determinants, local gluing, operator preconditioning/functional calculus,
collateral rows, critical pole resonance, and Mellin filters, is
[`ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md`](../results/ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md).
Its category-theoretic consolidation packages the audited mechanisms into
four order-sensitive lemmas and isolates the carrier-grade transverse part
of the actual prime/collateral remainder as the remaining datum (a corona
class when the normalized family is uniformly bounded); see
[`ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md`](../results/ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md).
The follow-up search grammar sharpens that consolidation into a practical
stop/go tree.  Its immediate targets are a relative probe-cone/CP-recovery
test on the zero-independent arithmetic operator system, the one-sided
carrier-slice support of the actual remainder, and the minimal quadratic
mixed-correlation theorem.  It also identifies approximate positive
polarization with defect below one as a high-risk route that would already
give a fixed strip, without requiring exact purity.  See
[`ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`](../results/ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md),
[`ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md`](../results/ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md),
and
[`ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md`](../results/ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md),
with hostile audit in
[`CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md`](../results/CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md).
The three finite admissions have now been executed rather than left as a
program.  Finite scalar-probe descent fails on the first asymmetric
two-packet system; parity CP recovery and the obvious covariance only expose
the existing eigenvalue/Schur tests.  Ungraded approximate polarization is
blocked for generators retaining the pole/Tate eigenvalues `0,1`, while a
graded middle zeta generator and divisor identification have not been
constructed.

The formerly preferred target-subtracted carrier support has also now been
executed and exactly pruned.  On the selected positive-row quotient its
operator is `N_T+K_ar,T`, so its scalar dual merely deletes multipliers below
one and adds an aligned carrier baseline.  The faithful remaining object is
the direct constrained completed-arithmetic edge `q_eta(K_ar,T)`.  An actual
prime-power/pole/gamma fixture through `T=512` validates the construction and
completion bookkeeping in floating arithmetic, but proves no uniform sign.
A strip would still require both uniform arithmetic admission `q_eta>=0` and
a target-isolation theorem forcing `q_eta<0` for any actual off-strip zero;
both are open.  The next iteration made this statement more precise.  An
adversarial scan of 73,461 finite carrier slices found no negative; the
closest full-carrier point was rebuilt with Arb and rigorously proved
positive, but this remains only one finite certificate.  An exact
two-dimensional Ritz theorem reduces sub-full admission to one joint
orientation inequality among three completed scalars; separate KMT bounds
discard that orientation and retain the old fixed-power gap.

On the zero side, fixed-width mirror alignment holds after every collateral
positive row is imposed, but its target-only extension is false.  A strictly
deepest target and two slightly shallower pairs at gaps `+/-pi/D` form an
exact normalized phase-flip screen of positive carrier size.  Current bulk
zero inputs allow, but do not produce, that sparse configuration.  Universal
positive averaging over separations cannot remove all such phases without
losing the fixed-power carrier.  Thus the remaining divisor options are an
adaptive finite-list construction with all cross terms retained or genuinely
new zeta-specific local spacing/depth input.  See
[`ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md`](../results/ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md),
[`ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md`](../results/ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md),
and
[`ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md`](../results/ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md).
The combined high-height audit verdict is **PASS AFTER PATCHES** in
[`HIGH-HEIGHT-CARRIER-SLICE-REFEREE-AUDIT-2026-08-12.md`](../results/HIGH-HEIGHT-CARRIER-SLICE-REFEREE-AUDIT-2026-08-12.md).

The adaptive coherent option is now proved for every bounded rescaled
microscopic cluster.  A single fixed-degree endpoint-flat packet defeats the
`+/-pi/D` screen and arbitrary near-confluent multiplicity while retaining
`X^(alpha*d-o(1))` and all mixed cross terms.  Broad unit-width isolation is
still open, but the same-state factor two is no longer the obstruction.
Balanced bipartite coloring of conditions between endpoint legs pays one
total Blaschke product and has an exact real compact realization for every
fixed polynomially-conditioned list.  The remaining step is a growing-list
compact discrete-Pick/phase-cell theorem.  Its ideal compressed density
ledger retains exponent `0.0133834...` at the endpoint, conditionally only.
See
[`ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md`](../results/ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md),
[`ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md`](../results/ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md),
and
[`ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md`](../results/ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md).
Uniform dummy-lattice completion is now sharply excluded: the exact
continuum-signing lattice spends the whole carrier, and finite truncation
loses its apparent saving to missing phase delay.  Tailored discrete Pick
interpolation at occupied clusters remains open; see
[`ZETA23-GLOBAL-PHASE-CELL-COMPRESSION-PICK-LATTICE-GATE-2026-08-12.md`](../results/ZETA23-GLOBAL-PHASE-CELL-COMPRESSION-PICK-LATTICE-GATE-2026-08-12.md).
An exact alternating Pick lattice achieves the half-product exponent
`1/sqrt(cosh(a))`, while a five-point cell can force double-zero local
behavior.  Thus the sharp remaining conjecture is global half-product
control, not one simple root per cell; see
[`ZETA23-HALF-DISK-PICK-EXTREMAL-PROBE-2026-08-12.md`](../results/ZETA23-HALF-DISK-PICK-EXTREMAL-PROBE-2026-08-12.md).
Arbitrarily high fixed local jet obstructions exist, but their losses are not
proved to multiply globally.  The corrected multiplicity ledger is in
[`ZETA23-TAILORED-DISCRETE-PICK-JET-OBSTRUCTION-2026-08-12.md`](../results/ZETA23-TAILORED-DISCRETE-PICK-JET-OBSTRUCTION-2026-08-12.md).
The newest iteration removes one geometric uncertainty exactly.  Center the
critical grid at the hypothetical target and choose the endpoint order even;
then the carrier is odd, the inherited Hahn anchor is even, and
`theta_*=1` at finite dimension.  An independently endpoint-flat odd packet
retains `X^(alpha-o(1))/L`, so no Hahn-tail asymptotic is needed.  The
remaining arithmetic square is a cosine-only completed correlation, but its
sign is open and collateral rows need not preserve parity.

The cosine square has now been collapsed exactly to `P_T,P_T'` at the two
abscissae `1/2+/-alpha+i*gamma`.  Pointwise Herglotz positivity and local
positive height averaging are rigorously false/insufficient, and a symmetric
quartet countermodel proves that the functional equation and critical-line
phase alone cannot sign this special square.  The actual Euler coefficients
remain essential; see
[`ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md`](../results/ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md)
and
[`ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md`](../results/ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md).
Positive harmonic amplification also fails at this level: the extremal
nonnegative trigonometric polynomial retains the target quartet but inherits
a sign-changing sinh-tent prime weight and a larger same-sign pole response.
See
[`ZETA23-HARMONIC-CENTER-SINH-TENT-AMPLIFICATION-NOGO-2026-08-12.md`](../results/ZETA23-HARMONIC-CENTER-SINH-TENT-AMPLIFICATION-NOGO-2026-08-12.md).

On the prime side, positive atomic prime-power nulling now has an exact
compact scalar factorization with no hidden loss beyond its spectral mass.
Without the polynomial upper-frequency cap the moment problem is solvable at
`r>>1/log Y`; exact Riesz-product condition numbers show why the audited
bounded-degree absolute and stable-Gram transfers fall back to fixed-power
scale.  The still-open arithmetic input is quantitative return of the actual
one-dimensional prime-log orbit before `T=Y^(1/d)`.  The hostile-audited
synthesis is
[`ZETA23-BREAKTHROUGH-SPRINT-CENTERED-PARITY-AND-PRIME-MOMENT-SYNTHESIS-2026-08-12.md`](../results/ZETA23-BREAKTHROUGH-SPRINT-CENTERED-PARITY-AND-PRIME-MOMENT-SYNTHESIS-2026-08-12.md).
The direct ordinary Montgomery-mean-value/derivative conversion does not
force that return: its conductor and observation-length costs meet exactly
at every fixed moment order, and its uniform factorial form remains trivial
when the order grows.  The scoped no-go is
[`ZETA23-PRIME-LOG-EARLY-RETURN-MEAN-VALUE-GATE-2026-08-12.md`](../results/ZETA23-PRIME-LOG-EARLY-RETURN-MEAN-VALUE-GATE-2026-08-12.md).
Fixed-complexity bipartite divisor filters and arithmetic nulls can be
realized simultaneously.  At growing scale the exact remaining invariant is
a transverse twisted-prime inradius or aggregate Schur angle; see
[`ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md`](../results/ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md).
These theorems narrow the route but do not improve a known zero-free bound.

The opposite assertion is also open: failure of every fixed strip is the
strictly stronger statement `sup Re(rho)=1`, not merely the negation of RH;
see
[`ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md`](../results/ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md).
The exact scalar target does admit an unconditional logarithmic improvement:
on the transition scale `X=T log(T)^O(1)`, a published sharp prime-twist
estimate gives `B_X << X^(1/2)/(log X)^(3/10)`.  This is still
`X^(1/2-o(1))`, not the fixed power saving required at any depth
`alpha<1/2`; the derivation and its completion-preserving obstruction are in
[`ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md`](../results/ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md).
Restoring the pole continuum before compression does not improve the power:
the completed constrained Pick matrix still has only a
`sqrt(X)/(log X)^(13/10)` normalized lower-edge certificate.  Varying every
grid offset and every transition-scale cutoff recovers an exact complex
triangular shell, but neither the fixed-power saving nor the power-wide
cutoff aperture in Turan's localization criterion.  See
[`ZETA23-COMPLETED-CONSTRAINED-PICK-KMT-OBSTRUCTION-2026-08-11.md`](../results/ZETA23-COMPLETED-CONSTRAINED-PICK-KMT-OBSTRUCTION-2026-08-11.md)
and
[`ZETA23-VARYING-CUTOFF-OFFSET-TURAN-BLINDNESS-2026-08-11.md`](../results/ZETA23-VARYING-CUTOFF-OFFSET-TURAN-BLINDNESS-2026-08-11.md).
Endpoint differencing cannot be multiplied into that logarithmic estimate:
interlacing and an exact coordinate-leverage bound show that a codimension-`m`
jet space removes at most `m` bad spectral directions and preserves most
large confluent diagonals.  See
[`ZETA23-ENDPOINT-JET-PRIME-COMPRESSION-OBSTRUCTION-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-PRIME-COMPRESSION-OBSTRUCTION-2026-08-11.md).
The canonical narrow publication scope, theorem-to-code map, trust ledger, and
release gates are collected in
[`A-7-16-RELEASE-CANDIDATE.md`](A-7-16-RELEASE-CANDIDATE.md).

## Recommended reading routes

### For a mathematician

1. [`MATHEMATICAL-OVERVIEW.md`](MATHEMATICAL-OVERVIEW.md) gives the main
   definitions, result, proof architecture, and missing global bridge.
2. [`ANTHROPIC-ZETA23-INTEGRATION.md`](ANTHROPIC-ZETA23-INTEGRATION.md)
   audits the new two-thirds theorem, its Lean artifact, the smooth
   Guinand--Weil adapter, and the density-versus-strip boundary.
3. [`IMPORTED-ANALYTIC-BASELINE.md`](IMPORTED-ANALYTIC-BASELINE.md) is the
   primary-source theorem baseline for the active analytic program.  Read it
   before treating a zero-free, PNT, Mertens, mean-value, density,
   short-interval, decomposition, or Euler-transfer estimate as a research
   target.
4. [`FIXED-WINDOW-WIDTH-AND-TYPE-II-REDUCTION.md`](FIXED-WINDOW-WIDTH-AND-TYPE-II-REDUCTION.md)
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
   The proportional-order follow-up removes the nonattained-edge loophole for
   its distinct program-level bank (not for the fixed-step single schedule),
   transfers that bank to a retreated evaluated center, and audits the current
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
5. [`LEAN-ANALYTIC-INFRASTRUCTURE.md`](LEAN-ANALYTIC-INFRASTRUCTURE.md) explains
   the reusable analysis as ordinary mathematics rather than as a file list.
6. [`CERTIFICATE-GUIDE.md`](CERTIFICATE-GUIDE.md) explains what the exact
   certificates prove and how they enter the conceptual argument.
7. [`NO-GO-THEOREM-GUIDE.md`](NO-GO-THEOREM-GUIDE.md) organizes the negative
   results by mathematical mechanism.
8. [`../PUBLICATION.md`](../PUBLICATION.md) ranks possible papers and library
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
