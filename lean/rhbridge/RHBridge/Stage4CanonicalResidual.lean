/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage2DefectCharacterization

/-!
# Canonical comparator residual criterion

The zero-side formula gives a parsimonious criterion for a vector to lie in
the weak radical: all polarized symmetric-disk residuals must tend to zero.
For the CCM comparator this separates compact-zero convergence from the
genuinely uniform zero-tail problem.
-/

namespace RHP2Bridge.Stage4CanonicalResidual

open Filter Topology GeneralZetaWeilForm
open Stage2DefectCharacterization
open NestedSupport

/-- Zero-side spectral invisibility of a form-domain vector. -/
def SpectrallyInvisible {a : ℝ} (f : LogarithmicFormDomain a) : Prop :=
  ∀ g : LogarithmicFormDomain a,
    Tendsto (fun R : ℝ ↦ zeroCrossInDisk R f g) atTop (𝓝 0)

/-- Spectral invisibility is exactly enough to force the weak radical
identity, by uniqueness of the Guinand--Weil disk limit. -/
theorem weilCross_eq_zero_of_spectrallyInvisible
    {a : ℝ} {f : LogarithmicFormDomain a}
    (hf : SpectrallyInvisible f)
    (g : LogarithmicFormDomain a) :
    SupportDecomposition.weilCross a f.val g.val = 0 := by
  have hform := zeroCrossInDisk_tendsto_weilCross f g
  have hzero := hf g
  have hc : (SupportDecomposition.weilCross a f.val g.val : ℂ) = 0 :=
    tendsto_nhds_unique hform hzero
  exact_mod_cast hc

/-- Vanishing of the unpolarized symmetric-disk zero sum. -/
def DiagonallySpectrallyInvisible {a : ℝ}
    (f : LogarithmicFormDomain a) : Prop :=
  Tendsto (fun R : ℝ ↦ GuinandWeilFormula.zeroSumInDisk R a f.val)
    atTop (𝓝 0)

/-- Diagonal spectral invisibility forces zero Weil energy by uniqueness of
the Guinand--Weil disk limit. -/
theorem logarithmicWeilForm_eq_zero_of_diagonalSpectralInvisibility
    {a : ℝ} {f : LogarithmicFormDomain a}
    (hf : DiagonallySpectrallyInvisible f) :
    logarithmicWeilForm a f = 0 := by
  have hform :=
    GuinandWeilLiterature.logarithmic_zero_disk_limit_eq_weilForm f
  have hc : (logarithmicWeilForm a f : ℂ) = 0 :=
    tendsto_nhds_unique hform hf
  exact_mod_cast hc

/-! ## The support/zero-radius limit interchange

The CCM construction supplies a *sequence* of comparison vectors.  Compact-local
transform convergence controls each fixed zero disk.  The following definitions
isolate the one additional estimate needed to pass to the full Weil form. -/

/-- Every fixed symmetric zero disk eventually fails to see the comparator
sequence.  This is the part supplied by compact-local convergence to `Xi`. -/
def FixedDiskInvisible {a : ℝ}
    (f : ℕ → LogarithmicFormDomain a) : Prop :=
  ∀ (R : ℝ) (g : LogarithmicFormDomain a),
    Tendsto (fun n ↦ zeroCrossInDisk R (f n) g) atTop (𝓝 0)

/-- Eventual uniform control of the omitted zero tail.  Uniformity in all
sufficiently large `n` is the load-bearing fact absent from compact-local
convergence; no condition is imposed on a finite initial segment. -/
def UniformZeroTail {a : ℝ}
    (f : ℕ → LogarithmicFormDomain a) : Prop :=
  ∀ (g : LogarithmicFormDomain a) (ε : ℝ), 0 < ε →
    ∃ (N₀ : ℕ) (R₀ : ℝ), ∀ n ≥ N₀, ∀ R ≥ R₀,
      dist (zeroCrossInDisk R (f n) g)
        (SupportDecomposition.weilCross a (f n).val g.val : ℂ) < ε

/-- The desired conclusion: the canonical comparators form an approximate
weak radical for the full (not truncated-in-zero-height) Weil form. -/
def AsymptoticallyWeakRadical {a : ℝ}
    (f : ℕ → LogarithmicFormDomain a) : Prop :=
  ∀ g : LogarithmicFormDomain a,
    Tendsto
      (fun n ↦ (SupportDecomposition.weilCross a (f n).val g.val : ℂ))
      atTop (𝓝 0)

