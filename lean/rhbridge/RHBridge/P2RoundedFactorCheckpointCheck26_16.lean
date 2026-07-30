import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk16 :
    P2RoundedFactorCheckpointData.panel26Nonprefix =
      normalizedNonprefixAtomApprox ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel26Nonprefix =
      normalizedNonprefixAtomApprox ⟨26, by decide⟩ := by
  exact panel26FactorChunk16

end RHP2Bridge
