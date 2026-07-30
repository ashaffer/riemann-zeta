import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk16 :
    P2RoundedFactorCheckpointData.panel9Nonprefix =
      normalizedNonprefixAtomApprox ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel9Nonprefix =
      normalizedNonprefixAtomApprox ⟨9, by decide⟩ := by
  exact panel9FactorChunk16

end RHP2Bridge
