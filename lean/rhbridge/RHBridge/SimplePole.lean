/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.Complex.CauchyIntegral

/-!
# Finite simple-principal-part removal and circle formulas

This file gives an application-independent API for functions with finitely
many specified simple principal parts.  It constructs a globally
differentiable regularization, packages the result as an entire remainder,
and proves scalar- and Banach-valued circle-integral formulas.

The residue is allowed to vanish in `HasSimplePrincipalPartAt`, so that the
same predicate also covers removable singularities.  This file deliberately
does not define arbitrary higher-order residues.
-/

namespace RHBridge.ComplexResidue

open Complex Metric Set
open Filter
open scoped Interval Topology

noncomputable section

/-- A function has the indicated simple principal part at `p` if, on a
punctured neighborhood of `p`, subtracting `residue / (z - p)` leaves a
function differentiable at `p`. The residue is allowed to vanish, so this
predicate also covers removable singularities uniformly. -/
def HasSimplePrincipalPartAt
    (h : ℂ → ℂ) (p residue : ℂ) : Prop :=
  ∃ remainder : ℂ → ℂ,
    DifferentiableAt ℂ remainder p ∧
      h =ᶠ[nhdsWithin p {p}ᶜ]
        fun z ↦ residue * (z - p)⁻¹ + remainder z

/-- A genuine simple pole with a specified nonzero residue. -/
def HasSimplePoleAt (h : ℂ → ℂ) (p residue : ℂ) : Prop :=
  residue ≠ 0 ∧ HasSimplePrincipalPartAt h p residue

theorem HasSimplePoleAt.residue_ne_zero
    {h : ℂ → ℂ} {p residue : ℂ}
    (hp : HasSimplePoleAt h p residue) : residue ≠ 0 :=
  hp.1

theorem HasSimplePoleAt.hasSimplePrincipalPartAt
    {h : ℂ → ℂ} {p residue : ℂ}
    (hp : HasSimplePoleAt h p residue) :
    HasSimplePrincipalPartAt h p residue :=
  hp.2

/-- Replace the values of `h - ∑ rₚ/(z-p)` at its finitely many removable
singularities by the corresponding local analytic remainders. -/
noncomputable def finitePoleRegularization
    (poles : Finset ℂ) (residue : ℂ → ℂ)
    (localRemainder : ℂ → ℂ → ℂ) (h : ℂ → ℂ) : ℂ → ℂ :=
  fun z ↦ if _hz : z ∈ poles then
      localRemainder z z -
        ∑ q ∈ poles.erase z, residue q * (z - q)⁻¹
    else h z - ∑ q ∈ poles, residue q * (z - q)⁻¹

theorem finitePoleRegularization_add_principalParts
    (poles : Finset ℂ) (residue : ℂ → ℂ)
    (localRemainder : ℂ → ℂ → ℂ) (h : ℂ → ℂ)
    {z : ℂ} (hz : z ∉ poles) :
    finitePoleRegularization poles residue localRemainder h z +
        ∑ q ∈ poles, residue q * (z - q)⁻¹ = h z := by
  rw [finitePoleRegularization, dif_neg hz]
  ring

