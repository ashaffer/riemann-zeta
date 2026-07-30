import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk1 :
    P2RoundedFactorCheckpointData.panel26Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix4_eq :
    P2RoundedFactorCheckpointData.panel26Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk1.1

theorem panel26Prefix5_eq :
    P2RoundedFactorCheckpointData.panel26Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk1.2.1

theorem panel26Prefix6_eq :
    P2RoundedFactorCheckpointData.panel26Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk1.2.2.1

theorem panel26Prefix7_eq :
    P2RoundedFactorCheckpointData.panel26Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk1.2.2.2

end RHP2Bridge
