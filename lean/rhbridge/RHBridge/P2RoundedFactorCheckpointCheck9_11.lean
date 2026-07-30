import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk11 :
    P2RoundedFactorCheckpointData.panel9Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix44_eq :
    P2RoundedFactorCheckpointData.panel9Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk11.1

theorem panel9Prefix45_eq :
    P2RoundedFactorCheckpointData.panel9Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk11.2.1

theorem panel9Prefix46_eq :
    P2RoundedFactorCheckpointData.panel9Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk11.2.2.1

theorem panel9Prefix47_eq :
    P2RoundedFactorCheckpointData.panel9Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk11.2.2.2

end RHP2Bridge
