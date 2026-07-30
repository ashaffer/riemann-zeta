import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk16 :
    P2RoundedFactorCheckpointData.panel15Nonprefix =
      normalizedNonprefixAtomApprox ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel15Nonprefix =
      normalizedNonprefixAtomApprox ⟨15, by decide⟩ := by
  exact panel15FactorChunk16

end RHP2Bridge
