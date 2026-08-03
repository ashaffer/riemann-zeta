# The Positivity Gate

An instrumented research program on the Riemann Hypothesis, built during intensive
July 2026 human–AI sessions. This repository packages the
program document, the instruments, and the measured results so the investigation is
resumable by anyone — human, machine, or both together.

## What this is, and is not

**It is not a proof or disproof of RH.** Nothing here claims one. Read the honesty
clauses in `PROGRAM.md` §0 and §8 first; they are the house style.

**It is:** a set of numerical and formal instruments aimed at the Weil-positivity
formulation of RH, together with finite-dimensional measurements, explicitly
conditional analytic lemmas, and a research architecture. Claims are separated into
kernel-checked algebra, computer-assisted finite matrices, computer-assisted
full-space theorems at three endpoints in successive prime-power regimes, empirical
extrapolations, and open global
statements in `results/CODEX-REVIEW.md`.

## The one-paragraph summary of what was found

RH is equivalent (Weil) to positivity of a quadratic form built from a pole term, an
archimedean term, and the primes. This repository assembles finite Galerkin matrices
for that form and cross-checks their normalization numerically. Interval software
encloses several *finite-dimensional* eigenvalues down to the 10⁻²⁰ scale, and Lean
checks exact rational/real matrix certificates once their entries are supplied. On
the analytic side, the Glide Theorem proves that the full variational margin is
attained, non-increasing, and continuous in the support length. Spectral ladders
suggest a smooth, very rapidly decaying envelope and reveal interesting prime-sign,
family, and near-kernel phenomena, but every such ladder is a Rayleigh–Ritz upper
bound. FULLINF F7–F10 now go beyond those ladders: a clipped-symbol transfer
plus FLINT-Arb integration proves the unrestricted bounds
`inf Q_(7/4)/||.||² > 2.2699e-5` and
`inf Q_(497/200)/||.||² > 9.99e-11`, and
`inf Q_(749/250)/||.||² > 9.9e-16`. Support monotonicity therefore gives
full-domain positivity for every `L <= 749/250`. These are software-certified
local Weil-positivity results, not Lean theorems about the zeta form and not
RH. At `L=7/4`, Lean now checks the Fourier/Legendre/pole/operator/F8 skeleton,
the directed p=2 digamma and multiplier bounds, the arbitrary-real finite
interval certificate, and the exact comparison of the clipped multiplier
integral with the original multiplier integral. Lean now also proves entrywise
containment of both canonical parity matrices and therefore the strict clipped
endpoint directly. Candidate rationals are generated externally, but Lean
verifies their analytic error bounds and exact finite identities. The
original-integral theorem additionally assumes natural weighted integrability.
Lean still does not identify this integral-plus-pole expression with the zeta
Weil form and its domain, cover all support sizes, or prove the proposed
zero-side converse.

## Repository layout

