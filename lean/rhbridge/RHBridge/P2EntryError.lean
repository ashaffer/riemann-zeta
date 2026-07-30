/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2EntryCertificate
import RHBridge.P2AlphaEnclosure
import RHBridge.P2ElementaryConstants
import RHBridge.P2SphericalReal
import RHBridge.P2PoleApprox

/-!
# Error ledger for generated canonical p=2 entries

This file packages the two non-polynomial scalar constants and the final
triangle inequalities used by the generated 600-entry certificate.
-/

namespace RHP2Bridge

noncomputable def p2AlphaCenter : ℝ :=
  10938711277167 / 10 ^ 13

theorem abs_p2Alpha_sub_center_lt :
    |GlideKernel.p2Alpha - p2AlphaCenter| < 1 / 10 ^ 13 := by
  have h := p2Alpha_mem_Ioo_13
  rw [abs_lt]
  constructor <;> norm_num [p2AlphaCenter] at h ⊢ <;> linarith

noncomputable def p2InvTwoPiCenter : ℝ :=
  15915494309189533576 / 10 ^ 20

theorem abs_inv_two_pi_sub_center_lt :
    |1 / (2 * Real.pi) - p2InvTwoPiCenter| < 1 / 10 ^ 20 := by
  have h := inv_two_pi_mem_Ioo_20
  rw [abs_lt]
  constructor <;> norm_num [p2InvTwoPiCenter] at h ⊢ <;> linarith

theorem abs_inv_two_pi_le_four_twenty_five :
    |1 / (2 * Real.pi)| ≤ 4 / 25 := by
  rw [abs_of_pos (by positivity : 0 < 1 / (2 * Real.pi))]
  exact (inv_two_pi_mem_Ioo_20.2.le).trans (by norm_num)

/-- Transfer a raw integral enclosure through the Fourier normalization.
The rational center is deliberately the lower endpoint of the certified
`1/(2π)` interval, so its error is at most `10⁻²⁰`. -/
theorem abs_normalizedIntegral_sub_center_mul_le
    {I R e B : ℝ} (he : 0 ≤ e) (hB : 0 ≤ B)
    (hIR : |I - R| ≤ e) (hR : |R| ≤ B) :
    |(1 / (2 * Real.pi)) * I - p2InvTwoPiCenter * R| ≤
      (4 / 25) * e + (1 / 10 ^ 20) * B := by
  rw [show
      (1 / (2 * Real.pi)) * I - p2InvTwoPiCenter * R =
        (1 / (2 * Real.pi)) * (I - R) +
          (1 / (2 * Real.pi) - p2InvTwoPiCenter) * R by ring]
  calc
    |(1 / (2 * Real.pi)) * (I - R) +
        (1 / (2 * Real.pi) - p2InvTwoPiCenter) * R| ≤
      |1 / (2 * Real.pi)| * |I - R| +
        |1 / (2 * Real.pi) - p2InvTwoPiCenter| * |R| := by
      simpa only [abs_mul] using abs_add_le
        ((1 / (2 * Real.pi)) * (I - R))
        ((1 / (2 * Real.pi) - p2InvTwoPiCenter) * R)
    _ ≤ (4 / 25) * e + (1 / 10 ^ 20) * B := by
      apply add_le_add
      · exact mul_le_mul abs_inv_two_pi_le_four_twenty_five hIR
          (abs_nonneg _) (by norm_num)
      · exact mul_le_mul (abs_inv_two_pi_sub_center_lt.le) hR
          (abs_nonneg _) (by norm_num)

