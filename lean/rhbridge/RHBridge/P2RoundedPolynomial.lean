/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2DenseRationalPolynomial

/-!
# Outward-rounded polynomial arithmetic for canonical `p = 2` certificates

Exact rational convolution grows too expensive when repeated across all 600
matrix entries.  This module supplies an executable fixed-grid layer whose
error is computed from the coefficients actually discarded by rounding.
No theorem about nearest rounding is required: the semantic proofs consume
the exact rational difference between the raw and stored coefficients.
-/

namespace RHP2Bridge

namespace RoundedRatPoly

open DenseRatPoly

/-- A stored dense polynomial together with a uniform rational error. -/
structure Approx where
  coeffs : Poly
  error : ℚ
  deriving Repr, DecidableEq

/-- Round downward to the grid with denominator `cells + 1`.
The direction is irrelevant to soundness because the actual discarded
coefficient is included in `roundingError`. -/
def gridRound (cells : ℕ) (q : ℚ) : ℚ :=
  let d : ℚ := cells + 1
  ((Rat.floor (q * d) : ℤ) : ℚ) / d

/-- Round an error upward to a fixed denominator.  Applying this after each
operation prevents denominator growth in the error ledger. -/
def errorCeil (cells : ℕ) (q : ℚ) : ℚ :=
  let d : ℚ := cells + 1
  ((Rat.ceil (q * d) : ℤ) : ℚ) / d

theorem le_errorCeil (cells : ℕ) (q : ℚ) :
    q ≤ errorCeil cells q := by
  unfold errorCeil
  let d : ℚ := cells + 1
  have hd : 0 < d := by
    dsimp [d]
    positivity
  apply (le_div_iff₀ hd).2
  exact Rat.le_ceil

theorem errorCeil_nonneg (cells : ℕ) {q : ℚ} (hq : 0 ≤ q) :
    0 ≤ errorCeil cells q :=
  hq.trans (le_errorCeil cells q)

theorem cast_le_errorCeil (cells : ℕ) (q : ℚ) :
    (q : ℝ) ≤ (errorCeil cells q : ℝ) := by
  exact_mod_cast le_errorCeil cells q

def roundCoeffs (cells : ℕ) (p : Poly) : Poly :=
  p.map (gridRound cells)

/-- Horner absolute-value majorant on `|x| ≤ h`. -/
def absBound : Poly → ℚ → ℚ
  | [], _ => 0
  | a :: p, h => |a| + h * absBound p h

/-- A Lipschitz majorant for the represented polynomial on `[-h,h]`. -/
def lipschitzBound : Poly → ℚ → ℚ
  | [], _ => 0
  | _ :: p, h => h * lipschitzBound p h + absBound p h

/-- Uniform error caused by replacing `raw` with its rounded coefficients. -/
def roundingError (cells : ℕ) (h : ℚ) (raw : Poly) : ℚ :=
  absBound (DenseRatPoly.sub raw (roundCoeffs cells raw)) h

def rounded (cells : ℕ) (h : ℚ) (raw : Poly) : Approx :=
  ⟨roundCoeffs cells raw,
    errorCeil cells (roundingError cells h raw)⟩

/-- Embed a dense polynomial without adding approximation error.  This is
used only for the small constants at the leaves of rounded recursions. -/
def exact (p : Poly) : Approx := ⟨p, 0⟩

def add (cells : ℕ) (h : ℚ) (p q : Approx) : Approx :=
  let raw := DenseRatPoly.add p.coeffs q.coeffs
  ⟨roundCoeffs cells raw,
    errorCeil cells
      (p.error + q.error + roundingError cells h raw)⟩

def neg (cells : ℕ) (h : ℚ) (p : Approx) : Approx :=
  let raw := DenseRatPoly.neg p.coeffs
  ⟨roundCoeffs cells raw,
    errorCeil cells (p.error + roundingError cells h raw)⟩

def sub (cells : ℕ) (h : ℚ) (p q : Approx) : Approx :=
  let raw := DenseRatPoly.sub p.coeffs q.coeffs
  ⟨roundCoeffs cells raw,
    errorCeil cells
      (p.error + q.error + roundingError cells h raw)⟩

def scale (cells : ℕ) (h c : ℚ) (p : Approx) : Approx :=
  let raw := DenseRatPoly.scale c p.coeffs
  ⟨roundCoeffs cells raw,
    errorCeil cells
      (|c| * p.error + roundingError cells h raw)⟩

def mul (cells : ℕ) (h : ℚ) (p q : Approx) : Approx :=
  let raw := DenseRatPoly.mul p.coeffs q.coeffs
  ⟨roundCoeffs cells raw,
    errorCeil cells
      (p.error * q.error + p.error * absBound q.coeffs h +
        absBound p.coeffs h * q.error + roundingError cells h raw)⟩

/-- Rounded composition.  The outer approximation is consumed on the
automatically inferred domain
`absBound inner.coeffs h + inner.error`. -/
def comp (cells : ℕ) (h : ℚ) (outer inner : Approx) : Approx :=
  let H := absBound inner.coeffs h + inner.error
  let raw := DenseRatPoly.comp outer.coeffs inner.coeffs
  ⟨roundCoeffs cells raw,
    errorCeil cells
      (outer.error + lipschitzBound outer.coeffs H * inner.error +
        roundingError cells h raw)⟩

