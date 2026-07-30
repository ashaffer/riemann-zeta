import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk16 :
    P2RoundedFactorCheckpointData.panel24Nonprefix =
      normalizedNonprefixAtomApprox ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel24Nonprefix =
      normalizedNonprefixAtomApprox ⟨24, by decide⟩ := by
  exact panel24FactorChunk16

end RHP2Bridge
