# Publication portfolio

Status: conservative consolidation, 2026-08-05.

This file is the publication-facing index for the repository.  It separates
results that are ready to communicate from results that are merely promising,
and it states the strongest claim that the present artifacts support.  It does
not claim a proof of the Riemann Hypothesis.

The detailed paper plans are in
[`publication/MANUSCRIPT-BRIEFS.md`](publication/MANUSCRIPT-BRIEFS.md), and the
release gate is in
[`publication/REFEREE-CHECKLIST.md`](publication/REFEREE-CHECKLIST.md).
The governing proof policy is
[`publication/PROOF-STANDARD.md`](publication/PROOF-STANDARD.md).  Negative
results must use the canonical scopes and debt states in
[`NO-GO-ATLAS.md`](NO-GO-ATLAS.md).
The first adversarial audit and disposition table is
[`publication/NO-GO-REFEREE-RESPONSE.md`](publication/NO-GO-REFEREE-RESPONSE.md).

## 1. Claim vocabulary

Every public claim should use one of these labels.

- **Lean theorem:** checked by Lean with only the standard axioms printed by
  the relevant audit file.
- **analytic theorem:** a conventional proof is present, but the complete
  statement has not been checked by Lean.
- **computer-assisted theorem:** the conclusion depends on the stated
  interval-arithmetic, analytic, and software trust base.
- **literature-conditional theorem:** a Lean implication whose decisive input
  is an explicit axiom imported from the mathematical literature.
- **diagnostic:** exact or numerical evidence that is not itself a theorem
  about the infinite object.
- **proposal:** a research direction, not a result.

In particular, “formalized” must never be used for a theorem whose conclusion
still depends on a `*Literature` axiom unless that dependence is stated in the
same sentence.

## 2. Ranked portfolio

The rank measures readiness and distinctiveness, not importance to RH.

