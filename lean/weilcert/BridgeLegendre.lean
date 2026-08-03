/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Data.Nat.Choose.Central
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# Plain Legendre polynomials over `ℚ`

This file defines the Legendre sequence by Bonnet's recurrence

```text
P₀ = 1,  P₁ = X,
(n+2) Pₙ₊₂ = (2n+3) X Pₙ₊₁ - (n+1) Pₙ,
```

and proves its degree, leading coefficient, and evaluation recurrence.  The
leading coefficient is `n.centralBinom / 2^n`.  The rational sequence is a
convenient unshifted counterpart to `Polynomial.shiftedLegendre`.
-/

namespace Bridge

open Polynomial

/-- The Legendre polynomials over `ℚ`, by the Bonnet three-term recurrence
`(n+2) P_{n+2} = (2n+3) X P_{n+1} - (n+1) P_n`, normalized `P_0 = 1, P_1 = X`.
This is the exact recurrence used by the certificate generator
`src/certified_spectral.py` (function `leg`). -/
noncomputable def legendre : ℕ → ℚ[X]
  | 0 => 1
  | 1 => X
  | n + 2 =>
      C ((2 * n + 3 : ℚ) / (n + 2)) * (X * legendre (n + 1))
        - C ((n + 1 : ℚ) / (n + 2)) * legendre n

@[simp] lemma legendre_zero : legendre 0 = 1 := rfl

@[simp] lemma legendre_one : legendre 1 = X := rfl

lemma legendre_add_two (n : ℕ) :
    legendre (n + 2)
      = C ((2 * n + 3 : ℚ) / (n + 2)) * (X * legendre (n + 1))
        - C ((n + 1 : ℚ) / (n + 2)) * legendre n := by
  rw [legendre]

/-- The leading-coefficient sequence of the Legendre polynomials:
`legLead 0 = 1`, `legLead (n+1) = (2n+1)/(n+1) * legLead n`. -/
def legLead : ℕ → ℚ
  | 0 => 1
  | n + 1 => (2 * n + 1 : ℚ) / (n + 1) * legLead n

@[simp] lemma legLead_zero : legLead 0 = 1 := rfl

lemma legLead_succ (n : ℕ) :
    legLead (n + 1) = (2 * n + 1 : ℚ) / (n + 1) * legLead n := by
  rw [legLead]

lemma legLead_pos (n : ℕ) : 0 < legLead n := by
  induction n with
  | zero => norm_num
  | succ n ih =>
      rw [legLead_succ]
      have h1 : (0 : ℚ) < 2 * n + 1 := by positivity
      have h2 : (0 : ℚ) < n + 1 := by positivity
      exact mul_pos (div_pos h1 h2) ih

/-- Closed form: `legLead n = (2n choose n) / 2^n = (2n)! / (2^n n!^2)`. -/
lemma legLead_eq (n : ℕ) : legLead n = (n.centralBinom : ℚ) / 2 ^ n := by
  induction n with
  | zero => simp [Nat.centralBinom]
  | succ n ih =>
      have h := Nat.succ_mul_centralBinom_succ n
      have hq : ((n : ℚ) + 1) * ((n + 1).centralBinom : ℚ)
          = 2 * (2 * n + 1) * (n.centralBinom : ℚ) := by
        exact_mod_cast congrArg (Nat.cast : ℕ → ℚ) h
      rw [legLead_succ, ih]
      have hn1 : ((n : ℚ) + 1) ≠ 0 := by positivity
      have h2n : (2 : ℚ) ^ n ≠ 0 := by positivity
      field_simp
      linear_combination (-(2 : ℚ) ^ n) * hq

/-- Simultaneous two-step induction: degree bound and the exact top
coefficient, for `n` and `n+1` together. -/
lemma natDegree_coeff_aux :
    ∀ n : ℕ, ((legendre n).natDegree ≤ n ∧ (legendre n).coeff n = legLead n)
      ∧ ((legendre (n + 1)).natDegree ≤ n + 1
          ∧ (legendre (n + 1)).coeff (n + 1) = legLead (n + 1))
  | 0 => by
      refine ⟨⟨?_, ?_⟩, ?_, ?_⟩ <;>
        simp [legLead_succ]
  | n + 1 => by
      obtain ⟨h0, h1⟩ := natDegree_coeff_aux n
      refine ⟨h1, ?_, ?_⟩
      · -- degree bound for legendre (n+2)
        rw [show n + 1 + 1 = n + 2 from rfl, legendre_add_two]
        refine (natDegree_sub_le _ _).trans (max_le ?_ ?_)
        · refine (natDegree_C_mul_le _ _).trans (natDegree_mul_le.trans ?_)
          rw [natDegree_X]
          omega
        · exact (natDegree_C_mul_le _ _).trans (h0.1.trans (by omega))
      · -- top coefficient of legendre (n+2)
        rw [show n + 1 + 1 = n + 2 from rfl, legendre_add_two, coeff_sub,
          coeff_C_mul, coeff_C_mul, show n + 2 = (n + 1) + 1 from rfl,
          coeff_X_mul, h1.2,
          coeff_eq_zero_of_natDegree_lt (h0.1.trans_lt (by omega)),
          mul_zero, sub_zero, legLead_succ (n + 1)]
        push_cast
        ring

theorem coeff_legendre_self (n : ℕ) :
    (legendre n).coeff n = (n.centralBinom : ℚ) / 2 ^ n :=
  ((natDegree_coeff_aux n).1.2).trans (legLead_eq n)

theorem coeff_legendre_self_pos (n : ℕ) : 0 < (legendre n).coeff n := by
  rw [(natDegree_coeff_aux n).1.2]; exact legLead_pos n

theorem legendre_ne_zero (n : ℕ) : legendre n ≠ 0 := by
  intro h
  have hpos := coeff_legendre_self_pos n
  rw [h] at hpos
  simp at hpos

/-- The Legendre polynomial `P_n` has degree exactly `n`. -/
theorem natDegree_legendre (n : ℕ) : (legendre n).natDegree = n :=
  le_antisymm (natDegree_coeff_aux n).1.1
    (le_natDegree_of_ne_zero (coeff_legendre_self_pos n).ne')

theorem degree_legendre (n : ℕ) : (legendre n).degree = n := by
  rw [degree_eq_natDegree (legendre_ne_zero n), natDegree_legendre]

/-- The classical leading coefficient `(2n)! / (2^n n!^2) = C(2n,n) / 2^n`. -/
theorem leadingCoeff_legendre (n : ℕ) :
    (legendre n).leadingCoeff = (n.centralBinom : ℚ) / 2 ^ n := by
  rw [leadingCoeff, natDegree_legendre, coeff_legendre_self]

theorem leadingCoeff_legendre_pos (n : ℕ) : 0 < (legendre n).leadingCoeff := by
  rw [leadingCoeff, natDegree_legendre]; exact coeff_legendre_self_pos n

/-- The Bonnet recurrence under evaluation, in any commutative ℚ-algebra
(`BridgeOverlap` uses `R = ℝ`). -/
lemma aeval_legendre_add_two {R : Type*} [CommRing R] [Algebra ℚ R]
    (n : ℕ) (x : R) :
    aeval x (legendre (n + 2))
      = algebraMap ℚ R ((2 * n + 3 : ℚ) / (n + 2)) * (x * aeval x (legendre (n + 1)))
        - algebraMap ℚ R ((n + 1 : ℚ) / (n + 2)) * aeval x (legendre n) := by
  rw [legendre_add_two]
  simp

end Bridge
