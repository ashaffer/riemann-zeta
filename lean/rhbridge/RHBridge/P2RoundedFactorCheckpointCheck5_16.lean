import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk16 :
    P2RoundedFactorCheckpointData.panel5Nonprefix =
      normalizedNonprefixAtomApprox ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel5Nonprefix =
      normalizedNonprefixAtomApprox ⟨5, by decide⟩ := by
  exact panel5FactorChunk16

end RHP2Bridge
