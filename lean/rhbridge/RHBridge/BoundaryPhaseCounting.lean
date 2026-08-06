/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Int.Interval
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Boundary-phase counting and the non-uniform Weyl obstruction

For a strictly monotone real lift `phase` of a unit-circle boundary
characteristic, the eigenvalues of a fixed self-adjoint extension occur when
`phase = theta` modulo `2 * pi`.  On a half-open interval, their exact count is
therefore a difference of floors.  This file isolates the scalar part of that
operator-theoretic statement and proves that the count differs from normalized
phase variation by less than one.

The second part records a small but important quantifier warning.  Spectra can
have gap exactly `1 / a` after an onset at `a^2`.  Thus their high-energy
density grows with `a`, while every fixed compact can still be empty for large
`a`.  A fixed-support Weyl law consequently says nothing about the
support-uniform compact counts needed in a varying-window limit unless its
onset or remainder is controlled uniformly.
-/

namespace RHBridge.BoundaryPhaseCounting

/-- The integer obtained by counting lifted phase levels in a half-open
interval.  If `phaseLeft < phaseRight`, this is the number of integers `k`
such that

`phaseLeft < theta + 2 * pi * k <= phaseRight`.

The set-theoretic identification is the standard boundary-phase input; the
definition here keeps only its exact scalar output. -/
noncomputable def liftedPhaseCount
    (phaseLeft phaseRight theta : ℝ) : ℤ :=
  ⌊(phaseRight - theta) / (2 * Real.pi)⌋ -
    ⌊(phaseLeft - theta) / (2 * Real.pi)⌋

/-- The finite interval of lifted phase levels occurring between two endpoint
phases. -/
noncomputable def liftedPhaseLevels
    (phaseLeft phaseRight theta : ℝ) : Finset ℤ :=
  Finset.Ioc
    ⌊(phaseLeft - theta) / (2 * Real.pi)⌋
    ⌊(phaseRight - theta) / (2 * Real.pi)⌋

/-- Membership in `liftedPhaseLevels` is exactly the half-open phase-crossing
condition. -/
theorem mem_liftedPhaseLevels_iff
    {phaseLeft phaseRight theta : ℝ} {k : ℤ} :
    k ∈ liftedPhaseLevels phaseLeft phaseRight theta ↔
      phaseLeft < theta + (2 * Real.pi) * k ∧
        theta + (2 * Real.pi) * k ≤ phaseRight := by
  unfold liftedPhaseLevels
  simp only [Finset.mem_Ioc, Int.floor_lt, Int.le_floor]
  have hden : 0 < (2 * Real.pi : ℝ) := by positivity
  constructor
  · rintro ⟨hleft, hright⟩
    have hleft' := (div_lt_iff₀ hden).mp hleft
    have hright' := (le_div_iff₀ hden).mp hright
    constructor <;> linarith
  · rintro ⟨hleft, hright⟩
    constructor
    · apply (div_lt_iff₀ hden).mpr
      linarith
    · apply (le_div_iff₀ hden).mpr
      linarith

/-- The cardinality of the lifted phase-level interval is the nonnegative
part of the exact integer floor count. -/
theorem liftedPhaseLevels_card
    (phaseLeft phaseRight theta : ℝ) :
    (liftedPhaseLevels phaseLeft phaseRight theta).card =
      (liftedPhaseCount phaseLeft phaseRight theta).toNat := by
  simp [liftedPhaseLevels, liftedPhaseCount]

/-- A floor differs from its real argument by a quantity in `(-1, 0]`. -/
theorem floor_sub_self_mem (x : ℝ) :
    -1 < (⌊x⌋ : ℝ) - x ∧ (⌊x⌋ : ℝ) - x ≤ 0 := by
  constructor
  · have hx := Int.lt_floor_add_one x
    have hx' : x < (⌊x⌋ : ℝ) + 1 := by exact_mod_cast hx
    linarith
  · exact sub_nonpos.mpr (Int.floor_le x)

/-- The exact floor count differs from normalized phase variation by less
than one.  In particular, all support-uniform counting information is carried
by the support-uniform phase increment. -/
theorem liftedPhaseCount_error_lt_one
    (phaseLeft phaseRight theta : ℝ) :
    |(liftedPhaseCount phaseLeft phaseRight theta : ℝ) -
        (phaseRight - phaseLeft) / (2 * Real.pi)| < 1 := by
  let x := (phaseRight - theta) / (2 * Real.pi)
  let y := (phaseLeft - theta) / (2 * Real.pi)
  have hx := floor_sub_self_mem x
  have hy := floor_sub_self_mem y
  have hpi : (2 * Real.pi : ℝ) ≠ 0 := by positivity
  have hxy : x - y = (phaseRight - phaseLeft) / (2 * Real.pi) := by
    dsimp [x, y]
    field_simp
    ring
  rw [abs_lt]
  constructor <;>
    simp only [liftedPhaseCount, Int.cast_sub] <;>
    rw [← hxy] <;>
    dsimp only [x, y] at hx hy ⊢ <;>
    linarith

