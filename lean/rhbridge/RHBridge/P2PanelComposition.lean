/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2DefectApprox
import RHBridge.P2DigammaPrefix
import RHBridge.P2ComponentBounds
import RHBridge.P2ScaleCenters
import RHBridge.PolyEnclosure

/-!
# Canonical p=2 centered-panel composition

This module connects the rationalized symbol defect and degree-100 spherical
models to the generic centered-panel enclosure algebra.  Its core product
theorems accept arbitrary local polynomial witnesses and bounds, so generated
tables need not reduce the large global polynomial definitions.  Optional
adapters construct the canonical witnesses from a rational scale center.
-/

namespace RHP2Bridge

open Polynomial
open scoped BigOperators

noncomputable def p2DefectPanelPolynomial (c : ℝ) (M : ℕ) : ℝ[X] :=
  quarterDifferenceFinitePrefixPolynomial c M +
    PolyEnclosure.shiftPolynomial p2RationalNonPrefixPoly c

noncomputable def p2DefectPanelError (c h : ℝ) (M : ℕ) : ℝ :=
  quarterDifferenceFinitePrefixError c h M + 2 / 10 ^ 14

theorem p2RationalDefectApprox_centeredEncloses
    (c h : ℝ) (M : ℕ) (hh : 0 ≤ h)
    (hrho : prefixDenominatorRho 0 c h < 1) :
    PolyEnclosure.CenteredEncloses c h p2RationalDefectApprox
      (p2DefectPanelPolynomial c M)
      (quarterDifferenceFinitePrefixError c h M) := by
  have hp := quarterDifferenceFinitePrefix_centeredEncloses_of_rho_zero
    c h M hh hrho
  intro x hx
  unfold p2DefectPanelPolynomial
  rw [Polynomial.eval_add, PolyEnclosure.eval_shiftPolynomial]
  rw [p2RationalDefectApprox_eq_prefix_add_polynomial]
  rw [add_sub_add_right_eq_sub]
  simpa [quarterDifferenceFinitePrefix] using hp x hx

theorem p2Defect_centeredEncloses
    (c h : ℝ) (M : ℕ) (hh : 0 ≤ h)
    (hband : |c| + h ≤ 50)
    (hrho : prefixDenominatorRho 0 c h < 1) :
    PolyEnclosure.CenteredEncloses c h
      (fun r ↦ GlideKernel.p2Omega r - GlideKernel.p2Alpha)
      (p2DefectPanelPolynomial c M) (p2DefectPanelError c h M) := by
  have hrat := p2RationalDefectApprox_centeredEncloses c h M hh hrho
  intro x hx
  have hr : |c + x| ≤ 50 := by
    calc
      |c + x| ≤ |c| + |x| := abs_add_le c x
      _ ≤ |c| + h := by gcongr
      _ ≤ 50 := hband
  have hana := abs_p2Omega_sub_alpha_sub_rationalDefectApprox_lt hr
  calc
    |(GlideKernel.p2Omega (c + x) - GlideKernel.p2Alpha) -
        (p2DefectPanelPolynomial c M).eval x| ≤
      |(GlideKernel.p2Omega (c + x) - GlideKernel.p2Alpha) -
          p2RationalDefectApprox (c + x)| +
        |p2RationalDefectApprox (c + x) -
          (p2DefectPanelPolynomial c M).eval x| := abs_sub_le _ _ _
    _ ≤ 2 / 10 ^ 14 + quarterDifferenceFinitePrefixError c h M :=
      add_le_add hana.le (hrat x hx)
    _ = p2DefectPanelError c h M := by
      unfold p2DefectPanelError
      ring

theorem p2DefectPanelError_nonneg
    (c h : ℝ) (M : ℕ) (hh : 0 ≤ h)
    (hband : |c| + h ≤ 50)
    (hrho : prefixDenominatorRho 0 c h < 1) :
    0 ≤ p2DefectPanelError c h M := by
  have he := p2Defect_centeredEncloses c h M hh hband hrho
    0 (by simpa using hh)
  exact (abs_nonneg _).trans he

theorem p2DefectPanelPolynomial_polyBound
    (c h : ℝ) (M : ℕ) (hh : 0 ≤ h)
    (hband : |c| + h ≤ 50)
    (hrho : prefixDenominatorRho 0 c h < 1) :
    PolyEnclosure.PolyBound h (p2DefectPanelPolynomial c M)
      (7447 / 1000 + p2DefectPanelError c h M) := by
  have he := p2Defect_centeredEncloses c h M hh hband hrho
  apply he.polyBound_of_functionBound
  intro y hy
  apply GlideKernel.p2Omega_sub_alpha_abs_le
  calc
    |y| = |c + (y - c)| := by ring_nf
    _ ≤ |c| + |y - c| := abs_add_le _ _
    _ ≤ |c| + h := by gcongr
    _ ≤ 50 := hband

