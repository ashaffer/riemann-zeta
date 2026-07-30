import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk3 :
    P2RoundedFactorCheckpointData.panel26Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix12_eq :
    P2RoundedFactorCheckpointData.panel26Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk3.1

theorem panel26Prefix13_eq :
    P2RoundedFactorCheckpointData.panel26Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk3.2.1

theorem panel26Prefix14_eq :
    P2RoundedFactorCheckpointData.panel26Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk3.2.2.1

theorem panel26Prefix15_eq :
    P2RoundedFactorCheckpointData.panel26Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk3.2.2.2

end RHP2Bridge
