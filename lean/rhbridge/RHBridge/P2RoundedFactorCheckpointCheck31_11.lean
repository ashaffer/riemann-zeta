import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk11 :
    P2RoundedFactorCheckpointData.panel31Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix44_eq :
    P2RoundedFactorCheckpointData.panel31Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk11.1

theorem panel31Prefix45_eq :
    P2RoundedFactorCheckpointData.panel31Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk11.2.1

theorem panel31Prefix46_eq :
    P2RoundedFactorCheckpointData.panel31Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk11.2.2.1

theorem panel31Prefix47_eq :
    P2RoundedFactorCheckpointData.panel31Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk11.2.2.2

end RHP2Bridge
