/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2DigammaTail

/-!
# Concrete Euler--Maclaurin telescopers for the canonical `p = 2` tail

This module supplies exact rational two-sided certificates for the fifteen
shifted power tails occurring in `quarterTailPolynomial r 16 64`.  Each
finite inverse-power polynomial `G` matches

`G(x) - G(x + 1) = x⁻ᵖ + O(x⁻ˢ⁻²)`

through the stated order.  Adding and subtracting one explicit `C / xˢ`
makes the residual numerator coefficientwise nonnegative for every `x > 0`.
The generic telescoping theorems in `P2DigammaTail` then turn these pointwise
identities into rational enclosures of the complete infinite sums.

All coefficient generation is untrusted preprocessing; `field_simp`, `ring_nf`,
and positivity check every residual in the Lean kernel.
-/

namespace RHP2Bridge

open Set

private noncomputable def shiftedPoint (N n : ℕ) : ℝ :=
  ((N + n : ℕ) : ℝ) + 1 / 4

private lemma summable_const_div_shiftedPoint_pow
    (c : ℝ) (p N : ℕ) (hp : 1 < p) :
    Summable (fun n : ℕ => c / (shiftedPoint N n) ^ p) := by
  have h := (summable_shiftedPowerTail p N hp).mul_left c
  simpa only [shiftedPoint, div_eq_mul_inv, one_div, one_mul] using h

private theorem shiftedPowerTail_mem_Icc_of_telescopers
    (p N : ℕ) (hp : 1 < p) (lower upper : ℝ → ℝ)
    (hlower : Summable (fun n : ℕ => lower (shiftedPoint N n)))
    (hupper : Summable (fun n : ℕ => upper (shiftedPoint N n)))
    (hlowerStep : ∀ x, 0 < x → lower x - lower (x + 1) ≤ 1 / x ^ p)
    (hupperStep : ∀ x, 0 < x → 1 / x ^ p ≤ upper x - upper (x + 1)) :
    shiftedPowerTail p N ∈
      Icc (lower ((N : ℝ) + 1 / 4)) (upper ((N : ℝ) + 1 / 4)) := by
  have hf := summable_shiftedPowerTail p N hp
  constructor
  · unfold shiftedPowerTail
    apply telescope_le_tsum
      (fun n : ℕ => 1 / (shiftedPoint N n) ^ p)
      (fun n : ℕ => lower (shiftedPoint N n)) hf hlower
    intro n
    have hpoint : shiftedPoint N (n + 1) = shiftedPoint N n + 1 := by
      unfold shiftedPoint
      push_cast
      ring
    rw [hpoint]
    exact hlowerStep (shiftedPoint N n) (by unfold shiftedPoint; positivity)
  · unfold shiftedPowerTail
    apply tsum_le_of_telescope
      (fun n : ℕ => 1 / (shiftedPoint N n) ^ p)
      (fun n : ℕ => upper (shiftedPoint N n)) hf hupper
    intro n
    have hpoint : shiftedPoint N (n + 1) = shiftedPoint N n + 1 := by
      unfold shiftedPoint
      push_cast
      ring
    rw [hpoint]
    exact hupperStep (shiftedPoint N n) (by unfold shiftedPoint; positivity)

/-! ## `p = 3`, truncation order `S = 18` -/

private noncomputable def emBase3 (x : ℝ) : ℝ :=
  (1 / 2) / x ^ 2 + (1 / 2) / x ^ 3 + (1 / 4) / x ^ 4 -
    (1 / 12) / x ^ 6 + (1 / 12) / x ^ 8 - (3 / 20) / x ^ 10 +
    (5 / 12) / x ^ 12 - (691 / 420) / x ^ 14 + (35 / 4) / x ^ 16 -
    (3617 / 60) / x ^ 18

private noncomputable def emLower3 (x : ℝ) : ℝ :=
  emBase3 x - 61 / x ^ 18

private noncomputable def emUpper3 (x : ℝ) : ℝ :=
  emBase3 x + 61 / x ^ 18

private lemma emLower3_step (x : ℝ) (hx : 0 < x) :
    emLower3 x - emLower3 (x + 1) ≤ 1 / x ^ 3 := by
  unfold emLower3 emBase3
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper3_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 3 ≤ emUpper3 x - emUpper3 (x + 1) := by
  unfold emUpper3 emBase3
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase3 :
    Summable (fun n : ℕ => emBase3 (shiftedPoint 64 n)) := by
  unfold emBase3
  have h2 := summable_const_div_shiftedPoint_pow (1 / 2) 2 64 (by norm_num)
  have h3 := summable_const_div_shiftedPoint_pow (1 / 2) 3 64 (by norm_num)
  have h4 := summable_const_div_shiftedPoint_pow (1 / 4) 4 64 (by norm_num)
  have h6 := summable_const_div_shiftedPoint_pow (1 / 12) 6 64 (by norm_num)
  have h8 := summable_const_div_shiftedPoint_pow (1 / 12) 8 64 (by norm_num)
  have h10 := summable_const_div_shiftedPoint_pow (3 / 20) 10 64 (by norm_num)
  have h12 := summable_const_div_shiftedPoint_pow (5 / 12) 12 64 (by norm_num)
  have h14 := summable_const_div_shiftedPoint_pow (691 / 420) 14 64 (by norm_num)
  have h16 := summable_const_div_shiftedPoint_pow (35 / 4) 16 64 (by norm_num)
  have h18 := summable_const_div_shiftedPoint_pow (3617 / 60) 18 64 (by norm_num)
  exact ((((((((h2.add h3).add h4).sub h6).add h8).sub h10).add h12).sub h14).add h16).sub h18

private lemma summable_emLower3 :
    Summable (fun n : ℕ => emLower3 (shiftedPoint 64 n)) := by
  unfold emLower3
  exact summable_emBase3.sub
    (summable_const_div_shiftedPoint_pow 61 18 64 (by norm_num))

private lemma summable_emUpper3 :
    Summable (fun n : ℕ => emUpper3 (shiftedPoint 64 n)) := by
  unfold emUpper3
  exact summable_emBase3.add
    (summable_const_div_shiftedPoint_pow 61 18 64 (by norm_num))

theorem shiftedPowerTail_three_mem_Icc :
    shiftedPowerTail 3 64 ∈
      Icc
        ((309007081774810679908522180756279161863848 : ℝ) /
          2511802677423326495097908712361030096114967145)
        ((309007081774810679908522181636575658852008 : ℝ) /
          2511802677423326495097908712361030096114967145) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 3 64 (by norm_num)
    emLower3 emUpper3 summable_emLower3 summable_emUpper3
    emLower3_step emUpper3_step
  norm_num [emLower3, emUpper3, emBase3] at h ⊢
  exact h