noncomputable def p2Spherical100PanelPolynomial (n : ℕ) (c : ℝ) : ℝ[X] :=
  PolyEnclosure.shiftPolynomial (p2SphericalRealPolynomial n 100) c

noncomputable def p2Spherical100Error : ℝ := 1 / 10 ^ 19

theorem p2SphericalReal100_centeredEncloses
    (n : Fin 48) (c h : ℝ) (hband : |c| + h ≤ 50) :
    PolyEnclosure.CenteredEncloses c h (p2SphericalReal n.val)
      (p2Spherical100PanelPolynomial n.val c) p2Spherical100Error := by
  intro x hx
  have hr : |c + x| ≤ 50 := by
    calc
      |c + x| ≤ |c| + |x| := abs_add_le c x
      _ ≤ |c| + h := by gcongr
      _ ≤ 50 := hband
  unfold p2Spherical100PanelPolynomial p2Spherical100Error
  rw [PolyEnclosure.eval_shiftPolynomial]
  exact (abs_p2SphericalReal_sub_polynomial100_lt_1e19 n hr).le

theorem abs_p2LegendreSphericalScale_sub_rat_le_of_sq_bounds
    (n : ℕ) (q ε : ℚ)
    (hε : 0 ≤ ε) (hlower0 : 0 ≤ q - ε)
    (hlower : (((q - ε : ℚ) : ℝ) ^ 2) ≤
      7 * (2 * (n : ℝ) + 1) / 8)
    (hupper : 7 * (2 * (n : ℝ) + 1) / 8 ≤
      (((q + ε : ℚ) : ℝ) ^ 2)) :
    |p2LegendreSphericalScale n - (q : ℝ)| ≤ (ε : ℝ) := by
  have hs0 := p2LegendreSphericalScale_nonneg n
  have hlow0r : (0 : ℝ) ≤ ((q - ε : ℚ) : ℝ) := by exact_mod_cast hlower0
  have hupp0r : (0 : ℝ) ≤ ((q + ε : ℚ) : ℝ) := by
    exact_mod_cast (show (0 : ℚ) ≤ q + ε by linarith)
  have hlow : ((q - ε : ℚ) : ℝ) ≤ p2LegendreSphericalScale n := by
    apply (sq_le_sq₀ hlow0r hs0).mp
    rw [p2LegendreSphericalScale_sq]
    exact hlower
  have hupp : p2LegendreSphericalScale n ≤ ((q + ε : ℚ) : ℝ) := by
    apply (sq_le_sq₀ hs0 hupp0r).mp
    rw [p2LegendreSphericalScale_sq]
    exact hupper
  rw [abs_le]
  push_cast at hlow hupp
  constructor <;> linarith

inductive P2SelectedKind
  | even
  | odd
  deriving DecidableEq

def p2SelectedDegree : P2SelectedKind → ℕ → ℕ
  | .even, k => 2 * k
  | .odd, k => 2 * k + 1

noncomputable def p2SelectedComponent
    (kind : P2SelectedKind) (k : ℕ) (r : ℝ) : ℝ :=
  match kind with
  | .even => (p2LegendreCoeff (2 * k) r).re
  | .odd => (p2LegendreCoeff (2 * k + 1) r).im

noncomputable def p2SelectedPhase
    (kind : P2SelectedKind) (k : ℕ) : ℝ :=
  match kind with
  | .even => (-1 : ℝ) ^ k
  | .odd => -((-1 : ℝ) ^ k)

theorem p2SelectedComponent_eq_spherical
    (kind : P2SelectedKind) (k : ℕ) (r : ℝ) :
    p2SelectedComponent kind k r =
      p2SelectedPhase kind k *
        p2LegendreSphericalScale (p2SelectedDegree kind k) *
        p2SphericalReal (p2SelectedDegree kind k) r := by
  cases kind with
  | even =>
      simp only [p2SelectedComponent, p2SelectedPhase, p2SelectedDegree]
      rw [p2LegendreCoeff_even_re_eq]
      unfold p2LegendreSphericalScale
      push_cast
      ring_nf
  | odd =>
      simp only [p2SelectedComponent, p2SelectedPhase, p2SelectedDegree]
      rw [p2LegendreCoeff_odd_im_eq]
      unfold p2LegendreSphericalScale
      push_cast
      ring_nf