/-- Assemble scalar-floor, normalized-band, and pole approximation errors.
This common lemma is used for both parity signs. -/
theorem abs_threeTermEntry_sub_approx_le
    {alpha alpha0 band band0 pole pole0 ea eb ep d : ℝ}
    (ha : |alpha - alpha0| ≤ ea)
    (hb : |band - band0| ≤ eb)
    (hp : |pole - pole0| ≤ ep)
    (hd : d = 0 ∨ d = 1) :
    |(alpha * d + band + pole) -
        (alpha0 * d + band0 + pole0)| ≤ ea + eb + ep := by
  have hdabs : |d| ≤ 1 := by rcases hd with rfl | rfl <;> norm_num
  have hea : 0 ≤ ea := (abs_nonneg (alpha - alpha0)).trans ha
  rw [show
      (alpha * d + band + pole) - (alpha0 * d + band0 + pole0) =
        (alpha - alpha0) * d + (band - band0) + (pole - pole0) by ring]
  calc
    |(alpha - alpha0) * d + (band - band0) + (pole - pole0)| ≤
      |alpha - alpha0| * |d| + |band - band0| + |pole - pole0| := by
      rw [← abs_mul]
      exact (abs_add_le _ _).trans
        (add_le_add (abs_add_le _ _) (le_refl _))
    _ ≤ ea * 1 + eb + ep := by gcongr
    _ = ea + eb + ep := by ring

/-! ## Per-entry positive-half ledger -/

/-- The Kronecker coefficient of the scalar floor in a canonical entry. -/
noncomputable def p2EntryDiagonalIndicator (e : P2EntryIndex) : ℝ :=
  if e.row = e.col then 1 else 0

theorem p2EntryDiagonalIndicator_zero_or_one (e : P2EntryIndex) :
    p2EntryDiagonalIndicator e = 0 ∨ p2EntryDiagonalIndicator e = 1 := by
  unfold p2EntryDiagonalIndicator
  split <;> simp_all

/-- Raw (unnormalized) band integral on the positive half of the certified
frequency window.  Generated panel certificates naturally compute this
quantity; parity supplies the omitted negative half exactly. -/
noncomputable def p2PositiveHalfBandIntegral (e : P2EntryIndex) : ℝ :=
  match e.block with
  | .even => ∫ r in (0 : ℝ)..50, p2EvenBandIntegrand e.row.val e.col.val r
  | .odd => ∫ r in (0 : ℝ)..50, p2OddBandIntegrand e.row.val e.col.val r

/-- Legendre mode selected by a parity block and a block-local index. -/
def p2EntryPoleMode (block : P2EntryBlock) (k : Fin 24) : Fin 48 :=
  match block with
  | .even => ⟨2 * k.val, by omega⟩
  | .odd => ⟨2 * k.val + 1, by omega⟩

/-- Sign of the pole product after the even/odd parity reduction. -/
noncomputable def p2EntryPoleSign (block : P2EntryBlock) : ℝ :=
  match block with
  | .even => 1
  | .odd => -1

/-- Unsigned actual pole product for a parity-block entry. -/
noncomputable def p2UnsignedPoleContribution (e : P2EntryIndex) : ℝ :=
  2 * p2PoleCoeff (p2EntryPoleMode e.block e.col).val *
    p2PoleCoeff (p2EntryPoleMode e.block e.row).val

/-- The signed rank-two pole contribution, with the parity sign already
incorporated. -/
noncomputable def p2SignedPoleContribution (e : P2EntryIndex) : ℝ :=
  p2EntryPoleSign e.block * p2UnsignedPoleContribution e

/-- Fully finite Taylor-polynomial counterpart of the unsigned pole
product. -/
noncomputable def p2TaylorPoleContribution (e : P2EntryIndex) : ℝ :=
  2 * p2PoleTaylorPolynomialCoeff (p2EntryPoleMode e.block e.col).val *
    p2PoleTaylorPolynomialCoeff (p2EntryPoleMode e.block e.row).val

@[simp] theorem abs_p2EntryPoleSign (block : P2EntryBlock) :
    |p2EntryPoleSign block| = 1 := by
  cases block <;> simp [p2EntryPoleSign]