| Rank | Result | Supported public claim | Present state | Decisive next action |
|---:|---|---|---|---|
| 1 | Correction to Endo's hybrid joint limit | The recorded phase and random Dirichlet series require a coordinate inversion; a one-prime mixed moment separates the published and corrected laws.  The marginal/support conclusions survive after the stated repair. | Analytic correction with an explicit page-by-page repair | Send privately to Endo; obtain author confirmation and coordinate a revised version or corrigendum |
| 2 | Anchored Jensen horizon (internally “Hard Horizon”) | A normalized compactly supported transform satisfying the stated anchor and zero-count rigidity cannot vanish on the prescribed symmetric frequency head beyond the explicit `e^(2+eps*) T*` horizon; a selected-radius residual Jensen-mass bound is also checked. | Referee-style proof and complete Lean theorem for the abstract staircase statement and raw residual bound | Independent mathematical review; use a neutral title, do not claim the `e^2` factor is sharp, and keep the zeta specialization conditional on explicit zero-counting input |
| 3 | Finite simple-pole residue infrastructure in Lean | Circle and rectangle formulas for finitely many prescribed simple poles, via simultaneous removal of their principal parts | Lean theorem package; focused reusable audit passes | Extract `SimplePole.lean`, compare against current mathlib, then upstream the minimal API before the rectangle layer |
| 4 | Fixed-window arithmetic Weil positivity | At `a=7/16` (`L=7/4` in the program's support convention), the explicitly defined arithmetic Weil form has the checked strict lower bound on its full logarithmic form domain | Lean endpoint plus generated exact certificate; the zero-sum Guinand--Weil identification remains a literature axiom | Freeze a reproducible certificate bundle and write a formal-methods paper whose title and abstract say “arithmetic form,” not “zeta-zero sum” |
| 5 | Digamma/Gauss-kernel formalization | General digamma-difference series, derivative bridge, and positive vertical-line Gauss integral in Lean | Reusable Lean package; focused audit passes | Rebase, check overlap, minimize imports, and split the general series and integral into review-sized mathlib contributions |
| 6 | Legendre `L2` and certificate infrastructure | Complete Legendre bases on arbitrary intervals, Parseval/projection formulas, exact plane-wave coefficients, and generic exact `LDL^T`/two-block positivity certificates | Reusable Lean packages; focused audit passes | Separate the basis theory from the certificate algebra and add examples independent of the RH application |
| 7 | Effective Glide refinement | The known support-dependent variational margin admits an explicit logarithmic continuity modulus and a quantitative prime-threshold turn-on estimate | Analytic theorem with substantial Lean scaffolding; attainment, Galerkin convergence, monotonicity, and qualitative continuity all have prior art | Bundle only the exact quantitative refinement into the local-Weil/formalization paper and formalize the modulus end-to-end |
| 8 | Static Mobius boundary-exchange no-go | Every fixed scale-compatible summable dictionary of the stated sign-reversing prime templates leaves a positive-density set untouched; bounded-incidence hypertemplates are included | Analytic proof, explicit density-tail lemma, and computations; plausible modest novelty | Obtain independent review, retain an exhaustive certificate for finite counterexamples, and compare carefully with convergent-multiple-set density theory |
| 9 | Topology loss for finite Euler phases | The two canonical finite-prime phase models are null-homotopic; the literal shifted quotient is unbounded in `B^2`; the normalized right phase is `B^2`-Cauchy but not uniformly Cauchy in the relevant strip | Analytic synthesis; Lean currently checks only quartet algebra and finite local contraction | Formalize the `B^2` identities and Kronecker nonuniformity, and state a theorem about these two models rather than a universal arithmetic-index no-go |
| 10 | Semilocal trace/polarization obstructions | Every fixed finite-prime pole-zero multiplier is indefinite on sufficiently large compact supports; positive trace cannot simultaneously encode the required mixed-term cancellation and the positive polarization in the stated finite models | Analytic theorems and exact finite algebra | Combine only the nontrivial fixed-place theorem and sharp finite hypotheses into a short obstruction note; present elementary trace lemmas as support, not headline results |

### Formal-library contributions that are worthwhile without a paper

These are classical mathematics but meaningful additions to Lean/mathlib:

- compact-support Fourier--Laplace entirety and exponential-type bounds;
- real-line autocorrelation/Wiener--Khinchin with the exact normalization;
- quantitative two-sided smooth cutoffs;
- arbitrary-interval Legendre Hilbert bases and projection error identities;
- generic exact positivity certificates and optimal two-block coercivity;
- finite simultaneous simple-pole removal and contour formulas;
- the digamma difference and Gauss vertical kernel chain.

The extraction map is maintained in [`lean/UPSTREAMING.md`](lean/UPSTREAMING.md).
These should be submitted as small independent units, not as one RH-themed PR.

### Secondary formalization and software artifacts

- [`lean/weilcert/CurveCertE5.lean`](lean/weilcert/CurveCertE5.lean) checks
  finite-field point counts, Frobenius recurrences, Gram-matrix positivity,
  Cayley--Hamilton kernel vectors, and a sign-flip witness.  It is suitable as
  a formalization-paper example after the paper-side Rosati/Parseval--Zak
  identification is supplied.  Its header now states that boundary explicitly.
- [`lean/run_p2_kernel_checks.py`](lean/run_p2_kernel_checks.py) is reusable
  verification engineering: dependency fingerprints, stale-artifact
  rejection, resumable JSONL logs, time/RSS capture, process-group cleanup,
  and bounded parallelism.  It supports the certificate paper but is not a
  mathematical result.
- The software-certified endpoints through `L=749/250` belong as successive
  case studies in the local-Weil paper.  They should not be split into three
  nominally distinct publications.
- The logarithmic-derivative and contour scaffold around Guinand--Weil is
  substantial formal infrastructure, but the central zero-sum formula remains
  a `GuinandWeilLiterature` axiom.  It becomes a headline result only after
  that axiom is eliminated.

### Literature calibration behind the ranking

- The Hard Horizon mechanism is a quantitative Jensen argument in a
  Paley--Wiener space.  The closest located work includes point-normalized
  Jensen constraints in [Brevig--Chirre--Ortega-Cerda--Seip](https://arxiv.org/abs/2210.13922)
  and prescribed-zero Paley--Wiener spaces in
  [Burnol](https://arxiv.org/abs/1008.0617).  No exact predecessor for the
  displayed constants was located, which is evidence for a cautious
  “plausibly new as stated,” not proof of priority.
- Connes--Consani--Moscovici already establish the relevant spectral
  attainment/Galerkin/monotonicity results in
  [*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755), while
  [Suzuki](https://arxiv.org/abs/2606.09096) proves qualitative continuity.
  Only the explicit modulus and threshold estimate are retained as possible
  Glide novelty.
- Current mathlib exposes a substantial
  [Cauchy-integral layer](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Analysis/Complex/CauchyIntegral.lean),
  while active draft PRs develop
  [isolated-singularity and residue infrastructure](https://github.com/leanprover-community/mathlib4/pull/29588)
  and a
  [rectangle residue theorem](https://github.com/leanprover-community/mathlib4/pull/39232).
  The project's finite simultaneous simple-principal-part regularization may
  complement that work after the upstream API stabilizes; the rectangle
  theorem itself must not be presented as an independent novelty claim.
  Residue theory has also been formalized in Isabelle/HOL by
  [Li--Paulson](https://doi.org/10.1007/978-3-319-43144-4_15).

## 3. Exact artifact map

### A. Endo correction

- Mathematical note:
  [`results/ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md`](results/ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md)
- External object audited: Kenta Endo, *Limit theorem for the hybrid joint
  universality theorem on zeta and L-functions*, arXiv:2410.17575v1.
- Central witness:
  `E[omega(p) phi_X(s,conjugate(omega))]` equals the `p`-th coefficient,
  whereas the same-phase expectation is zero.
- Nonclaim: this correction does not supply a new RH mechanism.

### B. Hard Horizon

- Paper proof: [`results/experts/T1PRIME.md`](results/experts/T1PRIME.md)
- Lean proof: [`lean/glide/Glide/HardHorizon.lean`](lean/glide/Glide/HardHorizon.lean)
- Focused axiom audit:
  [`lean/glide/Glide/HardHorizonAudit.lean`](lean/glide/Glide/HardHorizonAudit.lean)
- Lean endpoints: `HardHorizon.hard_horizon`,
  `HardHorizon.hard_horizon_of_global_orders`, and
  `HardHorizon.zero_desert`.
- Nonclaim: the anchor is essential; the stronger paper-side zero-desert
  extraction is not identical to the Lean raw-bound theorem; and the zeta
  corollary still imports an explicit Riemann--von Mangoldt error estimate and
  a rigorous first-zero input outside this Lean theorem.  A release should
  compare the constants with the newer explicit estimate of
  [Bellotti--Wong](https://arxiv.org/abs/2412.15470).

### C. Local arithmetic Weil endpoint

- Definitions and specialization:
  [`lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean`](lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean)
- Certificate endpoint:
  [`lean/rhbridge/RHBridge/P2RoundedBoundedCertificateCheck.lean`](lean/rhbridge/RHBridge/P2RoundedBoundedCertificateCheck.lean)
- Zero-side assumption boundary:
  [`lean/rhbridge/RHBridge/GuinandWeilLiterature.lean`](lean/rhbridge/RHBridge/GuinandWeilLiterature.lean)
- Computer-assisted larger endpoints: [`THEOREMS.md`](THEOREMS.md)
- Nonclaim: no all-support positivity, no exclusion of an off-line zero, and no
  end-to-end Lean proof of the Guinand--Weil equality.

### D. Formal analysis infrastructure

- Residues:
  [`lean/rhbridge/RHBridge/SimplePole.lean`](lean/rhbridge/RHBridge/SimplePole.lean),
  [`lean/rhbridge/RHBridge/ComplexResidue.lean`](lean/rhbridge/RHBridge/ComplexResidue.lean)
- Digamma:
  [`lean/glide/Glide/DigammaSeries.lean`](lean/glide/Glide/DigammaSeries.lean),
  [`lean/glide/Glide/DigammaKernel.lean`](lean/glide/Glide/DigammaKernel.lean)
- Legendre:
  [`lean/weilcert/LegendreIntervalL2.lean`](lean/weilcert/LegendreIntervalL2.lean),
  [`lean/weilcert/LegendrePlaneWaveL2.lean`](lean/weilcert/LegendrePlaneWaveL2.lean)
- Certificates:
  [`lean/weilcert/CertFramework.lean`](lean/weilcert/CertFramework.lean),
  [`lean/weilcert/FullInfTransfer.lean`](lean/weilcert/FullInfTransfer.lean)
- Harmonic analysis:
  [`lean/rhbridge/RHBridge/AutocorrelationPlancherelCore.lean`](lean/rhbridge/RHBridge/AutocorrelationPlancherelCore.lean),
  [`lean/glide/Glide/CompactSupportFourierLaplace.lean`](lean/glide/Glide/CompactSupportFourierLaplace.lean),
  [`lean/rhbridge/RHBridge/SmoothCutoff.lean`](lean/rhbridge/RHBridge/SmoothCutoff.lean)

### E. Negative and structural results

- Static Mobius matching:
  [`results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md`](results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md)
- Phase topology:
  [`results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md)
- Semilocal trace/polarization:
  [`results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`](results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md)
- Higher-differential and finite-polarization formal no-gos:
  [`lean/rhbridge/RHBridge/CompletedIncidenceComplexNoGo.lean`](lean/rhbridge/RHBridge/CompletedIncidenceComplexNoGo.lean),
  [`lean/rhbridge/RHBridge/FinitePolarizationNoGo.lean`](lean/rhbridge/RHBridge/FinitePolarizationNoGo.lean)

## 4. Results that are supporting lemmas, not standalone publications

The following are useful and should be retained, but novelty should not be
manufactured around them:

- the equivalence between a positive metric satisfying `A*G+GA=G` and a
  diagonalizable finite operator with spectrum on the critical line;
- degree-zero Hodge energy being independent of later differentials;
- finite Euler-factor null-homotopy by radial contraction;
- the elementary Mobius/fugacity polynomial identities by themselves;
- finite Galerkin scans, Lee--Yang moment scans, and prime-event experiments;
- restatements of Weil, Li, Nyman--Beurling, or Guinand--Weil equivalences;
- any theorem whose decisive conclusion is still a project-specific axiom in
  `Stage3*`, `Stage4*`, or `SuzukiClosedDomainLiterature`.

These belong in appendices, regression suites, or the negative-results
ledger.  They should not be advertised as RH progress.

## 5. Validation snapshot

On 2026-08-05 the three focused reusable audits built successfully:

```text
lake build Glide.UpstreamAudit
lake build Glide.HardHorizonAudit
lake build Weilcert.UpstreamAudit
lake build RHBridge.ReusableAudit
```

The audited declarations report only standard Lean axioms.  A broad
`RHBridge` replay was intentionally stopped after it began regenerating the
large certificate corpus; focused builds are the supported verification path
on memory-constrained machines.  See the checklist for the release protocol.

The new `Glide.HardHorizonAudit` target also builds and reports only
`propext`, `Classical.choice`, and `Quot.sound` for every advertised endpoint.
The comment/header cleanup of `CurveCertE5` was checked with the focused
`lake build CurveCertE5` target.

The Python unit tests can now be collected from the repository root through
`pytest.ini`; they test exact helper logic and regressions, not the analytic
theorems themselves.  `requirements.txt` and `requirements-test.txt` record
the supported dependency ranges; an exact archival lock remains a release
task for each heavy certificate artifact.  The current snapshot passes all 18
root tests and all four dedicated kernel-runner cleanup tests.

An independent serialized replay of the Stage-3 boundary/parity,
Hodge-low-sector, completed-incidence, finite-polarization, and quantized-phase
audit files also reported only `propext`, `Classical.choice`, and `Quot.sound`.
The new prime-edge audit and the existing global-Mobius audit report the same.
These checks validate only their exact Lean declarations, not the analytic
convergence or zeta-specific interpretations in the reports.  Cold focused
processes initially measured between roughly 2.3 and 6.3 GB RSS.  After the
five broad no-go imports were minimized, their replay peaks fell to roughly
1.5--2.4 GB; the remaining focused audits were measured around 2.3--2.7 GB.
They should still run serially, and umbrella builds are not supported as
routine checks on a memory-constrained host.  A clean-checkout replay of the
frozen commit remains a release task.

## 6. What the consolidation teaches

Nearly every attempted RH route can be evaluated by a three-part test.

1. **Carrier:** identify data that changes under insertion of one arbitrarily
   high off-critical functional-equation quartet.
2. **Topology:** construct the arithmetic object and its all-prime/all-height
   limit in a topology that preserves that carrier.
3. **Engine:** prove, from arithmetic input independent of the zeros, that the
   carrier has its RH-compatible value.

Most failed routes possess at most two parts.  Weil inertia has a carrier and
a meaningful topology but lacks the positivity engine.  Finite Euler phases
have an arithmetic construction and a harmless finite topology but lose the
carrier in the available limit.  Argument-principle windings have the carrier
and integer stability, but their “computation” is zero counting itself.

A second invariant lesson is that **equality and order are different
structures**.  Trace formulas, Poisson summation, functional equations, and
connected logarithms explain exact cancellation.  A positive polarization,
contractive evolution, or comparison principle is additional data.  Trying
to force one positive trace to perform both jobs caused several finite no-go
theorems.

A third lesson is that **completion is the theorem**.  Finite positive
windows, finite Euler factors, self-adjoint approximants, or local matching
rules do not constrain a remote exceptional zero unless the limiting topology
prevents escape.  The gamma factor, poles, counterterms, and domain cannot be
added after a local sign argument.

## 7. New research intuition

The most coherent new candidate is a **relative anomaly index**, not an
absolute finite-Euler winding.  Finite local phases are contractible, but the
failure of their contractions to converge uniformly may define a relative
class between two trivializations: an arithmetic prime--gamma
renormalization and an analytic completed-function trivialization.  Such a
class would have to satisfy all of the following before receiving any RH
credit:

- be defined without locating or counting zeta zeros;
- change under insertion of one remote quartet;
- exist in a topology stronger than `B^2` but attainable by completed
  prime--gamma approximants;
- have an arithmetic computation of its value;
- not reduce, after unwinding definitions, to the argument principle.

The first fail-fast calculation is to write a renormalized cocycle on the
boundary of a fixed strip and test whether its integer defect can be computed
from prime and gamma truncations with a cutoff-independent error.  If the only
proof of cutoff independence invokes the divisor of `xi`, the proposal is
circular and should be killed.

Within the Weil program, the consolidation points to a narrower control
problem: **signed eventwise spectral flow**.  New prime shells are indefinite,
so monotone positive propagation is the wrong invariant.  The prime-5 rescue
suggests tracking the Schur complement of the old negative sector as each
prime event activates.  A conserved or contractive renormalized quantity
could be meaningful; merely repeating one finite rescue is not.  The required
uniform event theorem remains RH-strength and should be stated before further
computation.

For the Mobius branch, the static theorem says that a viable cancellation
mechanism must be scale-adaptive, use unbounded prime incidence, or maintain
global matching state.  The natural next object is therefore an augmenting-
path or mass-transport invariant, not a larger dictionary of local toggles.
That is a sharply reduced search space, although it is not presently a route
with substantial RH probability.

## 8. Publication order

1. Communicate the Endo correction privately and seek a coordinated repair.
2. Extract the simple-pole and digamma units for upstream review.
3. Obtain an independent review of the Hard Horizon statement and anchor
   scope; then decide its venue.
4. Freeze the local-Weil certificate and prepare the formal-methods case
   study with the explicit-formula axiom boundary visible in the abstract.
5. Independently review the strengthened Mobius density proof and formalize the
   analytic phase-topology core before treating either as a standalone note.
6. Keep semilocal and categorical no-gos as a consolidated obstruction paper
   only if a single theorem architecture survives editorial compression.

Authorship, acknowledgements, and a `CITATION.cff` are intentionally not
invented here.  They must be supplied by the human contributors before any
public submission.
