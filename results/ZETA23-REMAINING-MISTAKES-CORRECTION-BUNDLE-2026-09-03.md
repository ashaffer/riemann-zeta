# ZETA23 remaining-mistakes correction bundle

Date: 2026-09-03; synchronized through R188 on 2026-09-04.

Status: this pass repairs mathematical scope, normalization, trust labels,
quantifier domains, routing, and reproducibility guards.  It proves no new
fixed-power estimate, uniform zero-free strip, or statement of RH.

This document is the human-readable member of a synchronized three-part
bundle:

1. kernel-checked finite guards in
   [`CorrectionGuards.lean`](../lean/rhbridge/RHBridge/CorrectionGuards.lean)
   and the R181
   [`S1B1CompletedSourceCommutator.lean`](../lean/rhbridge/RHBridge/S1B1CompletedSourceCommutator.lean),
   plus the R182
   [`QPSourceFiberBifurcation.lean`](../lean/rhbridge/RHBridge/QPSourceFiberBifurcation.lean),
   plus the R183
   [`ExteriorFactorizationAudit.lean`](../lean/rhbridge/RHBridge/ExteriorFactorizationAudit.lean),
   plus the R184
   [`CompletedSourceConstructiveSearch.lean`](../lean/rhbridge/RHBridge/CompletedSourceConstructiveSearch.lean)
   and
   [`CompactSourceDerivativeBridge.lean`](../lean/rhbridge/RHBridge/CompactSourceDerivativeBridge.lean),
   plus the R185
   [`FourCauchyGlobalCompatibility.lean`](../lean/rhbridge/RHBridge/FourCauchyGlobalCompatibility.lean),
   plus the R186
   [`SplitCarlemanFormDomainCloseout.lean`](../lean/rhbridge/RHBridge/SplitCarlemanFormDomainCloseout.lean),
   and the R187
   [`R71MinorArcTriage.lean`](../lean/rhbridge/RHBridge/R71MinorArcTriage.lean),
   plus the R188
   [`R188PrincipalBandSerialization.lean`](../lean/rhbridge/RHBridge/R188PrincipalBandSerialization.lean),
   together with their
   [`correction audit`](../lean/rhbridge/RHBridge/CorrectionGuardsAudit.lean),
   [`commutator audit`](../lean/rhbridge/RHBridge/S1B1CompletedSourceCommutatorAudit.lean),
   [`source-fiber audit`](../lean/rhbridge/RHBridge/QPSourceFiberBifurcationAudit.lean),
   and
   [`exterior-factorization audit`](../lean/rhbridge/RHBridge/ExteriorFactorizationAuditAxioms.lean),
   together with the
   [`constructive-source audit`](../lean/rhbridge/RHBridge/CompletedSourceConstructiveSearchAudit.lean)
   and
   [`compact-derivative audit`](../lean/rhbridge/RHBridge/CompactSourceDerivativeBridgeAudit.lean)
   and
   [`four-Cauchy compatibility audit`](../lean/rhbridge/RHBridge/FourCauchyGlobalCompatibilityAudit.lean),
   [`split-Carleman audit`](../lean/rhbridge/RHBridge/SplitCarlemanFormDomainCloseoutAudit.lean),
   [`R71 localization audit`](../lean/rhbridge/RHBridge/R71MinorArcTriageAudit.lean),
   and
   [`R188 principal-band audit`](../lean/rhbridge/RHBridge/R188PrincipalBandSerializationAudit.lean);
2. this report; and
3. the canonical compact reload ledger
   [`zeta23_correction_bundle_v1.zctx`](context/zeta23_correction_bundle_v1.zctx).

The JSON file is now a deterministic audit/interchange projection of the
ledger.  The generated `Z23V/1` index is its uncompressed random-access
runtime projection; neither generated file is a fourth independent authority.

The verifier
[`verify_zeta23_correction_bundle.py`](verify_zeta23_correction_bundle.py)
checks their shared correction IDs, theorem names, domains, and global
nonclaims.

## Rapid resumption representation

`Z23C/1` is a typed, tab-delimited semantic ledger with a versioned header,
path symbols, explicit correction/modifier opcodes, and a terminal semantic
SHA-256.  It retains every status, trust label, equation ledger, theorem name,
source, debt, and nonclaim in this bundle.  At the current size it is `24851`
bytes, versus `31952` bytes for the generated pretty JSON projection.

Whole-stream compression is not used for runtime resumption.  Instead,
[`zeta23_correction_bundle_v1.z23v`](context/zeta23_correction_bundle_v1.z23v)
is an uncompressed seekable store of typed integer vectors.  Its fixed
directory addresses C01--C20 and the shared state records separately; vector
payloads reference individually indexed exact UTF-8 strings.  A selected read
checks the header, selected record digest, and selected string CRCs without
decoding unrelated records.  Full verification separately regenerates the
index and checks every byte.

The named `resume` vector is deliberately lossy.  It preserves the useful
working state—grand and immediate objectives, active frontier, route
invariant, current hypotheses, learned prohibitions, open debts, next targets,
and decision policy—but is not a serialization of hidden chain-of-thought or
latent activations and is not proof evidence.  Exact claims remain available
by correction ID.  For example:

```text
python3 src/zeta23_correction_context.py resume
python3 src/zeta23_correction_context.py query C02 C05
python3 src/zeta23_correction_context.py query --vector math
python3 src/zeta23_correction_context.py verify
```

In the current artifact, a guarded C02 query reads `1753/31440` index bytes;
the broader working-state `resume` vector reads `9578/31440`.  These figures
measure file access, not proof progress or model-token counts.

## Corrected mathematical state

### C01 — Signed coefficients are not an actual sign theorem

