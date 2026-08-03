# Stage 3: parsimony and support saturation

## Refactor before proof search

The completed-kernel, arithmetic-balance, and zero-side-limit fields in the
Stage-2 package are synchronized coordinate descriptions of one radical
functional.  They are not three independent equations.  Lean proves that,
for a negative shift, nonemptiness of the full Stage-2 package is equivalent
to nonemptiness of its minimal source: a first-crossing zero mode.

This prevents an important intuition error.  Combining equivalent explicit
formulas cannot overdetermine the mode; a Stage-3 proof needs information not
already contained in the fixed-window radical equation.

## First new invariant

The missing information is the support-parameter history.  At a genuine first
crossing, every smaller nonnegative window is strictly positive.  Exact nested
support invariance, already proved in `ActivationCancellation.lean`, then
implies:

> The first-crossing vector is not the zero-extension of any nonzero
> form-domain vector from a strictly smaller symmetric interval.

Thus its essential symmetric support reaches the crossing boundary in the
only representation-independent sense currently formalized.  This is
`no_nonzero_smaller_support_preimage`.

The equivalent geometric consequence is now kernel-checked as
`collarPart_ne_zero`: for every `0 <= b < a`, the orthogonal residual outside
the old-support subspace `L2[-b,b]` is nonzero.  In other words, every proper
boundary collar carries some mass.  This is qualitative saturation; it does
not yet give a uniform lower bound as the collar shrinks.

The result also explains the completed-space boundary terms: a candidate
cannot be reduced to an interior-supported mode, so endpoint/collar behavior
is necessarily load-bearing.

## Status

This is genuine Stage-3 progress, not the transversality theorem itself.  The
remaining target is narrower:

*combine the weak radical identity with support saturation to show that its
boundary defect cannot be nonzero.*

Generic fixed-window transformations cannot accomplish this because they add
no information.  A successful next lemma must use boundary traces, shrinking
windows, or a one-sided support variation.

The parameter-history existence theorem is kept as a named literature axiom;
both support-saturation implications themselves are kernel-checked.  The
axiom audit also makes clear that `collarPart_ne_zero` uses no new analytic
axiom beyond exact nested-support invariance.
