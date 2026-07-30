import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk16 :
    P2RoundedFactorCheckpointData.panel4Nonprefix =
      normalizedNonprefixAtomApprox ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel4Nonprefix =
      normalizedNonprefixAtomApprox ⟨4, by decide⟩ := by
  exact panel4FactorChunk16

end RHP2Bridge
