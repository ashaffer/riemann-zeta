# Stage 1: closed-domain Suzuki bridge

## Result

The repository now distinguishes three spaces that earlier reports sometimes
blurred together:

1. the logarithmic form domain of the localized Weil form;
2. the smooth/H1 core on which differentiation and kernel integrals are
   pointwise meaningful;
3. Suzuki's shift-dependent completed Hilbert space carrying the extended
   derivative and continuous-kernel operator.

A first-crossing vector belongs initially only to the form domain.  For any
negative shift, the completed closed derivative sends it to the shifted
Suzuki space.  The literature-backed intertwining theorem gives

`G_a_bar (D_bar f) = 0`,

and injectivity of `D_bar` preserves nonzeroness.  Lean composes these facts as

`firstCrossing_to_completedSuzukiZeroMode`.

Thus Stage 1 closes at the correct domain level: a nonzero zero-energy vector
at a nonnegative window yields a nonzero kernel vector of the **extended**
continuous-kernel operator.  It does not assert that the vector is smooth or
that its derivative is an ordinary pointwise L2 function.

## Imported analytic content

`SuzukiClosedDomainLiterature.lean` introduces exactly two substantive
literature assertions:

* the closed derivative does not kill a nonzero form-domain vector;
* at a nonnegative zero crossing and a negative shift, it intertwines the zero
  Weil mode with the kernel of the extended Suzuki operator.

The completed space and its operator are opaque declarations because mathlib
and RHBridge do not currently construct the relevant form completions and
Friedrichs extensions.  The audit file prints the axioms of both public
composition theorems.

## Consequence and limitation

The completed Suzuki operator is noninjective at any first crossing.  This is
the precise Stage-1 output needed by the compression roadmap.

The accepted first-crossing literature package is now also explicit.  It
combines Weil's criterion, a positive small-support window, continuity of the
lowest localized eigenvalue, attainment of its zero value, and the associated
closed operator representation.  Lean consequently proves:

* if RH is false, then at some positive finite support every negatively
  shifted completed Suzuki realization is noninjective;
* if all such completed operators are injective, then RH follows.

The public reduction theorem is
`riemannHypothesis_of_completedSuzuki_injective`.  Its audit exposes the
first-crossing and closed-domain literature axioms; it contains no hidden RH
assumption.

Passing further to the elementary pointwise statement

`integral g(x-y)u(y)dy = constant`

still requires a regularity theorem identifying a completed kernel vector
with an ordinary mean-zero L2 representative.  That assertion is no longer
silently included in Stage 1.  It is now a separate Stage-2 regularity and
defect-characterization question.
