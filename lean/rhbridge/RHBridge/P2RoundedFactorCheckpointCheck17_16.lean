import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk16 :
    P2RoundedFactorCheckpointData.panel17Nonprefix =
      normalizedNonprefixAtomApprox ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel17Nonprefix =
      normalizedNonprefixAtomApprox ⟨17, by decide⟩ := by
  exact panel17FactorChunk16

end RHP2Bridge