/-- Moore--Osgood in the exact form required here: fixed-disk invisibility plus
a comparator-uniform zero tail proves the full weak-radical limit. -/
theorem asymptoticallyWeakRadical_of_fixedDisk_of_uniformZeroTail
    {a : ℝ} {f : ℕ → LogarithmicFormDomain a}
    (hfixed : FixedDiskInvisible f) (htail : UniformZeroTail f) :
    AsymptoticallyWeakRadical f := by
  intro g
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N₀, R₀, hR₀⟩ := htail g (ε / 2) (half_pos hε)
  have hdisk := (Metric.tendsto_atTop.mp (hfixed R₀ g)) (ε / 2) (half_pos hε)
  obtain ⟨N, hN⟩ := hdisk
  refine ⟨max N N₀, fun n hn ↦ ?_⟩
  have hnN : N ≤ n := le_trans (le_max_left N N₀) hn
  have hnN₀ : N₀ ≤ n := le_trans (le_max_right N N₀) hn
  calc
    dist (↑(SupportDecomposition.weilCross a (f n).val g.val) : ℂ) 0 =
        dist 0 (↑(SupportDecomposition.weilCross a (f n).val g.val) : ℂ) :=
          dist_comm _ _
    _ ≤ dist 0 (zeroCrossInDisk R₀ (f n) g) +
          dist (zeroCrossInDisk R₀ (f n) g)
            (↑(SupportDecomposition.weilCross a (f n).val g.val) : ℂ) :=
          dist_triangle _ _ _
    _ < ε / 2 + ε / 2 :=
      add_lt_add (by simpa [dist_comm] using hN n hnN)
        (hR₀ n hnN₀ R₀ le_rfl)
    _ = ε := by ring

/-! ## Correct moving-support formulation

The actual CCM vectors do not lie in one fixed interval: their support radii
increase.  A fixed compact test must therefore be included into each larger
form domain before it is paired with the comparator. -/

/-- Full Weil pairing of a moving-support vector with a fixed compact test. -/
noncomputable def movingWeilCross {a : ℕ → ℝ} (f : (n : ℕ) → LogarithmicFormDomain (a n))
    {b : ℝ} (hba : ∀ n, b ≤ a n) (g : LogarithmicFormDomain b) (n : ℕ) : ℂ :=
  SupportDecomposition.weilCross (a n) (f n).val
    (nestedLogarithmicSupport (hba n) g).val

/-- Symmetric-zero-disk pairing in the same moving-support geometry. -/
noncomputable def movingZeroCrossInDisk {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) {b : ℝ}
    (hba : ∀ n, b ≤ a n) (g : LogarithmicFormDomain b)
    (R : ℝ) (n : ℕ) : ℂ :=
  zeroCrossInDisk R (f n) (nestedLogarithmicSupport (hba n) g)

def MovingFixedDiskInvisibleAt {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) {b : ℝ}
    (hba : ∀ n, b ≤ a n) : Prop :=
  ∀ (R : ℝ) (g : LogarithmicFormDomain b),
    Tendsto (movingZeroCrossInDisk f hba g R) atTop (𝓝 0)

def MovingUniformZeroTailAt {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) {b : ℝ}
    (hba : ∀ n, b ≤ a n) : Prop :=
  ∀ (g : LogarithmicFormDomain b) (ε : ℝ), 0 < ε →
    ∃ (N₀ : ℕ) (R₀ : ℝ), ∀ n ≥ N₀, ∀ R ≥ R₀,
      dist (movingZeroCrossInDisk f hba g R n) (movingWeilCross f hba g n) < ε

/-- The corrected Stage-4 limit interchange, on every fixed compact test
space embedded into the growing CCM windows. -/
theorem movingWeilCross_tendsto_zero_of_fixedDisk_of_uniformZeroTail
    {a : ℕ → ℝ} {f : (n : ℕ) → LogarithmicFormDomain (a n)} {b : ℝ}
    (hba : ∀ n, b ≤ a n) (hfixed : MovingFixedDiskInvisibleAt f hba)
    (htail : MovingUniformZeroTailAt f hba) (g : LogarithmicFormDomain b) :
    Tendsto (movingWeilCross f hba g) atTop (𝓝 0) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N₀, R₀, hR₀⟩ := htail g (ε / 2) (half_pos hε)
  obtain ⟨N, hN⟩ :=
    (Metric.tendsto_atTop.mp (hfixed R₀ g)) (ε / 2) (half_pos hε)
  refine ⟨max N N₀, fun n hn ↦ ?_⟩
  have hnN : N ≤ n := le_trans (le_max_left N N₀) hn
  have hnN₀ : N₀ ≤ n := le_trans (le_max_right N N₀) hn
  calc
    dist (movingWeilCross f hba g n) 0 =
        dist 0 (movingWeilCross f hba g n) := dist_comm _ _
    _ ≤ dist 0 (movingZeroCrossInDisk f hba g R₀ n) +
          dist (movingZeroCrossInDisk f hba g R₀ n)
            (movingWeilCross f hba g n) := dist_triangle _ _ _
    _ < ε / 2 + ε / 2 :=
      add_lt_add (by simpa [dist_comm] using hN n hnN)
        (hR₀ n hnN₀ R₀ le_rfl)
    _ = ε := by ring

