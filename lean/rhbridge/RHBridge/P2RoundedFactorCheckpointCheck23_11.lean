import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk11 :
    P2RoundedFactorCheckpointData.panel23Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix44_eq :
    P2RoundedFactorCheckpointData.panel23Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk11.1

theorem panel23Prefix45_eq :
    P2RoundedFactorCheckpointData.panel23Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk11.2.1

theorem panel23Prefix46_eq :
    P2RoundedFactorCheckpointData.panel23Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk11.2.2.1

theorem panel23Prefix47_eq :
    P2RoundedFactorCheckpointData.panel23Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk11.2.2.2

end RHP2Bridge