/-- Power with a rounding barrier after every multiplication. -/
def powRounded (cells : ℕ) (h : ℚ) (p : Approx) : ℕ → Approx
  | 0 => exact DenseRatPoly.one
  | n + 1 => mul cells h (powRounded cells h p n) p

/-- Finite sum with a rounding barrier after every addition. -/
def sumRangeRounded (cells : ℕ) (h : ℚ) :
    (N : ℕ) → (ℕ → Approx) → Approx
  | 0, _ => exact DenseRatPoly.zero
  | N + 1, f =>
      add cells h (sumRangeRounded cells h N f) (f N)

/-- Geometric Horner recurrence `S 0 = 0`,
`S (N+1) = 1 + factor * S N`, with a rounding barrier at each step.
The one-result recurrence avoids duplicating normalization of a recursive
pair when a generated certificate is checked by the kernel. -/
def geometricPowerSumRounded (cells : ℕ) (h : ℚ)
    (factor : Approx) : ℕ → Approx
  | 0 => exact DenseRatPoly.zero
  | N + 1 =>
      add cells h (exact DenseRatPoly.one)
        (mul cells h factor
          (geometricPowerSumRounded cells h factor N))

def geometricReciprocalRounded (cells : ℕ) (h : ℚ)
    (r : Approx) (N : ℕ) : Approx :=
  geometricPowerSumRounded cells h (neg cells h r) N

/-- Recursive Horner composition.  Unlike `comp`, this rounds after every
Horner multiplication and addition, so intermediate rational denominators
do not grow with the degree of the outer polynomial. -/
def compCoeffsRounded (cells : ℕ) (h : ℚ) (inner : Approx) :
    Poly → Approx
  | [] => exact DenseRatPoly.zero
  | a :: outer =>
      add cells h (exact (DenseRatPoly.const a))
        (mul cells h inner
          (compCoeffsRounded cells h inner outer))

/-- Compose an approximate outer function by recursive rounded Horner
evaluation and then add the outer approximation error. -/
def compRounded (cells : ℕ) (h : ℚ)
    (outer inner : Approx) : Approx :=
  let core := compCoeffsRounded cells h inner outer.coeffs
  ⟨core.coeffs, errorCeil cells (outer.error + core.error)⟩

/-! ## Real semantics -/

noncomputable def evalReal (p : Poly) (x : ℝ) : ℝ :=
  (RatPoly.toReal (DenseRatPoly.realize p)).eval x

def Encloses (h : ℚ) (f : ℝ → ℝ) (p : Approx) : Prop :=
  ∀ x : ℝ, |x| ≤ (h : ℝ) →
    |f x - evalReal p.coeffs x| ≤ (p.error : ℝ)

theorem Encloses.mono_domain
    {h H : ℚ} {f : ℝ → ℝ} {p : Approx}
    (hp : Encloses H f p) (hhH : h ≤ H) :
    Encloses h f p := by
  intro x hx
  apply hp x
  exact hx.trans (by exact_mod_cast hhH)

theorem error_nonneg_of_encloses
    {h : ℚ} (hh : 0 ≤ h) {f : ℝ → ℝ} {p : Approx}
    (hp : Encloses h f p) :
    0 ≤ p.error := by
  have hx : |(0 : ℝ)| ≤ (h : ℝ) := by
    exact_mod_cast hh
  have hp0 := hp 0 hx
  have hp0' : (0 : ℝ) ≤ (p.error : ℝ) :=
    (abs_nonneg _).trans hp0
  exact_mod_cast hp0'

@[simp] theorem evalReal_zero (x : ℝ) :
    evalReal DenseRatPoly.zero x = 0 := by
  simp [evalReal]

@[simp] theorem evalReal_const (q : ℚ) (x : ℝ) :
    evalReal (DenseRatPoly.const q) x = (q : ℝ) := by
  simp [evalReal]

@[simp] theorem evalReal_one (x : ℝ) :
    evalReal DenseRatPoly.one x = 1 := by
  simp [DenseRatPoly.one, evalReal, DenseRatPoly.realize]

theorem evalReal_add (p q : Poly) (x : ℝ) :
    evalReal (DenseRatPoly.add p q) x =
      evalReal p x + evalReal q x := by
  simp [evalReal, DenseRatPoly.realize_add]

theorem evalReal_neg (p : Poly) (x : ℝ) :
    evalReal (DenseRatPoly.neg p) x = -evalReal p x := by
  simp [evalReal, DenseRatPoly.realize_neg]

theorem evalReal_sub (p q : Poly) (x : ℝ) :
    evalReal (DenseRatPoly.sub p q) x =
      evalReal p x - evalReal q x := by
  simp [evalReal, DenseRatPoly.realize_sub]

theorem evalReal_scale (c : ℚ) (p : Poly) (x : ℝ) :
    evalReal (DenseRatPoly.scale c p) x =
      (c : ℝ) * evalReal p x := by
  simp [evalReal, DenseRatPoly.realize_scale]

theorem evalReal_mul (p q : Poly) (x : ℝ) :
    evalReal (DenseRatPoly.mul p q) x =
      evalReal p x * evalReal q x := by
  simp [evalReal, DenseRatPoly.realize_mul]

theorem evalReal_comp (p q : Poly) (x : ℝ) :
    evalReal (DenseRatPoly.comp p q) x =
      evalReal p (evalReal q x) := by
  simp [evalReal, DenseRatPoly.realize_comp,
    RatPoly.eval_toReal]

