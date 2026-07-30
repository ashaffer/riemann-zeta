import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk16 :
    P2RoundedFactorCheckpointData.panel6Nonprefix =
      normalizedNonprefixAtomApprox ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel6Nonprefix =
      normalizedNonprefixAtomApprox ⟨6, by decide⟩ := by
  exact panel6FactorChunk16

end RHP2Bridge
