import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk11 :
    P2RoundedFactorCheckpointData.panel12Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix44_eq :
    P2RoundedFactorCheckpointData.panel12Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk11.1

theorem panel12Prefix45_eq :
    P2RoundedFactorCheckpointData.panel12Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk11.2.1

theorem panel12Prefix46_eq :
    P2RoundedFactorCheckpointData.panel12Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk11.2.2.1

theorem panel12Prefix47_eq :
    P2RoundedFactorCheckpointData.panel12Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk11.2.2.2

end RHP2Bridge