R120's Mellin/coprimality formula has signed coefficients.  That fact alone
does not prove that the actual constrained primitive form is negative,
indefinite, or non-order-reflecting.  R124 proves a positive narrow band and
has D-rated floating evidence of full-shell sign changes; the latter remains
uncertified.  R120, R121, R122, R124, R128, the registry, and the proxy ledger
now preserve this distinction.

Lean proves the underlying logical guard by an explicit signed-coefficient,
positive-aggregate counterexample:
`signed_coefficients_positive_aggregate`, and derives
`signed_coefficients_do_not_force_nonpositive`.  It does not formalize or
claim the sign of the analytic R124 kernel.

### C02 — R125 raw and critical-relative normalizations differ

For

```text
Delta_P=P(C_(P-1)-C_P)=P^(1/2)tau_(-log P),
```

the raw off-line amplitude at scale `X` is

```text
X^(beta-1/2)P^(1-beta).
```

The corresponding critical-line response is `P^(1/2)`.  Only after dividing
by it does one obtain

```text
X^(beta-1/2)P^(1-beta)/P^(1/2)=(X/P)^(beta-1/2).
```

Thus R125's scale-replication conclusion survives, while its former phrase
“critical normalization” was ambiguous.  Lean checks both the additive
exponent identity and the positive-real-power identity in
`raw_sub_critical_exponent_identity` and
`raw_div_critical_eq_reduced_scale`.

### C03 — Three tested routes are not an exhaustive trilemma

The correction closure disposes of exactly three constructions: local
restriction, faithful all-class restoration, and adjacent-filter
faithfulness.  It does not classify arbitrary compositions, subfamilies, or
linear combinations.  Lean's four-constructor ambient model proves
`tested_routes_not_exhaustive`; the fourth constructor asserts only the
logical possibility of an unclassified case, not a working analytic route.

### C04 — The licensed exponent domain is explicit

For the complete quadratic energy, the correspondence is

```text
eta=kappa/2,       0<kappa<=1,       0<eta<=1/2.
```

Every active and supporting occurrence found in this pass now carries the
licensed domain.  The reverse-calibration preflight also uses its declared
strip variable `delta`, rather than an undefined `eta`.  Lean checks both
domain maps in `kappa_half_in_strip_domain` and
`twice_eta_in_energy_domain`.

### C05 — R116's half saving was already at energy level

The R116 balanced-semiprime proper-conductor bound is a contribution to the
bilinear/quadratic energy expression, not an amplitude awaiting another
square.  Its exponent-one-half contribution has saving `1/2` against an
energy baseline exponent `1`, not saving `1`.  Conditional on that external
analytic classification, Lean records only the numeric/algebraic ledger guard
in `already_quadratic_half_saving` and `already_quadratic_not_full_saving`; it
does not type the R116 analytic object.

### C06 — R116 remains packet-scoped

R116 proves its proper-conductor estimate only for the balanced squarefree
semiprime packet.  It is not a global primitive-only reduction.  R128 restores
all conductor, gcd, profile, orientation, and head classes exactly, but the
result is the original positive R71 energy.  This is a faithful coordinate
restoration, not a smaller theorem.

### C07 — The three growing detector families remain distinct

The fixed-total-width single schedule, the fixed-step sublinear schedule, and
R80's proportional-order dyadic bank have different quantifiers.  R80 proves
a moving-edge converse for the third family only.  It does not prove the
missing converse for either single schedule.  The registry, proxy ledger,
publication guide, and imported baseline now say this explicitly.

### C08 — S1-A0 and the finite S1-B1 commutator both fail admission

The naked two-scale re-expansion collapses to `C*1=Lambda` and fails admission
as a strict adapter.  The subsequently tested S1-B1 arithmetic commutator
obeys

```text
W Lambda = [W,T_C]1 + T_C w.
```

On a narrow shell its compressed residual vanishes and the commutator is
exactly the original windowed `Lambda` source; globally the residual is an
uncontrolled divisor-boundary tail.  Its completion-sensitive repair obeys

```text
[P_-,M_H]U = (H-H^R) R(U)/2,
```

so it is an off-critical-faithful reflected coordinate, not a smaller norm.
Two reflection commutators collapse to scalar multiplication, and every
finite word in multipliers and one reflection has normal form `M_a+M_b R`.
Thus neither the literal arithmetic window commutator nor the tested finite
multiplier/reflection crossed product supplies a strict adapter.

This does not classify nested arithmetic commutators or source laws using
operators outside that finite algebra, nor every possible nontrivial complete
two-scale structural inequality.  The
full audit is recorded in
[`ZETA23-S1-B1-COMPLETED-SOURCE-COMMUTATOR-AUDIT-2026-09-03.md`](ZETA23-S1-B1-COMPLETED-SOURCE-COMMUTATOR-AUDIT-2026-09-03.md).
Lean checks the finite normal forms in
`windowKernelCommutator_eq`, `source_reconstruction`,
`commutator_eq_source_of_residual_zero`,
`reflectionMultiplierCommutator_eq`,
`two_reflection_commutators_collapse`, and
`crossedOp_comp_normal_form`.  It does not formalize the analytic completion
or off-critical nonvanishing argument.

## Corrected operational state

### C09 — The route CLI validates a dated snapshot

`zeta23_proof_tree.py resume` and `verify` load the route, S0 adapter, and
correction-closure caches together.  They reject schema/date/global-status,
S0, primitive-sign trust, R128, R125, exponent-domain, S1, family-separation,
authority-path, or source-path drift.  That internally verified snapshot is
dated 2026-09-02, however, and its serialized next action predates the R181
S1-B1 audit.  The canonical correction ledger and the R181/R182 reports
supersede only that next action; `zeta23_correction_context.py resume` is the current
rapid-resumption command.  Mutation tests continue to exercise the older
snapshot's fail-closed cases.

### C10 — August cache CLIs identify themselves as historical