theorem abs_p2SelectedComponent_le_one
    (kind : P2SelectedKind) (k : ℕ) (r : ℝ) :
    |p2SelectedComponent kind k r| ≤ 1 := by
  cases kind with
  | even => exact abs_p2LegendreCoeff_re_le_one (2 * k) r
  | odd => exact abs_p2LegendreCoeff_im_le_one (2 * k + 1) r

@[simp] theorem abs_p2SelectedPhase
    (kind : P2SelectedKind) (k : ℕ) :
    |p2SelectedPhase kind k| = 1 := by
  cases kind <;> simp [p2SelectedPhase, abs_pow]

noncomputable def p2SelectedSphericalPanelPolynomial
    (kind : P2SelectedKind) (k : ℕ) (q : ℝ) (ps : ℝ[X]) : ℝ[X] :=
  C (p2SelectedPhase kind k) * (C q * ps)

noncomputable def p2SelectedSphericalPanelError
    (q ε es Bs : ℝ) : ℝ :=
  ε * es + ε * Bs + |q| * es

/-- Turn any local spherical-real witness into a witness for the actual
selected Fourier component.  The scale center and radius are rationals;
`hscale` may be produced by
`abs_p2LegendreSphericalScale_sub_rat_le_of_sq_bounds`. -/
theorem p2SelectedComponent_centeredEncloses_of_spherical
    {c h es Bs : ℝ} {ps : ℝ[X]}
    (kind : P2SelectedKind) (k : ℕ) (q ε : ℝ)
    (hscale : |p2LegendreSphericalScale (p2SelectedDegree kind k) -
      q| ≤ ε)
    (hsphere : PolyEnclosure.CenteredEncloses c h
      (p2SphericalReal (p2SelectedDegree kind k)) ps es)
    (hps : PolyEnclosure.PolyBound h ps Bs)
    (hε : 0 ≤ ε) :
    PolyEnclosure.CenteredEncloses c h (p2SelectedComponent kind k)
      (p2SelectedSphericalPanelPolynomial kind k q ps)
      (p2SelectedSphericalPanelError q ε es Bs) := by
  have hscaleEncl : PolyEnclosure.CenteredEncloses c h
      (fun _ ↦ p2LegendreSphericalScale (p2SelectedDegree kind k))
      (C q) ε := by
    intro x hx
    simpa using hscale
  have hq : PolyEnclosure.PolyBound h (C q) |q| := by
    intro x hx
    simp
  have hmul := hscaleEncl.mul hsphere hq hps hε (abs_nonneg q)
  have hphase := hmul.const_mul (p2SelectedPhase kind k)
  intro x hx
  have h := hphase x hx
  rw [p2SelectedComponent_eq_spherical]
  simpa [p2SelectedSphericalPanelPolynomial,
    p2SelectedSphericalPanelError, abs_p2SelectedPhase, mul_assoc] using h

def p2SelectedModeFin
    (kind : P2SelectedKind) (k : Fin 24) : Fin 48 :=
  match kind with
  | .even => ⟨2 * k.val, by omega⟩
  | .odd => ⟨2 * k.val + 1, by omega⟩

@[simp] theorem p2SelectedModeFin_val
    (kind : P2SelectedKind) (k : Fin 24) :
    (p2SelectedModeFin kind k).val = p2SelectedDegree kind k.val := by
  cases kind <;> rfl

def p2SelectedScaleCenterQ
    (kind : P2SelectedKind) (k : Fin 24) : ℚ :=
  p2ScaleCenterQ (p2SelectedDegree kind k.val)

theorem abs_p2SphericalReal_selected_le_two
    (kind : P2SelectedKind) (k : ℕ) (r : ℝ) :
    |p2SphericalReal (p2SelectedDegree kind k) r| ≤ 2 := by
  cases kind with
  | even => exact abs_p2SphericalReal_even_le_two k r
  | odd => exact abs_p2SphericalReal_odd_le_two k r

noncomputable def p2SelectedComponent100PanelPolynomial
    (kind : P2SelectedKind) (k : Fin 24) (c q : ℝ) : ℝ[X] :=
  p2SelectedSphericalPanelPolynomial kind k.val q
    (p2Spherical100PanelPolynomial (p2SelectedDegree kind k.val) c)

noncomputable def p2SelectedComponent100PanelError (q ε : ℝ) : ℝ :=
  p2SelectedSphericalPanelError q ε p2Spherical100Error
    (2 + p2Spherical100Error)

theorem p2SelectedComponent100PanelError_nonneg
    (q ε : ℝ) (hε : 0 ≤ ε) :
    0 ≤ p2SelectedComponent100PanelError q ε := by
  unfold p2SelectedComponent100PanelError
    p2SelectedSphericalPanelError p2Spherical100Error
  positivity

