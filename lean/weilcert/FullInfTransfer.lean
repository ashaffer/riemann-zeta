/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import CertFramework
import Mathlib.Analysis.InnerProductSpace.Projection.Basic

/-!
# Two-block coercivity transfer on real inner-product spaces

The hypotheses are block estimates for a symmetric bilinear form along an
orthogonal decomposition; the conclusions give strict or closed-form uniform
lower bounds on the whole vector.  This file contains no numerical enclosure
and no zeta-specific definition.
-/

namespace FullInfTransfer

open scoped RealInnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The Hilbert-space form of the strict two-by-two transfer.

`u` is the finite-dimensional component and `w` its orthogonal complement.
The assumptions bound the two diagonal blocks and the absolute value of the
cross block.  A positive shifted determinant then gives a strict uniform
lower bound for the sum. -/
theorem bilinear_two_block_strict_lower_bound
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (beta d c gamma : ℝ) (u w : E)
    (hsymm : ∀ x y, B x y = B y x)
    (horth : inner ℝ u w = 0)
    (hfinite : beta * ‖u‖ ^ 2 ≤ B u u)
    (hcomplement : d * ‖w‖ ^ 2 ≤ B w w)
    (hcross : |B u w| ≤ c * ‖u‖ * ‖w‖)
    (hbeta : gamma < beta) (hd : gamma < d)
    (hdet : c ^ 2 < (beta - gamma) * (d - gamma))
    (huw : u + w ≠ 0) :
    gamma * ‖u + w‖ ^ 2 < B (u + w) (u + w) := by
  have hpair : (‖u‖, ‖w‖) ≠ (0, 0) := by
    intro h
    have hu_norm : ‖u‖ = 0 := congrArg Prod.fst h
    have hw_norm : ‖w‖ = 0 := congrArg Prod.snd h
    have hu : u = 0 := norm_eq_zero.mp hu_norm
    have hw : w = 0 := norm_eq_zero.mp hw_norm
    exact huw (by simp [hu, hw])
  have hscalar := CertFramework.two_by_two_strict_lower_bound
    beta d c gamma ‖u‖ ‖w‖ hbeta hd hdet hpair
  have hcross_lower : -(c * ‖u‖ * ‖w‖) ≤ B u w := neg_le_of_abs_le hcross
  have hexpand :
      B (u + w) (u + w) = B u u + B u w + B w u + B w w := by
    simp [map_add]
    ring
  have hform :
      beta * ‖u‖ ^ 2 + d * ‖w‖ ^ 2 - 2 * c * ‖u‖ * ‖w‖
        ≤ B (u + w) (u + w) := by
    rw [hexpand, hsymm w u]
    nlinarith
  have hpythagoras : ‖u + w‖ ^ 2 = ‖u‖ ^ 2 + ‖w‖ ^ 2 := by
    rw [norm_add_sq_real, horth]
    ring
  rw [hpythagoras]
  exact hscalar.trans_le hform

/-- **Optimal two-block coercivity bound.**

This is the human-facing closed form of the transfer theorem.  It removes the
auxiliary target `gamma` and returns the sharp universal lower constant
`CertFramework.twoBlockLowerEigenvalue beta d c`, the smaller eigenvalue of
`[[beta, -c], [-c, d]]`.  Equality is allowed, so no nonzero hypothesis is
needed. -/
theorem bilinear_two_block_lower_bound_optimal
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (beta d c : ℝ) (u w : E)
    (hsymm : ∀ x y, B x y = B y x)
    (horth : inner ℝ u w = 0)
    (hfinite : beta * ‖u‖ ^ 2 ≤ B u u)
    (hcomplement : d * ‖w‖ ^ 2 ≤ B w w)
    (hcross : |B u w| ≤ c * ‖u‖ * ‖w‖) :
    CertFramework.twoBlockLowerEigenvalue beta d c * ‖u + w‖ ^ 2 ≤
      B (u + w) (u + w) := by
  have hscalar := CertFramework.two_by_two_lower_bound_optimal
    beta d c ‖u‖ ‖w‖
  have hcross_lower : -(c * ‖u‖ * ‖w‖) ≤ B u w :=
    neg_le_of_abs_le hcross
  have hexpand :
      B (u + w) (u + w) = B u u + B u w + B w u + B w w := by
    simp [map_add]
    ring
  have hform :
      beta * ‖u‖ ^ 2 + d * ‖w‖ ^ 2 - 2 * c * ‖u‖ * ‖w‖ ≤
        B (u + w) (u + w) := by
    rw [hexpand, hsymm w u]
    nlinarith
  have hpythagoras : ‖u + w‖ ^ 2 = ‖u‖ ^ 2 + ‖w‖ ^ 2 := by
    rw [norm_add_sq_real, horth]
    ring
  rw [hpythagoras]
  exact hscalar.trans hform

/-- A decomposition-oriented wrapper around
`bilinear_two_block_strict_lower_bound`.

