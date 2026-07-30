import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk16 :
    P2RoundedFactorCheckpointData.panel10Nonprefix =
      normalizedNonprefixAtomApprox ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel10Nonprefix =
      normalizedNonprefixAtomApprox ⟨10, by decide⟩ := by
  exact panel10FactorChunk16

end RHP2Bridge