/-- Canonical degree-100 selected-component adapter.  Its only
mode-specific transcendental input is the kernel-checked rational scale
certificate `hscale`; all polynomial coefficients and displayed errors are
rational. -/
theorem p2SelectedComponent100_centeredEncloses
    (kind : P2SelectedKind) (k : Fin 24) (c h q ε : ℝ)
    (hband : |c| + h ≤ 50)
    (hε : 0 ≤ ε)
    (hscale : |p2LegendreSphericalScale (p2SelectedDegree kind k.val) -
      q| ≤ ε) :
    PolyEnclosure.CenteredEncloses c h (p2SelectedComponent kind k.val)
      (p2SelectedComponent100PanelPolynomial kind k c q)
      (p2SelectedComponent100PanelError q ε) := by
  let ps := p2Spherical100PanelPolynomial
    (p2SelectedDegree kind k.val) c
  let Bs := 2 + p2Spherical100Error
  have hs : PolyEnclosure.CenteredEncloses c h
      (p2SphericalReal (p2SelectedDegree kind k.val)) ps
      p2Spherical100Error := by
    simpa [ps] using
      p2SphericalReal100_centeredEncloses (p2SelectedModeFin kind k) c h hband
  have hp : PolyEnclosure.PolyBound h ps Bs := by
    apply hs.polyBound_of_functionBound
    intro y hy
    exact abs_p2SphericalReal_selected_le_two kind k.val y
  simpa [p2SelectedComponent100PanelPolynomial,
    p2SelectedComponent100PanelError, ps, Bs] using
      p2SelectedComponent_centeredEncloses_of_spherical
        kind k.val q ε hscale hs hp hε

theorem p2SelectedComponent100PanelPolynomial_polyBound
    (kind : P2SelectedKind) (k : Fin 24) (c h q ε : ℝ)
    (hband : |c| + h ≤ 50) (hε : 0 ≤ ε)
    (hscale : |p2LegendreSphericalScale (p2SelectedDegree kind k.val) -
      q| ≤ ε) :
    PolyEnclosure.PolyBound h
      (p2SelectedComponent100PanelPolynomial kind k c q)
      (1 + p2SelectedComponent100PanelError q ε) := by
  have he := p2SelectedComponent100_centeredEncloses
    kind k c h q ε hband hε hscale
  apply he.polyBound_of_functionBound
  intro y hy
  exact abs_p2SelectedComponent_le_one kind k.val y

noncomputable def p2SelectedComponent100ScaleCenterPolynomial
    (kind : P2SelectedKind) (k : Fin 24) (c : ℝ) : ℝ[X] :=
  p2SelectedComponent100PanelPolynomial kind k c
    (p2SelectedScaleCenterQ kind k : ℝ)

noncomputable def p2SelectedComponent100ScaleCenterError
    (kind : P2SelectedKind) (k : Fin 24) : ℝ :=
  p2SelectedComponent100PanelError
    (p2SelectedScaleCenterQ kind k : ℝ) (1 / 10 ^ 20)

/-- The canonical degree-100 component witness using the 48 exact rational
scale centers from `P2ScaleCenters`. -/
theorem p2SelectedComponent100_scaleCenter_centeredEncloses
    (kind : P2SelectedKind) (k : Fin 24) (c h : ℝ)
    (hband : |c| + h ≤ 50) :
    PolyEnclosure.CenteredEncloses c h (p2SelectedComponent kind k.val)
      (p2SelectedComponent100ScaleCenterPolynomial kind k c)
      (p2SelectedComponent100ScaleCenterError kind k) := by
  have hscale :=
    (abs_p2LegendreSphericalScale_sub_center_lt
      (p2SelectedModeFin kind k)).le
  have hscale' :
      |p2LegendreSphericalScale (p2SelectedDegree kind k.val) -
        (p2SelectedScaleCenterQ kind k : ℝ)| ≤ 1 / 10 ^ 20 := by
    simpa only [p2SelectedModeFin_val, p2ScaleCenter,
      p2SelectedScaleCenterQ] using hscale
  simpa [p2SelectedComponent100ScaleCenterPolynomial,
    p2SelectedComponent100ScaleCenterError] using
      p2SelectedComponent100_centeredEncloses kind k c h
        (p2SelectedScaleCenterQ kind k : ℝ) (1 / 10 ^ 20)
        hband (by norm_num) hscale'

theorem p2SelectedComponent100ScaleCenterError_nonneg
    (kind : P2SelectedKind) (k : Fin 24) :
    0 ≤ p2SelectedComponent100ScaleCenterError kind k := by
  apply p2SelectedComponent100PanelError_nonneg
  norm_num

