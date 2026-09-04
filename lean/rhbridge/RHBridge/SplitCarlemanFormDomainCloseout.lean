/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Finite algebra for the split-Carleman/form-domain closeout

This file checks only the algebraic skeleton of the corrected old-interval
serialization:

* the unweighted and inverse-root-weighted fourth-root partial fractions;
* cancellation of a common two-sided finite-part counterterm;
* the resulting sign of the local completion term; and
* equivalence between an operator kernel and its weak inner-product radical.

It does **not** formalize the Hurwitz--Lerch kernel, Hadamard finite parts,
the cutoff limit, the desingularized Carleman integral, Suzuki's closed form
or Friedrichs extension, density of a form core, collar boundedness, Cauchy
boundary values, prime-power dilation sums, KNC, a completed-source factor,
a zero-free strip, the four-cycle bound, or RH.  The last two theorems below
are abstract Hilbert-space logic only; they do not instantiate Suzuki's
analytic operator.
-/

namespace RHBridge.SplitCarlemanFormDomainCloseout

/-- The fourth-root partial fraction used below the diagonal.  The explicit
nonvanishing hypotheses merely license division; analytically they correspond
to staying off the four rotated cuts. -/
theorem fourthRoot_unweighted_partialFraction
    (X Y : ℂ)
    (hsub : X - Y ≠ 0) (hadd : X + Y ≠ 0)
    (hsubI : X - Y * Complex.I ≠ 0)
    (haddI : X + Y * Complex.I ≠ 0)
    (hquartic : X ^ 4 - Y ^ 4 ≠ 0) :
    1 / (X - Y) + 1 / (X + Y) +
        1 / (X - Y * Complex.I) + 1 / (X + Y * Complex.I) =
      4 * X ^ 3 / (X ^ 4 - Y ^ 4) := by
  field_simp [hsub, hadd, hsubI, haddI, hquartic]
  ring_nf
  rw [Complex.I_sq]
  ring

/-- The inverse-root-weighted fourth-root partial fraction used above the
diagonal.  Its numerator is `4 * X * Y^2`, rather than the unweighted
`4 * Y^3`; this is the orientation-sensitive weight in the old operator. -/
theorem fourthRoot_inverseWeighted_partialFraction
    (X Y : ℂ)
    (hsub : Y - X ≠ 0) (hadd : Y + X ≠ 0)
    (hsubI : Y - X * Complex.I ≠ 0)
    (haddI : Y + X * Complex.I ≠ 0)
    (hquartic : Y ^ 4 - X ^ 4 ≠ 0) :
    1 / (Y - X) - 1 / (Y + X) -
        Complex.I / (Y - X * Complex.I) +
        Complex.I / (Y + X * Complex.I) =
      4 * X * Y ^ 2 / (Y ^ 4 - X ^ 4) := by
  field_simp [hsub, hadd, hsubI, haddI, hquartic]
  ring_nf
  rw [Complex.I_sq]
  ring

/-- Abstract form of the exact two-sided counterterm cancellation.  If the
left and right truncated kernel masses are `(cutoff-leftEndpoint)/2` and
`(cutoff-rightEndpoint)/2`, subtracting the one common counterterm leaves
minus one half of the two endpoint values. -/
theorem twoSided_counterterm_cancel
    (cutoff leftEndpoint rightEndpoint : ℝ) :
    (cutoff - leftEndpoint) / 2 + (cutoff - rightEndpoint) / 2 - cutoff =
      -(leftEndpoint + rightEndpoint) / 2 := by
  ring

/-- Since the completed old operator contains `local - Lerch`, the preceding
counterterm identity changes the surviving local coefficient from `local` to
`local + (leftEndpoint + rightEndpoint)/2`. -/
theorem localCompletion_after_counterterm
    (localTerm cutoff leftEndpoint rightEndpoint : ℝ) :
    localTerm -
        ((cutoff - leftEndpoint) / 2 +
          (cutoff - rightEndpoint) / 2 - cutoff) =
      localTerm + (leftEndpoint + rightEndpoint) / 2 := by
  ring

section WeakRadical

variable {𝕜 E F : Type*} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F]

/-- A vector is in the weak inner-product radical of an operator exactly when
the operator kills it.  No positivity or self-adjointness is needed for this
Hilbert-space separation statement. -/
theorem weakRadical_iff_operatorKernel
    (A : E →L[𝕜] E) (x : E) :
    (∀ y : E, inner 𝕜 (A x) y = 0) ↔ A x = 0 := by
  constructor
  · intro h
    exact inner_self_eq_zero.mp (h (A x))
  · intro hx y
    simp [hx]

/-- Requiring a readout to vanish on every weak-radical state is exactly the
usual kernel-null-charge inclusion.  Thus changing from operator language to
weak-form language does not lower the logical strength of KNC. -/
theorem weakRadical_readout_iff_kernelNullCharge
    (A : E →L[𝕜] E) (readout : E →L[𝕜] F) :
    (∀ x : E, (∀ y : E, inner 𝕜 (A x) y = 0) → readout x = 0) ↔
      ∀ x : E, A x = 0 → readout x = 0 := by
  constructor
  · intro h x hx
    apply h x
    intro y
    simp [hx]
  · intro h x hradical
    apply h x
    exact (weakRadical_iff_operatorKernel A x).mp hradical

end WeakRadical

end RHBridge.SplitCarlemanFormDomainCloseout