```
PROGRAM.md              the full research program: findings (§2.1–2.13 with all
                        numbers), target lemma (§3), six tracks (§4), milestones (§5),
                        normalization ledger (§6), related work (§7), postscript (§8)
READING.md              the reading order into the mathematics
results/RESULTS.md      every key measured number, as a regression target
results/CODEX-REVIEW.md current audit, theorem tiers, gaps, and next steps
src/weil_core.py        shared primitives: digamma, hat basis, form builders (zeta
                        and Dirichlet), fixed Kronecker symbol
src/oracle.py           the two-sided Guinand–Weil identities — RUN THIS FIRST
src/spectral_instruments.py  Riemann–Siegel scanner, census, Lehmer hunt, GUE gaps,
                        prime-side spectrum, rogue-line scan, Davenport–Heilbronn
src/model_zeros.py      RH-conditional finite-frame comparison of on-line,
                        smooth-staircase, and seeded Poisson ordinates, with
                        cutoff-safe generation and a multi-seed helper
src/margin_experiments.py    margin sweeps, basis escalation, mechanism test, pole
                        flip, Temple bounds, cascade, keyhole
src/family_experiments.py    Dirichlet cartography, twisted margins, conductor law,
                        sign ledger
src/chowla_hunt.py      high-precision numerical central values, scaled hunt, distribution fit,
                        D = 14693 lowest zero
src/hp_margins.py       the margin ladder in extended precision: exact x-space
                        archimedean kernel (no Simpson, no r-truncation), mpmath
                        eigensolve — the instrument that measured the float
                        pipeline's true error and the fate of the p >= 3 margins;
                        now conductor-aware (q, D, prime_set) for the family
src/spectral_margins.py the ladder in an orthonormal Legendre (spectral) basis:
                        Gram = I, overlaps exact by Gauss-Legendre, same x-space
                        kernel — converges past the hat wall and gives decreasing
                        finite Galerkin upper bounds for the full margin
src/certified_margins.py software interval enclosures (mpmath.iv, 220-bit):
                        exact-rational hat autocorrelation pieces, Bernoulli-
                        series kernel with rigorous tails, interval Cholesky
                        lower bounds + interval Rayleigh upper bounds — the
                        finite hat-space positivity margins under the stated trust base
src/certified_spectral.py the same certificates in the Legendre basis (exact
                        universal overlap polynomials, hinge-free): finite
                        Legendre-matrix positivity down to the 1e-20 scale
src/fullinf_class_certificate.py a conservative software-certified application
                        of FULLINF F4 to the class with L=7/4, R=50 and
                        Fourier-tail mass at most 1e-15, plus an explicit
                        degree-28 non-vacuity witness; not the unrestricted
                        infimum or an NT-4 packet certificate
src/arb_fullinf_certificate.py an independent FLINT-Arb reproduction of the
                        finite core, F4 class ledger, and exact-moment witness
src/fullinf_unrestricted_certificate.py the clipped-symbol Arb certificate and
                        F8 transfer proving the unrestricted L=7/4 lower
                        bound >2.2699e-5
src/fullinf_unrestricted_p3_certificate.py the independent 80-mode Arb driver
                        for F9, proving the unrestricted L=497/200 lower
                        bound >9.99e-11
src/fullinf_n4_scout.py fast n=4 parameter reconnaissance; its exterior-floor
                        panel check is rigorous, but its scan is explicitly
                        nonrigorous and it is not a positivity certificate
src/fullinf_unrestricted_n4_certificate.py the resumable 132-mode Arb driver
                        for F10, proving the unrestricted L=749/250 lower
                        bound >9.9e-16
results/fullinf_n4_M132_S110_entries.jsonl outward Arb checkpoint for all
                        4,422 independent n=4 band integrals
ENVELOPE.md             draft note for the frontier authors: the measured
                        envelope law, its validations, the certified ladder,
                        the family universality — NOT yet distributed
THEOREMS.md             proved statements: the Glide Theorem (margin monotone
                        + continuous through thresholds, closed form and compact
                        resolvent, explicit constants), the finite
                        machine-checked window with its Bridge Proposition,
                        and the Arb-certified unrestricted endpoints through
                        L=749/250
lean/weilcert/          Lean 4 + mathlib development: WeilCert.weil_window_positive,
                        kernel-verified (axioms: propext, Classical.choice,
                        Quot.sound; no native_decide) — exact finite matrix
                        positivity; FullInfTransfer formalizes F8's canonical
                        orthogonal-projection step. The Legendre modules now
                        formalize F2 from Rodrigues and the exact coefficient
                        through normalization, interval scaling, L² density,
                        a complete Hilbert basis, Parseval, canonical finite
                        projections, the actual zero-extension/Plancherel band
                        operator, and the exact integrated leakage bound.
                        PoleProjectionL2 proves the two exponential residuals;
                        BoundedSymbolMultiplier and FullInfP2Endpoint compose
                        the bounded real symbol, poles, 48-mode certificate,
                        complement/cross estimates, and F8 determinant;
                        LegendreParityCoordinates supplies canonical matrices,
                        and SymbolQuadraticComparison compares the clipped and
                        original weighted integrals;
                        FullInfClipped48, FullInfClipped48Real, and
                        FullInfClipped48Transfer kernel-check the exact rational
                        certificate, its strict real extension, and its
                        composition with the L=7/4 projection ledger.
                        Identification with the
                        analytic zeta form remains a separate bridge
lean/glide/Glide/       analytic Lean lemmas, including the archimedean kernel
                        sandwich, the positive trigamma series, unconditional
                        locally-uniform GammaSeq convergence and digamma
                        monotonicity, the exact p=2 exterior-symbol comparison,
                        and directed rational p=2 scalar bounds
lean/rhbridge/           cross-project p=2 composition: clipped positivity from
                        canonical matrix containment and transfer to the original
                        weighted integral plus pole term under integrability
```

