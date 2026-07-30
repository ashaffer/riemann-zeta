import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk10 :
    P2RoundedFactorCheckpointData.panel26Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix40_eq :
    P2RoundedFactorCheckpointData.panel26Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk10.1

theorem panel26Prefix41_eq :
    P2RoundedFactorCheckpointData.panel26Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk10.2.1

theorem panel26Prefix42_eq :
    P2RoundedFactorCheckpointData.panel26Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk10.2.2.1

theorem panel26Prefix43_eq :
    P2RoundedFactorCheckpointData.panel26Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk10.2.2.2

end RHP2Bridge
