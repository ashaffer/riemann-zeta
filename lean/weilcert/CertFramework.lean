/-
CertFramework: the certificate calculus of `Weilcert.lean`, generalized to
arbitrary dimension n over an arbitrary linearly ordered field.

`Weilcert.lean` proves one 12-dimensional instance (`weil_window_positive`)
with all algebra inlined at n = 12 over ℚ.  This file restates the entire
argument so that a future window certificate has to supply *only data*:

  * `quad_of_ldl`   — quadratic form of a congruence  c² A = Wᵀ diag(g) W
                      (lifted verbatim; it was already n-generic),
  * `pert_bound`    — |xᵀ E x| ≤ n · d · |x|²  for entrywise |E| ≤ d,
  * `resolve` / `y_exists` — injectivity of x ↦ W x from the one-sided
                      inverse identity  Wi · W = f · 1  (f ≠ 0),
  * `ldl_quad_pos`  — strict positivity of the quadratic form from the
                      integer congruence certificate,
  * `cert_window_positive` — the full window theorem: every matrix M
                      entrywise within δ of A/scale has 0 < xᵀ M x for all
                      x ≠ 0, provided n · (scale · δ) ≤ s and
                      c² (A − s·1) = Wᵀ diag(g) W with g > 0.

`CertInstance.lean` re-derives the kernel-checked 12-dimensional window of
`Weilcert.lean` through this framework as a consistency check.

Axiom base: propext, Classical.choice, Quot.sound only.
-/
import Mathlib

namespace CertFramework

open Matrix Finset

section CommRing

variable {K : Type*} [CommRing K] {n : ℕ}

/-! ## Congruence: quadratic form of `A = L diag(d) Lᵀ` -/

/-- If `A i j = ∑ k, L i k * d k * L j k` then the quadratic form of `A` is the
`d`-weighted sum of squares of the coordinates `∑ i, x i * L i k`.
(Lifted from `WeilCert.quad_of_ldl`, which is stated over ℚ; only the
commutative ring structure is used.) -/
theorem quad_of_ldl (A L : Matrix (Fin n) (Fin n) K) (d : Fin n → K)
    (hA : ∀ i j, A i j = ∑ k, L i k * d k * L j k) (x : Fin n → K) :
    x ⬝ᵥ A *ᵥ x = ∑ k, d k * (∑ i, x i * L i k) ^ 2 := by
  have expand : x ⬝ᵥ A *ᵥ x = ∑ i, ∑ j, x i * A i j * x j := by
    unfold Matrix.mulVec dotProduct
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by ring
  rw [expand]
  have h1 : ∀ i j, x i * A i j * x j
      = ∑ k, d k * ((x i * L i k) * (x j * L j k)) := by
    intro i j
    rw [hA, Finset.mul_sum, Finset.sum_mul]
    exact Finset.sum_congr rfl fun k _ => by ring
  simp_rw [h1]
  have h2 : (∑ i, ∑ j, ∑ k, d k * ((x i * L i k) * (x j * L j k)))
      = ∑ k, ∑ i, ∑ j, d k * ((x i * L i k) * (x j * L j k)) := by
    calc ∑ i, ∑ j, ∑ k, d k * ((x i * L i k) * (x j * L j k))
        = ∑ i, ∑ k, ∑ j, d k * ((x i * L i k) * (x j * L j k)) :=
          Finset.sum_congr rfl fun i _ => Finset.sum_comm
      _ = ∑ k, ∑ i, ∑ j, d k * ((x i * L i k) * (x j * L j k)) :=
          Finset.sum_comm
  rw [h2]
  refine Finset.sum_congr rfl fun k _ => ?_
  calc ∑ i, ∑ j, d k * ((x i * L i k) * (x j * L j k))
      = ∑ i, (x i * L i k) * (d k * ∑ j, x j * L j k) := by
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Finset.mul_sum]
        refine Eq.trans ?_ (Finset.mul_sum _ _ _).symm
        exact Finset.sum_congr rfl fun j _ => by ring
    _ = (∑ i, x i * L i k) * (d k * ∑ j, x j * L j k) := by
        rw [← Finset.sum_mul]
    _ = d k * (∑ i, x i * L i k) ^ 2 := by ring

