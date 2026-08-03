# Zero-spacing/GUE bridge audit

## Verdict

Ordinary pair-correlation or GUE statistics do **not** imply RH and do not by
themselves give the deterministic lower frame bounds needed by this program.
The most direct pointwise strengthening does imply RH, but it is exactly RH
rephrased using the functional-equation symmetry.

## Three statements that must not be conflated

1. **Classical GUE/pair correlation.**  This is a normalized limiting law for
   differences of ordinates.  Montgomery's original formulation explicitly
   assumes RH and writes each zero as `1/2 + iγ`.  It is therefore unavailable
   as an unconditional input in that form.
2. **Unconditional projected GUE.**  One can instead project *all* nontrivial
   zeros to their ordinates, with multiplicity, and conjecture the same limiting
   correlations.  This avoids assuming RH syntactically, but still cannot prove
   RH: finitely many, or any zero-density family of, off-line quartets disappears
   after normalization by `N(T)`.
3. **Pointwise ordinate rigidity.**  Assert that distinct nontrivial zero
   locations never share an imaginary part.  If `ρ` is a zero, the functional
   equation and conjugation make `1-conj(ρ)` a zero with the same imaginary
   part.  Injectivity then gives `ρ=1-conj(ρ)`, hence `Re ρ=1/2`.  Conversely RH makes the ordinate map
   injective on distinct zero locations.  Thus this is equivalent to RH, not a
   simpler independent conjecture.  If formulated for zero *occurrences* rather
   than locations, it additionally includes simplicity.

The elementary implication and converse are kernel-checked in
`RHBridge/ZeroSpacingBridge.lean` for any reflection-closed set of complex
points.

## Why GUE does not produce the needed frame bound

Under RH, the zero side becomes the positive sampling energy

`sum_ρ m_ρ |F(γ)|²`.

Fourier-frame theorems characterize when a *deterministic real frequency set*
samples a Paley–Wiener space.  GUE correlation is only an averaged local
statistic.  It allows exceptional holes and clusters of zero density, while a
lower frame bound is a worst-case inequality over every bandlimited function.
Indeed the GUE model predicts arbitrarily small normalized gaps, not uniform
separation.  Additional all-interval discrepancy/hole estimates would be
needed to invoke sampling theory.

More importantly, even a perfect frame theorem for the **ordinates** cannot
identify the real parts.  Off the critical line the explicit-formula summand is
a product of transform values at two complex arguments, not the modulus square
at the real frequency `γ`.  Replacing that product by `|F(γ)|²` is precisely
the RH-dependent step already isolated in `RHZeroFrame.lean`.

## Exact candidate implication and its obstruction

A logically valid candidate is:

> (A) all nontrivial-zero ordinates form a deterministic sampling set for every
> required Paley–Wiener window; and (B) every zero summand equals its positive
> squared ordinate sample.  Then every windowed Weil form is nonnegative, hence
> RH by Weil's criterion.

Clause (A) is a genuine frame-analysis target.  Clause (B), however, says the
centered zero argument is purely imaginary (up to the same pointwise
factorization) and therefore contains RH.  Spacing information does not remove
this hidden dependence.

The only potentially non-circular statistical consequence is weaker: an
unconditional projected-GUE law whose test class detects the atom at zero could
force the **proportion** of off-line reflected pairs to tend to zero.  This is
far short of excluding the first or a sparse sequence of off-line zeros, and
so cannot close RH or yield positivity at every support.

## Primary sources

- H. L. Montgomery, *The pair correlation of zeros of the zeta function*,
  Proc. Sympos. Pure Math. 24 (1973), 181–193. The opening sentence explicitly
  assumes RH; equations (14)–(17) state the pair-correlation and gap predictions:
  <https://public.websites.umich.edu/~hlm/paircor1.pdf>
- Z. Rudnick and P. Sarnak, *Zeros of principal L-functions and random matrix
  theory*, Duke Math. J. 81 (1996), 269–322. Author publication record and paper:
  <https://www.math.tau.ac.il/~rudnick/pub.html>
- J. Ortega-Cerdà and K. Seip, *Fourier frames*, Ann. of Math. 155 (2002),
  789–806. This characterizes deterministic Fourier frames / Paley–Wiener
  sampling sequences; it is not a theorem turning pair correlation into a
  quantitative frame floor:
  <https://diposit.ub.edu/dspace/bitstream/2445/164422/1/506128.pdf>

## Recommendation

Do not use GUE as a proposed shortcut to RH positivity.  It remains useful as
a model for the *typical* near-null spectrum and for falsifying proposed margin
laws.  A proof route would need deterministic all-height control (especially
of exceptional holes) **and** an independent mechanism detecting horizontal
displacement of zeros; the latter, not vertical spacing, is the essential RH
content.