/-- Global removal of finitely many simple-pole singularities.  Notice that
the hypothesis at a pole is only a punctured-neighborhood identity; the
definition above supplies the missing value from the local remainder. -/
theorem differentiableOn_finitePoleRegularization
    (S : Set ℂ)
    (poles : Finset ℂ) (residue : ℂ → ℂ)
    (localRemainder : ℂ → ℂ → ℂ) (h : ℂ → ℂ)
    (hoff : ∀ z ∈ S, z ∉ poles → DifferentiableAt ℂ h z)
    (hrem : ∀ p ∈ poles, DifferentiableAt ℂ (localRemainder p) p)
    (hloc : ∀ p ∈ poles,
      h =ᶠ[nhdsWithin p {p}ᶜ]
        fun z ↦ residue p * (z - p)⁻¹ + localRemainder p z) :
    DifferentiableOn ℂ
      (finitePoleRegularization poles residue localRemainder h) S := by
  classical
  intro x hxS
  by_cases hx : x ∈ poles
  · let R : ℂ → ℂ := fun z ↦ localRemainder x z -
        ∑ q ∈ poles.erase x, residue q * (z - q)⁻¹
    have hR : DifferentiableAt ℂ R x := by
      apply (hrem x hx).sub
      apply DifferentiableAt.fun_sum
      intro q hq
      have hqx : q ≠ x := (Finset.mem_erase.mp hq).1
      exact (differentiableAt_const (c := residue q)).mul
        ((differentiableAt_id.sub_const q).inv (sub_ne_zero.mpr hqx.symm))
    have havoid : ∀ᶠ z in 𝓝 x, ∀ q ∈ poles.erase x, z ≠ q :=
      (poles.erase x).eventually_all.mpr fun q hq ↦
        eventually_ne_nhds (Finset.mem_erase.mp hq).1.symm
    have hlocal : ∀ᶠ z in 𝓝 x, z ≠ x →
        h z = residue x * (z - x)⁻¹ + localRemainder x z :=
      eventually_nhdsWithin_iff.mp (hloc x hx)
    have heq : finitePoleRegularization poles residue localRemainder h =ᶠ[𝓝 x] R := by
      filter_upwards [havoid, hlocal] with z hzavoid hzloc
      by_cases hzx : z = x
      · subst z
        simp [finitePoleRegularization, hx, R]
      · have hznot : z ∉ poles := by
          intro hzp
          have : z ∈ poles.erase x := Finset.mem_erase.mpr ⟨hzx, hzp⟩
          exact hzavoid z this rfl
        have hprincipal := hzloc hzx
        rw [finitePoleRegularization, dif_neg hznot, hprincipal]
        rw [← Finset.sum_erase_add _ _ hx]
        simp [R]
        ring
    exact (hR.congr_of_eventuallyEq heq).differentiableWithinAt
  · have hopen : (↑poles : Set ℂ)ᶜ ∈ 𝓝 x := by
      exact poles.finite_toSet.isClosed.isOpen_compl.mem_nhds (by simpa using hx)
    have heq : finitePoleRegularization poles residue localRemainder h =ᶠ[𝓝 x]
        fun z ↦ h z - ∑ q ∈ poles, residue q * (z - q)⁻¹ := by
      filter_upwards [hopen] with z hz
      have hz' : z ∉ poles := by simpa using hz
      simp [finitePoleRegularization, hz']
    apply (((hoff x hxS hx).sub ?_).congr_of_eventuallyEq heq).differentiableWithinAt
    apply DifferentiableAt.fun_sum
    intro q hq
    have hxq : x ≠ q := by
      intro h
      subst q
      exact hx hq
    exact (differentiableAt_const (c := residue q)).mul
      ((differentiableAt_id.sub_const q).inv (sub_ne_zero.mpr hxq))

theorem differentiable_finitePoleRegularization
    (poles : Finset ℂ) (residue : ℂ → ℂ)
    (localRemainder : ℂ → ℂ → ℂ) (h : ℂ → ℂ)
    (hoff : ∀ z, z ∉ poles → DifferentiableAt ℂ h z)
    (hrem : ∀ p ∈ poles, DifferentiableAt ℂ (localRemainder p) p)
    (hloc : ∀ p ∈ poles,
      h =ᶠ[nhdsWithin p {p}ᶜ]
        fun z ↦ residue p * (z - p)⁻¹ + localRemainder p z) :
    Differentiable ℂ
      (finitePoleRegularization poles residue localRemainder h) := by
  intro x
  simpa only [differentiableWithinAt_univ] using
    differentiableOn_finitePoleRegularization Set.univ poles residue
      localRemainder h (fun z _ ↦ hoff z) hrem hloc x (Set.mem_univ x)

/-- Removing finitely many specified simple principal parts produces an
entire function. Away from the pole set, adding the principal parts back
recovers the original function exactly. -/
theorem exists_entire_add_finite_simplePrincipalParts
    (poles : Finset ℂ) (residue : ℂ → ℂ) (h : ℂ → ℂ)
    (hoff : ∀ z, z ∉ poles → DifferentiableAt ℂ h z)
    (hpoles : ∀ p ∈ poles, HasSimplePrincipalPartAt h p (residue p)) :
    ∃ g : ℂ → ℂ, AnalyticOnNhd ℂ g Set.univ ∧
      ∀ z, z ∉ poles →
        g z + ∑ p ∈ poles, residue p * (z - p)⁻¹ = h z := by
  classical
  have hpoles' : ∀ p ∈ poles, ∃ remainder : ℂ → ℂ,
      DifferentiableAt ℂ remainder p ∧
        h =ᶠ[nhdsWithin p {p}ᶜ]
          fun z ↦ residue p * (z - p)⁻¹ + remainder z := by
    simpa only [HasSimplePrincipalPartAt] using hpoles
  let localRemainder : ℂ → ℂ → ℂ := fun p ↦
    if hp : p ∈ poles then Classical.choose (hpoles' p hp) else 0
  have hrem : ∀ p ∈ poles, DifferentiableAt ℂ (localRemainder p) p := by
    intro p hp
    have heq : localRemainder p = Classical.choose (hpoles' p hp) := by
      simp [localRemainder, hp]
    rw [heq]
    exact (Classical.choose_spec (hpoles' p hp)).1
  have hloc : ∀ p ∈ poles,
      h =ᶠ[nhdsWithin p {p}ᶜ]
        fun z ↦ residue p * (z - p)⁻¹ + localRemainder p z := by
    intro p hp
    have heq : localRemainder p = Classical.choose (hpoles' p hp) := by
      simp [localRemainder, hp]
    rw [heq]
    exact (Classical.choose_spec (hpoles' p hp)).2
  let g := finitePoleRegularization poles residue localRemainder h
  have hg : Differentiable ℂ g := by
    apply differentiable_finitePoleRegularization poles residue localRemainder h hoff
    · exact hrem
    · exact hloc
  refine ⟨g, analyticOnNhd_univ_iff_differentiable.mpr hg, ?_⟩
  intro z hz
  exact finitePoleRegularization_add_principalParts
    poles residue localRemainder h hz

/-- A simple principal part with pole `p` and residue `r`. -/
def simplePrincipalPart (p r z : ℂ) : ℂ := (z - p)⁻¹ * r

theorem circleIntegrable_simplePrincipalPart
    {c p r : ℂ} {R : ℝ} (hp : p ∈ ball c R) :
    CircleIntegrable (simplePrincipalPart p r) c R := by
  have hR : 0 < R := dist_nonneg.trans_lt hp
  apply ContinuousOn.circleIntegrable hR.le
  apply ((continuousOn_id.sub continuousOn_const).inv₀ ?_).mul continuousOn_const
  intro z hz
  have hpnot : p ∉ sphere c R := by
    intro hpSphere
    rw [mem_ball] at hp
    rw [mem_sphere] at hpSphere
    linarith
  exact sub_ne_zero.mpr <| ne_of_mem_of_not_mem hz hpnot

/-- The integral of one simple principal part is `2πi` times its residue. -/
theorem circleIntegral_simplePrincipalPart
    {c p r : ℂ} {R : ℝ} (hp : p ∈ ball c R) :
    (∮ z in C(c, R), simplePrincipalPart p r z) = 2 * Real.pi * I * r := by
  unfold simplePrincipalPart
  change (∮ z in C(c, R), (z - p)⁻¹ • r) = _
  rw [circleIntegral.integral_smul_const]
  rw [circleIntegral.integral_sub_inv_of_mem_ball hp]
  rfl

/-- Banach-valued version of one simple principal-part integral. -/
theorem circleIntegral_sub_inv_smul
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E]
    {c p : ℂ} {r : E} {R : ℝ} (hp : p ∈ ball c R) :
    (∮ z in C(c, R), (z - p)⁻¹ • r) = (2 * Real.pi * I : ℂ) • r := by
  rw [circleIntegral.integral_smul_const]
  rw [circleIntegral.integral_sub_inv_of_mem_ball hp]

/-- Banach-valued finite sum of Cauchy kernels plus a holomorphic remainder.
This is the linear core of the finite simple-pole residue formula. -/
theorem circleIntegral_add_finite_sub_inv_smul
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E]
    {ι : Type*} (poles : Finset ι) (pole : ι → ℂ) (residue : ι → E)
    {c : ℂ} {R : ℝ} (g : ℂ → E)
    (hg : DiffContOnCl ℂ g (ball c R))
    (hR : 0 ≤ R)
    (hp : ∀ i ∈ poles, pole i ∈ ball c R) :
    (∮ z in C(c, R),
      g z + ∑ i ∈ poles, (z - pole i)⁻¹ • residue i) =
        (2 * Real.pi * I : ℂ) • ∑ i ∈ poles, residue i := by
  have hgInt : CircleIntegrable g c R :=
    (hg.continuousOn_ball.mono sphere_subset_closedBall).circleIntegrable hR
  have hpInt : ∀ i ∈ poles,
      CircleIntegrable (fun z ↦ (z - pole i)⁻¹ • residue i) c R := by
    intro i hi
    have hRpos : 0 < R := dist_nonneg.trans_lt (hp i hi)
    apply ContinuousOn.circleIntegrable hRpos.le
    apply ((continuousOn_id.sub continuousOn_const).inv₀ ?_).smul continuousOn_const
    intro z hz
    have hpnot : pole i ∉ sphere c R := by
      intro hpSphere
      have hip := hp i hi
      rw [mem_ball] at hip
      rw [mem_sphere] at hpSphere
      linarith
    exact sub_ne_zero.mpr <| ne_of_mem_of_not_mem hz hpnot
  rw [circleIntegral.integral_add hgInt (CircleIntegrable.fun_sum poles hpInt)]
  rw [hg.circleIntegral_eq_zero hR]
  rw [circleIntegral.integral_fun_sum hpInt]
  rw [zero_add, Finset.smul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  exact circleIntegral_sub_inv_smul (hp i hi)

/-- Finite simple-principal-part formula on a circle, including the empty
pole set. The explicit nonnegative-radius hypothesis is exactly what the
holomorphic zero-integral theorem needs in the empty case. -/
theorem circleIntegral_add_finite_simplePrincipalParts
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    {c : ℂ} {R : ℝ} (g : ℂ → ℂ)
    (hg : DiffContOnCl ℂ g (ball c R))
    (hR : 0 ≤ R)
    (hp : ∀ i ∈ poles, pole i ∈ ball c R) :
    (∮ z in C(c, R),
        g z + ∑ i ∈ poles, simplePrincipalPart (pole i) (residue i) z) =
      2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  simpa only [simplePrincipalPart, smul_eq_mul] using
    circleIntegral_add_finite_sub_inv_smul poles pole residue g hg hR hp

/-- Compatibility wrapper for the original nonempty-pole statement. -/
theorem circleIntegral_eq_two_pi_I_mul_sum_residues
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    {c : ℂ} {R : ℝ} (g : ℂ → ℂ)
    (hg : DiffContOnCl ℂ g (ball c R))
    (hne : poles.Nonempty)
    (hp : ∀ i ∈ poles, pole i ∈ ball c R) :
    (∮ z in C(c, R),
        g z + ∑ i ∈ poles, simplePrincipalPart (pole i) (residue i) z) =
      2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  let i₀ := hne.choose
  have hi₀ : i₀ ∈ poles := hne.choose_spec
  exact circleIntegral_add_finite_simplePrincipalParts poles pole residue g hg
    (dist_nonneg.trans_lt (hp i₀ hi₀)).le hp

/-- Extensional finite simple-pole residue theorem.  Only the values on the
contour matter; the supplied decomposition may be chosen independently of the
function's arbitrary values at its poles. -/
theorem circleIntegral_eq_two_pi_I_mul_sum_residues_of_eqOn
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    {c : ℂ} {R : ℝ} (f g : ℂ → ℂ)
    (hg : DiffContOnCl ℂ g (ball c R))
    (hne : poles.Nonempty)
    (hp : ∀ i ∈ poles, pole i ∈ ball c R)
    (hdecomp : EqOn f
      (fun z ↦ g z + ∑ i ∈ poles,
        simplePrincipalPart (pole i) (residue i) z) (sphere c R)) :
    (∮ z in C(c, R), f z) =
      2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  let i₀ := hne.choose
  have hi₀ : i₀ ∈ poles := hne.choose_spec
  have hR : 0 ≤ R := (dist_nonneg.trans_lt (hp i₀ hi₀)).le
  rw [circleIntegral.integral_congr hR hdecomp]
  exact circleIntegral_eq_two_pi_I_mul_sum_residues
    poles pole residue g hg hne hp

/-- Extensional circle formula that also supports an empty pole set. -/
theorem circleIntegral_add_finite_simplePrincipalParts_of_eqOn
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    {c : ℂ} {R : ℝ} (f g : ℂ → ℂ)
    (hg : DiffContOnCl ℂ g (ball c R))
    (hR : 0 ≤ R)
    (hp : ∀ i ∈ poles, pole i ∈ ball c R)
    (hdecomp : EqOn f
      (fun z ↦ g z + ∑ i ∈ poles,
        simplePrincipalPart (pole i) (residue i) z) (sphere c R)) :
    (∮ z in C(c, R), f z) =
      2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  rw [circleIntegral.integral_congr hR hdecomp]
  exact circleIntegral_add_finite_simplePrincipalParts
    poles pole residue g hg hR hp

end

end RHBridge.ComplexResidue