/-- A finite Taylor-product enclosure transfers to the correctly signed
actual pole contribution.  The `10⁻²⁸` term is proved analytically in
`P2PoleApprox`; a generated certificate supplies only `hfinite`. -/
theorem abs_p2SignedPoleContribution_sub_signedCenter_lt_of_taylor_enclosure
    (e : P2EntryIndex) (q ep : ℝ)
    (hfinite : |p2TaylorPoleContribution e - q| ≤ ep) :
    |p2SignedPoleContribution e - p2EntryPoleSign e.block * q| <
      1 / 10 ^ 28 + ep := by
  have hunsigned :=
    p2PoleEntry_sub_rational_abs_lt_of_taylor_enclosure
      (p2EntryPoleMode e.block e.col)
      (p2EntryPoleMode e.block e.row) q ep (by
        simpa [p2TaylorPoleContribution] using hfinite)
  rw [p2SignedPoleContribution,
    show p2EntryPoleSign e.block * p2UnsignedPoleContribution e -
        p2EntryPoleSign e.block * q =
      p2EntryPoleSign e.block * (p2UnsignedPoleContribution e - q) by ring,
    abs_mul, abs_p2EntryPoleSign, one_mul]
  simpa [p2UnsignedPoleContribution] using hunsigned

/-- Exact positive-half decomposition of either parity block entry. -/
theorem p2ScalarEntry_eq_positiveHalf (e : P2EntryIndex) :
    p2ScalarEntry e =
      GlideKernel.p2Alpha * p2EntryDiagonalIndicator e +
        (1 / (2 * Real.pi)) * (2 * p2PositiveHalfBandIntegral e) +
        p2SignedPoleContribution e := by
  rcases e with ⟨block, i, j⟩
  cases block <;>
    simp [p2ScalarEntry, p2EvenScalarEntry, p2OddScalarEntry,
      p2EntryDiagonalIndicator, p2PositiveHalfBandIntegral,
      p2SignedPoleContribution, p2EntryPoleSign,
      p2UnsignedPoleContribution, p2EntryPoleMode,
      integral_p2EvenBandIntegrand_symmetric,
      integral_p2OddBandIntegrand_symmetric] <;>
    ring

/-- Transfer a positive-half raw integral enclosure through the exact factor
`2/(2π)`.  Both the panel error and the rational-center magnitude are
doubled before applying `abs_normalizedIntegral_sub_center_mul_le`. -/
theorem abs_normalizedPositiveHalfIntegral_sub_center_mul_le
    {I R e B : ℝ} (he : 0 ≤ e) (hB : 0 ≤ B)
    (hIR : |I - R| ≤ e) (hR : |R| ≤ B) :
    |(1 / (2 * Real.pi)) * (2 * I) -
        p2InvTwoPiCenter * (2 * R)| ≤
      (8 / 25) * e + (2 / 10 ^ 20) * B := by
  have h2IR : |2 * I - 2 * R| ≤ 2 * e := by
    rw [show 2 * I - 2 * R = 2 * (I - R) by ring, abs_mul]
    norm_num
    linarith
  have h2R : |2 * R| ≤ 2 * B := by
    rw [abs_mul]
    norm_num
    linarith
  have h := abs_normalizedIntegral_sub_center_mul_le
    (I := 2 * I) (R := 2 * R) (e := 2 * e) (B := 2 * B)
    (by positivity) (by positivity) h2IR h2R
  convert h using 1 <;> ring

/-- Final generated-certificate interface for one canonical entry.

