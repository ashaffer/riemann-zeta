/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SuzukiKernelZeroReduction

/-!
# Abstract log-elliptic zero-mode reduction

The diagonal `|t| log |t|` term gives an invertible principal operator after
an appropriate spectral shift.  Writing the full equation as `(P + R)u = 0`
then reduces it to a fixed-point equation for `-P⁻¹R`.  Ellipticity supplies
regularity and Fredholm structure, but injectivity still requires excluding
the eigenvalue one of this Birman--Schwinger operator.
-/

namespace RHP2Bridge.LogEllipticReduction

/-- Exact algebraic Birman--Schwinger reduction. -/
theorem principal_add_remainder_eq_zero_iff
    {V : Type*} [AddCommGroup V]
    (P Pinv R : V →+ V)
    (hleft : Pinv.comp P = AddMonoidHom.id V)
    (hright : P.comp Pinv = AddMonoidHom.id V)
    (u : V) :
    P u + R u = 0 ↔ u = -(Pinv (R u)) := by
  constructor
  · intro h
    have h' := congrArg Pinv h
    have hPI : Pinv (P u) = u := by
      exact congrArg (fun f : V →+ V ↦ f u) hleft
    rw [eq_neg_iff_add_eq_zero]
    simpa [map_add, hPI] using h'
  · intro h
    have hPP : P (Pinv (R u)) = R u := by
      exact congrArg (fun f : V →+ V ↦ f (R u)) hright
    have hp := congrArg P h
    rw [map_neg, hPP] at hp
    rw [hp, neg_add_cancel]

/-- A strict contraction estimate excludes a nonzero fixed point.  This is
the quantitative condition still missing for the zeta remainder. -/
theorem eq_zero_of_fixed_point_strict
    {normSq imageNormSq : ℝ}
    (hnorm : 0 ≤ normSq)
    (hstrict : imageNormSq < normSq)
    (hfixed : imageNormSq = normSq) :
    normSq = 0 := by
  exfalso
  linarith

end RHP2Bridge.LogEllipticReduction
