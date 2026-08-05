# Referee and release checklist

This checklist is the publication gate for mathematical notes, formal-library
extractions, and computer-assisted results in this repository.
It operationalizes [`PROOF-STANDARD.md`](PROOF-STANDARD.md); if the two differ,
the proof standard controls.

## 1. Claim audit

- State the strongest theorem in one sentence without motivational language.
- Label it as Lean, analytic, computer-assisted, literature-conditional, or
  diagnostic using [`PUBLICATION.md`](../PUBLICATION.md).
- Put every assumption in the theorem statement, including anchors,
  integrability, support conventions, multiplicity conventions, and
  normalizations.
- State the closest known prior result and the exact increment over it.
- Add a nonclaim paragraph listing the tempting stronger conclusions that do
  not follow.
- Search for counterexamples to the proposed headline before polishing the
  exposition.
- Create or update the canonical theorem card and proof-debt ledger.
- For a no-go result, name the exact eliminated class and the smallest escape
  hatch in the same section.
- Give a proof spine in standard mathematical notation before citing Lean
  declarations, tactics, or generated data.
- Map every step of that proof spine to a public declaration or a plainly
  labeled external obligation.

## 2. Mathematical normalization audit

- Fix the Fourier convention, Plancherel constant, and translation sign once.
- Record whether support is `[-a,a]`, length `2a`, or the program parameter
  `L=4a`.
- Record whether the zero sum is over all zeros, positive ordinates, distinct
  ordinates, or multiplicities.
- Record the orientation of every contour and winding number.
- Check the pole term, gamma shift, logarithmic derivative sign, and every
  factor of two against an independent source or calculation.
- Test one prime coefficient and one simple pole by hand.
- For functional-equation symmetries, write both transformed coordinates
  explicitly; do not rely on “Haar invariance” to identify a joint law.

## 3. Lean release audit

- Extract the candidate onto a clean branch; do not submit the application
  stack or generated certificates with a reusable theorem.
- Rebase on current mathlib and adopt its current module/import syntax.
- Replace project namespaces and compatibility aliases with destination names.
- Minimize imports and run the available linters.
- Run `#print axioms` on every advertised endpoint.
- Accept only the documented standard axioms for unconditional theorem claims.
- List every `*Literature` input separately from checked theorems.
- Add docstrings and at least one small example independent of RH.
- Provide actual author names and retain repository provenance in the PR.

Focused local audits are preferred on memory-constrained machines:

```text
cd lean/glide && lake build Glide.UpstreamAudit
cd lean/glide && lake build Glide.HardHorizonAudit
cd lean/weilcert && lake build Weilcert.UpstreamAudit
cd lean/rhbridge && lake build RHBridge.ReusableAudit
```

Do not use an umbrella rebuild as a routine smoke test when it triggers the
generated certificate corpus.  Record peak memory for any required heavy
build and provide a bounded-concurrency runner.

## 4. Computer-assisted theorem audit

- Freeze all source files used to generate the candidate data.
- Hash inputs, generated rational tables, interval checkpoints, and outputs.
- Fail closed if the integrand or normalization source changes.
- State which arithmetic operations are exact and which use outward-rounded
  intervals.
- Include an independent normalization oracle.
- Separate finite-matrix positivity from the analytic tail/complement bound.
- State the generic certificate soundness lemma and one small hand-checkable
  instance before referring the reader to a generated witness.
- Keep large exact tables in machine-readable artifacts; a manuscript should
  report their dimensions, margins, hashes, and mathematical role instead.
- Record the software versions, precision, worker count, peak memory, and
  expected runtime.
- Make stale artifacts detectable.
- Reproduce the headline theorem from a clean checkout before release.

## 5. Python artifact audit

- Run unit tests from the repository root with `python3 -m pytest`.
- Distinguish unit/regression tests from proof-producing interval runs.
- Add a machine-readable dependency environment before archival release.
- Keep optional heavy dependencies out of the light test path.
- Give every long computation a timeout, resumable checkpoint, and bounded
  parallelism.
- Never infer a theorem from a floating-point scan.

## 6. Conventional proof audit

- Expand every passage from a probability/product model to natural density
  into a quantitative truncation lemma.
- Verify every interchange of limit, sum, expectation, derivative, and
  integral under the exact stated topology.
- For an infinite product, identify the topology of convergence and prove that
  the claimed invariant is continuous in it.
- For a zero-counting argument, distinguish an index computation from a
  rephrased argument principle.
- For a positive form, identify its closed domain and show that the completion
  preserves the inequality.
- For an operator approximation, prove no spectral mass or defect can escape
  at infinity.

## 7. Reproducibility and archival metadata

- Add `CITATION.cff` only after authorship and preferred citation are known.
- Add a release tag and archive DOI only after the exact artifact set is
  frozen.
- Record the Lean, mathlib, Python, and numerical-library versions.
- Include the license in every extracted source file.
- Link the paper theorem numbers to code declarations and verification
  commands.
- Preserve negative results and failed hypotheses; they prevent future work
  from silently repeating invalid paths.
- Freeze the theorem card, proof, axiom output, and artifact hashes together;
  later summaries may not strengthen that snapshot.

## 8. Independent review and provenance

- Obtain a hostile mathematical review that tries to falsify every
  hypothesis, quantifier, and limiting step.
- Obtain an artifact review that reproduces only the advertised endpoint from
  the theorem card.
- Record each objection and its disposition; absence of a comment is not a
  sign-off.
- Disclose material AI assistance under the venue's policy.  Human authors
  approve the statement and accept responsibility for the proof.
- Do not use chat history, an AI judgment, or a numerical scout as a premise.

## 9. Final language check

Before submission, search the draft for `prove RH`, `formalized
Guinand--Weil`, `unconditional`, `first`, `novel`, and `general no-go`.
Inspect every occurrence manually.  Replace broad language by the exact scope
unless priority and dependencies have been independently established.
