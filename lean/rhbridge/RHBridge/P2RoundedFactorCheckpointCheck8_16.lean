import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk16 :
    P2RoundedFactorCheckpointData.panel8Nonprefix =
      normalizedNonprefixAtomApprox ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel8Nonprefix =
      normalizedNonprefixAtomApprox ⟨8, by decide⟩ := by
  exact panel8FactorChunk16

end RHP2Bridge
