import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk12 :
    P2RoundedFactorCheckpointData.panel26Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix48_eq :
    P2RoundedFactorCheckpointData.panel26Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk12.1

theorem panel26Prefix49_eq :
    P2RoundedFactorCheckpointData.panel26Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk12.2.1

theorem panel26Prefix50_eq :
    P2RoundedFactorCheckpointData.panel26Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk12.2.2.1

theorem panel26Prefix51_eq :
    P2RoundedFactorCheckpointData.panel26Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk12.2.2.2

end RHP2Bridge
