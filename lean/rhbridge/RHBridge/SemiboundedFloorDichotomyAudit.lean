/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SemiboundedFloorDichotomy

/-! Axiom audit for the abstract semibounded spectral-floor dichotomy. -/

#print axioms
  RHBridge.SemiboundedFloorDichotomy.uniformlyLowerBounded_iff_hasStrictGlobalShift
#print axioms RHBridge.SemiboundedFloorDichotomy.truncateBelow_antitone
#print axioms
  RHBridge.SemiboundedFloorDichotomy.truncateBelow_uniformlyLowerBounded_iff
#print axioms
  RHBridge.SemiboundedFloorDichotomy.tendsto_atBot_of_antitone_of_not_uniformlyLowerBounded
#print axioms
  RHBridge.SemiboundedFloorDichotomy.tendsto_atBot_iff_not_uniformlyLowerBounded
#print axioms
  RHBridge.SemiboundedFloorDichotomy.uniformlyLowerBounded_or_tendsto_atBot
#print axioms RHBridge.SemiboundedFloorDichotomy.uniformlyLowerBounded_of_nonnegative
