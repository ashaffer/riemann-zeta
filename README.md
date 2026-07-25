# The Positivity Gate

An instrumented research program on the Riemann Hypothesis, built and measured in a
single day (July 26, 2026) of human–AI collaboration. This repository packages the
program document, the instruments, and the measured results so the investigation is
resumable by anyone — human, machine, or both together.

## What this is, and is not

**It is not a proof or disproof of RH.** Nothing here claims one. Read the honesty
clauses in `PROGRAM.md` §0 and §8 first; they are the house style.

**It is:** a set of cross-validated numerical instruments aimed at the Weil-positivity
formulation of RH (the frontier program of Connes–Consani–Moscovici), a body of
measurements at that frontier — several of which we believe are new, pending
diligence — and a six-track research architecture with kill criteria, milestones,
and an always-on disproof channel.

## The one-paragraph summary of what was found

RH is equivalent (Weil) to positivity of a quadratic form built from a pole term, an
archimedean (digamma) term, and the primes. Truncated to test functions of bounded
support, that form was built, certified against a two-sided explicit-formula oracle to
29 digits, and measured: positivity survives each prime-power support threshold with
margins that collapse to zero at thresholds (the "zero-slack" law, locally); each
prime's rescue obeys a verified first-order mechanism law whose sign is set by the
minimizer autocorrelation; the pole of zeta is what flips that sign and makes zeta's
primes stabilizers (the "pole flip"); for Dirichlet characters the primes split into
stabilizers and drains by character sign (the "sign ledger"); the bottom of the
spectrum is a growing near-null cascade whose vectors' Fourier transforms vanish at
the actual zeros of zeta to three decimals (the "keyhole"), so the cascade is the zeta
spectrum materializing and the missing uniform factorization *is* the Hilbert–Pólya
object. Along the way: a record-of-scan Lehmer pair (t = 17143.79), a record-of-scan Chowla
near-miss (D = 14693, L(1/2) = 0.00180, lowest zero at 5.7% of mean spacing), the symplectic
small-value law confirmed at exponent 1.50, and three fake catastrophes — including
two fake GRH disproofs — manufactured by our own pipeline and caught by the layered
oracle discipline, one per scaling step.

**Day two (July 25) in one sentence:** everything above reproduced and was then
taken past the hat-basis wall — the operator-level margins follow a single smooth
envelope, ln λ_min ≈ 10.2 − 1.755·e^{L/2}(L/2+4), across all prime windows *and*
thresholds (the threshold "knife-edge" was a basis artifact), universally in the
family Nyquist height T*_χ = (2π/q)e^{L/2} for q = 1, 3, 5, 7, with
interval-certified rungs down to the 10⁻²⁰ scale — see PROGRAM.md §2.14–2.16,
`results/RESULTS.md`, and the draft note `ENVELOPE.md`.

## Repository layout

```
PROGRAM.md              the full research program: findings (§2.1–2.13 with all
                        numbers), target lemma (§3), six tracks (§4), milestones (§5),
                        normalization ledger (§6), related work (§7), postscript (§8)
READING.md              the reading order into the mathematics
results/RESULTS.md      every key measured number, as a regression target
src/weil_core.py        shared primitives: digamma, hat basis, form builders (zeta
                        and Dirichlet), fixed Kronecker symbol
src/oracle.py           the two-sided Guinand–Weil identities — RUN THIS FIRST
src/spectral_instruments.py  Riemann–Siegel scanner, census, Lehmer hunt, GUE gaps,
                        prime-side spectrum, rogue-line scan, Davenport–Heilbronn
src/margin_experiments.py    margin sweeps, basis escalation, mechanism test, pole
                        flip, Temple bounds, cascade, keyhole
src/family_experiments.py    Dirichlet cartography, twisted margins, conductor law,
                        sign ledger
src/chowla_hunt.py      exact central values, the scaled hunt, distribution fit,
                        D = 14693 lowest zero
src/hp_margins.py       the margin ladder in extended precision: exact x-space
                        archimedean kernel (no Simpson, no r-truncation), mpmath
                        eigensolve — the instrument that measured the float
                        pipeline's true error and the fate of the p >= 3 margins;
                        now conductor-aware (q, D, prime_set) for the family
src/spectral_margins.py the ladder in an orthonormal Legendre (spectral) basis:
                        Gram = I, overlaps exact by Gauss-Legendre, same x-space
                        kernel — converges past the hat wall and measures the
                        operator-level window margins f(p) themselves
src/certified_margins.py rigorous interval enclosures (mpmath.iv, 220-bit):
                        exact-rational hat autocorrelation pieces, Bernoulli-
                        series kernel with rigorous tails, interval Cholesky
                        lower bounds + interval Rayleigh upper bounds — the
                        program's first certified window positivity margins
src/certified_spectral.py the same certificates in the Legendre basis (exact
                        universal overlap polynomials, hinge-free): certified
                        positivity down to the 1e-20 scale
ENVELOPE.md             draft note for the frontier authors: the measured
                        envelope law, its validations, the certified ladder,
                        the family universality — NOT yet distributed
THEOREMS.md             proved statements: the Glide Theorem (margin monotone
                        + continuous through thresholds, explicit constants,
                        complete proof) and the machine-checked positivity
                        window, with its Bridge Proposition
lean/weilcert/          Lean 4 + mathlib development: WeilCert.weil_window_positive,
                        kernel-verified (axioms: propext, Classical.choice,
                        Quot.sound; no native_decide) — the first formally
                        verified window of Weil positivity, at L = 497/200
                        with both primes 2 and 3 participating
```