@[simp] theorem evalReal_cons (a : ℚ) (p : Poly) (x : ℝ) :
    evalReal (a :: p) x = (a : ℝ) + x * evalReal p x := by
  simp [evalReal, DenseRatPoly.realize]

theorem absBound_nonneg (p : Poly) {h : ℚ} (hh : 0 ≤ h) :
    0 ≤ absBound p h := by
  induction p with
  | nil => simp [absBound]
  | cons a p ih =>
      simp only [absBound]
      positivity

theorem abs_evalReal_le_absBound
    (p : Poly) {h : ℚ} (hh : 0 ≤ h)
    {x : ℝ} (hx : |x| ≤ (h : ℝ)) :
    |evalReal p x| ≤ (absBound p h : ℝ) := by
  induction p with
  | nil => simp [evalReal, DenseRatPoly.realize, absBound]
  | cons a p ih =>
      rw [evalReal_cons]
      rw [show ((absBound (a :: p) h : ℚ) : ℝ) =
          |(a : ℝ)| + (h : ℝ) * (absBound p h : ℝ) by
        simp [absBound]]
      calc
        |(a : ℝ) + x * evalReal p x| ≤
            |(a : ℝ)| + |x| * |evalReal p x| := by
          simpa only [abs_mul] using abs_add_le (a : ℝ) (x * evalReal p x)
        _ ≤ |(a : ℝ)| + (h : ℝ) * (absBound p h : ℝ) := by
          gcongr

theorem roundingError_nonneg
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (raw : Poly) :
    0 ≤ roundingError cells h raw :=
  absBound_nonneg _ hh

theorem abs_evalReal_sub_rounded_le
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (raw : Poly)
    {x : ℝ} (hx : |x| ≤ (h : ℝ)) :
    |evalReal raw x - evalReal (roundCoeffs cells raw) x| ≤
      (roundingError cells h raw : ℝ) := by
  rw [← evalReal_sub]
  exact abs_evalReal_le_absBound _ hh hx

theorem lipschitzBound_nonneg (p : Poly) {h : ℚ} (hh : 0 ≤ h) :
    0 ≤ lipschitzBound p h := by
  induction p with
  | nil => simp [lipschitzBound]
  | cons a p ih =>
      simp only [lipschitzBound]
      exact add_nonneg (mul_nonneg hh ih) (absBound_nonneg p hh)

theorem abs_evalReal_sub_evalReal_le_lipschitzBound
    (p : Poly) {H : ℚ} (hH : 0 ≤ H)
    {x y : ℝ} (hx : |x| ≤ (H : ℝ)) (hy : |y| ≤ (H : ℝ)) :
    |evalReal p x - evalReal p y| ≤
      (lipschitzBound p H : ℝ) * |x - y| := by
  induction p with
  | nil => simp [evalReal, DenseRatPoly.realize, lipschitzBound]
  | cons a p ih =>
      rw [evalReal_cons, evalReal_cons]
      rw [show
        ((lipschitzBound (a :: p) H : ℚ) : ℝ) =
            (H : ℝ) * (lipschitzBound p H : ℝ) +
              (absBound p H : ℝ) by
        simp [lipschitzBound]]
      rw [show
        ((a : ℝ) + x * evalReal p x) -
            ((a : ℝ) + y * evalReal p y) =
          x * (evalReal p x - evalReal p y) +
            (x - y) * evalReal p y by ring]
      calc
        |x * (evalReal p x - evalReal p y) +
            (x - y) * evalReal p y| ≤
            |x| * |evalReal p x - evalReal p y| +
              |x - y| * |evalReal p y| := by
          simpa only [abs_mul] using
            abs_add_le
              (x * (evalReal p x - evalReal p y))
              ((x - y) * evalReal p y)
        _ ≤ (H : ℝ) *
              ((lipschitzBound p H : ℝ) * |x - y|) +
            |x - y| * (absBound p H : ℝ) := by
          gcongr
          exact abs_evalReal_le_absBound p hH hy
        _ = ((H : ℝ) * (lipschitzBound p H : ℝ) +
              (absBound p H : ℝ)) * |x - y| := by ring

theorem rounded_error_nonneg
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (raw : Poly) :
    0 ≤ (rounded cells h raw).error := by
  unfold rounded
  exact errorCeil_nonneg cells (roundingError_nonneg cells hh raw)

theorem rounded_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (raw : Poly) :
    Encloses h (evalReal raw) (rounded cells h raw) := by
  intro x hx
  change
    |evalReal raw x - evalReal (roundCoeffs cells raw) x| ≤
      (errorCeil cells (roundingError cells h raw) : ℝ)
  exact (abs_evalReal_sub_rounded_le cells hh raw hx).trans
    (cast_le_errorCeil cells (roundingError cells h raw))

theorem exact_encloses (h : ℚ) (p : Poly) :
    Encloses h (evalReal p) (exact p) := by
  intro x hx
  simp [exact]

theorem exact_zero_encloses (h : ℚ) :
    Encloses h (fun _ => 0) (exact DenseRatPoly.zero) := by
  intro x hx
  simp [exact]

theorem exact_one_encloses (h : ℚ) :
    Encloses h (fun _ => 1) (exact DenseRatPoly.one) := by
  intro x hx
  simp [exact]

theorem exact_const_encloses (h : ℚ) (q : ℚ) :
    Encloses h (fun _ => (q : ℝ))
      (exact (DenseRatPoly.const q)) := by
  intro x hx
  simp [exact]

