# Recursive publication-theorem audit

**Date:** 2026-09-02  
**Scope:** the complete R1--R180 reduction registry, the current publication
portfolio, and theorem artifacts added through R178  
**Status:** fixed-point research audit; not a novelty certificate

## Executive conclusion

The project does contain several results that are plausible publication
nuclei.  It does **not** presently contain a proof of RH, a uniform zero-free
strip, or the sharp four-cycle bound.  Those open objectives must not be used
to inflate the publication status of independent by-products.

After canonicalizing statements, merging descendants, removing equivalent
reformulations and imported results, and running proof and literature attacks,
the 180 registry entries collapse to:

1. three high-upside theorem packages needing bounded specialist audits;
2. three lower-risk papers or notes with more modest mathematical novelty;
3. two structural/countermodel packages that need a sharper narrative before
   they are papers;
4. one correction suitable first for private author contact; and
5. one high-upside incubator, SR2PF, which is explicitly not yet a theorem.

No item below is labelled `CERTIFIED_NEW`.  `CANDIDATE_NEW` means only that a
specific theorem delta survived the hostile comparisons performed here.  It
still requires independent subject-specialist review and a database-level
novelty search.

## 1. Audit method and recursive fixed point

The input has exactly 180 contiguous registry records, R1 through R180.
A mechanical heading search finds 933 theorem-like headings in the Markdown
tree, but that number is deliberately treated as noise: many headings are
lemmas, restatements, gates, numerical observations, imported results, or
countermodels.

Each recursive pass applied four independent publication gates:

| Gate | Question | Failure action |
|---|---|---|
| correctness | Is every quantified claim proved in the stated scope, including imported-input uniformity? | repair or demote to proof draft |
| substance | Is the result more than a routine coordinate change, finite computation, or standard corollary? | make it supporting material |
| literature delta | Can the exact improvement over the closest primary theorem be stated in one sentence? | use `NOVELTY_UNRESOLVED` or `IMPORTED` |
| paper coherence | Does the result answer a recognizable question for a mathematical audience? | merge with its theorem descendants or do not publish separately |

The passes were:

1. **Canonicalization.** Replace project codenames by invariant theorem
   statements and attach every claim to its first genuinely open edge.
2. **Deletion.** Remove RH equivalences, conditional chains, diagnostics,
   imported theorems, and elementary scaffolding from the headline pool.
3. **Descendant merging.** Merge results that prove successive portions of
   the same mathematical assertion.
4. **Hostile proof audit.** Search for missing uniformities, degenerate
   fibers, injectivity failures, quantifier drift, and numerical-to-symbolic
   jumps.
5. **Hostile literature audit.** Compare exact statements and exponents with
   primary sources, including work posted after the theorem drafts.
6. **Second merge/demotion pass.** In particular, demote R178 from a
   standalone positive theorem and SR2PF from “proved”; isolate the R110 part
   of the continuant package from the R119/Blomer--Pascadi collision risk.
7. **Fixed point.** Reapply all four gates to the resulting packages.  No
   further merger improves both correctness of attribution and paper
   coherence.

This is the first stable portfolio in which “repo-proved,” “apparently new,”
and “ready to submit” are separate fields.

## 2. Fixed-point publication portfolio

### A. Highest-upside bounded audits

| Package | Theorem nucleus | Mathematical status | Novelty status | Decisive external gate |
|---|---|---|---|---|
| rough gaps | For integers with no prime factor below `z`, the consecutive-gap second moment is `O_epsilon(X log^2 X)` uniformly for `X^epsilon <= z <= X^(3/16-epsilon)` | complete internal proof, but its refactoring of imported sieve estimates has not had an independent specialist audit | `CANDIDATE_NEW` for the exponent range only | a sieve specialist must verify that Matomäki's `S1/S2/S3` argument and well-factorable decomposition remain uniform under the moving levels used here |
| cyclic-continuant energy | The nonparabolic weighted trace energy is `O(H^epsilon(H+H^(3/2)/sqrt(|lambda|)) prod ||z_i||_2^2)`; hence the unit-weight eight-variable energy is `O(H^(5+epsilon)+H^(11/2+epsilon)/sqrt(|lambda|))` | internally proved, including zero-coordinate and parabolic separation | R110 is `CANDIDATE_NEW`; the larger R108/R110/R119 package remains `NOVELTY_UNRESOLVED` | compare the exact weighted inequality line by line with Blomer--Pascadi (2026), especially their discriminant collision bounds, and add sharpness examples |
| solvable support quotient | In a faithful transitive solvable action, the normal closure of elements of support at most `ell` has orbit size at most `2ell`; the constant 2 is sharp, and selected Frobenii split in the corresponding intermediate field | internally complete proof with an affine primitive-section argument and a wreath-product sharpness family | `NOVELTY_UNRESOLVED` | a permutation-group specialist must locate or exclude the exact normal-closure/common-block formulation in the minimal-degree and base-size literature |

