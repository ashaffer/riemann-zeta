import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk16 :
    P2RoundedFactorCheckpointData.panel29Nonprefix =
      normalizedNonprefixAtomApprox ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel29Nonprefix =
      normalizedNonprefixAtomApprox ⟨29, by decide⟩ := by
  exact panel29FactorChunk16

end RHP2Bridge