theorem p2SelectedComponent100ScaleCenterPolynomial_polyBound
    (kind : P2SelectedKind) (k : Fin 24) (c h : ℝ)
    (hband : |c| + h ≤ 50) :
    PolyEnclosure.PolyBound h
      (p2SelectedComponent100ScaleCenterPolynomial kind k c)
      (1 + p2SelectedComponent100ScaleCenterError kind k) := by
  have hscale :=
    (abs_p2LegendreSphericalScale_sub_center_lt
      (p2SelectedModeFin kind k)).le
  have hscale' :
      |p2LegendreSphericalScale (p2SelectedDegree kind k.val) -
        (p2SelectedScaleCenterQ kind k : ℝ)| ≤ 1 / 10 ^ 20 := by
    simpa only [p2SelectedModeFin_val, p2ScaleCenter,
      p2SelectedScaleCenterQ] using hscale
  simpa [p2SelectedComponent100ScaleCenterPolynomial,
    p2SelectedComponent100ScaleCenterError] using
      p2SelectedComponent100PanelPolynomial_polyBound kind k c h
        (p2SelectedScaleCenterQ kind k : ℝ) (1 / 10 ^ 20)
        hband (by norm_num) hscale'

theorem polyBound_mul
    {h P Q : ℝ} {p q : ℝ[X]}
    (hp : PolyEnclosure.PolyBound h p P)
    (hq : PolyEnclosure.PolyBound h q Q)
    (hP : 0 ≤ P) :
    PolyEnclosure.PolyBound h (p * q) (P * Q) := by
  intro x hx
  rw [Polynomial.eval_mul, abs_mul]
  exact mul_le_mul (hp x hx) (hq x hx) (abs_nonneg _) hP

noncomputable def panelPairError
    (eu ev Bu Bv : ℝ) : ℝ :=
  eu * ev + eu * Bv + Bu * ev

noncomputable def panelTripleError
    (ed eu ev Bd Bu Bv : ℝ) : ℝ :=
  ed * panelPairError eu ev Bu Bv + ed * (Bu * Bv) +
    Bd * panelPairError eu ev Bu Bv

/-- Witness-driven product closure for generated panel certificates.  The
three input polynomials and all six scalar bounds may be supplied directly
by a generated table; no reduction of a global symbolic polynomial is
required. -/
theorem panelTripleProduct_centeredEncloses
    {c h ed eu ev Bd Bu Bv : ℝ}
    {d u v : ℝ → ℝ} {pd pu pv : ℝ[X]}
    (hd : PolyEnclosure.CenteredEncloses c h d pd ed)
    (hu : PolyEnclosure.CenteredEncloses c h u pu eu)
    (hv : PolyEnclosure.CenteredEncloses c h v pv ev)
    (hpd : PolyEnclosure.PolyBound h pd Bd)
    (hpu : PolyEnclosure.PolyBound h pu Bu)
    (hpv : PolyEnclosure.PolyBound h pv Bv)
    (hed : 0 ≤ ed) (heu : 0 ≤ eu)
    (hBd : 0 ≤ Bd) (hBu : 0 ≤ Bu) :
    PolyEnclosure.CenteredEncloses c h
      (fun r ↦ d r * (u r * v r)) (pd * (pu * pv))
      (panelTripleError ed eu ev Bd Bu Bv) := by
  have huv := hu.mul hv hpu hpv heu hBu
  have hpuv := polyBound_mul hpu hpv hBu
  have h := hd.mul huv hpd hpuv hed hBd
  simpa [panelPairError, panelTripleError] using h

/-- Exact local-coordinate integral enclosure corresponding to
`panelTripleProduct_centeredEncloses`. -/
theorem integral_panelTripleProduct_sub_exactIntegral_le
    {c h ed eu ev Bd Bu Bv : ℝ}
    {d u v : ℝ → ℝ} {pd pu pv : ℝ[X]}
    (hh : 0 ≤ h)
    (hd : PolyEnclosure.CenteredEncloses c h d pd ed)
    (hu : PolyEnclosure.CenteredEncloses c h u pu eu)
    (hv : PolyEnclosure.CenteredEncloses c h v pv ev)
    (hpd : PolyEnclosure.PolyBound h pd Bd)
    (hpu : PolyEnclosure.PolyBound h pu Bu)
    (hpv : PolyEnclosure.PolyBound h pv Bv)
    (hed : 0 ≤ ed) (heu : 0 ≤ eu)
    (hBd : 0 ≤ Bd) (hBu : 0 ≤ Bu)
    (hint : IntervalIntegrable (fun r ↦ d r * (u r * v r))
      MeasureTheory.volume (c - h) (c + h)) :
    |(∫ r in c-h..c+h, d r * (u r * v r)) -
        PolyEnclosure.exactIntegral (pd * (pu * pv)) (-h) h| ≤
      2 * h * panelTripleError ed eu ev Bd Bu Bv := by
  apply PolyEnclosure.integral_panel_sub_exactIntegral_le hh
    (panelTripleProduct_centeredEncloses hd hu hv hpd hpu hpv
      hed heu hBd hBu)
  exact hint

