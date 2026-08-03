# Form-relative old--collar cross checkpoint

Status: the proposed contraction has been identified exactly; it is not a
consequence of support uncertainty alone.

Write the restriction of the Weil form to one old vector and one collar
vector as

`q(t) = A + 2 t C + t^2 D`,

where `A=Q(old)`, `D=Q(collar)`, and `C=B(old,collar)`.  For `A,D >= 0`, Lean
now proves the exact equivalence

`q(t) >= 0 for every real t  <->  C^2 <= A D`.

The reverse implication is the existing Schur argument.  The forward
implication evaluates at the minimizing direction `t=-C/D`, with the
degenerate `D=0` case handled separately.

This rules out a shortcut: proving the form-relative contraction for every
old/collar pair is exactly proving positivity on every corresponding mixed
plane.  Since those planes exhaust the enlarged form domain after a valid
decomposition, the desired universal contraction is the local block form of
the remaining positivity problem, not an independent uncertainty lemma.

Scale-uniform collar leakage remains useful.  It proves that the collar
diagonal grows in the arbitrarily thin regime and controls numerical Fourier
truncation.  It cannot create the factor `sqrt(Q(old))`, especially when the
old spectral margin is tiny.

Any non-circular continuation must therefore add genuinely arithmetic
structure.  Viable targets are narrower than the original request:

1. factor the *combined* pole--archimedean--prime cross kernel through a known
   positive old-form comparison operator;
2. prove the contraction first on a certified low-energy old spectral sector,
   since high old energy is controlled by ordinary Cauchy--Schwarz;
3. find an event-specific cancellation identity tying the prime cross term to
   the archimedean cross term.

Componentwise absolute-value estimates cannot close the determinant because
they discard precisely this required cancellation.
