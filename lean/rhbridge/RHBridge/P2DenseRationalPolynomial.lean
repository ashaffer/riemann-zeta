/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RationalPolynomial

/-!
# Executable dense rational polynomials for the canonical `p = 2` proof

Mathlib's `Polynomial ℚ` multiplication and composition are intentionally
noncomputable.  Generated p=2 certificates instead evaluate this low-to-high
coefficient-list representation.  `realize` is used only in proofs and shows
that every executable operation denotes the corresponding `Polynomial ℚ`.
-/

namespace RHP2Bridge

namespace DenseRatPoly

open Polynomial

/-- Coefficients in increasing degree order.  Trailing zeroes are allowed. -/
abbrev Poly := List ℚ

def zero : Poly := []

def one : Poly := [1]

def const (q : ℚ) : Poly := [q]

def X : Poly := [0, 1]

def add : Poly → Poly → Poly
  | [], q => q
  | p, [] => p
  | a :: p, b :: q => (a + b) :: add p q

def neg (p : Poly) : Poly := p.map (-·)

def sub (p q : Poly) : Poly := add p (neg q)

def scale (a : ℚ) (p : Poly) : Poly := p.map (a * ·)

def xmul (p : Poly) : Poly := 0 :: p

/-- Executable convolution, written recursively in low-degree Horner form. -/
def mul : Poly → Poly → Poly
  | [], _ => zero
  | a :: p, q => add (scale a q) (xmul (mul p q))

def pow (p : Poly) : ℕ → Poly
  | 0 => one
  | n + 1 => mul (pow p n) p

/-- Executable Horner composition. -/
def comp : Poly → Poly → Poly
  | [], _ => zero
  | a :: p, q => add (const a) (mul q (comp p q))

def affine (p : Poly) (c s : ℚ) : Poly :=
  comp p [c, s]

def shift (p : Poly) (c : ℚ) : Poly :=
  affine p c 1

def monomial : ℕ → ℚ → Poly
  | 0, q => const q
  | n + 1, q => xmul (monomial n q)

def sumRange : (N : ℕ) → (ℕ → Poly) → Poly
  | 0, _ => zero
  | N + 1, f => add (sumRange N f) (f N)

/-- Accumulate `∑ k < N, (-r)^k` together with the next power.
Keeping the power in the state avoids the quadratic recomputation caused by
calling `pow` independently at every index. -/
def geometricReciprocalState (r : Poly) : ℕ → Poly × Poly
  | 0 => (zero, one)
  | N + 1 =>
      let previous := geometricReciprocalState r N
      (add previous.1 previous.2, mul previous.2 (neg r))

def geometricReciprocal (r : Poly) (N : ℕ) : Poly :=
  (geometricReciprocalState r N).1

/-- Fully executable exact oriented integral. -/
def exactIntegral (p : Poly) (a b : ℚ) : ℚ :=
  RatPoly.exactIntegralCoeffs (fun i : Fin p.length => p.get i) a b

/-! ## Proof-only realization into `Polynomial ℚ` -/

noncomputable def realize : Poly → RatPoly.QPoly
  | [] => 0
  | a :: p => C a + Polynomial.X * realize p

@[simp] theorem realize_zero : realize zero = 0 := rfl

@[simp] theorem realize_one : realize one = 1 := by
  simp [one, realize]

@[simp] theorem realize_const (q : ℚ) : realize (const q) = C q := by
  simp [const, realize]

@[simp] theorem realize_X : realize X = Polynomial.X := by
  simp [X, realize]

theorem realize_add (p q : Poly) :
    realize (add p q) = realize p + realize q := by
  induction p generalizing q with
  | nil => simp [add, realize]
  | cons a p ih =>
      cases q with
      | nil => simp [add, realize]
      | cons b q =>
          simp only [add, realize]
          rw [ih]
          rw [Polynomial.C_add]
          ring

theorem realize_neg (p : Poly) :
    realize (neg p) = -realize p := by
  induction p with
  | nil => simp [neg, realize]
  | cons a p ih =>
      simp only [neg, List.map_cons, realize]
      change C (-a) + Polynomial.X * realize (neg p) =
        -(C a + Polynomial.X * realize p)
      rw [ih]
      rw [Polynomial.C_neg]
      ring

theorem realize_sub (p q : Poly) :
    realize (sub p q) = realize p - realize q := by
  rw [sub, realize_add, realize_neg]
  rfl

