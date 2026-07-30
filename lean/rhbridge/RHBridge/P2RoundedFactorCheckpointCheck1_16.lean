import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk16 :
    P2RoundedFactorCheckpointData.panel1Nonprefix =
      normalizedNonprefixAtomApprox ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel1Nonprefix =
      normalizedNonprefixAtomApprox ⟨1, by decide⟩ := by
  exact panel1FactorChunk16

end RHP2Bridge
