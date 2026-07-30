import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk11 :
    P2RoundedFactorCheckpointData.panel25Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix44_eq :
    P2RoundedFactorCheckpointData.panel25Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk11.1

theorem panel25Prefix45_eq :
    P2RoundedFactorCheckpointData.panel25Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk11.2.1

theorem panel25Prefix46_eq :
    P2RoundedFactorCheckpointData.panel25Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk11.2.2.1

theorem panel25Prefix47_eq :
    P2RoundedFactorCheckpointData.panel25Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk11.2.2.2

end RHP2Bridge