theorem add_error_nonneg
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (p q : Approx)
    (hp : 0 ≤ p.error) (hq : 0 ≤ q.error) :
    0 ≤ (add cells h p q).error := by
  unfold add
  apply errorCeil_nonneg
  exact add_nonneg (add_nonneg hp hq)
    (roundingError_nonneg cells hh _)

theorem add_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f g : ℝ → ℝ} (p q : Approx)
    (hp : Encloses h f p) (hq : Encloses h g q) :
    Encloses h (fun x => f x + g x) (add cells h p q) := by
  intro x hx
  have hpAt := hp x hx
  have hqAt := hq x hx
  have hround := abs_evalReal_sub_rounded_le cells hh
    (DenseRatPoly.add p.coeffs q.coeffs) hx
  change
    |f x + g x -
        evalReal
          (roundCoeffs cells
            (DenseRatPoly.add p.coeffs q.coeffs)) x| ≤
      (errorCeil cells
        (p.error + q.error + roundingError cells h
          (DenseRatPoly.add p.coeffs q.coeffs)) : ℝ)
  rw [show
      f x + g x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.add p.coeffs q.coeffs)) x =
        (f x - evalReal p.coeffs x) +
          (g x - evalReal q.coeffs x) +
          (evalReal (DenseRatPoly.add p.coeffs q.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.add p.coeffs q.coeffs)) x) by
    rw [evalReal_add]
    ring]
  calc
    |(f x - evalReal p.coeffs x) +
        (g x - evalReal q.coeffs x) +
        (evalReal (DenseRatPoly.add p.coeffs q.coeffs) x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.add p.coeffs q.coeffs)) x)| ≤
        |f x - evalReal p.coeffs x| +
          |g x - evalReal q.coeffs x| +
          |evalReal (DenseRatPoly.add p.coeffs q.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.add p.coeffs q.coeffs)) x| := by
      exact (abs_add_le _ _).trans
        (add_le_add (abs_add_le _ _) le_rfl)
    _ ≤ (p.error : ℝ) + q.error +
          roundingError cells h
            (DenseRatPoly.add p.coeffs q.coeffs) := by
      gcongr
    _ = ((p.error + q.error + roundingError cells h
          (DenseRatPoly.add p.coeffs q.coeffs) : ℚ) : ℝ) := by
      push_cast
      norm_num
    _ ≤ (errorCeil cells
          (p.error + q.error + roundingError cells h
            (DenseRatPoly.add p.coeffs q.coeffs)) : ℝ) :=
      cast_le_errorCeil cells _

theorem neg_error_nonneg
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (p : Approx)
    (hp : 0 ≤ p.error) :
    0 ≤ (neg cells h p).error := by
  unfold neg
  apply errorCeil_nonneg
  exact add_nonneg hp (roundingError_nonneg cells hh _)

theorem neg_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f : ℝ → ℝ} (p : Approx) (hp : Encloses h f p) :
    Encloses h (fun x => -f x) (neg cells h p) := by
  intro x hx
  have hpAt := hp x hx
  have hround := abs_evalReal_sub_rounded_le cells hh
    (DenseRatPoly.neg p.coeffs) hx
  change
    |-f x -
        evalReal (roundCoeffs cells
          (DenseRatPoly.neg p.coeffs)) x| ≤
      (errorCeil cells
        (p.error + roundingError cells h
          (DenseRatPoly.neg p.coeffs)) : ℝ)
  rw [show
      -f x - evalReal
          (roundCoeffs cells (DenseRatPoly.neg p.coeffs)) x =
        -(f x - evalReal p.coeffs x) +
          (evalReal (DenseRatPoly.neg p.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.neg p.coeffs)) x) by
    rw [evalReal_neg]
    ring]
  calc
    |-(f x - evalReal p.coeffs x) +
        (evalReal (DenseRatPoly.neg p.coeffs) x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.neg p.coeffs)) x)| ≤
        |f x - evalReal p.coeffs x| +
          |evalReal (DenseRatPoly.neg p.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.neg p.coeffs)) x| := by
      simpa only [sub_eq_add_neg, abs_neg] using abs_add_le
        (-(f x - evalReal p.coeffs x))
        (evalReal (DenseRatPoly.neg p.coeffs) x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.neg p.coeffs)) x)
    _ ≤ (p.error : ℝ) + roundingError cells h
          (DenseRatPoly.neg p.coeffs) := by
      gcongr
    _ = ((p.error + roundingError cells h
          (DenseRatPoly.neg p.coeffs) : ℚ) : ℝ) := by
      push_cast
      norm_num
    _ ≤ (errorCeil cells
          (p.error + roundingError cells h
            (DenseRatPoly.neg p.coeffs)) : ℝ) :=
      cast_le_errorCeil cells _

theorem sub_error_nonneg
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (p q : Approx)
    (hp : 0 ≤ p.error) (hq : 0 ≤ q.error) :
    0 ≤ (sub cells h p q).error := by
  unfold sub
  apply errorCeil_nonneg
  exact add_nonneg (add_nonneg hp hq)
    (roundingError_nonneg cells hh _)

