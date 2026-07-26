/-
CurveCertE5: the first fully kernel-checked END-TO-END Weil-positivity window
(function-field side), implementing spec §(d) "Integer data spec: the first
kernel-checked curve window (`CurveCert_E5`)" of
results/experts/PLAN-algebraic-geometry.md (Round 2).

Curve: E : y² = x³ + x + 1 over F₅ (genus 1).

Unlike the ζ-side artifacts (`Weilcert.lean` etc.), whose Bridge Proposition is
computer-assisted (interval arithmetic outside Lean), here the ENTIRE chain is
kernel-checked, `decide` end to end, no interval arithmetic anywhere:

  point count (`decide` over ZMod 5:  #affine E(F₅) = 8, so N₁ = 9)
    → Frobenius trace  a = q + 1 − N₁ = −3          (definition + `decide`)
    → power sums       S₀ = 2g = 2, S₁ = a, S_k = a·S_{k−1} − q·S_{k−2}
                                                     (integer recurrence; the
                                                      g = 1 Newton identity —
                                                      classical, two lines)
    → Rosati Gram matrices  G_n = [ 5^{min(i,j)}·S_{|i−j|} ]_{i,j=1..n}
                            (the un-normalized Frobenius trace form on H¹;
                             pure-ℤ replacement for T_n over ℤ[√q])
    → Theorem A  (`curve_window_positive`): every rational symmetric 2×2
      matrix entrywise within δ = 2 of G₂ has a strictly positive quadratic
      form — the rung-2 window, via `CertFramework.cert_window_positive`
      with certificate  c = 6, f = 6, W, Winv, g = (6, 306), s = 4
    → Theorem B  (`gram3_charpoly_kernel`, `gram3_psd`): G₃ is PSD and
      G₃ · (5, 3, 1)ᵀ = 0 — the kernel vector is the characteristic
      polynomial of Frobenius z² + 3z + 5 = z² − a·z + q, constant
      coefficient first: Cayley–Hamilton, kernel-checked
    → Theorem C  (`flip_witness`): the signing companion — flipping the
      sign of the degree-1 prime band (S₁ᶠ = q + 1 + N₁ = 15) makes the
      form indefinite, with the single integer witness x = (−7, 1):
      xᵀ G₂ᶠ x = −510 < 0
    → optional genus-2 block (C : y² = x⁵ + x + 1 over F₇): both point
      counts N₁ = 9 (over ZMod 7) and N₂ = 63 (over F₄₉ = F₇[w]/(w² = 3),
      2401 decidable checks) done by `decide`; G₄ ≻ 0 by certificate;
      G₅ · (49, 7, 7, 1, 1)ᵀ = 0 (char poly z⁴ + z³ + 7z² + 7z + 49).

Margin-value caveat (spec §(d), stated so nobody overclaims): Theorems A/B
certify positivity/kernel of G_n, hence the SIGN of the rung margin; the
diagonal congruence G_n = D·T_n·D does not preserve eigenvalues, so this is
not a two-sided enclosure of λ_C(L) = ln q · λ_min(T_n) itself.

Paper-side remainder of the bridge (spec §(d) B2): AG-1 Steps 2–4 (the
Parseval–Zak reduction) plus the classical g = 1 fact P_E(T) = 1 − aT + qT²
from N₁ alone; for the genus-2 block additionally the functional equation
(c₁ = q·c₃, c₀ = q²) feeding the Newton identities `newton_*` below.

Axiom base: propext, Classical.choice, Quot.sound only (audited).
-/
import Mathlib
import CertFramework

namespace CurveCertE5

open Matrix Finset

/-! ## Part 0 — the Bridge (B1): point count of E : y² = x³ + x + 1 over F₅ -/

/-- Number of affine points of `y² = x³ + x + 1` over `F₅`, as a `Finset.card`
over `ZMod 5 × ZMod 5` — computed by the Lean kernel, nothing external. -/
def affineCount : ℕ :=
  ((Finset.univ : Finset (ZMod 5 × ZMod 5)).filter
    (fun p => p.2 ^ 2 = p.1 ^ 3 + p.1 + 1)).card

/-- Kernel-checked: E has 8 affine points over F₅. -/
theorem affine_count : affineCount = 8 := by decide

/-- `N₁ = #E(F₅)`: the affine points plus the single point at infinity of the
smooth Weierstrass model. -/
def numPoints : ℕ := affineCount + 1

theorem point_count : numPoints = 9 := by decide

/-- The Frobenius trace `a = q + 1 − N₁`.  Everything below is DEFINED from
the point count through this number — the bridge is definitional. -/
def frobTrace : ℤ := 5 + 1 - (numPoints : ℤ)

theorem frobTrace_eq : frobTrace = -3 := by decide

/-- Power sums of the Frobenius eigenvalues:
`S₀ = 2g = 2`, `S₁ = a`, `S_k = a·S_{k−1} − q·S_{k−2}` (g = 1 Newton
recurrence from the characteristic polynomial `z² − a·z + q`). -/
def powSum : ℕ → ℤ
  | 0 => 2
  | 1 => frobTrace
  | (k + 2) => frobTrace * powSum (k + 1) - 5 * powSum k

/-- The integer Rosati Gram matrix `G_n = [5^{min(i,j)} · S_{|i−j|}]`
(1-based `min` in the spec = `min i.val j.val + 1` here), spec §(a)(1):
the un-normalized trace form `Tr(F^i (F^j)† | H¹)` of the Frobenius powers. -/
def gram (n : ℕ) : Matrix (Fin n) (Fin n) ℤ :=
  Matrix.of fun i j => (5 : ℤ) ^ (min i.val j.val + 1) * powSum (Nat.dist i.val j.val)

/-- Kernel-checked bridge: the rung-2 Gram matrix derived from the point
count is exactly the certificate matrix `[[10, −15], [−15, 50]]`. -/
theorem bridge_g2 : ∀ i j, gram 2 i j = !![10, -15; -15, 50] i j := by decide

/-- Kernel-checked bridge at rung 3. -/
theorem bridge_g3 : ∀ i j,
    gram 3 i j = !![10, -15, -5; -15, 50, -75; -5, -75, 250] i j := by decide

/-! ## Part 1 — Theorem A: the rung-2 window (`CertFramework` instance)

Certificate (spec §(d) Theorem A): `c = 6`, `f = 6`, `W = [[6, −15], [0, 1]]`,
`Winv = [[1, 15], [0, 6]]`, `g = (6, 306)`, `s = 4`, `δ = 2`, `scale = 1`;
`B := G₂ − 4·1 = [[6, −15], [−15, 46]]`, `36·B = Wᵀ·diag(g)·W`,
`Winv·W = 6·1`, margin `n·(scale·δ) = 4 ≤ s = 4`. -/

def wInt : Matrix (Fin 2) (Fin 2) ℤ := !![6, -15; 0, 1]

def wiInt : Matrix (Fin 2) (Fin 2) ℤ := !![1, 15; 0, 6]

def gInt : Fin 2 → ℤ := ![6, 306]

/-- `B = G₂ − s·1` with `s = 4`, over ℤ. -/
def bInt : Matrix (Fin 2) (Fin 2) ℤ :=
  Matrix.of fun i j => gram 2 i j - if i = j then 4 else 0

/-! The kernel-checked integer facts.  Note `bInt` is defined through `gram 2`,
hence through the point count: the kernel re-derives `#E(F₅)` inside each
`decide` below. -/

set_option maxHeartbeats 1000000 in
-- kernel `decide` re-derives the F₅ point count inside the congruence check
lemma key_int : ∀ i j : Fin 2,
    (6 : ℤ) ^ 2 * bInt i j = ∑ k, wInt k i * gInt k * wInt k j := by decide

set_option maxHeartbeats 1000000 in
-- kernel `decide` on the integer one-sided-inverse identity
lemma winv_int : ∀ i j : Fin 2,
    (∑ k, wiInt i k * wInt k j) = if i = j then (6 : ℤ) else 0 := by decide

lemma g_pos : ∀ k, 0 < gInt k := by decide

/-! Casts to ℚ (house pattern of `Weilcert.lean`). -/

def gram2Q : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of fun i j => ((gram 2 i j : ℤ) : ℚ)

def bQ : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of fun i j => ((bInt i j : ℤ) : ℚ)

def wQ : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of fun i j => ((wInt i j : ℤ) : ℚ)

def wiQ : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of fun i j => ((wiInt i j : ℤ) : ℚ)

def gQ : Fin 2 → ℚ := fun k => ((gInt k : ℤ) : ℚ)

lemma key_q (i j : Fin 2) :
    (6 : ℚ) ^ 2 * bQ i j = ∑ k, wQ k i * gQ k * wQ k j := by
  have h := key_int i j
  have h2 : (((6 : ℤ) ^ 2 * bInt i j : ℤ) : ℚ)
      = ((∑ k, wInt k i * gInt k * wInt k j : ℤ) : ℚ) := by exact_mod_cast h
  push_cast at h2
  rw [show ((6 : ℚ) ^ 2) = 36 by norm_num]
  simpa [bQ, wQ, gQ, Matrix.of_apply] using h2

lemma winv_q (i j : Fin 2) :
    (∑ k, wiQ i k * wQ k j) = if i = j then (6 : ℚ) else 0 := by
  have h := winv_int i j
  by_cases hij : i = j
  · subst hij
    simp only [↓reduceIte] at h ⊢
    have : ((∑ k, wiInt i k * wInt k i : ℤ) : ℚ) = (((6 : ℤ)) : ℚ) := by
      exact_mod_cast h
    push_cast at this
    simpa [wiQ, wQ, Matrix.of_apply] using this
  · simp only [if_neg hij] at h ⊢
    have : ((∑ k, wiInt i k * wInt k j : ℤ) : ℚ) = ((0 : ℤ) : ℚ) := by
      exact_mod_cast h
    push_cast at this
    simpa [wiQ, wQ, Matrix.of_apply] using this

lemma bq_eq (i j : Fin 2) :
    bQ i j = gram2Q i j - if i = j then (4 : ℚ) else 0 := by
  by_cases hij : i = j
  · subst hij
    simp only [bQ, bInt, gram2Q, Matrix.of_apply]
    push_cast
    ring
  · simp only [bQ, bInt, gram2Q, Matrix.of_apply, if_neg hij]
    push_cast
    ring

/-- **Theorem A (the rung-2 curve window; END-TO-END kernel-checked).**
Every rational 2×2 matrix `M` entrywise within `2` of the Rosati Gram matrix
`G₂` of `E : y² = x³ + x + 1 / F₅` — with `G₂` DEFINED inside Lean from the
kernel-computed point count `#E(F₅) = 9` — has a strictly positive quadratic
form.  Instance of `CertFramework.cert_window_positive` with `n = 2`,
`scale = 1`, `δ = 2`, `s = 4`. -/
theorem curve_window_positive (M : Matrix (Fin 2) (Fin 2) ℚ)
    (hM : ∀ i j, |M i j - gram2Q i j| ≤ 2)
    (x : Fin 2 → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ M *ᵥ x := by
  refine CertFramework.cert_window_positive gram2Q wQ wiQ gQ 6 6 4 1 2 ?_ winv_q
    (fun k => by unfold gQ; exact_mod_cast g_pos k) (by norm_num) (by norm_num)
    (by norm_num) (by norm_num) (by norm_num) M ?_ hx
  · intro i j
    rw [← bq_eq]
    exact key_q i j
  · intro i j
    rw [div_one]
    exact hM i j

/-- The midpoint itself: `G₂ ≻ 0` (over ℚ, hence over ℝ by density). -/
theorem gram2_positive (x : Fin 2 → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ gram2Q *ᵥ x := by
  refine curve_window_positive gram2Q (fun i j => ?_) x hx
  simp only [sub_self, abs_zero]
  norm_num

/-! ## Part 2 — Theorem B: rung 3, Cayley–Hamilton kernel + PSD

The wall (spec AG-1 Step 6): `G₃` has rank 2; its kernel vector is the
characteristic polynomial of Frobenius `z² + 3z + 5 = z² − a·z + q`, constant
coefficient first — `(q, −a, 1) = (5, 3, 1)`. -/

/-- The characteristic polynomial of Frobenius as a coefficient vector,
constant coefficient first, DEFINED from the point count: `(q, −a, 1)`. -/
def frobCharPoly : Fin 3 → ℤ := ![5, -frobTrace, 1]

theorem frobCharPoly_eq : ∀ i, frobCharPoly i = ![5, 3, 1] i := by decide

/-- **Theorem B(i) (Cayley–Hamilton, kernel-checked):**
`G₃ · (q, −a, 1)ᵀ = 0` — the zeta function of `E` is the kernel of the
rung-3 Rosati form. -/
theorem gram3_charpoly_kernel : ∀ i, (gram 3 *ᵥ frobCharPoly) i = 0 := by decide

/-! PSD certificate for `G₃` (the `g ≥ 0` variant of `quad_of_ldl`): exact
rational LDLᵀ has pivots `(10, 55/2, 0)` (third pivot 0 = the wall); cleared
to integers with `c = 2`, row scalings `r = (2, 1, 1)`:
`4·G₃ = W₃ᵀ·diag(10, 110, 0)·W₃`. -/

def w3Int : Matrix (Fin 3) (Fin 3) ℤ := !![2, -3, -1; 0, 1, -3; 0, 0, 1]

def g3Int : Fin 3 → ℤ := ![10, 110, 0]

set_option maxHeartbeats 1000000 in
-- kernel `decide` re-derives the F₅ point count inside the rung-3 congruence
lemma key3_int : ∀ i j : Fin 3,
    (2 : ℤ) ^ 2 * gram 3 i j = ∑ k, w3Int k i * g3Int k * w3Int k j := by decide

lemma g3_nonneg : ∀ k, 0 ≤ g3Int k := by decide

def gram3Q : Matrix (Fin 3) (Fin 3) ℚ := Matrix.of fun i j => ((gram 3 i j : ℤ) : ℚ)

def w3Q : Matrix (Fin 3) (Fin 3) ℚ := Matrix.of fun i j => ((w3Int i j : ℤ) : ℚ)

def g3Q : Fin 3 → ℚ := fun k => ((g3Int k : ℤ) : ℚ)

lemma key3_q (i j : Fin 3) :
    (2 : ℚ) ^ 2 * gram3Q i j = ∑ k, w3Q k i * g3Q k * w3Q k j := by
  have h := key3_int i j
  have h2 : (((2 : ℤ) ^ 2 * gram 3 i j : ℤ) : ℚ)
      = ((∑ k, w3Int k i * g3Int k * w3Int k j : ℤ) : ℚ) := by exact_mod_cast h
  push_cast at h2
  rw [show ((2 : ℚ) ^ 2) = 4 by norm_num]
  simpa [gram3Q, w3Q, g3Q, Matrix.of_apply] using h2

/-- **Theorem B(ii) (rung-3 positive semidefiniteness):** `0 ≤ xᵀ G₃ x` for
all rational `x`.  With `gram3_charpoly_kernel`: the rung-3 form is PSD and
its kernel is the zeta function of `E` — the exact, formally verified
statement of which the repo's keyhole (§2.13/Groskin) is the ℚ-shadow. -/
theorem gram3_psd (x : Fin 3 → ℚ) : 0 ≤ x ⬝ᵥ gram3Q *ᵥ x := by
  have hkey' : ∀ i j, (((2 : ℚ) ^ 2) • gram3Q) i j
      = ∑ k, w3Qᵀ i k * g3Q k * w3Qᵀ j k := by
    intro i j
    simp only [Matrix.smul_apply, smul_eq_mul, Matrix.transpose_apply]
    exact key3_q i j
  have hquad := CertFramework.quad_of_ldl (((2 : ℚ) ^ 2) • gram3Q) w3Qᵀ g3Q hkey' x
  have hsmul : x ⬝ᵥ (((2 : ℚ) ^ 2) • gram3Q) *ᵥ x
      = (2 : ℚ) ^ 2 * (x ⬝ᵥ gram3Q *ᵥ x) := by
    rw [smul_mulVec, dotProduct_smul, smul_eq_mul]
  rw [hsmul] at hquad
  have hnn : 0 ≤ ∑ k, g3Q k * (∑ i, x i * w3Qᵀ i k) ^ 2 := by
    refine Finset.sum_nonneg fun k _ => mul_nonneg ?_ (sq_nonneg _)
    unfold g3Q
    exact_mod_cast g3_nonneg k
  linarith [hquad, hnn]

/-! ## Part 3 — Theorem C: the signing witness (C5 format)

Flipping the sign of the degree-1 prime band replaces `S₁ = q + 1 − N₁` by
`S₁ᶠ = q + 1 + N₁ = 15`; the flipped Gram matrix is indefinite, certified by
ONE integer vector. -/

/-- The sign-flipped degree-1 band: `S₁ᶠ = q + 1 + N₁`, defined from the
point count. -/
def flipTrace : ℤ := 5 + 1 + (numPoints : ℤ)

/-- The flipped rung-2 Gram matrix `[[10, 75], [75, 50]]`
(`5·S₁ᶠ = 75` off the diagonal, diagonal unchanged). -/
def gram2Flip : Matrix (Fin 2) (Fin 2) ℤ :=
  Matrix.of fun i j =>
    (5 : ℤ) ^ (min i.val j.val + 1) * (if i = j then 2 else flipTrace)

theorem bridge_flip : ∀ i j, gram2Flip i j = !![10, 75; 75, 50] i j := by decide

/-- **Theorem C (signing witness, kernel-checked):** the wrong signing fails
against an integer witness: `(−7, 1)ᵀ G₂ᶠ (−7, 1) = −510 < 0`.  The curve
transplant of GT-G4(A); one `decide`-checked vector per signing. -/
theorem flip_witness :
    (![(-7 : ℤ), 1]) ⬝ᵥ gram2Flip *ᵥ ![(-7 : ℤ), 1] = -510 := by decide

theorem flip_not_positive : ∃ x : Fin 2 → ℤ, x ⬝ᵥ gram2Flip *ᵥ x < 0 :=
  ⟨![(-7 : ℤ), 1], by decide⟩

/-! ## Part 4 — optional genus-2 block: C : y² = x⁵ + x + 1 over F₇

Both point counts are kernel-checked: `N₁` over `ZMod 7`, and `N₂` over
`F₄₉ = F₇[w]/(w² = 3)` (3 is a non-residue mod 7) realized as pairs
`(a, b) = a + b·w` in `ZMod 7 × ZMod 7` with explicit multiplication —
2401 decidable checks, all by the kernel. -/

/-- Affine count of `y² = x⁵ + x + 1` over `F₇`. -/
def affineCount7 : ℕ :=
  ((Finset.univ : Finset (ZMod 7 × ZMod 7)).filter
    (fun p => p.2 ^ 2 = p.1 ^ 5 + p.1 + 1)).card

theorem affine_count7 : affineCount7 = 8 := by decide

/-- `N₁ = #C(F₇) = 9`: one point at infinity on the smooth model of the odd-
degree hyperelliptic curve. -/
def numPoints7 : ℕ := affineCount7 + 1

/-- Multiplication in `F₄₉ = F₇[w]/(w² = 3)` on pairs `(a, b) = a + b·w`. -/
def mul49 (u v : ZMod 7 × ZMod 7) : ZMod 7 × ZMod 7 :=
  (u.1 * v.1 + 3 * u.2 * v.2, u.1 * v.2 + u.2 * v.1)

/-- Fifth power in `F₄₉`. -/
def x5pow (u : ZMod 7 × ZMod 7) : ZMod 7 × ZMod 7 :=
  mul49 u (mul49 u (mul49 u (mul49 u u)))

/-- Affine count of `y² = x⁵ + x + 1` over `F₄₉` (2401 checks). -/
def affineCount49 : ℕ :=
  ((Finset.univ : Finset ((ZMod 7 × ZMod 7) × (ZMod 7 × ZMod 7))).filter
    (fun p => mul49 p.2 p.2 = x5pow p.1 + p.1 + ((1 : ZMod 7), (0 : ZMod 7)))).card

set_option maxHeartbeats 8000000 in
-- 2401-element kernel point count over F₄₉
theorem affine_count49 : affineCount49 = 62 := by decide

/-- `N₂ = #C(F₄₉) = 63`. -/
def numPoints49 : ℕ := affineCount49 + 1

/-- Power sums of Frobenius for `C/F₇` (`2g = 4`): `S₁ = q + 1 − N₁` is
definitional in the count; `S₂ = −13`, `S₃ = −1`, `S₄ = −97` are literals
certified against the counts and the Newton identities by the kernel-checked
`bridge_s2` / `newton_s3` / `newton_s4` below (the F₄₉ count is expensive, so
it is bridged once rather than re-derived inside every later `decide`);
higher power sums by the degree-4 linear recurrence of the characteristic
polynomial `z⁴ + z³ + 7z² + 7z + 49`. -/
def powSum7 : ℕ → ℤ
  | 0 => 4
  | 1 => 8 - (numPoints7 : ℤ)
  | 2 => -13
  | 3 => -1
  | 4 => -97
  | (k + 5) => -(powSum7 (k + 4) + 7 * powSum7 (k + 3)
      + 7 * powSum7 (k + 2) + 49 * powSum7 (k + 1))

set_option maxHeartbeats 8000000 in
-- re-evaluates the 2401-element F₄₉ point count inside the kernel
/-- Kernel-checked bridge: `S₂ = q² + 1 − N₂` with `N₂` the F₄₉ point count. -/
theorem bridge_s2 : powSum7 2 = 7 ^ 2 + 1 - (numPoints49 : ℤ) := by decide

/-- Newton: `c₂ = (S₁² − S₂)/2 = 7` — the `z²` coefficient of the char poly. -/
theorem newton_c2 : (2 : ℤ) * 7 = powSum7 1 ^ 2 - powSum7 2 := by decide

/-- Newton identity for `S₃` (with `b = −S₁` the `z³` coefficient and the
functional-equation coefficient `c₁ = q·b` — classical input, spec B2). -/
theorem newton_s3 : powSum7 3
    = -((-powSum7 1) * powSum7 2 + 7 * powSum7 1 + 3 * (7 * (-powSum7 1))) := by
  decide

/-- Newton identity for `S₄` (with `c₀ = q²` from the functional equation). -/
theorem newton_s4 : powSum7 4
    = -((-powSum7 1) * powSum7 3 + 7 * powSum7 2
        + (7 * (-powSum7 1)) * powSum7 1 + 4 * 49) := by decide

/-- The genus-2 Rosati Gram matrix `G_n = [7^{min(i,j)} · S_{|i−j|}]`. -/
def gram7 (n : ℕ) : Matrix (Fin n) (Fin n) ℤ :=
  Matrix.of fun i j => (7 : ℤ) ^ (min i.val j.val + 1) * powSum7 (Nat.dist i.val j.val)

theorem bridge_g4 : ∀ i j, gram7 4 i j
    = !![28, -7, -91, -7; -7, 196, -49, -637;
         -91, -49, 1372, -343; -7, -637, -343, 9604] i j := by decide

/-! Positivity certificate for `G₄` from `lean/make_certificate.py`'s exact
fraction-free routine run on `G₄`: `c = f = 18204`,
`c²·G₄ = W₄ᵀ·diag(g₄)·W₄`, `Winv₄·W₄ = f·1`, `g₄ > 0`. -/

def w4Int : Matrix (Fin 4) (Fin 4) ℤ :=
  !![4, -1, -13, -1; 0, 111, -41, -365; 0, 0, 82, -47; 0, 0, 0, 1]

def wi4Int : Matrix (Fin 4) (Fin 4) ℤ :=
  !![4551, 41, 742, 54390; 0, 164, 82, 63714; 0, 0, 222, 10434; 0, 0, 0, 18204]

def g4Int : Fin 4 → ℤ := ![579924828, 5224548, 51735768, 2371722812424]

set_option maxHeartbeats 4000000 in
-- 16-entry congruence with 13-digit certificate integers, all in the kernel
lemma key4_int : ∀ i j : Fin 4,
    (18204 : ℤ) ^ 2 * gram7 4 i j = ∑ k, w4Int k i * g4Int k * w4Int k j := by
  decide

set_option maxHeartbeats 4000000 in
-- kernel `decide` on the genus-2 one-sided-inverse identity
lemma winv4_int : ∀ i j : Fin 4,
    (∑ k, wi4Int i k * w4Int k j) = if i = j then (18204 : ℤ) else 0 := by decide

lemma g4_pos : ∀ k, 0 < g4Int k := by decide

def gram4Q : Matrix (Fin 4) (Fin 4) ℚ := Matrix.of fun i j => ((gram7 4 i j : ℤ) : ℚ)

def w4Q : Matrix (Fin 4) (Fin 4) ℚ := Matrix.of fun i j => ((w4Int i j : ℤ) : ℚ)

def wi4Q : Matrix (Fin 4) (Fin 4) ℚ := Matrix.of fun i j => ((wi4Int i j : ℤ) : ℚ)

def g4Q : Fin 4 → ℚ := fun k => ((g4Int k : ℤ) : ℚ)

lemma key4_q (i j : Fin 4) :
    (18204 : ℚ) ^ 2 * gram4Q i j = ∑ k, w4Q k i * g4Q k * w4Q k j := by
  have h := key4_int i j
  have h2 : (((18204 : ℤ) ^ 2 * gram7 4 i j : ℤ) : ℚ)
      = ((∑ k, w4Int k i * g4Int k * w4Int k j : ℤ) : ℚ) := by exact_mod_cast h
  push_cast at h2
  rw [show ((18204 : ℚ) ^ 2) = 331385616 by norm_num]
  simpa [gram4Q, w4Q, g4Q, Matrix.of_apply] using h2

lemma winv4_q (i j : Fin 4) :
    (∑ k, wi4Q i k * w4Q k j) = if i = j then (18204 : ℚ) else 0 := by
  have h := winv4_int i j
  by_cases hij : i = j
  · subst hij
    simp only [↓reduceIte] at h ⊢
    have : ((∑ k, wi4Int i k * w4Int k i : ℤ) : ℚ) = (((18204 : ℤ)) : ℚ) := by
      exact_mod_cast h
    push_cast at this
    simpa [wi4Q, w4Q, Matrix.of_apply] using this
  · simp only [if_neg hij] at h ⊢
    have : ((∑ k, wi4Int i k * w4Int k j : ℤ) : ℚ) = ((0 : ℤ) : ℚ) := by
      exact_mod_cast h
    push_cast at this
    simpa [wi4Q, w4Q, Matrix.of_apply] using this

/-- **Genus-2 rung-4 positivity:** `G₄ ≻ 0` for `C : y² = x⁵ + x + 1 / F₇` —
the rung where both counted primes (degrees 1 and 2) participate. -/
theorem gram4_positive (x : Fin 4 → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ gram4Q *ᵥ x :=
  CertFramework.ldl_quad_pos gram4Q w4Q wi4Q g4Q 18204 18204 key4_q winv4_q
    (fun k => by unfold g4Q; exact_mod_cast g4_pos k) (by norm_num) (by norm_num)
    hx

/-- The genus-2 characteristic polynomial of Frobenius as a coefficient
vector, constant first: `z⁴ + z³ + 7z² + 7z + 49 ↦ (49, 7, 7, 1, 1)`. -/
def frobCharPoly7 : Fin 5 → ℤ := ![49, 7, 7, 1, 1]

/-- **Genus-2 Cayley–Hamilton, kernel-checked:** `G₅ · (49, 7, 7, 1, 1)ᵀ = 0`. -/
theorem gram5_charpoly_kernel : ∀ i, (gram7 5 *ᵥ frobCharPoly7) i = 0 := by decide

end CurveCertE5
