import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk11 :
    P2RoundedFactorCheckpointData.panel13Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix44_eq :
    P2RoundedFactorCheckpointData.panel13Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk11.1

theorem panel13Prefix45_eq :
    P2RoundedFactorCheckpointData.panel13Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk11.2.1

theorem panel13Prefix46_eq :
    P2RoundedFactorCheckpointData.panel13Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk11.2.2.1

theorem panel13Prefix47_eq :
    P2RoundedFactorCheckpointData.panel13Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk11.2.2.2

end RHP2Bridge
