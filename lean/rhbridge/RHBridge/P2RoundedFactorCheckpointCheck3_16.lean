import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk16 :
    P2RoundedFactorCheckpointData.panel3Nonprefix =
      normalizedNonprefixAtomApprox ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel3Nonprefix =
      normalizedNonprefixAtomApprox ⟨3, by decide⟩ := by
  exact panel3FactorChunk16

end RHP2Bridge
