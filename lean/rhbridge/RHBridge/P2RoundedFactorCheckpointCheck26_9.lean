import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk9 :
    P2RoundedFactorCheckpointData.panel26Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix36_eq :
    P2RoundedFactorCheckpointData.panel26Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk9.1

theorem panel26Prefix37_eq :
    P2RoundedFactorCheckpointData.panel26Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk9.2.1

theorem panel26Prefix38_eq :
    P2RoundedFactorCheckpointData.panel26Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk9.2.2.1

theorem panel26Prefix39_eq :
    P2RoundedFactorCheckpointData.panel26Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk9.2.2.2

end RHP2Bridge
