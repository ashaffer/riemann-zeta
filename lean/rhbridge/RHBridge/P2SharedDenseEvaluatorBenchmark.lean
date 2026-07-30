/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2SharedDenseEvaluator

/-!
# Performance sentinel for the shared canonical `p = 2` evaluator

This module is deliberately not imported by the library root.  Its theorem
forces native evaluation of all 600 entry integrals on the first panel and is
used to measure the streaming cache independently of proof elaboration.
-/

namespace RHP2Bridge.DenseRatPoly

set_option maxHeartbeats 20000000
set_option maxRecDepth 4096

/-- Force every slot of the first-panel shared vector.  The intentionally
loose bound is only a performance sentinel; the final certificate uses the
much sharper center-fit predicate. -/
theorem p2SharedFirstPanel_performanceSentinel :
    ∀ r : Fin 600, |(p2SharedPanelSums 1).get r| < 10 ^ 100 := by
  native_decide

end RHP2Bridge.DenseRatPoly
