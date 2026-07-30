import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk16 :
    P2RoundedFactorCheckpointData.panel18Nonprefix =
      normalizedNonprefixAtomApprox ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel18Nonprefix =
      normalizedNonprefixAtomApprox ⟨18, by decide⟩ := by
  exact panel18FactorChunk16

end RHP2Bridge
