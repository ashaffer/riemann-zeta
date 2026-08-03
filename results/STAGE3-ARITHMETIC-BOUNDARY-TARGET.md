# Stage 3: the quantitative collar obstruction is not the right target

## Decisive no-go check

A quantitative lower bound on collar norm does not, by itself, exclude a
first-crossing radical.  `Stage3BoundaryNoGo.lean` gives an axiom-free
two-dimensional countermodel:

- the old sector is strictly positive;
- the new boundary vector is nonzero and not inherited from the old sector;
- its collar coordinate has the fixed lower bound `1`;
- nevertheless it has zero energy and annihilates every variation.

Therefore no argument using only nested Hilbert spaces, collar mass, and
first-crossing positivity can finish Stage 3.  This remains true even if the
qualitative saturation theorem is upgraded to a uniform norm bound.

For actual `L2` functions, a fixed vector's mass in shrinking boundary collars
also tends to zero by absolute continuity of the integral.  Thus a positive
support-independent lower bound would be false in the intended model.

## Correct replacement

One initially plausible target is `ArithmeticBoundarySeparation`: every
support-saturating first-crossing candidate must admit a form-domain variation
for which the prime cross kernel differs from the combined pole and
archimedean cross kernels.  Lean proves that this statement implies RH.

This is stronger than a collar estimate because it couples boundary geometry
to the special zeta kernel.  It also exposes the technical issue hidden by a
sharp orthogonal collar: the projection need not preserve the logarithmic form
domain.

## Circularity audit

This target does **not** survive the parsimony audit.  A first-crossing vector
is already a weak radical, so its prime and pole--archimedean cross kernels are
equal for every form-domain variation.  Stage 3 automatically supplies the
collar premise.  Lean therefore proves

`ArithmeticBoundarySeparation` iff there is no positive-support
`FirstCrossingWithHistory`.

Consequently, proving a nonzero normalized residual for such a vector would
not be an intermediate analytic lemma: it would be the contradiction itself.
The honest remaining problem is to find additional independently provable
zeta structure that excludes the radical.  Neither qualitative nor
quantitative collar mass supplies that structure.

Suzuki's 2026 paper proves continuity of the lowest eigenvalue in the support
parameter.  That result produces a zero crossing if RH fails; it does not give
a shape derivative or boundary-flux sign capable of excluding the crossing.
