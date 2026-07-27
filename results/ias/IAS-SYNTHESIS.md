# IAS panel synthesis — Rounds 1–2 (2026-07-26)

Moderator's synthesis of the 8-seat maximum-variance panel (magic-functions
[MF], quantum-chaos [QC], riemann-hilbert [RH], log-gas [LG], free-boundary
[FB], quasicrystal [QX], proof-theory [PT], renormalization [REN]). Sources:
COLLOQUIUM-BRIEF.md (C-1…C-11) and all eight SEAT files, both rounds, read in
full. House rules applied throughout: honesty tiers preserved as the seats
wrote them; every claim attributed; disagreements stated, never averaged.
Label collision note: quantum-chaos and quasicrystal both numbered candidates
"QC-n"; below, unprefixed QC-n means the quantum-chaos seat's, and the
quasicrystal seat's are written qx-QC-n.

Status vocabulary: SETTLED / SETTLED-WITH-AMENDMENT / PENDING-DATA /
CONTESTED.

---

## §1 Verdict table C-1…C-11

**C-1 (rigidity trichotomy) — SETTLED-WITH-AMENDMENT.** Adjudicated by MF
(R2.2.1 + the pre-registered SEP test), QC (R2.2, with the charge-matched
Sine₂ separator), and LG (R2.2 + the pre-registered separator run), with
concurring paragraphs from RH, FB, REN, QX. Verdict: at first order and fixed
L, worth-weighted charge neutrality (QC's I_w), the low-pass/charge functional
(LG's −(π²/2)J — literally the same integral, opposite sign convention), and
midpoint phase (MF's β_eff chart) are ONE statement — the linear response of
ln λ to δN with kernel (π²/2) d ln t on [t₀, eT*] — verified by the unit-slope
law measured four independent ways (0.955/0.975 MF transport; 0.96 QC; 0.954
LG; 0.94 MF SEP) and by exact cross-checks (β_eff − ½ = 0.0034 ⟺ I_w ≈ +0.03
vs measured +0.07; QC's I_w(ζ) = +0.073 vs LG's −(π²/2)J = +0.071 to the
printed digit, two implementations). LG's spectral gap (no ζ-deficiency
Fourier content below ln 2) is STRICTLY STRONGER: gap ⇒ neutrality at every L
⇒ fixed-L neutrality; both converses fail. Two separating examples now exist:
QC's charge-matched Sine₂ (I_w = 0 but intrinsic cost 0.55 ± 0.10 → β_eff ≈
0.433, separating phase from charge at second order) and LG's SEP coherent
narrowband mode (charge-neutral, sup|δN| ≤ 2, yet +2.8/+3.2 nats — separating
both per-L scalars from the gap at the level of validity domains). The
AMENDMENT (forced by LG's R2.5 run): the affine law's hypothesis must exclude
coherent narrowband sub-ln 2 modes — sup|δN| ≤ 2 alone is NOT sufficient.
Surviving statement: §2(d) below. ζ passes all three tests simultaneously;
that triple pass is the sharpened content of "maximally rigid."

**C-2 (the w∞ cluster) — SETTLED**, in three tiers with the horizon merger
SEPARATED out. The statement of record is RH's R2.2 draft as consolidated by
FB (R2.7(a)): Layer-0 identity web at THEOREM tier (FB, pure calculus,
re-verified; Lambert form w∞ = 1 + W(1/e) = 1.2784645 ≡ FB's root of
e^w(w−1) = 1, verified identical); RH's chart dictionary (I)(c) adopted as a
Layer-0 clause (w(ℓ) formula reproducing all five converged w_E2 values to
≤ 0.001 — a consistency identity across charts, NOT independent confirmation,
per RH's own flag); two corrections accepted by all parties: g′(w∞) = −1 is
STRUCTURAL (identical at any root — RH), and the approach is RESONANT,
w∞ − w ≍ ℓe^{−ℓ}, not pure e^{−ℓ} (RH + REN; REN's regime map: the drift
branch reaches w∞ only at ℓ* ≈ 3.28, so every existing deep window is
mid-crossover). Mechanism remains ONE missing derivation with four
reparameterizations (FB's phrase), CONJECTURE tier. The quasicrystal
horizon-merger hypothesis is NOT part of the theorem (all seats agree it must
not be bundled — QC put it sharpest: bundling would let one falsification
take down an exact-algebra theorem); priors on record: FB ≤ 0.15, QX 0.10
(down from 0.25), RH 0.4. Full text: §2(a).

**C-3 (the new constant p, A′) — PENDING-DATA.** RH pre-registered the
decision rule BEFORE scoring (R2.2): boundary log₁₀λ = −73.2 (λ = 6.3e−74);
any single RR rung < 1.0e−73 kills A′ = 16.75 outright (RH pre-committed the
retraction in writing); ≥ 3e−73 with decrement ratio flattening ≥ 0.2 favors
it. The finished L = 5.50 triple (1.9854e−64 / 1.4414e−67 / 4.2959e−69 at
m = 152/168/184) was scored NOT ADJUDICATED — value ratios INCREASING by 41×
(plunge pathology; Aitken invalid as a limit estimator), last rung 4.8 decades
above the boundary. REN's independent arithmetic concurs (mid-plunge; cannot
separate candidates). The m = 208 rung is COMPUTING as this synthesis is
written (results/ias/riemann-hilbert/rung_5p50_m208.log: G1/G2 gates passed,
assembly in progress). On p = 9/2 vs π²/2: unresolved by data (both survive
flatness, spreads 0.095/0.074); the colloquium's theory prior shifted TOWARD
9/2 (REN + RH Maslov/parametrix half-integer quantization; RH's Round-1
π²/2-as-prefactor mechanism has an acknowledged sign problem); LG registered
a third possibility (freezing-class 3/4-type shifts — p need not be either).
MF accepted the from-above assignment with the pre-committed four-line
prefactor ledger (R2.2.2; prediction: lines 2–4 sum to +1.5..+2.5 nats, i.e.
Δ = +2.08 is real structure). The two K5-quarantined numerology items
(A′_Fuchs + 2; ln(2^{29/2}π⁵)) stay quarantined; same rung kills or spares
them.

**C-4 (chirp trichotomy) — SETTLED.** QX owned. Verdict: the block-spin PASS
(REN), the low-pass functional (LG), the charge regression (QC), and the
β-dial transport (MF) are four coordinatizations of ONE object — the marginal
kernel (π²/2)ln(eT*/t)dN on [0, eT*] — quantitatively consistent NOW at the
5–25% level, which is the measured second-order dressing. The residue only QX
sees: all four are linearizations around the graded baseline; the trichotomy
is about the BASELINE — periodic ⇒ exactly zero toll (THEOREM), incommensurate
constant-density ⇒ polynomial small-divisor floor (COMPUTED, pre-registered:
factor ~23 between walls, not ≥ 10²), grading ⇒ the super-exponential toll.
LG supplied the one-sentence reconciliation ("the worth potential is the
integral of a weight only a GRADED density creates; at constant density
f ≡ 0"), co-signed by QX and REN. REN's strict "zero toll for any FQ" was
corrected by QX's measurement (its own Round-1 bet, graded honestly).
Surviving statement: §2(b). QX's discriminating displacement-response scan on
the two-scale union is pre-registered and unrun (offered to REN).

**C-5 (Q3 factor 6.3) — SETTLED as a first-order/rigidity effect: DEAD.**
Two independent death verdicts formally co-signed (QC: I_w(true, 3.555) =
+0.11 vs +1.84 needed, a 3.3σ excess over the charge-line scatter; LG-2's
low-k budget: nothing below ln 2 can sustain 1.84 nats), joined by MF, which
RETRACTED its own §5.1 phase reading (by the C-1 equivalence, a β_eff excess
IS first-order charge, and the charge isn't there), and by FB (no
constrained-sweep mechanism exists for it). The surviving suspects are Gcut
truncation (both owners' lean, parsimonious) or an anomalous second-order
local effect. The formal death of the ANOMALY still requires the SYNTHESIS-Q3
Gcut escalation; joint pre-registered prediction (LG + QC): the gap collapses
to |ΔE| ≤ 0.4–0.5 nats as Gcut → ∞. Pre-committed consequence if it survives
above 1 nat converged: QC-2's magnitude clause and LG-2's quadratic bound
both need repair, and that outcome would be the first visible arithmetic
beyond density + neutrality — "either way Q3 stops being folklore" (LG).

**C-6 (Poisson diligence) — SETTLED-WITH-AMENDMENT; run pending.** The
apparent QC/LG conflict dissolved: QC's "intrinsic −2.0 to −2.7" is a slope-1
residual on ONE seed; LG's "+5.5 intercept" is an OLS artifact of forcing an
affine law through seeds whose slope-1 residuals are +2.7…+9.6 — not a
constant. Joint co-signed verdict: at sup|δN| ≳ 2–3 NO affine law in J
exists; the functional crosses over to extreme-value form (worst local
deficit priced by the marginal law; surpluses non-refunding); "intrinsic
Poisson cost" is only well-defined charge-matched. The deliverable exists:
QC's seven-step protocol (R2.2) adopted verbatim by LG with three riders
(m-ladder requirement from F3; SEP disambiguation variant; Var-J growth
discriminator). Two distinct pre-registered central bands are ON RECORD and
the run adjudicates between them: LG +3.5 ± 1.5 vs QC 2.0–3.2 nats
(charge-matched, L = 2.485). ENVELOPE.md §2b rewrite text is drafted (§7).

**C-7 (ensemble ≠ number) — SETTLED.** λ_GUE is a distribution: free-window
sd 3.60 nats (4.7 orders across ten seeds), anchored 1.48–1.92; 7/10 (DG-P3)
and 9/10 (NT-P2) of seeds outside the prior panel's locked windows; window
phase u₁ alone explains ~89% of the variance (corr 0.945). The correct
invariants are (bias, Var J): bias = intrinsic local-statistics cost (rigid
0; ζ ≤ 0.1; Sine₂ 0.55 ± 0.10 pooled over 28 samples, two seats, two
conventions; Poisson non-affine), Var J = the number-variance kernel read
through d ln t ⊗ d ln t on [0, eT*]². LG drafted the distributional
restatement for the prior panel's ledger (R2.2 C-7 blockquote — adopt as
written). PT added the metamathematical rider: instance-level certificates
are immune (soundness untouched); ensemble-mean certificate pricing is now
MEANINGLESS (inherits the 4.7-order spread); ζ is measured measure-atypical
(0 ± 0.1 against sd 3.6), so independence- and disproof-hunting must run on
the instance, never a surrogate ensemble.

**C-8 (prior-art risk on MF-1) — SETTLED by executed diligence.** MF ran the
live check (WebSearch/WebFetch, arXiv 2206.03682 / 2209.04658 / 2606.09096 +
the repo's sweep). Verdict, binding on the MF seat: **MF-1(a) as a novelty
claim is WITHDRAWN** — the global positive-representation dictionary is
Suzuki-on-Kreĭn–Langer (in print 2022–2026; "g is a screw function on ℝ iff
RH"); the windowed extension statement is a bridging remark to be written
with full credit, not a lemma to claim. MF-1(b) (dual-witness
identifiability / super-resolution) and MF-1(c) (extension-set width =
envelope) SURVIVE as the seat's own: the targeted full-text interrogation of
2606.09096 found none of the four decisive items (no windowed Krein
continuation, no dual/variational λ_a characterization, no
Pontryagin/negative-square pole treatment, no quadrature/super-resolution
content). Residual obligation: a full read of 2209.04658 (MF, days, queued).

**C-9 (Lean-ready queue) — SETTLED and partially EXECUTED.** PT's ranking by
value-per-person-day stands: (1) qx-QC-2 annihilating-pair rearrangement,
(2) Floor Witness, (3) PT-1 transfer theorem (F(i).0 de-risk first).
Execution status: qx-QC-2 is DONE — `anchor_collapse` and
`anchor_collapse_of_deep` are implemented in
`lean/glide/Glide/HardHorizon.lean` per QX's R2.2-C9 spec (Hypothesis A
dropped via `by_cases`; no sorries; see §6). The Floor Witness (PT-3(c),
dispatch spec in PT R2.2) is IN BUILD with success bands pre-registered
(PT R2.6-T1). PT-1 remains a scheduled workstream, not a panel-week task
(110–215 pd Tier 1; pacing item F(i).1 doubles as the formal
disproof-receiver).

**C-10 (the wall) — SETTLED.** The five-clause Wall-Breaking Specification
(PT R2.2) is countersigned VERBATIM by FB (R2.7(b)) — it subsumes FB's own
four-clause draft — and co-signed by MF through Merge M2 (the density answer
delivered: pure staircase data is NOT a uniqueness set; the correct data set
is staircase head ∪ boundary k-jet ∪ anchor band; the jet supplies the
finitely many missing dimensions). Core content: (1) any wall-breaking
theorem must use an input invisible to the template interface (PT-2's
gap-band countermodel at ε ≈ 5×10⁻⁸); (2) that input cannot be a
positive-exponent decay modulus (s = 0 log-Laplacian endpoint; F5 is sharp;
raw decay beyond trace-driven r⁻² is FALSE for actual minimizers, FB-T1
measured); (3) the minimal candidate is the Corner-Jet Decomposition; (4)
extraction demand: the jet bounds must be Π₂ moduli, uniform in the
EL-residual, no unquantified compactness — FB accepted this into FB-3's
execution plan; (5) the joint falsifier (𝒯+jet adversary search) is
pre-registered with dual bands (PT R2.6-T2). FB-T1's next-rung gate
(m = 96/128 trace stability, > 20% drift = red flag) rides along. Full text
pointer: §2(c).

**C-11 (vector shape test) — SETTLED (integrated).** The scalar cap evidence
stands unopposed and uncertified (B_smooth NOT CERTIFIED; falsifier unfired;
null control refuted the discriminator's premise). The panel absorbed the
vector deliverables: RH reconciled the universal E-normalized profile with
BKMM (profile = fixed-point g-function; predicted collapse residual O(δ) ≈
±0.02–0.05·E matches the measured ±0.02·E; offered the one-page
integration-by-parts lemma converting the 30/20/50 shares into equilibrium
data — accepted by FB and REN). QC RETRACTED the pointwise node-ledger
reading of QC-3 (dodged zone = only ~20% of the exponent) and kept the
tunneling/evanescent version (80% smallness IS the WKB signature), flagging
honestly that the (aT*)^{−2/3} Airy width looks too small for the 30%
below-T* share — recorded as open tension. FB RETRACTED its filler mechanism
and pointwise-Agmon clauses, promoted the three-zone + floor phase diagram
(0.30·E sub-T* band / 0.19–0.21·E registered zone to x_d ≈ 0.60–0.65 /
≈0.50·E nodeless, floor at E/2 + 3±1 nats) to the adequacy condition any
derivation must reproduce, re-based the horizon-merger evidence (the eleven
"stopping heights" are ACTION heights — §7 item 1), flipped its Q7
expectation to fixed-profile, and pre-registered the x_d → ln 2 share
speculation (share → ln 2 − ½ = 0.19315, dead center of the measured
0.192–0.210) as a falsifiable rider. Material design consequence (FB → REN,
MF): the stopped-chirp construction should stop REGISTRATION at ≈ 2T*, not
at e^{w∞}T*, with nodeless suppression carrying ~4/5 of the action.

---

## §2 The co-signed artifacts

### (a) The w∞ Saturation Statement

Statement of record: RH's R2.2 draft, consolidated by FB R2.7(a), amended by
REN R2.2; co-sign slots FB, RH, REN, QC (QX observer status pending its
qx-QC-3 computation; DG vector data as evidence). Notation: E = −ln λ,
ℓ = L/2, c = e^ℓ, T* = 2πc, D(T) = (a/π)T − N̂(T); w(ℓ) defined by the
action bookkeeping E + A = 2π[D(T*) − D(e^w T*)] = T*(e^w(w−1) + 1).

> **(I) THEOREM (exact algebra; provable today; no mechanism assumed).**
> (a) [FB Layer-0 web + RH excess-count + QC Heisenberg forms] The following
> are equivalent as ℓ → ∞: dE/dc → 4π; (E+A)/T* → 2; the swept surplus
> repays the deficit twice, Surplus(w) := ∫_{T*}^{e^wT*}(ρ − a/π)dt → 2e^ℓ;
> e^w(w−1) → 1; −D(T_s) → e^ℓ; τ_H(T_s) → t_obs + w∞; dE/dM → 4π (M = e^ℓ).
> The root is w∞ = 1 + W(1/e) = 1.2784645…, T_s/T* → e^{w∞} = 3.5911.
> (b) [FB, new, 7/8-clean] D(eT*) − D(e^{w∞}T*) = e^ℓ EXACTLY — the second
> epoch's balayage identity in D-form.
> (c) [structural, RH's correction accepted by FB and REN] At ANY root of
> e^w(w−1) = 1 the flow w′ = g(w) = (1 − e^w(w−1))/(e^w w) has g′ = −1
> IDENTICALLY: FB's attracting fixed point, REN's cap eigenvalue −1, and the
> Fuchs p·ℓ subleading form are ONE fact in three notations; the falsifiable
> content is entirely that the subleading term is O(ℓ).
> (d) [RH chart dictionary, adopted as Layer 0 by FB] If E = 4πe^ℓ − p·ℓ −
> A′ + o(1), then w(ℓ) = w∞ − [p·ℓ + (A′ − A)]e^{−ℓ}/(2π(1 + e^{w∞})) +
> O(ℓ²e^{−2ℓ}): the deep pair (p, A′) and the stopping-height approach are
> ONE datum, and the approach is RESONANT (ℓe^{−ℓ} — the flow is
> non-autonomous at the order the ODE is written). COMPUTED consistency:
> reproduces all five converged w_E2 values to ≤ 0.001 (consistency
> identity, not independent confirmation). REN regime map: drift branch
> reaches w∞ at ℓ* ≈ 3.28 (L ≈ 6.6); every existing deep window is
> mid-crossover; co-signed qualitative expectation — approach from below, no
> overshoot, drift residuals growing more negative through L ≈ 5.5–6.
> **(II) MEASURED.** dE/dc = 4π to 0.4–1.3% past L ≈ 4.32 by three scalar
> routes; B_abrupt excluded; the vector discriminator returned NOT CERTIFIED
> with its falsifier unfired and its premise refuted by the null control
> (C-11): the scalar evidence stands unopposed and uncertified.
> **(III) CONJECTURE (the co-signed claim).** lim dE/dc = 4π, equivalently
> any (hence every) item of menu (I)(a); unit-rate RESONANT approach.
> Candidate mechanisms on record — second-epoch mass balance (FB-2), budget
> exhaustion / min-of-two-costs (RH pump 1), RG fixed point (REN §1.3),
> smooth pasting with third-order (pulled-to-pushed) crossover (QC-4, the
> attached falsifiable rider: C² with third-derivative jump) — are
> reparameterizations of ONE missing derivation, not four derivations. The
> factor 2 (why the second epoch sweeps exactly one more deficit mass) is
> trajectory/matching data (REN's classification) and is the open core.
> **(IV) SEPARATED — not part of the theorem.** The horizon-merger
> hypothesis (sharp anchored-vanishing horizon = e^{w∞}T*) is a distinct
> conjecture about a different object (feasibility ceiling vs variational
> standoff); its previously quoted empirical support is RE-BASED by C-11
> (the eleven stopping heights are action heights; actual registration dies
> at ≈ 1.9T*). Priors on record: FB ≤ 0.15, QX 0.10, RH 0.4. Deciders: FB's
> slit-plane K₀ computation (FB R2.6, joint with QX) and QX's pre-registered
> BM-window anchored-dodger kill test.
> **Kill criteria:** converged deep secant slope off 4π by > 0.5%; the
> L ≥ 5.5 ladder violating (I)(d)'s dictionary beyond the A-band; DG-style
> vector drift verdict; FB's share-drift falsifier (x_dodge → ln 2, share →
> 0.1931 — a share settling elsewhere kills the 2T* reading).

### (b) The Deficit Mechanism Statement

REN's R2.2 C-4 box, with QX's base-point clause built in as clause (2) and
LG's coherence exclusion appended as the binding amendment. Co-sign slots:
REN, QX, LG, FB, MF (transport clause), QC (charge clause).

> For windowed frame margins of symmetric point configurations:
> (1) the super-exponential exponent is a functional of the Nyquist-deficit
> measure dμ_L alone — E + A = Φ[dμ_L], with Φ ≈ b·M·ln(e^{c₀}M) mid-range
> and dΦ/dM capped at 4π (M = deficit mass = e^ℓ);
> (2) [QX's base-point clause] configurations with NO deficit pay no
> exponent: periodic sub-Nyquist = exact tight frame (zero toll, THEOREM);
> incommensurate unions below their Landau wall = prefactor/conditioning
> cost only (MEASURED: ~23× across the whole inter-wall band — small-divisor
> physics, not deficit physics; a Diophantine floor invisible to every
> linearization);
> (3) at fixed deficit profile, perturbations are priced by the
> linear-response kernel f(t) = (π²/2)ln(t_cap/t) — the Gateaux derivative
> of Φ — in the small-discrepancy regime, crossing over to an extreme-value
> (worst-local-deficit, surplus-non-refunding) functional beyond sup|δN| ≈ 2
> (LG P5). [FB-T2 rider, accepted by REN:] the kernel is a Danskin/envelope
> derivative of the VALUE along optimized families; the frozen-configuration
> potential-gap reading is MEASURED DEAD (FB-T2: wrong sign, slopes 3–4×) —
> any equilibrium derivation must price on the re-optimized sweep;
> (4) the grading (drifting density) is precisely the operator that
> manufactures deficit at every scale; it is marginal (its rescaled profile
> ln(1/u)du is flow-invariant), and its logs are the (ℓ + c₀) factor.
> Discreteness rider (K2): Φ's argument is the deficit measure of the
> DISCRETE configuration; density smoothing destroys the value. Additivity
> rider (K7): the kernel is marginal only; global per-zero accounting fails.
> **[LG coherence amendment, binding on clause (3):]** the affine regime
> requires sup|δN| ≤ 2 AND an incoherent (correlation length ≲ one spacing)
> or monotone-transport displacement field; coherent narrowband modes below
> ln 2 are EXCLUDED, with LG's SEP run (k₀ = 0.10, sup|δN| = 1.8, cost +3.2
> nats with wrong sign vs charge) as the recorded counterexample. ζ
> satisfies the hypothesis vacuously (its deficiency spectrum, primes AND
> sawtooth, lies entirely at k ≥ ln 2 > the functional's band).

Four instruments measure clause (3)'s kernel consistently: REN block-spin
dipoles (1.173/1.259), LG CUE ensemble (r = 0.991, slope 0.954), MF β-dial
transport (0.955–0.975), law-theory RUN 4 (the original). The second-order
structure (dipole enhancement +17/+26% vs distributed slopes ≈ 0.95 vs W > 0
pair superadditivity vs deficit/surplus asymmetry) is unified in no seat's
theory yet; the C-4 block-size scan (REN + LG, one afternoon, designed) is
the assigned probe of Φ's Hessian.

### (c) The Wall-Breaking Specification

PT's five clauses (R2.2, C-10), countersigned VERBATIM by FB (R2.7(b));
MF co-signs via Merge M2 with its density verdict. Reproduced as program law:

> Any theorem that certifies the unrestricted infimum of Q_L (retiring
> FULLINF F5's obstruction) must contain:
> 1. [PT; THEOREM once PT-2(ii)'s bookkeeping is done] an input about
> near-minimizers NOT derivable from the template interface {certified
> Galerkin data; W₊ ≤ C_B*; symbol envelope; bilinear composition} — that
> interface is consistent with negativity (gap-band countermodel, mass
> ε ≈ λ_m/√T₂ ≈ 5×10⁻⁸ at (7/4, 192)).
> 2. [FB; structural verdict] that input cannot be a positive-exponent decay
> statement from coercivity: the EL operator sits at the s = 0 (logarithmic)
> endpoint — the CSS package degenerates, F5 is sharp there — and raw tail
> decay beyond trace-driven r⁻² is FALSE for actual minimizers (FB-T1:
> trace 0.0106 m-stable; τ_φ(287) = 3.8e−7 = FULLINF's mystery tail,
> explained).
> 3. [FB; CONJECTURE with measured support] the minimal known candidate is
> the Corner-Jet Decomposition: finitely many explicit boundary atoms (exact
> data, no modulus needed) + remainder ψ_k with τ_{ψ_k}(R) ≤ C_k R^{−(2k+1)}.
> [MF's M2 clause: the underlying uniqueness statement must be on staircase
> head ∪ boundary k-jet ∪ anchor band — pure staircase data is
> density-deficient; the jet supplies exactly the missing finite dimensions.]
> 4. [PT; modulus-extraction requirement] the corner-jet route satisfies
> PT-2(iii)'s necessity demand PROVIDED FB-3(ii)/(iii) is stated in Π₂
> moduli form — explicit C_k(ρ, L), uniform in the EL-residual ρ, consumed
> at Galerkin argmins; no compactness or unquantified Fredholm step. FB has
> accepted this as binding on FB-3's execution.
> 5. [joint falsifier, pre-registered PT R2.6-T2] the countermodel search
> re-run inside the corner-corrected interface must come up empty at
> moderate C₃ (the k = 3 class allows tail mass ≈ 3×10⁻¹⁹·C₃ where the
> countermodel needs ε ≈ 5×10⁻⁸ — the atoms re-inject the support constraint
> at the boundary, where it lives); within the UNCORRECTED interface the
> search must SUCCEED at ε ∈ [2, 20]×10⁻⁸ with Q^{F0} ≤ −10⁻⁵. Either half
> failing sends Merge M1 back to the definitional drawing board —
> pre-committed.

Additional standing falsifier: FB-T1's next rung (|t_m| drifting > 20% at
m = 96/128 kills the jet stability the structure theorem needs).

### (d) The First-Order Response Law (the C-1 dictionary)

Merged statement (QC's M-A + LG's M-1, post-SEP amendment; MF's phase chart;
HA's T4(i) as engine; PT certifies extraction; DG/T3 consumes):

> For symmetric configurations at RvM density with sup_{[0, eT*]}|δN| ≤ 2
> AND displacement fields that are incoherent (correlation length ≲ one
> spacing) or monotone-transport — coherent narrowband components below
> ln 2 excluded (LG F1 counterexample on record):
>   ln λ[Γ](L) − ln λ[smooth](L) = κ·(π²/2)∫δN(t) dt/t − c_int + err,
> with κ = 1 + o(1) (measured 0.94–0.975 by four instruments), c_int
> depending only on the local-statistics class (rigid: 0; Sine₂: 0.55 ± 0.10,
> pooled 28 samples/two seats; ζ at accessible heights: ≤ 0.1), and err
> second-order (dressing band +17…+26% for concentrated dipoles; −0.08 nats
> for in-gap neutral modes at A ≲ 0.35). Beyond sup|δN| ≈ 2 the functional
> is extreme-value: deficit-side sup-pricing, surplus saturation — transfer
> hypotheses must be ONE-SIDED (sup-deficit) discrepancy.
> Chart dictionary: I_w (QC) = −(π²/2)J (LG) exactly; β_eff − ½ =
> −J/S + O(c_int/((π²/2)S)) with S = Σ_{t_k ≤ eT*} 1/(t_k N̂′(t_k)) (MF).
> Mechanism clause (QC/LG): the ζ deficiency field has no Fourier content
> below ln 2 (primes AND sawtooth), the functional's weight is a low-pass
> filter at k ≲ 1/t₀ ≪ ln 2 — hence neutrality at EVERY L; Berry saturation
> and Selberg's CLT are this statement integrated.
> Separating examples (the trichotomy's second order): charge-matched Sine₂
> (I_w = 0, β_eff ≈ 0.433 ≠ 0.5034 — intrinsic term leaks into phase; QC);
> coherent sub-ln 2 mode (neutral at its window, +2.8 nats there — validity
> domain, not just uniformity; LG). Hierarchy: gap ⇒ all-L neutrality ⇒
> fixed-L neutrality = midpoint phase; both converses fail; ζ passes all
> three.
> Corollary (to DG/T3): the deterministic LR-regime transfer constant is
> κ(π²/2)ln(eT*/t₀) per unit sup-discrepancy — predicts MF's measured
> phase-transport bound 6.64 as 6.59 (1%). T3's hypotheses restated in
> one-sided deficit discrepancy (LG revision 1, co-signed FB, MF).

---

## §3 Scorecard — every pre-registered test, both rounds

Format: seat / test / prediction / outcome / lesson. "KILLED-OWN-MODEL"
marks a seat's pre-registered test destroying its own prior claim — the
panel's most productive category.

**Round 1.**

| seat | test | verdict | what the failures taught |
|---|---|---|---|
| MF | β-dial (P1–P4, locked) | P1 FAIL (monotone in β, peak/trough 768, no interior optimum); P2 half (direction right, magnitude ×38.6); P3 PASS (near-vacuous; post-hoc β_eff = 0.5034); P4 PASS (barely) | KILLED-OWN-MODEL for MF-2(b) as stated: the staircase is NOT near-optimal in the naive class (optimum is bang-bang at the boundary); "maximally rigid = maximal λ" is false — the zeros optimize BALANCE. Bonus: transport check validated the marginal law at 2.5–4.5% with zero fitted parameters (a new validation mode) |
| QC | GUE rung (P1–P3 + KILL) | KILL not fired (every seed ≥ 2.9 nats above Poisson); P2 PASS; P1 FAIL (median +1.53, positive); P3 FAIL (spread 6.28 ≫ [0.2, 1.5]) | Realized charge dominates single samples; post-hoc decomposition Δ = 0.96·I_w − 0.66 (r = 0.963) became the panel's central object; a sign correlation was predicted BACKWARDS in a post-hoc diagnostic and corrected in print |
| LG | CUE/Sine₂ battery (P1–P7, locked) | P1 FAIL (mean −1.34 vs [−0.5, +2.2] — overtaken by exactly the scatter P2 predicted); P2 PASS dead center (sd 3.60); P3 PASS (r = 0.991, slope 0.954); P4 PASS (2.43); P5 PARTIAL — concavity cap FAILED 4/4 applicable seeds; P6 PARTIAL — LG-4(ii)/(iii) REFUTED (W > 0 at ALL separations, growing toward the edge); P7 PASS ((π²/2)J[ζ] = −0.071) | One-sided extreme-value crossover discovered (deficit-amplified, surplus non-refunding); pairwise screening-sharing dead — subadditivity is many-body; the window-phase mode is the spread |
| QX | two-scale union (P-A…P-E, prereg.md) | P-A PASS (point guess wrong by 10²⁺ in the informative direction); P-B PASS (glide restored by incommensurability alone; control flat to 7 digits); P-C FAIL-informative (23×, not ≥ 10²); P-D PASS (instrument certified to 1.0595883); P-E PASS | Aperiodicity at constant density is CHEAP (polynomial small-divisor toll); the super-exponential toll is priced entirely by the chirp; "glide needs an archimedean place" dead as a necessity claim |
| REN | block-spin decimation (locked bands) | PASS both directions (ratios 1.173/1.259 in [0.65, 1.35]) — with an honesty note: the pre-registration PROSE asserted the wrong sign; magnitudes/bands were locked correctly; correction logged, both files kept | The marginal law is a genuine linear-response kernel for count-preserving redistribution; dressing +17/+26% ≈ law-theory's ~20% non-additivity; positive interaction curvature (+0.044) — staircase locally a strict minimum against dipoles |
| FB | FB-T1 trace/tails (PREREGISTRATION-FBT1.md) | Regression PASS; P1 PASS (trace 0.0106, m-stable); P2 PASS (far tail = trace tail; FULLINF's 4e−7 explained as 3.8e−7); P3 structure confirmed, payoff gate FAILED AS REGISTERED (jet is O(1)–O(5), not small — retracted); P4 inconclusive as anticipated | Corner atoms must enter as certified DIRECTIONS, not small corrections; the payoff argument runs on tail exponents (−2 → −4 per atom, as predicted) |
| PT | mathlib audit (4 claims, locked) | 3/4; T3 FALSIFIED (no argument principle/residue/Rouché in mathlib — only Jensen) | The miss was load-bearing: PT-1 rerouted through the Jensen-disk Cert; any zero-certificate design assuming winding-number machinery is currently wrong |
| RH | pinned-action extraction (P1–P4, locked; disclosure of by-hand previews stated) | P1 PASS (p = 4.85 ± 0.10; 11/2 and 6.5 excluded; 9/2 and π²/2 both survive); P2 PASS — headline: A′ = 16.75, Δ = +2.076 over Connes/Fuchs 14.6757, Fuchs-literal jointly rejected at matched action; P3 logged (L = 5.50 forecast −72.6/−72.7 vs Fuchs −73.6); P4 not triggered | A new Widom–Dyson-class constant; also corrected the record: L = 4.60 limit ≈ 2.100e−43, not 2.336e−43 (§7) |

**Round 2.**

| seat | test | verdict | lesson |
|---|---|---|---|
| MF | SEP separating-example (R2.2.1a, locked) | SEP-P1 PASS (|−0.183| ≤ 0.4; ratio 0.060); SEP-P2 PASS (slope 0.94 vs exact discrete charge — fourth unit-slope appearance); SEP-P3 PASS (second-order remainder −0.08 nats) | At fixed L the functional prices charge, not spectral position; the gap's role is all-L enforcement; C-1 adjudicated as claimed |
| LG | separator run (P-R2-A/B/C, locked; credit-outage interruption disclosed; design-stage amplitude amendment logged before any eigensolve) | P-R2-A FAILED AS LOCKED (A = 0.9 could not reach the gate; passed at A = 1.8 under the labeled amendment); P-R2-B: CTRL PASS at all L; SEP HARD FAIL at L₂ (+2.78 vs −0.09) and L₃ (+3.18, WRONG SIGN vs −1.56); P-R2-C: CTRL PASS; SEP "failed as intended" (wrong mechanism) | KILLED-OWN-MODEL: M-1/M-A's sup|δN| ≤ 2 hypothesis REFUTED AS WRITTEN — the coherence exclusion (F1) was forced; plus the m = 48 basis warning (F3): structured configs can carry the wrong sign at m = 48 (CTRL L₃ swung −1.74 → +0.22) |
| RH | C-3 triple discriminator (decision rule written before scoring) | NOT ADJUDICATED — the triple's own diagnostic failed (ratios rising 41×; Aitken invalid); last rung 4.8 decades above the boundary; m = 208 rung launched under the same rule (PENDING) | Pre-commitment held: no side selected; upper-bound kill logic (< 1.0e−73 kills A′) rides the running rung |
| FB | FB-T2 defect-potential sum (R2.5, locked) | G1 FAIL 0/9 (2G negative everywhere; slopes 2.98×/4.00× the target); G2 FAIL (wrong sign throughout); G3 recorded (registration-edge mildly less wrong; decides nothing) | KILLED-OWN-MODEL as designed: the bare potential-gap reading of the marginal law is DEAD; the worth is a Danskin envelope derivative on the re-optimized sweep; LG's multiplier bet pays NO in bare form; Merge-B road (1) closed before RH's ordering even landed |

**Bets formally retracted or paid (the material ones).** Retracted: MF's Q3
phase reading (joined the C-5 death verdict); MF-1(a) novelty (C-8); QC's
node-ledger clause of QC-3 and QC-1's ensemble-ladder ratio clause; RH's
two-saddle/Stokes reading (refuted partly by its own pump; renamed smooth
pasting) and its bet 5 on QX (crossover as AP-resolution scale); FB's
filler-mechanism pump and 42/58 split (C-11), plus its Airy expectation
flipped and jet-smallness sub-claim withdrawn; REN's strict zero-toll form
and the "archimedean = necessary for glide" slogan; QX's merger confidence
0.25 → 0.10; LG's LG-4(ii)/(iii) and its "T3 constant worse than jitter"
framing withdrawn jointly with MF (correct chart: one-sided charge). Paid /
confirmed: FB↔RH mutual BKMM identification (verbatim convergence under
independence); REN↔FB↔RH the three −1's unified; LG's bet 3 on QC (Berry
saturation ≡ prime-sum bound — certified, independently replicated at the 1%
slope level, 28 pooled samples); PT's B1 on MF (converged, sharpened by
FB-T1); QX's bet on REN (chirp-as-RG, landed verbatim); FB's Poisson-LIL bet
on LG (inside factor 2 on the number, wrong mechanism — paid with
correction); REN's p = n + ½ assignment to RH (adopted as primary). Unclaimed:
PT's B4 toy (transfer-operator F5 model) — REN accepted the framing, priced
it MEDIUM, will co-author only if PT drives.

---

## §4 Kill list additions (for program law)

Precision matters here: each entry states what EXACTLY died and what
survives.

1. **Bare potential-gap model of the marginal worth** (frozen-configuration
   sum 2G(t₀) vs a fixed budget lattice). DEAD — FB-T2, 0/9, wrong sign,
   slopes 3–4×. Survives: the worth as Danskin/envelope derivative of the
   VALUE along the deletion family (T4's rank-two secular route untouched;
   the multiplier reading only on the re-optimized sweep).
2. **sup|δN| ≤ 2 as a sufficient hypothesis for the affine response law.**
   DEAD — LG SEP: a coherent narrowband mode (k₀ = 0.10 < ln 2, sup|δN| =
   1.8) costs +3.2 nats with the wrong sign. Survives: sup|δN| ≤ 2 AND
   incoherent-or-monotone-transport; coherent sub-ln 2 modes excluded.
   Consequence: M-1/M-A statements amended; T3 hypotheses restated one-sided
   AND coherence-aware.
3. **MF-1(a) as a novelty claim.** WITHDRAWN — Suzuki 2206.03682/2209.04658/
   2606.09096 on Kreĭn–Langer own the global dictionary. Survives: the
   windowed statement as a bridging remark with full citations; MF-1(b)
   identifiability and MF-1(c) extension-width as MF's own (verified absent
   from the flagship screw paper by targeted interrogation).
4. **Horizon-merger as a corollary or clause of the w∞ theorem.** SEPARATED
   — and its quoted data support RE-BASED (the eleven stopping heights are
   action heights; registration dies at ≈ 1.9T*). Survives: as a standalone
   conjecture with priors 0.10 (QX) / ≤ 0.15 (FB) / 0.4 (RH) and two named
   deciders (slit-plane K₀; BM-window dodger test).
5. **Stokes-jump / two-saddle-exchange reading of the L ≈ 4.32 crossover.**
   DEAD — first-order slope jump excluded by the deep-windows level test; no
   seat defends it (RH's own pump predicted smoothness). Survives: boundary
   saturation / smooth pasting, with QC-4's third-derivative test as the
   attached order discriminator.
6. **QC-3's pointwise node-ledger clause** ("|F|² drops 2π(1−τ) per zero
   dodged" as a pointwise mechanism). DEAD — C-11: dodged zone carries only
   ≈ 20% of the exponent. Survives: the integrated action identity and the
   tunneling/evanescent restatement (M-B protocol; evanescent share 0.7–0.9
   pre-registered).
7. **Ensemble-mean certificate pricing; "λ_GUE" as a number.** DEAD — C-7
   (sd 3.6 nats; 4.7 orders across ten seeds). Survives: per-window
   instance-level pricing (immune, PT); the (bias, Var J) pair as the
   ensemble invariant.
8. **"Zeros as λ-extremizers" / "maximally rigid = maximal λ".** DEAD — MF
   β-dial (pure phase beats the zeros inside the class; the class optimum is
   bang-bang at the boundary). Survives: the zeros as worth-NEUTRAL /
   balanced (charge-neutral at every L; spectral-gap mechanism); REN's
   "fixed-profile offset" wording adopted program-wide.
9. **Pairwise screening-sharing (LG-4 clauses (ii)/(iii)).** DEAD — W > 0 at
   all tested separations, growing toward the capacity edge (three seats'
   data now concur: LG pairs, REN dressing, QC Poisson amplification).
   Survives: capacity-dilation + edge-rehardening (W ≥ 0); subadditivity as
   a many-body/deletion-density effect; T5's shared-suppression design must
   share at density level.
10. **Fuchs-literal deep constants (p, A′) = (4.5, 14.676).** REJECTED at
    ~2 nats of constant at matched action and log-slope (RH §5) — subject to
    C-3's pending rung, with RH's retraction pre-committed if the rung lands
    < 1.0e−73.
11. **Raw frequency-decay form of the forced regularity modulus.** DEAD —
    FB-T1 (near-minimizers have trace-driven r⁻² tails with O(1) constants).
    Survives: the jet-corrected remainder modulus (Wall-Breaking Spec clause
    3); PT's necessity argument STRENGTHENED (one more candidate class
    measured out).
12. **The one-cut/artanh global worth shape.** DEAD — FB Round 1 (predicts
    4.54 where 6.92 is measured); the bulk has zero additive offset; edge
    corrections confined to the last e-fold.
13. **Single-rung m = 48 readings of structured/coherent configurations at
    L ≥ 3.** UNRELIABLE below |ΔE| ≈ 2 — can carry the WRONG SIGN (LG F3:
    −1.74 → +0.22). Protocol law: m-ladder (48/64/80) required. Random
    (CUE/Poisson) configs are not affected (two-builder cross-checks).
14. **"Zero toll for any Fourier-quasicrystal spectrum" (strict form) and
    "aperiodicity is expensive" (the opposite prior).** BOTH corrected by one
    measurement (QX §5): constant-density incommensurate toll is polynomial
    (~23×), neither zero nor ≥ 10². Survives: "no deficit ⇒ no
    super-exponential toll" (clause 2 of §2(b)).
15. **"The glide requires the archimedean place" (necessity form).** DEAD —
    QX P-B (incommensurability alone restores the glide). Survives: Theorem
    1 (sufficiency) untouched; REN's wobble-audit criterion sharpened
    (smoothness excludes single-preferred-lattice candidates only).
16. **MF's "b in a Painlevé σ-form or nowhere" dichotomy.** REFUTED (RH):
    b and μ are crossover-trajectory amplitudes (REN's classification —
    NOT eigenvalues, invisible to fixed-point expansions); the right object
    is the full g-function at T5 price. MF instructed not to downgrade
    MF-1(c) when no σ-form materializes.

---

## §5 Merged-lemma register

| # | lemma / program | owner seats (division recorded in seat files) | status | effort | single gating item |
|---|---|---|---|---|---|
| 1 | **M-1/M-A First-Order Response Law** (§2(d)) | LG + QC + MF (charts); HA/T4(i) engine; REN dressing; PT certifies; DG/T3 consumes | Statement amended (coherence clause); four-instrument measured; two-seat replicated | Statement: days; proof rides T4(i) (weeks) | The three-L ensemble battery (= C-6 run): intercept drift beyond ±0.3 kills B-is-local; slope off [0.85, 1.05] kills κ = 1 + o(1) |
| 2 | **M-2 Screened deficit energy** (mid-range constants; b = 3/2 ⟺ 3/π² adjudication) | LG (equilibrium) + FB (constrained-sweep formulation) + REN (crossover integration); RH consumes as A′-input | Entry gate ALREADY FIRED NO (FB-T2): frozen sums inadmissible; must go through the constrained-equilibrium g-function (Merge-A lower lane) | Months | LG's pre-committed kill band: derived screening fraction outside [0.09, 0.13] of the full additive reference (b outside [1.2, 1.75]) kills b = 3/2 |
| 3 | **The w∞ theorem / Merge A** (§2(a)) | FB owner; RH (BKMM/dictionary), REN (flow/κ-family), QC (transition order) co; QX observer; DG data | Layer 0 DONE (theorem tier); mechanism = the 60–90-day slot with three routes to one statement | (I) writable in days; (II) months | RH's mandatory AP-dichotomy calibration of the BKMM transplant — one day, kill-or-live, runs before any hard analysis |
| 4 | **Marginal-Kernel Theorem, four-coordinate form** (qx-M1 = REN Merge B) | HA/T4(i) engine; corollary owners: LG (low-pass + ζ prime-sum), REN (flow/L-invariance), QC (charge + intercept), QX (zero-grading calibration) | Kernel measured by four instruments; Hessian unresolved | Weeks on top of T4(i) | T4(i) on paper; the block-size scan (REN + LG, one afternoon) for the Hessian |
| 5 | **π²/2 by the surviving roads** (RH Merge B, road 1 closed) | HA owner of record (T4); RH (one-node Schlesinger/parametrix + the promised π²-vs-π²/2 parity audit, half page); LG (regime of validity); FB (via re-optimized sweep only) | Road (1) potential-gap DEAD (FB-T2); roads (2)–(3) carry | Weeks–months | NA's P3 closure test (> 40% failure kills); κ = 1 coefficient off π²/2 by > 10% kills grading-universality |
| 6 | **κ-lab ladder** (REN Merge A) | REN (family design; endpoint formula DONE) + FB (Dragnev–Saff proof at general κ; FB-5 five-line capacity corollary DELIVERED: A_κ = (1+κ)^{1/κ}T*) + RH (κ = 1 parametrix, easier first case) + QC (Selberg memo) + LG (ensemble variant) | FB-5 THEOREM (calculus tier); scans pre-registered | Scan: half a day; κ = 1 proof attempt: weeks–months | REN's pre-registered κ = 1 scan: plateau off π²/2 by > 10% (drift-controlled) kills R3(ii) universality; endpoint ≠ 2T* ± 10% kills balayage semantics beyond κ → 0 |
| 7 | **Stopped-chirp constructive bound** (MF M1, = RH-1(a) + REN R2(i) merged) | MF (function family, anchor/mass ledger line 2, node-transport error budget) + RH (Fuchs normalization + edge parametrices, lines 1/4) + FB (line 3, w∞ pasting algebra; design revision: registration stops ≈ 2T*) | Ledger pre-committed (MF R2.2.2); pilot sized | Pilot 2–4 days; paper bound weeks–months | The L = 4.75 pilot: rate off 4π by > 5% kills the w∞-frozen form; A′_constr < 15 reopens Q1 bias at the constant level |
| 8 | **Slit-plane K₀** (qx-QC-3(i)) | FB (declared next action, R2.6) + QX; HA consulted | Designed; mission re-scoped to "locate κ* ∈ (e^{w∞}, e²]" | 2–4 days paper-grade | None — self-deciding; kill: K₀ ≥ e²(1−o(1)) means the disk wasn't lossy (clean negative); K₀ < 3.4 contradicts data ⇒ setup bug |
| 9 | **Template calculus + corner extension** (PT M1) | PT (calculus definitions, semantic wall, clauses 1/4) + FB (clauses 2/3, Wiener–Hopf) + NT (F6 data) + NA (adversary search) | Spec co-signed (§2(c)); countermodel route concrete | Definitional section + (a): 2–4 weeks PT-side; (b) on FB's ladder | PT R2.6-T2 dual-band falsifier (both halves pre-committed) |
| 10 | **Impossibility wing** (PT M2) | PT (Floor Witness + framing note) + QX (qx-QC-2 math); Lean track executes; CS reviews sizes | qx-QC-2 SHIPPED (anchor_collapse, §6); Floor Witness IN BUILD | ≤ 11 pd total; remainder ≈ 4–8 pd | Floor Witness bands (PT R2.6-T1); kill = program-level alarm if the rational Rayleigh value lands above 1e−20 |
| 11 | **Stable-polynomial summation formula** (qx-M2) | QX (FQ/Kurasov–Sarnak framing + ACV caveat) + MF (Krein/moment note) + AG data; Lean prices (~100 lines) | Blocked behind C-8 residue (2209.04658 full read) | Two-page note + light Lean | MF's Suzuki diligence completes first (days) |
| 12 | **M-B Evanescent-Action Extraction** | QC (bookkeeping) + RH (g-function predictions) + DG executes on stored vectors (no new eigensolves) | Protocol fixed, bands pre-registered (slope within 20% of 2π(1−τ); evanescent share 0.7–0.9; T*-layer width report-don't-gate) | Days of extraction | Mid-band slope off > 20% after basis-bias control kills the per-cell action reading at operator level |

---

## §6 Lean ledger

**Cashed by this panel:**

1. **`anchor_collapse` + `anchor_collapse_of_deep` — DONE, audited.**
   `lean/glide/Glide/HardHorizon.lean` (the QC-2 block, ≈ lines 1495–1588;
   zero sorries in the file), implemented to QX's R2.2-C9 spec: Hypothesis A
   dropped entirely (`by_cases` on F(x₀) = 0), conclusion bounds ‖F(x₀)‖ for
   every |x₀| ≤ 2π; the deep form prices de-anchoring at
   exp(B₀ + 2R(2a+1+δ) − 2δe^{2a+2}) — anchor mass dies at 2e²δ·e^{2a},
   the envelope's own super-exponential scale (2e² = 14.78 vs 4π = 12.57).
   Axioms remain the three standard ones. This is the panel's first new
   kernel-checked analytic theorem: T1′ in annihilating-pair form, supplying
   clause (3) of the C-2 three-height picture and the quantitative target
   for T1PRIME Gap 1 (compose with a mass-location lemma), and PT-4's second
   RCA₀-grade analytic artifact.
2. **Floor Witness — IN BUILD** (weilcert; PT's dispatch spec R2.2): the
   kernel-checked statement that no sound 1e−20-ball certificate exists at
   L = 711/200 (M = A − δ·ssᵀ rank-one adversary; one exact-ℚ inequality on
   a 40×40 form). Success bands pre-registered (PT R2.6-T1: rational
   Rayleigh-per-coherence in [3.5, 5.5]×10⁻²¹ reproducing Q5's
   δ* = 4.489×10⁻²¹; headroom ≥ 1.8×; coherence oracle vs certified
   enclosure). Pre-committed alarm: a value above 1e−20 means Q5's settled
   number is wrong — report to coordinator before anything ships. To the
   panel's knowledge, the first kernel-checked proof-complexity lower-bound
   artifact for a live open-problem proof family.

**Ranked remaining queue (PT's C-9 ranking with colloquium updates):**

1. Floor Witness completion + audit (3–6 pd; the running item).
2. PT-1 F(i).0 de-risk (3–6 pd): pin FormalizedFormalLogic/Foundation
   against a compatible mathlib; audit its Σ₁-completeness statement form —
   BEFORE committing the 110–215 pd Tier-1 map. Kill criteria K-a/K-b/K-c
   recorded in PT §2.
3. HardHorizon K₀ tightening — a light edit per qx-QC-2's precedent, IF the
   slit-plane computation lands K₀ < e² (conditional; rides item 8 of §5).
4. qx-M2 stable-polynomial artifact (~100 lines, CertFramework format) —
   after the Suzuki diligence residue clears.
5. PT-1 Tier 1 full build (110–215 pd Foundation-assisted): scheduled
   workstream, not a panel task; pacing item F(i).1 (certified ζ evaluator,
   60–120 pd) doubles as the program's formal disproof-receiver — the
   strongest program-internal reason to build it.
6. Standing offer (PT B3): the T4(i) secular-identity certification lane
   opens the quarter its paper proof lands (extraction-friendly per LG's
   R2.1(f) audit: finite-dimensional linear algebra + explicit integrals;
   caveat — the second-order bias term is measured-only).

Toolchain topology (PT U3): three independent projects (glide / weilcert /
PT-1-with-Foundation) — no shared build risk.

---

## §7 Data corrections the panel owes the program docs

1. **T1PRIME.md — the stopping-height clauses are about ACTION heights, not
   vanishing heights.** Affected text: §0 (the "eleven measured stopping
   heights … all in T_s/T* ∈ [3.14, 3.41] ⊂ (e, e²)" clause, ~lines 35–36),
   §2 (~lines 140–141, "stopping heights sit in (e, e²)"), and §6 "Data
   consistency" (the V7 block, ~lines 392–420). Correction (FB R2.2(c),
   from C-11 F1): w_E2 heights are action-bookkeeping heights; the
   minimizer's actual registration (vanishing) terminates at ≈ 1.9T* — far
   below eT*. The consistency clause should read: action heights in (e, e²)
   say only that registration ends well inside the variational horizon
   (trivially consistent with T1′); the genuinely feasibility-flavored
   measured number is the registration endpoint ≈ e^{0.62}T*. The observed
   w_E2 drift toward 3.59 is bookkeeping convergence under the cap, NOT
   feasibility saturation — it is no longer evidence for the horizon merger.
2. **ENVELOPE.md §2b (and the twin passage in results/RESULTS.md, "The
   mechanism experiment" section) — the Poisson number is one seed, half of
   it realized charge.** Replace "Poisson costs 1.5–2 orders" with the
   decomposition (QC §5R + LG §5.4/C-6, co-signed): "Poisson: charge-matched
   intrinsic cost ≈ 1–2 orders [competing pre-registered bands: LG
   +3.5 ± 1.5 nats, QC 2.0–3.2 — the joint battery adjudicates], one-sided
   deficit-amplified (no affine law beyond sup|δN| ≈ 2–3; surpluses
   non-refunding), PLUS realized-charge scatter of ±2–3 orders; the recorded
   1.5–2-order number was one seed (7), roughly half of it that seed's
   realized charge (I_w ≈ −1.9 to −2.7)." Add the ζ row as measured:
   I_w(ζ) = +0.07 / +0.07 / +0.11 at L = 2.485/2.996/3.555 — worth-neutral
   to ~0.1 nats, spectral-gap mechanism cited for uniformity. Adopt the
   joint charge-matched protocol (QC R2.2 steps 1–7 + LG's three riders) as
   the §2b measurement standard. T3's Poisson corollary simultaneously
   adopts the one-sided sup-DEFICIT hypothesis.
3. **results/agent-deep-windows.md — the L = 4.60 limit of record.** The
   quoted Aitken 2.336e−43 (computed pre-final) is superseded: with the
   landed m = 160 rung the Aitken limit is ≈ 2.100e−43 (staircase descent
   continued, exactly as SYNTHESIS Q1 warned), and the 4π-pinned p moves
   from 4.93 to 4.81–4.92 across variants (RH §5 — same conclusion, updated
   center). Any downstream table quoting 2.336e−43 or p = 4.93 should be
   updated with a pointer to results/ias/riemann-hilbert/extract_constants.out.
4. **Instrument protocol — the m = 48 wrong-sign warning for structured
   configurations.** RESULTS.md's model_zeros protocol section and every
   future ensemble/configuration battery: structured or coherent
   configurations at L ≥ 3 can be off by 3+ nats WITH THE WRONG SIGN at
   m = 48 (LG F3: CTRL at L = 3.555 swung −1.74 → +0.22 between m = 48 and
   64); single-rung m = 48 readings of structured configs are unreliable
   below |ΔE| ≈ 2; an m-ladder (48/64/80) is required. Random (CUE/Poisson)
   configurations showed no such transients.
5. *(Wording-level, same authority)* PROGRAM.md §2.17 / ENVELOPE.md: the
   slogan "the zeros sit at the maximally-rigid offset" should be restated
   as "the worth-neutral (charge-neutral at every L, spectrally gapped)
   offset" — three seats (MF dial consequence 3, LG Track-E amendment, REN
   R2.4-3) killed the λ-extremizer reading; and LG's suggested citation of
   Ghosh's completeness circle belongs in ENVELOPE.md's next revision.

---

## §8 Convergence assessment and the Round-3 question

**Are any C-items genuinely CONTESTED?** No. The full accounting: C-1, C-2,
C-4, C-7, C-8, C-10, C-11 are SETTLED (two with amendments the owning seats
co-signed in writing); C-9 is settled and half-executed; C-3 is PENDING-DATA
with the scoring rule pre-committed and the rung literally computing; C-5
and C-6 are settled as adjudications with their confirming runs scheduled
and their interpretation bands pre-registered. The disagreements that
survive are not contested claims but PRICED PRIORS attached to named
experiments: the horizon-merger residue (FB ≤ 0.15 / QX 0.10 / RH 0.4 —
decided by the slit-plane computation and the BM-window test, both
designed); p = 9/2 vs π²/2 (decided by the m ≥ 208 ladder, with LG's third
possibility on record); REN's 60/40 wager on family-dependence of p (decided
by one deep family ladder); LG's +3.5 ± 1.5 vs QC's 2.0–3.2 Poisson band
(decided by the joint battery). In every case the parties have agreed on the
decider AND pre-committed to what each outcome means. That is convergence in
the only sense that matters.

**Is the marginal information of another all-hands round positive?** Round 2
was expensive and paid: it produced four co-signed artifacts, two
independent replications (the response law at 1% slope; the BKMM
identification under independence), five KILLED-OWN-MODEL events, the
coherence amendment, and two kernel-checked artifacts moving. But its
mechanism was seats reading each other's DATA. There is no new data until
the queued executions land — a Round 3 held now would be seats re-deriving
each other's context at cost, with nothing to adjudicate that is not already
wired to a pre-registered decider. The remaining work is uniformly
executor-shaped: proofs (T4(i), the Dragnev–Saff layer, Wiener–Hopf jet
bounds, the AP-dichotomy calibration), computations (deep rungs, ensemble
battery, Gcut escalation, κ = 1 scan, slit-plane, stopped-chirp pilot,
ψ-packet search), and Lean (Floor Witness, F(i).0).

**Recommendation: no Round 3. Panel converged; further iteration is
execution, not harmonization.** That is the honest and direct answer to the
repository owner's stopping criterion: convergence has been reached on every
item that discussion could settle, and most of the extractable information
has been squeezed — what remains is scheduled, owned, and pre-scored.
Reconvening is warranted only as targeted pairs on trigger events, each of
which already has named consumers and a pre-committed reading (so even then,
written adjudication by the owning seats suffices; no all-hands needed).

**Ranked executor assignments** (owner; size; what it closes):

1. **Land the L = 5.50, m = 208 rung (running) and, unless the kill fires,
   the m = 224 companion** (deep-windows agent; ~35–50 min each; RH scores
   under the pre-registered rule) — closes C-3, kills or spares the two
   quarantined numerology items, discharges QC's sharpest Fredholm test.
2. **The joint three-L ensemble battery = the C-6 protocol run** (LG owns,
   QC joint; ~85 eigensolves, 45–60 min + writeup, m-ladder rider) — closes
   C-6, adjudicates the two Poisson bands, runs M-1's intercept-drift and
   Var-J falsifiers, delivers the ENVELOPE §2b rewrite of §7 item 2.
3. **Finish the Floor Witness** (Lean track; 3–6 pd; bands PT R2.6-T1) —
   completes the impossibility wing's second artifact.
4. **The Q3 Gcut escalation** (law-theory exact-Bessel builder; cheap;
   Gcut = 840/1680/3360, m = 64) — formally closes C-5's anomaly under the
   joint LG+QC prediction (collapse to ≤ 0.4–0.5 nats), or triggers the
   pre-committed second-order investigation.
5. **The stopped-chirp pilot at L = 4.75 with the pre-committed ledger**
   (MF, with RH/FB lines; 2–4 days) — adjudicates C-3 from above (real
   structure vs RR bias), doubles as REN R2(i)'s kill test and M-1(§5-7)'s
   gate.
6. **The slit-plane K₀ computation + the BM-window anchored-dodger test**
   (FB, QX; 2–4 days + ≤ 30 min) — retires the merger residue either way;
   possibly tightens HardHorizon (Lean queue item 3).
7. **The κ = 1 marginal-worth scan** (REN; half a day; pre-registered
   P1/P2/P3 + kill) — the sharpest open edge of C-4 (π²/2
   grading-universality); hands T4 its solvable first case.
8. **The program-doc corrections of §7** (repo owner / coordinator; hours)
   — T1PRIME action-height restatement, ENVELOPE §2b, deep-windows L = 4.60,
   the m-ladder protocol line, the worth-neutral wording.
9. **The PT-2 ψ-packet countermodel + 𝒯+jet adversary search** (NA/NT under
   PT M1; pre-registered dual bands) — turns F5 into semantic unprovability
   and tests the corner axiom's sufficiency.
10. **Paper-track ignitions** (weeks-to-months, in parallel): T4(i) secular
    identity (HA + RH roads 2–3, including RH's promised π²-vs-π²/2 parity
    audit); FB-1's Dragnev–Saff layer + the κ-family generalization;
    the corner-corrected F4 (FB, Merge B′ item 2); PT-1's F(i).0 de-risk;
    MF's 2209.04658 full read (unblocks qx-M2 and the MF-1 bridging remark).

One standing instruction carried forward from the panel's own discipline:
items 1, 2, 4, 6, and 7 all have pre-registered outcome bands written by the
seats that stand to lose — score against those bands, unedited, in the
seats' files, exactly as both rounds did.

*— Moderator, 2026-07-26.*
