import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk12 :
    P2RoundedFactorCheckpointData.panel4Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix48_eq :
    P2RoundedFactorCheckpointData.panel4Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk12.1

theorem panel4Prefix49_eq :
    P2RoundedFactorCheckpointData.panel4Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk12.2.1

theorem panel4Prefix50_eq :
    P2RoundedFactorCheckpointData.panel4Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk12.2.2.1

theorem panel4Prefix51_eq :
    P2RoundedFactorCheckpointData.panel4Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk12.2.2.2

end RHP2Bridge
