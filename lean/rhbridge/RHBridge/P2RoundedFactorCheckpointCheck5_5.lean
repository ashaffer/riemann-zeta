import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk5 :
    P2RoundedFactorCheckpointData.panel5Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix20_eq :
    P2RoundedFactorCheckpointData.panel5Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk5.1

theorem panel5Prefix21_eq :
    P2RoundedFactorCheckpointData.panel5Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk5.2.1

theorem panel5Prefix22_eq :
    P2RoundedFactorCheckpointData.panel5Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk5.2.2.1

theorem panel5Prefix23_eq :
    P2RoundedFactorCheckpointData.panel5Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk5.2.2.2

end RHP2Bridge
