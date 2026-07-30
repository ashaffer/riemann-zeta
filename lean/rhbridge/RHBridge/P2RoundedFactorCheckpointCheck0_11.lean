import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk11 :
    P2RoundedFactorCheckpointData.panel0Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix44_eq :
    P2RoundedFactorCheckpointData.panel0Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk11.1

theorem panel0Prefix45_eq :
    P2RoundedFactorCheckpointData.panel0Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk11.2.1

theorem panel0Prefix46_eq :
    P2RoundedFactorCheckpointData.panel0Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk11.2.2.1

theorem panel0Prefix47_eq :
    P2RoundedFactorCheckpointData.panel0Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk11.2.2.2

end RHP2Bridge
