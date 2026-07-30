import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk0 :
    P2RoundedFactorCheckpointData.panel26Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix0_eq :
    P2RoundedFactorCheckpointData.panel26Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk0.1

theorem panel26Prefix1_eq :
    P2RoundedFactorCheckpointData.panel26Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk0.2.1

theorem panel26Prefix2_eq :
    P2RoundedFactorCheckpointData.panel26Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk0.2.2.1

theorem panel26Prefix3_eq :
    P2RoundedFactorCheckpointData.panel26Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk0.2.2.2

end RHP2Bridge
