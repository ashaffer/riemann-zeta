import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk16 :
    P2RoundedFactorCheckpointData.panel13Nonprefix =
      normalizedNonprefixAtomApprox ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel13Nonprefix =
      normalizedNonprefixAtomApprox ⟨13, by decide⟩ := by
  exact panel13FactorChunk16

end RHP2Bridge