The deprecated v1 context and v2 theorem-graph CLIs print a stderr warning
that their “live” gates are August snapshots and point to the September
resume command.  Their README language and the root historical chronology no
longer call those routes current.

### C11 — The n=4 Arb checkpoint fingerprint is complete for new artifacts

New n=4 checkpoints use metadata version 3.  Its canonical fingerprint binds
the integrand function bodies, all load-bearing exact and Arb globals, the
odd-double-factorial table, and python-flint/FLINT versions.  The existing
version-2 artifact is accepted only at its pinned path when its full file
SHA-256 and the complete current fingerprint match the documented generation
state.  This makes later code/global/dependency drift fail closed.  A fresh
v3 regeneration and independent cross-check are still required before that
endpoint is released.

### C12 — The V4 fixed-point hashes are explicitly unattached

The recursive fixed-point postflight's V4 digests do not resolve to preserved
frozen bytes or a binding archive/commit in this worktree.  They are now
labeled historical unattached evidence, not a current-file integrity
certificate.  A verifier enforces that nonclaim.

### C13 — Historical handoff and route language is scoped by date

Old `FQPP`, “current exact state,” and related handoff language is now written
in the past tense or explicitly labeled as a dated snapshot.  A bare resume
uses the September authority bundle.

### C14 — The six September-2 snapshot bytes have a local manifest

The dated route, adapter, and closure caches and their three human reports have
role-labeled SHA-256 entries in
[`zeta23_current_authority_manifest_v1.json`](context/zeta23_current_authority_manifest_v1.json).
Its verifier detects local byte drift.  The manifest explicitly has no
commit/archive binding, so it does not solve the untracked-worktree durability
debt or claim that a clean clone contains these files.

### C15 — The QP/Turán soft source-fiber class is obstructed

The bifurcation first corrected a scope error: direct
`LTRAD_P(.0189,.001)` is a lower bound on the `-q` radial inradius, whereas
the event-dependent `v=a(t0)+Dq` source-fiber bound is only a sufficient
transverse mechanism for it.  Failure on the `-v` ray alone is not failure on
the `-q` ray.

The smooth filled real-node antenna already constructed in §5.2 of the PWCT
audit has full-band dip `Y^(-1/2+o(1))`.  Applying its probability `alpha` in
the two distinct normalizations gives

```text
z=-alpha,                         z.q=-1,
h(z)<=Y^(-1/2+o(1)),

y=-alpha/[D+Phi_alpha(t0)],       y.v=-1,
h(y)<=Y^(-.499+o(1)).
```

The first line directly bounds the synthetic radial inradius, while the
second defeats the sufficient `.0179` source-fiber theorem.  The same filled
model retains a legal contiguous source, the complete height band,
prime-scale density and maximum gaps, diffuseness, unpaired support, and
generic nonresonance.  It omits the literal deterministic ordinary-prime log
mask, so it is not an actual-prime counterexample.

No independently stated quantitative prime invariant emerged at the
`.0179/.0189/.019` ledger.  Accordingly, the target's mask-coarser soft proof
class is closed and QP/Turán is parked; actual-prime `LTRAD_P` and `DPA_P`
remain open.  The complete audit is
[`ZETA23-QP-SOURCE-FIBER-BIFURCATION-2026-09-03.md`](ZETA23-QP-SOURCE-FIBER-BIFURCATION-2026-09-03.md).

This conclusion is classified as **LOCAL_PREDECESSOR + PROJECT_SYNTHESIS**:
the diffuse model and `.499` exponent predate this pass, while the direct
radial application, separation of the two dual problems, finite Lean algebra,
and routing consequence are the present synthesis.  Lean checks
`legalSource_annihilates_direction`, `radialDual_response_le`,
`normalizedSeparator_pairs_sourceDirection`,
`normalizedSeparator_response_le`, `radialPoint_le_of_dual`, and the exact
exponent ledger.  It proves no real-node concentration theorem or
actual-prime asymptotic statement.

### C16 — Exterior factorization collapses to KNC at contact

The post-synthesis factorization first required a typing correction.  In the
fixed outer form Hilbert space, the desired old-to-collar charge is

```text
Gamma_(a,b)=P_(W_(a,b))^h G|_(V_a): V_a -> W_(a,b),
```

the adjoint of the block called `C` in the earlier screw-collar convention.
The identity `Gamma=T A_a` is now typed in that orientation.

For a bounded nonnegative old operator `A` and bounded charge `Gamma`, any
factorization `Gamma=T A` kills `ker(A)`.  Conversely, kernel annihilation
makes `T_0(Ax)=Gamma x` well defined on `ran(A)`.  A bounded factor exists
exactly when

```text
||Gamma x|| <= M ||A x||,
Gamma* Gamma <= M^2 A^2,
ran(Gamma*) subset ran(A).
```

At the actual localized form contact, `A=I+compact` has closed range, so
kernel annihilation already implies a bounded factor.  Bare existential
factorization is therefore exactly KNC, and universal KNC is RH-equivalent
under the accepted continuation interfaces.  A pseudoinverse supplies no
independent mechanism.

The dense-core wording also needed a guard.  A bounded or closable factor
identity on a dense core forces KNC.  An exact graph-core countermodel shows
that a nonclosable factor can satisfy the identity on a dense subspace while
the true kernel vector remains charged.  Similarly, the positive scalar
block `[[r^2,r],[r,1]]` has only square-root alignment and forces linear
factor coefficient `1/r`; positivity and finite invertibility do not give a
uniform contact factor.  The shifted-resolvent factor has the same reciprocal
pole on a charged zero mode.

Backward calibration sharpens the routing conclusion.  A fixed strip of
width `eta` gives the complete R71 exponent `1-2eta` and eventual positivity
of `Psi_(1/2-eta)`, but unshifted universal exterior factorization remains an
RH-strength statement.  Deriving it from the strip would be a new
strip-to-RH amplifier, not an intermediate strip lemma.

