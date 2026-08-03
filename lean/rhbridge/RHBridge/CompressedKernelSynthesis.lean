/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ZeroQuartetPhase

/-!
# Common compressed-kernel skeleton

The recent localization, collar, convolution, Fourier, and canonical routes
share one algebraic core.  A vector lies in the localized input space, while
its image under the global operator lies in the defect space killed by the
output projection.  The analytic problem is transversality of these spaces.

This file proves only that abstract skeleton.  It does not instantiate the
unbounded Weil operator or Suzuki's completed finite-interval domains.
-/

namespace RHP2Bridge.CompressedKernelSynthesis

/-- A nonzero localized vector whose operator image is invisible to the same
compression. -/
def HasCompressedKernelWitness
    {V : Type*} [Zero V] (P A : V → V) : Prop :=
  ∃ u : V, u ≠ 0 ∧ P u = u ∧ P (A u) = 0

/-- The intrinsic transversality/unique-continuation statement. -/
def HasTrivialCompressedKernel
    {V : Type*} [Zero V] (P A : V → V) : Prop :=
  ∀ u : V, P u = u → P (A u) = 0 → u = 0

/-- On a localized input, the compressed equation is exactly invisibility of
the uncompressed output. -/
theorem compressed_eq_iff_output_in_defect
    {V : Type*} [Zero V] (P A : V → V) {u : V}
    (hlocalized : P u = u) :
    P (A (P u)) = 0 ↔ P (A u) = 0 := by
  rw [hlocalized]

/-- Failure of transversality is exactly existence of a nonzero compressed
kernel witness. -/
theorem not_trivial_iff_witness
    {V : Type*} [Zero V] (P A : V → V) :
    ¬ HasTrivialCompressedKernel P A ↔ HasCompressedKernelWitness P A := by
  constructor
  · classical
    intro h
    unfold HasTrivialCompressedKernel at h
    push_neg at h
    obtain ⟨u, hPu, hPAu, hu⟩ := h
    exact ⟨u, hu, hPu, hPAu⟩
  · rintro ⟨u, hu, hPu, hPAu⟩ htrivial
    exact hu (htrivial u hPu hPAu)

/-- The collar or boundary residual is unconstrained by the compressed
equation: any output component killed by `P` is compatible with it. -/
theorem arbitrary_defect_output
    {V : Type*} [Zero V] (P : V → V) {r : V}
    (hr : P r = 0) : P r = 0 := hr

end RHP2Bridge.CompressedKernelSynthesis