theorem sub_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f g : ℝ → ℝ} (p q : Approx)
    (hp : Encloses h f p) (hq : Encloses h g q) :
    Encloses h (fun x => f x - g x) (sub cells h p q) := by
  intro x hx
  have hpAt := hp x hx
  have hqAt := hq x hx
  have hround := abs_evalReal_sub_rounded_le cells hh
    (DenseRatPoly.sub p.coeffs q.coeffs) hx
  change
    |f x - g x -
        evalReal
          (roundCoeffs cells
            (DenseRatPoly.sub p.coeffs q.coeffs)) x| ≤
      (errorCeil cells
        (p.error + q.error + roundingError cells h
          (DenseRatPoly.sub p.coeffs q.coeffs)) : ℝ)
  rw [show
      f x - g x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.sub p.coeffs q.coeffs)) x =
        (f x - evalReal p.coeffs x) -
          (g x - evalReal q.coeffs x) +
          (evalReal (DenseRatPoly.sub p.coeffs q.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.sub p.coeffs q.coeffs)) x) by
    rw [evalReal_sub]
    ring]
  calc
    |(f x - evalReal p.coeffs x) -
        (g x - evalReal q.coeffs x) +
        (evalReal (DenseRatPoly.sub p.coeffs q.coeffs) x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.sub p.coeffs q.coeffs)) x)| ≤
        |f x - evalReal p.coeffs x| +
          |g x - evalReal q.coeffs x| +
          |evalReal (DenseRatPoly.sub p.coeffs q.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.sub p.coeffs q.coeffs)) x| := by
      apply (abs_add_le _ _).trans
      apply add_le_add _ le_rfl
      have hsub :
          |(f x - evalReal p.coeffs x) -
              (g x - evalReal q.coeffs x)| ≤
            |f x - evalReal p.coeffs x| +
              |g x - evalReal q.coeffs x| := by
        rw [sub_eq_add_neg]
        simpa only [abs_neg] using abs_add_le
          (f x - evalReal p.coeffs x)
          (-(g x - evalReal q.coeffs x))
      exact hsub
    _ ≤ (p.error : ℝ) + q.error +
          roundingError cells h
            (DenseRatPoly.sub p.coeffs q.coeffs) := by
      gcongr
    _ = ((p.error + q.error + roundingError cells h
          (DenseRatPoly.sub p.coeffs q.coeffs) : ℚ) : ℝ) := by
      push_cast
      norm_num
    _ ≤ (errorCeil cells
          (p.error + q.error + roundingError cells h
            (DenseRatPoly.sub p.coeffs q.coeffs)) : ℝ) :=
      cast_le_errorCeil cells _

theorem scale_error_nonneg
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (c : ℚ) (p : Approx)
    (hp : 0 ≤ p.error) :
    0 ≤ (scale cells h c p).error := by
  unfold scale
  apply errorCeil_nonneg
  exact add_nonneg (mul_nonneg (abs_nonneg c) hp)
    (roundingError_nonneg cells hh _)

theorem scale_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (c : ℚ)
    {f : ℝ → ℝ} (p : Approx)
    (hp : Encloses h f p) :
    Encloses h (fun x => (c : ℝ) * f x) (scale cells h c p) := by
  intro x hx
  have hpAt := hp x hx
  have hround := abs_evalReal_sub_rounded_le cells hh
    (DenseRatPoly.scale c p.coeffs) hx
  change
    |(c : ℝ) * f x -
        evalReal
          (roundCoeffs cells (DenseRatPoly.scale c p.coeffs)) x| ≤
      (errorCeil cells
        (|c| * p.error + roundingError cells h
          (DenseRatPoly.scale c p.coeffs)) : ℝ)
  rw [show
      (c : ℝ) * f x -
          evalReal
            (roundCoeffs cells (DenseRatPoly.scale c p.coeffs)) x =
        (c : ℝ) * (f x - evalReal p.coeffs x) +
          (evalReal (DenseRatPoly.scale c p.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.scale c p.coeffs)) x) by
    rw [evalReal_scale]
    ring]
  calc
    |(c : ℝ) * (f x - evalReal p.coeffs x) +
        (evalReal (DenseRatPoly.scale c p.coeffs) x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.scale c p.coeffs)) x)| ≤
        |(c : ℝ)| * |f x - evalReal p.coeffs x| +
          |evalReal (DenseRatPoly.scale c p.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.scale c p.coeffs)) x| := by
      simpa only [abs_mul] using abs_add_le
        ((c : ℝ) * (f x - evalReal p.coeffs x))
        (evalReal (DenseRatPoly.scale c p.coeffs) x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.scale c p.coeffs)) x)
    _ ≤ (|c| : ℚ) * p.error +
          roundingError cells h
            (DenseRatPoly.scale c p.coeffs) := by
      push_cast
      gcongr
    _ = ((|c| * p.error +
          roundingError cells h
            (DenseRatPoly.scale c p.coeffs) : ℚ) : ℝ) := by
      push_cast
      norm_num
    _ ≤ (errorCeil cells
          (|c| * p.error + roundingError cells h
            (DenseRatPoly.scale c p.coeffs)) : ℝ) :=
      cast_le_errorCeil cells _

theorem mul_error_nonneg
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (p q : Approx)
    (hp : 0 ≤ p.error) (hq : 0 ≤ q.error) :
    0 ≤ (mul cells h p q).error := by
  unfold mul
  apply errorCeil_nonneg
  have hpBound := absBound_nonneg p.coeffs hh
  have hqBound := absBound_nonneg q.coeffs hh
  have hround := roundingError_nonneg cells hh
    (DenseRatPoly.mul p.coeffs q.coeffs)
  positivity