The full analytic audit is
[`ZETA23-EXTERIOR-FACTORIZATION-AND-BACKWARD-STRIP-AUDIT-2026-09-03.md`](ZETA23-EXTERIOR-FACTORIZATION-AND-BACKWARD-STRIP-AUDIT-2026-09-03.md).
Lean checks only the finite algebra in
`factorization_implies_kernel_annihilation`, `scalar_factor_eq_inv`,
`scalar_factor_abs_eq_inv`, `squareRootBlock_eq_sq`,
`squareRootBlock_nonnegative`, `squareRoot_cross_factor_eq_inv`,
`squareRoot_psd_defeats_fixed_linear_bound`,
`shiftedResolventFactor_identity`, `shiftedResolventFactor_abs`, and
`shiftedResolventFactor_unbounded`.  It does
not formalize Douglas's theorem, Suzuki's results, the completed source, a
strip, or RH.

### C17 — Constructive source words expose their remainder

The direct source lane was reopened with a concrete operation grammar.  Its
canonical finite word is

```text
T_m=Gamma sum_(j=0)^(m-1)(-K)^j,
Gamma=T_m(I+K)+Gamma(-K)^m.
```

On a contact mode `(I+K)n=0`, every remainder is exactly `Gamma n`.  More
generally, every scalar function of `K` regular at `-1` leaves residual one;
only the forbidden pole `1/(1+K)` removes it.  A regular
translation-invariant xi-annihilator parametrix has the same defect: its
residual multiplier is one at each xi zero.  The rational three-coordinate
model confirms that an annihilator plus the old equation need not kill the
exterior charge.

The finite-state obstruction is also exact at its proper scope.  Suzuki's
near-edge source has leading kernel `1/[2(r+s)]`; Cauchy determinants of every
finite order are nonzero.  Hence a finite-rank scalar sampler, endpoint-jet,
or unforced boundary state cannot represent the collar source.  This does
not exclude continuum integral operators, distributed memory, or
boundary-localized source-piece identities.

The surviving continuum grammar is explicit.  With `X=e^(x/2)`, `Y=e^(y/2)`,
the Lerch part of `g''(x-y)` for `x>y` is

```text
(Y/4) sum_(zeta^4=1) 1/(X-zeta Y),
```

while the other completion terms have rank two or are local and every prime
ramp is a dilation atom `X=sqrt(m)Y`.  The local triangular Cauchy jump has
determinant one.  But the full old equation is a nonlocal operator-valued
Riemann--Hilbert system: on the genuine state range, independence of the
exterior readout from a chosen homogeneous solution is exactly
`Gamma ker(A)=0`.  Thus the four-Cauchy form is a useful completed-source
normal form, not yet a factor `T^src`.

The strip comparison produced the compact source derivative

```text
S_h(t)=sum Lambda(n)/n h'(t-log n)
      =e^(-t/2)(d/dt-1/2)D_W(t).
```

For sufficient fixed spline smoothing and one globally fixed sign, the
eventual bound `epsilon S_h(t)>=-C e^(-theta t)` implies the width-`theta`
right zero-free strip by Landau; the strip gives the matching absolute bound.
This is an endpoint coordinate, not a smaller lemma.  In the standard causal
distribution convention the pole-killed ramp identity contains the exact initial collar `-V_delta`;
omitting it globally was a false formula.

The complete audit is
[`ZETA23-CONSTRUCTIVE-COMPLETED-SOURCE-AND-COMPACT-DERIVATIVE-AUDIT-2026-09-03.md`](ZETA23-CONSTRUCTIVE-COMPLETED-SOURCE-AND-COMPACT-DERIVATIVE-AUDIT-2026-09-03.md).
Its classification is **IMPORTED + LOCAL_PREDECESSOR + PROJECT_SYNTHESIS**,
not candidate-new mathematics.  Lean checks only the finite geometric,
Cauchy-pairing, countermodel, derivative, multiplier, and collar algebra.  It
does not formalize the analytic Suzuki kernel, the Hankel theorem, Landau, a
strip, or RH.

### C18 — Exact state closeout still does not imply global compatibility

R185 performs the exterior-source part of the calculation left open by R184.
On arbitrary smooth localized data, the fourth-root Cauchy filter cancels
exactly one pole mode on each exterior side.  The right readout is

```text
exp(x/2) M_-1
- sum_(j>=1) exp(-(4j+1)x/2) M_(4j+1)
- sum_m Lambda(m)/sqrt(m) n(x-log m),
```

and the reflected left readout retains `exp(-x/2)M_1`, the negative-index
moment tail, and `n(x+log m)`.  Thus completion gives a genuine one-mode
cancellation, not exterior annihilation.

The signs use Suzuki's convention `g=-Psi` and `W=-g''=Psi''`.  The central
structural correction is exact: fourth-root rotations and positive dilations
commute globally and preserve the four rays.
Multiplicative reflection has the semidirect law `J S_r=S_(1/r)J`, so it
swaps the directed channels; the bilateral prime pair `S_r+S_(1/r)` is
reflection invariant.  Fixed-window/cut/trace compression adds the boundary
leakage.  With `K_r=P S_r P` and `Omega_r=Q S_r P`, its cocycle is

```text
Omega_(rs)=Omega_r K_s+Q S_r Omega_s.
```

Opposite shifts have a two-boundary re-entry defect.  A closed cocycle
identity balances boundary leakage; it does not force any individual leakage
or collar charge to vanish.  In particular, `Omega_r` is only a projected
dilation channel, whereas KNC concerns the total pole--Lerch--prime readout.

