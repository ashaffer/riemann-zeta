import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk8 :
    P2RoundedFactorCheckpointData.panel26Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix32_eq :
    P2RoundedFactorCheckpointData.panel26Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk8.1

theorem panel26Prefix33_eq :
    P2RoundedFactorCheckpointData.panel26Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk8.2.1

theorem panel26Prefix34_eq :
    P2RoundedFactorCheckpointData.panel26Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk8.2.2.1

theorem panel26Prefix35_eq :
    P2RoundedFactorCheckpointData.panel26Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk8.2.2.2

end RHP2Bridge
