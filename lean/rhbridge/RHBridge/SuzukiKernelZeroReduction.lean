/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.CanonicalShiftObstruction

/-!
# Exact zero-mode reduction through Suzuki's derivative coordinate

On a finite interval the Dirichlet derivative is a bijection onto the
mean-zero space.  At generalized eigenvalue zero, Suzuki's equation
`Gₐ u = lambda Kₐ u` therefore reduces to `Gₐ u = 0`.  The theorem below
isolates the purely logical content without adding positivity assumptions.
-/

namespace RHP2Bridge.SuzukiKernelZeroReduction

/-- A bijective change of coordinates preserves existence of a nonzero
kernel vector.  Here `D` models the Dirichlet derivative and `G` the
compressed Suzuki integral operator. -/
theorem nonzero_kernel_iff_under_bijection
    {V U : Type*} [Zero V] [Zero U]
    (D : V → U) (G : U → U)
    (hD : Function.Bijective D)
    (hDzero : D 0 = 0) :
    (∃ v : V, v ≠ 0 ∧ G (D v) = 0) ↔
      ∃ u : U, u ≠ 0 ∧ G u = 0 := by
  constructor
  · rintro ⟨v, hv, hG⟩
    refine ⟨D v, ?_, hG⟩
    intro hzero
    apply hv
    exact hD.1 (hzero.trans hDzero.symm)
  · rintro ⟨u, hu, hG⟩
    obtain ⟨v, rfl⟩ := hD.2 u
    refine ⟨v, ?_, hG⟩
    intro hv
    subst v
    exact hu hDzero

/-- At generalized spectral parameter zero the comparison operator drops out
algebraically; no positivity or canonical-system uniqueness is gained. -/
theorem generalized_zero_equation_iff
    {U : Type*} [AddCommMonoid U] [Module ℝ U]
    (G K : U → U) (u : U) :
    G u = (0 : ℝ) • K u ↔ G u = 0 := by
  simp

/-- Abstract mean-removal projection.  In Suzuki's application `e` is the
constant function and `c x` is the interval average of `x`. -/
def removeMean {U : Type*} [AddCommGroup U] [Module ℝ U]
    (c : U → ℝ) (e x : U) : U :=
  x - c x • e

/-- Vanishing after mean removal says exactly that the unprojected output is
a constant vector.  Applied to `x = G u`, this turns `Gₐ u = 0` into the
constant-convolution equation on the interval. -/
theorem removeMean_eq_zero_iff
    {U : Type*} [AddCommGroup U] [Module ℝ U]
    (c : U → ℝ) (e x : U) :
    removeMean c e x = 0 ↔ x = c x • e := by
  simp [removeMean, sub_eq_zero]

end RHP2Bridge.SuzukiKernelZeroReduction
