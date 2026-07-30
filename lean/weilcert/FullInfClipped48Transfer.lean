/-
Composition of the real clipped-block certificate with the abstract F8
orthogonal-projection theorem.
-/
import FullInfClipped48Real
import FullInfTransfer

namespace FullInfClipped48Transfer

open Matrix
open scoped RealInnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The exact 48-dimensional interval certificate, expressed as a reusable
finite-subspace lower bound.  This separates the matrix-to-form bridge from
the subsequent orthogonal-complement transfer. -/
theorem finite_lower_bound_of_clipped48_intervals
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    (Me Mo : Matrix (Fin 24) (Fin 24) ℝ)
    (coordEven coordOdd : E → Fin 24 → ℝ)
    (hnorm : ∀ u ∈ U,
      ‖u‖ ^ 2 = coordEven u ⬝ᵥ coordEven u +
        coordOdd u ⬝ᵥ coordOdd u)
    (hform : ∀ u ∈ U,
      B u u = coordEven u ⬝ᵥ Me *ᵥ coordEven u +
        coordOdd u ⬝ᵥ Mo *ᵥ coordOdd u)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤ Me i j ∧
        Me i j ≤ FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤ Mo i j ∧
        Mo i j ≤ FullInfClipped48Real.oddUpperReal i j) :
    ∀ u ∈ U, (227 / 10 ^ 7 : ℝ) * ‖u‖ ^ 2 ≤ B u u := by
  intro u hu
  by_cases hu0 : u = 0
  · simp [hu0]
  · have hcoords : (coordEven u, coordOdd u) ≠ (0, 0) := by
      intro hzero
      have he0 : coordEven u = 0 := congrArg Prod.fst hzero
      have ho0 : coordOdd u = 0 := congrArg Prod.snd hzero
      have hn := hnorm u hu
      rw [he0, ho0] at hn
      simp only [dotProduct_zero, zero_add] at hn
      have hnu : ‖u‖ = 0 := by nlinarith [norm_nonneg u]
      exact hu0 (norm_eq_zero.mp hnu)
    have hcert :=
      FullInfClipped48Real.clipped48IntervalLowerBoundReal
        Me Mo he ho (coordEven u) (coordOdd u) hcoords
    rw [← hnorm u hu, ← hform u hu] at hcert
    norm_num [FullInfClipped48.beta] at hcert ⊢
    exact hcert.le

/-- The L=7/4 finite certificate and F8 ledger, composed in the kernel.

The coordinate hypotheses say that the chosen finite subspace is isometric to
the two parity-reordered 24-dimensional coordinate blocks and that the
restriction of `B` is represented by `Me ⊕ Mo`.  The interval hypotheses then
discharge F8's finite-block estimate using `FullInfClipped48Real`; only the
complement and cross estimates remain as explicit analytic assumptions. -/
theorem p2_projection_lower_bound_of_clipped48_intervals
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    [U.HasOrthogonalProjection]
    (Me Mo : Matrix (Fin 24) (Fin 24) ℝ)
    (coordEven coordOdd : E → Fin 24 → ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hnorm : ∀ u ∈ U,
      ‖u‖ ^ 2 = coordEven u ⬝ᵥ coordEven u +
        coordOdd u ⬝ᵥ coordOdd u)
    (hform : ∀ u ∈ U,
      B u u = coordEven u ⬝ᵥ Me *ᵥ coordEven u +
        coordOdd u ⬝ᵥ Mo *ᵥ coordOdd u)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤ Me i j ∧
        Me i j ≤ FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤ Mo i j ∧
        Mo i j ≤ FullInfClipped48Real.oddUpperReal i j)
    (hcomplement : ∀ w ∈ Uᗮ,
      (1093 / 1000 : ℝ) * ‖w‖ ^ 2 ≤ B w w)
    (hcross : ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ (212 / 10 ^ 12 : ℝ) * ‖u‖ * ‖w‖)
    {f : E} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  have hfinite := finite_lower_bound_of_clipped48_intervals
    B U Me Mo coordEven coordOdd hnorm hform he ho
  exact FullInfTransfer.fullinf_p2_projection_lower_bound
    B U hsymm hfinite hcomplement hcross hf

end FullInfClipped48Transfer
