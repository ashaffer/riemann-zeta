/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.BoundaryPhaseCoherence
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-!
# Clark atoms versus fixed-vector spectral weights

The upper-half-plane Clark atom at a phase crossing is

`2 * pi / Phi' = pi * (1+x^2) * rho^2`.

It is not, by itself, the scalar spectral mass seen by a fixed Hilbert-space
vector.  For the normalized reference defect vector, the Cauchy boundary
factor divides the Clark atom by `pi * (1+x^2)`, leaving exactly `rho^2`.
This file checks that normalization and the resulting local-density
cancellation.

The final scalar definitions record a second distinction used in the Suzuki
limit audit.  A fixed negative energy shift adds `(-sigma) * ||f||_2^2` to
the total spectral mass of a core vector.  Identifying that term with an
absolutely continuous Fourier spectral measure uses Plancherel and the global
zero-frame representation; those analytic inputs are stated in the companion
report and are not asserted by this scalar module.
-/

namespace RHBridge.ClarkSpectralWeight

open RHBridge.BoundaryPhaseCoherence

/-- Scalar spectral atom of the normalized reference defect vector. -/
noncomputable def referenceAtomFromCoherence (rhoSq : ℝ) : ℝ := rhoSq

/-- Convert a Clark-measure atom to the spectral atom of the normalized
reference defect vector by the upper-half-plane Cauchy boundary factor. -/
noncomputable def referenceAtomFromClark (x clarkAtom : ℝ) : ℝ :=
  clarkAtom / (Real.pi * (1 + x ^ 2))

/-- The fixed-reference spectral atom is exactly the squared normalized
defect-line coherence. -/
theorem referenceAtomFromClark_eq_coherence
    (x rhoSq : ℝ) :
    referenceAtomFromClark x (clarkWeightFromCoherence x rhoSq) =
      referenceAtomFromCoherence rhoSq := by
  unfold referenceAtomFromClark clarkWeightFromCoherence
    referenceAtomFromCoherence
  have hpi : Real.pi ≠ 0 := Real.pi_ne_zero
  have hx : 1 + x ^ 2 ≠ 0 := by positivity
  field_simp

/-- Formal phase-level density: one crossing per `2*pi` units of phase. -/
noncomputable def phaseLevelDensity (x rhoSq : ℝ) : ℝ :=
  densityFromCoherence x rhoSq / (2 * Real.pi)

/-- Product of phase-level density with the reference-vector atom.  Calling
this an actual limiting density additionally requires a mesh/Riemann-sum
theorem; the definition isolates only its exact scalar integrand. -/
noncomputable def formalReferenceMassDensity (x rhoSq : ℝ) : ℝ :=
  phaseLevelDensity x rhoSq * referenceAtomFromCoherence rhoSq

/-- Root crowding and shrinking reference weights cancel algebraically to the
universal Cauchy density. -/
theorem formalReferenceMassDensity_eq_cauchy
    {x rhoSq : ℝ} (hrho : rhoSq ≠ 0) :
    formalReferenceMassDensity x rhoSq =
      1 / (Real.pi * (1 + x ^ 2)) := by
  unfold formalReferenceMassDensity phaseLevelDensity
    referenceAtomFromCoherence densityFromCoherence
  have hpi : Real.pi ≠ 0 := Real.pi_ne_zero
  have hx : 1 + x ^ 2 ≠ 0 := by positivity
  field_simp

/-- Total spectral mass added to a core vector by the energy shift
`Q - sigma * ||.||_2^2`. -/
def continuousShiftMass (sigma l2Mass : ℝ) : ℝ :=
  -sigma * l2Mass

/-- Pure zero-frame mass plus the mass contributed by a fixed energy shift. -/
def shiftedSpectralMass (zeroFrameMass sigma l2Mass : ℝ) : ℝ :=
  zeroFrameMass + continuousShiftMass sigma l2Mass

/-- A strictly negative fixed shift contributes strictly positive mass to
every nonzero core vector. -/
theorem continuousShiftMass_pos
    {sigma l2Mass : ℝ} (hsigma : sigma < 0) (hl2 : 0 < l2Mass) :
    0 < continuousShiftMass sigma l2Mass := by
  unfold continuousShiftMass
  exact mul_pos (neg_pos.mpr hsigma) hl2

/-- For a nonzero core vector, the shift contribution vanishes exactly when
the shift itself vanishes. -/
theorem continuousShiftMass_eq_zero_iff
    {sigma l2Mass : ℝ} (hl2 : l2Mass ≠ 0) :
    continuousShiftMass sigma l2Mass = 0 ↔ sigma = 0 := by
  unfold continuousShiftMass
  rw [mul_eq_zero]
  simp [hl2]

/-- A fixed negative shift makes the total scalar spectral mass strictly
larger than its pure zero-frame part. -/
theorem zeroFrameMass_lt_shiftedSpectralMass
    {zeroFrameMass sigma l2Mass : ℝ}
    (hsigma : sigma < 0) (hl2 : 0 < l2Mass) :
    zeroFrameMass < shiftedSpectralMass zeroFrameMass sigma l2Mass := by
  unfold shiftedSpectralMass
  exact lt_add_of_pos_right _ (continuousShiftMass_pos hsigma hl2)

end RHBridge.ClarkSpectralWeight