theorem mul_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f g : ℝ → ℝ} (p q : Approx)
    (hp : Encloses h f p) (hq : Encloses h g q) :
    Encloses h (fun x => f x * g x) (mul cells h p q) := by
  intro x hx
  have hpAt := hp x hx
  have hqAt := hq x hx
  have hpError := error_nonneg_of_encloses hh hp
  have hqError := error_nonneg_of_encloses hh hq
  have hpBound0 := absBound_nonneg p.coeffs hh
  have hqBound0 := absBound_nonneg q.coeffs hh
  have hpBound := abs_evalReal_le_absBound p.coeffs hh hx
  have hqBound := abs_evalReal_le_absBound q.coeffs hh hx
  have hround := abs_evalReal_sub_rounded_le cells hh
    (DenseRatPoly.mul p.coeffs q.coeffs) hx
  change
    |f x * g x -
        evalReal
          (roundCoeffs cells
            (DenseRatPoly.mul p.coeffs q.coeffs)) x| ≤
      (errorCeil cells
        (p.error * q.error +
          p.error * absBound q.coeffs h +
          absBound p.coeffs h * q.error +
          roundingError cells h
            (DenseRatPoly.mul p.coeffs q.coeffs)) : ℝ)
  rw [show
      f x * g x -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.mul p.coeffs q.coeffs)) x =
        (f x - evalReal p.coeffs x) *
            (g x - evalReal q.coeffs x) +
          (f x - evalReal p.coeffs x) * evalReal q.coeffs x +
          evalReal p.coeffs x * (g x - evalReal q.coeffs x) +
          (evalReal (DenseRatPoly.mul p.coeffs q.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.mul p.coeffs q.coeffs)) x) by
    rw [evalReal_mul]
    ring]
  let t₁ := (f x - evalReal p.coeffs x) *
    (g x - evalReal q.coeffs x)
  let t₂ := (f x - evalReal p.coeffs x) * evalReal q.coeffs x
  let t₃ := evalReal p.coeffs x * (g x - evalReal q.coeffs x)
  let t₄ := evalReal (DenseRatPoly.mul p.coeffs q.coeffs) x -
    evalReal
      (roundCoeffs cells (DenseRatPoly.mul p.coeffs q.coeffs)) x
  change |t₁ + t₂ + t₃ + t₄| ≤ _
  calc
    |t₁ + t₂ + t₃ + t₄| ≤
        |t₁| + |t₂| + |t₃| + |t₄| := by
      calc
        |t₁ + t₂ + t₃ + t₄| ≤ |t₁ + t₂ + t₃| + |t₄| :=
          abs_add_le _ _
        _ ≤ (|t₁ + t₂| + |t₃|) + |t₄| := by
          gcongr
          exact abs_add_le _ _
        _ ≤ (|t₁| + |t₂|) + |t₃| + |t₄| := by
          gcongr
          exact abs_add_le _ _
    _ = |f x - evalReal p.coeffs x| *
          |g x - evalReal q.coeffs x| +
        |f x - evalReal p.coeffs x| * |evalReal q.coeffs x| +
        |evalReal p.coeffs x| *
          |g x - evalReal q.coeffs x| + |t₄| := by
      simp only [t₁, t₂, t₃, abs_mul]
    _ ≤ (p.error : ℝ) * q.error +
        p.error * absBound q.coeffs h +
        absBound p.coeffs h * q.error +
        roundingError cells h
          (DenseRatPoly.mul p.coeffs q.coeffs) := by
      dsimp [t₄]
      gcongr
    _ = ((p.error * q.error +
          p.error * absBound q.coeffs h +
          absBound p.coeffs h * q.error +
          roundingError cells h
            (DenseRatPoly.mul p.coeffs q.coeffs) : ℚ) : ℝ) := by
      push_cast
      norm_num
    _ ≤ (errorCeil cells
          (p.error * q.error +
            p.error * absBound q.coeffs h +
            absBound p.coeffs h * q.error +
            roundingError cells h
              (DenseRatPoly.mul p.coeffs q.coeffs)) : ℝ) :=
      cast_le_errorCeil cells _

theorem powRounded_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f : ℝ → ℝ} (p : Approx) (hp : Encloses h f p) (n : ℕ) :
    Encloses h (fun x => f x ^ n) (powRounded cells h p n) := by
  induction n with
  | zero =>
      simpa [powRounded] using exact_one_encloses h
  | succ n ih =>
      simpa [powRounded, pow_succ] using
        mul_encloses cells hh (powRounded cells h p n) p ih hp

theorem sumRangeRounded_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f : ℕ → ℝ → ℝ} (p : ℕ → Approx)
    (hp : ∀ k, Encloses h (f k) (p k)) (N : ℕ) :
    Encloses h (fun x => ∑ k ∈ Finset.range N, f k x)
      (sumRangeRounded cells h N p) := by
  induction N with
  | zero =>
      simpa [sumRangeRounded] using exact_zero_encloses h
  | succ N ih =>
      simpa [sumRangeRounded, Finset.sum_range_succ] using
        add_encloses cells hh
          (sumRangeRounded cells h N p) (p N) ih (hp N)

