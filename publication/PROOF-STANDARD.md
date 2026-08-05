# Proof and release standard

Version 1.0, 2026-08-05.

The goal of this standard is not to make criticism impossible.  A serious
mathematical artifact should make criticism *easy to aim and hard to sustain*:
every claim has one meaning, every dependency is visible, every computation is
reproducible, and every gap is named before a referee has to find it.

This document governs public theorem claims from this repository.  It is
stricter than the exploratory research notes.  The operational checklist is
[`REFEREE-CHECKLIST.md`](REFEREE-CHECKLIST.md), and the first claim-by-claim
application is [`../NO-GO-ATLAS.md`](../NO-GO-ATLAS.md).

## 1. The theorem contract

Every result promoted beyond an exploratory note must have one canonical
theorem card containing all of the following.

1. **Statement.** A standalone quantified statement, without motivational
   language or a reference to an earlier conversation.
2. **Hypotheses.** Every regularity, support, topology, multiplicity,
   normalization, positivity, and independence hypothesis.
3. **Conclusion.** The weakest literal conclusion proved by the argument.
4. **Evidence class.** Lean theorem, analytic theorem, computer-assisted
   theorem, literature-conditional theorem, diagnostic, or proposal.
5. **Trust base.** Imported axioms, named literature theorems, numerical
   libraries, generated data, and foundational axioms.
6. **Exact scope.** The class of objects or proof architectures to which the
   result applies.
7. **Sharpness.** A witness showing why a material hypothesis cannot simply be
   dropped, or an explicit declaration that sharpness is unknown.
8. **Nonclaims.** The nearest tempting statements that do not follow.
9. **Prior-art boundary.** The closest located theorem and the exact proposed
   increment; “new” is forbidden until an independent search supports it.
10. **Reproduction.** Stable artifact paths and the smallest command that
    checks the advertised endpoint.

The theorem card is the claim of record.  Abstracts, READMEs, talks, code
comments, and commit messages may shorten it but may not strengthen it.

## 2. Evidence classes do not collapse

These labels answer different questions and must remain distinct.

| Label | What it licenses | What it does not license |
|---|---|---|
| Lean theorem | The named declaration follows from the axioms printed by its audit in the pinned environment | That the formal statement models the intended analytic object, is novel, or has no hidden strength in its definitions |
| Analytic theorem | A conventional proof of the displayed statement is present | Kernel checking, priority, or correctness of an unstated limiting argument |
| Computer-assisted theorem | Exact/interval computation plus the stated analytic transfer proves the endpoint under a frozen trust base | An infinite theorem inferred from floating-point behavior |
| Literature-conditional theorem | The conclusion follows once the named imported result is granted | That the imported interface has been formalized or normalized correctly |
| Diagnostic | A finite exact or numerical test supports, refutes, or guides a conjecture | A theorem outside the tested finite object |
| Proposal | A falsifiable research target has been specified | Any mathematical conclusion |

An artifact can carry more than one label only componentwise.  For example,
“Lean checks the finite algebra; the convergence theorem is analytic” is
acceptable.  “The whole result is formalized” is not.

## 3. Four ledgers required for analytic work

### 3.1 Normalization ledger

Record, in one place:

- Fourier transform sign and Plancherel constant;
- support parameter and its conversion to physical length;
- contour orientation and winding convention;
- zero multiplicity and summation convention;
- pole, gamma, and logarithmic-derivative signs;
- inner-product linearity convention;
- the exact prime-power weight and autocorrelation translation.

At least one prime coefficient, one pole residue, and one symmetry transform
must be checked independently by hand.  Changing a normalization invalidates
all downstream certificates until their fingerprints are regenerated.

### 3.2 Dependency ledger

Write the proof as a directed acyclic graph.  Each node is one theorem,
literature input, or computer certificate.  No node may be called
“consensus” without a precise statement and source.  An implication whose
decisive node is RH-equivalent must say so where the implication is advertised.

### 3.3 Limit ledger

For every interchange or passage to a limit, record:

- the topology of convergence;
- the dominating or compactness statement;
- the theorem permitting the interchange;
- whether exceptional sets depend on the parameter;
- why the desired invariant is continuous in that topology.

Locally uniform analytic continuation, uniform convergence, Hilbert-space
convergence, convergence in measure, and Besicovitch mean convergence are not
interchangeable.  A proof that changes topology must contain an explicit
bridge theorem.

### 3.4 Proof-debt ledger

Every missing obligation is assigned one of four states.

- **Green:** proved and independently reproduced at the claimed evidence
  level.
- **Amber:** a complete-looking proof exists, but independent review,
  formalization, or a frozen certificate is still required.
- **Red:** a mathematical implication needed by the headline is open,
  assumed, or supported only diagnostically.