noncomputable def p2SelectedBandIntegrand
    (kind : P2SelectedKind) (i j : ℕ) (r : ℝ) : ℝ :=
  (GlideKernel.p2Omega r - GlideKernel.p2Alpha) *
    (p2SelectedComponent kind j r * p2SelectedComponent kind i r)

@[simp] theorem p2SelectedBandIntegrand_even
    (i j : ℕ) (r : ℝ) :
    p2SelectedBandIntegrand .even i j r = p2EvenBandIntegrand i j r := by
  unfold p2SelectedBandIntegrand p2SelectedComponent p2EvenBandIntegrand
  ring

@[simp] theorem p2SelectedBandIntegrand_odd
    (i j : ℕ) (r : ℝ) :
    p2SelectedBandIntegrand .odd i j r = p2OddBandIntegrand i j r := by
  unfold p2SelectedBandIntegrand p2SelectedComponent p2OddBandIntegrand
  ring

theorem continuous_p2SelectedBandIntegrand
    (kind : P2SelectedKind) (i j : ℕ) :
    Continuous (p2SelectedBandIntegrand kind i j) := by
  cases kind with
  | even =>
      rw [show p2SelectedBandIntegrand .even i j =
          p2EvenBandIntegrand i j by
        funext r
        exact p2SelectedBandIntegrand_even i j r]
      exact continuous_p2EvenBandIntegrand i j
  | odd =>
      rw [show p2SelectedBandIntegrand .odd i j =
          p2OddBandIntegrand i j by
        funext r
        exact p2SelectedBandIntegrand_odd i j r]
      exact continuous_p2OddBandIntegrand i j

/-- Local selected-component integrand closure from arbitrary generated
defect and component witnesses. -/
theorem p2SelectedBandIntegrand_centeredEncloses
    {c h ed ei ej Bd Bi Bj : ℝ}
    {pd pi pj : ℝ[X]} (kind : P2SelectedKind) (i j : ℕ)
    (hd : PolyEnclosure.CenteredEncloses c h
      (fun r ↦ GlideKernel.p2Omega r - GlideKernel.p2Alpha) pd ed)
    (hi : PolyEnclosure.CenteredEncloses c h
      (p2SelectedComponent kind i) pi ei)
    (hj : PolyEnclosure.CenteredEncloses c h
      (p2SelectedComponent kind j) pj ej)
    (hpd : PolyEnclosure.PolyBound h pd Bd)
    (hpi : PolyEnclosure.PolyBound h pi Bi)
    (hpj : PolyEnclosure.PolyBound h pj Bj)
    (hed : 0 ≤ ed) (hej : 0 ≤ ej)
    (hBd : 0 ≤ Bd) (hBj : 0 ≤ Bj) :
    PolyEnclosure.CenteredEncloses c h
      (p2SelectedBandIntegrand kind i j) (pd * (pj * pi))
      (panelTripleError ed ej ei Bd Bj Bi) := by
  exact panelTripleProduct_centeredEncloses
    hd hj hi hpd hpj hpi hed hej hBd hBj

/-- Integral form of the selected-component witness theorem.  Integrability
is discharged from the analytic continuity theorem rather than generated
data. -/
theorem integral_p2SelectedBandIntegrand_sub_exactIntegral_le
    {c h ed ei ej Bd Bi Bj : ℝ}
    {pd pi pj : ℝ[X]} (kind : P2SelectedKind) (i j : ℕ)
    (hh : 0 ≤ h)
    (hd : PolyEnclosure.CenteredEncloses c h
      (fun r ↦ GlideKernel.p2Omega r - GlideKernel.p2Alpha) pd ed)
    (hi : PolyEnclosure.CenteredEncloses c h
      (p2SelectedComponent kind i) pi ei)
    (hj : PolyEnclosure.CenteredEncloses c h
      (p2SelectedComponent kind j) pj ej)
    (hpd : PolyEnclosure.PolyBound h pd Bd)
    (hpi : PolyEnclosure.PolyBound h pi Bi)
    (hpj : PolyEnclosure.PolyBound h pj Bj)
    (hed : 0 ≤ ed) (hej : 0 ≤ ej)
    (hBd : 0 ≤ Bd) (hBj : 0 ≤ Bj) :
    |(∫ r in c-h..c+h, p2SelectedBandIntegrand kind i j r) -
        PolyEnclosure.exactIntegral (pd * (pj * pi)) (-h) h| ≤
      2 * h * panelTripleError ed ej ei Bd Bj Bi := by
  apply integral_panelTripleProduct_sub_exactIntegral_le hh
    hd hj hi hpd hpj hpi hed hej hBd hBj
  exact (continuous_p2SelectedBandIntegrand kind i j).intervalIntegrable _ _

