/-
# Real scalar extension of the clipped 48-dimensional certificate

`FullInfClipped48` stores and checks the exact integer congruence certificate.
This file casts that certificate directly to `ℝ`, so its strict lower bound
applies to arbitrary real matrices in the displayed intervals.  No density
argument is used: density alone would preserve only a non-strict inequality.

The theorem remains a finite interval statement.  Identifying an analytic
clipped zeta-form matrix with these intervals is a separate obligation.
-/
import FullInfClipped48

namespace FullInfClipped48Real

open Matrix Finset
open FullInfClipped48

noncomputable section

/-! ## Even parity block -/

def evenAReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => (evenAQ i j : ℝ)

def evenWReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => (evenWQ i j : ℝ)

def evenWiReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => (evenWiQ i j : ℝ)

def evenGReal : Fin 24 → ℝ := fun k => (evenGQ k : ℝ)

def evenMidReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j =>
    evenAReal i j / (scale : ℝ) + if i = j then (beta : ℝ) else 0

def evenLowerReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => evenMidReal i j - (delta : ℝ)

def evenUpperReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => evenMidReal i j + (delta : ℝ)

lemma evenKeyReal (i j : Fin 24) :
    (evenCInt : ℝ) ^ 2 *
        (evenAReal i j - if i = j then (shiftInt : ℝ) else 0) =
      ∑ k, evenWReal k i * evenGReal k * evenWReal k j := by
  have h := congrArg (fun q : ℚ => (q : ℝ)) (evenKeyQ i j)
  push_cast at h
  by_cases hij : i = j
  · subst j
    simpa [evenAReal, evenWReal, evenGReal] using h
  · simpa [evenAReal, evenWReal, evenGReal, hij] using h

lemma evenWinvReal (i j : Fin 24) :
    (∑ k, evenWiReal i k * evenWReal k j) =
      if i = j then (evenFInt : ℝ) else 0 := by
  have h := congrArg (fun q : ℚ => (q : ℝ)) (evenWinvQ i j)
  push_cast at h
  by_cases hij : i = j
  · subst j
    simpa [evenWiReal, evenWReal] using h
  · simpa [evenWiReal, evenWReal, hij] using h

lemma evenGPosReal : ∀ k, 0 < evenGReal k := by
  intro k
  unfold evenGReal evenGQ
  exact_mod_cast evenGPos k

/-- Every real matrix in the stored even-block interval has quadratic form
strictly above `beta = 2.27e-5` on nonzero real vectors. -/
theorem evenIntervalLowerBoundReal (M : Matrix (Fin 24) (Fin 24) ℝ)
    (hM : ∀ i j,
      evenLowerReal i j ≤ M i j ∧ M i j ≤ evenUpperReal i j)
    (x : Fin 24 → ℝ) (hx : x ≠ 0) :
    (beta : ℝ) * (x ⬝ᵥ x) < x ⬝ᵥ M *ᵥ x := by
  let N : Matrix (Fin 24) (Fin 24) ℝ := M - (beta : ℝ) • 1
  have hclose : ∀ i j,
      |N i j - evenAReal i j / (scale : ℝ)| ≤ (delta : ℝ) := by
    intro i j
    have bounds := hM i j
    have habs : |M i j - evenMidReal i j| ≤ (delta : ℝ) := by
      rw [abs_le]
      constructor
      · have hlo := bounds.1
        simp only [evenLowerReal, Matrix.of_apply] at hlo
        linarith
      · have hhi := bounds.2
        simp only [evenUpperReal, Matrix.of_apply] at hhi
        linarith
    have heq :
        N i j - evenAReal i j / (scale : ℝ) =
          M i j - evenMidReal i j := by
      simp only [N, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul,
        evenMidReal, Matrix.of_apply]
      by_cases hij : i = j
      · subst j
        simp
        ring
      · simp [Matrix.one_apply_ne hij, hij]
    rwa [heq]
  have hpos : 0 < x ⬝ᵥ N *ᵥ x := by
    refine CertFramework.cert_window_positive evenAReal evenWReal evenWiReal
      evenGReal (evenCInt : ℝ) (evenFInt : ℝ) (shiftInt : ℝ)
      (scale : ℝ) (delta : ℝ) evenKeyReal evenWinvReal evenGPosReal
      ?_ ?_ ?_ ?_ ?_ N hclose hx
    · exact_mod_cast evenCPos.ne'
    · exact_mod_cast evenFPos.ne'
    · norm_num [scale]
    · norm_num [delta]
    · norm_num [scale, delta, shiftInt]
  have hrewrite :
      x ⬝ᵥ N *ᵥ x = x ⬝ᵥ M *ᵥ x - (beta : ℝ) * (x ⬝ᵥ x) := by
    simp only [N, sub_mulVec, smul_mulVec, one_mulVec, dotProduct_sub,
      dotProduct_smul, smul_eq_mul]
  rw [hrewrite] at hpos
  exact sub_pos.mp hpos

/-! ## Odd parity block -/

def oddAReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => (oddAQ i j : ℝ)

def oddWReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => (oddWQ i j : ℝ)

def oddWiReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => (oddWiQ i j : ℝ)

def oddGReal : Fin 24 → ℝ := fun k => (oddGQ k : ℝ)

def oddMidReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j =>
    oddAReal i j / (scale : ℝ) + if i = j then (beta : ℝ) else 0

def oddLowerReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => oddMidReal i j - (delta : ℝ)

