import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk12 :
    P2RoundedFactorCheckpointData.panel7Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix48_eq :
    P2RoundedFactorCheckpointData.panel7Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk12.1

theorem panel7Prefix49_eq :
    P2RoundedFactorCheckpointData.panel7Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk12.2.1

theorem panel7Prefix50_eq :
    P2RoundedFactorCheckpointData.panel7Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk12.2.2.1

theorem panel7Prefix51_eq :
    P2RoundedFactorCheckpointData.panel7Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk12.2.2.2

end RHP2Bridge
