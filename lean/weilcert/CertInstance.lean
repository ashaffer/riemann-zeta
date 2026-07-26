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

end CertInstance