/-- The key strip-uniform gain in the quadratic zero summand: the losses of
the two complementary Mellin factors cancel exactly. -/
theorem paired_strip_exponents_cancel (scale : ℝ) (hscale : 0 < scale) (α : ℝ) :
    scale ^ (-1 / 2 - α) * scale ^ (-1 / 2 + α) = scale⁻¹ := by
  rw [← Real.rpow_add hscale]
  convert Real.rpow_neg_one scale using 1 <;> ring

/-! A cofinal cutoff depending on the comparator scale is enough.  This is
strictly weaker than uniform convergence of the zero tails and is the form
matched by the low/high zero split. -/

def ScheduledDiskInvisibleAt {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) {b : ℝ}
    (hba : ∀ n, b ≤ a n) (cutoff : ℕ → ℝ) : Prop :=
  Tendsto cutoff atTop atTop ∧
    ∀ g : LogarithmicFormDomain b,
      Tendsto (fun n ↦ movingZeroCrossInDisk f hba g (cutoff n) n)
        atTop (𝓝 0)

def ScheduledZeroTailAt {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) {b : ℝ}
    (hba : ∀ n, b ≤ a n) (cutoff : ℕ → ℝ) : Prop :=
  ∀ g : LogarithmicFormDomain b,
    Tendsto (fun n ↦ dist
      (movingZeroCrossInDisk f hba g (cutoff n) n)
      (movingWeilCross f hba g n)) atTop (𝓝 0)

/-- Scheduled low-zero convergence plus scheduled high-zero control gives the
full moving-support weak residual.  No uniform interchange of limits is
required. -/
theorem movingWeilCross_tendsto_zero_of_scheduled_split
    {a : ℕ → ℝ} {f : (n : ℕ) → LogarithmicFormDomain (a n)} {b : ℝ}
    (hba : ∀ n, b ≤ a n) {cutoff : ℕ → ℝ}
    (hlow : ScheduledDiskInvisibleAt f hba cutoff)
    (hhigh : ScheduledZeroTailAt f hba cutoff)
    (g : LogarithmicFormDomain b) :
    Tendsto (movingWeilCross f hba g) atTop (𝓝 0) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N₁, hN₁⟩ :=
    (Metric.tendsto_atTop.mp (hlow.2 g)) (ε / 2) (half_pos hε)
  obtain ⟨N₂, hN₂⟩ :=
    (Metric.tendsto_atTop.mp (hhigh g)) (ε / 2) (half_pos hε)
  refine ⟨max N₁ N₂, fun n hn ↦ ?_⟩
  have hn₁ : N₁ ≤ n := le_trans (le_max_left N₁ N₂) hn
  have hn₂ : N₂ ≤ n := le_trans (le_max_right N₁ N₂) hn
  have htail : dist
      (movingZeroCrossInDisk f hba g (cutoff n) n)
      (movingWeilCross f hba g n) < ε / 2 := by
    simpa only [Real.dist_eq, sub_zero, abs_of_nonneg dist_nonneg] using hN₂ n hn₂
  calc
    dist (movingWeilCross f hba g n) 0 =
        dist 0 (movingWeilCross f hba g n) := dist_comm _ _
    _ ≤ dist 0 (movingZeroCrossInDisk f hba g (cutoff n) n) +
          dist (movingZeroCrossInDisk f hba g (cutoff n) n)
            (movingWeilCross f hba g n) := dist_triangle _ _ _
    _ < ε / 2 + ε / 2 :=
      add_lt_add (by simpa [dist_comm] using hN₁ n hn₁) htail
    _ = ε := by ring

end RHP2Bridge.Stage4CanonicalResidual