## How to reproduce

Requirements: Python 3 with `numpy` and `mpmath`; the Arb certificates also
require `python-flint >= 0.9.0`. The optional n=4 scout uses SciPy. No network
is needed after installation.

1. **Run the regression oracle first (program law).** `python3 src/oracle.py` — the two-sided
   explicit-formula identities for zeta and for the mod-3/mod-4 characters. All
   downstream conventions are checked by these. This is a high-precision numerical
   cross-check, not an interval or formal certificate. Expected: differences at the
   1e-13-to-1e-29 level depending on precision settings.
2. Each other script is self-contained, has an `if __name__ == "__main__"` demo,
   and carries `EXPECTED:` comments with its measurement/audit date. A
   reproduction that matches those numbers is a regression pass; one that does not
   is either a bug (ours or yours) or a discovery — treat it as a bug until an
   independent oracle says otherwise. That rule caught three fake catastrophes here.
3. `python3 src/hp_margins.py` — the extended-precision ladder (validates the float
   pipeline against the exact x-space archimedean kernel, then re-measures the
   p = 3 window). ~1 minute; EXPECTED values in the module docstring.
4. `python3 src/spectral_margins.py` — the spectral (Legendre) ladder: unit tests,
   then the L = 1.75 and L = 2.485 ladders that pass below the hat wall. ~1 minute.
5. `python3 src/certified_margins.py` — the interval calculations: containment
   sanity, then four two-sided finite Galerkin eigenvalue enclosures (three zeta
   matrices and one chi_{-7} matrix), conditional on the stated `mpmath.iv` trust
   base. ~20 seconds. (Optional speedup for all hp/spectral
   work: `pip install gmpy2` gives mpmath a fast backend; results are identical.)
6. `python3 src/certified_spectral.py` — the spectral-basis certificates: exact
   overlap cross-checks, then certified enclosures at the 1e-10 / 1e-15 / 1e-20
   scales. ~3 minutes.
7. `python3 src/fullinf_class_certificate.py` — rebuilds the m=48 interval
   core and a closed-form tail majorant, proving `Q_(7/4) > 1.1139e-5` for every
   member of the stated frequency-tail class under the documented trust base.
   The same run certifies an explicit normalized polynomial's tail below
   `3e-17`, proving the class is nonempty. ~1 minute.
8. `python3 src/fullinf_unrestricted_certificate.py` — Arb-encloses 600 clipped
   matrix integrals, proves the clipped V₄₈ block above `2.27e-5`, and executes
   F8's two-by-two transfer to certify the unrestricted bound
   `inf Q_(7/4)/||.||² > 2.2699e-5`. About 2 minutes on the audit machine.
9. `python3 src/fullinf_unrestricted_p3_certificate.py` — independently
   encloses 1,640 clipped matrix integrals and executes the same full-space
   transfer with primes 2 and 3, certifying
   `inf Q_(497/200)/||.||² > 9.99e-11`. About 7 minutes on the audit machine.
