import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk11 :
    P2RoundedFactorCheckpointData.panel3Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix44_eq :
    P2RoundedFactorCheckpointData.panel3Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk11.1

theorem panel3Prefix45_eq :
    P2RoundedFactorCheckpointData.panel3Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk11.2.1

theorem panel3Prefix46_eq :
    P2RoundedFactorCheckpointData.panel3Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk11.2.2.1

theorem panel3Prefix47_eq :
    P2RoundedFactorCheckpointData.panel3Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk11.2.2.2

end RHP2Bridge
