/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic
import FullInfTransfer

/-!
# Uniform support transfer from relative adjacent-step bounds

This file isolates an abstract mechanism for propagating positivity through
arbitrarily large support parameters.  Along a cofinal sequence of support
scales, it is enough to bound each new value below by a *positive* multiple of
the preceding value.  The factors need not have a common positive lower bound,
and no infinite product is used: reaching any fixed scale requires only a
finite product of positive factors.

The intended application is to a lowest spectral value indexed by support.
The analytic work in such an application is precisely the adjacent-step
relative bound; the results below contain no claim that this bound already
holds for the Weil form.
-/

namespace RHBridge.UniformSupportTransfer

open scoped BigOperators

/-! ## Finite two-block margins -/

/-- A conservative explicit lower margin for a positive two-by-two block
matrix with diagonal bounds `beta`, `d` and cross bound `c`. -/
noncomputable def schurMargin (beta d c : ℝ) : ℝ :=
  (beta * d - c ^ 2) / (2 * (beta + d))

/-- The explicit Schur margin is positive and satisfies all three strict
inequalities required by `FullInfTransfer.starProjection_strict_lower_bound`.
-/
theorem schurMargin_spec
    (beta d c : ℝ)
    (hbeta : 0 < beta)
    (hd : 0 < d)
    (hdet : c ^ 2 < beta * d) :
    0 < schurMargin beta d c ∧
      schurMargin beta d c < beta ∧
      schurMargin beta d c < d ∧
      c ^ 2 < (beta - schurMargin beta d c) *
        (d - schurMargin beta d c) := by
  let gamma := schurMargin beta d c
  have hsum : 0 < beta + d := add_pos hbeta hd
  have hden : 0 < 2 * (beta + d) := mul_pos (by norm_num) hsum
  have hgap : 0 < beta * d - c ^ 2 := sub_pos.mpr hdet
  have hgamma_pos : 0 < gamma := by
    exact div_pos hgap hden
  have hgamma_beta : gamma < beta := by
    apply (div_lt_iff₀ hden).2
    nlinarith [sq_nonneg c, mul_pos hbeta hd, sq_pos_of_pos hbeta]
  have hgamma_d : gamma < d := by
    apply (div_lt_iff₀ hden).2
    nlinarith [sq_nonneg c, mul_pos hbeta hd, sq_pos_of_pos hd]
  have hrelation : 2 * (beta + d) * gamma = beta * d - c ^ 2 := by
    dsimp [gamma, schurMargin]
    field_simp
  have hshifted :
      c ^ 2 < (beta - gamma) * (d - gamma) := by
    nlinarith [sq_nonneg gamma]
  exact ⟨hgamma_pos, hgamma_beta, hgamma_d, hshifted⟩

/-- Orthogonal-projection transfer with an automatically selected, explicitly
positive Schur margin.  Thus an application needs only positive diagonal
bounds and the unshifted determinant inequality `c² < beta * d`. -/
theorem starProjection_strict_lower_bound_of_positive_determinant
    {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ)
    (U : Submodule ℝ E)
    [U.HasOrthogonalProjection]
    (beta d c : ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hfinite : ∀ u ∈ U, beta * ‖u‖ ^ 2 ≤ B u u)
    (hcomplement : ∀ w ∈ Uᗮ, d * ‖w‖ ^ 2 ≤ B w w)
    (hcross : ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ c * ‖u‖ * ‖w‖)
    (hbeta : 0 < beta)
    (hd : 0 < d)
    (hdet : c ^ 2 < beta * d)
    {f : E} (hf : f ≠ 0) :
    schurMargin beta d c * ‖f‖ ^ 2 < B f f := by
  obtain ⟨_, hmargin_beta, hmargin_d, hmargin_det⟩ :=
    schurMargin_spec beta d c hbeta hd hdet
  exact FullInfTransfer.starProjection_strict_lower_bound
    B U beta d c (schurMargin beta d c) hsymm hfinite hcomplement hcross
      hmargin_beta hmargin_d hmargin_det hf

/-! ## Translation-energy identity -/