/-! ## `p = 5`, truncation order `S = 18` -/

private noncomputable def emBase5 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 4) / x ^ 4 +
    ((1 : ℝ) / 2) / x ^ 5 +
    ((5 : ℝ) / 12) / x ^ 6 -
    ((7 : ℝ) / 24) / x ^ 8 +
    ((1 : ℝ) / 2) / x ^ 10 -
    ((11 : ℝ) / 8) / x ^ 12 +
    ((65 : ℝ) / 12) / x ^ 14 -
    ((691 : ℝ) / 24) / x ^ 16 +
    ((595 : ℝ) / 3) / x ^ 18

private noncomputable def emLower5 (x : ℝ) : ℝ :=
  emBase5 x - 199 / x ^ 18

private noncomputable def emUpper5 (x : ℝ) : ℝ :=
  emBase5 x + 199 / x ^ 18

private lemma emLower5_step (x : ℝ) (hx : 0 < x) :
    emLower5 x - emLower5 (x + 1) ≤ 1 / x ^ 5 := by
  unfold emLower5 emBase5
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper5_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 5 ≤ emUpper5 x - emUpper5 (x + 1) := by
  unfold emUpper5 emBase5
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase5 :
    Summable (fun n : ℕ => emBase5 (shiftedPoint 64 n)) := by
  unfold emBase5
  have h4 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 4) 4 64 (by norm_num)
  have h5 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 5 64 (by norm_num)
  have h6 := summable_const_div_shiftedPoint_pow ((5 : ℝ) / 12) 6 64 (by norm_num)
  have h8 := summable_const_div_shiftedPoint_pow ((7 : ℝ) / 24) 8 64 (by norm_num)
  have h10 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 10 64 (by norm_num)
  have h12 := summable_const_div_shiftedPoint_pow ((11 : ℝ) / 8) 12 64 (by norm_num)
  have h14 := summable_const_div_shiftedPoint_pow ((65 : ℝ) / 12) 14 64 (by norm_num)
  have h16 := summable_const_div_shiftedPoint_pow ((691 : ℝ) / 24) 16 64 (by norm_num)
  have h18 := summable_const_div_shiftedPoint_pow ((595 : ℝ) / 3) 18 64 (by norm_num)
  exact ((((((((h4).add h5).add h6).sub h8).add h10).sub h12).add h14).sub h16).add h18

private lemma summable_emLower5 :
    Summable (fun n : ℕ => emLower5 (shiftedPoint 64 n)) := by
  unfold emLower5
  exact summable_emBase5.sub
    (summable_const_div_shiftedPoint_pow 199 18 64 (by norm_num))

private lemma summable_emUpper5 :
    Summable (fun n : ℕ => emUpper5 (shiftedPoint 64 n)) := by
  unfold emUpper5
  exact summable_emBase5.add
    (summable_const_div_shiftedPoint_pow 199 18 64 (by norm_num))

theorem shiftedPowerTail_five_mem_Icc :
    shiftedPowerTail 5 64 ∈
      Icc
        ((1086044680735235658335281740158843584 : ℝ) / 71765790783523614145654534638886574174713347)
        ((1086044680735235658335363791214066368 : ℝ) / 71765790783523614145654534638886574174713347) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 5 64 (by norm_num)
    emLower5 emUpper5 summable_emLower5 summable_emUpper5
    emLower5_step emUpper5_step
  norm_num [emLower5, emUpper5, emBase5] at h ⊢
  exact h

/-! ## `p = 7`, truncation order `S = 18` -/

private noncomputable def emBase7 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 6) / x ^ 6 +
    ((1 : ℝ) / 2) / x ^ 7 +
    ((7 : ℝ) / 12) / x ^ 8 -
    ((7 : ℝ) / 10) / x ^ 10 +
    ((11 : ℝ) / 6) / x ^ 12 -
    ((143 : ℝ) / 20) / x ^ 14 +
    ((455 : ℝ) / 12) / x ^ 16 -
    ((11747 : ℝ) / 45) / x ^ 18

private noncomputable def emLower7 (x : ℝ) : ℝ :=
  emBase7 x - 262 / x ^ 18

private noncomputable def emUpper7 (x : ℝ) : ℝ :=
  emBase7 x + 262 / x ^ 18

private lemma emLower7_step (x : ℝ) (hx : 0 < x) :
    emLower7 x - emLower7 (x + 1) ≤ 1 / x ^ 7 := by
  unfold emLower7 emBase7
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper7_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 7 ≤ emUpper7 x - emUpper7 (x + 1) := by
  unfold emUpper7 emBase7
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase7 :
    Summable (fun n : ℕ => emBase7 (shiftedPoint 64 n)) := by
  unfold emBase7
  have h6 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 6) 6 64 (by norm_num)
  have h7 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 7 64 (by norm_num)
  have h8 := summable_const_div_shiftedPoint_pow ((7 : ℝ) / 12) 8 64 (by norm_num)
  have h10 := summable_const_div_shiftedPoint_pow ((7 : ℝ) / 10) 10 64 (by norm_num)
  have h12 := summable_const_div_shiftedPoint_pow ((11 : ℝ) / 6) 12 64 (by norm_num)
  have h14 := summable_const_div_shiftedPoint_pow ((143 : ℝ) / 20) 14 64 (by norm_num)
  have h16 := summable_const_div_shiftedPoint_pow ((455 : ℝ) / 12) 16 64 (by norm_num)
  have h18 := summable_const_div_shiftedPoint_pow ((11747 : ℝ) / 45) 18 64 (by norm_num)
  exact (((((((h6).add h7).add h8).sub h10).add h12).sub h14).add h16).sub h18

private lemma summable_emLower7 :
    Summable (fun n : ℕ => emLower7 (shiftedPoint 64 n)) := by
  unfold emLower7
  exact summable_emBase7.sub
    (summable_const_div_shiftedPoint_pow 262 18 64 (by norm_num))

private lemma summable_emUpper7 :
    Summable (fun n : ℕ => emUpper7 (shiftedPoint 64 n)) := by
  unfold emUpper7
  exact summable_emBase7.add
    (summable_const_div_shiftedPoint_pow 262 18 64 (by norm_num))

