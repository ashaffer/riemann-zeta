import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk16 :
    P2RoundedFactorCheckpointData.panel16Nonprefix =
      normalizedNonprefixAtomApprox ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Nonprefix_eq :
    P2RoundedFactorCheckpointData.panel16Nonprefix =
      normalizedNonprefixAtomApprox ⟨16, by decide⟩ := by
  exact panel16FactorChunk16

end RHP2Bridge