noncomputable def p2CanonicalPanelIntegrandPolynomial
    (kind : P2SelectedKind) (i j : Fin 24) (c : ℝ) (M : ℕ)
    (qi qj : ℝ) : ℝ[X] :=
  p2DefectPanelPolynomial c M *
    (p2SelectedComponent100PanelPolynomial kind j c qj *
      p2SelectedComponent100PanelPolynomial kind i c qi)

noncomputable def p2CanonicalPanelIntegrandError
    (c h : ℝ) (M : ℕ) (qi εi qj εj : ℝ) : ℝ :=
  panelTripleError
    (p2DefectPanelError c h M)
    (p2SelectedComponent100PanelError qj εj)
    (p2SelectedComponent100PanelError qi εi)
    (7447 / 1000 + p2DefectPanelError c h M)
    (1 + p2SelectedComponent100PanelError qj εj)
    (1 + p2SelectedComponent100PanelError qi εi)

/-- Fully composed canonical local panel theorem.  This is a convenience
adapter; generated tables may instead call
`p2SelectedBandIntegrand_centeredEncloses` with smaller pre-expanded
witness polynomials. -/
theorem p2CanonicalPanelIntegrand_centeredEncloses
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℝ) (M : ℕ) (qi εi qj εj : ℝ)
    (hh : 0 ≤ h) (hband : |c| + h ≤ 50)
    (hrho : prefixDenominatorRho 0 c h < 1)
    (hεi : 0 ≤ εi) (hεj : 0 ≤ εj)
    (hscalei :
      |p2LegendreSphericalScale (p2SelectedDegree kind i.val) -
        qi| ≤ εi)
    (hscalej :
      |p2LegendreSphericalScale (p2SelectedDegree kind j.val) -
        qj| ≤ εj) :
    PolyEnclosure.CenteredEncloses c h
      (p2SelectedBandIntegrand kind i.val j.val)
      (p2CanonicalPanelIntegrandPolynomial kind i j c M qi qj)
      (p2CanonicalPanelIntegrandError c h M qi εi qj εj) := by
  have hd := p2Defect_centeredEncloses c h M hh hband hrho
  have hi := p2SelectedComponent100_centeredEncloses
    kind i c h qi εi hband hεi hscalei
  have hj := p2SelectedComponent100_centeredEncloses
    kind j c h qj εj hband hεj hscalej
  have hpd := p2DefectPanelPolynomial_polyBound c h M hh hband hrho
  have hpi := p2SelectedComponent100PanelPolynomial_polyBound
    kind i c h qi εi hband hεi hscalei
  have hpj := p2SelectedComponent100PanelPolynomial_polyBound
    kind j c h qj εj hband hεj hscalej
  have hed := p2DefectPanelError_nonneg c h M hh hband hrho
  have hej := p2SelectedComponent100PanelError_nonneg qj εj hεj
  have hBd : 0 ≤ 7447 / 1000 + p2DefectPanelError c h M := by positivity
  have hBj : 0 ≤ 1 + p2SelectedComponent100PanelError qj εj := by positivity
  simpa [p2CanonicalPanelIntegrandPolynomial,
    p2CanonicalPanelIntegrandError] using
      p2SelectedBandIntegrand_centeredEncloses kind i.val j.val
        hd hi hj hpd hpi hpj hed hej hBd hBj

