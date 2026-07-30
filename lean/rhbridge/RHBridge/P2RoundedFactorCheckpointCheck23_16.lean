import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk16 :
    P2RoundedFactorCheckpointData.panel23Nonprefix =
      normalizedNonprefixAtomApprox ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel23Nonprefix =
      normalizedNonprefixAtomApprox ⟨23, by decide⟩ := by
  exact panel23FactorChunk16

end RHP2Bridge
