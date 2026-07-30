import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk12 :
    P2RoundedFactorCheckpointData.panel0Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix48_eq :
    P2RoundedFactorCheckpointData.panel0Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk12.1

theorem panel0Prefix49_eq :
    P2RoundedFactorCheckpointData.panel0Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk12.2.1

theorem panel0Prefix50_eq :
    P2RoundedFactorCheckpointData.panel0Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk12.2.2.1

theorem panel0Prefix51_eq :
    P2RoundedFactorCheckpointData.panel0Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk12.2.2.2

end RHP2Bridge