theorem integral_p2CanonicalPanelIntegrand_sub_exactIntegral_le
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℝ) (M : ℕ) (qi εi qj εj : ℝ)
    (hh : 0 ≤ h) (hband : |c| + h ≤ 50)
    (hrho : prefixDenominatorRho 0 c h < 1)
    (hεi : 0 ≤ εi) (hεj : 0 ≤ εj)
    (hscalei :
      |p2LegendreSphericalScale (p2SelectedDegree kind i.val) -
        qi| ≤ εi)
    (hscalej :
      |p2LegendreSphericalScale (p2SelectedDegree kind j.val) -
        qj| ≤ εj) :
    |(∫ r in c-h..c+h, p2SelectedBandIntegrand kind i.val j.val r) -
        PolyEnclosure.exactIntegral
          (p2CanonicalPanelIntegrandPolynomial kind i j c M qi qj)
          (-h) h| ≤
      2 * h * p2CanonicalPanelIntegrandError c h M qi εi qj εj := by
  apply PolyEnclosure.integral_panel_sub_exactIntegral_le hh
    (p2CanonicalPanelIntegrand_centeredEncloses kind i j c h M
      qi εi qj εj hh hband hrho hεi hεj hscalei hscalej)
  exact (continuous_p2SelectedBandIntegrand kind i.val j.val).intervalIntegrable _ _

noncomputable def p2ScaleCenteredPanelIntegrandPolynomial
    (kind : P2SelectedKind) (i j : Fin 24) (c : ℝ) (M : ℕ) : ℝ[X] :=
  p2CanonicalPanelIntegrandPolynomial kind i j c M
    (p2SelectedScaleCenterQ kind i : ℝ)
    (p2SelectedScaleCenterQ kind j : ℝ)

noncomputable def p2ScaleCenteredPanelIntegrandError
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℝ) (M : ℕ) : ℝ :=
  p2CanonicalPanelIntegrandError c h M
    (p2SelectedScaleCenterQ kind i : ℝ) (1 / 10 ^ 20)
    (p2SelectedScaleCenterQ kind j : ℝ) (1 / 10 ^ 20)

/-- Concrete local integrand enclosure using the common degree-100 models
and the kernel-checked 48-entry rational scale-center table. -/
theorem p2ScaleCenteredPanelIntegrand_centeredEncloses
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℝ) (M : ℕ)
    (hh : 0 ≤ h) (hband : |c| + h ≤ 50)
    (hrho : prefixDenominatorRho 0 c h < 1) :
    PolyEnclosure.CenteredEncloses c h
      (p2SelectedBandIntegrand kind i.val j.val)
      (p2ScaleCenteredPanelIntegrandPolynomial kind i j c M)
      (p2ScaleCenteredPanelIntegrandError kind i j c h M) := by
  have hscalei :=
    (abs_p2LegendreSphericalScale_sub_center_lt
      (p2SelectedModeFin kind i)).le
  have hscalei' :
      |p2LegendreSphericalScale (p2SelectedDegree kind i.val) -
        (p2SelectedScaleCenterQ kind i : ℝ)| ≤ 1 / 10 ^ 20 := by
    simpa only [p2SelectedModeFin_val, p2ScaleCenter,
      p2SelectedScaleCenterQ] using hscalei
  have hscalej :=
    (abs_p2LegendreSphericalScale_sub_center_lt
      (p2SelectedModeFin kind j)).le
  have hscalej' :
      |p2LegendreSphericalScale (p2SelectedDegree kind j.val) -
        (p2SelectedScaleCenterQ kind j : ℝ)| ≤ 1 / 10 ^ 20 := by
    simpa only [p2SelectedModeFin_val, p2ScaleCenter,
      p2SelectedScaleCenterQ] using hscalej
  simpa [p2ScaleCenteredPanelIntegrandPolynomial,
    p2ScaleCenteredPanelIntegrandError] using
      p2CanonicalPanelIntegrand_centeredEncloses kind i j c h M
        (p2SelectedScaleCenterQ kind i : ℝ) (1 / 10 ^ 20)
        (p2SelectedScaleCenterQ kind j : ℝ) (1 / 10 ^ 20)
        hh hband hrho (by norm_num) (by norm_num) hscalei' hscalej'

theorem integral_p2ScaleCenteredPanelIntegrand_sub_exactIntegral_le
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℝ) (M : ℕ)
    (hh : 0 ≤ h) (hband : |c| + h ≤ 50)
    (hrho : prefixDenominatorRho 0 c h < 1) :
    |(∫ r in c-h..c+h, p2SelectedBandIntegrand kind i.val j.val r) -
        PolyEnclosure.exactIntegral
          (p2ScaleCenteredPanelIntegrandPolynomial kind i j c M)
          (-h) h| ≤
      2 * h * p2ScaleCenteredPanelIntegrandError kind i j c h M := by
  apply PolyEnclosure.integral_panel_sub_exactIntegral_le hh
    (p2ScaleCenteredPanelIntegrand_centeredEncloses
      kind i j c h M hh hband hrho)
  exact (continuous_p2SelectedBandIntegrand kind i.val j.val).intervalIntegrable _ _

end RHP2Bridge