theorem geometricPowerSumRounded_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f : ℝ → ℝ} (factor : Approx)
    (hFactor : Encloses h f factor) (N : ℕ) :
    Encloses h (fun x => ∑ k ∈ Finset.range N, f x ^ k)
      (geometricPowerSumRounded cells h factor N) := by
  induction N with
  | zero =>
      simpa [geometricPowerSumRounded] using exact_zero_encloses h
  | succ N ih =>
      have hProduct := mul_encloses cells hh factor
        (geometricPowerSumRounded cells h factor N) hFactor ih
      simpa [geometricPowerSumRounded, Finset.sum_range_succ',
        pow_succ', Finset.mul_sum, add_comm] using
        add_encloses cells hh (exact DenseRatPoly.one)
          (mul cells h factor
            (geometricPowerSumRounded cells h factor N))
          (exact_one_encloses h) hProduct

theorem geometricReciprocalRounded_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f : ℝ → ℝ} (r : Approx) (hr : Encloses h f r) (N : ℕ) :
    Encloses h (fun x => ∑ k ∈ Finset.range N, (-f x) ^ k)
      (geometricReciprocalRounded cells h r N) := by
  simpa [geometricReciprocalRounded] using
    geometricPowerSumRounded_encloses cells hh
      (neg cells h r) (neg_encloses cells hh r hr) N

theorem compCoeffsRounded_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {g : ℝ → ℝ} (inner : Approx) (hInner : Encloses h g inner) :
    ∀ outer : Poly,
      Encloses h (fun x => evalReal outer (g x))
        (compCoeffsRounded cells h inner outer) := by
  intro outer
  induction outer with
  | nil =>
      intro x hx
      simp [compCoeffsRounded, exact, evalReal,
        DenseRatPoly.realize]
  | cons a outer ih =>
      have hConst :
          Encloses h (fun _ => (a : ℝ))
            (exact (DenseRatPoly.const a)) := by
        exact exact_const_encloses h a
      have hProduct := mul_encloses cells hh inner
        (compCoeffsRounded cells h inner outer) hInner ih
      simpa [compCoeffsRounded, evalReal_cons] using
        add_encloses cells hh
          (exact (DenseRatPoly.const a))
          (mul cells h inner
            (compCoeffsRounded cells h inner outer))
          hConst hProduct

theorem compRounded_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f g : ℝ → ℝ} (outer inner : Approx)
    (hOuter : Encloses
      (absBound inner.coeffs h + inner.error) f outer)
    (hInner : Encloses h g inner) :
    Encloses h (fun x => f (g x))
      (compRounded cells h outer inner) := by
  intro x hx
  let H : ℚ := absBound inner.coeffs h + inner.error
  have hInnerAt := hInner x hx
  have hInnerError := error_nonneg_of_encloses hh hInner
  have hInnerBound := abs_evalReal_le_absBound inner.coeffs hh hx
  have hgBound : |g x| ≤ (H : ℝ) := by
    calc
      |g x| = |(g x - evalReal inner.coeffs x) +
          evalReal inner.coeffs x| := by ring_nf
      _ ≤ |g x - evalReal inner.coeffs x| +
          |evalReal inner.coeffs x| := abs_add_le _ _
      _ ≤ (inner.error : ℝ) +
          (absBound inner.coeffs h : ℝ) :=
        add_le_add hInnerAt hInnerBound
      _ = (H : ℝ) := by
        dsimp [H]
        push_cast
        ring
  have hOuterAt := hOuter (g x) (by simpa [H] using hgBound)
  have hCore := compCoeffsRounded_encloses cells hh inner hInner
    outer.coeffs
  have hCoreAt := hCore x hx
  change
    |f (g x) -
        evalReal
          (compCoeffsRounded cells h inner outer.coeffs).coeffs x| ≤
      (errorCeil cells
        (outer.error +
          (compCoeffsRounded cells h inner outer.coeffs).error) : ℝ)
  rw [show
      f (g x) -
          evalReal
            (compCoeffsRounded cells h inner outer.coeffs).coeffs x =
        (f (g x) - evalReal outer.coeffs (g x)) +
          (evalReal outer.coeffs (g x) -
            evalReal
              (compCoeffsRounded cells h inner outer.coeffs).coeffs x) by
    ring]
  calc
    |(f (g x) - evalReal outer.coeffs (g x)) +
        (evalReal outer.coeffs (g x) -
          evalReal
            (compCoeffsRounded cells h inner outer.coeffs).coeffs x)| ≤
        |f (g x) - evalReal outer.coeffs (g x)| +
          |evalReal outer.coeffs (g x) -
            evalReal
              (compCoeffsRounded cells h inner outer.coeffs).coeffs x| :=
      abs_add_le _ _
    _ ≤ (outer.error : ℝ) +
          (compCoeffsRounded cells h inner outer.coeffs).error :=
      add_le_add hOuterAt hCoreAt
    _ = ((outer.error +
          (compCoeffsRounded cells h inner outer.coeffs).error : ℚ) : ℝ) := by
      push_cast
      norm_num
    _ ≤ (errorCeil cells
          (outer.error +
            (compCoeffsRounded cells h inner outer.coeffs).error) : ℝ) :=
      cast_le_errorCeil cells _

theorem comp_error_nonneg
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (outer inner : Approx)
    (hOuter : 0 ≤ outer.error) (hInner : 0 ≤ inner.error) :
    0 ≤ (comp cells h outer inner).error := by
  unfold comp
  apply errorCeil_nonneg
  have hBound := absBound_nonneg inner.coeffs hh
  have hH : 0 ≤ absBound inner.coeffs h + inner.error :=
    add_nonneg hBound hInner
  have hLip := lipschitzBound_nonneg outer.coeffs hH
  have hround := roundingError_nonneg cells hh
    (DenseRatPoly.comp outer.coeffs inner.coeffs)
  positivity