theorem shiftedPowerTail_seven_mem_Icc :
    shiftedPowerTail 7 64 ∈
      Icc
        ((2671710493896450855240915736877056 : ℝ) / 1076486861752854212184818019583298612620700205)
        ((2671710493896450856861320998311936 : ℝ) / 1076486861752854212184818019583298612620700205) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 7 64 (by norm_num)
    emLower7 emUpper7 summable_emLower7 summable_emUpper7
    emLower7_step emUpper7_step
  norm_num [emLower7, emUpper7, emBase7] at h ⊢
  exact h


/-! ## `p = 9`, truncation order `S = 18` -/

private noncomputable def emBase9 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 8) / x ^ 8 +
    ((1 : ℝ) / 2) / x ^ 9 +
    ((3 : ℝ) / 4) / x ^ 10 -
    ((11 : ℝ) / 8) / x ^ 12 +
    ((143 : ℝ) / 28) / x ^ 14 -
    ((429 : ℝ) / 16) / x ^ 16 +
    ((1105 : ℝ) / 6) / x ^ 18

private noncomputable def emLower9 (x : ℝ) : ℝ :=
  emBase9 x - 185 / x ^ 18

private noncomputable def emUpper9 (x : ℝ) : ℝ :=
  emBase9 x + 185 / x ^ 18

private lemma emLower9_step (x : ℝ) (hx : 0 < x) :
    emLower9 x - emLower9 (x + 1) ≤ 1 / x ^ 9 := by
  unfold emLower9 emBase9
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper9_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 9 ≤ emUpper9 x - emUpper9 (x + 1) := by
  unfold emUpper9 emBase9
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase9 :
    Summable (fun n : ℕ => emBase9 (shiftedPoint 64 n)) := by
  unfold emBase9
  have h8 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 8) 8 64 (by norm_num)
  have h9 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 9 64 (by norm_num)
  have h10 := summable_const_div_shiftedPoint_pow ((3 : ℝ) / 4) 10 64 (by norm_num)
  have h12 := summable_const_div_shiftedPoint_pow ((11 : ℝ) / 8) 12 64 (by norm_num)
  have h14 := summable_const_div_shiftedPoint_pow ((143 : ℝ) / 28) 14 64 (by norm_num)
  have h16 := summable_const_div_shiftedPoint_pow ((429 : ℝ) / 16) 16 64 (by norm_num)
  have h18 := summable_const_div_shiftedPoint_pow ((1105 : ℝ) / 6) 18 64 (by norm_num)
  exact ((((((h8).add h9).add h10).sub h12).add h14).sub h16).add h18

private lemma summable_emLower9 :
    Summable (fun n : ℕ => emLower9 (shiftedPoint 64 n)) := by
  unfold emLower9
  exact summable_emBase9.sub
    (summable_const_div_shiftedPoint_pow 185 18 64 (by norm_num))

private lemma summable_emUpper9 :
    Summable (fun n : ℕ => emUpper9 (shiftedPoint 64 n)) := by
  unfold emUpper9
  exact summable_emBase9.add
    (summable_const_div_shiftedPoint_pow 185 18 64 (by norm_num))

theorem shiftedPowerTail_nine_mem_Icc :
    shiftedPowerTail 9 64 ∈
      Icc
        ((230018921604882793948479266816 : ℝ) / 502360535484665299019581742472206019222993429)
        ((230018921604883327898813505536 : ℝ) / 502360535484665299019581742472206019222993429) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 9 64 (by norm_num)
    emLower9 emUpper9 summable_emLower9 summable_emUpper9
    emLower9_step emUpper9_step
  norm_num [emLower9, emUpper9, emBase9] at h ⊢
  exact h


/-! ## `p = 11`, truncation order `S = 19` -/

private noncomputable def emBase11 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 10) / x ^ 10 +
    ((1 : ℝ) / 2) / x ^ 11 +
    ((11 : ℝ) / 12) / x ^ 12 -
    ((143 : ℝ) / 60) / x ^ 14 +
    ((143 : ℝ) / 12) / x ^ 16 -
    ((2431 : ℝ) / 30) / x ^ 18

private noncomputable def emLower11 (x : ℝ) : ℝ :=
  emBase11 x - 133 / x ^ 19

private noncomputable def emUpper11 (x : ℝ) : ℝ :=
  emBase11 x + 133 / x ^ 19

private lemma emLower11_step (x : ℝ) (hx : 0 < x) :
    emLower11 x - emLower11 (x + 1) ≤ 1 / x ^ 11 := by
  unfold emLower11 emBase11
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper11_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 11 ≤ emUpper11 x - emUpper11 (x + 1) := by
  unfold emUpper11 emBase11
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase11 :
    Summable (fun n : ℕ => emBase11 (shiftedPoint 64 n)) := by
  unfold emBase11
  have h10 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 10) 10 64 (by norm_num)
  have h11 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 11 64 (by norm_num)
  have h12 := summable_const_div_shiftedPoint_pow ((11 : ℝ) / 12) 12 64 (by norm_num)
  have h14 := summable_const_div_shiftedPoint_pow ((143 : ℝ) / 60) 14 64 (by norm_num)
  have h16 := summable_const_div_shiftedPoint_pow ((143 : ℝ) / 12) 16 64 (by norm_num)
  have h18 := summable_const_div_shiftedPoint_pow ((2431 : ℝ) / 30) 18 64 (by norm_num)
  exact (((((h10).add h11).add h12).sub h14).add h16).sub h18

private lemma summable_emLower11 :
    Summable (fun n : ℕ => emLower11 (shiftedPoint 64 n)) := by
  unfold emLower11
  exact summable_emBase11.sub
    (summable_const_div_shiftedPoint_pow 133 19 64 (by norm_num))

private lemma summable_emUpper11 :
    Summable (fun n : ℕ => emUpper11 (shiftedPoint 64 n)) := by
  unfold emUpper11
  exact summable_emBase11.add
    (summable_const_div_shiftedPoint_pow 133 19 64 (by norm_num))

theorem shiftedPowerTail_eleven_mem_Icc :
    shiftedPowerTail 11 64 ∈
      Icc
        ((8308625769002417350933741568 : ℝ) / 92219041156827844177166077010969247814506650895)
        ((8308625769003514113782448128 : ℝ) / 92219041156827844177166077010969247814506650895) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 11 64 (by norm_num)
    emLower11 emUpper11 summable_emLower11 summable_emUpper11
    emLower11_step emUpper11_step
  norm_num [emLower11, emUpper11, emBase11] at h ⊢
  exact h


/-! ## `p = 13`, truncation order `S = 21` -/