## How to reproduce

Requirements: Python 3 with `numpy` and `mpmath`. No network needed.

1. **Certify first (program law).** `python3 src/oracle.py` — the two-sided
   explicit-formula identities for zeta and for the mod-3/mod-4 characters. All
   downstream conventions are locked by these. Expected: differences at the
   1e-13-to-1e-29 level depending on precision settings.
2. Each other script is self-contained, has an `if __name__ == "__main__"` demo,
   and carries `EXPECTED:` comments with the values measured on July 26. A
   reproduction that matches those numbers is a regression pass; one that does not
   is either a bug (ours or yours) or a discovery — treat it as a bug until an
   independent oracle says otherwise. That rule caught three fake catastrophes here.
3. `python3 src/hp_margins.py` — the extended-precision ladder (validates the float
   pipeline against the exact x-space archimedean kernel, then re-measures the
   p = 3 window). ~1 minute; EXPECTED values in the module docstring.
4. `python3 src/spectral_margins.py` — the spectral (Legendre) ladder: unit tests,
   then the L = 1.75 and L = 2.485 ladders that pass below the hat wall. ~1 minute.
5. `python3 src/certified_margins.py` — the interval certificates: containment
   sanity, then four CERTIFIED two-sided margin enclosures (three zeta windows and
   one chi_{-7} family window). ~20 seconds. (Optional speedup for all hp/spectral
   work: `pip install gmpy2` gives mpmath a fast backend; results are identical.)
6. `python3 src/certified_spectral.py` — the spectral-basis certificates: exact
   overlap cross-checks, then certified enclosures at the 1e-10 / 1e-15 / 1e-20
   scales. ~3 minutes.
7. Lean verification: `cd lean/weilcert && lake exe cache get && lake build`,
   then the axiom audit of `lean/README-verify.md`. Requires elan; ~10 s build
   after the mathlib cache.

## The discipline (read this even if you read nothing else)

Every assembled positivity form must be spot-checked against the zero-side sum
2 Σ |φ̂(γ)|², computed from an independently generated zero list. It is a sum of
squares; it cannot be negative. Any pre-threshold negativity, any negative central
value of a real character, any "disproof" your pipeline produces is an implementation
bug until that oracle — plus regression anchors, plus unit tests against mpmath —
convicts mathematics instead. Observed base rate in this project: one convincing
fake catastrophe per scaling step, three for three caught.

## Diligence status (be honest when citing)

- **Verified July 25, 2026 (second working day):** every EXPECTED number in this
  repository reproduces on a fresh machine, several to all printed digits; the
  |D| ≤ 1e5 hunt reproduces end-to-end; L(½, χ₁₄₆₉₃) confirms against a fully
  independent implementation. See `results/RESULTS.md`, second section. (Dateline
  note: the original documents self-date July 26; the clock on both working days
  read July 25.)
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
- The float pipeline is double precision, Galerkin m ≤ 101, Rayleigh–Ritz one-sided.
  `src/hp_margins.py` now runs the same ladder at 25+ digits (still Rayleigh–Ritz
  one-sided, and mpmath quadrature is estimated, not interval-certified); true
  interval enclosures (ARB) remain Track A, milestone M1 — in the prolate basis,
  per §2.14.

## Where the door is

`PROGRAM.md` §2.12–2.13 and §3. The finite factorizations all exist (gap-free
Cholesky succeeds at every tested support). The infinite object behind them — the
uniform factorization whose near-kernel is the zeros, five of whose bottom
eigenvalues and seven of whose kernel nodes are measured in this repository — is,
by Weil's criterion, the Riemann Hypothesis itself.
