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
  * `two_by_two_strict_lower_bound` — the scalar Schur-complement step used
                      to combine a finite block with its orthogonal complement,
  * `hilbert_two_block_strict_lower_bound` — the same transfer for an
                      orthogonal decomposition in a real inner-product space,
  * `hilbert_two_block_strict_lower_bound` — the corresponding transfer from
                      orthogonal vectors to the full quadratic-form estimate,
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

/-! ## Two-by-two block positivity -/

/-- **Strict Schur-complement criterion for a two-by-two quadratic form.**

If both diagonal entries lie strictly above `γ` and the shifted determinant
is positive, then the quadratic form with off-diagonal entry `-c` is strictly
larger than `γ` times the Euclidean norm on every nonzero pair.  This is the
scalar algebra used in the finite/complement block step of the unrestricted
`FULLINF` certificate. -/
theorem two_by_two_strict_lower_bound (beta d c gamma x y : K)
    (hbeta : gamma < beta) (hd : gamma < d)
    (hdet : c ^ 2 < (beta - gamma) * (d - gamma))
    (hxy : (x, y) ≠ (0, 0)) :
    gamma * (x ^ 2 + y ^ 2)
      < beta * x ^ 2 + d * y ^ 2 - 2 * c * x * y := by
  have hB : 0 < beta - gamma := sub_pos.mpr hbeta
  have hD : 0 < d - gamma := sub_pos.mpr hd
  have hq : 0 <
      (beta - gamma) * x ^ 2 + (d - gamma) * y ^ 2 - 2 * c * x * y := by
    by_cases hy : y = 0
    · have hx : x ≠ 0 := by
        intro hx
        apply hxy
        simp [hx, hy]
      simp only [hy, ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow,
        mul_zero, add_zero, sub_zero]
      exact mul_pos hB (sq_pos_of_ne_zero hx)
    · by_cases hx : x = 0
      · simp only [hx, ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow,
          mul_zero, zero_mul, zero_add, sub_zero]
        exact mul_pos hD (sq_pos_of_ne_zero hy)
      · have hdet' : 0 < (beta - gamma) * (d - gamma) - c ^ 2 :=
          sub_pos.mpr hdet
        have hrhs : 0 < ((beta - gamma) * x - c * y) ^ 2
            + ((beta - gamma) * (d - gamma) - c ^ 2) * y ^ 2 :=
          add_pos_of_nonneg_of_pos (sq_nonneg _)
            (mul_pos hdet' (sq_pos_of_ne_zero hy))
        have hid :
            (beta - gamma) *
                ((beta - gamma) * x ^ 2 + (d - gamma) * y ^ 2 - 2 * c * x * y)
              = ((beta - gamma) * x - c * y) ^ 2
                + ((beta - gamma) * (d - gamma) - c ^ 2) * y ^ 2 := by
          ring
        have hmul : 0 < (beta - gamma) *
            ((beta - gamma) * x ^ 2 + (d - gamma) * y ^ 2 - 2 * c * x * y) := by
          rw [hid]
          exact hrhs
        exact ((mul_pos_iff.mp hmul).resolve_right
          (fun hneg => not_lt_of_ge hB.le hneg.1)).2
  have hshift :
      (beta * x ^ 2 + d * y ^ 2 - 2 * c * x * y)
          - gamma * (x ^ 2 + y ^ 2)
        = (beta - gamma) * x ^ 2 + (d - gamma) * y ^ 2 - 2 * c * x * y := by
    ring
  apply sub_pos.mp
  rw [hshift]
  exact hq

section RealInnerProductSpace

open scoped InnerProductSpace

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]

/-- **F8 two-block transfer on a real inner-product space.**

Suppose `u` and `w` are orthogonal and a real-valued quadratic-form expression
at `u + w` has the displayed two-block lower estimate.  The strict scalar
Schur-complement conditions then give a strict lower bound by
`gamma * ‖u + w‖²` whenever the sum is nonzero.  No completeness assumption is
used, so the result applies in particular to every real Hilbert space. -/
theorem hilbert_two_block_strict_lower_bound
    (q : H → ℝ) (beta d c gamma : ℝ) (u w : H)
    (horth : ⟪u, w⟫_ℝ = 0)
    (hlower : beta * ‖u‖ ^ 2 + d * ‖w‖ ^ 2 - 2 * c * ‖u‖ * ‖w‖ ≤ q (u + w))
    (hbeta : gamma < beta) (hd : gamma < d)
    (hdet : c ^ 2 < (beta - gamma) * (d - gamma))
    (hsum : u + w ≠ 0) :
    gamma * ‖u + w‖ ^ 2 < q (u + w) := by
  have hnorms : (‖u‖, ‖w‖) ≠ (0, 0) := by
    intro h
    have hu_norm : ‖u‖ = 0 := by
      simpa using congrArg Prod.fst h
    have hw_norm : ‖w‖ = 0 := by
      simpa using congrArg Prod.snd h
    have hu : u = 0 := norm_eq_zero.mp hu_norm
    have hw : w = 0 := norm_eq_zero.mp hw_norm
    exact hsum (by simp [hu, hw])
  have hscalar := two_by_two_strict_lower_bound beta d c gamma ‖u‖ ‖w‖
    hbeta hd hdet hnorms
  have hpyth : ‖u + w‖ ^ 2 = ‖u‖ ^ 2 + ‖w‖ ^ 2 := by
    simpa [horth] using norm_add_sq_real u w
  rw [hpyth]
  exact hscalar.trans_le hlower

end RealInnerProductSpace

/-! ### Exact scalar instances used by the unrestricted FULLINF ledgers -/

/-- The strict two-block estimate for the `p = 2` FULLINF ledger.  All
displayed decimal bounds in the analytic certificate have been rounded inward
to the exact rational coefficients used here. -/
theorem fullinf_p2_block_lower_bound (x y : ℝ) (hxy : (x, y) ≠ (0, 0)) :
    (22699 / 10 ^ 9) * (x ^ 2 + y ^ 2)
      < (227 / 10 ^ 7) * x ^ 2 + (1093 / 1000) * y ^ 2
        - 2 * (212 / 10 ^ 12) * x * y := by
  apply two_by_two_strict_lower_bound
  · norm_num
  · norm_num
  · norm_num
  · exact hxy

/-- The strict two-block estimate for the `p = 3` FULLINF ledger, with exact
rational coefficients rounded inward from its Arb certificate. -/
theorem fullinf_p3_block_lower_bound (x y : ℝ) (hxy : (x, y) ≠ (0, 0)) :
    (999 / 10 ^ 13) * (x ^ 2 + y ^ 2)
      < (1 / 10 ^ 10) * x ^ 2 + (161 / 1000) * y ^ 2
        - 2 * (721 / 10 ^ 13) * x * y := by
  apply two_by_two_strict_lower_bound
  · norm_num
  · norm_num
  · norm_num
  · exact hxy

/-- The strict two-block estimate for the certified scalar `n = 4` FULLINF ledger.
This theorem certifies only the scalar Schur-complement arithmetic; the
analytic and finite-matrix premises remain separate certificate obligations. -/
theorem fullinf_n4_block_lower_bound (x y : ℝ) (hxy : (x, y) ≠ (0, 0)) :
    (99 / 10 ^ 17) * (x ^ 2 + y ^ 2)
      < (1 / 10 ^ 15) * x ^ 2 + (289 / 1000) * y ^ 2
        - 2 * (106 / 10 ^ 11) * x * y := by
  apply two_by_two_strict_lower_bound
  · norm_num
  · norm_num
  · norm_num
  · exact hxy

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