Möbius transmutation does not repair the defect.  The exact arithmetic law is
`mu*Lambda=-mu log`, so filtering returns the R71 coefficient source.  If a
formal inverse is compressed through the old projection, the resulting
exterior term is the negative omitted tail.  Global use on the completed
archimedean source also requires reciprocal-zeta closure that is unavailable
at critical zeros.

The three-lag Toeplitz contact identifies what successful propagation would
need.  The even singular branch requires the new next-lag law
`d=2ac-a=T_3(a)`; the odd branch requires `d=a`.  An exact symbolic charged
contact shows that positive-semidefinite Toeplitz old-contact algebra does not
alone force exterior null charge, but its completion weights are synthetic.
It does not instantiate the full source grammar, is not the actual von
Mangoldt/Suzuki operator, and does not refute KNC or RH.

The previous claim that the global calculation was complete was wrong.  The
exterior derivation never uses `mathcal B_a f=0`.  Moreover, the old Lerch
operator is a split Hadamard-finite-part/Carleman operator: its `zeta=1`
channel has a positive two-sided `1/abs(Y-X)` singularity, not the oriented
principal value of one full Cauchy transform.  Four ordinary Plemelj traces
therefore do not serialize the old equation.  Visible nonzero terms for
arbitrary `f` cannot exclude a zeta-coefficient-specific identity on its
kernel.

Reflection supplies an omitted affine compatibility

```text
C_(f^vee)(z)=A_f-C_f(1/z),
E_L[f](X)=E_R[f^vee](1/X).
```

The affine constant cancels only after the fourth-root weighted sum.  For
smooth compactly supported exact homogeneous states, every endpoint jet of
both exterior formulas also vanishes, coupling the surviving pole, higher
moments, and prime-power jets.  These constraints halve under parity but do
not force collar vanishing; smooth flatness need not propagate.

The R186 closeout resolves that framing.  The split finite part has an exact
counterterm-free difference-kernel serialization and a minimal state
`H_+ + H_- + pi(C(iX)-C(-iX))`.  Suzuki's form core then gives a canonical
weak old equation for every genuine contact, while the adjacent Carleman
bound, bounded root channels, finite-rank poles, and finitely many restricted
prime translations give an `L2` readout on every finite collar.  Equivalently,
the continuous integrated potential
`H_n(x)=i integral g'(x-y)n(y)dy` is constant on the old interval.

What fails is the stronger pointwise trace formulation.  Fixed-height
shrinking bumps have logarithmic form norm squared
`O(epsilon log(1/epsilon)) -> 0`, so generic form-domain point values and
endpoint jets are not continuous and cannot be passed by density.  The
smooth-core jet tower remains only a conditional diagnostic pending a new
regularity theorem for homogeneous solutions.

Both preregistered falsifiers have also been executed.  The arcsine transform
has zero interior Plemelj average but a nonzero exterior value.  More
decisively, an exact rational reciprocal three-node split-Cauchy/dilation
model has a PSD old matrix, nullvector `(1,0,-1)`, and exterior charge
`201161/8190`.  Its completion weights are synthetic, so this is not an
actual-zeta counterexample; it refutes only coefficient-free propagation.

The two technical tasks are closed, but serialization is only bookkeeping:
global compatibility remains exactly the assertion that the total R186
exterior map annihilates `ker A_a`, namely KNC.  Any direct proof must now be a
completed-zeta-coefficient-specific unique-continuation or spectral-synthesis
theorem.  The immediate strip target remains complete source-preserving R71.

The corrected exterior calculation and compatibility audit is
[`ZETA23-FOUR-CAUCHY-GLOBAL-COMPATIBILITY-CALCULATION-2026-09-03.md`](ZETA23-FOUR-CAUCHY-GLOBAL-COMPATIBILITY-CALCULATION-2026-09-03.md).
Its final closeout is
[`ZETA23-SPLIT-CARLEMAN-FORM-DOMAIN-CLOSEOUT-2026-09-03.md`](ZETA23-SPLIT-CARLEMAN-FORM-DOMAIN-CLOSEOUT-2026-09-03.md).
The classification is **IMPORTED CLASSICAL ANALYSIS + PROJECT SYNTHESIS**, not
candidate-new analytic mathematics.  Lean checks finite scalar-pullback,
root-partial-fraction, counterterm, weak-kernel, Toeplitz, and rational
algebra; Python replays the Gaussian-rational roots and exact hostile contact.
Neither machine layer formalizes Suzuki's analytic form closure, Carleman's
inequality, global compatibility, KNC, `T^src`, a strip, the four-cycle bound,
or RH.

### C19 — “Minor arc” was three different coordinates

The post-R186 instruction to attack a completion-preserving R71 minor arc
needed a coordinate passport.  In Mellin two-frequency coordinates, the
sector `|u-t|>K R^s` is now proved negligible for any fixed `s>1` after the
*whole* completed field is localized and the block weight is chosen Gevrey.
Young and Plancherel give the exact bound

```text
|E_far| <= (2 pi)^(-1)
  ||1_(|v|>K R^s) psihat(v)||_1 ||chi G||_2^2.          (C19.1)
```

This hard difference split is Hermitian but not positive.  A completed
`X=127,Y=8` fixture
has total `0.1277499014525`, near part `0.1575199385126`, and far part
`-0.02977003706009`.  The sign is stable under the recorded quadrature
refinement and includes tail--tail, tail--center, and center--center terms.

There is a sharper additive localization.  The affine Type-I center has an
exact two-moment representation as the continuous part of the same signed
measure as `a_(U,V)=mu_(>U)*Lambda_(>V)*1`.  For the frozen order-four window,
the complementary smooth multiplier `1-m(X^(99/100)xi)` has field exponent
`.46`, energy exponent `.92`, and completed cross-term exponent `.96`.
Therefore

