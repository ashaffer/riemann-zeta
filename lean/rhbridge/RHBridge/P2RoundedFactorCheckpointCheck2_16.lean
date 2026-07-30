import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk16 :
    P2RoundedFactorCheckpointData.panel2Nonprefix =
      normalizedNonprefixAtomApprox ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel2Nonprefix =
      normalizedNonprefixAtomApprox ⟨2, by decide⟩ := by
  exact panel2FactorChunk16

end RHP2Bridge