10. `python3 -u src/fullinf_unrestricted_n4_certificate.py --workers 12` —
   loads or builds the resumable 4,422-entry Arb checkpoint, proves the
   132-mode clipped block above `1e-15`, and transfers it to
   `inf Q_(749/250)/||.||² > 9.9e-16`. The first run took 1,040 seconds on
   12 cores; a completed-checkpoint rerun performs only reconstruction and
   Cholesky. Checkpoint SHA-256:
   `7591f662b1c1a79ed83cb6999881d8face43836dec1131ccff8d56d6bdf7354f`.
   Its metadata binds the cached raw integrals to the source of the numerical
   kernel, so an integrand change fails closed instead of silently reusing it.
11. Lean verification: build `lean/glide`, `lean/weilcert`, and finally
   `lean/rhbridge` (which imports both), then run the focused axiom audits in
   `lean/README-verify.md`. Requires elan; cached rebuilds are short.

## The discipline (read this even if you read nothing else)

Every assembled positivity form must be spot-checked against the zero-side sum
2 Σ |φ̂(γ)|², computed from an independently generated on-line zero list. This is
an excellent regression oracle, but its sum-of-squares interpretation is conditional
on the relevant zeros lying on the critical line; it cannot logically veto an RH
counterexample. Any apparent negativity should first be treated as a likely
implementation bug and then adjudicated with interval bounds, explicit tails, and an
unconditional form of the explicit formula. Observed base rate in this project:
the apparent catastrophes investigated so far were implementation or test errors.

## Diligence status (be honest when citing)

- **Verified July 25, 2026 (second working day):** every EXPECTED number in this
  repository reproduces on a fresh machine, several to all printed digits; the
  |D| ≤ 1e5 hunt reproduces end-to-end; L(½, χ₁₄₆₉₃) confirms against a fully
  independent implementation. See `results/RESULTS.md`, second section. (Dateline
  note: the original documents self-date July 26; the clock on both working days
  read July 25.)
- **Re-audited July 27, 2026:** the interval suites and Lean builds pass after
  the claim-tier repairs; the committed restricted-class certificate and its
  non-vacuity witness reproduce independently in mpmath.iv and FLINT-Arb. The
  three clipped-symbol full-space certificates also pass end-to-end. Lean now also
  checks F8's scalar two-by-two determinant implication and the three exact
  rational block ledgers, while its analytic estimates and Arb bridge remain
  external. The model-zero
  audit found and fixed a silent
  180-point cutoff, so its July 27 EXPECTED table supersedes the older nominal
  Gcut=420 rows. See `results/CODEX-REVIEW.md`.
- **Lean-first update July 28, 2026:** the abstract Hilbert and canonical
  orthogonal-projection F8 transfers, F2's exact oscillatory integral model,
  sharp double-factorial bound, infinite geometric tail, all-degree Rodrigues
  formula, exact plane-wave coefficients, normalized Legendre orthonormality,
  arbitrary-interval scaling, L² completeness, Parseval, canonical projection
  tails, and the explicit pointwise leakage inequality are kernel-checked.
  Zero extension, `L¹∩L²` Fourier compatibility, the exact `z/(2π)`
  normalization, band restriction, and the rational
  `ρ≤81/10^23` endpoint leakage are now kernel-checked as well. The
  exponential pole vectors have norm at most one and 48-mode residual below
  `195/10^95`. Operator algebra derives the complement and cross blocks, and
  `FullInfP2Endpoint.projection_lower_bound_of_fourier_clipped48_p2_symbol`
  composes these with the real interval certificate and exact determinant.
  F7 is unconditional: `GammaUniform` proves locally uniform Euler GammaSeq
  convergence, hence the trigamma derivative and strict monotonicity;
  `P2Symbol` proves the actual exterior-symbol comparison. `DigammaBounds`
  proves `109387/100000 ≤ p2Alpha` and
  `|p2Omega r-p2Alpha| ≤ 7447/1000` on `|r|≤50` by exact series and rational
  tail bounds. `SymbolQuadraticComparison` proves the exact clipped-integral
  identity and its order comparison with the original, possibly unbounded,
  multiplier under the stated weighted-integrability hypothesis. The
  bounded-certificate theorem
  `RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment`
  proves the even/odd canonical matrix containments. Its immediate corollary
  `p2_canonical_clipped_endpoint` proves the strict `22699/10^9` clipped bound;
  the existing original-integral theorem transfers it to the unbounded p=2
  weighted Fourier integral plus the exact pole term under weighted
  integrability. The remaining local p=2 work is identifying that expression
  and its domain with the truncated zeta Weil form.