```text
E_R71 = E_completed_principal_band + O(X^(.96+o(1))).   (C19.2)
```

The target exponent for `eta=1/100` is `.98`, so (C19.2) is an exact
exponent-level equivalence, not a strip proof.  Primitive balanced reciprocal
kernel response was already controlled in R87.  The genuinely open arithmetic
object is the signed accumulation of the high-determinant packets together
with the reducible/low-character projector, exact center, and all cofactor
cross terms.  Pointwise packet saving cannot be promoted through the
conditional rectangular sum.

The local novelty firewall also corrects the attribution.  The earlier
`COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md` had already constructed the
full-von-Mangoldt prime-minus-continuum measure, kept its center at every
additive frequency, and identified the principal zero carrier and the
zero/reducible Wright-completion gap.  The earlier Mertens principal-band
gate had already shown that generic minor-frequency saving leaves the hard
principal mode.  R187 sharpens those predecessors only by giving the frozen
Vaughan affine-center formula, explicit `.46/.92/.96` exponent ledger,
Gevrey difference localization, and signed finite falsifier.

The closest primary import with a signed projector is Drappeau's dispersion
theorem, but at `Q~x^(1/2)` its range stops near `N<=x^(1/3)` and its removed
low-conductor projector contains rather than cancels the obstruction.
Wright's 2026 subdyadic theorem gives a fixed-power improvement for its
nonzero reciprocal-phase form and treats its native determinant-zero part
separately, but does not supply the R71 zero-phase/reducible/center completion
or preserve those cross terms.  No audited primary theorem passes the full
source/center/sector/window/fixed-power passport.

The next experiment recorded here was therefore a signed principal-band
serialization retaining the nonzero packets, reducible/low-character
projector, and exact affine center before absolute values.  R188, recorded as
C20 below, completed that serialization and suppressed the low cofactors, but
also showed that the surviving high-cofactor field cannot be split into two
independently estimated first-open edges.  The required cancellation is one
joint completed correlation theorem.

The full audit is
[`ZETA23-R71-COMPLETION-PRESERVING-MINOR-ARC-TRIAGE-2026-09-03.md`](ZETA23-R71-COMPLETION-PRESERVING-MINOR-ARC-TRIAGE-2026-09-03.md).
The localization is **LOCAL PREDECESSOR + IMPORTED CLASSICAL
FOURIER/GEVREY ANALYSIS + SHARPENED PROJECT SYNTHESIS**, not candidate-new
mathematics.  Lean checks the exponent,
two-moment, signed-recombination, and aggregation guards.  Python replays the
finite completed Fourier split.  Neither layer proves the open principal-band
estimate, a strip, the four-cycle bound, or RH.

### C20 — Exact serialization closes bookkeeping, not the exponent `.98`

The C19 principal-band serialization experiment has now been executed.  Put

```text
gamma=(mu 1_(>U))*(Lambda 1_(>V)),   a=gamma*1,
Phi_r=chi_X T_delta f_r,              T=ceil(CX)+1.
```

For the affine Type-I center `A_R+B_R log t`, define

```text
C_T=sum_(q<=T) gamma(q)/q,
ell_T(t)=C_T-A_R-B_R log t,
D_q[Phi]=q^(-1) sum_(b!=0) Phihat(b/q).
```

Finite support and Poisson summation then give the exact completion-preserving
identity

```text
G_R^pri(r)=sum_(q<=T) gamma(q) D_q[Phi_r]
           + integral ell_T(t) Phi_r(t) dt.             (C20.1)
```

Squaring (C20.1) retains the alias--alias, both alias--center, and
center--center terms.  In particular, the entire affine residual `ell_T`
remains; it is not a low-cofactor error and cannot be discarded after
localization.  The elementary coefficient ledgers are

```text
|gamma(q)| <= log q,
sum_(q<=T) |gamma(q)|/q  << log^2 X,
sum_(q<=T) |gamma(q)|^2/q << log^3 X.                   (C20.2)
```

Smooth physical compactification does prove low-cofactor suppression: for
each fixed `D`, the nonzero-alias line with `q<=X^(.99)/4` is `O_D(X^(-D))`.
This suppresses only that `gamma(q)D_q` line.  The affine residual in (C20.1)
survives.  Effective aliases therefore have

```text
q >= X^(.99+o(1)),   |b| <= q X^(-.99+o(1)),
physical quotient <= X^(.01+o(1)).                    (C20.3)
```

Using the order-four window's full fifth-order Fourier decay gives the
target-matched collar

```text
Q=floor(X^(499/500)),       A=floor(X^(1/400)),
G_collar=integral ell_T Phi_r
 +sum_(Q<q<=T) gamma(q)/q sum_(0<|a|<=A) Phihat_r(a/q).
```

The exact residual `ell_T` remains inside `G_collar`, while

```text
||G_R^pri-G_collar||_infinity
 << X^(49/100) log^2 X = X^(49/100+o(1)).             (C20.3a)
```

Weighted `L2` Minkowski in both directions therefore makes the collar
equivalent to the `X^(49/50+o(1))` energy target.  This is not a power saving:
the discarded field sits exactly at the target's square-root exponent.  On
the retained physical support `q*v_phys<=CX`, the geometry sharpens to

```text
q>X^(499/500),   0<|a|<=X^(1/400),
v_phys<=C X^(1/500)=X^(1/500+o(1)).                   (C20.3b)
```

Here `v_phys=n/q` is the physical free quotient.  It is not the Section-5
solution-line Poisson dual, and this statement does not remove the surviving
`J~X` top box.

The crucial correction is that high cofactor is not low determinant.  The
same core contains determinant one, determinant comparable with `X`, and the
reducible pair `(1,2)`: unit modes at `(X,X+1)`, `(X,2X-1)`, and `(X,2X)` are
explicit witnesses.  The common-`g` primitive line mask has Fourier-algebra
cost at most `3^omega(g)=g^o(1)`, but that norm estimate does not prove that
its fractional shifts and conductors fit a scalar Wright theorem.