The first package has the greatest conventional analytic-number-theory upside.
Its theorem type is classical: Friedlander obtained the same endpoint with a
smaller prescribed roughness range.  The possible new content is solely the
extension to `3/16-epsilon` extracted from Matomäki's raw lemma.  This makes
the imported-input audit a red gate, not a formality.  See
[`publication/ROUGH-GAP-SECOND-MOMENT.md`](../publication/ROUGH-GAP-SECOND-MOMENT.md).

The second package should be written as **Integer and finite-field energies of
the length-four cyclic continuant**.  R110 is the headline; R108 is support.
R119 should be included only if its exact delta from the July 2026
Blomer--Pascadi paper survives.  The algebraic bridge

```text
k^4(F^2-4) = (P-kxy)(P-kxy+4k^2),  k=lambda^(-1),
```

connects the integer energy to the finite-field Vieta discriminant and gives
the package a coherent narrative.  See
[`R110-TRACE-COLLISION-POWER-SAVING-THEOREM.md`](R110-TRACE-COLLISION-POWER-SAVING-THEOREM.md).

The third package becomes stronger as a paper if R138, R144, R146, R151, and
R152 are used as applications rather than counted as five additional papers.
A plausible title is **Small-support Frobenius classes and positive virtual
Artin filters**.  The support-to-block theorem is the clean group-theoretic
nucleus; the number-field and virtual-character consequences supply motive
and examples.  See
[`R143-SOLVABLE-SUPPORT-QUOTIENT-AND-PRIMITIVE-CLASSIFICATION.md`](R143-SOLVABLE-SUPPORT-QUOTIENT-AND-PRIMITIVE-CLASSIFICATION.md).

### B. Real but more modest publication candidates

| Package | Supported contribution | Status and correct framing |
|---|---|---|
| sparse positive-cosine antipodes | sharp `M`-atom compression, generic exact `M`-atom uniqueness, realization on every prescribed `M`-harmonic support, and a Chebyshev sign classification for consecutive harmonics | proof and replay are strong; `NOVELTY_UNRESOLVED` because Caratheodory, analytic full spark, Chebyshev alternation, and trigonometric moment-curve geometry are classical individually |
| local arithmetic Weil formalization at `a=7/16` | a strict Lean theorem for the explicitly defined arithmetic form on its full logarithmic form domain, plus reproducible exact certificates | `PROJECT_SYNTHESIS`; publishable as formal mathematics only if the title and abstract state that the zero-divisor identification is a literature axiom |
| constrained Euler-product rigidity/flexibility | R160 fixed-bank cofactor zeros, R161 finite-Euler `a`-point microclouds, R163 actual-prime signed local approximation, and R178 positive sparse surgery | merge as one `NOVELTY_UNRESOLVED` manuscript; repair R161's root separation/injectivity argument and treat R178 as a countermodel section, not a standalone theorem paper |

The cosine result is the cleanest short note after novelty review.  Its value
is the transposed synthesis theorem and sharp support size, not any implication
for prime logarithms or zeta.  See
[`publication/SPARSE-POSITIVE-COSINE-ANTIPODES.md`](../publication/SPARSE-POSITIVE-COSINE-ANTIPODES.md).

The local Weil package has unusually strong reproducibility, but its analytic
bridge is not proved by the Lean endpoint.  The public claim must therefore
remain “strict positivity of the arithmetic form,” not “positivity of the
zeta-zero Weil sum.”  See
[`publication/A-7-16-RELEASE-CANDIDATE.md`](../publication/A-7-16-RELEASE-CANDIDATE.md).

The Euler results become more credible when presented together as a
rigidity/flexibility boundary.  Separately, their mechanisms are close to
classical Hurwitz, universality, Pechersky rearrangement, and Euler-product
surgery.  Together they identify exactly which finite-bank, local-approximation,
and positivity data fail to control global divisors.  The merge does not
create a zero-free strip and must not be marketed as doing so.

### C. Structural notes needing a narrower thesis

