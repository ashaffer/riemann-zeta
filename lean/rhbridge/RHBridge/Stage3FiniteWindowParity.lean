/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Finite-window parity reduction

For a reflection-invariant finite Weil matrix, simplicity plus nonvanishing of
the even boundary functional forces the lowest eigenvector to be even.  Thus
the two hypotheses in the CCM construction are not independent.
-/

namespace RHP2Bridge.Stage3FiniteWindowParity

variable {V : Type*} [AddCommGroup V] [Module ℂ V]

/-- Abstract finite-window parity lemma.  `simple` states one-dimensionality
of the relevant eigenspace in the only form needed here. -/
theorem even_of_simple_of_boundary_nonzero
    (T reflection : V →ₗ[ℂ] V) (boundary : V →ₗ[ℂ] ℂ)
    (eigenvalue : ℂ) (v : V)
    (heigen : T v = eigenvalue • v)
    (hcomm : T.comp reflection = reflection.comp T)
    (hsimple : ∀ w : V, T w = eigenvalue • w →
      ∃ c : ℂ, w = c • v)
    (hboundaryInvariant : boundary.comp reflection = boundary)
    (hboundary : boundary v ≠ 0) :
    reflection v = v := by
  have hrefEigen : T (reflection v) = eigenvalue • reflection v := by
    have hc := LinearMap.congr_fun hcomm v
    rw [LinearMap.comp_apply, LinearMap.comp_apply] at hc
    rw [hc, heigen, map_smul]
  obtain ⟨c, hc⟩ := hsimple (reflection v) hrefEigen
  have hb := LinearMap.congr_fun hboundaryInvariant v
  rw [LinearMap.comp_apply, hc, map_smul] at hb
  have hcOne : c = 1 := by
    apply mul_right_cancel₀ hboundary
    simpa using hb
  simpa [hcOne] using hc

end RHP2Bridge.Stage3FiniteWindowParity
