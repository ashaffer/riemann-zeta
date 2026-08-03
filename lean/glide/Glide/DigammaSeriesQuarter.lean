/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/

import Glide.DigammaMonotone
import Glide.DigammaSeries

/-!
# Quarter-line consequences of the general digamma series

This module is the fixed-normalization compatibility layer over
`Glide.DigammaSeries`.
-/

open Filter Set
open scoped Topology

namespace GlideKernel

/-- The locally uniform Euler limit supplies the precise derivative premise
used by the quarter-line monotonicity argument. -/
theorem hasDerivAt_quarterDigammaReal_of_gammaSeq_locallyUniform
    (hGammaSeq : TendstoLocallyUniformlyOn
      (fun n z => Complex.GammaSeq z n) Complex.Gamma atTop positiveRealHalfPlane)
    (r : ℝ) :
    HasDerivAt quarterDigammaReal (quarterTrigammaSlope r) r := by
  apply hasDerivAt_quarterDigammaReal_of_trigammaSeries
  have h := hasDerivAt_digamma_of_gammaSeq_locallyUniform hGammaSeq
    (z := (1 / 4 : ℂ) + Complex.I * ((r / 2 : ℝ) : ℂ)) (by norm_num)
  unfold trigammaSeries at h
  convert h using 1
  apply tsum_congr
  intro n
  congr 2
  push_cast
  ring

/-- Strict monotonicity of the real quarter-line restriction follows from a
locally uniform Euler limit for Gamma. -/
theorem quarterDigammaReal_strictMonoOn_of_gammaSeq_locallyUniform
    (hGammaSeq : TendstoLocallyUniformlyOn
      (fun n z => Complex.GammaSeq z n) Complex.Gamma atTop positiveRealHalfPlane) :
    StrictMonoOn quarterDigammaReal (Ici 0) :=
  quarterDigammaReal_strictMonoOn_of_hasDerivAt
    (fun r _ => hasDerivAt_quarterDigammaReal_of_gammaSeq_locallyUniform hGammaSeq r)

/-- The exterior comparison needed by the p=2 application, conditional only
on the locally uniform form of mathlib's existing pointwise Euler limit. -/
theorem quarterDigammaReal_exterior_lower_bound_of_gammaSeq_locallyUniform
    (hGammaSeq : TendstoLocallyUniformlyOn
      (fun n z => Complex.GammaSeq z n) Complex.Gamma atTop positiveRealHalfPlane)
    {S r : ℝ} (hS : 0 ≤ S) (hr : S ≤ |r|) :
    quarterDigammaReal S ≤ quarterDigammaReal r :=
  quarterDigammaReal_exterior_lower_bound_of_hasDerivAt
    (fun x _ => hasDerivAt_quarterDigammaReal_of_gammaSeq_locallyUniform hGammaSeq x) hS hr

end GlideKernel
