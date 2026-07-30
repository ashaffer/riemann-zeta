import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk16 :
    P2RoundedFactorCheckpointData.panel7Nonprefix =
      normalizedNonprefixAtomApprox ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel7Nonprefix =
      normalizedNonprefixAtomApprox ⟨7, by decide⟩ := by
  exact panel7FactorChunk16

end RHP2Bridge