private noncomputable def emBase13 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 12) / x ^ 12 +
    ((1 : ℝ) / 2) / x ^ 13 +
    ((13 : ℝ) / 12) / x ^ 14 -
    ((91 : ℝ) / 24) / x ^ 16 +
    ((221 : ℝ) / 9) / x ^ 18 -
    ((4199 : ℝ) / 20) / x ^ 20

private noncomputable def emLower13 (x : ℝ) : ℝ :=
  emBase13 x - 381 / x ^ 21

private noncomputable def emUpper13 (x : ℝ) : ℝ :=
  emBase13 x + 381 / x ^ 21

private lemma emLower13_step (x : ℝ) (hx : 0 < x) :
    emLower13 x - emLower13 (x + 1) ≤ 1 / x ^ 13 := by
  unfold emLower13 emBase13
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper13_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 13 ≤ emUpper13 x - emUpper13 (x + 1) := by
  unfold emUpper13 emBase13
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase13 :
    Summable (fun n : ℕ => emBase13 (shiftedPoint 64 n)) := by
  unfold emBase13
  have h12 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 12) 12 64 (by norm_num)
  have h13 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 13 64 (by norm_num)
  have h14 := summable_const_div_shiftedPoint_pow ((13 : ℝ) / 12) 14 64 (by norm_num)
  have h16 := summable_const_div_shiftedPoint_pow ((91 : ℝ) / 24) 16 64 (by norm_num)
  have h18 := summable_const_div_shiftedPoint_pow ((221 : ℝ) / 9) 18 64 (by norm_num)
  have h20 := summable_const_div_shiftedPoint_pow ((4199 : ℝ) / 20) 20 64 (by norm_num)
  exact (((((h12).add h13).add h14).sub h16).add h18).sub h20

private lemma summable_emLower13 :
    Summable (fun n : ℕ => emLower13 (shiftedPoint 64 n)) := by
  unfold emLower13
  exact summable_emBase13.sub
    (summable_const_div_shiftedPoint_pow 381 21 64 (by norm_num))

private lemma summable_emUpper13 :
    Summable (fun n : ℕ => emUpper13 (shiftedPoint 64 n)) := by
  unfold emUpper13
  exact summable_emBase13.add
    (summable_const_div_shiftedPoint_pow 381 21 64 (by norm_num))

theorem shiftedPowerTail_thirteen_mem_Icc :
    shiftedPowerTail 13 64 ∈
      Icc
        ((337419731120299407433502031872 : ℝ) / 18272926348101966840172926661492523546701049354891565)
        ((337419731120450216448367788032 : ℝ) / 18272926348101966840172926661492523546701049354891565) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 13 64 (by norm_num)
    emLower13 emUpper13 summable_emLower13 summable_emUpper13
    emLower13_step emUpper13_step
  norm_num [emLower13, emUpper13, emBase13] at h ⊢
  exact h


/-! ## `p = 15`, truncation order `S = 23` -/

private noncomputable def emBase15 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 14) / x ^ 14 +
    ((1 : ℝ) / 2) / x ^ 15 +
    ((5 : ℝ) / 4) / x ^ 16 -
    ((17 : ℝ) / 3) / x ^ 18 +
    ((323 : ℝ) / 7) / x ^ 20 -
    ((969 : ℝ) / 2) / x ^ 22

private noncomputable def emLower15 (x : ℝ) : ℝ :=
  emBase15 x - 963 / x ^ 23

private noncomputable def emUpper15 (x : ℝ) : ℝ :=
  emBase15 x + 963 / x ^ 23

private lemma emLower15_step (x : ℝ) (hx : 0 < x) :
    emLower15 x - emLower15 (x + 1) ≤ 1 / x ^ 15 := by
  unfold emLower15 emBase15
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper15_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 15 ≤ emUpper15 x - emUpper15 (x + 1) := by
  unfold emUpper15 emBase15
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase15 :
    Summable (fun n : ℕ => emBase15 (shiftedPoint 64 n)) := by
  unfold emBase15
  have h14 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 14) 14 64 (by norm_num)
  have h15 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 15 64 (by norm_num)
  have h16 := summable_const_div_shiftedPoint_pow ((5 : ℝ) / 4) 16 64 (by norm_num)
  have h18 := summable_const_div_shiftedPoint_pow ((17 : ℝ) / 3) 18 64 (by norm_num)
  have h20 := summable_const_div_shiftedPoint_pow ((323 : ℝ) / 7) 20 64 (by norm_num)
  have h22 := summable_const_div_shiftedPoint_pow ((969 : ℝ) / 2) 22 64 (by norm_num)
  exact (((((h14).add h15).add h16).sub h18).add h20).sub h22

private lemma summable_emLower15 :
    Summable (fun n : ℕ => emLower15 (shiftedPoint 64 n)) := by
  unfold emLower15
  exact summable_emBase15.sub
    (summable_const_div_shiftedPoint_pow 963 23 64 (by norm_num))

private lemma summable_emUpper15 :
    Summable (fun n : ℕ => emUpper15 (shiftedPoint 64 n)) := by
  unfold emUpper15
  exact summable_emBase15.add
    (summable_const_div_shiftedPoint_pow 963 23 64 (by norm_num))

theorem shiftedPowerTail_fifteen_mem_Icc :
    shiftedPowerTail 15 64 ∈
      Icc
        ((2192281007613786054416912089088 : ℝ) / 563223972437367176985738095430295854276826884125908722453)
        ((2192281007616632188643921887232 : ℝ) / 563223972437367176985738095430295854276826884125908722453) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 15 64 (by norm_num)
    emLower15 emUpper15 summable_emLower15 summable_emUpper15
    emLower15_step emUpper15_step
  norm_num [emLower15, emUpper15, emBase15] at h ⊢
  exact h


/-! ## `p = 17`, truncation order `S = 25` -/

private noncomputable def emBase17 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 16) / x ^ 16 +
    ((1 : ℝ) / 2) / x ^ 17 +
    ((17 : ℝ) / 12) / x ^ 18 -
    ((323 : ℝ) / 40) / x ^ 20 +
    ((323 : ℝ) / 4) / x ^ 22 -
    ((81719 : ℝ) / 80) / x ^ 24

private noncomputable def emLower17 (x : ℝ) : ℝ :=
  emBase17 x - 2207 / x ^ 25

private noncomputable def emUpper17 (x : ℝ) : ℝ :=
  emBase17 x + 2207 / x ^ 25