There is also a hostile actual-coefficient witness.  For distinct primes
`p,r` in fixed square-root intervals, `gamma(pr)=-log(pr)`.  The PNT supplies
about `X/log^2 X` such balanced semiprimes, and the numerator-one alias can be
phase-aligned on a fixed output subinterval.  This isolated unit-alias
subfield has energy

```text
X/log^2 X = X^(1-o(1)).                                (C20.4)
```

Thus a componentwise `X^(.98+o(1))` bound is false.  Equation (C20.4) is not a
lower bound for the full completed field: the other aliases, reducible sector,
and affine or prelocalized-`Q_h` completion may cancel it.

The finite Vaughan coordinate is also pole-faithful.  For `Re(s)>1`, if
`M_U` and `L_V` are the finite Mobius and von-Mangoldt truncations, then

```text
A_(U,V)(s)
 = zeta(s)(1/zeta(s)-M_U(s))(-zeta'(s)/zeta(s)-L_V(s))
 = (1-zeta(s)M_U(s))(-zeta'(s)/zeta(s)-L_V(s)).        (C20.5)
```

At every nontrivial zero, the first factor equals one, so the logarithmic
derivative retains its simple pole, with residue recording the zero's
multiplicity.  Applying `Q_h`
before localization kills the affine center exactly; physical compactification
after low-pass reintroduces only arbitrary-power-small scalar/axis leakage.
It does not delete the hard box.

The decisive surviving box is

```text
g=1,  M=N=X,  J=Theta=X,  |j theta|=X^2=MN,  Z=1.
```

R105's applicable Wright-I/Bettin--Chandee ledger gives
`X^(15/8+o(1))`, worse than the direct `X^(1+o(1))` energy scale.  The
tempting Wright-II attribution was wrong: Wright II requires both denominator
supports to have relative length `X^(-sigma)`.  Partitioning both variables
and summing scalar boxes by triangle does not save this top box.  The favorable
`1/40-1/200=1/50` subledger is therefore not a global saving.

The surviving open assertion is a single globally signed, actual-coefficient
correlation bound on this target-matched collar, retaining every determinant,
conductor, alias, projector term, affine or prelocalized-`Q_h` completion
term, and cross term, and saving `X^(-1/50)` in energy.  With that conclusion
imposed on the complete family, it is the R71 endpoint and remains
uniform-strip-equivalent.  It is not a smaller theorem obtained merely by
serialization.

The full audit is
[`ZETA23-R71-PRINCIPAL-BAND-EXACT-SERIALIZATION-2026-09-04.md`](ZETA23-R71-PRINCIPAL-BAND-EXACT-SERIALIZATION-2026-09-04.md).
The result is **LOCAL PREDECESSOR + IMPORTED CLASSICAL POISSON/PNT AND CHECKED
CURRENT RECIPROCAL-SUM THEOREMS + SHARPENED PROJECT SYNTHESIS**, not a
candidate-new or certified literature novelty.  Lean checks only rational
exponents—including the four target-matched collar identities—and finite
denominator, determinant, affine, and complete-square algebra.  Python
replays the same finite geometry and mask/cross-term guards.
Neither formalizes Poisson/Fourier analysis, the PNT semiprime block, mask
analysis, Wright/R87, the open `.98` bound, a zero-free strip, the four-cycle
bound, or RH.

## What survives, and what remains open

The following exact facts survive the hostile audit:

- `Q_h` zero-faithfulness and the complete-energy map `eta=kappa/2` in its
  licensed domain;
- `C=mu*Lambda=-mu log` and `C*1=Lambda`;
- the R116 balanced-semiprime conductor ledger in its stated scope;
- R123's collapse and R125's exact scale replication;
- R128's all-class identity `O_full=E_R71`;
- R130's frame identities after removing the double-square error; and
- R180's fixed-window strip/energy exponent calibration;
- the S1-B1 identity `W Lambda=[W,T_C]1+T_Cw` and its narrow-shell
  endpoint collapse; and
- the reflection normal form `[P_-,M_H]U=(H-H^R)R(U)/2`, with finite
  multiplier/reflection words confined to `M_a+M_b R`; and
- the QP legal-source identity `lambda.v=0`, the two distinct dual
  normalizations `z.q=-1` and `y.v=-1`, and the exact exponent identities
  `.001+.0179=.0189` and `.5-.001=.499`; and
- the correctly typed exterior charge, the Fredholm-contact equivalence
  between bounded existential factorization and KNC, the dense-core
  closability guard, and the square-root-versus-linear scaling distinction.
- the exact finite source-word remainder and its unchanged contact charge,
  the four-Cauchy Lerch normal form, and the infinite near-edge Hankel-rank
  obstruction at finite-state scope; and
- the compact source derivative bridges, with the causal `-V_delta` collar
  restored and the globally oriented Landau criterion correctly smoothed; and
- the one-mode fourth-root cancellation, global rotation/dilation
  commutativity, affine reflection relation, smooth-core boundary-jet
  constraints, projection-induced two-boundary cocycle, and branch-specific
  Toeplitz next-lag conditions from R185, all without a global compatibility
  theorem; and
- the exact split finite-part serialization, weak/distributional old equation,
  bounded `L2` finite-collar adapter, and continuous-potential plateau from
  R186, together with the no-go for generic endpoint jets and the exact
  synthetic coefficient-free propagation countermodel; and
- the R187 affine-center signed-measure identity, additive principal-band
  reduction, Gevrey Mellin-difference localization, and the guard that hard
  near/far pieces are signed rather than positive; and
