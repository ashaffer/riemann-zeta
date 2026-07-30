import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk12 :
    P2RoundedFactorCheckpointData.panel23Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix48_eq :
    P2RoundedFactorCheckpointData.panel23Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk12.1

theorem panel23Prefix49_eq :
    P2RoundedFactorCheckpointData.panel23Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk12.2.1

theorem panel23Prefix50_eq :
    P2RoundedFactorCheckpointData.panel23Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk12.2.2.1

theorem panel23Prefix51_eq :
    P2RoundedFactorCheckpointData.panel23Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk12.2.2.2

end RHP2Bridge
