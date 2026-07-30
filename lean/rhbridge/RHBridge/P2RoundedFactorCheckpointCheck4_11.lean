import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk11 :
    P2RoundedFactorCheckpointData.panel4Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix44_eq :
    P2RoundedFactorCheckpointData.panel4Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk11.1

theorem panel4Prefix45_eq :
    P2RoundedFactorCheckpointData.panel4Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk11.2.1

theorem panel4Prefix46_eq :
    P2RoundedFactorCheckpointData.panel4Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk11.2.2.1

theorem panel4Prefix47_eq :
    P2RoundedFactorCheckpointData.panel4Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk11.2.2.2

end RHP2Bridge
