import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk16 :
    P2RoundedFactorCheckpointData.panel25Nonprefix =
      normalizedNonprefixAtomApprox ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel25Nonprefix =
      normalizedNonprefixAtomApprox ⟨25, by decide⟩ := by
  exact panel25FactorChunk16

end RHP2Bridge
