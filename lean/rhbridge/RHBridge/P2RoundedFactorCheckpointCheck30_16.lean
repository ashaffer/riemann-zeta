import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk16 :
    P2RoundedFactorCheckpointData.panel30Nonprefix =
      normalizedNonprefixAtomApprox ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel30Nonprefix =
      normalizedNonprefixAtomApprox ⟨30, by decide⟩ := by
  exact panel30FactorChunk16

end RHP2Bridge