- the R188 finite gamma-plus-affine completion, low-cofactor suppression,
  target-matched fifth-order collar with retained geometry
  `q>X^(499/500)`, `|a|<=X^(1/400)`, and physical quotient
  `v_phys<=X^(1/500+o(1))`, pole-faithfulness identity, and the correction
  that this core still contains low, high, and reducible determinants.  The
  collar is exponent-equivalent rather than a power saving.  The PNT
  semiprime block and Wright scale test remain analytic arguments rather than
  Lean claims.

The unresolved analytic debts are not reclassified as bugs:

- interval or symbolic certification of R124's sampled full-shell sign;
- an explicit all-profile/all-`g` order-reflecting comparison, if one exists;
- a genuinely non-tautological complete two-scale inequality or a
  coefficient--completion law outside the tested finite
  multiplier/reflection algebra;
- varying-test converses for the two sublinear single schedules; and
- centrally, a fixed-power bound for the complete R71 energy, which is
  already uniform-strip strength;
- equivalently after R188, one globally signed actual-coefficient correlation
  estimate on the target-matched collar, retaining every alias, determinant,
  conductor, projector term, affine or `Q_h` completion term, and cross term,
  with `X^(-1/50)` energy saving;
- actual-prime `DPA_P(.019)` and `LTRAD_P(.0189,.001)`; and
- a source-enforced zeta-specific boundary recurrence, quasianalyticity, or
  spectral-synthesis theorem beyond the commuting scalar
  four-Cauchy/dilation algebra.

No exhaustive impossibility theorem for primitive or combined structural
routes has been proved.  No uniform strip or RH follows from this correction
bundle.

The QP/Turán bifurcation remains parked.  The exterior-factorization
falsifier and constructive-source stop rule have now fired: every
existential/unqualified-core version collapses to KNC, and every tested
finite regular source word leaves the whole contact charge.  R185 has parked
only the proposed scalar root--dilation noncommutativity mechanism: those
pullbacks commute.  Its exterior-source formulas never used the old
homogeneous equation, and the projection cocycle is not the total KNC charge.
The split-Carleman state system and weak/L2 domain adapter are now closed.
The remaining direct statement is the zeta-specific propagation theorem
itself; no generic pointwise/jet adapter is available or needed.
The primary strip discovery target is the complete
source-preserving fixed-window R71 power bound; the compact source derivative
is its clean scalar falsifier.  R187 removes the analytic window tails and
localizes this endpoint to the completed additive principal band.  R188
serializes that band exactly and reduces it, at target-equivalent error, to
`q>X^(499/500)`, `|a|<=X^(1/400)`, and physical quotient
`v_phys<=X^(1/500+o(1))`.  This physical quotient is not the solution-line
Poisson dual; the surviving top box defeats componentwise Wright/R87 control.
The remaining joint correlation theorem has not been lowered below
uniform-strip strength.

## Durability and verification

The current workspace contains a large untracked research corpus.  These
files exist and are verified locally, but a clean clone will not retain them
until the user chooses a commit/staging policy.  This pass does not silently
stage or commit that corpus.

The synchronized bundle is checked by:

```text
python3 results/verify_zeta23_correction_bundle.py
python3 src/zeta23_correction_context.py verify
python3 src/zeta23_proof_tree.py verify
pytest -q src/test_zeta23_correction_context.py \
  src/test_zeta23_current_routing_state.py \
  src/test_fullinf_n4_checkpoint_fingerprint.py \
  src/test_s1_b1_completed_source_commutator.py \
  src/test_qp_source_fiber_bifurcation.py \
  src/test_exterior_factorization_audit.py \
  src/test_completed_source_constructive_search.py \
  src/test_four_cauchy_global_compatibility.py \
  src/test_split_carleman_form_domain_closeout.py \
  src/test_r71_minor_arc_triage.py \
  src/test_r188_principal_band_serialization_falsifier.py
cd lean/rhbridge && lake build RHBridge.CorrectionGuards \
  RHBridge.CorrectionGuardsAudit RHBridge.S1B1CompletedSourceCommutator \
  RHBridge.QPSourceFiberBifurcation RHBridge.ExteriorFactorizationAudit \
  RHBridge.CompletedSourceConstructiveSearch \
  RHBridge.CompactSourceDerivativeBridge \
  RHBridge.FourCauchyGlobalCompatibility \
  RHBridge.SplitCarlemanFormDomainCloseout \
  RHBridge.R71MinorArcTriage \
  RHBridge.R188PrincipalBandSerialization \
  RHBridge
lake env lean RHBridge/QPSourceFiberBifurcationAudit.lean
lake env lean RHBridge/ExteriorFactorizationAuditAxioms.lean
lake env lean RHBridge/CompletedSourceConstructiveSearchAudit.lean
lake env lean RHBridge/CompactSourceDerivativeBridgeAudit.lean
lake env lean RHBridge/FourCauchyGlobalCompatibilityAudit.lean
lake env lean RHBridge/SplitCarlemanFormDomainCloseoutAudit.lean
lake env lean RHBridge/R71MinorArcTriageAudit.lean
lake env lean RHBridge/R188PrincipalBandSerializationAudit.lean
```

The retained 2026-09-03 focused Python baseline passed `129` tests.  On
2026-09-04 the full Python suite passed `2428` tests in `71.78s`, and the full
Lean aggregate completed successfully (`13470` jobs).  The R188-only Python
suite passed `7` tests, the combined R187/R188 suite passed `14` tests, both
R188 Lean files passed, and the synchronized twenty-correction verifier
passed.  The
correction-guard, source-fiber,
exterior-factorization, constructive-source, compact-derivative, and
four-Cauchy compatibility, R71 localization, and R188 serialization axiom
audits report only Lean/mathlib's standard `propext`, `Classical.choice`, and
`Quot.sound` where used.