- **Reusable-infrastructure update August 3, 2026:** Gauss's general two-point
  digamma series and positive-vertical-line integral are now proved from the
  locally uniform Gamma sequence.  Lean also has an actual Fourier–Legendre
  Hilbert basis on every interval `[b,c]` with `b<c`, a standalone
  Fourier–Laplace entirety/growth module, finite simple-principal-part removal
  and contour sums, real-line Wiener–Khinchin identities, a quantitative smooth
  cutoff, a bundled exact `LDLᵀ` certificate, and a formally optimal scalar
  two-block lower constant.  These reusable endpoints are Apache-2.0 licensed,
  separately packaged, and axiom-audited.  This is infrastructure hardening,
  not a new RH implication.
- The Chowla-scan values are very likely recoverable from existing large computations
  (Rubinstein-era tables, LMFDB); D = 14693 is a record *of our scan*, not
  necessarily of mathematics. Still unchecked against those tables.
- **Keyhole novelty is dead** (checked July 25): arXiv:2605.20224 (Groskin, May 2026)
  already recovers zeros from the truncated form's ground state to 300+ digits.
  §2.13 is full-pipeline validation, not discovery. The Lehmer "record" is a record
  of this scan's range only — and by *normalized* gap the classic 7005.06 pair is
  the tighter one; far closer pairs are known at large height.
- Remaining plausible novelties: the sign ledger, the pole flip, the conductor
  coasting law, the safety-factor decay, and the systematic per-prime margin data —
  now including the hp ladder's findings (float-pipeline bias +0.7–0.9e−9, the p = 2
  basis-limit bracket [3.18, 3.30]e−5, the m^{−3.6} transient law, the floor-bias of
  κ). Check against Connes–Consani(–Moscovici), Suzuki, and Groskin before claiming.
- Every positive finite Galerkin value by itself is one-sided evidence for the
  full operator, not a lower bound for it. F8–F10 are different: they add a proved
  exterior floor, an orthogonal-complement band-defect bound, and a cross-block
  determinant. Their three endpoint conclusions use FLINT-Arb plus explicit
  analytic lemmas and are not yet theorems about zeta in Lean. For the p=2
  endpoint, however, the transfer machinery, scalar bounds, Fourier/pole
  constants, canonical matrix containment, and clipped endpoint are now
  kernel-checked. Only the original-integral and zeta-form steps retain explicit
  integrability/form-domain obligations.

## Where the door is

`PROGRAM.md` §3 states the intended uniform target. The passage to the complete
form domain is now closed through L=749/250. Extending positivity to every
support size,
formalizing the zeta-form/domain chain, and
proving a quantitative zero-side converse remain open; uniform closure would
be RH-strength work. The immediate local priority is the remaining
form-identification and weighted-integrability bridge at `L=7/4`, not a deeper
numerical ladder; canonical p=2 matrix containment is closed.

## Lean reuse and upstreaming

Several general-purpose results have been separated from their RH applications:
finite simple-pole residue identities, quantitative smooth cutoffs,
autocorrelation/Plancherel identities, digamma kernel formulas, arbitrary-
interval Legendre `L²` bases, and reusable certificate/coercivity lemmas.  See
[`lean/UPSTREAMING.md`](lean/UPSTREAMING.md) for their public endpoints, proof
status, and proposed small upstream-review units.

## License

Original material in this repository is released under the
[Apache License 2.0](LICENSE).  Third-party dependencies retain their own
licenses.  Named author attribution should be confirmed before any upstream
submission; the current Lean headers use the collective project attribution.
