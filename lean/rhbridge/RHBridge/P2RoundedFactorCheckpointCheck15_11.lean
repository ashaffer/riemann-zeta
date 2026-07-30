import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk11 :
    P2RoundedFactorCheckpointData.panel15Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix44_eq :
    P2RoundedFactorCheckpointData.panel15Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk11.1

theorem panel15Prefix45_eq :
    P2RoundedFactorCheckpointData.panel15Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk11.2.1

theorem panel15Prefix46_eq :
    P2RoundedFactorCheckpointData.panel15Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk11.2.2.1

theorem panel15Prefix47_eq :
    P2RoundedFactorCheckpointData.panel15Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk11.2.2.2

end RHP2Bridge
