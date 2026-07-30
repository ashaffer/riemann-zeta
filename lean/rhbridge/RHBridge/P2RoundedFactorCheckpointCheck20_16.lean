import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk16 :
    P2RoundedFactorCheckpointData.panel20Nonprefix =
      normalizedNonprefixAtomApprox ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel20Nonprefix =
      normalizedNonprefixAtomApprox ⟨20, by decide⟩ := by
  exact panel20FactorChunk16

end RHP2Bridge