This is convenient for an orthogonal projection: `split f` can be instantiated
as `(P f, f - P f)`.  No continuity or finite-dimensionality is needed for the
algebraic transfer itself; those properties enter only when proving the block
hypotheses. -/
theorem bilinear_decomposition_strict_lower_bound
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (split : E → E × E)
    (beta d c gamma : ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hsum : ∀ f, f = (split f).1 + (split f).2)
    (horth : ∀ f, inner ℝ (split f).1 (split f).2 = 0)
    (hfinite : ∀ f, beta * ‖(split f).1‖ ^ 2 ≤ B (split f).1 (split f).1)
    (hcomplement : ∀ f, d * ‖(split f).2‖ ^ 2 ≤ B (split f).2 (split f).2)
    (hcross : ∀ f, |B (split f).1 (split f).2|
      ≤ c * ‖(split f).1‖ * ‖(split f).2‖)
    (hbeta : gamma < beta) (hd : gamma < d)
    (hdet : c ^ 2 < (beta - gamma) * (d - gamma))
    {f : E} (hf : f ≠ 0) : gamma * ‖f‖ ^ 2 < B f f := by
  have hsplit_ne : (split f).1 + (split f).2 ≠ 0 := by
    intro hzero
    apply hf
    rw [hsum f, hzero]
  have h := bilinear_two_block_strict_lower_bound
    B beta d c gamma (split f).1 (split f).2 hsymm (horth f)
    (hfinite f) (hcomplement f) (hcross f) hbeta hd hdet hsplit_ne
  rw [← hsum f] at h
  exact h

/-- Two-block transfer specialized to the canonical orthogonal projection onto
a subspace.

The theorem turns block estimates stated only on `U` and `Uᗮ` into a lower
bound for every nonzero vector in the ambient space.  For the Weil
application, `U` is the finite Legendre space.  Finite dimensionality is one
way to obtain the `HasOrthogonalProjection` instance, but is not needed by the
transfer theorem itself. -/
theorem starProjection_strict_lower_bound
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    [U.HasOrthogonalProjection] (beta d c gamma : ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hfinite : ∀ u ∈ U, beta * ‖u‖ ^ 2 ≤ B u u)
    (hcomplement : ∀ w ∈ Uᗮ, d * ‖w‖ ^ 2 ≤ B w w)
    (hcross : ∀ u ∈ U, ∀ w ∈ Uᗮ, |B u w| ≤ c * ‖u‖ * ‖w‖)
    (hbeta : gamma < beta) (hd : gamma < d)
    (hdet : c ^ 2 < (beta - gamma) * (d - gamma))
    {f : E} (hf : f ≠ 0) : gamma * ‖f‖ ^ 2 < B f f := by
  have hu : U.starProjection f ∈ U := U.starProjection_apply_mem f
  have hw : Uᗮ.starProjection f ∈ Uᗮ := Uᗮ.starProjection_apply_mem f
  have horth : inner ℝ (U.starProjection f) (Uᗮ.starProjection f) = 0 :=
    Submodule.inner_right_of_mem_orthogonal hu hw
  have hsum : U.starProjection f + Uᗮ.starProjection f = f :=
    U.starProjection_add_starProjection_orthogonal f
  have hsum_ne : U.starProjection f + Uᗮ.starProjection f ≠ 0 := by
    rw [hsum]
    exact hf
  have h := bilinear_two_block_strict_lower_bound B beta d c gamma
    (U.starProjection f) (Uᗮ.starProjection f) hsymm horth
    (hfinite _ hu) (hcomplement _ hw) (hcross _ hu _ hw)
    hbeta hd hdet hsum_ne
  rw [hsum] at h
  exact h

/-- Optimal closed-form transfer for the canonical decomposition
`f = P_U f + P_{Uᵮ} f`. -/
theorem starProjection_lower_bound_optimal
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    [U.HasOrthogonalProjection] (beta d c : ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hfinite : ∀ u ∈ U, beta * ‖u‖ ^ 2 ≤ B u u)
    (hcomplement : ∀ w ∈ Uᗮ, d * ‖w‖ ^ 2 ≤ B w w)
    (hcross : ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ c * ‖u‖ * ‖w‖)
    (f : E) :
    CertFramework.twoBlockLowerEigenvalue beta d c * ‖f‖ ^ 2 ≤ B f f := by
  have hu : U.starProjection f ∈ U := U.starProjection_apply_mem f
  have hw : Uᗮ.starProjection f ∈ Uᗮ := Uᗮ.starProjection_apply_mem f
  have horth : inner ℝ (U.starProjection f) (Uᗮ.starProjection f) = 0 :=
    Submodule.inner_right_of_mem_orthogonal hu hw
  have hsum : U.starProjection f + Uᗮ.starProjection f = f :=
    U.starProjection_add_starProjection_orthogonal f
  have h := bilinear_two_block_lower_bound_optimal B beta d c
    (U.starProjection f) (Uᗮ.starProjection f) hsymm horth
    (hfinite _ hu) (hcomplement _ hw) (hcross _ hu _ hw)
  rwa [hsum] at h

end FullInfTransfer