theorem comp_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h)
    {f g : ℝ → ℝ} (outer inner : Approx)
    (hOuter : Encloses
      (absBound inner.coeffs h + inner.error) f outer)
    (hInner : Encloses h g inner) :
    Encloses h (fun x => f (g x)) (comp cells h outer inner) := by
  intro x hx
  let H : ℚ := absBound inner.coeffs h + inner.error
  have hInnerAt := hInner x hx
  have hInnerError := error_nonneg_of_encloses hh hInner
  have hInnerBound0 := absBound_nonneg inner.coeffs hh
  have hH : 0 ≤ H := by
    dsimp [H]
    positivity
  have hApproxBound :
      |evalReal inner.coeffs x| ≤
        (absBound inner.coeffs h : ℝ) :=
    abs_evalReal_le_absBound inner.coeffs hh hx
  have hgBound : |g x| ≤ (H : ℝ) := by
    calc
      |g x| = |(g x - evalReal inner.coeffs x) +
          evalReal inner.coeffs x| := by ring_nf
      _ ≤ |g x - evalReal inner.coeffs x| +
          |evalReal inner.coeffs x| := abs_add_le _ _
      _ ≤ (inner.error : ℝ) +
          (absBound inner.coeffs h : ℝ) :=
        add_le_add hInnerAt hApproxBound
      _ = (H : ℝ) := by
        dsimp [H]
        push_cast
        ring
  have hApproxBoundH : |evalReal inner.coeffs x| ≤ (H : ℝ) := by
    calc
      |evalReal inner.coeffs x| ≤
          (absBound inner.coeffs h : ℝ) := hApproxBound
      _ ≤ (absBound inner.coeffs h : ℝ) +
          (inner.error : ℝ) := by
        have hInnerErrorReal : (0 : ℝ) ≤ (inner.error : ℝ) := by
          exact_mod_cast hInnerError
        linarith
      _ = (H : ℝ) := by
        dsimp [H]
        push_cast
        norm_num
  have hOuterAt := hOuter (g x) (by simpa [H] using hgBound)
  have hLip := abs_evalReal_sub_evalReal_le_lipschitzBound
    outer.coeffs hH hgBound hApproxBoundH
  have hLipBound0 := lipschitzBound_nonneg outer.coeffs hH
  have hround := abs_evalReal_sub_rounded_le cells hh
    (DenseRatPoly.comp outer.coeffs inner.coeffs) hx
  change
    |f (g x) -
        evalReal
          (roundCoeffs cells
            (DenseRatPoly.comp outer.coeffs inner.coeffs)) x| ≤
      (errorCeil cells
        (outer.error +
          lipschitzBound outer.coeffs
              (absBound inner.coeffs h + inner.error) * inner.error +
          roundingError cells h
            (DenseRatPoly.comp outer.coeffs inner.coeffs)) : ℝ)
  rw [show
      f (g x) -
          evalReal
            (roundCoeffs cells
              (DenseRatPoly.comp outer.coeffs inner.coeffs)) x =
        (f (g x) - evalReal outer.coeffs (g x)) +
          (evalReal outer.coeffs (g x) -
            evalReal outer.coeffs (evalReal inner.coeffs x)) +
          (evalReal
              (DenseRatPoly.comp outer.coeffs inner.coeffs) x -
            evalReal
              (roundCoeffs cells
                (DenseRatPoly.comp outer.coeffs inner.coeffs)) x) by
    rw [evalReal_comp]
    ring]
  let t₁ := f (g x) - evalReal outer.coeffs (g x)
  let t₂ := evalReal outer.coeffs (g x) -
    evalReal outer.coeffs (evalReal inner.coeffs x)
  let t₃ := evalReal (DenseRatPoly.comp outer.coeffs inner.coeffs) x -
    evalReal
      (roundCoeffs cells
        (DenseRatPoly.comp outer.coeffs inner.coeffs)) x
  change |t₁ + t₂ + t₃| ≤ _
  calc
    |t₁ + t₂ + t₃| ≤ |t₁| + |t₂| + |t₃| := by
      exact (abs_add_le (t₁ + t₂) t₃).trans
        (add_le_add (abs_add_le t₁ t₂) le_rfl)
    _ ≤ (outer.error : ℝ) +
        (lipschitzBound outer.coeffs H : ℝ) *
          (inner.error : ℝ) +
        (roundingError cells h
          (DenseRatPoly.comp outer.coeffs inner.coeffs) : ℝ) := by
      dsimp [t₁, t₂, t₃]
      apply add_le_add
      · apply add_le_add hOuterAt
        exact hLip.trans (mul_le_mul_of_nonneg_left hInnerAt
          (by exact_mod_cast hLipBound0))
      · exact hround
    _ = ((outer.error +
          lipschitzBound outer.coeffs
              (absBound inner.coeffs h + inner.error) * inner.error +
          roundingError cells h
            (DenseRatPoly.comp outer.coeffs inner.coeffs) : ℚ) : ℝ) := by
      dsimp [H]
      push_cast
      norm_num
    _ ≤ (errorCeil cells
          (outer.error +
            lipschitzBound outer.coeffs
                (absBound inner.coeffs h + inner.error) * inner.error +
            roundingError cells h
              (DenseRatPoly.comp outer.coeffs inner.coeffs)) : ℝ) :=
      cast_le_errorCeil cells _

end RoundedRatPoly

end RHP2Bridge
