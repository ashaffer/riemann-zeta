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
2. [`LEAN-ANALYTIC-INFRASTRUCTURE.md`](LEAN-ANALYTIC-INFRASTRUCTURE.md) explains
   the reusable analysis as ordinary mathematics rather than as a file list.
3. [`CERTIFICATE-GUIDE.md`](CERTIFICATE-GUIDE.md) explains what the exact
   certificates prove and how they enter the conceptual argument.
4. [`NO-GO-THEOREM-GUIDE.md`](NO-GO-THEOREM-GUIDE.md) organizes the negative
   results by mathematical mechanism.
5. [`../PUBLICATION.md`](../PUBLICATION.md) ranks possible papers and library
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
- [`../NO-GO-ATLAS.md`](../NO-GO-ATLAS.md) for the scope of obstruction results;
- [`../PUBLICATION.md`](../PUBLICATION.md) for publication status and novelty;
- [`MANUSCRIPT-BRIEFS.md`](MANUSCRIPT-BRIEFS.md) for proposed paper structure;
- historical files in `results/` only for branch provenance and experimental
  detail.

If a historical report conflicts with a current theorem card or audit, the
current theorem card and audit govern.
