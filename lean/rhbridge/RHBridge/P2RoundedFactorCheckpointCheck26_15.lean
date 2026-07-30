import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk15 :
    P2RoundedFactorCheckpointData.panel26Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix60_eq :
    P2RoundedFactorCheckpointData.panel26Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk15.1

theorem panel26Prefix61_eq :
    P2RoundedFactorCheckpointData.panel26Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk15.2.1

theorem panel26Prefix62_eq :
    P2RoundedFactorCheckpointData.panel26Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk15.2.2.1

theorem panel26Prefix63_eq :
    P2RoundedFactorCheckpointData.panel26Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk15.2.2.2

end RHP2Bridge