def oddUpperReal : Matrix (Fin 24) (Fin 24) ℝ :=
  Matrix.of fun i j => oddMidReal i j + (delta : ℝ)

lemma oddKeyReal (i j : Fin 24) :
    (oddCInt : ℝ) ^ 2 *
        (oddAReal i j - if i = j then (shiftInt : ℝ) else 0) =
      ∑ k, oddWReal k i * oddGReal k * oddWReal k j := by
  have h := congrArg (fun q : ℚ => (q : ℝ)) (oddKeyQ i j)
  push_cast at h
  by_cases hij : i = j
  · subst j
    simpa [oddAReal, oddWReal, oddGReal] using h
  · simpa [oddAReal, oddWReal, oddGReal, hij] using h

lemma oddWinvReal (i j : Fin 24) :
    (∑ k, oddWiReal i k * oddWReal k j) =
      if i = j then (oddFInt : ℝ) else 0 := by
  have h := congrArg (fun q : ℚ => (q : ℝ)) (oddWinvQ i j)
  push_cast at h
  by_cases hij : i = j
  · subst j
    simpa [oddWiReal, oddWReal] using h
  · simpa [oddWiReal, oddWReal, hij] using h

lemma oddGPosReal : ∀ k, 0 < oddGReal k := by
  intro k
  unfold oddGReal oddGQ
  exact_mod_cast oddGPos k

/-- Every real matrix in the stored odd-block interval has quadratic form
strictly above `beta = 2.27e-5` on nonzero real vectors. -/
theorem oddIntervalLowerBoundReal (M : Matrix (Fin 24) (Fin 24) ℝ)
    (hM : ∀ i j,
      oddLowerReal i j ≤ M i j ∧ M i j ≤ oddUpperReal i j)
    (x : Fin 24 → ℝ) (hx : x ≠ 0) :
    (beta : ℝ) * (x ⬝ᵥ x) < x ⬝ᵥ M *ᵥ x := by
  let N : Matrix (Fin 24) (Fin 24) ℝ := M - (beta : ℝ) • 1
  have hclose : ∀ i j,
      |N i j - oddAReal i j / (scale : ℝ)| ≤ (delta : ℝ) := by
    intro i j
    have bounds := hM i j
    have habs : |M i j - oddMidReal i j| ≤ (delta : ℝ) := by
      rw [abs_le]
      constructor
      · have hlo := bounds.1
        simp only [oddLowerReal, Matrix.of_apply] at hlo
        linarith
      · have hhi := bounds.2
        simp only [oddUpperReal, Matrix.of_apply] at hhi
        linarith
    have heq :
        N i j - oddAReal i j / (scale : ℝ) =
          M i j - oddMidReal i j := by
      simp only [N, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul,
        oddMidReal, Matrix.of_apply]
      by_cases hij : i = j
      · subst j
        simp
        ring
      · simp [Matrix.one_apply_ne hij, hij]
    rwa [heq]
  have hpos : 0 < x ⬝ᵥ N *ᵥ x := by
    refine CertFramework.cert_window_positive oddAReal oddWReal oddWiReal
      oddGReal (oddCInt : ℝ) (oddFInt : ℝ) (shiftInt : ℝ)
      (scale : ℝ) (delta : ℝ) oddKeyReal oddWinvReal oddGPosReal
      ?_ ?_ ?_ ?_ ?_ N hclose hx
    · exact_mod_cast oddCPos.ne'
    · exact_mod_cast oddFPos.ne'
    · norm_num [scale]
    · norm_num [delta]
    · norm_num [scale, delta, shiftInt]
  have hrewrite :
      x ⬝ᵥ N *ᵥ x = x ⬝ᵥ M *ᵥ x - (beta : ℝ) * (x ⬝ᵥ x) := by
    simp only [N, sub_mulVec, smul_mulVec, one_mulVec, dotProduct_sub,
      dotProduct_smul, smul_eq_mul]
  rw [hrewrite] at hpos
  exact sub_pos.mp hpos

/-! ## Direct sum -/

/-- The real 48-dimensional direct-sum certificate, represented by its two
parity-reordered 24-dimensional blocks. -/
theorem clipped48IntervalLowerBoundReal
    (Me Mo : Matrix (Fin 24) (Fin 24) ℝ)
    (he : ∀ i j,
      evenLowerReal i j ≤ Me i j ∧ Me i j ≤ evenUpperReal i j)
    (ho : ∀ i j,
      oddLowerReal i j ≤ Mo i j ∧ Mo i j ≤ oddUpperReal i j)
    (xe xo : Fin 24 → ℝ) (hx : (xe, xo) ≠ (0, 0)) :
    (beta : ℝ) * (xe ⬝ᵥ xe + xo ⬝ᵥ xo) <
      xe ⬝ᵥ Me *ᵥ xe + xo ⬝ᵥ Mo *ᵥ xo := by
  by_cases hxe : xe = 0
  · have hxo : xo ≠ 0 := by
      intro hxo
      exact hx (Prod.ext hxe hxo)
    have hodd := oddIntervalLowerBoundReal Mo ho xo hxo
    simpa [hxe] using hodd
  · have heven := evenIntervalLowerBoundReal Me he xe hxe
    have hodd :
        (beta : ℝ) * (xo ⬝ᵥ xo) ≤ xo ⬝ᵥ Mo *ᵥ xo := by
      by_cases hxo : xo = 0
      · simp [hxo]
      · exact (oddIntervalLowerBoundReal Mo ho xo hxo).le
    linarith

end

end FullInfClipped48Real