/-- Changing the extension phase changes a fixed interval count by less than
two as a real number.  Since the difference is integral, the next theorem
sharpens this to at most one. -/
theorem liftedPhaseCount_phase_difference_lt_two
    (phaseLeft phaseRight theta₁ theta₂ : ℝ) :
    |(liftedPhaseCount phaseLeft phaseRight theta₁ : ℝ) -
        (liftedPhaseCount phaseLeft phaseRight theta₂ : ℝ)| < 2 := by
  let q := (phaseRight - phaseLeft) / (2 * Real.pi)
  have h₁ := liftedPhaseCount_error_lt_one phaseLeft phaseRight theta₁
  have h₂ := liftedPhaseCount_error_lt_one phaseLeft phaseRight theta₂
  have h₁q :
      |(liftedPhaseCount phaseLeft phaseRight theta₁ : ℝ) - q| < 1 := by
    simpa [q] using h₁
  have h₂q :
      |(liftedPhaseCount phaseLeft phaseRight theta₂ : ℝ) - q| < 1 := by
    simpa [q] using h₂
  calc
    |(liftedPhaseCount phaseLeft phaseRight theta₁ : ℝ) -
        (liftedPhaseCount phaseLeft phaseRight theta₂ : ℝ)| =
        |((liftedPhaseCount phaseLeft phaseRight theta₁ : ℝ) - q) +
          (q - (liftedPhaseCount phaseLeft phaseRight theta₂ : ℝ))| := by
            congr 1
            ring
    _ ≤ |(liftedPhaseCount phaseLeft phaseRight theta₁ : ℝ) - q| +
        |q - (liftedPhaseCount phaseLeft phaseRight theta₂ : ℝ)| := abs_add_le _ _
    _ < 2 := by
      rw [abs_sub_comm q]
      linarith

/-- Counts from any two extension phases differ by at most one on the same
half-open phase interval. -/
theorem liftedPhaseCount_phase_difference_le_one
    (phaseLeft phaseRight theta₁ theta₂ : ℝ) :
    -1 ≤ liftedPhaseCount phaseLeft phaseRight theta₁ -
        liftedPhaseCount phaseLeft phaseRight theta₂ ∧
      liftedPhaseCount phaseLeft phaseRight theta₁ -
        liftedPhaseCount phaseLeft phaseRight theta₂ ≤ 1 := by
  have hreal :=
    liftedPhaseCount_phase_difference_lt_two
      phaseLeft phaseRight theta₁ theta₂
  rw [abs_lt] at hreal
  have hl : (-2 : ℤ) <
      liftedPhaseCount phaseLeft phaseRight theta₁ -
        liftedPhaseCount phaseLeft phaseRight theta₂ := by
    exact_mod_cast hreal.1
  have hr :
      liftedPhaseCount phaseLeft phaseRight theta₁ -
        liftedPhaseCount phaseLeft phaseRight theta₂ < (2 : ℤ) := by
    exact_mod_cast hreal.2
  omega

/-- A monotone lifted phase gives a nonnegative floor count. -/
theorem liftedPhaseCount_nonneg
    {phaseLeft phaseRight theta : ℝ} (hphase : phaseLeft ≤ phaseRight) :
    0 ≤ liftedPhaseCount phaseLeft phaseRight theta := by
  unfold liftedPhaseCount
  have hden : 0 < (2 * Real.pi : ℝ) := by positivity
  have hquot :
      (phaseLeft - theta) / (2 * Real.pi) ≤
        (phaseRight - theta) / (2 * Real.pi) := by
    exact div_le_div_of_nonneg_right (sub_le_sub_right hphase theta) hden.le
  exact sub_nonneg.mpr (Int.floor_mono hquot)

/-- For an increasing phase interval, the integer floor count is exactly the
cardinality of the corresponding finite set of phase levels. -/
theorem liftedPhaseLevels_card_cast
    {phaseLeft phaseRight theta : ℝ} (hphase : phaseLeft ≤ phaseRight) :
    ((liftedPhaseLevels phaseLeft phaseRight theta).card : ℤ) =
      liftedPhaseCount phaseLeft phaseRight theta := by
  rw [liftedPhaseLevels_card]
  exact Int.toNat_of_nonneg (liftedPhaseCount_nonneg hphase)

/-- A model spectrum with an onset at `a^2` and exact subsequent spacing
`1 / a`. -/
noncomputable def escapingSpectrum (a : ℝ) (n : ℕ) : ℝ :=
  a ^ 2 + n / a

/-- Consecutive levels in the escaping model have gap exactly `1 / a`. -/
theorem escapingSpectrum_succ_sub
    {a : ℝ} (ha : a ≠ 0) (n : ℕ) :
    escapingSpectrum a (n + 1) - escapingSpectrum a n = 1 / a := by
  unfold escapingSpectrum
  simp only [Nat.cast_add, Nat.cast_one]
  field_simp
  ring

/-- More generally, a block of `m` gaps has length exactly `m / a`. -/
theorem escapingSpectrum_add_sub
    {a : ℝ} (ha : a ≠ 0) (n m : ℕ) :
    escapingSpectrum a (n + m) - escapingSpectrum a n = m / a := by
  unfold escapingSpectrum
  simp only [Nat.cast_add]
  field_simp
  ring

/-- Despite its arbitrarily small high-energy gaps, the escaping model has no
level below a fixed threshold once its onset `a^2` has passed that threshold. -/
theorem escapingSpectrum_above_compact
    {a threshold : ℝ} (ha : 0 < a) (honset : threshold < a ^ 2) (n : ℕ) :
    threshold < escapingSpectrum a n := by
  unfold escapingSpectrum
  have hnonneg : 0 ≤ (n : ℝ) / a := div_nonneg (Nat.cast_nonneg n) ha.le
  linarith

end RHBridge.BoundaryPhaseCounting