end CommRing

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {n : ℕ}

/-! ## Perturbation -/

/-- Entrywise bound to quadratic-form bound:
`|xᵀ E x| ≤ n · d · ⟨x, x⟩` when `|E i j| ≤ d`.
(`WeilCert.pert_bound` at n = 12 over ℚ.) -/
theorem pert_bound (E : Matrix (Fin n) (Fin n) K) (d : K) (hd : 0 ≤ d)
    (hE : ∀ i j, |E i j| ≤ d) (x : Fin n → K) :
    |x ⬝ᵥ E *ᵥ x| ≤ n * d * (x ⬝ᵥ x) := by
  have hxEx : x ⬝ᵥ E *ᵥ x = ∑ i, x i * ∑ j, E i j * x j := by
    unfold Matrix.mulVec dotProduct
    rfl
  rw [hxEx]
  have habs : |∑ i, x i * ∑ j, E i j * x j| ≤ d * (∑ i, |x i|) ^ 2 := by
    have step1 : |∑ i, x i * ∑ j, E i j * x j| ≤ ∑ i, |x i| * ∑ j, d * |x j| := by
      refine (Finset.abs_sum_le_sum_abs _ _).trans ?_
      refine Finset.sum_le_sum fun i _ => ?_
      rw [abs_mul]
      refine mul_le_mul_of_nonneg_left ?_ (abs_nonneg _)
      refine (Finset.abs_sum_le_sum_abs _ _).trans ?_
      refine Finset.sum_le_sum fun j _ => ?_
      rw [abs_mul]
      exact mul_le_mul_of_nonneg_right (hE i j) (abs_nonneg _)
    refine step1.trans ?_
    have : ∑ i, |x i| * ∑ j, d * |x j|
        = d * ((∑ i, |x i|) * (∑ j, |x j|)) := by
      rw [← Finset.mul_sum, ← Finset.sum_mul]
      ring
    rw [this, sq]
  refine habs.trans ?_
  have hcs : (∑ i, |x i|) ^ 2 ≤ (n : K) * ∑ i, |x i| ^ 2 := by
    simpa using sq_sum_le_card_mul_sum_sq (s := Finset.univ)
      (f := fun i : Fin n => |x i|)
  have hsq : (∑ i, |x i| ^ 2) = x ⬝ᵥ x := by
    unfold dotProduct
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [sq_abs, sq]
  calc d * (∑ i, |x i|) ^ 2 ≤ d * ((n : K) * ∑ i, |x i| ^ 2) :=
        mul_le_mul_of_nonneg_left hcs hd
    _ = n * d * (x ⬝ᵥ x) := by rw [hsq]; ring

/-! ## Reconstruction from a one-sided inverse -/

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- With `Wi * W = f * 1` entrywise, `f * x j` is recovered from the
coordinates `y k = ∑ i, x i * W k i`.  (`WeilCert.resolve` generalized.) -/
theorem resolve (W Wi : Matrix (Fin n) (Fin n) K) (f : K)
    (hwinv : ∀ i j, (∑ k, Wi i k * W k j) = if i = j then f else 0)
    (x : Fin n → K) (j : Fin n) :
    f * x j = ∑ k, Wi j k * (∑ i, x i * W k i) := by
  have h : (∑ k, Wi j k * (∑ i, x i * W k i))
      = ∑ i, x i * ∑ k, Wi j k * W k i := by
    calc ∑ k, Wi j k * (∑ i, x i * W k i)
        = ∑ k, ∑ i, Wi j k * (x i * W k i) := by
          exact Finset.sum_congr rfl fun k _ => Finset.mul_sum _ _ _
      _ = ∑ i, ∑ k, Wi j k * (x i * W k i) := Finset.sum_comm
      _ = ∑ i, x i * ∑ k, Wi j k * W k i := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Finset.mul_sum]
          exact Finset.sum_congr rfl fun k _ => by ring
  rw [h]
  simp_rw [hwinv, mul_ite, mul_zero]
  rw [Finset.sum_ite_eq Finset.univ j (fun i => x i * f)]
  simp [mul_comm]

