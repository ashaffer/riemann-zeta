import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk6 :
    P2RoundedFactorCheckpointData.panel26Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix24_eq :
    P2RoundedFactorCheckpointData.panel26Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk6.1

theorem panel26Prefix25_eq :
    P2RoundedFactorCheckpointData.panel26Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk6.2.1

theorem panel26Prefix26_eq :
    P2RoundedFactorCheckpointData.panel26Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk6.2.2.1

theorem panel26Prefix27_eq :
    P2RoundedFactorCheckpointData.panel26Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk6.2.2.2

end RHP2Bridge