private lemma emLower17_step (x : ℝ) (hx : 0 < x) :
    emLower17 x - emLower17 (x + 1) ≤ 1 / x ^ 17 := by
  unfold emLower17 emBase17
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper17_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 17 ≤ emUpper17 x - emUpper17 (x + 1) := by
  unfold emUpper17 emBase17
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase17 :
    Summable (fun n : ℕ => emBase17 (shiftedPoint 64 n)) := by
  unfold emBase17
  have h16 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 16) 16 64 (by norm_num)
  have h17 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 17 64 (by norm_num)
  have h18 := summable_const_div_shiftedPoint_pow ((17 : ℝ) / 12) 18 64 (by norm_num)
  have h20 := summable_const_div_shiftedPoint_pow ((323 : ℝ) / 40) 20 64 (by norm_num)
  have h22 := summable_const_div_shiftedPoint_pow ((323 : ℝ) / 4) 22 64 (by norm_num)
  have h24 := summable_const_div_shiftedPoint_pow ((81719 : ℝ) / 80) 24 64 (by norm_num)
  exact (((((h16).add h17).add h18).sub h20).add h22).sub h24

private lemma summable_emLower17 :
    Summable (fun n : ℕ => emLower17 (shiftedPoint 64 n)) := by
  unfold emLower17
  exact summable_emBase17.sub
    (summable_const_div_shiftedPoint_pow 2207 25 64 (by norm_num))

private lemma summable_emUpper17 :
    Summable (fun n : ℕ => emUpper17 (shiftedPoint 64 n)) := by
  unfold emUpper17
  exact summable_emBase17.add
    (summable_const_div_shiftedPoint_pow 2207 25 64 (by norm_num))

theorem shiftedPowerTail_seventeen_mem_Icc :
    shiftedPowerTail 17 64 ∈
      Icc
        ((4450783877283296690414748172288 : ℝ) / 5314340022216523524675859352153658697018591267090306458471171)
        ((4450783877298205856981158199296 : ℝ) / 5314340022216523524675859352153658697018591267090306458471171) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 17 64 (by norm_num)
    emLower17 emUpper17 summable_emLower17 summable_emUpper17
    emLower17_step emUpper17_step
  norm_num [emLower17, emUpper17, emBase17] at h ⊢
  exact h


/-! ## `p = 19`, truncation order `S = 27` -/

private noncomputable def emBase19 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 18) / x ^ 18 +
    ((1 : ℝ) / 2) / x ^ 19 +
    ((19 : ℝ) / 12) / x ^ 20 -
    ((133 : ℝ) / 12) / x ^ 22 +
    ((4807 : ℝ) / 36) / x ^ 24 -
    ((24035 : ℝ) / 12) / x ^ 26

private noncomputable def emLower19 (x : ℝ) : ℝ :=
  emBase19 x - 4673 / x ^ 27

private noncomputable def emUpper19 (x : ℝ) : ℝ :=
  emBase19 x + 4673 / x ^ 27

private lemma emLower19_step (x : ℝ) (hx : 0 < x) :
    emLower19 x - emLower19 (x + 1) ≤ 1 / x ^ 19 := by
  unfold emLower19 emBase19
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper19_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 19 ≤ emUpper19 x - emUpper19 (x + 1) := by
  unfold emUpper19 emBase19
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase19 :
    Summable (fun n : ℕ => emBase19 (shiftedPoint 64 n)) := by
  unfold emBase19
  have h18 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 18) 18 64 (by norm_num)
  have h19 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 19 64 (by norm_num)
  have h20 := summable_const_div_shiftedPoint_pow ((19 : ℝ) / 12) 20 64 (by norm_num)
  have h22 := summable_const_div_shiftedPoint_pow ((133 : ℝ) / 12) 22 64 (by norm_num)
  have h24 := summable_const_div_shiftedPoint_pow ((4807 : ℝ) / 36) 24 64 (by norm_num)
  have h26 := summable_const_div_shiftedPoint_pow ((24035 : ℝ) / 12) 26 64 (by norm_num)
  exact (((((h18).add h19).add h20).sub h22).add h24).sub h26

private lemma summable_emLower19 :
    Summable (fun n : ℕ => emLower19 (shiftedPoint 64 n)) := by
  unfold emLower19
  exact summable_emBase19.sub
    (summable_const_div_shiftedPoint_pow 4673 27 64 (by norm_num))

private lemma summable_emUpper19 :
    Summable (fun n : ℕ => emUpper19 (shiftedPoint 64 n)) := by
  unfold emUpper19
  exact summable_emBase19.add
    (summable_const_div_shiftedPoint_pow 4673 27 64 (by norm_num))

theorem shiftedPowerTail_nineteen_mem_Icc :
    shiftedPowerTail 19 64 ∈
      Icc
        ((64250839281878483626001950572544 : ℝ) / 351006844127379162281315834350397003279380934600047651275562373379)
        ((64250839282383571331410806439936 : ℝ) / 351006844127379162281315834350397003279380934600047651275562373379) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 19 64 (by norm_num)
    emLower19 emUpper19 summable_emLower19 summable_emUpper19
    emLower19_step emUpper19_step
  norm_num [emLower19, emUpper19, emBase19] at h ⊢
  exact h


/-! ## `p = 21`, truncation order `S = 29` -/

private noncomputable def emBase21 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 20) / x ^ 20 +
    ((1 : ℝ) / 2) / x ^ 21 +
    ((7 : ℝ) / 4) / x ^ 22 -
    ((1771 : ℝ) / 120) / x ^ 24 +
    ((1265 : ℝ) / 6) / x ^ 26 -
    ((29601 : ℝ) / 8) / x ^ 28

private noncomputable def emLower21 (x : ℝ) : ℝ :=
  emBase21 x - 9270 / x ^ 29

private noncomputable def emUpper21 (x : ℝ) : ℝ :=
  emBase21 x + 9270 / x ^ 29

private lemma emLower21_step (x : ℝ) (hx : 0 < x) :
    emLower21 x - emLower21 (x + 1) ≤ 1 / x ^ 21 := by
  unfold emLower21 emBase21
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper21_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 21 ≤ emUpper21 x - emUpper21 (x + 1) := by
  unfold emUpper21 emBase21
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase21 :
    Summable (fun n : ℕ => emBase21 (shiftedPoint 64 n)) := by
  unfold emBase21
  have h20 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 20) 20 64 (by norm_num)
  have h21 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 21 64 (by norm_num)
  have h22 := summable_const_div_shiftedPoint_pow ((7 : ℝ) / 4) 22 64 (by norm_num)
  have h24 := summable_const_div_shiftedPoint_pow ((1771 : ℝ) / 120) 24 64 (by norm_num)
  have h26 := summable_const_div_shiftedPoint_pow ((1265 : ℝ) / 6) 26 64 (by norm_num)
  have h28 := summable_const_div_shiftedPoint_pow ((29601 : ℝ) / 8) 28 64 (by norm_num)
  exact (((((h20).add h21).add h22).sub h24).add h26).sub h28

