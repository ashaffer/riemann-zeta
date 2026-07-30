import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk16 :
    P2RoundedFactorCheckpointData.panel28Nonprefix =
      normalizedNonprefixAtomApprox ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel28Nonprefix =
      normalizedNonprefixAtomApprox ⟨28, by decide⟩ := by
  exact panel28FactorChunk16

end RHP2Bridge
