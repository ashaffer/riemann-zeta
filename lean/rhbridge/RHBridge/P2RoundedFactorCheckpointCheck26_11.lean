import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk11 :
    P2RoundedFactorCheckpointData.panel26Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix44_eq :
    P2RoundedFactorCheckpointData.panel26Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk11.1

theorem panel26Prefix45_eq :
    P2RoundedFactorCheckpointData.panel26Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk11.2.1

theorem panel26Prefix46_eq :
    P2RoundedFactorCheckpointData.panel26Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk11.2.2.1

theorem panel26Prefix47_eq :
    P2RoundedFactorCheckpointData.panel26Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk11.2.2.2

end RHP2Bridge
