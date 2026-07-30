import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk12 :
    P2RoundedFactorCheckpointData.panel15Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix48_eq :
    P2RoundedFactorCheckpointData.panel15Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk12.1

theorem panel15Prefix49_eq :
    P2RoundedFactorCheckpointData.panel15Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk12.2.1

theorem panel15Prefix50_eq :
    P2RoundedFactorCheckpointData.panel15Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk12.2.2.1

theorem panel15Prefix51_eq :
    P2RoundedFactorCheckpointData.panel15Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk12.2.2.2

end RHP2Bridge
