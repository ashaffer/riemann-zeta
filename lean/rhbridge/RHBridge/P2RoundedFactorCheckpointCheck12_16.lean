import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk16 :
    P2RoundedFactorCheckpointData.panel12Nonprefix =
      normalizedNonprefixAtomApprox ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel12Nonprefix =
      normalizedNonprefixAtomApprox ⟨12, by decide⟩ := by
  exact panel12FactorChunk16

end RHP2Bridge
