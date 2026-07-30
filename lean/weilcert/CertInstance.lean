/-
CertInstance: consistency check for `CertFramework.lean`.

The kernel-checked 12-dimensional window of `Weilcert.lean`
(`WeilCert.weil_window_positive` / `WeilCert.mRat_positive`) is re-derived
here through the dimension- and field-generic `CertFramework.cert_window_positive`,
consuming exactly the integer data and kernel-checked facts of `Weilcert.lean`
(`key_q`, `winv_q`, `g_pos`, `f_pos`, `c_ne`).  This certifies that the
generic framework specializes to the existing certificate, so future windows
(other n, other L) only need to supply data plus the `decide`-checked integer
congruence.

It also casts the same certificate to `ℝ` and instantiates the generic theorem
there.  This direct scalar extension is what justifies strict positivity for
real matrices and real vectors; a continuity/density argument alone would only
give nonnegativity in the limit.

Axiom base: propext, Classical.choice, Quot.sound only.
-/
import Weilcert
import CertFramework

namespace CertInstance

open Matrix WeilCert

/-- `WeilCert.weil_window_positive`, re-proved through the generic framework:
every rational 12×12 matrix entrywise within `1e-20` of `mRat` has a strictly
positive quadratic form. -/
theorem weil_window_positive_via_framework (M : Matrix (Fin 12) (Fin 12) ℚ)
    (hM : ∀ i j, |M i j - mRat i j| ≤ delta)
    (x : Fin 12 → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ M *ᵥ x := by
  refine CertFramework.cert_window_positive aQ wQ wiQ gQ (cInt : ℚ) (fInt : ℚ)
    120000 (10 ^ 24) (1 / 10 ^ 20) ?_ winv_q
    (fun k => by unfold gQ; exact_mod_cast g_pos k) c_ne
    (by exact_mod_cast f_pos.ne') (by norm_num) (by norm_num) (by norm_num)
    M ?_ hx
  · intro i j
    rw [← bq_eq]
    exact key_q i j
  · intro i j
    have h := hM i j
    have hmid : mRat i j = aQ i j / 10 ^ 24 := rfl
    rwa [hmid] at h

/-- The certificate midpoint matrix itself, via the framework. -/
theorem mRat_positive_via_framework (x : Fin 12 → ℚ) (hx : x ≠ 0) :
    0 < x ⬝ᵥ mRat *ᵥ x := by
  refine weil_window_positive_via_framework mRat (fun i j => ?_) x hx
  simp only [sub_self, abs_zero]
  norm_num [delta]

/-! ## Direct scalar extension to `ℝ` -/

/-- The integer certificate data, cast through `ℚ` to `ℝ`. -/
noncomputable def aReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => (aQ i j : ℝ)

noncomputable def wReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => (wQ i j : ℝ)

noncomputable def wiReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => (wiQ i j : ℝ)

noncomputable def gReal : Fin 12 → ℝ := fun k => (gQ k : ℝ)

/-- The rational midpoint matrix viewed over `ℝ`. -/
noncomputable def mRatReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => (mRat i j : ℝ)

lemma key_real (i j : Fin 12) :
    (cInt : ℝ) ^ 2 * (aReal i j - if i = j then (120000 : ℝ) else 0)
      = ∑ k, wReal k i * gReal k * wReal k j := by
  have h := key_q i j
  rw [bq_eq] at h
  have hReal := congrArg (fun q : ℚ => (q : ℝ)) h
  push_cast at hReal
  by_cases hij : i = j
  · subst j
    simpa [aReal, wReal, gReal] using hReal
  · simpa [aReal, wReal, gReal, hij] using hReal

lemma winv_real (i j : Fin 12) :
    (∑ k, wiReal i k * wReal k j) = if i = j then (fInt : ℝ) else 0 := by
  have h := winv_q i j
  have hReal := congrArg (fun q : ℚ => (q : ℝ)) h
  push_cast at hReal
  by_cases hij : i = j
  · subst j
    simpa [wiReal, wReal] using hReal
  · simpa [wiReal, wReal, hij] using hReal

lemma g_pos_real : ∀ k, 0 < gReal k := by
  intro k
  simp only [gReal, gQ]
  exact_mod_cast g_pos k

/-- The 12-dimensional certificate window over `ℝ`.

Every real matrix (symmetry is not required) entrywise within `delta = 1e-20`
of the real scalar extension of `mRat` has a strictly positive quadratic form
on every nonzero real vector.  This is a direct application of the exact
congruence certificate over `ℝ`, not an appeal to density. -/
theorem real_window_positive_via_framework (M : Matrix (Fin 12) (Fin 12) ℝ)
    (hM : ∀ i j, |M i j - mRatReal i j| ≤ (delta : ℝ))
    (x : Fin 12 → ℝ) (hx : x ≠ 0) : 0 < x ⬝ᵥ M *ᵥ x := by
  refine CertFramework.cert_window_positive aReal wReal wiReal gReal
    (cInt : ℝ) (fInt : ℝ) 120000 (10 ^ 24) (delta : ℝ)
    key_real winv_real g_pos_real ?_ ?_ (by norm_num) (by norm_num [delta])
    (by norm_num [delta]) M ?_ hx
  · exact_mod_cast c_ne
  · have hf : fInt ≠ 0 := ne_of_gt f_pos
    exact_mod_cast hf
  · intro i j
    have h := hM i j
    have hmid : mRatReal i j = aReal i j / 10 ^ 24 := by
      simp [mRatReal, mRat, aReal, aQ]
    rwa [hmid] at h

end CertInstance
