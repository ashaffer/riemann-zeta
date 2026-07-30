import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk16 :
    P2RoundedFactorCheckpointData.panel19Nonprefix =
      normalizedNonprefixAtomApprox ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel19Nonprefix =
      normalizedNonprefixAtomApprox ⟨19, by decide⟩ := by
  exact panel19FactorChunk16

end RHP2Bridge
