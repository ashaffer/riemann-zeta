import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk11 :
    P2RoundedFactorCheckpointData.panel5Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix44_eq :
    P2RoundedFactorCheckpointData.panel5Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk11.1

theorem panel5Prefix45_eq :
    P2RoundedFactorCheckpointData.panel5Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk11.2.1

theorem panel5Prefix46_eq :
    P2RoundedFactorCheckpointData.panel5Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk11.2.2.1

theorem panel5Prefix47_eq :
    P2RoundedFactorCheckpointData.panel5Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk11.2.2.2

end RHP2Bridge
