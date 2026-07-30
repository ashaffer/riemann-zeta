import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk16 :
    P2RoundedFactorCheckpointData.panel27Nonprefix =
      normalizedNonprefixAtomApprox ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel27Nonprefix =
      normalizedNonprefixAtomApprox ⟨27, by decide⟩ := by
  exact panel27FactorChunk16

end RHP2Bridge
