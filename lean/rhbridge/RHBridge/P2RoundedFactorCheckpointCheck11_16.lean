import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk16 :
    P2RoundedFactorCheckpointData.panel11Nonprefix =
      normalizedNonprefixAtomApprox ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel11Nonprefix =
      normalizedNonprefixAtomApprox ⟨11, by decide⟩ := by
  exact panel11FactorChunk16

end RHP2Bridge
