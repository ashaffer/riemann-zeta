import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk16 :
    P2RoundedFactorCheckpointData.panel21Nonprefix =
      normalizedNonprefixAtomApprox ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel21Nonprefix =
      normalizedNonprefixAtomApprox ⟨21, by decide⟩ := by
  exact panel21FactorChunk16

end RHP2Bridge
