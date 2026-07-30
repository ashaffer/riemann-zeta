import RHBridge.P2RoundedFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FactorChunk13 :
    P2RoundedFactorCheckpointData.panel26Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel26Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨26, by decide⟩ := by
  decide +kernel

theorem panel26Prefix52_eq :
    P2RoundedFactorCheckpointData.panel26Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk13.1

theorem panel26Prefix53_eq :
    P2RoundedFactorCheckpointData.panel26Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk13.2.1

theorem panel26Prefix54_eq :
    P2RoundedFactorCheckpointData.panel26Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk13.2.2.1

theorem panel26Prefix55_eq :
    P2RoundedFactorCheckpointData.panel26Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨26, by decide⟩ := by
  exact panel26FactorChunk13.2.2.2

end RHP2Bridge
