import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk16 :
    P2RoundedFactorCheckpointData.panel0Nonprefix =
      normalizedNonprefixAtomApprox ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel0Nonprefix =
      normalizedNonprefixAtomApprox ⟨0, by decide⟩ := by
  exact panel0FactorChunk16

end RHP2Bridge