| Cluster | What survives | Why it is not yet a paper |
|---|---|---|
| localized Weil-floor amplification | an off-line zero forces a localized quadratic-form floor to diverge negatively at exponential rate, under the recorded divisor hypotheses | likely a direct quantitative corollary of the Bondarenko--Radchenko--Seip framework; novelty unresolved |
| singular Hardy/Toeplitz boundary anomaly | a regulator-independent trace anomaly and boundary-flux jump | proof is self-contained, but the mechanism may be standard Toeplitz index technology |
| projection-defect Ward catastrophe | an exact direct-sum countermodel with arbitrary null envelope and finite-codimension immunity | correct and useful as a no-go, but probably too elementary for a standalone article without an optimal classification theorem |
| expanding de Branges topology blindness | Clark atoms can escape while fixed-window Weyl data and strong resolvent limits lose the divisor | `PROJECT_SYNTHESIS`; needs a theorem tied to the precise Suzuki/de Branges application |

These should not be forced into a miscellaneous anthology.  A package should
advance only when it acquires one precise literature-facing question and an
exact delta from its closest operator-theoretic predecessor.

### D. Corrective result

The Endo hybrid joint-limit phase correction remains an exact, small
`CANDIDATE_NEW` contribution: a coordinate inversion changes the random
Dirichlet-series law, and a one-prime mixed moment separates the two laws.
The current arXiv record is still version 1.  The ethical and efficient first
action is a private, fully explicit note to the author, not an adversarial
standalone paper.  See
[`ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md`](ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md).

### E. Incubator, not theorem

SR2PF has the largest speculative upside but is not literature-grade.  The
classification of the flattening `3 x 3` minors appears valid and no finite
counterexample was found.  The missing proof is not a cosmetic detail: it
still needs a standalone rational secant/tangent descent, a fixed quadratic
field, uniform Pell/fixed-norm counting, at least three active modes, and
explicit separation hypotheses.  Finite replay certifies examples only.
Its correct status is `PROOF_DRAFT / NOVELTY_UNRESOLVED`.  See
[`ZETA23-SR2PF-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md`](ZETA23-SR2PF-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md).

## 3. Important demotions and corrections

The hostile pass changes the previous decision tree in material ways.

1. **R178 sparse positive Euler surgery is not a standalone major theorem.**
   It is algebraically sound, but “sparse” means small positive density rather
   than density zero; the auxiliary period grows as the density shrinks, the
   finite head is nonuniform, and no functional equation is retained.  Its
   proper role is a sharp countermodel showing that positivity plus two PNTs
   and approximate convolution identities do not determine zeta's divisor.
2. **SR2PF is not proved.**  Symbolic minor identities and finite checks do not
   supply the arithmetic descent or uniform norm counting.  Calling the full
   statement proved was a proof-status error.
3. **R119 has a new priority risk.**  Blomer--Pascadi (2026) use the same
   discriminant geometry and nearby collision estimates.  R110's weighted
   integer bound still appears distinct, but the two claims must be separated.
4. **The Jordan/filter identities are mostly mechanism, not novelty.**  The
   publishable question is the sharp common quotient or a genuinely new Artin
   consequence, not the existence of familiar permutation-character filters.
5. **The static Mobius obstruction is likely classical in mechanism.**  Keep
   it as a lemma or computationally documented no-go unless a precise delta
   from Davenport--Erdos/convergent-multiple-set theory is found.
6. **Local Euler approximation does not propagate globally.**  R163 is a real
   finite-union/local theorem, but monodromy and polynomial-hull obstructions
   prevent it from being silently upgraded to a contour theorem.
7. **Formal proof does not discharge an analytic literature axiom.**  The
   local Weil build proves its intrinsic arithmetic form statement; it does
   not formalize the full Guinand--Weil zero-divisor identity.

These corrections reduce the apparent theorem count but increase the chance
that what remains can survive refereeing.

## 4. Literature comparisons that currently matter

Only primary sources are used as substantive comparators here.

- Matomäki's *Almost primes in almost all very short intervals* supplies the
  raw mean-square and shifted-correlation estimates used by the rough-gap
  draft: <https://arxiv.org/abs/2012.11565>.  Friedlander's 1984 and 2008
  results already give the same `X log^2 X` endpoint at smaller prescribed
  cutoff exponents.  Gafni--Tao's 2025 theorem concerns rough numbers inside
  prime gaps and does not obviously subsume the present second moment:
  <https://arxiv.org/abs/2508.06463>.