private lemma summable_emLower21 :
    Summable (fun n : ℕ => emLower21 (shiftedPoint 64 n)) := by
  unfold emLower21
  exact summable_emBase21.sub
    (summable_const_div_shiftedPoint_pow 9270 29 64 (by norm_num))

private lemma summable_emUpper21 :
    Summable (fun n : ℕ => emUpper21 (shiftedPoint 64 n)) := by
  unfold emUpper21
  exact summable_emBase21.add
    (summable_const_div_shiftedPoint_pow 9270 29 64 (by norm_num))

theorem shiftedPowerTail_twenty_one_mem_Icc :
    shiftedPowerTail 21 64 ∈
      Icc
        ((313010904216808843613877053685760 : ℝ) / 7727883682589755429839543181003123889866610449799515773033206399769857)
        ((313010904222152634787729789419520 : ℝ) / 7727883682589755429839543181003123889866610449799515773033206399769857) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 21 64 (by norm_num)
    emLower21 emUpper21 summable_emLower21 summable_emUpper21
    emLower21_step emUpper21_step
  norm_num [emLower21, emUpper21, emBase21] at h ⊢
  exact h


/-! ## `p = 23`, truncation order `S = 31` -/

private noncomputable def emBase23 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 22) / x ^ 22 +
    ((1 : ℝ) / 2) / x ^ 23 +
    ((23 : ℝ) / 12) / x ^ 24 -
    ((115 : ℝ) / 6) / x ^ 26 +
    ((4485 : ℝ) / 14) / x ^ 28 -
    ((26013 : ℝ) / 4) / x ^ 30

private noncomputable def emLower23 (x : ℝ) : ℝ :=
  emBase23 x - 17412 / x ^ 31

private noncomputable def emUpper23 (x : ℝ) : ℝ :=
  emBase23 x + 17412 / x ^ 31

private lemma emLower23_step (x : ℝ) (hx : 0 < x) :
    emLower23 x - emLower23 (x + 1) ≤ 1 / x ^ 23 := by
  unfold emLower23 emBase23
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper23_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 23 ≤ emUpper23 x - emUpper23 (x + 1) := by
  unfold emUpper23 emBase23
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase23 :
    Summable (fun n : ℕ => emBase23 (shiftedPoint 64 n)) := by
  unfold emBase23
  have h22 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 22) 22 64 (by norm_num)
  have h23 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 23 64 (by norm_num)
  have h24 := summable_const_div_shiftedPoint_pow ((23 : ℝ) / 12) 24 64 (by norm_num)
  have h26 := summable_const_div_shiftedPoint_pow ((115 : ℝ) / 6) 26 64 (by norm_num)
  have h28 := summable_const_div_shiftedPoint_pow ((4485 : ℝ) / 14) 28 64 (by norm_num)
  have h30 := summable_const_div_shiftedPoint_pow ((26013 : ℝ) / 4) 30 64 (by norm_num)
  exact (((((h22).add h23).add h24).sub h26).add h28).sub h30

private lemma summable_emLower23 :
    Summable (fun n : ℕ => emLower23 (shiftedPoint 64 n)) := by
  unfold emLower23
  exact summable_emBase23.sub
    (summable_const_div_shiftedPoint_pow 17412 31 64 (by norm_num))

private lemma summable_emUpper23 :
    Summable (fun n : ℕ => emUpper23 (shiftedPoint 64 n)) := by
  unfold emUpper23
  exact summable_emBase23.add
    (summable_const_div_shiftedPoint_pow 17412 31 64 (by norm_num))

theorem shiftedPowerTail_twenty_three_mem_Icc :
    shiftedPowerTail 23 64 ∈
      Icc
        ((355780007840533548504438864657514496 : ℝ) / 39302262180055548241681343042279800394738581027108232731566409211376744944461)
        ((355780007852899544755178947097919488 : ℝ) / 39302262180055548241681343042279800394738581027108232731566409211376744944461) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 23 64 (by norm_num)
    emLower23 emUpper23 summable_emLower23 summable_emUpper23
    emLower23_step emUpper23_step
  norm_num [emLower23, emUpper23, emBase23] at h ⊢
  exact h


/-! ## `p = 25`, truncation order `S = 33` -/

private noncomputable def emBase25 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 24) / x ^ 24 +
    ((1 : ℝ) / 2) / x ^ 25 +
    ((25 : ℝ) / 12) / x ^ 26 -
    ((195 : ℝ) / 8) / x ^ 28 +
    ((1885 : ℝ) / 4) / x ^ 30 -
    ((175305 : ℝ) / 16) / x ^ 32

private noncomputable def emLower25 (x : ℝ) : ℝ :=
  emBase25 x - 31222 / x ^ 33

private noncomputable def emUpper25 (x : ℝ) : ℝ :=
  emBase25 x + 31222 / x ^ 33

private lemma emLower25_step (x : ℝ) (hx : 0 < x) :
    emLower25 x - emLower25 (x + 1) ≤ 1 / x ^ 25 := by
  unfold emLower25 emBase25
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper25_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 25 ≤ emUpper25 x - emUpper25 (x + 1) := by
  unfold emUpper25 emBase25
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase25 :
    Summable (fun n : ℕ => emBase25 (shiftedPoint 64 n)) := by
  unfold emBase25
  have h24 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 24) 24 64 (by norm_num)
  have h25 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 25 64 (by norm_num)
  have h26 := summable_const_div_shiftedPoint_pow ((25 : ℝ) / 12) 26 64 (by norm_num)
  have h28 := summable_const_div_shiftedPoint_pow ((195 : ℝ) / 8) 28 64 (by norm_num)
  have h30 := summable_const_div_shiftedPoint_pow ((1885 : ℝ) / 4) 30 64 (by norm_num)
  have h32 := summable_const_div_shiftedPoint_pow ((175305 : ℝ) / 16) 32 64 (by norm_num)
  exact (((((h24).add h25).add h26).sub h28).add h30).sub h32

private lemma summable_emLower25 :
    Summable (fun n : ℕ => emLower25 (shiftedPoint 64 n)) := by
  unfold emLower25
  exact summable_emBase25.sub
    (summable_const_div_shiftedPoint_pow 31222 33 64 (by norm_num))

