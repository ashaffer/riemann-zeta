import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk5 :
    P2RoundedFactorCheckpointData.panel26Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix20_eq :
    P2RoundedFactorCheckpointData.panel26Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk5.1

theorem panel26Prefix21_eq :
    P2RoundedFactorCheckpointData.panel26Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk5.2.1

theorem panel26Prefix22_eq :
    P2RoundedFactorCheckpointData.panel26Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk5.2.2.1

theorem panel26Prefix23_eq :
    P2RoundedFactorCheckpointData.panel26Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk5.2.2.2

end RHP2Bridge