/-- Injectivity: if `x ≠ 0` then some certificate coordinate
`∑ i, x i * W k i` is nonzero.  (`WeilCert.y_exists` generalized.) -/
theorem y_exists (W Wi : Matrix (Fin n) (Fin n) K) {f : K} (hf : f ≠ 0)
    (hwinv : ∀ i j, (∑ k, Wi i k * W k j) = if i = j then f else 0)
    {x : Fin n → K} (hx : x ≠ 0) :
    ∃ k, (∑ i, x i * W k i) ≠ 0 := by
  by_contra hall
  push Not at hall
  apply hx
  funext j
  have h := resolve W Wi f hwinv x j
  simp only [hall, mul_zero, Finset.sum_const_zero] at h
  have hxj := (mul_eq_zero.mp h).resolve_left hf
  simpa using hxj

/-! ## Positivity from the integer congruence certificate -/

/-- Strict positivity of the quadratic form of `A` from a congruence
`c² A = Wᵀ diag(g) W` with `g > 0`, `c ≠ 0`, and a one-sided inverse
witnessing that `W` has full rank.  (`WeilCert.bq_quad_pos` generalized.) -/
theorem ldl_quad_pos (A W Wi : Matrix (Fin n) (Fin n) K) (g : Fin n → K)
    (c f : K)
    (hkey : ∀ i j, c ^ 2 * A i j = ∑ k, W k i * g k * W k j)
    (hwinv : ∀ i j, (∑ k, Wi i k * W k j) = if i = j then f else 0)
    (hg : ∀ k, 0 < g k) (hc : c ≠ 0) (hf : f ≠ 0)
    {x : Fin n → K} (hx : x ≠ 0) : 0 < x ⬝ᵥ A *ᵥ x := by
  have hkey' : ∀ i j, ((c ^ 2 • A) i j) = ∑ k, Wᵀ i k * g k * Wᵀ j k := by
    intro i j
    simp only [Matrix.smul_apply, smul_eq_mul, Matrix.transpose_apply]
    exact hkey i j
  have hquad := quad_of_ldl (c ^ 2 • A) Wᵀ g hkey' x
  have hsmul : x ⬝ᵥ (c ^ 2 • A) *ᵥ x = c ^ 2 * (x ⬝ᵥ A *ᵥ x) := by
    rw [smul_mulVec, dotProduct_smul, smul_eq_mul]
  rw [hsmul] at hquad
  have hpos : 0 < ∑ k, g k * (∑ i, x i * Wᵀ i k) ^ 2 := by
    obtain ⟨k, hk⟩ := y_exists W Wi hf hwinv hx
    have hk' : (∑ i, x i * Wᵀ i k) ≠ 0 := by
      simpa [Matrix.transpose_apply] using hk
    refine Finset.sum_pos' (fun m _ => ?_) ⟨k, Finset.mem_univ k, ?_⟩
    · have h1 : (0 : K) < g m := hg m
      positivity
    · have h1 : (0 : K) < g k := hg k
      have h2 : (0 : K) < (∑ i, x i * Wᵀ i k) ^ 2 := by positivity
      positivity
  have hc2 : (0 : K) < c ^ 2 := by positivity
  nlinarith [hquad, hpos, hc2]

/-! ## The generic window theorem -/