- **Retired:** a stated hypothesis or route has a proved counterexample; the
  exact counterexample is retained.

A headline theorem may contain no red debt.  Amber debt must be disclosed in
the abstract or release note.  A conditional theorem may be released only if
its red nodes appear as hypotheses in the theorem statement itself.

## 4. No-go theorems need a witness and an escape hatch

A negative result is especially prone to inflated language.  “This approach
fails” is not a theorem.  A publication-grade no-go result must provide:

1. a formally defined candidate class;
2. a universal obstruction on that class or an explicit member satisfying
   all proposed hypotheses and violating the desired conclusion;
3. verification that the countermodel does not quietly discard a listed
   hypothesis;
4. the smallest known hypothesis change that evades the obstruction.

The permitted closing sentence is:

> The class defined by hypotheses H1--Hn is eliminated; constructions that
> violate at least one of H1--Hn remain open.

The phrases “general no-go,” “the path is closed,” and “the entire class is
ruled out” are forbidden unless the exact class appears in the same sentence.
A toy countermodel proves logical insufficiency of its hypotheses.  It does
not prove that the zeta-specific object realizes the bad case.

## 5. Formal proof protocol

For every advertised Lean endpoint:

1. provide a small audit module containing `#print axioms` for the exact
   public declarations;
2. compile that audit from a clean pinned checkout;
3. distinguish standard Lean axioms from project-specific literature axioms;
4. inspect definitions for vacuity, circularity, and mismatch with the paper
   statement;
5. minimize imports and include a non-RH example when proposing an upstream
   contribution;
6. record Lean and mathlib revisions and the license of each extracted file.

Proof length and kernel acceptance are not substitutes for mathematical
model validation.  Conversely, an elementary one-line Lean theorem should be
presented as an elementary supporting lemma, not enlarged into a research
claim by formal packaging.

## 6. Computer-assisted proof protocol

The theorem statement must separate:

- exact symbolic identities;
- outward-rounded interval enclosures;
- analytic truncation and tail bounds;
- the finite-to-infinite transfer;
- ordinary floating-point diagnostics.

All proof-producing inputs and outputs receive hashes.  Cached artifacts bind
to the source defining the integrand and fail closed after a source change.
The release records software versions, precision, peak memory, worker count,
runtime, and a bounded-memory reproduction command.  A second implementation
or independent normalization oracle is required for a headline numerical
constant.

## 7. Adversarial review protocol

Before promotion, two reviews are written independently.

- The **mathematical referee** tries to falsify the statement, attacks every
  quantifier and limiting step, and searches for a smaller countermodel.
- The **artifact referee** starts from the theorem card and tries to reproduce
  only the advertised endpoint, without relying on session history.

The author then produces a response table: objection, disposition, changed
statement or proof, and remaining debt.  Silence is not approval.  A review is
complete only when each objection is resolved, accepted as a scope reduction,
or recorded as open debt.

For a submission candidate, freeze the theorem card, proof, audit output, and
artifact hashes together.  Later prose edits may not silently broaden the
frozen claim.

## 8. Literature and priority protocol

A literature search is part of correctness whenever a result is described as
new, stronger, first, overlooked, or publication-worthy.  Search the theorem,
its contrapositive, the underlying abstract structure, and neighboring fields.
Prefer primary sources.  Record search date and terms, and distinguish:

- the mathematical statement;
- its application to zeta or another special object;
- its formalization in Lean;
- the exact constants or effective refinement.

Failure to locate a predecessor supports only “no exact predecessor was found
in this search.”  It does not prove priority.

## 9. AI--human provenance

AI assistance is neither evidence against a proof nor evidence for it.  It is
provenance.

- Human authors approve the theorem statement, take responsibility for the
  proof, and control submission.
- Material AI assistance is disclosed according to the venue's current
  policy.
- The public argument is a conventional self-contained proof; chat history is
  never a premise.
- Generated citations, computations, and translations into formal statements
  are independently checked.
- Useful failed attempts are preserved in the research archive but removed
  from the shortest proof unless they establish sharpness or explain scope.

The quality target is not “human-looking text.”  It is a compact chain of
claims for which a skeptical reader can locate every obligation.

## 10. Release states

| State | Minimum requirement |
|---|---|
| Exploratory | Honest label and enough provenance to reproduce the thought or experiment |
| Internally verified | Canonical theorem card, complete local proof, proof-debt ledger, and one adversarial audit |
| Submission candidate | Independent mathematical review, independent artifact reproduction, literature calibration, frozen dependencies, and no hidden red debt |
| Released | Public version matches the frozen claim and contains an errata channel |

Errors discovered after release are corrected visibly.  The repository should
make an erratum cheap to issue; credibility comes from traceable correction,
not a claim of infallibility.
