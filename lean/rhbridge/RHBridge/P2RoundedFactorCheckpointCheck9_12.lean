import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk12 :
    P2RoundedFactorCheckpointData.panel9Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix48_eq :
    P2RoundedFactorCheckpointData.panel9Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk12.1

theorem panel9Prefix49_eq :
    P2RoundedFactorCheckpointData.panel9Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk12.2.1

theorem panel9Prefix50_eq :
    P2RoundedFactorCheckpointData.panel9Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk12.2.2.1

theorem panel9Prefix51_eq :
    P2RoundedFactorCheckpointData.panel9Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk12.2.2.2

end RHP2Bridge