/-- **Generic certificate window positivity.**  Data: an n×n matrix `A` (the
scaled midpoint, `A = scale * midpoint`), a congruence
`c² (A − s·1) = Wᵀ diag(g) W` with `g > 0`, a one-sided inverse `Wi W = f·1`
with `f ≠ 0`, and the margin condition `n · (scale · δ) ≤ s`.  Conclusion:
every matrix `M` entrywise within `δ` of `A / scale` has a strictly positive
quadratic form.  (`WeilCert.weil_window_positive` is the instance
n = 12, K = ℚ, scale = 10²⁴, δ = 10⁻²⁰, s = 120000.) -/
theorem cert_window_positive
    (A W Wi : Matrix (Fin n) (Fin n) K) (g : Fin n → K) (c f s scale δ : K)
    (hkey : ∀ i j,
      c ^ 2 * (A i j - if i = j then s else 0) = ∑ k, W k i * g k * W k j)
    (hwinv : ∀ i j, (∑ k, Wi i k * W k j) = if i = j then f else 0)
    (hg : ∀ k, 0 < g k) (hc : c ≠ 0) (hf : f ≠ 0)
    (hscale : 0 < scale) (hδ : 0 ≤ δ) (hs : (n : K) * (scale * δ) ≤ s)
    (M : Matrix (Fin n) (Fin n) K) (hM : ∀ i j, |M i j - A i j / scale| ≤ δ)
    {x : Fin n → K} (hx : x ≠ 0) : 0 < x ⬝ᵥ M *ᵥ x := by
  set N : Matrix (Fin n) (Fin n) K := scale • M with hN
  set B : Matrix (Fin n) (Fin n) K :=
    Matrix.of fun i j => A i j - if i = j then s else 0 with hB
  set E : Matrix (Fin n) (Fin n) K := N - A with hE
  have hEbound : ∀ i j, |E i j| ≤ scale * δ := by
    intro i j
    have h := hM i j
    have hexp : E i j = scale * (M i j - A i j / scale) := by
      simp only [hE, hN, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]
      field_simp
    rw [hexp, abs_mul, abs_of_pos hscale]
    exact mul_le_mul_of_nonneg_left h hscale.le
  have hsplit : N = B + s • (1 : Matrix (Fin n) (Fin n) K) + E := by
    ext i j
    have hB' : B i j = A i j - if i = j then s else 0 := rfl
    have h1 : (s • (1 : Matrix (Fin n) (Fin n) K)) i j
        = if i = j then s else 0 := by
      simp [Matrix.one_apply, mul_ite]
    simp only [Matrix.add_apply, hB', h1, hE, Matrix.sub_apply]
    ring
  have hq : x ⬝ᵥ N *ᵥ x
      = x ⬝ᵥ B *ᵥ x + s * (x ⬝ᵥ x) + x ⬝ᵥ E *ᵥ x := by
    rw [hsplit, add_mulVec, add_mulVec, dotProduct_add, dotProduct_add,
      smul_mulVec, one_mulVec, dotProduct_smul]
    simp [smul_eq_mul]
  have hBkey : ∀ i j, c ^ 2 * B i j = ∑ k, W k i * g k * W k j := by
    intro i j
    simpa [hB] using hkey i j
  have h1 : 0 < x ⬝ᵥ B *ᵥ x :=
    ldl_quad_pos B W Wi g c f hBkey hwinv hg hc hf hx
  have h2 := pert_bound E (scale * δ) (by positivity) hEbound x
  have h3 : -((n : K) * (scale * δ) * (x ⬝ᵥ x)) ≤ x ⬝ᵥ E *ᵥ x :=
    neg_le_of_abs_le h2
  have hxx : 0 ≤ x ⬝ᵥ x := by
    unfold dotProduct
    exact Finset.sum_nonneg fun i _ => mul_self_nonneg (x i)
  have hNpos : 0 < x ⬝ᵥ N *ᵥ x := by
    rw [hq]
    nlinarith [h1, h3, mul_le_mul_of_nonneg_right hs hxx]
  have hNq : x ⬝ᵥ N *ᵥ x = scale * (x ⬝ᵥ M *ᵥ x) := by
    rw [hN, smul_mulVec, dotProduct_smul, smul_eq_mul]
  rw [hNq] at hNpos
  have hdiv : x ⬝ᵥ M *ᵥ x = (scale * (x ⬝ᵥ M *ᵥ x)) / scale := by
    field_simp
  rw [hdiv]
  exact div_pos hNpos hscale

end CertFramework
