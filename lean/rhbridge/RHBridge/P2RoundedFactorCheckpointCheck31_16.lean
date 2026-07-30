import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk16 :
    P2RoundedFactorCheckpointData.panel31Nonprefix =
      normalizedNonprefixAtomApprox ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel31Nonprefix =
      normalizedNonprefixAtomApprox ⟨31, by decide⟩ := by
  exact panel31FactorChunk16

end RHP2Bridge
