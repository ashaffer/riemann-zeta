import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk16 :
    P2RoundedFactorCheckpointData.panel22Nonprefix =
      normalizedNonprefixAtomApprox ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel22Nonprefix =
      normalizedNonprefixAtomApprox ⟨22, by decide⟩ := by
  exact panel22FactorChunk16

end RHP2Bridge
