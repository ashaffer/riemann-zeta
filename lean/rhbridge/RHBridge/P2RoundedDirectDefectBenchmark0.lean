import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

/-- Panel-0 defect pieces computed directly from the canonical atom evaluator.
This deliberately does not mention the generated per-atom checkpoint literals. -/
def panel0DirectDefectPieces : DefectPieces where
  prefixTerms := Vector.ofFn fun i =>
    normalizedPrefixTermAtomApprox i ⟨0, by decide⟩
  nonprefix := normalizedNonprefixAtomApprox ⟨0, by decide⟩

theorem panel0FlatDefect_eq_directAtomAssembly :
    P2RoundedFactorCheckpointData.panel0FlatDefect =
      panel0DirectDefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