private lemma summable_emUpper25 :
    Summable (fun n : ℕ => emUpper25 (shiftedPoint 64 n)) := by
  unfold emUpper25
  exact summable_emBase25.add
    (summable_const_div_shiftedPoint_pow 31222 33 64 (by norm_num))

theorem shiftedPowerTail_twenty_five_mem_Icc :
    shiftedPowerTail 25 64 ∈
      Icc
        ((68768722484719096811988728353390592 : ℝ) / 33712663827668687088504039306487513458079071925447683943989996909119774374502657)
        ((68768722489326650759743605317828608 : ℝ) / 33712663827668687088504039306487513458079071925447683943989996909119774374502657) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 25 64 (by norm_num)
    emLower25 emUpper25 summable_emLower25 summable_emUpper25
    emLower25_step emUpper25_step
  norm_num [emLower25, emUpper25, emBase25] at h ⊢
  exact h


/-! ## `p = 27`, truncation order `S = 35` -/

private noncomputable def emBase27 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 26) / x ^ 26 +
    ((1 : ℝ) / 2) / x ^ 27 +
    ((9 : ℝ) / 4) / x ^ 28 -
    ((609 : ℝ) / 20) / x ^ 30 +
    ((2697 : ℝ) / 4) / x ^ 32 -
    ((89001 : ℝ) / 5) / x ^ 34

private noncomputable def emLower27 (x : ℝ) : ℝ :=
  emBase27 x - 53786 / x ^ 35

private noncomputable def emUpper27 (x : ℝ) : ℝ :=
  emBase27 x + 53786 / x ^ 35

private lemma emLower27_step (x : ℝ) (hx : 0 < x) :
    emLower27 x - emLower27 (x + 1) ≤ 1 / x ^ 27 := by
  unfold emLower27 emBase27
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper27_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 27 ≤ emUpper27 x - emUpper27 (x + 1) := by
  unfold emUpper27 emBase27
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase27 :
    Summable (fun n : ℕ => emBase27 (shiftedPoint 64 n)) := by
  unfold emBase27
  have h26 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 26) 26 64 (by norm_num)
  have h27 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 27 64 (by norm_num)
  have h28 := summable_const_div_shiftedPoint_pow ((9 : ℝ) / 4) 28 64 (by norm_num)
  have h30 := summable_const_div_shiftedPoint_pow ((609 : ℝ) / 20) 30 64 (by norm_num)
  have h32 := summable_const_div_shiftedPoint_pow ((2697 : ℝ) / 4) 32 64 (by norm_num)
  have h34 := summable_const_div_shiftedPoint_pow ((89001 : ℝ) / 5) 34 64 (by norm_num)
  exact (((((h26).add h27).add h28).sub h30).add h32).sub h34

private lemma summable_emLower27 :
    Summable (fun n : ℕ => emLower27 (shiftedPoint 64 n)) := by
  unfold emLower27
  exact summable_emBase27.sub
    (summable_const_div_shiftedPoint_pow 53786 35 64 (by norm_num))

private lemma summable_emUpper27 :
    Summable (fun n : ℕ => emUpper27 (shiftedPoint 64 n)) := by
  unfold emUpper27
  exact summable_emBase27.add
    (summable_const_div_shiftedPoint_pow 53786 35 64 (by norm_num))

theorem shiftedPowerTail_twenty_seven_mem_Icc :
    shiftedPowerTail 27 64 ∈
      Icc
        ((66987786075829013024682965887455592448 : ℝ) / 144734702654989792378059213990022595465523200404253114993078694880279378547999189492545)
        ((66987786084083922143230834855030816768 : ℝ) / 144734702654989792378059213990022595465523200404253114993078694880279378547999189492545) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 27 64 (by norm_num)
    emLower27 emUpper27 summable_emLower27 summable_emUpper27
    emLower27_step emUpper27_step
  norm_num [emLower27, emUpper27, emBase27] at h ⊢
  exact h


/-! ## `p = 29`, truncation order `S = 37` -/

private noncomputable def emBase29 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 28) / x ^ 28 +
    ((1 : ℝ) / 2) / x ^ 29 +
    ((29 : ℝ) / 12) / x ^ 30 -
    ((899 : ℝ) / 24) / x ^ 32 +
    ((19778 : ℝ) / 21) / x ^ 34 -
    ((168113 : ℝ) / 6) / x ^ 36

private noncomputable def emLower29 (x : ℝ) : ℝ :=
  emBase29 x - 89480 / x ^ 37

private noncomputable def emUpper29 (x : ℝ) : ℝ :=
  emBase29 x + 89480 / x ^ 37

private lemma emLower29_step (x : ℝ) (hx : 0 < x) :
    emLower29 x - emLower29 (x + 1) ≤ 1 / x ^ 29 := by
  unfold emLower29 emBase29
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper29_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 29 ≤ emUpper29 x - emUpper29 (x + 1) := by
  unfold emUpper29 emBase29
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase29 :
    Summable (fun n : ℕ => emBase29 (shiftedPoint 64 n)) := by
  unfold emBase29
  have h28 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 28) 28 64 (by norm_num)
  have h29 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 29 64 (by norm_num)
  have h30 := summable_const_div_shiftedPoint_pow ((29 : ℝ) / 12) 30 64 (by norm_num)
  have h32 := summable_const_div_shiftedPoint_pow ((899 : ℝ) / 24) 32 64 (by norm_num)
  have h34 := summable_const_div_shiftedPoint_pow ((19778 : ℝ) / 21) 34 64 (by norm_num)
  have h36 := summable_const_div_shiftedPoint_pow ((168113 : ℝ) / 6) 36 64 (by norm_num)
  exact (((((h28).add h29).add h30).sub h32).add h34).sub h36

private lemma summable_emLower29 :
    Summable (fun n : ℕ => emLower29 (shiftedPoint 64 n)) := by
  unfold emLower29
  exact summable_emBase29.sub
    (summable_const_div_shiftedPoint_pow 89480 37 64 (by norm_num))

private lemma summable_emUpper29 :
    Summable (fun n : ℕ => emUpper29 (shiftedPoint 64 n)) := by
  unfold emUpper29
  exact summable_emBase29.add
    (summable_const_div_shiftedPoint_pow 89480 37 64 (by norm_num))

