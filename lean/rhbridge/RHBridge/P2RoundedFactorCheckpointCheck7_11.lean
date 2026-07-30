import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk11 :
    P2RoundedFactorCheckpointData.panel7Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix44_eq :
    P2RoundedFactorCheckpointData.panel7Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk11.1

theorem panel7Prefix45_eq :
    P2RoundedFactorCheckpointData.panel7Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk11.2.1

theorem panel7Prefix46_eq :
    P2RoundedFactorCheckpointData.panel7Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk11.2.2.1

theorem panel7Prefix47_eq :
    P2RoundedFactorCheckpointData.panel7Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk11.2.2.2

end RHP2Bridge
