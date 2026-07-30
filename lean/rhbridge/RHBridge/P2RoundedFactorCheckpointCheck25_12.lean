import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk12 :
    P2RoundedFactorCheckpointData.panel25Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix48_eq :
    P2RoundedFactorCheckpointData.panel25Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk12.1

theorem panel25Prefix49_eq :
    P2RoundedFactorCheckpointData.panel25Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk12.2.1

theorem panel25Prefix50_eq :
    P2RoundedFactorCheckpointData.panel25Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk12.2.2.1

theorem panel25Prefix51_eq :
    P2RoundedFactorCheckpointData.panel25Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk12.2.2.2

end RHP2Bridge