- Conley--Ovsienko give the cyclic-continuant setting
  (<https://arxiv.org/abs/1707.09106>), and Reuss gives general bilinear and
  trilinear hypersurface counts (<https://arxiv.org/abs/1502.07594>).
  Blomer--Pascadi's July 2026 paper is the decisive new comparator for R119
  and perhaps parts of R110: <https://arxiv.org/abs/2607.24311>.
- Recent work on base size and minimal degree of transitive groups confirms
  that the neighborhood is active but does not, in the inspected statement,
  settle R143's exact common normal-closure quotient:
  <https://arxiv.org/abs/2506.17668>.  This is not an exhaustive novelty
  certification.
- Convex hulls of trigonometric moment curves have an established facial
  theory; for one representative primary source see
  <https://arxiv.org/abs/1302.2226>.  The cosine paper must distinguish its
  sparse positive antipode theorem from that theory.
- The secant-variety literature, including Raicu
  (<https://arxiv.org/abs/1011.5867>), governs the algebraic portion of SR2PF
  but does not replace its missing arithmetic descent.
- Endo's current arXiv version is <https://arxiv.org/abs/2410.17575>.

Search failure is evidence only for `NOVELTY_UNRESOLVED`, never evidence of
certified novelty.

## 5. Verification performed

The following targeted regression suite passes:

```text
PYTHONPATH=src python3 -m pytest -q \
  src/test_rough_gap_lower_sieve_frontier.py \
  src/test_sparse_cosine_antipode_classification.py \
  src/test_global_euler_jordan_coercivity.py \
  src/test_jordan_detector_calculus.py

27 passed
```

The following standalone checkers also pass:

```text
python3 results/verify_rough_gap_second_moment_frontier.py
python3 results/verify_zeta23_matomaki_rough_gap_gate.py
python3 results/verify_sparse_cosine_antipode_classification.py
```

The SR2PF checker passes its finite certificates but explicitly does not prove
the symbolic descent or Pell/fixed-norm estimates.  Computational replay is
therefore not included as evidence for the missing theorem.

## 6. Ranked next actions

The ranking maximizes information gained per unit effort rather than proximity
to RH.

1. **Rough-gap referee packet.** Send the exact changing-level use of
   Matomäki's Proposition 5.1, Lemma 5.4, equations (49), (61), and (69) to one
   sieve specialist.  Ask a binary question: does every uniformity survive?
   In parallel, run MathSciNet/ZbM searches for the exact prescribed-cutoff
   range.  A yes/no answer resolves the leading candidate.
2. **R110/R119 collision packet.** Give a specialist the theorem statement,
   all degenerate cases, and a proposition-by-proposition comparison with
   Blomer--Pascadi.  Add constructions testing the `H^(3/2)` scale.  Publish
   R110 alone if R119 overlaps.
3. **R143 group-theory packet.** Send the exact normal-closure theorem and the
   sharp wreath-product family to a permutation-group specialist.  Search by
   theorem content—minimal degree of primitive solvable sections, normal
   closures, block kernels—not by project vocabulary.
4. **Endo contact.** Prepare a two-page correction with the separating mixed
   moment and offer it privately to the author.
5. **Formal reproduction.** Freeze and independently reproduce the `a=7/16`
   Lean build before preparing the formalization paper.
6. **Second wave.** Only after those bounded audits, invest in a cosine note,
   the merged Euler rigidity/flexibility paper, or a narrow operator theorem.
7. **SR2PF discipline.** Write the five missing arithmetic lemmas as separate
   statements.  Do not restore `PROVED` until each has a conventional proof.

This portfolio deliberately separates high mathematical upside from high
readiness.  The rough-gap and R110 candidates have the highest expected
theorem value; the Endo correction and local Weil formalization are closest to
responsible dissemination.

## 7. Self-improved research protocol

The audit yields the following persistent rules for future work.

1. Track **proof confidence**, **novelty confidence**, and **publication
   readiness** separately.  Never average them into one optimism score.
2. Count canonical theorem statements, not files, headings, reductions, or
   descendants.
3. Merge theorem descendants before assessing novelty; a sequence of lemmas
   solving one problem is one contribution.
4. Treat every changed parameter in an imported theorem as a new proof
   obligation.  Algebraic exponent replay cannot certify analytic uniformity.
5. Compare against the closest primary theorem at the statement and exponent
   level, especially work posted after the local draft.
6. Require at least one hostile sharpness family or boundary example for every
   proposed quantitative theorem.
7. A finite checker certifies only the proposition it executes.  It cannot
   close a symbolic descent, an asymptotic uniformity, or a literature axiom.
8. Promote a result only if its literature delta fits in one sentence without
   project jargon.
9. Demote elementary countermodels to supporting sections unless they prove an
   optimal impossibility or a classification theorem.
10. Stop a route after two independent novelty failures or when all remaining
    novelty is merely the conjunction of standard mechanisms with no new
    theorem-level consequence.
11. Re-run the portfolio audit only when a proof status changes, a theorem is
    generalized, or new literature appears—not after every exploratory note.
12. Keep the global nonclaim invariant: none of these packages proves RH, a
    uniform zero-free strip, or the sharp four-cycle bound.

The machine-readable fixed point is
[`context/zeta23_recursive_publication_audit_v1.json`](context/zeta23_recursive_publication_audit_v1.json).