theorem shiftedPowerTail_twenty_nine_mem_Icc :
    shiftedPowerTail 29 64 ∈
      Icc
        ((326238388147821550093763826176625737728 : ℝ) / 3088480459828428257420724515713339239476141217438627597472845370478446556123888735425464597)
        ((326238388218811185378809369601840775168 : ℝ) / 3088480459828428257420724515713339239476141217438627597472845370478446556123888735425464597) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 29 64 (by norm_num)
    emLower29 emUpper29 summable_emLower29 summable_emUpper29
    emLower29_step emUpper29_step
  norm_num [emLower29, emUpper29, emBase29] at h ⊢
  exact h


/-! ## `p = 31`, truncation order `S = 39` -/

private noncomputable def emBase31 (x : ℝ) : ℝ :=
  ((1 : ℝ) / 30) / x ^ 30 +
    ((1 : ℝ) / 2) / x ^ 31 +
    ((31 : ℝ) / 12) / x ^ 32 -
    ((682 : ℝ) / 15) / x ^ 34 +
    ((11594 : ℝ) / 9) / x ^ 36 -
    ((214489 : ℝ) / 5) / x ^ 38

private noncomputable def emLower31 (x : ℝ) : ℝ :=
  emBase31 x - 144370 / x ^ 39

private noncomputable def emUpper31 (x : ℝ) : ℝ :=
  emBase31 x + 144370 / x ^ 39

private lemma emLower31_step (x : ℝ) (hx : 0 < x) :
    emLower31 x - emLower31 (x + 1) ≤ 1 / x ^ 31 := by
  unfold emLower31 emBase31
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma emUpper31_step (x : ℝ) (hx : 0 < x) :
    1 / x ^ 31 ≤ emUpper31 x - emUpper31 (x + 1) := by
  unfold emUpper31 emBase31
  have hx1 : 0 < x + 1 := by positivity
  rw [← sub_nonneg]
  field_simp
  ring_nf
  positivity

private lemma summable_emBase31 :
    Summable (fun n : ℕ => emBase31 (shiftedPoint 64 n)) := by
  unfold emBase31
  have h30 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 30) 30 64 (by norm_num)
  have h31 := summable_const_div_shiftedPoint_pow ((1 : ℝ) / 2) 31 64 (by norm_num)
  have h32 := summable_const_div_shiftedPoint_pow ((31 : ℝ) / 12) 32 64 (by norm_num)
  have h34 := summable_const_div_shiftedPoint_pow ((682 : ℝ) / 15) 34 64 (by norm_num)
  have h36 := summable_const_div_shiftedPoint_pow ((11594 : ℝ) / 9) 36 64 (by norm_num)
  have h38 := summable_const_div_shiftedPoint_pow ((214489 : ℝ) / 5) 38 64 (by norm_num)
  exact (((((h30).add h31).add h32).sub h34).add h36).sub h38

private lemma summable_emLower31 :
    Summable (fun n : ℕ => emLower31 (shiftedPoint 64 n)) := by
  unfold emLower31
  exact summable_emBase31.sub
    (summable_const_div_shiftedPoint_pow 144370 39 64 (by norm_num))

private lemma summable_emUpper31 :
    Summable (fun n : ℕ => emUpper31 (shiftedPoint 64 n)) := by
  unfold emUpper31
  exact summable_emBase31.add
    (summable_const_div_shiftedPoint_pow 144370 39 64 (by norm_num))

theorem shiftedPowerTail_thirty_one_mem_Icc :
    shiftedPowerTail 31 64 ∈
      Icc
        ((10591270505126268350648736161959818297344 : ℝ) / 437123669766873981373674500439322164488913538437008387540322779731566249825914415184535381072685)
        ((10591270509053252313648426475887257452544 : ℝ) / 437123669766873981373674500439322164488913538437008387540322779731566249825914415184535381072685) := by
  have h := shiftedPowerTail_mem_Icc_of_telescopers 31 64 (by norm_num)
    emLower31 emUpper31 summable_emLower31 summable_emUpper31
    emLower31_step emUpper31_step
  norm_num [emLower31, emUpper31, emBase31] at h ⊢
  exact h

set_option maxHeartbeats 2000000 in
-- Combining the fifteen exact tail enclosures requires a large rational normalization.
/-- The complete accelerated rational approximation at `r = 0`, including
the 64-term prefix and all fifteen polynomial tail terms, lies in a rational
interval of width `10⁻¹⁵`. -/
theorem quarterDifferenceApprox_zero_mem_Icc_15 :
    quarterDifferenceApprox 0 16 64 ∈
      Icc (-(7446312690410890 : ℝ) / 1000000000000000)
        (-(7446312690410889 : ℝ) / 1000000000000000) := by
  have h3 := shiftedPowerTail_three_mem_Icc
  have h5 := shiftedPowerTail_five_mem_Icc
  have h7 := shiftedPowerTail_seven_mem_Icc
  have h9 := shiftedPowerTail_nine_mem_Icc
  have h11 := shiftedPowerTail_eleven_mem_Icc
  have h13 := shiftedPowerTail_thirteen_mem_Icc
  have h15 := shiftedPowerTail_fifteen_mem_Icc
  have h17 := shiftedPowerTail_seventeen_mem_Icc
  have h19 := shiftedPowerTail_nineteen_mem_Icc
  have h21 := shiftedPowerTail_twenty_one_mem_Icc
  have h23 := shiftedPowerTail_twenty_three_mem_Icc
  have h25 := shiftedPowerTail_twenty_five_mem_Icc
  have h27 := shiftedPowerTail_twenty_seven_mem_Icc
  have h29 := shiftedPowerTail_twenty_nine_mem_Icc
  have h31 := shiftedPowerTail_thirty_one_mem_Icc
  rcases h3 with ⟨h3l, h3u⟩
  rcases h5 with ⟨h5l, h5u⟩
  rcases h7 with ⟨h7l, h7u⟩
  rcases h9 with ⟨h9l, h9u⟩
  rcases h11 with ⟨h11l, h11u⟩
  rcases h13 with ⟨h13l, h13u⟩
  rcases h15 with ⟨h15l, h15u⟩
  rcases h17 with ⟨h17l, h17u⟩
  rcases h19 with ⟨h19l, h19u⟩
  rcases h21 with ⟨h21l, h21u⟩
  rcases h23 with ⟨h23l, h23u⟩
  rcases h25 with ⟨h25l, h25u⟩
  rcases h27 with ⟨h27l, h27u⟩
  rcases h29 with ⟨h29l, h29u⟩
  rcases h31 with ⟨h31l, h31u⟩
  unfold quarterDifferenceApprox quarterTailPolynomial
  norm_num [GlideKernel.quarterDifferenceTerm, Finset.sum_range_succ]
  constructor <;> linarith

end RHP2Bridge
