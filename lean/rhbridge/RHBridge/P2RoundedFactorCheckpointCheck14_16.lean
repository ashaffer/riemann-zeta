import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk16 :
    P2RoundedFactorCheckpointData.panel14Nonprefix =
      normalizedNonprefixAtomApprox ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel14Nonprefix =
      normalizedNonprefixAtomApprox ⟨14, by decide⟩ := by
  exact panel14FactorChunk16

end RHP2Bridge