`R` is the exact rational center of the raw positive-half band integral and
`B` bounds its magnitude.  `P` is any signed rational pole center.  The
first three hypotheses are the analytic obligations; `hround` and `hbudget`
are exact rational inequalities discharged by the kernel for each generated
entry. -/
theorem abs_p2ScalarEntry_sub_storedCenter_le_of_positiveHalf
    (e : P2EntryIndex) {R eBand B P ePole eRound : ℝ}
    (heBand : 0 ≤ eBand) (hB : 0 ≤ B)
    (hband : |p2PositiveHalfBandIntegral e - R| ≤ eBand)
    (hR : |R| ≤ B)
    (hpole : |p2SignedPoleContribution e - P| ≤ ePole)
    (hround :
      |p2AlphaCenter * p2EntryDiagonalIndicator e +
          p2InvTwoPiCenter * (2 * R) + P - p2StoredCenter e| ≤ eRound)
    (hbudget :
      1 / 10 ^ 13 + ((8 / 25) * eBand + (2 / 10 ^ 20) * B) +
          ePole + eRound ≤ p2StoredRadius) :
    |p2ScalarEntry e - p2StoredCenter e| ≤ p2StoredRadius := by
  have halpha := (abs_p2Alpha_sub_center_lt).le
  have hnorm := abs_normalizedPositiveHalfIntegral_sub_center_mul_le
    heBand hB hband hR
  have hthree := abs_threeTermEntry_sub_approx_le
    (alpha := GlideKernel.p2Alpha) (alpha0 := p2AlphaCenter)
    (band := (1 / (2 * Real.pi)) * (2 * p2PositiveHalfBandIntegral e))
    (band0 := p2InvTwoPiCenter * (2 * R))
    (pole := p2SignedPoleContribution e) (pole0 := P)
    (ea := 1 / 10 ^ 13)
    (eb := (8 / 25) * eBand + (2 / 10 ^ 20) * B)
    (ep := ePole) (d := p2EntryDiagonalIndicator e)
    halpha hnorm hpole (p2EntryDiagonalIndicator_zero_or_one e)
  rw [p2ScalarEntry_eq_positiveHalf]
  calc
    |(GlideKernel.p2Alpha * p2EntryDiagonalIndicator e +
          (1 / (2 * Real.pi)) * (2 * p2PositiveHalfBandIntegral e) +
          p2SignedPoleContribution e) - p2StoredCenter e| ≤
        |(GlideKernel.p2Alpha * p2EntryDiagonalIndicator e +
            (1 / (2 * Real.pi)) * (2 * p2PositiveHalfBandIntegral e) +
            p2SignedPoleContribution e) -
          (p2AlphaCenter * p2EntryDiagonalIndicator e +
            p2InvTwoPiCenter * (2 * R) + P)| +
        |(p2AlphaCenter * p2EntryDiagonalIndicator e +
            p2InvTwoPiCenter * (2 * R) + P) - p2StoredCenter e| :=
      abs_sub_le _ _ _
    _ ≤ (1 / 10 ^ 13 +
          ((8 / 25) * eBand + (2 / 10 ^ 20) * B) + ePole) + eRound :=
      add_le_add hthree hround
    _ ≤ p2StoredRadius := by
      linarith

/-- Certificate-generator specialization of
`abs_p2ScalarEntry_sub_storedCenter_le_of_positiveHalf`.

The raw panel sum encloses the positive-half integral.  The pole input is an
enclosure of an entirely finite Taylor-polynomial expression; this theorem
adds the proved analytic Taylor remainder and the parity sign before closing
the entry against its stored center. -/
theorem abs_p2ScalarEntry_sub_storedCenter_le_of_positiveHalf_taylorPole
    (e : P2EntryIndex) {R eBand B qPole ePole eRound : ℝ}
    (heBand : 0 ≤ eBand) (hB : 0 ≤ B)
    (hband : |p2PositiveHalfBandIntegral e - R| ≤ eBand)
    (hR : |R| ≤ B)
    (hpole : |p2TaylorPoleContribution e - qPole| ≤ ePole)
    (hround :
      |p2AlphaCenter * p2EntryDiagonalIndicator e +
          p2InvTwoPiCenter * (2 * R) +
          p2EntryPoleSign e.block * qPole - p2StoredCenter e| ≤ eRound)
    (hbudget :
      1 / 10 ^ 13 + ((8 / 25) * eBand + (2 / 10 ^ 20) * B) +
          (1 / 10 ^ 28 + ePole) + eRound ≤ p2StoredRadius) :
    |p2ScalarEntry e - p2StoredCenter e| ≤ p2StoredRadius := by
  apply abs_p2ScalarEntry_sub_storedCenter_le_of_positiveHalf
    (e := e) (R := R) (eBand := eBand) (B := B)
    (P := p2EntryPoleSign e.block * qPole)
    (ePole := 1 / 10 ^ 28 + ePole) (eRound := eRound)
    heBand hB hband hR
  · exact
      (abs_p2SignedPoleContribution_sub_signedCenter_lt_of_taylor_enclosure
        e qPole ePole hpole).le
  · exact hround
  · exact hbudget

end RHP2Bridge