theorem realize_scale (a : ℚ) (p : Poly) :
    realize (scale a p) = C a * realize p := by
  induction p with
  | nil => simp [scale, realize]
  | cons b p ih =>
      simp only [scale, List.map_cons, realize]
      change C (a * b) + Polynomial.X * realize (scale a p) =
        C a * (C b + Polynomial.X * realize p)
      rw [ih, Polynomial.C_mul]
      ring

theorem realize_xmul (p : Poly) :
    realize (xmul p) = Polynomial.X * realize p := by
  simp [xmul, realize]

theorem realize_mul (p q : Poly) :
    realize (mul p q) = realize p * realize q := by
  induction p with
  | nil => simp [mul, realize]
  | cons a p ih =>
      rw [mul, realize_add, realize_scale, realize_xmul, ih]
      simp only [realize]
      ring

theorem realize_pow (p : Poly) (n : ℕ) :
    realize (pow p n) = realize p ^ n := by
  induction n with
  | zero => simp [pow]
  | succ n ih =>
      rw [pow, realize_mul, ih, pow_succ]

theorem realize_comp (p q : Poly) :
    realize (comp p q) = (realize p).comp (realize q) := by
  induction p with
  | nil => simp [comp, realize]
  | cons a p ih =>
      rw [comp, realize_add, realize_const, realize_mul, ih]
      simp only [realize, Polynomial.add_comp, Polynomial.C_comp,
        Polynomial.mul_comp, Polynomial.X_comp]

theorem realize_affine (p : Poly) (c s : ℚ) :
    realize (affine p c s) =
      (realize p).comp (C c + C s * Polynomial.X) := by
  rw [affine, realize_comp]
  simp [realize]

theorem realize_shift (p : Poly) (c : ℚ) :
    realize (shift p c) = RatPoly.shift (realize p) c := by
  rw [shift, realize_affine]
  simp [RatPoly.shift]

theorem realize_monomial (n : ℕ) (q : ℚ) :
    realize (monomial n q) = Polynomial.monomial n q := by
  induction n with
  | zero => simp [monomial]
  | succ n ih =>
      rw [monomial, realize_xmul, ih, Polynomial.X_mul_monomial]

theorem realize_sumRange (N : ℕ) (f : ℕ → Poly) :
    realize (sumRange N f) =
      ∑ k ∈ Finset.range N, realize (f k) := by
  induction N with
  | zero => simp [sumRange]
  | succ N ih =>
      rw [sumRange, realize_add, ih, Finset.sum_range_succ]

theorem realize_geometricReciprocal (r : Poly) (N : ℕ) :
    realize (geometricReciprocal r N) =
      ∑ k ∈ Finset.range N, (-realize r) ^ k := by
  have hstate :
      realize (geometricReciprocalState r N).1 =
          ∑ k ∈ Finset.range N, (-realize r) ^ k ∧
        realize (geometricReciprocalState r N).2 =
          (-realize r) ^ N := by
    induction N with
    | zero => simp [geometricReciprocalState]
    | succ N ih =>
        simp only [geometricReciprocalState, realize_add, realize_mul,
          realize_neg, ih.1, ih.2]
        constructor
        · rw [Finset.sum_range_succ]
        · rw [pow_succ]
  simpa [geometricReciprocal] using hstate.1

theorem coeff_realize (p : Poly) (k : ℕ) :
    (realize p).coeff k = p.getD k 0 := by
  induction p generalizing k with
  | nil => simp [realize]
  | cons a p ih =>
      cases k with
      | zero => simp [realize]
      | succ k => simp [realize, ih]

theorem realize_eq_ofCoeffs (p : Poly) :
    realize p = RatPoly.ofCoeffs (fun i => p.get i) := by
  ext k
  by_cases hk : k < p.length
  · simp [coeff_realize, RatPoly.coeff_ofCoeffs_of_lt, hk, List.getD]
  · have hge : p.length ≤ k := Nat.le_of_not_gt hk
    simp [coeff_realize, RatPoly.coeff_ofCoeffs_of_ge, hge, List.getD]

theorem cast_exactIntegral (p : Poly) (a b : ℚ) :
    (exactIntegral p a b : ℝ) =
      PolyEnclosure.exactIntegral (RatPoly.toReal (realize p))
        (a : ℝ) (b : ℝ) := by
  unfold exactIntegral
  rw [realize_eq_ofCoeffs]
  exact RatPoly.cast_exactIntegralCoeffs
    (fun i : Fin p.length => p.get i) a b

end DenseRatPoly

end RHP2Bridge
