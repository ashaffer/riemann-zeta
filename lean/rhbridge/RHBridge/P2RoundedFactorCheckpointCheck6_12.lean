import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk12 :
    P2RoundedFactorCheckpointData.panel6Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix48_eq :
    P2RoundedFactorCheckpointData.panel6Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk12.1

theorem panel6Prefix49_eq :
    P2RoundedFactorCheckpointData.panel6Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk12.2.1

theorem panel6Prefix50_eq :
    P2RoundedFactorCheckpointData.panel6Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk12.2.2.1

theorem panel6Prefix51_eq :
    P2RoundedFactorCheckpointData.panel6Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk12.2.2.2

end RHP2Bridge