/-- A finite weighted sum of autocorrelation shifts is exactly a nonlocal
Dirichlet energy minus a scalar mass term.  Only norm preservation of each
shift is used; linearity is not needed for this algebraic identity. -/
theorem weighted_shift_energy_identity
    {E I : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (indices : Finset I)
    (weight : I → ℝ)
    (shift : I → E → E)
    (hnorm : ∀ i ∈ indices, ∀ x, ‖shift i x‖ = ‖x‖)
    (x : E) :
    (∑ i ∈ indices, -2 * weight i * inner ℝ x (shift i x)) =
      (∑ i ∈ indices, weight i * ‖x - shift i x‖ ^ 2) -
        2 * (∑ i ∈ indices, weight i) * ‖x‖ ^ 2 := by
  have hpointwise : ∀ i ∈ indices,
      -2 * weight i * inner ℝ x (shift i x) =
        weight i * ‖x - shift i x‖ ^ 2 -
          2 * weight i * ‖x‖ ^ 2 := by
    intro i hi
    rw [norm_sub_sq_real, hnorm i hi x]
    ring
  calc
    (∑ i ∈ indices, -2 * weight i * inner ℝ x (shift i x)) =
        ∑ i ∈ indices,
          (weight i * ‖x - shift i x‖ ^ 2 -
            2 * weight i * ‖x‖ ^ 2) := by
      apply Finset.sum_congr rfl
      intro i hi
      exact hpointwise i hi
    _ = (∑ i ∈ indices, weight i * ‖x - shift i x‖ ^ 2) -
          (∑ i ∈ indices, 2 * weight i * ‖x‖ ^ 2) := by
      rw [Finset.sum_sub_distrib]
    _ = (∑ i ∈ indices, weight i * ‖x - shift i x‖ ^ 2) -
          2 * (∑ i ∈ indices, weight i) * ‖x‖ ^ 2 := by
      congr 1
      calc
        (∑ i ∈ indices, 2 * weight i * ‖x‖ ^ 2) =
            ∑ i ∈ indices, weight i * (2 * ‖x‖ ^ 2) := by
          apply Finset.sum_congr rfl
          intro i hi
          ring
        _ = (∑ i ∈ indices, weight i) * (2 * ‖x‖ ^ 2) := by
          rw [Finset.sum_mul]
        _ = 2 * (∑ i ∈ indices, weight i) * ‖x‖ ^ 2 := by ring

/-! ## Qualitative nondegeneracy route -/

/-- On a connected parameter space, a continuous real-valued function that is
positive at one point and never vanishes is positive everywhere.

For a lowest spectral value, this packages the qualitative alternative to a
quantitative glide estimate: continuity plus nondegeneracy at every finite
support rules out a sign change. -/
theorem positive_everywhere_of_continuous_ne_zero
    {S : Type*} [TopologicalSpace S] [PreconnectedSpace S]
    (value : S → ℝ)
    (hcontinuous : Continuous value)
    (base : S)
    (hbase : 0 < value base)
    (hne : ∀ s, value s ≠ 0) :
    ∀ s, 0 < value s := by
  intro s
  by_contra hpositive
  have hs_nonpos : value s ≤ 0 := le_of_not_gt hpositive
  have hs_neg : value s < 0 := lt_of_le_of_ne hs_nonpos (hne s)
  have hzero_range : 0 ∈ Set.range value :=
    intermediate_value_univ s base hcontinuous
      ⟨hs_neg.le, hbase.le⟩
  obtain ⟨z, hz⟩ := hzero_range
  exact hne z hz

/-- Iterating nonnegative multiplicative adjacent-step estimates gives the
corresponding finite-product lower bound. -/
theorem finite_product_lower_bound
    (value factor : ℕ → ℝ)
    (hfactor : ∀ n, 0 ≤ factor n)
    (hstep : ∀ n, factor n * value n ≤ value (n + 1))
    (n : ℕ) :
    (∏ k ∈ Finset.range n, factor k) * value 0 ≤ value n := by
  induction n with
  | zero => simp
  | succ n ih =>
      calc
        (∏ k ∈ Finset.range (n + 1), factor k) * value 0 =
            factor n * ((∏ k ∈ Finset.range n, factor k) * value 0) := by
          rw [Finset.prod_range_succ]
          ac_rfl
        _ ≤ factor n * value n :=
          mul_le_mul_of_nonneg_left ih (hfactor n)
        _ ≤ value (n + 1) := hstep n

/-- Positive initial data stay positive under positive multiplicative
adjacent-step estimates.  This conclusion is pointwise in `n`; it requires no
uniform lower bound for `factor` and no assertion about its infinite product. -/
theorem positive_nat_of_multiplicative_steps
    (value factor : ℕ → ℝ)
    (hbase : 0 < value 0)
    (hfactor : ∀ n, 0 < factor n)
    (hstep : ∀ n, factor n * value n ≤ value (n + 1)) :
    ∀ n, 0 < value n := by
  intro n
  have hprod : 0 < ∏ k ∈ Finset.range n, factor k :=
    Finset.prod_pos fun k _ ↦ hfactor k
  exact lt_of_lt_of_le (mul_pos hprod hbase)
    (finite_product_lower_bound value factor
      (fun k ↦ (hfactor k).le) hstep n)

/-- Quantitative finite-product bound along a selected sequence of scales. -/
theorem cofinal_sequence_finite_product_lower_bound
    {S : Type*}
    (scale : ℕ → S)
    (value : S → ℝ)
    (factor : ℕ → ℝ)
    (hfactor : ∀ n, 0 ≤ factor n)
    (hstep : ∀ n,
      factor n * value (scale n) ≤ value (scale (n + 1)))
    (n : ℕ) :
    (∏ k ∈ Finset.range n, factor k) * value (scale 0) ≤
      value (scale n) := by
  exact finite_product_lower_bound (fun k ↦ value (scale k)) factor
    hfactor hstep n

/-- If `value` is antitone in the support parameter, positivity along a
cofinal sequence implies positivity at every support parameter.  Relative
adjacent-step bounds supply positivity along that sequence.

This is the qualitative uniform-in-support mechanism: every requested support
is covered after finitely many positive multipliers, even when those
multipliers approach zero. -/
theorem positive_everywhere_of_cofinal_multiplicative
    {S : Type*} [Preorder S]
    (scale : ℕ → S)
    (value : S → ℝ)
    (factor : ℕ → ℝ)
    (hcofinal : ∀ s, ∃ n, s ≤ scale n)
    (hantitone : Antitone value)
    (hbase : 0 < value (scale 0))
    (hfactor : ∀ n, 0 < factor n)
    (hstep : ∀ n,
      factor n * value (scale n) ≤ value (scale (n + 1))) :
    ∀ s, 0 < value s := by
  have hsequence : ∀ n, 0 < value (scale n) :=
    positive_nat_of_multiplicative_steps
      (fun n ↦ value (scale n)) factor hbase hfactor hstep
  intro s
  obtain ⟨n, hsn⟩ := hcofinal s
  exact lt_of_lt_of_le (hsequence n) (hantitone hsn)

/-- Loss-form version of `positive_everywhere_of_cofinal_multiplicative`.
The adjacent multiplier is `1 - loss n`; the sole sign requirement is
`loss n < 1`.  In particular, neither a uniform gap below one nor summability
of the losses is needed. -/
theorem positive_everywhere_of_cofinal_relative_loss
    {S : Type*} [Preorder S]
    (scale : ℕ → S)
    (value : S → ℝ)
    (loss : ℕ → ℝ)
    (hcofinal : ∀ s, ∃ n, s ≤ scale n)
    (hantitone : Antitone value)
    (hbase : 0 < value (scale 0))
    (hloss : ∀ n, loss n < 1)
    (hstep : ∀ n,
      (1 - loss n) * value (scale n) ≤ value (scale (n + 1))) :
    ∀ s, 0 < value s := by
  apply positive_everywhere_of_cofinal_multiplicative
    scale value (fun n ↦ 1 - loss n) hcofinal hantitone hbase
  · exact fun n ↦ sub_pos.mpr (hloss n)
  · exact hstep

/-- Strict positivity of a family of forms is also preserved by pointwise
positive multiplicative adjacent-step estimates. -/
def StrictlyPositive {X : Type*} [Zero X] (form : X → ℝ) : Prop :=
  ∀ x, x ≠ 0 → 0 < form x

/-- Form-level version of `positive_nat_of_multiplicative_steps`. -/
theorem strictlyPositive_nat_of_multiplicative_steps
    {X : Type*} [Zero X]
    (form : ℕ → X → ℝ)
    (factor : ℕ → ℝ)
    (hbase : StrictlyPositive (form 0))
    (hfactor : ∀ n, 0 < factor n)
    (hstep : ∀ n x, factor n * form n x ≤ form (n + 1) x) :
    ∀ n, StrictlyPositive (form n) := by
  intro n x hx
  exact positive_nat_of_multiplicative_steps
    (fun k ↦ form k x) factor (hbase x hx) hfactor (fun k ↦ hstep k x) n

end RHBridge.UniformSupportTransfer
