import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk4 :
    P2RoundedFactorCheckpointData.panel26Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix16_eq :
    P2RoundedFactorCheckpointData.panel26Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk4.1

theorem panel26Prefix17_eq :
    P2RoundedFactorCheckpointData.panel26Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk4.2.1

theorem panel26Prefix18_eq :
    P2RoundedFactorCheckpointData.panel26Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk4.2.2.1

theorem panel26Prefix19_eq :
    P2RoundedFactorCheckpointData.panel26Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk4.2.2.2

end RHP2Bridge
