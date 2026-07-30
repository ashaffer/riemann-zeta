import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk12 :
    P2RoundedFactorCheckpointData.panel5Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix48_eq :
    P2RoundedFactorCheckpointData.panel5Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk12.1

theorem panel5Prefix49_eq :
    P2RoundedFactorCheckpointData.panel5Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk12.2.1

theorem panel5Prefix50_eq :
    P2RoundedFactorCheckpointData.panel5Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk12.2.2.1

theorem panel5Prefix51_eq :
    P2RoundedFactorCheckpointData.panel5Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk12.2.2.2

end RHP2Bridge
