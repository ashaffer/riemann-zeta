import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk2 :
    P2RoundedFactorCheckpointData.panel26Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix8_eq :
    P2RoundedFactorCheckpointData.panel26Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk2.1

theorem panel26Prefix9_eq :
    P2RoundedFactorCheckpointData.panel26Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk2.2.1

theorem panel26Prefix10_eq :
    P2RoundedFactorCheckpointData.panel26Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk2.2.2.1

theorem panel26Prefix11_eq :
    P2RoundedFactorCheckpointData.panel26Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk2.2.2.2

end RHP2Bridge
