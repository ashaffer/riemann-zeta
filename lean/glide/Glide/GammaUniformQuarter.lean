/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/

import Glide.DigammaSeriesQuarter
import Glide.GammaUniform

/-!
# Quarter-line consequences of locally uniform Gamma convergence

This fixed-normalization module is deliberately downstream of the general
`Glide.GammaUniform` API.
-/

open Set

namespace GlideKernel

/-- The derivative formula needed on the quarter-line, with no remaining
analytic premise. -/
theorem hasDerivAt_quarterDigammaReal (r : ℝ) :
    HasDerivAt quarterDigammaReal (quarterTrigammaSlope r) r :=
  hasDerivAt_quarterDigammaReal_of_gammaSeq_locallyUniform
    gammaSeq_tendstoLocallyUniformlyOn r

/-- The quarter-line real part of digamma is strictly increasing on the
nonnegative half-line. -/
theorem quarterDigammaReal_strictMonoOn :
    StrictMonoOn quarterDigammaReal (Ici 0) :=
  quarterDigammaReal_strictMonoOn_of_gammaSeq_locallyUniform
    gammaSeq_tendstoLocallyUniformlyOn

/-- The unconditional exterior comparison used by the p=2 application. -/
theorem quarterDigammaReal_exterior_lower_bound {S r : ℝ}
    (hS : 0 ≤ S) (hr : S ≤ |r|) :
    quarterDigammaReal S ≤ quarterDigammaReal r :=
  quarterDigammaReal_exterior_lower_bound_of_gammaSeq_locallyUniform
    gammaSeq_tendstoLocallyUniformlyOn hS hr

end GlideKernel
